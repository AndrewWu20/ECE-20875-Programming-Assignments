import scipy.stats as stats
import numpy as np


def get_data(filename):
    return np.loadtxt(filename)


def get_coordinates(data, each_dist):
    # Part A
    """
    :param: np.ndarray, str
    :return: np.ndarray, np.ndarray
    """
    # Your code starts here...
    QQplot = stats.probplot(data, dist = each_dist) #Function uses data to create a qq plot, and obtains position of x and y
    X, Y = QQplot[0]
    return(np.array (X), np.array(Y))


def calculate_distance(x, y):
    # Part B

    """
    :param: float, float
    :return: float
    """
    # Your code starts here...
    add_xy = x + y          #Function uses x and y and calculates the distance between the two points
    dist_left = (x - (add_xy / 2))**2
    dist_right = (y - (add_xy / 2))**2
    calc_dist = np.sqrt(dist_left + dist_right)
    return calc_dist


def find_dist(sum_err, dists):
    # Part C
    """
    :param: list[float], list[str]
    :return: float, str
    """
    # Your code starts here...
    min_sum_err = min(sum_err)      #Function uses the minimum sum of squared distances to determine the distribution of the data
    min_sum_err_index = sum_err.index(min_sum_err)
    dist = dists[min_sum_err_index]
    return(min_sum_err, dist)


def main(data_file):
    """
    Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return 0.32, 'norm')
    :param: *.csv file name (str)
    :return: float, str
    """
    # Part B
    data = get_data(data_file)
    dists = ("norm", "expon", "uniform", "wald")
    sum_err = [0] * 4
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist)
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y)
    return find_dist(sum_err, dists)


if __name__ == "__main__":
    #test case for calculate_distance function
    print("Test case for calculate_distance:")
    print("Student answer was (rounded to 4 places):", round(calculate_distance(10, 20),4), "    calculate_distance answer correct?",
          round(calculate_distance(10, 20),4) == 7.0711)
    print(" ")
    print("Error and the distribution selected for the given .csv files ")
    
    for each_dataset in [
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
        "distA.csv",
        "distB.csv",
        "distC.csv",
    ]:
        print(main(each_dataset))
