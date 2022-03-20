import random

import requests
from rest_framework.exceptions import ValidationError


class Fetcher(object):
    """"""

    def serialize_objects(self, response_objects, serializer):
        serialized_objects = serializer(data=response_objects, many=True)
        serialized_objects.is_valid(raise_exception=True)
        return serialized_objects.data

    def fetch_objects(self, url, serializer):
        """"""
        random_int = random.randint(0, 10)
        print(random_int)
        if random_int < 6:
            raise ValidationError(detail={'message': 'Validation Error'})
        response = requests.get(url)
        not_expected_status = 400
        if response.status_code >= not_expected_status:
            response.raise_for_status()
        extracted_objects = response.json()['data']
        return self.serialize_objects(extracted_objects, serializer)

    def exceptions_handler(self, function):
        def decorator(*args, **kwargs):
            try:
                function_response = function(*args, **kwargs)
            except Exception:
                return None
            return function_response
        return decorator
