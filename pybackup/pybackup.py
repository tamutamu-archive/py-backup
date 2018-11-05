import os, tarfile, argparse, struct, re
from datetime import datetime


exclude_list = list()

def args_parse():
    """
    Command Argument Parse.
    """

    parser = argparse.ArgumentParser(
        prog='argparseTest',
        usage='Demonstration of argparser',
        description='description',
        epilog='end',
        add_help=True
    )

    parser.add_argument('-s', '--src', required=True, help='Backup source directory.')
    parser.add_argument('-d', '--dst', required=True, help='Backup destination directory.')
    parser.add_argument('-e', '--exclude', required=False, help='Exclude regexp pattern.', action='append')
    parser.add_argument('-r', '--retension', type=int, required=True, help='Retension policy')
    parser.add_argument('-v', '--verbose')

    return parser.parse_args()


def is_exclude(file_path):
    for exclude_pattern in exclude_list:
        if exclude_pattern.match(file_path):
            return True
    return False


def add_file_dir(root, elems, tar):
    for elm in elems:
        elm_path = os.path.join(root, elm)
        if is_exclude(elm_path):
            continue
        tar.add(elm_path, recursive = False)


def backup(args):
    src = args.src
    dst = args.dst

    if args.exclude:
        global exclude_list
        exclude_list = [re.compile(exclude) for exclude in args.exclude] 
    
    exec_datetime = datetime.now()
    exec_datetime_str = exec_datetime.strftime('%Y-%m-%d_%H.%M.%S')
    tar = tarfile.open(os.path.join(dst, f'{exec_datetime_str}.tar.gz'), 'w:gz', compresslevel = 9)

    for _root, _dirs, _files in os.walk(src):
        add_file_dir(_root, _dirs, tar)
        add_file_dir(_root, _files, tar)

    tar.close()


def rotate_backup(args):
    dst = args.dst
    retension = args.retension

    for _root, _dirs, _files in os.walk(dst):
        sort_files = sorted(_files, reverse=True)
        for _file in sort_files[retension:]:
            os.remove(os.path.join(_root,_file))


def main():
    args = args_parse()

    # backup.
    backup(args)

    # backup rotation.
    rotate_backup(args)

