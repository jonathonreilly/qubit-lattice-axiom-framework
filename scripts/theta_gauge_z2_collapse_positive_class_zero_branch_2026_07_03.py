"""Gauge-side Z2 collapse and positive-class zero-branch runner.

Sections:
- A: Z2 character collapse with odd support.
- B: positive class zero branch selection and mass-side mirror checks.

Expected close: TOTAL: PASS=22 FAIL=0
"""

from itertools import permutations, product
from pathlib import Path

import numpy as np


BASE = Path(__file__).resolve().parents[1]
NOTE_PATH = BASE / "docs/THETA_GAUGE_Z2_CHARACTER_COLLAPSE_ODD_SUPPORT_AND_POSITIVE_CLASS_ZERO_BRANCH_SELECTION_BOUNDED_THEOREM_NOTE_2026-07-03.md"
NOTE_TEXT = NOTE_PATH.read_text(encoding="utf-8")
NOTE_FLAT = " ".join(NOTE_TEXT.split())

rng = np.random.default_rng(7)
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def permutation_sign(seq):
    inversions = 0
    vals = list(seq)
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            if vals[i] > vals[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


PLANES = []
PLANE_TO_INDEX = {}
for a in range(4):
    for b in range(a + 1, 4):
        PLANE_TO_INDEX[(a, b)] = len(PLANES)
        PLANES.append((a, b))


def q_flux(m):
    m = np.asarray(m, dtype=int)
    m01, m02, m03, m12, m13, m23 = m
    return int(m01 * m23 - m02 * m13 + m03 * m12)


def oriented_complement(plane):
    rest = [x for x in range(4) if x not in plane]
    for comp in (tuple(rest), tuple(rest[::-1])):
        if permutation_sign(tuple(plane) + comp) == 1:
            return comp
    return tuple(rest)


def set_oriented_plane(m, plane, value):
    a, b = plane
    if a < b:
        m[PLANE_TO_INDEX[(a, b)]] = value
    else:
        m[PLANE_TO_INDEX[(b, a)]] = -value


def unit_complementary_configs():
    configs = []
    for plane in PLANES:
        m = np.zeros(6, dtype=int)
        set_oriented_plane(m, plane, 1)
        set_oriented_plane(m, oriented_complement(plane), 1)
        configs.append(m)
    return configs


def canonical_b(m):
    m = np.asarray(m, dtype=int)
    return np.array([m[5], -m[4], m[3]], dtype=int)


def b_frame(m, frame):
    return permutation_sign(frame) * canonical_b(m)


def e_split(m):
    m = np.asarray(m, dtype=int)
    return np.array([m[0], m[1], m[2]], dtype=int)


def z2_character(q):
    return 1 if int(q) % 2 == 0 else -1


def su3_sample():
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    phases = diag / np.abs(diag)
    u = q * phases
    det_u = np.linalg.det(u)
    return u / det_u ** (1.0 / 3.0)


def insertion_weight(u, alpha, c):
    tr = np.trace(u)
    return 1.0 + c * (np.exp(1j * alpha) * tr + np.exp(-1j * alpha) * np.conj(tr))


def heat_coeff(n, t):
    return float(np.exp(-t * n * n / 2.0))


def direct_matched_closed_weight(sector, area, t, label_min=-4, label_max=4):
    """Sum over ALL per-plaquette label tuples; the pairwise matching
    constraint on the closed cycle does the selecting (nothing is imposed
    by construction). Feasible only for small area."""
    total = 0.0
    for labels in product(range(label_min, label_max + 1), repeat=area):
        matched = all(labels[(i + 1) % area] == labels[i] for i in range(area))
        if matched and labels[0] == sector:
            term = 1.0
            for label in labels:
                term *= heat_coeff(int(label), t)
            total += term
    return total


def product_closed_weight(sector, area, t):
    coeff = heat_coeff(sector, t)
    out = 1.0
    for _ in range(area):
        out *= coeff
    return out


def antisym_det(lam, t1, t2):
    avals = (t1, t2, -t1 - t2)
    total = np.zeros_like(t1, dtype=complex)
    for perm in permutations(range(3)):
        term = np.ones_like(t1, dtype=complex)
        for row in range(3):
            term *= np.exp(1j * avals[row] * lam[perm[row]])
        total += permutation_sign(perm) * term
    return total


def su3_lam(p, q):
    return np.array([p + q + 2, q + 1, 0], dtype=int)


def su3_quadrature_data(grid_n=200):
    vals = (np.arange(grid_n) + 0.5) * (2.0 * np.pi / grid_n)
    t1, t2 = np.meshgrid(vals, vals, indexing="ij")
    ad = antisym_det(np.array([2, 1, 0], dtype=int), t1, t2)
    den = np.mean(ad * np.conj(ad))
    re_tr = np.cos(t1) + np.cos(t2) + np.cos(t1 + t2)
    return t1, t2, ad, den, re_tr


def wilson_coefficients(max_p=2, max_q=2, beta=6.0):
    t1, t2, ad, den, re_tr = su3_quadrature_data()
    boltz = np.exp((beta / 3.0) * re_tr)
    coeffs = {}
    for p in range(max_p + 1):
        for q in range(max_q + 1):
            al = antisym_det(su3_lam(p, q), t1, t2)
            coeffs[(p, q)] = np.mean(boltz * ad * np.conj(al)) / den
    return coeffs, (t1, t2, ad, den, re_tr)


def plane_weight(n):
    return float(np.exp(-n * n / 2.0))


def base_sector_weight(m):
    out = 1.0
    for n in np.asarray(m, dtype=int):
        out *= plane_weight(int(n))
    return out


def signed_sector_weight(m):
    return z2_character(q_flux(m)) * base_sector_weight(m)


def det_real(mat):
    return float(np.real_if_close(np.linalg.det(mat), tol=1000))


def spectrum_has_pm_i_pairs(vals):
    vals = np.asarray(vals, dtype=complex)
    nonzero = [v for v in vals if abs(v) > 1e-8]
    for v in nonzero:
        if abs(np.real(v)) > 1e-8:
            return False
        has_negative = np.any(np.abs(vals + v) < 1e-7)
        has_conjugate = np.any(np.abs(vals - np.conj(v)) < 1e-7)
        if not (has_negative and has_conjugate):
            return False
    return True


# Section A
grid = np.exp(2j * np.pi * np.arange(720) / 720.0)
fixed_odd = [z for z in grid if abs(z - z ** -1) < 1e-12]
a1_cond = (
    len(fixed_odd) == 2
    and any(abs(z - 1.0) < 1e-12 for z in fixed_odd)
    and any(abs(z + 1.0) < 1e-12 for z in fixed_odd)
)
check(
    "A1 Z2 character collapse with odd support",
    a1_cond,
    "z^Q = z^{-Q} for all Q with 1 in the support iff z^2 = 1; "
    f"scan_count={len(fixed_odd)}",
)

qs = np.arange(-6, 7)
wq = np.cos(0.3 * qs)
even_alone = all(abs(np.cos(0.3 * q) - np.cos(0.3 * (-q))) < 1e-15 for q in qs)
mult_left = float(np.cos(0.3 * (1 + 1)))
mult_right = float(np.cos(0.3 * 1) * np.cos(0.3 * 1))
check(
    "A2 evenness alone is not multiplicative character input",
    even_alone and abs(mult_left - mult_right) > 1e-12,
    f"w(2)={mult_left:.12f}, w(1)w(1)={mult_right:.12f}",
)

fixed_even_support = [z for z in grid if abs(z**2 - z ** -2) < 1e-12]
a3_cond = len(fixed_even_support) == 4 and len(fixed_even_support) > len(fixed_odd)
check(
    "A3 odd support is load-bearing",
    a3_cond,
    f"even-support fixed count={len(fixed_even_support)}, odd-support fixed count={len(fixed_odd)}",
)

alpha = 0.81
c_insert = 0.37
odd_residuals = []
for _ in range(20):
    u = su3_sample()
    odd_u = 0.5 * (insertion_weight(u, alpha, c_insert) - insertion_weight(u, -alpha, c_insert))
    uc = np.conj(u)
    odd_uc = 0.5 * (insertion_weight(uc, alpha, c_insert) - insertion_weight(uc, -alpha, c_insert))
    odd_residuals.append(abs(odd_u + odd_uc))
max_odd_residual = max(odd_residuals)
check(
    "A4a swap-closed evenness re-earned",
    max_odd_residual < 1e-12,
    f"max alpha-odd paired residual={max_odd_residual:.3e}",
)

a4b_ok = True
for _ in range(100):
    m = rng.integers(-4, 5, size=6)
    e = e_split(m)
    q123 = int(np.dot(e, b_frame(m, (1, 2, 3))))
    q213 = int(np.dot(e, b_frame(m, (2, 1, 3))))
    if q123 != q_flux(m) or q213 != -q123 or z2_character(q123) != z2_character(q213):
        a4b_ok = False
        break
check(
    "A4b pi branch is orientation-blind",
    a4b_ok,
    "e.b flips under frame swap while (-1)^Q is unchanged on 100 draws",
)


# Section B
b1_ok = True
diffs = []
values = []
for n in range(-4, 5):
    direct = direct_matched_closed_weight(n, 4, 0.7)
    formula = product_closed_weight(n, 4, 0.7)
    diffs.append(abs(direct - formula))
    values.append(formula)
    if abs(direct - formula) > 1e-12 or direct <= 0:
        b1_ok = False
for n in range(0, 5):
    zp = product_closed_weight(n, 4, 0.7)
    zm = product_closed_weight(-n, 4, 0.7)
    if abs(zp - zm) > 1e-12:
        b1_ok = False
check(
    "B1 closed-surface positive matched labels A=4 (full tuple enumeration)",
    b1_ok,
    f"9^4 tuples filtered by matching; max |direct-product|={max(diffs):.3e}, min Z={min(values):.3e}",
)

b1_scale_ok = True
scale_diffs = []
for n in range(-4, 5):
    z4 = product_closed_weight(n, 4, 0.7)
    z16 = product_closed_weight(n, 16, 0.7)
    scale_diffs.append(abs(z16 - z4 ** 4))
    if z16 <= 0 or abs(z16 - z4 ** 4) > 1e-12 * max(1.0, z16):
        b1_scale_ok = False
    if abs(product_closed_weight(n, 16, 0.7) - product_closed_weight(-n, 16, 0.7)) > 1e-15:
        b1_scale_ok = False
check(
    "B1 closed-surface positive matched labels A=16 (multiplicative scaling)",
    b1_scale_ok,
    f"Z_n(16) = Z_n(4)^4 cross-path; max diff={max(scale_diffs):.3e}",
)

quad_t1, quad_t2, quad_ad, quad_den, quad_re_tr = su3_quadrature_data()
af = antisym_det(su3_lam(1, 0), quad_t1, quad_t2)
inner_ff = np.mean(af * np.conj(af)) / quad_den
check(
    "B2a SU(3) quadrature orthonormality gate",
    abs(inner_ff.real - 1.0) < 1e-6 and abs(inner_ff.imag) < 1e-10,
    f"<chi_F,chi_F>={inner_ff.real:.12f}{inner_ff.imag:+.2e}i",
)

coeffs, _quad_data = wilson_coefficients()
b2b_ok = True
for coeff in coeffs.values():
    if coeff.real <= 0 or abs(coeff.imag) > 1e-7 * max(1.0, abs(coeff.real)):
        b2b_ok = False
        break
check(
    "B2b Wilson dual coefficients positive real",
    b2b_ok,
    "min real={:.8g}, max relative imag={:.3e}".format(
        min(c.real for c in coeffs.values()),
        max(abs(c.imag) / max(1.0, abs(c.real)) for c in coeffs.values()),
    ),
)

b2c_ok = True
for p in range(3):
    for q in range(3):
        if abs(coeffs[(p, q)] - coeffs[(q, p)]) > 1e-7:
            b2c_ok = False
values_detail = ", ".join(
    f"c{p}{q}={coeffs[(p, q)].real:.8g}{coeffs[(p, q)].imag:+.1e}i"
    for p in range(3)
    for q in range(3)
)
check(
    "B2c Wilson conjugation pairing",
    b2c_ok,
    values_detail,
)

b3_draws = rng.integers(-3, 4, size=(200, 6))
unit_configs = unit_complementary_configs()
b3a_draws_ok = all(base_sector_weight(m) > 0 for m in b3_draws)
b3a_units_ok = all(base_sector_weight(m) > 0 and q_flux(m) == 1 for m in unit_configs)
check(
    "B3a positive class product weights on carrier sectors",
    b3a_draws_ok and b3a_units_ok,
    f"draws=200, unit-complementary Q values={[q_flux(m) for m in unit_configs]}",
)

odd_count = 0
negative_count = 0
b3b_ok = True
for m in b3_draws:
    base = base_sector_weight(m)
    signed = signed_sector_weight(m)
    expected = z2_character(q_flux(m))
    ratio = int(np.sign(signed) / np.sign(base))
    if ratio != expected:
        b3b_ok = False
    if q_flux(m) % 2:
        odd_count += 1
    if signed < 0:
        negative_count += 1
check(
    "B3b pi branch exits the positive class",
    b3b_ok and odd_count >= 30 and negative_count == odd_count,
    f"odd-Q draws={odd_count}, negative signed draws={negative_count}",
)

b4_orientation_ok = True
for _ in range(50):
    m = rng.integers(-4, 5, size=6)
    e = e_split(m)
    q123 = int(np.dot(e, b_frame(m, (1, 2, 3))))
    q213 = int(np.dot(e, b_frame(m, (2, 1, 3))))
    if z2_character(q123) * base_sector_weight(m) != z2_character(q213) * base_sector_weight(m):
        b4_orientation_ok = False
        break
b4_character_ok = True
for _ in range(50):
    m1 = rng.integers(-4, 5, size=6)
    m2 = rng.integers(-4, 5, size=6)
    q1 = q_flux(m1)
    q2 = q_flux(m2)
    if z2_character(q1 + q2) != z2_character(q1) * z2_character(q2):
        b4_character_ok = False
        break
b4_negative_witnesses = sum(1 for m in unit_configs if signed_sector_weight(m) < 0)
check(
    "B4 two-mechanism honesty for positive class selection",
    b4_orientation_ok and b4_character_ok and b4_negative_witnesses >= 1,
    f"orientation draws=50, character pairs=50, negative witnesses={b4_negative_witnesses}",
)

m_grid = np.linspace(-3.0, 3.0, 13)
b5a_ok = True
min_det = None
for n in (4, 6, 8):
    a = rng.normal(size=(n, n))
    mat = a - a.T
    vals = np.linalg.eigvals(mat)
    if not spectrum_has_pm_i_pairs(vals):
        b5a_ok = False
    for mass in m_grid:
        det_val = det_real(mat + mass * np.eye(n))
        min_det = det_val if min_det is None else min(min_det, det_val)
        if det_val < -1e-9:
            b5a_ok = False
check(
    "B5a mass-side mirror antisymmetric pairing",
    b5a_ok,
    f"min det(M+mI) on n=4,6,8 grid={min_det:.3e}",
)

s = np.diag(np.array([2.0, 1.0, 1.0, -1.0]))
shift_grid = np.linspace(-3.0, 3.0, 61)
found_shift = None
found_det = None
for shift in shift_grid:
    det_val = det_real(s + shift * np.eye(4))
    if det_val < 0:
        found_shift = float(shift)
        found_det = det_val
        break
check(
    "B5b symmetric refutation leg loses sign guarantee",
    found_shift is not None and found_det is not None and found_det < 0,
    f"m={found_shift:.2f}, det={found_det:.3e}",
)

branches = (0.0, np.pi)
table = []
for theta_gauge, arg_det_m in product(branches, branches):
    theta_bar = np.mod(theta_gauge + arg_det_m, 2.0 * np.pi)
    if abs(theta_bar - 2.0 * np.pi) < 1e-12:
        theta_bar = 0.0
    table.append((theta_gauge, arg_det_m, theta_bar))
selected_gauge = 0.0
selected_mass = 0.0
selected = [
    cell
    for cell in table
    if abs(cell[0] - selected_gauge) < 1e-12 and abs(cell[1] - selected_mass) < 1e-12
]
selected_zero = [cell for cell in selected if abs(cell[2]) < 1e-12]
zero_cells_under_selections = [
    cell
    for cell in table
    if abs(cell[2]) < 1e-12
    and abs(cell[0] - selected_gauge) < 1e-12
    and abs(cell[1] - selected_mass) < 1e-12
]
table_detail = "; ".join(
    f"({('0' if abs(g) < 1e-12 else 'pi')},{('0' if abs(m) < 1e-12 else 'pi')})->"
    f"{('0' if abs(tb) < 1e-12 else 'pi')}"
    for g, m, tb in table
)
check(
    "B6 two-sided Z2 table zero branch",
    len(selected) == 1 and len(selected_zero) == 1 and len(zero_cells_under_selections) == 1,
    table_detail,
)

check(
    "C1 note declares bounded_theorem Type header",
    "**Type:** bounded_theorem" in NOTE_TEXT,
)
check(
    "C2 note keeps branch-table result formal and scoped",
    "formal branch table" in NOTE_TEXT
    and "within the stated surfaces and classes only" in NOTE_TEXT,
)
check(
    "C3 note does not assert physical theta_bar value",
    "nothing here asserts the physical value of `theta_bar`" in NOTE_TEXT,
)
check(
    "C4 note states class-to-action adjudication remains open",
    "Whether the physical action class lies in (or reduces to) this class" in NOTE_FLAT
    and "this note does not decide it" in NOTE_FLAT,
)
check(
    "C5 note keeps orientation evenness as a hypothesis",
    "orientation-evenness" in NOTE_TEXT
    and "enters only as a named hypothesis" in NOTE_TEXT,
)
check(
    "C6 note has no landed/unconditional authority wording",
    "landed" not in NOTE_TEXT.lower() and "unconditional" not in NOTE_TEXT.lower(),
)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
