#!/usr/bin/python

import pyaudio
import wave
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

			# Display XML
			xmlfile = xml.dom.minidom.parse(filename_xml)
			pretty_xml_as_string = xmlfile.toprettyxml()
			print pretty_xml_as_string

			#Play Audio
			CHUNK = 1024
			wf = wave.open(filename_wav, 'rb')
			p = pyaudio.PyAudio()
			
			stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
				channels=wf.getnchannels(),
				rate=wf.getframerate(),
				output=True)
			data = wf.readframes(CHUNK)
			while len(data) > 0:
				stream.write(data)
				data = wf.readframes(CHUNK)

			stream.stop_stream()
			stream.close()
			p.terminate()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "CTRL+C Pressed"