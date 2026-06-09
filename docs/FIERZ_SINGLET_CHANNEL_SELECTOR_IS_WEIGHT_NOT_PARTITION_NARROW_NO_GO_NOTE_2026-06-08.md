# The Fierz Singlet-Channel Selector Is a Weight, Not a Partition — the Register-Not-Read κ_EW=0 Route Demoted

**Date:** 2026-06-08
**Type:** narrow no-go (route-demote) — prunes ONE proposed closure route; the gate stays open
**Claim type:** no_go
**Script:** `scripts/frontier_fierz_singlet_selector_weight_not_partition_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_fierz_singlet_selector_weight_not_partition_2026_06_08.txt`
**Status:** source proposal. The three grounds are exact finite algebra (runner `PASS=14
FAIL=0`); the route assessment was independently recomputed by an adversarial panel before
this note was written. Authority role: source proposal; audit lane sets status.

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

**This note demotes that route** (not the gate): the register-not-read move does not apply
to the channel split, on three exact grounds.

## The three grounds (each exact — runner `PASS=14 FAIL=0`)

**(G-A) The singlet projector is a twirl, not a partition map.** The channel split sends
`M → E_sing(M) = (Tr M/N_c)·I` — which is the **Haar/depolarizing twirl** `∫ U M U† dU`
(Ad-invariant, idempotent, unital; MC-confirmed). It is **not** of the form
`D(M) = Σ_k P_k M P_k` for any orthogonal partition: partition maps preserve each diagonal
block verbatim, the twirl replaces them by their average; and on the SU(3)-**irreducible**
triplet the only G1-compliant (symmetry-respecting) partition is the trivial `{I}` (Schur:
the only central projectors are `{0, I}`), whose `D = identity ≠ twirl`. So the **genuine**
register-not-read license — the central-sector partition map of
`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE` under guardrail G1 — does not cover the channel
split. Invoking register-not-read here is the **loose** dichotomy demoted by
[`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06`](REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md).

**(G-B) κ_EW is a within-channel weight — the r-dial move (weight-leak).** The Fierz
**count** fraction `8/9` is fixed by the decomposition (a dimension count), but `κ_EW` is
the realized **weight** of the singlet channel — exactly the within-sector data guardrail
G3 says a partition never delivers. The runner exhibits the formal isomorphism: `R(κ)` is
the same fixed-count/free-weight shape as the Koide `r`-dial (two channels, counts fixed,
realized weight free). *"Declare the singlet unregistered ⟹ κ=0"* assigns a weight by fiat
— structurally the move that would force the **known-free** Koide `r` (the
scope-correction's directionless tell).

**(G-C) Category: the channel lives on the same-site current trace, not the gauge link.**
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
