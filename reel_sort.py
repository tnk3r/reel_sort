#!/usr/bin/python
import subprocess, os, sys
try:
        directory = sys.argv[1]
        file_list = subprocess.check_output(["ls", str(directory)]).split("\n")
        current = ""
        for file in file_list:
                if file[0:4] == "All ":
                    print "skipping Main ALE File"
                else:
                    if ".ale" or ".mov" or ".mxf" in file:
                        if current != file[0:4]:
                                print "="*50
                                current = file[0:4]
                        if file != "":
                                print "Moving "+file+" to "+file[0:4]
                                os.system("mkdir -p "+directory+"/"+file[0:4])
                                os.system("mv "+directory+"/"+file+" "+directory+"/"+file[0:4])
except IndexError:
        print "Usage: ./reel_sort 'directory'"
        sys.exit(1)
except StandardError as msg:
        print str(msg)
        sys.exit(1)
exit()
