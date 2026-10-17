"""cache invariant bases as dicts of blocks"""
import os, pickle
from invspace import *
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bases.pkl')
SPECS = {
    'X_r1':        dict(S='r1', imag=True, with_inv=True),            # the claimed 9-dim space
    'X_r1_noI':    dict(S='r1', imag=True, with_inv=False),
    'R_r1_OI':     dict(S='r1', imag=False, with_inv=True),
    'R_r1_O':      dict(S='r1', imag=False, with_inv=False),
}
for S in ('onsite', 'r1', 'l1<=2', 'cube'):
    for imag in (False, True):
        for a2 in (0, 1):
            SPECS[f'Q_{S}_{"im" if imag else "re"}_{"A2" if a2 else "A1"}'] = dict(S=S, stag=True, imag=imag, chiA2=a2, with_inv=False)
    for imag in (False, True):
        SPECS[f'P0_{S}_{"im" if imag else "re"}_O'] = dict(S=S, imag=imag, with_inv=False)
def get(name):
    db = pickle.load(open(CACHE, 'rb')) if os.path.exists(CACHE) else {}
    if name not in db:
        sp = dict(SPECS[name]); S = sp.pop('S')
        idx, b = invariant_basis(shifts(S), **sp)
        db[name] = [to_blocks(idx, v, imag=sp.get('imag', False)) for v in b]
        pickle.dump(db, open(CACHE, 'wb'))
    return db[name]
if __name__ == '__main__':
    for n in SPECS: print(n, len(get(n)))
