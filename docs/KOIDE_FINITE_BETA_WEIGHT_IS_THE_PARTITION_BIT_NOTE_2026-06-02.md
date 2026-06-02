# Koide finite-beta scoring is the partition-weight ratio, not an extra freedom

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** structural reduction + an exact reparametrization identity. This note proves
the surviving channel-vs-direction *scoring* residual of the tracial-standard-form carrier is a
single weight-ratio choice, and that the "finite-beta / temperature" form of that residual
(`KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02`) is the same choice as the
2-sector partition choice, by the exact identity `beta*gap = -ln t` with `t = w0/w1 = r`. It does
**not** derive `r=1/2`, does **not** supply a dynamics, does **not** approve any import, and does
**not** set an audit verdict. It is a diagnosis that collapses the finite-beta and partition
framings into one already-open object, with retained-no-go support for the underlying
weight-freedom boundary.
**Primary runner:** [`scripts/koide_finite_beta_weight_is_the_partition_bit_2026_06_02.py`](../scripts/koide_finite_beta_weight_is_the_partition_bit_2026_06_02.py) (SCORECARD PASS=11).

## What this adds

The carrier-scoring note
[`KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02.md`](KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02.md)
showed the channel-counting weight (`r=1/2`) is a finite-beta KMS/Gibbs
weight (`beta*gap=ln2`) that the tracial carrier (`Delta=1`, beta=0) lacks, and concluded the value-lane residual
"reduces to the emergent-time dynamics -- which finite-beta the dynamics realizes." That phrasing
invites reading the temperature as a *new* continuous degree of freedom the dynamics must supply
on top of the known partition gate. This note shows it is **not** new:

> **Identity.** With per-direction weights `w=(w0,w1,w1)` and the channel-counting balance
> `w0*a^2 = w1*b^2`, one has `r = w0/w1 = t` and `t = exp(-beta*gap)`, i.e. **`beta*gap = -ln t`**.
> Hence **`beta*gap = ln2` (finite-beta on the 3 directions) <=> `t=1/2` <=> uniform weighting of the two elected sectors <=> `r=1/2`**,
> while **beta=0 (tracial) <=> `t=1` <=> uniform on the 3 directions <=> `r=1`**. The "temperature" and the
> "2-sector vs 3-direction partition" are two names for the **same weight-ratio choice**.

So the carrier-scoring residual and the partition residual of the four 2026-06-02 flow/extremum
notes are the same scalar choice under this parametrization, not two independent reductions. Naming
the residual as `beta` does not add a second independent degree of freedom; a future derivation still
has to deliver the specific scalar/coarse-graining (`t=1/2`) rather than the tracial default (`t=1`).

## Retained no-go support: Ad-invariant weights remain free

`r=1/2` (channel/`t=1/2`) and `r=1` (direction/`t=1`) are two rays of the **one-parameter
Ad-invariant isotype-weight freedom** on `Herm(3)`,
`B_{alpha,beta_F}(A,A) = (alpha+3 beta_F)*Tr(A_s^2) + alpha*Tr(A_t^2)` (scalar/traceless split), positive-definite
for `alpha>0`, `alpha+3 beta_F>0`.
[`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
(**retained_no_go** on `origin/main`) proves PD + Ad-invariance + scalar/traceless orthogonality
do **not** force the Frobenius point `beta_F=0`. The finite-beta KMS/Gibbs weight has the same
weight-ratio shape: `beta*gap = ln2` is one interior point, `beta=0` another. This does **not**
promote the new carrier residual to an already-audited theorem; it says the residual is not a fresh
modular axiom candidate, but the same kind of retained-open weight freedom in modular coordinates.

## Why the candidate forcing principles do not pin the ratio

- **Self-consistency / "H sets its own temperature" (circular).** The cyclic-vector split
  `{e}|{g,g^2}` is **not** an eigenspace of `H=a*e+b*(g+g^2)` (`e` is not an H-eigenvector for `b!=0`),
  so `exp(-beta H)` cannot thermalize *on that partition*; H's own thermal weight lives on its
  eigenbasis, whose Aut(Z_3)-invariant line is the **democratic** `(1,1,1)` -- the demoted idempotent
  split, not the vacuum line `Omega=e`. beta carries units (1/energy) and H supplies a single scale
  (`gap=3b`), so beta is free; closing a self-consistent `(beta,r)` loop merely lets `beta=ln2/(3b)` absorb
  the channel target -- the target is the input.
- **n_gen=3 / C_3 (insufficient).** The most general Aut(Z_3)- and `(g<->g^2)`-invariant per-direction
  weight is `(w0,w1,w1)`, a free ratio. `r=1/(N-1)` holds *given* channel-counting; C_3 does not
  select channel- over direction-counting.
- **Entropy / 1-bit = ln2 (real but conditional).** The 2-outcome vacuum-detection observable
  `{P_id, I-P_id}` has Shannon entropy maximized (`=ln2`, one bit) **exactly at `r=1/2`** -- the ln2
  in `beta*gap=ln2` genuinely *is* the 1-bit entropy of the 2-channel split, not a coincidence.
  **But** the *unconstrained* Jaynes max-entropy state on `M_3` is `rho=I/3` (the trace, `Delta=1`),
  giving **direction-counting `r=1`**; `r=1/2` arises only once the 2-outcome coarse-graining is
  *elected* as the observable whose entropy is maximized. The 1-bit reading presupposes the
  partition; it does not force it.
- **Records/decoherence fixed point (does not land forced).** The retained_bounded
  [`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
  flow
  `r->2r^2` has `r=1/2` as an *unstable separatrix*; its thermalizing time-reverse makes `r=1/2`
  stable only on the **2-sector** functional (the 3-direction functional attracts to `r=1`). The
  flow notes
  ([`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
  [`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md),
  both `unaudited`) themselves reduce to the same 2-sector partition gate.

## No-Go Discipline Gate

This gate applies only to the negative/open part of the claim: the tested principles do not force
`t=1/2` over `t=1`.

- **N1 alternative routes:** (1) self-thermalization by `H`; (2) `n_gen=3`/`C_3` symmetry; (3)
  unconstrained maximum entropy; (4) records/Luders flow; (5) Ad-invariant Frobenius/isotype
  linear algebra. Routes (1)-(4) are computed here; route (5) is ruled out by the retained no-go
  cited above.
- **N2 wall independence:** the finite-beta scalar, the two-sector coarse-graining, and the
  Ad-invariant isotype-weight freedom are coordinate descriptions of one residual, not three
  independent walls. The remaining wall is the selection of `t=1/2`.
- **N3 hidden-wall scan:** "temperature," "partition," and "ratio" are not admitted inputs. The note
  treats them as equivalent names for the missing weight ratio and keeps any future dynamics that
  selects the ratio out of scope.
- **N4 residual matching:** the Frobenius no-go attacks weight-ratio forcing by accepted
  linear-algebra premises; this note attacks forcing of the channel/direction weight ratio by the
  tested carrier/entropy/records routes. The match is the weight-freedom shape, not a claim that the
  Frobenius row already audited the new carrier note.
- **N5 rhetoric audit:** "not a new freedom" means "not independent of the partition-weight ratio."
  It does not mean no future dynamics can derive `t=1/2`.
- **N6 partial-closure scan:** a retained derivation of the 2-sector readout, a records/einselection
  bridge, or a convention/audit repair that makes the coarse-graining source-authoritative would
  retire the residual without adding an axiom.
- **N7 steelman:** an emergent-time dynamics could make the binary readout physically inevitable and
  then compute `t=1/2`; that would defeat the open residual while preserving the identity
  `beta*gap=-ln t`.
- **N8 cross-cycle echo:** the tracial carrier note and the 2026-06-02 flow notes already name the
  same carrier/records partition gate. This note collapses their duplicated language; it does not
  close the gate.

## Verdict

**The specific finite-beta weight (`beta*gap=ln2 -> r=1/2`) remains an open selection.** Its
sharp content is that the temperature is **not an independent posit**: by `beta*gap = -ln t` it is
the same scalar as the 2-sector-vs-3-direction weight ratio, whose unconstrained form matches the
retained Frobenius isotype-weight freedom. The unconstrained / tracial default (no partition elected, full-algebra max-entropy) is
`r=1` (`Q=1`); reaching `r=1/2` requires electing the 2-sector coarse-graining = the finite-beta
structure = the cyclic-vector binary readout -- one and the same weight-ratio choice. The value-lane
residual is shared with the carrier/CAR/emergent-time partition gate.

## Falsifiable content (kept)

Channel-counting gives `r=1/(N-1)` at each `N` (`Z_N`: `||I||^2=N`, `||J-I||^2=N(N-1)`), tying `r=1/2`
to the derived `n_gen=3`; a dynamics that supplied a different gap would break this N-scaling -- a
structural cross-check on any future dynamical derivation, independent of how the ratio is named.

## Decoupling from the chirality no-go

`r=1/2` sits at `[H,S]=0` and `H` does not anticommute with `Gamma_chi=(2/3)J-I`, so this note introduces
no chiral operator and does not trip `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`
(retained_bounded). The value-lane reduction is structurally decoupled from the generation-chirality
gate.

## Non-circularity

`r=1/2` / `Q=2/3` are never inputs to a forcing claim; they appear only as the OUTPUT of an
externally chosen weight/partition and are used solely as check targets. The unconstrained default
is shown to be `r=1`; `Delta=1` and `rho=I/3` are computed upstream of any Koide value.

## Tiers verified on `origin/main` (`.rows[claim_id].effective_status`)

| claim_id | effective_status | role here |
|---|---|---|
| [`koide_frobenius_isotype_split_uniqueness_note_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md) | `retained_no_go` | one-parameter weight freedom support |
| [`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained` | `Q=1/3+(2/3)r` |
| [`charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained` | `Q=2/3 <=> r=1/2` |
| [`koide_q23_block_weight_frontier_bounded_note_2026-05-29`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md) | `retained_bounded` | block-weight algebra |
| [`luders_rule_from_composition_consistency_note_2026-05-20`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md) | `retained_bounded` | `r->2r^2` records flow |
| [`koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) | `retained_bounded` | chirality decoupling |
| [`flavor_missing_axiom_carrier_measure_note_2026-05-30`](FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md) | `unaudited` | context (carrier fork) |
