"""P1/P2/P5 on the 2D U(1) staggered surface with uniform flux 2 pi Q (same surface as the 07-02 supplier note)."""
import numpy as np
from stag import *

out = []
def rep(s):
    print(s); out.append(s)

m = 0.5
rows = []
for L in (8, 12):
    lat = Lat(L, 2)
    E = np.diag(lat.eps)
    for Q in (-2, -1, 0, 1, 2):
        U = u1_flux_links_2d(lat, Q)
        assert abs(total_flux_plane(lat, U, 0, 1) - 2 * np.pi * Q) < 1e-9
        D = stag_D(lat, U).toarray()
        Gf = gamma_f_2d(lat, U).toarray()
        Os = singlet_op(lat, U, True).toarray()
        for r in (0.2, 1.0, 5.0):
            m5 = r * m
            # eps direction
            a_e, ld_e = argdet(D + m * np.eye(lat.V) + 1j * m5 * E)
            ref = np.linalg.slogdet(D + np.sqrt(m ** 2 + m5 ** 2) * np.eye(lat.V))[1]
            a_e = (a_e + np.pi) % (2 * np.pi) - np.pi
            rows.append(("eps", L, Q, r, a_e, ld_e - ref))
            # Gamma_f direction
            a_g, _ = argdet(D + m * np.eye(lat.V) + 1j * m5 * Gf)
            a_o, _ = argdet(D + m * np.eye(lat.V) + 1j * m5 * Os)
            rows.append(("Gf", L, Q, r, a_g, np.nan))
            rows.append(("Os", L, Q, r, a_o, np.nan))
        # complex scalar control m e^{i alpha}
        a_c, _ = argdet(D + m * np.exp(1j * 0.2) * np.eye(lat.V))
        rows.append(("cplx", L, Q, 0.2, a_c, np.nan))

rep("kind  L   Q   m5/m   arg det   [eps: log|det| - log det(D+sqrt(m^2+m5^2)) ]")
for k, L, Q, r, a, ld in rows:
    rep(f"{k:5s} {L:3d} {Q:3d} {r:5.1f} {a:+.6f} {ld if ld==ld else ''}")

# P1 check
eps_rows = [x for x in rows if x[0] == "eps"]
rep(f"P1(2D): max |arg det eps-direction| = {max(abs(x[4]) for x in eps_rows):.2e}; max |log|det| diff| = {max(abs(x[5]) for x in eps_rows):.2e}")

# P2: ratio to 2 Q phi
for kind in ("Gf", "Os"):
    for L in (8, 12):
        rep(f"--- {kind} L={L}: arg det / (2 Q arctan(m5/m)) at m5/m=0.2 and 1.0")
        for Q in (-2, -1, 1, 2):
            for r in (0.2, 1.0):
                a = [x[4] for x in rows if x[0] == kind and x[1] == L and x[2] == Q and x[3] == r][0]
                phi = np.arctan(r)
                rep(f"   Q={Q:+d} r={r}: arg={a:+.5f}  arg/(2Q phi)={a/(2*Q*phi):+.4f}")
        a0 = [x[4] for x in rows if x[0] == kind and x[1] == L and x[2] == 0 and x[3] == 0.2][0]
        rep(f"   Q=0: arg={a0:+.2e}")

# P5: linearity in phi at Q=1, L=8, Gf
lat = Lat(8, 2)
U = u1_flux_links_2d(lat, 1)
D = stag_D(lat, U).toarray(); Gf = gamma_f_2d(lat, U).toarray()
rep("--- P5 linearity (Gf, L=8, Q=1): m5/m, arg, arg/(2 arctan)")
for r in (0.05, 0.1, 0.2, 0.4, 0.8):
    a, _ = argdet(D + m * np.eye(lat.V) + 1j * r * m * Gf)
    rep(f"   {r:4.2f}  {a:+.5f}  {a/(2*np.arctan(r)):+.4f}")
open("p2_out.txt", "w").write("\n".join(out) + "\n")
