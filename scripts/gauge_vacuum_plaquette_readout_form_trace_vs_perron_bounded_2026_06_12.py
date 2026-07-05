#!/usr/bin/env python3
"""Finite derived-time trace readout versus Perron readout for landed sources.

This runner uses the landed source-sector transfer machinery:

    T_src(6) = exp(3 J) D_6^loc C_(Z_6^env) exp(3 J)

and compares the finite derived-time trace readout

    R(L_t) = Tr[J T_src(6)^L_t] / Tr[T_src(6)^L_t]

against the Perron readout <psi_0, J psi_0> for three already-landed rho inputs:
rho=1, rho=delta_(0,0), and the finite tensor-word rho^tw zero-extension.

The beta-derivative diagnostic is restricted to the explicit exp(beta J / 2)
multipliers. It does not evaluate the D_beta' or environment-beta terms.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
REPO_ROOT = SCRIPT_DIR.parent
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_READOUT_FORM_TRACE_VS_PERRON_BOUNDED_NOTE_2026-06-12.md"
)

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing
import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as tw_existing


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
SOURCE_NMAX = 7
SOURCE_MODE_MAX = 200
TRACE_L_VALUES = (2, 4, 8, 16, 32, 64)
ACCEPTED_MC_L_VALUES = (3, 4, 5, 6, 8)
ALL_CHECK_L_VALUES = tuple(sorted(set(TRACE_L_VALUES + ACCEPTED_MC_L_VALUES)))
RESIDUAL_SCALE = 0.02
TOL = 1.0e-10

ANCHORS = {
    "rho=1 P_loc": ("0.4524071590", 0.4524071590),
    "rho=delta P_triv": ("0.4225317396", 0.4225317396),
    "rho^tw P_tw": ("0.434215413260", 0.434215413260),
}

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
    print("=" * 100)
    print(title)
    print("=" * 100)


def source_setup() -> dict[str, object]:
    j_op, weights, index = src_existing.build_J(SOURCE_NMAX)
    a_link, d_loc, c00 = src_existing.build_local_factor(
        weights, index, SOURCE_MODE_MAX, BETA
    )
    multiplier = src_existing.matrix_exp_symmetric(j_op, BETA / 2.0)
    swap = src_existing.conjugation_swap_matrix(weights, index)
    return {
        "j": j_op,
        "weights": weights,
        "index": index,
        "a_link": a_link,
        "d_loc": d_loc,
        "c00": c00,
        "multiplier": multiplier,
        "swap": swap,
    }


def rho_tw_zero_extension(
    source_weights: list[tuple[int, int]],
) -> tuple[np.ndarray, dict[str, float]]:
    tw = tw_existing.build_tensor_word(
        tw_existing.TW_NMAX_DEFAULT, tw_existing.TW_MODE_MAX_DEFAULT
    )
    tw_eig, psi_tw, rho_small = tw_existing.perron_vector_of_tensor_word(
        tw["tensor_word"], tw["index"]
    )
    rho_map = {w: float(rho_small[i]) for i, w in enumerate(tw["weights"])}
    rho_vec = np.array([rho_map.get(w, 0.0) for w in source_weights], dtype=float)
    tw_index = tw["index"]
    residual = float(
        np.linalg.norm(tw["tensor_word"] @ psi_tw - tw_eig * psi_tw, ord=np.inf)
    )
    return rho_vec, {
        "tw_eig": float(tw_eig),
        "rho10": float(rho_small[tw_index[(1, 0)]]),
        "rho11": float(rho_small[tw_index[(1, 1)]]),
        "rho_min_available": float(np.min(rho_small)),
        "rho_available_swap": float(
            np.max(
                np.abs(
                    rho_small
                    - np.array(
                        [rho_small[tw_index[(q, p)]] for p, q in tw["weights"]]
                    )
                )
            )
        ),
        "psi_residual": residual,
    }


def rho_cases(setup: dict[str, object]) -> list[dict[str, object]]:
    weights = setup["weights"]
    index = setup["index"]
    rho_one = np.ones(len(weights), dtype=float)
    rho_delta = np.zeros(len(weights), dtype=float)
    rho_delta[index[(0, 0)]] = 1.0
    rho_tw, tw_meta = rho_tw_zero_extension(weights)
    return [
        {
            "label": "rho=1 P_loc",
            "short": "rho=1",
            "rho": rho_one,
            "anchor_digits": ANCHORS["rho=1 P_loc"][0],
            "anchor_value": ANCHORS["rho=1 P_loc"][1],
            "digits": 10,
            "meta": {},
        },
        {
            "label": "rho=delta P_triv",
            "short": "rho=delta",
            "rho": rho_delta,
            "anchor_digits": ANCHORS["rho=delta P_triv"][0],
            "anchor_value": ANCHORS["rho=delta P_triv"][1],
            "digits": 10,
            "meta": {},
        },
        {
            "label": "rho^tw P_tw",
            "short": "rho^tw",
            "rho": rho_tw,
            "anchor_digits": ANCHORS["rho^tw P_tw"][0],
            "anchor_value": ANCHORS["rho^tw P_tw"][1],
            "digits": 12,
            "meta": tw_meta,
        },
    ]


def transfer_from_rho(setup: dict[str, object], rho_vec: np.ndarray) -> np.ndarray:
    multiplier = setup["multiplier"]
    d_loc = setup["d_loc"]
    return multiplier @ d_loc @ np.diag(rho_vec) @ multiplier


def eig_trace_data(transfer: np.ndarray, j_op: np.ndarray) -> dict[str, object]:
    vals, vecs = np.linalg.eigh(transfer)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    lam0 = float(vals[0])
    ratios = vals / lam0
    j_diag = np.einsum("ij,ij->j", vecs, j_op @ vecs)
    r_inf = float(j_diag[0])
    gap_abs = float(np.max(np.abs(ratios[1:]))) if len(ratios) > 1 else 0.0
    gap_signed = float(ratios[1]) if len(ratios) > 1 else 0.0
    return {
        "values": vals,
        "vectors": vecs,
        "ratios": ratios,
        "j_diag": j_diag,
        "lambda0": lam0,
        "R_inf": r_inf,
        "gap_abs": gap_abs,
        "gap_signed": gap_signed,
    }


def trace_readout_from_eigs(data: dict[str, object], lt: int) -> float:
    ratios = data["ratios"]
    j_diag = data["j_diag"]
    weights = ratios**lt
    return float(np.sum(weights * j_diag) / np.sum(weights))


def powers_up_to(transfer: np.ndarray, max_power: int) -> list[np.ndarray]:
    powers = [np.eye(transfer.shape[0])]
    for _ in range(max_power):
        powers.append(powers[-1] @ transfer)
    return powers


def raw_trace_readout(powers: list[np.ndarray], j_op: np.ndarray, lt: int) -> float:
    return float(np.trace(j_op @ powers[lt]) / np.trace(powers[lt]))


def insertion_position_residual(
    powers: list[np.ndarray], j_op: np.ndarray, lt: int
) -> float:
    denom = float(np.trace(powers[lt]))
    baseline = raw_trace_readout(powers, j_op, lt)
    residuals = []
    for pos in range(lt):
        val = float(np.trace(powers[pos] @ j_op @ powers[lt - pos]) / denom)
        residuals.append(abs(val - baseline))
    return max(residuals) if residuals else 0.0


def explicit_multiplier_derivative_density(
    powers: list[np.ndarray], transfer: np.ndarray, j_op: np.ndarray, lt: int
) -> float:
    # T'_explicit = 1/2 (J T + T J), holding D_beta and C_env fixed.
    t_prime_explicit = 0.5 * (j_op @ transfer + transfer @ j_op)
    numerator = lt * float(np.trace(t_prime_explicit @ powers[lt - 1]))
    denominator = float(np.trace(powers[lt]))
    return numerator / (float(lt) * denominator)


def rho_admissibility(
    case: dict[str, object], setup: dict[str, object], transfer: np.ndarray
) -> tuple[bool, str]:
    rho = case["rho"]
    weights = setup["weights"]
    index = setup["index"]
    swap_residual = float(
        np.max(np.abs(rho - np.array([rho[index[(q, p)]] for p, q in weights])))
    )
    normalized = abs(float(rho[index[(0, 0)]]) - 1.0)
    rho_min = float(np.min(rho))
    rho_max = float(np.max(rho))
    transfer_sym = float(np.max(np.abs(transfer - transfer.T)))
    eig_min = float(np.min(np.linalg.eigvalsh(transfer)))
    ok = (
        np.all(np.isfinite(rho))
        and normalized < 1.0e-12
        and rho_min >= -1.0e-14
        and swap_residual < 1.0e-12
        and transfer_sym < 1.0e-11
        and eig_min > -1.0e-12
    )
    return (
        ok,
        (
            f"rho00={float(rho[index[(0, 0)]]):.12f}, min={rho_min:.3e}, "
            f"max={rho_max:.3e}, swap={swap_residual:.3e}, "
            f"T_sym={transfer_sym:.3e}, min_eig={eig_min:.3e}"
        ),
    )


def format_anchor(value: float, digits: int) -> str:
    return f"{value:.{digits}f}"


def main() -> int:
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())

    print("Gauge-vacuum plaquette finite-L_t trace readout versus Perron readout")
    print(f"source NMAX={SOURCE_NMAX}, MODE_MAX={SOURCE_MODE_MAX}, beta={BETA:.1f}")
    print(
        "Status authority: independent audit lane only. "
        "This runner does not set or predict an audit outcome."
    )

    setup = source_setup()
    j_op = setup["j"]
    weights = setup["weights"]
    index = setup["index"]
    swap = setup["swap"]
    j_sym = float(np.max(np.abs(j_op - j_op.T)))
    j_swap = float(np.max(np.abs(swap @ j_op - j_op @ swap)))
    multiplier = setup["multiplier"]
    m_sym = float(np.max(np.abs(multiplier - multiplier.T)))
    m_min = float(np.min(np.linalg.eigvalsh(multiplier)))

    section("Gate 1: source operator and rho admissibility")
    check(
        "source operator J is symmetric and conjugation-swap symmetric",
        j_sym < 1.0e-15 and j_swap < 1.0e-12,
        f"J_sym={j_sym:.3e}, J_swap={j_swap:.3e}",
    )
    check(
        "half-slice multiplier exp(3J) is symmetric positive in the source box",
        m_sym < 1.0e-12 and m_min > 0.0,
        f"M_sym={m_sym:.3e}, M_min_eig={m_min:.12e}",
    )

    cases = rho_cases(setup)
    results: list[dict[str, object]] = []
    for case in cases:
        transfer = transfer_from_rho(setup, case["rho"])
        admissible, detail = rho_admissibility(case, setup, transfer)
        check(f"{case['short']} rho is normalized nonnegative and symmetric", admissible, detail)
        if case["short"] == "rho^tw":
            meta = case["meta"]
            print(
                "rho^tw builder metadata: "
                f"tw_eig={meta['tw_eig']:.12f}, "
                f"rho10={meta['rho10']:.12f}, rho11={meta['rho11']:.12f}, "
                f"available_min={meta['rho_min_available']:.3e}, "
                f"available_swap={meta['rho_available_swap']:.3e}, "
                f"psi_residual={meta['psi_residual']:.3e}"
            )
            check(
                "rho^tw landed builder Perron residual and conjugation symmetry are stable",
                meta["psi_residual"] < 1.0e-12
                and meta["rho_available_swap"] < 1.0e-12
                and meta["rho_min_available"] > 0.0,
                (
                    f"residual={meta['psi_residual']:.3e}, "
                    f"swap={meta['rho_available_swap']:.3e}, "
                    f"available_min={meta['rho_min_available']:.3e}"
                ),
            )
        data = eig_trace_data(transfer, j_op)
        powers = powers_up_to(transfer, max(ALL_CHECK_L_VALUES))
        eig, psi, perron_p = src_existing.perron_state_and_value(transfer, j_op)
        results.append(
            {
                "case": case,
                "transfer": transfer,
                "data": data,
                "powers": powers,
                "perron_eig": eig,
                "perron_p": perron_p,
                "psi_min": float(np.min(psi)),
            }
        )

    section("Gate 2: Perron anchor reproduction")
    for row in results:
        case = row["case"]
        data = row["data"]
        r_inf = data["R_inf"]
        perron_p = row["perron_p"]
        digits = case["digits"]
        anchor_digits = case["anchor_digits"]
        formatted = format_anchor(r_inf, digits)
        check(
            f"{case['short']} L_t -> inf readout reproduces landed anchor digits",
            formatted == anchor_digits and abs(r_inf - perron_p) < 5.0e-13,
            (
                f"R_inf={r_inf:.15f}, formatted={formatted}, "
                f"anchor={anchor_digits}, Perron_solver={perron_p:.15f}"
            ),
        )
        check(
            f"{case['short']} Perron eigenvalue is positive and eigenvector sign is fixed",
            row["perron_eig"] > 0.0 and row["psi_min"] >= -1.0e-12,
            f"lambda0={row['perron_eig']:.15f}, psi_min={row['psi_min']:.3e}",
        )

    section("Finite trace table: requested L_t values")
    print(
        "rho | L_t | R_trace(L_t) | R_infinity | correction R(L_t)-R_inf | "
        "gap_abs^L_t"
    )
    print("-" * 100)
    for row in results:
        case = row["case"]
        data = row["data"]
        for lt in TRACE_L_VALUES:
            r_lt = trace_readout_from_eigs(data, lt)
            corr = r_lt - data["R_inf"]
            rate = data["gap_abs"] ** lt
            print(
                f"{case['short']:<9} | {lt:>3d} | {r_lt:.15f} | "
                f"{data['R_inf']:.15f} | {corr:+.15e} | {rate:.3e}"
            )
    print()
    print("Spectral convergence rates:")
    for row in results:
        case = row["case"]
        data = row["data"]
        print(
            f"  {case['short']:<9}: lambda0={data['lambda0']:.15f}, "
            f"lambda1/lambda0={data['gap_signed']:.15e}, "
            f"max_subperron_abs={data['gap_abs']:.15e}"
        )

    section("Accepted MC-surface L values: comparison-context table only")
    print(
        "No fitting or L_t selection is performed here; these rows only report "
        "the finite trace reading at the geometry inputs named by the FSS context."
    )
    print("rho | L_t | R_trace(L_t) | correction R(L_t)-R_inf")
    print("-" * 78)
    for row in results:
        case = row["case"]
        data = row["data"]
        for lt in ACCEPTED_MC_L_VALUES:
            r_lt = trace_readout_from_eigs(data, lt)
            corr = r_lt - data["R_inf"]
            print(f"{case['short']:<9} | {lt:>3d} | {r_lt:.15f} | {corr:+.15e}")

    section("Gate 3: cyclic trace and derivative-form diagnostics")
    max_cyclic = 0.0
    max_eig_direct = 0.0
    max_derivative = 0.0
    for row in results:
        case = row["case"]
        data = row["data"]
        transfer = row["transfer"]
        powers = row["powers"]
        for lt in ALL_CHECK_L_VALUES:
            eig_readout = trace_readout_from_eigs(data, lt)
            direct_readout = raw_trace_readout(powers, j_op, lt)
            cyclic = insertion_position_residual(powers, j_op, lt)
            deriv = explicit_multiplier_derivative_density(powers, transfer, j_op, lt)
            max_eig_direct = max(max_eig_direct, abs(eig_readout - direct_readout))
            max_cyclic = max(max_cyclic, cyclic)
            max_derivative = max(max_derivative, abs(deriv - direct_readout))
        print(
            f"{case['short']:<9}: max insertion-position residual <= "
            f"{max_cyclic:.3e} so far"
        )
    check(
        "spectral formula matches direct finite traces for all reported L_t values",
        max_eig_direct < 1.0e-12,
        f"max|R_eigh-R_direct|={max_eig_direct:.3e}",
    )
    check(
        "cyclic trace makes the raw J insertion independent of insertion position",
        max_cyclic < 1.0e-12,
        f"max insertion-position residual={max_cyclic:.3e}",
    )
    check(
        "explicit-multiplier beta-derivative density equals the symmetrized raw J readout",
        max_derivative < 1.0e-12,
        (
            f"max derivative-density residual={max_derivative:.3e}; "
            "D_beta prime and environment beta terms are not evaluated here"
        ),
    )

    section("Gate 4: residual-scale question")
    max_trace_set = 0.0
    max_trace_record = ("", 0)
    max_mc_set = 0.0
    max_mc_record = ("", 0)
    for row in results:
        case = row["case"]
        data = row["data"]
        for lt in TRACE_L_VALUES:
            corr_abs = abs(trace_readout_from_eigs(data, lt) - data["R_inf"])
            if corr_abs > max_trace_set:
                max_trace_set = corr_abs
                max_trace_record = (case["short"], lt)
        for lt in ACCEPTED_MC_L_VALUES:
            corr_abs = abs(trace_readout_from_eigs(data, lt) - data["R_inf"])
            if corr_abs > max_mc_set:
                max_mc_set = corr_abs
                max_mc_record = (case["short"], lt)
    print(
        f"max requested-set correction: {max_trace_set:.15e} "
        f"at {max_trace_record[0]}, L_t={max_trace_record[1]}"
    )
    print(
        f"max accepted-MC-L correction: {max_mc_set:.15e} "
        f"at {max_mc_record[0]}, L_t={max_mc_record[1]}"
    )
    check(
        "no reported finite trace correction exceeds the panel-era residual scale 0.02",
        max(max_trace_set, max_mc_set) < RESIDUAL_SCALE,
        (
            f"max={max(max_trace_set, max_mc_set):.3e}, "
            f"scale={RESIDUAL_SCALE:.3e}; statement is restricted to reported L_t values"
        ),
    )

    section("Boundaries")
    print("Convention-consistent readout: Tr[J T_src(6)^L_t] / Tr[T_src(6)^L_t].")
    print(
        "Derivative diagnostic: (1/L_t) d/d beta log Tr[T_beta^L_t] restricted "
        "to the explicit exp(beta J/2) multipliers."
    )
    print(
        "Difference from the full beta derivative: the D_beta prime and any "
        "environment-beta contribution are named open terms, not computed here."
    )
    print(
        "Named open targets: identification theorem for readout versus per-plaquette "
        "f-prime; HF D_beta prime term; per-plaquette normalization; licensed L_t "
        "geometry input."
    )
    required_note_markers = [
        "**Type:** bounded_theorem",
        "finite source-sector computation at source `NMAX = 7`",
        "This note does not compute the physical 3D unmarked spatial Wilson environment",
        "No literature value, new axiom, external citation, new comparator number, or fitted selector is used.",
        "This statement is restricted to the finite rho inputs and `L_t` values reported above.",
        "Full beta derivative: the HF `D_beta prime` term",
        "Licensed `L_t` geometry input for the accepted periodic source surface.",
    ]
    forbidden_note_markers = [
        "effective_status",
        "audited_clean",
        "full beta derivative is negligible",
        "physical 3D unmarked spatial Wilson environment is negligible",
    ]
    missing_note_markers = [m for m in required_note_markers if m not in note_flat]
    present_forbidden = [m for m in forbidden_note_markers if m in note_flat]
    check(
        "source note states the finite bounded boundary and leaves physical targets open",
        not missing_note_markers and not present_forbidden,
        (
            f"missing={missing_note_markers}; "
            f"forbidden_present={present_forbidden}"
        ),
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
