def parse_args():
    '''Parse arguments.

    Returns:
        option: Option for the tool
        pattern: Pattern for the option
        filename: The csv file path
    '''

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
    rows = read_csv(filename)

    if option in ('-name', '-n'):
        match_name(pattern, rows)
    elif option in ('-email', '-e'):
        match_email(pattern, rows)
    elif option in ('-gpa', '-g'):
        match_gpa(pattern, rows)
    elif option in ('-help', '-h'):
        print("""
        Usage: tool [-help][-name <pattern> <path>][-email <pattern> <path>][-gpa <pattern> <path>]
        """)
    else:
        print('Unknown option: %s, check usage using \'-help\' or \'-h\'' % option)
