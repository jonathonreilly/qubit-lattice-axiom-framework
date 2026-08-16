---
claim_id: admissibility_dirac_kahler_even_parity_paired_branch_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the momentum-factorized circulant involution variety of Block 111, the paired k=1,3 sector's negative-count parity is not globally odd--the displayed exact chart witness gives a paired involution with reality coupling, exactly Hermitian paired Gram blocks with leading-minor signs `+---` and `++--` (negative counts one and one, sum two), assembling with the exactly positive self-blocks to an exact (14,2,0) involution with positive determinant, and at the second fixture the same chart point yields an even branch of sum four assembling to (12,4,0); the paired determinant sign equals the parity sign at the displayed points and flips between the odd base point of sum one and the even witness, so no global determinant-orientation invariant exists at the paired level; the displayed attained paired sums are one, two, three, and four, including a point whose first half is exactly definite (zero and three), while no displayed point attains sum zero--the zero-sum decision (equivalently full positivity of a circulant assembly) and the paired floor are the named open gates; the displayed structured mixed-variety slices contain only unmixed axes; curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_momentum_factorized_positivity_frontier_bounded_theorem_note_2026-08-15
runner: scripts/admissibility_dirac_kahler_even_parity_paired_branch_2026_08_15.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_momentum_factorized_positivity_frontier_bounded_theorem_note_2026-08-15
target_blocker_text: "Decide the paired-sector parity globally on the paired involution variety; solve the mixed circulant-plus-A-star dressing variety; any positive dressed reflection feeds the OS package and the gravity constraint quotient."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Decide whether a paired branch with zero negative count exists; prove or refute the paired floor; then the mixed variety; any positive dressed reflection feeds the OS package and the gravity constraint quotient."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-111 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact paired-chart involution and reality certificates, exact Hermiticity and leading-minor inertia certificates, exact blockwise assemblies, exact determinant-parity and orientation-flip certificates, exact attained-sum and definite-half certificates, and exact structured mixed-slice axis certificates on the declared d=2 carrier; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Even-Parity Paired Branch And The Zero-Sum Gate

**Date:** 2026-08-15

**Campaign block:** 112

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_even_parity_paired_branch_2026_08_15.py`](../scripts/admissibility_dirac_kahler_even_parity_paired_branch_2026_08_15.py)

## 1. Result Up Front

[Block 111](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:16`
and elaborated at
`docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:747-764`:

> Decide the paired-sector parity globally on the paired involution variety;
> solve the mixed circulant-plus-A-star dressing variety; any positive dressed
> reflection feeds the OS package and the gravity constraint quotient.

The first clause is refuted in its global-odd form. On the first displayed
rational fixture, the exact paired chart contains an involution whose two
Hermitian half-blocks have leading-principal-minor sign strings

\[
 +---\qquad\hbox{and}\qquad ++--.               \tag{1}
\]

Including the conventional positive zeroth minor, each string has one sign
change. The two exact negative counts are therefore `1` and `1`, so the
paired negative count is `2` rather than odd. The combined paired inertia is
`(6,2,0)`. Adding the two exactly positive self-conjugate blocks gives

\[
 (4,0,0)_0\mathbin\oplus(6,2,0)_{13}
 \mathbin\oplus(4,0,0)_2=(14,2,0),             \tag{2}
\]

with positive determinant. At the second rational fixture, the same exact
chart point has paired negative count `4` and combined paired inertia
`(4,4,0)`. With the same positive self-block choice it assembles as

\[
 (4,0,0)_0\mathbin\oplus(4,4,0)_{13}
 \mathbin\oplus(4,0,0)_2=(12,4,0).             \tag{3}
\]

The paired determinant sign is `(-1)^{n_{13}}` at every displayed
nonsingular point. It is negative at Block 111's odd base point
`n_{13}=1` and positive at the even witness `n_{13}=2`. The displayed
orientation therefore flips inside the paired involution variety. Neither
global oddness nor a global paired determinant-orientation invariant
survives.

The displayed exact chart attains the paired negative-count sums

\[
 \{1,2,3,4\}.                                   \tag{4}
\]

One sum-three point has half-counts `(0,3)`, so its first half is exactly
positive definite. No displayed chart point has sum zero. Thus this note
decides the global-odd conjecture but does not decide positivity. The live
binary gate is whether the even paired branch reaches zero or has floor
two. Because both self blocks are already exactly positive, a paired
zero-sum point is equivalent on this assembly to a fully positive
circulant Gram.

The displayed structured slices of the mixed circulant-plus-parity variety
contain only the two unmixed axes. That finite slice result does not close
the complete mixed variety.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. The two authority blobs are
unchanged from the Block 111 snapshot.

The exact stacked parent is
[Block 111](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `b04e7c8747b09734711cfcd2bfab961bd12e81ad`, content-bound through
note blob `58eb5dee6229ebecc588034c514c5da2cf2690be`. Its direct parent is
[Block 110](ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `d6761278fca9cac617200792473a8f4da3a6cfff`, content-bound through
note blob `8401946b778d8d41b0a553d0844f59e616c22e9f`. The complementary
parity class is inherited from
[Block 109](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `ad84cfcc857a65285389ba93b47cd7b718589be5`, content-bound through
note blob `3ed51ad603b3c4dc9a0e9eb3c98e343b49c3b9ea`. No audit verdict is
imported.

The executed contract is:

1. the Blocks 107--111 `d=2` one-fine-mode carrier on
   `Z8_t x Z4_x`, ordered time first with representatives `-4,...,3`;
2. antiperiodic time closure and the antilinear link-centered reflection
   `theta(t)=-1-t`;
3. the inherited step-shear history, with `m=9/20`, `v=1`, and the two
   exact rational fixtures `c=5/13` and `c=3/5`;
4. the full positive span `Lambda_+={0,1,2,3} x Z4` and the inherited
   exact two-history target-arm Gram convention;
5. the Block 111 complete circulant class, its self-conjugate `k=0,2`
   blocks, its reality-coupled `k=1,3` pair, the displayed paired
   `R(Q)(D+N)R(Q)^{-1}` chart, the displayed sign cells, and the displayed
   structured mixed slices with the four-dimensional pure `x`-parity
   class; and
6. exact chart identities, exact rational involution and reality residuals,
   exact Hermiticity, exact leading-minor signs, exact inertia and
   determinant signs, exact blockwise assembly, and exact mixed-slice
   elimination only.

The exact scope is the displayed `d=2` carrier, the two displayed rational
shear fixtures, the displayed paired chart and chart points, the positive
self-block choices, and the displayed structured mixed slices. The
zero-sum decision, the even-branch paired floor, the complete mixed variety,
curved OS positivity, the completed ADM/history transporter, joint gravity,
the gravity constraint quotient, Records, retention, axiom amendment,
obligation retirement, and TOE percentage movement are outside the
executed contract.

## 3. The Chart And The Witness

Write \(\rho(A)=J\overline A J\) for the exact antilinear reality map that
exchanges the `k=1` and `k=3` momentum slices. On the first slice of the
paired carrier, use the lower-graph chart

\[
 B_1(Q,U)=R(Q)\bigl(D+N(U)\bigr)R(Q)^{-1},      \tag{5}
\]

where

\[
 D=
 \begin{pmatrix}I_4&0\\0&-I_4\end{pmatrix},
 \qquad
 N(U)=
 \begin{pmatrix}0&U\\0&0\end{pmatrix},
 \qquad
 D^2=I,\quad N(U)^2=0,\quad DN(U)+N(U)D=0.     \tag{6}
\]

The exact lower change and its inverse are

\[
 R(Q)=
 \begin{pmatrix}
  I_4&0\\Q&I_4
 \end{pmatrix},
 \qquad
 R(Q)^{-1}=
 \begin{pmatrix}
  I_4&0\\-Q&I_4
 \end{pmatrix},
 \qquad Q\in{\rm Mat}_4(\mathbb Q(i)).          \tag{7}
\]

In the runner's fixed basis ordering, the displayed even witness uses

\[
 Q_{\rm ev}=
 \begin{pmatrix}
  0&i&0&0\\
  -1+i&0&0&0\\
  0&0&1&0\\
  0&0&0&2i
 \end{pmatrix}.                                 \tag{7a}
\]

The nilpotent coordinate `U_{\rm ev}` is the exact Gaussian-rational
solution of the paired joint equations at (7a). The runner checks it
against the exact pinned coordinate before using it. The symbol
`Q_{\rm fp}` denotes the inherited odd base point, and `Q_{\rm def}` the
displayed definite-half point. These names refer to exact chart
coordinates, not decimal approximations.

Equations (5)--(6) give the involution identity before Gram evaluation:

\[
 B_1(Q,U)^2
 =R(Q)\bigl(D+N(U)\bigr)^2R(Q)^{-1}
 =I.                                            \tag{8}
\]

The companion slice is defined by the inherited reality coupling,

\[
 B_3(Q,U)=J\overline{B_1(Q,U)}J
          =\rho\!\left(B_1(Q,U)\right).         \tag{9}
\]

The runner checks both `B_1^2=I` and `B_3^2=I` exactly, as well as (9).
This is the required paired reality coupling. It is an identity on the
involution blocks; it does not assert that the two target-arm Gram halves
are the same matrix. Below, `U` is suppressed from the point label once
its exact joint-equation value has been fixed.

Let

\[
 K_1(Q;c),\qquad K_3(Q;c)                       \tag{10}
\]

be the two `4 x 4` target-arm Gram halves after the inherited exact
reflection and history maps are inserted. The runner clears denominators
and checks

\[
 K_j(Q;c)^\dagger=K_j(Q;c),\qquad j\in\{1,3\}, \tag{11}
\]

as exact rational identities. Define their leading principal minors by

\[
 \delta_{j,r}(Q;c)
 =\det K_j(Q;c)[1{:}r,1{:}r],
 \quad r=1,\ldots,4,\qquad\delta_{j,0}=1.       \tag{12}
\]

At `c=5/13` and `Q=Q_{\rm ev}`, no minor in (12) vanishes and

\[
 \begin{aligned}
  \bigl(\operatorname{sgn}\delta_{1,r}\bigr)_{r=1}^4
    &=+---,\\
  \bigl(\operatorname{sgn}\delta_{3,r}\bigr)_{r=1}^4
    &=++--.
 \end{aligned}                                  \tag{13}
\]

The sign-variation form of exact `LDL^\dagger` inertia, with the positive
`delta_{j,0}` prepended, gives one negative direction in each half. Thus

\[
 \operatorname{In}K_1(Q_{\rm ev};5/13)
 =\operatorname{In}K_3(Q_{\rm ev};5/13)
 =(3,1,0),                                      \tag{14}
\]

and the paired negative-count sum is exactly two. Equations (8), (9),
(11), and (13) are separate certificates: involution, reality coupling,
Hermiticity, and inertia are not inferred from one numerical
diagonalization.

## 4. The Assembly

Block 111 supplies positive-semidefinite representatives in both
self-conjugate sectors; the displayed choices are in fact exactly positive
definite. At the first fixture their Gram inertias are

\[
 \operatorname{In}K_0=(4,0,0),\qquad
 \operatorname{In}K_2=(4,0,0).                 \tag{15}
\]

Their exact leading-minor sign strings are `++++` and `++++`. They are
positive-semidefinite certificates strengthened to exact positive
definiteness, not certificates with unresolved kernels. In particular,
both self-block determinants are strictly positive.

The momentum projectors are mutually orthogonal, and the involution,
reality, and Gram equations decouple exactly as established in Block 111.
Consequently the paired chart point assembles blockwise to an exact
circulant involution, and its inertia adds:

\[
 \begin{aligned}
 \operatorname{In}K_{\rm ev}
  &=\operatorname{In}K_0+
    \operatorname{In}(K_1\mathbin\oplus K_3)+
    \operatorname{In}K_2\\
  &=(4,0,0)+(6,2,0)+(4,0,0)\\
  &=(14,2,0).                                   \tag{16}
 \end{aligned}
\]

The determinant factors over the same exact direct sum:

\[
 \det K_{\rm ev}
 =\det K_0\det K_1\det K_3\det K_2>0.           \tag{17}
\]

The sign in (17) follows twice over: the two self determinants are
positive and both half determinants in (13) are negative, while the full
matrix in (16) has two negative directions. No floating-point determinant
tail enters the certificate.

At the second fixture `c=3/5`, the same chart coordinate
`Q_{\rm ev}` is still an exact paired involution with exact reality
coupling. The exact half-block leading-minor sign strings are `+-++` and
`---+`, giving the split `(2,2)` and paired negative count four. Hence

\[
 \operatorname{In}(K_1\mathbin\oplus K_3)
 =(4,4,0).                                      \tag{18}
\]

The exactly positive self-block choice then gives

\[
 (4,0,0)_0\mathbin\oplus(4,4,0)_{13}
 \mathbin\oplus(4,0,0)_2=(12,4,0).             \tag{19}
\]

This second assembly is also even and nonsingular. It is a separate
fixture certificate, not a continuity assertion between `c=5/13` and
`c=3/5`.

## 5. The Orientation Refutation

For any nonsingular Hermitian matrix `H`, exact inertia gives

\[
 \operatorname{sgn}\det H=(-1)^{n_-(H)}.        \tag{20}
\]

Apply (20) to the full paired Gram block. At the inherited Block 111 base
point,

\[
 n_{13}(Q_{\rm fp})=1,\qquad
 \operatorname{sgn}\det K_{13}(Q_{\rm fp})=-1. \tag{21}
\]

At the displayed even witness,

\[
 n_{13}(Q_{\rm ev})=2,\qquad
 \operatorname{sgn}\det K_{13}(Q_{\rm ev})=+1. \tag{22}
\]

The determinant sign therefore agrees with the negative-count parity at
both displayed points and takes both orientations. Two exact points with
opposite signs suffice to refute a determinant-orientation invariant on
the whole paired variety. They also refute the hypothesis that every
paired involution has odd negative count.

This is a global-hypothesis refutation by counterexample, not a connected-
component theorem. The certificate does not assert that `Q_{\rm fp}` and
`Q_{\rm ev}` lie in one nonsingular component or that a path between them
avoids the determinant-zero wall. Those questions are unnecessary for the
refutation and cannot be upgraded into a positive-point claim.

## 6. The Attained Sums And The Definite Half

The exact displayed certificates can be normalized by fixture, chart
point, half-count data, total paired count, and paired determinant sign:

| fixture and point | displayed half counts | `n_13` | `In K_13` | `sign det K_13` |
|---|---:|---:|---:|---:|
| inherited odd base point | total certificate `1` | `1` | `(7,1,0)` | `-` |
| `c=5/13`, `Q_ev` | `(1,1)` | `2` | `(6,2,0)` | `+` |
| displayed definite-half point | `(0,3)` | `3` | `(5,3,0)` | `-` |
| `c=3/5`, same `Q_ev` | `(2,2)` | `4` | `(4,4,0)` | `+` |

Thus the displayed attained-sum set is exactly

\[
 S_{\rm shown}=\{1,2,3,4\}.                    \tag{23}
\]

The word “displayed” is essential. Equation (23) states that each listed
sum has an exact witness in the declared chart; it does not classify every
attainable sum on every real component.

The `(0,3)` row provides a second useful refutation. Its first half has

\[
 \operatorname{In}K_1=(4,0,0),                 \tag{24}
\]

so an individual paired half can be exactly positive definite. Reality
coupling of the involution therefore does not force a negative direction
in each half. The other half has three negative directions, leaving the
paired sum nonzero. This row does not produce a positive paired block.

For a nonsingular even paired branch, define the relevant floor

\[
 \nu_{\rm ev}
 :=\min\{n_{13}(Q):
          Q\in\mathscr V_{13},\
          n_{13}(Q)\ {\rm even},\
          \det K_{13}(Q)\ne0\}.                 \tag{25}
\]

The sum-two witness proves only \(\nu_{\rm ev}\le 2\). Since (25) is a
nonnegative even integer, the unresolved alternatives are

\[
 \nu_{\rm ev}=0\qquad\hbox{or}\qquad
 \nu_{\rm ev}=2.                               \tag{26}
\]

No displayed point attains the first alternative. That finite non-
observation is not an emptiness proof. If a nonsingular zero-sum point
exists, its paired inertia is `(8,0,0)` and the positive self blocks in
(15) assemble it to `(16,0,0)`. Conversely, on this blockwise assembly,
full positivity forces zero negative count in the paired block. This is
the precise sense in which the zero-sum decision is equivalent to full
positivity of a circulant assembly.

What is decided is:

1. global oddness of `n_{13}` is false;
2. a paired determinant-orientation invariant is false;
3. the displayed chart attains each sum in (23); and
4. the first half can be exactly definite.

What is not decided is:

1. whether a nonsingular zero-sum paired branch exists;
2. whether the even-branch floor in (25) is two;
3. whether (23) exhausts the attainable sums or real components; or
4. whether any point in the complete circulant or mixed variety is
   positive.

## 7. The Mixed Slices

Let `C_circ,c` be the Block 111 circulant joint class and let

\[
 \mathscr X_c\simeq\mathbb R^4                 \tag{27}
\]

be the Block 109 pure `x`-parity class. A general element of the inherited
linear joint space is

\[
 M(A,x)=A+X(x),
 \qquad A\in\mathscr C_{{\rm circ},c},\quad
 x\in\mathscr X_c.                              \tag{28}
\]

A genuinely mixed point has both `A\ne0` and `x\ne0`. The complete
involution and positivity problem for (28) remains nonlinear and is not
solved here.

The runner does close both displayed structured slices. For
\(\alpha\in\{1,2\}\), let `I_{\rm mix}^{(\alpha)}` denote the
corresponding exact slice ideal. Its real solution set obeys

\[
 \begin{aligned}
 \mathscr V_{\mathbb R}(I_{\rm mix}^{(\alpha)})
  ={}&
  \bigl(\mathscr V_{\mathbb R}(I_{\rm mix}^{(\alpha)})
         \cap\{x=0\}\bigr)\\
 &{}\cup
  \bigl(\mathscr V_{\mathbb R}(I_{\rm mix}^{(\alpha)})
         \cap\{A=0\}\bigr).                    \tag{29}
 \end{aligned}
\]

Therefore every solution in every displayed structured slice lies on an
unmixed axis: the circulant axis `x=0` or the four-dimensional parity axis
`A=0`. In particular,

\[
 \mathscr V_{\mathbb R}(I_{\rm mix}^{(\alpha)})
 \cap\{A\ne0,\ x\ne0\}=\varnothing.            \tag{30}
\]

Equations (29)--(30) are complete for the displayed slice ideals and
nothing wider. They do not prove that the complete mixed variety has no
mixed involution, do not turn the pure axes into positive solutions, and
do not change the zero-sum gate in Section 6.

## 8. No-Go Discipline Gate

There is exactly one bounded finite-carrier wall.

- `W1` — **REFUTATION:** on the displayed momentum-factorized circulant
  involution variety, the global-odd paired-parity hypothesis and the
  paired determinant-orientation invariant are refuted. The exact even
  witness has paired count two and the opposite determinant sign from the
  odd base point. On the same scope, the displayed structured mixed slices
  contain no genuinely mixed involution: their exact real solution sets
  lie on the two unmixed axes.

The wall is refutation-shaped. It rejects two global readings of the
Block 111 odd germ and one existence reading inside the displayed mixed
slices. It does not assert a positive dressing, classify every real
component, decide zero-sum existence, prove the even-branch floor, or
close the complete mixed variety.

The exact scope is the displayed carrier, the two rational fixtures, the
paired chart and displayed chart points, the positive self-block choices,
and the displayed structured mixed slices. `W1` is not a transporter
impossibility or an OS or gravity theorem.

### N1 — Alternative Route Enumeration

Routes are normalized by `(object, mechanism, terminal)`. An exact
countercertificate against global oddness is distinguished from a
displayed attained-sum chart and from a structured-slice elimination.

1. **PROVED — paired involution variety / exact even chart witness /
   global-odd parity and full assembly.** At `c=5/13`, equations
   (13)--(17) give exact reality coupling, exactly Hermitian Gram halves,
   leading-minor strings `+---` and `++--`, half counts `(1,1)`, and
   paired sum two. The resulting exact circulant involution has inertia
   `(14,2,0)` and positive determinant. This is the strongest row.
2. **PROVED — second rational fixture / same exact chart point / even
   paired branch.** At `c=3/5`, `Q_{\rm ev}` has exact leading-minor
   strings `+-++` and `---+`, half counts `(2,2)`, and paired sum four.
   It assembles with the exactly positive self blocks to `(12,4,0)`.
   This is an independent fixture certificate, not a path argument.
3. **PROVED — displayed paired points / exact determinant and inertia /
   orientation.** The odd base point has count one and negative paired
   determinant; the even witness has count two and positive paired
   determinant. The sign flip refutes a class-wide paired determinant-
   orientation invariant.
4. **PROVED — displayed definite-half point / exact leading-minor
   inertia / individual-half definiteness.** The half counts `(0,3)`
   prove that the first half can be exactly positive definite. The total
   remains three, so this row does not settle zero-sum existence.
5. **ATTEMPTED — two displayed structured mixed slices / exact elimination
   / mixed involution.** Equations (29)--(30) prove that every solution in
   either displayed slice lies on an unmixed axis. This completely closes
   those two slices and nothing beyond them.
6. **UNTESTED — LIVE — complete paired and mixed varieties /
   componentwise zero-sum and floor decision, then full mixed solve /
   positivity.** This `UNTESTED-LIVE` route must decide whether the even
   paired branch reaches zero or has floor two, then solve the complete
   mixed variety. It is not counted as an attempted route against the
   displayed refutations in `W1`.

### N2 — Wall-Independence Audit

There is one current wall, so no pairwise current-wall table is needed. It
is independent of Block 111's `W1`, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:524-540`.

Block 111 refutes a fixed determinant and total-index parity obstruction
on the circulant class by changing only the `k=0` self branch. Its paired
block stays at the displayed odd germ. The present wall instead keeps the
self blocks positive and changes the paired branch itself, producing
paired counts two and four. A self-branch parity change cannot prove the
paired refutation, and the paired refutation does not reproduce the
self-branch factorization.

The structured-family clauses are also independent. Block 111 closes
three equal-block subfamilies inside the pure circulant variety. The
present clause closes displayed slices of the circulant-plus-parity
mixture by proving that their solutions lie on unmixed axes. Equality-
subfamily emptiness and mixed-slice axis confinement are different
residuals; neither implies the other.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified
explicitly.

| lowercase hit | classification |
|---|---|
| `displayed d=2 carrier` | the exact Blocks 107--111 finite carrier |
| `two displayed rational shear fixtures` | exactly `c=5/13` and `c=3/5` |
| `momentum-factorized circulant involution variety` | the Block 111 circulant class, not every global operator |
| `paired k=1,3 sector` | the conjugate momentum pair, with self sectors excluded |
| `r(q)(d+n)r(q)^-1 chart` | the displayed paired involution chart only |
| `exact reality coupling` | the exact `k=1` to `k=3` relation (9) |
| `exactly hermitian paired gram blocks` | exact identity (11), not numerical symmetry |
| `leading-minor signs +--- and ++--` | exact first-fixture witness signs |
| `paired negative counts one and one` | exact half counts at `Q_ev` |
| `full inertia (14,2,0)` | exact first-fixture circulant assembly |
| `second-fixture signs +-++ and ---+` | exact half-count split `(2,2)` |
| `second-fixture inertia (12,4,0)` | exact same-chart-point assembly at `c=3/5` |
| `paired determinant sign equals parity sign` | exact nonsingular Hermitian identity at displayed points |
| `paired orientation flips` | negative at count one and positive at count two |
| `attained paired sums {1,2,3,4}` | exact displayed witnesses, not an exhaustive global range |
| `definite-half counts (0,3)` | exact first-half definiteness with nonzero total |
| `zero-sum untested-live` | no displayed zero and no nonexistence theorem |
| `paired floor untested-live` | the alternatives in (26) remain open |
| `two structured mixed slices have only unmixed axes` | exact closure of the displayed slice ideals only |
| `four-dimensional x-parity space` | the inherited Block 109 complement |
| `not a transporter impossibility` | scope firewall for `w1` |
| `no axiom amendment is justified` | constitutional firewall |
| `zero obligation retirement` | TOE accounting firewall |
| `no toe percentage moves` | TOE accounting firewall |
| `retained-positive end-to-end theory count remains zero` | audit-status accounting |
| `actual adm/history transporter remains unexecuted` | partial-closure statement only |
| `n1 n2 n3 n4 n5 n6 n7 n8` | every discipline gate is present |
| `w1` | the wall set has exactly one member |
| `per_element per_site per_mode per_block lattice_wide` | the five N5 resolution keys |

No phrase upgrades an even paired witness into positivity, turns failure
to display sum zero into a floor theorem, or widens structured-slice axis
confinement to the complete mixed variety.

### N4 — Residual Matching

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 111 Next Decision](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:747-764` | decide paired parity globally, then solve the mixed variety before OS and gravity | equations (13)--(22) refute global oddness and paired orientation; equations (23)--(26) isolate the still-live zero-sum and floor decision; equations (29)--(30) close only displayed mixed slices |
| [Block 111 paired boundary](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:397-439` | the displayed paired germ has odd negative count, while other real components remain live | the exact sum-two witness refutes the global-odd alternative; the zero-sum component decision remains live |
| [Block 111 mixture frontier](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:440-522` | the complete circulant-plus-`A_star` variety survives the grading split | equations (27)--(30) prove only that the displayed structured slices contain unmixed axes |
| [Block 110 momentum factorization](ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md:382-457` | four exact momentum-slice involution problems with inherited reality relations | equations (5)--(14) enter the paired `k=1,3` slice chart, preserve exact reality coupling, and certify the even witness |
| [Block 109 global split](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:161-239` | the global joint space contains the four-dimensional pure `x`-parity complement | equations (27)--(30) retain that full complement while making only structured-slice claims |

Every inherited residual reaches its stated interface. No citation is used
as an audit verdict.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the displayed Blocks 107--111
carrier, both displayed rational shear fixtures, and the displayed paired
chart inside the circulant involution variety, the exact sum-two and
sum-four witnesses refute global odd paired parity and any class-wide
paired determinant orientation; the first witness assembles to
`(14,2,0)` with positive determinant, the displayed sums are
`{1,2,3,4}`, and the displayed structured mixed slices contain only
unmixed axes, while zero-sum existence, the paired floor, and the complete
mixed variety remain open.”

Forbidden upgrades include “a positive dressing exists,” “the floor is
proven,” “a paired zero-sum point exists,” “no paired zero-sum point
exists,” “the displayed sums exhaust the paired variety,” “the complete
mixed variety has only unmixed axes,” “curved OS is closed,”
“ADM/history transport is finished,” “the gravity quotient has been
executed,” “an axiom amendment is required,” and “a TOE obligation is
retired.”

The five resolution lines from the runner specification are reproduced
verbatim:

```text
per_element: exact witness, coupling, minor-sign, assembly, and orientation identities are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: the even paired branch exists at both displayed shear fixtures with even sums two and four
per_block: the displayed attained paired sums include one and two and a definite-half point while zero remains unobserved
lattice_wide: checked and not executed — the paired zero-sum decision, the paired floor, the mixed dressing variety, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The remaining decisions are exact
finite action and representation problems inside the inherited carrier.

| route | present status | remaining terminal |
|---|---|---|
| paired involution chart | exact `R(Q)(D+N)R(Q)^{-1}` involutions with exact reality coupling | classify the real chart components relevant to zero sum |
| first-fixture even witness | exact half counts `(1,1)` and full inertia `(14,2,0)` | remove the final two negative directions |
| second-fixture same point | exact half counts `(2,2)`, paired sum four, and full inertia `(12,4,0)` | decide fixture-uniform zero-sum reachability |
| paired determinant orientation | exact negative-to-positive sign change between displayed points | none for the global-orientation refutation |
| attained-sum chart | exact displayed sums `{1,2,3,4}` | decide whether zero is attained |
| definite-half point | exact half counts `(0,3)` | make both halves definite compatibly |
| displayed structured mixed slices | exact unmixed-axis confinement | leave the displayed slice restrictions |
| even-branch paired floor | bounded above by two, not decided | prove zero-sum existence or prove floor two |
| complete mixed variety | not solved | solve the full circulant-plus-four-dimensional-parity involution and positivity equations |
| OS and gravity route | not executed | carry any positive dressed reflection through OS, then form the gravity constraint quotient |

The scan finds no axiom-amendment route. A positive dressing has not been
produced, and the absence of a displayed zero is not counted as evidence
for floor two.

### N7 — Steelman

**Hostile steelman against overreading the wall.** The even paired branch
might still have floor two. The exact sum-two witness disproves global
oddness but may sit on a component whose Hermitian Gram cannot lose its
last two negative directions without becoming singular. The
`(0,3)` witness shows that one half can be definite, yet the exact reality
and involution equations may force the other half to carry negative
directions whenever the first has none.

The opposite possibility remains equally live: an unvisited real component
or sign cell may contain half counts `(0,0)` and therefore a positive
circulant assembly. The displayed chart attains four successive sums but
does not prove that its list is exhaustive. That is exactly why the zero-
sum decision and the even-branch paired floor are named together.

The current wall claims only what its exact countercertificates reach:
global oddness is false, a global paired determinant orientation is false,
and the displayed structured mixed slices contain no genuinely mixed
point. It does not choose between floor two and zero-sum existence. If
floor two survives the componentwise decision, the complete mixed variety
is the honest next frontier.

### N8 — Cross-Cycle Echo

| earlier exact boundary | echo here |
|---|---|
| [Block 109's global joint space](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:161-239` | the four-dimensional pure `x`-parity complement is kept intact; only displayed structured mixture slices are confined to axes |
| [Block 110's momentum factorization](ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md:382-457` | the `k=1,3` paired slice is entered through an exact involution chart with its inherited reality relation |
| [Block 111's paired boundary](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:397-439` | the odd germ is confronted by exact even witnesses, refuting global oddness while leaving zero sum undecided |
| [Block 111's mixture frontier](ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md:440-522` | exact slice elimination makes narrow progress without closing the complete mixed variety |

The repeated discipline is to let an exact even counterexample refute the
odd global hypothesis, while refusing to convert a finite attained-sum
chart into a zero-sum existence or nonexistence theorem.

**No-Go Discipline verdict:** **PASS** only for narrow `W1`: the global-
odd paired-parity hypothesis and paired determinant-orientation invariant
are refuted by exact displayed points, and the displayed structured mixed
slices contain only unmixed axes. **FAIL** for a positive dressing, the
zero-sum decision, the paired floor, the complete circulant or mixed
variety, transporter completion, curved OS positivity, gravity, axiom
necessity, or TOE.

## 9. Axiom And TOE Disposition

No axiom amendment is justified. The paired chart, reality coupling,
Hermiticity, leading-minor inertia, blockwise assembly, determinant parity,
and structured mixed-slice elimination are finite consequences of the
displayed carrier and dressing classes; no new primitive is assumed.

This is bounded route progress, not an audit-grade assignment. It retires
no end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 10. Next Decision

The shortest high-value sequence is:

1. decide whether a paired branch with zero negative count exists and
   thereby prove or refute the even-branch paired floor;
2. solve the complete mixed circulant-plus-`A_star` dressing variety;
3. carry any positive dressed reflection through the OS package; and
4. only then form the gravity constraint quotient.

The actual ADM/history transporter remains unexecuted beyond the displayed
even paired witnesses, orientation refutation, attained-sum chart, and
structured mixed-slice closures.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted.
