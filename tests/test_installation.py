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
