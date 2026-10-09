"""Independent arithmetic and array checks for the E1-prime referee report.

The quarantined INVALID_*.npz file is excluded explicitly.  This script does
not import or execute anything under lit_johnston/.
"""

from __future__ import annotations

import glob
import math
import os

import numpy as np


PI = math.pi
SQRT6 = math.sqrt(6.0)
A = 1.0 / (2.0 * PI * SQRT6)
ELL_P = 1.616255e-35
GPC = 3.0857e25
HBARC = 1.97327e-16  # GeV m
M_PL = 1.220890e19  # GeV


def massless_rows() -> None:
    print("massless valid-array recomputation")
    grouped: dict[float, list[tuple[float, float]]] = {}
    for path in sorted(glob.glob("out/massless_[AB]_*.npz")):
        assert not os.path.basename(path).startswith("INVALID_")
        with np.load(path, allow_pickle=False) as d:
            if not math.isinf(float(d["Ts"])):
                continue
            nf = d["NF"]
            s = float(d["s"])
            D = float(d["D"])
            mean_exact = float(d["m1f"])
            fano = float(nf.var(ddof=1) / mean_exact)
            kappa = (fano - 1.0) * D / s
            grouped.setdefault(s, []).append((s / D, fano - 1.0))
            print(
                f"  {os.path.basename(path):44s} "
                f"F={fano:7.4f}  kappa={(kappa):8.3f}"
            )
    print("  through-origin fits of F-1=kappa*s/D")
    for s, pairs in sorted(grouped.items()):
        x = np.array([p[0] for p in pairs])
        y = np.array([p[1] for p in pairs])
        slope = float(np.dot(x, y) / np.dot(x, x))
        print(f"    s/ell={s:g}: kappa_fit={slope:.4f}")


def exact_constants() -> None:
    c = PI / 24.0
    sigma_mean = 1.0 / math.sqrt(PI * c)
    sigma_var = 1.0 / (2.0 * c) - sigma_mean**2
    # E[L^2] -> (pi/2) [int_0^inf exp(-c s^2) ds]^2 = 3 pi.
    el2_limit = (PI / 2.0) * (math.sqrt(PI) / (2.0 * math.sqrt(c))) ** 2
    floor_coeff = (
        A**2
        * math.sqrt(3.0 * PI)
        * 4.0
        * PI
        * math.sqrt(PI / 2.0)
    )
    crossing = (1.0 / floor_coeff) ** (2.0 / 3.0)
    seed_coeff = SQRT6 / 96.0
    renewal_gamma_coeff = math.sqrt(1.0 / (2.0 * PI * SQRT6))
    # q(t)=int d^3x P1(t,x)=2 pi sqrt(6)t - 12/t + ... .
    # The logarithmic Laplace-transform term moves s=+/- i m to a conjugate
    # pair with Re(s)=3 pi A m^3 ell^2=3/(2 sqrt(6)) m^3 ell^2.
    mean_pole_coeff = 3.0 * PI * A
    print("exact/asymptotic constants")
    print(f"  <sigma>/ell^2={sigma_mean:.12f}")
    print(f"  sd(sigma)/ell^2={math.sqrt(sigma_var):.12f}")
    print(f"  E[L^2] limit={el2_limit:.12f}; 3pi={3*PI:.12f}")
    print(f"  point-floor coefficient={floor_coeff:.12f}")
    print(f"  point-floor envelope crossing m*tau={crossing:.12f}")
    print(f"  one-end seed coefficient={seed_coeff:.12f}")
    print(f"  overlap-free renewal gamma coefficient={renewal_gamma_coeff:.12f}")
    print(f"  mean complex-pole Re(s) coefficient={mean_pole_coeff:.12f}")


def gravity_margin() -> None:
    source_volume = 2.0 * 4.0 * PI / 3.0 * (1.2e4) ** 3
    s = 1.0e5
    D = GPC
    nbar = SQRT6 * source_volume / (2.0 * D * ELL_P**2)
    kappa0 = 5.0
    fcrit_raw = nbar
    fcrit_q10 = nbar / 100.0
    kcrit_raw = (fcrit_raw - 1.0) * D / s
    kcrit_q10 = (fcrit_q10 - 1.0) * D / s
    scale_ratio = (s / ELL_P) / 24.0
    p_raw = math.log(kcrit_raw / kappa0) / math.log(scale_ratio)
    p_q10 = math.log(kcrit_q10 / kappa0) / math.log(scale_ratio)
    print("gravity extrapolation margin")
    print(f"  Nbar={nbar:.6e}")
    print(f"  F needed for sd/mean=1: {fcrit_raw:.6e}")
    print(f"  F needed after an ad-hoc 10x amplitude penalty: {fcrit_q10:.6e}")
    print(f"  kappa needed if F-1=kappa*s/D: {kcrit_raw:.6e}")
    print(f"  kappa needed with 10x penalty: {kcrit_q10:.6e}")
    print(
        "  power p in kappa=5[(s/ell)/24]^p needed: "
        f"raw={p_raw:.4f}, 10x penalty={p_q10:.4f}"
    )


def matter_translation() -> None:
    print("matter translation from the stated asymptotic laws")
    seed_coeff = SQRT6 / 96.0
    gamma_coeff = math.sqrt(1.0 / (2.0 * PI * SQRT6))
    for name, mass_gev in (("electron", 0.51099895e-3), ("proton", 0.938272)):
        mell = mass_gev / M_PL
        lambda_bar = HBARC / mass_gev
        m2ell = mell**2 / ELL_P
        one_end = (1.0 / (seed_coeff * mell**2)) ** (1.0 / 3.0) * lambda_bar
        two_end = (1.0 / (2.0 * seed_coeff * mell**2)) ** (1.0 / 3.0) * lambda_bar
        packet_1km = SQRT6 / (24.0 * PI) * (m2ell * 1000.0) ** 2
        gamma = gamma_coeff * m2ell
        print(
            f"  {name:8s} one-end={one_end:.6e} m  two-end={two_end:.6e} m  "
            f"packet(sigma=1 km)={packet_1km:.6e}  "
            f"renewal exp(gamma*1 km)={math.exp(gamma*1000.0):.9f}"
        )


if __name__ == "__main__":
    exact_constants()
    gravity_margin()
    matter_translation()
    massless_rows()
