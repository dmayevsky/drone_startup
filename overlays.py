import matplotlib.pyplot as plt

class create_graphs:
    @classmethod
    def draw_and_fill(cls, img_orig, polygon_data, img_height):
        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 10))

        ax1.imshow(img_orig)
        ax1.plot(polygon_data[:, 0], polygon_data[:, 1])
        ax2.imshow(img_orig)
        ax2.fill(polygon_data[:, 0], polygon_data[:, 1])
        plt.show()

        plt.fill(polygon_data[:, 0], polygon_data[:, 1])
        plt.ylim([img_height, 0])
        plt.show()

