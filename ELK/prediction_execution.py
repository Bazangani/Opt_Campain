import numpy as np
from sklearn.mixture import GaussianMixture

# predict execution time
# input : array of execution times
# output: a prediction for execution time according to the mixtures of Gaussian


def predict_exe(execution_array):
    distribution_data = []
    execution_array = np.array(execution_array)

    # use str or any other format as the input
    for number in execution_array:
        try:
            val = float(number)
        except ValueError:
            return 'string cant consider as the execution time'

    # E0 error of empty array
    if (len(execution_array)) == 0:
        return 'empty array'

    # the Expectation Maximization can implement  only an array bigger than 2 value to predict the execution
    if (len(execution_array)) == 2 or (len(execution_array)) == 1:
        execution_time = max(execution_array)
        return execution_time

    # Consider 1000 last example as the execution time array
    if (len(execution_array)) > 1000:
        index_last = len(execution_array)
        execution_array = execution_array[(index_last-100):index_last]

    # Expected maximization with mixture of Gaussian (number_of_Gaussian=3)
    mix_gaussian_model = GaussianMixture(n_components=3, max_iter=100, tol=0.01)
    mix_gaussian_model.fit(np.expand_dims(execution_array, 1))
    # 9 feature as the feature of tests Distribution
    for mu, sd, p in zip(mix_gaussian_model.means_.flatten(), np.sqrt(mix_gaussian_model.covariances_.flatten()), mix_gaussian_model.weights_):
        distribution_data.append([mu, sd, p])
    # consider the expectation of Distribution as a execution time of the test
    execution_time = (distribution_data[0][0] * distribution_data[0][2]) + (
            distribution_data[1][0] * distribution_data[1][2]) + (
            distribution_data[2][0] * distribution_data[2][2])
   # execution_time = max(distribution_data[0])+max(distribution_data[1])

    return int(execution_time)
