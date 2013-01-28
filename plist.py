#!/usr/bin/python

# Copyright 2013
# Author: Brad Dworak

import sys, getopt, os, shutil, codecs

def main(argv):
	inputfile = ''
	outputpath = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'plist.py -i <inputfile> -o <outputpath>'
		sys.exit(2)
	print opts
	for opt, arg in opts:
		print opt
		print arg
		if opt == '-h':
			print 'plist.py -i <inputfile> -o <outputpath>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputpath = arg
	print 'Input file is :',inputfile
	print 'Output path is :', outputpath
	if os.path.isdir(outputpath):
		print 'SUCCESS: Output path found'
	else:
		print 'Could not find path at',outputpath
		sys.exit()
	try:
		musiclist = codecs.open(inputfile,"r","iso-8859-1")
	except IOError:
		print 'There was an error opening', inputfile
		sys.exit()
	print 'SUCCESS: File', inputfile,'was opened.'
	fin = inputfile.rpartition("/")[2]
	print outputpath+'/'+fin
	new_playlist = codecs.open(outputpath+'/'+fin,"w","iso-8859-1")
	lines = musiclist.readlines()
	musiclist.close()
	for line in lines:
		ltemp = line.strip('\n')
		fout = ltemp.rpartition("/")[2]
		new_playlist.write(fout+os.linesep)
		if ltemp[:4] != '#EXT':
			ffout = outputpath+'/'+fout
			if not os.path.isfile(ffout):
				print 'Copying',ltemp,'to path',ffout
				try:
					shutil.copy(ltemp,ffout)
				except IOError, e:
					print 'Error copying file. %s' % e
					sys.exit()
			else:
				print 'The file',ffout,'already exists. No copying necessary.'
	new_playlist.close()
if __name__ == "__main__":
	main(sys.argv[1:])