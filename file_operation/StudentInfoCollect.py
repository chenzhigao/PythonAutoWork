# coding:utf-8
import os
import shutil


def make_student_dirs(student_file_dict, dst_dir):
    for dir_name in student_file_dict.keys():
        dir_path = os.path.join(dst_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        else:
            continue


def move_files_to_dirs(student_file_dict, dst_dir):
    for key, value in student_file_dict.items():
        for file in value:
            shutil.copy(file, os.path.join(dst_dir, key))


def student_info_collect(src_dir, dst_dir):
    student_file_dict = dict()
    for file in os.scandir(src_dir):
        if os.path.isfile(file):
            file_name = os.path.basename(file)
            print(file_name)
            info_list = []
            if file_name:
                info_list = file_name.split("_")
                if len(info_list) < 2:
                    continue
                else:
                    dir_name = info_list[0] + '_' + info_list[1]
                    if dir_name in student_file_dict.keys():
                        student_file_dict[dir_name].append(file)
                    else:
                        student_file_dict[dir_name] = [file]

    make_student_dirs(student_file_dict, dst_dir)
    move_files_to_dirs(student_file_dict, dst_dir)
    print(student_file_dict)


if __name__ == '__main__':
    src_dir = input("请输入源文件所在目录：")
    dst_dir = input("请输入目标文件所在目录：")
    student_info_collect(src_dir, dst_dir)
    student_info_collect("a", "b")
