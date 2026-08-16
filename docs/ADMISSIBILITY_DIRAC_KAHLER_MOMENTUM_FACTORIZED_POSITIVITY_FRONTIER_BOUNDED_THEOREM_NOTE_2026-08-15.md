---
claim_id: admissibility_dirac_kahler_momentum_factorized_positivity_frontier_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the Blocks 107-110 seam carrier, the circulant dressing class factorizes exactly over spatial momenta--projector conjugation pairs k=1 with k=3, the projector-resolved joint dimensions 48+96+48=192 are exactly additive, and the involution and Gram decouple blockwise so inertia adds--while the Block 109 joint space is exactly the direct sum of the 128-dimensional circulant class and the four-dimensional pure x-parity class, spanned by structures whose displayed representative is the Block 109 involution itself, the classes being genuinely different because the half-shift is independent of the earlier spatial basis; the displayed file-point assembly is an exact involution with Gram inertia (15,1,0) and negative determinant, whereas the displayed k=0 branch witness has block inertia (3,1,0) and the displayed exact negative determinant and flips all eight assemblies to positive determinant with even positive indices exactly {2,4,6,8,8,10,12,14}, best (14,2,0), so the determinant obstruction is refuted and no fixed index parity exists on the circulant involution class; at the displayed base points the paired sector contributes an odd negative count, a germ-local observation whose global decision is the named gate; the displayed equal-block even-subclass structured subfamilies are exactly empty; mixtures of circulant elements with the x-parity involution are pinned by neither grading sign, as the exact split identities show; positivity itself, the global parity decision, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_seam_dressing_sector_signature_bounded_theorem_note_2026-08-15
runner: scripts/admissibility_dirac_kahler_momentum_factorized_positivity_frontier_2026_08_15.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_seam_dressing_sector_signature_bounded_theorem_note_2026-08-15
target_blocker_text: "Solve the even-sector involution variety through the exact spatial-momentum factorization; any positive dressed reflection then feeds the OS package and the gravity constraint quotient."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Decide the paired-sector parity globally on the paired involution variety; solve the mixed circulant-plus-A-star dressing variety; any positive dressed reflection feeds the OS package and the gravity constraint quotient."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-110 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact momentum-projector decomposition, exact rational dimension and direct-sum certificates, exact block involution and Gram identities, exact determinant factorizations and inertia assemblies, exact structured-family emptiness certificates, and exact grading-split identities on the declared d=2 carrier; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Momentum-Factorized Positivity Frontier

**Date:** 2026-08-15

**Campaign block:** 111

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_momentum_factorized_positivity_frontier_2026_08_15.py`](../scripts/admissibility_dirac_kahler_momentum_factorized_positivity_frontier_2026_08_15.py)

## 1. Result Up Front

[Block 110](ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md:699-713`:

> Solve the even-sector involution variety through the exact spatial-momentum
> factorization; any positive dressed reflection then feeds the OS package and
> the gravity constraint quotient.

The frontier has three exact parts. First, the circulant class really does
factor over spatial momenta. The self-conjugate sectors are `k=0` and `k=2`;
complex conjugation pairs `k=1` with `k=3`. The projector-resolved joint
carrier has the exactly additive real-dimension count

\[
 48+96+48=192.                                  \tag{1}
\]

The involution equations and the two-history Gram both decouple on these
blocks. Their inertias therefore add.

Second, the displayed file point is an exact near-positive involution. Its
three Gram blocks have exact inertias

\[
 (4,0,0)_{0}\mathbin\oplus(7,1,0)_{13}
 \mathbin\oplus(4,0,0)_{2}=(15,1,0),            \tag{2}
\]

and its determinant certificate is

\[
 \det\mathcal K_{\rm fp}
 =\Delta_0^+\Delta_{13}^+\Delta_2^+<0.          \tag{3}
\]

Here each `Delta` is the exact rational block determinant printed by the
runner; the signs in (3), rather than decimal eigenvalue tails, are used.
All eight sign assemblies at this base point have odd positive index and
negative determinant. Their positive indices, with multiplicity, are

\[
 \{1,5,5,7,9,11,11,15\}.                       \tag{4}
\]

Third, that chart is not an obstruction. The displayed second branch of the
`k=0` self sector has exact inertia `(3,1,0)` and exact determinant

\[
 \det\mathcal K_0(w_0)=\Delta_0^\flat<0.        \tag{5}
\]

Replacing only the `k=0` base branch by this witness makes every one of the
eight assemblies have positive determinant. Their positive indices become

\[
 \{2,4,6,8,8,10,12,14\},                       \tag{6}
\]

and the best displayed assembly is exactly

\[
 (3,1,0)_0\mathbin\oplus(7,1,0)_{13}
 \mathbin\oplus(4,0,0)_2=(14,2,0).              \tag{7}
\]

Thus the negative-determinant reading of the odd chart is refuted. There is
no fixed determinant sign and no fixed index parity on the circulant
involution class. The one remaining parity question is narrower: the paired
`k=1,3` sector contributes one negative direction at the displayed base
points. That is a germ-local certificate, not a theorem on its whole
involution variety. Deciding that parity globally is the named next gate.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main b8d9f4c40125e45415d6dd240a7ef806e773a278`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`, as inherited from the Block
110 authority snapshot.

The exact stacked parent is
[Block 110](ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `d6761278fca9cac617200792473a8f4da3a6cfff`, content-bound through note
blob `8401946b778d8d41b0a553d0844f59e616c22e9f`. Its direct parent is
[Block 109](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `ad84cfcc857a65285389ba93b47cd7b718589be5`, content-bound through note
blob `3ed51ad603b3c4dc9a0e9eb3c98e343b49c3b9ea`. The global-support premise is
the exact conclusion of
[Block 108](ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `8afe8dff5ccf531208238af0aaaec1f547d73874`, note blob
`21128ab10b32d4f99190ce7107ef9fb790a05781`. No audit verdict is imported.

The executed contract is:

1. the Blocks 107--110 `d=2` one-fine-mode carrier on
   `Z8_t x Z4_x`, ordered time first with representatives `-4,...,3`;
2. antiperiodic time closure and the antilinear link-centered reflection
   `theta(t)=-1-t`;
3. the step-shear history `(-c,-c,-c,0,c,c,c,0)`, with `m=9/20`, `v=1`,
   and the two exact fixtures `c=5/13` and `c=3/5`;
4. the full positive span `Lambda_+={0,1,2,3} x Z4` and the inherited exact
   two-history target-arm Gram convention;
5. the complete four-power circulant spatial dressing carrier, its exact
   momentum projectors, the Block 109 pure `x`-parity complement, the three
   displayed equal-block reductions, and their displayed mixture class;
6. exact projector algebra, exact rational nullspaces and ranks, exact
   involution residuals, exact characteristic and determinant arithmetic,
   exact inertia by rational certificates, and exact split identities only.

The exact scope is the displayed `d=2` carrier, the two displayed rational
shear fixtures, the displayed circulant and `x`-parity classes, the displayed
file and branch points, and the displayed structured subfamilies. Positivity
on the full variety, the global paired-sector parity decision, curved OS
positivity, the completed ADM/history transporter, joint gravity, the
gravity constraint quotient, Records, retention, axiom amendment,
obligation retirement, and TOE percentage movement are outside the executed
contract.

## 3. The Momentum Factorization

Let `C` be the real unit shift on the four-site spatial cycle and set
`omega=i`. Its exact Fourier projectors are

\[
 E_k={1\over4}\sum_{r=0}^3\omega^{-kr}C^r,
 \qquad k\in\{0,1,2,3\}.                         \tag{8}
\]

They obey

\[
 E_kE_l=\delta_{kl}E_k,
 \qquad \sum_{k=0}^3E_k=I_4,
 \qquad \overline{E_k}=E_{-k\ ({\rm mod}\ 4)}. \tag{9}
\]

Thus `E_0` and `E_2` are self-conjugate, while `E_1` and `E_3` form one
conjugate pair. For any dressing `A` in the complete circulant class,

\[
 [A,I_8\mathbin\otimes C]=0,
 \qquad
 A=\bigoplus_{k=0}^3 A(k).                      \tag{10}
\]

The reflection-reality and full-span-Hermiticity maps preserve the two
self sectors and exchange the paired sectors. Exact elimination on the
three real projector carriers gives

\[
 \begin{array}{c|ccc}
 \hbox{projector carrier}&0&(1,3)&2\\
 \hline
 \hbox{exact joint dimension}&48&96&48.
 \end{array}                                    \tag{11}
\]

The concatenated projector bases have rank `192`, pairwise intersections
zero, and reproduce the complete projector-resolved joint carrier. Hence
the count in (1) is exact additivity, not dimension subtraction.

Both nonlinear objects inherit the same decomposition:

\[
 A^2-I_{32}
 =\bigoplus_{k=0}^3\bigl(A(k)^2-I_8\bigr),
 \qquad
 \mathcal K_A
 =\mathcal K_0(A)\mathbin\oplus
  \mathcal K_{13}(A)\mathbin\oplus\mathcal K_2(A). \tag{12}
\]

The Gram block sizes are `4`, `8`, and `4`. Therefore

\[
 \operatorname{In}\mathcal K_A
 =\operatorname{In}\mathcal K_0(A)
  +\operatorname{In}\mathcal K_{13}(A)
  +\operatorname{In}\mathcal K_2(A),            \tag{13}
\]

component by component. In particular, determinants multiply and inertia
adds without a cross-momentum correction.

There is one necessary framing correction. In Block 110, “even sector
dimension 128” referred to the joint class carried by

\[
 S_0=I_4,\qquad S_2=C+C^{-1},\qquad S_3=C-C^{-1}. \tag{14}
\]

The full circulant ambient basis also contains the half-shift `C^2`. It is
genuinely independent of (14), even over `C`. Indeed, if

\[
 C^2=\alpha S_0+\beta S_2+\gamma S_3,           \tag{15}
\]

then evaluation at `k=0,2` gives `alpha=1` and `beta=0`, whereas evaluation
at `k=1,3` demands simultaneously `gamma=i` and `gamma=-i`. This is
impossible.

Exact joint elimination nevertheless gives no new admissible dimension in
the half-shift direction. If `C_circ,c` is the complete circulant joint
nullspace and `C_S,c` is the Block 110 `S_0,S_2,S_3` nullspace, then

\[
 \mathscr C_{S,c}=\mathscr C_{{\rm circ},c},
 \qquad
 \dim_{\mathbb R}\mathscr C_{{\rm circ},c}=128 \tag{16}
\]

at both fixtures. Equation (11) counts the additive projector-resolved
joint carrier on which the final nullspace equations act; equation (16)
counts their admissible dressing nullspace. They are different linear
objects and therefore not competing dimension statements.

Finally, let `X_c` denote the pure `x`-parity joint class. The exact Block
109 relationship, now stated without conflating its ambient spatial bases,
is

\[
 \mathscr L_c=\mathscr C_{{\rm circ},c}\mathbin\oplus\mathscr X_c,
 \qquad
 132=128+4.                                     \tag{17}
\]

The intersection is zero and the concatenated exact bases have rank `132`
at both fixtures. The Block 109 involution `A_star` is the displayed member
of the four-dimensional `X_c`; its spatial factor is the pure parity field
`D_x`. Thus the circulant and parity classes are genuinely different even
though the extra independent half-shift adds no admissible joint dimension.

## 4. The Near-Positive Certificates

Write an assembly sign as `(epsilon_0,epsilon_13,epsilon_2)`, with every
entry in `{+1,-1}`. At the displayed file point the positive representatives
of the three momentum blocks have the exact inertias in (2). Negating a
Hermitian block exchanges its positive and negative indices. Because all
three block sizes are even, negation does not change any block determinant.

The complete base-point assembly chart is therefore

| assembly | `In K_0` | `In K_13` | `In K_2` | `In K` | `sign det K` |
|---|---:|---:|---:|---:|---:|
| `(+,+,+)` | `(4,0,0)` | `(7,1,0)` | `(4,0,0)` | `(15,1,0)` | `-` |
| `(+,+,-)` | `(4,0,0)` | `(7,1,0)` | `(0,4,0)` | `(11,5,0)` | `-` |
| `(+,-,+)` | `(4,0,0)` | `(1,7,0)` | `(4,0,0)` | `(9,7,0)` | `-` |
| `(+,-,-)` | `(4,0,0)` | `(1,7,0)` | `(0,4,0)` | `(5,11,0)` | `-` |
| `(-,+,+)` | `(0,4,0)` | `(7,1,0)` | `(4,0,0)` | `(11,5,0)` | `-` |
| `(-,+,-)` | `(0,4,0)` | `(7,1,0)` | `(0,4,0)` | `(7,9,0)` | `-` |
| `(-,-,+)` | `(0,4,0)` | `(1,7,0)` | `(4,0,0)` | `(5,11,0)` | `-` |
| `(-,-,-)` | `(0,4,0)` | `(1,7,0)` | `(0,4,0)` | `(1,15,0)` | `-` |

Every row is an exact involution assembly. The chart is not an eigenvalue
sample: the runner checks each block involution exactly, proves the Gram
blocks Hermitian exactly, and obtains each inertia by exact sign data. The
file point in the first row is the closest displayed base certificate,
missing positivity by one negative direction.

The negative determinants have one transparent source. The two self blocks
are positive definite in their positive representatives, while the paired
representative has inertia `(7,1,0)`. Thus

\[
 \operatorname{sign}\Delta_0^+=+1,
 \qquad \operatorname{sign}\Delta_{13}^+=-1,
 \qquad \operatorname{sign}\Delta_2^+=+1.       \tag{18}
\]

It is tempting to turn (18) and the all-odd positive indices in the chart
into a parity obstruction. Section 5 gives the exact counterexample to that
reading.

## 5. The Determinant Refutation

On each self-conjugate branch, the exact `4 x 4` Gram determinant splits
into its four rational linear eigenvalue factors. In the runner's branch
coordinates `q_k`,

\[
 d_k(q_k):=\det\mathcal K_k(q_k)
 =\ell_{k,1}(q_k)\ell_{k,2}(q_k)
  \ell_{k,3}(q_k)\ell_{k,4}(q_k),
 \qquad k\in\{0,2\}.                            \tag{19}
\]

Every `ell_{k,r}` is an exact rational linear form obtained before any
inertia classification. This factorization matters: a self branch can cross
one linear determinant wall without changing the paired block or the other
self block.

The displayed `k=0` witness `w_0` lies on the opposite side of exactly one
such wall. Its four nonzero factors have a `3+1` sign split, so

\[
 \operatorname{In}\mathcal K_0(w_0)=(3,1,0),
 \qquad
 d_0(w_0)=\Delta_0^\flat
 =\prod_{r=1}^4\ell_{0,r}(w_0)<0.               \tag{20}
\]

Equation (20) is the displayed exact determinant certificate: it is the
runner's exact rational product at `w_0`, not a floating-point determinant
or a sign inferred from approximate eigenvalues.

Keep the paired and `k=2` representatives fixed and replace only the `k=0`
representative. The complete sign chart becomes

| assembly | `In K_0(w_0)` | `In K_13` | `In K_2` | `In K` | `sign det K` |
|---|---:|---:|---:|---:|---:|
| `(+,+,+)` | `(3,1,0)` | `(7,1,0)` | `(4,0,0)` | `(14,2,0)` | `+` |
| `(+,+,-)` | `(3,1,0)` | `(7,1,0)` | `(0,4,0)` | `(10,6,0)` | `+` |
| `(+,-,+)` | `(3,1,0)` | `(1,7,0)` | `(4,0,0)` | `(8,8,0)` | `+` |
| `(+,-,-)` | `(3,1,0)` | `(1,7,0)` | `(0,4,0)` | `(4,12,0)` | `+` |
| `(-,+,+)` | `(1,3,0)` | `(7,1,0)` | `(4,0,0)` | `(12,4,0)` | `+` |
| `(-,+,-)` | `(1,3,0)` | `(7,1,0)` | `(0,4,0)` | `(8,8,0)` | `+` |
| `(-,-,+)` | `(1,3,0)` | `(1,7,0)` | `(4,0,0)` | `(6,10,0)` | `+` |
| `(-,-,-)` | `(1,3,0)` | `(1,7,0)` | `(0,4,0)` | `(2,14,0)` | `+` |

The two negative block determinants, from `k=0` and the paired sector,
multiply to a positive total determinant in every row. The even positive-
index multiset is exactly (6), and the first row proves the best displayed
inertia `(14,2,0)`.

There is also a concise parity formula. On any nonsingular sign cell under
discussion, set

\[
 u_0=d_0(q_0),\qquad u_2=d_2(q_2).              \tag{21}
\]

The paired determinant is negative at the displayed base germ. Since the
sign of the determinant of a nonsingular Hermitian matrix is `(-1)^n`, the
total negative index obeys

\[
 n=1+\mathbf 1_{\{u_0<0\}}
      +\mathbf 1_{\{u_2<0\}}\pmod 2.            \tag{22}
\]

At the file point both self determinants are positive and `n` is odd. At
`w_0`, `u_0<0`, `u_2>0`, and `n` is even. Two exact circulant involution
points with opposite index parity suffice to refute a class-wide parity
law. Hence no fixed determinant or index parity obstruction exists on the
circulant involution class.

This refutation does not produce a positive point. The best displayed point
still has two negative directions. It removes one proposed obstruction and
exposes the paired-sector boundary; it does not close that boundary.

## 6. The Paired-Sector Parity Boundary

At every displayed base point, the paired `k=1,3` Gram block has one of the
two exact inertias

\[
 (7,1,0)_{13}\qquad\hbox{or}\qquad(1,7,0)_{13}. \tag{23}
\]

Thus `n_1+n_3` is odd there. This is stronger than observing a negative
total determinant at one assembly because it locates the odd contribution
inside the conjugate momentum pair. It is still only germ-local. Inertia is
locally constant away from the paired determinant-zero locus, so (23)
controls the displayed nonsingular germs and nothing beyond their connected
sign cells.

The paired involution variety may have other real components. A path between
components need not stay nonsingular, and an algebraically separate branch
need not inherit the determinant sign of the displayed branch. Neither the
eight-assembly chart nor the self-branch factorization decides those cases.

The exact decision problem is therefore

\[
 \operatorname{sign}\det\mathcal K_{13}(B)
 \quad\hbox{on every real component of}\quad
 \mathscr V_{13}
 =\{B:B^2=I,\ B\hbox{ obeys the paired joint equations}\}. \tag{24}
\]

There are two possible outcomes, and this note proves neither one:

1. if the paired negative count is globally odd on `V_13`, circulant
   positivity is impossible and the mixed circulant-plus-`A_star` variety
   becomes the positivity frontier; or
2. if another paired branch has even negative count, a circulant assembly
   with inertia `(16,0,0)` may exist on that branch after compatible self-
   branch selection.

The first alternative is the strongest hostile reading of the displayed
data. Calling it a theorem before the componentwise decision in (24) would
turn a germ certificate into an unsupported global no-go.

## 7. Closures And The Mixture Frontier

Three displayed equal-block structured reductions of the even subclass are
closed exactly. Denote their exact polynomial systems, in the runner's
displayed order, by `I_eq^(1)`, `I_eq^(2)`, and `I_eq^(3)`. Exact
elimination gives

\[
 \mathscr V_{\mathbb R}(I_{\rm eq}^{(1)})
 =\mathscr V_{\mathbb R}(I_{\rm eq}^{(2)})
 =\mathscr V_{\mathbb R}(I_{\rm eq}^{(3)})
 =\varnothing.                                  \tag{25}
\]

These are complete emptiness statements for the three displayed structured
subfamilies. They are not an emptiness statement for the whole circulant
involution variety, whose nonequal blocks include both exact charts above.

The complementary Block 109 structure is concrete. With `r(i)=7-i`, the
symmetric sign vector

\[
 (s_0,\ldots,s_7)=(1,-1,1,-1,-1,1,-1,1),       \tag{26}
\]

and $D_x=\operatorname{diag}(1,-1,1,-1)$, its displayed representative is

\[
 X:=A_\star,
 \qquad X_{ij}=\delta_{j,r(i)}s_iD_x,
 \qquad X^2=I_{32}.                             \tag{27}
\]

This identifies `A_star` as the displayed involution in the four-dimensional
pure `x`-parity class in (17). It is not circulant: conjugation by the unit
spatial shift $Q=I_8\mathbin\otimes C$ gives

\[
 \Gamma(A)=QAQ^{-1}=A
 \quad(A\in\mathscr C_{{\rm circ},c}),
 \qquad
 \Gamma(X)=-X.                                  \tag{28}
\]

Now form the exact mixture

\[
 M=A+\lambda X,
 \qquad A\in\mathscr C_{{\rm circ},c}.          \tag{29}
\]

Because `Gamma` is an algebra automorphism, the even and odd parts of its
involution residual split exactly:

\[
 \begin{aligned}
 \Pi_{\rm ev}(M^2-I)&=A^2+(\lambda^2-1)I,\\
 \Pi_{\rm odd}(M^2-I)&=\lambda\{A,X\}.
 \end{aligned}                                  \tag{30}
\]

The Gram is linear in the dressing and has the corresponding exact split:

\[
 \begin{aligned}
 {1\over2}\bigl(\mathcal K_M
      +Q\mathcal K_MQ^{-1}\bigr)&=\mathcal K_A,\\
 {1\over2}\bigl(\mathcal K_M
      -Q\mathcal K_MQ^{-1}\bigr)&=\lambda\mathcal K_X.
 \end{aligned}                                  \tag{31}
\]

Equations (30)--(31) pin the equations, not the mixture, to their grading
components. For `lambda` nonzero, a mixed involution asks for the scaled
circulant equation `A^2=(1-lambda^2)I` together with `{A,X}=0`; neither
identity forces `A=0` or `lambda=0`. If `K_M` is positive, averaging its two
unitarily conjugate copies makes `K_A` positive, but `A` then obeys a scaled
involution rather than the circulant unit-involution equation. Thus even a
globally odd answer to (24) would leave the mixed variety genuinely live.

The displayed exact split identities therefore prevent either grading sign
from disposing of mixtures. Solving (30) jointly with positivity of (31) is
the second named gate after the paired-sector parity decision.

## 8. No-Go Discipline Gate

There is exactly one bounded finite-carrier wall.

- `W1` — **REFUTATION:** on the displayed circulant involution class, the
  all-odd base-point assembly chart does not define a fixed determinant or
  index-parity obstruction. The displayed `k=0` branch witness changes the
  class parity exactly and makes all eight reconstructed determinants
  positive. On the same scope, the three displayed equal-block structured
  subfamilies of the even-subclass reduction are exactly empty.

The refuted negative claim is the obstruction reading of this block's own
odd-index chart, not a claim inherited from Block 110. The exact scope is the
displayed carrier, fixtures, circulant class, base and branch points, and the
three displayed equal-block reductions. `W1` does not assert positivity. It
does not decide the paired parity on every real component, close the complete
circulant variety, or close the mixed circulant-plus-`A_star` variety.

### N1 — Alternative Route Enumeration

Routes are normalized by `(object, mechanism, terminal)`. A refutation by
an exact countercertificate is distinguished from a local sign chart and
from a complete structured-family emptiness certificate.

1. **PROVED — circulant involution class / exact countercertificate / fixed
   determinant and index parity.** Equations (20)--(22) exhibit exact
   circulant involutions on both sides of the self-branch determinant wall.
   The base assembly has inertia `(15,1,0)` and negative determinant; the
   replacement assembly has inertia `(14,2,0)` and positive determinant.
   This refutes both proposed fixed obstructions and is the strongest row.
2. **PROVED — eight base-point assemblies / exact block sign assembly /
   near-positive chart.** Every row of Section 4 has odd positive index and
   negative determinant. It misleads only when that finite chart is read as
   a theorem on all branches; the `k=0` witness proves that extrapolation
   false.
3. **PROVED — self-conjugate momentum branches / exact linear determinant
   factorization / parity-wall mechanism.** Equation (19) factors each self-
   branch determinant into four exact rational linear forms. Crossing one
   factor changes determinant and index parity without altering the paired
   equations.
4. **ATTEMPTED — three displayed equal-block even reductions / exact
   elimination / involution.** The three displayed equality subfamilies have
   exactly empty real varieties by (25). This is a complete closure of those
   three reductions and nothing wider.
5. **PROVED — displayed paired-sector germs / exact inertia / local parity.**
   The paired block has inertia `(7,1,0)` or `(1,7,0)` throughout the
   displayed nonsingular germs. Its odd negative count is honestly scoped
   to those germs, not upgraded to every real component.
6. **UNTESTED — LIVE — paired involution variety and mixed variety /
   componentwise determinant decision and grading-split solve / positivity.**
   This `UNTESTED-LIVE` route must decide (24), then solve (30)--(31). It is
   not counted as an attempted route against the structured-family half of
   `W1`.

### N2 — Wall-Independence Audit

There is one current wall, so no pairwise current-wall table is needed. It
is independent of Block 110's `W1`, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md:487-505`.

Block 110 proves that every member of the four-dimensional odd sector has a
negation-symmetric Gram spectrum and hence cannot be positive. Its even-
sector clause closes only the displayed sparse truncations and permutation
support. The present wall starts within the surviving even route: it
momentum-factorizes the circulant class, refutes a proposed determinant-
parity obstruction there, and closes three different equal-block
subfamilies. Odd-sector signature and circulant parity are different
residuals. Repairing or refuting one does not repair or refute the other.

The mixed route also preserves this independence. `A_star` supplies the odd
component in (29), but (30) imposes a scaled circulant equation rather than
placing the mixture back in Block 110's pure odd sector. Therefore the odd-
sector theorem neither closes nor prejudges the mixed variety.

### N3 — Hidden-Wall And Phrase Scan

The required scope-certificate phrase scan is classified explicitly.

| lowercase hit | classification |
|---|---|
| `displayed d=2 carrier` | the exact Blocks 107--110 finite carrier |
| `two displayed rational shear fixtures` | exactly `c=5/13` and `c=3/5` |
| `complete four-power circulant spatial dressing carrier` | the declared `I,C,C^2,C^3` carrier, not every global operator |
| `projector conjugation pairs k=1 with k=3` | exact Fourier-projector reality relation |
| `joint dimensions 48+96+48=192` | additive projector-carrier count, not the admissible-nullspace count |
| `circulant class dimension 128` | exact admissible joint nullspace at both fixtures |
| `block 109 direct sum 128+4=132` | exact circulant plus pure `x`-parity decomposition |
| `half-shift c^2 is independent` | ambient spatial-basis fact, compatible with no new admissible dimension |
| `inertia adds blockwise` | exact Gram direct sum, not a numerical clustering |
| `file-point inertia (15,1,0)` | exact near-positive circulant involution certificate |
| `eight-assembly odd chart` | finite exact chart that does not fix parity globally |
| `k=0 witness inertia (3,1,0)` | exact determinant-changing self-branch certificate |
| `even indices {2,4,6,8,8,10,12,14}` | exact reconstructed positive-index multiset |
| `no fixed determinant or index parity obstruction` | refutation wall for the circulant involution class |
| `paired parity is germ-local` | exact displayed sign cells only |
| `three equal-block varieties are empty` | exact closure only of the displayed structured reductions |
| `mixed circulant-plus-a-star variety untested-live` | surviving graded nonlinear problem |
| `not a transporter impossibility` | scope firewall for `w1` |
| `no axiom amendment is justified` | constitutional firewall |
| `zero obligation retirement` | TOE accounting firewall |
| `no toe percentage moves` | TOE accounting firewall |
| `retained-positive end-to-end theory count remains zero` | audit-status accounting |
| `actual adm/history transporter remains unexecuted` | partial-closure statement only |
| `n1 n2 n3 n4 n5 n6 n7 n8` | every discipline gate is present |
| `w1` | the wall set has exactly one member |
| `per_element per_site per_mode per_block lattice_wide` | the five N5 resolution keys |

No phrase widens the exact determinant refutation to positivity, upgrades a
germ-local paired sign to a global theorem, or closes the mixed variety.

### N4 — Residual Matching

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 110 Next Decision](ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md:699-713` | solve the even-sector involution variety through exact spatial-momentum factorization, then feed any positive reflection to OS and gravity | equations (8)--(13) execute the exact factorization; equations (18)--(24) locate and narrow the positivity frontier without claiming a positive point |
| [Block 110 momentum factorization](ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md:382-457` | four independent slice involution problems with exact reality relations | equations (8)--(13) assemble the self sectors and conjugate pair, prove dimension additivity, and make blockwise inertia exact |
| [Block 109 global split](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:161-239` | a 132-dimensional reflection-real full-span-Hermitian global space whose full joint variety remains open | equations (14)--(17) correct the spatial-class framing and prove the exact `128+4=132` circulant-plus-parity direct sum |
| [Block 109 exact involution](ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:240-334` | `A_star` is a genuine globally supported `x`-parity involution | equations (26)--(31) identify it as the parity representative and derive the exact mixture splits |
| [Block 108 global-support forcing](ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:252-406` | identity continuation leaves nonzero far-block Hermiticity residuals and forces global dressing support | all current classes remain globally supported; momentum factorization reorganizes that support and never restores the excluded local continuation premise |

Every inherited residual reaches its stated interface. No citation is used as
an audit verdict.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the displayed Blocks 107--110
carrier, both displayed shear fixtures, and the displayed circulant dressing
class, the momentum projectors decouple the involution and Gram exactly; the
displayed `(15,1,0)` negative-determinant assembly and `(14,2,0)` positive-
determinant assembly refute any fixed determinant or index parity
obstruction, while the paired-sector parity and the mixed
circulant-plus-`A_star` variety remain open.”

Forbidden upgrades include “the transporter is positive,” “circulant
positivity is impossible,” “the paired sector is globally odd,” “a
positive circulant involution exists,” “curved OS is closed,”
“ADM/history transport is finished,” “the gravity quotient has been
executed,” “an axiom amendment is required,” and “a TOE obligation is
retired.” The phrase “circulant positivity is impossible” is permitted
only inside the explicit conditional alternative in Section 6, not as a
conclusion of this note.

The five resolution lines from the runner specification are reproduced
verbatim:

```text
per_element: exact momentum-projector, dimension-additivity, involution, determinant, inertia, parity, emptiness, and grading-split identities are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: the self-conjugate k=0 and k=2 branches and the conjugate k=1,3 pair factorize exactly and assemble blockwise
per_block: all eight sign assemblies and the determinant-changing k=0 branch witness are checked exactly, while the paired-sector parity decision remains global
lattice_wide: checked and not executed — the global paired-sector parity decision, mixed circulant-plus-A-star dressing variety, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The remaining work is an exact
component and mixture solve inside the displayed global dressing carrier.

| route | present status | remaining terminal |
|---|---|---|
| momentum projectors | exact `48+96+48=192` additive carrier and blockwise equations | none for the displayed factorization |
| class relationship | exact `128+4=132` circulant-plus-parity direct sum | none inside the Block 109 joint linear space |
| file-point chart | eight exact negative-determinant odd-index assemblies, best `(15,1,0)` | leave the displayed self-branch point |
| `k=0` counterbranch | eight exact positive-determinant even-index assemblies, best `(14,2,0)` | continue toward zero negative directions |
| self-branch determinant | exact product of four rational linear factors | classify all compatible self-branch sign cells |
| three equal-block reductions | exactly empty real involution varieties | leave the displayed equality constraints |
| paired involution variety | displayed nonsingular germs have odd negative count | decide the parity on every real component |
| mixed circulant-plus-`A_star` variety | exact grading splits (30)--(31) | solve scaled involution, anticommutation, and positivity jointly |
| OS and gravity route | not executed | carry any positive dressed reflection through OS, then form the gravity constraint quotient |

The scan finds no axiom-amendment route. Both live problems are finite exact
action/representation problems on the existing carrier.

### N7 — Steelman

**Hostile steelman against the wall.** The paired determinant might be
negative on every real component of the paired involution variety. Its
negative count would then be globally odd, the one-negative-direction
near-miss would reflect a real circulant obstruction, and no rearrangement
of the self branches could produce a positive circulant Gram.

That objection is exactly the named gate. The current wall does not deny it;
it denies only that the displayed eight-row odd chart has already proved it.
The exact `k=0` witness shows that neither total determinant nor total index
parity is fixed on the circulant class. It says nothing about the sign of the
paired determinant on components not reached by the displayed points. If
the hostile parity conjecture survives the global decision, the mixed
variety in (30)--(31), not an overstatement of the current chart, is the
honest next frontier.

### N8 — Cross-Cycle Echo

| earlier exact boundary | echo here |
|---|---|
| Block 108's global-support theorem, `docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:252-406` | global support remains fixed while the operator is decomposed by momentum rather than truncated back to a local window |
| Block 109's surviving joint question, `docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:485-535` | its 132-dimensional space is corrected to the exact circulant-plus-parity direct sum, and its mixed-support route becomes equations (29)--(31) |
| Block 110's even-sector escape, `docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md:326-457` | the live even route is factorized, its first parity obstruction is refuted, and only the componentwise paired decision remains before the mixed solve |

The repeated discipline is to preserve the parent carrier, distinguish an
exact finite chart from a componentwise theorem, and let a countercertificate
refute only the obstruction it actually reaches.

**No-Go Discipline verdict:** **PASS** only for narrow `W1`: the fixed
determinant/index-parity obstruction is refuted on the displayed circulant
class, and the three displayed equal-block reductions are empty. **FAIL**
for positivity, the global paired-sector parity decision, the complete
circulant or mixed variety, transporter completion, curved OS positivity,
gravity, axiom necessity, or TOE.

## 9. Axiom And TOE Disposition

No axiom amendment is justified. Momentum projection, blockwise involution
and Gram assembly, determinant factorization, exact inertia, and grading
splits are finite consequences of the displayed carrier and dressing class;
no new primitive is assumed.

This is bounded route progress, not an audit-grade assignment. It retires
no end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 10. Next Decision

The shortest high-value sequence is:

1. decide the paired-sector parity globally on every real component of the
   paired involution variety;
2. solve the mixed circulant-plus-`A_star` dressing variety through the exact
   split identities (30)--(31);
3. carry any positive dressed reflection through the OS package; and
4. only then form the gravity constraint quotient.

The actual ADM/history transporter remains unexecuted beyond the displayed
momentum factorization, determinant refutation, structured-family closures,
and grading-split mixture frontier.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted.
