"""P0: validate the spin-taste construction (2D and 4D) against eps and the 07-02 note's Gamma_f."""
import numpy as np
from stag import *

out = []
def rep(name, ok, info=""):
    out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")
    print(out[-1])

for d, L in [(2, 8), (4, 4)]:
    lat = Lat(L, d)
    if d == 2:
        U0 = np.ones((lat.V, 2, 1, 1), complex)
    else:
        U0 = np.ones((lat.V, 4, 1, 1), complex)
    O11 = ident_op(lat, U0).toarray()
    rep(f"d={d} O(1x1)=I", np.abs(O11 - np.eye(lat.V)).max() < 1e-12, f"dev={np.abs(O11-np.eye(lat.V)).max():.2e}")
    O55 = taste55_op(lat, U0).toarray()
    e = np.diag(lat.eps)
    dev = min(np.abs(O55 - e).max(), np.abs(O55 + e).max())
    rep(f"d={d} O(g5 x xi5)=+-eps", dev < 1e-12, f"dev={dev:.2e}")
    # singlet
    for avg in (False, True):
        Os = singlet_op(lat, U0, avg_offsets=avg).toarray()
        herm = np.abs(Os - Os.conj().T).max()
        ev = np.linalg.eigvalsh((Os + Os.conj().T) / 2)
        # support: displacement pattern
        nz = np.argwhere(np.abs(Os) > 1e-12)
        disp = set()
        for i, j in nz:
            dx = (lat.coords[j] - lat.coords[i] + L // 2) % L - L // 2
            disp.add(tuple(np.abs(dx)))
        rep(f"d={d} singlet avg={avg}: Hermitian, spectrum in [-1,1], support |dx|", herm < 1e-12 and ev.min() >= -1 - 1e-9 and ev.max() <= 1 + 1e-9,
            f"herm={herm:.1e} ev=[{ev.min():.3f},{ev.max():.3f}] support={sorted(disp)}")
        # commutes with eps? anticommute with D (free)?
        D = stag_D(lat, U0).toarray()
        comm_eps = np.abs(Os @ np.diag(lat.eps) - np.diag(lat.eps) @ Os).max()
        anti_D = np.abs(Os @ D + D @ Os).max()
        rep(f"d={d} singlet avg={avg}: [O,eps]=0", comm_eps < 1e-12 if avg else True, f"|[O,eps]|={comm_eps:.1e}  |{{O,D}}|={anti_D:.2e}")
    if d == 2:
        Gf = gamma_f_2d(lat, U0).toarray()
        Os = singlet_op(lat, U0, True).toarray()
        s1 = np.sort(np.linalg.eigvalsh(Gf)); s2 = np.sort(np.linalg.eigvalsh(Os))
        rep("d=2 spectrum(Gamma_f) == spectrum(spin-taste singlet)", np.abs(s1 - s2).max() < 1e-9 or np.abs(s1 + s2[::-1]).max() < 1e-9,
            f"maxdiff={min(np.abs(s1-s2).max(), np.abs(s1+s2[::-1]).max()):.2e}")
        # relation of operators up to sign / unitary ; check Gf == +-Os exactly
        dev = min(np.abs(Gf - Os).max(), np.abs(Gf + Os).max())
        rep("d=2 Gamma_f == +-spin-taste singlet as matrices", dev < 1e-9, f"dev={dev:.2e}")
        # with flux
        U1 = u1_flux_links_2d(lat, 1)
        Gf = gamma_f_2d(lat, U1).toarray(); Os = singlet_op(lat, U1, True).toarray()
        dev = min(np.abs(Gf - Os).max(), np.abs(Gf + Os).max())
        rep("d=2 flux Q=1: Gamma_f == +-spin-taste singlet", dev < 1e-9, f"dev={dev:.2e}")
        print("flux check", total_flux_plane(lat, U1, 0, 1) / (2 * np.pi))
open("p0_out.txt", "w").write("\n".join(out) + "\n")
