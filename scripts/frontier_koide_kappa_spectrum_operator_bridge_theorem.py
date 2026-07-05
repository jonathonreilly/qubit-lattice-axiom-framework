"""
Frontier runner — Koide kappa spectrum-operator bridge theorem.

Companion to
`docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`.

Claim.  On the cyclic-compression bridge
`H = a I + b C + bbar C^2  <->  circulant operator with Fourier eigenvalues
a_0, z, zbar`, the exact symbolic identity

    a_0^2 - 2 |z|^2  =  3 (a^2 - 2 |b|^2)

holds identically on Herm_circ(3). Therefore spectrum-side Koide
`Q = 2/3` (equivalently `a_0^2 = 2 |z|^2`) IS operator-side `kappa = 2`
(equivalently `a^2 = 2 |b|^2`). No independent operator-side primitive
is needed once the spectrum-side condition is supplied.

Tasks exercised by the runner (T1 .. T9) use sympy for the symbolic
bridge identity, a numerical realization at PDG charged-lepton masses,
and a random-matrix family scan to rule out coincidence. Every PASS is
keyed to a substantive computation; there are no hard-coded True values.

  T1 Hermitian circulant construction is algebraically closed
  T2 Eigenvalues lam_k = a + b omega^k + bbar omega^{-k} are real
  T3 Bridge  a_0 = sqrt(3) a  (exact symbolic)
  T4 Bridge  |z|^2 = 3 |b|^2  (exact symbolic)
  T5 Bridge identity a_0^2 - 2|z|^2 = 3 (a^2 - 2 |b|^2)  (exact symbolic)
  T6 PDG charged-lepton Q ~ 2/3
  T7 PDG numerical kappa = a^2/|b|^2 ~ 2
  T8 Bridge holds pointwise on 200 random Herm_circ(3) samples
  T9 Bridge residual collapses Koide-condition equivalence
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
BRIDGE_NOTE = ROOT / "docs" / "KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md"
DEMOTION_NOTE = ROOT / "docs" / "KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md"


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return cond


def normalize(text: str) -> str:
    return " ".join(text.split()).lower()


# ---------------------------------------------------------------------------
# T1 / T2 — Hermitian circulant construction and real eigenvalues
# ---------------------------------------------------------------------------

print("Section A — symbolic Hermitian circulant and Fourier bridge")

a_sym = sp.symbols("a", real=True)
b1_sym, b2_sym = sp.symbols("b1 b2", real=True)
b_sym = b1_sym + sp.I * b2_sym

omega = sp.exp(2 * sp.pi * sp.I / 3)
C = sp.Matrix(
    [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]
)
I3 = sp.eye(3)

H_sym = a_sym * I3 + b_sym * C + sp.conjugate(b_sym) * (C ** 2)

# T1 — Hermiticity symbolic
Hdag = H_sym.H
check(
    "T1 Hermitian circulant: H = H^H symbolically",
    sp.simplify(H_sym - Hdag) == sp.zeros(3, 3),
)

# Eigenvalues of the cyclic-compression bridge
lam = []
for k in range(3):
    lk = a_sym + b_sym * omega ** k + sp.conjugate(b_sym) * sp.conjugate(omega ** k)
    lam.append(sp.simplify(lk))

# T2 — eigenvalues are real
t2_real = all(sp.simplify(sp.im(lk)) == 0 for lk in lam)
check(
    "T2 Fourier eigenvalues lam_k are real",
    t2_real,
    detail=f"lam_k = {[sp.simplify(sp.re(lk)) for lk in lam]}",
)

lam_r = [sp.simplify(sp.re(lk)) for lk in lam]

# ---------------------------------------------------------------------------
# T3 / T4 / T5 — exact symbolic bridge identities
# ---------------------------------------------------------------------------

sqrt3 = sp.sqrt(3)
a0 = sp.simplify((lam_r[0] + lam_r[1] + lam_r[2]) / sqrt3)
z = sp.simplify((lam_r[0] + sp.conjugate(omega) * lam_r[1] + omega * lam_r[2]) / sqrt3)
z_mag_sq = sp.simplify(sp.re(z) ** 2 + sp.im(z) ** 2)

check(
    "T3 bridge a_0 = sqrt(3) * a  (symbolic)",
    sp.simplify(a0 - sqrt3 * a_sym) == 0,
    detail=f"a_0 = {a0}",
)

check(
    "T4 bridge |z|^2 = 3 |b|^2  (symbolic)",
    sp.simplify(z_mag_sq - 3 * (b1_sym ** 2 + b2_sym ** 2)) == 0,
    detail=f"|z|^2 = {z_mag_sq}",
)

lhs_spectrum = sp.simplify(a0 ** 2 - 2 * z_mag_sq)
rhs_operator = 3 * (a_sym ** 2 - 2 * (b1_sym ** 2 + b2_sym ** 2))
check(
    "T5 bridge identity a_0^2 - 2|z|^2 = 3 (a^2 - 2 |b|^2)",
    sp.simplify(lhs_spectrum - rhs_operator) == 0,
)

# T6 — exact cubic trace diagnostic used by the MRU demotion note.
tr_h3 = sp.expand(sp.trace(H_sym ** 3))
phase_piece = sp.expand(tr_h3 - 3 * a_sym ** 3 - 18 * a_sym * (b1_sym ** 2 + b2_sym ** 2))
expected_phase_piece = sp.expand(3 * (b_sym ** 3 + sp.conjugate(b_sym) ** 3))
obsolete_phase_piece = sp.expand(a_sym * (b_sym ** 3 + sp.conjugate(b_sym) ** 3))
check(
    "T6 tr(H^3) phase term is 3(b^3+bbar^3), not a(b^3+bbar^3)",
    sp.simplify(phase_piece - expected_phase_piece) == 0
    and sp.simplify(phase_piece - obsolete_phase_piece) != 0,
    detail=f"phase piece = {sp.simplify(phase_piece)}",
)

# ---------------------------------------------------------------------------
# T7 / T8 — PDG numerical realization
# ---------------------------------------------------------------------------

print("\nSection B — PDG charged-lepton numerical realization")

m_e = 0.51099895000
m_mu = 105.6583755
m_tau = 1776.86
v = np.array([math.sqrt(m_e), math.sqrt(m_mu), math.sqrt(m_tau)])

Q_num = float(np.sum(v ** 2) / np.sum(v) ** 2)
check(
    "T7 PDG Koide Q ~ 2/3",
    abs(Q_num - 2.0 / 3.0) < 3e-5,
    detail=f"Q = {Q_num:.8f}",
)

w = np.exp(2j * np.pi / 3)
a_op = float(np.sum(v) / 3.0)
b_op = (v[0] + np.conj(w) * v[1] + w * v[2]) / 3.0
kappa_num = (a_op ** 2) / abs(b_op) ** 2
check(
    "T8 PDG operator-side kappa = a^2/|b|^2 ~ 2",
    abs(kappa_num - 2.0) < 3e-4,
    detail=f"kappa = {kappa_num:.8f}",
)

# ---------------------------------------------------------------------------
# T9 — bridge holds pointwise on random Herm_circ(3) samples
# ---------------------------------------------------------------------------

print("\nSection C — random Herm_circ(3) sample scan")

rng = np.random.default_rng(20260419)
max_residual = 0.0
N_samples = 200

for _ in range(N_samples):
    a_val = float(rng.normal())
    b_val = complex(rng.normal(), rng.normal())
    lam_vec = np.array(
        [a_val + b_val * w ** k + np.conj(b_val) * np.conj(w ** k) for k in range(3)]
    )
    # Force real projection — should already be real up to numerical error
    lam_vec = lam_vec.real
    a0_n = np.sum(lam_vec) / math.sqrt(3.0)
    z_n = (lam_vec[0] + np.conj(w) * lam_vec[1] + w * lam_vec[2]) / math.sqrt(3.0)
    lhs = a0_n ** 2 - 2 * abs(z_n) ** 2
    rhs = 3 * (a_val ** 2 - 2 * abs(b_val) ** 2)
    max_residual = max(max_residual, abs(lhs - rhs))

check(
    "T9 bridge identity holds on 200 random samples (max residual < 1e-10)",
    max_residual < 1e-10,
    detail=f"max residual = {max_residual:.3e}",
)

# ---------------------------------------------------------------------------
# T10 — condition-equivalence
# ---------------------------------------------------------------------------

print("\nSection D — condition equivalence under bridge")

# Check that: spectrum-side Koide Q = 2/3 iff operator-side kappa = 2.
# We test by sampling values that satisfy one side and verify they satisfy the other.

# Pick b, solve for a so that a^2 = 2 |b|^2 (operator-side kappa = 2).
for trial in range(50):
    b_val = complex(rng.normal(), rng.normal())
    a_val = math.sqrt(2.0 * abs(b_val) ** 2)
    lam_vec = np.array(
        [a_val + b_val * w ** k + np.conj(b_val) * np.conj(w ** k) for k in range(3)]
    ).real
    a0_n = np.sum(lam_vec) / math.sqrt(3.0)
    z_n = (lam_vec[0] + np.conj(w) * lam_vec[1] + w * lam_vec[2]) / math.sqrt(3.0)
    spec_residual = a0_n ** 2 - 2 * abs(z_n) ** 2
    if abs(spec_residual) > 1e-10:
        break
else:
    spec_residual = 0.0

check(
    "T10 operator kappa = 2 implies spectrum a_0^2 = 2|z|^2 (zero residual on sample set)",
    abs(spec_residual) < 1e-10,
    detail=f"|spectrum residual| = {abs(spec_residual):.3e}",
)

# ---------------------------------------------------------------------------
# T11 .. T15 — source-boundary checks for the MRU demotion note
# ---------------------------------------------------------------------------

print("\nSection E — MRU demotion source-boundary checks")

demotion_note = DEMOTION_NOTE.read_text(encoding="utf-8")
demotion_norm = normalize(demotion_note)
bridge_note = BRIDGE_NOTE.read_text(encoding="utf-8")
bridge_norm = normalize(bridge_note)

check(
    "T11 demotion note records the 2026-06-18 source-boundary repair",
    "## 2026-06-18 source-boundary repair" in demotion_note,
)
check(
    "T12 clean claim is bounded demotion / bridge-corollary support",
    "bounded demotion / bridge-corollary" in demotion_norm
    and "primary exact bridge-corollary route" in demotion_norm,
)
check(
    "T13 block-total route is bounded support, not standalone closure",
    "independent bounded support" in demotion_norm
    and "not a standalone full physical scalar-measure closure theorem" in demotion_norm,
)
check(
    "T14 demotion note prints the corrected cubic trace diagnostic",
    "tr(h^3) = 3 a^3 + 18 a |b|^2 + 3 (b^3 + bbar^3)" in demotion_norm
    and "not to `a (b^3 + bbar^3)`" in demotion_norm,
)
check(
    "T15 demotion note removes old retained-route overclaim phrases",
    "primary retained closure route" not in demotion_norm
    and "two retained independent routes" not in demotion_norm
    and "independent second closure route" not in demotion_norm,
)
check(
    "T16 demotion note narrows the SO(2) quotient failure to Path A",
    "path a cannot close" in demotion_norm
    and "displayed spectral-observable route" in demotion_norm
    and "checks path a only" in demotion_norm,
)
check(
    "T17 demotion note leaves alternative quotient attack routes open",
    "other attack routes" in demotion_norm
    and "remain open, not closed" in demotion_norm
    and "alternative attack routes remain open" in demotion_norm
    and "no currently retained framework theorem delivers it" not in demotion_norm
    and "not a corollary of any retained framework theorem currently" not in demotion_norm,
)
check(
    "T18 bridge note declares bounded_theorem source claim type",
    "**Type:** bounded_theorem" in bridge_note
    and "**Claim type:** bounded_theorem" in bridge_note
    and "bounded bridge-corollary support" in bridge_norm,
)
check(
    "T19 bridge note removes retained-proposal and independent-closure overclaim phrases",
    ("proposed_" + "retained positive theorem") not in bridge_norm
    and "second independent closure route" not in bridge_norm
    and "closure comes free" not in bridge_norm
    and "does not independently derive the spectrum-side koide condition" in bridge_norm
    and "does not apply or predict an audit verdict" in bridge_norm,
)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL > 0:
    raise SystemExit(1)
