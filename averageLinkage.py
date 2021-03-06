import math

class AverageLinkage:
    def __init__(self, data, k):
        self.k = k
        self.data = data
        self.clusters = [[i] for i in xrange(len(self.data))]


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

    # calculate between cluster distance using average-linkage algorithm
    def averageDistance(self):
        sumDistance = 0.0
        merge = (None, None)
        betweenDistance = []                # store between cluster distance
        mergeIndices = []                   # store cluster pair index

        for i in xrange(len(self.clusters)-1):
            for j in xrange(i + 1, len(self.clusters)):
                for c in self.clusters[i]:
                    for d in self.clusters[j]:
                        dist = self.euclidean_distance(self.data[c], self.data[d])      # calculate distance of points between two clusters
                        sumDistance += dist
                average = sumDistance /(len(self.clusters[i]) * len(self.clusters[j]))
                betweenDistance.append(average)                                            # choose the avarage distance as the distance between two clusters
                mergeIndices.append((i, j))                                              # store cluster pair index
                sumDistance = 0.0

        minInd = betweenDistance.index(min(betweenDistance))
        pair = mergeIndices[minInd]                                                     # return index of two clusters with mimimum between cluster distance
        return pair

    def merging(self, pair):
        c1 = pair[0]
        c2 = pair[1]
        self.clusters[c1] += self.clusters[c2]
        self.clusters.pop(c2)


    def fit(self):
        n = len(self.data)
        for i in xrange(n-self.k):
            mergePair = self.averageDistance()
            self.merging(mergePair)
        return self.clusters








