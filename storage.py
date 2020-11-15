import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()

parser.add_argument("--key", type=str, help="KEY")
parser.add_argument("--val", type=str, help="VALUE")

args = parser.parse_args()

key = str(args.key)
val = str(args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
check_file_exist = os.path.exists(storage_path)

main_dict = {}

def read_file_import_main_dict():
    with open(storage_path, 'r') as f:
        data_from_file = f.readline()
        d = json.loads(data_from_file)
        return d


# d - dict, k - key, v - value

def add_new_pare_in_main_dict(d, k, v):
    new_value = [v]
    if k in d:
        old_value = list(d[k])
        d[k] = old_value + new_value
    else:
        d[k] = new_value
    return main_dict


def get_items_from_dict(d, k):
    if k in d:
        item = d.get(k)
        return ', '.join(item)
    else:
        return None


def write_new_data_in_file(data):
    export_to_json = json.dumps(data)
    with open(storage_path, 'w') as f:
        f.write(export_to_json)


if args.key and args.val:
    if check_file_exist and os.path.getsize(storage_path) != 0:
        main_dict = read_file_import_main_dict()
        new_data = add_new_pare_in_main_dict(main_dict, key, val)
        write_new_data_in_file(new_data)
    else:
        new_data = {args.key: [args.val]}
        write_new_data_in_file(new_data)
if args.key and args.val is None:
    if not check_file_exist:
        os.mknod(storage_path)
        print("None")
    elif os.path.getsize(storage_path) == 0:
        print("None")
    else:
        main_dict = read_file_import_main_dict()
        items = get_items_from_dict(main_dict, key)
        print(items)
