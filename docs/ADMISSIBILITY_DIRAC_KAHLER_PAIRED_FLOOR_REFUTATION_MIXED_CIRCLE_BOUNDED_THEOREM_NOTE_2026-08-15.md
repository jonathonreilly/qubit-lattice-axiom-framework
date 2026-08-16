---
claim_id: admissibility_dirac_kahler_paired_floor_refutation_mixed_circle_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the Blocks 111-112 momentum-factorized seam-dressing variety, the paired-sector negative-count floor of two is exactly refuted--the displayed branch point has block inertias (4,0,0),(4,0,0),(4,0,0),(3,1,0), paired sum one, assembling to an exact (15,1,0) involution--and the mixed sector is exactly nonempty: the displayed circulant dressing squares to the identity, commutes with the spatial shift, anticommutes exactly with the Block 109 involution, and generates the Pythagorean circle of involutions whose membership is structural and whose displayed interior points all carry exact inertia (8,8,0) at both fixtures while the pure-circulant endpoint degenerates to rank twelve with inertia (6,6,4); the paired zero-sum (the requirement for a fully positive circulant assembly) is neither attained nor excluded; the mixed-circle inertia mechanism, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_even_parity_paired_branch_bounded_theorem_note_2026-08-15
runner: scripts/admissibility_dirac_kahler_paired_floor_refutation_mixed_circle_2026_08_15.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_even_parity_paired_branch_bounded_theorem_note_2026-08-15
target_blocker_text: "Decide whether a paired branch with zero negative count exists; prove or refute the paired floor; then the mixed variety; any positive dressed reflection feeds the OS package and the gravity constraint quotient."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Derive the mixed-circle inertia mechanism; decide the paired zero-sum; any positive dressed reflection feeds the OS package and the gravity constraint quotient."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-112 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact paired-branch involution and reality certificates, exact Hermiticity and leading-minor inertia certificates, exact blockwise sum-one assembly, exact circulant and anticommutation identities, structural exact Pythagorean-circle membership, exact displayed interior-point and endpoint inertia certificates, and exact rank certification on the declared d=2 carrier; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Paired Floor Refutation And The Pythagorean Mixed Circle

**Date:** 2026-08-15

**Campaign block:** 113

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_paired_floor_refutation_mixed_circle_2026_08_15.py`](../scripts/admissibility_dirac_kahler_paired_floor_refutation_mixed_circle_2026_08_15.py)

## 1. Result Up Front

[Block 112](ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:16`
and elaborated at
`docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:753-769`:

> Decide whether a paired branch with zero negative count exists; prove or
> refute the paired floor; then the mixed variety; any positive dressed
> reflection feeds the OS package and the gravity constraint quotient.

The floor-two reading is refuted. In the runner's displayed momentum-block
ordering, the exact branch point has block inertias

\[
 (4,0,0),\qquad(4,0,0),\qquad(4,0,0),\qquad(3,1,0). \tag{1}
\]

The paired `k=1,3` sum is one. Exact blockwise assembly therefore gives

\[
 (4,0,0)_0\mathbin\oplus(4,0,0)_1
 \mathbin\oplus(4,0,0)_2\mathbin\oplus(3,1,0)_3
 =(15,1,0).                                     \tag{2}
\]

Thus a paired-sector negative-count floor of two is false on the declared
variety. This does not supply the missing paired zero-sum. The exact
displayed attained sums remain

\[
 S_{\rm shown}=\{1,2,3,4\},                    \tag{3}
\]

and zero is neither attained nor excluded.

The mixed sector is exactly nonempty. Let `C_circ` be the displayed
circulant dressing and let `A_star` be the exact Block 109 involution. The
runner certifies

\[
 C_{\rm circ}^{\,2}=I,\qquad
 [C_{\rm circ},Q_x]=0,qquad
 \{C_{\rm circ},A_\star\}=0.                   \tag{4}
\]

Together with `A_star^2=I`, equation (4) makes every real Pythagorean
combination

\[
 M(t,s)=tC_{\rm circ}+sA_\star,qquad t^2+s^2=1, \tag{5}
\]

an exact involution in the inherited joint space. Points with `ts != 0`
are genuinely mixed. Circle membership is therefore structural, not a
finite sample inference.

At both rational shear fixtures, every displayed interior circle point has
exact Gram inertia `(8,8,0)`. At the pure-circulant endpoint `t=1`, where
the `A_star` component vanishes, the Gram has exact rank twelve and inertia
`(6,6,4)`. At `t=0`, equation (5) returns the Block 109 `A_star` endpoint,
with inertia `(8,8,0)`. These certificates exhibit no positive point. They
do not yet derive the mixed-circle inertia mechanism, classify every
untested circle point, or close a wider mixed family.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. The two authority blobs are
unchanged from the Block 112 snapshot.

The exact stacked parent is
[Block 112](ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `385a6ba5b1594f20e5d4eebba9da68d8e72abc10`, content-bound through
note blob `c1a05e0f9fdd7a6379fb469fca1c3964d30fb508`. Its direct parent is
[Block 111](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `b04e7c8747b09734711cfcd2bfab961bd12e81ad`, content-bound through
note blob `58eb5dee6229ebecc588034c514c5da2cf2690be`. The complementary
involution is inherited from
[Block 109](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `ad84cfcc857a65285389ba93b47cd7b718589be5`, content-bound through
note blob `3ed51ad603b3c4dc9a0e9eb3c98e343b49c3b9ea`. No audit verdict is
imported.

The executed contract is:

1. the Blocks 107--112 `d=2` one-fine-mode carrier on
   `Z8_t x Z4_x`, ordered time first with representatives `-4,...,3`;
2. antiperiodic time closure and the antilinear link-centered reflection
   `theta(t)=-1-t`;
3. the inherited step-shear history, with `m=9/20`, `v=1`, and the two
   exact rational fixtures `c=5/13` and `c=3/5`;
4. the full positive span `Lambda_+={0,1,2,3} x Z4` and the inherited
   exact two-history target-arm Gram convention;
5. the Block 111 momentum decomposition and complete circulant class, the
   Block 112 paired chart and attained-sum certificates, the Block 109
   `A_star` involution, the displayed `C_circ`, and their displayed
   Pythagorean circle; and
6. exact involution, reality, joint-space, shift-commutation, and
   anticommutation residuals, exact Hermiticity and leading-minor signs,
   exact blockwise inertia and assembly, exact displayed circle-point
   inertias, and exact endpoint rank only.

The exact scope is the displayed `d=2` carrier, the two displayed rational
shear fixtures, the displayed sum-one paired branch point, the inherited
attained-sum certificates, the displayed `C_circ` and `A_star`, the
structurally admitted Pythagorean circle, its displayed interior points,
and its two named endpoints. The mixed-circle inertia mechanism, the
paired zero-sum decision, every untested circle point, wider mixed families,
curved OS positivity, the completed ADM/history transporter, joint gravity,
the gravity constraint quotient, Records, retention, axiom amendment,
obligation retirement, and TOE percentage movement are outside the
executed contract.

## 3. The Sum-One Branch

Let \(K_k(B;c)\) be the four exact `4 x 4` momentum-block Grams in
the runner's fixed ordering. For each block, define

\[
 \delta_{k,r}(B;c)
 :=\det K_k(B;c)[1{:}r,1{:}r],
 \quad r=1,\ldots,4,\qquad \delta_{k,0}=1.      \tag{6}
\]

The runner first clears denominators and checks exact Hermiticity,

\[
 K_k(B;c)^\dagger=K_k(B;c),\qquad k=0,1,2,3.   \tag{7}
\]

At the displayed sum-one branch point, the exact leading-principal-minor
sign strings, in the same block order, are

\[
 ++++\,,\qquad ++++\,,\qquad ++++\,,\qquad ----\,. \tag{8}
\]

The positive zeroth minor is understood. The first three strings have no
sign change, and the fourth has exactly one. Exact sign-variation
`LDL^\dagger` inertia therefore gives

\[
 \begin{aligned}
 \operatorname{In}K_0&=(4,0,0),&
 \operatorname{In}K_1&=(4,0,0),\\
 \operatorname{In}K_2&=(4,0,0),&
 \operatorname{In}K_3&=(3,1,0).
 \end{aligned}                                  \tag{9}
\]

The exact involution and reality residuals are checked independently of
(7)--(9). In particular, inertia is not inferred from a floating-point
eigendecomposition, and involution is not inferred from Hermiticity. The
paired negative count is

\[
 n_{13}=n_-(K_1)+n_-(K_3)=0+1=1.               \tag{10}
\]

The orthogonal momentum projectors make the assembly exact. Hence

\[
 \begin{aligned}
 \operatorname{In}K_{\rm one}
  &=\operatorname{In}K_0+\operatorname{In}K_1+
    \operatorname{In}K_2+\operatorname{In}K_3\\
  &=(4,0,0)+(4,0,0)+(4,0,0)+(3,1,0)\\
  &=(15,1,0).                                   \tag{11}
 \end{aligned}
\]

Its determinant is negative, as exact inertia requires. The certificate is
an exact branch point in the inherited momentum-factorized seam-dressing
variety, not merely a nearby point in an ambient matrix space.

For the unrestricted nonsingular paired variety, define

\[
 \nu_{13}
 :=\min\{n_{13}(B):
          B\in\mathscr V_{13},\
          \det K_{13}(B)\ne0\}.                 \tag{12}
\]

Equation (10) proves \(\nu_{13}\le1\), so the reading
\(\nu_{13}=2\) is refuted exactly. The remaining alternatives are

\[
 \nu_{13}=0\qquad\hbox{or}\qquad\nu_{13}=1.     \tag{13}
\]

This is narrower than a positivity result. The displayed sum-one branch
removes the proposed floor of two but does not remove its final negative
direction.

The earlier sample sweeps did not certify a lower bound. They visited
displayed points and sign cells but did not exhaust every real branch.
Equation (10) is the exact point those finite sweeps missed. Their
non-observation of this branch could never have been upgraded into a
floor theorem, just as the present non-observation of zero cannot be
upgraded into a zero-sum exclusion.

## 4. The Circulant Square Root

Let \(\mathscr L_c\) denote the inherited real joint linear space at
fixture `c`: its elements obey the exact reflection-reality and full-span
two-history Hermiticity equations. Let
\(\mathscr C_{{\rm circ},c}\subset\mathscr L_c\) be its circulant part.
The displayed runner matrix satisfies

\[
 C_{\rm circ}\in\mathscr C_{{\rm circ},c}
 \quad\hbox{for}\quad c\in\{5/13,3/5\}.         \tag{14}
\]

It is a square root of the identity in the exact sense

\[
 C_{\rm circ}^{\,2}=I_{32}.                    \tag{15}
\]

Let \(Q_x=I_8\mathbin\otimes C_x\) be the inherited unit spatial shift.
Circulant membership is also checked directly by

\[
 Q_xC_{\rm circ}Q_x^{-1}=C_{\rm circ},
 \qquad [C_{\rm circ},Q_x]=0.                  \tag{16}
\]

The complementary
[Block 109 involution](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md),
anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:240-334`,
obeys

\[
 A_\star^2=I_{32},\qquad
 Q_xA_\star Q_x^{-1}=-A_\star.                 \tag{17}
\]

The new exact identity is

\[
 C_{\rm circ}A_\star+A_\star C_{\rm circ}=0.   \tag{18}
\]

Equation (18) is an entrywise exact anticommutation certificate. It is not
inferred merely from the opposite shift gradings in (16)--(17). The shift
grading places the two matrices in different linear components; the
runner separately proves that their anticommutator vanishes.

Both matrices belong to the same inherited joint linear space. Therefore

\[
 tC_{\rm circ}+sA_\star\in\mathscr L_c
 \quad\hbox{for every}\quad (t,s)\in\mathbb R^2 \tag{19}
\]

at both fixtures. This is the required joint-space membership. The
quadratic involution condition is imposed next.

## 5. The Pythagorean Circle

Define

\[
 M(t,s):=tC_{\rm circ}+sA_\star.                \tag{20}
\]

Using (15), (17), and (18),

\[
 \begin{aligned}
 M(t,s)^2
  &=t^2C_{\rm circ}^2+s^2A_\star^2+
    ts\{C_{\rm circ},A_\star\}\\
  &=(t^2+s^2)I_{32}.                            \tag{21}
 \end{aligned}
\]

Consequently

\[
 \mathscr P
 :=\{M(t,s):t^2+s^2=1\}                        \tag{22}
\]

is an exact circle of involutions inside the joint space. This conclusion
holds for every real point of the circle. It is structural: it follows
from the polynomial identity (21), not interpolation between tested
points.

The shift grading resolves the two components:

\[
 \begin{aligned}
 {1\over2}\bigl(M+Q_xMQ_x^{-1}\bigr)&=tC_{\rm circ},\\
 {1\over2}\bigl(M-Q_xMQ_x^{-1}\bigr)&=sA_\star.
 \end{aligned}                                  \tag{23}
\]

Thus `ts != 0` makes both components nonzero and gives a genuinely mixed
involution. The mixed sector is therefore exactly nonempty. Neither axis
confinement result from Block 112's displayed structured slices applies
to this anticommuting circle.

Let \(\mathscr P_{\rm shown}^{\circ}\) denote the runner's displayed
finite set of exact rational Pythagorean pairs with `ts != 0`. For every
one of those points, denominator-cleared Hermiticity and exact
leading-minor or rank-revealing certificates give

| displayed point class | `c=5/13` | `c=3/5` |
|---|---:|---:|
| every `(t,s)` in `P_shown^circ` | `(8,8,0)` | `(8,8,0)` |

Equivalently,

\[
 \operatorname{In}K_{M(t,s);c}=(8,8,0)
 \quad
 \begin{matrix}
 ((t,s)\in\mathscr P_{\rm shown}^{\circ}),\\[-2pt]
 (c\in\{5/13,3/5\}).
 \end{matrix}                                   \tag{24}
\]

These exact displayed interiors are maximally balanced and nonsingular.
They are not positive. Equation (24) is a finite exact inertia statement,
whereas equations (21)--(22) are the continuum membership theorem. No
inertia is assigned here to an untested interior circle point.

The distinction matters. Structural membership proves that mixed
involutions exist. It does not by itself make their Grams positive or
pin their inertia. Deriving why the displayed interiors all have the same
balanced inertia is the named live mechanism question.

## 6. The Endpoint Degeneracy

At the pure-circulant endpoint,

\[
 (t,s)=(1,0),\qquad M(1,0)=C_{\rm circ}.        \tag{25}
\]

The exact Gram rank and inertia at both fixtures are

\[
 \operatorname{rank}K_{C_{\rm circ};c}=12,
 \qquad
 \operatorname{In}K_{C_{\rm circ};c}=(6,6,4),
 \quad c\in\{5/13,3/5\}.                       \tag{26}
\]

Thus `C_circ` is an exact dressing involution but its Gram has four exact
zero directions. The endpoint is neither positive definite nor one of the
nonsingular balanced interiors.

At the other named endpoint,

\[
 (t,s)=(0,1),\qquad M(0,1)=A_\star.             \tag{27}
\]

This is exactly Block 109's displayed involution, whose Gram inertia at
both fixtures is

\[
 \operatorname{In}K_{A_\star;c}=(8,8,0).       \tag{28}
\]

The displayed pinning pattern therefore fails precisely at the named
endpoint where the `A_star` component vanishes: `s=0` changes the observed
`(8,8,0)` pattern to the rank-twelve `(6,6,4)` pattern. This is an exact
boundary observation, not yet the derivation of a circle-wide mechanism.

One plausible lead is that a nonzero `A_star` component removes the four
endpoint kernel directions in opposite-sign pairs while preserving a
balanced signature. That sentence names the mechanism to derive; it is
not counted as a theorem here. The derivation must decide whether the
balance is forced at every untested interior point or is only a property
of the displayed rational points.

## 7. The Zero-Sum Gate

Combining the new sum-one point with the exact Block 112 certificates, the
displayed paired negative-count set is

\[
 S_{\rm shown}=\{1,2,3,4\}.                    \tag{29}
\]

This set is attained, not inferred from approximate eigenvalues. Its rows
are:

| displayed certificate | paired negative count |
|---|---:|
| current exact sum-one branch | `1` |
| Block 112 exact sum-two witness | `2` |
| Block 112 exact definite-half witness | `3` |
| Block 112 exact second-fixture witness | `4` |

No displayed certificate has paired sum zero. For the unrestricted paired
floor (12), the only live values after the sum-one refutation are exactly
those in (13). Thus the surviving binary question is now

\[
 \text{zero is attained}\qquad\hbox{or}\qquad
 \nu_{13}=1.                                   \tag{30}
\]

The positive self-conjugate `k=0,2` blocks are already available. Hence a
paired zero-sum point would have paired inertia `(8,0,0)` and assemble as

\[
 (4,0,0)_0\mathbin\oplus(8,0,0)_{13}
 \mathbin\oplus(4,0,0)_2=(16,0,0).             \tag{31}
\]

Conversely, a fully positive circulant assembly forces zero negative count
in its paired block. On this blockwise assembly, the paired zero-sum
decision is therefore exactly the requirement for full circulant
positivity.

The Pythagorean circle does not decide (30). It proves the mixed sector
nonempty, but its displayed interiors are indefinite and its
pure-circulant endpoint is singular. A failed positive search on this
one circle cannot exclude a positive point on another paired component or
in a wider mixed family.

What is decided is:

1. the paired-sector floor-two reading is false;
2. the displayed paired sums are exactly those in (29);
3. the mixed sector contains the exact structural circle (22);
4. every displayed interior circle point has inertia `(8,8,0)` at both
   fixtures; and
5. the pure-circulant endpoint has exact rank twelve and inertia
   `(6,6,4)` at both fixtures.

What is not decided is:

1. whether a paired zero-sum point exists;
2. whether the unrestricted paired floor is one;
3. the inertia of every untested interior circle point;
4. the mechanism behind the displayed balanced inertia; or
5. whether any point in the complete circulant or mixed variety is
   positive.

## 8. No-Go Discipline Gate

There is exactly one bounded finite-carrier wall.

- `W1` — **REFUTATION AND DISPLAYED-CLASS BOUNDARY:** the
  paired-sector negative-count floor-two reading is refuted by the exact
  sum-one branch, which assembles to `(15,1,0)`. The displayed circle
  carries no positive point: every displayed interior point has exact
  inertia `(8,8,0)` at both fixtures, the `A_star` endpoint is likewise
  indefinite, and the pure-circulant endpoint is rank-twelve degenerate
  with inertia `(6,6,4)`.

The wall is narrow. “The displayed circle” in `W1` means the exact
runner-certified interior points and named endpoints, not an inertia
classification of every real circle point. The full circle is proved to
consist of joint-space involutions, but the inertia mechanism between the
displayed points remains live.

`W1` does not assert a positive dressing or classify the complete paired,
circulant, or mixed varieties. It does not attain or exclude paired zero
sum. It is not a transporter impossibility or an OS or gravity theorem.

The exact scope is the displayed carrier, the two rational fixtures, the
displayed sum-one branch, the exact anticommuting pair, the structurally
admitted Pythagorean circle, its displayed rational interiors, and its
named endpoints. The live questions are the mixed-circle inertia
mechanism and the paired zero-sum decision.

### N1 — Alternative Route Enumeration

Routes are normalized by `(object, mechanism, terminal)`. A floor
countercertificate is distinguished from a finite inertia chart and from
the structural membership theorem for the full circle.

1. **PROVED — displayed paired branch / exact minor signs and blockwise
   assembly / floor-two refutation.** Equations (8)--(11) give exact block
   inertias `(4,0,0)`, `(4,0,0)`, `(4,0,0)`, and `(3,1,0)`, paired sum
   one, and full inertia `(15,1,0)`. This is the strongest row.
2. **PROVED — displayed mixed-circle interiors / exact Hermiticity and
   inertia / displayed-point positivity test.** Equation (24) gives exact
   inertia `(8,8,0)` at both fixtures for every displayed rational
   interior point. Every such point is indefinite.
3. **PROVED — pure-circulant endpoint / exact rank and inertia /
   endpoint positivity test.** Equations (25)--(26) give exact rank
   twelve and inertia `(6,6,4)` at both fixtures. The four exact kernel
   directions make the endpoint degenerate.
4. **PROVED — Pythagorean parameter circle / joint-space linearity and
   the square identity / structural mixed membership.** Equations
   (19)--(23) prove that every `t^2+s^2=1` point is an involution and
   that every `ts != 0` point is genuinely mixed. This row proves
   membership, not circle-wide inertia.
5. **PROVED — `C_circ` and `A_star` / exact anticommutation /
   Pythagorean involution mechanism.** Equations (15), (17), and (18)
   reduce the mixed square to `(t^2+s^2)I`. This is the exact
   anticommutation mechanism behind structural membership, not the still
   underived inertia mechanism.
6. **UNTESTED — LIVE — mixed circle and paired variety /
   derive the inertia mechanism and decide paired zero sum /
   positivity.** This `UNTESTED-LIVE` route must decide whether the
   displayed `(8,8,0)` pattern extends around the circle and whether a
   paired zero-sum branch exists. It is not counted as an attempted route
   against the displayed refutations in `W1`.

### N2 — Wall-Independence Audit

There is one current wall, so no pairwise current-wall table is needed. It
is independent of Block 112's `W1`, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:507-528`.

Block 112 refutes global odd paired parity and a class-wide paired
determinant orientation by displaying even paired sums two and four. It
also confines two displayed structured mixed slices to their unmixed axes.
The present sum-one branch instead refutes the proposed floor of two. An
even witness cannot prove a sum-one branch, and a sum-one branch does not
reproduce the even-parity or orientation refutations.

The mixed clauses are likewise independent. Block 112's exact slice ideals
contain only axis solutions. The present `C_circ` is chosen to
anticommute with `A_star`, and the resulting circle supplies exact mixed
involutions outside those displayed slice restrictions. Existence in this
new anticommuting family does not invalidate the earlier restricted
eliminations; the earlier eliminations do not imply the circle identities.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified
explicitly.

| lowercase hit | classification |
|---|---|
| `displayed d=2 carrier` | the exact Blocks 107--112 finite carrier |
| `two displayed rational shear fixtures` | exactly `c=5/13` and `c=3/5` |
| `blocks 111-112 momentum-factorized seam-dressing variety` | the inherited finite variety, not every global operator |
| `displayed sum-one paired branch` | one exact branch point, not a component classification |
| `minor strings ++++, ++++, ++++, ----` | the exact displayed block signs |
| `block inertias (4,0,0), (4,0,0), (4,0,0), (3,1,0)` | the exact sum-one certificate |
| `paired sum one` | the exact count in (10) |
| `full inertia (15,1,0)` | the exact blockwise assembly |
| `paired floor two refuted` | the counterexample to `nu_13=2` |
| `attained paired sums {1,2,3,4}` | exact displayed witnesses, not an exhaustive range |
| `paired zero-sum untested-live` | zero is neither attained nor excluded |
| `displayed circulant square root` | `C_circ^2=I` exactly |
| `commutes with the spatial shift` | exact identity (16) |
| `anticommutes with a_star` | exact identity (18), checked separately from grading |
| `pythagorean circle membership is structural` | exact continuum identity (21) |
| `mixed sector exactly nonempty` | every circle point with `ts != 0` is mixed |
| `displayed interior inertia (8,8,0)` | exact at both fixtures and only at displayed points |
| `pure-circulant endpoint rank twelve` | exact rank certificate in (26) |
| `endpoint inertia (6,6,4)` | exact four-dimensional kernel at both fixtures |
| `mixed-circle inertia mechanism untested-live` | no continuum inertia derivation is claimed |
| `not a transporter impossibility` | scope firewall for `w1` |
| `no axiom amendment is justified` | constitutional firewall |
| `zero obligation retirement` | TOE accounting firewall |
| `no toe percentage moves` | TOE accounting firewall |
| `retained-positive end-to-end theory count remains zero` | audit-status accounting |
| `actual adm/history transporter remains unexecuted` | partial-closure statement only |
| `n1 n2 n3 n4 n5 n6 n7 n8` | every discipline gate is present |
| `w1` | the wall set has exactly one member |
| `per_element per_site per_mode per_block lattice_wide` | the five N5 resolution keys |

No phrase converts exact circle membership into positive circle-wide
inertia, turns the sum-one point into zero sum, or widens finite displayed
inertia certificates to the complete mixed variety.

### N4 — Residual Matching

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 112 Next Decision](ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:753-769` | decide whether paired zero sum exists, prove or refute the paired floor, then solve the mixed variety before OS and gravity | equations (8)--(13) refute the floor-two reading but leave zero sum live; equations (14)--(24) prove the mixed sector nonempty and isolate the underived inertia mechanism |
| [Block 112 zero-sum gate](ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:382-455` | the displayed attained sums are `{1,2,3,4}`, zero is unobserved, and the proposed even-branch alternatives are zero or two | the exact current branch makes the unrestricted paired count one and refutes a floor-two reading; equations (29)--(31) preserve zero as the full-positivity gate |
| [Block 112 mixed slices](ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:456-505` | two displayed structured slices contain only unmixed axes while the complete mixed variety remains open | the anticommuting pair in (15)--(18) generates the exact mixed circle outside those slice restrictions |
| [Block 111 momentum factorization](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:164-278` | circulant involution and Gram equations decouple over the four spatial momenta, with inertia adding blockwise | equations (6)--(11) retain the exact factorization and assemble the four displayed block inertias to `(15,1,0)` |
| [Block 111 mixture frontier](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:440-522` | a mixed involution requires the scaled circulant square and exact anticommutation with `A_star` | equations (15), (18), and (21) solve that requirement on the displayed Pythagorean family |
| [Block 109 `A_star`](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:240-334` | `A_star` is a genuine globally supported involution in the four-dimensional `x`-parity class | equations (17)--(23) retain that exact involution as the shift-odd endpoint and mixed-circle generator |

Every inherited residual reaches its stated interface. No citation is used
as an audit verdict.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the displayed Blocks 111--112
momentum-factorized seam-dressing variety, the exact sum-one branch has
block inertias `(4,0,0)`, `(4,0,0)`, `(4,0,0)`, and `(3,1,0)` and
assembles to `(15,1,0)`, refuting the paired-sector floor-two reading;
the displayed `C_circ` squares to the identity, commutes with the spatial
shift, and anticommutes with Block 109's `A_star`, so their full
Pythagorean circle is structurally a circle of joint-space involutions;
every displayed interior has exact inertia `(8,8,0)` at both fixtures,
while the pure-circulant endpoint has rank twelve and inertia `(6,6,4)`,
and the mixed-circle inertia mechanism and paired zero-sum decision remain
open.”

Forbidden upgrades include
“the circle proves mixed positivity impossible,” “zero-sum is excluded,”
“the paired floor is one,” “every interior circle point has inertia
`(8,8,0)`,” “the displayed points classify the complete mixed variety,”
“a positive dressing exists,” “curved OS is closed,”
“ADM/history transport is finished,” “the gravity quotient has been
executed,” “an axiom amendment is required,” and “a TOE obligation is
retired.”

The five resolution lines from the runner specification are reproduced
verbatim:

```text
per_element: exact branch, square-root, anticommutator, circle, and endpoint identities are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: the paired sum-one branch and the mixed circle verify at both displayed shear fixtures
per_block: the interior circle points are pinned at eight-eight while the pure-circulant endpoint degenerates to rank twelve
lattice_wide: checked and not executed — the mixed-circle inertia mechanism, the paired zero-sum decision, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The remaining decisions are exact
finite action and representation problems inside the inherited carrier.

| route | present status | remaining terminal |
|---|---|---|
| displayed paired branch | exact minor strings, paired sum one, and full inertia `(15,1,0)` | remove the final paired negative direction |
| attained-sum chart | exact displayed sums `{1,2,3,4}` | decide whether zero is attained |
| paired floor | floor two refuted and unrestricted floor bounded above by one | prove zero-sum existence or prove floor one |
| displayed anticommuting pair | exact squares, joint-space membership, shift gradings, and anticommutation | none for structural circle membership |
| Pythagorean circle | every `t^2+s^2=1` point is structurally an involution | derive the Gram-inertia mechanism |
| displayed circle interiors | exact `(8,8,0)` inertia at both fixtures | decide all untested circle points and explain the pinning |
| pure-circulant endpoint | exact rank twelve and inertia `(6,6,4)` | derive how a nonzero `A_star` component lifts the kernel |
| complete mixed variety | one exact mixed circle is present | search or classify wider mixed families |
| OS and gravity route | not executed | carry any positive dressed reflection through OS, then form the gravity constraint quotient |

The scan finds no axiom-amendment route. The exact mixed circle supplies
involutions but no displayed positive point, and the absence of a
displayed paired zero is not counted as a zero-sum exclusion.

### N7 — Steelman

**Hostile steelman against overreading the wall.** The balanced
`(8,8,0)` pinning might break at untested circle points. Structural
involution membership says nothing by itself about the Gram determinant,
and a determinant-zero crossing between displayed rational points could
change inertia. The rank-four kernel at the pure-circulant endpoint is
evidence that the circle has a nontrivial boundary mechanism, not a proof
that every nonzero `A_star` coefficient resolves it in a fixed way.

The pinning might also be special to this circle and fail in wider mixed
families. A different circulant direction could anticommute with
`A_star`, or a nonlinear mixed component could evade the displayed
balanced signatures and reach positivity. Those are not objections to the
exact displayed certificates; they are exactly the named mixed-circle
inertia-mechanism question.

The paired route remains independent. The sum-one point refutes floor two
but may still lie on a component whose last negative direction cannot be
removed without singularity. Conversely, an unvisited paired component
may have sum zero and assemble to `(16,0,0)`. The attained set
`{1,2,3,4}` does not decide between those alternatives.

The current wall claims only what its exact countercertificates reach:
floor two is false, mixed involutions exist on the structural circle, the
displayed interiors are balanced and indefinite, and the pure-circulant
endpoint is degenerate. It does not make a circle-wide positivity
impossibility or a zero-sum exclusion.

### N8 — Cross-Cycle Echo

| earlier exact boundary | echo here |
|---|---|
| [Block 109's `A_star` involution](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:240-334` | the exact shift-odd involution becomes one endpoint and one generator of the structural mixed circle |
| [Block 111's momentum factorization](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:164-278` | exact blockwise decoupling turns the new four-block minor strings into paired sum one and full inertia `(15,1,0)` |
| [Block 111's mixture frontier](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:440-522` | its scaled-square plus anticommutation equations are solved structurally by `tC_circ+sA_star` on `t^2+s^2=1` |
| [Block 112's zero-sum gate](ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:382-455` | the proposed floor two is refuted by sum one while the actual zero-sum decision remains live |
| [Block 112's mixed-slice boundary](ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_EVEN_PARITY_PAIRED_BRANCH_BOUNDED_THEOREM_NOTE_2026-08-15.md:456-505` | the exact anticommuting circle proves the full mixed sector nonempty without contradicting axis confinement in the earlier displayed slices |

The repeated discipline is to let an exact counterexample refute a proposed
floor and to let anticommutation prove mixed membership, while refusing to
turn finitely displayed inertia into a circle-wide or variety-wide
positivity theorem.

**No-Go Discipline verdict:** **PASS** only for narrow `W1`: the
paired-sector floor-two reading is refuted by the exact sum-one assembly,
and the displayed circle carries no positive certificate because its
displayed interiors are exactly `(8,8,0)` and its pure-circulant endpoint
is exactly rank-twelve `(6,6,4)`. **FAIL** for a positive dressing, the
paired zero-sum decision, a circle-wide inertia theorem, the complete
circulant or mixed variety, transporter completion, curved OS positivity,
gravity, axiom necessity, or TOE.

## 9. Axiom And TOE Disposition

No axiom amendment is justified. The paired minor signs, blockwise
assembly, circulant and `A_star` involutions, shift gradings,
anticommutation, structural circle membership, displayed-point inertia,
and endpoint rank are finite consequences of the displayed carrier and
dressing classes; no new primitive is assumed.

This is bounded route progress, not an audit-grade assignment. It retires
no end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 10. Next Decision

The shortest high-value sequence is:

1. derive the mixed-circle inertia mechanism and decide whether the
   displayed `(8,8,0)` pinning extends to every interior point;
2. decide whether a paired zero-sum point exists and thereby settle the
   unrestricted paired floor;
3. carry any positive dressed reflection through the OS package; and
4. only then form the gravity constraint quotient.

The actual ADM/history transporter remains unexecuted beyond the displayed
sum-one floor refutation, structural Pythagorean mixed circle, exact
displayed interior inertias, and pure-circulant endpoint degeneracy.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted.
