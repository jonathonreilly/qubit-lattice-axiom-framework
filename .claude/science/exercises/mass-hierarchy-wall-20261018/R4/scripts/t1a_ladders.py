"""T1a: scalar exponential ladders m_i = Lambda_f * b^{S_i} with lattice-fixed b, S.

Score per sector = half-range of (y - S ln b) (one free Lambda_f); factor = exp(score).
Pass = every sector factor <= 3.
"""
import itertools
import numpy as np
from common import (MZ, LOW, LN3, SECTORS, obs_logs, null_N1, null_N2,
                    ALPHA_BARE, ALPHA_LM, ALPHA_SV, P_PLAQ, U0)

rng = np.random.default_rng(20261018)
NR = 20000


def triples(vals):
    out = set()
    for x, y, z in itertools.combinations(sorted(set(vals)), 3):
        out.add((z - x, y - x))  # (S_light, S_mid), S_heavy = 0
    return sorted(out)


HOP = triples([0, 1, 2, 3, 4])
SQ = triples([0, 1, 4, 9, 16])
SLIB = sorted(set(HOP) | set(SQ))
BASES = {
    "alpha_bare": ALPHA_BARE, "alpha_LM": ALPHA_LM, "alpha_s(v)": ALPHA_SV,
    "<P>": P_PLAQ, "u0": U0, "1/2": 0.5, "1/3": 1 / 3, "1/4": 0.25, "1/6": 1 / 6,
    "1/8": 0.125, "1/16": 1 / 16, "e^-pi": np.exp(-np.pi), "e^-pi/2": np.exp(-np.pi / 2),
    "1/(16pi^2)": 1 / (16 * np.pi ** 2),
}
BN = list(BASES)
LB = np.log(np.array([BASES[k] for k in BN]))  # nb
S = np.array([[s1, s2, 0.0] for (s1, s2) in SLIB])  # ns x 3 (light, mid, heavy)
print(f"exponent library: hop {len(HOP)}, squares {len(SQ)}, union {len(SLIB)}; bases {len(BN)}")


def halfrange(Y):
    """Y: (..., 3 sectors, 3 masses) log masses -> h: (..., 3, nb, ns)."""
    model = LB[:, None, None] * S[None, :, :]  # nb x ns x 3
    R = Y[:, :, None, None, :] - model[None, None]  # n x 3 x nb x ns x 3
    return 0.5 * (R.max(-1) - R.min(-1))


def variants(H):
    """H: (n, 3, nb, ns) half-ranges. Return best log-factor per variant, shape (n,)."""
    v1 = H.max(axis=1).min(axis=(1, 2))                      # universal (b,S)
    v2 = H.min(axis=3).max(axis=1).min(axis=1)               # universal b, S per sector
    v3 = H.min(axis=(2, 3)).max(axis=1)                      # (b,S) per sector
    return {"V1 universal (b,S)": v1, "V2 universal b, S per sector": v2,
            "V3 (b,S) per sector": v3}


def shape_only(Y, slib=S):
    """V4: continuous per-sector base: h = |dev|/2; min over S per sector; max over sectors."""
    y1, y2, y3 = Y[..., 0], Y[..., 1], Y[..., 2]
    s1, s2 = slib[:, 0], slib[:, 1]
    P = y3[..., None] + (y1 - y3)[..., None] * (s2 / s1)
    h = 0.5 * np.abs(y2[..., None] - P)
    return h.min(-1).max(-1), h


def universal_sigma(Y, sig=np.linspace(0.05, 8.0, 400)):
    """V5: one continuous sigma for all sectors, S per sector from library."""
    best = np.full(Y.shape[0], np.inf)
    for sg in sig:
        model = -sg * S  # ns x 3
        R = Y[:, :, None, :] - model[None, None]
        h = 0.5 * (R.max(-1) - R.min(-1))  # n x 3 x ns
        best = np.minimum(best, h.min(-1).max(-1))
    return best


for label, data in (("MZ", MZ), ("LOW", LOW)):
    Yo = obs_logs(data)[None]
    Ho = halfrange(Yo)
    vo = variants(Ho)
    v4o, h4 = shape_only(Yo)
    v5o = universal_sigma(Yo)
    print(f"\n=== observed set {label} ===")
    for k, v in vo.items():
        print(f"{k:32s} best factor x{np.exp(v[0]):.2f}  pass={v[0] <= LN3}")
    print(f"{'V4 continuous base per sector':32s} best factor x{np.exp(v4o[0]):.2f}  pass={v4o[0] <= LN3}")
    print(f"{'V5 universal continuous sigma':32s} best factor x{np.exp(v5o[0]):.2f}  pass={v5o[0] <= LN3}")
    # best V1 entry
    i = np.unravel_index(np.argmin(Ho[0].max(axis=0)), Ho[0].shape[1:])
    print(f"  V1 best: base {BN[i[0]]}, S={SLIB[i[1]]}")
    # R windows (continuous base) per sector
    for s, key in enumerate(SECTORS):
        y = Yo[0, s]
        g1, g2 = y[2] - y[0], y[2] - y[1]
        lo = g1 / (g2 + 2 * LN3)
        hi = g1 / (g2 - 2 * LN3) if g2 > 2 * LN3 else np.inf
        ok = [f"{a}/{b}" for (a, b) in SLIB if lo <= a / b <= hi]
        print(f"  sector {key}: R_obs={g1/g2:.3f}, x3 window R in [{lo:.2f}, {hi:.2f}]; library hits {len(ok)}/{len(SLIB)}")

# random controls
for nname, gen in (("N1", lambda: null_N1(rng, NR)), ("N2", lambda: null_N2(rng, NR))):
    Y = gen()
    parts, single = [], 0.0
    for i in range(0, NR, 1000):
        Hc = halfrange(Y[i:i + 1000])
        parts.append(variants(Hc))
        single = single + (Hc.max(axis=1) <= LN3).sum(axis=0)
    vr = {k: np.concatenate([p[k] for p in parts]) for k in parts[0]}
    single = single / NR
    print(f"[{nname}] single pre-registered (b,S), all sectors: pass rate mean {single.mean():.4f}, max {single.max():.4f} over {single.size} combos")
    v4r, _ = shape_only(Y)
    v5r = universal_sigma(Y[:5000])
    print(f"\n=== random control {nname} (n={NR}; V5 n=5000) ===")
    Yo = obs_logs(MZ)[None]
    vo = variants(halfrange(Yo))
    for k, v in vr.items():
        print(f"{k:32s} pass rate {np.mean(v <= LN3):.3f};  P(random as good as observed MZ) {np.mean(v <= vo[k][0]):.3f}")
    v4o, _ = shape_only(Yo)
    v5o = universal_sigma(Yo)
    print(f"{'V4 continuous base per sector':32s} pass rate {np.mean(v4r <= LN3):.3f};  P(as good) {np.mean(v4r <= v4o[0]):.3f}")
    print(f"{'V5 universal continuous sigma':32s} pass rate {np.mean(v5r <= LN3):.3f};  P(as good) {np.mean(v5r <= v5o[0]):.3f}")
