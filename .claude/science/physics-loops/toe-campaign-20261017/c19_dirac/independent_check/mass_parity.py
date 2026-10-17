"""Inversion parity of the imaginary A2 staggered on-site mass space and which parity gives the mass."""
import numpy as np
from core import *
from bases import get
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
eI, sI = PSGI
D = [(1j ** w) * W for w, W in zip(W1, WR)]; Lf = lift(D)[0]
def iso(ch):
    P = sum(np.conj(ch[g]) * Lf[g] for g in range(48)) * 2 / 48; e, V = np.linalg.eigh((P + P.conj().T) / 2); return V[:, e > 0.5]
V12, V52 = iso(CH12), iso(CH52)
bs = get('Q_onsite_im_A2'); n = len(bs)
vec = lambda m: m[(0, 0, 0)].ravel()
B = np.array([vec(m) for m in bs]).T                      # 144 x 5
IB = np.array([vec(act(INV, eI, sI, m)) for m in bs]).T
C = np.linalg.lstsq(B, IB, rcond=None)[0]                  # inversion as 5x5 on the space
w, Z = np.linalg.eig(C); print("inversion eigenvalues on the 5-dim mass space:", np.round(w.real, 6))
for par in (1, -1):
    sel = Z[:, np.abs(w - par) < 1e-6]
    cps = []
    for j in range(sel.shape[1]):
        m0 = (B @ sel[:, j]).reshape(12, 12)
        cps.append(np.abs(V52.conj().T @ m0 @ V12).max())
    print(f"  inversion {'even' if par > 0 else 'odd '} subspace dim {sel.shape[1]}: max node coupling per element {np.round(cps, 5)}")
# relative phase of the node coupling between I-even and I-odd masses
ev = Z[:, np.abs(w - 1) < 1e-6]; od = Z[:, np.abs(w + 1) < 1e-6]
blk = lambda col: V52.conj().T @ (B @ col).reshape(12, 12) @ V12
b0 = blk(ev[:, 0]); ratios = []
for col in list(ev.T) + list(od.T):
    b = blk(col); r = np.vdot(b0.ravel(), b.ravel()) / np.vdot(b0.ravel(), b0.ravel())
    ratios.append((np.round(r, 5), np.allclose(b, r * b0)))
print("  node block of each element relative to the first I-even one (ratio, proportional?):", ratios)
