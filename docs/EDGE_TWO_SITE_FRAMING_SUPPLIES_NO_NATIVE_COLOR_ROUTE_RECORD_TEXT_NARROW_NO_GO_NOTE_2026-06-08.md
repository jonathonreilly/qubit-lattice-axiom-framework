# Edge/Two-Site Framing Supplies No Native Color Route — and the RECORD Axiom Has No Cross-Site Clause

**Date:** 2026-06-08
**Type:** narrow no-go (route-demote) + a canonical-text correction
**Claim type:** no_go
**Script:** `scripts/frontier_edge_two_site_framing_no_native_color_route_record_text_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_edge_two_site_framing_no_native_color_route_record_text_2026_06_08.txt`
**Status:** source proposal. The algebra is exact and the text audit is against the live
authority file (runner `PASS=11 FAIL=0`); the route assessment was independently recomputed
by an adversarial panel before this note was written. Authority role: source proposal;
audit lane sets status.

## The route under demotion

Several ADM-1 (local color-frame redundancy) discharge attempts framed the problem at the
**edge/two-site** level: *"the link/two-site structure — e.g. the native SWAP between
neighbour qubits, or a two-endpoint dressing — supplies the color/cross-site structure, and
the RECORD axiom's 'supplies no cross-site identification' clause makes the frame
unregistered."* The ADM-1 find-the-escape panel (`forced_finding`) refuted this framing on
exact grounds, **including a text error about the axiom itself**. This note records the
demotion.

## The grounds (runner `PASS=11 FAIL=0`)

**(G-A) The native two-site operation is color-blind.** The qubit-native two-site primitive
`SWAP` on `C²⊗C²` commutes with **every** diagonal rotation `g⊗g` (to `10⁻¹⁷`) — it is a
**real permutation** (`SWAP=SWAP*=SWAPᵀ`, `SWAP²=I`) carrying no internal direction, no
phase/holonomy data. And a single qubit link natively carries only `u(2)` (`dim 4 < 8 =
dim su(3)`) — the
[`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
boundary, restated. **Pre-gauging, the edge supplies symmetric (color-blind) structure
only.**

**(G-B) Extracting Ad-class content needs a supplied continuous average (the collapse).**
On the irreducible color triplet the genuine register-not-read partition map is trivial
(`D(U)=U`; Schur — only `{0,I}` are central), so the record registers the **framed** link,
never the Ad-class. Recovering the gauge-invariant class/trace content `U → (TrU/N_c)I` is
the **Haar average** — a *continuous group integral* = a **supplied generator**, exactly
what the retained record boundaries
([`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md),
[`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md))
say Record alone does not provide. **The edge/two-site framing therefore collapses into the
same supplied-carrier / color-trace gate; it does not bypass it.**

**(G-C) The RECORD axiom has no cross-site clause (canonical-text correction).** The live
authority [`MINIMAL_AXIOMS_2026-06-04`](MINIMAL_AXIOMS_2026-06-04.md) (which supersedes the
2026-05-20 wording) supplies **only** the additive scalar readout
`I(R_1 ⊔ R_2) = I(R_1) + I(R_2)` and explicitly **disclaims** composition and arbitrary
observable identification; the runner's structural text audit verifies the additive law,
the disclaimers, and that **no "cross-site" clause exists anywhere in the text**. Routes
that leaned on a *"supplies no cross-site identification"* paraphrase were **importing
structure the axiom does not contain** — in either direction (neither supplying nor
forbidding cross-site identification is the axiom's content).

## Honest residuals (what this does NOT foreclose)

- **Supplied-carrier models are untouched.** The
  [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  is an honest *bounded model* (its link-end carrier is declared supplied) and is not
  affected; this note demotes only the claim that the edge framing is **native**.
- **ADM-1 and the gauging-selection gate stay open** — this prunes one framing, it closes
  nothing; no closing language; no route enumeration is presupposed.
- A future retained theorem deriving genuine cross-site structure from the axioms would
  re-open the framing; the demotion is scoped to the current surface.
- The matter-bilinear link-carrier construction (PR #3398) is a *different* route
  (conditional on the supplied `C³` carrier, no edge DOF) and is unaffected.

## Forbidden-imports check

No PDG value, fitted number, new axiom, or new framing is consumed. SWAP algebra, Schur's
lemma, and the Haar average are standard math reproven in the runner; the text audit reads
the live authority file (precedent: the repo's note-text scope-split audit runners).

## Cross-references

- The canonical axiom text (audited verbatim): [`MINIMAL_AXIOMS_2026-06-04`](MINIMAL_AXIOMS_2026-06-04.md)
- The qubit-link boundary (restated): [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
- The record boundaries (retained): [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md), [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
- The honest supplied-carrier model (untouched): [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- Sister route-demote (the κ_EW weight-leak): `FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08` (PR #3405)
- Standard math (method only): SWAP/permutation algebra; Schur's lemma; Haar average.
