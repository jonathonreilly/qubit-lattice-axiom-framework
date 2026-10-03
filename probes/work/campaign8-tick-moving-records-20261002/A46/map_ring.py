"""A46 map_ring: for the SU(2)/U(1)-symmetric states the energy per bond is J'_eff e_J' + R ring with
J'_eff = J' + K'/3 (e_K' = e_J'/3 by symmetry), so the (J', K', R) map reduces to rho = R / J'_eff.
Per L: the projected pi-flux singlet (m = 0) against the AF family (m > 0, variational), the ferromagnet
(J'_eff + 2R; exact eigenstate at K' = 0, an upper bound otherwise), the Neel product (-J'_eff), the
Neel LSWT (-1.1943 J'_eff; the ring adds nothing at harmonic order) and the plaquette product state
(each chosen face in the 4-site Heisenberg ground state: e_J' = -2/3, ring = 19/48)."""
import glob, numpy as np, signal
signal.alarm(60)
D = __file__.rsplit('/', 1)[0]
def binm(S):
    x = S.real; return x.mean()
for L in ("fcc16", "4", "6", "8"):
    fam = {}
    for f in glob.glob(f"{D}/vmcr_{L}_m*.npy"):
        m = float(f.rsplit("_m", 1)[1][:-4]); S = np.load(f); fam[m] = (S[:, 0].real.mean(), S[:, 2].real.mean())
    if 0.0 not in fam: continue
    print(f"L={L}: (e_J', ring) by m: " + "; ".join(f"m={m}: ({v[0]:+.4f}, {v[1]:+.4f})" for m, v in sorted(fam.items())))
    rhos = np.round(np.arange(-3.0, 3.0001, 0.01), 3); win = []; trans = None; prev = None
    for rho in rhos:
        E = {f"AF m={m}": v[0] + rho * v[1] for m, v in fam.items()}
        E["FM"] = 1 + 2 * rho; E["Neel product"] = -1.0; E["Neel LSWT"] = -1.1943; E["plaquette"] = -2 / 3 + rho * 19 / 48
        best = min(E, key=E.get)
        if best == "AF m=0.0": win.append(rho)
        if prev is not None and best != prev:
            print(f"   rho = {rho:+.2f}: lowest changes {prev} -> {best}")
        prev = best
    print(f"   window where the pi-flux singlet (m=0) is lowest: {('[%.2f, %.2f]' % (min(win), max(win))) if win else 'EMPTY'}")
    # margin: how far is m=0 from the lowest competitor at its best rho
    gaps = [(min(v for k, v in {**{f'AF m={m}': fam[m][0] + r * fam[m][1] for m in fam if m > 0}, 'FM': 1 + 2 * r, 'LSWT': -1.1943, 'plaq': -2/3 + r*19/48}.items()) - (fam[0.0][0] + r * fam[0.0][1]), r) for r in rhos]
    g, r = max(gaps)
    print(f"   closest approach: at rho = {r:+.2f} the pi-flux singlet is {-g:.4f} per bond above the lowest other state")
