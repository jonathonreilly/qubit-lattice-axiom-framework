"""R13-4 (i): constants of the BF O'Neill pair-transfer tail.
(a) G(r) = (Delta^{-1})_{0,r e_x} for the cubic-lattice graph Laplacian (cochain d0^T d0), via
    G(r) = int_0^inf e^{-6t} I_r(2t) I_0(2t)^2 dt (exponentially scaled Bessels); 4 pi r G(r) -> 1.
    Tail subtraction (named before the run): none; compared with the continuum 1/(4 pi r).
(b) Mean-field screened version (reading only): uniform e^2 v^2 added to Delta.
(c) v^2 = <|phi_s|^2> in the free matter vacuum, 16 real bosons with R8-5/R10-5 Wilson-box E(k):
    <phi_a^2> = int d^3k/(2pi)^3 1/(2E(k)) per real component (unit-mass oscillators).
"""
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

def G(r, mu2=0.0):
    f = lambda t: np.exp(-mu2*t)*ive(r, 2*t)*ive(0, 2*t)**2   # e^{-6t} I_r I_0^2 = ive*ive*ive (e^{-2t} each)
    v1, _ = quad(f, 0, 50, limit=400)
    v2, _ = quad(f, 50, np.inf, limit=400)
    return v1 + v2

out = []
def pr(*a):
    s_ = " ".join(str(x) for x in a); print(s_, flush=True); out.append(s_)

pr("(a) lattice Coulomb kernel G(r) on the axis; 4 pi r G(r)")
for r in [1, 2, 4, 8, 16, 32, 64]:
    g = G(r); pr(f"   r={r:3d}: G={g:.6e}  4 pi r G = {4*np.pi*r*g:.5f}")
pr(f"   G(0) = {G(0):.6f}  (Watson: 0.252731)")

e = np.sqrt(4*np.pi/137.036)
pr(f"\n(b) mean-field screening (reading): e = {e:.4f}")
def Ewilson(k, m=0.3, b1=2.0, b2=3.0, rr=1.0):
    def sstep(x):
        x = np.clip(x, 0, 1)
        with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
            e1 = np.where(x > 0, np.exp(-1/np.where(x > 0, x, 1)), 0.0)
            e2 = np.where(x < 1, np.exp(-1/np.where(x < 1, 1-x, 1)), 0.0)
        return e1/(e1+e2)
    rho = 1 - sstep((np.abs(k) - b1)/(b2 - b1))
    S = rho*k + (1-rho)*np.sin(k); W = rr*(1-rho)*(1-np.cos(k))
    return S, W
N = 96
k = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
for (m, b1, b2) in [(0.3, 2.0, 3.0), (0.1, 2.0, 3.0), (0.3, 0.8, 2.0)]:
    S, W = Ewilson(k, m, b1, b2)
    Mw = m + W[:, None, None] + W[None, :, None] + W[None, None, :]
    E = np.sqrt(Mw**2 + S[:, None, None]**2 + S[None, :, None]**2 + S[None, None, :]**2)
    var1 = np.mean(1/(2*E))
    v2 = 16*var1
    mu = e*np.sqrt(v2)
    pr(f"   Wilson-box matter m={m}, box=({b1},{b2}): <phi_a^2> = {var1:.4f}, v^2 = 16x = {v2:.3f}, "
       f"screening mass e v = {mu:.3f}/a, length {1/mu:.2f} a")
    for r in [4, 16, 32]:
        pr(f"      r={r}: G_screened/G = {G(r, mu**2)/G(r):.3e}")
pr("\n(c) norm of the O'Neill double commutator, ||[[H_q,N_x],N_y]|| = 2 ||X^W dag|0>||^2 G(r) = 56 e^2 G(r):")
for r in [2, 10, 100]:
    pr(f"   r={r}: 56 e^2 G(r) = {56*e*e*G(r):.4e}  (continuum 14 e^2/(pi r) = {14*e*e/(np.pi*r):.4e})")
with open(__file__.replace('.py', '.out'), 'w') as f:
    f.write("\n".join(out) + "\n")
