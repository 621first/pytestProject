from string import Template
import yaml
import random

def yaml_template(data=None):
    with open("./yaml_data.yaml", encoding="utf-8") as f:
       #  f.read()读取的是yaml文件的文本格式数据（即读取出来的数据为字符串格式）
       #  这里代码的作用是将data数据替换f.read()读出来的$标识的数据---简单来说就是读取yaml文件中的数据
       #  然后替换原数据中被$符号标识的变量，得到新的数据（此时没有生成新的对象，只是改变了数据的内容）
        re = Template(f.read()).substitute(data)
        # print(re, type(re))
        # print(yaml.safe_load(stream=re), type(yaml.safe_load(stream=re)))
        # 返回字典格式的数据---反序列化
        return yaml.safe_load(stream=re)

if __name__ == '__main__':
    print(yaml_template({'get_username_random': str(random.randint(1000,9999))}))


