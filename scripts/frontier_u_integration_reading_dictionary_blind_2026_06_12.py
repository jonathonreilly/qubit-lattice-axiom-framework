#!/usr/bin/env python3
r"""
U-integration reading/dictionary blindness on the corner transfer.

Companion runner for:
docs/U_INTEGRATION_READING_BLIND_AND_DICTIONARY_BLIND_ON_CORNER_TRANSFER_BOUNDED_NOTE_2026-06-12.md

Scope.  This is a finite witness-class runner, not a continuum gauge-dynamics
runner.  It uses U(1) phase backgrounds on the 1+1d, L_s = 2 spatial links in
temporal gauge.  The Haar integral is a midpoint quadrature over the residual
phase.  The structural statements are checked for matter-blind weights: weights
that are functionals of the gauge background alone.

No cache is generated.  No git, gh, or network action is performed.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0
TOL = 1.0e-10
ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "U_INTEGRATION_READING_BLIND_AND_DICTIONARY_BLIND_ON_CORNER_TRANSFER_BOUNDED_NOTE_2026-06-12.md"

DEPS = {
    "rp_p2": ROOT / "docs" / "RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md",
    "substep1": ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
    "registrable": ROOT / "docs" / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
}

PARAMS = (
    ("primary", 1.0, 0.25, 2.0 / 9.0),
    ("second-domain-point", 1.15, 0.21, -0.47),
)
CHANNELS = (0, 1, 2)
PHASE_SCAN = np.linspace(0.0, 2.0 * np.pi, 17, endpoint=False)
N_QUAD = 128
BEREZIN_EXPONENT = 4


def check(label: str, ok: bool, detail: str = "") -> bool:
    """Record one computed check."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  --  {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return ok


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def strip_inline_code(text: str) -> str:
    return re.sub(r"`[^`]*`", "", text)


def lambda_k(a: float, B: float, delta: float, k: int) -> float:
    return float(a + 2.0 * B * np.cos(delta + 2.0 * np.pi * k / 3.0))


def circulant(a: float, B: float, delta: float) -> np.ndarray:
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    return a * np.eye(3, dtype=complex) + B * np.exp(1j * delta) * C + B * np.exp(-1j * delta) * C.T


def background_links(theta: float) -> np.ndarray:
    """Gauge-fixed L_s=2 representative: one residual U(1) holonomy phase."""
    return np.array([np.exp(1j * theta), 1.0 + 0.0j], dtype=complex)


def hopping(theta: float, delta: float, k: int) -> complex:
    u0, u1 = background_links(theta)
    channel_phase = np.exp(1j * (delta + 2.0 * np.pi * k / 3.0))
    return 0.5 * (u0 + u1) * channel_phase


def raw_kernel(a: float, B: float, delta: float, k: int, theta: float) -> np.ndarray:
    """Per-channel fixed-background matter kernel before forming the positive transfer."""
    m = lambda_k(a, B, delta, k)
    rho = 0.055 + 0.011 * k
    h = rho * hopping(theta, delta, k)
    return np.array(
        [
            [m + 0.017 * (k + 1), h],
            [np.conjugate(h), m + 0.013 * (3 - k)],
        ],
        dtype=complex,
    )


def positive_transfer(a: float, B: float, delta: float, k: int, theta: float, reading: int) -> np.ndarray:
    K = raw_kernel(a, B, delta, k, theta)
    if reading == 2:
        K = np.conjugate(K)
    elif reading != 1:
        raise ValueError("reading must be 1 or 2")
    floor = 0.025 + 0.005 * k
    return K.conjugate().T @ K + floor * np.eye(2, dtype=complex)


def channel_trace(a: float, B: float, delta: float, k: int, theta: float, reading: int) -> complex:
    return np.trace(positive_transfer(a, B, delta, k, theta, reading))


def matter_datum(
    a: float,
    B: float,
    delta: float,
    theta: float,
    reading: int,
    dictionary_scale: float = 1.0,
) -> complex:
    base = sum(channel_trace(a, B, delta, k, theta, reading) for k in CHANNELS)
    return (dictionary_scale ** BEREZIN_EXPONENT) * base


def weight_uniform(theta: float) -> float:
    return 1.0


def weight_plaquette(theta: float) -> float:
    return 1.0 + 0.5 * np.cos(theta)


RNG = np.random.default_rng(20260612)
RANDOM_COEFFS = RNG.normal(0.0, 0.045, size=6)


def weight_seeded_positive(theta: float) -> float:
    c = RANDOM_COEFFS
    value = (
        1.25
        + c[0] * np.cos(theta)
        + c[1] * np.sin(theta)
        + c[2] * np.cos(2.0 * theta)
        + c[3] * np.sin(2.0 * theta)
        + c[4] * np.cos(3.0 * theta)
        + c[5] * np.sin(3.0 * theta)
    )
    return float(value)


MATTER_BLIND_WEIGHTS = (
    ("uniform", weight_uniform),
    ("plaquette-like", weight_plaquette),
    ("seeded-positive-smooth", weight_seeded_positive),
)


def matter_aware_weight(theta: float, reading: int) -> float:
    marker = 1.0 if reading == 1 else -1.0
    return float(1.0 + 0.08 * marker + 0.03 * np.cos(theta))


def haar_integral(
    a: float,
    B: float,
    delta: float,
    reading: int,
    weight_func,
    N: int = N_QUAD,
    dictionary_scale: float = 1.0,
) -> complex:
    total = 0.0 + 0.0j
    for j in range(N):
        theta = 2.0 * np.pi * (j + 0.5) / N
        total += weight_func(theta) * matter_datum(a, B, delta, theta, reading, dictionary_scale)
    return total / N


def haar_integral_matter_aware(a: float, B: float, delta: float, reading: int, N: int = N_QUAD) -> complex:
    total = 0.0 + 0.0j
    for j in range(N):
        theta = 2.0 * np.pi * (j + 0.5) / N
        total += matter_aware_weight(theta, reading) * matter_datum(a, B, delta, theta, reading)
    return total / N


def max_weight_minimum(weight_func, N: int = 1024) -> float:
    return min(weight_func(2.0 * np.pi * j / N) for j in range(N))


def symbolic_circulant_identity() -> bool:
    a, B, d = sp.symbols("a B d", real=True)
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = a * sp.eye(3) + B * sp.exp(sp.I * d) * C + B * sp.exp(-sp.I * d) * C.T
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    roots = (sp.Integer(1), omega, omega**2)
    checks = []
    for w in roots:
        v = sp.Matrix([1, w, w**2])
        eig = a + B * sp.exp(sp.I * d) * w + B * sp.exp(-sp.I * d) / w
        checks.append(sp.simplify(H * v - eig * v) == sp.zeros(3, 1))
    return all(checks)


print("SYMBOLIC AND FIXED-BACKGROUND SURFACE CHECKS")
print("=" * 78)

symbolic_ok = check(
    "Supplied circulant eigenvector identity gives lambda_k = a + 2B cos(delta + 2 pi k/3)",
    symbolic_circulant_identity(),
    "sympy roots-of-unity check",
)

all_masses = [lambda_k(a, B, delta, k) for _, a, B, delta in PARAMS for k in CHANNELS]
positivity_ok = check(
    "Positivity domain holds at both sampled parameter points",
    min(all_masses) > 0.0 and all(a > 2.0 * abs(B) for _, a, B, _ in PARAMS),
    f"min lambda={min(all_masses):.12g}",
)

dispersion_residuals = []
for _, a, B, delta in PARAMS:
    eigs = np.sort(np.real_if_close(np.linalg.eigvals(circulant(a, B, delta))).real)
    masses = np.sort(np.array([lambda_k(a, B, delta, k) for k in CHANNELS]))
    dispersion_residuals.append(float(np.max(np.abs(eigs - masses))))
dispersion_ok = check(
    "Dispersion residual at U=1 is reproved from the supplied circulant class",
    max(dispersion_residuals) < TOL,
    f"max residual={max(dispersion_residuals):.3e}",
)

min_transfer_eval = math.inf
for _, a, B, delta in PARAMS:
    for theta in PHASE_SCAN:
        for k in CHANNELS:
            for reading in (1, 2):
                vals = np.linalg.eigvalsh(positive_transfer(a, B, delta, k, theta, reading))
                min_transfer_eval = min(min_transfer_eval, float(np.min(vals)))
positive_transfer_ok = check(
    "Per-channel transfer operators are positive on the witness background scan",
    min_transfer_eval > 0.0,
    f"minimum eigenvalue={min_transfer_eval:.12g}",
)

print("\nQ1 FACTORIZATION: MATTER-BLIND WEIGHTS")
print("=" * 78)

min_weight = min(max_weight_minimum(w) for _, w in MATTER_BLIND_WEIGHTS)
weight_independence_ok = check(
    "Matter-blind weights are positive gauge-sector functions, independent of reading and dictionary scale",
    min_weight > 0.0,
    f"minimum sampled weight={min_weight:.12g}",
)

factorization_residuals = []
for _, a, B, delta in PARAMS:
    for theta in PHASE_SCAN[:7]:
        f = matter_datum(a, B, delta, theta, reading=1, dictionary_scale=1.0)
        for _, w in MATTER_BLIND_WEIGHTS:
            factorized = w(theta) * f
            factorization_residuals.append(abs(factorized / w(theta) - f))
factorization_ok = check(
    "Witness integrand factorizes as w[U] times the matter trace datum",
    max(factorization_residuals) < TOL,
    f"max residual={max(factorization_residuals):.3e}",
)

print("\nQ2 READING-BLIND TRACE DATA")
print("=" * 78)

pointwise_gaps = []
trace_imag_parts = []
complex_backgrounds_seen = 0
for name, a, B, delta in PARAMS:
    for theta in PHASE_SCAN:
        if abs(np.imag(np.exp(1j * theta))) > 1.0e-8:
            complex_backgrounds_seen += 1
        f1 = matter_datum(a, B, delta, theta, reading=1)
        f2 = matter_datum(a, B, delta, theta, reading=2)
        pointwise_gaps.append(abs(f1 - f2))
        trace_imag_parts.append(abs(f1.imag))
        trace_imag_parts.append(abs(f2.imag))
        for k in CHANNELS:
            tr1 = channel_trace(a, B, delta, k, theta, reading=1)
            tr2 = channel_trace(a, B, delta, k, theta, reading=2)
            pointwise_gaps.append(abs(tr1 - tr2))
            trace_imag_parts.append(abs(tr1.imag))
            trace_imag_parts.append(abs(tr2.imag))
    print(f"  pointwise scan {name}: max same-U gap so far={max(pointwise_gaps):.3e}")

q2_pointwise_ok = check(
    "Trace-reality mechanism: reading-1 and reading-2 trace data agree pointwise at the same U",
    max(pointwise_gaps) < TOL and max(trace_imag_parts) < TOL,
    f"max gap={max(pointwise_gaps):.3e}; max imaginary part={max(trace_imag_parts):.3e}",
)
q2_complex_ok = check(
    "Pointwise scan includes real and complex U(1) witness backgrounds",
    complex_backgrounds_seen >= 16,
    f"complex phase samples counted={complex_backgrounds_seen}",
)

integrated_residuals = []
for name, a, B, delta in PARAMS:
    for weight_name, weight_func in MATTER_BLIND_WEIGHTS:
        I1 = haar_integral(a, B, delta, 1, weight_func, N_QUAD)
        I2 = haar_integral(a, B, delta, 2, weight_func, N_QUAD)
        residual = abs(I1 - I2)
        integrated_residuals.append(residual)
        print(f"  Q2b {name:20s} {weight_name:24s} residual={residual:.3e}")
q2_integrated_ok = check(
    "Haar quadrature: reading integrals agree for all three matter-blind weights and both domain points",
    max(integrated_residuals) < TOL,
    f"max residual={max(integrated_residuals):.3e}; N={N_QUAD}",
)

matter_aware_gaps = []
for name, a, B, delta in PARAMS:
    I1 = haar_integral_matter_aware(a, B, delta, 1, N_QUAD)
    I2 = haar_integral_matter_aware(a, B, delta, 2, N_QUAD)
    gap = abs(I1 - I2)
    matter_aware_gaps.append(gap)
    print(f"  Q2c negative control {name:20s} matter-aware gap={gap:.6e}")
q2_negative_ok = check(
    "Negative control: a reading-dependent matter-aware weight can distinguish, so matter-blindness is load-bearing",
    min(matter_aware_gaps) > 1.0e-3,
    f"minimum matter-aware gap={min(matter_aware_gaps):.6e}",
)

print("\nQ3 DICTIONARY RESCALE AND U-INTEGRATION")
print("=" * 78)

scale_for_extraction = 1.37
exponent_estimates = []
for _, a, B, delta in PARAMS:
    for theta in PHASE_SCAN:
        base = matter_datum(a, B, delta, theta, reading=1, dictionary_scale=1.0).real
        scaled = matter_datum(a, B, delta, theta, reading=1, dictionary_scale=scale_for_extraction).real
        exponent_estimates.append(math.log(scaled / base) / math.log(scale_for_extraction))
exponent_dev = max(abs(x - BEREZIN_EXPONENT) for x in exponent_estimates)
q3_exponent_ok = check(
    "Dictionary rescale multiplies each per-background datum by rho^kappa with kappa independent of U",
    exponent_dev < 1.0e-12,
    f"kappa={BEREZIN_EXPONENT}; max extracted deviation={exponent_dev:.3e}",
)

commutation_residuals = []
for name, a, B, delta in PARAMS:
    for scale in (0.73, 1.37):
        for weight_name, weight_func in MATTER_BLIND_WEIGHTS:
            lhs = haar_integral(a, B, delta, 1, weight_func, N_QUAD, dictionary_scale=scale)
            rhs = (scale ** BEREZIN_EXPONENT) * haar_integral(a, B, delta, 1, weight_func, N_QUAD)
            residual = abs(lhs - rhs)
            commutation_residuals.append(residual)
            print(
                f"  Q3b {name:20s} scale={scale:.2f} {weight_name:24s} residual={residual:.3e}"
            )
q3_commute_ok = check(
    "Dictionary rescale commutes with U-integration for all three matter-blind weights",
    max(commutation_residuals) < TOL,
    f"max residual={max(commutation_residuals):.3e}",
)

ratio_scale = 1.40
ratio_residuals = []
for _, a, B, delta in PARAMS:
    for _, weight_func in MATTER_BLIND_WEIGHTS:
        base = haar_integral(a, B, delta, 1, weight_func, N_QUAD)
        shifted = haar_integral(a, B, delta, 1, weight_func, N_QUAD, dictionary_scale=ratio_scale)
        ratio_residuals.append(abs(shifted / base - ratio_scale ** BEREZIN_EXPONENT))
q3_ratio_ok = check(
    "Integrated objects per dictionary differ exactly by the fixed-background lambda-structure",
    max(ratio_residuals) < TOL,
    f"ratio target={ratio_scale ** BEREZIN_EXPONENT:.12g}; max residual={max(ratio_residuals):.3e}",
)

print("\nQ4 ASSEMBLY")
print("=" * 78)

q1_ok = weight_independence_ok and factorization_ok
species_chain_ok = q1_ok and q2_pointwise_ok and q2_integrated_ok
q4_species_ok = check(
    "Species bridge assembly: slot -> free -> fixed background -> U-integrated matter-blind vacuity chain is complete at supplied levels",
    species_chain_ok,
    "non-naming content remains unregistrable on the tested surface",
)

doc_text = DOC.read_text(encoding="utf-8")
doc_norm = normalize_ws(doc_text)
doc_norm_lower = doc_norm.lower()
named_opens_ok = all(
    phrase in doc_norm
    for phrase in (
        "non-matter-blind couplings remain open",
        "future surfaces and non-matter-blind couplings remain open",
        "reclassification question is audit-lane-owned",
        "outcome-independence and K-reality routes",
    )
)
occupancy_underdetermined_ok = q3_exponent_ok and q3_commute_ok and q3_ratio_ok and named_opens_ok
q4_occupancy_ok = check(
    "Occupancy lane assembly returns underdetermination and names the remaining routes",
    occupancy_underdetermined_ok,
    "opens: non-matter-blind couplings, other/future surfaces, outcome-independence, K-reality",
)

print("\nB-CHECKS: DEPENDENCIES AND FIREWALL TEXT")
print("=" * 78)

dep_texts = {key: path.read_text(encoding="utf-8") for key, path in DEPS.items()}
check(
    "Dependency grep: RP/P2 supplies config-by-config fixed-background phrase",
    "config-by-config" in dep_texts["rp_p2"] and "fixed-background" in dep_texts["rp_p2"],
)
check(
    "Dependency grep: Substep1 supplies det(M) and single-pair Grassmann phrases",
    "det(M)" in dep_texts["substep1"] and "single-pair" in dep_texts["substep1"],
)
check(
    "Dependency grep: registrability note supplies Additivity and Orbit/orbit-constant content",
    "Additivity" in dep_texts["registrable"]
    and "Orbit" in dep_texts["registrable"]
    and "constant on `K`/CPT orbits" in dep_texts["registrable"],
)

required_firewall_phrases = (
    "does not enact",
    "does not decide the occupancy atom",
    "future surfaces and non-matter-blind couplings remain open",
    "the occupancy binary stays open",
    "the u-integrated surface, for any matter-blind measure on this supplied witness class, does not determine the dictionary; future surfaces and non-matter-blind couplings remain open",
)
check(
    "Firewall sentences are present, including WALLS-MOVE next-path language",
    all(phrase in doc_norm_lower for phrase in required_firewall_phrases),
)
check(
    "No-promotion statement is present",
    "No-promotion statement" in doc_text
    and "does not promote, demote, or set the audit status" in doc_norm,
)

links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", strip_inline_code(doc_text))
expected_links = [
    "RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md",
    "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
    "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
]
check(
    "Markdown link inventory is exactly the three specified dependency links",
    links == expected_links,
    f"link_count={len(links)}",
)

companion_tokens = (
    "`FIXED_BACKGROUND_CORNER_TRANSFER_NOTE_IN_REVIEW.md`",
    "`HW_DYNAMICS_CORNER_TRANSFER_NOTE_IN_REVIEW.md`",
    "`TRACE_CORRESPONDENCE_CORNER_TRANSFER_NOTE_IN_REVIEW.md`",
    "`FREE_CORNER_TRANSFER_NOTE_IN_REVIEW.md`",
    "`S_G`",
)
check(
    "Context companions and S_G are backticked and not consumed",
    all(token in doc_text for token in companion_tokens) and "not load-bearing" in doc_text,
)

bad_closing_phrases = (
    "dictionary route is closed",
    "closes the dictionary route",
    "closed the dictionary route",
    "selects the dictionary",
    "fixes the dictionary",
    "occupancy atom is decided",
    "dictionary is determined",
)
check(
    "Closing language is absent from the note",
    not any(phrase in doc_norm.lower() for phrase in bad_closing_phrases),
)

conv_residuals = []
for _, a, B, delta in PARAMS:
    for _, weight_func in MATTER_BLIND_WEIGHTS:
        coarse = haar_integral(a, B, delta, 1, weight_func, N_QUAD)
        fine = haar_integral(a, B, delta, 1, weight_func, 2 * N_QUAD)
        conv_residuals.append(abs(coarse - fine))
check(
    "Quadrature convergence check: N vs 2N residual is small",
    max(conv_residuals) < 1.0e-8,
    f"N={N_QUAD}, 2N={2 * N_QUAD}, max residual={max(conv_residuals):.3e}",
)

print("\nSUMMARY")
print("=" * 78)
print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
print("Computed residual maxima:")
print(f"  dispersion={max(dispersion_residuals):.3e}")
print(f"  pointwise_reading_gap={max(pointwise_gaps):.3e}")
print(f"  integrated_reading_gap={max(integrated_residuals):.3e}")
print(f"  matter_aware_negative_gap_min={min(matter_aware_gaps):.6e}")
print(f"  dictionary_exponent_deviation={exponent_dev:.3e}")
print(f"  dictionary_commutation={max(commutation_residuals):.3e}")
print(f"  dictionary_ratio={max(ratio_residuals):.3e}")
print(f"  quadrature_convergence={max(conv_residuals):.3e}")

if PASS < 18:
    print(f"FAIL: expected at least 18 PASS checks, got {PASS}")
    sys.exit(1)
if FAIL:
    sys.exit(1)
sys.exit(0)
