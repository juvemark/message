from test_plus.test import TestCase
import json

class TestEcho(TestCase):

    def setUp(self):
        self.url = '/api/v1/echo/'

    def test_get_echo_message_null(self):
        '''without msg parameters'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertEqual(result['msg'], '')

    def test_get_echo_message_english(self):
        response = self.client.get(self.url, data={'msg': 'hello world'})
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertEqual(result['msg'], 'hello world')

    def test_get_echo_message_chinese(self):
        response = self.client.get(self.url, data={'msg': '你好世界'})
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertEqual(result['msg'], '你好世界')

    def test_echo_message_post_fobbidden(self):
        '''without msg parameters'''
        response = self.client.post(self.url, data={'msg': 'hello world'})
        self.assertEqual(response.status_code, 403)

