# Occupancy-Grain Universality over the Admissible Record-Write Class: Bounded Theorem

**Date:** 2026-07-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/acphilambda_occupancy_grain_rule_class_universality_2026_07_11.py`](../scripts/acphilambda_occupancy_grain_rule_class_universality_2026_07_11.py)
**Cache:** [`logs/runner-cache/acphilambda_occupancy_grain_rule_class_universality_2026_07_11.txt`](../logs/runner-cache/acphilambda_occupancy_grain_rule_class_universality_2026_07_11.txt)

## Purpose

This note proves a bounded occupancy-grain statement over the admissible
controlled-copy record-write class. Conditional on one named supplied K/CPT
2-sector occupancy context, it identifies the unique interior stationary
weight of every sector-exchange-symmetric strict-sharpening record-influence
update and converts that weight to the equal-power-per-block grain `r=1/2`.
It quantifies over the class; it neither chooses a record-formation rule nor
asserts which occupancy a realized state registers.

## Supplied-context declaration

> **Declared supplied context — `charged_lepton_k_cpt_2_sector_occupancy_context`.**
> The charged-lepton 2-sector occupancy surface is the K/CPT-orbit partition
> `{singlet sector, doublet orbit}` with occupancy distribution `(p_s,p_d)`,
> `p_s+p_d=1`, where the equal-power-per-block grain reads `r=1/2` at
> `p_s=p_d`. This is the landed adoption's Candidate 1 occupancy wording
> together with the custody L9 equipartition cell. The identification is
> supplied per the K/CPT supplied-context bridge pattern; it is not derived
> here, and every claim below is conditional on it.

This is the note's one named supplied context. The declared Record-clause
reading in L1 and the operative meaning of strict sharpening in L3 are stated
openly below; neither is a derivation of the supplied K/CPT partition.

## Theorem

Write `q:=p_d`, so `1-q=p_s`, on the supplied closed 2-sector simplex
`0<=q<=1`.

### L1. Permanence implies stationarity

The consumed Record clauses are, verbatim:

> “A site never carries more than one record; records are permanent.”
>
> “Only records are readable. A readout value is determined by record content
> alone.”
>
> “For any finite collection of pairwise-disjoint records, scalar readout `I`
> is additive, with `I(empty)=0`.”

At this surface, this note makes the following **declared reading** of those
clauses. The registered two-sector occupancy weight is itself permanent record
content. Additivity and `I(empty)=0` give its normalized two-content readout

```text
R(q) = (1-q) I_s + q I_d,
```

where the two readable contents are nondegenerate, `I_s != I_d`. If an
admissible continued-registration update `T` moved the permanently registered
weight, the same record would instead read

```text
R(T(q)) - R(q) = (T(q)-q)(I_d-I_s) != 0.
```

Its value would then depend on when it was read, not on record content alone.
Under this declared surface reading, permanence plus content-determined
readout therefore requires

```text
T(q)=q.
```

Thus a durably registered two-sector weight must be a fixed point of every
admissible continued-registration update. U2 checks the implication
mechanically, including an exact moved-weight witness. The nondegenerate
two-content reading is load-bearing: a scalar readout with `I_s=I_d` would not
detect movement of `q`.

### L2. The class gives sector-exchange-symmetric strict sharpening

The sibling class theorem
[`RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md`](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md)
classifies every admissible blank-input one-step write, under its declared
readings, into the controlled-copy isometry class. Its R5 statement is:
“The class is therefore one register-unitary orbit, with column phases
included in `U_R`.”

On the supplied orbit-constant 2-sector partition, this note takes the
following **declared record-influence reading** of continued registration at
this surface (the same declared-reading discipline as L1; the repeat-write
computation in U3 exhibits membership, it does not derive exhaustiveness):
the normalized record influence of a continued-registration rule in that
class has the form

```text
T_f(q) = f(q) / (f(q)+f(1-q)),
f : [0,1] -> [0,1],
f continuous and strictly increasing,  f(0)=0.
```

Here an admissible **continued-registration** rule is a recording update: its
off-center action strictly amplifies the majority sector in the sense stated
in L3. The identity family in N2 is non-recording dynamics and is therefore a
negative control outside that recording-update hypothesis.

The same `f` acts on both sectors. Indeed, a pair `f_s != f_d` would carry a
sector-distinguishing parameter. Such a parameter would be a `C_3/K`-breaking
selector, while the class has only its register-basis orbit and the supplied
partition is K/CPT-orbit-constant. Consequently

```text
T_f(1-q)=1-T_f(q).
```

No particular `f` is selected. The repeat-write Lüders record-influence
exemplar multiplies each initial sector influence by the same sector influence
once more:

```text
(q,1-q) -> (q^2,(1-q)^2),
Z=q^2+(1-q)^2,
T_2(q)=q^2/Z.
```

It is the `k=2` member of the symbolic power subfamily

```text
f_k(q)=q^k,
T_k(q)=q^k/(q^k+(1-q)^k),  k>1.
```

The general family remains `T_f`; the power profiles are exact witnesses, not
a choice of record rule.

### L3. Universal fixed-point set

For this lemma, **strict sharpening** has its majority-amplification meaning:

```text
T_f(q) < q  for 0<q<1/2,
T_f(q) > q  for 1/2<q<1.
```

Equivalently, with input odds `O(q)=q/(1-q)` and influence odds
`F(q)=f(q)/f(1-q)`, strict sharpening means

```text
F(q) < O(q)  for 0<q<1/2,
F(q) > O(q)  for 1/2<q<1.
```

The ratio `F(q)` is strictly increasing because `f(q)` strictly increases
while `f(1-q)` strictly decreases. **FLAG — operative strictness and
admissibility:** strict increase of `F` by itself is not the amplification
inequality; the identity profile `f(q)=q` has strictly increasing odds but is
N2 below. This note reads an admissible continued-registration update as the
off-center-amplifying recording update described in L2. That hypothesis is
load-bearing.

For every update in the L2 family with that strict sharpening, the fixed-point
set on the closed simplex is exactly

```text
Fix(T_f) = {0, 1/2, 1}.
```

First, strict increase and `f(0)=0` give `f(1/2)>0` and `f(1)>0`. Hence

```text
T_f(0)   = f(0)/(f(0)+f(1))         = 0,
T_f(1/2) = f(1/2)/(2 f(1/2))        = 1/2,
T_f(1)   = f(1)/(f(1)+f(0))         = 1.
```

For an interior `q`, a fixed point would require

```text
f(q)/(f(q)+f(1-q)) = q
<=> f(q)(1-q) = q f(1-q)
<=> F(q) = O(q).
```

That equality fails strictly below and above `1/2` by majority amplification.
Thus there is no other interior fixed point. This is the general monotone
argument; it does not depend on a rule choice. U4 also checks the exact power
family equation

```text
q^k(1-q) = q(1-q)^k
```

for `k in {2,3,5/2,4}`. In each case the exact solution on `[0,1]` is only
`{0,1/2,1}`.

It remains to translate the unique interior point from occupancy to the
equal-power-per-block grain. Starting from the two block powers, rather than
importing the answer, set

```text
P_s = a^2,
P_d = 2|b|^2,
r   = |b|^2/a^2.
```

Then

```text
p_d = P_d/(P_s+P_d)
    = 2|b|^2/(a^2+2|b|^2)
    = 2r/(1+2r).
```

Therefore

```text
p_d=1/2
<=> 2r/(1+2r)=1/2
<=> 4r=1+2r
<=> r=1/2.
```

The reverse substitutions are exact, so `p_d=1/2 <=> r=1/2`.

### Bounded conclusion

Conditional on `charged_lepton_k_cpt_2_sector_occupancy_context`, L1 requires
a durable interior registration to be stationary, L2 makes every admissible
continued-registration rule sector-exchange-symmetric with no
sector-distinguishing selector, and L3 gives the same unique interior fixed
point for every strict-sharpening member. Hence the unique interior
durably-registrable occupancy is

```text
p_s=p_d=1/2,
```

which is exactly the equal-power-per-block grain `r=1/2`. This is universal
over the admissible record-write class at this supplied surface: no rule choice
enters.

The adopted premise `ac_orbit_occupancy_statistical_grain_premise` has the
following Candidate 1 text, quoted verbatim:

```text
For the AC_phi_lambda charged-lepton matter-action surface, the physical
statistical grain is the K/CPT orbit or holomorphic-pair occupancy grain:
the doublet contributes once per K/CPT orbit rather than once per sector or
channel. This premise supplies only the matter-action occupancy grain needed
to discharge the surviving AC(i) measure-side realization binary.
```

At this surface, that adopted premise is therefore a rule-class-universal
theorem conditional on the named supplied context, rather than a
rule-dependent selection.

**Consequence (named, not executed):** a registry action retiring that adopted
atom by retained derivation is available to a future gated, owner-approved
registry lane; this note does not execute or request it.

## Negative controls

### N1. Sector-asymmetric influence

Let the singlet and doublet carry different profiles,

```text
f_s(x)=x^2,  f_d(x)=x^3,
T_asym(q)=f_d(q)/(f_d(q)+f_s(1-q))
         =q^3/(q^3+(1-q)^2).
```

The exact interior fixed point is

```text
q=(sqrt(5)-1)/2,
```

not `1/2`; indeed `T_asym(1/2)=1/3`. Sector-exchange symmetry is therefore
load-bearing. This is exactly where the supplied K/CPT partition's
orbit-constancy enters. Without it, the grain is not forced.

### N2. Non-sharpening influence

For `f(q)=q`,

```text
T_f(q)=q/(q+(1-q))=q
```

for every `q in [0,1]`. Every weight is fixed, so strictness is load-bearing;
a non-recording dynamics selects nothing.

### N3. Three-sector Born/dimension contrast

On the per-sector partition, use the analogous symmetric square sharpening

```text
(p_1,p_2,p_3) -> (p_1^2,p_2^2,p_3^2)/(p_1^2+p_2^2+p_3^2).
```

Its unique simplex-interior fixed point is

```text
(p_1,p_2,p_3)=(1/3,1/3,1/3).
```

For the three individual powers

```text
(p_s,p_+,p_-)=(a^2,|b|^2,|b|^2)/(a^2+2|b|^2),
```

uniformity gives `a^2=|b|^2`, hence `r=|b|^2/a^2=1`, not `r=1/2`.
The grain binary—K/CPT orbit versus individual-sector counting—is exactly the
supplied-context choice. This theorem consumes that choice; it does not
collapse or derive it.

## What is not derived

- The K/CPT 2-sector partition, its orbit-constancy, K-reality, or the
  identification of that partition with the charged-lepton occupancy surface
  is not derived. It is the one named supplied context.
- No particular record-formation rule, process, trigger state, site, weight,
  rate, or record-influence profile `f` is selected. The result quantifies over
  the symmetric strict-sharpening family.
- The theorem derives the unique **durable grain**. It does not assert that a
  realized state's registered value is `r=1/2`; that remains registered data.
- No R-eta bridge, `delta`, charged-lepton mass, or `AC_phi_lambda` value is
  derived. No comparator or exactness threshold is introduced.
- No registry edit or registry action is performed or requested.

## Scope boundary

- The mathematical surface is only the supplied closed two-sector simplex and
  the common-`f` record-influence family induced there by the controlled-copy
  class.
- L1 is explicitly a declared reading of permanence, record-only readability,
  and additive scalar readout at this surface. Its nondegenerate content labels
  are load-bearing.
- L3 uses off-center majority amplification as strict sharpening. Bare
  monotonicity of the influence odds is insufficient, as N2 shows.
- The conclusion is unique only in the simplex interior. The two pure-sector
  endpoints are fixed for every admissible `f` and are not equal-power points.
- The narrowed record-formation boundary says, verbatim: “The surviving no-go
  is only: the current minimal axioms do **not** force the formation
  rule/process/state/site/weight/rate.” This theorem is compatible with that
  boundary: it quantifies over the controlled-copy class and selects no rule,
  process, state, site, weight, or rate.
- N3 is an exact contrast, not a competing derivation. It shows why the
  supplied orbit-versus-sector grain choice remains load-bearing.

## Load-bearing dependencies

| Dependency | Consumed content |
|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Supplies the three verbatim Record-clause passages used in L1. The permanence-to-stationarity reading remains declared here rather than imported as a memo theorem. |
| [`RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md`](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md) | Supplies the controlled-copy isometry classification and R5's single register-unitary-orbit statement. This note consumes that class statement as a markdown-link dependency. |
| [`TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md`](TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md) | Supplies Candidate 1, quoted verbatim above, and its boundary: it supplies the matter-action occupancy grain but no value of `r`, probability rule, or sector-weight law. |
| `charged_lepton_k_cpt_2_sector_occupancy_context` | The one declared supplied context: the charged-lepton occupancy surface is the K/CPT-orbit partition `{singlet sector, doublet orbit}`. This identification is consumed, not derived. |
| `record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go` | Boundary context only: occurrence is supplied, while formation rule/process/state/site/weight/rate is not forced. The exact narrowed sentence is quoted in Scope boundary. |
| `charged_lepton_koide_value_full_chain_of_custody:L9` | Orientation-only supplied-context wording: “`r=1/2` characterizes HS **2-sector equipartition** (`‖aI‖²=‖bC+b̄C²‖²`)”; that cell explicitly does not select the coarse-graining physically. |

## Runner verification map

| Block | Exact verification | Result |
|---|---|---:|
| U1 | Flattened-whitespace verbatim checks for permanence, content-determined readability, and additive `I` with `I(empty)=0` | `PASS=3 FAIL=0` |
| U2 | Affine additive readout difference, stationarity implication for nondegenerate content, and an exact moved-weight witness | `PASS=3 FAIL=0` |
| U3 | Repeat-write influence products, exact Lüders normalization, general common-`f` exchange symmetry, and the `k=2` reduction | `PASS=4 FAIL=0` |
| U4 | Three general symbolic fixed points, interior odds equation, exact solves for `k in {2,3,5/2,4}`, and from-scratch `p_d <=> r` arithmetic | `PASS=11 FAIL=0` |
| U5 | N1 asymmetric shifted fixed point, N2 identity family, and N3 exact three-sector uniform contrast with `r=1` | `PASS=7 FAIL=0` |
| U6 | Sibling class and R5 statements, Candidate 1 and its boundary, and the narrowed no-go sentence | `PASS=5 FAIL=0` |

Run:

```text
python3 scripts/acphilambda_occupancy_grain_rule_class_universality_2026_07_11.py
```

Cached run result:

```text
TOTAL: PASS=33 FAIL=0
```

**No check passes by literal stipulation.**
