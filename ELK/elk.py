from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
import datetime
import time


def elk_connect(test_name,sample_size):

    # no test name
    if len(test_name) == 0:
        return 'no name'

    test_document = []


    cilent = Elasticsearch([{'host': '...', 'port': 9200}])    # not locall
    search_index = '*-reindex'   # not local

    start_date = datetime.datetime(2018, 1, 3, 0, 1, 1)
    end_date = datetime.datetime(2019, 7, 11, 23, 50, 50)
    formated_start_date = start_date.isoformat().split('.')[0]
    formated_end_date = end_date.isoformat().split('.')[0]

    query = {
        "size": sample_size,
        "query": {
            "bool": {
                "must": [
                    {"match": {"...": test_name}},
                    {"exists": {"field": "..."}},
                    {"exists": {"field": "..."}},
                    {"range": {"@timestamp": {"gte": formated_start_date,"lt": formated_end_date}}}
                ]
            }
        },

    }

    data = cilent.search(index=search_index, body=query)

    # new_test
    if not data['hits']['hits']:
        return 'new_test'

    features = ["...", "...",'...','...','...']

    for document in data['...']['...']:
        document = document['_source']
        featured_document = {key: document[key] for key in features}
        test_document.append(featured_document)

    data_one_test = pd.DataFrame.from_dict(test_document)
    data_one_test.drop(data_one_test.loc[data_one_test['...'] != test_name].index, inplace=True)

    one_execution_times = np.array(data_one_test["..."]).astype(float)

    return one_execution_times





