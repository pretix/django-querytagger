from .tagging import current_tag


def wrapper(execute, sql, params, many, context):
    tag = current_tag.get()
    if tag:
        if "*" in tag:
            # Everything else should be safe, as comments can contain anything but */
            # https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-COMMENTS
            raise ValueError("Tags are not allowed to contain * for security reasons")
        # Insert tag after first word (e.g. after SELECT) to keep query types highly visible
        if " " in sql:
            verb, remainder = sql.split(" ", 1)
        else:
            verb = sql
            remainder = ""
        sql = f"{verb} /* {tag} */ {remainder}"
    return execute(sql, params, many, context)
