class Field():
    def __init__(self, id, isOwned):
        self.id = id
        self.isOwned = isOwned
        self.plots = [[['empty', 0] for x in range(10)] for y in range(10)]