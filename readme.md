### Pomo Timer

This is a very simple timer program to run in the terminal. When executed it will
start a 25 minute timer by default. The script accepts arguments to override the 
durration. pomo 15 for example will start a 15 minute timer.

There are 2 bash scripts that can be used if you'd rather not build an executable.

tpomo works in conjunction with the pomo (Either the bash script, or an executable
called pomo so long as it is in the PATH.) This was created to work specifically 
in tmux. Using tpomo while in a tmux session will create a new pane, resize it 
and execute pomo, essencially emulating a status bar.

Using the pomo bash script
1. Fix the path to the python script on your local machine
2. Move pomo to the bin you keep your scripts (~/bin for me) and ensure that 
is in your PATH
3. chmod 755 pomo to allow it to execute anywere
4. follow these steps for tpomo if you are using tmux
