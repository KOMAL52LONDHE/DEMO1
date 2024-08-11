import pytest



class Test_002:
    @pytest.mark.skip

    def test_sum_004(self):
        a=100
        b=90
        sum=(a+b)
        print("SUMMATION--->"+str(sum))
        if sum == 190:
            assert True
        else:
            assert False

    @pytest.mark.sanity
    def test_mul_005(self):
        a=9
        b=9
        mul=a*b
        print("MULTIPLICATION OF TWO NUMBER---->",(mul))
        if mul== 16:
            assert True
        else:
            assert False
    @pytest.mark.sanity
    def test_div_006(self):
        a=2
        b=4
        div=a/b
        print("DIVISION OF TWO NUMBERS---->",(div))
        if div==2:
            assert True
        else:
            assert False

    @pytest.mark.regression
    @pytest.mark.integration
    def test_sum_007(self):
        a=9
        b=7
        add=a+b
        print("Addition Of Two Number is---->",(add))
        if add == 15:
            assert  True

        else:
            assert False

