import uuid
from asyncpg import Connection


async def get_hypotheses(conn: Connection, theme_id: uuid.UUID, user_id: uuid.UUID) -> list[dict]:
    """Return all hypotheses for a theme, ordered by status priority then date."""
    rows = await conn.fetch(
        """
        SELECT h.id, h.theme_id, h.title, h.description, h.status, h.created_at, h.updated_at
        FROM hypotheses h
        JOIN themes t ON t.id = h.theme_id
        WHERE h.theme_id = $1
          AND t.user_id  = $2
        ORDER BY
            CASE h.status
                WHEN 'confirmed' THEN 1
                WHEN 'testing'   THEN 2
                WHEN 'new'       THEN 3
                WHEN 'rejected'  THEN 4
            END,
            h.created_at DESC
        """,
        theme_id,
        user_id,
    )
    return [dict(r) for r in rows]


async def get_hypothesis(
    conn: Connection, hypothesis_id: uuid.UUID, user_id: uuid.UUID
) -> dict | None:
    row = await conn.fetchrow(
        """
        SELECT h.id, h.theme_id, h.title, h.description, h.status, h.created_at, h.updated_at
        FROM hypotheses h
        JOIN themes t ON t.id = h.theme_id
        WHERE h.id = $1 AND t.user_id = $2
        """,
        hypothesis_id,
        user_id,
    )
    return dict(row) if row else None


async def create_hypothesis(
    conn: Connection,
    theme_id: uuid.UUID,
    user_id: uuid.UUID,
    title: str,
    description: str | None,
) -> dict:
    row = await conn.fetchrow(
        """
        INSERT INTO hypotheses (theme_id, user_id, title, description)
        VALUES ($1, $2, $3, $4)
        RETURNING id, theme_id, title, description, status, created_at, updated_at
        """,
        theme_id,
        user_id,
        title,
        description,
    )
    return dict(row)


async def update_hypothesis(
    conn: Connection,
    hypothesis_id: uuid.UUID,
    user_id: uuid.UUID,
    title: str | None,
    description: str | None,
    status: str | None,
) -> dict | None:
    row = await conn.fetchrow(
        """
        UPDATE hypotheses h
        SET title       = COALESCE($3, h.title),
            description = COALESCE($4, h.description),
            status      = COALESCE($5, h.status)
        FROM themes t
        WHERE h.id = $1
          AND h.theme_id = t.id
          AND t.user_id  = $2
        RETURNING h.id, h.theme_id, h.title, h.description, h.status, h.created_at, h.updated_at
        """,
        hypothesis_id,
        user_id,
        title,
        description,
        status,
    )
    return dict(row) if row else None


async def delete_hypothesis(
    conn: Connection, hypothesis_id: uuid.UUID, user_id: uuid.UUID
) -> bool:
    result = await conn.execute(
        """
        DELETE FROM hypotheses h
        USING themes t
        WHERE h.id = $1
          AND h.theme_id = t.id
          AND t.user_id  = $2
        """,
        hypothesis_id,
        user_id,
    )
    return result == "DELETE 1"
