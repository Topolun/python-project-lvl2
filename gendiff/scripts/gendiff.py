from gendiff.engine import generate_diff
from gendiff import cli


def main():
    args = cli.get_args()
    print(
        generate_diff(
            args.first_file, args.second_file, args.format
            )
        )


if __name__ == '__main__':
    main()
