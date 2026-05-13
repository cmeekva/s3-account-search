import pytest
from s3_account_search.cli import get_policy


def test_list_input():
    actual = get_policy("1")
    assert actual.get("Statement")[0].get("Condition").get("StringLike").get("s3:ResourceAccount") == ["1*"]

