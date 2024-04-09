#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import get_json, GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

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

    def test_public_repos_url(self):
        mock_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            test_client = GithubOrgClient('test_org')

            result = test_client._public_repos_url()

            self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=MagicMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
        mock_get_json.return_value = mock_payload

        test_client = GithubOrgClient('test_org')

        repos = test_client.public_repos()

        expected_repos = [{"name": "repo1"}, {"name": "repo2"}]
        self.assertEqual(repos, expected_repos)

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        test_client = GithubOrgClient('test_org')
        result = test_client.has_license(license_key, [repo])
        self.assertEqual(result, expected_result)

class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Configure the side_effect of mock_get
        cls.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: cls.org_payload),
            unittest.mock.Mock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        test_client = GithubOrgClient('test_org')
        repos = test_client.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        test_client = GithubOrgClient('test_org')
        apache2_repos = test_client.public_repos('Apache-2.0')

        self.assertEqual(apache2_repos, self.apache2_repos)
