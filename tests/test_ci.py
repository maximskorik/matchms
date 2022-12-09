from matchms.ci_script import placeholder_function, trigger_ci


def test_placeholder_function():
    """Test placeholder_function."""
    assert placeholder_function() is not None


def test_trigger_ci():
    """Test trigger_ci."""
    assert trigger_ci() is not None
