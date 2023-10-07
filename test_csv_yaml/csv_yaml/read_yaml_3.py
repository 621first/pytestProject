import random
from contextlib import ExitStack
from test_csv_yaml.csv_yaml.csv_to_json import FromCsvToJson
from common_util.yaml_util import read_yaml

'''外部函数'''
def get_appid():
    return random.randint(100000,999999)
def get_token():
    return read_yaml(r'\test_csv_yaml\csv_yaml\token_1.yaml')['token']



'''
    实现将模板用例全部数据替换：
    csv测试用例数据，以及需要调用的动态函数
    函数命名规则(get开头，并且模板中必须$get的形式)
'''
def EnvReplaceYaml(yaml_file, new_yaml_file):
    try:
        with ExitStack() as stack:
            yml_file = stack.enter_context(open(yaml_file, 'r+'))
            yml_output = stack.enter_context(open(new_yaml_file, 'w'))
            # 先读取YAML模板文件，返回值为字符串列表
            yml_file_lines = yml_file.readlines()
            # profileList的长度即为测试用例的数量
            profileList = FromCsvToJson(r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\data.csv')
            for i in range(0, len(profileList)):
                # 循环遍历列表
                for line in yml_file_lines:
                    new_line = line
                    replacement = ""

                    # 如果找到以“$csv{”开头的字符串
                    if new_line.find('$csv{') > 0:
                        # 找到需要替换的变量明程
                        env_list = new_line.split(':')
                        env_name = env_list[1].strip().split('{', 1)[1].split('}')[0]
                        # 如果name在字典列表的key里
                        if env_name in profileList[i].keys():
                            # 取出name对应的值赋给replacement
                            replacement = profileList[i][env_name]
                            # 用replacement替换掉YAML模板中的“$csv{name}”
                            # for j in range(0, len(profileList)):
                            #     print(j,replacement)
                            new_line = new_line.replace(env_list[1].strip(), replacement)
##############################          调用外部函数      ########################
                    elif new_line.find('$get') > 0:
                        # 找到需要替换的变量明程
                        env_list = new_line.split(':')
                        env_name = env_list[1].strip().split('{', 1)[1].split('}')[0]
                        replacement = str(eval(env_name)())
                        new_line = new_line.replace(env_list[1].strip(), replacement)
                    # 将new_line写入到yml_output文件里
                    yml_output.write(new_line)
                yml_output.write("\n\n")    #没写完一行换行
    except IOError as e:
        print("Error: " + format(str(e)))
        raise

if __name__ == '__main__':
    EnvReplaceYaml(r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\yamlData_3.yaml', r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\yamlData_new_3.yaml')