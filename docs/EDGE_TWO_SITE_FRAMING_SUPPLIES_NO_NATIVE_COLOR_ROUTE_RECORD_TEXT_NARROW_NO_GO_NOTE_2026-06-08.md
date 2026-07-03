# Edge/Two-Site Framing Supplies No Native Color Route — and the Record Axiom Has No Cross-Site Clause

**Date:** 2026-06-08
**Type:** narrow no-go (route-demote) + a canonical-text correction
**Claim type:** no_go
**Script:** `scripts/frontier_edge_two_site_framing_no_native_color_route_record_text_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_edge_two_site_framing_no_native_color_route_record_text_2026_06_08.txt`
**Status:** source proposal. The finite checks and text audit run against the live authority
file (runner `PASS=12 FAIL=0`). Authority role: source proposal; audit lane sets status.

## The route under demotion

Several ADM-1 (local color-frame redundancy) discharge attempts framed the problem at the
**edge/two-site** level: *"the link/two-site structure — e.g. the native SWAP between
neighbour qubits, or a two-endpoint dressing — supplies the color/cross-site structure, and
the Record axiom's 'supplies no cross-site identification' clause makes the frame
unregistered."* The ADM-1 find-the-escape panel (`forced_finding`) refuted this framing on
exact grounds, **including a text error about the axiom itself**. This note records the
demotion.

## The grounds (runner `PASS=12 FAIL=0`)

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

**(G-C) The Record axiom has no cross-site clause (canonical-text correction).** The live
authority [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md) states durable
registration of the realized outcome in a supplied readout context, identifies the realized
outcome as a `K`/CPT orbit of the realized central sector, gives finite scalar additivity,
and explicitly disclaims the readout context, decomposition, `K`/CPT structure, weighting,
probability, dynamics, within-sector data, and occupancy rule. The runner's structural text
audit verifies these current clauses and that **no "cross-site" clause exists anywhere in
the text**. Routes that leaned on a *"supplies no cross-site identification"* paraphrase
were **importing structure the axiom does not contain** — in either direction (neither
supplying nor forbidding cross-site identification is the axiom's content).

## Honest residuals (what this does NOT foreclose)

- **Supplied-carrier models are untouched.** The
  [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  is an honest *bounded model* (its link-end carrier is declared supplied) and is not
  affected; this note demotes only the claim that the edge framing is **native**.
- **ADM-1 and the gauging-selection gate stay open** — this prunes one framing, not all
  possible carrier or dynamics routes.
- A future retained theorem deriving genuine cross-site structure from the axioms would
  re-open the framing; the demotion is scoped to the current surface.
- The matter-bilinear link-carrier construction (PR #3398) is a *different* route
  (conditional on the supplied `C³` carrier, no edge DOF) and is unaffected.

## No-Go Discipline Gate

**Result:** PASS for the narrowed route-demotion only. This is not a universal no-go for
ADM-1, gauging, supplied carriers, or future cross-site derivations.

**N1 — Alternative route enumeration.**

| Route | Test / status | Why it does not close native edge/two-site color |
|---|---|---|
| Native two-site SWAP | ATTEMPTED, runner G-A | SWAP commutes with all `g⊗g` by the swap identity and carries no internal direction, phase, or holonomy. |
| Single-qubit link algebra | RULED OUT BY PRIOR | The qubit-link boundary gives only `u(2)` at the link, below faithful `su(3)` dimension. |
| Register-not-read partition on an irreducible color triplet | ATTEMPTED, runner G-B | The only central partition is trivial by Schur; it registers the framed link, not the Ad-class. |
| Ad-class / trace extraction | ATTEMPTED, runner G-B | It requires the continuous Haar average `U -> (Tr U/N_c)I`, a supplied generator, not Record alone. |
| Record cross-site paraphrase | ATTEMPTED, runner G-C | Current Record text has no cross-site clause; the paraphrase supplies neither a permission nor a prohibition. |
| Supplied two-endpoint carrier | RULED OUT BY CLAIM SCOPE; open otherwise | It may be a bounded supplied-carrier model, but then the carrier is admitted rather than native to edge framing. |
| Matter-bilinear link-carrier route | RULED OUT BY CLAIM SCOPE; open otherwise | It is a separate route conditional on a supplied `C^3` color carrier, not the native two-site SWAP/edge route. |

**N2 — Wall-independence audit.** The collapsed wall is one route-demotion: native
edge/two-site structure does not supply color. The text correction is not a second physics
wall; it prevents a stale Record paraphrase from being used in either direction.

**N3 — Hidden-wall scan.** "Native" means no supplied carrier, no supplied continuous group
average, and no supplied gauge dynamics. "Record" means the current 2026-06-05 durable
realized-outcome axiom. The supplied-carrier and dynamics routes are explicitly left open.

**N4 — Residual matching.** The qubit-link boundary is used only for the one-qubit link
dimension check. The Record semigroup/generator boundaries are used only for the claim that
Record does not supply a continuous averaging generator. The two-endpoint and matter-bilinear
routes are named only as unaffected alternatives.

**N5 — Rhetoric audit.** The negative result is at the edge/two-site/native-link resolution.
It does not claim no color route exists on larger carriers, supplied endpoint models,
matter-bilinear constructions, or future dynamics.

**N6 — Partial-closure path scan.** A future derivation or owner-approved import of a
cross-site carrier, gauge-link dynamics, or channel/selection rule could close the broader
ADM-1 residual. The current Lattice + Quantum + Record baseline and approved primitives do
not supply that content.

**N7 — Steelman.** A hostile reviewer would bypass native edge framing entirely: supply a
two-endpoint carrier, use a matter bilinear carrying `C^3`, or derive an actual gauge-link
dynamics. That does not break this note; it confirms the narrowed demotion of the native
edge/two-site route.

**N8 — Cross-cycle echo.** Similar route-demotions in the current interacting queue warn
against treating a failed shortcut as a global no-go. This note follows that pattern by
landing only the finite algebra/text correction and keeping the carrier/dynamics gates open.

## Forbidden-imports check

No PDG value, fitted number, new axiom, primitive, Tier-A admission, or new framing is
consumed. SWAP algebra, Schur's lemma, and the Haar average are standard math; the runner
checks the finite identities, a numerical Haar projection, and the live authority text.

## Cross-references

- The canonical axiom text (text-checked): [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md)
- The qubit-link boundary (restated): [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
- The record boundaries (retained): [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md), [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
- The honest supplied-carrier model (untouched): [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- Sister route-demote (the `kappa_EW` weight-leak): [`FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08`](FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08.md)
- Standard math (method only): SWAP/permutation algebra; Schur's lemma; Haar average.
