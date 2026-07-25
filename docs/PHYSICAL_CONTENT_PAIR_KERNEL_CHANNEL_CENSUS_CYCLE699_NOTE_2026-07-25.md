# The framework's covariance permits exactly five nearest-neighbour two-body couplings, and one of them exists only because the rotations are proper — Cycle 699

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted, and no coupling is selected or given a value.

Runner: `scripts/physical_content_pair_kernel_channel_census_cycle699_2026_07_25.py`
(7 PASS / 0 FAIL, exit 0; exact integer and `Fraction` arithmetic in every
decisive row).

## The question

Cycle 698 classified the content-blind two-body kernel and found exactly one
constant at nearest-neighbour range. But a record does not carry only a
position: it locks one admissible element of the one-site possibility domain,
whose algebraic presentation is `M_2(C)`. Carrying that content through the
same classification turns a qualitative residual — the audit verdicts' "source
action" — into a number.

This cycle counts. It selects nothing.

## The group action is supplied, not chosen

Proper cubic rotations act on displacements by the rotation matrix. They act on
the one-site possibility domain by conjugation with the corresponding spin
element. On the Hermitian real form `C = span_R{I, sigma_1, sigma_2, sigma_3}`
that action is exactly the identity on `I` and the same rotation matrix on the
Pauli vector, so the sign ambiguity of the spin element cancels and every
matrix in the computation is an exact integer. The runner verifies that this
assignment is a homomorphism on the proper cubic group, fixes the identity
component, and has character `1 + tr(R)`.

### Three named conditions, stated rather than claimed

The sentence above should not be read as "nothing was assumed". Three
identifications are load-bearing and none is written in the axiom text:

1. **Rotations act on the possibility domain by spin conjugation.** The
   Admissibility axiom says the nearest-neighbour rule is covariant under
   proper cubic rotations, so rotations do act on the possibility structure;
   that the action is conjugation by the corresponding spin element is the
   natural identification for the `M_2(C)` / `Cl(3,0)` presentation, and it is
   the one used here. It is a named condition, not an axiom sentence.
2. **Contents are taken in the Hermitian real form.** The count is performed on
   `span_R{I, sigma_1, sigma_2, sigma_3}` rather than on all of `M_2(C)`. The
   complex case is a different count and is out of scope.
3. **Record exchange is imposed as `K(-v, o', o) = K(v, o, o')`.** That is the
   condition appropriate to an unordered pair of records. It is reported
   separately from the covariance count throughout, so a reader who rejects it
   can read the 6 instead of the 5.

Every number below is stated against these three conditions. Reject any of
them and the census changes.

## The count

The object counted is a real trilinear form

```text
K : (functions on the 6 face displacements) x C x C -> Q
```

subject to joint covariance `K(Rv, R.o, R.o') = K(v, o, o')`, and separately to
the exchange condition `K(-v, o', o) = K(v, o, o')` that swapping the two
records imposes.

| stage | dimension |
|---|---|
| unconstrained coefficients | 96 |
| after joint cubic covariance | **6** |
| after record exchange as well | **5** |

The 6 is computed twice, independently: once as the exact nullspace of the
covariance system over `Q`, and once as the Burnside character average
`(1/24) sum_R fix_6(R) (1 + tr R)^2`. A linear-algebra count and a
character-theoretic count agree; neither is derived from the other. Without the
rotations all 96 stay free, so the covariance clause is doing the entire
reduction.

## The census

| channel | dimension |
|---|---|
| density–density | 1 |
| density–spin and spin–density | 1 + 1, identified to **1** by exchange |
| spin–spin | 3 |
| **total after exchange** | **5** |

The four channels without exchange sum to exactly 6, matching the full count.
The whole effect of the exchange condition is to identify the two mixed
channels: it leaves the pure channels untouched and takes 6 to 5. The
density–density entry is exactly cycle 698's single content-blind constant,
recovered as a special case.

## The spin–spin basis, exhibited

The runner exhibits three explicit forms, verifies each is exactly invariant
under all 24 proper rotations, and verifies they are linearly independent, so
they are a basis for that channel:

```text
isotropic    S . S'
bond-axis    (S . v)(S' . v)
chiral       v . (S x S')
```

These are the familiar isotropic, pseudo-dipolar, and antisymmetric forms of a
nearest-neighbour bond. That the framework's own covariance produces exactly
this triple, and no fourth, is the content of the count.

## What the word "proper" is doing

The Lattice axiom says *proper* cubic rotations. The chiral form
`v . (S x S')` is invariant under all 24 of them precisely because
`det R = +1`.

As a labelled counterfactual — not a framework claim — the runner extends the
group to all 48 cubic elements with the Pauli vector treated as axial, the
standard choice, and verifies that the extension agrees with the supplied
action on the proper subgroup. Under that extension the chiral coupling is no
longer invariant while the other two survive.

So the axiom's restriction to proper rotations is load-bearing for exactly one
of the five couplings. Improper elements are not implemented by conjugation
with a spin element at all, so extending the group requires choosing how they
act; the counterfactual is offered to isolate the dependence, not to argue for
either group.

**The framework's own improper-action question is already owned elsewhere, and
this note defers to it.**
[Admissibility-rule covariance extension classified](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md)
asks the same proper-versus-full-cubic question on the same six directions, for
the *admissibility rule* rather than for a two-body readout kernel, and it
takes the improper action on rule values to be complex-antilinear, re-earned
from the `Cl(3,0)` presentation. That is a more framework-motivated choice than
the axial convention used above. This note does not compete with it: the
objects differ (rule colorings by a `k`-letter condition alphabet there, a
trilinear form on the Hermitian real form of `M_2(C)` here), and the axial
extension here is labelled a counterfactual precisely because the principled
improper action is that note's subject, not this one's.

## What this does not do

- It does not adopt a source action, select any of the five couplings, fix a
  value, sign, or unit, or claim any of them is realized. The census is a
  budget.
- It does not claim the physical range is nearest-neighbour. At larger range
  the count grows with the octahedral orbit structure of the support ball.
- It does not derive that the two-body extension is licensed at all. Cycle 698
  showed that the additivity clause, read strictly, forbids it; this cycle
  counts what the extension would contain if licensed, and that conditional is
  stated rather than resolved.
- It does not treat the contents as anything but the Hermitian real form. The
  complex case, higher-body terms, and content-dependent range are outside
  scope.
- It repairs no gravity row and no AC obligation, and changes no status.

## Named residuals after this cycle

| residual | state |
|---|---|
| source action | **counted**: 5 independent nearest-neighbour two-body couplings, with an exhibited basis. Values, signs, range, and licensing all remain open. |
| site-anchored readout | shape derived in cycle 698; existence still gated by the additivity reading. |
| reference normalization | untouched; still the object cycle 697 named. |
| carrier | untouched. |

## Scope for independent review

Every decisive equality is exact integer or `Fraction` arithmetic; there is no
floating-point comparison, no sampling, and no fit. The two independent counts
of the same dimension are the principal internal check, and the homomorphism
property of the content action is verified rather than assumed. The three
exhibited forms are checked for invariance against all 24 group elements and
all 54 coefficient positions, not on sampled inputs. The axial extension in the
counterfactual is a named choice and is flagged as such in the runner and here.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
[Cycle 698](PHYSICAL_PAIR_KERNEL_MINIMAL_POSITION_EXTENSION_CYCLE698_NOTE_2026-07-25.md)
is cited for the content-blind classification this cycle generalizes and for
the licensing question it leaves open;
[cycle 697](PHYSICAL_READOUT_POSITION_SCALE_LIMITS_AND_FORCED_LOCAL_LAW_CYCLE697_NOTE_2026-07-25.md)
for the readout limits that motivate the extension. Neither is load-bearing for
this runner's arithmetic. The standard-math analogue for the orbit and
character machinery is
[Cubic-orbit Reynolds projector](CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md),
cited in cycle 698 with the same distinction: it fixes a preferred forward
direction, this lane does not.
