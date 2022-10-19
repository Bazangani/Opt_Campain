# use the coef and intercept of the the regression model to predict the capacity of each node
import numpy as np

# input of function: array of execution time of tests (a campaign)
# input feature of regression: 1. sum of the execution time in a group  2. number of test


def regression(execution_time_array):

    coef_array = [0.16464, 0.656109]
    model_intercept = 70.62721598207304
    sum_array_execution_time = sum(execution_time_array)
    number_of_test = len(execution_time_array)
    regression_node_capacity = int((coef_array[0]*sum_array_execution_time) +
                                   (coef_array[1]*number_of_test) +
                                   model_intercept )

    return regression_node_capacity

