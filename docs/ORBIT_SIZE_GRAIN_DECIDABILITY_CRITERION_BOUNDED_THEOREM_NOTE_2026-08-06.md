# Orbit-Size Grain-Decidability Criterion (Bounded Theorem)

**Date:** 2026-08-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** proposed_retained
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit outcome, and edits no registry.
**Primary runner:**
[`scripts/frontier_orbit_size_grain_decidability_criterion_2026_08_06.py`](../scripts/frontier_orbit_size_grain_decidability_criterion_2026_08_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_orbit_size_grain_decidability_criterion_2026_08_06.txt`](../logs/runner-cache/frontier_orbit_size_grain_decidability_criterion_2026_08_06.txt)

## Question

The open obligation
[`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
asks which grain the physical charged-lepton matter action implements: count
the `K`/CPT orbit once, or count each sector.

This note does not attempt that question. It asks the prior, structural one:

> On which sectors is the orbit-versus-point grain binary decidable **at all**
> by a readout of the kind the Record axiom supplies?

The answer is a finite dichotomy driven by one integer per sector.

## Setting

Let a finite group act on a finite set of substrate cells with orbits
`O_1, ..., O_m` of sizes `n_1, ..., n_m`. Let `iota` be any orbit-invariant
real weight, `iota_k` its value on `O_k`. The two grains are the two natural
readouts built from the same `iota`:

```text
orbit grain   I_1(iota) = sum_k          iota_k
point grain   I_2(iota) = sum_k  n_k  *  iota_k
```

Orbit-invariance of `iota` is a **supplied condition** of this setting, not a
derived one: it is what "the readout does not separate members of an orbit"
means, stated as a hypothesis.

## Theorem

### T1 — constancy dichotomy (exact)

`I_2 = c * I_1` as functionals — that is, for **every** orbit-invariant
`iota` — for some constant `c`, if and only if all `n_k` are equal; and then
`c = n`.

*Proof.* The difference functional is
`D(iota) = I_2(iota) - c*I_1(iota) = sum_k (n_k - c) * iota_k`. Evaluating on
the indicator weight `e_j` gives `D(e_j) = n_j - c`. So `D` vanishes
identically iff `n_j = c` for every `j`. The indicator evaluations are a
complete finite check, not a sample; the runner performs them on eight
size families. ∎

### T2 — the axioms fix the readout's zero, not its unit

The Record axiom supplies, verbatim:

> "Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`."

A positive rescaling `I -> c*I` preserves content-determination, finite
additivity over pairwise-disjoint collections, and the empty-collection
anchor. No further axiom or approved primitive normalizes `I`. The runner
verifies preservation exactly on a finite family of record collections at
four scale values.

Consequently a **constant** grain factor is not distinguishable by any
axiom-supplied readout property.

### T3 — decidability criterion (T1 + T2)

The orbit-versus-point grain binary is decidable in principle by an
axiom-supplied readout **exactly on sectors whose group action is non-free**,
i.e. whose orbit sizes are not all equal. Where every orbit has the same
size, the two grains differ by a constant, which T2 shows is absorbed into the
readout's free unit.

### T4 — the grain factor is the orbit size

Model a sector as one fixed cell (block power `a^2`) plus one orbit of size
`n` (each member `|b|^2`), and write `r = |b|^2 / a^2`. Adopt the
**equilibration hypothesis**: sector weights equilibrate to the uniform
distribution on the counted cells. That hypothesis is *supplied here, not
derived*; it is stated so that the comparison is between the two grains and
nothing else. Then

```text
orbit grain : 2 cells uniform    ->  a^2 = n|b|^2  ->  r = 1/n
point grain : (1+n) cells uniform ->  a^2 =  |b|^2  ->  r = 1
```

so `r_point / r_orbit = n`. The grain factor on a sector is that sector's
orbit size: `w_sector = |orbit|`. Verified exactly for `n = 2, 3, 4, 5`.

### T5 — the `K`/CPT instance

The `K`/CPT surface has orbit sizes `(1, 2)`: the singlet is fixed, the
doublet pair is exchanged. Non-free, so by T3 the binary is decidable there,
and by T4 the factor is exactly `2`:

```text
orbit grain  r = 1/2 ,  multiplet weight 1/2
point grain  r = 1   ,  multiplet weight 2/3
```

Cross-checked against the block-power parameterisation `p = 2r/(1+2r)` used on
the charged-lepton surface: `p(1/2) = 1/2` and `p(1) = 2/3`, exactly.

## What this buys

The obligation's binary can only ever be settled on sectors with unequal orbit
sizes — that is, at symmetry **fixed points**, where some cell is stabilised
and others are not. On any sector where the action is free, the two grains are
equivalent for every axiom-supplied readout, permanently and as a matter of
kind rather than of difficulty.

That is a scope result for the obligation, not progress on it: it says where
to look and where looking cannot help.

## Relation to the standing non-supply no-go

[`ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md)
(unaudited at the time of writing; status authority is the audit lane)
exhibits two conservative extensions of the same four-axiom model whose
readouts differ by the global factor `F_R = 2 F_C`, and concludes that the
axiom surface does not select between them.

This note is consistent with that result and locates it: a *global* factor is
the uniform-orbit-size case of T1, which T2 absorbs. The present criterion adds
that the *non-uniform* case is not absorbed, and identifies which integer
controls the residue. Nothing here contradicts, re-grades, or reopens that
no-go.

## Non-claims

- This note **selects no grain**. Neither horn is asserted, preferred, or
  ruled out.
- This note **does not close** the AC orbit-occupancy statistical-grain
  derivation obligation, and supplies no part of a closing theorem. The
  obligation's own closure criterion requires deriving the physical matter
  action and its measure; nothing of the sort is attempted here.
- No `r`, `Q`, `delta`, charged-lepton mass, mixing angle, probability rule,
  Born weight, species map, or sector weight is derived.
- The equilibration hypothesis in T4 is supplied, not derived. Without it, T4
  states nothing.
- Orbit-invariance of `iota` is supplied, not derived.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted. The Tier-A count is unchanged.
- The `K`/CPT partition itself, its orbit structure, and its identification
  with the charged-lepton occupancy surface are **not** derived here; T5 is
  conditional on that partition as supplied elsewhere.

## Scope boundary

Finite group, finite cell set, finite orbits, finite record collections —
matching the Record axiom's own finiteness. Real-valued readouts. The theorem
is about functional identity over the full space of orbit-invariant weights;
it says nothing about any particular weight, and nothing about which weight a
realized state registers.

## Reproduce

```bash
python3 scripts/frontier_orbit_size_grain_decidability_criterion_2026_08_06.py
```

Standard library only — `fractions.Fraction` and integers throughout. No
floating point in any load-bearing check, no randomness, no external
dependencies.
