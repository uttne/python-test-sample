import sample.math as t
import pytest


class test__add:
    def test__success(self):
        """sample.math.Math.add が正常に実行できることを確認
        """
        target = t.Math()

        x = 1
        y = 2
        actual = target.add(x=x, y=y)

        assert actual == 3

    def test__failed(self):
        """sample.math.Math.add で例外が発生することを確認する
        """
        target = t.Math()

        x = "aa"
        y = 2

        with pytest.raises(TypeError):
            target.add(x=x, y=y)
