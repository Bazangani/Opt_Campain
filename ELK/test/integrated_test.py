import os
import json
import mock
import pytest
import pkg_resources

from execution_time.main import execution_time

ASSETS_PATH = pkg_resources.resource_filename('execution_time.test', 'assets')

def _get_test_configs():
    with open(os.path.join(ASSETS_PATH, 'test_group.txt'))as file_h:
        data = file_h.read()
    return json.loads(data)

#@pytest.mark.parametrize('config1', empty_file)
#def test_no_name(config1):

   # assert main(config1) == ValueError

#new_test = np.array(['new_test'])

def workflow_test():
    with mock.patch('execution_time.main.database') as mock_database:
        execution_time.workflow()

    assert mock_database.insert.assert_called_once_with(('...',))


def test_new_test():
    with open(os.path.join(ASSETS_PATH, 'test_group.txt')) as file_h:
        data = file_h.read()
    # expected_data = {'Test_name': ["new_test"], 'Execution_time': [100]}
    assert len(execution_time) == 1
    # assert main(config2) == expected_data





