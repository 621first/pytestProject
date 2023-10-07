import os
import yaml

def get_obj_path():

    return os.path.dirname(__file__).split('common')[0]


# 读取yaml文件1：适用于读取测试用例的数据
def read_yaml(yamlPath):
    with open(get_obj_path()+yamlPath,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
    return value

# 读取yaml文件2：适用于读取零食存入的数据交互数据
def read_yaml1(yamlPath,key):
    with open(get_obj_path()+yamlPath,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
    return value[key]

# 写入yaml文件:某些需要数据关联的接口，可以吧数据零时写入yaml文件，不需要设置全局变量
def writ_yaml(data):
    # 使用mode=a，追加的方式，在每次使用之前调用清空的函数，伤处掉上一次的数据
    with open(get_obj_path()+yamlPath,mode='a',encoding='utf-8') as f:
        value = yaml.dump(data=data,stream=f,allow_unicode=True)
    return value

# 清除yaml：接口关联的数据每次运行完后清除
def clear_yaml():
    with open(get_obj_path()+yamlPath,mode='w',encoding='utf-8') as f:
        f.truncate()

if __name__ == '__main__':
    print(read_yaml('./testCase/interfaceTestcase/yamlFile/inter1.yaml'))
    print(get_obj_path())
