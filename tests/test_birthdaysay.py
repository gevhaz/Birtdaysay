"""File with all tests for the app."""
from birthdaysay import __version__


def test_version() -> None:
    """Test that the version can be read properly."""
    assert __version__ == "0.1.0b0"
