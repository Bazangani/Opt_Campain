from __future__ import absolute_import, print_function
import numpy as np
import pandas as pd
from distribution.Knapsack_algorithm import knapsack
import sys
import argparse


DATABASE_KNAPSACK = pd.DataFrame()
#  initialization of number of Jenkins node


def Distribution(DATABASE_KNAPSACK,NumberofJenkinsnode):

    DATABASE_KNAPSACK["Execution_time"] = DATABASE_KNAPSACK["Execution_time"].astype(int)  # conver Execution time of each test to int

    sum_execution_time_b = sum(DATABASE_KNAPSACK["Execution_time"])  # sum of executions time for all the tests
    capacity_of_node = int((DATABASE_KNAPSACK["Execution_time"].max()).tolist())

    # save the output of the Knapsack as KNAPSACK_RESULT
    knapsack_result = knapsack(DATABASE_KNAPSACK, capacity_of_node)
    number_of_node = np.array(knapsack_result["group_ID"])[-1]
    Optima = sum_execution_time_b / NumberofJenkinsnode

    new_capacity = Optima  # consider optima as the new capasity

    while number_of_node > NumberofJenkinsnode:

                capacity_of_node = int(new_capacity)

                if capacity_of_node > int((DATABASE_KNAPSACK['Execution_time'].max()).tolist()) or capacity_of_node ==int((DATABASE_KNAPSACK['Execution_time'].max()).tolist()):

                         knapsack_result = knapsack(DATABASE_KNAPSACK, capacity_of_node)

                         number_of_node = np.array(knapsack_result["group_ID"])[-1]

                         knapsack_result = knapsack_result.drop("VALUE", axis=1)

                # use the sum of group which have a group ID bigger then 6 as the error for updating sum
                amount_of_error = knapsack_result[knapsack_result["group_ID"] > NumberofJenkinsnode]
                # use 0.25 of amount_of_error divided by 6 as the error
                error = sum(0.25 * amount_of_error["Execution_time"]) / NumberofJenkinsnode
                new_capacity = new_capacity + error

    return knapsack_result









