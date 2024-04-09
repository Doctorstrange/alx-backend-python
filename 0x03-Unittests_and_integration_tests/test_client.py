#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import get_json, GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        test_client = GithubOrgClient(org_name)

        test_client.org()
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

if __name__ == '__main__':
    unittest.main()