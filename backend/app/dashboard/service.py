import uuid
from asyncpg import Connection


async def get_dashboard(conn: Connection, user_id: uuid.UUID) -> dict:
    """
    Returns aggregated dashboard data:
    - themes: list with status, hypothesis counts, last event info
    - stats: totals across all themes
    """

    themes_rows = await conn.fetch(
        """
        SELECT
            t.id,
            t.title,
            t.description,
            t.status,
            t.created_at,
            t.updated_at,
            COUNT(DISTINCT h.id)                                            AS hypotheses_count,
            COUNT(DISTINCT h.id) FILTER (WHERE h.status = 'confirmed')     AS confirmed_count,
            COUNT(DISTINCT h.id) FILTER (WHERE h.status = 'testing')       AS testing_count,
            MAX(h.title) FILTER (WHERE h.status = 'confirmed')             AS confirmed_hypothesis,
            MAX(h.title) FILTER (
                WHERE h.status = 'testing'
                  AND h.status != 'confirmed'
            )                                                               AS testing_hypothesis
        FROM themes t
        LEFT JOIN hypotheses h ON h.theme_id = t.id
        WHERE t.user_id = $1
        GROUP BY t.id
        ORDER BY t.created_at DESC
        """,
        user_id,
    )

    themes = []
    for r in themes_rows:
        row = dict(r)
        # leading hypothesis: confirmed > testing > None
        row["leading_hypothesis"] = row.pop("confirmed_hypothesis") or row.pop("testing_hypothesis")
        themes.append(row)
        if "testing_hypothesis" in row:
            del row["testing_hypothesis"]

    stats_row = await conn.fetchrow(
        """
        SELECT
            COUNT(*)                                    AS total_themes,
            COUNT(*) FILTER (WHERE status = 'active')  AS active_themes,
            COUNT(*) FILTER (WHERE status = 'resolved')AS resolved_themes
        FROM themes
        WHERE user_id = $1
        """,
        user_id,
    )

    hypotheses_row = await conn.fetchrow(
        """
        SELECT
            COUNT(*)                                              AS total_hypotheses,
            COUNT(*) FILTER (WHERE h.status = 'confirmed')       AS confirmed_hypotheses,
            COUNT(*) FILTER (WHERE h.status = 'testing')         AS testing_hypotheses
        FROM hypotheses h
        JOIN themes t ON t.id = h.theme_id
        WHERE t.user_id = $1
        """,
        user_id,
    )

    return {
        "themes": themes,
        "stats": {
            **dict(stats_row),
            **dict(hypotheses_row),
        },
    }
