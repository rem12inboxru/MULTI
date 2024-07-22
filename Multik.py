import multiprocessing

class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        self.request = request
        if "receipt" in request:
            if request[0] in self.data:
                self.data[request[0]] += request[len(request)-1]
            else:
                self.data[request[0]] = request[len(request)-1]
        if "shipment" in self.request:
            if request[0] in self.data and self.data[request[0]] > 0:
                self.data[request[0]] -= request[len(request)-1]
            else:
                print(f'Нет такого товара')

    def run(self, requests):
        self.requests = requests
        for i in self.requests:
            i = multiprocessing.Process(self.process_request(i))
            i.start()
            i.join()
if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [('prod1', 'receipt', 1000), ('prod2', 'receipt', 2000), ('prod1', 'shipment', 500),
            ('prod3', 'receipt', 5000), ('prod2', 'shipment', 1750), ('prod3', 'shipment', 4999)]
    manager.run(requests)
    print(manager.data)