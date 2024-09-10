import pytest
from balanced_parentheses import is_valid


@pytest.mark.parametrize("s, valid", [("()", True), ("((", False), ("()[]{}", True), ("(]", False)])
def test_is_valid(s: str, valid: bool) -> None:
    assert is_valid(s) == valid
