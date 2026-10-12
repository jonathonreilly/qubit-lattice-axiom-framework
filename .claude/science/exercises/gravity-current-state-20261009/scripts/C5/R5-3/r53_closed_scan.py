"""R5-3: closed-FRW sequestering toy scan. For every self-consistent (s,k,C*) history:
the best 'today' candidate on the expanding branch (the epoch of minimum Omega_m), and the
inequality Omega_k0 >= <adot^2>_a / adot0^2 (from <R>=0: k int a dt = int a adot^2 dt - [a^3 H])."""
import numpy as np
from scipy.optimize import brentq
src = open('r53_sequester.py').read().split('def fixed_points')[0]
exec(src)

def roots_for(s, k, Cs):
    g = lambda C: F(s, C, k=k)[0] - C
    v = np.array([g(C) for C in Cs])
    out = []
    for j in range(len(Cs) - 1):
        if np.isfinite(v[j]) and np.isfinite(v[j+1]) and v[j]*v[j+1] < 0:
            out.append(brentq(g, Cs[j], Cs[j+1], xtol=1e-10))
    return out

print("s | k | C* | min Omega_m (expanding) | Omega_k there | q there | H t there | identity: k vs <adot^2>_a + |bnd|/int a")
best = []
for s in [0.25, 0.5, 1.0, 2.0, 4.0, 8.0]:
    for k in [0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0, 5.0]:
        try:
            rts = roots_for(s, k, np.linspace(-5, 80, 86))
        except Exception as e:
            print(f"{s} | {k} | error {e}"); continue
        for Cst in rts:
            sol, _ = run(s, Cst, dense=True, k=k)
            t = np.linspace(sol.t[0], sol.t[-1], 200001)
            a, ad, ph, phd = sol.sol(t)[:4]
            H = ad/a
            rho_m = A/a**3
            Om = rho_m/(3*H**2)
            Omk = -k/(a*H)**2
            q = -(np.gradient(ad, t))*a/ad**2
            m = (H > 0) & (t > 2*sol.t[0])
            j = np.argmin(np.where(m, Om, np.inf))
            Ia = np.trapezoid(a, t); Iad = np.trapezoid(a*ad**2, t)
            bnd = a[-1]**3*H[-1] - a[0]**3*H[0]
            print(f"{s} | {k} | {Cst:.4f} | {Om[j]:.4f} | {Omk[j]:+.4f} | {q[j]:+.3f} | {H[j]*t[j]:.3f} | k={k:.4f} vs {(Iad - bnd)/Ia:.4f} ; <adot^2>_a/adot_j^2 = {Iad/Ia/ad[j]**2:.4f}")
            best.append((Om[j], Omk[j], s, k, Cst))
if best:
    b = min(best, key=lambda x: x[0])
    print(f"\nlowest Omega_m reached on the expanding branch by any self-consistent history: {b[0]:.4f} (Omega_k={b[1]:+.4f}) at s={b[2]}, k={b[3]}")
