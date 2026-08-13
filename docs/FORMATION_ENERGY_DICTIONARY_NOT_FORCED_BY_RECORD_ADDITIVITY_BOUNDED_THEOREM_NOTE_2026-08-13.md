---
claim_id: formation_energy_dictionary_not_forced_by_record_additivity_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Record additivity on disjoint formation cells supplies only the constant union readout I({s,d})=1; that single scalar cannot equal the declared energy-image r=(1-w)/(2w) on {w=1/3,w=1/2}, and equally additive alternative dictionaries assign different r pairs, so the dictionary is not forced."
upstream_dependencies:
  - minimal_axioms
  - koide_formation_gate_relocation_tied_measure_per_cell_weight_compatibility_bounded_theorem_note_2026-07-12
runner: scripts/formation_energy_dictionary_not_forced_by_record_additivity_2026_08_13.py
---

# Formation Energy Dictionary Not Forced By Record Additivity

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact rational algebra of the two-cell channel split versus
formation-weight energy shares; Record additivity on the disjoint union.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/formation_energy_dictionary_not_forced_by_record_additivity_2026_08_13.py`](../scripts/formation_energy_dictionary_not_forced_by_record_additivity_2026_08_13.py)

## Result Up Front

The July 12 formation-gate relocation note
[`KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
declares, rather than derives, an energy-to-formation-state bridge. Residual
Atom 2 of that source states that the identification

`E_s = w E_tot`, `E_d = (1-w) E_tot`

against the first-order channel split `E_s = 3 a^2`, `E_d = 6 |b|^2` is
"this note's own declared modeling element" and "is not supplied by the Record axiom".
Conditional on that declaration one has the bijection

`r = (1-w)/(2w)`, `w = 1/(1+2r)`

for `E_tot>0` and `0<w<1`. Downstream notes consume the map at declared-
modeling grade. This note does not install the dictionary and does not
derive `r=1/2`.

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies a
single additive scalar on finite pairwise-disjoint record collections:

> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

If the two cells are typed as disjoint record collections with formal
strengths `I(s)=w` and `I(d)=1-w`, additivity supplies only `I({s,d})=1`,
the same for every `w`. The union scalar is not a physical energy dictionary.

Four exact statements locate the gap.

1. **Declared solve.** Conditional on the declared map `D_*` and on
   `a^2>0`, `E_tot>0`, `0<w<1`, the channel split inverts to
   `a^2 = w E_tot / 3`, `|b|^2 = (1-w) E_tot / 6`,
   `r=(1-w)/(2w)`, and `w = 1/(1+2r)`. Special points:
   `w=1/2` gives `r=1/2`; `w=1/3` gives `r=1`. This is exact algebra of the
   declared map, not a derivation that the map is physical.
2. **Alternative dictionaries disagree.** At `E_tot=1`, the four share maps
   `D_*`, `D_eq`, `D_dim`, and `D_inv` assign the `r` pairs
   `(1,1/2)`, `(1/2,1/2)`, `(1,1)`, and `(1/4,1/2)` at the lawful weights
   `{w=1/3,w=1/2}`. Equal-share and carrier-dimension maps are not bijections
   `w ↔ r`. Inverse share is a different bijection, equal to `D_*` only at
   `w=1/2`. Therefore `r=(1-w)/(2w)` is dictionary-dependent.
3. **Record additivity cannot select a dictionary.** The union readout is
   `I({s,d})=1` at both lawful `w`. Any function of that one scalar is
   constant on the menu. It cannot equal the declared image
   `{1, 1/2}` and cannot distinguish `D_*` from the constant-`1/2` equal-share
   map.
4. **Scoped negative.** There is no function of the single additive scalar
   `I({s,d})` that equals the declared energy-image `r=(1-w)/(2w)` on
   `{w=1/3, w=1/2}`. Record additivity does not force `D_*`.

This is a scoped algebraic obstruction. It does not say that no energy
dictionary exists, and it does not say that `r=1/2` is impossible.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The declared-dictionary solve, the four-dictionary r table, and the I-union obstruction are exact rational identities on declared two-cell objects. Record additivity supplies only the constant I({s,d})=1 and cannot select D_*. A later formation-to-energy bridge remains open."
trace_class: negative_route_pruning
target_claim_id: koide_energy_dictionary_r_from_w
target_blocker_text: "derive the energy dictionary r=(1-w)/(2w) or prove an exact obstruction"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "A physical formation-to-energy bridge remains open; do not adopt the declared dictionary or axiom text."
conditional_surface_status: "exact for alternative-dictionary rejectors and the I-union obstruction; a later dynamics bridge remains live"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Channel energies are quoted as declared common objects and recomputed here:

```text
E_s = 3 a^2,   E_d = 6 |b|^2,   E_tot = E_s + E_d,
r := |b|^2 / a^2 = E_d / (2 E_s)   (when a^2>0).
```

A formation state is a weight `w ∈ (0,1)` on the two-cell menu `{s,d}`.

The **declared dictionary** `D_*` is the share map

```text
D_*(w, E_tot) = (w E_tot, (1-w) E_tot).
```

Three **alternative dictionaries**, all compatible with `E_s+E_d=E_tot`, are
used only as rejectors:

- Equal share `D_eq`: `(E_tot/2, E_tot/2)`, independent of `w`.
- Carrier-dimension `D_dim`: `(E_tot/3, 2 E_tot/3)`, independent of `w`.
- Inverse share `D_inv`: `((1-w) E_tot, w E_tot)`.

The energy-image of a dictionary `D` is

`r_D := E_d / (2 E_s)`

computed from the pair `D(w, E_tot)`. The lawful comparison weights are the
July 12 special points `w=1/3` and `w=1/2`.

If the two cells are typed as disjoint record collections with formal
strengths `I(s)=w` and `I(d)=1-w`, Record additivity and `I(empty)=0` give

`I({s,d})=I(s)+I(d)=1`

for every `w`. A **function of the union scalar** is any map of the form
`f(I({s,d}))`.

## Exact Target And Obligation Graph

**Exact target.** Decide whether Record additivity plus the channel split
force the declared shares `D_*` and the formula `r=(1-w)/(2w)`, by comparing
equally additive alternatives and by testing whether any function of
`I({s,d})` can match the declared image on the lawful pair.

| Obligation | Role | Disposition |
|---|---|---|
| pin Record additivity and `I(empty)=0` | premise | quoted from the axiom memo |
| pin Residual Atom 2 as a declared modeling element | premise | quoted from the July 12 relocation note |
| invert `D_*` against the channel split | Theorem 1 | exact algebra of the declared map |
| compute `r_D` for `D_*`, `D_eq`, `D_dim`, `D_inv` | Theorem 2 | four-dictionary table |
| show `I({s,d})=1` for every `w` | Theorem 3 | additivity |
| reject any function of that one scalar as `r_{D_*}` | Theorem 4 | common union `1`, images `1` and `1/2` |
| derive a physical formation-to-energy bridge | autonomous closure | open |
| claim no dictionary exists, or that `r=1/2` is impossible | non-claim | not attempted |

## Theorem 1 — Declared Solve

**Claim.** Conditional on `D_*` and on `a^2>0`, `E_tot>0`, `0<w<1`,

```text
a^2 = w E_tot / 3,
|b|^2 = (1-w) E_tot / 6,
r = (1-w)/(2w),
w = 1/(1+2r).
```

In particular `w=1/2` gives `r=1/2` and `w=1/3` gives `r=1`.

**Proof.** The declared shares and the channel split are the two equations

```text
3 a^2 = w E_tot,          6 |b|^2 = (1-w) E_tot.
```

The unique solution with `E_tot>0` and `0<w<1` is the displayed pair
`(a^2, |b|^2)`. Their ratio is

```text
r = |b|^2 / a^2
  = ((1-w) E_tot / 6) / (w E_tot / 3)
  = (1-w)/(2w).
```

The same ratio is the energy-image identity

```text
r = E_d / (2 E_s) = ((1-w) E_tot) / (2 w E_tot) = (1-w)/(2w).
```

Solving `r = (1-w)/(2w)` for `w` gives `2 r w + w = 1`, hence
`w = 1/(1+2r)`. Substituting the lawful points:

```text
w = 1/2  =>  r = (1/2) / 1 = 1/2,
w = 1/3  =>  r = (2/3) / (2/3) = 1.
```

This is exact algebra of the declared map. It is not a derivation that the
map is physical.

## Theorem 2 — Alternative Dictionaries Disagree

**Claim.** Fix `E_tot=1`. For `w=1/3` and `w=1/2` the energy-images
`r_D := E_d/(2 E_s)` are

| D | w=1/3 | w=1/2 |
|---|---|---|
| `D_*` | `1` | `1/2` |
| `D_eq` | `1/2` | `1/2` |
| `D_dim` | `1` | `1` |
| `D_inv` | `1/4` | `1/2` |

So `D_eq` and `D_dim` are not bijections `w ↔ r`. `D_inv` is a different
bijection: `r = w/(2(1-w))`, equal to `D_*` only at `w=1/2`. Therefore the
formula `r=(1-w)/(2w)` is dictionary-dependent.

**Proof.** Direct substitution at `E_tot=1`.

- `D_*(1/3,1)=(1/3,2/3)` gives `r=(2/3)/(2·1/3)=1`.
- `D_*(1/2,1)=(1/2,1/2)` gives `r=(1/2)/(2·1/2)=1/2`.
- `D_eq(any,1)=(1/2,1/2)` gives `r=(1/2)/(2·1/2)=1/2`.
- `D_dim(any,1)=(1/3,2/3)` gives `r=(2/3)/(2/3)=1`.
- `D_inv(1/3,1)=(2/3,1/3)` gives `r=(1/3)/(4/3)=1/4`.
- `D_inv(1/2,1)=(1/2,1/2)` gives `r=1/2`.

For inverse share the general identity is

`r = w / (2(1-w))`.

Setting this equal to `(1-w)/(2w)` forces `(1-w)^2 = w^2`, hence `w=1/2` in
`(0,1)`. The two bijections therefore meet only at that one point. Equal
share and carrier-dimension share ignore `w`, so they cannot invert a
varying formation weight.

## Theorem 3 — Record Additivity Cannot Select A Dictionary

**Claim.** Typing `I(s)=w` and `I(d)=1-w` on disjoint cells, one has
`I({s,d})=1` for every `w`. Any function of that one scalar is constant on
the menu. It cannot equal `r_{D_*}(w)` at the two lawful weights, whose
images are `1` and `1/2`, and it cannot distinguish `D_*` from `D_eq`,
whose image is the constant `1/2`.

**Proof.** The cells are disjoint by typing, so Record additivity gives

`I({s,d})=I(s)+I(d)=w+(1-w)=1`.

The same identity holds at `w=1/3` and at `w=1/2`. A function `f` of the
single union scalar therefore returns one value `f(1)` at both lawful
weights.

The declared images are not one value: Theorem 1 gives `r_{D_*}(1/3)=1` and
`r_{D_*}(1/2)=1/2`. No single number `f(1)` can equal both. The equal-share
images are the constant `1/2`, which agrees with `D_*` at `w=1/2` and
disagrees at `w=1/3`. Discriminating rejector: the single Record datum on
the union is the same at `w=1/3` and `w=1/2`, while `D_*` and `D_eq`
assign different `r` pairs. The inverse-share image `1/4` at `w=1/3` is
the extra rational witness that a third additive dictionary is available.

## Theorem 4 — Scoped Negative (N-gate)

**Claim.** There is no function of the single additive scalar `I({s,d})`
that equals the declared energy-image `r=(1-w)/(2w)` on `{w=1/3, w=1/2}`.
Record additivity does not force `D_*`.

**Proof.** Theorem 3 already records that `I({s,d})=1` at both lawful
weights, while the declared images are `1` and `1/2`. A function of one
scalar cannot take two values at one argument. The four share maps of
Theorem 2 are equally compatible with `E_s+E_d=E_tot`; additivity of `I`
does not prefer `D_*` among them.

**Scope.** The negative is restricted to functions of the union scalar, and
to the claim that Record additivity forces `D_*`. It does not address a
two-argument readout of the cells, a later formation-dynamics bridge, or
the existence of some other energy dictionary. It does not say that
`r=1/2` is impossible.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- install `D_*`, or identify it with a physical Record law;
- claim that no energy dictionary exists;
- claim that `r=1/2` is impossible;
- derive a formation dynamics, a formation site, or a formation rate;
- exhaust other two-cell maps.

The declared map remains a modeling element of the July 12 source. The
present obstruction is only that Record additivity plus the channel split
do not force those shares. Independent audit is required. This note authors
no audit verdict.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record additivity sentence and `I(empty)=0` | premise | quoted; no edit |
| July 12 Residual Atom 2 energy dictionary | declared modeling element | quoted; not installed |
| channel split `E_s=3 a^2`, `E_d=6 |b|^2` | common objects | restated and recomputed |
| four share maps and the `r` table | declared algebra | computed here |
| physical formation-to-energy bridge | escape route | live, not derived |

The exact advance is a finite additivity-versus-dictionary theorem.
Independent audit remains required before any effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | Residual Atom 2 of the July 12 relocation note states that the identification `E_s=w E_tot`, `E_d=(1-w) E_tot` is "this note's own declared modeling element" and "is not supplied by the Record axiom". This note supplies the matching obstruction with explicit alternative dictionaries. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for energy dictionary, Residual Atom 2, and `r=(1-w)/(2w)`. Hits: the July 12 relocation note declares the map; the July 12 selection note solves it conditionally; the occupancy-grain correspondence and the r-half backlog consume it as unadopted. No landed alternative-dictionary rejector or Record-additivity obstruction for `D_*` appears on that commit. |
| V3 | Independently checkable? | Textbook share maps do not mention the Koide channel split `E_s=3a^2`, `E_d=6|b|^2`, the lawful pair `{1/3,1/2}`, or Residual Atom 2. The runner recomputes the four dictionaries and the union readout in exact rational arithmetic. |
| V4 | More than a restatement? | Yes: the exact `r` table `1` versus `1/2` versus inverse-share `1/4`, and the fact that union `I=1` cannot separate the two lawful `w`. |
| V5 | One-step relabel? | No. The claim is not a restatement of Residual Atom 2's declaration. Closest is the declaration itself; this note adds rejector dictionaries and the additivity obstruction. |

## No-Go Discipline Gate (Theorem 4 only)

The negative claim is restricted to this: no function of `I({s,d})` equals
the declared `r(w)` on `{1/3,1/2}`, and Record additivity does not force
`D_*`. The gate does not ship a global non-existence theorem.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| declared `D_*` as algebra | invert `E_s=w E_tot` against `E_s=3 a^2` | Theorem 1: the solve is exact and is not forced | **ATTEMPTED** |
| equal share `D_eq` | set `(E_s,E_d)=(E_tot/2,E_tot/2)` | Theorem 2: constant `r=1/2`, distinct from `D_*` at `w=1/3` | **ATTEMPTED** |
| carrier-dimension `D_dim` | set `(E_s,E_d)=(E_tot/3,2 E_tot/3)` | Theorem 2: constant `r=1`, distinct from `D_*` at `w=1/2` | **ATTEMPTED** |
| inverse share `D_inv` | swap the declared weights | Theorem 2: different bijection `r=w/(2(1-w))` | **ATTEMPTED** |
| two separate `I` readouts of the cells | use `I(s)` and `I(d)` as two arguments | an escape from Theorem 4, not a function of the union scalar | **ATTEMPTED** (escape) |
| formation dynamics supplying shares | derive `E_s=w E_tot` from a formation rule | live escape; not derived here | **ATTEMPTED** (escape) |
| axiom-text addition as a selector | treat an axiom edit as forcing `D_*` | forbidden by the no-edit surface; see N6 | **RULED OUT** |

### N2 — wall independence

Theorem 4 closes only functions of the union scalar, and only the claim
that Record additivity forces `D_*`. It does not close two-argument
readouts, formation dynamics, or some other independently justified
dictionary. Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| channel split `E_s=3 a^2`, `E_d=6 |b|^2` | quoted common object; recomputed |
| `D_*` | explicit declared map; not derived |
| `D_eq`, `D_dim`, `D_inv` | explicit rejectors |
| typing `I(s)=w`, `I(d)=1-w` | formal strengths on disjoint cells |
| lawful pair `{1/3,1/2}` | July 12 special points; comparison set of Theorem 4 |
| formation dynamics | open; not assumed |
| observations or empirical frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Record additivity sentence and `I(empty)=0` | quoted as premises only; no edit |
| July 12 relocation note, Residual Atom 2 | identification `E_s=w E_tot`, `E_d=(1-w) E_tot` as a declared modeling element, not supplied by the Record axiom | quoted; the present obstruction is new |

No citation is used as authority for the four-dictionary table or the
I-union collision; those are proved here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the two cells `{s,d}` and the four share maps | no classification of every energy map |
| per site | one two-cell formation menu | no composite carrier theorem |
| per mode | the channel split `E_s=3 a^2`, `E_d=6 |b|^2` | no spectral-mode exhaustion |
| per block | I-union obstruction and alternative-dictionary rejectors only | no formation dynamics |
| lattice-wide | checked and not executed | no lattice-wide no-go |

The obstruction is two-cell / union-scalar; it is not lattice-wide.

### N6 — live partial-closure paths

1. Two separate `I` readouts of the cells, which is a two-argument map and
   not a function of the union scalar.
2. A later formation-dynamics bridge that supplies energy shares.
3. Some other dictionary, including `D_eq`, `D_dim`, or `D_inv`, if
   independently justified.

No axiom sentence is required by the I-union obstruction. Those paths
remain live.

### N7 — hostile steelman

> Once one names energy shares equal to formation weights, the dictionary
> is tautological.

**Answer.** Naming is the declaration. Theorem 4 shows that Record
additivity does not perform that naming, and Theorems 2–3 exhibit equally
additive alternatives.

### N8 — cross-cycle echo

July 12 Residual Atom 2 is a declaration that the identification is a
modeling element and is not supplied by the Record axiom. The July 12
selection note solves the declared map conditionally. Occupancy-grain and
r-half backlog notes consume the map as unadopted. The present negative is
a different residual: the union scalar cannot equal the declared image, and
equally additive dictionaries disagree. The declaration is not the
obstruction.

**Gate disposition.** PASS for the scoped obstruction. FAIL / DO NOT SHIP
for "no dictionary exists" or for "`r=1/2` is underived from this note
alone as a universal no-go".

## Primary Runner

[`scripts/formation_energy_dictionary_not_forced_by_record_additivity_2026_08_13.py`](../scripts/formation_energy_dictionary_not_forced_by_record_additivity_2026_08_13.py)
recomputes the declared solve, the four-dictionary `r` table, the union
readout `I({s,d})=1`, and the I-union obstruction in exact rational
arithmetic. Identity gates call `declared_shares` and `r_from_energies`;
replacing `declared_shares` by `D_eq` fails `w=1/3 => r=1`, replacing it by
`D_dim` fails `w=1/2 => r=1/2`, and replacing `r_from_energies` by the
constant `1/2` fails the `w=1/3` declared image.
