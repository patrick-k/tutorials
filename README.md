#p4log

##Install
1.  Install Vagrant and VirtualBox

2.  Clone the repository

3.  Before proceeding, ensure that your system has at least 25 Gbytes of free disk space, otherwise the installation can fail in unpredictable ways.

    *  cd vm

    *  vagrant up - This step typically takes over 1 hour to complete, and requires a reliable Internet connection throughout.

When the machine reboots, you should have a graphical desktop machine with the required software pre-installed. There are two user accounts on the VM, vagrant (password vagrant) and p4 (password p4). The account p4 should be logged in when the VM boots up by default, and is the one you are expected to use.

##Run
1.  From ~/tutorials/exercises/basic
	- run make (build the project and execute mininet)
	
2.  From ~/tutorials/exercises/p4runtime (new terminal window)
	- run make (which will fail)
	- ./mycontroller.py
	! This will start the p4log controller


P4 INFO : ./build/advanced_tunnel.p4.p4info.txt

BMV2 INFO : ./build/advanced_tunnel.json

