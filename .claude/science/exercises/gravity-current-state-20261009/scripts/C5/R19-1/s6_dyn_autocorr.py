"""R19-1 s6 (added after the main runs; NOT the literal registered H): time autocorrelation of the TT/V/S modes under
R18-1's random-sequential Metropolis dynamics (rates min(1, e^{-bU Delta}) per move per sweep). This is another reversible
local generator in the RK class (its RK Hamiltonian has hopping -t e^{-bU|Delta|/2}); Lemma 1 maps its relaxation
spectrum to that Hamiltonian's spectrum. Purpose: look at the exact (finite-L) relaxation of each channel beyond the SMA:
is the decay rate k-independent (flat band) or does it vanish as k -> 0? Usage: python3 s6_dyn_autocorr.py L bU nsweep seed"""
import numpy as np, sys
sys.path.insert(0, '.')
from mc import *
L, bU, NS, seed = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
V = L**3; S, GE, GN = move_tables(L)
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L)
sweeps(n, g, L, 0.0, S, GE, GN, 50, seed + 7, 1); sweeps(n, g, L, bU, S, GE, GN, 20000 if bU < 2.5 else 60000, seed + 11, 0)
kd = kgrid_dirs(L); klist = []
for name, lst in kd.items():
    for m, vecs in lst:
        if m > 2: continue
        for v in vecs: klist.append((name, m, v))
K = np.array([2*np.pi*np.array(v)/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist]); ph = np.exp(-1j*(K @ OFFS.T))
pols = [channel_pols(np.array(v, float)) for _, _, v in klist]
chs = ["TT1", "TT2", "V1", "V2", "S1"]
C = np.array([[cvec(p[c[:-1]][int(c[-1]) - 1]) for c in chs] for p in pols])     # (nk, 5, 6)
ser = np.zeros((NS, len(klist), 5), complex)
for it in range(NS):
    sweeps(n, g, L, bU, S, GE, GN, 1, seed*100003 + it, it % 2)
    F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T * ph    # (nk, 6)
    ser[it] = np.einsum('kcs,ks->kc', C, F)/np.sqrt(V)
T = 40
def acf(x):
    x = x - x.mean(); f = np.fft.fft(x, 2*len(x)); a = np.fft.ifft(f*np.conj(f))[:T].real/np.arange(len(x), len(x) - T, -1)
    return a
out = {}
for ik, (name, m, v) in enumerate(klist):
    for ic, c in enumerate(chs):
        out.setdefault((name, m, c), []).append(acf(ser[:, ik, ic]))
print("L=%d bU=%.1f nsweep=%d seed=%d ; E/edge=%.5f ; time unit = 1 sweep (each move proposed once on average)" % (L, bU, NS, seed, (g**2).sum()/4/(3*V)))
print("rate Gamma = -d ln C/dtau fitted on tau in [1,6] ; C(1)/C(0) ; C(5)/C(0)")
for key in sorted(out):
    a = np.mean(out[key], 0); r = a/a[0]
    tt = np.arange(1, 7); ok = r[1:7] > 0.02
    gam = -np.polyfit(tt[ok], np.log(r[1:7][ok]), 1)[0] if ok.sum() >= 3 else np.nan
    print("  %-4s m=%d %-3s S=%.4f  Gamma=%.4f  C1/C0=%.4f  C5/C0=%.4f  C10/C0=%.4f" % (key[0], key[1], key[2], a[0], gam, r[1], r[5], r[10]))
