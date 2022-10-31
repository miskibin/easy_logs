from miskibin.ml import LinearModel
import pytest


class TestLinearModel:
    def test_set_method(self):
        with pytest.raises(ValueError):
            LinearModel("not implemented method")
