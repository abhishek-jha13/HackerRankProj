from scipy import misc
import matplotlib.pyplot as plt
import random
import numpy as np

def apply(avg_pixel_list, K):

    #centroids = np.zeros((K, 3), dtype=int)
    C = np.zeros(len(avg_pixel_list), dtype=int)
    centroids = np.random.randint(255, size = (K, 3))
    #for i in range(0, len(centroids)):
        #centroids[i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    print (centroids)
    # C = numpy.zeros((len(centroids)))
    ctr_of_clusters = np.zeros((len(centroids)), dtype=int)
    sum_of_clusters = np.zeros((len(centroids), 3))
    ctr = 30
    while (ctr != 0):
        ctr -= 1
        for i in range(0, len(avg_pixel_list)):
            C[i] = 0
            min_dist = np.linalg.norm(avg_pixel_list[i] - centroids[C[i]])
            for k in range(1, len(centroids)):
                if np.linalg.norm(avg_pixel_list[i] - centroids[k]) < min_dist:
                    C[i] = k
                    min_dist = np.linalg.norm(avg_pixel_list[i] - centroids[C[i]])
            sum_of_clusters[C[i]] += avg_pixel_list[i]
            ctr_of_clusters[C[i]] += 1
        print ("######################################")
        for i in range(0, len(centroids)):
            if ctr_of_clusters[i] != 0:
                centroids[i] = sum_of_clusters[i] / ctr_of_clusters[i]
            else:
                centroids[i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            print ",".join(map(str, centroids[i]))

    #for i in range(0, len(avg_pixel_list)):
        #avg_pixel_list[i] = centroids[C[i]]
