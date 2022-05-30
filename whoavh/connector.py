import ovh
import webbrowser


class OVHAppConnector(object):
    def __init__(self, from_conf_file=True, new_consumer_key=True):
        # TODO: Add config file parser / validator
        if from_conf_file:
            # The client is the basic endpoint connector
            self.client = ovh.Client()

        if new_consumer_key:
            # The Key_Request is the request that allows your app to access certain paths
            self.key_request = self.client.new_consumer_key_request()

            # Here we request RO Access to the "/me" path.
            self.key_request.add_rules(ovh.API_READ_ONLY, "/me")

            # For the purpose of our App, we'd also need /domain RO for example
            self.key_request.add_rules(ovh.API_READ_ONLY, "/domain")

        self.consumer_key_response = self.key_request.request()

        # Point browser to validation URL
        _validation_url = self.consumer_key_response['validationUrl']
        webbrowser.open(_validation_url)

    def get_client_data(self):
        client_data = self.client.get('/me')
        print(client_data)

    def get_consumer_key_token(self):
        # TODO: Store Token in .conf file for reuse.
        self.consumer_key = self.consumer_key_response['consumerKey']
        print(self.consumer_key)
