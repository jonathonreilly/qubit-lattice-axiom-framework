"""(a) Generic invertibility of the Born O(e^2) Moller T-matrix on the degenerate + band (taste x spin), d=2,3 (and d=1 control).
(b) Trace reduction: if T invertible, f(k)=tr_+ P(k)/n+ obeys the scalar collision equation.  Odd scalar null space,
    basis sin(2 n.k), |n|_inf <= R, on Moller shells (generic, lowK, lowE, near-O(e)-pole); abs+rel tolerance; sv gaps.
usage: python s2_moller.py d m R ns"""
import sys, time, numpy as np
from s2_core import *
d = int(sys.argv[1]); m = float(sys.argv[2]); R = int(sys.argv[3]); ns = int(sys.argv[4])
rng = np.random.default_rng(7 + d)
S = Stag(d, m); t0 = time.time()
samp = []
for mode, frac in (('generic', 0.5), ('lowK', 0.25), ('lowE', 0.25)):
    s = sample_moller(S, int(ns*frac), rng, mode=mode); samp += [(mode,) + q for q in s]
print(f"d={d} m={m}: {len(samp)} Moller shells sampled ({time.time()-t0:.1f}s)", flush=True)
ratios = []; near = 0; rows = []; ratios_by = {}
B = odd_basis(d, R)
for (mode, k1, k2, k3, k4) in samp:
    T, U, md = moller_T(S, k1, k2, k3, k4, return_parts=True)
    sv = np.linalg.svd(T, compute_uv=False)
    r = sv[-1]/sv[0]; ratios.append(r); ratios_by.setdefault(mode, []).append(r)
    if md < 0.05: near += 1
    E = eps(k1, m)+eps(k2, m)-eps(k3, m)-eps(k4, m); assert abs(E) < 1e-12
    row = np.sin(2*B@k1) + np.sin(2*B@k2) - np.sin(2*B@k3) - np.sin(2*B@k4)
    rows.append(row)
ratios = np.array(ratios)
print(f"T is {T.shape[0]}x{T.shape[1]} on the + band; min-sv/max-sv: min {ratios.min():.2e}, 1st pct {np.percentile(ratios,1):.2e}, median {np.median(ratios):.2e}; samples near an O(e) pole (|w^2-D^2|/w^2<0.05): {near}")
for k_, v in ratios_by.items(): print(f"   {k_:8s}: n={len(v)} min ratio {np.min(v):.2e} median {np.median(v):.2e}")
A = np.array(rows); A /= np.sqrt(len(A))
for Rr in range(1, R+1):
    cols = np.nonzero(np.max(np.abs(B), axis=1) <= Rr)[0]
    sv = np.linalg.svd(A[:, cols], compute_uv=False)
    print(f"  scalar odd f, R={Rr}: {len(cols)} functions, null dim {nullity(sv, len(cols))} (abs 1e-10 + rel 1e-9); sv min {sv[-1]:.3e} max {sv[0]:.3e} ratio {sv[-1]/sv[0]:.3e}", flush=True)
print(f"time {time.time()-t0:.1f}s")
