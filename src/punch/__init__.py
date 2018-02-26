from munch import Munch

def punch_it(d):
    if not isinstance(d, dict):
        return d

    dd = {k: punch_it(v) for k, v in d.items()}
    return Munch(dd)


it = punch_it
