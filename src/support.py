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
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path, rescale=4):
    """Function to import all the images from a folder

    :param path: Path to the folder
    :type path: str
    :return: List with the images
    :rtype: list
    """
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            x = image_surf.get_width()
            y = image_surf.get_height()
            image_surf = pygame.transform.scale(
                image_surf, (rescale*x, rescale*y))
            surface_list.append(image_surf)

    return surface_list


def import_tiles(path, w_tile=64, h_tile=64, rescale=4):
    """Function to import the tiles from a single spritesheet

    :param path: Path to the spritesheet
    :type path: str
    :param w_tile: Width of the tile
    :type w_tile: int
    :param h_tile: Height of the tile
    :type h_tile: int
    :param rescale: Rescale factor
    :type rescale: int
    :return: List with the tiles in the spritesheet
    :rtype: list
    """
    surface = pygame.image.load(path).convert_alpha()
    surface_x = surface.get_width()
    surface_y = surface.get_height()
    # Necessary to resize the tiles to the 64x64 format
    surface = pygame.transform.scale(
        surface, (surface_x*rescale, surface_y*rescale))

    tile_x = surface.get_size()[0] // w_tile  # Number of tiles in the x axis
    tile_y = surface.get_size()[1] // h_tile  # Number of tiles in the y axis

    tiles = []

    # Iterate through the spritesheet and append the tiles to the list
    for row in range(tile_y):
        for col in range(tile_x):
            x = col * w_tile
            y = row * h_tile
            new_surface = pygame.Surface(
                (w_tile, h_tile), flags=pygame.SRCALPHA)
            new_surface.blit(
                surface, (0, 0), pygame.Rect(x, y, w_tile, h_tile))
            tiles.append(new_surface)

    return tiles


def import_text(path):
    """Function to read the speech from a txt file

    :param path: Path to the txt file
    :type path: str
    :return: List with the speech
    :rtype: list
    """
    speech = []
    with open(path) as speech_file:
        for line in speech_file:
            speech.append(line)
    return speech
