"""Independent, low-memory checks for the C5/F2 referee.

This deliberately does not import the worker scripts.  It uses only 1-D
quadrature/algebra and keeps arrays below a few MB.
"""

from __future__ import annotations

import math

import numpy as np


DEG = math.pi / 180.0
R_E = 6_371_000.0
HBARC = 1.973269804e-7  # eV m
HBAR = 6.582119569e-16  # eV s
C = 299_792_458.0
G = 6.67430e-11
MPC = 3.0857e22
M_SUN = 1.98892e30


def julian_day_utc(year: int, month: int, day: int, hour: int, minute: int, second: float) -> float:
    """Gregorian-calendar Julian day, independently written from the worker."""
    if month <= 2:
        year -= 1
        month += 12
    a = math.floor(year / 100)
    b = 2 - a + math.floor(a / 4)
    j0 = (
        math.floor(365.25 * (year + 4716))
        + math.floor(30.6001 * (month + 1))
        + day
        + b
        - 1524.5
    )
    return j0 + (hour + minute / 60.0 + second / 3600.0) / 24.0


def gmst_degrees(jd_ut1: float) -> float:
    """IAU-1982/Meeus GMST; UT1-UTC is immaterial at quoted precision."""
    t = (jd_ut1 - 2451545.0) / 36525.0
    return (
        280.46061837
        + 360.98564736629 * (jd_ut1 - 2451545.0)
        + 0.000387933 * t * t
        - t * t * t / 38_710_000.0
    ) % 360.0


def altitude_degrees(ra_deg: float, dec_deg: float, lat_deg: float, lon_deg_east: float, jd: float) -> float:
    h = ((gmst_degrees(jd) + lon_deg_east - ra_deg + 180.0) % 360.0 - 180.0) * DEG
    lat = lat_deg * DEG
    dec = dec_deg * DEG
    return math.asin(math.sin(lat) * math.sin(dec) + math.cos(lat) * math.cos(dec) * math.cos(h)) / DEG


def slab_transmission(k: float, q: complex, length: float) -> complex:
    """Exact scalar transmission through one uniform slab, vacuum on both sides."""
    den = np.cos(q * length) - 0.5j * (k / q + q / k) * np.sin(q * length)
    return np.exp(-1j * k * length) / den


def halfspace_surface(kz: float, qz: complex) -> complex:
    """Total field just outside/inside a step for unit incident amplitude."""
    return 2.0 * kz / (kz + qz)


def main() -> None:
    print("GEOMETRY")
    jd = julian_day_utc(2017, 8, 17, 12, 41, 4.43)
    # AT2017gfo optical counterpart, not the NGC 4993 nucleus.
    ra = 15.0 * (13 + 9 / 60 + 48.089 / 3600)
    dec = -(23 + 22 / 60 + 53.35 / 3600)
    # LAL detector constants converted from radians.
    sites = {
        "H1": (0.81079526383 / DEG, -2.08405676917 / DEG),
        "L1": (0.53342313506 / DEG, -1.58430937078 / DEG),
    }
    for name, (lat, lon) in sites.items():
        alt = altitude_degrees(ra, dec, lat, lon, jd)
        chord = -2 * R_E * math.sin(alt * DEG)
        rmin = R_E * math.cos(alt * DEG)
        print(f"{name}: altitude={alt:+.4f} deg chord={chord/1e3:.2f} km rmin={rmin/1e3:.2f} km")

    print("\nDISPERSION BUDGET")
    budget = (9.51e-22) ** 2 * 40.0 * MPC
    col_h1 = 7.371e10
    col_l1 = 4.280e10
    print(f"budget={budget:.6e} eV^2 m")
    print(f"mu(H1)={budget/col_h1:.6e}; mu(L1)={budget/col_l1:.6e} eV^2 m^3/kg")
    # Quantify failure of the small-m expansion near the quoted H1 limit.
    mu = budget / col_h1
    rho = 10_626.0
    mass = math.sqrt(mu * rho)
    for f in (30.0, 100.0, 300.0):
        energy = 2 * math.pi * HBAR * f
        exact_m = abs(math.sqrt(energy * energy + mass * mass) - energy)
        asymptotic = mass * mass / (2 * energy)
        print(f"tachyonic core {f:4.0f} Hz: m/E={mass/energy:.3f}, exact/asymptotic={exact_m/asymptotic:.3f}")

    print("\nINTERFACE / RESONANCE CHECK")
    f = 100.0
    k = 2 * math.pi * f / C
    mu_placeholder = 1.0115e-21
    q_t = math.sqrt(k * k + mu_placeholder * 2600.0 / HBARC**2)
    kappa_m = math.sqrt(mu_placeholder * 2600.0 / HBARC**2 - k * k)
    print(f"surface massive |h|={abs(halfspace_surface(k, 1j*kappa_m)):.6e}")
    print(f"surface tachyonic |h|={abs(halfspace_surface(k, q_t)):.6e}")
    # A finite tachyonic slab has exact unit-transmission resonances qL=n*pi.
    n = 10_000
    l_res = n * math.pi / q_t
    t_res = slab_transmission(k, q_t, l_res)
    t_quarter = slab_transmission(k, q_t, l_res + math.pi / (2 * q_t))
    print(f"tachyonic slab resonance |t|={abs(t_res):.12f}; antiresonance |t|={abs(t_quarter):.6e}")

    print("\nPULSAR BORN SCALE")
    m_ns = 1.3 * M_SUN
    r_ns = 12_000.0
    phi_avg = 1.5 * G * m_ns / r_ns
    mu_ns = 1.3e-4 * 4 * math.pi * G * HBARC**2 / phi_avg
    rho_ns = 3 * m_ns / (4 * math.pi * r_ns**3)
    print(f"mu_Born={mu_ns:.6e}; m(mean rho)={math.sqrt(mu_ns*rho_ns):.6e} eV; mR={math.sqrt(mu_ns*rho_ns)*r_ns/HBARC:.6f}")
    # Circular-orbit tensor algebra: lambda_i lambda_j and n_i n_j have
    # equal-and-opposite oscillatory parts, so the two stated source pieces
    # have equal oscillatory coefficients when v^2=GM/r.
    angles = np.linspace(0.0, 2 * math.pi, 4096, endpoint=False)
    nn_xx = np.cos(angles) ** 2
    ll_xx = np.sin(angles) ** 2
    c_nn = 2 * np.mean(nn_xx * np.cos(2 * angles))
    c_ll = 2 * np.mean(ll_xx * np.cos(2 * angles))
    print(f"cos(2Omega t) coefficients nn_xx={c_nn:+.6f}, lambda_lambda_xx={c_ll:+.6f}")

    print("\nRADIATION-ERA GROWTH")
    for a in (35.0, 64.0, 4.0e3, 8.0e3, 3.0e13):
        p = (-0.5 + math.sqrt(0.25 + a)) / 2.0
        per_lna = 2 * p
        print(f"A={a:.3e}: exact dlnh/dlna={per_lna:.6e}; sqrt(A)={math.sqrt(a):.6e}")
    print("massive WKB: h is proportional to a^(-3/2) m^(-1/2)")
    print("  constant m -> a^-3/2; m proportional to T -> a^-1; m^2 proportional to number density -> a^-3/4")


if __name__ == "__main__":
    main()
