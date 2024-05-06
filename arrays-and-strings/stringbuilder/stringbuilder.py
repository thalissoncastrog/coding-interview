class StringBuilder:
    
    def __init__(self):
        self.parts = []
    
    def append(self, text):
        self.parts.append(text)
    
    def appendLine(self, text):
        self.parts.append(f'{text}\n')
    
    def __str__(self):
        return ''.join(self.parts)
    