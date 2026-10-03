"""A46 map_j2r: dual frame, per nearest-neighbour bond, J'_eff = J' + K'/3 = 1:
E = e_J' + R ring + 2 J2 c2  (6 face-diagonal bonds per site = 2 per NN bond; c2 = face-diagonal <s.s>).
States: VMC pi-flux singlet (m = 0) and AF family (L given); ferromagnet (1 + 2R + 2J2); Neel product
(-1 + 2J2); collinear (pi,pi,0) product (-(1 + 2J2)/3); plaquette product (-2/3 + 19R/48 + J2/6);
LSWT: Neel (A44 star_j2, ring adds nothing at harmonic order), collinear (A44 star_j2, ring taken at its
classical value 0: an estimate).  Original frame: J'_eff = (K - J)/3, same R and J2 (Klein-twisted terms)."""
import sys, glob, numpy as np, signal
signal.alarm(60)
D = __file__.rsplit('/', 1)[0]; L = sys.argv[1] if len(sys.argv) > 1 else "6"
fam = {}
for f in glob.glob(f"{D}/vmcj_{L}_m*.npy"):
    m = float(f.rsplit("_m", 1)[1][:-4]); S = np.load(f).real; fam[m] = (S[:, 0].mean(), S[:, 2].mean(), S[:, 4].mean())
for m, v in sorted(fam.items()):
    print(f"L={L} m={m}: e_J' {v[0]:+.4f}, ring {v[1]:+.4f}, face-diagonal c2 {v[2]:+.4f}")
col = {}
for f in glob.glob(f"{D}/vmcjc_6_m*.npy"):      # collinear (pi,pi,0) family, L = 6 only (used for every L; flagged)
    m = float(f.rsplit("_m", 1)[1][:-4]); S = np.load(f).real; col[m] = (S[:, 0].mean(), S[:, 2].mean(), S[:, 4].mean())
for m, v in sorted(col.items()):
    print(f"collinear family (L=6) m={m}: e_J' {v[0]:+.4f}, ring {v[1]:+.4f}, face-diagonal c2 {v[2]:+.4f}")
jl = np.array([0, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5])
neel_lswt = np.array([-3.5828, -3.1014, -2.7214, -2.6722, np.nan, np.nan, np.nan]) / 3     # per NN bond; nan = LSWT unstable
coll_lswt = np.array([np.nan, np.nan, np.nan, -2.2888, -2.2693, -2.4052, -2.6001]) / 3
def interp(tab, j):
    ok = ~np.isnan(tab)
    if j < jl[ok].min() - 1e-9 or j > jl[ok].max() + 1e-9: return np.nan
    return np.interp(j, jl[ok], tab[ok])
win = []; closest = (-np.inf, None)
for J2 in np.round(np.arange(0, 0.501, 0.025), 3):
    for R in np.round(np.arange(-2.0, 0.501, 0.05), 3):
        E = {f"AF m={m}": v[0] + R * v[1] + 2 * J2 * v[2] for m, v in fam.items()}
        E.update({f"COL m={m}": v[0] + R * v[1] + 2 * J2 * v[2] for m, v in col.items()})
        E["FM"] = 1 + 2 * R + 2 * J2; E["Neel product"] = -1 + 2 * J2; E["collinear product"] = -(1 + 2 * J2) / 3
        E["plaquette"] = -2 / 3 + 19 * R / 48 + J2 / 6
        nl, cl_ = interp(neel_lswt, J2), interp(coll_lswt, J2)
        if not np.isnan(nl): E["Neel LSWT"] = nl
        if not np.isnan(cl_): E["collinear LSWT"] = cl_
        e0 = E.pop("AF m=0.0"); other = min(E.values()); who = min(E, key=E.get)
        if e0 < other: win.append((J2, R, other - e0, who))
        if other - e0 > closest[0]: closest = (other - e0, (J2, R, who))
print(f"points (J2, R) where the pi-flux singlet is lowest: {len(win)} of {21*51}; J2 range {min(w[0] for w in win) if win else None}-{max(w[0] for w in win) if win else None}, R range {min(w[1] for w in win) if win else None}..{max(w[1] for w in win) if win else None}")
for w in win[::max(1, len(win) // 25)]:
    print(f"   J2={w[0]:.3f} R={w[1]:+.2f}: margin {w[2]:.4f} over {w[3]}")
print(f"best margin {closest[0]:+.4f} at J2={closest[1][0]}, R={closest[1][1]} (runner-up {closest[1][2]})")
