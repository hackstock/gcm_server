__author__ = 'Edward Pie'
import requests
import json


class GCMServer(object):
    def __init__(self, server_key):
        self.server_key = server_key
        self.headers = {"Authorization": "%s=%s" % ("key", self.server_key), "Content-Type": "application/json"}
        self.url = "https://android.googleapis.com/gcm/send"

    def send_to_one(self, gcm_id, title, message):
        try:
            payload = {"data": {"title": title, "message": message}, "registration_ids": [gcm_id]}
            response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))

            print "Response Status Code : ", response.status_code
            print "Response Body : ", response.json()
        except Exception, e:
            print "Oops! An error occured! ", e.message

    def send_to_many(self, gcm_ids, title, message):
        try:
            payload = {"data": {"title": title, "message": message}, "registration_ids": gcm_ids}
            response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))

            print "Response Status Code : ", response.status_code
            print "Response Body : ", response.json()
        except Exception, e:
            print "Oops! An error occured! ", e.message

