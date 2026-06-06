# Small CKM vs Large PMNS as Readout-Context Misalignment — Conditional Observation; the Detection Grounding Fails

**Date:** 2026-06-06
**Claim type:** bounded_theorem (conditional structural observation) + recorded failed-grounding (a correction for future work)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/ckm_small_from_record_readout_context_runner.py`](../scripts/ckm_small_from_record_readout_context_runner.py)
**Cached output:** [`logs/runner-cache/ckm_small_from_record_readout_context_runner.txt`](../logs/runner-cache/ckm_small_from_record_readout_context_runner.txt)

## Audit context

The framework has **noticed** — but not derived — the small-CKM/large-PMNS
anti-correlation
([`FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30`](FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30.md),
`audited_conditional`). This note records (1) a conditional structural mapping of that
contrast onto a readout-context misalignment, and (2) — prominently — the **failure** of
the natural "detection/localization" grounding for it, so the corner=momentum correction
is not re-derived by future work.

## The conditional observation (what holds)

The observed mixing is the misalignment between the two sectors' mass eigenbases. With
the lepton structure (charged leptons diagonal in the corner basis, `U_e = I`; the
neutrino mass `C_3`-structured — its recorded `C_3`-singlet `W` is the PMNS trimaximal
column):

**Conditional theorem.** *If* both quark mass operators are diagonal in the **same**
basis (the corner basis, `U_up = U_dn = I`) while the neutrino mass is `C_3`-structured
(misaligned with the charged-lepton corner basis), then:

- **CKM aligns:** `V_CKM = U_up^† U_dn = I` (identity permutation); the small Cabibbo
  structure is a *registered* deviation. CKM is **small / near-diagonal**, with **no
  trimaximal column**.
- **PMNS is large:** charged-lepton corner basis vs neutrino `C_3` basis → the recorded
  `C_3`-singlet gives a trimaximal column and `O(1)` mixing.

So the small-vs-large contrast = same-readout-context (quarks) vs different-readout-context
(leptons). This respects/refines the retained no-go
([`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md),
`retained_no_go`; two shared-`C_3` circulants commute → `V_CKM` is a permutation): the
aligned-corner case is the **identity** element of that permutation set. The Koide
circulant remains the *eigenvalue pattern* (`r_up ≈ 0.77`, `r_down ≈ 0.59`, registered),
not the corner-basis operator form.

## The failed grounding (recorded so it is not repeated)

The natural way to *ground* "both quarks corner-diagonal, neutrino `C_3`" is a
detection-vs-propagation story: gauge-charged fermions are localized/detected (recorded in
a "local" basis), the gauge-neutral neutrino propagates. **This grounding fails on the
framework's own structure, and the failure is sharp:**

- **The corner basis is the *momentum* (BZ) basis, not the local one.** The generation
  carrier is the momentum factor (the `C_3` orbit of the hw=1 BZ corners), and
  **position-locality is generation-blind**: a local per-site observable has *identical*
  expectation across all three generations
  ([`FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31`](FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md),
  `⟨P_site0⟩ = 1/8` for each generation). So "corner = local/detection basis" is
  **contradicted** — the corner is delocalized in position, and the local basis cannot
  even distinguish generations.
- **No gauge→recording link exists.** The framework's only "gauge environment" is the
  Wilson-plaquette vacuum (it fixes the coupling `g`), never fermion decoherence; the
  einselection monitor is an abstract `K`-real `C_3`-invariant observable, with its
  physical identity an *open* slot
  ([`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
  `retained_bounded`). Nothing ties gauge charge to the readout basis.
- **Neutrino gauge-neutrality is never tied to propagation/`C_3`-recording.**

**Conclusion:** the corner-vs-`C_3` asymmetry between the quark and lepton sectors is
**not grounded** by a detection/localization mechanism — the local basis is
generation-blind, and the corner basis is momentum. The conditional observation above
therefore rests on an **ungrounded posit** (quark masses corner-diagonal, neutrino mass
`C_3`-structured), with no record-ontology derivation. The only remaining lead — that the
neutrino's gauge-singlet `ν_R` permits a Majorana (`C_3`) mass while charged fermions get
only Dirac/Yukawa (corner-diagonal via the `Z_3` trichotomy) masses — is **unsupported on
the framework** and is *not* asserted here.

## Boundary (honest)

- **The structural mapping is conditional** on an ungrounded posit; it is near-tautological
  algebra (aligned bases → small mixing) once the posit is granted.
- **The detection/localization grounding is refuted** (corner = momentum, local =
  generation-blind) — recorded here precisely so it is not retried.
- **Qualitative, not quantitative:** does not derive the Cabibbo angle, Wolfenstein
  `λ, A, ρ, η`, the CP phase, or the quark `r` values (all registered/separate).
- Color/`SU(3)` is generation-blind for the mixing analysis.

## Forbidden imports check

No new axiom. The conditional uses existing structure (corner basis, `C_3` singlet
`P_0 = J/3`). The detection/localization grounding is *recorded as failed*, not imported.
No claim rests on the unsupported Majorana-vs-Dirac lead.

## Runner check breakdown

Class A: both-circulant → permutation CKM (the no-go); aligned bases (`U_up=U_dn=I`) →
identity CKM; a small registered deviation → small Cabibbo, no trimaximal column; the
`C_3`-structured neutrino vs corner-basis charged lepton → trimaximal column + large; and
the failed-grounding control (a local per-site observable is generation-blind, so the
corner basis is not the local one). Expected `runner_check_breakdown = {A: N, B: 0, C: 0,
D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact linear algebra: aligned mass eigenbases give a near-identity
(small) CKM with no trimaximal column; a `C_3`-structured neutrino against the
corner-basis charged lepton gives a large PMNS with a trimaximal column; and the local
per-site observable is generation-blind (so the corner basis is *not* the local basis).
The note's honest content is twofold: a **conditional** structural mapping of the
small-vs-large contrast (resting on the ungrounded posit that quark masses are
corner-diagonal and the neutrino mass is `C_3`-structured), and a **recorded refutation**
of the detection/localization grounding for that posit (corner = momentum; local =
generation-blind). It does **not** derive the posit, the angles, or the quark `r` values,
and it does **not** rest on the unsupported Majorana-vs-Dirac lead. Effective status
remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/ckm_small_from_record_readout_context_runner.py
```
