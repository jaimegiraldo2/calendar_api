from django.test import TestCase

import json

from .models import Event
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class EventTestCase(APITestCase):
    def test_post_event(self):
        data = {"name":"testcase",
                "details":"details to test the backend",
                "start":"2020-04-18",
                "end":"2020-04-18",
                }
        response = self.client.post("/api/v1/events/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

