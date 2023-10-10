class Dataset:
    def __init__(self, name, data, labels, balanced):
        self.name = name
        self.data = data
        self.labels = labels
        self.balanced = balanced

    def __getitem__(self, index):
        return self.data[index], self.labels[index]

    def __len__(self):
        return len(self.data)