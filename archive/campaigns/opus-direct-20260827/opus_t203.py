"""
T203 - convergence RATE of the conformal-channel lattice error against the
exact continuum reference (T202).  Fits  |Rlat - Rcont| ~ C * L^{-p}  at fixed
x = s kappa^2, for the plain and Symanzik-improved operators.

Expectation if the channel is healthy:  p = 2 (plain), p = 4 (improved).
"""
import numpy as np, sys, time
from opus_t200 import heat, K2, qspec
from opus_t202 import cont_K2

n_mode = 2
xs = np.array([0.4, 0.6, 0.8, 1.0, 1.4, 2.0])
Ls = [int(a) for a in sys.argv[1:]] or [32, 48, 64, 96]
J = 22

# continuum reference is L-independent (verified in T202); compute once on a
# reference L and reuse the x-grid.
Lref = 32
kref = 2*np.pi*n_mode/Lref
c2, _ = cont_K2(Lref, n_mode, xs/kref**2, 0.05, J)
Rcont = (4*np.pi*(xs/kref**2))**2 * c2 / (Lref**4/2.0)
print("x      : " + " ".join(f"{q:10.3f}" for q in xs))
print("Rcont  : " + " ".join(f"{q:10.5f}" for q in Rcont))

err = {True: {}, False: {}}
for L in Ls:
    t0 = time.time(); kap = 2*np.pi*n_mode/L; sv = xs/kap**2; QC = qspec(L)
    for imp in (True, False):
        lk2, _ = K2(L, kap, sv, 0.05, imp, QC)
        R = (4*np.pi*sv)**2*lk2/(L**4/2.0)
        err[imp][L] = R - Rcont
        print(f"L={L:3d} {'IMPR ' if imp else 'plain'} err: "
              + " ".join(f"{q:10.3e}" for q in err[imp][L]))
    print(f"        [{time.time()-t0:.1f}s]")

print("\nfitted exponent p in |err| ~ L^-p   (log-log LSQ over all L)")
lg = np.log(np.array(Ls, float))
for imp in (True, False):
    E = np.array([err[imp][L] for L in Ls])
    ps = []
    for i in range(len(xs)):
        y = np.abs(E[:, i])
        if np.any(y <= 0): ps.append(np.nan); continue
        p = -np.polyfit(lg, np.log(y), 1)[0]
        ps.append(p)
    print(f"  {'IMPROVED' if imp else 'plain   '}: " + " ".join(f"{q:10.3f}" for q in ps))
    if len(Ls) >= 2:
        for a, b in zip(Ls[:-1], Ls[1:]):
            r = err[imp][a]/err[imp][b]
            print(f"    ratio L={a}->{b} (a^2 pred {(b/a)**2:.2f}, a^4 pred {(b/a)**4:.2f}): "
                  + " ".join(f"{q:8.2f}" for q in r))
