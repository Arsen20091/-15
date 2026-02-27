"""Small demo for BST operations."""

from bst import BinarySearchTree


def run_demo() -> None:
    tree = BinarySearchTree()

    for key, value in [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six")]:
        tree.insert(key, value)

    print("search(6):", tree.search(6))
    print("search(9):", tree.search(9))
    print("height before delete:", tree.height())
    print("is_balanced before delete:", tree.is_balanced())

    tree.delete(3)
    print("search(3) after delete:", tree.search(3))
    print("height after delete:", tree.height())
    print("is_balanced after delete:", tree.is_balanced())


if __name__ == "__main__":
    run_demo()
