import math
import random
import copy

# each cluster center will be a point
class Point(object):
    def __init__(self, coords):
        self.coords = coords
        # self.n = len(coords)


class KMeans:
    def __init__(self, data, k):
        self.k = k
        self.data = data
        self.dimension = len(self.data[0])
        self.centers = []
        self.clusters = [[] for i in xrange(self.k)]
        '''
        list of clusters store k clusters, each cluster contains the index of instances of data
        '''



    def initCenters(self):
        '''
        randomly choose k data from dataset, convert them to points, used as initial centers of k clusters
        '''
        centerPoints = random.sample(self.data, self.k)
        for point in centerPoints:
            center = Point(point)
            self.centers.append(center)


    # calculate new center for a cluster, return center as Point
    def getCentroid(self, cluster):
        centroid = [0 for _ in xrange(self.dimension)]
        n = len(cluster)
        for i in xrange(self.dimension):
            for j in xrange(n):
                centroid[i] += self.data[cluster[j]][i]
            centroid[i] /= float(n)
        center = Point(centroid)
        return center


    # update new center for each cluster
    def reCenters(self):
        for i in xrange(self.k):
            self.centers[i] = self.getCentroid(self.clusters[i])



    def euclidean_distance(self, data_point_one, data_point_two):
        """
        euclidean distance: https://en.wikipedia.org/wiki/Euclidean_distance
        assume that two data points have same dimension
        """
        size = len(data_point_one)
        result = 0.0
        for i in range(size):
            f1 = float(data_point_one[i])  # feature for data one
            f2 = float(data_point_two[i])  # feature for data two
            tmp = f1 - f2
            result += pow(tmp, 2)
        result = math.sqrt(result)
        return result

    # calculate between cluster distance using Lloyd's method algorithm
    def kmeans(self):
        self.initCenters()
        cutoff = 0.0
        while True:
            for i in xrange(len(self.data)):
                # Get distance between the point and first cluster.
                smallest_distance = self.euclidean_distance(self.data[i], self.centers[0].coords)
                clusterIndex = 0

                #get distance between this point and other clusters
                for j in range(self.k-1):
                    distance = self.euclidean_distance(self.data[i], self.centers[j+1].coords)
                    if distance < smallest_distance:  # update smallest_distance and index accordingly
                        smallest_distance = distance
                        clusterIndex = j + 1
                self.clusters[clusterIndex].append(i)  # put that index of that data instance to the right cluster

            # find bigest shift among all clusters
            biggest_shift = 0.0
            oldCenters = copy.deepcopy(self.centers)
            self.reCenters()
            for i in range(self.k):
                shift = self.euclidean_distance(oldCenters[i].coords, self.centers[i].coords)
                biggest_shift = max(biggest_shift, shift)

            # If the centroids have stopped moving much, say we're done!
            if biggest_shift == cutoff:
                break
            # after each iteration, clear self.clusters
            self.clusters = [[] for i in xrange(self.k)]

        return self.clusters








