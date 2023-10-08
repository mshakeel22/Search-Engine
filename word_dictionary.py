class WordDictionary:
    def __init__(self):
        self.token_to_id = {}
        self.current_id = 1
    
    def add_token(self, token):
        if token not in self.token_to_id:
            self.token_to_id[token] = self.current_id
            self.current_id += 1
    
    def get_id(self, token):
        return self.token_to_id.get(token, None)