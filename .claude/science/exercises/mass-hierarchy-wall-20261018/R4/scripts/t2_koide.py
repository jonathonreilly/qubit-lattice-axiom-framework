"""T2: Koide / Brannen twisted-circulant control.

sqrt(m_k) = mu (1 + r cos(delta + 2 pi k/3)),  Q = (1 + r^2/2)/3.
"""
from fractions import Fraction
import numpy as np
from common import MZ, LOW, LN3, SECTORS

rng = np.random.default_rng(2)
POLE_E = np.array([0.51099895e-3, 0.1056583755, 1.77686])
DTAU = 0.12e-3


def koide(m):
    v = np.sqrt(np.asarray(m, float))
    return (v ** 2).sum(-1) / v.sum(-1) ** 2


def brannen(m):
    """return r, delta in fundamental domain [0, pi/3] for positive roots (vectorized over last axis)."""
    v = np.sqrt(np.asarray(m, float))
    a0 = v.mean(-1)
    w = np.exp(-2j * np.pi * np.arange(3) / 3)
    z = (v * w).sum(-1) / 3
    r = 2 * np.abs(z) / a0
    d = np.mod(np.angle(z), 2 * np.pi / 3)
    d = np.where(d > np.pi / 3, 2 * np.pi / 3 - d, d)
    return r, d


def brannen_masses(r, d):
    k = np.arange(3)
    v = 1 + r * np.cos(d + 2 * np.pi * k / 3)
    return np.sort(v ** 2)


# grammars
QG = sorted({Fraction(a, b) for b in range(1, 13) for a in range(1, b + 1) if 1 / 3 < a / b < 1})
DG_rad = sorted({Fraction(a, b) for b in range(1, 13) for a in range(0, 2 * b) if a / b <= np.pi / 3})
DG_pi = sorted({Fraction(a, b) for b in range(1, 13) for a in range(0, b + 1) if a / b <= 1 / 3})
print(f"grammar sizes: Q targets {len(QG)}, delta rad-rationals {len(DG_rad)}, delta pi-rationals {len(DG_pi)}")
qg = np.array([float(x) for x in QG])
dg = np.concatenate([[float(x) for x in DG_rad], [np.pi * float(x) for x in DG_pi]])

# observed
Qe = koide(POLE_E)
re_, de = brannen(POLE_E)
mt_hi = POLE_E.copy(); mt_hi[2] += DTAU
Qe_hi = koide(mt_hi); _, de_hi = brannen(mt_hi)
print(f"leptons (pole): Q = {Qe:.8f}, |Q-2/3| = {abs(Qe-2/3):.2e} (1-sigma tau shift moves Q by {abs(Qe_hi-Qe):.1e})")
print(f"   Brannen r = {re_:.6f} (sqrt2 = {np.sqrt(2):.6f}), delta = {de:.8f} rad, |delta-2/9| = {abs(de-2/9):.2e} "
      f"(tau 1-sigma moves delta by {abs(de_hi-de):.1e}); delta/pi = {de/np.pi:.6f}")
for label, data in (("MZ", MZ), ("LOW", LOW)):
    for key in SECTORS:
        r, d = brannen(data[key])
        print(f"   {label} {key}: Q = {koide(data[key]):.4f}, r = {r:.4f}, delta = {d:.4f} rad")

# random control: Q and delta coincidences under N1 (log-uniform on [m_e, m_t])
N = 1_000_000
lo, hi = np.log(MZ["e"][0]), np.log(MZ["u"][2])
M = np.exp(rng.uniform(lo, hi, size=(N, 3)))
Qr = koide(M)
rr, dr = brannen(M)
eps_Q = max(abs(Qe - 2 / 3), abs(Qe_hi - Qe))
eps_d = max(abs(de - 2 / 9), abs(de_hi - de))
hitQ = np.zeros(N, bool)
for q in qg:
    hitQ |= np.abs(Qr - q) <= eps_Q
pQ_single = np.mean(np.abs(Qr - 2 / 3) <= eps_Q)
pQ = hitQ.mean()
print(f"\nrandom N1 (n={N}): P(|Q-2/3| <= {eps_Q:.1e}) = {pQ_single:.2e}; any of {len(qg)} grammar Q = {pQ:.2e}")
# delta coincidence, conditional on Q near 2/3 is too rare to sample: use the delta distribution of all triples
hitD = np.zeros(N, bool)
for d in dg:
    hitD |= np.abs(dr - d) <= eps_d
pD_single = np.mean(np.abs(dr - 2 / 9) <= eps_d)
print(f"random N1: P(|delta-2/9| <= {eps_d:.1e}) = {pD_single:.2e}; any of {len(dg)} grammar deltas = {hitD.mean():.2e}")
print(f"trials-corrected joint (independence assumed, x3 sectors): p ~ {3*pQ*hitD.mean():.1e}")

# quarks: nearest grammar (Q, delta) point -> does it reproduce masses within x3?
GL = []
for q in qg:
    for d in dg:
        mm = brannen_masses(np.sqrt(6 * q - 2), d)
        if mm[0] > 1e-300:
            GL.append(np.log(mm))
GL = np.array(GL)
print(f"grammar (Q,delta) points with positive masses: {len(GL)}")


def grammar_fit(m):
    """best x-factor over grammar (Q, delta) with free mu."""
    y = np.log(np.sort(m))
    return (0.5 * np.ptp(y[None] - GL, axis=1)).min()


print()
for label, data in (("MZ", MZ), ("LOW", LOW)):
    for key in ("u", "d", "e"):
        print(f"   {label} {key}: best grammar (Q,delta) factor x{np.exp(grammar_fit(data[key])):.2f}")
n2 = 300
Mr = np.exp(rng.uniform(lo, hi, size=(n2, 3)))
fr = np.array([grammar_fit(m) for m in Mr])
print(f"random N1 triples (n={n2}): grammar (Q,delta) fit within x3: {np.mean(fr <= LN3):.3f}; within x1.1: {np.mean(fr <= np.log(1.1)):.3f}")
