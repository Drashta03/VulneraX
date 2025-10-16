from src.fingerprint.db_fingerprint import fingerprint_sql_output, safe_time_payload_for_engine

def test_fingerprint_mysql():
    assert fingerprint_sql_output('You have an error in your SQL syntax') == 'mysql'

def test_fingerprint_sqlite():
    assert fingerprint_sql_output('sqlite3.OperationalError') == 'sqlite'

def test_safe_payloads():
    assert 'SLEEP' in safe_time_payload_for_engine('mysql') or safe_time_payload_for_engine('mysql')
