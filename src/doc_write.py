import re


def intro(name: str, file: open) -> None:
    """Creates the into

    Args:
        name (str): Name of the script
        file (open): The script open object
    """

    file.write("# {0}\n\n###### Documentation for {0}".format(name))


def modules(name: str, file: open, script: open) -> None:
    """Creates the imported module section

    Args:
        name (str): Name of the script
        file (open): The script open object
    """

    print(re.findall(r'(from [\w+\.]+)?(\s+)?import \w+', script.read()))
