import unittest

from bst import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def make_tree(self) -> BinarySearchTree:
        tree = BinarySearchTree()
        for key, value in [
            (8, "eight"),
            (3, "three"),
            (10, "ten"),
            (1, "one"),
            (6, "six"),
            (14, "fourteen"),
            (4, "four"),
            (7, "seven"),
            (13, "thirteen"),
        ]:
            tree.insert(key, value)
        return tree

    def test_insert_and_search(self) -> None:
        tree = BinarySearchTree()
        tree.insert(5, "five")
        tree.insert(2, "two")
        tree.insert(9, "nine")

        self.assertEqual(tree.search(5), "five")
        self.assertEqual(tree.search(2), "two")
        self.assertEqual(tree.search(9), "nine")
        self.assertIsNone(tree.search(100))

    def test_insert_updates_existing_key(self) -> None:
        tree = BinarySearchTree()
        tree.insert(5, "five")
        tree.insert(5, "FIVE")
        self.assertEqual(tree.search(5), "FIVE")

    def test_delete_leaf(self) -> None:
        tree = self.make_tree()
        tree.delete(4)
        self.assertIsNone(tree.search(4))
        self.assertEqual(tree.search(6), "six")

    def test_delete_node_with_one_child(self) -> None:
        tree = self.make_tree()
        tree.delete(14)
        self.assertIsNone(tree.search(14))
        self.assertEqual(tree.search(13), "thirteen")

    def test_delete_node_with_two_children(self) -> None:
        tree = self.make_tree()
        tree.delete(3)
        self.assertIsNone(tree.search(3))
        self.assertEqual(tree.search(1), "one")
        self.assertEqual(tree.search(6), "six")
        self.assertEqual(tree.search(4), "four")
        self.assertEqual(tree.search(7), "seven")

    def test_height(self) -> None:
        tree = BinarySearchTree()
        self.assertEqual(tree.height(), 0)
        tree.insert(1, "one")
        self.assertEqual(tree.height(), 1)
        tree.insert(2, "two")
        tree.insert(3, "three")
        self.assertEqual(tree.height(), 3)

    def test_is_balanced(self) -> None:
        balanced_tree = BinarySearchTree()
        for key in [4, 2, 6, 1, 3, 5, 7]:
            balanced_tree.insert(key, str(key))
        self.assertTrue(balanced_tree.is_balanced())

        unbalanced_tree = BinarySearchTree()
        for key in [1, 2, 3, 4]:
            unbalanced_tree.insert(key, str(key))
        self.assertFalse(unbalanced_tree.is_balanced())


if __name__ == "__main__":
    unittest.main()
