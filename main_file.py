#### http://theory.stanford.edu/~amitp/GameProgramming/index.html

import loading_data
import overlays
import edit_matrices
from implementation import *
import numpy as np
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt


polygon_file = 'Lugano Main City Polygon.csv'
img_file = 'Lugano.PNG'
#start_point = (400, 300) ###### x, y
#end_point = (640, 350) ###### x, y
weighting_list = [30, 100, 100]


def run():
    raw = loading_data.loader()
    #raw.run_loader(img_file, polygon_file)
    raw.run_loader_multipolygons(img_file, "polygon_csvs")
    print('raw_polygon_list:', raw.polygon_list)
    raw.display_loader_data()

    print('Select start and end points')
    start_point, end_point = raw.point_selection[0], raw.point_selection[1]
    start_point = int(start_point[0]), int(start_point[1])
    end_point = int(end_point[0]), int(end_point[1])



    #overlays.create_graphs.draw_and_fill(raw.img_orig, raw.polygon_data, raw.img_height)

    polygon_mat = edit_matrices.fill_polygon(raw.img_height, raw.img_width)
    polygon_count = 0
    for i in raw.polygon_list:
        polygon_mat.fill_polygon(i, weighting_list[polygon_count])
        polygon_count += 1

    compressed_data = edit_matrices.compressor(polygon_mat.base, scale=1, height=raw.img_height, width=raw.img_width)
    compressed_data.compress()

    data_for_algorithm = edit_matrices.prepare_data_for_algorithm(compressed_data.compressed_mat,
                                                                  height=compressed_data.compressed_height,
                                                                  width=compressed_data.compressed_width,
                                                                  start=start_point,
                                                                  end=end_point)

    data_for_algorithm.create_weighting_dict()
    print(data_for_algorithm.weighting_dict)
    data_for_algorithm.prepare_board()
    data_for_algorithm.run_dijkstras()

    print(data_for_algorithm.shortest_path)

    data_for_algorithm.translate_to_numpy()

if __name__ == '__main__':
    run()