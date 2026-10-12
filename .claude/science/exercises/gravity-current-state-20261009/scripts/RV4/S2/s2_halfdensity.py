"""S2 (3): half-density / sqrt(J)-compensated couplings and the bulk-isospectral counterterm, NN KG scalar, p = sin k.
Family A (Weyl-type weight):  omega_c(q) = [omega * J^-c](Phi^-1 q)     (c=0 flow, c=1/2 half-density, c=1 density)
     mu(c) = <e J^{1-c}''> = (1-c)[ <e J2> - c <e D^2> ],  D = div v, J2 = div(v D), e = omega/2.
     Its O(eps) term changes the linear stress coupling T1 by -c D omega  (E channel; T2 separable has D=0).
Family B (bulk unitarity at O(eps^2), T1 untouched):  Omega~(q) = Omega(Phi^-1 q) + eps^2 G2(q),
     G2 = 1/2 (grad Omega . v) D   [trig polynomial, M-independent]  => every DOS moment kept at O(eps^2) => mu = 0.
Checks: analytic formulas vs brute-force RK4 flow (+ Jacobian transported along the flow) and finite differences."""
import numpy as np
from s2_core import *

def hess_fd(E, de=0.02):
    v = {e: E(e) for e in [-de, -de/2, 0, de/2, de]}
    Dd = lambda e: (v[e]+v[-e]-2*v[0])/e**2
    return (4*Dd(de/2)-Dd(de))/3

def vel(ch, K):
    """v = 1/2 hhat sin k and div v for the NN symbol; works for 2D/3D."""
    s = [np.sin(k) for k in K]; c = [np.cos(k) for k in K]; z = np.zeros_like(K[0])
    if ch == 'E':  V = [0.5*s[0], -0.5*s[1]] + [z]*(len(K)-2); D = 0.5*(c[0]-c[1])
    if ch == 'T2': V = [0.5*s[1], 0.5*s[0]] + [z]*(len(K)-2); D = 0*z
    if ch == 'tr': V = [0.5*x for x in s]; D = 0.5*sum(c)
    return V, D

def flow_back(Q, ch, eps, n=40):
    """x(eps) = Phi_eps^{-1}(q) by RK4 on xdot = -v(x); also lnJ = int div v along it (so J(Phi^-1 q) = e^{lnJ})."""
    x = [q.copy() for q in Q]; lnJ = np.zeros_like(Q[0]); h = eps/n
    def f(x):
        V, D = vel(ch, x); return [-vv for vv in V], D
    for _ in range(n):
        k1, d1 = f(x); x2 = [a+h/2*b for a, b in zip(x, k1)]
        k2, d2 = f(x2); x3 = [a+h/2*b for a, b in zip(x, k2)]
        k3, d3 = f(x3); x4 = [a+h*b for a, b in zip(x, k3)]
        k4, d4 = f(x4)
        x = [a + h/6*(b1+2*b2+2*b3+b4) for a, b1, b2, b3, b4 in zip(x, k1, k2, k3, k4)]
        lnJ += h/6*(d1+2*d2+2*d3+d4)
    return x, lnJ

def Omega(K, M): return M*M + sum(4*np.sin(k/2)**2 for k in K)

for d, L in [(2, 128), (3, 40)]:
    K = grid(d, L)
    print(f"\n======== d={d}, L={L} (midpoint; brute force RK4 n=40, 5-point Richardson FD) ========")
    for M in [1.0, 0.3]:
        w = np.sqrt(Omega(K, M)); e = 0.5*w; gradO = [2*np.sin(k) for k in K]
        for ch in ['E', 'T2', 'tr']:
            V, D = vel(ch, K)
            # J2 = div(v D): use identity <e J2> = -<grad e . v D>
            ge_v = sum((g/(4*w))*vv for g, vv in zip(gradO, V))     # grad(omega/2).v = grad Omega . v /(4 omega)
            mu0 = -np.mean(ge_v*D); eD2 = np.mean(e*D*D)
            muA = lambda c: (1-c)*(mu0 - c*eD2)
            cstar = mu0/eD2 if eD2 > 0 else np.nan
            G2 = 0.5*sum(g*vv for g, vv in zip(gradO, V))*D
            muB = mu0 + np.mean(G2/(2*w))*1.0      # d2/de2 of 1/2 sqrt(Omega+eps^2 G2) = G2/(2 omega)
            # brute force
            def E_A(eps, c):
                x, lnJ = flow_back(K, ch, eps); return np.mean(0.5*np.sqrt(Omega(x, M))*np.exp(-c*lnJ))
            def E_B(eps):
                x, lnJ = flow_back(K, ch, eps); return np.mean(0.5*np.sqrt(Omega(x, M) + eps*eps*G2))
            bf0 = hess_fd(lambda s: E_A(s, 0.0)); bfh = hess_fd(lambda s: E_A(s, 0.5)); bf1 = hess_fd(lambda s: E_A(s, 1.0)); bfB = hess_fd(E_B)
            print(f" M={M} {ch:2s}: flow mu0={mu0:+.6e} [bf {bf0:+.6e}] | half-density c=1/2: {muA(0.5):+.6e} [bf {bfh:+.6e}] | c=1: {muA(1.0):+.1e} [bf {bf1:+.1e}]"
                  f" | c*={cstar:+.5f} | isospectral G2: {muB:+.1e} [bf {bfB:+.1e}]")
            if ch == 'E':
                # DOS moments: <Omega~^n>_q - <Omega^n>_k, flow vs flow+G2, at eps=0.02 and 0.01 (scaling)
                for eps in [0.02, 0.01]:
                    x, lnJ = flow_back(K, ch, eps); Of = Omega(x, M); Ob = Of + eps*eps*G2; O0 = Omega(K, M)
                    dm_f = [np.mean(Of**n) - np.mean(O0**n) for n in (1, 2, 3, 4)]
                    dm_b = [np.mean(Ob**n) - np.mean(O0**n) for n in (1, 2, 3, 4)]
                    print(f"      eps={eps}: DOS moment shifts n=1..4  flow: " + " ".join(f"{z/eps**2:+.3e}" for z in dm_f) +
                          "  (/eps^2) | flow+G2: " + " ".join(f"{z/eps**3:+.3e}" for z in dm_b) + " (/eps^3)")
    # first-order coupling change of family A (stress defect): symbol -c D omega ; size relative to T1 symbol v.grad omega
    M = 1.0; w = np.sqrt(Omega(K, M)); V, D = vel('E', K)
    T1 = sum((2*np.sin(k)/(2*w))*vv for k, vv in zip(K, V))
    print(f" family A first-order stress change (E, M=1): rms(D*omega)/rms(T1 symbol) = {np.sqrt(np.mean((D*w)**2))/np.sqrt(np.mean(T1**2)):.3f}  (c=1; times c)")
