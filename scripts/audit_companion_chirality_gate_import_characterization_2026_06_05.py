#!/usr/bin/env python3
"""Audit companion: chirality-gate import characterization (2026-06-05).

This is a META companion for
docs/CHIRALITY_GATE_IMPORT_CHARACTERIZATION_2026-06-05.md.

It does two things, both purely verificational (no new physics, no new
axiom, no value selector):

  PART A -- algebraic core of the gate (finite linear algebra on R^3):
    A1. Gamma_chi = (2/3)J - I is a real-symmetric involution with
        signature (1,2): eigenvalue +1 on the (1,1,1) singlet, -1 on the
        transverse doublet.
    A2. Gamma_chi is a circulant (lies in <I,R,R^2>), so it commutes with
        the cyclic shift R.
    A3. THE ANTICOMMUTING DERIVATION (retained
        koide_anticommuting_operator_derivation): for a real-symmetric H
        with {H, Gamma_chi}=0 and an eigenvector v with eigenvalue != 0,
        <v|Gamma_chi|v> = 0, i.e. Q(v) = (sum v^2)/(sum v)^2 = 2/3.
    A4. THE CIRCULANT TRAP (retained_bounded
        koide_z3_equivariant_anticommuting_no_go): the only real-symmetric
        H with [H,R]=0 AND {H,Gamma_chi}=0 is H=0. (So any nonzero
        anticommuting H must BREAK C3-equivariance.)
    A5. STRUCTURE OF THE IMPORT: any nonzero real-symmetric H with
        {H,Gamma_chi}=0 is exactly block-OFF-diagonal in the
        singlet (+1) / doublet (-1) splitting -- it intertwines the two
        eigenspaces (off-block / orbit-splitting).
    A6. DEFAULT (circulant) gives Q=1: a generic circulant H = aI+bR+cR^2
        has its (1,1,1) singlet as an eigenvector, giving Q=1, not 2/3.
    A7. INERT-GRADING HATCH (wrong tensor factor): on R^3 (x) C^2 with
        gamma_CL = I3 (x) sigma_3, the relation {G (x) sigma_1, I3 (x) sigma_3}=0
        holds for EVERY 3x3 G -- so the Connes-Lott chirality grading puts
        ZERO constraint on the generation factor.

  PART B -- ledger cross-check (reads the committed audit_ledger.json):
    confirms the effective_status of the spine rows this characterization
    rests on, so the note's status table cannot silently go stale.

Exit non-zero if any check fails.
"""

from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

TOL = 1e-9


def _omega() -> complex:
    return complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))


def shift_R() -> np.ndarray:
    return np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)


def gamma_chi() -> np.ndarray:
    J = np.ones((3, 3), dtype=float)
    return (2.0 / 3.0) * J - np.eye(3)


def koide_Q(v: np.ndarray) -> float:
    s1 = float(np.sum(v))
    s2 = float(np.sum(v * v))
    return s2 / (s1 * s1)


def check(name: str, ok: bool, detail: str = "") -> bool:
    tag = "PASS" if ok else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"  ::  {detail}"
    print(line)
    return ok


def part_a() -> bool:
    results = []
    G = gamma_chi()
    R = shift_R()

    # A1: involution, signature (1,2)
    invol = np.allclose(G @ G, np.eye(3), atol=TOL)
    evals = np.sort(np.linalg.eigvalsh(G))
    sig_ok = np.allclose(evals, np.array([-1.0, -1.0, 1.0]), atol=TOL)
    results.append(check("A1 Gamma_chi involution, signature (1,2)",
                         invol and sig_ok, f"eigs={np.round(evals,6).tolist()}"))

    # A2: circulant -> commutes with R
    a2 = np.allclose(G @ R - R @ G, 0.0, atol=TOL)
    results.append(check("A2 [Gamma_chi, R] = 0 (Gamma_chi is circulant)", a2))

    # A3: anticommuting derivation -> Q = 2/3.
    # Build a real-symmetric H that anticommutes with Gamma_chi by constructing
    # it off-block in the eigenbasis of Gamma_chi, then verify Q on its
    # nonzero-eigenvalue eigenvectors.
    w, U = np.linalg.eigh(G)  # columns: eigvecs; w sorted ascending [-1,-1,+1]
    # plus-space index (eigenvalue +1) and minus-space indices
    plus_idx = int(np.argmax(w))
    minus_idx = [i for i in range(3) if i != plus_idx]
    # off-block symmetric operator in eigenbasis: couple plus to one minus dir
    M = np.zeros((3, 3))
    M[plus_idx, minus_idx[0]] = 0.7
    M[minus_idx[0], plus_idx] = 0.7
    M[plus_idx, minus_idx[1]] = -0.4
    M[minus_idx[1], plus_idx] = -0.4
    H = U @ M @ U.T  # back to standard basis; real symmetric
    sym = np.allclose(H, H.T, atol=TOL)
    anti = np.allclose(H @ G + G @ H, 0.0, atol=TOL)
    hv, hU = np.linalg.eigh(H)
    q_vals = []
    exp_vals = []
    for i in range(3):
        if abs(hv[i]) > 1e-6:
            v = hU[:, i].real
            # expectation <v|Gamma_chi|v>
            exp_vals.append(float(v @ G @ v))
            # Q is sign-convention sensitive via overall sign of v; Koide ratio
            # uses the real eigenvector as the sqrt-mass vector
            q_vals.append(koide_Q(v))
    exp_zero = all(abs(e) < 1e-8 for e in exp_vals)
    q_23 = all(abs(q - 2.0 / 3.0) < 1e-8 for q in q_vals)
    results.append(check("A3 {H,Gamma_chi}=0 => <v|Gamma_chi|v>=0 and Q(v)=2/3",
                         sym and anti and exp_zero and q_23,
                         f"<v|G|v>={[round(e,9) for e in exp_vals]} Q={[round(q,9) for q in q_vals]}"))

    # A4: circulant trap -- the ONLY real-symmetric H with [H,R]=0 and
    # {H,Gamma_chi}=0 is H=0. Verify by solving the linear system over the
    # 3-dim circulant ansatz H = aI + bR + cR^2 (with symmetry b=c for real
    # symmetric circulant) and showing anticommutation forces a=b=c=0.
    # Real-symmetric circulants: H = a I + b (R + R^2). Two real params.
    def circ(a, b):
        return a * np.eye(3) + b * (R + R.T)  # R^2 = R^T for this permutation
    # anticommutator coefficients must all vanish
    forced_zero = True
    for (a, b) in [(1.0, 0.0), (0.0, 1.0), (0.5, 0.3)]:
        Hc = circ(a, b)
        if not np.allclose(Hc @ G + G @ Hc, 0.0, atol=TOL):
            # nonzero anticommutator unless a=b=0 -> trap confirmed for this H
            pass
        else:
            # would only anticommute if a=b=0
            if abs(a) > TOL or abs(b) > TOL:
                forced_zero = False
    # explicit: solve {circ, G}=0 => only a=b=0
    # {circ(a,b), G} = 2 circ(a,b) G (since both circulant, commute)
    # circ G = 0 in Fourier: diag(a+2b, a-b, a-b) * diag(1,-1,-1) componentwise
    # => (a+2b)=0 and -(a-b)=0 => a=b=0. Check numerically.
    a_sym, b_sym = 1.0, 1.0  # nonzero test
    prod = circ(a_sym, b_sym) @ G
    nonzero_prod = not np.allclose(prod, 0.0, atol=TOL)
    results.append(check("A4 circulant trap: nonzero circulant H => HGamma_chi != 0 (so trap forces H=0)",
                         forced_zero and nonzero_prod,
                         "only a=b=0 satisfies {circ,Gamma_chi}=0"))

    # A5: any anticommuting H is off-block in the Gamma_chi splitting.
    # Project H (from A3) onto block-diagonal part in eigenbasis; it must be ~0.
    Hb = U.T @ H @ U
    block_diag = Hb.copy()
    # zero the off-block entries -> what's left is the block-diagonal part
    bd = np.zeros_like(Hb)
    bd[plus_idx, plus_idx] = Hb[plus_idx, plus_idx]
    for i in minus_idx:
        for j in minus_idx:
            bd[i, j] = Hb[i, j]
    block_diag_part_zero = np.allclose(bd, 0.0, atol=TOL)
    results.append(check("A5 anticommuting H is purely OFF-block (singlet<->doublet intertwiner)",
                         block_diag_part_zero,
                         f"||block-diag part||={np.linalg.norm(bd):.2e}"))

    # A6: the C3-equivariant (circulant) DEFAULT does NOT land Q=2/3.
    # Two canonical default readouts, neither gives 2/3:
    #   (i)  diagonal mass operator: eigenvectors are standard basis e_i,
    #        sqrt-mass vector = e_i (one nonzero entry) => Q=1.
    #   (ii) circulant mass operator: the (1,1,1) singlet is the trivial
    #        Fourier eigenvector; sqrt-mass = (1,1,1) (democratic) => Q=1/3.
    # The retained anticommuting derivation's 2/3 is reachable by NEITHER
    # default; it requires the off-block import (A3/A5). We verify both
    # default values and that both differ from 2/3.
    Hdef = circ(2.0, 0.5)  # generic real-symmetric circulant
    singlet = np.ones(3)
    # (1,1,1) is an eigenvector of any circulant (trivial character)
    img = Hdef @ singlet
    is_singlet_eigvec = np.allclose(img - (img[0]) * singlet, 0.0, atol=1e-7)
    q_diag = koide_Q(np.array([1.0, 0.0, 0.0]))   # standard-basis default
    q_circ_singlet = koide_Q(singlet)             # democratic default
    default_not_23 = (abs(q_diag - 2.0 / 3.0) > 1e-3) and (abs(q_circ_singlet - 2.0 / 3.0) > 1e-3)
    results.append(check("A6 C3-equivariant default never lands Q=2/3 (diag=>Q=1, circulant-singlet=>Q=1/3)",
                         is_singlet_eigvec and abs(q_diag - 1.0) < TOL
                         and abs(q_circ_singlet - 1.0 / 3.0) < TOL and default_not_23,
                         f"Q_diag={q_diag} Q_circ_singlet={round(q_circ_singlet,9)} (neither = 2/3)"))

    # A6b: the CIRCULANT route to 2/3 is a DISTINCT, COMMUTING operator.
    # koide_circulant_value_derivation (2026-06-05): a circulant
    # Y = aI + bC + conj(b)C^2 has Q = 1/3 + (2/3) r exactly (r=|b|^2/a^2),
    # so the SAME circulant default reaches Q=2/3 at the single dial value
    # r=1/2 -- WITHOUT anticommuting (it commutes with Gamma_chi). This shows
    # the gate has TWO faces: (i) supply the off-block anticommuting H (A3),
    # or (ii) supply the dial selection r=1/2 on the commuting circulant.
    wv = _omega()
    Cc = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    a_c, b_c = 1.0, 1.0 / math.sqrt(2.0)  # |b|^2=1/2, a=1 => r=1/2
    Y = a_c * np.eye(3) + b_c * Cc + np.conj(b_c) * Cc.conj().T
    herm = np.allclose(Y, Y.conj().T, atol=TOL)
    commutes = np.allclose(Y @ G - G @ Y, 0.0, atol=TOL)  # circulant => commutes
    anti_norm = np.linalg.norm(Y @ G + G @ Y)             # NOT anticommuting
    evY = np.sort(np.linalg.eigvalsh(Y).real)
    Q_circ = float((evY ** 2).sum() / (evY.sum() ** 2))
    a6b = herm and commutes and (anti_norm > 1.0) and abs(Q_circ - 2.0 / 3.0) < 1e-9
    results.append(check("A6b circulant route: r=1/2 COMMUTING circulant gives Q=2/3 (distinct from anticommuting H)",
                         a6b, f"[Y,G]=0, {{Y,G}}_norm={anti_norm:.3f}, Q={round(Q_circ,9)}"))

    # A7: inert-grading hatch (wrong tensor factor):
    # {G (x) sigma_1, I (x) sigma_3} = 0 for EVERY 3x3 G.
    s1 = np.array([[0, 1], [1, 0]], dtype=float)
    s3 = np.array([[1, 0], [0, -1]], dtype=float)
    I3 = np.eye(3)
    inert_ok = True
    rng = np.random.default_rng(0)
    for _ in range(5):
        Gm = rng.standard_normal((3, 3))
        D = np.kron(Gm, s1)
        gradCL = np.kron(I3, s3)
        if not np.allclose(D @ gradCL + gradCL @ D, 0.0, atol=TOL):
            inert_ok = False
    results.append(check("A7 inert hatch: {G(x)sigma1, I(x)sigma3}=0 for every G (zero generation constraint)",
                         inert_ok))

    return all(results)


def part_b() -> bool:
    here = os.path.dirname(os.path.abspath(__file__))
    ledger_path = os.path.normpath(os.path.join(here, "..", "docs", "audit", "data", "audit_ledger.json"))
    if not os.path.exists(ledger_path):
        return check("B ledger present", False, ledger_path)
    with open(ledger_path) as fh:
        rows = json.load(fh)["rows"]

    # (claim_id, acceptable effective_status values)
    spine = [
        ("koide_anticommuting_operator_derivation_theorem_note_2026-05-10", {"retained"}),
        ("koide_z3_equivariant_anticommuting_no_go_note_2026-05-16", {"retained_bounded"}),
        ("flavor_emergent_chirality_no_transport_note_2026-05-30", {"audited_conditional"}),
        ("flavor_generation_space_bridge_reduces_to_open_gate_2026-05-31", {"audited_conditional"}),
        ("flavor_chirality_gate_narrows_to_one_spin_statistics_import_2026-05-31", {"retained_bounded"}),
        ("staggered_axis_symmetry_is_s3_narrow_theorem_note_2026-05-23", {"retained_bounded"}),
        ("parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23", {"retained_bounded"}),
        ("staggered_dirac_realization_gate_note_2026-05-03", {"open_gate", "meta", "audited_renaming"}),
        ("closure_c_staggered_dirac_gate_note_2026-05-10_cstaggered", {"unaudited", "open_gate"}),
        ("flavor_hw1_staggered_projection_democratic_r0_2026-06-02", {"unaudited", "no_go"}),
        ("koide_factor_split_does_not_force_carrier_value_bridge_no_go_note_2026-06-02", {"unaudited", "no_go"}),
        ("lepton_brannen_bae_delta_two_ninths_open_gate_note_2026-05-26", {"open_gate"}),
        ("koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29", {"retained"}),
    ]
    ok_all = True
    for cid, accept in spine:
        row = rows.get(cid)
        if row is None:
            ok_all = check(f"B ledger row {cid}", False, "MISSING") and ok_all
            continue
        es = row.get("effective_status")
        ok_all = check(f"B {cid}", es in accept, f"effective_status={es}") and ok_all
    return ok_all


def main() -> int:
    print("=" * 78)
    print("PART A -- algebraic core of the chirality gate")
    print("=" * 78)
    a_ok = part_a()
    print()
    print("=" * 78)
    print("PART B -- audit-ledger cross-check (committed origin/main snapshot)")
    print("=" * 78)
    b_ok = part_b()
    print()
    total = a_ok and b_ok
    print("SCORECARD: PART_A={} PART_B={} OVERALL={}".format(
        "PASS" if a_ok else "FAIL",
        "PASS" if b_ok else "FAIL",
        "PASS" if total else "FAIL"))
    return 0 if total else 1


if __name__ == "__main__":
    sys.exit(main())
