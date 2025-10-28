import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'test_data')
print(DATA_PATH)

HOST = 'http://117.72.115.136:8003'

# 变量定义形式 ${}
PATTEN = '\$\{(.*?)\}'