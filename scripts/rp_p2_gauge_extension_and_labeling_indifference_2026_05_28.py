#!/usr/bin/env python3
"""Conditional static-recurrence positivity and relabeling-invariance checks.

Companion for
docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md.

The theorem checked here starts with two supplied construction inputs:

  1. a finite anti-Hermitian matrix h and m > 0; and
  2. the alternating companion recurrence

       A_even = m I + h,       A_odd = m I - h,
       T_s = [[-2 A_s, I], [I, 0]],       C(h,m) = T_odd T_even.

It proves that C(h,m) is Hermitian positive definite with modal eigenvalues
exp(+/-2 asinh(sqrt(m^2+lambda^2))).  A supplied finite list of unitary link
matrices gives one family of anti-Hermitian h matrices used as regression
exhibits.  The runner does not derive the recurrence or link carrier from the
framework axioms and does not identify C(h,m), either reciprocal branch, or a
constructed diagonal matrix with a physical quantum transfer operator.

Independently, the runner checks the exact finite identity that determinant,
spectrum, and Tr(exp(-beta H)) are invariant under permutation-unitary
conjugation.  It makes no P2, AC_phi_lambda, reflection-positivity,
second-quantization, or U-integrated claim.

SCORECARD (7 checks): modal formula, identity-link specialization, sampled
SU(3) matrix positivity, sampled U(1) matrix positivity, determinant
invariance, spectrum invariance, and exponential-trace invariance.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


MASS = 0.5
TOL = 1e-9
RNG = np.random.default_rng(20260528)


def random_su3() -> np.ndarray:
    """Return a Haar-random SU(3) matrix."""
    z = (RNG.standard_normal((3, 3)) + 1j * RNG.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    q = q * phases
    return q * np.linalg.det(q) ** (-1.0 / 3.0)


def random_u1() -> np.ndarray:
    """Return a random U(1) phase as a 1 by 1 unitary matrix."""
    return np.array([[np.exp(1j * RNG.uniform(0.0, 2.0 * math.pi))]], dtype=complex)


def spatial_hop_matrix(links: list[np.ndarray]) -> np.ndarray:
    """Build h[U] from a supplied finite periodic list of unitary links."""
    length = len(links)
    colors = links[0].shape[0]
    dim = length * colors
    h = np.zeros((dim, dim), dtype=complex)

    def block(x: int) -> slice:
        return slice(x * colors, (x + 1) * colors)

    for x in range(length):
        xp = (x + 1) % length
        xm = (x - 1) % length
        h[block(x), block(xp)] += 0.5 * links[x]
        h[block(x), block(xm)] -= 0.5 * links[xm].conj().T
    return h


def two_step_matrix(h: np.ndarray, m: float) -> np.ndarray:
    """Return the supplied recurrence's two-step matrix C(h,m)."""
    dim = h.shape[0]
    identity = np.eye(dim, dtype=complex)
    zero = np.zeros((dim, dim), dtype=complex)
    a_even = m * identity + h
    a_odd = m * identity - h
    t_even = np.block([[-2.0 * a_even, identity], [identity, zero]])
    t_odd = np.block([[-2.0 * a_odd, identity], [identity, zero]])
    return t_odd @ t_even


def modal_pair(lam: float, m: float) -> tuple[float, float]:
    q = math.sqrt(m * m + lam * lam)
    energy = math.asinh(q)
    return math.exp(-2.0 * energy), math.exp(2.0 * energy)


def expected_spectrum_from_h(h: np.ndarray, m: float) -> np.ndarray:
    """Evaluate the theorem formula from the real spectrum of -i h."""
    lambdas = np.linalg.eigvalsh(-1j * h)
    expected = [value for lam in lambdas for value in modal_pair(float(lam), m)]
    return np.sort(np.asarray(expected))


def matrix_diagnostics(h: np.ndarray, m: float) -> dict[str, float]:
    """Check anti-Hermiticity, Hermiticity, positivity, and modal equality."""
    cmat = two_step_matrix(h, m)
    antiherm_err = float(np.max(np.abs(h + h.conj().T)))
    herm_err = float(np.max(np.abs(cmat - cmat.conj().T)))
    observed = np.linalg.eigvalsh((cmat + cmat.conj().T) / 2.0)
    expected = expected_spectrum_from_h(h, m)
    return {
        "antiherm_err": antiherm_err,
        "herm_err": herm_err,
        "min_eig": float(np.min(observed)),
        "modal_residual": float(np.max(np.abs(np.sort(observed) - expected))),
    }


def check_modal_formula(m: float) -> dict[str, float]:
    """Check the displayed 2 by 2 block independently at sample lambdas."""
    worst_residual = 0.0
    worst_herm_err = 0.0
    worst_det_residual = 0.0
    minimum = math.inf
    for lam in (-3.0, -1.25, -0.2, 0.0, 0.7, 2.5):
        block = np.array(
            [
                [4.0 * (m * m + lam * lam) + 1.0, -2.0 * (m - 1j * lam)],
                [-2.0 * (m + 1j * lam), 1.0],
            ],
            dtype=complex,
        )
        observed = np.linalg.eigvalsh(block)
        expected = np.sort(np.asarray(modal_pair(lam, m)))
        worst_residual = max(worst_residual, float(np.max(np.abs(observed - expected))))
        worst_herm_err = max(worst_herm_err, float(np.max(np.abs(block - block.conj().T))))
        worst_det_residual = max(worst_det_residual, abs(float(np.linalg.det(block).real) - 1.0))
        minimum = min(minimum, float(np.min(observed)))
    return {
        "residual": worst_residual,
        "herm_err": worst_herm_err,
        "det_residual": worst_det_residual,
        "min_eig": minimum,
    }


def check_identity_link_specialization(length: int, m: float) -> dict[str, float]:
    """Compare the same supplied recurrence in position and Fourier bases."""
    h = spatial_hop_matrix([np.eye(1, dtype=complex) for _ in range(length)])
    observed = np.linalg.eigvalsh(two_step_matrix(h, m))
    momenta = [2.0 * math.pi * k / length for k in range(length)]
    expected = np.sort(
        np.asarray([value for p in momenta for value in modal_pair(math.sin(p), m)])
    )
    return {
        "residual": float(np.max(np.abs(np.sort(observed) - expected))),
        "min_eig": float(np.min(observed)),
    }


def scan_static_links(factory, *, length: int, count: int, m: float) -> dict[str, float | int]:
    """Regression scan over supplied static unitary-link matrices."""
    worst_antiherm = 0.0
    worst_herm = 0.0
    worst_modal = 0.0
    min_eig = math.inf
    failures = 0
    for _ in range(count):
        links = [factory() for _ in range(length)]
        diag = matrix_diagnostics(spatial_hop_matrix(links), m)
        worst_antiherm = max(worst_antiherm, diag["antiherm_err"])
        worst_herm = max(worst_herm, diag["herm_err"])
        worst_modal = max(worst_modal, diag["modal_residual"])
        min_eig = min(min_eig, diag["min_eig"])
        if (
            diag["antiherm_err"] >= TOL
            or diag["herm_err"] >= TOL
            or diag["modal_residual"] >= TOL
            or diag["min_eig"] <= 0.0
        ):
            failures += 1
    return {
        "count": count,
        "worst_antiherm": worst_antiherm,
        "worst_herm": worst_herm,
        "worst_modal": worst_modal,
        "min_eig": min_eig,
        "failures": failures,
    }


def permutation_unitary(perm: tuple[int, ...]) -> np.ndarray:
    """Return the permutation unitary with P e_i = e_perm[i]."""
    size = len(perm)
    pmat = np.zeros((size, size), dtype=complex)
    for i, target in enumerate(perm):
        pmat[target, i] = 1.0
    return pmat


def trace_exp_hermitian(hmat: np.ndarray, beta: float) -> float:
    return float(np.sum(np.exp(-beta * np.linalg.eigvalsh(hmat))))


def check_conjugation_invariants() -> dict[str, float | int]:
    """Check det/spec/Tr(exp(-beta H)) over all permutations of three modes."""
    generator = np.random.default_rng(7)
    raw_h = generator.standard_normal((3, 3)) + 1j * generator.standard_normal((3, 3))
    hmat = (raw_h + raw_h.conj().T) / 2.0
    mmat = generator.standard_normal((3, 3)) + 1j * generator.standard_normal((3, 3))
    beta = 1.7

    det0 = np.linalg.det(mmat)
    spec0 = np.linalg.eigvalsh(hmat)
    trace0 = trace_exp_hermitian(hmat, beta)
    max_det = 0.0
    max_spec = 0.0
    max_trace = 0.0

    permutations = list(itertools.permutations(range(3)))
    for perm in permutations:
        pmat = permutation_unitary(perm)
        mp = pmat @ mmat @ pmat.conj().T
        hp = pmat @ hmat @ pmat.conj().T
        max_det = max(max_det, float(abs(np.linalg.det(mp) - det0)))
        max_spec = max(max_spec, float(np.max(np.abs(np.linalg.eigvalsh(hp) - spec0))))
        max_trace = max(max_trace, abs(trace_exp_hermitian(hp, beta) - trace0))

    return {
        "permutations": len(permutations),
        "det_baseline_abs": float(abs(det0)),
        "trace_baseline": trace0,
        "max_det": max_det,
        "max_spec": max_spec,
        "max_trace": max_trace,
    }


def record(flag: bool, label: str, passes: int, fails: int) -> tuple[int, int]:
    print(f"    {label}: {'PASS' if flag else 'FAIL'}")
    return passes + int(flag), fails + int(not flag)


def main() -> int:
    print("=" * 78)
    print("CONDITIONAL STATIC-RECURRENCE POSITIVITY + FINITE CONJUGATION INVARIANCE")
    print("=" * 78)
    print("INPUT FIREWALL: h^dag=-h and the alternating recurrence are supplied.")
    print("No axiom-to-carrier, quantum-transfer, second-quantization, RP, P2, or")
    print("AC_phi_lambda identification is tested or claimed.")
    print()

    passes = 0
    fails = 0

    print("MODAL 2 BY 2 FORMULA")
    modal = check_modal_formula(MASS)
    print(f"    max spectral residual = {modal['residual']:.3e}")
    print(f"    max Hermiticity error = {modal['herm_err']:.3e}")
    print(f"    max |det-1|           = {modal['det_residual']:.3e}")
    print(f"    minimum eigenvalue    = {modal['min_eig']:.6e}")
    ok = (
        modal["residual"] < TOL
        and modal["herm_err"] < TOL
        and modal["det_residual"] < TOL
        and modal["min_eig"] > 0.0
    )
    passes, fails = record(ok, "modal transfer formula", passes, fails)
    print()

    print("IDENTITY-LINK SPECIALIZATION OF THE SAME SUPPLIED RECURRENCE")
    identity_residual = 0.0
    identity_min = math.inf
    for length in (3, 4, 6):
        diag = check_identity_link_specialization(length, MASS)
        identity_residual = max(identity_residual, diag["residual"])
        identity_min = min(identity_min, diag["min_eig"])
        print(
            f"    length={length}: position/Fourier residual={diag['residual']:.3e}, "
            f"min eig={diag['min_eig']:.6e}"
        )
    passes, fails = record(
        identity_residual < TOL and identity_min > 0.0,
        "identity-link specialization",
        passes,
        fails,
    )
    print()

    for label, factory, length in (
        ("SU(3)", random_su3, 4),
        ("U(1)", random_u1, 6),
    ):
        print(f"SAMPLED {label} STATIC-LINK MATRIX EXHIBIT")
        scan = scan_static_links(factory, length=length, count=200, m=MASS)
        print(f"    supplied link lists    = {scan['count']}")
        print(f"    max ||h+h^dag||        = {scan['worst_antiherm']:.3e}")
        print(f"    max ||C-C^dag||        = {scan['worst_herm']:.3e}")
        print(f"    max modal residual     = {scan['worst_modal']:.3e}")
        print(f"    min eig(C)             = {scan['min_eig']:.6e}")
        print(f"    failed lists           = {scan['failures']} / {scan['count']}")
        passes, fails = record(
            scan["failures"] == 0,
            f"sampled {label} matrix positivity",
            passes,
            fails,
        )
        print()

    print("FINITE PERMUTATION-CONJUGATION INVARIANCE")
    invariants = check_conjugation_invariants()
    print(f"    permutations tested    = {invariants['permutations']} (all of S_3)")
    print(f"    |det(M)| baseline      = {invariants['det_baseline_abs']:.8f}")
    print(f"    Tr(exp(-beta H))       = {invariants['trace_baseline']:.8f}")
    print(f"    max determinant dev    = {invariants['max_det']:.3e}")
    print(f"    max spectrum dev       = {invariants['max_spec']:.3e}")
    print(f"    max exp-trace dev      = {invariants['max_trace']:.3e}")
    passes, fails = record(invariants["max_det"] < TOL, "determinant invariance", passes, fails)
    passes, fails = record(invariants["max_spec"] < TOL, "spectrum invariance", passes, fails)
    passes, fails = record(
        invariants["max_trace"] < TOL,
        "exponential-trace invariance",
        passes,
        fails,
    )
    print()

    print("=" * 78)
    print(f"SCORECARD: PASS={passes} FAIL={fails}")
    print("  claim surface: conditional finite-matrix theorem only")
    print("  excluded: quantum transfer, Gamma/Fock map, U integration, RP, P2, AC_phi_lambda")
    print("=" * 78)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
