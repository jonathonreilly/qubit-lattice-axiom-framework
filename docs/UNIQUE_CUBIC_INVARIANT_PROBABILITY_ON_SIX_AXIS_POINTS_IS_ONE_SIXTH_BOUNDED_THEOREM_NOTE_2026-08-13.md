---
claim_id: unique_cubic_invariant_probability_on_six_axis_points_is_one_sixth_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the six cubic axis points X={±e1,±e2,±e3}, the unique probability that is invariant under the proper cubic group is the uniform Haar law p(x)=1/6. A preferred-axis point mass is a legal extra selector and is not G-invariant. The statement is a uniqueness theorem for an invariant measure on this six-point set. It is not a universal Bloch radius r=1/2, not a Born kernel, and not an invariant Bloch vector."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unique_cubic_invariant_probability_on_six_axis_points_is_one_sixth_2026_08_13.py
---

# Unique Cubic-Invariant Probability On The Six Axis Points Is 1/6

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact G-invariant probabilities on the six cubic axis points
`X={±e1,±e2,±e3}`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unique_cubic_invariant_probability_on_six_axis_points_is_one_sixth_2026_08_13.py`](../scripts/unique_cubic_invariant_probability_on_six_axis_points_is_one_sixth_2026_08_13.py)
**Parents:** the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `X` be the six axis points of `Z^3`. Let `G` be the proper cubic rotation
group about a site (24 matrices, `det=+1`). Among probabilities
`p: X -> Q_{\ge 0}` with `\sum p = 1`, invariance under `G` forces a unique
law: the Haar (uniform) assignment `p(x)=1/6` at every point.

That uniqueness is a theorem about invariant measures on this finite set. It
does not adopt Haar as a vacuum axiom. A preferred-axis selector such as
`\delta_{e3}` remains a legal probability; it is simply not `G`-invariant.
Admissibility covariance does not force a preferred-axis menu.

This is not a universal Bloch radius `r=1/2`, not a Born kernel, and not the
unique invariant Bloch vector (that object is a vector, not a measure on
`X`). The identity `1/2` is not forced.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Uniqueness of the G-invariant probability on the declared six-point set is proved by transitivity and exact rational arithmetic. Haar is displayed, not adopted as an axiom. No Born kernel, Bloch vector, or vacuum law is derived."
trace_class: uniqueness_on_declared_finite_orbit
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e1=(1,0,0)`, `e2=(0,1,0)`, `e3=(0,0,1)` in `Z^3`, and set

`X = {±e1, ±e2, ±e3}`.

A probability on `X` is a map `p: X -> Q_{\ge 0}` with `\sum_{x \in X} p(x) = 1`.
All arithmetic below is exact in `Q`.

The proper cubic group `G` is the group of `3\times 3` signed permutation
matrices with determinant `+1`. It is the Lattice axiom's proper cubic
rotations about a site. It has 24 elements and acts on `X` by matrix-vector
product. The action is by signed permutations of the three axes.

A probability `p` is `G`-invariant when `p(gx)=p(x)` for every `g \in G` and
every `x \in X`. Equivalently, `p` is constant on `G`-orbits.

The uniform (Haar) assignment on this finite set is the probability
`haar_six` defined by `haar_six(x) = 1/|X|` at every `x`. Because `|X|=6`,
this is the constant value `1/6`. The name "Haar" here means only the unique
normalized counting measure on a finite group orbit. It is displayed as the
invariant law on `X`. It is not written into the axiom memo and is not a
vacuum axiom.

The preferred-axis point mass `\delta_{e3}` is the legal probability with
`\delta_{e3}(e3)=1` and `\delta_{e3}(x)=0` for `x \neq e3`.

## Theorem 1 — Six Points, Transitive Action

`|X|=6`. The group `G` acts transitively on `X`.

Witness. A `+90^\circ` rotation about the third axis,

```text
R_z = [[0,-1,0],[1,0,0],[0,0,1]],
```

sends `e1 \mapsto e2`. The same family of `90^\circ` axis rotations permutes
the three unsigned axes and the two signs, so the orbit of `e1` is all of
`X`. Transitivity follows.

## Theorem 2 — Invariance Forces The Constant Law 1/6

If `p` is `G`-invariant, then `p` is constant on `X`, hence
`p(x)=1/6` for every `x \in X`.

Witness. Transitivity gives `g` with `g e1 = x` for each `x \in X`, so
invariance yields `p(x)=p(e1)`. Thus

`p(e1)=p(e2)=p(e3)=p(-e1)=p(-e2)=p(-e3)`.

Six equal nonnegative rationals summing to `1` are each equal to `1/6`.
Therefore `p = haar_six`.

The same conclusion is the Reynolds average: for any probability `q`,

`(Avg_G q)(x) = (1/|G|) \sum_{g \in G} q(g^{-1} x)`

is `G`-invariant, hence equals `haar_six` by the previous paragraph.

## Theorem 3 — Preferred-Axis Mass Is Legal And Not Invariant

The point mass `\delta_{e3}` is a legal probability: its values are
nonnegative rationals and sum to `1`. It is not `G`-invariant.

Witness. The `90^\circ` rotation about the first axis that sends the third
axis to the second,

```text
R_x = [[1,0,0],[0,0,1],[0,-1,0]],
```

satisfies `R_x e3 = e2`. Invariance would require
`\delta_{e3}(e2)=\delta_{e3}(e3)`, i.e. `0=1`.

Admissibility covariance (one nearest-neighbor rule, covariant under lattice
translations and proper cubic rotations) therefore does not force a
preferred-axis menu. A selector that privileges `e3` is extra structure
beyond the covariant rule.

## Theorem 4 — Lattice And Qubit Display Haar; They Do Not Adopt It

The Lattice axiom supplies proper cubic rotations about each site and states
that no site is privileged. The Qubit axiom states that no possibility is
privileged: possibilities are distinguished by the supplied algebraic
structure alone.

On the six-point set `X`, those two clauses license the symmetry `G` used
above. The unique `G`-invariant probability on `X` is Haar (uniform `1/6`).
A preferred-axis selector (`\delta_{e3}`) is extra.

Display that unique invariant law. Do not adopt Haar as a vacuum axiom. The
axioms do not name a distinguished vacuum measure on `X`, and this note does
not add one. Haar appears here only as the unique solution of the invariance
equation on this declared finite set.

## Theorem 5 — Not Universal `r=1/2`, Not A Born Kernel, Not An Invariant Vector

This uniqueness statement is a statement about probabilities on `X`. It is
not any of the following.

1. **Not universal `r=1/2`.** The invariant value on each of six points is
   `1/6`. The identity `1/2` is a different rational. Forcing `p(e1)=1/2`
   cannot produce a `G`-invariant law: invariance would require
   `p(e1)=1/6`, and a mass `1/2` on a single point cannot be constant on a
   six-point orbit.
2. **Not a Born kernel.** No effect menu, no trace rule, and no
   preparation-to-outcome kernel is derived. The object is a probability on
   six lattice axis points, not a grade on projectors.
3. **Not an invariant Bloch vector.** A Bloch vector is an element of
   `R^3` (or of the ball in that space). The unique rotation-invariant
   *vector* is the zero vector. That is a different mathematical object from
   a probability measure on `X`. The present theorem does not identify, use,
   or replace that vector.

Do not force `r=1/2`.

## Consequence For The Axiom Surface

No axiom is edited. The current memo already names proper cubic rotations and
the no-privileged-possibility clause. Those clauses make `G`-invariance a
well-posed filter on probabilities supported on `X`. The filter has one
solution, displayed above. Preferred-axis menus and Haar-as-vacuum remain
non-axiom extra structure.

### N5 — rhetoric and resolution audit (Theorem 5)

"Unique" in this note means unique among `G`-invariant probabilities on the
declared six-point set `X`. It does not mean unique among all probabilities
on `X` (`\delta_{e3}` is a counterexample). It does not mean unique among
Bloch vectors, unique among Born kernels, or unique among vacuum proposals.

The words "Haar" and "uniform `1/6`" resolve only the invariance equation
`p \circ g = p` on `X`. They do not resolve a Bloch radius, a two-outcome
Born weight, or a vacuum axiom. Theorem 5 is the resolution fence: a reader
who promotes `1/6` to a universal `r=1/2`, to a Born kernel, or to the
zero Bloch vector is reading a different object than the one proved.

Controls that reject `\delta_{e3}` as invariant, and that reject
`p(e1)=1/2` as the unique invariant law, test only those two predicates on
this finite set. They exclude no other measure on a larger space and they
import no unmerged construction.

## Reproduction

```bash
python3 -B scripts/unique_cubic_invariant_probability_on_six_axis_points_is_one_sixth_2026_08_13.py
```

Audit status remains the independent audit lane's responsibility.
