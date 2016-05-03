#!/bin/sh

vagrant up
sleep 3s
exec ansible-playbook -i hosts.vagrant webapp.yml -K
