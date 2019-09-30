import unittest
import requests

'''
This code takes input dict as the input endpoints that need to be tested.

Picks each testcase one by one and then takes the expected status code and api status code and
compares the same to check if fails or pass


'''
class APITest():
    def __init__(self, input):

        #Converting  input dict to Class attributes
        self.__dict__ = input

    def start_test(self):
        print ("Starting Testing  for {}".format(self.base_url + self.endpoint))

        response = requests.get(self.base_url + self.endpoint)
        rsp = response.status_code
        if self.assert_code == str(rsp):
            print ("Tescase Passed")

        else:
            print ("Testcase Failed")



if __name__ == "__main__":

    input = [ {
        'base_url' :'http://dummy.restapiexample.com/api/v1/',
        'endpoint' : 'employee/81848' ,
        'type': 'json',
        'assert_key' : 'employee_salary',
        'assert_code': "406",


    },
        {
            'base_url': 'http://dummy.restapiexample.com/api/v1/',
            'endpoint': 'employees/212',
            'type': 'json',
            'assert_code': "406",


        },

        {
            'base_url': 'http://dummy.restapiexample.com/api/v1/',
            'endpoint': 'employees',
            'type': 'json',
            'assert_code': "406",

        }
    ]

    for each in input:
        APITest(each).start_test()