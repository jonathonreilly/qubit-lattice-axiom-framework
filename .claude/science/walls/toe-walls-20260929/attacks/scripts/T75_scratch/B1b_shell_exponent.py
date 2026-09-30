"""B1b: shell-averaged exterior profile of the stopped ball (simplest bond energy) and the
near-surface exponent of the lapse w = phi^2.  Pre-registration amendment (recorded in report):
the axis-site exponent of B1 is contaminated by the staircase surface, so the coarse-grained
(shell-averaged) profile is used instead.  Free fit  phi(r) = A (r - r0)^(p/2)  over r in [R+1, R+Nfit];
a linear lapse zero would give p = 1, a double zero p = 2."""
import numpy as np, json
from scipy.optimize import least_squares
from B1_stopped_ball import solve

def shell_profile(P, c, rmax):
    L = P.shape[0]; idx = np.arange(L)
    X, Y, Z = np.meshgrid(idx, idx, idx, indexing="ij")
    r = np.sqrt((X-c)**2 + (Y-c)**2 + (Z-c)**2)
    phi = 1 - P
    bins = np.arange(0.25, rmax, 0.5)   # width 0.5 bins
    rc, pm = [], []
    for b in bins:
        m = (r >= b) & (r < b + 0.5)
        if m.sum() > 3: rc.append(r[m].mean()); pm.append(phi[m].mean())
    return np.array(rc), np.array(pm)

out = []
print("shell-averaged fits  phi = A (r-r0)^(p/2),  r in [R+1.5, R+1.5+span]")
print("  R    L  span |   p     r0-R    A   | linear-in-r fit of phi: rms resid | linear-in-r fit of w=phi^2: rms resid")
for (L, R) in [(61, 10), (61, 14), (81, 18), (81, 22)]:
    P, cap, c = solve(L, R)
    rc, pm = shell_profile(P, c, c - 3)
    for span in (4.0, 6.0):
        m = (rc >= R + 1.5) & (rc <= R + 1.5 + span)
        r, f = rc[m], pm[m]
        res = least_squares(lambda q: q[0] * np.clip(r - q[1], 1e-9, None) ** (q[2] / 2) - f,
                            x0=[0.1, R - 0.5, 1.5], bounds=([0, R - 3, 0.2], [10, R + 1.4, 4]))
        A, r0, p = res.x
        # compare straight-line fits
        def lin_rms(y):
            co = np.polyfit(r, y, 1); return np.sqrt(np.mean((np.polyval(co, r) - y) ** 2)) / (y.max() - y.min())
        print(f" {R:3d} {L:4d} {span:4.1f} | {p:5.2f} {r0-R:7.2f} {A:6.3f} |   {lin_rms(f):8.4f}   |   {lin_rms(f**2):8.4f}")
        out.append(dict(R=R, L=L, span=span, p=p, r0_minus_R=r0-R, A=A, rms_phi=lin_rms(f), rms_w=lin_rms(f**2)))
json.dump(out, open("B1b_results.json", "w"), indent=1)
