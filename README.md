# ubuntu-desktop-config
Configs for new ubuntu desktop

Set up for new Ubuntu desktop - tested on 18.04

1. Install ansible via ansible-install.sh script

2. Run the playbook.yml file

```bash
# Run with K for sudo password prompt
ansible-playbook playbook.yml -K -e 'user=username'

# Use environment variable if using current logged in user to run docker
ansible-playbook playbook.yml -K -e "user=$USER"
```