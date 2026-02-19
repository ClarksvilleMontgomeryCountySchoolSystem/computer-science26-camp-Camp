from unittest.mock import patch
import sys


# =============================================================================
# TASK 1 TESTS: Camp Registration Input/Output
# =============================================================================

def test_task1_sample1(capsys):
    """Test task1 with Alice Johnson sample data"""
    with patch('builtins.input', side_effect=[
        'Alice',
        'Johnson',
        '2012',
        '5',
        'Robert',
        'Johnson',
        '615-555-1234',
        '123 Main Street',
        'Clarksville',
        'TN',
        '37040'
    ]):
        if 'task1' in sys.modules:
            del sys.modules['task1']
        import task1
        task1.main()

    captured = capsys.readouterr().out
    assert "Camper's Name: Alice Johnson" in captured
    assert "Birth Year: 2012" in captured
    assert "Camp Duration: 5 days" in captured
    assert "Parent's Name: Robert Johnson" in captured
    assert "Phone Number: 615-555-1234" in captured
    assert "123 Main Street" in captured
    assert "Clarksville, TN 37040" in captured


def test_task1_sample2(capsys):
    """Test task1 with Marcus Williams sample data"""
    with patch('builtins.input', side_effect=[
        'Marcus',
        'Williams',
        '2015',
        '3',
        'Keisha',
        'Williams',
        '931-555-9876',
        '456 Oak Avenue',
        'Nashville',
        'TN',
        '37201'
    ]):
        if 'task1' in sys.modules:
            del sys.modules['task1']
        import task1
        task1.main()

    captured = capsys.readouterr().out
    assert "Camper's Name: Marcus Williams" in captured
    assert "Birth Year: 2015" in captured
    assert "Camp Duration: 3 days" in captured
    assert "Parent's Name: Keisha Williams" in captured
    assert "Phone Number: 931-555-9876" in captured
    assert "456 Oak Avenue" in captured
    assert "Nashville, TN 37201" in captured


# =============================================================================
# TASK 2 TESTS: Type Conversion
# =============================================================================

def test_task2_birth_is_int():
    """birth should be converted to int"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.birth, int), "birth should be an int"


def test_task2_days_is_int():
    """days should be converted to int"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.days, int), "days should be an int"


def test_task2_first_is_str():
    """first should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.first, str), "first should be a str"


def test_task2_last_is_str():
    """last should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.last, str), "last should be a str"


def test_task2_p_first_is_str():
    """p_first should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.p_first, str), "p_first should be a str"


def test_task2_p_last_is_str():
    """p_last should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.p_last, str), "p_last should be a str"


def test_task2_phone_is_str():
    """phone should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.phone, str), "phone should be a str"


def test_task2_street_is_str():
    """street should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.street, str), "street should be a str"


def test_task2_city_is_str():
    """city should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.city, str), "city should be a str"


def test_task2_state_is_str():
    """state should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.state, str), "state should be a str"


def test_task2_zip_code_is_str():
    """zip_code should remain a str"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    if 'data' in sys.modules:
        del sys.modules['data']
    import task2
    assert isinstance(task2.zip_code, str), "zip_code should be a str"