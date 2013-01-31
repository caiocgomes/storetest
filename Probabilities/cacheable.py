from functools import wraps

def cache(fun):
    cacheDict = {}
    @wraps(fun)
    def wrapper(*args, **kwargs):
        hashFQ = str(args)
        if hashFQ in cacheDict:
            result = cacheDict[hashFQ]
        else:
            result = fun(*args, **kwargs)
            cacheDict[hashFQ] = result
        return result
    return wrapper


