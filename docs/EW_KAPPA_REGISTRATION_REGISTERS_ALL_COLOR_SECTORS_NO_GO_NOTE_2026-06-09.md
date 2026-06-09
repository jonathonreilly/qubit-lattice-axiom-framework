# Register-not-read does NOT fix kappa_EW: it registers all color sectors

**Date:** 2026-06-09
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict; effective status is pipeline-derived after
independent audit.
**Primary runner:**
[`scripts/frontier_ew_kappa_registration_color_sector_nogo.py`](../scripts/frontier_ew_kappa_registration_color_sector_nogo.py)
(`RUNNER STATUS: PASS (PASS=12 FAIL=0)`, zero PDG/experimental inputs).

## Summary

The only framework-native reopen route for the EW color-readout coefficient
`kappa_EW` is recorded as an **open gate** in
[`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md)
(`unaudited`, `open_gate`):

> If a future retained theorem proves that the register-not-read discipline
> governs the color operator-trace channel, then the registered channel is the
> traceless connected channel and `kappa_EW = 0`.

**This note proves the antecedent fails, as a no-go**, by the identical machinery
the retained no-go
[`REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07`](REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07.md)
used for Koide chirality. The canonical record map
`D(rho) = sum_k P_k rho P_k` registers the content of **every** central sector and
removes only inter-sector coherence. The color singlet `S = (1/N_c)|Tr G|^2` is
the **trivial irrep** of the SU(`N_c`) adjoint action — the most central sector —
so it is **registered, never annihilated**. Registration therefore **keeps** the
singlet population; it does not drop it (`kappa_EW = 0`).

`kappa_EW` is the **inter-sector weight** in the readout `Pi_phys = C + kappa_EW S`.
The central-sector partition delivers the per-sector contents `{S, C}` and the mode
**count** (the `(N_c^2-1)/N_c^2 = 8/9` cardinality fraction) but **not** that
weight — exactly as it delivers the Koide block counts while leaving the
within-block weight `r` free. By the same structure that makes registration
"constrain `r` not at all," it **constrains `kappa_EW` not at all**.

The `kappa_EW = 0` route (treat the singlet trace as "an unregistered reference"
and drop it) is the **loose registration-vs-reconstruction dichotomy** that the
[`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06`](REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md)
demoted: it is **directionless** (the physical W/Z/gamma **is** a color singlet,
so the same slogan equally registers the singlet and drops the confined adjoint),
and — per
[`EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08`](EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08.md)
— `kappa_EW` is a continuum renormalization-**scheme** weight, which the panel's
A4 verdict identifies as exactly the kind of object register-not-read may not fix
("einselection fixes pointer bases, not schemes").

**This note does not force `kappa_EW = 1` and does not fabricate `kappa_EW = 0`.**
It shows register-not-read leaves `kappa_EW` undetermined, consistent with the
MC-undecidability and matching-rule no-gos.

## Setup

The EW current correlator's color readout is the `q`-`qbar` matrix
`G in End(C^{N_c})`, decomposed by the SU(`N_c`) Fierz/sector projectors into the
trivial (singlet) and adjoint irreps:

```text
G = P_1(G) + P_adj(G),   P_1(G) = (Tr G / N_c) I,   P_adj(G) = G - P_1(G),
S = ||P_1(G)||^2 = (1/N_c)|Tr G|^2,   C = ||P_adj(G)||^2,   S + C = Tr[G G^dag].
```

`{P_1, P_adj}` is the central-sector partition of `End(C^{N_c}) = 1 (+) adj`. The
canonical record principle
([`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md))
registers the central-sector content via `D(rho) = sum_k P_k rho P_k`
(which-sector + sector populations + counts; inter-sector coherence not recorded).
The named coefficient is
`R_phys(kappa_EW) = F_adj + kappa_EW(1 - F_adj)`, `Pi_phys = C + kappa_EW S`,
with `kappa_EW = 0 -> 8/9` and `kappa_EW = 1 -> 1`
([`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md),
[`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md)).

## Theorem (no-go)

**(T1) The singlet is the trivial irrep — a genuine central sector.** `P_1` is
SU(`N_c`)-equivariant: `P_1(U G U^dag) = U P_1(G) U^dag` (the singlet subspace is
invariant under the adjoint action). It is the most central content, never
sector-off-diagonal (runner §B1).

**(T2) Registration keeps every central sector's population.** In the sector basis
`{|singlet>, |adjoint>}` the readout state is `rho = [[S, x], [x*, C]]`; the record
map dephases, `D(rho) = diag(S, C)`. It keeps **both** populations `S` and `C` and
removes only the inter-sector coherence `x` (runner §B2). The registered readout
therefore contains `S` **and** `C`.

**(T3) Registration never drops the singlet.** A registration-based *derivation* of
`kappa_EW = 0` would require the map `rho -> diag(0, C)` — **discarding** the
registered singlet population `S`. That is **not** the record map `D` (which keeps
`S`); discarding a registered diagonal outcome is not a dephasing/record operation
(runner §B3). (`kappa_EW = 0` remains an admissible *external* scheme readout — see
the MC-undecidability no-go — it simply is not *derived* by register-not-read.) What `D` annihilates is
the off-diagonal coherence `x`, the analog of a grading-anticommuting carrier in the
chirality no-go — **not** the diagonal singlet population (runner §B4).

**(T4) `kappa_EW` is an inter-sector weight the partition does not deliver (the
`r`-dial).** Given the registered `{S, C}`, both `Pi_phys(kappa_EW = 0) = C` and
`Pi_phys(kappa_EW = 1) = C + S` are functions of the **same** data; the partition
delivers the **count** (the `8/9` cardinality fraction) but not the weight
`kappa_EW` (runner §C). This is the identical structure by which the Koide
character partition `{P_0, P_d}` delivers block counts while leaving the within-block
weight `r` free: `D(H) = H` for every circulant `H`, so `D` "constrains `r` not at
all" (runner §D; retained no-go REGISTRATION_REINSTATES_CHIRALITY). By the same
structure, `D` constrains `kappa_EW` not at all.

**(T5) The `kappa_EW = 0` route is the demoted, directionless loose dichotomy.**
Treating the singlet trace as "an unregistered reference" to drop it (`kappa_EW = 0`)
and treating the singlet as the physical W/Z color-singlet content to keep it (the
opposite direction) are the **same** register-not-read slogan pointed opposite ways
(runner §E) — the canonical retrofit signature the scope-correction panel flagged.
Per the MC-undecidability no-go, `kappa_EW` is a renormalization-scheme weight; the
panel's A4 verdict is that register-not-read may not relabel a scheme choice as a
registration.

**Consequence.** Register-not-read registers all central color sectors (keeps the
singlet), delivers the channel count but not the inter-sector weight, and the
singlet-drop is directionless. So it does **not** supply `kappa_EW = 0`; the reopen
route is closed. It does not supply `kappa_EW = 1` either — `kappa_EW` remains
undetermined, as the MC-undecidability and matching-rule no-gos already hold.

## No-Go Discipline (N1-N8)

**N1 — Alternative-route enumeration (>=5).**
1. *Drop the singlet via a finer color partition.* RULED OUT: any central-sector
   partition still registers the singlet diagonal population (T2-T3); finer
   partitions add sectors, never discard the trivial one.
2. *Coarsen to the trivial partition `{I}`.* RULED OUT: then the whole readout
   `Tr[G G^dag] = S + C` is registered (`kappa_EW = 1`), not `kappa_EW = 0`.
3. *Treat the singlet trace as a normalization reference (not content).* RULED OUT:
   `Tr[G G^dag]`'s singlet part `S` is a varying physical channel weight, not a fixed
   normalization; calling it a reference to drop it is the loose dichotomy (T5),
   directionless against the W/Z-is-a-color-singlet reading.
4. *Make the singlet sector-off-diagonal so `D` annihilates it.* RULED OUT: the
   singlet is the trivial irrep (T1); no central-sector partition makes it
   anticommute with the grading. (Contrast: the Koide `Q=2/3` carrier genuinely
   anticommutes and is annihilated — that mechanism does not transfer to a central
   sector.)
5. *Identify `kappa_EW` with the delivered count.* RULED OUT: the count is the
   `8/9` cardinality fraction `F_adj`; `K_EW(kappa_EW) = 1/(F_adj + kappa_EW/9)`
   still requires the separate weight `kappa_EW` (runner §C).
6. *ATTEMPTED-OPEN: a non-register-not-read selector (a retained lattice-current /
   continuum readout-functional theorem) fixes `kappa_EW`.* Not foreclosed here;
   this no-go is scoped to the register-not-read route only.

**N2 — Wall-independence.** Two distinct objects: (a) registration registers all
central sectors (T1-T3, pure algebra); (b) `kappa_EW` is an inter-sector weight not
delivered by any partition (T4). (a) is *why* register-not-read cannot drop the
singlet; (b) is *what stays open* (the weight). Neither follows from the other.

**N3 — Hidden-wall scan.** The proof uses only the canonical record map
`D(rho) = sum_k P_k rho P_k`, the SU(`N_c`) Fierz/sector projectors, and exact
linear algebra. The partition `{P_1, P_adj}` is an **explicit input**; no
"naturally / by construction / standard QFT" step is load-bearing, and the result is
partition-robust (N1.1-N1.2).

**N4 — Residual matching.** The residual (`kappa_EW` undetermined) matches the
MC-undecidability no-go's "`kappa_EW` is a continuum scheme weight external to the
ensemble" and the matching-rule no-go's "the selector is an extra premise," exactly.

**N5 — Rhetoric audit.** "Registration keeps the singlet" is verified at the irrep
level (T1), the dephasing level (T2-T4), and the contrast with the annihilated
coherence (B4). The claim is scoped to the register-not-read route; it does not say
"`kappa_EW` can never be fixed."

**N6 — Partial-closure scan.** No convention or relabeling closes the route: every
register-not-read shape either keeps the singlet (`kappa_EW = 1` content) or invokes
the demoted directionless dichotomy. The open selector (N1.6) needs a different
(non-registration) theorem.

**N7 — Steelman.** *"Record does not privilege `{P_1, P_adj}`; with a partition
whose blocks straddle singlet and adjoint, the singlet is registered differently."*
Reply: blocks that straddle the irreps are **not** central-sector (SU(`N_c`)-invariant)
decompositions of the color readout; adopting one to engineer `kappa_EW = 0` is the
forbidden Record partition over-reach (the exact move the chirality no-go N7 rejects).
The only SU(`N_c`)-respecting partitions coarsen/refine `{P_1, P_adj}`, all of which
register the singlet (N1.1-N1.2).

**N8 — Cross-cycle echo.** Structurally adjacent walls remain standing:
`registration_reinstates_chirality` (retained_no_go) and the `r`-dial teeth of the
scope-correction panel. Register-not-read joins the CMT, OZI, tracelessness, and
MC routes that all fail to fix `kappa_EW`.

## Does Not Claim

- Does **not** force or derive `kappa_EW = 1`. Registration's "register all sectors"
  content is `S + C`, but selecting it as the physical readout is itself an external
  scheme choice; the honest endpoint is `kappa_EW` undetermined.
- Does **not** fabricate `kappa_EW = 0`; it closes the register-not-read route to it.
- Does **not** claim Record selects any partition (the partition is a per-lane input).
- Does **not** revisit the MC-undecidability or matching-rule no-gos; it adds the
  register-not-read route to the list of routes that do not fix `kappa_EW`.
- Makes no statement about `sin^2(theta_W)` (which is `kappa_EW`-invariant and
  survives either way).

## Relation to Retained Inventory

- Mirrors the machinery of retained no-go `registration_reinstates_chirality`
  (`D` registers central sectors; "`D` constrains `r` not at all").
- Applies the `register_not_read_scope_correction` panel's `r`-dial test and
  directional-inverse tell (meta) to the color-readout route.
- Uses the canonical `record_outcome_observable_principle_canonical_proposal`
  registration map (meta).
- Closes the route named open in
  `rconn_kappa_ew_register_not_read_color_trace_open_gate` (unaudited open_gate).
- Consistent with `ew_kappa_self_energy_object_pin_mc_undecidable` (scheme weight,
  MC-undecidable) and `ew_current_matching_rule_open_gate` (selector is an extra
  premise).

## Boundary / Honest-Auditor Read

The new content is T1-T4: the color singlet is the trivial irrep, so the
registration map keeps it (never the annihilated object), and `kappa_EW` is an
inter-sector weight the partition does not deliver — the exact `r`-dial structure of
the retained chirality no-go, transported to color. This **sharpens** the open gate
to a no-go on the register-not-read route; it does **not** close `kappa_EW` (the
open non-registration selector, N1.6, is untouched) and does **not** privilege
either completion.

## Verification

```bash
python3 scripts/frontier_ew_kappa_registration_color_sector_nogo.py
```

Verifies (zero PDG inputs): (A) the singlet/adjoint sector partition with counts
`1 : N_c^2-1` (`-> 8/9`) for `N_c = 2,3,4,5`; (B) the singlet is the
SU(`N_c`)-equivariant trivial irrep, registration (dephasing) keeps both
populations and removes only coherence, and `kappa_EW = 0` (discard the singlet
population) is not the record map; (C) `kappa_EW` is a free inter-sector weight while
the count `8/9` is delivered; (D) the Koide parallel (`D(H) = H`, "`D` constrains
`r` not at all"); (E) the directionless tell. Expected:
`RUNNER STATUS: PASS (PASS=12 FAIL=0)`.

## Safe wording

**Can claim:**
- "Register-not-read registers all central color sectors (keeps the singlet); it
  does not supply `kappa_EW = 0`."
- "`kappa_EW` is an inter-sector weight the partition leaves free, exactly as the
  Koide within-block weight `r`."
- "The `kappa_EW = 0` register-not-read route is the demoted, directionless loose
  dichotomy; the reopen route is closed."

**Cannot claim:**
- bare `retained` / `promoted`.
- "`kappa_EW = 1` is forced" or "`kappa_EW = 0` is forced." (Register-not-read leaves
  it undetermined.)
- "This closes `kappa_EW`." (It closes only the register-not-read route; the
  non-registration selector remains open.)
- "Record selects the color partition." (It does not.)
