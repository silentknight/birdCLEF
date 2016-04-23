#!/usr/bin/python

import time
import scipy
import scipy.io.wavfile as sciwav
import matplotlib.pyplot as plt
import numpy
import os
import xml.dom.minidom

def main():
	global rootPath

	rootPath = os.path.join(os.sep, 'media', os.getlogin(), 'Seagate Expansion Drive', 'Datasets', 'TrainingSet')
	access_all_data();


def access_all_data():
	wavPath = os.path.join(rootPath, 'wav')
	xmlPath = os.path.join(rootPath, 'xml')

	for root, dirs, files in os.walk(wavPath):
		for tempfile in files:
			filename_wav = os.path.join(wavPath, tempfile)
			filename_xml = os.path.join(xmlPath, os.path.splitext(tempfile)[0]+".xml")

			xmlfile = xml.dom.minidom.parse(filename_xml)

			[rate, data] = sciwav.read(filename_wav)
			plt.plot(data)
			plt.show()

			time.sleep(1)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "CTRL+C Pressed"