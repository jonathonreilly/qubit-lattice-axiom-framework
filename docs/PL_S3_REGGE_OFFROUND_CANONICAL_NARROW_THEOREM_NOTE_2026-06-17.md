# Off-Round Robustness of the PL S³ Regge Hessian: Generic Probes Lift the Frame-Ambiguity-Hosting Degeneracy

**Date:** 2026-06-17
**Claim type:** bounded_theorem (answers the named open residual of the retained_bounded round-PL-S³ Regge-Hessian note on its finite atlas; a structural reframing of the polarization-frame gate's obstruction, **not** a construction of the distinguished connection)

**Claim scope:** Reusing the verified machinery of the retained_bounded round-PL-S³ Regge-Hessian note
([`UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md`](UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md)), this note
answers **that note's own named open residual** — *"off-round, where the S₅ symmetry breaks and
multiplicities could reappear, the question reopens."* Result: the frame-ambiguity-hosting degeneracy
of the curved-background Regge Hessian on `∂Δ⁴` (the gate's own PL S³ atlas) — the round-point
multiplicity structure `10 = 1 ⊕ 4 ⊕ 5`, which **is** the gate's degenerate complement where a frame
must be chosen — **is a symmetry artifact.** A **generic** off-round deformation lifts it to a fully
**simple** 10-dimensional spectrum (no degenerate eigenspace ⇒ the Hessian itself fixes the channel
basis up to eigenvector signs ⇒ no within-complement frame freedom). Symmetric loci retain
residual-group-controlled degeneracies (computed: `S₅` round → `1,4,5`; `S₄` (apex-stabilizer) →
`1,1,3,3,2`, the branching `4→1⊕3`, `5→2⊕3`). Hence the gate's frame-ambiguity host is a
non-generic degeneracy of this finite Hessian family; the round-point canonicity is the
Schur-controlled high-symmetry case of the same generic lifting pattern.

**Status authority:** independent audit lane only. This note writes no audit verdict and retags no
ledger row.
**Loop:** science-fix lane 2026-06-17 (gravity-capstone follow-on).
**Runner:** [`scripts/pl_s3_regge_offround_canonical_2026_06_17.py`](../scripts/pl_s3_regge_offround_canonical_2026_06_17.py)
(`TOTAL: PASS=7 FAIL=0`, deterministic — off-round probes seeded; reuses the retained note's exact
symbolic dihedral/volume machinery, numpy+sympy only).
**Authority role:** source-note proposal. If retained, answers the round-PL-S³ note's named off-round
residual and reframes the polarization-frame gate's obstruction as a degeneracy-locus phenomenon.

## 1. The residual this answers

The retained_bounded round-PL-S³ note proved the Regge Hessian on the round `∂Δ⁴` is an exact Λ-Regge
critical point with multiplicity-free canonical channels `10 = 1 ⊕ 4 ⊕ 5` (Schur-unique), so *"the
scalar-route frame ambiguity does not arise … there is no degenerate complement at the round point."*
Its explicit honest residual (verbatim): *"Off-round, where the `S₅` symmetry breaks and
multiplicities could reappear, the question reopens — that is the honest residual, named."* This note
answers it on the same finite atlas.

## 2. Inputs (one hop, fresh statuses on origin/main)

| Input | Role | Status |
|---|---|---|
| round `∂Δ⁴` Λ-Regge critical point + Hessian `H = ∂δ/∂ℓ − 2Λ*∂²V` + `S₅` channels `1⊕4⊕5` | the round baseline (reproduced) | [`UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md`](UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md) — **retained_bounded** |
| the gate's obstruction (frame-dependent localized channel coefficients on the complement) | the residual reframed | [`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md) — audited_conditional |
| 3D Λ-Regge action `S_Λ = Σ_e ℓ_e δ_e − 2Λ Σ_T Vol_T` on `∂Δ⁴` | the action class (supplied) | (same round note; reused machinery) |

No fitted parameters, no observed values, no GR/PDG comparator, no new axioms; numpy+sympy only.

## 3. The theorem (computed; runner blocks [R],[LIFT],[SYMLOCUS],[VERDICT])

- **[R]** Round baseline reproduced exactly: deficit/edge `= 2π − 3·arccos(1/3) ≈ 2.5903`, exact
  Λ-Regge critical point at `Λ* ≈ 7.3265` (EOM residual `0`), `H` symmetric, spectrum multiplicity
  structure `{1,4,5}` (the `S₅` channels). The `×4` and `×5` degenerate eigenspaces **are** the gate's
  "degenerate complement" — the host of the frame ambiguity (a frame choice within a degenerate space).
- **[LIFT]** A **generic** off-round deformation (two seeds, `ε = 0.02, 0.08`) lifts **all** degeneracy:
  the spectrum becomes a fully **simple** 10-level spectrum (`#levels = 10`, `max mult = 1`). With no
  degenerate eigenspace, the second-variation form itself fixes the channel basis — there is no
  within-complement frame freedom. (The off-round spectrum is the second-variation form evaluated at
  the round `Λ*`; the deformed configurations are not themselves Regge-critical, so this is a statement
  about the symmetric-matrix family, not a new critical-point Hessian.) The mechanism is the standard
  genericity of Hermitian spectra (degeneracies are
  codimension `≥ 2`, generically avoided — von Neumann–Wigner); the content here is that the degenerate
  eigenspace that **hosts the gate's frame-ambiguity lies on this non-generic locus.**
- **[SYMLOCUS]** Symmetric off-round loci retain degeneracy controlled by the residual group:
  an `S₄`-symmetric off-round deformation (scale the four apex edges) gives `{1,1,3,3,2}` — the `S₄`
  branching of `1⊕4⊕5` (`4→1⊕3`, `5→2⊕3`). This exhibits the residual-symmetry mechanism without
  claiming that every possible accidental degeneracy is symmetry-forced.
- **[VERDICT]** The round-S³ note's "off-round multiplicities could reappear" residual is answered in
  the canonical direction on the tested finite family: generic off-round probes carry no degenerate
  complement (simple spectrum, canonical up to eigenvector signs), while symmetric loci retain
  controlled multiplicities.

## 4. What this is, and is not (the honest bound)

**Is:** a finite, firewall-clean, exact reframing of the polarization-frame gate's obstruction on its
own PL S³ atlas — the frame-ambiguity-hosting degeneracy is non-generic on the checked Hessian family,
so the round-point canonicity is not a fragile artifact but a high-symmetry case of the generic
lifting pattern; and the residual is answered by direct computation rather than left open.

**Is not** (explicitly, to avoid overclaim):
- **Not** the distinguished **connection** the blocker names. A generic simple spectrum fixes the
  Hessian's *eigenbasis* (the channel-degeneracy structure); it does **not** construct the covariant
  *localization-level* lapse/shift/shear split, nor a transport rule across the off-round family of
  backgrounds. That construction — the literal "distinguished connection / horizontal distribution /
  canonical `Π_curv`" — remains the multi-step open capstone.
- **Not** the cubic `O_h` transplant. `∂Δ⁴` carries `S₅`, not the lattice's `O_h`; this is the gate's
  own atlas, not the `Z³` cubic frame-selection of PRs #4285/#4367 (which lives on a different group).
- **Not** a continuum-limit statement (the PL-atlas refinement obstruction stands), and **not** the
  3+1 prism (`S³ × Z_τ`) extension (not built here).
- **Not** a derivation of action selection or physical GR dynamics; the dimensionful GR calibration
  stays import-bounded.

## 5. Boundary / honest-auditor read

The load-bearing facts are finite/exact: the round baseline is reproduced from the retained note's own
machinery (deficit, `Λ*`, EOM `0`, `{1,4,5}`), and the off-round spectra are exact eigenvalue
multiplicity counts (generic → simple `{1×10}`; `S₄` → `{1,1,3,3,2}`). The lifting mechanism is
standard spectral genericity, named as such; the contribution is its identification with the gate's
frame-ambiguity host plus the residual-group control at the symmetric examples and the answer to the
named residual. This **reframes** the blocker (its obstruction is a degeneracy phenomenon of the finite
Hessian family) and is a step toward — but is **not** — the distinguished connection. Whether a physical
background is generic (canonical), sits on a symmetry-forced or accidental degeneracy locus
(ambiguous), and whether the localization-level connection can be built across the off-round family,
are left to downstream work and the independent audit lane.
