#!/usr/bin/python2
import os
import re
import sys

def main():
    for line in sys.stdin:

                match = re.match("^#", line) 

		fields = line.strip().split(':') #strip any whitespace and split into 
                                                #into an array

		if match or len(fields) != 5: # if its a #/comment then move on, or if the .input file line is not 5 then dont check it
			continue  #the continue here is for the FOR loop. So if the line
				   #starts with a # or does NOT have five fields, we skip it
		
                username = fields[0]
		password = fields[1]

		gecos    = "%s %s,,," % (fields[3],fields[2])

		groups   = fields[4].split(',') #This splits the line with the ',' delimiter. used to split the 5th field users into groups. now corresponding lines with usernames have the same line for groups

		print "==> Creating account for %s..." % (username)
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
		#print cmd
		os.system(cmd)  # executing the cmd command and runs in the terminal automatically
		print "==> Setting the password for %s..." % (username)
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
		#print cmd
		os.system(cmd)
		for group in groups: #in this case loops the .input group field and assign usernames to group parties.
			if group != '-':
			    print "==> Assigning %s to the %s group..." % (username,group)
			    cmd = "/usr/sbin/adduser %s %s" % (username,group)
			    #print cmd
			    os.system(cmd)


if __name__ == '__main__':
	main()

