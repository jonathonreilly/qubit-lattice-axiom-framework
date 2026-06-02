# Koide F1: the finite-beta weight giving r=1/2 is the 2-sector PARTITION bit reparametrized, not a new dynamical freedom -- and that bit is a retained no-go

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** structural reduction + an exact reparametrization identity. This note proves
the surviving channel-vs-direction *scoring* residual of the tracial-standard-form carrier is a
single free bit, and that the "finite-beta / temperature" form of that residual
(`KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02`) is the *same* bit as the
2-sector partition choice, by the exact identity `beta*gap = -ln t` with `t = w0/w1 = r`. It does
**not** derive `r=1/2`, does **not** supply a dynamics, does **not** approve any import, and does
**not** set an audit verdict. It is a diagnosis that *collapses* three framings of F1's residual
into one already-open object and grounds that object in a **retained no-go**.
**Primary runner:** [`scripts/koide_finite_beta_weight_is_the_partition_bit_2026_06_02.py`](../scripts/koide_finite_beta_weight_is_the_partition_bit_2026_06_02.py) (SCORECARD PASS=11).

## What this adds

The carrier-scoring note showed the channel-counting weight (`r=1/2`) is provably a finite-beta KMS
weight (`beta*gap=ln2`) that the tracial carrier (`Delta=1`, beta=0) lacks, and concluded F1's residual
"reduces to the emergent-time dynamics -- which finite-beta the dynamics realizes." That phrasing
invites reading the temperature as a *new* continuous degree of freedom the dynamics must supply
on top of the known partition gate. This note shows it is **not** new:

> **Identity.** With per-direction weights `w=(w0,w1,w1)` and the channel-counting balance
> `w0*a^2 = w1*b^2`, one has `r = w0/w1 = t` and `t = exp(-beta*gap)`, i.e. **`beta*gap = -ln t`**.
> Hence **`beta*gap = ln2` (finite-beta on the 3 directions) <=> `t=1/2` <=> beta=0 / uniform on the 2 SECTORS <=> `r=1/2`**,
> while **beta=0 (tracial) <=> `t=1` <=> uniform on the 3 directions <=> `r=1`**. The "temperature" and the
> "2-sector vs 3-direction partition" are two names for the **same one free bit**.

So the carrier-scoring residual and the partition residual of the four 2026-06-02 flow/extremum
notes are **literally the same**, not two reductions. The dynamics is not under-determined by an
extra continuous beta; it must deliver exactly the discrete 2-sector-vs-3-direction coarse-graining --
no more, no less.

## The bit is a retained no-go (the grounding)

`r=1/2` (channel/`t=1/2`) and `r=1` (direction/`t=1`) are two rays of the **one-parameter
Ad-invariant isotype-weight freedom** on `Herm(3)`,
`B_{alpha,beta_F}(A,A) = (alpha+3 beta_F)*Tr(A_s^2) + alpha*Tr(A_t^2)` (scalar/traceless split), positive-definite
for `alpha>0`, `alpha+3 beta_F>0`. `koide_frobenius_isotype_split_uniqueness_note_2026-04-21`
(**retained_no_go** on `origin/main`) proves PD + Ad-invariance + scalar/traceless orthogonality
do **not** force the Frobenius point `beta_F=0`. The finite-beta KMS weight is a reparametrization of
**that** already-open freedom: `beta*gap = ln2` is one interior point, `beta=0` another. The residual is
therefore not a fresh unaudited modular claim -- it is an existing retained no-go in modular dress.

## Why the candidate forcing principles do not pin the bit

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
- **Records/decoherence fixed point (does not land forced).** The retained_bounded Luders flow
  `r->2r^2` has `r=1/2` as an *unstable separatrix*; its thermalizing time-reverse makes `r=1/2`
  stable only on the **2-sector** functional (the 3-direction functional attracts to `r=1`). The
  flow notes themselves reduce to the same 2-sector partition gate (both `unaudited`).

## Verdict

**The specific finite-beta weight (`beta*gap=ln2 -> r=1/2`) is a POSIT -- the temperature is free.** Its
sharp content is that the temperature is **not an independent posit**: by `beta*gap = -ln t` it equals
the 2-sector-vs-3-direction partition bit, which is a **retained no-go** (Frobenius isotype-weight
freedom). The unconstrained / tracial default (no partition elected, full-algebra max-entropy) is
`r=1` (`Q=1`); reaching `r=1/2` requires electing the 2-sector coarse-graining = the finite-beta
structure = the cyclic-vector binary readout -- one and the same free bit. F1's value-lane residual
is exactly that one bit, shared with the carrier/CAR/emergent-time partition gate.

## Falsifiable content (kept)

Channel-counting gives `r=1/(N-1)` at each `N` (`Z_N`: `||I||^2=N`, `||J-I||^2=N(N-1)`), tying `r=1/2`
to the derived `n_gen=3`; a dynamics that supplied a different gap would break this N-scaling -- a
structural cross-check on any future dynamical derivation, independent of how the bit is named.

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
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | `retained_no_go` | **the one-parameter weight freedom = the bit** |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | `retained` | `Q=1/3+(2/3)r` |
| `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10` | `retained` | `Q=2/3 <=> r=1/2` |
| `koide_q23_block_weight_frontier_bounded_note_2026-05-29` | `retained_bounded` | block-weight algebra |
| `luders_rule_from_composition_consistency_note_2026-05-20` | `retained_bounded` | `r->2r^2` records flow |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | `retained_bounded` | chirality decoupling |
| `flavor_missing_axiom_carrier_measure_note_2026-05-30` | `unaudited` | context (carrier fork) |
