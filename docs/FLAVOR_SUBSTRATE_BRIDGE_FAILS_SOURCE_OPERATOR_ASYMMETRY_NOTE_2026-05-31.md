# Flavor — the substrate-necessity bridge fails; the onsite-source line rests on an unjustified source/operator asymmetry (consistent onsite-locality gives Q=1/3, not Q=2/3)

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** bounded negative (bridge fails 3 ways) + a load-bearing structural correction to the onsite-source line.
**Runner:** `scripts/flavor_substrate_bridge_fails_source_operator_asymmetry_2026_05_31.py` (SCORECARD PASS=4).
**Source:** 6-agent build `wf_e95a1fb8` (centering guard / single-axiom audit / off-diagonal-source / adversary → adjudication).

## Question
Can the substrate-necessity bridge (retaining `single_axiom_hilbert` / `single_axiom_information`) **derive
source/observable-locality from framework baseline**, upgrading the Axiom 2-plus half-axiom to A2 and thereby deriving Q=2/3?

## Verdict — the bridge fails, three independent ways, and the guard exposed a deeper problem
**B1 — the vehicles ASSUME, do not DERIVE locality.** Confirmed against the ledger: `single_axiom_hilbert` =
audited_renaming; `single_axiom_information` = meta/unaudited. Their *own* headers and audit verdicts state
they do **not** derive the local Hamiltonian, the locality restriction, or the Born readout from the
tensor-product Hilbert space — these are *admitted* inputs (class-E/F definitional compression). The audit
verdict: "the chain does not close from the single axiom alone." Neither is near retained-grade; neither is
"one retention away."

**B2 — wrong target even if retained.** What they would deliver is *generic* tensor-product / observable
locality, **not** the specific retention law ("physical mass *sources* are onsite-diagonal") the descent needs.

**B3 — the centering re-centers on the answer.** `z = (1−2r)/(1+2r)` is the Möbius image of the operator
modulus `r`. The *literal* source operator `H = S(z) = I + zZ` at source-free `S=I` (z=0) gives the
**degenerate spectrum {1,1,1} → Q=1/3, not 2/3** (verified). "z=0 → Q=2/3" holds *only* on the reduced/Brannen
carrier, where z=0 means `r=1/2` (the *split* operator) — i.e. the coordinate is centered on the answer.

**B4 — the fatal source/operator asymmetry (what the guard found).** The descent `E_loc(X)=(Tr X/3)·I` erases
the `Z` background on the *source* `S=I+zZ` → Q=2/3. But the generation **mass operator** `H = aI + bC + b̄C²`
is *itself* off-diagonal (`Diag(H)=I`). Applying the **same** onsite-locality to `H` collapses it to a scalar
→ **degenerate → Q=1/3** (verified). So Q=2/3 requires onsite-locality acting on the *source* but **withheld
from the operator** — an asymmetry nothing native justifies. **Applied consistently, onsite-locality destroys
the masses (Q=1/3); it does not select Q=2/3.**

## Consequence — the onsite-source line is weaker than it appeared
The "Q=2/3 = onsite-physical, Q=1 = off-site shadow" picture (PR #2442) is not wrong as algebra, but its
physical force depends on (i) reading on the Brannen carrier (where z=0 is re-centered to r=1/2) and (ii) an
unjustified source/operator asymmetry. **Locality is therefore not a selector for Q=2/3** — it joins symmetry
(generation-blind / forbidden) and positivity (agnostic) as a principle that does **not** natively pick the value.

## Honest standing of the charged-lepton value (consolidated standing)
Every native selector class tested so far has not been shown to force Q=2/3 over Q=1:
- **Symmetry** — exhausted (lattice point group, projective/magnetic via `H²=0`, full O_h, algebra
  automorphisms, gauge U(1)s, idempotent U(1)): all generation-blind, inert, or the blocked chiral grading.
- **Measure/positivity** — agnostic (OS reflection positivity blind to complex-vs-real; Bargmann generation-blind).
- **Locality / onsite-source** — does not select it (consistent application gives Q=1/3; Q=2/3 needs an
  unjustified asymmetry; the substrate-necessity bridge's vehicles assume rather than derive locality).

So the campaign's defensible endpoint stands and is reinforced: **the framework derives all of
charged-lepton flavor (3 generations, C₃, the circulant operator, emergent time, the signed/Hermitian readout,
the exact identity `Q=1/3+(2/3)r`, and `J_cs` forced by Schur) EXCEPT one reality/statistics bit — the
complex-vs-real (det_C/block vs det_R/dimension) counting of the doublet — and no native principle (symmetry,
positivity, or locality) selects it.** `Q=2/3` is the *natural* reading (block / K₀-real / coherent-state),
the more faithful reading of "a qubit at each site," and requires no new axiom — but it is not *forced*, and
the competing Q=1 reading is at least as motivated by the off-diagonal location of the mass operator itself.

## Next paths (live, not closed)
No native principle in the three classes tested selects the value; what remains genuinely open is upstream
of them: (i) the statistics-selection gap `G3` (fermionic-vs-bosonic = real-vs-complex = the *same* bit) — but
note this build shows locality does not resolve it; (ii) a genuinely new structural primitive, which would be
an import requiring user approval + audit. Honest assessment: this is the consolidation of the value campaign's current standing for the
value campaign.

## Stale-citation flags
- `single_axiom_hilbert_note` = audited_renaming, `single_axiom_information_note` = meta/unaudited (both ASSUME
  locality); `koide_q_onsite_source_domain_no_go_synthesis` = retained_no_go ("retention law still missing");
  `koide_q_source_domain_canonical_descent` / `koide_q_op_locality_source_domain_closure` = unaudited;
  `physical_lattice_necessity §9` narrowed out of load-bearing.
