import argparse
from gendiff import generate_diff


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format', type=str, help='set format of output')
parser.add_argument('first_file', type=str, help='first file for check')
parser.add_argument('second_file', type=str, help='second file for check')
args = parser.parse_args()


def main():
    print(generate_diff.recieve_json(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
