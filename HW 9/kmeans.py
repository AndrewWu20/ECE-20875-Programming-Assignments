import numpy as np
from cluster import createClusters
from point import makePointList


def kmeans(point_data, cluster_data):
    """Performs k-means clustering on points.

    Args:
      point_data: a p-by-d numpy array used for creating a list of Points.
      cluster_data: A k-by-d numpy array used for creating a list of Clusters.

    Returns:
      A list of clusters (with update centers) after peforming k-means
      clustering on the points initialized from point_data
    """
    # Fill in

    # 1. Make list of points using makePointList and point_data
    point_list = makePointList(point_data)
    # 2. Make list of clusters using createClusters and cluster_data
    cluster_list = createClusters(cluster_data)
    # 3. As long as points keep moving:

    #   A. Move every point to its closest cluster (use Point.closest and
    #     Point.moveToCluster)
    #     Hint: keep track here whether any point changed clusters by
    #           seeing if any moveToCluster call returns "True"

    #   B. Update the centers for each cluster (use Cluster.updateCenter)
    while (True): #If the point keeps moving
        point_moved = False
        for element in point_list:  #Move point towards nearest cluster
            closest_cluster_point = element.closest(cluster_list)
            if element.moveToCluster(closest_cluster_point): 
                point_moved = True
        for counter in cluster_list:  #Update center of cluster
            counter.updateCenter()
        if not point_moved: #Exit loop if points don't change cluster
            break
            
    # 4. Return the list of clusters, with the centers in their final positions
    return cluster_list


if __name__ == "__main__":
    data = np.array(
        [[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]],
        dtype=float,
    )
    centers = np.array([[0, 0], [1, 1]], dtype=float)

    clusters = kmeans(data, centers)
    for c in clusters:
        c.printAllPoints()
