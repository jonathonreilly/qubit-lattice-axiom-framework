"""TOR-1 (b1) un-fixed Ward test: log rho with the transverse endpoint A^T + d(omega) (no canonicalisation of that piece) minus the
canonical value, for Ns = 4, 8, 16 and s_k = -1, +1.  usage: python3 tor1_ward.py Lx Lt"""
import sys, time
import numpy as np
from tor1_lib import *
Lx, Lt = int(sys.argv[1]), int(sys.argv[2]); S = Torus(Lx, Lt); rng = np.random.default_rng(7101); t0 = time.time()
A = []
while len(A) < 3:
    th = rng.normal(0, 0.12, S.nl) + rng.uniform(0, 2*np.pi) * S.Ux + rng.uniform(0, 2*np.pi) * S.Ut
    Fr = (th @ S.Pm.T + np.pi) % (2*np.pi) - np.pi
    if np.abs(Fr).max() < 0.55 and abs(round(Fr.sum()/(2*np.pi))) == 0: A.append(th)
A = np.array(A)
om_small = rng.uniform(-0.3, 0.3, (3, S.ns)); om_big = rng.uniform(-np.pi, np.pi, (3, S.ns))
dsm = om_small[:, S.frm] - om_small[:, S.to]; dbg = om_big[:, S.frm] - om_big[:, S.to]
print(f"# TOR-1 Ward Lx={Lx} Lt={Lt}: Delta = log rho(A^T + d omega) - log rho(A^T) (phase mod 2pi, modulus); 3 fields", flush=True)
for sk in (-1, +1):
    for Ns in (4, 8, 16):
        M = TorusMeasure(S, '11112', Ns=Ns, sk=sk, ntor=192, nloop=256) if (Ns == 4 or True) else None
        W = M.logrho(A)
        for nm, d in (('small', dsm), ('big', dbg)):
            Wd = M.logrho(A, dAT=d); ph = np.angle(np.exp(1j * (Wd.imag - W.imag)))
            print(f"s_k={sk:+d} Ns={Ns:2d} omega={nm:5s}: max|dphase| {np.abs(ph).max():.3e}  max|dmod| {np.abs(Wd.real - W.real).max():.3e}  [{time.time()-t0:.0f}s]", flush=True)
