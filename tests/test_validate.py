import unittest

from password.validate import validate


class TestPasswordValidator(unittest.TestCase):
    def test_validate_fail_no_args(self):
        password = validate('123')
        self.assertFalse(password)

    def test_validate_pass_no_args(self):
        password = validate('abc123A!')
        self.assertTrue(password)

    def test_validate_fail_with_uppercase(self):
        password = validate('123asdasdaSS', uppercase=3)
        self.assertFalse(password)

    def test_validate_pass_with_uppercase(self):
        password = validate('abcasAdEE', uppercase=3)
        self.assertTrue(password)

    def test_validate_fail_with_length(self):
        password = validate('123', length=5)
        self.assertFalse(password)

    def test_validate_pass_with_length(self):
        password = validate('abAEE', length=5)
        self.assertTrue(password)

    def test_validate_fail_with_lowercase(self):
        password = validate('123ASDFG', lowercase=1)
        self.assertFalse(password)

    def test_validate_pass_with_lowercase(self):
        password = validate('abAEEasd', lowercase=5)
        self.assertTrue(password)

    def test_validate_fail_with_numbers(self):
        password = validate('1aaaaASDFG', numbers=2)
        self.assertFalse(password)

    def test_validate_pass_with_numbers(self):
        password = validate('1abA365a1sd', numbers=5)
        self.assertTrue(password)

    def test_validate_fail_with_symbols(self):
        password = validate('1!aaaaASDFG', symbols=2)
        self.assertFalse(password)

    def test_validate_pass_with_numbers(self):
        password = validate('1a!bA36-5a1sd', numbers=2)
        self.assertTrue(password)

    def test_validate_pass_with_everything(self):
        password = validate('1a!bA-5aQ1sd', lowercase=3, uppercase=2, numbers=2, symbols=2, length=12)
        self.assertTrue(password)


if __name__ == "__main__":
    unittest.main()
