import json

from common_util.requests_util import RequestUtil
import pytest
from common_util.yaml_util import read_yaml
from log.test_log import create_log

# 初始化创建日志对象
log = create_log('requestUtil_log')

class TestRequestUtil():

    # parametrize装饰器传参
    @pytest.mark.parametrize('paramInfo',read_yaml('./testCase/interfaceTestcase/yamlFile/inter1.yaml'))
    def test_01(self,paramInfo,classScope):
        '''
        描述信息
        '''
        # classScope：是conftest中设置的fixture
        # 获取yaml文件的参数
        name = paramInfo['name']
        method = paramInfo['request']['method']
        url = paramInfo['request']['url']
        data = paramInfo['request']['data']

        # 打印日志
        log.info('接口功能：' + name)
        log.info('接口地址：' + url)
        log.info('请求方式：' + method)
        log.info('接口入参：' + str(data))

        # 调用封装类发送请求
        res = RequestUtil.session.request(method=method,url=url,data=data)
        # json.loads(res.text)    #将str->dict

        # 断言
        acture_val = 1  # 实际结果
        if paramInfo['validate'] != None:   # 如果设置了断言
            for keys,values in paramInfo['validate'].items():   # 遍历断言
                # python3.7中的dict.values()不再是list，索要类型转换
                except_val = list(values.values())[0]   # 获取预期结果
                try:
                    assert except_val == acture_val, '断言结果：预期结果：%s,实际结果：%s' % (except_val, acture_val)
                    log.info('断言结果：预期结果：%s,实际结果：%s' % (except_val, acture_val))
                except AssertionError as e:
                    log.error('断言结果：'+ str(e))

