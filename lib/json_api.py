import json


class JSON:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def write(self, input):
        try:
            with open(self.file_name, 'w') as results:
                json.dump(input, results)
        except Exception as e:
            print(f"Error during saving: {e}")

    def load(self):
        try:
            with open(self.file_name, 'r') as results:
                return json.load(results)
        except Exception as e:
            print(f"Error during loading: {e}")
