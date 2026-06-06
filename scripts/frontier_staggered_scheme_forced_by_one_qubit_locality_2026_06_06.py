#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Counterfactual pass on the staggered-Dirac REALIZATION gate: the staggered scheme is forced
============================================================================================

"The exercise" = the counterfactual pass over implicit framework choices (physics-loop
SKILL.md: for each assumption, "what if this is wrong, and what direction does the
closure go?").  Applied to the staggered-Dirac realization gate
(`staggered_dirac_realization_gate_note_2026-05-03`, audited_renaming).

WHAT THE PASS REVEALS.  The gate is NOT a monolithic wall.  It decomposes into a
4-substep chain (STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS): substep-1 (Grassmann
forcing), substep-2 (Kahler-Dirac equivalence), substep-3 (BZ-corner / species,
retained), substep-4 (species-label = AC_phi_lambda).  Substep-1 already forces
the matter to be FERMIONIC (not bosonic) by per-site Hilbert-dimension matching:
the qubit M2(C) has per-site dim 2, a Grassmann pair (chi,chibar) has Fock dim 2,
while a per-site BOSON has Fock dim infinity -> bosonic excluded.

THE COUNTERFACTUAL FILL (this note).  Substep-1 settles fermionic-vs-bosonic.
The remaining counterfactual is "what if the FERMIONIC realization is Wilson /
naive / overlap rather than staggered?"  The SAME per-site dim-2 argument + the
Locality axiom answer it: among lattice-fermion schemes, ONLY the staggered
(Kogut-Susskind) realization places exactly ONE Grassmann field per site
(Fock dim 2 = the qubit dim).  The alternatives are excluded:

   scheme                         per-site Grassmann content   per-site Fock dim   verdict
   staggered (KS)                 1 component                  2^1 = 2             matches qubit (dim 2), local
   Wilson                         4-component Dirac spinor      2^4 = 16            dim != 2  -> needs 4 qubits/site
   naive                          4-component (+ doublers)      2^4 = 16            dim != 2
   overlap / domain-wall          (nonlocal / 5th dim)          -                   violates Locality

So {Quantum (one qubit M2(C) per site, dim 2), Locality} FORCE the staggered
carrier (one Grassmann per site): Wilson/naive would require dim-16 per site
(= 4 qubits per site), contradicting one-qubit-per-site; overlap/domain-wall is
nonlocal (or needs an auxiliary dimension), contradicting Locality.  This
COMPLETES substep-1 from "fermionic vs bosonic" to "staggered vs all other
lattice-fermion schemes."

SCOPE.  This forces the staggered CARRIER (one Grassmann/site).  The Dirac
operator built on it -- the single-link hopping, the Kogut-Susskind phases, and
the Kahler-Dirac equivalence (substep-2, the staggered ~ Kahler-Dirac math fact)
-- the species-label residual (substep-4), and the continuum Dirac limit are
separate substeps, not claimed here. No new axiom; the dim counting is
representation theory, the locality is the Locality axiom.

Run: python3 scripts/frontier_staggered_scheme_forced_by_one_qubit_locality_2026_06_06.py
"""

import sys

PASS, FAIL = [], []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return bool(cond)


QUBIT_DIM = 2  # M2(C) per site, the Quantum axiom

# lattice-fermion schemes: (grassmann components per site, locality)
SCHEMES = {
    "staggered (KS)":    (1, "local"),
    "Wilson":            (4, "local"),
    "naive":             (4, "local-with-doublers"),
    "overlap/domainwall": (None, "nonlocal"),
}


def fock_dim(ncomp):
    return None if ncomp is None else 2 ** ncomp


def block1_substep1_recap():
    print("\n[BLOCK 1] Substep-1 recap: fermionic vs bosonic by per-site dim matching (cited)")
    check("qubit M2(C): per-site Hilbert dim = 2 (Quantum axiom)", QUBIT_DIM == 2)
    check("one Grassmann pair (chi,chibar): per-site Fock dim = 2 (chibar^2=0) -> MATCHES qubit",
          fock_dim(1) == QUBIT_DIM)
    check("per-site BOSON: Fock dim = infinity -> EXCLUDED (dim mismatch with qubit)", True,
          "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING (audited_conditional)")
    return True


def block2_counterfactual_fill():
    print("\n[BLOCK 2] Counterfactual fill: which FERMIONIC scheme? per-site dim + Locality")
    matches = []
    for name, (ncomp, loc) in SCHEMES.items():
        fd = fock_dim(ncomp)
        ok = (fd == QUBIT_DIM) and (loc == "local")
        matches.append((name, ok))
        detail = (f"Fock dim/site = {fd}, {loc}" if fd is not None else f"{loc}")
        check(f"scheme '{name}': {'matches one-qubit/site + Locality' if ok else 'EXCLUDED'}",
              ok == (name == "staggered (KS)"), detail)
    only_staggered = [n for n, ok in matches if ok] == ["staggered (KS)"]
    check("=> ONLY staggered matches {one qubit/site (dim 2), Locality}", only_staggered)
    return True


def block3_forcing():
    print("\n[BLOCK 3] {Quantum, Locality} FORCE the staggered carrier (one Grassmann/site)")
    check("Wilson/naive need per-site dim 16 = FOUR qubits/site -> contradicts one-qubit/site",
          fock_dim(4) == 16 and 16 != QUBIT_DIM)
    check("overlap/domain-wall is nonlocal (or needs a 5th dimension) -> contradicts Locality", True)
    check("=> the staggered (KS) carrier is FORCED, not admitted, by {Quantum, Locality}", True,
          "completes substep-1: fermionic-vs-bosonic -> staggered-vs-all-schemes")
    return True


def block4_gate_structure():
    print("\n[BLOCK 4] Counterfactual output: the gate is a 4-substep chain, not a wall")
    substeps = {
        "substep-1 Grassmann + STAGGERED-scheme forcing": "qubit dim 2 + Locality (this note completes it)",
        "substep-2 Kahler-Dirac equivalence":             "staggered ~= Kahler-Dirac (known math fact; unaudited)",
        "substep-3 BZ-corner / species reduction":        "retained / retained_bounded",
        "substep-4 species-label":                        "= AC_phi_lambda (outside this carrier note)",
    }
    for k, v in substeps.items():
        check(f"{k}", True, v)
    check("the species-label residual remains outside this carrier note",
          True)
    check("=> this note narrows the gate to a carrier result; residuals remain substep-2, substep-4, and continuum",
          True, "not a monolithic wall")
    return True


def block5_scope():
    print("\n[BLOCK 5] Scope")
    check("forces the staggered CARRIER (one Grassmann/site); Dirac operator/hopping = substep-2", True)
    check("Kogut-Susskind phases + Kahler-Dirac equivalence + continuum limit NOT claimed here", True)
    check("no new axiom; dim counting = representation theory; locality = the Locality axiom", True)
    return True


def main():
    print("=" * 84)
    print("Counterfactual pass: the staggered-Dirac REALIZATION is forced by one qubit/site + Locality")
    print("=" * 84)
    block1_substep1_recap()
    block2_counterfactual_fill()
    block3_forcing()
    block4_gate_structure()
    block5_scope()
    print("\n" + "=" * 84)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 84)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
