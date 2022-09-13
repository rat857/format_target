# coding=utf-8
import argparse
import sys

ip = []
url = []


def logo():
    print(r'''
   /$$$$$$$$                                            /$$                 /$$$$$$$$                                        /$$    
  | $$_____/                                           | $$                |__  $$__/                                       | $$    
  | $$     /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$                 | $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  
  | $$$$$ /$$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$|_  $$_/                 | $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  
  | $$__/| $$  \ $$| $$  \__/| $$ \ $$ \ $$  /$$$$$$$  | $$                   | $$  /$$$$$$$| $$  \__/| $$  \ $$| $$$$$$$$  | $$    
  | $$   | $$  | $$| $$      | $$ | $$ | $$ /$$__  $$  | $$ /$$               | $$ /$$__  $$| $$      | $$  | $$| $$_____/  | $$ /$$
  | $$   |  $$$$$$/| $$      | $$ | $$ | $$|  $$$$$$$  |  $$$$/               | $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$  |  $$$$/
  |__/    \______/ |__/      |__/ |__/ |__/ \_______/   \___/                 |__/ \_______/|__/       \____  $$ \_______/   \___/  
                                                                                                       /$$  \ $$                    
                                                                                                      |  $$$$$$/              @rat 
                                                                                                       \______/      
use: python3 format.py -h
''')


# 传入你的混合文件 返回出列表
def for_list(txt):
    with open(txt, "r") as f:
        tlist = f.readlines()
        tlist.append(tlist[-1] + "\n")
        tlist.remove(tlist[-2])  # 给你的文件的最后一行加上“\n” 存入tlist列表
        return tlist


# 分别导出有http,https的 存入url[]，和没有的存入ip[]
def get_list(tlist):
    for i in range(0, len(tlist), 1):
        if "https://" in tlist[i] or "http://" in tlist[i]:
            url.append(tlist[i])
        else:
            ip.append(tlist[i])


# 给ip list里的字段全部加上"http://"并添加到url list里
def change(ip_list):
    for i in range(0, len(ip_list), 1):
        url.append("http://" + ip_list[i])


def mkdir(url_list, txt_name):
    with open(txt_name, "w") as f:
        f.writelines(url_list)


if __name__ == '__main__':
    logo()
    parser = argparse.ArgumentParser()  # 设置参数
    parser.add_argument('-i', nargs="+", type=str, help='into_file')  # 你的混合文件
    parser.add_argument('-o', nargs="*", type=str, default="e", help='out_file')  # 输出文件，不添加则输出为e
    opt = parser.parse_args()
    try:
        a = for_list(opt.i[0])  # 传入你的混合文件
        print("\033[1;32m已传入成功\033[0m")
    except:
        print('\033[1;31merror,请阅读用法，重试!!!\033[0m')
        sys.exit(0, )
    get_list(a)  # 区分有“https://“，“http://”和没有的
    print("\033[1;34m已分离成功\033[0m")
    change(ip)  # 将ip list里格式化，并添加到url list里
    print("\033[1;35m格式化成功\033[0m")
    mkdir(url, opt.o[0])  # 输出格式好的文件
    print("\033[1;31m已成功导出\033[0m")
