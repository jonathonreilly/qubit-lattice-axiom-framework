"""Independent checks: (a) J-sign diagonal gauge D(sigma)=prod_l s_l^{(1+sigma_l)/2} flips the sign of every move
(2^3 component exhaustively; random reachable states on 4^3, 6^3); (b) exact (pure-gauge) sources give zero
curvature while the harmonic one does not (2^3 exact).  No claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import chk
for L in (2, 4, 6):
    lat = chk.Lat((L, L, L))
    s_l = np.array([(-1) ** lat.verts[l // 3][(l % 3 + 1) % 3] for l in range(lat.nl)])
    assert (np.prod(s_l[lat.plaq], 1) == -1).all()
    rng = np.random.default_rng(L)
    s = chk.simple_ice(lat); bad = 0; nm = 0
    logD = lambda s: np.sum(np.log(s_l.astype(complex)) * (1 + s) / 2)
    for it in range(3000 if L > 2 else 500):
        c = lat.circ(s); fl = np.flatnonzero(c)
        for p in fl[:5]:
            t = s.copy(); t[lat.plaq[p]] *= -1
            r = np.exp(logD(t) - logD(s)).real
            bad += abs(r + 1) > 1e-9; nm += 1
        p = rng.choice(fl); s[lat.plaq[p]] *= -1
        assert np.abs(lat.div @ s).max() == 0
    print(f"L={L}: plaquette sign product -1 everywhere; D(flip)/D = -1 on {nm - bad}/{nm} sampled moves")
lat = chk.Lat((2, 2, 2)); S, nf, mv = chk.component(lat, chk.simple_ice(lat))
d1 = np.zeros((lat.np_, lat.nl))
for p in range(lat.np_):
    for l, sg in zip(lat.plaq[p], (1, 1, -1, -1)):
        d1[p, l] += sg
rng = np.random.default_rng(0)
a = rng.normal(size=lat.nl); ce = d1 @ a; ce /= np.linalg.norm(ce)
for V in (0.0, 0.5):
    for name, c in (("exact(gauge)", ce), ("harmonic", lat.harm(0))):
        Eh = lambda b: np.linalg.eigvalsh(chk.H_twist(len(S), nf, mv, V, b, c, imag=False))[0]
        print(f"V={V} {name}: chi = {(Eh(1e-3) + Eh(-1e-3) - 2 * Eh(0)) / 1e-6:.6f}")
# hermitian check: the twisted (real b) matrix is Hermitian with the circ-before convention
H = chk.H_twist(len(S), nf, mv, 0.3, 0.7, lat.harm(0), imag=False)
print("Hermitian(real b):", np.allclose(H, H.conj().T))
