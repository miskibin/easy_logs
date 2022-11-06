import pytest


class TestLinearModel:
    def test_set_method(self):
        a = {}
        with pytest.raises(KeyError):
            a["b"]
