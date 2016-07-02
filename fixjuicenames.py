#!/usr/bin/python
# Copyright (c) 2016 Jeffrey Sutherland <jeffs@fomsystems.com>
#
# I get CD's every month from BBC Music Magazine, and of course step one is to rip them to
# my media library on my main Linux server.  The filenames and directories created by
# Sound Juicer, even though it has a tick box for removing special characters, doesn't 
# remove spaces, commas, colons or semi-colons, things which can prove problematic for some
# Linux apps.  This little Python script scrubs my media library and renames files and 
# directories into something more friendly for Linux/Unix applications.  Note we do NOT do
# anything with the characters themselves, unicode is cool.  So there may be Cyrillic,
# Japanese, Chinese or other characters in the names, which is perfectly OK, at least with
# modern Linux apps.  Note this should work on Windows as well but Windows is less picky about
# special characters, particularly spaces.

# Note that this method walks a directory tree rooted at sys.argv[1] from
# the bottom up, useful if you wish to rename ALL of the files AND directories
# in the tree.

import re, os, sys, string

scanlist = '[\s\[\]\}\{,\|?$!&:\'\)\(;\\\]'
dirscanlist = '[\s\[\]\}\{,.\|?$!&:\'\)\(;\\\]'
renamed_file = 0
renamed_dir = 0

for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for name in files:
#DEBUG
#	print 'regular file: %s' % name
#	print 'full path: %s' % (os.path.join(root,name))
	fixed_name = re.sub(scanlist,'_',name)
	if name != fixed_name:
		print 'regular file: %s' % name
		print 'Fixed name: %s' % fixed_name
		print 'Renaming file...'
		os.renames(os.path.join(root,name),os.path.join(root,fixed_name))
		renamed_file = renamed_file + 1
		
    for name in dirs:
#DEBUG
#	print 'regular directory: %s' % name
#	print 'full dir path: %s' % (os.path.join(root,name))
	fixed_name = re.sub(dirscanlist,'_',name)
	if name != fixed_name:
		print 'regular directory: %s' % name
		print 'Fixed dir: %s' % fixed_name
		print 'Renaming directory...'
		os.renames(os.path.join(root,name),os.path.join(root,fixed_name))
    		renamed_dir = renamed_dir + 1

print '%d Directories and %d files renamed.' % (renamed_dir, renamed_file)
print 'Processing finished' 
    
