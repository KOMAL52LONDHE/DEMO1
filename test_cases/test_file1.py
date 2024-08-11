import pytest


class Test001:
    @pytest.mark.smoke
    def test_sum_001(self):
        a=10
        b=20
        sum=a+b
        print("sum of two number--->" + str(sum))
        if sum == 30:
            assert True
        else:
            assert False
    @pytest.mark.skip
    @pytest.mark.sanity
    def test_mul_002(self):
        a=2
        b=3
        mul=a*b
        print("MUl of two Numer--->" + str(mul))
        if mul ==7:
            assert True
        else:
            assert False
    @pytest.mark.sanity
    def test_sub_003(self):
        a=10
        b=5
        sub=a-b
        print("SUBSTRACTION--->" + str(sub))
        if sub == 5:
            assert True
        else:
            assert False



