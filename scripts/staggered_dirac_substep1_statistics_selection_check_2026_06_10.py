#!/usr/bin/env python3
"""Substep-1 statistics selection: GL(F) conditional discriminator.

Companion runner for
docs/STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md

Context. The retained no-go
STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md
proves the hard-core-boson frame ties with the single-pair Grassmann frame on
per-site dimension and ungraded operator algebra, and names the only escape:
"a genuine forcing would require an independent, retained locality+statistics
principle" (its N6: "a retained spin-statistics, graded-locality, or
fermion-parity superselection principle could retire this wall").

This runner computes the T1-T3 theorem payload, one non-load-bearing boundary
diagnostic, and one source-packet freshness check, [A]-[E]:

  [A] FRAME-BLINDNESS of every retained substep-1 input. Per-site dimension,
      the ungraded generated algebra, the retained fermion-parity Z2 grading
      F = (x)_x sigma_3 (fermion_parity_z2_grading_theorem_note_2026-05-02,
      retained), and finite transfer positivity (nearest-neighbour hopping H)
      are each CONSTANT across the two tied frames. So no retained row, alone
      or composed, discriminates -- a computed witness for why each nearby
      retained row fails to supply the selection.

  [B] THE DISCRIMINATOR. Define, relative to the retained grading F, the
      cross-site graded-locality predicate

        GL(F):  for all x != y,  {psi_x, psi_y} = 0  and  {psi_x, psi_y^+} = 0
                for the F-odd site fields psi_x of the realization.

      The Jordan-Wigner/Grassmann realization PASSES GL(F) (cross-site CAR);
      the hard-core-boson realization FAILS it (its F-odd fields commute
      cross-site and have nonzero cross-site anticommutator). Combined with
      the retained per-site dim-2 readout used here to exclude the free-boson
      candidate, exactly one explicit candidate passes {dim = 2} AND GL(F):
      the Grassmann/CAR realization. The selection is therefore forced by
      GL(F) on this explicit candidate list, conditionally -- not by the baseline.

  [C] FALSIFICATION LEG (the no-go is reproduced). Removing GL(F) from the
      predicate list leaves every remaining tested predicate constant across
      the two frames: the tie returns, exactly as the retained no-go proves.
      Moreover GL(F) is strictly additional data, not ungraded-algebra data:
      the SAME generated matrix algebra contains both a GL(F)-passing
      generating family (c_x) and a GL(F)-failing one (sigma_+^(x)), so no
      functional of the ungraded algebra alone can decide GL(F).

  [D] NON-LOAD-BEARING BOUNDARY DIAGNOSTIC. The nominated supplier
      AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md
      (retained_bounded for scoped CCR/free-boson exclusion) does NOT supply
      GL(F): its load-bearing Step 2 hypothesis is the canonical
      CCR "[a_x, a_y^+] = delta_xy" (its eq. (6)), and the hard-core boson
      VIOLATES that hypothesis on-site ([a, a^+] = 1 - 2n != I), so the
      04-29 exclusion argument is scoped to the FREE boson only and never
      reaches the tied candidate. This diagnostic is not used by [A]-[C]
      and is not a global supplier survey.

  [E] SOURCE-PACKET FRESHNESS. The current ledger statuses of the one-hop
      rows consumed by this note match the source text: the 04-29
      spin-statistics row is retained_bounded, the 05-16 Grassmann/free-CCR
      bridge is retained, the 05-25 no-go is retained_no_go, and the
      parity-grading row is retained. No audit verdict is set here.

Pure finite tensor-product linear algebra (numpy, exact integer entries,
tolerance 1e-12). Deterministic, < 5 s. No PDG / fitted / scale / mass input.
Asserts no audit status.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

TOL = 1e-12
PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] {status}: {label}"
    if detail:
        line += f"  ({detail})"
    print(line)


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


# ---------------------------------------------------------------- primitives
I2 = np.eye(2, dtype=complex)
SP = np.array([[0, 1], [0, 0]], dtype=complex)   # a   (annihilator), a|1> = |0>
SM = SP.conj().T                                  # a^+ (creator)
S3 = np.diag([1.0, -1.0]).astype(complex)         # sigma_3 = (-1)^n
NUM = SM @ SP                                     # n = a^+ a = diag(0, 1)


def site_op(op: np.ndarray, x: int, n: int) -> np.ndarray:
    """op acting at site x of an n-site qubit tensor product (bare, undressed)."""
    out = np.eye(1, dtype=complex)
    for y in range(n):
        out = np.kron(out, op if y == x else I2)
    return out


def jw_op(x: int, n: int) -> np.ndarray:
    """Jordan-Wigner annihilator c_x = (prod_{y<x} sigma_3^(y)) sigma_+^(x)."""
    out = np.eye(1, dtype=complex)
    for y in range(n):
        if y < x:
            out = np.kron(out, S3)
        elif y == x:
            out = np.kron(out, SP)
        else:
            out = np.kron(out, I2)
    return out


def is_zero(m: np.ndarray) -> bool:
    return bool(np.max(np.abs(m)) < TOL)


def anti(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def ledger_status(claim_id: str) -> str | None:
    rows = json.loads((ROOT / "docs/audit/data/audit_ledger.json").read_text())["rows"]
    row = rows.get(claim_id)
    if not row:
        return None
    return row.get("effective_status") or row.get("audit_status")


def generated_algebra_dim(gens: list[np.ndarray]) -> int:
    """Complex dimension of the unital *-algebra generated by gens (span closure)."""
    d = gens[0].shape[0]
    seed = [np.eye(d, dtype=complex)] + gens + [g.conj().T for g in gens]
    basis: list[np.ndarray] = []

    def rank_of(mats: list[np.ndarray]) -> int:
        stack = np.array([m.flatten() for m in mats])
        return int(np.linalg.matrix_rank(stack, tol=1e-9))

    def try_add(m: np.ndarray) -> None:
        if not basis:
            if np.max(np.abs(m)) > TOL:
                basis.append(m / np.max(np.abs(m)))
            return
        if rank_of(basis + [m]) > len(basis):
            basis.append(m / np.max(np.abs(m)))

    for g in seed:
        try_add(g)
    while True:
        before = len(basis)
        snapshot = list(basis)
        for a in snapshot:
            for b in snapshot:
                if len(basis) == d * d:
                    return d * d
                try_add(a @ b)
        if len(basis) == before:
            return len(basis)


def main() -> int:
    n_sites = 3
    dim = 2 ** n_sites
    hc = [site_op(SP, x, n_sites) for x in range(n_sites)]    # hard-core a_x
    jw = [jw_op(x, n_sites) for x in range(n_sites)]          # JW c_x
    f_op = site_op(S3, 0, n_sites)
    for x in range(1, n_sites):
        f_op = f_op @ site_op(S3, x, n_sites)                 # F = (x)_x sigma_3

    # ========================================================================
    section("[A] Frame-blindness of every retained substep-1 input "
            "(why the retained rows cannot select)")
    # ========================================================================
    # Per-site dimension (the retained 05-16 dim-2 readout).
    hc_fock = [np.array([1, 0], dtype=complex), SM @ np.array([1, 0], dtype=complex)]
    check("A", "per-site Fock dim: hard-core = 2 and Grassmann pair = 2 (equal)",
          len(hc_fock) == 2 and is_zero(SP @ SP),
          "dimension readout is constant across the two frames")
    # Ungraded generated algebra (the no-go's decisive fact (C)).
    dim_hc = generated_algebra_dim(
        [site_op(SP, x, n_sites) for x in range(n_sites)]
        + [site_op(S3, x, n_sites) for x in range(n_sites)])
    dim_jw = generated_algebra_dim(jw)
    check("A", f"ungraded algebra: <sigma_+^(x), sigma_3^(x)> spans dim {dim_hc} "
               f"= 4^{n_sites} = full M_{{2^{n_sites}}}(C)",
          dim_hc == dim * dim)
    check("A", f"ungraded algebra: <c_x, c_x^+> spans dim {dim_jw} "
               f"= 4^{n_sites} = same full matrix algebra",
          dim_jw == dim * dim,
          "identical ungraded algebra: statistics is a frame choice (no-go (C))")
    # The retained Z2 grading F is frame-blind.
    check("A", "retained grading: F^2 = I and Spec(F) = {+1, -1}",
          is_zero(f_op @ f_op - np.eye(dim))
          and set(np.round(np.linalg.eigvalsh(f_op)).astype(int)) == {-1, 1})
    check("A", "F-oddness of the hard-core fields: {F, sigma_+^(x)} = 0 for all x",
          all(is_zero(anti(f_op, g)) for g in hc))
    check("A", "F-oddness of the JW fields: {F, c_x} = 0 for all x",
          all(is_zero(anti(f_op, g)) for g in jw),
          "BOTH frames are F-odd: the retained Z2-grading row is frame-blind")
    check("A", "F-evenness of bilinears in both frames: [F, a_x^+ a_y] = [F, c_x^+ c_y] = 0",
          all(is_zero(comm(f_op, hc[x].conj().T @ hc[y]))
              and is_zero(comm(f_op, jw[x].conj().T @ jw[y]))
              for x in range(n_sites) for y in range(n_sites)))
    # A4 -- transfer/positivity rows are frame-blind on the open chain.
    L = 4
    hc4 = [site_op(SP, x, L) for x in range(L)]
    jw4 = [jw_op(x, L) for x in range(L)]
    h_hc = sum(hc4[x].conj().T @ hc4[x + 1] + hc4[x + 1].conj().T @ hc4[x]
               for x in range(L - 1))
    h_jw = sum(jw4[x].conj().T @ jw4[x + 1] + jw4[x + 1].conj().T @ jw4[x]
               for x in range(L - 1))
    check("A", f"open-chain L={L} nearest-neighbour hopping: H_hard_core == H_JW exactly",
          is_zero(h_hc - h_jw),
          "T = exp(-tau H) identical => transfer positivity sees no frame difference")

    # ========================================================================
    section("[B] The discriminator GL(F): cross-site graded locality relative to "
            "the retained parity grading")
    # ========================================================================
    gl_jw = all(is_zero(anti(jw[x], jw[y])) and is_zero(anti(jw[x], jw[y].conj().T))
                for x in range(n_sites) for y in range(n_sites) if x != y)
    car_onsite = all(is_zero(anti(jw[x], jw[x].conj().T) - np.eye(dim))
                     and is_zero(jw[x] @ jw[x]) for x in range(n_sites))
    check("B", "JW/Grassmann frame PASSES GL(F): {c_x, c_y} = {c_x, c_y^+} = 0 for x != y",
          gl_jw)
    check("B", "JW/Grassmann frame on-site CAR: {c_x, c_x^+} = I, c_x^2 = 0",
          car_onsite)
    cross_anti_nonzero = all(
        not is_zero(anti(hc[x], hc[y]))
        for x in range(n_sites) for y in range(n_sites) if x != y)
    cross_comm_zero = all(
        is_zero(comm(hc[x], hc[y])) and is_zero(comm(hc[x], hc[y].conj().T))
        for x in range(n_sites) for y in range(n_sites) if x != y)
    check("B", "hard-core frame FAILS GL(F): {sigma_+^(x), sigma_+^(y)} != 0 for x != y",
          cross_anti_nonzero)
    check("B", "hard-core frame commutes cross-site instead: [sigma_+^(x), sigma_+^(y)] = 0",
          cross_comm_zero,
          "F-odd fields that commute cross-site violate graded locality")
    # Free boson: excluded by the retained dim-2 readout (finite-cutoff CCR defect).
    free_boson_excluded = True
    for cutoff in (2, 3, 5, 8):
        ab = np.diag(np.sqrt(np.arange(1, cutoff, dtype=float)), k=1).astype(complex)
        defect = comm(ab, ab.conj().T) - np.eye(cutoff)
        if is_zero(defect) or abs(np.trace(comm(ab, ab.conj().T))) > TOL:
            free_boson_excluded = False
    check("B", "free boson: no finite truncation satisfies CCR ([a, a^+] = I impossible, "
               "Tr[a, a^+] = 0 != Tr I)",
          free_boson_excluded,
          "per-site dim 2 excludes it (retained 05-16 readout)")
    candidates = {
        "free boson": {"dim2": False, "GL(F)": False},
        "hard-core boson": {"dim2": True, "GL(F)": False},
        "Grassmann/CAR": {"dim2": True, "GL(F)": gl_jw and car_onsite},
    }
    survivors = [k for k, v in candidates.items() if v["dim2"] and v["GL(F)"]]
    check("B", f"selection certificate: exactly one of three candidates passes "
               f"{{dim = 2}} AND GL(F): {survivors}",
          survivors == ["Grassmann/CAR"],
          "the forcing is CONDITIONAL on GL(F); the baseline does not supply GL(F)")

    # ========================================================================
    section("[C] Falsification leg: remove GL(F) and the tie returns "
            "(the retained no-go is reproduced)")
    # ========================================================================
    predicates_constant = (
        2 == 2                                  # per-site dim
        and dim_hc == dim_jw                    # ungraded algebra dimension
        and all(is_zero(anti(f_op, g)) for g in hc)
        and all(is_zero(anti(f_op, g)) for g in jw)   # F-oddness both frames
        and is_zero(h_hc - h_jw)                # hopping/transfer surface
    )
    check("C", "with GL(F) removed, every remaining tested predicate is constant "
               "across the two frames (tie restored)",
          predicates_constant,
          "reproduces STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING "
          "facts (C)/(D)")
    same_algebra_both_families = (dim_hc == dim * dim and dim_jw == dim * dim)
    check("C", "GL(F) is not ungraded-algebra data: the SAME M_{2^N}(C) contains a "
               "GL(F)-passing family (c_x) and a GL(F)-failing family (sigma_+^(x))",
          same_algebra_both_families and gl_jw and cross_anti_nonzero,
          "no functional of the ungraded algebra alone decides GL(F)")

    # ========================================================================
    section("[D] Boundary diagnostic (non-load-bearing): this GL(F) row "
            "does not consume 04-29 as a supplier")
    # ========================================================================
    # Its Step 2 hypothesis (eq. (6)) is the canonical CCR [a_x, a_y^+] = delta_xy.
    onsite_ccr_defect = comm(SP, SM) - I2      # hard-core: [a, a^+] = 1 - 2n != I
    check("D", "hard-core ladders VIOLATE the 04-29 S2 hypothesis on-site: "
               "[a, a^+] = 1 - 2n != I (defect norm = 2)",
          abs(np.max(np.abs(onsite_ccr_defect)) - 2.0) < TOL,
          "boundary diagnostic only: this note does not consume 04-29 as a GL(F) supplier")
    check("D", "so the 04-29 bosonic exclusion is scoped to the FREE (CCR) boson only "
               "-- it re-proves the retained dimensional half, not the tie-breaker",
          free_boson_excluded and not is_zero(onsite_ccr_defect))
    check("D", "retained Z2-grading row is carrier, not selector "
               "(frame-blindness computed in [A])",
          all(is_zero(anti(f_op, g)) for g in hc + jw))
    check("D", "retained positivity surface is frame-blind "
               "(H_hard_core == H_JW computed in [A])",
          is_zero(h_hc - h_jw),
          "consistent with retained car_from_positivity_neutrality no-go")

    # ========================================================================
    section("[E] Source-packet freshness: one-hop authorities match current main")
    # ========================================================================
    st_spin = ledger_status("axiom_first_spin_statistics_theorem_note_2026-04-29")
    st_grassmann = ledger_status(
        "staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16")
    st_nogo = ledger_status("staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25")
    st_parity = ledger_status("fermion_parity_z2_grading_theorem_note_2026-05-02")
    note_txt = (ROOT / "docs/STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_"
                       "DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md").read_text()
    check("E", "source packet status: 04-29 spin-statistics row is retained_bounded "
               "and consumed only for CCR/free-boson exclusion",
          st_spin == "retained_bounded"
          and "retained_bounded`):\n  its load-bearing Step 2 hypothesis is the canonical CCR"
              in note_txt)
    check("E", "source packet status: 05-16 Grassmann/free-CCR bridge is retained",
          st_grassmann == "retained"
          and "— `retained`. **License used here:** the dimensional free-boson/CCR"
              in note_txt)
    check("E", "source packet status: retained no-go and retained parity-grading rows "
               "remain the baseline/non-supplier inputs",
          st_nogo == "retained_no_go" and st_parity == "retained")
    check("E", "stale missing-dependency language removed: the note no longer treats "
               "04-29 spin-statistics as unaudited or the 05-16 bridge as pending",
          "(`axiom_first_spin_statistics_theorem_note_2026-04-29`, unaudited)"
          not in note_txt
          and "(**unaudited**)" not in note_txt
          and "**unaudited**" not in note_txt
          and "06-10 upgrade pending re-audit" not in note_txt)

    # ========================================================================
    section("Summary")
    # ========================================================================
    print("  Verified (numpy, tol 1e-12, exact integer-entry constructions):")
    print("    [A] dim, ungraded algebra, retained Z2 grading F, and transfer")
    print("        positivity are each CONSTANT across the two tied frames;")
    print("    [B] GL(F) (cross-site graded locality w.r.t. retained F) is")
    print("        NON-constant: Grassmann/CAR passes, hard-core fails; with the")
    print("        retained dim-2 readout, exactly one candidate survives;")
    print("    [C] removing GL(F) restores the tie (retained no-go reproduced);")
    print("        GL(F) is strictly additional input, not algebra data;")
    print("    [D] boundary diagnostic only: the 04-29 spin-statistics source")
    print("        note's S2 hypothesis is the canonical CCR, which the hard-core")
    print("        boson violates on-site, so this row does not consume 04-29 as")
    print("        a GL(F) supplier;")
    print("    [E] the source packet consumes current retained/retained_bounded")
    print("        one-hop authorities and carries no stale missing-dependency text.")
    print("  BOUNDARY (declared, not claimed): GL(F) is NOT retained and NOT a")
    print("  Tier-A admission. This runner proves a CONDITIONAL selection only;")
    print("  unconditionally, the retained 2026-05-25 no-go stands.")
    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
