import unittest

from password.generate import generate


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_without_options(self):
        password = generate(8)
        self.assertRegex(password, r'^[a-z]{8}$')

    def test_generate_with_uppercase(self):
        password = generate(8, include_uppercase=True)
        self.assertRegex(password, r'^(?=.*[a-z]*)(?=.*[A-Z])[A-Za-z]{8}$')

    def test_generate_with_numbers(self):
        password = generate(8, include_numbers=True)
        self.assertRegex(password, r'^(?=.*[a-z]*)(?=.*\d)[a-z\d]{8}$')

    def test_generate_with_symbols(self):
        password = generate(8, include_symbols=True)
        self.assertRegex(password, r'^(?=.*[a-z]*)(?=.*[_@.!\-])[a-z\-_@.!]{8}$')

    def test_generate_with_everything(self):
        password = generate(
            25,
            include_uppercase=True,
            include_numbers=True,
            include_symbols=True
        )
        self.assertRegex(password, r'^(?=.*[a-z]*)(?=.*[A-Z])(?=.*\d)(?=.*[-_@.!])[A-Za-z\d\-_@.!]{25}$')

    def test_generate_with_length_lower_than_args(self):
        with self.assertRaises(RuntimeError):
            generate(
                2,
                include_uppercase=True,
                include_numbers=True,
                include_symbols=True
            )

    def test_generate_with_0_length(self):
        password = generate(0)
        self.assertEqual(password, '')


if __name__ == "__main__":
    unittest.main()
