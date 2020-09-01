import hashlib
import unittest

from unittest.mock import patch, MagicMock

from password.pwn_check import request_api_data, get_password_leaks_count, pwned_api_check


class TestPwnCheck(unittest.TestCase):
    @patch('password.pwn_check.urllib.request.urlopen')
    def test_request_api_data_success(self, patcher):
        patcher.return_value.__enter__.return_value.read.return_value = 'ok'
        patcher.return_value.__enter__.return_value.code = 200
        request_api_data('test')
        patcher.assert_called()

    @patch('password.pwn_check.urllib.request')
    def test_request_api_data_fail(self, patcher):
        patcher.return_value.__enter__.return_value.read.return_value = 'ok'
        patcher.return_value.__enter__.return_value.code = 400
        with self.assertRaises(RuntimeError):
            request_api_data('test')

    def test_get_password_leaks_count_found(self):
        count = get_password_leaks_count(b'First:2\nSecond:4', 'Second')
        self.assertEqual(count, '4')

    def test_get_password_leaks_count_not_found(self):
        count = get_password_leaks_count(b'First:2\nSecond:4', 'Foo')
        self.assertEqual(count, 0)

    @patch(
        'password.pwn_check.request_api_data',
        return_value=b'5DA08DH:2\n1E4C9B93F3F0682250B6CF8331B7EE68FD8:4'
    )
    def test_pwned_api_check_found(self, mock_api):
        response = pwned_api_check('password')
        self.assertEqual(response, '4')
