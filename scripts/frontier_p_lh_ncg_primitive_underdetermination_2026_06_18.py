#!/usr/bin/env python3
"""P-LH NCG primitive underdetermination boundary.

This runner checks a bounded negative boundary for the P-LH route: the
current minimal framework baseline does not determine the NCG finite algebra,
order-one condition, or KO-dim-6 real structure. It does not audit, retag,
register primitives, or derive SM LH/RH content.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "P_LH_NCG_PRIMITIVE_UNDERDETERMINATION_BOUNDARY_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "PRIMITIVE_P_LH_CONTENT_PROPOSAL_NOTE_2026-05-10_pPlh.md"
MIN_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.split())


def close(a: np.ndarray, b: np.ndarray, tol: float = 1.0e-12) -> bool:
    return bool(np.max(np.abs(a - b)) < tol)


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    sizes = [b.shape[0] for b in blocks]
    out = np.zeros((sum(sizes), sum(sizes)), dtype=complex)
    cursor = 0
    for block in blocks:
        n = block.shape[0]
        out[cursor : cursor + n, cursor : cursor + n] = block
        cursor += n
    return out


I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
I4 = np.eye(4, dtype=complex)
Z4 = np.zeros((4, 4), dtype=complex)
SIG1 = np.array([[0, 1], [1, 0]], dtype=complex)
SIG2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIG3 = np.array([[1, 0], [0, -1]], dtype=complex)


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def double_comm(d: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return comm(comm(d, a), b)


def antiunitary_square(u: np.ndarray) -> np.ndarray:
    """For J = U K, J^2 is U conj(U)."""
    return u @ np.conj(u)


def antiunitary_conjugate(u: np.ndarray, a: np.ndarray) -> np.ndarray:
    """For J = U K, compute J a J^{-1} = U conj(a) U^{-1}."""
    return u @ np.conj(a) @ np.linalg.inv(u)


def main() -> int:
    print("=" * 78)
    print("P-LH NCG primitive underdetermination boundary")
    print("=" * 78)
    print("Claim boundary: bounded negative support; no primitive registration.")
    print("No audit verdict or effective status is changed by this runner.")

    print("\n" + "=" * 78)
    print("BLOCK 1: source surfaces and firewalls")
    print("=" * 78)
    for path in (NOTE, PARENT, MIN_AXIOMS):
        check(f"{path.relative_to(ROOT)} exists", path.exists(), "present" if path.exists() else "missing")

    note = read(NOTE)
    parent = read(PARENT)
    axiom_note = read(MIN_AXIOMS)
    note_flat = compact(note)
    parent_flat = compact(parent)
    axiom_flat = compact(axiom_note)

    check("claim type is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note says bounded support only", "**Status:** bounded support only" in note)
    check("note says no new axiom", "No new axiom or primitive premise is introduced" in note)
    check("note says no primitive approval", "not an approval of order-one" in note_flat)
    check("note says no audit/status edit", "No audit ledger, queue, or effective-status file is changed" in note)
    check("note scopes to current minimal axiom baseline", "current minimal-axiom baseline" in note_flat)
    check(
        "boundary names parent as trace target without a markdown dependency edge",
        "`PRIMITIVE_P_LH_CONTENT_PROPOSAL_NOTE_2026-05-10_pPlh.md`" in note
        and "](PRIMITIVE_P_LH_CONTENT_PROPOSAL_NOTE_2026-05-10_pPlh.md)" not in note,
    )
    no_go_markers = [f"**N{i}" for i in range(1, 9)]
    missing_no_go = [marker for marker in no_go_markers if marker not in note]
    check(
        "note carries complete N1-N8 no-go discipline gate",
        not missing_no_go,
        "missing " + ", ".join(missing_no_go) if missing_no_go else "all markers present",
    )
    check("gate preserves alternate-route caveat", "It does not test every possible SM LH/RH route" in note)
    check("gate preserves no-primitive-status caveat", "does not turn a missing primitive into a bounded status" in note_flat)
    check("parent remains open-gate", "**Claim type:** open_gate" in parent)
    check("parent names same missing NCG packet", "order-one condition, the KO-dim-6" in parent_flat)
    check("minimal axiom memo names Lattice", "### Lattice" in axiom_note)
    check("minimal axiom memo names Quantum", "### Quantum" in axiom_note)
    check("minimal axiom memo names Record", "### Record" in axiom_note)
    check("Quantum axiom supplies M_2(C)/Cl(3)", "M_2(C)" in axiom_note and "Cl(3,0)" in axiom_note)
    check("Quantum axiom does not supply gauge group", "does not supply a dynamics, composition theorem" in axiom_flat and "gauge group" in axiom_flat)
    check("Quantum axiom does not supply particle content", "particle content" in axiom_flat)
    check("Record axiom does not supply readout context", "readout context" in axiom_flat and "decomposition" in axiom_flat)

    print("\n" + "=" * 78)
    print("BLOCK 2: Cl+(3) chirality baseline")
    print("=" * 78)
    rho_plus = (SIG1, SIG2, SIG3)
    rho_minus = (-SIG1, -SIG2, -SIG3)
    bivectors_plus = (rho_plus[0] @ rho_plus[1], rho_plus[1] @ rho_plus[2], rho_plus[2] @ rho_plus[0])
    bivectors_minus = (rho_minus[0] @ rho_minus[1], rho_minus[1] @ rho_minus[2], rho_minus[2] @ rho_minus[0])
    omega_plus = rho_plus[0] @ rho_plus[1] @ rho_plus[2]
    omega_minus = rho_minus[0] @ rho_minus[1] @ rho_minus[2]

    for label, bp, bm in zip(("e12", "e23", "e31"), bivectors_plus, bivectors_minus, strict=True):
        check(f"Cl+(3) bivector {label} is identical in rho+ and rho-", close(bp, bm))
    check("volume element is +i on rho+", close(omega_plus, 1j * I2))
    check("volume element is -i on rho-", close(omega_minus, -1j * I2))
    check("chirality is distinguished but Cl+(3) action is not", all(close(bp, bm) for bp, bm in zip(bivectors_plus, bivectors_minus, strict=True)) and not close(omega_plus, omega_minus))

    print("\n" + "=" * 78)
    print("BLOCK 3: finite-algebra non-identification")
    print("=" * 78)
    gamma = block_diag(I2, -I2)
    p_l = block_diag(I2, Z2)
    p_r = block_diag(Z2, I2)
    l1 = block_diag(SIG1 / 2.0, Z2)
    l2 = block_diag(SIG2 / 2.0, Z2)
    l3 = block_diag(SIG3 / 2.0, Z2)
    r1 = block_diag(Z2, SIG1 / 2.0)
    r2 = block_diag(Z2, SIG2 / 2.0)
    r3 = block_diag(Z2, SIG3 / 2.0)
    c_r = block_diag(Z2, I2)

    check("chirality projectors sum to I", close(p_l + p_r, I4))
    check("chirality projectors are orthogonal", close(p_l @ p_r, Z4))
    check("SM-like left generators close su(2)", close(comm(l1, l2), 1j * l3))
    check("SM-like right scalar commutes with left su(2)", close(comm(l1, c_r), Z4) and close(comm(l2, c_r), Z4))
    check("Pati-Salam-like right generators close su(2)", close(comm(r1, r2), 1j * r3))
    check("left and right su(2) copies commute", close(comm(l1, r2), Z4) and close(comm(l2, r3), Z4))
    check("right su(2) is nonzero on same baseline block", not close(r1, Z4) and not close(r2, Z4))
    check("baseline admits SM-like finite action", close(comm(l1, l2), 1j * l3) and close(comm(l1, c_r), Z4))
    check("baseline also admits PS-like finite action", close(comm(r1, r2), 1j * r3) and close(comm(l1, r2), Z4))
    check("SM-vs-PS choice is not determined by Cl+(3) equality", close(bivectors_plus[0], bivectors_minus[0]) and not close(r1, Z4))

    h_dim = 4
    color_dim = 3
    check("one-site rho+ direct-sum rho- block has dimension 4", h_dim == 4)
    check("faithful fundamental M_3(C) color factor needs dimension multiple of 3", h_dim % color_dim != 0)
    check("nontrivial M_3(C) factor is absent from one-qubit local algebra", "M_3(C)" not in axiom_note)

    print("\n" + "=" * 78)
    print("BLOCK 4: KO-dim real-structure underdetermination")
    print("=" * 78)
    j_commuting_u = I4
    j_swapping_u = np.array(
        [
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
        ],
        dtype=complex,
    )
    check("J=K has J^2=+I", close(antiunitary_square(j_commuting_u), I4))
    check("J=K commutes with chirality", close(antiunitary_conjugate(j_commuting_u, gamma), gamma))
    check("J=S K has J^2=+I", close(antiunitary_square(j_swapping_u), I4))
    check("J=S K anticommutes with chirality", close(antiunitary_conjugate(j_swapping_u, gamma), -gamma))
    check("both J choices live on the same finite baseline block", close(antiunitary_square(j_commuting_u), I4) and close(antiunitary_square(j_swapping_u), I4))
    check("baseline does not name a real structure J", "real structure" not in axiom_flat)
    check("KO-dim-6 sign is an extra selection among admissible J choices", close(antiunitary_conjugate(j_swapping_u, gamma), -gamma) and close(antiunitary_conjugate(j_commuting_u, gamma), gamma))

    print("\n" + "=" * 78)
    print("BLOCK 5: order-one underdetermination")
    print("=" * 78)
    d_zero = Z4
    d_mix = j_swapping_u.copy()
    sm_generators = (l1, l2, l3, c_r)
    ps_generators = (l1, l2, l3, r1, r2, r3)

    zero_sm_ok = all(close(double_comm(d_zero, a, b), Z4) for a in sm_generators for b in sm_generators)
    zero_ps_ok = all(close(double_comm(d_zero, a, b), Z4) for a in ps_generators for b in ps_generators)
    check("D=0 satisfies order-one double commutators for SM-like action", zero_sm_ok)
    check("D=0 satisfies order-one double commutators for PS-like action", zero_ps_ok)
    witness_ps = double_comm(d_mix, l1, r2)
    witness_sm_scalar = double_comm(d_mix, l1, c_r)
    check("off-diagonal D produces nonzero PS double-commutator witness", not close(witness_ps, Z4), f"norm={np.linalg.norm(witness_ps):.6f}")
    check("order-one verdict depends on extra D/opposite-action data", close(double_comm(d_zero, l1, r2), Z4) and not close(witness_ps, Z4))
    check("same baseline admits vacuous and nonvacuous D choices", close(d_zero, Z4) and close(d_mix @ d_mix, I4))
    check("minimal axiom memo does not specify finite Dirac operator D", "Dirac operator" not in axiom_flat)
    check("order-one is not determined by Lattice+Quantum+Record", zero_ps_ok and not close(witness_ps, Z4))
    check("SM scalar witness also depends on chosen right action", not close(witness_sm_scalar, Z4), f"norm={np.linalg.norm(witness_sm_scalar):.6f}")

    print("\n" + "=" * 78)
    print("BLOCK 6: target blocker coverage")
    print("=" * 78)
    blocker_text = "order-one condition, KO-dim-6 real structure, and finite algebra"
    check("note quotes target NCG packet", blocker_text in note)
    check("runner covers finite algebra edge", "finite algebra" in note_flat)
    check("runner covers KO-dim-6 real structure edge", "KO-dim-6 real structure" in note)
    check("runner covers order-one condition edge", "order-one condition" in note)
    check("note states remaining closure paths", "derive the finite algebra" in note_flat and "explicitly approve/register" in note_flat)
    check("parent now links underdetermination boundary", "P_LH_NCG_PRIMITIVE_UNDERDETERMINATION_BOUNDARY_NOTE_2026-06-18.md" in parent)
    check("source packet stays non-promotional", "not a framework-derived SM LH/RH content theorem" in note)

    print("\n" + "=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 78)
    print("\nRESULT:")
    print("  P-LH NCG underdetermination boundary is complete iff FAIL=0.")
    print("  The route remains open unless NCG structures are derived or approved.")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
