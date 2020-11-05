import numpy as np
import mahotas
import matplotlib.pyplot as plt
import scipy.misc
import scipy.ndimage
from implementation import *

class fill_polygon:
    def __init__(self, img_height, img_width):
        self.base = np.ones((img_height, img_width), 'int32')

    def fill_polygon(self, polygon_data, weighting):
        pointlist = []
        for i in polygon_data:
            Y, X = i[1], i[0]
            pointlist.append((Y, X))
        mahotas.polygon.fill_polygon(pointlist, self.base, color=weighting)
        #plt.matshow(self.base)
        #plt.show()

class compressor:
    def __init__(self, polygon_mat, scale, height, width):
        self.scale = scale
        self.i_width = int(width/scale)
        self.i_height = int(height/scale)
        self.polygon_mat = polygon_mat
        self.compressed_mat = None
        self.weights = None
        self.walls = None
        self.GridWithWeights = None

    def compress(self):
        self.compressed_mat = scipy.ndimage.zoom(self.polygon_mat, [1/self.scale,1/self.scale])
        self.compressed_height = self.compressed_mat.shape[0]
        self.compressed_width = self.compressed_mat.shape[1]
        plt.matshow(self.compressed_mat)
        plt.show()

class prepare_data_for_algorithm:
    def __init__(self, compressed_weighting_map, height, width, start, end):
        self.height = height
        self.width = width
        self.compressed_weighting_map = compressed_weighting_map
        self.weighting_dict = None
        self.set_board = None
        self.shortest_path = None
        self.start = start
        self.end = end

    def printer(self):
        print('height', self.height)
        print('width', self.width)
        print('weighting_map', self.compressed_weighting_map)


    ### NOTE: in this section row and col are switched - Algorithm implementation uses X,Y notation.
    def create_weighting_dict(self):
        d = {}
        for row in range(self.height):
            for col in range(self.width):
                val = self.compressed_weighting_map[row, col]
                d[(col, row)] = val
        self.weighting_dict = d

    def prepare_board(self):
        self.set_board = GridWithWeights(self.width, self.height)
        self.set_board.weights = self.weighting_dict
        self.set_board.walls = []

    def run_dijkstras(self):
        came_from, cost_so_far = dijkstra_search(self.set_board, self.start, self.end)
        shortest_path = reconstruct_path(came_from, start=self.start, goal=self.end)
        self.shortest_path = shortest_path

    def translate_to_numpy(self):
        self.shortest_path_matrix = np.zeros((self.height, self.width), 'int32')
        X, Y = [], []
        for i in self.shortest_path:
            x, y = i[0], i[1]
            X.append(i[0])
            Y.append(i[1])
            self.shortest_path_matrix[y,x] = 1
        plt.close('all')
        f, (ax1, ax2) = plt.subplots(1, 2)
        ax1.matshow(self.compressed_weighting_map)
        ax2.matshow(self.compressed_weighting_map)
        ax2.scatter(X, Y, c='r', marker='+')
        #ax2.matshow(self.shortest_path_matrix)
        plt.show()

