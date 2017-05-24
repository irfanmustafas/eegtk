import numpy as np


# replace this with the directory containing the data
data_directory = "."

# lists of different populations
pid_noConcussion = np.arange(1, 34)  # patients 1-33 had no concussions
pid_3stepProtocol = np.arange(34, 45)  # patients 34-44 used the 3 step protocol
pid_testRetest = np.arange(45, 55)  # patients 45-55 were freshmen, 1/2 male, 1/2 female, retested within a few days
pid_concussion = np.arange(55, 99)  # patients 55-98 were assessed for concussion

# features to use. For each tuple:
#   first element is function name in feature_extractors.py and second element are positional arguments for the function
feature_functions = [
    ("correlation", []),
]


embedding_args = {
    "mode": "pca",
    "n_components": 2,
}
