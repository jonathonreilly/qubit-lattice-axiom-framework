"""B1 (lane RB): 1D boost-like generators K = (1/2){V(k), i d/dk} on one lattice band.
Conventions: i[K, f(k)] = -V f'.  P := V w'  (so i[K,H] = -P),  F := V P'  (i[K,P] = -F).
Checks:
 (a) first moment V = w for lattice KG: F = H(1-(H^2-m^2)/2) exactly (sympy) -> closed nonlinear algebra
 (b) orbit sum rule: int_{orbit} F dH = 0 for ANY smooth V (random even V); F<0 near band top
 (c) Magueijo-Smolin-type V with V(pi)=0: rapidity infinite, H -> w_max (invariant max energy)
 (d) exact (undeformed) Poincare on the band needs V -> infinity at the band edge
 (e) Fock space: [K,P] on 2-particle states is not a function of (H_tot,P_tot) (non-additivity)
 (f) Bojowald-form bookkeeping: P=k (SLAC) gives beta(k)=sin k/k in {H,H}; P=sin k puts cos k in {D,H}
"""
import numpy as np, sympy as sp
np.random.seed(1)
print("=== (a) first-moment boost, 1D lattice KG, exact ===")
k, m = sp.symbols('k m', positive=True)
w = sp.sqrt(m**2 + 2*(1-sp.cos(k)))
V = w
P = sp.simplify(V*sp.diff(w,k))
F = sp.simplify(V*sp.diff(P,k))
H = sp.symbols('H')
target = H*(1-(H**2-m**2)/2)
print("P =", P, "  F =", F)
print("F - H(1-(H^2-m^2)/2) at H=w :", sp.simplify(F - target.subs(H,w)))
print("Casimir C = P^2 - 2*int F dH ; dC along flow:", sp.simplify(sp.diff(P**2,k)*V - 2*F*sp.diff(w,k)*V))

print("\n=== (b) orbit sum rule for random even V (any generator, not first moment) ===")
kk = np.linspace(0, np.pi, 200001)
mm = 0.7
wk = np.sqrt(mm**2 + 2*(1-np.cos(kk)))
dw = np.gradient(wk, kk)
for trial in range(6):
    c = np.random.randn(5)*0.4
    Vk = wk*(1 + sum(c[j]*(1-np.cos((j+1)*kk)) for j in range(5)))**2 / (1+sum(c[j]*(1-np.cos((j+1)*0.0)) for j in range(5)))**2
    Vk = np.abs(Vk) + 1e-3   # even, positive
    Pk = Vk*dw
    Fk = Vk*np.gradient(Pk, kk)
    I = np.trapezoid(Fk*dw, kk)        # int F dH over (0,pi)
    scale = np.trapezoid(np.abs(Fk*dw), kk)
    # F near top vs IR value
    print(f"trial {trial}: int F dH / int|F dH| = {I/scale:+.2e};  F(0)/(V(0)^2 w''(0)) = {Fk[5]/(Vk[5]**2*(1/mm)):.4f};  min F = {Fk.min():+.3f} at k = {kk[Fk.argmin()]:.3f};  F(pi) = {Fk[-3]:+.3f}")

print("\n=== (c) Magueijo-Smolin-type boost: V = w*cos(k/2) (zero at k=pi) ===")
Vms = wk*np.cos(kk/2)
s_of_k = np.concatenate([[0], np.cumsum(0.5*(1/Vms[1:]+1/Vms[:-1])*np.diff(kk))])
for kv in [np.pi/2, 3.0, 3.13, 3.1415]:
    i = np.searchsorted(kk, kv)
    print(f"k={kk[i]:.5f}: rapidity s={s_of_k[i]:.3f}  H={wk[i]:.6f}  (w_max={wk[-1]:.6f})  m*cosh(s)={mm*np.cosh(s_of_k[i]):.3e}")
Pms = Vms*dw; Fms = Vms*np.gradient(Pms,kk)
print("int F dH / int|F dH| =", np.trapezoid(Fms*dw,kk)/np.trapezoid(abs(Fms*dw),kk), "; F<0 for k >", kk[np.argmax(Fms<0)])
print("first-moment rapidity period (V=w) tau = 2*int_0^pi dk/w =", 2*np.trapezoid(1/wk,kk))

print("\n=== (d) exact Poincare along the band: V_exact = sqrt(w^2-m^2)/w' ===")
for kv in [0.5, 2.0, 3.0, 3.1, 3.14]:
    i = np.searchsorted(kk, kv)
    print(f"k={kk[i]:.3f}: V_exact = {np.sqrt(wk[i]**2-mm**2)/dw[i]:.3e}   (w = {wk[i]:.3f})")

print("\n=== (e) Fock space: 2-particle [K,P] is not a function of (H_tot, P_tot) ===")
mm2 = 0.7
def om(q): return np.sqrt(mm2**2 + 2*(1-np.cos(q)))
def Ff(q): return om(q)*np.cos(q)          # one-particle F for V=w, P=sin k
from scipy.optimize import brentq
found = 0
for k1 in np.linspace(0.2, 2.8, 14):
    k2 = -0.4
    Et, Pt = om(k1)+om(k2), np.sin(k1)+np.sin(k2)
    # find another pair (q1,q2) with same E,P: scan q1, solve for q2 from P, check E
    def g(q1):
        s2 = Pt - np.sin(q1)
        if abs(s2) > 1: return np.nan
        best = None
        for q2 in [np.arcsin(s2), np.pi-np.arcsin(s2)]:
            val = om(q1)+om(q2)-Et
            if best is None or abs(val) < abs(best[0]): best = (val, q2)
        return best
    qs = np.linspace(-np.pi, np.pi, 4001)
    vals = []
    for q in qs:
        r = g(q); vals.append(np.nan if (r is np.nan or r is None) else r[0])
    vals = np.array(vals, dtype=float)
    for j in range(len(qs)-1):
        if np.isfinite(vals[j]) and np.isfinite(vals[j+1]) and vals[j]*vals[j+1] < 0:
            q1 = brentq(lambda q: g(q)[0], qs[j], qs[j+1]); q2 = g(q1)[1]
            if min(abs(q1-k1), abs(q1-k2)) > 1e-3 and abs(om(q1)+om(q2)-Et) < 1e-9:
                d = Ff(q1)+Ff(q2) - (Ff(k1)+Ff(k2))
                if found < 5:
                    print(f"(k1,k2)=({k1:.3f},{k2:.3f}) vs ({q1:.3f},{q2:.3f}): dE={om(q1)+om(q2)-Et:.1e} dP={np.sin(q1)+np.sin(q2)-Pt:.1e}  d(sum F)={d:+.4f}")
                found += 1
            break
print("pairs found with equal (H_tot,P_tot) but different sum F:", found)

print("\n=== (f) where the 1D deformation sits ===")
print("local P = sin k : i[K,H] = -P (undeformed {H[1],H[x]});  i[P,K] = H*cos k  -> deformation cos k in {D,H}")
print("SLAC P = k      : i[P,K] = H (undeformed {D,H});  i[K,H] = -beta(k)*P with beta = sin k/k :")
for kv in [0.1, 1.0, 2.0, 3.0, np.pi]:
    print(f"   k={kv:.3f}  beta={np.sin(kv)/kv:+.4f}")
