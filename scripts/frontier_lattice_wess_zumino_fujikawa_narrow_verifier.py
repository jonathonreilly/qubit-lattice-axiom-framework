#!/usr/bin/env python3
"""
frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py
--------------------------------------------------------

Runner paired with
    AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md

Lane: dynamics-lane-native-axioms-only-20260526 (research lane).

This runner verifies the bounded finite-lattice trace claims of the
successor theorem note. Compared to the closed-PR-402 runner, this
runner has been scoped down so it checks finite matrix identities and
does not assert an ABJ import-retirement theorem:

  V1 [W1]:  log-Jacobian is R-linear in alpha on free and gauged
            Z^4 backgrounds.

  V2 [eps-D]: eps * D[U] * eps = -D[U] at machine precision on free
            and gauged Z^4 with random U(1) phases. This is the
            CPT_EXACT_NOTE Z^4 extension that powers W3.

  V3 [W3 t-indep]: Tr[eps exp(-t D†D)] is t-independent across
            t in {0.1, 0.5, 1.0, 2.0} on free Z^4 and on a
            non-trivial U(1) background.

  V4 [W3 integer-valued]: Tr[eps exp(-t D†D)] is integer-valued
            (modulo machine precision) at the chosen t values.

  V5 [W3 gauge-inv]: Under a U(1) gauge rotation
            U_mu(x) -> G(x)^* U_mu(x) G(x+mu^),
            Tr[eps exp(-t D†D[U])] is unchanged.

  V6 [non-trivial U]: Exhibit an explicit U(1) background whose
            principal-branch plaquette angles carry one flux quantum
            through each (x0, x1) plane, with periodic Polyakov-loop
            checks, and verify that the integer-index machinery runs on it.
            The observed
            staggered index on the tested small even boxes is zero;
            non-zero-index existence is not claimed.

  V7 [size-independence of structural facts]: Repeat V2-V5 on L=4
            AND L=6 to confirm the lattice algebra does not depend
            on the specific choice of even L.

The runner uses numpy + scipy. PASS/FAIL classified per-check; the
script exits 0 iff PASS_COUNT > 0 and FAIL_COUNT == 0.

No local-counterterm cohomology claim. No ABJ import retirement. No
audit-lane wiring. No retained-status claim. Source-only.
"""

from __future__ import annotations

import sys
from itertools import product

import numpy as np
from numpy.linalg import eigh, eigvalsh

# scipy is only used for an optional sanity cross-check (expm); the
# main path uses eigendecomposition of D^dag D (a Hermitian matrix),
# which is exact up to machine precision on small L.
try:
    from scipy.linalg import expm  # noqa: F401
    HAVE_SCIPY = True
except Exception:
    HAVE_SCIPY = False


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"[{status}] {name}"
    if detail:
        msg += f"  {detail}"
    print(msg)


# ---------------------------------------------------------------------------
# Lattice and operator construction
# ---------------------------------------------------------------------------

def site_index(x, L):
    """Linear index of site x = (x0, x1, x2, x3) in (Z/L)^4."""
    return (
        (x[0] % L) * (L * L * L)
        + (x[1] % L) * (L * L)
        + (x[2] % L) * L
        + (x[3] % L)
    )


def epsilon_diagonal(L):
    """Sublattice parity epsilon(x) = (-1)^(x_0+x_1+x_2+x_3), shape (L^4,)."""
    eps = np.zeros(L ** 4, dtype=np.float64)
    for x in product(range(L), repeat=4):
        eps[site_index(x, L)] = (-1.0) ** (sum(x))
    return eps


def staggered_phase(mu, x):
    """Kogut-Susskind staggered phase eta_mu(x) for mu in {0, 1, 2, 3}."""
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** (x[0])
    if mu == 2:
        return (-1.0) ** (x[0] + x[1])
    if mu == 3:
        return (-1.0) ** (x[0] + x[1] + x[2])
    raise ValueError(f"mu must be in {{0,1,2,3}}: got {mu}")


def free_staggered_dirac_matrix(L):
    """Free (U = I) staggered Dirac matrix on Z^4, periodic.

    D = (1/2) sum_mu eta_mu(x) [delta_{x+mu, y} - delta_{x-mu, y}]
    massless, no Wilson term. Real antisymmetric -> antihermitian.
    """
    N = L ** 4
    D = np.zeros((N, N), dtype=np.float64)
    for x in product(range(L), repeat=4):
        ix = site_index(x, L)
        for mu in range(4):
            eta = staggered_phase(mu, x)
            xp = list(x); xp[mu] = (xp[mu] + 1) % L
            xm = list(x); xm[mu] = (xm[mu] - 1) % L
            D[ix, site_index(xp, L)] += 0.5 * eta
            D[ix, site_index(xm, L)] -= 0.5 * eta
    return D


def gauged_u1_staggered_dirac_matrix(L, link_phases):
    """Staggered Dirac coupled to U(1) link phases U_mu(x)."""
    N = L ** 4
    D = np.zeros((N, N), dtype=complex)
    for x in product(range(L), repeat=4):
        ix = site_index(x, L)
        for mu in range(4):
            eta = staggered_phase(mu, x)
            xp = list(x); xp[mu] = (xp[mu] + 1) % L
            xm = list(x); xm[mu] = (xm[mu] - 1) % L
            iy_p = site_index(xp, L)
            iy_m = site_index(xm, L)
            U_pos = link_phases[mu, ix]
            U_neg_atxm = link_phases[mu, iy_m]
            D[ix, iy_p] += 0.5 * eta * U_pos
            D[ix, iy_m] -= 0.5 * eta * U_neg_atxm.conj()
    return D


def random_u1_link_phases(L, rng):
    N = L ** 4
    phases = np.zeros((4, N), dtype=complex)
    for mu in range(4):
        thetas = rng.uniform(-np.pi, np.pi, size=N)
        phases[mu] = np.exp(1j * thetas)
    return phases


def apply_u1_gauge_rotation(link_phases, gauge_phases, L):
    """U_mu(x) -> G(x)^* U_mu(x) G(x+mu^)."""
    N = L ** 4
    out = np.zeros_like(link_phases)
    for x in product(range(L), repeat=4):
        ix = site_index(x, L)
        for mu in range(4):
            xp = list(x); xp[mu] = (xp[mu] + 1) % L
            iy_p = site_index(xp, L)
            out[mu, ix] = gauge_phases[ix].conj() * link_phases[mu, ix] * gauge_phases[iy_p]
    return out


def winding_u1_background(L):
    """Explicit U(1) link background with one principal-branch flux quantum.

    The local plaquette phases are not constant because the boundary twist is
    carried on the mu=1 links. The gauge-invariant finite assertion used below
    is that the principal plaquette-angle sum through each fixed (x_2, x_3)
    plane is 2*pi, i.e. one flux quantum.
    """
    N = L ** 4
    phases = np.ones((4, N), dtype=complex)
    flux_quanta = 1
    # A_mu choice: A_1(x) = -(2 pi n / L^2) * x_0, A_0(x) = 0 except
    # on the boundary x_1 = L-1 -> 0 where we add a compensating
    # twist A_0(x) = (2 pi n / L) * x_1 to make the total holonomy
    # consistent with periodic boundaries (Landau-gauge-like).
    two_pi_n_over_L2 = 2.0 * np.pi * flux_quanta / (L * L)
    two_pi_n_over_L = 2.0 * np.pi * flux_quanta / L
    for x in product(range(L), repeat=4):
        ix = site_index(x, L)
        # U_1(x) = exp(i A_1(x)) = exp(-i (2pi n / L^2) x_0)
        phases[1, ix] = np.exp(-1j * two_pi_n_over_L2 * x[0])
        # Compensating twist on the x_1 = L-1 -> 0 link
        if x[1] == L - 1:
            phases[1, ix] *= np.exp(1j * two_pi_n_over_L * x[0])
        # mu = 0, 2, 3 stay at identity
    return phases


def plaquette(link_phases, L, mu, nu, x):
    """Oriented U(1) plaquette U_mu(x) U_nu(x+mu) U_mu(x+nu)^* U_nu(x)^*."""
    ix = site_index(x, L)
    x_mu = list(x); x_mu[mu] = (x_mu[mu] + 1) % L
    x_nu = list(x); x_nu[nu] = (x_nu[nu] + 1) % L
    ix_mu = site_index(x_mu, L)
    ix_nu = site_index(x_nu, L)
    return (
        link_phases[mu, ix]
        * link_phases[nu, ix_mu]
        * link_phases[mu, ix_nu].conj()
        * link_phases[nu, ix].conj()
    )


def principal_flux_quanta_01(link_phases, L):
    """Principal-branch flux quanta through each fixed (x_2, x_3) plane."""
    out = []
    for x2 in range(L):
        for x3 in range(L):
            angle_sum = 0.0
            for x0 in range(L):
                for x1 in range(L):
                    angle_sum += np.angle(plaquette(link_phases, L, 0, 1, (x0, x1, x2, x3)))
            out.append(angle_sum / (2.0 * np.pi))
    return np.array(out, dtype=float)


def max_non_01_plaquette_deviation(link_phases, L):
    """Maximum |P_munu - 1| over plaquettes other than the flux (0,1) plane."""
    max_dev = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            if (mu, nu) == (0, 1):
                continue
            for x in product(range(L), repeat=4):
                max_dev = max(max_dev, abs(plaquette(link_phases, L, mu, nu, x) - 1.0))
    return float(max_dev)


def polyakov_loop(link_phases, L, mu, base_x):
    """Product of U_mu links around the periodic mu-cycle through base_x."""
    prod_loop = 1.0 + 0.0j
    x = list(base_x)
    for _ in range(L):
        ix = site_index(tuple(x), L)
        prod_loop *= link_phases[mu, ix]
        x[mu] = (x[mu] + 1) % L
    return prod_loop


def max_polyakov_unit_deviation(link_phases, L):
    """Maximum |Polyakov_mu - 1| over all coordinate cycles."""
    max_dev = 0.0
    for mu in range(4):
        other_ranges = [range(L) if axis != mu else (0,) for axis in range(4)]
        for base_x in product(*other_ranges):
            max_dev = max(max_dev, abs(polyakov_loop(link_phases, L, mu, base_x) - 1.0))
    return float(max_dev)


# ---------------------------------------------------------------------------
# Heat-kernel diagonal via spectral decomposition of D^dag D
# ---------------------------------------------------------------------------

def heat_kernel_diag(D, t):
    """Return diag(exp(-t D^dag D)) as a real vector of length L^4."""
    DtD = D.conj().T @ D
    evals, evecs = eigh(DtD)
    # diag(U exp(-t Lambda) U^dag)
    # |U[x, n]|^2 weighted by exp(-t lambda_n)
    weights = np.exp(-t * evals)
    diag = np.real(np.einsum("xn,n,xn->x", evecs, weights, evecs.conj()))
    return diag


def chiral_anomaly_trace(D, eps, t):
    """A[1, U] = sum_x eps(x) <x|exp(-t D^dag D)|x>."""
    return float(np.sum(eps * heat_kernel_diag(D, t)))


def chiral_zero_mode_index(D, eps, zero_tol=1e-8):
    """n_+(D) - n_-(D) via direct zero-mode chirality count."""
    DtD = D.conj().T @ D
    evals, evecs = eigh(DtD)
    zero_modes = evals < zero_tol
    if not np.any(zero_modes):
        return 0.0
    # diag of eps in eigenbasis, restricted to kernel
    chirality_on_modes = np.real(
        np.einsum("xn,x,xn->n", evecs.conj(), eps, evecs)
    )
    return float(np.sum(chirality_on_modes[zero_modes]))


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_V1_W1_linearity(L, seed):
    print(f"\n=== V1 [W1, L={L}]: heat-kernel log-Jacobian is R-linear in alpha ===")
    rng = np.random.default_rng(seed)
    eps = epsilon_diagonal(L)
    D_free = free_staggered_dirac_matrix(L)
    D_gauged = gauged_u1_staggered_dirac_matrix(L, random_u1_link_phases(L, rng))

    for tag, D in [("free", D_free), ("U(1)-random", D_gauged)]:
        for t in (0.1, 0.5, 1.0):
            T_diag = heat_kernel_diag(D, t)
            alpha1 = rng.normal(size=eps.size)
            alpha2 = rng.normal(size=eps.size)
            A1 = float(np.sum(alpha1 * eps * T_diag))
            A2 = float(np.sum(alpha2 * eps * T_diag))
            A_sum = float(np.sum((alpha1 + alpha2) * eps * T_diag))
            residual = abs(A_sum - (A1 + A2))
            check(
                f"V1/L={L}/{tag}/t={t}: A[a1+a2] = A[a1] + A[a2]",
                residual < 1e-10,
                f"residual = {residual:.2e}",
            )


def check_V2_eps_anticomm_D(L, seed):
    print(f"\n=== V2 [eps-D anticommutation, L={L}]: eps D[U] eps = -D[U] ===")
    eps = epsilon_diagonal(L)

    D_free = free_staggered_dirac_matrix(L)
    res_free = float(np.max(np.abs(np.outer(eps, eps) * D_free + D_free)))
    check(
        f"V2/L={L}/free: ||eps D eps + D|| = 0",
        res_free < 1e-12,
        f"residual = {res_free:.2e}",
    )

    rng = np.random.default_rng(seed)
    link_phases = random_u1_link_phases(L, rng)
    D_g = gauged_u1_staggered_dirac_matrix(L, link_phases)
    res_g = float(np.max(np.abs(np.outer(eps, eps) * D_g + D_g)))
    check(
        f"V2/L={L}/U(1)-random: ||eps D[U] eps + D[U]|| = 0",
        res_g < 1e-10,
        f"residual = {res_g:.2e}",
    )

    link_phases_w = winding_u1_background(L)
    D_w = gauged_u1_staggered_dirac_matrix(L, link_phases_w)
    res_w = float(np.max(np.abs(np.outer(eps, eps) * D_w + D_w)))
    check(
        f"V2/L={L}/U(1)-winding: ||eps D[U_wind] eps + D[U_wind]|| = 0",
        res_w < 1e-10,
        f"residual = {res_w:.2e}",
    )


def check_V3_V4_t_independence_integer_valued(L, seed):
    print(
        f"\n=== V3/V4 [W3, L={L}]: Tr[eps exp(-t D^dag D)] is t-independent and integer-valued ==="
    )
    eps = epsilon_diagonal(L)
    rng = np.random.default_rng(seed)

    backgrounds = [
        ("free", free_staggered_dirac_matrix(L)),
        ("U(1)-random", gauged_u1_staggered_dirac_matrix(L, random_u1_link_phases(L, rng))),
        ("U(1)-winding", gauged_u1_staggered_dirac_matrix(L, winding_u1_background(L))),
    ]

    t_values = (0.1, 0.5, 1.0, 2.0)
    for tag, D in backgrounds:
        A_values = []
        for t in t_values:
            A = chiral_anomaly_trace(D, eps, t)
            A_values.append((t, A))
            print(f"  L={L}/{tag}/t={t}: A[1, U] = {A:.6e}")
        A_first = A_values[0][1]
        max_dev = max(abs(A - A_first) for _, A in A_values)
        check(
            f"V3/L={L}/{tag}: t-independent across t in {t_values}",
            max_dev < 1e-7,
            f"max deviation = {max_dev:.2e}",
        )
        # Cross-check with zero-mode count
        idx = chiral_zero_mode_index(D, eps)
        check(
            f"V3-cross/L={L}/{tag}: A[1,U] = zero-mode chirality count",
            abs(A_first - idx) < 1e-7,
            f"|A_heat_kernel - idx_spectral| = {abs(A_first - idx):.2e}",
        )
        check(
            f"V4/L={L}/{tag}: A[1, U] is integer-valued",
            abs(A_first - round(A_first)) < 1e-7,
            f"A = {A_first:.6e}, nearest int = {int(round(A_first))}",
        )


def check_V5_gauge_invariance(L, seed):
    print(f"\n=== V5 [W3 gauge-inv, L={L}]: chiral trace and spectrum are gauge-invariant ===")
    rng = np.random.default_rng(seed)
    eps = epsilon_diagonal(L)
    link_phases = random_u1_link_phases(L, rng)
    gauge_phases = np.exp(1j * rng.uniform(-np.pi, np.pi, size=L ** 4))

    D_pre = gauged_u1_staggered_dirac_matrix(L, link_phases)
    D_post = gauged_u1_staggered_dirac_matrix(
        L, apply_u1_gauge_rotation(link_phases, gauge_phases, L)
    )

    # Spectrum is gauge-invariant
    evals_pre = np.sort(eigvalsh(D_pre.conj().T @ D_pre))
    evals_post = np.sort(eigvalsh(D_post.conj().T @ D_post))
    spec_diff = float(np.max(np.abs(evals_pre - evals_post)))
    check(
        f"V5/L={L}: sigma(D^dag D[U]) = sigma(D^dag D[G^* U G])",
        spec_diff < 1e-8,
        f"spectrum max diff = {spec_diff:.2e}",
    )

    for t in (0.1, 0.5, 1.0):
        A_pre = chiral_anomaly_trace(D_pre, eps, t)
        A_post = chiral_anomaly_trace(D_post, eps, t)
        diff = abs(A_pre - A_post)
        check(
            f"V5/L={L}/t={t}: chiral trace gauge-invariant",
            diff < 1e-7,
            f"|A_pre - A_post| = {diff:.2e}",
        )


def check_V6_winding_background(L):
    """Exhibit a U(1) background with one flux quantum and report the
    integer index the staggered-Dirac machinery observes on it.

    Honest scope: this check is about the *machinery* (integer-
    valuedness, reproducibility, gauge-invariance, spectral
    consistency) running correctly on a non-trivial U. It now also checks
    the finite plaquette/Polyakov invariants of the displayed background.
    On these
    small even tori with quantized U(1) flux, staggered Dirac is
    known in the literature (Adams 2002) to typically produce
    paired chiralities so n_+ - n_- = 0; getting robust non-zero
    indices on small lattices generally requires the overlap-Dirac
    construction. The successor note explicitly flags
    non-zero-index *existence* as bounded scope and NOT load-bearing.
    """
    print(f"\n=== V6 [non-trivial U: machinery + observed index, L={L}] ===")
    eps = epsilon_diagonal(L)
    link_phases_w = winding_u1_background(L)
    D_free = free_staggered_dirac_matrix(L)
    D_wind = gauged_u1_staggered_dirac_matrix(L, link_phases_w)

    t = 0.5
    A_free = chiral_anomaly_trace(D_free, eps, t)
    A_wind = chiral_anomaly_trace(D_wind, eps, t)
    flux_quanta = principal_flux_quanta_01(link_phases_w, L)
    max_flux_dev = float(np.max(np.abs(flux_quanta - 1.0)))
    max_non01_dev = max_non_01_plaquette_deviation(link_phases_w, L)
    max_poly_dev = max_polyakov_unit_deviation(link_phases_w, L)
    nonidentity_link_count = int(np.count_nonzero(np.abs(link_phases_w - 1.0) > 1e-12))
    print(
        f"  L={L}: principal (0,1)-plaquette flux quanta per (x2,x3) plane: "
        f"min={float(np.min(flux_quanta)):.6f}, max={float(np.max(flux_quanta)):.6f}"
    )
    print(f"  L={L}: non-(0,1) plaquette max |P-1| = {max_non01_dev:.2e}")
    print(f"  L={L}: Polyakov-loop max |P_mu-1| = {max_poly_dev:.2e}")
    print(f"  L={L}: A[1, U=I]    = {A_free:.6e}  (observed integer: {int(round(A_free))})")
    print(f"  L={L}: A[1, U_wind] = {A_wind:.6e}  (observed integer: {int(round(A_wind))})")
    print(
        f"  L={L}: one-quantum flux background DOES exist and the machinery DOES run; "
        f"observed staggered index on this small lattice is "
        f"{int(round(A_wind))} (zero on these small L — "
        "expected from Adams 2002; non-zero existence is bounded-scope per the note)."
    )

    check(
        f"V6a/L={L}: U_wind has non-identity U(1) links",
        nonidentity_link_count > 0 and np.allclose(np.abs(link_phases_w), 1.0, atol=1e-12),
        f"nonidentity links = {nonidentity_link_count}",
    )
    check(
        f"V6b/L={L}: principal (0,1)-plaquette flux is one quantum",
        max_flux_dev < 1e-12,
        f"max |flux_quanta - 1| = {max_flux_dev:.2e}",
    )
    check(
        f"V6c/L={L}: all non-(0,1) plaquettes are flat",
        max_non01_dev < 1e-12,
        f"max non-(0,1) |P-1| = {max_non01_dev:.2e}",
    )
    check(
        f"V6d/L={L}: Polyakov loops close periodically",
        max_poly_dev < 1e-12,
        f"max |Polyakov-1| = {max_poly_dev:.2e}",
    )
    # Both heat-kernel traces must be integer.
    check(
        f"V6e/L={L}: A[1, U_wind] integer-valued",
        abs(A_wind - round(A_wind)) < 1e-7,
        f"A_wind = {A_wind:.6e}, nearest int = {int(round(A_wind))}",
    )
    # The machinery must be reproducible: independent recomputation gives
    # the same integer. This is the bare existence check that the
    # integer-index mechanism *runs* on a non-trivial U; existence of a
    # non-zero-index background is bounded-scope and not load-bearing
    # for this note.
    A_wind_2 = chiral_anomaly_trace(D_wind, eps, 1.0)
    check(
        f"V6f/L={L}: A[1, U_wind] reproducible across t",
        abs(A_wind - A_wind_2) < 1e-7,
        f"|A(t=0.5) - A(t=1.0)| = {abs(A_wind - A_wind_2):.2e}",
    )
    # Cross-check via direct zero-mode count
    idx_wind = chiral_zero_mode_index(D_wind, eps)
    check(
        f"V6g/L={L}: A[1, U_wind] matches zero-mode spectral count",
        abs(A_wind - idx_wind) < 1e-7,
        f"|A - idx_spectral| = {abs(A_wind - idx_wind):.2e}",
    )


def check_V7_size_independence(seed):
    print("\n=== V7 [size-independence of structural facts] ===")
    # All of V2-V5 already loop over L; this check is the marker
    # that we ran them at L=4 and L=6 and they all passed.
    # The actual passing is recorded by check() in V2-V5; here we
    # just note that running at both sizes is part of the protocol.
    print("  V2-V5 are exercised at L=4 and L=6 in main().")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Finite Z4 Staggered-Grading Trace Verifier")
    print("===========================================")
    print(
        "Theorem note: "
        "docs/AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md"
    )
    print("Status: bounded source theorem. No audit-lane wiring.")
    print()

    seed = 20260526

    for L in (4, 6):
        check_V1_W1_linearity(L=L, seed=seed)
        check_V2_eps_anticomm_D(L=L, seed=seed)
        check_V3_V4_t_independence_integer_valued(L=L, seed=seed)
        check_V5_gauge_invariance(L=L, seed=seed)
        check_V6_winding_background(L=L)
    check_V7_size_independence(seed=seed)

    print()
    print(f"Summary: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT > 0:
        sys.exit(1)
    if PASS_COUNT == 0:
        sys.exit(2)
    print("All narrow-claim checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
