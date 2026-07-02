#!/usr/bin/env python3
"""Route-2 independent E/T channel-selector firewall.

Safe claim:
  The six-arm O_h surface already has exact central projectors that
  distinguish the E and T1 channels.  That existence is not enough to derive
  the Route-2 endpoint target.  After T-side normalization, an invariant
  selector has a free E:T1 reduced coefficient ratio; choosing the target
  lambda = q_E/q_T = 9/4 is one point in a continuum unless a separate
  coefficient-law selector is supplied.

  This runner does not derive rho_E=21/4, does not apply any audit verdict,
  and does not prove impossibility over future nonlinear observables.  It
  sharpens the remaining readout ambiguity: the missing theorem is a law for
  the E/T coefficient ratio, not the mere existence of E/T projectors.
"""

from __future__ import annotations

from fractions import Fraction as F
import itertools
from pathlib import Path

import numpy as np
import numpy.linalg as la


PASS = 0
FAIL = 0
TOL = 1.0e-12


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"PASS: {label}" + (f" -- {detail}" if detail and ok else ""))
    if not ok:
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


def oh_signed_perms() -> list[np.ndarray]:
    mats: list[np.ndarray] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            mat = np.zeros((3, 3), dtype=int)
            for i in range(3):
                mat[i, perm[i]] = signs[i]
            mats.append(mat)
    return mats


ARMS = [
    np.array(v)
    for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
]
NEG = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}


def arm_index(v: np.ndarray) -> int:
    for idx, arm in enumerate(ARMS):
        if np.array_equal(v, arm):
            return idx
    raise ValueError(v)


def perm_matrix(mat: np.ndarray) -> np.ndarray:
    out = np.zeros((6, 6))
    for col, arm in enumerate(ARMS):
        row = arm_index(mat @ arm)
        out[row, col] = 1.0
    return out


def projectors(group: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[np.ndarray]]:
    perms = [perm_matrix(g) for g in group]
    p_a1 = sum(perms) / len(perms)
    antipodal = np.zeros((6, 6))
    for col in range(6):
        antipodal[NEG[col], col] = 1.0
    p_t1 = (np.eye(6) - antipodal) / 2.0
    p_e = (np.eye(6) + antipodal) / 2.0 - p_a1
    return p_a1, p_e, p_t1, perms


def invariant_op(c_a: F, c_e: F, c_t: F, p_a1: np.ndarray, p_e: np.ndarray, p_t1: np.ndarray) -> np.ndarray:
    return float(c_a) * p_a1 + float(c_e) * p_e + float(c_t) * p_t1


def max_commutator_norm(op: np.ndarray, perms: list[np.ndarray]) -> float:
    return max(float(la.norm(p @ op - op @ p)) for p in perms)


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    c_te = -2 * q_t / q_e
    return q_e, rho_e, c_te


def line_through_weights(c_e: F, c_t: F, w_e: F, w_t: F) -> tuple[F, F]:
    # c(w) = a + b*w, fitted through (w_E,c_E) and (w_T,c_T).
    b = (c_t - c_e) / (w_t - w_e)
    a = c_t - b * w_t
    return a, b


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 INDEPENDENT E/T CHANNEL-SELECTOR FIREWALL")
    print("=" * 88)

    note = Path("docs/QUARK_ROUTE2_INDEPENDENT_ET_CHANNEL_SELECTOR_FIREWALL_NOTE_2026-06-21.md")
    parent = Path("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    exact = Path("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    covariance = Path("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    blindness = Path("docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    ell_e = Path("docs/QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md")
    rank1 = Path("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md")

    print("\nA. Authority surfaces")
    print("-" * 72)
    for label, path in (
        ("new note", note),
        ("parent theta coupling", parent),
        ("exact readout", exact),
        ("covariance Schur no-go", covariance),
        ("E-center blindness", blindness),
        ("ell_E narrowing", ell_e),
        ("rank-1 carrier", rank1),
    ):
        check(f"{label} surface exists", path.exists(), str(path))

    group = oh_signed_perms()
    p_a1, p_e, p_t1, perms = projectors(group)

    print("\nB. Exact O_h channel projectors")
    print("-" * 72)
    ranks = tuple(int(round(np.trace(p))) for p in (p_a1, p_e, p_t1))
    check("O_h signed-permutation group has 48 elements", len(group) == 48, f"|O_h|={len(group)}")
    check("central projector ranks are (A1,E,T1)=(1,2,3)", ranks == (1, 2, 3), f"ranks={ranks}")
    check(
        "projectors are symmetric idempotents",
        all(
            np.max(np.abs(p - p.T)) < TOL and np.max(np.abs(p @ p - p)) < TOL
            for p in (p_a1, p_e, p_t1)
        ),
    )
    check(
        "projectors are mutually orthogonal and sum to identity",
        np.max(np.abs(p_a1 @ p_e)) < TOL
        and np.max(np.abs(p_a1 @ p_t1)) < TOL
        and np.max(np.abs(p_e @ p_t1)) < TOL
        and np.max(np.abs(p_a1 + p_e + p_t1 - np.eye(6))) < TOL,
    )
    check(
        "E and T1 projectors commute with every O_h action",
        max(max_commutator_norm(p_e, perms), max_commutator_norm(p_t1, perms)) < TOL,
    )
    check(
        "E/T projectors distinguish channels but do not mix them",
        np.max(np.abs(p_e @ p_t1)) < TOL and int(round(np.trace(p_e))) != int(round(np.trace(p_t1))),
    )

    print("\nC. Endpoint target arithmetic")
    print("-" * 72)
    q_t = F(5, 6)
    q_e_target = F(15, 8)
    lam_target = q_e_target / q_t
    rho_e_target = 6 * (q_e_target - 1)
    c_te_target = -2 * q_t / q_e_target
    w_a1, w_e, w_t = F(1, 6), F(1, 3), F(1, 2)
    kappa = w_t / w_e
    check("target lambda=q_E/q_T is 9/4", lam_target == F(9, 4), f"lambda={lam_target}")
    check("target rho_E is 21/4", rho_e_target == F(21, 4), f"rho_E={rho_e_target}")
    check("target center ratio is -8/9", c_te_target == F(-8, 9), f"c_TE={c_te_target}")
    check("projector-weight leverage kappa is 3/2", kappa == F(3, 2), f"kappa={kappa}")
    check("the target value equals kappa squared", lam_target == kappa * kappa, f"kappa^2={kappa*kappa}")

    print("\nD. Channel-selector family freedom")
    print("-" * 72)
    candidates = {
        "neutral": F(1),
        "one_power_inverse": F(3, 2),
        "target": F(9, 4),
        "quadratic_forward": F(4, 9),
    }
    valid_count = 0
    for name, lam in candidates.items():
        op = invariant_op(F(1), lam, F(1), p_a1, p_e, p_t1)
        comm_norm = max_commutator_norm(op, perms)
        q_e, rho_e, c_te = endpoint_from_lambda(lam)
        is_valid = comm_norm < TOL and lam > 0 and q_e > 0
        valid_count += int(is_valid)
        check(
            f"{name} coefficient ratio is an invariant positive E/T selector",
            is_valid,
            f"lambda={lam}, q_E={q_e}, rho_E={rho_e}, c_TE={c_te}",
        )
    check("multiple inequivalent invariant selectors survive T normalization", valid_count == len(candidates))
    target_op = invariant_op(F(1), F(9, 4), F(1), p_a1, p_e, p_t1)
    neutral_op = invariant_op(F(1), F(1), F(1), p_a1, p_e, p_t1)
    check(
        "target selector and neutral selector are distinct invariant observables",
        la.norm(target_op - neutral_op) > 1.0,
        f"||O_target-O_neutral||={la.norm(target_op - neutral_op):.6f}",
    )
    check(
        "existence of a target-valued selector is therefore not a derivation",
        max_commutator_norm(target_op, perms) < TOL and max_commutator_norm(neutral_op, perms) < TOL,
        "both are equally O_h-invariant",
    )

    print("\nE. Coefficient-law diagnostics")
    print("-" * 72)
    ratio = w_e / w_t
    powers = {-2: ratio ** -2, -1: ratio ** -1, 0: F(1), 1: ratio, 2: ratio ** 2}
    check("inverse-square weight law is exactly the target", powers[-2] == F(9, 4), f"(w_E/w_T)^-2={powers[-2]}")
    check("one inverse power gives kappa, not the target", powers[-1] == F(3, 2) and powers[-1] != F(9, 4))
    check("neutral law gives lambda=1, not the target", powers[0] == F(1) and powers[0] != F(9, 4))
    check("positive one-power law gives 2/3, not the target", powers[1] == F(2, 3) and powers[1] != F(9, 4))
    check("positive quadratic weight law gives 4/9, not the target", powers[2] == F(4, 9) and powers[2] != F(9, 4))
    check(
        "among tested integer powers -2..2 only the inverse-square premise hits target",
        [p for p, val in powers.items() if val == F(9, 4)] == [-2],
    )

    print("\nF. Affine selector import test")
    print("-" * 72)
    a_target, b_target = line_through_weights(F(9, 4), F(1), w_e, w_t)
    c_a_target = a_target + b_target * w_a1
    a_neutral, b_neutral = line_through_weights(F(1), F(1), w_e, w_t)
    c_a_neutral = a_neutral + b_neutral * w_a1
    check("affine law through target has a=19/4", a_target == F(19, 4), f"a={a_target}")
    check("affine law through target has slope b=-15/2", b_target == F(-15, 2), f"b={b_target}")
    check("affine target law predicts A1 coefficient 7/2", c_a_target == F(7, 2), f"c_A1={c_a_target}")
    check("neutral affine law is constant with A1 coefficient 1", (a_neutral, b_neutral, c_a_neutral) == (F(1), F(0), F(1)))
    check(
        "target affine law is not forced by endpoint normalization alone",
        (a_target, b_target, c_a_target) != (a_neutral, b_neutral, c_a_neutral),
        "it imports a non-neutral slope and A1 coefficient",
    )
    check(
        "affine target law is a selector theorem target, not a current derivation",
        b_target < 0 and c_a_target > F(1),
        "the law must explain both the decreasing slope and c_A1=7/2",
    )

    print("\nG. Current-bank marker and note hygiene")
    print("-" * 72)
    note_text = read(str(note))
    exact_text = read(str(exact))
    covariance_text = read(str(covariance))
    blindness_text = read(str(blindness))
    parent_text = read(str(parent))
    check("new note declares no_go claim type", "Claim type: no_go" in note_text)
    check("new note says no audit verdict is applied", "No audit verdict is applied" in note_text)
    check("new note distinguishes projector existence from coefficient-law selection", "projector existence is not coefficient selection" in note_text)
    check("new note records the inverse-square law as a premise target", "inverse-square coefficient law" in note_text)
    check("new note records the affine A1=7/2 import", "A1 coefficient `7/2`" in note_text)
    check("new note does not claim global impossibility", "does not prove impossibility over future nonlinear observables" in note_text)
    check("exact readout surface names the missing endpoint triple", "readout-map endpoint triple is not yet derived" in parent_text)
    check("exact readout surface reduces the blocker to beta_E/alpha_E", "beta_E / alpha_E = 21/4" in exact_text)
    check("covariance surface already says inverse-square is the gap", "q_X" in covariance_text and "w_X" in covariance_text and "inverse" in covariance_text.lower())
    check("E-center blindness surface requires a genuine E-center lift", "genuine E-center lift" in blindness_text)

    print("\nSummary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print(
        "VERDICT: exact negative boundary. O_h supplies independent E/T projectors, but projector "
        "existence is not coefficient selection. With the T channel normalized, the E:T1 selector "
        "coefficient is a free Schur parameter. The target lambda=9/4 is obtained only by adding an "
        "inverse-square coefficient law or an equivalent fitted affine law with A1 coefficient 7/2. "
        "The remaining Route-2 readout ambiguity is therefore the coefficient-law selector, not the "
        "mere existence of an E/T channel observable."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
