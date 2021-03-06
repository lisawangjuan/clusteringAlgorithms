from singleLinkage import SingleLinkage
from averageLinkage import AverageLinkage
from completeLinkage import CompleteLinkage
from kMeansMethod import KMeans
from kMedoidsMethod import KMedoids
from hammingDistance import HammingDistance
import string

def main():
    # start_time = time.time()

    # data = [[0, 0], [1, 3], [4, 5], [1, 1], [2, 1], [5, 2]]
    # labels = ["close", "close", "far", "close", "close", "far"]

    # data, labels = readIris("iris_test.txt")
    # data, labels = readIris("iris.txt")
    # data, labels = readUserKnowledge("userKnowledge.txt")
    data, labels = readUserKnowledge("seeds.txt")


    # find number of classifiers, use its number as cluster number k
    uniqueLabels = []
    for label in labels:
        if label not in uniqueLabels:
            uniqueLabels.append(label)
    k = len(uniqueLabels)


    # # clustering using single linkage algorithm
    # print "clustering based on single-linkage...."
    # single = SingleLinkage(data, k)
    # singCluster = single.fit()
    # print (singCluster)
    # print
    #
    # # evaluate clustering algorithm by using hamming distance algorithm
    # singleHamming = HammingDistance(singCluster, labels)
    # singleCost = singleHamming.cost()
    # print "singleCost: " + str(singleCost)
    # print
    # #
    #
    # # clustering using complete linkage algorithm
    # print "clustering based on complete-linkage...."
    # complete = CompleteLinkage(data, k)
    # completeCluster = complete.fit()
    # print completeCluster
    # print
    #
    # completeHamming = HammingDistance(completeCluster, labels)
    # completeCost = completeHamming.cost()
    # print "completeCost: "+ str(completeCost)
    # print


    # clustering using average linkage algorithm
    print "clustering based on average-linkage...."
    average = AverageLinkage(data, k)
    averageCluster = average.fit()
    # print averageCluster
    print

    averageHamming = HammingDistance(averageCluster, labels)
    averageCost = averageHamming.cost()
    print "averageCost: " + str(averageCost)
    print



    # # clustering using k-means
    # print "clustering based on kmeans-method...."
    # costKMeans = []
    # for i in xrange(100):
    #     kmeans = KMeans(data, k)
    #     kmeansCluster = kmeans.kmeans()
    #     kmeansCost = HammingDistance(kmeansCluster, labels).cost()
    #     costKMeans.append(kmeansCost)
    # print "kmeansCost: " + str(min(costKMeans))
    # print
    #
    # # clustering using k-medoids
    # print "clustering based on kMedoids-method...."
    # costKMedoids = []
    # for i in xrange(100):
    #     kmedoids = KMedoids(data, k)
    #     kmedoidsCluster = kmedoids.kmedoids()
    #     kmedoidsCost = HammingDistance(kmedoidsCluster, labels).cost()
    #     costKMedoids.append(kmedoidsCost)
    # print "completeCost: "+ str(min(costKMedoids))
    # print


def readIris(filename):
    datafile = open(filename, 'r')
    data = []
    labels = []
    for line in datafile:
        row = line.rstrip("\n").split(",")
        instance = []
        for cord in row[:-1]:
            instance.append(float(cord))
        data.append(instance)
        labels.append(row[-1])
    return data, labels

def readUserKnowledge(filename):
    datafile = open(filename, 'r')
    data = []
    labels = []
    for line in datafile:
        row = line.rstrip("\t\n").split("\t")
        instance = []
        for cord in row[:-1]:
            cord = string.replace(cord, ",", ".")
            # print float(cord)
            instance.append(float(cord))
        data.append(instance)
        labels.append(row[-1])
    return data, labels

main()

