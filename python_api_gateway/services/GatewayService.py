from repositories.GatewayRepository import GatewayRepository

class GatewayService(object):
    def __init__(self):
        self.gateway_repository = GatewayRepository()

    def gateway(self, data, url):
        self.gateway_repository.gateway()