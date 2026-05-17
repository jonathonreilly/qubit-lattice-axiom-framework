# `AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Claim type:** meta
**Parent under repair:** [`AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only. This note does not set or predict the parent's audit outcome.

## 1. Source character

`AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md` is a
`positive_theorem` that derives the Stefan-Boltzmann law

```
u(T) = (π²/15) (k_B T)⁴ / (ℏc)³                        (SB1-SB4)
```

for blackbody photon radiation on the framework's cited
`(EW + emergent Lorentz + Block 01 KMS)` surface, via:

- Block 01 KMS support theorem → Planck distribution `n(ω, T) = 1/(e^(βω) - 1)`;
- cited 3+1 dimensions → standard 3D density of states;
- cited U(1) photon → two transverse polarizations;
- standard math identity `Γ(4) ζ(4) = π⁴/15`.

The proof `(SB1)-(SB4)` is unchanged. What was patched is the **tier
qualifier** on the upstream composite ("retained" → "cited").

## 2. Findings

### F-A — Tier over-claim "retained" for the upstream composite

**Symptom:** approximately 18 sites in the note used "retained" as the
tier qualifier for the upstream composite. Examples:

| Section | Original wording |
|---|---|
| Claim scope | "framework retained EW + emergent Lorentz + Block 01 KMS surface" |
| Scope | "framework's retained emergent-spacetime surface" |
| Scope | "framework's retained U(1) photon" |
| Scope | "framework's retained emergent Lorentz invariance" |
| Retained inputs (heading) | "## Retained inputs" |
| Retained inputs | "Retained emergent Lorentz invariance" |
| Retained inputs | "Retained anomaly-forced 3+1 dimensions" |
| Retained inputs | "Retained U(1) photon" |
| Retained inputs | "from retained AXIOM_FIRST_SPECTRUM_CONDITION" |
| Admitted-context | "implied by the retained framework structure" |
| Statement | "retained U(1) photon sector" |
| Proof | "framework retained surface plus Block 01 KMS support" |
| Step 2 | "framework's retained 3D spatial substrate" |
| Step 2 | "framework's retained surface" |
| C2 | "framework's retained surface" |
| Honest status | "retained framework EW + Lorentz package + Block 01 KMS support" |
| Citations | "retained EW package", "retained anomaly-forced 3+1", "retained emergent Lorentz", "retained spin-statistics", "retained spectrum condition" |

**Reality (per 2026-05-17 ledger snapshot):**

| Upstream | `audit_status` | `effective_status` |
|---|---|---|
| `axiom_first_kms_condition_theorem_note_2026-05-01` (Block 01 KMS) | `unaudited` | `unaudited` |
| `emergent_lorentz_invariance_note` | `unaudited` | `unaudited` |
| `lorentz_kernel_positive_closure_note` | `unaudited` | `unaudited` |
| `anomaly_forces_time_theorem` | `unaudited` | `unaudited` |
| `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | `unaudited` | `unaudited` |
| `axiom_first_spin_statistics_theorem_note_2026-04-29` | `unaudited` | `unaudited` |
| `axiom_first_spectrum_condition_theorem_note_2026-04-29` | `unaudited` | `unaudited` |
| `rconn_derived_note` (EW package) | `audited_conditional` | `audited_conditional` |

**7 of 8 named upstreams are `unaudited`.** Only the EW package's
RCONN_DERIVED_NOTE is `audited_conditional`. None is at
`retained_bounded`. "Retained" is therefore systematically over-stated.

**Fix:**

- the most prominent wordings (Claim scope, Scope bullets, "Retained
  inputs" section heading + bullets, Citations list) have been
  corrected inline to "cited" with explicit notation that the cited
  companion is currently `unaudited`;
- a new "Upstream-tier accounting (2026-05-17)" section provides the
  tier table above and states the effective-tier-inherits-from-weakest
  logic;
- remaining "retained" mentions in body/proof text are now understood
  through the tier-accounting section. The proof structure
  `(SB1)-(SB4)` is unaffected.

### Admission-inheritance from upstream parent (lower stringency)

This note uses only `d_s = 3` from the upstream parent's spacetime
conclusion. Per the parent's recent
[F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md),
the `d_t = 1` decomposition (Step 3 derived + admission (iv)
inherited) does **not propagate** into the Stefan-Boltzmann proof
because `d_s = 3` comes from axiom A2 (`Z^3` substrate) directly per
`MINIMAL_AXIOMS_2026-05-03.md`, independent of admissions (i)-(iv).

Only the **overall effective tier** of this Stefan-Boltzmann row
inherits from the parent's tier (currently `unaudited`). The
arithmetic of `(SB1)-(SB4)` is insulated from the parent's admission
structure.

## 3. What this fix does NOT do

- Change `(SB1)-(SB4)`.
- Change the proof steps (Step 1: Planck from KMS; Step 2: 3D DOS;
  Step 3: energy density integral; Step 4: σ_SB constant).
- Change the runner expectation.
- Change the corollaries (C1: Wien displacement; C2: CMB blackbody;
  C3: photon-gas EOS; C4: cosmological consistency).
- Change the falsifiability framing or the "Honest claim-status" YAML
  block.
- Promote any upstream companion or alter any retained-tier claim.
- Modify pipeline code or any other source theorem note.
- Set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (positive_theorem retained; effective tier
inherits from the weakest upstream, currently `unaudited` for 7 of 8
named upstreams).

The corrected note brings the in-note tier description into line with
the ledger and discloses the admission-inheritance from the upstream
parent (lower-stringency: only `d_s = 3` is used, which is
admission-independent). The arithmetic of `(SB1)-(SB4)` is unaffected.

Once the cited upstreams audit through, the Stefan-Boltzmann row's
effective tier rises automatically.

## 5. Verification

Paired runner:
`scripts/frontier_axiom_first_stefan_boltzmann_downstream_fix.py`

Programmatically verifies:

- **F-A:** the most prominent stale "retained" sites (Claim scope,
  Scope, "Retained inputs" section heading, Citations) have been
  retired and replaced with "cited" wording; new "Upstream-tier
  accounting (2026-05-17)" section is present; tier table lists 7
  upstreams at `unaudited`; effective-tier-inherits-from-weakest
  wording present.
- **Admission inheritance:** the lower-stringency note about `d_s = 3`
  coming from axiom A2 (admission-independent) is recorded.
- **Structural invariants:** Statement (SB1)-(SB4) preserved; proof
  Steps 1-4 preserved; Γ(4) ζ(4) = π⁴/15 identity preserved; numerical
  σ_SB = 5.670374419 × 10⁻⁸ value preserved; corollaries C1-C4
  preserved.

Cached output: `logs/runner-cache/frontier_axiom_first_stefan_boltzmann_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent (d_s = 3 used; admission-independent)
- [`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md) — upstream F-B fix (tier-inheritance route only)
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — sibling downstream fix
- [PR #1509](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1509) — sibling downstream fix
- [PR #1510](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1510) — sibling downstream fix
- [PR #1511](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1511) — sibling downstream fix
- [PR #1512](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1512) — sibling downstream fix
- [PR #1513](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1513) — sibling downstream fix
