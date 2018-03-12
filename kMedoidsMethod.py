import math
import random
import copy


class KMedoids:
    def __init__(self, data, k):
        self.k = k
        self.data = data
        self.dimension = len(self.data[0])
        self.medoids = []
        self.clusters = [[] for i in xrange(self.k)]
        '''
        list of clusters store k clusters, each cluster contains the index of instances of data
        '''



    def initMedoids(self):
        '''
        randomly choose k data from dataset, convert them to points, used as initial medoids of k clusters
        '''
        # medoidPoints = random.sample(self.data, self.k)
        medoidPoints = random.sample(xrange(len(self.data)), self.k)
        for medoid in medoidPoints:
            self.medoids.append(medoid)


    # calculate new medoid for a cluster, return medoid as Point
    def getMedoid(self, cluster):
        mini = 1e99
        sumDistance = 0
        medoid = 0
        for i in xrange(len(cluster)):
            for j in xrange(len(cluster)):
                sumDistance += self.euclidean_distance(self.data[i], self.data[j])
            if sumDistance < mini:
                mini = sumDistance
                medoid = i
        return cluster[medoid]


    # update new center for each cluster
    def reMedoids(self):
        for i in xrange(self.k):
            self.medoids[i] = self.getMedoid(self.clusters[i])



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
    def kmedoids(self):
        self.initMedoids()
        cutoff = 0.0
        while True:
            for i in xrange(len(self.data)):
                # Get distance between the point and first cluster.
                smallest_distance = self.euclidean_distance(self.data[i], self.data[self.medoids[0]])
                clusterIndex = 0

                #get distance between this point and other clusters
                for j in range(self.k-1):
                    distance = self.euclidean_distance(self.data[i], self.data[self.medoids[j+1]])
                    if distance < smallest_distance:  # update smallest_distance and index accordingly
                        smallest_distance = distance
                        clusterIndex = j + 1
                self.clusters[clusterIndex].append(i)  # put that index of that data instance to the right cluster

            # find bigest shift among all clusters
            biggest_shift = 0.0
            oldMedoids = copy.deepcopy(self.medoids)
            self.reMedoids()
            for i in range(self.k):
                shift = self.euclidean_distance(self.data[oldMedoids[i]], self.data[self.medoids[i]])
                biggest_shift = max(biggest_shift, shift)

            # If the centroids have stopped moving much, say we're done!
            if biggest_shift == cutoff:
                break
            # after each iteration, clear self.clusters
            self.clusters = [[] for i in xrange(self.k)]

        return self.clusters








