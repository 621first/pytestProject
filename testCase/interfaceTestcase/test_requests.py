from common_util.requests_util import RequestUtil
import pytest
from common_util.yaml_util import read_yaml
from log.test_log import create_log

# 初始化创建日志对象
log = create_log('request_log')

class TestRequests():

    @pytest.mark.parametrize('paramInfo',read_yaml('./testCase/interfaceTestcase/yamlFile/inter2.yaml'))
    def test_01(self,paramInfo,classScope):

        
        name = paramInfo['name']
        method = paramInfo['request']['method']
        url = paramInfo['request']['url']
        data = paramInfo['request']['data']

        # 调用封装类发送请求
        RequestUtil.session.request(method=method,url=url,data=data)
        #
        # try:
        #     response = RequestUtil.session.request(method=method,url=url,data=data)
        #
        #     # If the response was successful, no Exception will be raised
        #     response.raise_for_status()
        # except HTTPError as http_err:
        #     print(f'HTTP error occurred: {http_err}')  # Python 3.6
        # except Exception as err:
        #     print(f'Other error occurred: {err}')  # Python 3.6
        # else:
        #     print('Success!')