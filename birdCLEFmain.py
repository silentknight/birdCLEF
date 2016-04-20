#!/usr/bin/python

import time

def main():
	print "Hello World"

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "CTRL+C Pressed"