"""Write one pickle per feasible twisted-pair branch from spinj_exact.py's output (run in its directory)."""
import pickle, sympy as sp
d = pickle.load(open('spinj_E12+E52.pkl', 'rb')); eqs, unk, feas = d['eqs'], d['unk'], d['feas']
for bi, (m, p, sol) in enumerate(feas):
    sub = dict(zip(unk, sol)); free = sorted(set().union(*[sp.sympify(v).free_symbols for v in sol]), key=str)
    red = sorted(set(e for e in (sp.expand(e.subs(sub)) for e in eqs) if e != 0), key=str)
    pickle.dump({'free': free, 'red': red, 'sub': sub, 'branch': m}, open(f'tw/branch{bi}.pkl', 'wb'))
    print(bi, m, len(free), len(red), flush=True)
