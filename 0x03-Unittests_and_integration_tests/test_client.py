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

    class TestGithubOrgClient(unittest.TestCase):

    def test_public_repos_url(self):
        # Define a known payload
        mock_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Patch the org property to return the known payload
        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            # Create an instance of GithubOrgClient
            test_client = GithubOrgClient('test_org')

            # Call the _public_repos_url method
            result = test_client._public_repos_url()

            # Assert that the result is the expected one
            self.assertEqual(result, mock_payload["repos_url"])

if __name__ == '__main__':
    unittest.main()