from gendiff.engine import generate_diff
from gendiff import parsers


def main():
    args = parsers.cli()
    print(
        generate_diff(
            args.first_file, args.second_file, args.format
            )
        )


if __name__ == '__main__':
    main()
