import os
import pygame

BASE_PATH = 'images/'

def load_image(path):
    img = pygame.image.load(BASE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_PATH):
        images.append(load_image(img_name))
    return images