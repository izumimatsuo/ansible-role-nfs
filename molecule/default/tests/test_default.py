import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nfs_utils_is_installed(host):
    package = host.package("nfs-utils")
    assert package.is_installed
    assert package.version.startswith("1.3")


def test_nfs_server_running_and_enabled(host):
    service = host.service("nfs-server")
    assert service.is_running
    assert service.is_enabled


def test_nfs_listen(host):
    assert host.socket('tcp://0.0.0.0:2049').is_listening
