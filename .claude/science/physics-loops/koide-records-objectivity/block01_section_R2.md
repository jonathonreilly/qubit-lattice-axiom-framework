# Block01 Section R2 — Objectivity Selector: Derive From Record, or Named Premise?

**Date:** 2026-06-20
**Route:** R2 (objectivity selector — the hard residual)
**Branch:** physics-loop/koide-records-objectivity-block01-20260620
**Runner:** `scripts/frontier_koide_objectivity_selector_record_derivation_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_koide_objectivity_selector_record_derivation_2026_06_20.txt`
**Runner result:** TOTAL: PASS=15 FAIL=0 (exit 0)
**Outcome:** NAMED-PREMISE SPLIT — the objectivity-maximization selector is NOT
derived from Record; it is a separate admitted readout-context choice. r and Q
remain OUTPUTS conditional on that admitted selector.

---

## Task

Attempt to DERIVE input (2) of `KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`
— the records/objectivity maximization selector (that the physical readout
criterion is objectivity / redundancy / spectrum-broadcast-structure maximization
over the K/CPT sector readout, uniquely selecting the determinant-symmetric point
r=1/2) — from the framework baseline {Lattice, Quantum, Record} + the four approved
primitives. Build the SBS / quantum-Darwinism objectivity functional over the
readout and test whether MAXIMIZING it selects r=1/2 WITHOUT assuming equal sector
weights. Honest target: is objectivity-maximization a derived consequence of Record,
or a separate admitted readout-context choice (the readout-context bridge A_min may
withhold — the same wall as T1-d observable_principle)?

## Method (all real computation; no headline-mining)

The runner builds the objects, it does not import verdicts:

- **Sector alphabet + weight↔r map (S1).** K/CPT (≈ conjugation on C3 irrep labels)
  gives exactly two orbits: singlet {1} (rank 1) and doublet {ω, ω̄} (rank 2) — a
  2-symbol objective alphabet. Signed-readout block energies E_+ = 3a², E_perp = 6|b|²
  give the doublet share p_perp = 2r/(1+2r), singlet share p_+ = 1/(1+2r), a 1-1
  reparametrization of r by the sector weight. Determinant-symmetric point r=1/2 ⟺
  E_+ = E_perp ⟺ uniform weight (1/2,1/2); dimension/Born weight (1/3,2/3) ⟺ r=1.
- **SBS objectivity functional, swept over weights (S2).** Build the ideal
  spectrum-broadcast state ρ = Σ_i p_i |i⟩⟨i|_S ⊗ ρ_{E1,i} ⊗ … ⊗ ρ_{EN,i} on the
  2-symbol alphabet over N=4 environment fragments, per-sector fragment states
  orthogonal (ideal objective broadcast). Compute, via exact numpy partial traces +
  von Neumann / mutual information, the per-fragment recovered information I(S:E1) and
  the two-fragment value I(S:E1E2) (redundancy plateau) for weights (1/2,1/2),
  (1/3,2/3), (0.2,0.8), (0.9,0.1).
- **What peaks at r=1/2 (S3).** sympy extremum of the plateau value H(p(r)); plus a
  weight-independence check on the redundancy MULTIPLICITY (number of fragments
  carrying the record).
- **Supplier check (S4).** Record additivity blindness to weight; the realized-state
  primitive's counterfactual/ban-on-typical clauses; the minimal_axioms node text.
- **Comparator (S5).** The Record-invariant tracial reference I/3 → (1/3,2/3) → r=1.

## Findings (the residuals)

**RESIDUAL-1 — objectivity is WEIGHT-BLIND (S2, the central wall).** For EVERY weight
the SBS objectivity is FULL: each single fragment recovers I(S:E1) = H(p) exactly, and
a second fragment adds nothing (I(S:E1E2) = I(S:E1), the redundancy plateau). Verified
at p = (1/2,1/2), (1/3,2/3), (0.2,0.8), (0.9,0.1). The objectivity / redundant-broadcast
PROPERTY therefore holds at r=1/2, at r=1, and at every interior r — it fixes the sector
BASIS/alphabet, not the weight, hence does not select r. This independently reproduces
`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md` by direct construction.

**RESIDUAL-2 — the r=1/2-selecting functional is H(weights), an INDIFFERENCE rule, not
redundancy (S3).** The only functional that peaks at r=1/2 is the plateau VALUE H(p(r))
(= argmax r=1/2, value log 2 = 1 bit, d²/dr² = −1 < 0). But H(p) is the recovered-info
content = the Shannon entropy of the supplied weights; maximizing it is the max-entropy /
equal-a-priori (indifference) rule over sector LABELS, not a broadcast property. The
genuine Darwinism objectivity observable — the redundancy MULTIPLICITY (how many fragments
carry the record) — is weight-INDEPENDENT in ideal SBS (constant 4 across all weights) and
does NOT peak at uniform. So "objectivity-maximization → r=1/2" decomposes cleanly:
(broadcast objectivity: weight-blind) + (maximize Shannon entropy of the readout weights:
a SEPARATE indifference selector). The r=1/2-selecting half is the indifference half.

**RESIDUAL-3 — Record + the four primitives supply no such weight (S4–S5).** Record's
finite additive scalar I is blind to the weight (relabelled disjoint records give identical
I; I(∅)=0). The realized_state_primitive bans "typical/generic" weighting and averaging,
and the counterfactual test marks any weight-contingent r as registered DATA, not derivation.
The minimal_axioms node states Record supplies no readout context / weighting / normalization
/ probability. This reproduces `DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md`:
SBS objectivity (local observability of a determined outcome) is itself a NAMED open premise
over {Lattice, Quantum, Record}. Comparator: the Record-invariant tracial reference I/3 is
U(3)-invariant and gives (1/3,2/3) → r=1 — a DIFFERENT point — so the uniform weight is a
genuine choice and the dephasing/tracial fixed point points to r=1 (matches the conditional
note's F4).

## Verdict

R2 does NOT close. Two independent reasons, both computed:

1. Objectivity / SBS broadcast over the K/CPT sector alphabet is **weight-blind** — full
   for every r — so even granting it, it fixes the sector BASIS, not r=1/2.
2. The functional that actually selects r=1/2 is **H(readout weights)**, a maximum-Shannon-
   entropy / indifference (equal-a-priori) rule over the sector LABELS. That is NOT
   redundancy/objectivity, and it is NOT supplied by Record additivity/determinacy nor by any
   of the four primitives (which explicitly supply no measure/weight/probability).

Moreover SBS objectivity is itself an open local-observability bridge over the axioms. So the
records/objectivity maximization selector is a **separate admitted readout-context choice** —
precisely the readout-context bridge A_min withholds (the same wall as T1-d observable_principle).

**Characterization of the precise missing premise:** to select r=1/2 the framework needs a
**maximum-entropy / equal-a-priori indifference selector over the two K/CPT sector labels**
(equivalently: read the sectors by atom/share count, not by dimension/Born), supplied ON TOP
of an SBS-objectivity readout context. Both halves are outside {Lattice, Quantum, Record} +
the four primitives. The conditional note's row stays conditional, not unconditional retained.

## Effect on the conditional note row

No flip. R2 sharpens input (2) from "objectivity maximization selector" to a two-part named
premise: (a) an SBS / local-observability readout-context bridge (itself open per the Darwinism
gate), and (b) a max-entropy/indifference selector over sector labels. This does not remove the
boundary; it names it precisely. No new axiom/primitive introduced; audit lane is the sole
status authority.
