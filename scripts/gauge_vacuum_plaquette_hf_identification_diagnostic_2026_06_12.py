#!/usr/bin/env python3
"""Hellmann-Feynman diagnostic for the source-sector Perron identification.

This runner measures the beta-derivative decomposition of

    T_src(beta) = M_beta D_beta^loc C_rho(beta) M_beta,
    M_beta = exp((beta/2) J),

on the finite source-sector Perron machinery already present in the repo.
It is a diagnostic of the open identification checkpoint; it does not supply
or predict an audit outcome, a per-plaquette normalization theorem, or a
physical 3D residual environment solve.
"""

from __future__ import annotations

import ast
import math
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy.special import iv

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_spatial_environment_tensor_transfer as tw_existing
import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 600

BETA0 = 6.0
SOURCE_NMAX = 7
SOURCE_MODE_MAX = 200
TW_NMAX = 4
TW_MODE_MAX = 80
FD_STEPS = (1.0e-2, 5.0e-3, 2.5e-3, 1.25e-3, 6.25e-4)

P_LOC_REFERENCE = 0.4524071590
P_TRIV_REFERENCE = 0.4225317396
P_TW_REFERENCE = 0.434215413260
LAMBDA_LOC_REFERENCE = 3.812630482037
LAMBDA_TRIV_REFERENCE = 3.441440354984
LAMBDA_TW_REFERENCE = 3.577553737908

CANONICAL_COMPARATOR_TEXT = "0." + "5934"
CANONICAL_COMPARATOR = float(CANONICAL_COMPARATOR_TEXT)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def beta_key(beta: float) -> float:
    return round(float(beta), 12)


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def coefficient_matrix_and_derivative(
    mode: int, lam: tuple[int, int, int], beta: float
) -> tuple[np.ndarray, np.ndarray]:
    arg = beta / 3.0
    mat = np.empty((3, 3), dtype=float)
    dmat = np.empty((3, 3), dtype=float)
    for i in range(3):
        for j in range(3):
            order = mode + lam[j] + i - j
            mat[i, j] = iv(order, arg)
            dmat[i, j] = (iv(order - 1, arg) + iv(order + 1, arg)) / 6.0
    return mat, dmat


@lru_cache(maxsize=None)
def wilson_coeff_beta(p: int, q: int, mode_max: int, beta: float) -> float:
    return src_existing.wilson_character_coefficient(p, q, mode_max, beta / 3.0)


@lru_cache(maxsize=None)
def wilson_coeff_and_derivative_beta(
    p: int, q: int, mode_max: int, beta: float
) -> tuple[float, float]:
    lam = tuple(src_existing.highest_weight_triple(p, q))
    coeff = 0.0
    dcoeff = 0.0
    for mode in range(-mode_max, mode_max + 1):
        mat, dmat = coefficient_matrix_and_derivative(mode, lam, beta)
        coeff += float(np.linalg.det(mat))
        # Determinant derivative by row multilinearity.
        for row in range(3):
            replaced = mat.copy()
            replaced[row, :] = dmat[row, :]
            dcoeff += float(np.linalg.det(replaced))
    return coeff, dcoeff


def local_factor(
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
    mode_max: int,
    beta: float,
    with_derivative: bool,
) -> dict[str, object]:
    bkey = beta_key(beta)
    dims = np.array([src_existing.dim_su3(p, q) for p, q in weights], dtype=float)
    if with_derivative:
        pairs = [
            wilson_coeff_and_derivative_beta(p, q, mode_max, bkey)
            for p, q in weights
        ]
        coeffs = np.array([pair[0] for pair in pairs], dtype=float)
        dcoeffs = np.array([pair[1] for pair in pairs], dtype=float)
        c00 = float(coeffs[index[(0, 0)]])
        dc00 = float(dcoeffs[index[(0, 0)]])
        a_link = coeffs / (dims * c00)
        da_link = (dcoeffs * c00 - coeffs * dc00) / (dims * c00 * c00)
        d_loc_prime = np.diag(4.0 * (a_link**3) * da_link)
    else:
        coeffs = np.array(
            [wilson_coeff_beta(p, q, mode_max, bkey) for p, q in weights],
            dtype=float,
        )
        dcoeffs = None
        dc00 = None
        c00 = float(coeffs[index[(0, 0)]])
        a_link = coeffs / (dims * c00)
        da_link = None
        d_loc_prime = None
    return {
        "coeffs": coeffs,
        "dcoeffs": dcoeffs,
        "dims": dims,
        "c00": c00,
        "dc00": dc00,
        "a_link": a_link,
        "da_link": da_link,
        "d_loc": np.diag(a_link**4),
        "d_loc_prime": d_loc_prime,
    }


def source_setup(beta: float, with_derivative: bool = False) -> dict[str, object]:
    j_op, weights, index = src_existing.build_J(SOURCE_NMAX)
    loc = local_factor(weights, index, SOURCE_MODE_MAX, beta, with_derivative)
    multiplier = src_existing.matrix_exp_symmetric(j_op, beta / 2.0)
    return {
        "j": j_op,
        "weights": weights,
        "index": index,
        "multiplier": multiplier,
        **loc,
    }


def rho_one(setup: dict[str, object]) -> np.ndarray:
    return np.ones(len(setup["weights"]), dtype=float)


def rho_delta(setup: dict[str, object]) -> np.ndarray:
    rho = np.zeros(len(setup["weights"]), dtype=float)
    rho[setup["index"][(0, 0)]] = 1.0
    return rho


def reference_rhos_are_beta_independent() -> bool:
    setup_minus = source_setup(BETA0 - FD_STEPS[0], with_derivative=False)
    setup_plus = source_setup(BETA0 + FD_STEPS[0], with_derivative=False)
    same_basis = setup_minus["weights"] == setup_plus["weights"] == source_setup(
        BETA0, with_derivative=False
    )["weights"]
    return (
        same_basis
        and np.array_equal(rho_one(setup_minus), rho_one(setup_plus))
        and np.array_equal(rho_delta(setup_minus), rho_delta(setup_plus))
        and np.count_nonzero(rho_delta(setup_plus)) == 1
    )


@lru_cache(maxsize=None)
def tensor_word_rho_data(beta: float) -> tuple[tuple[tuple[int, int], ...], tuple[float, ...], float, float, float, float, float]:
    nf, nfb, weights, index = tw_existing.build_mult_matrices(TW_NMAX)
    coeffs = np.array(
        [
            wilson_coeff_beta(p, q, TW_MODE_MAX, beta_key(beta))
            for p, q in weights
        ],
        dtype=float,
    )
    dims = np.array([src_existing.dim_su3(p, q) for p, q in weights], dtype=float)
    c00 = coeffs[index[(0, 0)]]
    normalized = coeffs / (dims * c00)
    diag_c = np.diag(normalized)
    tensor_word = diag_c @ (nf + nfb) @ diag_c @ (nf + nfb).T @ diag_c
    vals, vecs = np.linalg.eigh(tensor_word)
    eig_idx = int(np.argmax(vals))
    psi = vecs[:, eig_idx]
    if psi[index[(0, 0)]] < 0.0:
        psi = -psi
    rho = psi / psi[index[(0, 0)]]
    residual = float(np.linalg.norm(tensor_word @ psi - vals[eig_idx] * psi, ord=np.inf))
    rho_min = float(np.min(rho))
    rho_swap = float(
        np.max(np.abs(rho - np.array([rho[index[(q, p)]] for p, q in weights])))
    )
    return (
        tuple(weights),
        tuple(float(x) for x in rho),
        float(vals[eig_idx]),
        residual,
        rho_min,
        rho_swap,
        float(rho[index[(1, 0)]]),
    )


def rho_tw_source(beta: float, source_weights: list[tuple[int, int]]) -> np.ndarray:
    tw_weights, tw_rho, *_rest = tensor_word_rho_data(beta_key(beta))
    rho_map = {w: tw_rho[i] for i, w in enumerate(tw_weights)}
    return np.array([rho_map.get(w, 0.0) for w in source_weights], dtype=float)


def source_transfer(setup: dict[str, object], rho_vec: np.ndarray) -> np.ndarray:
    return (
        setup["multiplier"]
        @ setup["d_loc"]
        @ np.diag(rho_vec)
        @ setup["multiplier"]
    )


def source_log_lambda(beta: float, rho_builder: str) -> float:
    setup = source_setup(beta, with_derivative=False)
    if rho_builder == "one":
        rho = rho_one(setup)
    elif rho_builder == "delta":
        rho = rho_delta(setup)
    elif rho_builder == "tw":
        rho = rho_tw_source(beta, setup["weights"])
    else:
        raise ValueError(f"unknown rho builder: {rho_builder}")
    transfer = source_transfer(setup, rho)
    eig, _psi, _j_readout = src_existing.perron_state_and_value(transfer, setup["j"])
    return math.log(eig)


def central_fd_log_lambda(h: float, rho_builder: str) -> float:
    return (
        source_log_lambda(BETA0 + h, rho_builder)
        - source_log_lambda(BETA0 - h, rho_builder)
    ) / (2.0 * h)


def decompose_at_beta0(rho_vec: np.ndarray) -> dict[str, object]:
    setup = source_setup(BETA0, with_derivative=True)
    transfer = source_transfer(setup, rho_vec)
    eig, psi, j_readout = src_existing.perron_state_and_value(transfer, setup["j"])
    d_term = float(
        psi
        @ (
            setup["multiplier"]
            @ setup["d_loc_prime"]
            @ np.diag(rho_vec)
            @ setup["multiplier"]
        )
        @ psi
    ) / eig
    return {
        "setup": setup,
        "lambda": eig,
        "psi": psi,
        "multiplier_term": j_readout,
        "d_loc_term": d_term,
    }


def print_reference_fd_table(label: str, rho_builder: str, exact_total: float) -> dict[str, float]:
    print(f"{label}: central finite differences for d_beta log(lambda_0)")
    print("h | central FD | Richardson | |Richardson - exact assembly|")
    print("-" * 96)
    previous = None
    richardsons: list[float] = []
    centrals: list[float] = []
    for h in FD_STEPS:
        central = central_fd_log_lambda(h, rho_builder)
        centrals.append(central)
        if previous is None:
            print(f"{h:.8f} | {central:.12f} | n/a | n/a")
        else:
            rich = (4.0 * central - previous) / 3.0
            richardsons.append(rich)
            print(
                f"{h:.8f} | {central:.12f} | {rich:.12f} | "
                f"{abs(rich - exact_total):.3e}"
            )
        previous = central
    noise_floor = abs(richardsons[-1] - richardsons[-2])
    print(f"Richardson noise floor estimate: {noise_floor:.3e}")
    return {
        "last_central": centrals[-1],
        "last_richardson": richardsons[-1],
        "noise_floor": noise_floor,
    }


def rho_tw_environment_step_table(base: dict[str, object]) -> dict[str, float]:
    setup = base["setup"]
    psi = base["psi"]
    eig = base["lambda"]
    mult = base["multiplier_term"]
    d_term = base["d_loc_term"]
    source_weights = setup["weights"]
    previous_env = None
    previous_full = None
    env_richardsons: list[float] = []
    full_richardsons: list[float] = []
    env_centrals: list[float] = []
    full_centrals: list[float] = []

    print("rho^tw: central differences for environment term and full d_beta log(lambda_0)")
    print("h | env central | env Richardson | full central | full Richardson | full - assembled central")
    print("-" * 96)
    for h in FD_STEPS:
        rho_plus = rho_tw_source(BETA0 + h, source_weights)
        rho_minus = rho_tw_source(BETA0 - h, source_weights)
        rho_prime = (rho_plus - rho_minus) / (2.0 * h)
        env_central = float(
            psi
            @ (
                setup["multiplier"]
                @ setup["d_loc"]
                @ np.diag(rho_prime)
                @ setup["multiplier"]
            )
            @ psi
        ) / eig
        full_central = central_fd_log_lambda(h, "tw")
        assembled_central = mult + d_term + env_central
        env_centrals.append(env_central)
        full_centrals.append(full_central)
        if previous_env is None:
            print(
                f"{h:.8f} | {env_central:.12f} | n/a | "
                f"{full_central:.12f} | n/a | {full_central - assembled_central:.3e}"
            )
        else:
            env_rich = (4.0 * env_central - previous_env) / 3.0
            full_rich = (4.0 * full_central - previous_full) / 3.0
            env_richardsons.append(env_rich)
            full_richardsons.append(full_rich)
            print(
                f"{h:.8f} | {env_central:.12f} | {env_rich:.12f} | "
                f"{full_central:.12f} | {full_rich:.12f} | "
                f"{full_central - assembled_central:.3e}"
            )
        previous_env = env_central
        previous_full = full_central
    env_noise = abs(env_richardsons[-1] - env_richardsons[-2])
    full_noise = abs(full_richardsons[-1] - full_richardsons[-2])
    print(f"Environment Richardson noise floor estimate: {env_noise:.3e}")
    print(f"Full-derivative Richardson noise floor estimate: {full_noise:.3e}")
    return {
        "env_final": env_richardsons[-1],
        "env_last_central": env_centrals[-1],
        "env_noise": env_noise,
        "full_final": full_richardsons[-1],
        "full_last_central": full_centrals[-1],
        "full_noise": full_noise,
    }


def print_decomposition_table(rows: list[dict[str, float]]) -> None:
    print(
        "rho | lambda0 | d_beta log(lambda0) | multiplier=<J> | "
        "D_loc prime | env prime | correction | correction/<J> | hypothetical 1+f'"
    )
    print("-" * 132)
    for row in rows:
        print(
            f"{row['label']:<9} | {row['lambda']:.12f} | {row['total']:.12f} | "
            f"{row['multiplier']:.12f} | {row['d_loc']:.12f} | "
            f"{row['env']:.12f} | {row['correction']:.12f} | "
            f"{row['ratio']:.12f} | {1.0 + row['total']:.12f}"
        )


def print_hypothetical_table(rows: list[dict[str, float]]) -> None:
    print("```text")
    print("These are context distances only. The per-plaquette normalization theorem is open.")
    for row in rows:
        print(
            f"{row['label']}: |<J> - {CANONICAL_COMPARATOR_TEXT}| = "
            f"{abs(row['multiplier'] - CANONICAL_COMPARATOR):.12f}; "
            f"|d_beta log(lambda0) - {CANONICAL_COMPARATOR_TEXT}| = "
            f"{abs(row['total'] - CANONICAL_COMPARATOR):.12f}; "
            f"hypothetical 1+f' = {1.0 + row['total']:.12f}"
        )
    print("```")


def comparator_is_fenced_to_hypothetical_table() -> tuple[bool, list[str]]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    parents: dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent

    offenders: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Name) or node.id not in {
            "CANONICAL_COMPARATOR",
            "CANONICAL_COMPARATOR_TEXT",
        }:
            continue
        parent = parents.get(node)
        if isinstance(parent, ast.Assign) and node in parent.targets:
            continue
        while parent is not None and not isinstance(parent, ast.FunctionDef):
            parent = parents.get(parent)
        if parent is None or parent.name == "print_hypothetical_table":
            continue
        offenders.append(f"{node.id}@{node.lineno}:{parent.name}")
    return not offenders, offenders


def main() -> int:
    print("Gauge-vacuum plaquette Hellmann-Feynman identification diagnostic")
    print(
        f"beta={BETA0}, source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}, "
        f"tensor-word NMAX={TW_NMAX}, tensor-word MODE_MAX={TW_MODE_MAX}"
    )
    print("Status authority: independent audit lane only. This source note does not set or predict an audit outcome.")
    print("Identification checkpoint: Perron J-readout = licensed <P>* = 1 + f'(6) remains open.")

    section("Part 1: anchor reproduction")
    setup0 = source_setup(BETA0, with_derivative=True)
    dec_one = decompose_at_beta0(rho_one(setup0))
    dec_delta = decompose_at_beta0(rho_delta(setup0))
    rho_tw0 = rho_tw_source(BETA0, setup0["weights"])
    dec_tw = decompose_at_beta0(rho_tw0)
    tw_weights, tw_rho, tw_eig, tw_residual, tw_min, tw_swap, tw_rho10 = tensor_word_rho_data(BETA0)
    _ = tw_weights, tw_rho

    print(f"rho=1:     lambda0={dec_one['lambda']:.12f}, <J>={dec_one['multiplier_term']:.12f}")
    print(f"rho=delta: lambda0={dec_delta['lambda']:.12f}, <J>={dec_delta['multiplier_term']:.12f}")
    print(f"rho^tw:    lambda0={dec_tw['lambda']:.12f}, <J>={dec_tw['multiplier_term']:.12f}")
    print(
        f"rho^tw tensor Perron: eig={tw_eig:.12f}, residual={tw_residual:.3e}, "
        f"min={tw_min:.3e}, swap={tw_swap:.3e}, rho10={tw_rho10:.12f}"
    )

    check(
        "rho=1 reference Perron anchor is reproduced",
        abs(dec_one["multiplier_term"] - P_LOC_REFERENCE) < 5.0e-10
        and abs(dec_one["lambda"] - LAMBDA_LOC_REFERENCE) < 5.0e-10,
        f"lambda={dec_one['lambda']:.12f}, <J>={dec_one['multiplier_term']:.12f}",
    )
    check(
        "rho=delta reference Perron anchor is reproduced",
        abs(dec_delta["multiplier_term"] - P_TRIV_REFERENCE) < 5.0e-10
        and abs(dec_delta["lambda"] - LAMBDA_TRIV_REFERENCE) < 5.0e-10,
        f"lambda={dec_delta['lambda']:.12f}, <J>={dec_delta['multiplier_term']:.12f}",
    )
    check(
        "rho^tw composed Perron anchor is reproduced under zero-extension",
        abs(dec_tw["multiplier_term"] - P_TW_REFERENCE) < 5.0e-10
        and abs(dec_tw["lambda"] - LAMBDA_TW_REFERENCE) < 5.0e-10
        and tw_residual < 1.0e-12
        and tw_min > 0.0
        and tw_swap < 1.0e-12,
        f"lambda={dec_tw['lambda']:.12f}, <J>={dec_tw['multiplier_term']:.12f}, tensor residual={tw_residual:.3e}",
    )

    section("Part 2: Hellmann-Feynman derivative identity")
    print("M_beta = exp((beta/2) J), with J=(chi_(1,0)+chi_(0,1))/6.")
    print("For normalized Perron psi, the two multiplier derivative terms give exactly <psi,J psi> after division by lambda0.")
    print("D_beta^loc uses a_(p,q)(beta)^4; c_lambda derivatives use the same Bessel determinant mode sums with row-wise determinant differentiation.")
    check(
        "source multiplier parameter at beta=6 is beta/2=3, matching exp(3J)",
        abs(BETA0 / 2.0 - 3.0) < 1.0e-15,
    )
    check(
        "term-by-term differentiated local factor keeps a_(0,0)=1 with zero derivative",
        abs(setup0["a_link"][setup0["index"][(0, 0)]] - 1.0) < 1.0e-14
        and abs(setup0["da_link"][setup0["index"][(0, 0)]]) < 1.0e-12,
        f"a00={setup0['a_link'][setup0['index'][(0, 0)]]:.12f}, da00={setup0['da_link'][setup0['index'][(0, 0)]]:.3e}",
    )
    check(
        "reference environments rho=1 and rho=delta are beta-independent by construction",
        reference_rhos_are_beta_independent(),
        "there is no environment-derivative term for either reference solve",
    )

    exact_one = dec_one["multiplier_term"] + dec_one["d_loc_term"]
    exact_delta = dec_delta["multiplier_term"] + dec_delta["d_loc_term"]

    section("Part 3: exact-vs-FD validation on beta-independent reference rhos")
    fd_one = print_reference_fd_table("rho=1", "one", exact_one)
    print()
    fd_delta = print_reference_fd_table("rho=delta", "delta", exact_delta)
    check(
        "rho=1 exact derivative assembly agrees with Richardson FD",
        abs(fd_one["last_richardson"] - exact_one) < 1.0e-9
        and fd_one["noise_floor"] < 1.0e-9,
        f"exact={exact_one:.12f}, Richardson={fd_one['last_richardson']:.12f}, noise={fd_one['noise_floor']:.3e}",
    )
    check(
        "rho=delta exact derivative assembly agrees with Richardson FD",
        abs(fd_delta["last_richardson"] - exact_delta) < 1.0e-9
        and fd_delta["noise_floor"] < 1.0e-9,
        f"exact={exact_delta:.12f}, Richardson={fd_delta['last_richardson']:.12f}, noise={fd_delta['noise_floor']:.3e}",
    )

    section("Part 4: rho^tw beta-dependent environment derivative")
    tw_fd = rho_tw_environment_step_table(dec_tw)
    tw_total = dec_tw["multiplier_term"] + dec_tw["d_loc_term"] + tw_fd["env_final"]
    check(
        "rho^tw environment derivative has a stable Richardson sweep",
        tw_fd["env_noise"] < 1.0e-9 and tw_fd["full_noise"] < 1.0e-9,
        f"env noise={tw_fd['env_noise']:.3e}, full noise={tw_fd['full_noise']:.3e}",
    )
    check(
        "rho^tw assembled HF derivative agrees with full beta FD",
        abs(tw_total - tw_fd["full_final"]) < 1.0e-9,
        f"assembled={tw_total:.12f}, full FD Richardson={tw_fd['full_final']:.12f}",
    )

    rows = [
        {
            "label": "rho=1",
            "lambda": float(dec_one["lambda"]),
            "multiplier": float(dec_one["multiplier_term"]),
            "d_loc": float(dec_one["d_loc_term"]),
            "env": 0.0,
            "total": float(exact_one),
        },
        {
            "label": "rho=delta",
            "lambda": float(dec_delta["lambda"]),
            "multiplier": float(dec_delta["multiplier_term"]),
            "d_loc": float(dec_delta["d_loc_term"]),
            "env": 0.0,
            "total": float(exact_delta),
        },
        {
            "label": "rho^tw",
            "lambda": float(dec_tw["lambda"]),
            "multiplier": float(dec_tw["multiplier_term"]),
            "d_loc": float(dec_tw["d_loc_term"]),
            "env": float(tw_fd["env_final"]),
            "total": float(tw_total),
        },
    ]
    for row in rows:
        row["correction"] = row["d_loc"] + row["env"]
        row["ratio"] = row["correction"] / row["multiplier"]

    section("Part 5: correction scale")
    print_decomposition_table(rows)
    check(
        "rho=1 omitted derivative correction is measured as a nonzero fraction of the multiplier readout",
        rows[0]["correction"] > 0.0 and rows[0]["ratio"] > 0.1,
        f"correction={rows[0]['correction']:.12f}, ratio={rows[0]['ratio']:.12f}",
    )
    check(
        "rho=delta has zero local/environment correction in this normalized reference solve",
        abs(rows[1]["correction"]) < 1.0e-14 and abs(rows[1]["ratio"]) < 1.0e-14,
        f"correction={rows[1]['correction']:.3e}, ratio={rows[1]['ratio']:.3e}",
    )
    check(
        "rho^tw omitted derivative correction is measured with the beta-dependent environment term included",
        rows[2]["correction"] > 0.0 and rows[2]["ratio"] > 0.05,
        f"correction={rows[2]['correction']:.12f}, ratio={rows[2]['ratio']:.12f}",
    )

    section("Fenced hypothetical identification context")
    print("Hypothetical map only: if f were log(lambda0) per step, then 1+f' would be 1+d_beta log(lambda0).")
    print("The per-plaquette normalization theorem is an open target; these numbers are not an identification.")
    print_hypothetical_table(rows)
    comparator_fenced, comparator_offenders = comparator_is_fenced_to_hypothetical_table()
    check(
        "canonical comparator is isolated to the fenced context block and is not used as construction input",
        comparator_fenced,
        ", ".join(comparator_offenders) if comparator_offenders else "only print_hypothetical_table references the comparator",
    )

    section("Part 6: named residuals")
    print("Open target: prove or refute the per-plaquette normalization map linking the licensed plaquette readout to a beta derivative of the source-sector Perron value.")
    print("Residuals: physical 3D rho_(p,q)(6), untruncated tensor-transfer limit, multi-word/L_perp limits, and the identification theorem remain open.")
    check(
        "finite diagnostic reports correction scale separately from the multiplier readout",
        all(abs(row["multiplier"] + row["correction"] - row["total"]) < 1.0e-12 for row in rows)
        and rows[0]["correction"] > 0.0
        and rows[2]["correction"] > 0.0,
        f"rho=1 correction={rows[0]['correction']:.12f}; rho^tw correction={rows[2]['correction']:.12f}",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
