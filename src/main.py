"""Script to create documentation in markdown"""
import sys
import doc_tree
import doc_write


def main():
    """Main entry point for the script."""

    root_path = "../tests"
    doc_path = root_path + "/docs"

    tree = doc_tree.create_json(root_path)

    doc_tree.build(tree, doc_path)

    for file in tree:
        name = file.split("/")[-1]
        root_file = open("{0}{1}.py".format(root_path, file), "r")
        doc_file = open("{0}{1}.md".format(doc_path, file), "a")

        #doc_write.intro(name, doc_file)
        doc_write.modules(name, doc_file, root_file)


if __name__ == '__main__':
    sys.exit(main())
