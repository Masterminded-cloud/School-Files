import math as m
import matplotlib.pyplot as plt

def display_groups(samples,reps,k, input_file_name):
    '''
    Displays the resulting k groups when the data in samples is formed into k groups
    Each groups gets its own color. The reps for each groups are plotted with an "x"
    and the samples are plotted with an "o". The x axis is Vit C, and the y axis is GLA
    :param samples:
    :param reps:
    :param k: The number of groups
    :param input_file_name: The name of the input file
    :return: None
    '''

    colors = ["g","b","r","y","k"]
    for c in range(k): plt.plot(reps[c]["C"],reps[c]["GLA"],"x"+colors[c],markersize=12)
    for p in samples:
        plt.plot(p["C"],p["GLA"],"o"+colors[p["rep"]])
    plotsize = 1.1*max([max(p["C"],p["GLA"]) for p in samples])
    plt.xlim(-1,plotsize)
    plt.ylim(-1,plotsize)
    plt.xlabel("Vit C")
    plt.ylabel("GLA")
    plt.title("File " + input_file_name + "   "+str(k) + " Groups Displayed")
    plt.show()


def get_samples(input_file):
    '''
    Reads in nutrient data from a file whose name is given.
    Assumes each line of the file contains a comma separated pair.
    The first number of a pair is an integer level of
    vitamin C, and the second is an integer level of GLA
    :param input_file: name of file to read from
    :return: A list of dictionaries, where each dictionary has three items,
    "C" for vitamin C level, "GLA" for GLA level, and "rep" for which
    group it belongs to. To begin, the rep for each sample is set to zero
    '''
    f = open(input_file,"r")
    samples_list = []
    for sample in f:
        sample_data = sample.rstrip().split(",")
        samples_list.append({"C": int(sample_data[0]),"GLA": int(sample_data[1]), "rep": 0})
    return samples_list

def dist(p,q):
    """
    Computes the Euclidean distance between two 2d points p and q.
    Uses math module for square root
    :param p: A point with coordinates in a list
    :param q: A point with coordinates in a list
    :return: Euclidean distance between p and q
    """
    return m.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


def classify(samples,k):
    """
    This function treats the "C" values and "GLA" values in samples as two dimensional
    points. It uses k-means to cluster them into k groups. To begin the first k samples
    are used  as the representatives for the k groups. The samples are then ASSIGNed
    to the nearest rep. Then the reps are UPDATEd to have the average coordinates
    of the members of their group. The assign, and update phases are repeated until
    no more changes occur.
    :param samples:
    :param k:
    :return:
    """
# initialize
    reps = [{"C": samples[i]["C"],"GLA": samples[i]["GLA"]} for i in range(k)]
    old_reps = None

    while old_reps != reps:
        #repeat until no changes occur
        old_reps = reps.copy()
#assign: each sample to the nearest  of the k reps
        for p in samples:
          for c in range(k):
            if dist([p["C"],p["GLA"]], [reps[c]["C"],reps[c]["GLA"]]) \
                    < dist([p["C"],p["GLA"]], [reps[p["rep"]]["C"],reps[p["rep"]]["GLA"]]):
                    p["rep"] = c

#update reps to have the average coordinates in their groups
        gp_ct = [0]*k   # count the number of samples in each group
        gp_sum = [{"C":0,"GLA":0} for i in range(k)]
        # sum the "C" & "GLA" levels in each group
        for p in samples:
            gp_ct[p["rep"]] += 1
            gp_sum[p["rep"]]["C"] += p["C"]
            gp_sum[p["rep"]]["GLA"] += p["GLA"]
        # now compute the average coordinates of each group
        for i in range(k):
            reps[i] = {"C":gp_sum[i]["C"]/gp_ct[i],"GLA":gp_sum[i]["GLA"]/gp_ct[i]}

    return(reps)

################################################################
# main program
################################################################
files = ["backyard", "locationA", "locationB","locationC"]
for file_name in files:
    samples = get_samples(file_name + ".txt")
    for s in range(2,5):
        display_groups(samples,classify(samples,s),s,file_name)

