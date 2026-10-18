"""T1b: worldsheet-area texture on Z^3.

Y^f_ij = exp(-sigma * A(l_i, h^f, r^f_j)), A = (1/2)||(h-l) x (r-l)||_1 (lattice L1 area,
a lower bound on the plaquette count of any lattice surface spanning the triangle).
l = {e_x, e_y, e_z} common to all sectors. r^f = hw1 or hw2 orbit + t, t in {-1,0,1}^3.
h^f in {-1,0,1,2}^3. sigma universal (one tension for all sectors).
Masses = singular values * Lambda_f. CKM = U_u^T U_d.
"""
import itertools
import numpy as np
from common import MZ, LOW, CKM, LN3, SECTORS, obs_logs, null_N1, null_N2

rng = np.random.default_rng(7)
E = np.eye(3, dtype=int)
L = [E[0], E[1], E[2]]
ORB = {"hw1": [E[0], E[1], E[2]], "hw2": [E[1] + E[2], E[2] + E[0], E[0] + E[1]]}
TS = [np.array(t) for t in itertools.product((-1, 0, 1), repeat=3)]
HS = [np.array(h) for h in itertools.product((-1, 0, 1, 2), repeat=3)]


def area(p, q, r):
    return 0.5 * np.abs(np.cross(q - p, r - p)).sum()


configs, seen = [], {}
for on, orb in ORB.items():
    for t in TS:
        R = [o + t for o in orb]
        for h in HS:
            A = np.array([[area(L[i], h, R[j]) for j in range(3)] for i in range(3)])
            key = tuple(A.ravel())
            if key in seen:
                continue
            seen[key] = len(configs)
            configs.append((on, tuple(t), tuple(h), A))
NC = len(configs)
AM = np.array([c[3] for c in configs])  # NC x 3 x 3
print(f"distinct area matrices: {NC} (from {2*len(TS)*len(HS)} placements)")
SIG = np.linspace(0.25, 12.0, 48)

# precompute log singular values (ascending: light, mid, heavy) and left vectors
LS = np.empty((len(SIG), NC, 3))
UL = np.empty((len(SIG), NC, 3, 3))
for a, sg in enumerate(SIG):
    Y = np.exp(-sg * AM)
    U, s, Wt = np.linalg.svd(Y)
    s = np.maximum(s, 1e-300)
    LS[a] = np.log(s[:, ::-1])
    UL[a] = U[:, :, ::-1]
degenerate = np.mean(np.abs(np.diff(LS, axis=2)) < 1e-6, axis=(1,))  # per sigma, per gap
print("fraction of configs with a degenerate pair (mean over sigma):",
      np.round(np.mean(np.abs(np.diff(LS, axis=2)).min(axis=2) < 1e-6), 3))


def sector_h(y):
    """y: (n,3) log masses (light..heavy). returns h: (n, nsig, NC)."""
    R = y[:, None, None, :] - LS[None]
    return 0.5 * (R.max(-1) - R.min(-1))


def mass_score(Y):
    """Y: (n,3,3). universal sigma, per-sector config. returns best log factor (n,) and argbest sigma."""
    hs = np.stack([sector_h(Y[:, s]).min(-1) for s in range(3)], axis=1)  # n x 3 x nsig
    worst = hs.max(axis=1)  # n x nsig
    return worst.min(-1), worst.argmin(-1), hs


def ckm_best(yu, yd, tol=LN3):
    """for observed: over sigma, over mass-passing (u,d) config pairs, best CKM factor."""
    best = (np.inf, None)
    for a in range(len(SIG)):
        hu = 0.5 * np.ptp(yu[None] - LS[a], axis=-1)
        hd = 0.5 * np.ptp(yd[None] - LS[a], axis=-1)
        iu, idd = np.where(hu <= tol)[0], np.where(hd <= tol)[0]
        if len(iu) == 0 or len(idd) == 0:
            continue
        for c0 in range(0, len(iu), 100):
            iuc = iu[c0:c0 + 100]
            V = np.einsum("aki,bkj->abij", UL[a, iuc], UL[a, idd])
            v = np.abs(np.stack([V[..., 0, 1], V[..., 1, 2], V[..., 0, 2]], -1))
            f = np.abs(np.log(np.maximum(v, 1e-300) / CKM)).max(-1)
            k = np.unravel_index(np.argmin(f), f.shape)
            if f[k] < best[0]:
                best = (f[k], (SIG[a], configs[iuc[k[0]]][:3], configs[idd[k[1]]][:3], v[k]))
    return best


for label, data in (("MZ", MZ), ("LOW", LOW)):
    Yo = obs_logs(data)[None]
    sc, ia, hs = mass_score(Yo)
    print(f"\n=== {label}: masses, universal sigma: best factor x{np.exp(sc[0]):.2f} at sigma={SIG[ia[0]]:.2f}; "
          f"pass={sc[0] <= LN3}")
    print("   per-sector best factor at that sigma:", np.round(np.exp(hs[0, :, ia[0]]), 2))
    # per-sector own sigma
    print("   per-sector best factor, own sigma:", np.round(np.exp(hs[0].min(-1)), 2))
    f, info = ckm_best(Yo[0, 0], Yo[0, 1])
    if info is None:
        print("   CKM: no sigma with both u and d passing masses")
    else:
        print(f"   CKM (masses u,d within x3): best CKM factor x{np.exp(f):.2f}; sigma={info[0]:.2f}; "
              f"|Vus,Vcb,Vub|={np.round(info[3], 4)}; u cfg={info[1]}, d cfg={info[2]}")
    # CKM with relaxed mass tolerance x10
    f10, info10 = ckm_best(Yo[0, 0], Yo[0, 1], tol=np.log(10))
    if info10 is not None:
        print(f"   CKM (masses u,d within x10): best CKM factor x{np.exp(f10):.2f}; |V|={np.round(info10[3], 4)}")

for nname, gen in (("N1", lambda n: null_N1(rng, n)), ("N2", lambda n: null_N2(rng, n))):
    n = 2000
    Y = gen(n)
    scs = np.concatenate([mass_score(Y[i:i + 20])[0] for i in range(0, n, 20)])
    Yo = obs_logs(MZ)[None]
    so = mass_score(Yo)[0][0]
    print(f"\n[{nname}] masses universal sigma, per-sector config: random pass rate {np.mean(scs <= LN3):.3f}; "
          f"P(random as good as observed) {np.mean(scs <= so):.3f}")
    # CKM control on a subsample: random spectra + random CKM targets
    m = 60
    ok = 0
    for i in range(m):
        ck = np.exp(rng.uniform(np.log(1e-4), 0, size=3))
        old = CKM.copy()
        CKM[:] = ck
        f, info = ckm_best(Y[i, 0], Y[i, 1])
        CKM[:] = old
        ok += (info is not None and f <= LN3)
    print(f"[{nname}] masses(u,d) + CKM all within x3: random pass rate {ok}/{m}")
