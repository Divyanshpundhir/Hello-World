from configparser import ConfigParser
parser = ConfigParser()
path = "test1.config"
parser.read(path)
num = parser.get('test1', 'num')
my_list = [print("Hello World") for i in range(int(num))]
