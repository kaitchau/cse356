root@kaitlyn-hw4:~# sudo nano /root/deploy/deploy.yaml
root@kaitlyn-hw4:~# echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPw6yxRemIWUyepSodu5QCx5aDXh+dgodVFD0qCY1CQ1 root@master-server" >> ~/.ssh/authorized_keys
root@kaitlyn-hw4:~# ansible-playbook /root/deploy/deploy.yaml
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the
implicit localhost does not match 'all'

PLAY [Deploy web servers] ******************************************************************
skipping: no hosts matched

PLAY RECAP *********************************************************************************

root@kaitlyn-hw4:~# sudo nano /root/deploy/inventory.ini
root@kaitlyn-hw4:~# sudo nano /root/deploy/inventory.ini
root@kaitlyn-hw4:~# sudo nano /root/deploy/deploy.yaml
root@kaitlyn-hw4:~# ansible-playbook -i /root/deploy/inventory.ini /root/deploy/deploy.yaml
[WARNING]: Found both group and host with same name: red
[WARNING]: Found both group and host with same name: blue

PLAY [Deploy web servers] ******************************************************************

TASK [Gathering Facts] *********************************************************************
The authenticity of host '130.245.136.193 (130.245.136.193)' can't be established.
ED25519 key fingerprint is SHA256:yFAAoSD21yvgLhtCgNFXImHrHMMHR2iQfEu5dlBWE/M.
This key is not known by any other names
The authenticity of host '130.245.136.205 (130.245.136.205)' can't be established.
ED25519 key fingerprint is SHA256:NUZHB4po0iyECih2GHrKfgvakDqKOtfxSAPJziezUZg.
This key is not known by any other names
The authenticity of host '130.245.136.86 (130.245.136.86)' can't be established.
ED25519 key fingerprint is SHA256:gbE9ayIpOZtj7+jGYe09LCOH7hPuIRIcnWBLHuOV4AM.
This key is not known by any other names
The authenticity of host '130.245.136.254 (130.245.136.254)' can't be established.
ED25519 key fingerprint is SHA256:NGYPI3+/8uhOwinPpDVuPp5X5e2Uu7cgWWM8LQKujI8.
This key is not known by any other names
The authenticity of host '130.245.136.148 (130.245.136.148)' can't be established.
ED25519 key fingerprint is SHA256:42oCMQriggImr5N6HmPXfElDie5haw48ixKtMFFuJ74.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [red]
The authenticity of host '130.245.136.137 (130.245.136.137)' can't be established.
ED25519 key fingerprint is SHA256:6Sho30ML30P6xthgjOjwzpGhFdMMNdDOGCSaKhDqjU8.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [redi]
The authenticity of host '130.245.136.47 (130.245.136.47)' can't be established.
ED25519 key fingerprint is SHA256:GVAF75JsBiP2RaNuSl76JQehVb47tje2UArLPSTcYyQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [redii]
The authenticity of host '130.245.136.157 (130.245.136.157)' can't be established.
ED25519 key fingerprint is SHA256:sS1uJj7MXzI1uiydEd4WWMYknXXgNsKFiVwRUH+Wbxs.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [rediii]
The authenticity of host '130.245.136.130 (130.245.136.130)' can't be established.
ED25519 key fingerprint is SHA256:bA1dc73ul/w8U8HR7Cw8rUhtJBswXoeIX5uEYCMAufY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [rediv]
The authenticity of host '130.245.136.186 (130.245.136.186)' can't be established.
ED25519 key fingerprint is SHA256:N0NU06wrMNNoGxGWnS0c++ElWMCZ6jGm05G4APWj2vI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [blue]
yes
ok: [bluei]
yes
ok: [blueii]
yes
ok: [blueiii]
yes
ok: [blueiv]

TASK [Update apt cache] ********************************************************************
changed: [rediii]
changed: [redii]
changed: [redi]
changed: [rediv]
changed: [red]
changed: [blue]
changed: [blueii]
changed: [blueiii]
changed: [blueiv]
changed: [bluei]

TASK [Install web server] ******************************************************************
changed: [red]
changed: [redi]
changed: [rediv]
changed: [redii]
changed: [rediii]
changed: [bluei]
changed: [blue]
changed: [blueiii]
changed: [blueii]
changed: [blueiv]

TASK [Start and enable nginx] **************************************************************
ok: [red]
ok: [redi]
ok: [redii]
ok: [rediii]
ok: [rediv]
ok: [blue]
ok: [bluei]
ok: [blueii]
ok: [blueiii]
ok: [blueiv]

TASK [Create hw1.html for Red Team] ********************************************************
changed: [red]
changed: [rediii]
changed: [rediv]
changed: [redii]
changed: [redi]
skipping: [blue]
skipping: [bluei]
skipping: [blueii]
skipping: [blueiii]
skipping: [blueiv]

TASK [Create hw1.html for Blue Team] *******************************************************
skipping: [red]
skipping: [redi]
skipping: [redii]
skipping: [rediii]
skipping: [rediv]
changed: [bluei]
changed: [blue]
changed: [blueii]
changed: [blueiii]
changed: [blueiv]

TASK [Install curl] ************************************************************************
ok: [redii]
ok: [red]
ok: [redi]
ok: [rediii]
ok: [rediv]
ok: [bluei]
ok: [blue]
ok: [blueiv]
ok: [blueii]
ok: [blueiii]

PLAY RECAP *********************************************************************************
blue                       : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
bluei                      : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
blueii                     : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
blueiii                    : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
blueiv                     : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
red                        : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
redi                       : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
redii                      : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
rediii                     : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
rediv                      : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

root@kaitlyn-hw4:~#