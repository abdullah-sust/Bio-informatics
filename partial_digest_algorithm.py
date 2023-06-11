# PartialDigest Algorithm

class delta:
    N = 0
    def __init__(self, v, listOfInts):
        delta.N += 1
        self.items = [abs(v - x) for x in listOfInts]

    def subset(self, listOfInts):
        Lcopy = [i for i in listOfInts]
        for delta in self.items:
            if delta not in Lcopy:
                return False
            else:
                Lcopy.remove(delta)
        return True

def Place(L, X):
    if (len(L) == 0):
        print(X)
        return
    y = max(L)
    dyX = delta(y, X)
    if (dyX.subset(L)):
        X.append(y); map(L.remove, dyX.items)
        Place(L, X)
        X.remove(y); map(L.append, dyX.items)
    w = max(X) - y          # width - y
    dwX = delta(w, X)
    if (dwX.subset(L)):
        X.append(w); map(L.remove, dwX.items)
        Place(L, X)
        X.remove(w); map(L.append, dwX.items)
    return

def partialDigest(L):
    width = max(L)
    L.remove(width)
    X = [0, width]
    Place(L, X)

L = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]
partialDigest(L)
