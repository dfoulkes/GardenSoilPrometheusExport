import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server

class Instance():

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name    

class CustomCollector(object):
    def __init__(self,instance: Instance):
        self.instance = instance
        pass

    def collect(self):
        g = GaugeMetricFamily("MemoryUsage", 'Help text', labels=['instance'])
        g.add_metric([self.instance.getName()], 20)
        yield g

        c = CounterMetricFamily("Soil", 'Current soil moisture level', labels=['instance'])
        c.add_metric([self.instance.getName()], 2000)
        yield c


if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector(Instance("test")))
    while True:
        time.sleep(1)