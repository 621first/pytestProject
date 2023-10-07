from string import Template
import yaml
import random
from test_csv_yaml.csv_yaml.csv_to_json import FromCsvToJson
from contextlib import ExitStack
'''
该方法不会写入yaml文件，返回一个列表
'''

# 1、处理单个数据
def yaml_template1(data: dict):
    with open(r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\yamlData_2_1.yaml', encoding="utf-8") as f:
       #  f.read()读取的是yaml文件的文本格式数据（即读取出来的数据为字符串格式）
       #  这里代码的作用是将data数据替换f.read()读出来的$标识的数据---简单来说就是读取yaml文件中的数据
       #  然后替换原数据中被$符号标识的变量，得到新的数据（此时没有生成新的对象，只是改变了数据的内容）
        re = Template(f.read()).substitute(data)
        # print(re, type(re))
        # print(yaml.safe_load(stream=re), type(yaml.safe_load(stream=re)))
        # 返回字典格式的数据---反序列化
        return yaml.safe_load(stream=re)

# 2、批量处理csv文件
def yaml_template2(csvFile):
    # 批量处理csv文件数据
    data = FromCsvToJson(csvFile)
    test_case = []
    # with ExitStack() as stack:
    # yml_output = stack.enter_context(open(r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\yamlData_new_2.yaml', 'w'))
    for data_dict in data:
        with open(r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\yamlData_2_2.yaml', encoding="utf-8") as f:
        #  f.read()读取的是yaml文件的文本格式数据（即读取出来的数据为字符串格式）
        #  这里代码的作用是将data数据替换f.read()读出来的$标识的数据---简单来说就是读取yaml文件中的数据
        #  然后替换原数据中被$符号标识的变量，得到新的数据（此时没有生成新的对象，只是改变了数据的内容）
            re = Template(f.read()).substitute(data_dict)
            test_case.append(yaml.safe_load(stream=re))
            # yml_output.write(str(yaml.safe_load(stream=re)))
            # yml_output.write("\n\n")
    return test_case


if __name__ == '__main__':
    # 1、设定一个变量的随机数变量
    print(yaml_template1({'appid': str(random.randint(1000,9999))}))

    # 2、模板初始化用例
    print(yaml_template2(r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\data.csv'))