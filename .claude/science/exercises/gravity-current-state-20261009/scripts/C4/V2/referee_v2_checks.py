"""Independent checks for the C4/RV2 V2 referee report.

This script does not import or call any v2/v3 worker code.  It checks:
  1. the free-scalar Jacobian Hessian in the E channel;
  2. the same Hessian by finite-differencing the exact momentum flow;
  3. the normal-process sine-defect identity; and
  4. the generic L^2 growth of a first-moment vacuum norm.
"""

import numpy as np


def omega(kx, ky, kz, mass=1.0):
    return np.sqrt(
        mass**2
        + 4.0 * np.sin(kx / 2.0) ** 2
        + 4.0 * np.sin(ky / 2.0) ** 2
        + 4.0 * np.sin(kz / 2.0) ** 2
    )


def scalar_mu_e_jacobian(size, mass=1.0):
    """BZ quadrature of <(omega/2) J''(0)> in RN-L1 normalization.

    E flow: v=(sin(kx),-sin(ky),0)/2.  For a flow Jacobian J,
    J''(0)=(div v)^2+v.grad(div v).
    """
    grid = 2.0 * np.pi * (np.arange(size) + 0.5) / size - np.pi
    kx, ky = np.meshgrid(grid, grid, indexing="ij")
    sx, sy = np.sin(kx), np.sin(ky)
    cx, cy = np.cos(kx), np.cos(ky)
    jacobian_second = 0.25 * ((cx - cy) ** 2 - sx**2 - sy**2)
    total = 0.0
    for kz in grid:
        total += np.sum(0.5 * omega(kx, ky, kz, mass) * jacobian_second)
    return total / size**3


def inverse_e_flow(q, strain, sign):
    """Inverse of qdot=sign*sin(q)/2, with the torus branch preserved."""
    return 2.0 * np.arctan2(
        np.exp(-sign * strain / 2.0) * np.sin(q / 2.0), np.cos(q / 2.0)
    )


def local_scalar_energy(size, strain, mass=1.0):
    """Zero-point energy/site of the periodized bulk local flow."""
    grid = 2.0 * np.pi * (np.arange(size) + 0.5) / size - np.pi
    qx, qy = np.meshgrid(grid, grid, indexing="ij")
    kx = inverse_e_flow(qx, strain, +1.0)
    ky = inverse_e_flow(qy, strain, -1.0)
    total = 0.0
    for kz in grid:
        total += np.sum(0.5 * omega(kx, ky, kz, mass))
    return total / size**3


def finite_difference_mu(size, step, mass=1.0):
    zero = local_scalar_energy(size, 0.0, mass)
    return (
        local_scalar_energy(size, step, mass)
        - 2.0 * zero
        + local_scalar_energy(size, -step, mass)
    ) / step**2


def defect_identity_error(samples=100_000, seed=20261011):
    rng = np.random.default_rng(seed)
    q = rng.uniform(-1.0, 1.0, (samples, 3))
    kap = rng.uniform(-1.0, 1.0, (samples, 3))
    kap_prime = rng.uniform(-1.0, 1.0, (samples, 3))
    direct = (
        np.sin(q / 2.0 + kap)
        + np.sin(q / 2.0 - kap)
        - np.sin(q / 2.0 + kap_prime)
        - np.sin(q / 2.0 - kap_prime)
    )
    closed = 2.0 * np.sin(q / 2.0) * (np.cos(kap) - np.cos(kap_prime))
    return np.max(np.abs(direct - closed))


def first_moment_product_norm_per_site(size):
    """For orthogonal b_x|Omega>, ||sum_x x b_x Omega||^2/V."""
    x = np.arange(size) - (size - 1.0) / 2.0
    return np.mean(x**2)


print("free scalar, m=1, E channel, RN-L1 normalization")
for size in (32, 64, 128):
    print(f"Jacobian quadrature L={size:3d}: mu_E = {scalar_mu_e_jacobian(size):+.15e}")

print("independent exact-flow finite difference, L=128")
for step in (0.04, 0.02, 0.01, 0.005):
    print(f"step={step:7.4f}: mu_E = {finite_difference_mu(128, step):+.15e}")

print("T2 channel: div v = 0 identically, hence J=1 and mu_T2=0")
print(f"max sine-defect identity error: {defect_identity_error():.3e}")

print("first-moment product-vacuum norm density")
for size in (16, 32, 64, 128):
    value = first_moment_product_norm_per_site(size)
    print(f"L={size:3d}: N/V={value:.6f}, (N/V)/L^2={value/size**2:.9f}")
