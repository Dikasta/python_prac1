# port listening : netstat -tulpn | grep LISTEN
# list to running processes : top or ps
# list of dead processes : ps -a
# check services status : systemctl start/stop/restart/status/enable/disable {service name}
# shutdown machine : systemctl poweroff or init 0
# Forces the process to terminate immediately, without allowing it to clean up or save data. : kill -9 {process name or id}
#kill the process and also free that process memory : kill -15 {process name or id}
# Retrieve last 100 lines logs (Now last 100 lines will be present in newLogfile):  tail -100 <log file>   > newLogfile
# Retrive log buttom to top (latest comming log print first)  : tail -f <message.log>
# hidden file retrive : ls -a
# rename file in same directory or move file one location to another :  mv [source_file_name(s)] [Destination_file_name]

'''rename Command Syntax and Options
There are three types of Perl regular expressions: match, substitute and translate. The rename command uses substitute and translate expressions to change file and directory names.

Substitute expressions replace a part of the filename with a different string. They use the following syntax:

rename [options] 's/[filename element]/[replacement]/' [filename]

With this syntax, the command renames the file by replacing the first occurrence of the filename element with the replacement. In the command above:

rename: Invokes the rename command.
[options]: Provides an optional argument that changes the way the command executes.
s: Indicates a substitute expression.
[filename element]: Specifies the part of the filename you want to replace.
[replacement]: Specifies a replacement for the part of the current filename.
[filename]: Defines the file you want to rename.
A translate expression translates one string of characters into another, character for character. This type of expression uses the following syntax:

rename [options] 'y/[string 1]/[string 2]/' [filename]

An example of a rename command using a translate expression:

rename 'y/abc/xyz/'

In this example, every a character in the filename is replaced by an x, every b by a y, and every c by a z.
===============================================================================================+++++++

Returning to our last example, to change the file extension from .txt to .pdf, use:

rename -v 's/.txt/.pdf/*.txt

phoenixnap@test-systen:-$ rename -v 's/.txt/.pdf/ *.txt
example1.txt renamed as example1.pdf
example2.txt renamed as example2.pdf
example3.txt renamed as example3.pdf
------------------------------------------------------------------------------------------------------------------------
phoentxnap@test-system:-$

2. Replacing a Part of a Filename

Replacing a different part of the filename follows the same syntax. To rename example1.txt, example2.txt,

and example3.txt to test1.txt, test2.txt, and text3.txt, use:


rename -v 's/example/test/ *.txt

phoenixnap@test-system:-$ rename -v 's/example/test/' *.txt
example1.txt renamed as test1.txt
example2.txt renamed as test2.txt
example3.txt renamed as test3.txt

phoenixnap@test-system:-$
==============================================
'''

# awk cmds : https://phoenixnap.com/kb/awk-command-in-linux (read it)

# scan hard disk in depth  : du -h --max-depth=1
# curl (communicates with a web or application server by specifying a relevant URL) : curl https://www.gnu.org/gnu/gnu.html(url)

# create directory : mkdir <directory name>
'''change the permissions of files and folders. We can change permissions of Read/Write on a single file, on a single folder, 
or recursively other subfolders as well. chmod is used to read the current file and write it.
:   sudo chmod -R 777 /var/www
'''
#If the file you want to copy already exists in the destination directory, you can backup your existing file with  :cp --backup <filename> <destinationDirectory>

# create empty txt file : touch File1_name.txt  File2_name.txt  File3_name.txt

# change extention of directory : sudo mkfs -t ext4 /dev/sdb (after run do yes)
#mount directory :sudo mount /dev/sdb /home/user01/Videos/webuiex/results
#sudo chmod -R 0777 /home/user01/Videos/webuiex/results

# sudo umount /dev/sda1
----------------------
File Level permissions
These control permissions on the file level.

r – Grants read permission
w – Grant write permission
x – Grant execute permission
These operations need to be preceded with a '+' or '-' operator.

'+' indicates adding a new permission, and '-'  indicates removing an existing permission.

Here's an example:

chmod +r sample.txt

#display information about the CPU on Linux :   lscpu

#Display information about memory total :   free

 #How can I exclude one word with grep (I understood the question as "How do I match a word but exclude another", for which one solution is two greps in series: First grep finding the wanted "word1", second grep excluding "word2"):  grep "word1" | grep -v "word2"
