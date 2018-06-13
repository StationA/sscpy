from ssc import api


def test_data():
    input_array = [0, 1, 2, 3]
    d = api.Data()
    d['test_array'] = input_array
    assert input_array == d['test_array']
