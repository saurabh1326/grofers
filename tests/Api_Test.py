import unittest
import requests

'''
This code takes input dict as the input endpoints that need to be tested.

Picks each testcase one by one and then takes the expected status code and api status code and
compares the same to check if fails or pass

Add assert_code param to the input to compare its return code


'''


class APITest():
    def __init__(self, input):

        # Converting  input dict to Class attributes
        self.__dict__ = input

    def get_request(self, url ):

        return requests.get(url)

    def post_request(self , url , body):
        return requests.post(url , body = body)


    def start_test(self):
        print("Starting Testing  for {}".format(self.base_url + self.endpoint))

        #Depending on the method in the configuration it will either post a request or get the request

        if self.method == 'get':
            response = self.get_request(self.base_url + self.endpoint)

        if self.method == 'post':
            response = self.post_request(self.base_url + self.endpoint)

        #response = requests.get(self.base_url + self.endpoint)

        if hasattr(self, 'assert_code'):
            print("Testing of Status Code")
            rsp = response.status_code

            if self.assert_code == str(rsp):
                print("Tescase Passed")

            else:
                print("Testcase Failed")

        if hasattr(self, 'assert_res'):
            '''
            If some passed to assert response also then we can implement this 
            '''
            pass

        if hasattr(self, 'assert_schema'):
            '''
            if some passed to assert the schema then we can implement this 
            '''
            pass




if __name__ == "__main__":

    input = [{
        'base_url': 'http://dummy.restapiexample.com/api/v1/',
        'endpoint': 'employee/81988',
        'method' : 'get',
        'type': 'json',
        'assert_key': 'employee_salary',
        'assert_code': "406",

    },
        {
            'base_url': 'http://dummy.restapiexample.com/api/v1/',
            'endpoint': 'employees/212',
            'type': 'json',
            'method' : 'get',
            'assert_code': "406",

        },

        {
            'base_url': 'http://dummy.restapiexample.com/api/v1/',
            'endpoint': 'employees',
            'type': 'json',
            'assert_code': "406",

        },

        {
            'base_url' : 'http://localhost:8080',
            'endpoint' : '/post',
            'method' : 'post',
            'body' : '{"key":"test" , "value" : "2"}',
            'assert_code' : '200'
        },
        {
            'base_url': 'http://localhost:8080',
            'endpoint': '/get/test',
            'method': 'get',
            'assert_code': '200'
        }

    ]

    for each in input:
        print(each)
        Test_obj = APITest(each)

        Test_obj.start_test()
