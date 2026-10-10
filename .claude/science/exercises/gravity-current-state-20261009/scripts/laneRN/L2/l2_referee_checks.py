"""Independent spot checks for the lane-RN L2 referee report.

This does not alter or import any claimed verdict.  It checks:
1. the exceptional K=pi resonance branch of the 1D cosine band;
2. the relative-tolerance failure in the worker's 1D nullity control;
3. fresh-seed finite-basis singular gaps in representative d>=2 cases;
4. the scalar-constraint preservation condition after vector constraints are
   removed from H_N; and
5. the m=1 tadpole-subtracted TT Hessians at a larger volume/smaller step.
"""

import numpy as np

import l2_collision_invariants as ci
import l2_sunset_mu as sm


def flat_1d_branch():
    k = np.linspace(-np.pi, np.pi, 257, endpoint=False)
    q = np.roll(k, 71)
    k2 = np.pi - k
    q2 = np.pi - q
    eps = lambda x: -2 * np.cos(x)
    energy_error = np.max(np.abs(eps(k) + eps(k2) - eps(q) - eps(q2)))
    defect_sin1 = np.max(np.abs(np.sin(k) + np.sin(k2) - np.sin(q) - np.sin(q2)))
    defect_sin2 = np.max(np.abs(np.sin(2 * k) + np.sin(2 * k2)
                                - np.sin(2 * q) - np.sin(2 * q2)))
    print("1D TB K=pi branch:")
    print(f"  max energy residual = {energy_error:.3e}")
    print(f"  max sin(k) defect   = {defect_sin1:.6f}")
    print(f"  max sin(2k) defect  = {defect_sin2:.3e}")


def sampled_1d_roundoff():
    ci.rng = np.random.default_rng(12345)
    eps = ci.make_disp("TB", 0.0)
    res = ci.sample_res(1, eps, eps, 100)
    ns = ci.nvecs(1, 8)
    A = ci.design(res, 1, ns, np.sin, False)
    rel_nullity, sv = ci.nullity(A)
    abs_nullity = int(np.sum(sv < 1e-10))
    print("1D TB random-sampler control, R=8:")
    print(f"  singular range      = [{sv[-1]:.3e}, {sv[0]:.3e}]")
    print(f"  worker rel nullity  = {rel_nullity}")
    print(f"  nullity at abs 1e-10= {abs_nullity}")


def fresh_gap(label, d, kind_a, mass_a, kind_b, mass_b, two_species, n_sample, radius):
    eps_a = ci.make_disp(kind_a, mass_a)
    eps_b = ci.make_disp(kind_b, mass_b)
    res = ci.sample_res(d, eps_a, eps_b, n_sample)
    ns = ci.nvecs(d, radius)
    A = ci.design(res, d, ns, np.sin, two_species) / np.sqrt(len(res))
    sv = np.linalg.svd(A, compute_uv=False)
    print(f"{label}: rows={len(res)}, cols={A.shape[1]}, "
          f"smin={sv[-1]:.6e}, smax={sv[0]:.6e}, ratio={sv[-1]/sv[0]:.6e}")


def hn_scalar_chain():
    J = 1.0
    K = np.array([[0.0, -J / np.sqrt(2)], [-J / np.sqrt(2), J / 2]])
    # qdot=K p, so preservation of S proportional to h_t requires qdot_t=0.
    print("H_N scalar chain without G:")
    print(f"  h_t dot coefficients on (E_t,E_z) = {K[0].tolist()}")
    print("  preserving S=0 therefore imposes E_z=0 (for nonzero k)")


def sunset_large_volume():
    f, fp = sm.fsym(1, "sin")
    print("m=1, L=48, eps=0.04, tadpole-subtracted I4 response:")
    for channel in ("E", "T2"):
        out = sm.mu(48, 1.0, channel, f, fp, eps=0.04)
        print(f"  {channel}: mu_I4/lambda^2={out['mu2_I4part']:.12e}, "
              f"full_bare_mu/lambda^2={out['mu2_per_lam2']:.12e}, G''={out['G']:.3e}")


if __name__ == "__main__":
    flat_1d_branch()
    sampled_1d_roundoff()
    ci.rng = np.random.default_rng(987654321)
    fresh_gap("2D TB R=8", 2, "TB", 0.0, "TB", 0.0, False, 4000, 8)
    fresh_gap("3D KG R=4", 3, "KG", 1.0, "KG", 1.0, False, 4000, 4)
    fresh_gap("3D unequal KG R=4", 3, "KG", 1.0, "KG", 0.5, True, 4000, 4)
    hn_scalar_chain()
    sunset_large_volume()
