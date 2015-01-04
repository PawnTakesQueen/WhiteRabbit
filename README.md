White Rabbit
============

White Rabbit is created by Vi Grey (http://pariahvi.com) and is licensed under a BSD 2-Clause License. Read LICENSE.txt for more license text.

Console-based time management program

####Dependencies
* Python (>= 3.0)

####Installation
To install, open a terminal and `cd` to the root directory of this program, then enter the command:
```
sh INSTALL.sh
```

####Starting the program
After installing, simply type this command to start:
```
white-rabbit -o [file]
```
* `-o` specifies the file name of the log file you will end up creating or editing. By default, [file] is set to *white-rabbit.log*.

Here are a few examples and explanations of the examples:
```
white-rabbit
```
or
```
white-rabbit -o
```
Once you start the program, a file named *white-rabbit.log* will be created if it does not yet exist, otherwise it opens *white-rabbit.log*, then writes into the file.  This only works if you have permissions to write or edit that file in the current directory.

```
white-rabbit -o test.log
```
Once you start the program, a file named *test.log* will be created if it does not yet exist, otherwise it opens *test.log*, then writes into the file.  This only works if you have permissions to write or edit that file in the current directory.

```
white-rabbit -o test/test2.log
```
Once you start the program, a file named *test2.log* in the directory *test* inside the current directory will be created if it does not yet exist, otherwise it opens *test2.log* in the directory *test*, then writes into the file.  This only works if you have permissions to write or edit that file in the specified directory and the specified directory exists in the current directory.

####Using the program
As soon as the program starts, you will have a few options of commands to input, depending on what's on the screen.

* `HELP` - Shows options
* `QUIT` - Quits program
* `START` - Starts timer if not started
* `STOP` - Stops timer if stopped
* `TIME` - Show time spent for day, month, year and total time

####Uninstallation
To uninstall, open a terminal and `cd` to the root directory of this program, then enter the command:
```
sh UNINSTALL.sh
```

####Deleting the *white-rabbit* Directory after Installation
If you wish to delete the *white-rabbit* directory, but you installed the program, you can use the command:
```
sudo rm -rf /path/to/white-rabbit
```
where `/path/to/` is the path to the *white-rabbit* directory.  The reason why you need to use `sudo` is because installing the program creates files in the *white-rabbit* that are written by root without giving write permissions to non-root users.
