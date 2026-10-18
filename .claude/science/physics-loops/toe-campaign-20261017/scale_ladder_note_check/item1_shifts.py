"""Item 1: derive s_R from the PSG gauge-sign commutator with translations, not from Bloch overlaps."""
import itertools
import numpy as np
from common import *

E = [(1,0,0),(0,1,0),(0,0,1)]
SR = []
for r, R in enumerate(ROTS):
    P, s = ROT[r]
    a = []
    for t in E:
        Pt, _ = TR[t]
        chi = s ^ s[Pt]            # sigma_R(q) sigma_R(q+t)
        vals = set(chi.tolist()); assert len(vals) == 1, (r, t, vals)
        a.append(vals.pop())
    # cross-check via operator identity M_R T_t M_R^-1 = chi T_{Rt}
    for t, at in zip(E, a):
        Rt = tuple(int(x) % L for x in R @ np.array(t))
        X = compose(compose(ROT[r], TR[t]), inverse(ROT[r]))
        Y = compose(X, inverse(TR[Rt]))
        assert const_sign(Y) == (-1) ** at
    sR = tuple(int(x) % 2 for x in (R @ np.array(a)))
    SR.append(sR)
print("shift vectors s_R per rotation (trace, w1, s_R):")
for R, w, sR in zip(ROTS, W1, SR): print("  tr", int(np.trace(R)), "w1", w, "s_R", sR)
print("distinct shift classes:", sorted(set(SR)), "count", len(set(SR)))

# verify with Bloch states: M_R B(k) spans B(Rk + pi s_R)
ok = True
for r, R in enumerate(ROTS):
    Mr = dense(ROT[r])
    for n in [(0,0,0),(1,-1,1),(1,2,3),(2,0,1)]:
        k = np.array(n) * np.pi / 2; kp = R @ k + np.pi * np.array(SR[r])
        A = Bloch(kp).conj().T @ Mr @ Bloch(k)
        ok &= np.allclose(A.conj().T @ A, np.eye(12))
print("Bloch cross-check M_R B(k) = B(Rk + pi s_R) U:", ok)

def fixed(N, shifts):
    out = []
    for n in itertools.product(range(2 * N), repeat=3):
        k = np.array(n) * np.pi / N
        if all(np.allclose(np.exp(1j * (R @ k + np.pi * np.array(sR) - k)), 1) for R, sR in zip(ROTS, shifts)):
            out.append(tuple(np.round(((k + np.pi) % (2 * np.pi) - np.pi) / np.pi, 4)))
    return out
print("fixed momenta (units of pi), L=4 grid (N=2):", fixed(2, SR))
print("fixed momenta with all s_R = 0, N=2:", fixed(2, [(0,0,0)] * 24))
for N in (4, 6, 12):
    print(f"same affine action on finer grid pi/{N}:", fixed(N, SR), "| linear:", fixed(N, [(0,0,0)] * 24))
