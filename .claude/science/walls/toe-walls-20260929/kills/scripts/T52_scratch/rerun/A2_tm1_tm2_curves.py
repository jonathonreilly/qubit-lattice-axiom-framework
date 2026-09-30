"""TM1 and TM2 families by explicit parametrisation (theta from s13^2, free phase psi): the (s23^2, delta) curve.
Columns: TM1 = (xi, cos t W + sin t e^{i psi} eta, -sin t e^{-i psi} W + cos t eta); TM2 = (cos t xi + sin t e^{i psi} eta..., W, ...)."""
import numpy as np, math
from common import *
def tm1(t, psi):
    c1 = XI.astype(complex)
    c2 = math.cos(t) * W + math.sin(t) * np.exp(1j * psi) * ETA
    c3 = -math.sin(t) * np.exp(-1j * psi) * W + math.cos(t) * ETA
    return np.column_stack([c1, c2, c3])
def tm2(t, psi):
    c2 = W.astype(complex)
    c1 = math.cos(t) * XI + math.sin(t) * np.exp(1j * psi) * ETA
    c3 = -math.sin(t) * np.exp(-1j * psi) * XI + math.cos(t) * ETA
    return np.column_stack([c1, c2, c3])
s13_target = 0.02245   # midpoint of the repo-quoted NuFIT-6.1 3sigma range (proxy for the centre; not a repo-quoted best fit)
for nm, f, sin_t2 in (("TM1", tm1, 3 * s13_target), ("TM2", tm2, 1.5 * s13_target)):
    t = math.asin(math.sqrt(sin_t2))
    rows = []
    for psi in np.linspace(0, 2 * math.pi, 3601):
        U = f(t, psi); assert np.allclose(U.conj().T @ U, np.eye(3), atol=1e-12)
        s12, s13, s23, sd, cd = observables(U)
        rows.append((psi, s12, s13, s23, sd, cd, math.degrees(math.atan2(sd, cd)) % 360))
    R = np.array(rows)
    print(f"\n{nm}: theta = {math.degrees(t):.3f} deg -> s13^2 = {R[0,2]:.5f}; s12^2 range over psi [{R[:,1].min():.4f},{R[:,1].max():.4f}]; s23^2 range [{R[:,3].min():.4f},{R[:,3].max():.4f}]")
    inb = [inbox((r[1], r[2], r[3]), BOX61) for r in R]
    print(f"  fraction of psi grid inside NuFIT-6.1 3sigma box: {np.mean(inb):.3f}")
    # delta range for s23^2 in [0.435,0.584] inside box
    sel = np.array(inb)
    if sel.any():
        d = R[sel, 6]; s23 = R[sel, 3]
        print(f"  inside box: s23^2 in [{s23.min():.3f},{s23.max():.3f}], delta (deg) covers [{d.min():.0f},{d.max():.0f}] (mod 360)")
        # delta at s23^2 closest to 0.470 and 0.545
        for tgt in (0.470, 0.5, 0.545):
            k = np.argmin(np.abs(R[sel, 3] - tgt))
            print(f"  s23^2={R[sel,3][k]:.3f}: delta = {R[sel,6][k]:.1f} deg (sin d = {R[sel,4][k]:.3f})")
    # exact reflection points psi = pi/2, 3pi/2
    for psi in (math.pi / 2, 3 * math.pi / 2):
        o = observables(f(t, psi)); print(f"  psi={math.degrees(psi):.0f}: s12^2={o[0]:.5f} s13^2={o[1]:.5f} s23^2={o[2]:.5f} sin d={o[3]:.6f} cos d={o[4]:.2e}")
