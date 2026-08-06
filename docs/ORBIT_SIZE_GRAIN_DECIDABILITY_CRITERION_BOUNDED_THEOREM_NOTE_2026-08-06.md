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

## What this buys

The obligation's binary can only ever be settled on sectors with unequal orbit
sizes — that is, at symmetry **fixed points**, where some cell is stabilised
and others are not. On any sector where the action is free, the two grains are
equivalent for every axiom-supplied readout, permanently and as a matter of
kind rather than of difficulty.

That is a scope result for the obligation, not progress on it: it says where
to look and where looking cannot help.

## Prior art this note does NOT duplicate, and defers to

The two horns themselves, their `r` values, and the `K`/CPT instance are
**already established elsewhere and are not re-derived here**:

- [`ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md`](ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md)
  gives the 2-cell and 3-cell stationary weights and names the two countings
  exactly — "carrier/orbit multiplicities give `w = 1/3`, while quotient-atom
  counting gives `w = 1/2`" — together with the dial coordinates `r = 1/2` and
  `r = 1`.
- [`FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md`](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md)
  gives the `r`-family classification `Q = 1/3` (`r = 0`, degenerate),
  `Q = 2/3` (`r = 1/2`, balanced), `Q = 1` (`r = 1`, hierarchy), the
  positivity endpoint at `r = 1`, and the framing that these are distinguished
  points of one family rather than competing answers.

The only content claimed here is **T1-T3**: the constancy dichotomy, the
readout-unit freedom, and the decidability criterion that follows from them.
That is a statement about *when the binary is settleable by an axiom-supplied
readout at all*, which is a different question from *what the two horns are*.
Readers wanting the horns should cite the two notes above, not this one.

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
- The two grain horns, their `r` values, and the `K`/CPT instance are **prior
  art** (see the section above) and are not claimed here.
- Orbit-invariance of `iota` is supplied, not derived.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted. The Tier-A count is unchanged.
- The `K`/CPT partition itself, its orbit structure, and its identification
  with the charged-lepton occupancy surface are **not** derived, used, or
  relied on here. T1-T3 are stated for an arbitrary finite group action and
  make no reference to any physical sector.

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
