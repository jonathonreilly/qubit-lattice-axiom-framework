# DM Neutrino Bosonic Normalization Theorem (Conditional)

**Date:** 2026-04-15 (status line narrowed 2026-04-28 per audit-lane verdict)
**Status:** bounded conditional normalization selector on the upstream local Higgs family — IF physical local scalar observables are taken to be exactly `W[J]` source-response coefficients (the observable-principle premise), THEN the algebraic checks close. The observable-principle premise is not registered as an audit-clean theorem in the audit packet, and the runner only checks `Y` log-det response and `Gamma_1` even response, not the admissibility of active-space ratios. Not a tier-ratifiable normalization selector.
**Type:** bounded_theorem
**Script:** `scripts/frontier_dm_neutrino_bosonic_normalization_theorem.py`

---

## Question

Can the remaining `1` versus `1/sqrt(2)` ambiguity in the direct neutrino
bridge normalization be resolved by importing the retained mainline
observable-principle toolkit?

---

## Answer

Yes, on the retained local Higgs family.

The exact direct bridge audit was correct as an audit:

- full `C^16` Frobenius normalization gives `y_nu^(0) / g_weak = 1/sqrt(2)`
- active chiral-subspace normalization gives `1`

What that audit did **not** yet decide was which normalization is physically
admissible for a local bosonic observable.

The mainline observable principle now fixes that.

Physical local scalar observables must be source-response coefficients of the
unique additive CPT-even generator

`W[J] = log|det(D+J)| - log|det D|`.

On the direct neutrino bridge, that changes the story sharply.

---

## Exact Theorem

Let

- `Y = P_R Gamma_1 P_L` be the exact direct local chiral bridge
- `Gamma_1` be the weak-axis post-EWSB scalar operator from the retained Higgs
  family `M(phi) = sum_i phi_i Gamma_i`

Then:

1. `Y` is nilpotent:

   `Y^2 = 0`

2. On a scalar local baseline `m I`, the raw bridge has identically zero
   additive bosonic response:

   `det(m I + j Y) = m^16`

   so

   `W[jY] = 0`

   for all real `j`.

3. The retained scalar Hermitian completion of the bridge is exactly

   `Y + Y^dagger = Gamma_1`.

4. That completion has nontrivial even bosonic response:

   `det(m I + j Gamma_1) = (m^2 - j^2)^8`

   so

   `W[j Gamma_1] = 8 log|1 - j^2/m^2|`.

Therefore the physical normalization surface is **not** the active chiral
bridge by itself. It is the full bosonic `Gamma_1` family.

---

## Why This Selects `1/sqrt(2)`

Once the physical source family is assigned on `Gamma_1`, the branch's
canonical trace normalization becomes unambiguous:

- `Tr(Gamma_1^dag Gamma_1) / 16 = 1`
- `Tr(Y^dag Y) / 16 = 1/2`

so the canonically normalized bridge ratio is exactly

`sqrt( Tr(Y^dag Y) / Tr(Gamma_1^dag Gamma_1) ) = 1/sqrt(2)`.

The active-space ratio `1` remains a mathematically exact comparator, but it is
no longer the physical bosonic normalization because the raw chiral bridge
itself carries no scalar source-response.

So the branch can now promote the previously bounded full-space benchmark to
the retained normalization statement:

> within the retained local Higgs family and the axiom-native observable
> principle, the physical base normalization is
> `y_nu^(0) / g_weak = 1/sqrt(2)`.

Equivalently, the branch's correct base benchmark is

`y_nu^(0) = g_weak / sqrt(2)`,

not the active-space comparator `g_weak`.

---

## What This Does And Does Not Close

This closes one real blocker:

- the base-normalization ambiguity of the direct `Gamma_1` bridge

This note by itself does **not** close the whole denominator. But the next
local step is now closed by the downstream companion

- `docs/DM_NEUTRINO_SCHUR_SUPPRESSION_THEOREM_NOTE_2026-04-15.md`
- `scripts/frontier_dm_neutrino_schur_suppression_theorem.py`

That theorem fixes the exact retained local second-order coefficient

`y_nu^eff = g_weak^2 / 64`

and upgrades the old bounded `k_B = 8` attraction to an exact local Dirac-lane
statement.

So the live denominator problem is no longer

> choose `1` versus `1/sqrt(2)`

and it is no longer

> derive the local second-order `Gamma_1` suppression coefficient.

It is now downstream:

> derive or rule out the Majorana / `Z_3` activation law that turns on the
> unique charge-`2` source and feeds the three-generation `A/B/epsilon`
> structure without fitted leftovers.

---

## Consequence For The `k_B = 8` Candidate

The denominator boundary is now sharper than this note alone.

This note fixes the physical base surface:

`y_nu^(0) = g_weak / sqrt(2)`.

The downstream Schur theorem then fixes the retained local suppression:

`y_nu^eff = g_weak^2 / 64`,

which implies `k_eff ~= 8.01` on the present seesaw calibration.

So the honest remaining question is no longer whether the direct Dirac lane can
reach `k_B = 8`. On the retained local lane, it does. The remaining question is
whether the Majorana side is axiom-forced strongly enough to turn that local
Dirac result into a full zero-import `eta`.

## Independent-audit boundary

Independent audit is required. The algebraic checks close after accepting the
observable-principle premise, but this note does not register or reproduce the
theorem that physical local scalar observables are exactly `W[J]`
source-response coefficients on the local Higgs family. Without that physical
selection theorem, the runner only shows that `Y` has zero log-det response
and `Gamma_1` has nonzero even response; it does not by itself prove that the
active-space ratio `1` is inadmissible or that `1/sqrt(2)` is the unique
admissible normalization.

## What this note does NOT claim

- A tier-ratifiable normalization selector.
- An audit-clean upstream observable-principle theorem.
- That the active-space ratio 1 is inadmissible without the
  observable-principle premise.

## What would close this lane (Path A future work)

A retained normalization selector would require registering the
physical-observable selection theorem (physical local scalar
observables = `W[J]` source-response coefficients) as an audit-clean
upstream dependency.

## Audit dependency repair links

This graph-bookkeeping section records the explicit upstream authority
the load-bearing observable-principle premise relies on, in response to
the `missing_bridge_theorem` repair target for
`dm_neutrino_bosonic_normalization_theorem_note_2026-04-15`.
It does not promote this note or change the audited claim scope, which
remains conditional algebra on the `Y`/`Gamma_1` decomposition plus the
imported observable-principle premise.

**Update 2026-07-09:** the inline status echo of the upstream row went
stale against the live ledger and is replaced by a live-ledger pointer;
the W-source application bridge note is added as the application-step
authority for the family/normalization bridge gap named in this row's
chain-closure explanation.

Authorities cited:

- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  — the upstream authority for the load-bearing premise that physical
  local scalar observables are exact source derivatives of the unique
  additive CPT-even scalar generator `W[J] = log|det(D+J)| - log|det D|`,
  given premises P1 (scalar additivity), P2 (CPT-even phase blindness),
  P3 (continuity / minimal regularity), and P4 (normalization choice).
  For its current standing see the live audit ledger row
  `observable_principle_from_axiom_note`; this note does not restate
  that status inline.

- [`NEUTRINO_GAMMA1_WSOURCE_APPLICATION_BRIDGE_NOTE_2026-07-09.md`](NEUTRINO_GAMMA1_WSOURCE_APPLICATION_BRIDGE_NOTE_2026-07-09.md)
  — the W-source application bridge: applies the observable-principle
  functional to this note's declared `Y`/`Gamma_1` family at a declared
  scalar comparator point `D = m I_16` and derives, as exact finite
  theorems on `C^16`, the selection `W[jY] = 0`, the activation
  `W[jGamma_1] = 8 log|1 - j^2/m^2|`, and the weak-coupling per-mode
  normalization identity
  `-m^2 W''(0)/16 = Tr(Gamma_1^dag Gamma_1)/16 = 1`. Its two named
  premises — the family identification (readout-identification
  admission class) and the comparator-point declaration — are stated
  in that note.

The runner-checked content of this note (Part 1 algebra: `Y` nilpotent,
`Y + Y^dag = Gamma_1`, pseudoscalar orthogonal to scalar Higgs span;
Part 2: `W[Y] = 0`, `W[Gamma_1] = 8 log|1 - j^2/m^2|`; Part 3 trace
ratios `Tr(Gamma_1^dag Gamma_1)/16 = 1`, `Tr(Y^dag Y)/16 = 1/2`,
full-space ratio `1/sqrt(2)`, active-space comparator `1`) is exact
finite-dimensional matrix algebra on `C^16` and is independent of the
cited upstream authority. The cite chain is what supplies the physical
selection rule that promotes `1/sqrt(2)` from a comparator to the
admissible bosonic normalization.

## Honest source boundary

The A=12 algebraic checks close once the observable-principle premise is
accepted, but the inadmissibility of the active-space ratio `1` and the
uniqueness of `1/sqrt(2)` as the physical normalization do not follow from the
runner alone — they require the upstream theorem that physical local scalar
observables are exact `W[J]` source-response coefficients. The cite-chain
repair above wires
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE` as that upstream authority, and
the W-source application bridge note linked above supplies the
application step: the functional applied to this note's declared
family, with the weak-coupling normalization derived as the per-mode
quadratic W-response at the declared comparator point. This source edit does
not apply a verdict; the independent audit lane owns row status, and row status
is unchanged by the source edit.

## Scope of this rigorization

This rigorization is class B (graph-bookkeeping citation). It does not
change any algebraic content, runner output, or load-bearing step
classification. It records the upstream authority the audit verdict
expected and matches the live cite-chain pattern used by the
`DM_NEUTRINO_SCHUR_SUPPRESSION_THEOREM_NOTE_2026-04-15.md` cluster
(commit `02ad4fadd`).
