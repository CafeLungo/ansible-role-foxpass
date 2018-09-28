CafeLungo.Foxpass
=========

[![Build Status](https://travis-ci.org/CafeLungo/ansible-role-foxpass.svg?branch=master)](https://travis-ci.org/CafeLungo/ansible-role-foxpass)

Installs FoxPass on a machine

Requirements
------------

Ansible 2.5+
Molecule 2.18.1+

Role Variables
--------------

```yaml
foxpass_base_dn: Base DN
foxpass_bind_user: Bind User
foxpass_bind_pw: Bind Password
foxpass_api_key: FoxPass API Key
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- name: servers
  hosts: all
  vars:
    # Don't worry, the sample vars are from FoxPass docs: https://foxpass.readme.io/docs/ubuntu-1604
    foxpass_base_dn: "dc=example,dc=com"
    foxpass_bind_user: "linux"
    foxpass_bind_pw: "efGHbD3aFq"
    foxpass_api_key: "5GC3NRI5goRBAGkrlsxzYedg0r8HPAO7"
  roles:
    - role: CafeLungo.foxpass
```

Testing and Development
-----------------------

* Run `molecule test` to run the playbook against supported platforms, and run tests
* Run `molecule create` to create all the supported platforms for development purposes
* Run `molecule converge` to run the role against the supported platforms created above
* Run `docker ps` to view the running platforms, and `docker exec -it <name of instance> /bin/bash` to connect to it to check things

License
-------

BSD
