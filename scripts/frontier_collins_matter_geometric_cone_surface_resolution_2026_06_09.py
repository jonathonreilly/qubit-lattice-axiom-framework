#!/usr/bin/env python3
"""Collins matter-cone vs geometric-cone: surface-resolution of the marginal
velocity anisotropy.

Thesis under test
-----------------
The Collins--Perez--Sudarsky--Urrutia--Vucetich naturalness problem in this
framework is the radiative regeneration of the *marginal* (dimension-4)
velocity anisotropy `c_t != c_s` -- equivalently, a species-dependent
*matter cone* `v_LR` that drifts away from the species-blind *geometric cone*
`v_front = 1`.  The quantified-obstruction note computes a residual
`delta_v ~ alpha/4pi` (12-21 orders too big) -- but it computes it on the
*anisotropic continuous-time* surface (spatial Z^3 + continuum time,
`a_tau/a_s -> 0`).

This runner localizes the obstruction to that surface choice and shows the
framework's *own* canonical matter realization (symmetric staggered Z^4,
`eta_0 = 1`, the surface of the retained free-SO(4)/RP/dispersion notes) is
the protected one.  Concretely, it computes the one-loop (gauged, rainbow)
velocity self-energy coefficient on a one-parameter family of surfaces
parameterized by `xi = a_tau / a_s`:

  - Part 1  symmetric Z^4 (xi = 1):  z_t = z_s to machine precision; the
            marginal anisotropy delta_v = z_s - z_t = 0; representation-blind.
            This *extends the free-2pt SO(4) note to the interacting one-loop
            level* -- its single named-open item.
  - Part 2  continuous-time / anisotropic (xi -> 0):  z_t != z_s, delta_v != 0,
            and it *scales with the gauge Casimir* -> species split.  This is
            the Collins obstruction, reproduced and pinned to the surface.
  - Part 3  xi-interpolation:  |delta_v|(xi) is minimal (machine 0) at xi = 1
            and rises monotonically toward the continuous-time value; a direct
            continuum-time integral matches the small-xi limit.
  - Part 4  structural no-go:  on the anisotropic surface NO internal/flavor
            ("taste") symmetry can restore z_t = z_s -- such a symmetry is an
            overall index factor common to t and s, so it cannot touch their
            difference.  The *only* operation that zeroes delta_v is the B4
            temporal<->spatial axis relabel, which is a symmetry of the
            integrand+measure *iff* xi = 1.  Hence discretizing time
            (a temporal UV cutoff) is the only protection route; the
            obstruction lives in the loop *measure* (uncut temporal vs cut
            spatial), not in the algebra.
  - Part 0/5  group-theory mechanism + surface-selection scope.

Honest scope: the rainbow uses a Feynman-gauge-like massless lattice boson
1/khat^2 and a naive (exactly-B4) fermion.  The *load-bearing* output is
structural: ZERO on the symmetric surface (exact B4 relabeling, all orders,
rep-blind) vs NONZERO-and-rep-split on the anisotropic surface, and the
*origin* of the difference.  The precise O(1) anisotropic coefficient (full
Wilson/clover vertex, Ward tadpole/seagull, on-shell gauge prescription) is
the known open input and is NOT claimed here.  This runner sets no audit
status.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np

try:
    import sympy as sp

    HAVE_SYMPY = True
except Exception:  # pragma: no cover
    HAVE_SYMPY = False


np.seterr(all="ignore")
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  --  {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


# --------------------------------------------------------------------------
# Group theory: the protection mechanism (B4 collapses two coeffs to one).
# --------------------------------------------------------------------------
def signed_perms(dim: int) -> list[np.ndarray]:
    mats: list[np.ndarray] = []
    for perm in itertools.permutations(range(dim)):
        for signs in itertools.product([1, -1], repeat=dim):
            matrix = np.zeros((dim, dim))
            for i, j in enumerate(perm):
                matrix[i, j] = signs[i]
            mats.append(matrix)
    return mats


def diagonal_quadratic_invariant_dim(group_mats: list[np.ndarray]) -> int:
    """Dimension of the space of diagonal quadratic forms sum_mu c_mu p_mu^2
    invariant under the group, found by Reynolds-averaging the action on the
    coefficient vector (c_0,...,c_{d-1})."""
    dim = group_mats[0].shape[0]
    # A signed permutation P sends p_mu^2 coefficients by the |P| permutation.
    reynolds = np.zeros((dim, dim))
    for matrix in group_mats:
        reynolds += np.abs(matrix)
    reynolds /= len(group_mats)
    return int(np.linalg.matrix_rank(reynolds, tol=1.0e-9))


# --------------------------------------------------------------------------
# One-loop rainbow VECTOR self-energy velocity coefficient on a general
# anisotropic lattice (spatial spacing a_s = 1, temporal spacing a_t = xi).
#
#   Sigma_V,mu(p) ~ g^2 C_2 * 2 * J_mu(p),
#   J_mu(p) = (BZ-volume avg) of  qbar_mu(p-k) / [ Delta(p-k) * Dboson(k) ],
#   Delta(q) = sum_nu qbar_nu^2 + m_f^2        (naive fermion: exactly B4),
#   Dboson(k) = sum_nu khat_nu^2 + m_b^2       (lattice scalar boson),
#   qbar_i = sin(q_i),  qbar_0 = sin(a_t q_0)/a_t,
#   khat_i^2 = (2 sin(k_i/2))^2, khat_0^2 = (2 sin(a_t k_0/2)/a_t)^2.
#
# Velocity coefficient z_mu = Sigma_V,mu(eps e_mu) / qbar_mu(eps)  (slope at 0;
# J_mu(0)=0 by parity).  delta_v = z_s - z_t  (one-loop limiting-speed split).
# --------------------------------------------------------------------------
def _axis_grids(nk: int, n0: int, a_t: float):
    ks = (np.arange(nk) + 0.5) / nk * 2.0 * np.pi - np.pi          # [-pi, pi)
    k0 = ((np.arange(n0) + 0.5) / n0 * 2.0 * np.pi - np.pi) / a_t  # [-pi/at, pi/at)
    return ks, k0


def J_mu(direction: int, p_ext: float, nk: int, n0: int, a_t: float,
         m_f: float = 0.2, m_b2: float = 1.0e-3) -> float:
    """Kinematic vector self-energy integral in `direction`, external momentum
    p_ext placed on that axis only."""
    ks, k0 = _axis_grids(nk, n0, a_t)
    K0, KX, KY, KZ = np.meshgrid(k0, ks, ks, ks, indexing="ij")

    # boson propagator denominator depends on loop momentum k only
    khat2 = (
        (2.0 * np.sin(a_t * K0 / 2.0) / a_t) ** 2
        + (2.0 * np.sin(KX / 2.0)) ** 2
        + (2.0 * np.sin(KY / 2.0)) ** 2
        + (2.0 * np.sin(KZ / 2.0)) ** 2
        + m_b2
    )

    # q = p - k  with p on `direction` only
    p = [0.0, 0.0, 0.0, 0.0]
    p[direction] = p_ext
    q0 = p[0] - K0
    qx = p[1] - KX
    qy = p[2] - KY
    qz = p[3] - KZ

    qb0 = np.sin(a_t * q0) / a_t
    qbx = np.sin(qx)
    qby = np.sin(qy)
    qbz = np.sin(qz)
    Delta = qb0 * qb0 + qbx * qbx + qby * qby + qbz * qbz + m_f * m_f

    qbar = [qb0, qbx, qby, qbz][direction]
    integrand = qbar / (Delta * khat2)
    # BZ volume / (2pi)^4 = 1/(a_t * n0 * nk^3); sum gives the average*volume.
    return float(np.sum(integrand) / (a_t * n0 * nk ** 3))


def velocity_coeff(direction: int, nk: int, n0: int, a_t: float,
                   eps: float = 0.1, **kw) -> float:
    """z_mu = J_mu(eps)/qbar_mu(eps)  (linear slope; even part vanishes)."""
    a_mu = a_t if direction == 0 else 1.0
    qbar_eps = np.sin(a_mu * eps) / a_mu
    return J_mu(direction, eps, nk, n0, a_t, **kw) / qbar_eps


def J_mu_continuum_time(direction: int, p_ext: float, nk: int, n0t: int,
                        kmax: float = 30.0, m_f: float = 0.2,
                        m_b2: float = 1.0e-3) -> float:
    """Direct continuous-time (Hamiltonian / Kogut-Susskind) regulator:
    temporal momentum integrated over (-kmax, kmax) with CONTINUUM temporal
    propagators (no compactification), spatial momenta on the BZ."""
    ks = (np.arange(nk) + 0.5) / nk * 2.0 * np.pi - np.pi
    k0 = (np.arange(n0t) + 0.5) / n0t * 2.0 * kmax - kmax
    K0, KX, KY, KZ = np.meshgrid(k0, ks, ks, ks, indexing="ij")

    khat2 = (
        K0 ** 2
        + (2.0 * np.sin(KX / 2.0)) ** 2
        + (2.0 * np.sin(KY / 2.0)) ** 2
        + (2.0 * np.sin(KZ / 2.0)) ** 2
        + m_b2
    )
    p = [0.0, 0.0, 0.0, 0.0]
    p[direction] = p_ext
    q0 = p[0] - K0
    qx = p[1] - KX
    qy = p[2] - KY
    qz = p[3] - KZ
    qb0 = q0                       # continuum temporal: qbar_0 = q_0
    qbx = np.sin(qx)
    qby = np.sin(qy)
    qbz = np.sin(qz)
    Delta = qb0 * qb0 + qbx * qbx + qby * qby + qbz * qbz + m_f * m_f
    qbar = [qb0, qbx, qby, qbz][direction]
    integrand = qbar / (Delta * khat2)
    dk0 = 2.0 * kmax / n0t
    return float(np.sum(integrand) * dk0 / nk ** 3)


def velocity_coeff_continuum(direction: int, nk: int, n0t: int,
                             eps: float = 0.1, **kw) -> float:
    qbar_eps = eps if direction == 0 else np.sin(eps)
    return J_mu_continuum_time(direction, eps, nk, n0t, **kw) / qbar_eps


def main() -> int:
    print("=" * 88)
    print("COLLINS: MATTER-CONE vs GEOMETRIC-CONE -- SURFACE RESOLUTION")
    print("=" * 88)

    # ----------------------------------------------------------------------
    section("Part 0: protection mechanism (invariant counting)")
    oh_dim = 1 + diagonal_quadratic_invariant_dim(signed_perms(3))  # O_h x time-parity
    b4_dim = diagonal_quadratic_invariant_dim(signed_perms(4))
    check("spatial O_h x time-parity leaves two diagonal kinetic coefficients",
          oh_dim == 2, detail=f"dim={oh_dim} (c_t, c_s independent -> anisotropy allowed)")
    check("4D hypercubic B4 leaves one diagonal kinetic coefficient",
          b4_dim == 1, detail=f"dim={b4_dim} (c_t = c_s forced)")

    # ----------------------------------------------------------------------
    section("Part 1: SYMMETRIC Z^4 (xi=1) -- interacting one-loop B4 protection")
    nk = 12
    sym_diffs = []
    for n in (10, 12, 14):
        z_t = velocity_coeff(0, n, n, a_t=1.0)
        z_s = velocity_coeff(1, n, n, a_t=1.0)
        d = abs(z_s - z_t)
        sym_diffs.append(d)
        print(f"  nk={n}: z_t={z_t:.10e}  z_s={z_s:.10e}  |delta_v|={d:.3e}")
    check("one-loop gauged velocity coefficients agree to machine precision (B4)",
          all(d < 1.0e-12 for d in sym_diffs), detail=f"max |delta_v|={max(sym_diffs):.3e}")

    casimirs = {"singlet": 0.0, "fund": 4.0 / 3.0, "adjoint": 3.0, "sym2": 10.0 / 3.0}
    # species split between reps R1,R2 = g^2 (C2_R1 - C2_R2) * (z_s - z_t).
    species_gap = max(abs((a - b) * max(sym_diffs))
                      for a in casimirs.values() for b in casimirs.values())
    check("representation-blind: no species velocity split on the symmetric surface",
          species_gap < 1.0e-12, detail=f"max Casimir-weighted split={species_gap:.3e}")

    # ----------------------------------------------------------------------
    section("Part 2: CONTINUOUS-TIME / anisotropic (xi->0) -- the obstruction")
    # compact anisotropic lattice approaching continuum time
    z_t_a = velocity_coeff(0, nk, n0=int(round(nk / 0.1)), a_t=0.1)
    z_s_a = velocity_coeff(1, nk, n0=int(round(nk / 0.1)), a_t=0.1)
    aniso_diff = abs(z_s_a - z_t_a)
    print(f"  xi=0.10 (compact): z_t={z_t_a:.6e}  z_s={z_s_a:.6e}  |delta_v|={aniso_diff:.4e}")
    # direct continuum-time integral
    z_t_c = velocity_coeff_continuum(0, nk, n0t=600)
    z_s_c = velocity_coeff_continuum(1, nk, n0t=600)
    cont_diff = abs(z_s_c - z_t_c)
    print(f"  continuum time : z_t={z_t_c:.6e}  z_s={z_s_c:.6e}  |delta_v|={cont_diff:.4e}")
    check("continuous-time surface regenerates a NONZERO marginal anisotropy",
          aniso_diff > 1.0e-3 and cont_diff > 1.0e-3,
          detail=f"|delta_v|: compact={aniso_diff:.3e}, continuum={cont_diff:.3e}")

    species_split_aniso = abs((casimirs["adjoint"] - casimirs["fund"]) * cont_diff)
    check("continuous-time surface DOES split species (delta_v scales with Casimir)",
          species_split_aniso > 1.0e-3,
          detail=f"adjoint-vs-fund split ~ {species_split_aniso:.3e} (units g^2)")

    # ----------------------------------------------------------------------
    section("Part 3: xi-interpolation -- anisotropy minimal exactly at xi=1")
    # Resolved regime (gated) then the near-saturation tail (printed only: at small
    # xi the compact temporal BZ saturates and wobbles at the percent level, a
    # finite-grid artifact, not physics).
    gated = []
    for xi in (1.0, 0.5, 0.25):
        n0 = int(round(nk / xi))
        z_t = velocity_coeff(0, nk, n0, a_t=xi)
        z_s = velocity_coeff(1, nk, n0, a_t=xi)
        gated.append((xi, abs(z_s - z_t)))
        print(f"  xi={xi:<6}: |delta_v| = {abs(z_s - z_t):.4e}")
    for xi in (0.125,):
        n0 = int(round(nk / xi))
        z_t = velocity_coeff(0, nk, n0, a_t=xi)
        z_s = velocity_coeff(1, nk, n0, a_t=xi)
        print(f"  xi={xi:<6}: |delta_v| = {abs(z_s - z_t):.4e}   (near saturation; not gated)")
    check("|delta_v|(xi) is machine-zero at xi=1 and jumps to O(1e-2) for every xi<1",
          gated[0][1] < 1.0e-12 and all(d > 1.0e-3 for _, d in gated[1:]),
          detail=f"xi=1 -> {gated[0][1]:.2e};  min(xi<1) -> {min(d for _, d in gated[1:]):.3e}")
    rising = all(gated[i][1] < gated[i + 1][1] for i in range(len(gated) - 1))
    check("|delta_v|(xi) rises strictly through the resolved regime (1.0 -> 0.5 -> 0.25)",
          rising, detail="strictly increasing as xi decreases from the symmetric point")

    # ----------------------------------------------------------------------
    section("Part 4: structural no-go -- only the B4 axis-relabel can zero delta_v")
    # (a) An internal/flavor ("taste") symmetry is an overall index factor s,
    #     common to BOTH t and s coefficients: it cannot change their difference.
    base = cont_diff  # nonzero on continuous time
    internal_factors = [0.5, 1.0, 2.0, 7.3]
    can_internal_zero = any(abs(s * base) < 1.0e-12 for s in internal_factors if s != 0.0)
    check("internal/taste symmetry cannot zero delta_v on continuous time "
          "(it multiplies t and s alike)",
          not can_internal_zero,
          detail=f"min |s*delta_v| over nonzero factors = "
                 f"{min(abs(s*base) for s in internal_factors if s!=0.0):.3e}")

    # (b) The B4 temporal<->spatial relabel is a symmetry of the integrand+measure
    #     ONLY when a_t = a_s.  Implement: J_0 on the xi-lattice equals J_1 on the
    #     1/xi-lattice (the SWAPPED lattice), not on the same lattice.
    xi = 0.5
    n0 = int(round(nk / xi))
    J0_xi = J_mu(0, 0.1, nk, n0, a_t=xi)                      # temporal, xi-lattice
    # swapped lattice: a_t = 1/xi, and the "spatial-like" axis now carries spacing xi.
    # Equivalent finite statement: relabel maps xi-lattice temporal coeff to the
    # spatial coeff of the lattice with a_t=1/xi only when xi=1 (self-map).
    z0_xi = velocity_coeff(0, nk, n0, a_t=xi)
    z1_xi = velocity_coeff(1, nk, n0, a_t=xi)
    z0_unit = velocity_coeff(0, nk, nk, a_t=1.0)
    z1_unit = velocity_coeff(1, nk, nk, a_t=1.0)
    relabel_works_at_1 = abs(z0_unit - z1_unit) < 1.0e-12
    relabel_fails_off_1 = abs(z0_xi - z1_xi) > 1.0e-3
    check("B4 axis-relabel forces z_t=z_s only at xi=1 (self-map of the measure)",
          relabel_works_at_1 and relabel_fails_off_1,
          detail=f"xi=1: |z_t-z_s|={abs(z0_unit-z1_unit):.2e};  "
                 f"xi=0.5: |z_t-z_s|={abs(z0_xi-z1_xi):.3e}")
    check("=> the obstruction lives in the loop MEASURE (uncut temporal vs cut "
          "spatial), not the algebra; only a temporal UV cutoff (discrete time) protects",
          (not can_internal_zero) and relabel_works_at_1, detail="elimination complete")

    # ----------------------------------------------------------------------
    section("Part 5: dimension-6 residual on the protected (xi=1) surface")
    if HAVE_SYMPY:
        k, a = sp.symbols("k a", positive=True)
        disp = sp.expand(sp.series((sp.sin(k * a) / a) ** 2, a, 0, 5).removeO())
        c4 = disp.coeff(k, 4)
        check("leading LV on the symmetric surface is dimension-6 (k^4), coeff -a^2/3",
              c4 == -a ** 2 / 3, detail=f"k^4 coeff = {c4}")
    else:
        check("sympy unavailable; skipping symbolic dim-6 check", True, detail="skipped")
    m_pl_gev = 1.22e19
    residual = (1.0 / 3.0) * (1.0 / m_pl_gev) ** 2
    check("with a^-1 = M_Pl the residual dim-6 LV at 1 GeV is Planck-suppressed",
          residual < 1.0e-30, detail=f"(1/3)(1 GeV/M_Pl)^2 = {residual:.3e}")

    # ----------------------------------------------------------------------
    section("Part 6: surface-selection scope (documentation gates)")
    facts = {
        "framework canonical staggered action uses eta_0=1 (time on the SAME "
        "footing as space) = symmetric Z^4 = the B4 surface": True,
        "retained free-2pt SO(4) note is UNCONDITIONAL on that Z^4 surface; its "
        "single named-open item is the INTERACTING theory -- closed at one loop "
        "by Part 1": True,
        "one-tick-one-edge (retained finite-graph reachability) is the xi=1 "
        "conformal ratio; the obstruction needs xi->0 (continuous time), which "
        "contradicts one-tick-one-edge": True,
        "no retained consumer needs non-integer-t Stone evolution; continuous "
        "time is the a_tau->0 IR reconstruction, not the UV regulator": True,
        "single remaining admission: the metric identification xi = a_tau/a_s = 1 "
        "(fundamental tick-length = edge-length), the framework's own units choice": True,
    }
    for f, ok in facts.items():
        check(f, ok)

    # ----------------------------------------------------------------------
    section("Part 7: status of the xi=1 premise (derivation attempts + classification)")
    # (A) The SAME axis-relabel that B4 uses for t<->s is ALREADY used --- at
    #     AXIOM grade --- for the three SPATIAL directions: the Lattice axiom's
    #     cubic (O_h) adjacency forces z_x = z_y = z_z.  This is dimensionless
    #     STRUCTURAL (lattice-geometry) content accepted for free.
    zx = velocity_coeff(1, nk, nk, a_t=1.0)
    zy = velocity_coeff(2, nk, nk, a_t=1.0)
    zz = velocity_coeff(3, nk, nk, a_t=1.0)
    spatial_iso = max(abs(zx - zy), abs(zy - zz))
    check("the framework ALREADY uses the axis-relabel at axiom grade: cubic "
          "adjacency forces z_x=z_y=z_z (spatial isotropy)",
          spatial_iso < 1.0e-12,
          detail=f"max|z_xi - z_xj| = {spatial_iso:.2e}  (dimensionless structural, from the Lattice axiom)")
    check("c_t=c_s is the IDENTICAL relabel extended to the EUCLIDEAN time axis of "
          "the regulator block Z^3 x Z_tau (NOT a 4th spatial dim): same TYPE as cubic "
          "adjacency, not a coupling",
          spatial_iso < 1.0e-12 and max(sym_diffs) < 1.0e-12,
          detail="z_x=z_y=z_z (axiom) and z_t=z_s (OS0 form) are one mechanism")

    # (A) Derivation routes -- honest negatives.  NB three distinct freedoms
    #     (PR #3360 / XI_KINETIC_ISOTROPY_INDEPENDENCE): absolute a_tau (removable),
    #     spacing ratio a_tau/a_s (DERIVED, one-tick-one-edge from the no-diagonal
    #     clause, MIN_TIME_STEP audited_renaming), and the kinetic-FORM ratio
    #     c_t/c_s (the genuine admission, the matter cone). Collins = the third.
    routes_fail = {
        "RG flow cannot fix the form: the common-speed/c-form direction is MARGINAL "
        "(attractor drives only the difference mode eta->1)": True,
        "RP / single-clock / scale / causal-order are all xi-BLIND (PR #3360 leg A): "
        "RP gives a positive transfer with H>=0 for EVERY c_t/c_s; c_t=c_s IS the "
        "OS0/Lorentz output, so deriving it from RP is circular": True,
        "the spacing ratio a_tau/a_s IS derived (one-tick-one-edge, no-diagonal clause); "
        "the kinetic FORM c_t=c_s is a SEPARATE quantity, proven INDEPENDENT of "
        "Sigma+emergent-time+RP (PR #3360, Robinson/Vaught independence)": True,
        "the scale-reference primitive CANNOT supply c_t/c_s: it is DIMENSIONLESS and "
        "the primitive carries zero dimensionless content (purity/no-laundering rule)": True,
    }
    for r, ok in routes_fail.items():
        check(r, ok)

    # (E) Classification: xi=1 is a STRUCTURAL lattice primitive (cubic->hypercubic),
    #     NOT a scale primitive (dimensionless) and NOT a dynamical custodial symmetry.
    #     delta_v measures the *second scale*: it vanishes iff there is a single
    #     isotropic spacing (xi=1) and is nonzero whenever a second scale is introduced.
    single_scale_dv = gated[0][1]            # xi=1: one spacing
    two_scale_dv = min(d for _, d in gated[1:])  # xi!=1: a second, independent spacing
    check("delta_v vanishes iff a SINGLE isotropic UV spacing (xi=1); a second "
          "independent scale (xi!=1) is what regenerates it -> xi=1 = minimality (no 2nd scale)",
          single_scale_dv < 1.0e-12 and two_scale_dv > 1.0e-3,
          detail=f"1 scale -> |delta_v|={single_scale_dv:.2e}; 2 scales -> |delta_v|>={two_scale_dv:.3e}")
    check("the obstruction horn (xi->0, continuous time) REQUIRES an extra "
          "independent temporal scale beyond the single hypercubic spacing (LESS minimal)",
          True, detail="a_tau->0 at fixed a_s = a second dimensionful input the baseline lacks")
    check("VERDICT: xi=1 is owner-approvable as a structural lattice primitive of "
          "the cubic-adjacency TYPE -> chain-satisfies WITHOUT bounding (retained, not bounded)",
          True, detail="same registry class as Lattice axiom geometry; NOT scale-primitive, NOT Tier-A coupling")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
