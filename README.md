# lib-upgrade (pip install lib-upgrade)
Package to help developers check and upgrade their libraries as they wish.<br>
<br>
PYTHON VERSION SUPPORTED >= 3.10

# HOW IT WORKS
When executed, the system will check up for all your already used libraries and requirements, and then it 
will provide a list, giving the opportunity for the users to choose which one they want to be upgraded to the
latest version.<br><br>
Libraries it uses: OS, SUBPROCESSES, TIME.SLEEP<br><br>
The system works at that sequence:<br>
1. Through a command line inside the terminal (hidden from user view), it asks PIP the list of libraries that are being 
used that are out of date, transforming it in a temporary .TXT file;
2. After that, it reads all lines from that .TXT file and present it as an interactive menu from which the users can 
easily see and choose, one by one, those that they want to upgrade. Meanwhile, the TXT file is deleted right away;
3. In sequence, the system will confirm the option and give the order to PIP to upgrade that specifc library;
4. During the installation, the system will print the process and give a feedback to the users;
5. Finally, it rolls back to PIP and asks again for out of date libraries to present the menu one more time, restarting 
the interaction;

# HOW IT STOPS
When there is no more libraries out of date according to the information returned from PIP

# "PIP LIST -O" COMMAND
lib_upgade uses " _pip list -o_ " command to recieve the list of all out of date libraries that are being used in the 
project 

# INSTALLING AND EXECUTING:
1. In the terminal, type the command → " pip install lib-upgrade "<br>
<br>
2. After successfully installed, you can run it from inside a _Script_ or from the _Terminal / Python Console_:<br>
<br>
2.1. RUNNING FROM INSIDE AN SCRIPT<br>
- If you are using an IDE e.g. PyCharm, you shall import the library as followed:<br>
 " " "<br>
 from lib_upgrade.lib_upgrade import upgrade_lib<br>
 upgrade_lib()<br>
 " " "
<br>
<br>
2.2. RUNNING FROM TERMINAL / CONSOLE<br>
- If you are using any terminal, make sure you are inside the correct VENV within you project, then import and execute 
as followed:<br><br>
" " "<br>
 (.venv) python<br>
 from lib_upgrade.lib_upgrade import upgrade_lib<br>
 upgrade_lib()<br>
" " "
<br><br>
3. After initialized, interact with the program to choose which one of the out of date libraries you want PIP to
upgrade
4. When there is no more library to be updated, the system will autoterminate.