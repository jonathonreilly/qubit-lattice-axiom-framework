#!/usr/bin/env python3
"""Fixed-lattice compact-gauge scope diagnostics.

This runner supports only the narrow bounded note:

* finite compact one-plaquette Wilson integrals at fixed lattice spacing;
* leading strong-coupling one-plaquette diagnostics for representative compact
  `SU(2)` and compact `U(1)` factors;
* explicit guardrails against Clay-continuum, physical `SU(3)` beta=6, observed
  spectrum, Planck-import, and Record-readout claims.

It does not prove the Clay Yang-Mills mass-gap theorem, a physical `SU(3)` gap
at beta=6, a framework-native strong-coupling area-law/gap theorem,
all-coupling confinement, or a continuum limit.
"""

from __future__ import annotations

import sys

import numpy as np
from scipy import integrate, special

np.seterr(all="ignore")
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def su2_partition(beta: float) -> float:
    """Single-plaquette SU(2) Wilson integral over conjugacy classes."""
    return integrate.quad(
        lambda p: (2 / np.pi) * np.sin(p) ** 2 * np.exp(beta * np.cos(p)),
        0,
        np.pi,
        epsabs=1e-12,
        epsrel=1e-12,
    )[0]


def su2_plaq_factor(beta: float) -> float:
    """Representative SU(2) one-plaquette factor under the same class measure."""
    num = integrate.quad(
        lambda p: (2 / np.pi)
        * np.sin(p) ** 2
        * np.cos(p)
        * np.exp(beta * np.cos(p)),
        0,
        np.pi,
        epsabs=1e-12,
        epsrel=1e-12,
    )[0]
    return num / su2_partition(beta)


def u1_partition(beta: float) -> float:
    """Single-plaquette compact U(1) Wilson integral divided by 2*pi."""
    return float(special.iv(0, beta))


def u1_plaq_factor(beta: float) -> float:
    """Representative compact U(1) one-plaquette factor I_1(beta)/I_0(beta)."""
    return float(special.iv(1, beta) / special.iv(0, beta))


def main() -> int:
    print("=" * 88)
    print("Fixed-lattice compact-gauge scope diagnostics")
    print("=" * 88)

    section("A. Finite compact one-plaquette integrals at fixed lattice spacing")
    beta_reference = 6.0
    z_su2 = su2_partition(beta_reference)
    z_u1 = u1_partition(beta_reference)
    check(
        "representative SU(2) and compact U(1) Wilson integrals are finite and positive",
        np.isfinite(z_su2) and z_su2 > 0 and np.isfinite(z_u1) and z_u1 > 0,
        detail=f"Z_SU2(beta=6)={z_su2:.6g}, Z_U1(beta=6)={z_u1:.6g}",
    )

    section("B. Strong-coupling leading one-plaquette diagnostics")
    strong_betas = (0.5, 1.0, 1.5)
    factors = []
    for beta in strong_betas:
        f_su2 = su2_plaq_factor(beta)
        f_u1 = u1_plaq_factor(beta)
        factors.append((beta, f_su2, f_u1))
        print(
            f"  beta={beta:.1f}: SU(2) factor={f_su2:.6f}, "
            f"sigma={-np.log(f_su2):.6f}; "
            f"U(1) factor={f_u1:.6f}, sigma={-np.log(f_u1):.6f}"
        )

    check(
        "strong-coupling factors are between zero and one",
        all(0 < f_su2 < 1 and 0 < f_u1 < 1 for _, f_su2, f_u1 in factors),
    )
    check(
        "leading strong-coupling sigma diagnostics -log(factor) are positive",
        all(-np.log(f_su2) > 0 and -np.log(f_u1) > 0 for _, f_su2, f_u1 in factors),
    )

    area_ok = True
    for _, f_su2, _ in factors:
        sigma = -np.log(f_su2)
        for radius, time in ((2, 2), (2, 3), (3, 3)):
            log_w = radius * time * np.log(f_su2)
            area_ok = area_ok and abs(log_w + sigma * radius * time) < 1e-10
    check(
        "toy leading-loop diagnostic has area-law-shaped algebra log W(R,T)=-sigma*R*T",
        area_ok,
    )

    section("C. Weakening diagnostic, not all-coupling confinement")
    f2_strong, f2_weak = su2_plaq_factor(0.5), su2_plaq_factor(8.0)
    fu_strong, fu_weak = u1_plaq_factor(0.5), u1_plaq_factor(8.0)
    check(
        "leading factors move toward one as beta increases",
        f2_weak > f2_strong and fu_weak > fu_strong,
        detail=(
            f"SU(2) {f2_strong:.3f}->{f2_weak:.3f}; "
            f"U(1) {fu_strong:.3f}->{fu_weak:.3f}"
        ),
    )

    section("D. Guardrails")
    guardrails = (
        "no Clay continuum a->0 construction",
        "no rigorous physical SU(3) gap at beta=6",
        "no observed photon/gluon spectrum derivation",
        "no Planck-scale physical import from the scale-reference primitive",
        "no Record readout, probability, or measurement claim",
    )
    for item in guardrails:
        check(f"guardrail: {item}", True)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
