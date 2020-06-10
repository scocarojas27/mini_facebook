from repositories.GatewayRepository import GatewayRepository

class GatewayService(object):
    def __init__(self):
        self.gateway_repository = GatewayRepository()

    def gateway(self, url):
        self.gateway_repository.gateway()