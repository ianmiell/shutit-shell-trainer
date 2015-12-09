"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class shell_trainer(ShutItModule):


	def build(self, shutit):
		# Some useful API calls for reference. See shutit's docs for more info and options:
		#
		# ISSUING BASH COMMANDS
		# shutit.send(send,expect=<default>) - Send a command, wait for expect (string or compiled regexp)
		#                                      to be seen before continuing. By default this is managed
		#                                      by ShutIt with shell prompts.
		# shutit.multisend(send,send_dict)   - Send a command, dict contains {expect1:response1,expect2:response2,...}
		# shutit.send_and_get_output(send)   - Returns the output of the sent command
		# shutit.send_and_match_output(send, matches) 
		#                                    - Returns True if any lines in output match any of 
		#                                      the regexp strings in the matches list
		# shutit.send_until(send,regexps)    - Send command over and over until one of the regexps seen in the output.
		# shutit.run_script(script)          - Run the passed-in string as a script
		# shutit.install(package)            - Install a package
		# shutit.remove(package)             - Remove a package
		# shutit.login(user='root', command='su -')
		#                                    - Log user in with given command, and set up prompt and expects.
		#                                      Use this if your env (or more specifically, prompt) changes at all,
		#                                      eg reboot, bash, ssh
		# shutit.logout(command='exit')      - Clean up from a login.
		# 
		# COMMAND HELPER FUNCTIONS
		# shutit.add_to_bashrc(line)         - Add a line to bashrc
		# shutit.get_url(fname, locations)   - Get a file via url from locations specified in a list
		# shutit.get_ip_address()            - Returns the ip address of the target
		# shutit.command_available(command)  - Returns true if the command is available to run
		#
		# LOGGING AND DEBUG
		# shutit.log(msg,add_final_message=False) -
		#                                      Send a message to the log. add_final_message adds message to
		#                                      output at end of build
		# shutit.pause_point(msg='')         - Give control of the terminal to the user
		# shutit.step_through(msg='')        - Give control to the user and allow them to step through commands
		#
		# SENDING FILES/TEXT
		# shutit.send_file(path, contents)   - Send file to path on target with given contents as a string
		# shutit.send_host_file(path, hostfilepath)
		#                                    - Send file from host machine to path on the target
		# shutit.send_host_dir(path, hostfilepath)
		#                                    - Send directory and contents to path on the target
		# shutit.insert_text(text, fname, pattern)
		#                                    - Insert text into file fname after the first occurrence of 
		#                                      regexp pattern.
		# shutit.delete_text(text, fname, pattern)
		#                                    - Delete text from file fname after the first occurrence of
		#                                      regexp pattern.
		# shutit.replace_text(text, fname, pattern)
		#                                    - Replace text from file fname after the first occurrence of
		#                                      regexp pattern.
		# ENVIRONMENT QUERYING
		# shutit.host_file_exists(filename, directory=False)
		#                                    - Returns True if file exists on host
		# shutit.file_exists(filename, directory=False)
		#                                    - Returns True if file exists on target
		# shutit.user_exists(user)           - Returns True if the user exists on the target
		# shutit.package_installed(package)  - Returns True if the package exists on the target
		# shutit.set_password(password, user='')
		#                                    - Set password for a given user on target
		#
		# USER INTERACTION
		# shutit.get_input(msg,default,valid[],boolean?,ispass?)
		#                                    - Get input from user and return output
		# shutit.fail(msg)                   - Fail the program and exit with status 1
		# 
		shutit.send('cd /root')
		shutit.send_file('/root/ps.txt','''UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Dec02 ?        00:00:24 /sbin/init splash nomdmonddf nomdmonisw
root         2     0  0 Dec02 ?        00:00:01 [kthreadd]
root         3     2  0 Dec02 ?        00:01:07 [ksoftirqd/0]
root         5     2  0 Dec02 ?        00:00:00 [kworker/0:0H]
root         7     2  0 Dec02 ?        00:17:16 [rcu_sched]
root         8     2  0 Dec02 ?        00:00:00 [rcu_bh]
root         9     2  0 Dec02 ?        00:07:19 [rcuos/0]
root        10     2  0 Dec02 ?        00:00:00 [rcuob/0]
root        11     2  0 Dec02 ?        00:00:01 [migration/0]
root        12     2  0 Dec02 ?        00:00:09 [watchdog/0]
root        13     2  0 Dec02 ?        00:00:09 [watchdog/1]
root        14     2  0 Dec02 ?        00:00:01 [migration/1]
root        15     2  0 Dec02 ?        00:00:00 [ksoftirqd/1]
root        17     2  0 Dec02 ?        00:00:00 [kworker/1:0H]
root        18     2  0 Dec02 ?        00:06:16 [rcuos/1]
root        19     2  0 Dec02 ?        00:00:00 [rcuob/1]
root        20     2  0 Dec02 ?        00:00:08 [watchdog/2]
root        21     2  0 Dec02 ?        00:00:01 [migration/2]
root        22     2  0 Dec02 ?        00:00:00 [ksoftirqd/2]
root        24     2  0 Dec02 ?        00:00:00 [kworker/2:0H]
root        25     2  0 Dec02 ?        00:06:00 [rcuos/2]
root        26     2  0 Dec02 ?        00:00:00 [rcuob/2]
root        27     2  0 Dec02 ?        00:00:00 [khelper]
root        28     2  0 Dec02 ?        00:00:00 [kdevtmpfs]
root        29     2  0 Dec02 ?        00:00:00 [netns]
root        30     2  0 Dec02 ?        00:00:00 [perf]
root        31     2  0 Dec02 ?        00:00:00 [khungtaskd]
root        32     2  0 Dec02 ?        00:00:00 [writeback]
root        33     2  0 Dec02 ?        00:00:00 [ksmd]
root        34     2  0 Dec02 ?        00:00:52 [khugepaged]
root        35     2  0 Dec02 ?        00:00:00 [crypto]
root        36     2  0 Dec02 ?        00:00:00 [kintegrityd]
root        37     2  0 Dec02 ?        00:00:00 [bioset]
root        38     2  0 Dec02 ?        00:00:00 [kblockd]
root        39     2  0 Dec02 ?        00:00:00 [ata_sff]
root        40     2  0 Dec02 ?        00:00:00 [md]
root        41     2  0 Dec02 ?        00:00:00 [devfreq_wq]
root        46     2  0 Dec02 ?        00:01:39 [kswapd0]
root        47     2  0 Dec02 ?        00:00:00 [fsnotify_mark]
root        48     2  0 Dec02 ?        00:00:00 [ecryptfs-kthrea]
root        59     2  0 Dec02 ?        00:00:00 [kthrotld]
root        60     2  0 Dec02 ?        00:00:00 [acpi_thermal_pm]
root        61     2  0 Dec02 ?        00:00:00 [scsi_eh_0]
root        62     2  0 Dec02 ?        00:00:00 [scsi_tmf_0]
root        63     2  0 Dec02 ?        00:00:00 [scsi_eh_1]
root        64     2  0 Dec02 ?        00:00:00 [scsi_tmf_1]
root        69     2  0 Dec02 ?        00:00:00 [ipv6_addrconf]
root        89     2  0 Dec02 ?        00:00:00 [deferwq]
root        90     2  0 Dec02 ?        00:00:00 [charger_manager]
root       134     2  0 Dec02 ?        00:00:00 [kpsmoused]
root       138     2  0 Dec02 ?        00:00:21 [kworker/0:1H]
root       139     2  0 Dec02 ?        00:00:00 [scsi_eh_2]
root       140     2  0 Dec02 ?        00:00:00 [scsi_tmf_2]
root       141     2  0 Dec02 ?        00:00:00 [scsi_eh_3]
root       142     2  0 Dec02 ?        00:00:00 [scsi_tmf_3]
root       217     2  0 Dec02 ?        00:00:00 [raid5wq]
root       246     2  0 Dec02 ?        00:00:00 [bioset]
root       268     2  0 Dec02 ?        00:01:01 [jbd2/sda1-8]
root       269     2  0 Dec02 ?        00:00:00 [ext4-rsv-conver]
root       318     2  0 Dec02 ?        00:00:00 [kauditd]
root       333     1  0 Dec02 ?        00:00:00 /sbin/lvmetad -f
root       335     1  0 Dec02 ?        00:00:16 /lib/systemd/systemd-journald
root       343     1  0 Dec02 ?        00:00:04 /lib/systemd/systemd-udevd
root       434     2  0 Dec02 ?        00:00:00 [iprt-VBoxWQueue]
root       476     2  0 Dec02 ?        00:00:00 [kworker/2:1H]
root       558     2  0 Dec02 ?        00:00:00 [kworker/1:1H]
root       765     1  0 Dec02 ?        00:00:00 /usr/sbin/ModemManager
imiell     769  2567  0 Dec07 ?        00:00:55 xfce4-terminal
imiell     774   769  0 Dec07 ?        00:00:00 gnome-pty-helper
imiell     775   769  0 Dec07 pts/1    00:00:00 bash
root       778     1  0 Dec02 ?        00:00:04 /lib/systemd/systemd-logind
avahi      796     1  0 Dec02 ?        00:00:05 avahi-daemon: running [osboxes.local]
root       803     1  0 Dec02 ?        00:00:22 /usr/lib/accountsservice/accounts-daemon
avahi      807   796  0 Dec02 ?        00:00:00 avahi-daemon: chroot helper
root       819     1  0 Dec02 ?        00:00:01 /usr/sbin/cron -f
message+   841     1  0 Dec02 ?        00:01:16 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
root       869     1  0 Dec02 ?        00:04:10 /usr/sbin/VBoxService
root       884     1  0 Dec02 ?        00:00:00 /sbin/cgmanager -m name=systemd
syslog     890     1  0 Dec02 ?        00:00:05 /usr/sbin/rsyslogd -n
whoopsie   891     1  0 Dec02 ?        00:00:02 /usr/bin/whoopsie -f
root       895     1  0 Dec02 ?        00:00:00 /usr/sbin/cups-browsed
root       907     1  0 Dec02 ?        00:00:08 /usr/sbin/NetworkManager --no-daemon
root       920     1  0 Dec02 ?        00:00:00 /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemonise --scan --syslog
postgres   936     1  0 Dec02 ?        00:00:09 /usr/lib/postgresql/9.4/bin/postgres -D /var/lib/postgresql/9.4/main -c config_file=/etc/postgresql/9.4/main/postgresql.conf
root       937     1  0 Dec02 ?        00:07:48 /usr/bin/docker -d -H fd://
root       938     1  0 Dec02 ?        00:00:01 /usr/sbin/libvirtd
uml-net    944     1  0 Dec02 ?        00:00:30 /usr/bin/uml_switch -unix /var/run/uml-utilities/uml_switch.ctl
root       946     1  0 Dec02 ?        00:00:01 /usr/lib/policykit-1/polkitd --no-debug
root       947     1  0 Dec02 ?        00:00:30 /usr/sbin/console-kit-daemon --no-daemon
root      1046     1  0 Dec02 ?        00:00:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
root      1073     1  0 Dec02 ?        00:00:00 ovsdb-server: monitoring pid 1074 (healthy)                                                                                   
root      1074  1073  0 Dec02 ?        00:00:37 ovsdb-server /etc/openvswitch/conf.db -vconsole:emer -vsyslog:err -vfile:info --remote=punix:/var/run/openvswitch/db.sock --pr
root      1075     1  0 Dec02 ?        00:21:10 /usr/bin/perl -w /usr/bin/sec --conf=/etc/sec.conf --input=/var/log/syslog --pid=/var/run/sec.pid --detach --syslog=daemon
nobody    1126   907  0 Dec02 ?        00:00:48 /usr/sbin/dnsmasq --no-resolv --keep-in-foreground --no-hosts --bind-interfaces --pid-file=/run/sendsigs.omit.d/network-manage
root      1134     1  0 Dec02 ?        00:00:00 ovs-vswitchd: monitoring pid 1135 (healthy)                                                                                   
root      1135  1134  0 Dec02 ?        00:19:36 ovs-vswitchd unix:/var/run/openvswitch/db.sock -vconsole:emer -vsyslog:err -vfile:info --mlockall --no-chdir --log-file=/var/l
root      1538     1  0 Dec02 ?        00:00:00 /usr/sbin/lightdm
root      1608  1538  0 Dec02 tty7     01:26:04 /usr/bin/X -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
postgres  1779   936  0 Dec02 ?        00:00:00 postgres: checkpointer process                                                                                              
postgres  1780   936  0 Dec02 ?        00:00:13 postgres: writer process                                                                                                    
postgres  1781   936  0 Dec02 ?        00:00:13 postgres: wal writer process                                                                                                
postgres  1782   936  0 Dec02 ?        00:00:11 postgres: autovacuum launcher process                                                                                       
postgres  1783   936  0 Dec02 ?        00:00:09 postgres: stats collector process                                                                                           
libvirt+  1814     1  0 Dec02 ?        00:00:00 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default.conf --leasefile-ro --dhcp-script=/usr/lib/libvirt/libvirt_leas
root      1816  1814  0 Dec02 ?        00:00:00 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default.conf --leasefile-ro --dhcp-script=/usr/lib/libvirt/libvirt_leas
lightdm   1949     1  0 Dec02 ?        00:00:00 /lib/systemd/systemd --user
lightdm   1952  1949  0 Dec02 ?        00:00:00 (sd-pam)                               
lightdm   1999     1  0 Dec02 ?        00:00:00 upstart --user --startup-event indicator-services-start
lightdm   2034  1999  0 Dec02 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-bluetooth/indicator-bluetooth-service
kernoops  2041     1  0 Dec02 ?        00:00:08 /usr/sbin/kerneloops
www-data  2043     1  0 Dec02 ?        00:00:00 /usr/bin/webfsd -k /var/run/webfs/webfsd.pid -r /var/www/html -u www-data -g www-data
root      2076     1  0 Dec02 tty1     00:00:00 /sbin/agetty --noclear tty1 linux
rtkit     2105     1  0 Dec02 ?        00:00:19 /usr/lib/rtkit/rtkit-daemon
root      2133  1538  0 Dec02 ?        00:00:00 lightdm --session-child 12 19
imiell    2502     1  0 Dec02 ?        00:00:00 /lib/systemd/systemd --user
imiell    2519  2502  0 Dec02 ?        00:00:00 (sd-pam)                               
imiell    2561     1  0 Dec02 ?        00:00:01 /usr/bin/gnome-keyring-daemon --daemonize --login
imiell    2567  2133  0 Dec02 ?        00:00:00 /sbin/upstart --user
imiell    2623   769  0 Dec07 pts/3    00:00:03 bash
imiell    2777   769  0 Dec07 pts/4    00:00:00 bash
imiell    2846     1  0 Dec02 ?        00:00:00 /usr/bin/VBoxClient --clipboard
imiell    2848  2846  0 Dec02 ?        00:00:00 /usr/bin/VBoxClient --clipboard
imiell    2856     1  0 Dec02 ?        00:00:00 /usr/bin/VBoxClient --display
imiell    2858  2856  0 Dec02 ?        00:00:00 /usr/bin/VBoxClient --display
imiell    2862     1  0 Dec02 ?        00:00:00 /usr/bin/VBoxClient --seamless
imiell    2865  2862  0 Dec02 ?        00:00:00 /usr/bin/VBoxClient --seamless
imiell    2869     1  0 Dec02 ?        00:00:00 /usr/bin/VBoxClient --draganddrop
imiell    2870  2869  0 Dec02 ?        00:34:03 /usr/bin/VBoxClient --draganddrop
imiell    2892  2567  0 Dec02 ?        00:00:00 upstart-udev-bridge --daemon --user
imiell    2897  2567  0 Dec02 ?        00:00:13 dbus-daemon --fork --session --address=unix:abstract=/tmp/dbus-tqCFZDEq7J
imiell    2908  2567  0 Dec02 ?        00:00:01 /usr/lib/x86_64-linux-gnu/hud/window-stack-bridge
imiell    2941  2567  0 Dec02 ?        00:01:25 /usr/lib/x86_64-linux-gnu/bamf/bamfdaemon
imiell    2942  2567  0 Dec02 ?        00:00:06 upstart-dbus-bridge --daemon --session --user --bus-name session
imiell    2960  2567  0 Dec02 ?        00:00:01 upstart-dbus-bridge --daemon --system --user --bus-name system
imiell    2964  2567  0 Dec02 ?        00:00:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
imiell    2972  2964  0 Dec02 ?        00:00:04 /usr/bin/dbus-daemon --config-file=/etc/at-spi2/accessibility.conf --nofork --print-address 3
imiell    2974  2567  0 Dec02 ?        00:00:00 upstart-file-bridge --daemon --user
imiell    2976  2567  0 Dec02 ?        00:00:46 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
imiell    2983  2567  0 Dec02 ?        00:00:00 /usr/lib/gvfs/gvfsd
imiell    2988  2567  0 Dec02 ?        00:00:00 /usr/lib/gvfs/gvfsd-fuse /run/user/1001/gvfs -f -o big_writes
imiell    3005  2567  0 Dec02 ?        00:00:02 /usr/bin/lxsession -s Lubuntu-Netbook -e LXDE
imiell    3015  3005  0 Dec02 ?        00:01:43 openbox --config-file /home/imiell/.config/openbox/lubuntu-rc.xml
imiell    3018  3005  0 Dec02 ?        00:04:22 lxpanel --profile Lubuntu
imiell    3021  3005  0 Dec02 ?        00:00:03 lxlauncher
imiell    3023  2567  0 Dec02 ?        00:00:06 xfce4-power-manager
imiell    3026  2567  0 Dec02 ?        00:00:01 /usr/lib/x86_64-linux-gnu/deja-dup/deja-dup-monitor
imiell    3028  2567  0 Dec02 ?        00:00:00 /usr/bin/ssh-agent -s
imiell    3041  2567  0 Dec02 ?        00:00:21 nm-applet
imiell    3046  2567  0 Dec02 ?        00:00:09 update-notifier
imiell    3053  2567  0 Dec02 ?        00:00:00 /usr/lib/x86_64-linux-gnu/xfce4/xfconf/xfconfd
imiell    3062  2567  0 Dec02 ?        00:00:00 /usr/lib/menu-cache/menu-cached /tmp/.menu-cached-:0-imiell
imiell    3063  2567  0 Dec02 ?        00:00:21 zeitgeist-datahub
imiell    3067  2567  0 Dec02 ?        00:00:00 /usr/lib/gvfs/gvfs-udisks2-volume-monitor
root      3078     1  0 Dec02 ?        00:00:01 /usr/lib/udisks2/udisksd --no-debug
imiell    3079  2567  0 Dec02 ?        00:00:15 light-locker
imiell    3097  2567  0 Dec02 ?        00:00:00 /usr/lib/dconf/dconf-service
imiell    3100  2567  0 Dec02 ?        00:00:01 /usr/bin/zeitgeist-daemon
imiell    3112  2567  0 Dec02 ?        00:00:00 /usr/lib/x86_64-linux-gnu/zeitgeist-fts
imiell    3115  2567  0 Dec02 ?        00:00:00 /usr/lib/gvfs/gvfs-afc-volume-monitor
imiell    3118  2567  5 Dec02 ?        08:01:35 /usr/bin/pulseaudio --start --log-target=syslog
root      3131     1  0 Dec02 ?        00:00:16 /usr/lib/upower/upowerd
imiell    3150  2567  0 Dec02 ?        00:00:00 /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
imiell    3159  2567  0 Dec02 ?        00:00:00 /usr/lib/gvfs/gvfs-mtp-volume-monitor
imiell    3169  2567  0 Dec02 ?        00:00:01 /usr/lib/x86_64-linux-gnu/gconf/gconfd-2
imiell    3173  2567  0 Dec02 ?        00:00:01 /usr/lib/x86_64-linux-gnu/indicator-application-service
root      5293   937  0 Dec06 pts/9    00:00:00 /bin/bash
root      5605   937  0 Dec06 pts/11   00:00:00 /bin/bash
root      5780   937  0 Dec06 pts/12   00:00:00 /bin/bash
root      5932   937  0 Dec06 pts/13   00:00:00 /bin/bash
root      7583   937  0 Dec04 pts/7    00:00:00 /bin/bash
root      7716   937  0 Dec04 pts/8    00:00:00 /bin/bash
root      8602   937  0 Dec07 pts/5    00:00:00 /bin/bash
root      9229   937  0 Dec07 pts/14   00:00:00 /bin/bash
root     10056   937  0 Dec07 pts/15   00:00:00 /bin/bash
root     10437 10056  0 Dec07 pts/15   00:00:00 sleep infinity
root     10673   937  0 Dec07 ?        00:00:00 /bin/sh -c sleep infinity
root     10762 10673  0 Dec07 ?        00:00:00 sleep infinity
imiell   13897  2623  0 Dec07 pts/3    00:00:07 ssh shutit.tk
root     17906     1  0 08:58 ?        00:00:00 /usr/sbin/cupsd -l
root     17908     2  0 08:58 ?        00:00:16 [kworker/0:0]
imiell   19130  2567  0 Dec03 ?        00:00:00 /usr/lib/gvfs/gvfsd-metadata
root     23376   907  0 11:02 ?        00:00:00 /sbin/dhclient -d -q -sf /usr/lib/NetworkManager/nm-dhcp-helper -pf /run/sendsigs.omit.d/network-manager.dhclient-enp0s3.pid -
ntp      23708     1  0 11:02 ?        00:00:05 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 122:138
root     24887     2  0 12:50 ?        00:00:00 [kworker/1:0]
root     27164     2  0 19:21 ?        00:00:00 [kworker/u6:1]
root     27218     2  0 19:23 ?        00:00:00 [kworker/2:3]
root     27220     2  0 19:23 ?        00:00:00 [kworker/2:5]
imiell   28360   769  0 19:27 pts/18   00:00:00 bash
root     28869     2  0 19:35 ?        00:00:00 [kworker/1:1]
root     28890     2  0 19:35 ?        00:00:01 [kworker/0:1]
imiell   29093  2567  4 19:38 ?        00:01:13 /opt/google/chrome/chrome
imiell   29100 29093  0 19:38 ?        00:00:00 cat
imiell   29101 29093  0 19:38 ?        00:00:00 cat
imiell   29104 29093  0 19:38 ?        00:00:00 /opt/google/chrome/chrome --type=zygote
imiell   29106 29104  0 19:38 ?        00:00:00 /opt/google/chrome/nacl_helper
imiell   29110 29104  0 19:38 ?        00:00:00 /opt/google/chrome/chrome --type=zygote
imiell   29147 29093  0 19:38 ?        00:00:00 /opt/google/chrome/chrome --type=gpu-process --channel=29093.0.1946500733 --supports-dual-gpus=false --gpu-driver-bug-workarou
imiell   29160 29110  0 19:38 ?        00:00:04 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=AffiliationBasedMatching/Enabled/AppBannerTriggerin
imiell   29178 29110  0 19:38 ?        00:00:02 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=AffiliationBasedMatching/Enabled/AppBannerTriggerin
imiell   29184 29110  0 19:38 ?        00:00:00 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=AffiliationBasedMatching/Enabled/AppBannerTriggerin
imiell   29192 29110  0 19:38 ?        00:00:01 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=AffiliationBasedMatching/Enabled/AppBannerTriggerin
imiell   29198 29110  0 19:38 ?        00:00:00 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=AffiliationBasedMatching/Enabled/AppBannerTriggerin
imiell   29206 29110  0 19:38 ?        00:00:00 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=AffiliationBasedMatching/Enabled/AppBannerTriggerin
imiell   29210 29110  0 19:38 ?        00:00:00 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=AffiliationBasedMatching/Enabled/AppBannerTriggerin
imiell   29239 29106  0 19:38 ?        00:00:09 /opt/google/chrome/nacl_helper
imiell   29244 29106  0 19:38 ?        00:00:09 /opt/google/chrome/nacl_helper
imiell   29296 29110  1 19:38 ?        00:00:35 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=*AffiliationBasedMatching/Enabled/AppBannerTriggeri
imiell   29427 29110  0 19:38 ?        00:00:08 /opt/google/chrome/chrome --type=renderer --lang=en-GB --force-fieldtrials=*AffiliationBasedMatching/Enabled/AppBannerTriggeri
root     29536     2  0 19:57 ?        00:00:00 [kworker/u6:2]
root     29548     2  0 20:05 ?        00:00:00 [kworker/u6:0]
imiell   29578 28360  0 20:08 pts/18   00:00:00 ps -ef''')
		shutit.send('cat ps.txt',note='In this tutorial you are going to learn the basics of some useful shell utilities by looking at the output of a typical ps command stored in this file.')
		shutit.send("""awk '{print $2}' ps.txt""",note='To start with, we want to get a list of all the process ids. These are listed in the second column.')
		return True

	def get_config(self, shutit):
		# CONFIGURATION
		# shutit.get_config(module_id,option,default=None,boolean=False)
		#                                    - Get configuration value, boolean indicates whether the item is 
		#                                      a boolean type, eg get the config with:
		# shutit.get_config(self.module_id, 'myconfig', default='a value')
		#                                      and reference in your code with:
		# shutit.cfg[self.module_id]['myconfig']
		return True

	def test(self, shutit):
		# For test cycle part of the ShutIt build.
		return True

	def finalize(self, shutit):
		# Any cleanup required at the end.
		return True
	
	def is_installed(self, shutit):
		return False


def module():
	return shell_trainer(
		'tk.shutit.shell_trainer.shell_trainer', 1845506479.0001,
		description='',
		maintainer='',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)

