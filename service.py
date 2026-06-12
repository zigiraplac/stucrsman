def display(list):
    for item in list:
        item.getAll()
    
def findById(list, id):
    for item in list:
        if item.id == id:
            return item
    return None