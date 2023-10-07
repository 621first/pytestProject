import pytest

def read_yaml():
    return ['ficture传参']

@pytest.fixture(scope='function',autouse=False,params=read_yaml())
def test_fixture(request):
    print('测试前')
    yield request.param
    print('测试后')



class Test_01:
    # 配置文件：-k='smoke'：执行smoke组的用例
    # @pytestProject.mark.smoke
    def atest_01(self,test_fixture):
        print(test_fixture)
        print('测试111')

    @pytest.mark.skip(reason='无理由跳过')
    def atest_02(self):
        print('测试222')

    age = 19
    @pytest.mark.skipif(age>18,reason='有理由跳过')
    def atest_03(self):
        print('测试333')

    def atest_04(self):
        print('测试444')







