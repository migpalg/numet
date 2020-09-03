import unittest
import numet as nm


class IterationsTestCase(unittest.TestCase):
    def test_bisection_method(self):
        f = lambda x: x ** 2 - 4
        f_root = 2
        rang = (1, 3)
        f_find_root, err = nm.bisection_method(f, *rang)

        self.assertEqual(f(f_root), 0)
        self.assertEqual(f_find_root, f_root)


if __name__ == '__main__':
    unittest.main()
