from opcua import Client


class OPCClient:

    def __init__(self, url="opc.tcp://127.0.0.1:48402/freeopcua/server/"):
        self.url = url
        self.client = Client(self.url)

    def get_value(self, count):
        num = 2
        list_value = list()
        while num < count + 2:
            list_value.append(self.client.get_node(f'ns=2; i={num}').get_value())
            num += 1
        return list_value

    def run(self):
        self.client.connect()
        print(f'Client connected to {self.url}')
