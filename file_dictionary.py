class FileDictionary:
    def __init__(self):
        self.file_to_id = {}
        self.current_id = 1
    
    def add_file(self, filename):
        if filename not in self.file_to_id:
            self.file_to_id[filename] = self.current_id
            self.current_id += 1
    
    def get_id(self, filename):
        return self.file_to_id.get(filename, None)