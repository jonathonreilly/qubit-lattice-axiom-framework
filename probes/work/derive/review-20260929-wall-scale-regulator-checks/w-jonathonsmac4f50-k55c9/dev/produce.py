import sys, json, time, numpy as np
from engine import *

SPECS = {
 'q44':      dict(dims=(4,4,4,4), Ns=0, m=0.1, nq=0,   ntherm=200, nmeas=4000, nmd=10, seed=11),
 'f44_m01':  dict(dims=(4,4,4,4), Ns=1, m=0.1, nq=100, ntherm=120, nmeas=1500, nmd=10, seed=21),
 'f44_ns2':  dict(dims=(4,4,4,4), Ns=2, m=0.1, nq=100, ntherm=120, nmeas=1000, nmd=12, seed=31),
 'f44_m05':  dict(dims=(4,4,4,4), Ns=1, m=0.5, nq=100, ntherm=80,  nmeas=1500, nmd=10, seed=41),
 'q66':      dict(dims=(6,6,6,6), Ns=0, m=0.1, nq=0,   ntherm=200, nmeas=1500, nmd=10, seed=51),
 'f66_m01':  dict(dims=(6,6,6,6), Ns=1, m=0.1, nq=100, ntherm=80,  nmeas=400, nmd=12, seed=61),
}

def run(name, nmeas_override=None, log=None):
    sp = SPECS[name]
    lat = Lat(sp['dims'])
    if sp['nq'] > 0:
        # quenched warm start with the same seed stream
        hq = HMC(lat, 6.0, Ns=0, nmd=10, tau=1.0, seed=sp['seed'])
        for _ in range(sp['nq']):
            hq.trajectory(thermal=True)
        h = HMC(lat, 6.0, Ns=sp['Ns'], m=sp['m'], nmd=sp['nmd'], tau=1.0, seed=sp['seed'] + 1000)
        h.U = hq.U.copy()
    else:
        h = HMC(lat, 6.0, Ns=sp['Ns'], m=sp['m'], nmd=sp['nmd'], tau=1.0, seed=sp['seed'])
    for k in range(sp['ntherm']):
        h.trajectory(thermal=(k < sp['ntherm'] // 2))
    h.nacc = 0; h.dH = []; h.ntraj = 0
    n = sp['nmeas'] if nmeas_override is None else nmeas_override
    P = []; dHs = []; acc = []
    t0 = time.time()
    for k in range(n):
        a, d = h.trajectory()
        P.append(h.g.plaq(h.U)); dHs.append(d); acc.append(int(a))
        if log and (k + 1) % 50 == 0:
            print(name, k + 1, 'of', n, 'elapsed', round(time.time() - t0, 1), 'meanP', np.mean(P), 'acc', np.mean(acc), flush=True)
    return dict(spec={k: (list(v) if isinstance(v, tuple) else v) for k, v in sp.items()}, P=P, dH=dHs, acc=acc,
                cg_iters=(h.f.cg_iters if h.f else 0), seconds=time.time() - t0)

if __name__ == '__main__':
    name = sys.argv[1]
    out = run(name, log=True)
    json.dump(out, open(f'ens_{name}.json', 'w'))
    print('done', name, flush=True)
