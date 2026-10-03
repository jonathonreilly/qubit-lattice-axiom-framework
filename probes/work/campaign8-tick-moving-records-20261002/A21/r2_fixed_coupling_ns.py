"""A21 re-check 2: is 'pace set by the shared possibilities' always signalling?
Same 4-qubit toy as A15 ns_eventpaced.py (b distant; a1,a2,a3 local; A9 linear instrument at a1; a3 recorded in Z).
Rules:
  ANGLE (A15): gate angle on (a2,a3) = th * weight(1) at a1, computed from the branch state (a nonlinear dial)
  CTRL  (new): fixed unitary exp(-i th |1><1|_{a1} (x) SWAP_{a2a3}) applied before a1's formation step:
               the possibility at a1 sets the pace on (a2,a3) coherently, through fixed dynamics.
Reports max TV of local record odds between distant conditions (none / Z / X at b)."""
import os, signal
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from scipy.linalg import expm
I2 = np.eye(2)
SW = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], complex)
def kron(*ops):
    out = np.array([[1.0+0j]])
    for o in ops: out = np.kron(out, o)
    return out
def on(op, site, n=4):
    ops = [I2]*n; ops[site] = op; return kron(*ops)
P = [np.diag([1.0,0.0]), np.diag([0.0,1.0])]
Hx = np.array([[1,1],[1,-1]])/np.sqrt(2); PX = [Hx@p@Hx for p in P]
F = np.diag([0.3,0.8]); sF = np.sqrt(F); s1F = np.sqrt(np.eye(2)-F)
def local_stats(rho, rule, th):
    out = {}
    if rule == 'CTRL':
        U = expm(-1j*th*kron(I2, P[1], SW))      # fixed, state-independent unitary on b(x)a1(x)a2a3
        rho = U @ rho @ U.conj().T
    R = rho.reshape(2,2,4,2,2,4); ra1 = np.einsum('xiyxjy->ij', R); p1 = float(np.real(ra1[1,1]))
    branches = [(('none',None), on(s1F,1))] + [(('form',k), on(sF@P[k]@sF,1)) for k in (0,1)]
    for key, K in branches:
        r1 = K @ rho @ K.conj().T
        if rule == 'ANGLE':
            G = kron(I2, I2, expm(-1j*th*p1*SW)); r1 = G @ r1 @ G.conj().T
        for m in (0,1):
            M = on(P[m],3); out[(key,m)] = out.get((key,m),0.0) + float(np.real(np.trace(M@r1@M)))
    return out
def distant(rho, cond):
    if cond == 'none': return [rho]
    proj = P if cond == 'Z' else PX
    return [on(proj[k],0) @ rho @ on(proj[k],0) for k in (0,1)]
rng = np.random.default_rng(20261003)
worst = {'ANGLE':0.0, 'CTRL':0.0}
for trial in range(200):
    v = rng.normal(size=16)+1j*rng.normal(size=16); v /= np.linalg.norm(v); rho = np.outer(v, v.conj())
    th = rng.uniform(0.2, 1.4)
    for rule in worst:
        stats = {}
        for cond in ('none','Z','X'):
            agg = {}
            for br in distant(rho, cond):
                w = np.real(np.trace(br)); st = local_stats(br/w, rule, th)
                for k2, val in st.items(): agg[k2] = agg.get(k2,0.0) + w*val
            stats[cond] = agg
        keys = set().union(*[set(s) for s in stats.values()])
        for c1 in ('Z','X'):
            tv = 0.5*sum(abs(stats[c1].get(k,0)-stats['none'].get(k,0)) for k in keys)
            worst[rule] = max(worst[rule], tv)
for rule, tv in worst.items():
    print("rule %-5s: max TV of local record odds between distant conditions (200 snapshots) = %.3e" % (rule, tv))
