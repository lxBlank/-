import uuid

def getUid():
    data = uuid.uuid4().hex
    return data

print(getUid())

def setUid():
    print(getUid())