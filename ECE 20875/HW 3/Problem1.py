import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a list of counts and converts to a list of probabilities, which is an output
    with a sum of the counts, i.e. the number of samples(int)
    :param hist: a numpy ndarray object
    :return: a tuple that contains a list and a int, i.e. ([...], int)
    """
    # please delete the "pass" below and your code starts here...
    num_samples = np.sum(hist)                        #Function sums the number of entries in hist and a list of probabilities
    return ((hist/num_samples).tolist(), num_samples)
    


def compute_j(histo, width):
    """
    takes list of counts, uses norm_histogram function to output the list of probabilities and the number of samples, 
    then calculates compute_j for one bin width (reference: histogram.pdf page19)
    :param histo: list
    :param width: float
    :return: float
    """
    # please delete the "pass" below and your code starts here...
    num_samples = sum(histo)                #Function sums entries in histo, calls norm_histogram function, calculates bin probabilities, and calculates j
    list_prob = norm_histogram(histo)       
    list_prob_sum = np.sum(np.square((list_prob[0])))
    j = (2 / ((num_samples - 1) * width)) - ((num_samples + 1) / ((num_samples - 1) * width)) * list_prob_sum
    return j


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    
    The variable "data" is the raw data that still needs to be "processed"
    with matplotlib.pyplot.hist to output the histogram

    You need to utilize the variables (data, minimum, maximum, min_bins, max_bins) 
    in sweep_n functions to give values to (x, bins, range) in the function matplotlib.pyplot.hist
    Other input variables of matplotlib.pyplot.hist can be set as default value.
    
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    # please delete the "pass" below and your code starts here...
    j_values = []
    for num_bins in range(min_bins, max_bins + 1):      #Function utilizes compute_j to calculate j values for each bin number in between min and max bins
        width = ((maximum - minimum) / num_bins)
        hist_values = plt.hist(data, num_bins, (minimum, maximum))
        j = compute_j(hist_values[0], width)
        j_values.append(j)
    return j_values
    


def find_min(l):
    """
    takes a list of numbers and returns a tuple that contains the value and index of the two smallest numbers in that list and their mean.
    i.e. 
    ([index_of_smallest_number, index_of_second_smallest_number],[value_of_smallest_number, value_of_second_smallest_number], mean)}
    
    For example:
        If the input list (l) is [14,27,15,49,23,41,147]
        Then it should return ([0,2], [14,15], 14.5)

    :param l: list
    :return: tuple
    """
    # please delete the "pass" below and your code starts here...
    min_indexl = l.index(min(l))            #Function uses l and calculates the two smallest values and their indexes in l, and calculates the mean between them
    copy_l = []
    copy_l = l.copy()
    copy_l.remove(min(l))
    min_index2 = l.index(min(copy_l))
    mean = (min(l) + min(copy_l)) / 2
    return([min_indexl, min_index2], [min(l), min(copy_l)], mean)


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
