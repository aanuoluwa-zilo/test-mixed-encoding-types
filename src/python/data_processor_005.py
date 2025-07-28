class DataProcessor5:
    def __init__(self, config):
        self.config = config
        self.data = []
    
    def process_data(self, data):
        results = []
        for item in data:
            if self._validate_item(item):
                processed = self._transform_item(item)
                results.append(processed)
        return results
    
    def _validate_item(self, item):
        return 'id' in item and 'value' in item
    
    def _transform_item(self, item):
        return {
            'id': item['id'],
            'value': item['value'] * 5,
            'processed': True
        }