# unit test for elk  function
from execution_time.elk import elk_connect


def test_no_name():
    assert elk_connect([]) == 'no name'


#def test_wrong_name():
   # assert elk_connect(['dgdfbhfg']) == 'wrong_name'


def test_no_dat():
    assert elk_connect('new_test') == 'new_test'


def test_one_exampl():
    assert len(elk_connect('com.amadeus.tis.TestFakeServer')) == 636



def test_one_example():
    assert len(elk_connect('spocktest.geb.test.short_life_cycle.RRC222.CommandPage_Banners_On_GG_AIR_Cryptic_Spec')) == 24



















