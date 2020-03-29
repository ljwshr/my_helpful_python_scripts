# -*- coding=utf-8 -*-
import os

allpath = []
allname = []


def getallfile(path):
    allfilelist = os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(file)
    return allpath, allname


def find_specific_files(files_list:list, specific_extension:str):
    file_list = []
    for file_path in files_list:
        if file_path.endswith(specific_extension):
            file_list.append(file_path)
            
    return file_list


def rm_files(files_list:list):
    for file in files_list:
        print("this file is removing... " + file)
        os.remove(file)


if __name__ == '__main__':
    folder_path = r"F:/BigDataFiles"
    specific_extension = r".itcast"
    path_list, file_list = getallfile(folder_path)
    result_list = find_specific_files(path_list, specific_extension)
    print(result_list)
    rm_files(result_list)

