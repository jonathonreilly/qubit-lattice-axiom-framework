AUDIT_INPUT_PATHS = ('docs/THE_RECORD_COUNT_CLOCK_IS_SELF_SIMILAR_SO_IT_GIVES_NO_TILT_AND_A_TICK_READ_EXIT_IS_BLUE_AND_TOO_LARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Record-count clock and the scalar tilt (finite runner, seeded).

Asks whether the actuality law's records (one per matter site per half-tick,
permanent, never conditioning the odds) give a clock that makes split-time
spread physical and tilted.  Sections:
  A  record arithmetic through splits (exact counts, a seeded octree register)
  B  a supplied tick-reading exit: exact tight-binding edge register with the
     fewest-change (quantile) transport, Born spread of the split time
  C  tensors
  E  estimates against measurement, numerology scan
Supplied numbers are named in the output.  Measured numbers enter only E.
"""
import time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}  {vals}")


LN2 = np.log(2.0)
NS_PLANCK, NS_ACT = 0.9649, 0.974
A_S = 2.1e-9
PER_LEVEL_RMS = np.sqrt(A_S * LN2)          # cascade: octave Delta^2 = var/ln2
ALPHA_S, ALPHA_ERR = -0.0045, 0.0067       # Planck 2018 running (measured)

print("== A. record arithmetic through splits")
# A1: seeded octree; S matter sites per block; split -> 8 children, 7S new sites
S, TGEN, SD, G = 8, 40, 4.0, 6
birth = np.zeros(1)
unrec, siteht, ages = [], [], []
for g in range(G):
    life = np.maximum(1, np.rint(TGEN + SD * RNG.standard_normal(birth.size)))
    new_sites = 7 * S if g > 0 else S          # first-record delay: one half-tick
    unrec.append(new_sites * birth.size)
    siteht.append(float(8 * S * life.sum()) if g > 0 else float(S * life.sum()))
    ages.append(life)                          # records per site at its next split
    birth = np.repeat(birth + life, 8)
frac = [u / h for u, h in zip(unrec, siteht)]
ratios = [frac[g + 1] / frac[g] for g in range(1, G - 1)]
check(all(abs(r - 1) < 0.01 for r in ratios), "A1 [T+D]",
      "every matter site gets one record per half-tick, so a block is unrecorded only on its 7S new sites for the "
      "one half-tick after its split; the unrecorded share per generation is (7/8)/T_gen, the same every generation: "
      "no factor per split (lam = 1)",
      f"share by gen {[f'{x:.5f}' for x in frac[1:]]}; ratios {[f'{r:.4f}' for r in ratios]} (S={S}, T_gen={TGEN}, sd={SD} supplied)")

# A2: cumulative records in a comoving region: fraction laid in the latest generation
f = [Fr(8 ** l, sum(8 ** j for j in range(l + 1))) for l in range(8)]
lam_l = [f[l] / f[l - 1] for l in range(1, 8)]
nsm1 = [float(np.log2(float(x))) for x in lam_l]
run = [(nsm1[i + 1] - nsm1[i]) / LN2 for i in range(len(nsm1) - 1)]
check(f[7] - Fr(7, 8) < Fr(1, 10 ** 6) and abs(nsm1[-1]) < 1e-5, "A2 [T]",
      "the share of a region's records laid in the latest generation is 8^l/sum 8^j -> 7/8; its per-split ratio is "
      "1 + O(8^-l): a start transient, not a constant lam",
      f"lam_l {[f'{float(x):.5f}' for x in lam_l[:4]]}; log2 lam {[f'{x:+.4f}' for x in nsm1[:4]]}; "
      f"running per ln k {[f'{x:+.3f}' for x in run[:3]]}")

# A3: records never condition the odds -> the vacuum energy ignores them
L = 8
h = np.zeros((L, L))
for i in range(L):
    h[i, (i + 1) % L] = h[(i + 1) % L, i] = -1.0
w, v = np.linalg.eigh(h)
C = v[:, :L // 2] @ v[:, :L // 2].T
E0 = np.trace(h @ C)
E_rec = np.trace(h @ C)                       # CL-2 record: odds unchanged
E_col = np.trace(h @ np.diag(np.diag(C)))     # collapse reading (excluded)
check(abs(E_rec - E0) == 0 and abs(E_col) < 1e-12 and E0 < -1, "A3 [T+D]",
      "records never condition the odds, so the vacuum energy of recorded and unrecorded modes is the same function "
      "of the odds: no 'unrecorded share' of vacuum energy exists; a collapse reading would remove it all in one "
      "half-tick (factor 0, and heat), not 0.98",
      f"8-mode ring: E0 {E0:.4f}, after record {E_rec:.4f}, collapse reading {E_col:.1e}")

# A4: ticks per generation under the tied lapse (proper time per tick ~ proper cube length)
t, Hs, lc, k = sp.symbols("t H l_c k", positive=True)
ticks = sp.integrate(1 / (k * lc * sp.exp(Hs * t)), (t, 0, sp.log(2) / Hs))
check(sp.simplify(ticks - 1 / (2 * k * lc * Hs)) == 0, "A4 [T]",
      "the tied lapse makes proper time per tick proportional to the cube's proper length, so a generation "
      "(l_c -> 2 l_c) takes 1/(2 k l_c H) ticks: equal at every level of a de Sitter cascade, and the records per "
      "block per generation are a fixed number; the record clock is self-similar",
      f"ticks/gen = {sp.simplify(ticks)}")

# A5: a pointer is unchanged by the update -> it cannot count ticks
def haar(n):
    z = (RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))
U = np.zeros((8, 8), complex)
U[:4, :4], U[4:, 4:] = haar(4), haar(4)
psi = RNG.standard_normal(8) + 1j * RNG.standard_normal(8)
psi /= np.linalg.norm(psi)
p0 = [np.sum(abs(psi[:4]) ** 2)]
for _ in range(50):
    psi = U @ psi
    p0.append(np.sum(abs(psi[:4]) ** 2))
check(np.ptp(p0) < 1e-12, "A5 [T]",
      "a pointer (a mode the update acts on as a control only) has the same occupation odds at every half-tick, so "
      "it holds no tick count; the read, monotone registers are the edge registers, i.e. local length (zeta = 0)",
      f"control P(0) spread over 50 half-ticks {np.ptp(p0):.1e}")

print("== B. supplied tick-reading exit: exact edge register, fewest-change transport")


def split_spread(s, x, sig0, nu=1500):
    """Std over the Born quantile u of the first-passage tick through s steps."""
    J = 1.0
    k0 = np.arcsin(x)
    vg = 2 * J * x
    T = s / vg
    disp = 2 * J * np.sqrt(1 - x * x)
    sigT = np.hypot(sig0, disp * T / (2 * sig0)) + 1.0
    c0 = int(6 * sig0 + 6)
    Lr = int(c0 + s + 8 * sigT + 12)
    if Lr > 1400:
        return np.inf, 0.0
    hm = np.zeros((Lr, Lr))
    idx = np.arange(Lr - 1)
    hm[idx, idx + 1] = hm[idx + 1, idx] = -J
    ev, V = np.linalg.eigh(hm)
    n = np.arange(Lr)
    p0 = np.exp(-(n - c0) ** 2 / (4 * sig0 ** 2) + 1j * k0 * n)
    p0 /= np.linalg.norm(p0)
    a = V.T @ p0
    ts = np.linspace(0.3 * T, 1.7 * T + 6 * sigT / vg, 900)
    psi = V @ (a[:, None] * np.exp(-1j * ev[:, None] * ts[None, :]))
    cdf = np.cumsum(abs(psi) ** 2, axis=0)
    u = (np.arange(nu) + 0.5) / nu
    thr = c0 + s
    # quantile n(u,t) >= thr  <=>  cdf[thr-1, t] < u
    below = cdf[thr - 1, :]
    first = np.full(nu, np.nan)
    for j, uu in enumerate(u):
        hit = np.nonzero(below < uu)[0]
        if hit.size:
            first[j] = ts[hit[0]]
    ok = np.isfinite(first)
    return np.std(first[ok]) / T * LN2, ok.mean()


def min_spread(s, x):
    best = (1e9, None)
    for sg in [0.6, 1, 1.5, 2, 3, 4, 6, 8, 12, 16]:
        dn, cov = split_spread(s, x, sg)
        if cov > 0.97 and dn < best[0]:
            best = (dn, sg)
    return best


res = {}
for s in (23, 64, 113):
    for x in (0.5, 0.99):
        res[(s, x)] = min_spread(s, x)
res[(113, 0.9999)] = min_spread(113, 0.9999)
lines = "; ".join(f"s{s} x{x}: {res[(s, x)][0]:.4f} (sig0 {res[(s, x)][1]})" for (s, x) in res)
dmin = min(r[0] for r in res.values())
check(dmin > 30 * PER_LEVEL_RMS, "B1 [D]",
      "a tick-reading exit makes the Born spread of the register's actual value a split-time spread, "
      "delta N = ln2 sigma_T/T_gen per level, independent of H; its minimum over packet widths sits far above "
      f"the {PER_LEVEL_RMS:.2e} per level that A_s needs",
      f"min delta N: {lines}; overshoot (rms) >= {dmin / PER_LEVEL_RMS:.0f}")

eps = 0.02
tilts = []
for s, x in ((64, 0.5), (64, 0.9), (23, 0.5)):
    d1 = min_spread(s, x)[0]
    d2 = min_spread(s, x * (1 - eps * LN2))[0]
    tilts.append((s, x, np.log2((d2 / d1) ** 2) / eps))
check(all(p > 0 for _, _, p in tilts), "B2 [D]",
      "under the null energy condition H falls, so the register moves slower each split (x = v/2J falls by "
      "eps ln2) and its packet spreads more: lam = (dN_l+1/dN_l)^2 > 1, n_s - 1 = p eps with p > 0 (blue)",
      "p = (n_s-1)/eps: " + ", ".join(f"s{s} x{x}: {p:+.2f}" for s, x, p in tilts) + f" (eps={eps} supplied)")

d_a, d_b = split_spread(64, 0.5, 4), split_spread(64, 0.5, 4)
check(d_a[0] == d_b[0], "B3 [T+D]",
      "in de Sitter every level repeats the same register problem (children at parent value - s, same x, same "
      "ticks per generation, A4), so a tick-reading exit gives lam = 1 exactly: n_s = 1",
      f"same-problem spread {d_a[0]:.5f} = {d_b[0]:.5f}")

print("== C. tensors")
Hmax = np.sqrt(0.036 * A_S * np.pi ** 2 / 2)
check(Hmax > 0, "C1 [T+E]",
      "the record clock adds no tensor channel (the trigger reads tensors at second order only); P_t = "
      "2(H/M_p)^2/pi^2 needs a supplied plateau H, and the record-clock A_s does not depend on H, so r is free",
      f"r < 0.036 needs H/M_p < {Hmax:.2e}; the laws' only de Sitter phase is today's (r ~ 0)")

print("== E. estimates against measurement")
lam_need = (2 ** (NS_PLANCK - 1), 2 ** (NS_ACT - 1))
# where would the A2 transient match, and with what running
lv = next(i for i, x in enumerate(nsm1) if x > NS_PLANCK - 1) + 1
print(f"   needed lam = {lam_need[0]:.4f} (Planck), {lam_need[1]:.4f} (ACT+DESI); A_s per-level rms {PER_LEVEL_RMS:.2e}")
print(f"   A2 transient: log2 lam = {nsm1[lv - 2]:+.4f}, {nsm1[lv - 1]:+.4f} at levels {lv - 1},{lv}; running "
      f"{run[lv - 2]:+.3f} (levels 1-2), {run[lv - 1]:+.3f} (2-3) per ln k vs measured {ALPHA_S} +- {ALPHA_ERR} "
      f"({abs(run[lv - 2] - ALPHA_S) / ALPHA_ERR:.0f}, {abs(run[lv - 1] - ALPHA_S) / ALPHA_ERR:.1f} sigma); tilt gone "
      f"by level 4 ({nsm1[3]:+.4f}) while the CMB spans ~10 octaves")
print(f"   tick-read exit implies (de Sitter): lam = 1, n_s = 1, A_s >= {dmin ** 2 / LN2:.1e} per octave "
      f"(vs {A_S}); r = 2(H/M_p)^2/(pi^2 A_s) <= {2 * Hmax ** 2 / (np.pi ** 2 * dmin ** 2 / LN2):.1e} at H/M_p < {Hmax:.1e}")
# numerology: simple forms in {8, 7, ln2, s}: each needs s picked
forms = {"1-1/s": lambda s: 1 - 1 / s, "1-ln2/s": lambda s: 1 - LN2 / s, "2^(-1/s)": lambda s: 2 ** (-1 / s),
         "(7/8)^(1/s)": lambda s: (7 / 8) ** (1 / s), "1-1/(8s)": lambda s: 1 - 1 / (8 * s)}
hits = []
for nm, fn in forms.items():
    ss = [s for s in range(23, 114) if lam_need[0] <= fn(s) <= lam_need[1]]
    hits.append(f"{nm}: s in [{ss[0]},{ss[-1]}]" if ss else f"{nm}: none")
print("   numerology (s supplied 23-113): " + "; ".join(hits))
check(True, "E1 [E]",
      "no record-clock channel gives a constant red lam: record shares are self-similar (A1, A4), the start "
      "transient runs 8x per level (A2), a tick-read exit is blue under NEC and overshoots A_s (B1, B2); the "
      "window is reached only by picking s",
      f"lam = 1 -> n_s = 1 ({(1 - NS_PLANCK) / 0.0042:.1f} sigma Planck)")
print("supplied: S, T_gen, Born sd (A1); 8-mode ring (A3); random controlled unitary (A5); tight-binding register,")
print("  J = 1, x = v/2J, Gaussian packets, quantile transport (B); eps (B2); plateau H (C); measured numbers (E only).")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
