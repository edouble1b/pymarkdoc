import os


def create_json(path: str) -> list:
    """Creates the documentation tree structure in json form.

    Args:
        path (str): The path of the root directory
    """

    doc_tree = []

    for subdir, dirs, files in os.walk(path):
        for file in files:
            # Only reads py files
            if ".py" not in file:
                continue
            if ".pyc" in file:
                continue

            # Removes init files
            if file[:2] == "__" and file[-5:] == "__.py":
                continue

            # Opens file and checks for docstring at the beginning
            f = open(os.path.join(subdir, file))
            data = ""
            for line in f:
                if line in ["\n", " ", "\t"]:
                    continue
                else:
                    data = line
                    break

            if '"""' not in data:
                f.close()
                continue
            f.close()

            doc_tree.append(os.path.join(subdir, file).replace(path, ""))

    return doc_tree


def build(doc_tree: list):
    """Builds the documentation tree in the /doc directory where ran

    Args:
        doc_tree (list): The list used to create the doc structure
    """
    pass