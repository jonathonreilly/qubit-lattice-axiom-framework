# PMNS Commutant Corner-Profile Selector-Map Obstruction

**Date:** 2026-04-16; exact selector-map repair 2026-07-12
**Type:** no_go
**Status:** exact negative boundary
**Script:**
[`frontier_pmns_commutant_eigenoperator_selector.py`](../scripts/frontier_pmns_commutant_eigenoperator_selector.py)

## Question

Do the scalar corner-trace profile of a projected non-`Cl(3)` commutant
operator and the stated Fourier maps

```text
tau(v) = 0 if Re(v_+) >= 0 else 1,
q(v)   = argmax(Re(v_0), Re(v_0)-Re(v_+), Re(v_0)+Re(v_+))
```

derive the PMNS passive offset and sector-orientation labels?

## Bottom line

No, for this scalar profile and these maps.

The exact `hw=1` projector algebra forces every operator lifted from one
corner onto the one-complex-dimensional trace-profile ray

```text
(v_1,v_2,v_3) = (t,t/2,t/2),
(v_0,v_+,v_-) = (2t/3,t/6,t/6),
t = Tr(M).
```

The old extraction maps fail the internal descent test, and two further
finite symmetry diagnostics expose the still-missing bridge:

1. they change under the unsupplied eigenoperator sign choice `M -> -M`;
2. on the three cyclic transports of the demonstrated ray, the `q` map
   returns `(2,1,1)` rather than separating three classes;
3. `Re(v_+)` is even under the corner reflection `v_2 <-> v_3`, while an
   abstract orientation-odd coordinate would change sign.

The `C_3` Fourier decomposition remains exact algebra. What fails is the
claim that the stated formulas are intrinsic to the projected eigenoperator.
The cyclic and reflection calculations are internal corner-space diagnostics;
they are not assumed to be PMNS offset or sector-exchange actions.

## Exact overlap-ray theorem

Conditional on the displayed finite staggered corner construction, let `H_i`
be the three Hermitian `hw=1` corner Hamiltonians at momenta
`(pi,0,0)`, `(0,pi,0)`, and `(0,0,pi)`. The runner constructs them directly
from the staggered sign rule and proves, with exact SymPy arithmetic,

```text
H_i^2 = I,
H_i H_j + H_j H_i = 0       (i != j).
```

Their positive projectors are

```text
Q_i = (I + H_i)/2.
```

For `i != j`, anticommutation gives

```text
Q_i Q_j Q_i = (1/2) Q_i.                    (1)
```

Take any operator `M_tilde` supported at the first corner,

```text
M_tilde = Q_1 M_tilde Q_1,
```

including the demonstrated lift of the projected non-`Cl(3)` commutant
witness. Define the literal corner-trace profile

```text
v_i = Tr(Q_i M_tilde).
```

Writing `t = Tr(M_tilde)`, cyclicity of trace and (1) give

```text
v_1 = t,
v_2 = Tr(Q_1 Q_2 Q_1 M_tilde) = t/2,
v_3 = Tr(Q_1 Q_3 Q_1 M_tilde) = t/2.        (2)
```

Thus the entire scalar profile map on this supported lift has rank one over
the complex numbers. This is stronger than the previous numerical
corner-distinguishing observation: the ratio `(1,1/2,1/2)` is forced and is
independent of the internal matrix entries of `M_tilde`.

## Exact Fourier image

With `omega = exp(2 pi i/3)`, use

```text
v_0 = (v_1 + v_2 + v_3)/3,
v_+ = (v_1 + omega v_2 + omega^2 v_3)/3,
v_- = (v_1 + omega^2 v_2 + omega v_3)/3.
```

Substitution of (2), together with `1 + omega + omega^2 = 0`, gives

```text
(v_0,v_+,v_-) = (2t/3,t/6,t/6).             (3)
```

The nonzero `v_+` on the demonstrated witness is therefore a nonzero trace
overlap on this ray. It is not an independently variable orientation
coordinate.

## Obstruction 1: no eigenoperator-line descent

If `M_tilde` is a commutant eigenoperator, so is `-M_tilde`, with the same
commutation and eigenspace relations. The construction supplies no sign or
phase normalization that distinguishes the two.

For a witness oriented so that `t>0`, (3) gives

```text
(tau,q)(M_tilde)  = (0,2),
(tau,q)(-M_tilde) = (1,1).
```

Therefore the stated maps do not descend to the eigenoperator line. Calling
one sign the selected generator would add exactly the missing normalization
rule; it is not a consequence of the present commutant construction.

## Diagnostic 2: cyclic three-class collapse

Transporting the ray through the three corner anchors cyclically permutes its
profile. For `t>0`, the three profiles are

```text
(t,t/2,t/2), (t/2,t/2,t), (t/2,t,t/2).
```

The stated map returns

```text
q = (2,1,1).
```

It therefore collapses two distinct cyclic transports and is not a
three-class readout on this corner orbit. A phase-sector map built from
`arg(v_+)` could separate the three anchors, but that would be a different
map and would still require a theorem identifying a corner anchor with the
passive-block offset.

This diagnostic does not assume that corner transport acts as passive-offset
shift. The missing intertwiner is precisely why the calculation alone cannot
be promoted to a physical `q` theorem.

## Diagnostic 3: reflection character

For a real profile `(x,y,z)`,

```text
Re(v_+) = (2x-y-z)/6.
```

The corner reflection `S:(x,y,z)->(x,z,y)` exchanges `v_+` and `v_-` but
leaves `Re(v_+)` fixed. Hence the stated `tau` map is reflection-even under
this corner involution. The demonstrated ray is itself fixed by `S`, so it
contains no nonzero corner-reflection-odd scalar datum.

The imaginary part of `v_+` has the correct abstract reflection parity, but
it vanishes on the demonstrated Hermitian profile. Allowing a non-Hermitian
generator does not fix the problem because `M -> exp(i alpha) M` rotates that
phase continuously until an additional phase convention is derived. This
diagnostic likewise does not identify corner reflection with lepton-sector
exchange; that physical intertwiner remains open.

## Theorem statement

**Theorem (narrow obstruction to the stated commutant selector maps).** For
the literal scalar corner-trace profile of an operator lifted from one
`hw=1` corner, the exact profile image is `(t,t/2,t/2)` and its Fourier image
is `(2t/3,t/6,t/6)`. The stated `q/tau` maps change under the unsupplied
replacement `M_tilde -> -M_tilde` and therefore do not descend to the
projected commutant eigenoperator line. Their cyclic and reflection behavior
also fails to supply, by itself, the missing passive-offset and sector-
exchange intertwiners. Therefore the current scalar profile and stated maps
do not internally derive a PMNS selector value law.

## What remains valid

- Every three-vector has the exact `C_3` Fourier decomposition displayed
  above.
- The demonstrated non-`Cl(3)` commutant lift has a nonconstant scalar corner
  profile and nonzero `v_+`.

None of these statements supplies the missing physical readout bridge.

## Explicit non-claims

This theorem does **not** claim:

- that no matrix-valued or enlarged commutant observable can realize a PMNS
  selector;
- that a future carrier/intertwiner theorem is impossible;
- that the displayed corner cycle or reflection is already the physical PMNS
  offset or sector-exchange action;
- that no factorization can exist on a future carrier-constrained physical
  domain;
- that every zero-odd profile lies in the projected `Cl(3)` span;
- any result for the active five-real PMNS source;
- any observed or fitted PMNS value.

A positive reopen must add an observable with enough representation content
and prove all of:

1. normalization/phase descent for its commutant eigenoperator;
2. an intertwiner from corner transport to passive-block offset;
3. an intertwiner from its orientation involution to lepton-sector exchange.

## Audit repair target

This revision addresses the prior independent-audit issue that the computed
Fourier modes were renamed as passive-offset and branch/orientation selectors
without a theorem deriving the readout. The repair does not restore that
positive claim. It proves the exact obstruction for the stated scalar profile
and maps. Independent audit remains required before the repository can treat
this no-go as retained-grade.

## Command

```bash
python3 scripts/frontier_pmns_commutant_eigenoperator_selector.py
```

Expected terminal line:

```text
PASS=30  FAIL=0
```
