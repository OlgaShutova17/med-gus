import uuid
from asyncpg import Connection


async def get_themes(conn: Connection, user_id: uuid.UUID) -> list[dict]:
    rows = await conn.fetch(
        """
        SELECT
            t.id,
            t.title,
            t.description,
            t.status,
            t.created_at,
            t.updated_at,
            COUNT(h.id)                                             AS hypotheses_count,
            MAX(h.title) FILTER (WHERE h.status = 'confirmed')     AS confirmed_hypothesis
        FROM themes t
        LEFT JOIN hypotheses h ON h.theme_id = t.id
        WHERE t.user_id = $1
        GROUP BY t.id
        ORDER BY t.created_at DESC
        """,
        user_id,
    )
    return [dict(r) for r in rows]


async def get_theme(conn: Connection, theme_id: uuid.UUID, user_id: uuid.UUID) -> dict | None:
    row = await conn.fetchrow(
        """
        SELECT
            t.id,
            t.title,
            t.description,
            t.status,
            t.created_at,
            t.updated_at,
            COUNT(h.id)                                             AS hypotheses_count,
            MAX(h.title) FILTER (WHERE h.status = 'confirmed')     AS confirmed_hypothesis
        FROM themes t
        LEFT JOIN hypotheses h ON h.theme_id = t.id
        WHERE t.id = $1 AND t.user_id = $2
        GROUP BY t.id
        """,
        theme_id,
        user_id,
    )
    return dict(row) if row else None


async def create_theme(
    conn: Connection, user_id: uuid.UUID, title: str, description: str | None
) -> dict:
    row = await conn.fetchrow(
        """
        INSERT INTO themes (user_id, title, description)
        VALUES ($1, $2, $3)
        RETURNING id, title, description, status, created_at, updated_at
        """,
        user_id,
        title,
        description,
    )
    return {**dict(row), "hypotheses_count": 0, "confirmed_hypothesis": None}


async def update_theme(
    conn: Connection,
    theme_id: uuid.UUID,
    user_id: uuid.UUID,
    title: str | None,
    description: str | None,
    status: str | None,
) -> dict | None:
    row = await conn.fetchrow(
        """
        UPDATE themes
        SET title       = COALESCE($3, title),
            description = COALESCE($4, description),
            status      = COALESCE($5, status)
        WHERE id = $1 AND user_id = $2
        RETURNING id, title, description, status, created_at, updated_at
        """,
        theme_id,
        user_id,
        title,
        description,
        status,
    )
    if not row:
        return None
    # re-fetch with counts
    return await get_theme(conn, theme_id, user_id)


async def delete_theme(conn: Connection, theme_id: uuid.UUID, user_id: uuid.UUID) -> bool:
    result = await conn.execute(
        "DELETE FROM themes WHERE id = $1 AND user_id = $2", theme_id, user_id
    )
    return result == "DELETE 1"
