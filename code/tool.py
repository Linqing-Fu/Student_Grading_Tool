import sys


def parse_args():
    '''Parse arguments and excute operations according to the option.

    Returns:
        option: Option for the tool
        pattern: Pattern for the option
        filename: The csv file path
    '''

    if len(sys.argv) < 2:
        print('Error: Argument missing, check usage using \'-help\'')
        sys.exit(2)

    if sys.argv[1] in ('-help', '-h'):
        return sys.argv[1], "", ""
    else:
        if len(sys.argv) != 4:
            print('Error: Argument missing or exceeding, check usage using \'-help\'')
            sys.exit(2)

        option = sys.argv[1]
        pattern = sys.argv[2]
        filename = sys.argv[3]
        return option, pattern, filename


def read_csv(filename):
    '''Read from csv file

    Args:
        filename: Path for a csv file

    Returns:
        rows: A list of records
    '''
    rows = []
    try:
        with open(filename) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                rows.append(row)
        return rows
    except IOError:
        print('Cannot read file from %s' % filename)
        sys.exit(2)


def match_name(pattern, rows):
    """Match the name with pattern and print the matching records.

    Args:
        pattern: A string
        rows: A list of records

    Returns: None
    """


def match_email(pattern, rows):
    """Match the email with pattern and print the matching records.

    Args:
        pattern: A string
        rows: A list of records

    Returns: None

    """


def match_gpa(pattern, rows):
    """Match the gpa with pattern and print the matching records.

    Args:
        pattern: A string of a decimal, may have + or - at the end
        rows: A list of records

    Returns: None
    """


if __name__ == "__main__":
	option, pattern, filename = parse_args()

    help_info = """
        Usage: tool [-help][-name <pattern> <path>][-email <pattern> <path>][-gpa <pattern> <path>]
    """
    if option in ('-help', '-h'):
        print(help_info)
    else:
        rows = read_csv(filename)

        if option in ('-name', '-n'):
            match_name(pattern, rows)
        elif option in ('-email', '-e'):
            match_email(pattern, rows)
        elif option in ('-gpa', '-g'):
            match_gpa(pattern, rows)
        else:
            print('Unknown option: %s, check usage using \'-help\' or \'-h\'' % option)
