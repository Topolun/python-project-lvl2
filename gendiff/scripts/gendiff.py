import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format', type=str, help='set format of output')
parser.add_argument('first_file', type=str, help='first file for check')
parser.add_argument('second_file', type=str, help='second file for check')
args = parser.parse_args()

def main():
    return print('srart ok')


if __name__ == '__main__':
    main()
