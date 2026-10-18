"""T1e (POST-HOC, added after T1a): which sectors can share a shape at x3, and an up-split rule.

Variants (one universal base b and triple S from the T1a libraries, Lambda_f free per sector):
 V6: d and e share (b,S); u uses exponents 2S (doubled, SU(5)-FN-like template).
 V7: d and e share (b,S); u uses exponents (3/2)S.
 V8: d and e share (b,S); u has its own free (b',S') (one extra choice).
"""
import numpy as np
from common import MZ, LOW, LN3, SECTORS, obs_logs, null_N1, null_N2
import t1a_ladders as A  # reuses libraries (re-runs T1a main; output discarded upstream)

LB, S = A.LB, A.S


def h_sector(y, scale=1.0):
    """y (n,3) -> (n, nb, ns) half-range with exponents scale*S."""
    model = LB[:, None, None] * (scale * S)[None]
    R = y[:, None, None, :] - model[None]
    return 0.5 * (R.max(-1) - R.min(-1))


def scores(Y):
    hd, he = h_sector(Y[:, 1]), h_sector(Y[:, 2])
    de = np.maximum(hd, he)
    out = {}
    for name, sc in (("V6 u doubled", 2.0), ("V7 u x3/2", 1.5)):
        out[name] = np.maximum(de, h_sector(Y[:, 0], sc)).min(axis=(1, 2))
    out["V8 u free own (b,S)"] = np.maximum(de.min(axis=(1, 2)), h_sector(Y[:, 0]).min(axis=(1, 2)))
    out["d,e share (b,S) only"] = de.min(axis=(1, 2))
    return out


for label, data in (("MZ", MZ), ("LOW", LOW)):
    so = scores(obs_logs(data)[None])
    print(label, {k: round(float(np.exp(v[0])), 2) for k, v in so.items()})
for k, (a, b) in enumerate([(0, 2), (1, 2), (0, 1)]):
    pass
# in-sector ratio spreads (sector-blind shape test)
for label, data in (("MZ", MZ), ("LOW", LOW)):
    r1 = {s: data[s][0] / data[s][2] for s in SECTORS}
    r2 = {s: data[s][1] / data[s][2] for s in SECTORS}
    print(f"{label}: m1/m3 u {r1['u']:.2e} d {r1['d']:.2e} e {r1['e']:.2e}; m2/m3 u {r2['u']:.2e} d {r2['d']:.2e} e {r2['e']:.2e}")
    print(f"   pair spreads gen1: u/d {r1['d']/r1['u']:.0f}, u/e {r1['e']/r1['u']:.0f}, d/e {r1['d']/r1['e']:.1f}; "
          f"gen2: u/d {r2['d']/r2['u']:.1f}, u/e {r2['e']/r2['u']:.1f}, e/d {r2['e']/r2['d']:.1f}  (x3 allows 9)")
rng = np.random.default_rng(5)
for nname, gen in (("N1", lambda n: null_N1(rng, n)), ("N2", lambda n: null_N2(rng, n))):
    Y = gen(6000)
    parts = [scores(Y[i:i + 500]) for i in range(0, 6000, 500)]
    sr = {k: np.concatenate([p[k] for p in parts]) for k in parts[0]}
    so = scores(obs_logs(MZ)[None])
    print(nname, {k: (round(float(np.mean(v <= LN3)), 3), round(float(np.mean(v <= so[k][0])), 3)) for k, v in sr.items()},
          "(pass rate, P(as good as observed MZ))")

# winners for V6/V7 on observed
for label, data in (("MZ", MZ), ("LOW", LOW)):
    Yo = obs_logs(data)[None]
    de = np.maximum(h_sector(Yo[:, 1]), h_sector(Yo[:, 2]))
    for name, sc in (("V6", 2.0), ("V7", 1.5)):
        tot = np.maximum(de, h_sector(Yo[:, 0], sc))[0]
        order = np.argsort(tot.ravel())[:3]
        print(label, name, [(A.BN[i // tot.shape[1]], A.SLIB[i % tot.shape[1]], round(float(np.exp(tot.ravel()[i])), 2)) for i in order])
