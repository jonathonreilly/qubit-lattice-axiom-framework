# The Fierz Singlet-Channel Selector Is a Weight, Not a Partition — the Register-Not-Read κ_EW=0 Route Demoted

**Date:** 2026-06-08
**Type:** narrow no-go (route-demote) — prunes ONE proposed closure route; the gate stays open
**Claim type:** no_go
**Script:** `scripts/frontier_fierz_singlet_selector_weight_not_partition_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_fierz_singlet_selector_weight_not_partition_2026_06_08.txt`
**Status:** source proposal. The load-bearing route grounds are finite linear
algebra (runner `PASS=14 FAIL=0`, including one deterministic Monte Carlo
sanity check of the Haar-twirl reading). Authority role: source proposal;
audit lane sets status.

## The route under demotion

The EW matching rule leaves the one-parameter family `R(κ_EW) = F_adj + κ_EW(1−F_adj)`,
`F_adj = (N_c²−1)/N_c² = 8/9` — the **existing** `retained_no_go` family
([`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md),
[`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md))
establishes the retained packet does not select `κ_EW`. A subsequently proposed route —
recorded as a gate in
[`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md)
(live status `audited_conditional`) — would set `κ_EW = 0` by declaring the color-singlet
trace channel **unregistered** under the register-not-read discipline.

**This note demotes that route** (not the gate): the register-not-read move
does not apply to the channel split, on three finite-algebra route grounds.

## The Three Route-Demotion Grounds

**Twirl-vs-partition ground.** The channel split sends
`M → E_sing(M) = (Tr M/N_c)·I` — which is the **Haar/depolarizing twirl** `∫ U M U† dU`
(Ad-invariant, idempotent, unital; MC-confirmed). It is **not** of the form
`D(M) = Σ_k P_k M P_k` for any orthogonal partition: partition maps preserve each diagonal
block verbatim, the twirl replaces them by their average; and on the SU(3)-**irreducible**
triplet the only central-sector symmetry-respecting partition is the trivial
`{I}` (Schur: the only central projectors are `{0, I}`), whose
`D = identity ≠ twirl`. So the **genuine**
register-not-read license — the central-sector partition map of
`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE` under the central-sector partition-map
guardrail — does not cover the channel split. Invoking register-not-read here
is the **loose** dichotomy demoted by
[`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06`](REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md).

**Weight-leak ground.** The Fierz
**count** fraction `8/9` is fixed by the decomposition (a dimension count), but `κ_EW` is
the realized **weight** of the singlet channel, and the within-sector data
guardrail says a partition never delivers such a weight. The runner exhibits
the formal isomorphism: `R(κ)` is the same fixed-count/free-weight shape as the
Koide `r`-dial (two channels, counts fixed, realized weight free). *"Declare
the singlet unregistered ⟹ κ=0"* assigns a weight by fiat — structurally the
move that would force the **known-free** Koide `r` (the
scope-correction's directionless tell).

**Category-separation ground.**
The Fierz split decomposes the EW current's **same-site** color trace `Tr[G G†]`
(observable content / the matching rule `M`), which is invariant under local color
rotations; a gauge-link kernel co-transforms bi-fundamentally. Selecting `κ_EW` therefore
says nothing about the gauge-link/frame question (ADM-1), and vice versa — conflating them
was part of the refuted route.

## Honest residuals (what this does NOT foreclose)

- **The `κ_EW` gate itself remains OPEN.** Other routes (a framework-native lattice EW
  current with an explicit adjoint projector at the two-current insertion; an exact
  non-perturbative disconnected-current computation; an explicitly-approved matching
  convention) are **not** addressed here. This note prunes one route; it adds no closing
  language and presupposes no closeable route enumeration.
- **The exact Fierz algebra is untouched** (the `S+C` split and `F_adj = 8/9` are
  reproduced as setup; they are owned by `ew_current_fierz_channel_decomposition`, a
  decoration under the retained `graph_first_su3_integration_note`).
- **ADM-1 is untouched** (its `forced_finding` and open status stand independently).
- This note **sits beside** the existing `retained_no_go` family and the `rconn` gate
  note; it duplicates neither (the family establishes *underdetermination by the retained
  packet*; this note demotes the *register-not-read discharge* specifically).
- A future **retained** theorem genuinely deriving a registered partition for the color
  trace would re-open the route — the demotion is scoped to the current surface.

## No-Go Discipline Gate

Status: `PASS` for the route-demotion scope only. The claim is not a global
no-go for `κ_EW`; it only demotes the register-not-read color-trace route on
the current surface.

**N1 - Alternative routes against this demotion.**

| Route | Result | Marker |
|---|---|---|
| Treat the singlet channel map as the genuine central-sector partition map. | Fails: the runner checks that `E_sing(M)=(Tr M/N_c)I` is the twirl and not `Σ P_k M P_k`; the only symmetry-respecting central partition on the irreducible triplet is trivial and gives identity, not twirl. | ATTEMPTED |
| Pick a non-symmetric color-basis partition to isolate the trace channel. | Fails: such projectors do not commute with the irreducible SU(3) action, so they are not a valid central-sector readout partition. | ATTEMPTED |
| Declare the singlet unregistered and set `κ_EW=0`. | Fails: that assigns a within-channel weight, while the partition license gives sectors/counts and forbids weight selection; the same move would force the known-free Koide `r` dial. | ATTEMPTED |
| Reinterpret the same-site Fierz trace as the ADM-1 gauge-link/frame kernel. | Fails: the runner separates the local trace object, which is invariant at one site, from a link kernel, which co-transforms between sites. | ATTEMPTED |
| Use the prior retained no-go family or the `rconn` open-gate packet as closure authority. | Fails: the retained family shows underdetermination by the retained packet, and the `rconn` packet explicitly records a missing theorem. | RULED OUT BY PRIOR |
| Supply a future retained color-trace readout theorem, matching convention, or owner-approved admission. | Open but outside this demotion. It could re-open the `κ_EW` gate; it is not supplied by this route. | OPEN |

**N2 - Wall independence.** The collapsed wall set has one wall for this route:
register-not-read does not supply the color-trace weight selector. The
twirl/partition, weight-leak, and category-separation checks are independent
diagnostics of that one route failure, not three independent global walls.

**N3 - Hidden-wall scan.** "Central," "registered," and "standard math" are
non-load-bearing labels unless backed by the displayed finite linear algebra.
Schur/centrality, the Fierz decomposition, and the twirl identities are
checked directly or used only as standard method language. No PDG value,
empirical fit, new axiom, new primitive, or Tier-A admission is load-bearing.

**N4 - Residual matching.** The scope-correction note is the matching witness:
it attacks loose register-not-read applications that would assign weights by
fiat. The retained `κ_EW` no-go family and the `rconn` open gate are context
only: their residual is underdetermination/open theorem, not this specific
route demotion.

**N5 - Rhetoric audit.** "Not a partition map" is scoped to the singlet-channel
linear map on the color matrix. "Says nothing about ADM-1" is scoped to the
same-site trace versus link-kernel category distinction. The note does not say
no `κ_EW` selector exists, no color-trace theorem can be retained, or ADM-1 is
closed.

**N6 - Partial-closure scan.** The legitimate closure paths remain open: a
future retained theorem, explicit matching convention, owner-approved
admission, or registry update could supply the missing color-trace readout
selector. Approved axioms and primitives do not supply that selector by
themselves.

**N7 - Steelman.** A hostile reviewer could argue that a future readout context
might make the color trace a genuine central-sector decomposition and identify
the singlet as unregistered reference content. That would defeat a broad
`κ_EW` no-go, but it is precisely extra theorem/admission content and therefore
does not rescue the current register-not-read route.

**N8 - Cross-cycle echo.** The register-not-read scope correction shows that
loose "registered physical, not reconstruction" applications have been retired
by narrowing them back to the central-sector partition-map license. The same
governance/reframe mechanism could later re-open `κ_EW` through an explicit
new readout theorem or admission, so this note keeps the gate open.

## Forbidden-imports check

No PDG value, fitted number, new axiom, or new framing is consumed. The Gell-Mann basis,
Schur's lemma, the Haar twirl, and the conditional-expectation identities are standard
math reproven in the runner. All cited statuses verified on the live `origin/main` ledger
(2026-06-08): the matching-rule and traceless-selector notes `retained_no_go`; the Fierz
decomposition note `decoration` under `graph_first_su3_integration_note` (`retained`); the
`rconn` note `audited_conditional`; the scope-correction `meta`.

## Cross-references

- The route's source (gate, stays open): [`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md)
- The existing family (beside, not duplicated): [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md), [`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md)
- The demoted loose form: [`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06`](REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md)
- The exact Fierz algebra (setup): [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
- Standard math (method only): Schur's lemma; Haar/depolarizing twirl; conditional expectations.
