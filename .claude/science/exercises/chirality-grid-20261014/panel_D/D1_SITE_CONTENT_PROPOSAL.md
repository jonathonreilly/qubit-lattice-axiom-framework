# Proposal draft: re-scope deferred decision #4 as "site content for all lanes" (NOT ADOPTED)

**Status.** A draft for the owner only. Nothing here is adopted, and the deferred-decision registry on main is **not** edited by this file. It comes from panel D, 2026-10-14: the skeptic's next action and the qinfo panelist's D1 recommendation, with the COL-1 question added at Jon's request.

## Why #4 is woken

`docs/repo/DEFERRED_DECISIONS.md:139-142` (on main) gives wake condition 1: "the chirality/generation program resumes, or a C222-class site-algebra extension becomes load-bearing." The chirality exercise (PR #9562, transferred to J tasks; this branch is retained) fires that condition literally (K3).

## Re-scope

The original question was "M₂(C) → M₄(C) for γ5". Within its stated class, Lemma R makes that motivation moot: the number of states per site does not change the zero net-chirality result.

The live question is broader and is shared by every lane: **how much state lives at, or is spread around, each grid point, and is it finite?**

## Today's over-budget, stated honestly (counted once; supplied, not derived)

| Lane | What it uses per site or cell | Source |
|---|---|---|
| Gravity root (C5) | ≥ 90 fermion modes on one edge (22.5 Dirac fields) | gravity packet, panel F synthesis :51-52 |
| Supplied graviton | conflicts with one M₂(C) per site (P-N1) | gravity SUMMARY :777 |
| Qubit-built graviton (estimate) | ~30–2000 qubits per cell | gravity PRICE_NOTE :602 (worker) |
| Chirality, corner package (X2) | 32 complex modes | X2 COMBO_REPORT :212 (skeptic correction) |
| Chirality, inflow slab (F4/X1) | ~10³ | F4 :153-164 |
| Chirality, finite-n overlap | ~60 auxiliary Dirac fields per physical field | F2 :157-160 |
| Chirality, exact overlap in real time | infinite fibre | X3-C (co-occurs; referee) |
| Colour with exact on-site SU(3) | ≥ 16 fermion modes per gauge cell, handed or not | qinfo panelist; COL-1 is testing whether a cell can be spread over single qubits |

## Proposed re-park (for the owner to accept or edit)

- **Standing default:** M₂(C) per site stands as written. Record "SM matter (colour, weak force, chirality) is not realized under the axioms as written" as **today's status**, not as policy.
- **One wake condition, gated on both of the following:**
  - (i) a route passes its decisive, pre-registered test at a stated per-site (or per-cell) count; **and**
  - (ii) a one-sentence layman reason survives a blind check.
- **Candidate sentence, for the record only (not adopted).** *"Three generations because space has three directions; sixteen slots per point because sixteen is the smallest bundle whose mirror can be hidden."* Its testable consequence: CKM mixing forces a preferred strain direction (X2-L8). OBS-1 is sizing that now.
- **Decide jointly with:** whether local domains are finite (matter, gauge links, graviton). Two landed notes read the axiom as one fermion mode per site and would need re-scoping if a register is adopted (qinfo panelist):
  - `docs/STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md:41-54`;
  - `docs/STAGGERED_DIRAC_KINETIC_CLASS_TWO_COMPONENT_EXCLUSION_NARROW_THEOREM_NOTE_2026-06-11.md`.

## What COL-1 can change

- If colour can live on single qubits under a twisted translation (COLOUR-SPREAD-OK), the cell count stays but the translation price of "blocks" disappears.
- If blocks are forced (COLOUR-BLOCK-FORCED), D1(a) carries the AX:37/57 price (P183).
- If only emergent colour survives, D1 hinges on an emergent non-abelian gauge construction that nobody has built in 3+1D.
