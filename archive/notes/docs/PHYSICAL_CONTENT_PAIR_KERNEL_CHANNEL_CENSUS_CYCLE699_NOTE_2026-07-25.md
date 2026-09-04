# Under four supplied conditions, proper-cubic covariance permits exactly five nearest-neighbour two-body couplings — Cycle 699

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

## The content action is a supplied theorem condition, not framework content

Proper cubic rotations act on displacements by the rotation matrix. This
bounded theorem additionally conditions on their action on the one-site
possibility domain being conjugation with the corresponding spin element. On
the Hermitian real form `C = span_R{I, sigma_1, sigma_2, sigma_3}` that supplied
action is exactly the identity on `I` and the same rotation matrix on the Pauli
vector, so the sign ambiguity of the spin element cancels and every matrix in
the computation is an exact integer. The runner verifies on all `24 x 24`
group-element pairs that the resulting trivial-plus-vector assignment is a
homomorphism, fixes the identity component, and has character `1 + tr(R)`. It
does not derive the spin-conjugation identification from the axioms.

### Four named conditions, stated rather than claimed

The sentence above should not be read as "nothing was assumed". Three
identifications plus one algebraic-class condition are load-bearing, and none
is written in the axiom text:

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
4. **The counted object is a rational, finite-support, linear trilinear form,
   covariant under the stated group.** Rational scalars, linearity in the two
   contents, support on the six face displacements, and covariance are all
   supplied conditions. The Lattice and Qubit axioms supply `Z^3`, its proper
   cubic rotations, and the `M_2(C)` presentation; they do **not** supply these
   four conditions for a downstream physical law, and Record additivity does not
   make a law linear. A prior review of an earlier block in this campaign found
   exactly this conflation, and the correction is applied here.

Every number below is stated against these four conditions. Reject any of them
and the census changes.

The orbit-count and character machinery is standard and is not claimed as new;
`CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md` already
proves that invariant functions are constant on orbit classes and that the
invariant dimension equals the orbit count. What is counted here is a specific
object under a specific supplied action.

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

The 6 is computed twice, independently after the same group and supplied
representation have been fixed: once as the exact nullspace of the
covariance system over `Q`, and once as the Burnside character average
`(1/24) sum_R fix_6(R) (1 + tr R)^2`. A linear-algebra count and a
character-theoretic count agree; neither implementation consumes or encodes
the other's result. They intentionally share the theorem's group/action input,
so agreement does not independently validate that supplied physical
identification. A single-coefficient negative control violates the covariance
equations; the unconstrained coefficient space has 96 coordinates by
definition.

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
under all 24 proper rotations and symmetric under record exchange, and verifies
they are linearly independent, so they are a basis for that channel:

```text
isotropic    S . S'
bond-axis    (S . v)(S' . v)
chiral       v . (S x S')
```

These are the familiar isotropic, pseudo-dipolar, and antisymmetric forms of a
nearest-neighbour bond. That proper-cubic covariance under the four supplied
conditions produces exactly this triple, and no fourth, is the content of the
count.

## Labelled axial full-cubic counterfactual

The Lattice axiom says *proper* cubic rotations. The chiral form
`v . (S x S')` is invariant under all 24 of them precisely because
`det R = +1`.

As a labelled counterfactual — not a framework claim — the runner extends the
group to all 48 cubic elements with the Pauli vector treated as axial, a
standard choice, and verifies that the extension agrees with the supplied
action on the proper subgroup. Under that extension the chiral spin-spin
coupling is no longer invariant while the other two spin-spin forms survive.
The mixed density-spin form is also lost: the displacement is polar while the
Pauli vector is axial, so their scalar product is odd under an improper
element. The exact full-system and channel solves give

| labelled action | density-density | mixed after exchange | spin-spin | total |
|---|---:|---:|---:|---:|
| proper cubic | 1 | 1 | 3 | 5 |
| full cubic, axial Pauli vector | 1 | 0 | 2 | 3 |

Thus this particular axial extension removes two of the five proper-cubic
couplings, the mixed and chiral channels. Improper elements are not implemented
by conjugation with a spin element at all, so extending the group requires
choosing how they act; the counterfactual reports the consequence of that
choice and does not attribute it to framework content or argue for either
group.

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
  showed that the additivity clause, read strictly, excludes an irreducible
  pair term from the scalar readout; it did not exclude a separate action or
  dynamics. This cycle counts what the extension would contain if licensed,
  and that conditional is stated rather than resolved.
- It does not treat the contents as anything but the Hermitian real form. The
  complex case, higher-body terms, and content-dependent range are outside
  scope.
- It repairs no gravity row and no AC obligation, and changes no status.

## Named residuals after this cycle

| residual | state |
|---|---|
| conditional pair-kernel budget | **counted** under the four supplied conditions: 5 independent nearest-neighbour two-body couplings, with an exhibited basis. Values, signs, range, and licensing all remain open. |
| site-anchored readout | shape derived in cycle 698; existence still gated by the additivity reading. |
| reference normalization | untouched. An *intensive* dimensionless target needs a selected reference; a dimensionless extensive count does not. |
| carrier | untouched. |

## Scope for independent review

Every decisive equality is exact integer or `Fraction` arithmetic; there is no
floating-point comparison, no sampling, and no fit. The two independent counts
of the same dimension are the principal internal check. The supplied action's
internal homomorphism property is verified rather than assumed, while its
identification with record contents remains a named condition. The three
exhibited forms are checked for invariance against all 24 group elements and
all 54 coefficient positions, and for exchange symmetry, not on sampled
inputs. The axial extension in the counterfactual is a named choice and is
flagged as such in the runner and here. Its full `96`-coordinate solve includes
all channels rather than inferring a five-coupling conclusion from the
spin-spin basis alone.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
[Cycle 698](PHYSICAL_PAIR_KERNEL_MINIMAL_POSITION_EXTENSION_CYCLE698_NOTE_2026-07-25.md)
is cited for the content-blind classification this cycle generalizes and for
the licensing question it leaves open;
the landed
[proper-cubic finite-support linear-kernel classification](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md)
for the orbit-count machinery in its scoped form. Neither is load-bearing for
this runner's arithmetic.

An earlier block in this campaign motivated the extension by arguing that a
Record readout is position-blind. That block was rejected as submitted and only
the abstract kernel classification above was salvaged and landed; this note
therefore does not cite it, and nothing below depends on it. The standard-math analogue for the orbit and
character machinery is
[Cubic-orbit Reynolds projector](CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md),
cited in cycle 698 with the same distinction: it fixes a preferred forward
direction, this lane does not.
