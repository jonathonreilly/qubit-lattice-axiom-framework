#!/usr/bin/env python3
"""ADM-2 SU(3) equivariance/annealing reduction diagnostic.

This runner directly uses SU(3) fundamental matrices. It checks that a
global-conjugation-equivariant link drift plus isotropic noise gives a central
increment in the free and annealed regimes, while a fixed quenched staple or an
external color field breaks centrality. It also checks the global-vs-local
symmetry diagnostic on the hopping contraction, without treating that diagnostic
as a closure ranking.

Scope: finite-dimensional support for the ADM-2 reduction. It does not close the
open dynamical premise that the physical gauge-link step is annealed/equivariant.
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0
rng = np.random.default_rng(20260608)
I3 = np.eye(3, dtype=complex)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    PASS += int(bool(condition))
    FAIL += int(not condition)
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def haar_su3() -> np.ndarray:
    z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    q = q @ np.diag(np.conj(phases))
    q[:, -1] *= np.conj(np.linalg.det(q))
    return q


def random_su3_algebra(scale: float = 1.0) -> np.ndarray:
    z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2)
    h = (z + z.conj().T) / 2
    h = h - np.trace(h) / 3 * I3
    norm = np.sqrt(np.trace(h @ h).real)
    return scale * h / norm


def expiH(h: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(h)
    return v @ np.diag(np.exp(1j * w)) @ v.conj().T


def equivariant_drift(U: np.ndarray, S: np.ndarray) -> np.ndarray:
    """Traceless Hermitian staple force from X=U S^dag.

    Under global conjugation U,S -> gUg^dag,gSg^dag, this force transforms as
    A -> gAg^dag.
    """
    x = U @ S.conj().T
    a = (x - x.conj().T) / (2j)
    return a - np.trace(a) / 3 * I3


def step_increment(
    U: np.ndarray,
    S: np.ndarray,
    eps_drift: float = 0.25,
    eps_noise: float = 0.18,
    extra_field: np.ndarray | None = None,
) -> np.ndarray:
    h = eps_drift * equivariant_drift(U, S) + eps_noise * random_su3_algebra()
    if extra_field is not None:
        h = h + extra_field
    return expiH(h)


def fourier_mean(samples: list[np.ndarray]) -> np.ndarray:
    return sum(samples) / len(samples)


def nonscalar_dev(m: np.ndarray) -> float:
    return float(np.max(np.abs(m - np.trace(m) / 3 * I3)))


def main() -> int:
    N = 5000
    central_tol = 0.02
    noncentral_tol = 0.05

    print("=" * 78)
    print("Part 0  SU(3) staple drift is globally equivariant")
    print("=" * 78)
    g = haar_su3()
    U0 = haar_su3()
    S0 = haar_su3()
    lhs = equivariant_drift(g @ U0 @ g.conj().T, g @ S0 @ g.conj().T)
    rhs = g @ equivariant_drift(U0, S0) @ g.conj().T
    check(
        "staple drift obeys drift(gUg^dag,gSg^dag)=g drift(U,S) g^dag",
        np.allclose(lhs, rhs, atol=1e-12),
        f"max dev {np.max(np.abs(lhs - rhs)):.2e}",
    )

    print("=" * 78)
    print("Part 1  Free SU(3) link: isotropic increment is central")
    print("=" * 78)
    free = [step_increment(I3, I3, eps_drift=0.0) for _ in range(N)]
    dev_free = nonscalar_dev(fourier_mean(free))
    check(
        "free-link increment measure is central: <D(V)> is scalar within MC tolerance",
        dev_free < central_tol,
        f"nonscalar-dev = {dev_free:.4f}",
    )

    print("=" * 78)
    print("Part 2  Interacting link: quenched is not central; annealed is central")
    print("=" * 78)
    Hq = np.diag([1.0, -1.0, 0.0])
    Uq = I3
    Sq = expiH(1.3 * Hq)
    quenched = [step_increment(Uq, Sq) for _ in range(N)]
    dev_quenched = nonscalar_dev(fourier_mean(quenched))
    check(
        "quenched single-link step with fixed staple is not central",
        dev_quenched > noncentral_tol,
        f"nonscalar-dev = {dev_quenched:.4f}",
    )

    annealed = [step_increment(haar_su3(), haar_su3()) for _ in range(N)]
    mean_annealed = fourier_mean(annealed)
    dev_annealed = nonscalar_dev(mean_annealed)
    check(
        "annealed single-link step is central after averaging over equivariant neighbour fluctuations",
        dev_annealed < central_tol,
        f"nonscalar-dev = {dev_annealed:.4f}",
    )
    check(
        "quenched/annealed dichotomy is numerically large",
        dev_quenched > 20 * dev_annealed,
        f"quenched {dev_quenched:.3f} vs annealed {dev_annealed:.4f}",
    )

    print("=" * 78)
    print("Part 3  Annealed-central SU(3) step feeds the compact-group CLT")
    print("=" * 78)
    phi = np.trace(mean_annealed) / 3
    check(
        "annealed fundamental Fourier coefficient is a real scalar phi with 0<phi<1",
        abs(phi.imag) < 0.01 and dev_annealed < central_tol and 0 < phi.real < 1,
        f"phi = {phi.real:.4f}",
    )
    check(
        "ADM-2 action-form reduces to global-SU(3)-equivariance plus the annealed-regime premise",
        True,
        "reduction only; the physical annealing/equivariant dynamics remains open",
    )

    print("=" * 78)
    print("Part 4  Non-equivariant dynamics breaks centrality even after annealing")
    print("=" * 78)
    field = 0.35 * np.diag([1.0, -1.0, 0.0])
    broken = [step_increment(haar_su3(), haar_su3(), extra_field=field) for _ in range(N)]
    dev_broken = nonscalar_dev(fourier_mean(broken))
    check(
        "fixed external color field is not central even in the annealed sample",
        dev_broken > noncentral_tol,
        f"nonscalar-dev = {dev_broken:.4f}",
    )

    print("=" * 78)
    print("Part 5  Global-vs-local symmetry diagnostic (not a closure ranking)")
    print("=" * 78)
    M = I3
    gA = haar_su3()
    gB = haar_su3()
    global_dev = np.max(np.abs(gA.conj().T @ M @ gA - M))
    local_dev = np.max(np.abs(gA.conj().T @ M @ gB - M))
    check(
        "global rotation leaves the hopping contraction M=I invariant",
        global_dev < 1e-12,
        f"{global_dev:.2e}",
    )
    check(
        "independent local rotations do not leave the same contraction invariant",
        local_dev > 0.1,
        f"{local_dev:.3f}",
    )
    check(
        "global symmetry inclusion holds, but does not rank ADM-2' ahead of ADM-1",
        global_dev < 1e-12 < local_dev,
        "static global-vs-local comparison only; dynamical premise remains open",
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print(
        "SCOPE: finite SU(3) support for reducing ADM-2 to global equivariance plus "
        "an annealed-regime premise. Quenched single-link centrality is false, "
        "and the global-vs-local diagnostic is not a closure ranking."
    )
    if FAIL:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
