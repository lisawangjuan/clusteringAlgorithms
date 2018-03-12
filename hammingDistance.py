
class HammingDistance(object):

    def __init__(self, clusters, labels):
        self.clusters = clusters
        self.labels = labels


    def rebuildClusters(self):

        # function for finding majority label
        def majority(values):
            mode = 0
            label = ""
            for k, v in values.items():
                if v > mode:
                    mode = v
                    label = k
            return label

        newClusters = {}
        names = {}
        for cluster in self.clusters:
            for c in cluster:
                name = self.labels[c]
                names[name] = names.get(name, 0) + 1
            clusterLabel = majority(names)
            newClusters[clusterLabel] = cluster
            names = {}
        # print newClusters
        return newClusters




    def hamming(self, clusters, labels):
        '''
        :param clusters: list of clusters, each cluster stores index of instances in data
        :param data: list of data
        :param labels: list of labels
        :return: int between 0-1, hanmming distance, the smaller the better
        '''

        n = len(labels)
        misMatch = 0                        # number of edges disagree with two clusters
        for name, cluster in clusters.items():
            for c in cluster:
                if labels[c] != name:
                    misMatch += 1
        return float(misMatch) / n


    def cost(self):
        newClusters = self.rebuildClusters()
        cost = self.hamming(newClusters, self.labels)
        return cost