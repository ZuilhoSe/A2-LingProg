from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
	"""Function to import the CSV file and return the map layout

	:param path: Path to the csv file
	:type path: str
	:return: List with the map layout
	:rtype: list
	"""
	terrain_map = []
	with open(path) as level_map:
		layout = reader(level_map,delimiter = ',')
		for row in layout:
			terrain_map.append(list(row))
		return terrain_map

def import_folder(path):
	"""Function to import all the images from a folder

	:param path: Path to the folder
	:type path: str
	:return: List with the images
	:rtype: list
	"""	
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			image_surf = pygame.transform.scale(image_surf, (64,64))
			surface_list.append(image_surf)

	return surface_list
