# Small CKM vs Large PMNS from the Record Readout Context — Narrow Structural Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (qualitative structural account; conditional on a named posit)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/ckm_small_from_record_readout_context_runner.py`](../scripts/ckm_small_from_record_readout_context_runner.py)
**Cached output:** [`logs/runner-cache/ckm_small_from_record_readout_context_runner.txt`](../logs/runner-cache/ckm_small_from_record_readout_context_runner.txt)

## Audit context

The lepton-sector record-ontology results (this session) gave the PMNS trimaximal column
as the recorded `C_3`-singlet central sector of the **propagating** neutrino, with the
charged leptons recorded in the **corner** (detection) basis (`U_e = I`). The framework
has separately **noticed** — but not derived — the small-CKM/large-PMNS anti-correlation
([`FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30`](FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30.md),
`audited_conditional`: "leptons land *exactly* on 2/3 despite **large** PMNS mixing;
quarks miss 2/3 despite **small** CKM mixing — mixing anti-correlates with deviation").
The record/detection distinction has **never been applied to quarks** (virgin territory).

This note gives that contrast a principled qualitative account from the **readout
context**, and shows it is consistent with — indeed refines — the retained CKM no-go.

## The posit (named, not retained)

> **Posit (P-det).** *Detected* fermions (charged leptons and quarks — massive, registered
> as mass eigenstates) are recorded in the **corner** basis (`U = I`), as the charged
> leptons are; the *propagating* neutrino is recorded in the `C_3` central-sector basis.

P-det is the natural extension of the lepton record/detection structure (`U_e = I` via the
`Z_3` trichotomy; the neutrino's `C_3` central-sector recording) to quarks. It is **not
established on the framework** for quarks; the result below is conditional on it.

## Safe statement

The observed mixing is the misalignment between the two sectors' recorded mass eigenbases
(readout contexts). Under P-det:

**Theorem (qualitative).**

1. **Both quark sectors share the readout context (corner), so CKM aligns.** With
   `U_up = U_dn = I` (both detected, corner-recorded), `V_CKM = U_up^† U_dn = I` — the
   **identity** permutation. The small Cabibbo structure is a *registered* deviation from
   it (a small relative rotation gives `|V_us|^2 ≈ 0.05`). CKM is **small / near-diagonal**
   and has **no trimaximal column**.

2. **The lepton sectors have different readout contexts, so PMNS is large.** Charged
   leptons corner-recorded (`U_e = I`) vs the neutrino `C_3`-recorded; the recorded
   `C_3`-singlet `W` is a PMNS column of magnitudes `1/3` (trimaximal), and the mixing is
   **O(1)** (large).

3. **The contrast is the readout context.** Same context (both detected → corner) → aligned
   → small mixing, no singlet column. Different context (detected corner vs propagating
   `C_3`) → large mixing with a trimaximal column. The specific angles (Cabibbo `λ`, …) are
   **registered** per-sector data (guardrail G3), not derived here.

## Consistency with the retained CKM no-go (refinement)

The retained-tier wall
([`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md),
`retained_no_go`) and the `unaudited` permutation no-go
([`NEWPHYSICS_NP_CKM_WOLFENSTEIN_NOTE_2026-05-10_npCKM`](NEWPHYSICS_NP_CKM_WOLFENSTEIN_NOTE_2026-05-10_npCKM.md))
establish that **two Hermitian circulants on the same `C_3` generator commute**, so they
share the Fourier eigenbasis and `V_CKM` is a **permutation** (`|V_ij| ∈ {0,1}`) — the
both-circulant realization gives *no* physical mixing. P-det is the record-ontology escape
the no-go itself names ("break the shared-`C_3` eigenbasis"): detected quarks are
**corner-recorded, not Fourier-diagonalized**, so `V_CKM` is the **identity** permutation
(the trivial element of the no-go's permutation set), with the small Cabibbo a registered
deviation. The Koide circulant remains the *eigenvalue pattern* (`r_up ≈ 0.77`,
`r_down ≈ 0.59`, registered), not the corner-basis operator form — exactly as `U_e = I`
coexists with the lepton Koide circulant.

## Boundary (honest)

- **Conditional on P-det.** That quarks are corner-recorded (detected) like charged leptons
  is a *posit* (the natural extension of the lepton record/detection structure), **not
  retained** — the agentic map found this is unaddressed on the framework. Drop P-det and
  the account does not stand.
- **Qualitative, not quantitative.** It accounts for *why* CKM is small and PMNS large (same
  vs different readout context); it does **not** derive the Cabibbo angle, the Wolfenstein
  `λ, A, ρ, η`, or the CP phase (those are registered per-sector data, G3 — the framework's
  Wolfenstein magnitude package is separate and `unaudited`).
- **Does not derive the quark `r` values.** `r_up, r_down` are registered eigenvalue
  patterns; the retained boundary forbids copying the lepton `r=1/2` into the quark lane.
- **Does not touch color.** Color/`SU(3)` is generation-blind for the mixing analysis
  (`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE`, the `Z_3` color↔generation bridge
  is an open gate).

## Forbidden imports check

No new axiom. The only new physical input is the **named posit P-det** (detected →
corner-recorded), an extension of the existing lepton record/detection distinction — flagged
explicitly and not asserted as derived. The algebra (`C_3` circulant, corner basis, `C_3`
singlet `P_0 = J/3`) is existing structure; the small Cabibbo deviation is a registered
datum, not a derivation.

## Runner check breakdown

Class A finite-dimensional algebra: both-circulant → permutation CKM (the no-go); both-corner
(detected) → identity CKM; a small registered deviation → small Cabibbo with no trimaximal
column; PMNS (corner vs `C_3`-singlet) → trimaximal column + large; and the contrast
statement. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact linear algebra: shared-`C_3` circulants give a permutation CKM
(reproducing the retained no-go); corner-recorded (detected) sectors give the identity
permutation; the propagating-neutrino `C_3`-singlet gives the trimaximal column and large
mixing. The genuine content is the *organizing principle*: small-CKM-vs-large-PMNS is the
same-vs-different readout context, a framework-noticed puzzle given a record-ontology account
and shown consistent with (a refinement of) the permutation no-go. It is **conditional on the
named posit P-det** (quarks corner-recorded), which is an unestablished extension of the
lepton structure, and it is **qualitative** — the angles are registered, not derived.
Effective status remains `unaudited` until the audit lane assigns one.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/ckm_small_from_record_readout_context_runner.py
```
