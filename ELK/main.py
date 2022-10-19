import sys
import argparse
import pandas as pd
import numpy as np
from execution_time.prediction_execution import predict_exe
from execution_time.elk import elk_connect
import time


def execution_time(tests_name):

    database_campaign = pd.DataFrame()
    all_tests_names = np.array(np.reshape(tests_name, len(tests_name), 1)).astype(str)
    all_tests_names = list(all_tests_names)

    for testname in all_tests_names:
        if testname == '':
            all_tests_names.remove(testname)

    if len(all_tests_names) == 0:
        print("No test to execute please insert test name!")

    data_execution_time = []
    number_of_tests = len(all_tests_names)


    start_time=time.time()
    for i in range(number_of_tests):
        #########
        samples = 10

        test_name = all_tests_names[i].astype(str)

        execution_time_array = elk_connect(test_name,samples)  # use prediction function
        print(execution_time_array)

        if str(execution_time_array) == 'new_test':
            execution_time_array = np.zeros(1)

        exe_time = predict_exe(execution_time_array)  # use prediction function

        data_execution_time.append(exe_time)
    end_time = time.time()
    duration = end_time-start_time

    database_campaign['...'] = all_tests_names
    database_campaign['...'] = data_execution_time
    max_time = max(database_campaign['...'])
    # consider a value fora campaign which consist of just new tests without any information for execution time
    if max_time == 0:
        max_time = 100
    database_campaign["..."].loc[(database_campaign['...'] == 0)] = max_time
    database_campaign = database_campaign.sort_index()


    return database_campaign


if __name__ == '__main__':

     test_names = np.loadtxt('Test_group.txt', dtype='S128', delimiter=',')

     result = execution_time(test_names)
     print (result)




