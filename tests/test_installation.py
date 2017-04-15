"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_system_prerequisites(Package, SystemInfo):
    """
    Check system prerequisites packages installed
    """

    packages = []

    if SystemInfo.distribution.lower() in ['debian', 'ubuntu']:
        packages = ['apt-transport-https', 'ca-certificates', 'curl',
                    'debian-archive-keyring', 'openssh-server', 'postfix']
    else:
        pytest.skip('Not apply to %s' % SystemInfo.distribution)

    for package in packages:
        assert Package(package).is_installed


def test_repositories(File, SystemInfo):
    """
    Check repositories files
    """

    repositories_files = []

    if SystemInfo.distribution.lower() in ['debian', 'ubuntu']:
        repositories_files = [
            '/etc/apt/sources.list.d/gitlab.list',
            '/etc/apt/sources.list.d/gitlab-src.list']
    else:
        pytest.skip('Not apply to %s' % SystemInfo.distribution)

    for repository_file in repositories_files:
        assert File(repository_file).exists
        assert File(repository_file).is_file


def test_gitlab_community_packages(Package):
    """
    Check Gitlab packages installed
    """

    packages = ['gitlab-ce']

    for package in packages:
        assert Package(package).is_installed
