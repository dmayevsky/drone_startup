import pandas as pd
import skimage
from skimage import viewer
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

polygon_file = 'Netivot Main City Polygon.csv'
img_file = 'Netivot.PNG'

polygon_directory = "polygon_csvs"

class loader:
    def __init__(self):
        self.img_file = None
        self.polygon_file = None
        self.img_orig = None
        self.img_height = None
        self.img_width = None
        self.polygon_data = None
        self.polygon_list = None
        self.point_selection = None

    def run_loader(self, img_file, poly_file):
        self.img_file, self.polygon_file = img_file, poly_file
        self.load_image()
        self.load_polygon(self.polygon_file)

    def run_loader_multipolygons(self, img_file, polygon_dir = polygon_directory):
        self.img_file = img_file
        self.load_image()
        self.polygon_file
        polygon_file_list = os.listdir(polygon_dir)
        self.polygon_list = []
        for i in polygon_file_list:
            polygon_path = os.path.join(polygon_dir, i)
            polygon = self.load_polygon(polygon_path)
            print(polygon)
            self.polygon_list.append(self.polygon_data)

        #print(self.polygon_list)

    def display_loader_data(self):
        self.print_image_dimensions()
        self.display_image()
        self.display_polygons()

    def load_image(self):
        self.img_orig = mpimg.imread(self.img_file)
        #self.img_orig = skimage.io.imread(self.img_file)
        self.img_height, self.img_width = self.img_orig.shape[0], self.img_orig.shape[1]

    def load_polygon(self, polygon_file):
        self.polygon_data = pd.read_csv(polygon_file)
        self.polygon_data = self.polygon_data.as_matrix().astype(int)

    def print_image_dimensions(self):
        print('height: ', self.img_height)
        print('width: ', self.img_width)

    def display_image(self):
        new_viewer = plt.imshow(self.img_orig)
        self.point_selection = plt.ginput(2)
        plt.close('all')

    def display_polygons(self):
        print(self.polygon_data)