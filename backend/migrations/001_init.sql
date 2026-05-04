-- МедДневник — MVP schema
-- Run once on fresh database

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ─────────────────────────────────────────
-- USERS
-- ─────────────────────────────────────────

CREATE TABLE IF NOT EXISTS users (
    id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    email         TEXT        UNIQUE NOT NULL,
    password_hash TEXT        NOT NULL,
    name          TEXT,
    gender        TEXT        CHECK (gender IN ('male', 'female', 'other')),
    birth_date    DATE,
    created_at    TIMESTAMPTZ DEFAULT NOW(),
    updated_at    TIMESTAMPTZ DEFAULT NOW()
);

-- ─────────────────────────────────────────
-- THEMES (проблемы пользователя)
-- ─────────────────────────────────────────

CREATE TABLE IF NOT EXISTS themes (
    id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title       TEXT        NOT NULL,
    description TEXT,
    status      TEXT        NOT NULL DEFAULT 'active'
                            CHECK (status IN ('active', 'resolved', 'archived')),
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_themes_user_id    ON themes(user_id);
CREATE INDEX IF NOT EXISTS idx_themes_status     ON themes(user_id, status);
CREATE INDEX IF NOT EXISTS idx_themes_created_at ON themes(user_id, created_at DESC);

-- ─────────────────────────────────────────
-- HYPOTHESES (гипотезы причин)
-- ─────────────────────────────────────────

CREATE TABLE IF NOT EXISTS hypotheses (
    id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id    UUID        NOT NULL REFERENCES themes(id) ON DELETE CASCADE,
    user_id     UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title       TEXT        NOT NULL,
    description TEXT,
    status      TEXT        NOT NULL DEFAULT 'new'
                            CHECK (status IN ('new', 'testing', 'confirmed', 'rejected')),
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_hypotheses_theme_id ON hypotheses(theme_id);
CREATE INDEX IF NOT EXISTS idx_hypotheses_user_id  ON hypotheses(user_id);
CREATE INDEX IF NOT EXISTS idx_hypotheses_status   ON hypotheses(theme_id, status);

-- ─────────────────────────────────────────
-- SYMPTOMS (для будущего использования в mobile MVP)
-- ─────────────────────────────────────────

CREATE TABLE IF NOT EXISTS symptoms (
    id          UUID  PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT  NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS theme_symptoms (
    id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id   UUID        NOT NULL REFERENCES themes(id) ON DELETE CASCADE,
    symptom_id UUID        REFERENCES symptoms(id),
    name       TEXT,       -- если symptom_id = NULL, хранится свободный текст
    severity   INT         CHECK (severity BETWEEN 1 AND 10),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_theme_symptoms_theme ON theme_symptoms(theme_id);

-- ─────────────────────────────────────────
-- AUTO-UPDATE updated_at
-- ─────────────────────────────────────────

CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_updated_at     BEFORE UPDATE ON users     FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER themes_updated_at    BEFORE UPDATE ON themes    FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER hypotheses_updated_at BEFORE UPDATE ON hypotheses FOR EACH ROW EXECUTE FUNCTION update_updated_at();
