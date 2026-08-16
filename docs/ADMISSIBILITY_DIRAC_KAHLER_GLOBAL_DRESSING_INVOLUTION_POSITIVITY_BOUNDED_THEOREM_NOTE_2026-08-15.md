---
claim_id: admissibility_dirac_kahler_global_dressing_involution_positivity_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the Block 107/108 seam carrier, the globally supported x-covariant dressing class (512 real parameters over all eight torus slices) jointly satisfying reflection-reality and full-span two-history Hermiticity has exact dimension 132 (rank 380: reality is a fixed-point-free signed involution of the parameter basis contributing rank 256, Hermiticity adds exact rank 124) at both displayed shear fixtures, and the undressed identity is excluded; the class contains the displayed exact involution A_star--anti-diagonal reflection-pairing of slices with alternating signs times the x-parity sign field--which makes the dressed reflection a genuine antilinear involution with an exactly Hermitian full-span Gram of exact inertia (8,8,0) (displayed negative minors at both fixtures), occupies every slice at magnitude one with a vanishing central-window block (invisible to every central-window search), and within the anti-diagonal class the joint linear system is exactly one-dimensional with involution variety exactly {+/-A_star} (Groebner basis lambda^2-1), both branches exactly indefinite; separately the positive fiber K_A=I is feasible with exact real dimension 72 and a displayed representative that is exactly non-involutive (rank(A^2-I)=32); hence involution and positivity each hold globally but are exactly disjoint on the displayed classes, and the joint variety on the full 132-dimensional space, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_involution_seam_dressing_locality_bounded_theorem_note_2026-08-15
runner: scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_involution_seam_dressing_locality_bounded_theorem_note_2026-08-15
target_blocker_text: "Construct the globally supported transfer/modular seam dressing; verify involution quadric, full-span Hermiticity, positivity"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Solve the joint involution-positivity variety on the full 132-dimensional global space (structured decompositions and the modular selection); carry any positive dressed reflection to the OS package and the gravity constraint quotient."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-108 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite operator identities, exact rational linear algebra, exact inertia, and an exact one-variable polynomial classification on the declared d=2 carrier; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Global Dressing Space, The Exact Reflection Involution, And The Positivity Split

**Date:** 2026-08-15

**Campaign block:** 109

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py`](../scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py)

## 1. Result Up Front

[Block 108](ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:629-645`:

> Construct the globally supported transfer/modular seam dressing; verify
> involution quadric, full-span Hermiticity, positivity.

Three exact theorems sharpen that gate.

First, the globally supported `x`-covariant dressing ansatz has 512 real
parameters. Reflection-reality is a fixed-point-free signed involution of
that parameter basis and contributes exact rank 256. Full-span two-history
Hermiticity contributes a further exact rank 124. Hence at each fixture,

\[
 \dim_{\mathbb R}\mathscr L_{5/13}
 =\dim_{\mathbb R}\mathscr L_{3/5}
 =512-(256+124)=132.                            \tag{1}
\]

The combined rank is 380 at both fixtures. The identity does not lie in
either space: its surviving Hermiticity residual is exactly the Block 108
non-decay defect.

Second, each 132-dimensional space contains the same displayed exact
involution `A_star`. It pairs the eight time slices anti-diagonally, with
alternating reflection-pair signs, and multiplies by the Block 106
shear-flip `x`-parity sign field. Its eight nonzero blocks are

\[
\begin{array}{c|rrrrrrrr}
 (t,t')&(-4,3)&(-3,2)&(-2,1)&(-1,0)&(0,-1)&(1,-2)&(2,-3)&(3,-4)\\
\hline
 A_{\star;t,t'}&D_x&-D_x&D_x&-D_x&-D_x&D_x&-D_x&D_x,
\end{array}                                      \tag{2}
\]

with every other time block zero and
`D_x=diag(1,-1,1,-1)` in the ordered `x`-character basis. Thus every time
slice has magnitude-one support. Exact multiplication gives

\[
 P\overline {A_\star}P=A_\star,
 \qquad A_\star^2=I_{32}.                       \tag{3}
\]

The dressed reflection is therefore a genuine antilinear involution. Its
full-span Gram is exactly Hermitian at both fixtures, but its exact inertia
is `(8,8,0)`. Section 5 displays an exact negative principal-minor witness
at each fixture.

Third, involution and positivity split on the displayed classes. The exact
64-real anti-diagonal class has joint linear rank 63 and hence is
one-dimensional, `A(lambda)=lambda A_star`. Its involution ideal has reduced
Groebner basis `{lambda^2-1}`, so its real variety is exactly
`{+A_star,-A_star}`. Both branches have inertia `(8,8,0)`. Separately, the
positive identity-Gram fiber

\[
 \mathscr P_c=\{A:P\overline A P=A,
                  \quad\mathcal K_+(A;c)=I_{16}\} \tag{4}
\]

is nonempty and has exact real dimension 72 at both fixtures. The displayed
canonical representative has
`rank(A^2-I_32)=32`, so it is exactly non-involutive.

Thus involution and positivity each occur globally, but they are exactly
disjoint on the classes just displayed. This does not decide their joint
existence on the full 132-dimensional space. That remaining problem has
132 real dressing variables, with 37 coordinates in the `A`-Hermitian
subfamily; it is the live next mechanism, not a transporter impossibility.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main b8d9f4c40125e45415d6dd240a7ef806e773a278`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`, recomputed when this draft was
written.

The exact stacked parent is [Block 108](ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `8afe8dff5ccf531208238af0aaaec1f547d73874`, content-bound through note
blob `21128ab10b32d4f99190ce7107ef9fb790a05781`. Its direct parent is
[Block 107](ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `d41a05e153d4cb77eee125b82fc0b0bd767bf32e`, note blob
`cefc3be28430a9069ef572eb992f2605e58fccd5`. The local shear-flip source is
[Block 106](ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md)
commit `22d6d90ec2279e5868c9c825149b2a20beea3797`, note blob
`a08c8d5381e5bfac52f23d28fa6ffd05adf81697`. No audit verdict is imported.

The executed contract is:

1. the Block 107/108 `d=2` one-fine-mode carrier on
   `Z8_t x Z4_x`, ordered time first with representatives `-4,...,3`;
2. antiperiodic time closure and the antilinear link-centered reflection
   `theta(t)=-1-t`;
3. the step-shear history `(-c,-c,-c,0,c,c,c,0)`, with `m=9/20`, `v=1`,
   and the two exact fixtures `c=5/13` and `c=3/5`;
4. the full positive span `Lambda_+={0,1,2,3} x Z4`, the central positive
   span `Lambda_cen={0,1} x Z4`, and the reflection-symmetric four-slice
   window `W4={-2,-1,0,1} x Z4`;
5. the globally supported `x`-covariant class: an `8 x 8` array of
   `4 x 4` spatial-circulant complex blocks, hence `8*8*4` complex or 512
   real coordinates, ordered lexicographically by target time, source time,
   spatial offset, and real then imaginary part; and
6. exact antilinear identities, exact rational row reduction and rank,
   exact principal-minor/inertia certification, and exact polynomial
   reduction only. Decimal values are never proof inputs.

No OS reconstruction theorem is used. No modular or transfer selection is
constructed. The joint variety on all 132 variables, curved positivity,
ADM/history transport, and gravity terminals are outside the executed
contract.

## 3. Global Feasibility

Let `X_x` be the 512-real-dimensional globally supported `x`-covariant
coordinate space in Section 2. In its ordered real parameter basis,
reflection-reality acts as

\[
 \rho(e_\alpha)=\epsilon_\alpha e_{\sigma(\alpha)},
 \qquad \epsilon_\alpha\epsilon_{\sigma(\alpha)}=1,
 \qquad \sigma(\alpha)\ne\alpha.                \tag{5}
\]

Thus `rho` is a signed involution whose underlying permutation is
fixed-point-free. Its 512 basis elements form 256 two-cycles. Each cycle
contributes one independent fixed coordinate and one independent reality
row, so

\[
 \dim\operatorname{Fix}(\rho)=256,
 \qquad \operatorname{rank}(I-\rho)=256.        \tag{6}
\]

This count includes the diagonal-reality rows. It is a basis permutation
mechanism, not a floating-point rank observation.

Let `S_+` embed the ordered sixteen-dimensional positive span, put
`G_c=Q_c^(-1)`, and define the dressed full-span Gram by the Block 108
target-arm convention,

\[
 \mathcal K_+(A;c)
 =\overline{S_+^\dagger A G_c P S_+}.           \tag{7}
\]

On `Fix(rho)`, impose the exact real-linear equations

\[
 \mathcal H_c(A)
 :=\mathcal K_+(A;c)-\mathcal K_+(A;c)^\dagger=0. \tag{8}
\]

Fraction-free elimination gives

\[
 \begin{array}{c|ccc}
 c&\operatorname{rank}(I-\rho)&
   \operatorname{rank}(\mathcal H_c\mid\operatorname{Fix}\rho)&
   &\operatorname{rank}_{\rm stacked}\\
 \hline
 5/13&256&124&380\\
 3/5 &256&124&380.
 \end{array}                                    \tag{9}
\]

Therefore

\[
 \mathscr L_c
 :=\{A\in\mathscr X_x:P\overline A P=A,
                  \ \mathcal H_c(A)=0\}
\]

is a real vector space of exact dimension 132 at each fixture.

The undressed identity is reflection-real, but it is not in `L_c`.
Indeed,

\[
 \mathcal H_{5/13}(I)\ne0,
 \qquad \mathcal H_{3/5}(I)\ne0.               \tag{10}
\]

These are exactly the nonzero undressed far-block constants and independent
rank inconsistency displayed in
[Block 108 Sections 6.1--6.3](ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md),
`docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:283-406`.
Global support makes the Hermiticity equations feasible; it does not make
the identity a solution.

## 4. The Exact Involution

Index time slices by `tau_i=i-4`, `i=0,...,7`, and set `r(i)=7-i`. Let

\[
 D_x=\operatorname{diag}(1,-1,1,-1),
 \qquad D_x^2=I_4,                              \tag{11}
\]

in the ordered four-mode `x`-character basis. This is the spatial
`x`-parity sign field in the Block 106 shear-flip channel, whose signed time
lift and action-derived seam link are anchored at
[Block 106 Section 8](ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md),
`docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md:410-509`.
The associated real-space operator is `x`-covariant.

Define the symmetric alternating sign vector

\[
 (s_0,s_1,s_2,s_3,s_4,s_5,s_6,s_7)
 =(1,-1,1,-1,-1,1,-1,1),                       \tag{12}
\]

and define `A_star` by

\[
 (A_\star)_{ij}=\delta_{j,r(i)}s_iD_x.          \tag{13}
\]

For completeness, its full list of eight nonzero time blocks is

\[
\begin{aligned}
 (A_\star)_{-4,3}&= D_x,&
 (A_\star)_{-3,2}&=-D_x,&
 (A_\star)_{-2,1}&= D_x,&
 (A_\star)_{-1,0}&=-D_x,\\
 (A_\star)_{0,-1}&=-D_x,&
 (A_\star)_{1,-2}&= D_x,&
 (A_\star)_{2,-3}&=-D_x,&
 (A_\star)_{3,-4}&= D_x.
                                                        \tag{14}
\end{aligned}
\]

There are two separate exact mechanisms. First,

\[
 s_i=s_{r(i)}                                   \tag{15}
\]

makes reflection-reality hold after `P` exchanges each anti-diagonal pair.
Second,

\[
 s_i s_{r(i)}=1,
 \qquad D_x^2=I_4                              \tag{16}
\]

gives `A_star^2=I_32` block by block. Combining (15)--(16) with the Block
108 reduction
`(Theta compose A)^2=A^2`, anchored at
[Block 108 Section 3](ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md),
`docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:128-179`,
gives

\[
 (\Theta\mathbin\circ A_\star)^2=I_{32}.       \tag{17}
\]

This is a genuine antilinear reflection involution, not merely a Hermitian
dressing.

The support mechanism is equally sharp. Every row slice has one nonzero
reflection partner and every nonzero entry of that partner has magnitude
one. Hence `A_star` occupies all eight torus slices. On the other hand,

\[
 S_{\rm cen}^\dagger A_\star S_{\rm cen}=0,     \tag{18}
\]

because `r` sends each central positive slice into its negative-time mate.
Thus its central positive-to-positive window block vanishes. Block 107's
central target-arm search, anchored at
[Block 107 Section 7](ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md),
`docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md:462-490`,
could not identify it through that block. Block 108's affine search instead
required identity continuation outside `W4`, while `A_star` is supported on
every slice. The two central-window searches therefore excluded this
candidate by their declared premises; they did not test and reject it. In
this exact sense, `A_star` is window-invisible.

This realizes Block 108's global-support forcing exactly. It does not yet
realize positivity.

## 5. The Positivity Split

Put

\[
 \mathcal K_\star(c)=\mathcal K_+(A_\star;c).   \tag{19}
\]

Exact conjugate-transpose comparison gives

\[
 \mathcal K_\star(c)=\mathcal K_\star(c)^\dagger
 \quad(c=5/13,3/5).                             \tag{20}
\]

Exact fraction-free Hermitian elimination, including zero-pivot principal
reordering rather than a numerical eigensolve, gives

\[
 \operatorname{inertia}\mathcal K_\star(5/13)
 =\operatorname{inertia}\mathcal K_\star(3/5)
 =(8,8,0).                                      \tag{21}
\]

Here are exact negative principal-minor witnesses at both fixtures:

\[
 \begin{aligned}
 \Delta_{\star,1}(5/13)
  &=-{33333963283450197824471164187210075293672388640
       \over
       61391349876435377016600254323619839508354485363}<0,\\
 \bigl(\mathcal K_\star(3/5)\bigr)_{8,8}
  &=-{30292616102306685544040740640984160
       \over
       68872508036021339265532585819028911}<0.
                                                        \tag{22}
 \end{aligned}
\]

Their signs are certified by positive integer numerators and denominators.
They independently exclude positive semidefiniteness, while (21) gives the
stronger complete inertia.

Positivity is nevertheless globally feasible. Let

\[
 \mathscr P_c
 =\{A\in\mathscr X_x:P\overline A P=A,
                  \ \mathcal K_+(A;c)=I_{16}\}. \tag{23}
\]

After the rank-256 reality reduction, the exact affine system has
`rank[M]=rank[M|b]=184` at both fixtures. Equivalently, the combined stack
has rank `256+184=440` in 512 real coordinates. Therefore

\[
 \dim_{\mathbb R}\mathscr P_{5/13}
 =\dim_{\mathbb R}\mathscr P_{3/5}=512-440=72. \tag{24}
\]

To display a reproducible exact representative, order the 512 coordinates
as in Section 3, row-reduce the reality-plus-`K=I` system over `Q`, and set
all 72 free coordinates to zero. If `R_c a=b_c` denotes that exact reduced
system, write

\[
 A_+^{(c)}
 :=\operatorname{unvec}_x\!\left(
      a_{\rm free}=0,\ a_{\rm piv}=R_{c,{\rm piv}}^{-1}b_c
    \right).                                    \tag{25}
\]

This definition displays the canonical zero-free-coordinate rational
member without decimal fitting. Direct exact substitution gives

\[
 \mathcal K_+(A_+^{(c)};c)=I_{16}>0,
 \qquad
 \operatorname{rank}\bigl((A_+^{(c)})^2-I_{32}\bigr)=32
 \quad(c=5/13,3/5).                             \tag{26}
\]

Thus the positive representative is exactly non-involutive. Conversely,
the displayed exact involutions are indefinite. Involution and positivity
are therefore disjoint on these displayed classes, but (26) does not prove
that the entire 72-dimensional positive fiber misses the involution
quadric.

## 6. The Anti-Diagonal Classification

The anti-diagonal class is not merely sampled. It can be closed exactly.
Let

\[
 \mathscr A_{\rm ad}
 =\{A:(A)_{ij}=\delta_{j,r(i)}C_i,
       \ C_i\text{ is a complex }4\mathbin\times4
          \text{ spatial-circulant block}\}.   \tag{27}
\]

Each `C_i` has four complex, hence eight real, coordinates, so (27) is a
64-real anti-diagonal class. Stacking reflection-reality with full-span
Hermiticity gives, at each fixture,

\[
 \operatorname{rank}M_{\rm ad}(c)=63,
 \qquad
 \dim\bigl(\mathscr A_{\rm ad}\cap\mathscr L_c\bigr)=1,
 \qquad C_i=\lambda s_iD_x.                     \tag{28}
\]

Hence every reflection-real, full-span-Hermitian member of this complete
anti-diagonal class is

\[
 A(\lambda)=\lambda A_\star.                    \tag{29}
\]

Substitution into the involution equations gives

\[
 A(\lambda)^2-I_{32}=(\lambda^2-1)I_{32}.       \tag{30}
\]

With the monomial order `lambda`, the reduced Groebner basis is exactly

\[
 \{\lambda^2-1\},                               \tag{31}
\]

and the real involution variety is exactly

\[
 V_{\rm ad}(\mathbb R)=\{-A_\star,+A_\star\}.  \tag{32}
\]

There are no missed nonlinear branches in this class. Since the Gram is
linear in `A`,

\[
 \mathcal K_+(-A_\star;c)=-\mathcal K_+(A_\star;c). \tag{33}
\]

Negation interchanges the positive and negative inertia counts. Because
both counts are eight, both branches have exact inertia `(8,8,0)` at both
fixtures. Each branch therefore has an exact negative principal minor and
is indefinite. Equations (27)--(33) close the anti-diagonal class
completely; they do not classify the full 132-dimensional solution space.

## 7. The Surviving Joint Question

Choose an exact real basis `B_1(c),...,B_132(c)` for `L_c` and write

\[
 A_c(u)=\sum_{j=1}^{132}u_jB_j(c),
 \qquad u\in\mathbb R^{132}.                    \tag{34}
\]

The unresolved semialgebraic set is

\[
 \mathscr V_c^+
 =\{u\in\mathbb R^{132}:A_c(u)^2=I_{32},
               \ \mathcal K_+(A_c(u);c)>0\}.   \tag{35}
\]

This is an honest 132-real-variable quadratic involution problem followed
by positivity of an exactly Hermitian `16 x 16` Gram. The linear subfamily
in which the dressing itself is Hermitian,

\[
 \mathscr L_c^{\rm h}
 =\{A\in\mathscr L_c:A=A^\dagger\},             \tag{36}
\]

has exactly 37 real coordinates. Thus the 666-pair scan in Section 8 is
the complete set of coordinate pairs in the 37-dimensional
`A`-Hermitian subfamily, whereas the 8,646-pair scan is the complete set of
coordinate pairs in the 132-dimensional full linear space. Neither pair
scan is the full quadratic variety (35).

Three structured routes remain live:

1. mixed diagonal-plus-anti-diagonal time supports, allowing the positive
   fiber to bend toward the closed anti-diagonal involution branches;
2. wider spatial classes beyond the declared `x`-covariant ansatz, if the
   full `x`-covariant variety is exhausted without a positive branch; and
3. the modular/transfer selection derived from `Q_seam`, which can select a
   nonlinear point of (35) without being sparse in the displayed basis.

The first and third routes attack the 132-dimensional problem without
changing the carrier. The second explicitly widens the representation
premise. None requires a new primitive.

The current split is therefore not a transporter impossibility. A positive
involution may exist away from the anti-diagonal line, away from all tested
coordinate two-planes, and away from the canonical positive-fiber
representative. Solving (35), then applying the modular/transfer selection,
is the exact surviving question.

## 8. No-Go Discipline Gate

There is exactly one narrow finite-carrier wall.

- `W1`: on the displayed classes, involution and positivity are disjoint.
  The anti-diagonal class is closed exactly: its only involutions are
  `+/-A_star`, and both are indefinite at both fixtures. The searched
  structured families of the full 132-dimensional space add no other
  involution, while the displayed identity-Gram representative is positive
  and has `rank(A^2-I)=32`.

The scope is exactly the declared carrier, two fixtures, complete
anti-diagonal class, coordinate-pair families, identity extension, and
displayed positive-fiber representative. The full joint variety (35) is
not closed. Mixed supports and the modular/transfer selection are the named
live repairs. No statement about a completed transporter, transporter
impossibility, or curved OS positivity follows.

### N1 — Alternative Route Enumeration

Routes are normalized by `(object, mechanism, terminal)`. The complete
class closure is distinguished from finite structured scans, and the
premise-widening live route is not counted as an attempted repair.

1. **ATTEMPTED — anti-diagonal class / complete exact classification /
   involution plus positivity.** The 64-real starting class has joint
   linear rank 63 and dimension one, its reduced involution basis is
   `{lambda^2-1}`, and its variety is exactly `{+A_star,-A_star}`. Both
   points have inertia `(8,8,0)` at both fixtures. This anti-diagonal
   complete classification is the strongest row.
2. **ATTEMPTED — `A`-Hermitian subfamily / all coordinate-pair planes /
   involution plus positivity.** The exact 37-coordinate basis has
   `binomial(37,2)=666` unordered pairs. Exact pairwise polynomial solves
   return only the already classified `+/-A_star` solutions and hence no
   positive involution. This is the Hermitian-subfamily pair scan.
3. **ATTEMPTED — full global linear space / all coordinate-pair planes /
   involution plus positivity.** The exact 132-coordinate basis has
   `binomial(132,2)=8646` unordered pairs. Exact pairwise solves again
   return only `+/-A_star`. This exhausts coordinate two-planes, not their
   nonlinear mixtures. This is the full-space pair scan.
4. **ATTEMPTED — `gamma*I` extensions / diagonal-plus-anti-diagonal line /
   full Hermiticity and involution.** In
   `A=lambda A_star+gamma I`, full-span Hermiticity forces `gamma=0` at
   both fixtures. The surviving involution equation is `lambda^2-1=0`, so
   no positive branch is added.
5. **ATTEMPTED — positive identity-Gram fiber / canonical exact
   representative / involution.** The representative (25) has
   `K_A=I_16>0` and exact `rank(A^2-I_32)=32` at both fixtures. It proves
   positivity feasibility, not joint feasibility. This is the
   positive-fiber representative involution test.
6. **UNTESTED — LIVE — full joint variety and modular selection /
   nonlinear action/representation construction / positive involution.**
   This `UNTESTED-LIVE` premise-widening route goes beyond every finite pair
   scan and is not counted as an attempted route against `W1`.

### N2 — Wall-Independence Audit

There is one current wall, so no pairwise current-wall table is needed. It
is independent of Block 108's `W1`, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:442-457`.

The Block 108 residual is locality: identity continuation outside `W4`
leaves parameter-free nonzero far-block Hermiticity rows. Current `W1` is a
positivity split after that locality premise has been removed and global
Hermiticity has become feasible. `A_star` is a globally supported exact
involution with a Hermitian but indefinite Gram; `A_+` has a positive Gram
but is non-involutive. Repairing the Block 108 residual therefore does not
repair the current residual. Conversely, a positive involution in (35)
would not change Block 108's theorem about identity continuation. The two
walls have different residuals: locality vs positivity.

### N3 — Hidden-Wall And Phrase Scan

The required scope-certificate phrase scan is classified explicitly.

| lowercase hit | classification |
|---|---|
| `globally supported x-covariant dressing class` | the declared 512-real-parameter ansatz, not every global operator |
| `fixed-point-free signed involution` | exact reality-basis mechanism giving rank 256 |
| `hermiticity adds exact rank 124` | exact incremental rank at both fixtures |
| `dimension 132` | global reflection-real, full-span-Hermitian linear space |
| `undressed identity is excluded` | inherited exact non-decay residual, not nonexistence of global solutions |
| `exact involution a_star` | displayed member of the global space, not a positive member |
| `every slice at magnitude one` | global-support certificate on this eight-slice torus |
| `vanishing central-window block` | equation (18), explaining central-search invisibility |
| `inertia (8,8,0)` | exact indefiniteness of both anti-diagonal branches |
| `anti-diagonal dimension one` | complete class closure, not closure of the full space |
| `groebner basis lambda^2-1` | exact involution ideal inside the anti-diagonal line |
| `positive fiber dimension 72` | exact feasibility of `K_A=I`, not joint feasibility |
| `rank(a^2-i)=32` | exact non-involution of the displayed positive representative |
| `666 pairs` | exhaustive coordinate pairs only in the 37-coordinate `A`-Hermitian subfamily |
| `8646 pairs` | exhaustive coordinate pairs only in the 132-coordinate global space |
| `gamma = 0 forced` | identity extension collapses to the anti-diagonal line |
| `joint variety untested-live` | the surviving 132-variable nonlinear problem |
| `not a transporter impossibility` | scope firewall for `w1` |
| `no axiom amendment is justified` | constitutional firewall |
| `zero obligation retirement` | TOE accounting firewall |
| `no toe percentage moves` | TOE accounting firewall |
| `retained-positive end-to-end theory count remains zero` | audit-status accounting |
| `actual adm/history transporter remains unexecuted` | partial-closure statement only |
| `n1 n2 n3 n4 n5 n6 n7 n8` | every discipline gate is present |
| `w1` | the wall set has exactly one member |
| `per_element per_site per_mode per_block lattice_wide` | the five N5 resolution keys |

The bounded note preserves the `N1`--`N8`, `W1`, N5, ADM, gravity, audit,
and TOE walls. No phrase upgrades a structured-family split into a theorem
about the full joint variety.

### N4 — Residual Matching

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 108 Next Decision](ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:629-645` | construct the global transfer/modular dressing; verify involution, full-span Hermiticity, and positivity; then form the gravity quotient | equations (5)--(10) construct the full global Hermitian space, (11)--(18) give an exact involution, and (19)--(33) isolate the positivity split; their joint full-space solution remains open |
| [Block 107 certificate section](ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md:462-490` | the eight-dimensional local space contains an exact central positive certificate but lacks involution, action selection, and full-span extension | equation (18) explains why `A_star` is invisible to the central positive-to-positive block, while (9) supplies full-span Hermiticity and (21) shows that this involution is not positive |
| [Block 105 Section 12](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md:630-643` | the action-derived ADM seam and both-eigenline Gram are required, and an uncancelled contact residual marks an action defect | the exact global linear space and involution are now present, but the modular/action selection of a positive involution remains the matching repair |

Every cited residual reaches its stated interface. No citation is used as an
audit verdict.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “Within the complete anti-diagonal
class, and within every searched coordinate-pair or identity-extension
family of the displayed 132-dimensional global space, the only exact
involutions are `+/-A_star`, whose full-span Hermitian Grams have inertia
`(8,8,0)` at both fixtures; the displayed positive identity-Gram
representative is exactly non-involutive.”

Forbidden upgrades include “the transporter exists,” “the transporter
cannot exist,” “curved OS is closed,” “the full 132-dimensional joint
variety is empty,” “ADM/history transport is finished,” “the gravity
quotient has been executed,” “an axiom amendment is required,” and “a TOE
obligation is retired.”

The five resolution lines from the runner specification are reproduced
verbatim:

```text
per_element: exact feasibility, involution, classification, fiber, and invisibility identities are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: both shear fixtures certify the same dimensions, variety, and inertia
per_block: the exact involution occupies every slice at magnitude one while its central window block vanishes
lattice_wide: checked and not executed — the joint involution-positivity variety on the full 132-dimensional space, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The full joint variety and its
modular/transfer selection are action/representation constructions from the
existing seam kernel.

| route | present status | remaining terminal |
|---|---|---|
| global reflection-reality plus full-span Hermiticity | exact dimension 132 at both fixtures by (5)--(10) | intersect with the involution quadric and positive cone |
| exact global involution | `A_star` obeys (17) and occupies every slice | replace its exact inertia `(8,8,0)` by positivity |
| complete anti-diagonal class | exactly `{+/-A_star}` on the involution variety, both indefinite | leave the anti-diagonal class |
| positive identity-Gram fiber | exact dimension 72, with the displayed member positive and non-involutive | solve the involution equations within or beyond that fiber |
| full joint variety | live 132-variable action/representation problem | structured decomposition, then modular selection |
| modular/transfer selection | live and axiom-free | carry any selected positive involution to the OS package |

The scan finds no axiom-amendment route. Solving the quadratic representation
problem changes neither the carrier axioms nor the registered primitives.

### N7 — Steelman

**Hostile steelman against the wall.** The split may dissolve on the full
132-dimensional variety. A nonlinear combination of three or more basis
directions could be involutive and positive even though every coordinate
pair returns only `+/-A_star`; likewise, another point of the
72-dimensional identity-Gram fiber could lie on the involution quadric even
though its displayed canonical representative does not.

That objection is correct and fixes the scope of `W1`. The anti-diagonal
classification is complete, but the coordinate-pair scans are not a
Groebner decomposition of (35), and a rank-32 result for one positive point
does not classify its entire fiber. This is exactly why the full joint
variety, structured decompositions, and modular selection are the named
next mechanisms. The shipped wall is class-scoped; it is not widened to a
full-space no-go.

### N8 — Cross-Cycle Echo

| earlier exact boundary | echo here |
|---|---|
| Block 107's two-history and dressing-space walls, `docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md:462-490` | its central positive certificate is preserved, while the globally supported involution is shown to have a vanishing central positive-to-positive block |
| Block 108's seam-locality wall, `docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:442-457` | its forced global-support escape is realized by the 132-dimensional space and every-slice `A_star`, after which positivity becomes the distinct residual |
| Block 108's discipline echo, `docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md:600-615` | the anti-diagonal class is closed completely before widening to mixed supports or the modular selection |

The repeated discipline is to close a stated class completely, preserve its
exact witness, and only then widen the representation premise. Blocks 107
and 108 did not turn their local walls into transporter no-go statements;
the present note does not turn its positivity split into one either.

**No-Go Discipline verdict:** **PASS** only for narrow `W1` on the
displayed classes and fixtures. **FAIL** for the full 132-dimensional joint
variety, transporter existence or impossibility, curved OS positivity,
gravity, axiom necessity, or TOE.

## 9. Axiom And TOE Disposition

No axiom amendment is justified. The global rank calculation, exact
involution, inertia split, anti-diagonal classification, and positive fiber
are finite consequences of the displayed carrier and pairing; no new
primitive is assumed.

This is bounded route progress, not an audit-grade assignment. It retires no
end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 10. Next Decision

The shortest high-value sequence is:

1. solve the joint involution-positivity variety on the full
   132-dimensional global space, beginning with mixed
   diagonal-plus-anti-diagonal decompositions and then wider spatial
   classes if required;
2. impose the modular/transfer selection derived from `Q_seam` on any
   surviving positive involution; and
3. only then carry the selected dressed reflection to the OS package and
   the gravity constraint quotient.

The actual ADM/history transporter remains unexecuted beyond the displayed global feasibility, exact anti-diagonal involution, and positivity-split certificates.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted.
