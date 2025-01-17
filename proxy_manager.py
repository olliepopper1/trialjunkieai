import random

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def get_geo_specific_proxy(self, location):
        # Placeholder for geo-specific proxy logic
        return random.choice(self.proxies)  # This should be replaced with actual geo-specific logic

# Example usage
if __name__ == '__main__':
    proxy_list = ['proxy1:port', 'proxy2:port', 'proxy3:port']
    manager = ProxyManager(proxy_list)
    print(manager.get_random_proxy())
