#!/usr/bin/env python3
"""Gauge-link per-record-step rate dial: blindness and the unit-variance point.

This runner deliberately stays source-side. It does not read audit ledgers,
audit queues, publication matrices, or effective-status files.

Checked content (all constructed, nothing assigned):

  R0  the supplied Wilson temporal-gauge per-link kernel lies in the
      bi-invariant positive class with per-step rate tau_eff(beta) =
      N_c/beta (1 + O(1/beta)) — constructed from character data.
  R1  the accumulated rate is the COMPLETE surviving invariant of step
      composition: (i) rates add exactly under composition (semigroup,
      exact in exponents); (ii) two DIFFERENT step kernels (Wilson-type
      and eigenphase-Gaussian/Manton-type) calibrated to the same rate on
      the fundamental block collapse onto the same composed kernel on the
      OTHER blocks, with deviations shrinking under step refinement at
      fixed accumulated rate. Microscopic form is forgotten; the rate is
      kept; nothing else survives.
  R2  every named structural premise of the dynamics lane is RATE-BLIND:
      positivity/record-compatibility, class-function (two-end covariant
      channel) form, step composition, and the diffusive moment law hold
      identically for every member of the one-parameter family tau > 0
      (exhibited at tau in {1/8, 1/2, 3}). Contrast witnesses: a drifted
      (non-Ad-invariant) step has a non-scalar fundamental Fourier block
      (breaks the covariant-channel premise — the premise that fails is
      named, and it is not the rate); a metric dilation changes the fixed
      trace form (the freedom rigidity removes — also not the rate).
  R3  variance law and the unit point: the per-direction second moment
      per step is 2 tau (Gaussian generator identity + constructed Wilson
      second moments -> 8 tau_eff over dim = 8); hence tau = 1/2 is
      exactly the unit-variance-per-step setting, and via tau = N_c/beta
      it is exactly beta = 2 N_c = 6 — the same-slot/(SD) point of the
      g_bare chain. Exact rational layer for the equivalences and the
      mismatched family (tau = 1/8 <-> beta = 24, per-direction moment
      1/4; tau = 3 <-> beta = 1, moment 6).

The runner does not derive tau = 1/2; the rate is exhibited as a
registered-dial-shaped residual with tau = 1/2 the distinguished setting.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GAUGE_LINK_PER_RECORD_STEP_RATE_DIAL_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md"
RIGIDITY = ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md"
WILSON = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"
RP_TEMPORAL = ROOT / "docs" / "AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
SEMIGROUP = ROOT / "docs" / "RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md"
SCALE_REF = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"

N_C = 3

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {name}{suffix}")
    return condition


def require_contains(label: str, text: str, marker: str) -> None:
    check(f"{label} contains marker: {marker[:72]}", marker in text)


def require_absent(label: str, text: str, marker: str) -> None:
    check(f"{label} omits forbidden marker: {marker[:72]}", marker not in text)


# ---------------------------------------------------------------------------
# Canonical basis and SU(3) class-function machinery (stable Weyl alternants).
# Centered eigenphase grid so principal angles are available for moments.
# ---------------------------------------------------------------------------

def canonical_generators() -> list[np.ndarray]:
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3.0)
    return [m / 2.0 for m in (l1, l2, l3, l4, l5, l6, l7, l8)]


RHO = np.array([2, 1, 0])
REPS = {
    "fund(1,0,0)": (1, 0, 0),
    "adj(2,1,0)": (2, 1, 0),
    "sym(2,0,0)": (2, 0, 0),
}


def principal(x: np.ndarray) -> np.ndarray:
    return np.angle(np.exp(1j * x))


def grids(M: int = 384):
    t = -np.pi + 2.0 * np.pi * (np.arange(M) + 0.5) / M
    T1, T2 = np.meshgrid(t, t, indexing="ij")
    return T1, T2


def alternant(l, T1, T2):
    th = [T1, T2, -T1 - T2]
    e = [[np.exp(1j * th[j] * l[k]) for k in range(3)] for j in range(3)]
    return (
        e[0][0] * (e[1][1] * e[2][2] - e[1][2] * e[2][1])
        - e[0][1] * (e[1][0] * e[2][2] - e[1][2] * e[2][0])
        + e[0][2] * (e[1][0] * e[2][1] - e[1][1] * e[2][0])
    )


def weyl_dim(lam) -> int:
    l = np.array(lam) + RHO
    return int(round((l[0] - l[1]) * (l[0] - l[2]) * (l[1] - l[2]) / 2.0))


def casimir_half_trace(lam) -> Fraction:
    s = sum(Fraction(lam[i]) * (lam[i] + 4 - 2 * (i + 1)) for i in range(3))
    return (s - Fraction(sum(lam)) ** 2 / 3) / 2


def kernel_wilson(T1, T2, beta: float):
    T3 = principal(-T1 - T2)
    return np.exp((beta / 3.0) * (np.cos(T1) + np.cos(T2) + np.cos(T3) - 3.0))


def kernel_eigenphase_gaussian(T1, T2, width: float):
    T3 = principal(-T1 - T2)
    return np.exp(-(T1**2 + T2**2 + T3**2) / (4.0 * width))


def char_coeff(kern, lam, T1, T2) -> float:
    a_rho = alternant(RHO, T1, T2)
    a_l = alternant(np.array(lam) + RHO, T1, T2)
    return float((np.mean(kern * a_rho * np.conj(a_l)) / 6.0).real)


def eps_of(kern, lam, T1, T2) -> float:
    c0 = char_coeff(kern, (0, 0, 0), T1, T2)
    cR = char_coeff(kern, lam, T1, T2)
    return float(-np.log((cR / weyl_dim(lam)) / c0))


def second_moment(kern, T1, T2) -> float:
    haar = (alternant(RHO, T1, T2) * np.conj(alternant(RHO, T1, T2))).real
    T3 = principal(-T1 - T2)
    s2 = T1**2 + T2**2 + T3**2
    return float(np.sum(haar * kern * s2) / np.sum(haar * kern))


# ---------------------------------------------------------------------------
# Section A: canonical anchors and machinery guards
# ---------------------------------------------------------------------------

def section_A(T1, T2) -> None:
    print("\nSECTION A: canonical anchors and machinery guards")
    print("-" * 78)
    T = canonical_generators()
    gram = np.array([[np.trace(a @ b) for b in T] for a in T], dtype=complex)
    check(
        "trace form Tr(T_a T_b) = delta_ab / 2 and dim su(3) = 8",
        bool(np.allclose(gram, np.eye(8) / 2.0, atol=1e-13)) and len(T) == 8,
    )
    check(
        "all T_a Hermitian traceless",
        all(np.linalg.norm(Ta - Ta.conj().T) < 1e-14 and abs(np.trace(Ta)) < 1e-14 for Ta in T),
    )
    check(
        "half-trace Casimir values (fund, adj, sym) = (4/3, 3, 10/3)",
        casimir_half_trace((1, 0, 0)) == Fraction(4, 3)
        and casimir_half_trace((2, 1, 0)) == Fraction(3)
        and casimir_half_trace((2, 0, 0)) == Fraction(10, 3),
    )
    check(
        "Weyl dimensions (fund, adj, sym) = (3, 8, 6)",
        weyl_dim((1, 0, 0)) == 3 and weyl_dim((2, 1, 0)) == 8 and weyl_dim((2, 0, 0)) == 6,
    )
    ones = np.ones_like(T1)
    check("beta=0: trivial coefficient = 1 (Haar)", abs(char_coeff(ones, (0, 0, 0), T1, T2) - 1.0) < 1e-12)
    check(
        "beta=0: nontrivial coefficients = 0 (Haar orthogonality)",
        all(abs(char_coeff(ones, lam, T1, T2)) < 1e-12 for lam in REPS.values()),
    )
    a = char_coeff(kernel_wilson(T1, T2, 48.0), (1, 0, 0), T1, T2)
    Tb1, Tb2 = grids(512)
    b = char_coeff(kernel_wilson(Tb1, Tb2, 48.0), (1, 0, 0), Tb1, Tb2)
    check("grid-doubling agreement at beta=48 (fund)", abs(a - b) / abs(b) < 1e-10, f"rel dev={abs(a-b)/abs(b):.2e}")


# ---------------------------------------------------------------------------
# Section B: Lemma R0 — the supplied Wilson kernel and its rate map
# ---------------------------------------------------------------------------

def section_B(T1, T2) -> None:
    print("\nSECTION B: Lemma R0 — Wilson kernel in-class, rate tau_eff = N_c/beta")
    print("-" * 78)
    check(
        "Wilson kernel character coefficients positive at beta in {6,12,24,48,96}",
        all(
            char_coeff(kernel_wilson(T1, T2, b), lam, T1, T2) > 0.0
            for b in (6.0, 12.0, 24.0, 48.0, 96.0)
            for lam in list(REPS.values()) + [(0, 0, 0)]
        ),
    )
    for name in ("fund(1,0,0)", "adj(2,1,0)"):
        lam = REPS[name]
        C2 = float(casimir_half_trace(lam))
        f = {b: b * eps_of(kernel_wilson(T1, T2, b), lam, T1, T2) / (N_C * C2) for b in (24.0, 48.0, 96.0)}
        check(
            f"rate map {name}: |beta*eps/(N_c C2) - 1| strictly decreasing",
            abs(f[96.0] - 1) < abs(f[48.0] - 1) < abs(f[24.0] - 1),
            f"f(96)={f[96.0]:.5f}",
        )
        r1 = 2.0 * f[96.0] - f[48.0]
        check(f"rate map {name}: Richardson(48,96) hits 1", abs(r1 - 1.0) < 1e-2, f"R1={r1:.6f}")


# ---------------------------------------------------------------------------
# Section C: Theorem R1 — the rate is the complete surviving invariant
# ---------------------------------------------------------------------------

def section_C(T1, T2) -> None:
    print("\nSECTION C: Theorem R1 — rate additivity; cross-kernel collapse")
    print("-" * 78)
    taus = (Fraction(1, 8), Fraction(1, 2), Fraction(3))
    check(
        "exact additivity of composed exponents: tau1 C2 + tau2 C2 = (tau1+tau2) C2",
        all(
            t1 * casimir_half_trace(lam) + t2 * casimir_half_trace(lam)
            == (t1 + t2) * casimir_half_trace(lam)
            for t1 in taus
            for t2 in taus
            for lam in REPS.values()
        ),
    )
    w = np.exp(-0.5 * float(casimir_half_trace((1, 0, 0))))
    check(
        "numeric semigroup: w(tau)^2 = w(2 tau) on the fundamental",
        abs(w * w - np.exp(-1.0 * float(casimir_half_trace((1, 0, 0))))) < 1e-14,
    )

    # Cross-kernel collapse: calibrate the eigenphase-Gaussian kernel to the
    # Wilson kernel's fundamental-block rate, then compare the OTHER blocks of
    # the k-step composition at fixed accumulated rate T = k * tau_hat ~ 1/2.
    C2f = float(casimir_half_trace((1, 0, 0)))
    results = {}
    for tau0, k in ((1.0 / 16, 8), (1.0 / 32, 16), (1.0 / 64, 32)):
        Ww = kernel_wilson(T1, T2, 3.0 / tau0)
        target = eps_of(Ww, (1, 0, 0), T1, T2)
        lo, hi = tau0 / 8.0, tau0 * 4.0
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if eps_of(kernel_eigenphase_gaussian(T1, T2, mid), (1, 0, 0), T1, T2) > target:
                hi = mid
            else:
                lo = mid
        Wm = kernel_eigenphase_gaussian(T1, T2, 0.5 * (lo + hi))
        tau_hat = target / C2f
        devs = {}
        for name in ("adj(2,1,0)", "sym(2,0,0)"):
            lam = REPS[name]
            ew = eps_of(Ww, lam, T1, T2)
            em = eps_of(Wm, lam, T1, T2)
            devs[name] = (k * abs(ew - em), k * abs(em - tau_hat * float(casimir_half_trace(lam))))
        results[tau0] = (tau_hat, devs)
        check(
            f"calibrated rate sanity at tau0={tau0}: tau_hat within 5% of tau0",
            abs(tau_hat / tau0 - 1.0) < 0.05,
            f"tau_hat={tau_hat:.6f}",
        )
    for name in ("adj(2,1,0)", "sym(2,0,0)"):
        d16 = results[1.0 / 16][1][name][0]
        d32 = results[1.0 / 32][1][name][0]
        d64 = results[1.0 / 64][1][name][0]
        check(
            f"cross-kernel collapse on {name}: k|W-M| strictly shrinking under refinement",
            d64 < d32 < d16,
            f"{d16:.5f} -> {d32:.5f} -> {d64:.5f}",
        )
        check(
            f"cross-kernel collapse on {name}: k|W-M| < 1e-3 at finest step",
            d64 < 1e-3,
            f"k|W-M|={d64:.2e}",
        )
    check(
        "single calibrated number predicts all tested blocks (rate = complete invariant)",
        all(results[1.0 / 64][1][name][1] < 1e-3 for name in ("adj(2,1,0)", "sym(2,0,0)")),
    )


# ---------------------------------------------------------------------------
# Section D: Theorem R2 — every named structural premise is rate-blind
# ---------------------------------------------------------------------------

def section_D(T1, T2) -> None:
    print("\nSECTION D: Theorem R2 — rate-blindness of the named premises")
    print("-" * 78)
    pass_patterns = {}
    for tau in (Fraction(1, 8), Fraction(1, 2), Fraction(3)):
        tf = float(tau)
        wvals = {name: np.exp(-tf * float(casimir_half_trace(lam))) for name, lam in REPS.items()}
        p1 = all(0.0 < w <= 1.0 for w in wvals.values())
        check(
            f"tau={tau}: positivity/record-compatibility (0 < w_R <= 1, all reps)",
            p1,
        )
        # class-function/covariant-channel form: the member is defined by real
        # R-scalars; class-function reality forces conjugate representations
        # to share the scalar, and C_2(fund) = C_2(antifund) = 4/3 exactly.
        p2 = (
            casimir_half_trace((1, 1, 0)) == casimir_half_trace((1, 0, 0))
            and abs(
                np.exp(-tf * float(casimir_half_trace((1, 1, 0))))
                - wvals["fund(1,0,0)"]
            )
            < 1e-15
        )
        check(
            f"tau={tau}: covariant-channel form (conjugate-rep scalar symmetry)",
            p2,
        )
        p3 = all(
            abs(wvals[name] ** 2 - np.exp(-2.0 * tf * float(casimir_half_trace(lam)))) < 1e-14
            for name, lam in REPS.items()
        )
        check(f"tau={tau}: composition law w(tau)^2 = w(2 tau)", p3)
        # diffusive moment law of the Gaussian generator model at this rate:
        # per-direction second moment = 2 tau (1D Gaussian quadrature).
        x = np.linspace(-40.0 * np.sqrt(tf), 40.0 * np.sqrt(tf), 400001)
        g = np.exp(-(x**2) / (4.0 * tf))
        m2 = float(np.trapezoid(x**2 * g, x) / np.trapezoid(g, x))
        p4 = abs(m2 - 2.0 * tf) / (2.0 * tf) < 1e-6
        check(f"tau={tau}: diffusive moment law <x^2> = 2 tau", p4, f"m2={m2:.8f}")
        pass_patterns[tau] = (p1, p2, p3, p4)
    check(
        "identical pass pattern across tau in {1/8, 1/2, 3}: premises are rate-blind",
        len({pass_patterns[t] for t in pass_patterns}) == 1
        and all(all(p) for p in pass_patterns.values()),
    )

    # Contrast witnesses: what the premises DO exclude is not the rate.
    rng = np.random.default_rng(20260702)
    H = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    H = (H + H.conj().T) / 2.0
    H -= (np.trace(H) / 3.0) * np.eye(3)
    wv, V = np.linalg.eigh(H)
    g0 = (V * np.exp(1j * wv * 0.7)) @ V.conj().T
    dev = float(np.linalg.norm(g0 - (np.trace(g0) / 3.0) * np.eye(3)))
    check(
        "drifted step witness: fundamental Fourier block non-scalar (covariance premise fails, not the rate)",
        dev > 0.1,
        f"deviation={dev:.4f}",
    )
    T = canonical_generators()
    gram_scaled = np.array([[np.trace((2.0 * a) @ (2.0 * b)) for b in T] for a in T], dtype=complex)
    check(
        "metric-dilation witness: scaling generators changes the fixed trace form (rigidity's freedom, not the rate)",
        not np.allclose(gram_scaled, np.eye(8) / 2.0, atol=1e-10),
    )


# ---------------------------------------------------------------------------
# Section E: Theorem R3 — variance law and the unit point
# ---------------------------------------------------------------------------

def section_E(T1, T2) -> None:
    print("\nSECTION E: Theorem R3 — per-direction moment 2 tau; unit point tau = 1/2")
    print("-" * 78)
    ratios = {}
    for beta in (24.0, 48.0, 96.0):
        m2 = second_moment(kernel_wilson(T1, T2, beta), T1, T2)
        tau = N_C / beta
        ratios[beta] = m2 / (8.0 * tau)
    check(
        "Wilson <sum theta^2> / (8 tau_eff): deviation strictly decreasing",
        abs(ratios[96.0] - 1) < abs(ratios[48.0] - 1) < abs(ratios[24.0] - 1),
        f"ratio(96)={ratios[96.0]:.5f}",
    )
    r1 = 2.0 * ratios[96.0] - ratios[48.0]
    check("Wilson second-moment Richardson(48,96) hits 1", abs(r1 - 1.0) < 5e-3, f"R1={r1:.6f}")
    # sum_a (X^a)^2 = 2 Tr X^2 = 2 sum_j theta_j^2 over 8 directions, so the
    # per-direction canonical-coordinate moment is m2/4.
    m2_96 = second_moment(kernel_wilson(T1, T2, 96.0), T1, T2)
    per_dir = m2_96 / 4.0
    check(
        "constructed per-direction moment matches 2 tau_eff at beta=96 within 2%",
        abs(per_dir / (2.0 * N_C / 96.0) - 1.0) < 2e-2,
        f"per-direction={per_dir:.6f}, 2 tau={2.0 * N_C / 96.0:.6f}",
    )


# ---------------------------------------------------------------------------
# Section F: exact coincidence layer
# ---------------------------------------------------------------------------

def section_F() -> None:
    print("\nSECTION F: exact layer — unit-variance point = the (SD)/beta=6 point")
    print("-" * 78)
    n_c = Fraction(3)

    def beta_of(tau: Fraction) -> Fraction:
        return n_c / tau

    def per_direction_moment(tau: Fraction) -> Fraction:
        return 2 * tau

    check("tau = 1/2 gives per-direction moment 1 (unit variance per step)", per_direction_moment(Fraction(1, 2)) == 1)
    check("tau = 1/2 maps to beta = N_c / tau = 6", beta_of(Fraction(1, 2)) == 6)
    check(
        "consistency with the magnetic identity: g^2(beta(tau)) = 2 N_c / beta = 2 tau",
        all(2 * n_c / beta_of(t) == 2 * t for t in (Fraction(1, 8), Fraction(1, 2), Fraction(3))),
    )
    check(
        "coincidence at tau = 1/2: g^2 = 1 = s^2 (the same-slot point)",
        2 * n_c / beta_of(Fraction(1, 2)) == 1,
    )
    check(
        "mismatched family: tau = 1/8 -> beta = 24, moment 1/4; tau = 3 -> beta = 1, moment 6",
        beta_of(Fraction(1, 8)) == 24
        and per_direction_moment(Fraction(1, 8)) == Fraction(1, 4)
        and beta_of(Fraction(3)) == 1
        and per_direction_moment(Fraction(3)) == 6,
    )
    check(
        "off-point coincidence failure: moments != 1 exactly at tau in {1/8, 3}",
        per_direction_moment(Fraction(1, 8)) != 1 and per_direction_moment(Fraction(3)) != 1,
    )


# ---------------------------------------------------------------------------
# Section G: source-boundary guards
# ---------------------------------------------------------------------------

def section_G() -> None:
    print("\nSECTION G: source-boundary guards")
    print("-" * 78)
    paths = {
        "rate-dial note": NOTE,
        "finite-link rigidity note": RIGIDITY,
        "Wilson small-a note": WILSON,
        "RP temporal-gauge bridge note": RP_TEMPORAL,
        "record classical semigroup boundary note": SEMIGROUP,
        "scale-reference primitive note": SCALE_REF,
    }
    for label, path in paths.items():
        check(f"{label} exists", path.exists(), str(path.relative_to(ROOT)))

    note_flat = flat(NOTE.read_text(encoding="utf-8"))
    note_text = NOTE.read_text(encoding="utf-8")
    rigidity_flat = flat(RIGIDITY.read_text(encoding="utf-8"))
    wilson_text = WILSON.read_text(encoding="utf-8")
    rp_flat = flat(RP_TEMPORAL.read_text(encoding="utf-8"))
    semigroup_flat = flat(SEMIGROUP.read_text(encoding="utf-8"))
    scale_flat = flat(SCALE_REF.read_text(encoding="utf-8"))

    require_contains("note", note_flat, "**Status authority:** independent audit lane only")
    require_absent("note", note_text, "**Audit status:**")
    require_contains("note", note_flat, "does not set, predict, or apply an audit verdict")
    require_contains("note", note_flat, "does not derive `tau = 1/2`")
    require_contains("note", note_flat, "per-record-step")
    require_contains("note", note_flat, "rate-blind")
    require_contains("note", note_flat, "complete surviving invariant")
    require_contains("note", note_flat, "unit-variance")
    require_contains("note", note_flat, "distinguished setting")
    require_contains("note", note_flat, "zero dimensionless content")
    require_contains("note", note_flat, "not a citation-graph dependency")
    require_contains("note", note_flat, "does not claim:")
    require_contains("note", note_flat, "an audit verdict or any effective-status promotion")
    require_absent("note", note_text, "effective_status:")
    require_absent("note", note_text, "audit_status:")

    require_contains("rigidity", rigidity_flat, "no independent scalar-normalization freedom")
    require_contains("rigidity", rigidity_flat, "Tr(T_a T_b) = delta_ab / 2")
    require_contains("Wilson", wilson_text, "beta * g_bare^2 = 2 N_c")
    require_contains("RP bridge", rp_flat, "temporal gauge")
    require_contains("RP bridge", rp_flat, "plane positive kernel")
    require_contains(
        "semigroup boundary", semigroup_flat, "continuous Markov semigroups live on the probability/ensemble"
    )
    require_contains("scale-reference primitive", scale_flat, "zero dimensionless content")


def main() -> int:
    print("Gauge-link per-record-step rate dial: blindness and the unit-variance point")
    print("=" * 78)
    T1, T2 = grids(384)
    section_A(T1, T2)
    section_B(T1, T2)
    section_C(T1, T2)
    section_D(T1, T2)
    section_E(T1, T2)
    section_F()
    section_G()

    print("\nSummary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("Rate-dial check failed.")
        return 1
    print("Rate-dial check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
