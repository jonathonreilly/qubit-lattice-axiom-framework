"""S3-time theta-to-slice rho_E dependency firewall.

This runner is a direct-consumer packet for the Route-2 endpoint ambiguity.
It does not try to derive rho_E = 21/4. Instead it proves exactly where the
unresolved E-channel readout entry propagates in the existing conditional
theta-to-slice family

    Xi_P(t ; c) = (P_R c) tensor exp(-t Lambda_R) u_*.

With the granted T-side entries, the reduced readout family is

    P(rho_E) = [[1, 0, rho_E, 0],
                [0,-2, 0,     2]].

Result: rho_E affects only the E-center carrier column, and it does so by the
single scalar factor 1 + rho_E/6. E-shell, T-shell, and T-center couplings are
rho-independent for every time t; the rho-dependence is a rank-one source
factor tensor the same exact slice seed V_R(t).
"""
from __future__ import annotations

from fractions import Fraction as F

import numpy as np
from scipy.linalg import expm

from frontier_quark_route2_exact_readout_map import EXACT_TOL
from frontier_quark_route2_exact_time_coupling import (
    route2_slice_backbone,
    v_r,
)

PASS = 0
FAIL = 0
TIMES = [0.0, 0.5, 1.0, 2.0]


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    return ok


E_SHELL = (F(1), F(0), F(0), F(0))
E_CENTER = (F(1), F(0), F(1, 6), F(0))
T_SHELL = (F(0), F(1), F(0), F(0))
T_CENTER = (F(0), F(1), F(0), F(1, 6))
COLUMNS = {
    "E-shell": E_SHELL,
    "E-center": E_CENTER,
    "T-shell": T_SHELL,
    "T-center": T_CENTER,
}


def readout_vector(rho_e: F, carrier: tuple[F, F, F, F]) -> tuple[F, F]:
    u_e, u_t, delta_u_e, delta_u_t = carrier
    gamma_e = u_e + rho_e * delta_u_e
    gamma_t = -2 * u_t + 2 * delta_u_t
    return gamma_e, gamma_t


def xi_from_source(source: tuple[F, F], time_seed: np.ndarray) -> np.ndarray:
    return np.outer(np.array([float(source[0]), float(source[1])]), time_seed)


def source_delta(rho_a: F, rho_b: F, carrier: tuple[F, F, F, F]) -> tuple[F, F]:
    a = readout_vector(rho_a, carrier)
    b = readout_vector(rho_b, carrier)
    return b[0] - a[0], b[1] - a[1]


def n5_execution_certificate(backbone) -> None:
    """Print-only record of what this runner resolves at each granularity.

    Adds no check and touches no counter.  Every floating figure below is
    interpolated from this run's own backbone at print time.
    """
    n_trace = int(backbone.lambda_sym.shape[0])
    print("\n" + "=" * 88)
    print("N5 execution certificate (print-only; adds no check and no counter)")
    print("=" * 88)
    print(
        "per_element: resolved in two layers -- on the source side the arithmetic is exact "
        "Fraction, only the row-0 column-2 entry of P(rho_E) is permitted to move, and differencing "
        "the four carrier columns between rho_E = 0 and rho_E = 21/4 returns (0, 0) on three of them "
        "and exactly (7/8, 0) on E-center. On the transported side the comparison stays entrywise: "
        f"the residual max over every component of the 2 x {n_trace} tensor is taken against the "
        f"shared EXACT_TOL = {EXACT_TOL:.0e}, not against an aggregate norm."
    )
    print(
        "per_site: exercised only as a uniform all-sites tolerance test, and reported as exactly "
        f"that -- the transported tensors carry one component per boundary-trace site, all {n_trace} "
        "of them, and each comparison is a maximum taken across every one, so agreement is certified "
        "site by site. Yet no site is ever distinguished: the slice seed u_* is the uniform unit "
        "vector over the whole trace set, and every scalar this runner reports is a max or a norm "
        "across it, so no individual site amplitude is resolved and none is claimed."
    )
    print(
        "per_mode: resolved as a two-channel source split -- gamma_E = u_E + rho_E * delta_u_E and "
        "gamma_T = -2 u_T + 2 delta_u_T are formed separately, and the T channel is certified "
        "rho-independent by exact rational equality at its granted values (0, -2) on T-shell and "
        "(0, -5/3) on T-center. The E channel alone carries the endpoint freedom, through "
        "q_E = 1 + rho_E/6, which is exactly 1 at rho_E = 0 and exactly 15/8 at rho_E = 21/4."
    )
    print(
        "per_block: resolved as one sensitive column against three blind ones -- of the four carrier "
        "columns only E-center responds to rho_E while E-shell, T-shell and T-center are exactly "
        "invariant, and that same partition is re-verified at the non-load-bearing comparison point "
        "rho_E = 526/100, where q_E becomes 563/300 and the blind block still differences to zero. "
        "The surviving rho-dependence is rank one: a single source factor times the same slice seed."
    )
    print(
        "lattice_wide: resolved as a finite-N statement on one fixed grid -- Lambda_R is the "
        "symmetrized Schur complement of the 15-cubed discrete Laplacian onto its boundary trace at "
        f"cutoff radius 4.0, a genuinely whole-grid operator of dimension {n_trace}, and it is "
        f"certified as a whole here: symmetry residual {backbone.sym_err:.3e} against EXACT_TOL, "
        f"smallest eigenvalue {backbone.min_eig:.6e} strictly positive, and the one-step transfer "
        f"exp(-Lambda_R) contractive with largest eigenvalue {backbone.transfer_max_eig:.6e} below "
        "one. Grid size 15 and cutoff 4.0 are the only ones executed; no thermodynamic limit is "
        "taken and nothing here is asserted about growing the box."
    )
    print(
        "Determinism: this runner uses no RNG, optimizer, root-finding or Monte Carlo. The only "
        f"sweep is the fixed time list {TIMES}, with the semigroup step t -> t+0.5 taken wherever "
        f"both endpoints lie in that list; tolerances are EXACT_TOL = {EXACT_TOL:.0e}, 5e-14 for the "
        "semigroup residual and 1e-12 for the norm ratio. The eigenvalue and symmetry figures above "
        "are interpolated from this run's own backbone rather than quoted from a past run, since "
        "LAPACK and expm residuals move between environments while the verdicts do not."
    )


def main() -> int:
    print("S3-time theta-to-slice rho_E dependency firewall")
    print("=" * 88)

    rho0 = F(0)
    rho_target = F(21, 4)
    rho_live_round = F(526, 100)  # non-load-bearing comparison point near live rho_E

    expected_sources = {
        "E-shell": (F(1), F(0)),
        "E-center@rho": None,
        "T-shell": (F(0), F(-2)),
        "T-center": (F(0), F(-5, 3)),
    }

    check(
        "reduced family P(rho_E) gives fixed E-shell, T-shell, and T-center source factors",
        readout_vector(rho0, E_SHELL) == expected_sources["E-shell"]
        and readout_vector(rho_target, E_SHELL) == expected_sources["E-shell"]
        and readout_vector(rho0, T_SHELL) == expected_sources["T-shell"]
        and readout_vector(rho_target, T_SHELL) == expected_sources["T-shell"]
        and readout_vector(rho0, T_CENTER) == expected_sources["T-center"]
        and readout_vector(rho_target, T_CENTER) == expected_sources["T-center"],
        (
            f"E-shell={readout_vector(rho_target, E_SHELL)}, "
            f"T-shell={readout_vector(rho_target, T_SHELL)}, "
            f"T-center={readout_vector(rho_target, T_CENTER)}"
        ),
    )

    q_e_target = readout_vector(rho_target, E_CENTER)[0]
    check(
        "E-center source factor is exactly q_E(rho_E)=1+rho_E/6; target rho_E=21/4 gives q_E=15/8",
        readout_vector(rho0, E_CENTER) == (F(1), F(0))
        and q_e_target == F(15, 8),
        f"q_E(0)={readout_vector(rho0, E_CENTER)[0]}, q_E(21/4)={q_e_target}",
    )

    symbolic_deltas = {name: source_delta(rho0, rho_target, col) for name, col in COLUMNS.items()}
    check(
        "rho_E variation is zero on E-shell/T-shell/T-center and equals (rho/6,0) on E-center",
        symbolic_deltas == {
            "E-shell": (F(0), F(0)),
            "E-center": (F(7, 8), F(0)),
            "T-shell": (F(0), F(0)),
            "T-center": (F(0), F(0)),
        },
        f"deltas={symbolic_deltas}",
    )

    q_e_live_round = readout_vector(rho_live_round, E_CENTER)[0]
    check(
        "near-live rho_E comparison changes only the same E-center scalar, not the dependency support",
        q_e_live_round == F(563, 300)
        and all(source_delta(rho0, rho_live_round, col) == (F(0), F(0)) for name, col in COLUMNS.items() if name != "E-center"),
        f"q_E(526/100)={q_e_live_round}",
    )

    backbone = route2_slice_backbone()
    lambda_sym = backbone.lambda_sym
    transfer = backbone.transfer
    check(
        "slice backbone is independent of rho_E: Lambda_R SPD and T_R contractive",
        np.max(np.abs(lambda_sym - lambda_sym.T)) < EXACT_TOL
        and float(np.min(np.linalg.eigvalsh(lambda_sym))) > 0.0
        and float(np.max(np.linalg.eigvalsh(transfer))) < 1.0,
        (
            f"min eig Lambda={float(np.min(np.linalg.eigvalsh(lambda_sym))):.6e}, "
            f"max eig T={float(np.max(np.linalg.eigvalsh(transfer))):.6e}"
        ),
    )

    all_shell_t_independent = True
    all_center_affine = True
    all_norm_ratios = True
    all_semigroup = True
    for t in TIMES:
        seed_t = v_r(backbone, t)
        seed_norm = float(np.linalg.norm(seed_t))
        for name in ("E-shell", "T-shell", "T-center"):
            xi0 = xi_from_source(readout_vector(rho0, COLUMNS[name]), seed_t)
            xit = xi_from_source(readout_vector(rho_target, COLUMNS[name]), seed_t)
            all_shell_t_independent = all_shell_t_independent and np.max(np.abs(xi0 - xit)) < EXACT_TOL

        center0 = xi_from_source(readout_vector(rho0, E_CENTER), seed_t)
        center_target = xi_from_source(readout_vector(rho_target, E_CENTER), seed_t)
        expected_delta = np.outer(np.array([float(F(7, 8)), 0.0]), seed_t)
        all_center_affine = all_center_affine and np.max(np.abs((center_target - center0) - expected_delta)) < EXACT_TOL
        all_norm_ratios = all_norm_ratios and abs(float(np.linalg.norm(center_target - center0)) / seed_norm - 0.875) < 1e-12

        if t + 0.5 in TIMES:
            lhs = center_target @ expm(-0.5 * lambda_sym).T
            rhs = xi_from_source(readout_vector(rho_target, E_CENTER), v_r(backbone, t + 0.5))
            all_semigroup = all_semigroup and np.max(np.abs(lhs - rhs)) < 5e-14

    check(
        "for all checked times, E-shell/T-shell/T-center Xi_P are rho_E-independent",
        all_shell_t_independent,
        f"times={TIMES}",
    )
    check(
        "for all checked times, E-center Xi_P is affine with delta=(rho_E/6) e_E tensor V_R(t)",
        all_center_affine,
        f"target delta factor={(rho_target / 6)}",
    )
    check(
        "target-vs-zero E-center tensor separation has norm (7/8)*||V_R(t)|| at every checked time",
        all_norm_ratios,
        "ratio=7/8 for rho_E=21/4 versus rho_E=0",
    )
    check(
        "rho_E-dependent E-center tensor evolves by the same exact slice semigroup",
        all_semigroup,
        "checked t -> t+0.5 where both times are in the sample set",
    )

    shell = readout_vector(rho_target, E_SHELL)
    center = readout_vector(rho_target, E_CENTER)
    q_ratio = center[0] / shell[0]
    check(
        "the target endpoint factor q_E=15/8 is exactly the E-center/E-shell source ratio",
        q_ratio == F(15, 8),
        f"center/shell={q_ratio}",
    )

    n5_execution_certificate(backbone)

    print("\n" + "=" * 88)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: exact-support firewall for the theta-to-slice consumer. The unresolved\n"
        "rho_E entry propagates only through the E-center source factor q_E=1+rho_E/6.\n"
        "Shell couplings and T-channel couplings are rho-independent for every checked\n"
        "time, and the rho-dependent E-center tensor is just a rank-one source factor\n"
        "times the same exact slice seed V_R(t). This narrows the consumer ambiguity but\n"
        "does not derive rho_E=21/4."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
