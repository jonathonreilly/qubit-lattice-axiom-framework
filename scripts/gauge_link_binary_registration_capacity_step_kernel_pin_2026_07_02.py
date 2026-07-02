"""Gauge-link binary registration capacity pins the native step kernel.

Source-side disclaimer: this runner checks the source note's finite algebra,
grid identities, and independent Monte Carlo discriminator. It does not set,
predict, or apply any audit verdict.

Summary:
S1. A one-site M_2(C) possibility domain supports at most a binary pointer
    partition per record step, and channel pullback cannot increase the number
    of cells.
S2. The native link carrier saturates that binary capacity with its 3+1 central
    split, so the nontrivial per-informative-step kernel is pinned to T_V.
S3. The exact composed family has m2(k) = m2_H + (2/27) * 16^(1-k), stays above
    the unit point, and is cross-checked by independent matrix sampling.
S4. The remaining rate dial is the informative-step fraction p, with p* located
    but not forced.
"""

from fractions import Fraction
from pathlib import Path

import numpy as np


SEED = 20260702
ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
TWOPI = 2.0 * np.pi


def check(name, condition, detail=""):
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def require(name, condition, detail=""):
    check(name, condition, detail)


def dagger(x):
    return x.conj().T


def wrap_pi(x):
    return (x + np.pi) % TWOPI - np.pi


def matrix_rank_projector(p, tol=1e-9):
    vals = np.linalg.eigvalsh((p + dagger(p)) / 2.0)
    return int(np.sum(vals > tol))


def random_unitary(n, rng):
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    phases = d / np.where(np.abs(d) == 0, 1.0, np.abs(d))
    return q * phases


def random_su3(rng):
    coeff = rng.normal(size=8)
    h = np.zeros((3, 3), dtype=complex)
    for c, t in zip(coeff, gell_mann_generators()):
        h += c * t
    vals, vecs = np.linalg.eigh(h)
    u = vecs @ np.diag(np.exp(1j * vals)) @ dagger(vecs)
    det_phase = np.angle(np.linalg.det(u))
    return u / np.exp(1j * det_phase / 3.0)


def gell_mann_generators():
    z = np.zeros((3, 3), dtype=complex)
    mats = []
    m = z.copy()
    m[0, 1] = m[1, 0] = 1
    mats.append(m)
    m = z.copy()
    m[0, 1] = -1j
    m[1, 0] = 1j
    mats.append(m)
    m = z.copy()
    m[0, 0] = 1
    m[1, 1] = -1
    mats.append(m)
    m = z.copy()
    m[0, 2] = m[2, 0] = 1
    mats.append(m)
    m = z.copy()
    m[0, 2] = -1j
    m[2, 0] = 1j
    mats.append(m)
    m = z.copy()
    m[1, 2] = m[2, 1] = 1
    mats.append(m)
    m = z.copy()
    m[1, 2] = -1j
    m[2, 1] = 1j
    mats.append(m)
    m = z.copy()
    m[0, 0] = 1 / np.sqrt(3)
    m[1, 1] = 1 / np.sqrt(3)
    m[2, 2] = -2 / np.sqrt(3)
    mats.append(m)
    return [m / 2.0 for m in mats]


def swap_split_basis_4():
    s = np.zeros((4, 4), dtype=complex)
    s[:, 0] = np.array([1, 0, 0, 0], dtype=complex)
    s[:, 1] = np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2.0)
    s[:, 2] = np.array([0, 0, 0, 1], dtype=complex)
    s[:, 3] = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2.0)
    return s


def embed_triplet_4(a3, singlet_value=0.0):
    block = np.zeros((4, 4), dtype=complex)
    block[:3, :3] = a3
    block[3, 3] = singlet_value
    s = swap_split_basis_4()
    return s @ block @ dagger(s)


def rho8(u3):
    return np.kron(embed_triplet_4(u3, 1.0), np.eye(2, dtype=complex))


def native_projectors():
    casimir = np.zeros((8, 8), dtype=complex)
    for t in gell_mann_generators():
        gen = np.kron(embed_triplet_4(t, 0.0), np.eye(2, dtype=complex))
        casimir += gen @ gen
    p3 = 0.75 * casimir
    p3 = (p3 + dagger(p3)) / 2.0
    p1 = np.eye(8, dtype=complex) - p3
    return p3, p1, casimir


def vectorize_row_major(x):
    return x.reshape(-1)


def grid_integrals(m, want_s2=True):
    xs = (np.arange(m, dtype=float) + 0.5) * (TWOPI / m) - np.pi
    totals = {
        "density": 0.0,
        "chi8_s2_naive": 0.0,
        "s2_naive": 0.0,
        "chi8_s2_min": 0.0,
        "s2_min": 0.0,
        "chi8": 0.0,
        "chi8_sq": 0.0,
    }
    chunk = 256
    for start in range(0, m, chunk):
        a = xs[start : start + chunk][:, None]
        b = xs[None, :]
        c = wrap_pi(-a - b)
        cab = np.cos(a - b)
        cac = np.cos(a - c)
        cbc = np.cos(b - c)
        chi3_abs2 = 3.0 + 2.0 * (cab + cac + cbc)
        chi8 = chi3_abs2 - 1.0
        density = ((2.0 - 2.0 * cab) * (2.0 - 2.0 * cac) * (2.0 - 2.0 * cbc)) / 6.0
        totals["density"] += float(np.sum(density))
        totals["chi8"] += float(np.sum(density * chi8))
        totals["chi8_sq"] += float(np.sum(density * chi8 * chi8))
        if want_s2:
            s2_naive = a * a + b * b + c * c
            phase_sum = a + b + c
            q = np.rint(phase_sum / TWOPI).astype(int)
            s2_min = s2_naive.copy()
            max_phase = np.maximum(np.maximum(a, b), c)
            min_phase = np.minimum(np.minimum(a, b), c)
            s2_min = np.where(q == 1, s2_naive + TWOPI * TWOPI - 2.0 * TWOPI * max_phase, s2_min)
            s2_min = np.where(q == -1, s2_naive + TWOPI * TWOPI + 2.0 * TWOPI * min_phase, s2_min)
            totals["s2_naive"] += float(np.sum(density * s2_naive))
            totals["chi8_s2_naive"] += float(np.sum(density * chi8 * s2_naive))
            totals["s2_min"] += float(np.sum(density * s2_min))
            totals["chi8_s2_min"] += float(np.sum(density * chi8 * s2_min))
    norm = float(m * m)
    return {k: v / norm for k, v in totals.items()}


def b2_identity_grid(m):
    xs = (np.arange(m, dtype=float) + 0.5) * (TWOPI / m) - np.pi
    max_diff = 0.0
    chunk = 256
    for start in range(0, m, chunk):
        a = xs[start : start + chunk][:, None]
        b = xs[None, :]
        c = wrap_pi(-a - b)
        chi3 = np.exp(1j * a) + np.exp(1j * b) + np.exp(1j * c)
        left = (np.abs(chi3) ** 2 + 1.0) / 2.0
        chi8 = 2.0 + 2.0 * (np.cos(a - b) + np.cos(a - c) + np.cos(b - c))
        right = 1.0 + chi8 / 2.0
        max_diff = max(max_diff, float(np.max(np.abs(left - right))))
    return max_diff


def batched_haar_su3(n, rng):
    z = rng.normal(size=(n, 3, 3)) + 1j * rng.normal(size=(n, 3, 3))
    q, r = np.linalg.qr(z)
    d = np.diagonal(r, axis1=1, axis2=2)
    phases = d / np.where(np.abs(d) == 0, 1.0, np.abs(d))
    q = q * phases[:, None, :]
    det_phase = np.angle(np.linalg.det(q))
    q = q / np.exp(1j * det_phase / 3.0)[:, None, None]
    return q


def tv_kernel_from_mats(u):
    tr = np.trace(u, axis1=1, axis2=2)
    return (np.abs(tr) ** 2 + 1.0) / 2.0


def sample_tv_su3(count, rng):
    out = np.empty((count, 3, 3), dtype=complex)
    filled = 0
    proposals = 0
    chunk = 50000
    while filled < count:
        u = batched_haar_su3(chunk, rng)
        t = tv_kernel_from_mats(u)
        accept = rng.random(chunk) < (t / 5.0)
        got = int(np.sum(accept))
        if got:
            take = min(got, count - filled)
            out[filled : filled + take] = u[accept][:take]
            filled += take
        proposals += chunk
    print(f"  rejection sampling accepted {count} from {proposals} Haar proposals")
    return out


def s2_zero_sum_min_from_phases(phases):
    s2 = np.sum(phases * phases, axis=1)
    q = np.rint(np.sum(phases, axis=1) / TWOPI).astype(int)
    max_phase = np.max(phases, axis=1)
    min_phase = np.min(phases, axis=1)
    s2 = np.where(q == 1, s2 + TWOPI * TWOPI - 2.0 * TWOPI * max_phase, s2)
    s2 = np.where(q == -1, s2 + TWOPI * TWOPI + 2.0 * TWOPI * min_phase, s2)
    return s2


def monte_carlo_composition_m2(target):
    rng = np.random.default_rng(SEED + 404)
    n_pairs = 200000
    accepted = sample_tv_su3(2 * n_pairs, rng)
    x1 = accepted[:n_pairs]
    x2 = accepted[n_pairs:]
    products = x1 @ x2
    eig = np.linalg.eigvals(products)
    phases = np.angle(eig)
    s2 = s2_zero_sum_min_from_phases(phases)
    estimate = float(np.mean(s2) / 4.0)
    print(f"  MC m2(2) estimate {estimate:.12f}; closed target {target:.12f}")
    del accepted, x1, x2, products, eig, phases, s2
    return estimate


def section_a(rng):
    print("\nSECTION A -- capacity lemmas")
    ok = True
    seen = set()
    no_room = True
    for _ in range(24):
        v = rng.normal(size=2) + 1j * rng.normal(size=2)
        v = v / np.linalg.norm(v)
        p = np.outer(v, v.conj())
        r1 = matrix_rank_projector(p)
        r2 = matrix_rank_projector(np.eye(2) - p)
        ranks = tuple(sorted((r1, r2), reverse=True))
        seen.add(ranks)
        ok = ok and ranks in {(1, 1), (2, 0)}
        # a third nonzero cell would need rank inside the joint orthocomplement,
        # whose dimension is 2 - r1 - r2 (computed, not asserted)
        no_room = no_room and (2 - r1 - r2 == 0)
    for p in (np.zeros((2, 2), dtype=complex), np.eye(2, dtype=complex)):
        r1 = matrix_rank_projector(p)
        r2 = matrix_rank_projector(np.eye(2) - p)
        ranks = tuple(sorted((r1, r2), reverse=True))
        seen.add(ranks)
        ok = ok and ranks in {(1, 1), (2, 0)}
        no_room = no_room and (2 - r1 - r2 == 0)
    require("A1-seeded-binary-partitions", ok, f"observed sorted rank pairs {sorted(seen)}")
    require(
        "A1-no-room-for-third-cell",
        no_room,
        "computed orthocomplement dimension 2 - rank(P) - rank(I-P) is 0 for every partition",
    )

    basis = np.eye(3, dtype=complex)
    ps = [np.outer(basis[:, i], basis[:, i].conj()) for i in range(3)]
    c3_ok = all(matrix_rank_projector(p) == 1 for p in ps) and np.allclose(sum(ps), np.eye(3))
    require("A1-C3-discriminating-contrast", c3_ok, "three rank-1 cells sum to I_3")

    v = random_unitary(4, rng)
    w = random_unitary(2, rng)
    p = np.outer(w[:, 0], w[:, 0].conj())
    e0 = dagger(v) @ np.kron(p, np.eye(2)) @ v
    e1 = dagger(v) @ np.kron(np.eye(2) - p, np.eye(2)) @ v
    require("A2-pullback-povm-sum", np.linalg.norm(e0 + e1 - np.eye(4)) < 1e-12, "two pulled-back cells sum to I_4")
    mineig = min(float(np.min(np.linalg.eigvalsh((e0 + dagger(e0)) / 2.0))), float(np.min(np.linalg.eigvalsh((e1 + dagger(e1)) / 2.0))))
    require("A2-pullback-positive-counting", mineig > -1e-12, f"min pulled-back effect eigenvalue {mineig:.3e}; count <= 2 by construction")


def section_b(rng):
    print("\nSECTION B -- native carrier, collapse, pin")
    p3, p1, casimir = native_projectors()
    vals = np.sort(np.real(np.linalg.eigvalsh((casimir + dagger(casimir)) / 2.0)))
    target = np.array([0.0, 0.0] + [4.0 / 3.0] * 6)
    require("B0-casimir-spectrum", np.max(np.abs(vals - target)) < 1e-12, f"spectrum {np.round(vals, 12)}")

    projectors = [p3, p1]
    max_one_two = 0.0
    max_formula = 0.0
    for _ in range(6):
        u = random_su3(rng)
        w = random_su3(rng)
        ru = rho8(u)
        rw = rho8(w)
        vu = vectorize_row_major(ru)
        vw = vectorize_row_major(rw)
        one = 0.0
        two = 0.0
        for pi in projectors:
            amp = np.vdot(vu, np.kron(pi, np.eye(8)) @ vw)
            one += float(np.abs(amp) ** 2)
            for pj in projectors:
                amp2 = np.vdot(vu, np.kron(pi, pj.T) @ vw)
                two += float(np.abs(amp2) ** 2)
        chi3 = np.trace(dagger(u) @ w)
        formula = float(np.abs(2.0 * chi3) ** 2 + np.abs(2.0) ** 2)
        max_one_two = max(max_one_two, abs(one - two))
        max_formula = max(max_formula, abs(one - formula), abs(two - formula))
    require("B1-one-sided-two-sided-collapse", max_one_two < 1e-10, f"max difference {max_one_two:.3e}")
    require("B1-closed-character-formula", max_formula < 1e-10, f"max formula difference {max_formula:.3e}")

    diff = b2_identity_grid(1600)
    require("B2-pinned-TV-grid-identity", diff < 1e-12, f"max grid difference {diff:.3e}")


def section_c():
    print("\nSECTION C -- exact identities")
    g1600 = grid_integrals(1600)
    g3200 = grid_integrals(3200)

    c1_target = float(Fraction(4, 9))
    c1_e1600 = abs(g1600["chi8_s2_naive"] - c1_target)
    c1_e3200 = abs(g3200["chi8_s2_naive"] - c1_target)
    print(f"  <chi8 s2_naive> M1600={g1600['chi8_s2_naive']:.12f} M3200={g3200['chi8_s2_naive']:.12f}")
    require("C1-chi8-s2-naive-anchor", c1_e3200 < 5e-11, f"error {c1_e3200:.3e}")
    require("C1-chi8-s2-naive-converges", c1_e3200 < c1_e1600, f"errors {c1_e1600:.3e} -> {c1_e3200:.3e}")

    c2_target = np.pi * np.pi - float(Fraction(4, 9))
    c2_e1600 = abs(g1600["s2_naive"] - c2_target)
    c2_e3200 = abs(g3200["s2_naive"] - c2_target)
    print(f"  <s2_naive> M1600={g1600['s2_naive']:.12f} M3200={g3200['s2_naive']:.12f}")
    require("C2-s2-naive-pi2-anchor", c2_e3200 < 5e-11, f"error {c2_e3200:.3e}")
    require("C2-s2-naive-converges", c2_e3200 < c2_e1600, f"errors {c2_e1600:.3e} -> {c2_e3200:.3e}")

    c3_target = float(Fraction(16, 27))
    c3_e1600 = abs(g1600["chi8_s2_min"] - c3_target)
    c3_e3200 = abs(g3200["chi8_s2_min"] - c3_target)
    print(f"  <chi8 s2_min> M1600={g1600['chi8_s2_min']:.12f} M3200={g3200['chi8_s2_min']:.12f}")
    require("C3-chi8-s2-min-anchor", c3_e3200 < 5e-12, f"error {c3_e3200:.3e}")
    require("C3-chi8-s2-min-converges", c3_e3200 < c3_e1600, f"errors {c3_e1600:.3e} -> {c3_e3200:.3e}")

    print(f"  <s2_min>_Haar M3200={g3200['s2_min']:.12f}")
    require("C4-s2-min-haar-anchor", abs(g3200["s2_min"] - 9.466227112) < 1e-8, f"value {g3200['s2_min']:.12f}")
    m2_haar = g3200["s2_min"] / 4.0
    require("C4-m2-haar-anchor", abs(m2_haar - 2.366557) < 3e-6, f"value {m2_haar:.12f}")

    require("C5-density-M1600", abs(g1600["density"] - 1.0) < 1e-9, f"value {g1600['density']:.12f}")
    require("C5-density-M3200", abs(g3200["density"] - 1.0) < 1e-9, f"value {g3200['density']:.12f}")
    return g3200, m2_haar


def section_d(g3200, m2_haar):
    print("\nSECTION D -- composed family and unreachability")
    values = []
    for k in range(1, 7):
        values.append(m2_haar + float(Fraction(2, 27)) * (16.0 ** (1 - k)))
    for k, value in enumerate(values, start=1):
        print(f"  m2({k}) = {value:.12f}")
    require("D1-closed-form-m2-native", abs(values[0] - 2.440631) < 2e-6, f"m2(1) {values[0]:.12f}")

    w8 = (g3200["chi8"] + 0.5 * g3200["chi8_sq"]) / 8.0
    require("D2-w8-TV", abs(w8 - float(Fraction(1, 16))) < 1e-9, f"w8 {w8:.12f}")
    require("D2-k2-eigenvalue-power", abs(w8 * w8 - float(Fraction(1, 16 * 16))) < 1e-9, f"w8^2 {w8*w8:.12f}")

    target_k2 = m2_haar + float(Fraction(2, 27 * 16))
    mc = monte_carlo_composition_m2(target_k2)
    require("D3-independent-MC-composition-k2", abs(mc - target_k2) < 1.5e-2, f"difference {abs(mc - target_k2):.6f}")

    require("D4-first-six-above-2p36", min(values) > 2.36, f"min {min(values):.12f}")
    require("D4-monotone-decreasing", all(values[i] > values[i + 1] for i in range(len(values) - 1)), "strictly decreasing for k=1..6")
    margin = values[-1] - 1.0
    require("D4-unit-margin", margin > 1.0, f"m2(6)-1 = {margin:.12f}")
    return values


def section_e(g3200):
    print("\nSECTION E -- informative-fraction dial")
    s2_tv = g3200["s2_min"] + float(Fraction(8, 27))
    p_star = 4.0 / s2_tv
    print(f"  p_star = {p_star:.9f}")
    require("E1-p-star-anchor", abs(p_star - 0.409731) < 5e-6, f"value {p_star:.9f}")
    require("E2-p-star-interior", 0.0 < p_star < 1.0, "0 < p* < 1")
    require("E2-p-star-not-half", abs(p_star - 0.5) > 0.05, f"|p*-0.5| = {abs(p_star - 0.5):.9f}")
    require("E2-p-star-not-one", abs(p_star - 1.0) > 0.5, f"|p*-1| = {abs(p_star - 1.0):.9f}")
    require("E2-p-star-not-zero", p_star > 0.05, f"p* = {p_star:.9f}")
    print("  Dial discipline: p* located, not forced")

    lin_ok = True
    for p_frac in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        variance_p = float(p_frac) * s2_tv
        lin_ok = lin_ok and abs(variance_p - float(p_frac) * s2_tv) < 1e-12
    require(
        "E3-lazy-family-linearity (definitional: delta contributes zero variance)",
        lin_ok,
        "variance of (1-p) delta + p T_V equals p * <s2>_{T_V} at p in {1/4, 1/2, 3/4}",
    )


def flatten(text):
    return " ".join(text.split())


def require_contains(label, text, needle):
    require(label, needle in text, f"needle={needle!r}")


def require_absent(label, text, needle):
    require(label, needle not in text, f"needle={needle!r}")


def rel_path(path):
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def section_f():
    print("\nSECTION F -- source-boundary guards")
    note = ROOT / "docs" / "GAUGE_LINK_BINARY_REGISTRATION_CAPACITY_STEP_KERNEL_PIN_THEOREM_NOTE_2026-07-02.md"
    deps = {
        "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
        "graph-first": ROOT / "docs" / "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
        "rigidity": ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md",
        "controlled-copy": ROOT / "docs" / "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md",
        "semigroup": ROOT / "docs" / "RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md",
    }
    require("F0-note-exists", note.exists(), rel_path(note))
    for name, path in deps.items():
        require(f"F0-dep-exists-{name}", path.exists(), rel_path(path))

    dep_text = {name: flatten(path.read_text(encoding="utf-8")) for name, path in deps.items()}
    require_contains(
        "F1-axioms-qubit-clause",
        dep_text["axioms"],
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
    )
    require_contains("F1-axioms-record-clause", dep_text["axioms"], "a record locks exactly one local possibility")
    require_contains("F1-axioms-no-weights-clause", dep_text["axioms"], "transition probabilities or weights")
    require_contains("F1-graph-first-marker", dep_text["graph-first"], "the joint commutant has dimension `10`")
    require_contains("F1-rigidity-marker", dep_text["rigidity"], "no independent scalar-normalization freedom")
    require_contains("F1-controlled-copy-marker", dep_text["controlled-copy"], "projective record-write isometry")
    require_contains(
        "F1-semigroup-marker",
        dep_text["semigroup"],
        "continuous Markov semigroups live on the probability/ensemble",
    )

    note_raw = note.read_text(encoding="utf-8")
    note_flat = flatten(note_raw)
    preserve = [
        "set only by the independent audit lane",
        "binary",
        "pinned",
        "informative-step fraction",
        "located on the dial, not forced",
        "not a distinguished setting",
        "does not derive that a record step occurs",
        "not a citation-graph dependency",
        "does not claim:",
        "an audit verdict or any effective-status promotion",
        "16/27",
        "pi^2 - 4/9",
        "m^2(k) = m^2_Haar + (2/27) * 16^(1-k)",
        "p* = 4 / <s2>_T_V",
    ]
    for marker in preserve:
        require_contains(f"F2-note-marker: {marker[:48]}", note_flat, marker)

    runner_raw = Path(__file__).read_text(encoding="utf-8")
    combined = (note_raw + "\n" + runner_raw).lower()
    forbidden = [
        "audit" + "_" + "status:",
        "effective" + "_" + "status:",
        "only" + " " + "route",
        "exh" + "austed",
        "closes" + " " + "the" + " " + "route",
    ]
    bad = [needle for needle in forbidden if needle in combined]
    require("F3-forbidden-strings-absent", not bad, ", ".join(bad) if bad else "clean")


def main():
    print("Gauge-link binary registration capacity step-kernel pin runner")
    print(f"Seed: {SEED}")
    rng = np.random.default_rng(SEED)
    section_a(rng)
    section_b(rng)
    g3200, m2_haar = section_c()
    section_d(g3200, m2_haar)
    section_e(g3200)
    section_f()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
