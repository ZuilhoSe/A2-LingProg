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

def import_folder(path, rescale=True):
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
			if rescale:
				x = image_surf.get_width()
				y = image_surf.get_height()
				image_surf = pygame.transform.scale(image_surf, (4*x, 4*y))
			surface_list.append(image_surf)

	return surface_list

def import_tiles(path):
	surface = pygame.image.load(path).convert_alpha()
	surface_x = surface.get_width()
	surface_y = surface.get_height()
	surface = pygame.transform.scale(surface, (surface_x*4,surface_y*4))
	tile_x = surface.get_size()[0] // 64
	tile_y = surface.get_size()[1] // 64
	tiles = []
	for row in range(tile_y):
		for col in range(tile_x):
			x = col * 64
			y = row * 64
			new_surface = pygame.Surface((64,64), flags = pygame.SRCALPHA)
			new_surface.blit(surface,(0,0),pygame.Rect(x,y,64,64))
			tiles.append(new_surface)
			
	return tiles