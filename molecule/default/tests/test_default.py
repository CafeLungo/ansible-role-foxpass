#!/usr/bin/env python

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_foxpass_sudoers_file(host):
    f = host.file('/etc/sudoers.d/95-foxpass-sudo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_foxpass_ssh_key_script(host):
    f = host.file('/usr/local/sbin/foxpass_ssh_keys.sh')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o700


def test_assert_ssh(host):
    openssh_server = host.package("openssh-server")

    assert openssh_server.is_installed
