# gitlab

[![Build Status](https://travis-ci.org/infOpen/ansible-role-gitlab.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-gitlab)

Install gitlab package.

## Requirements

This role requires Ansible 2.1 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial
and use:
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# General
gitlab_edition: 'gitlab-ce'

# Package management
gitlab_gpg_keys: "{{ _gitlab_gpg_keys }}"
gitlab_package_cache_valid_time: 3600
gitlab_package_repositories: "{{ _gitlab_package_repositories }}"
gitlab_packages:
  - name: "{{ gitlab_edition }}"
gitlab_system_prerequisites: "{{ _gitlab_system_prerequisites }}"
```

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: infOpen.gitlab }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro

