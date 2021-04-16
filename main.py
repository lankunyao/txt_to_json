# -*- coding: utf-8 -*-

import argparse
import os
import json
from pathlib import Path

parser = argparse.ArgumentParser(description="命令行传入参数")
parser.add_argument('-t', '--txt', default="SciKG_min_1.0")
args = parser.parse_args()
txt = args.txt
root_dir = os.path.dirname(__file__)


def main():
    path = os.path.normcase(os.path.join(root_dir, "txt", txt))
    print(path)
    for root, dirs, files in os.walk(path):
        for name in files:
            file_dir = os.path.join(path, name)
            f = open(file_dir, 'r', encoding='utf-8')
            data = f.read().encode('utf-8')
            data_dict = json.loads(data)
            data_json = json.dumps(data_dict, ensure_ascii=False)
            json_path = os.path.normcase(os.path.join(root_dir, "json", txt))
            if not Path(json_path).is_dir():
                os.mkdir(json_path)
            json_path = os.path.normcase(os.path.join(json_path, name[:-3]+"json"))
            w = open(json_path, 'wb')
            w.write(data_json.encode('utf-8'))
            w.close()
            f.close()


if __name__ == '__main__':
    main()
