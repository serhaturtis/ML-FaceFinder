import os
import sys
import shutil
import getopt
import cv2
import dlib
import face_recognition

def maketree(path):
    try:
        os.makedirs(path)
    except:
        pass

def print_usage(error_cause=''):
	print(error_cause)
	print('Usage: python3 face_finder.py -t <target_dir> -s <search_dir> -p <tolerance>')

def main(argv):
	target_directory = ''
	search_directory = ''
	results_directory = 'matches'
	tolerance = 0.6
	extensions = ('.jpg', '.jpeg', '.png', '.webp')
	
	try:
		opts, args = getopt.getopt(argv, 'ht:s:p:')

	except getopt.GetoptError as e:
		print_usage(e)
		sys.exit(1)
		
	for opt, arg in opts:
		if opt in ['-h']:
			print_usage()
			sys.exit()

		elif opt in ['-t']:
			target_directory = arg

		elif opt in ['-s']:
			search_directory = arg
			
		elif opt in ['-p']:
			tolerance = float(arg)
	
	print('Tolerance: {}'.format(tolerance))
	target_files = []
	search_files = []
	
	for file in os.listdir(target_directory):
		if file.endswith(extensions):
			target_files.append(file)
		
	for file in os.listdir(search_directory):
		if file.endswith(extensions):
			search_files.append(file)
	
	match_counter = 0
	for target_file in target_files:
		img = face_recognition.load_image_file(os.path.join(target_directory, target_file))
		print('Target file: {}'.format(target_file))
		try:
			target_encoding = face_recognition.face_encodings(img, model='small')[0]
		except:
			print('No target encoding found in {}'.format(target_file))
			continue
			
		for search_file in search_files:
			img = face_recognition.load_image_file(os.path.join(search_directory, search_file))
			print('Search file: {}'.format(search_file))
			try:
				search_encoding = face_recognition.face_encodings(img, model='small')[0]
			except:
				print('No encoding found in file {}'.format(search_file))
				continue
			
			result = face_recognition.compare_faces([target_encoding], search_encoding, tolerance)
			print(result)
			if True in result:
				print('Match found in file: {}'.format(search_file))
				result_path = results_directory + '/' + str(match_counter) + '/'
				maketree(result_path)
				shutil.copy(os.path.join(target_directory, target_file), result_path)
				shutil.copy(os.path.join(search_directory, search_file), result_path)
				match_counter += 1
			
	
	

if __name__ == "__main__":
	main(sys.argv[1:])
