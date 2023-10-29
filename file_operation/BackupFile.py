# coding:utf-8
import os
import shutil

DEFAULT_DOWNLOAD_PATH = '默认下载文件存放位置'
BACKUP_ROOT_PATH = '备份文件存放位置'

# key为文件后缀名，value为对应的最下层文件夹名称
FILE_TYPE = {
    '.pdf': 'pdf',
    '.csv': 'csv',
    '.xls': 'xls_xlsx',
    '.xlsx': 'xls_xlsx',
    '.zip': 'zip',
    '.doc': 'doc_docx',
    '.docx': 'doc_docx',
    '.dmg': 'dmg',
    '.jpg': 'jpg_png',
    '.png': 'jpg_png',
    '.mp4': 'mp4',
    '.mp3': 'mp3'
}


# 初始化备份目录
def init_backup_dirs():
    for dir_name in set(FILE_TYPE.values()):
        dir_path = os.path.join(BACKUP_ROOT_PATH, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        else:
            continue


# 将文件移动到制定目录
def move_file_to_designated_dir(file_name):
    suffix_name = os.path.splitext(file_name)[-1]
    print(suffix_name)
    if suffix_name in FILE_TYPE.keys():
        src_file_path = os.path.join(DEFAULT_DOWNLOAD_PATH, file_name)
        dst_dir_path = os.path.join(BACKUP_ROOT_PATH, FILE_TYPE.get(suffix_name))
        print(src_file_path, dst_dir_path)
        shutil.move(src_file_path, dst_dir_path)
    else:
        print('文件类型不存在：{}', file_name)
        pass


def backup_download_files(file_path, default_path):
    if not os.path.exists(file_path):
        file_path = default_path
    for file in os.scandir(file_path):
        print(file)
        if os.path.isdir(file):
            shutil.rmtree(file)
        elif os.path.isfile(file):
            init_backup_dirs()
            move_file_to_designated_dir(file)
        else:
            pass


if __name__ == '__main__':
    source_dir = input("请输入需要进行备份的文件目录：")
    backup_download_files(source_dir, default_path=DEFAULT_DOWNLOAD_PATH)
