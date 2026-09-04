# The gravity constraint quotient — grounding and opening construction

Status: **complete bounded report**. The source paths below are relative to
`/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/gravity-toe-lane-work-427b0b/`.
No repository file is modified.

## 1. GROUND — what the corpus defines

### 1.1 Exhaustive phrase result in b105

The b105 note has exactly two case-insensitive occurrences of either requested
phrase (`constraint quotient` or `gravity constraint`): lines 524 and 637.
The full surrounding subsections are b105 lines 508–528 (`N3 — Hidden-Wall
Scan`) and 628–643 (`12. Next Decision`). The operative primary text is:

> “`ADM`, `gravity` | non-load-bearing future target | only reflection parity
> (32); no history measure, constraint quotient, or recoil”
> — b105, line 524.

> “test the unnormalized two-history Gram on both spatial eigenlines; / only
> then couple the physical gravity constraint quotient and ask whether / a
> retained obligation can move.”
> — b105, lines 636–638.

These passages do **not** give a carrier, equivalence relation, constraint
generators, constraint surface/kernel, group action, orbit relation, reduced
span, or reduced Gram for the physical gravity constraint quotient. They define
only its dependency position and current status:

1. it is a **non-load-bearing future target**, not an executed ingredient
   (b105:524);
2. the current result supplies “no history measure, constraint quotient, or
   recoil” (b105:524);
3. it comes **after** derivation of the common patch/frame differential or its
   connection residual, derivation of the reflection-odd ADM temporal link and
   seam overlap from `Q_E(H)`, and the unnormalized two-history Gram test on
   both spatial eigenlines (b105:630–638);
4. only after coupling it may one ask whether a retained obligation moves
   (b105:637–638).

### 1.2 The one quotient operation that b105 *does* specify

B105 separately gives an exact frame-chart quotient requirement:

> “Thus the global section is a gauge convention only if all four descriptions
> are quotiented by their exact signed transitions and `N, d, H, Q_E` are
> transported together.”
> — b105, lines 310–312.

Its immediately stated consequences are that shifted charts may have
coarse-interblock support, a fixed blocking origin is not physical structure,
and a gauge-fixed representation with exact transition data need not privilege
a site (b105:312–315). The earlier construction says to choose one origin as a
gauge section and transport `N,d,H,Q_E` together (b105:81–84). Section 11 again
calls the origin a frame gauge and requires bounded interblock transition data,
or the stronger overlap-carrier descent (b105:612–617).

This is a **defined frame-description quotient**: quotient the four origin
descriptions by their exact signed transition identifications. It is not,
anywhere in b105, equated with the later “physical gravity constraint
quotient.”

### 1.3 Nearby objects that are not a definition of the gravity quotient

- The “exact constraint matrix” at b105:222–227 is the rank-three linear
  system forcing a shift-commuting diagonal exterior grade to be scalar. It is
  a grading obstruction, not a gravitational constraint algebra.
- The overlap Hodge is a positive, bounded-local, translation-covariant
  coframe Gram (b105:81–92), but it lacks the common nilpotent differential,
  ADM/history transporter, and reflection Gram (b105:101–105, 387–406).
- At constant metric, the off-diagonal component `c=g_xt`, “equivalently the
  minimal ADM shift,” is reflection odd (b105:435–444). This fixes a parity and
  says the negative-half shift must reverse. It does not declare the shift to
  be quotiented out.

### 1.4 Exact defined/open boundary

**DEFINED by b105:** a frame gauge among four origin descriptions; its exact
signed transition law; joint transport of `N,d,H,Q_E`; reflection oddness of
the minimal ADM shift; an ordering in which a physical gravity constraint
quotient is coupled only after the action-derived seam and two-history Gram.

**NOT DEFINED by b105:** that the physical quotient is by frame gauge, lapse,
shift, diagonal signs, or any combination; whether constraints act on fields,
histories, the history span, `Q`, or its Gram; whether reduction means a kernel,
image, group-orbit quotient, gauge fixing, or null-space quotient; and whether
the Gram should be invariant or merely covariant. Calling any of those the
corpus definition would add an unlanded design axiom.

### 1.5 B107 fixes the dependency ladder, not the missing definition

The supplied b107 file has numbered sections 1–10 (there are no numbered
sections 11–12 in this file). Its §10 is nevertheless exactly the requested
next-decision ladder:

> “derive the transfer/polar decomposition of the seam kernel and its induced
> reflection transporter …; / retest the two-history Gram under that
> transporter on both eigenlines; and / only then form and test the physical
> gravity constraint quotient.”
> — b107, lines 698–702.

> “The actual ADM/history transporter remains partially executed: the seam
> data and temporal link are derived; its positivity transporter remains open.
> The gravity constraint quotient remains unexecuted.”
> — b107, lines 704–706.

B107 defines the pre-quotient objects. On
`Lambda_+={0,1} x Z4_x`, in the stated eight-site order (b107:162–168), it
sets `G=Q_E(H)^(-1)` and

\[
  \mathcal K(H)_{ab}=\overline{G(b,\theta a)}
\]

(b107:344–351). It also derives the seam action

\[
 Q_{\rm step}=mH_{\rm step}+H_{\rm step}d_K-d_K^T H_{\rm step}
\]

with every temporal/seam block generated by that same action (b107:322–340).
The `H_image` diagnostic is exactly reflection-symmetric, but in b107 its
unmodified matter differential carries the remaining defect (b107:404–436).
Thus b107 supplies the carrier, history span, action/propagator/Gram convention,
and sequencing requirement; it still supplies no gravitational constraint
generators or equivalence relation.

### 1.6 Relevant b128 executable conventions

The b128 public helpers confirm the exact carrier conventions used below:
`cover_index` and `cover_embedding` use the four offsets
`((0,0),(0,1),(1,0),(1,1))` (b128:222–241); `curved_hodge_cover` forms the
all-anchor overlap with exact weight `1/4` (b128:244–263); and
`antiperiodic_quotient` is an explicit matrix fold (b128:280–285). Its
`chart_differential_cover` is expressly documented as “a displayed chartwise
nilpotent choice, not a common differential” (b128:266–277), so it cannot be
silently promoted into a gravity-constraint generator.

## 2. DESIGN — a minimal opening quotient

Everything in this section is **DESIGN**, except where a b105/b107 line is
explicitly cited. It is not attributed to the corpus and has status
`frontier_discovery / exact finite support`, not retained closure.

### 2.1 Candidate constraint actions and their proper domains

| candidate | corpus support | proposed action and test | present verdict |
|---|---|---|---|
| frame/origin gauge | b105:81–84 and 310–315 define joint transport by exact signed transitions | act on the full package `(H,D,Q,P,S_+)`; demand covariance of the history Gram under a simultaneous change of chart | required description quotient, but not identified with the physical gravity constraint quotient |
| ADM shift/shear | b105:435–444 proves the shear is reflection odd | first vary the Hodge/action and derive the induced history action; only then test Gram covariance | a modulus/parity direction, not yet a constraint generator |
| diagonal sign/lapse trial | no b105 definition; this is only a suggested ansatz | on `V_+=span Lambda_+`, enumerate `Z=diag(±1)` satisfying `Z^T K Z=K` | exact computation below leaves only the global center `±I`; no local diagonal sign algebra is supported |
| spatial shift-vector trial | motivated by translation covariance and the supplied `Z4_x` carrier, but not declared gravitational by b105 | let `U_x` cyclically translate `x` on `V_+`; test `U_x^T K U_x=K`, then quotient by `im(I-U_x)` using group averaging | passes exactly and is the minimal executable first quotient property |

The constraint acts on **histories/vectors** in `V_+`. The Gram `K` is the
form that must be preserved or covariantly transported; it is not itself the
thing being quotiented. A group-orbit quotient and a linear quotient also must
not be conflated:

- `U^T K U=K` makes the group action isometric and gives an orbit-space
  distance, but does not make the raw number `K(v,w)` independent of choosing
  either orbit representative.
- A form descends naively to `V_+/N` only when `N` is in its radical. The landed
  positive Gram has zero radical, so no nonzero linear gauge direction can be
  discarded while retaining the raw Gram.
- For a finite isometry group, the safe linear construction is instead the
  canonical averaged representative. For the spatial trial,
  `Pi_x=(I+U_x+U_x^2+U_x^3)/4` annihilates `im(I-U_x)` and identifies the
  coinvariant quotient with the invariant subspace.

### 2.2 Exact first certificate

Use exact rationals `m=9/20`, `c=5/13` and the b107 block `H(c,1)`. Construct
`H_image` with positive-half blocks, forced-flat seam-anchor blocks, and exact
`P_4 H(c,1) P_4^T` image blocks. From the antiperiodic staggered kernel take
its grade-raising part; with time representatives `-4,...,3`, the positive
half is `{0,1,2,3}`, and `A` contains its positive-half terms plus both seam
terms (equivalently, terms with at least one endpoint in that half). The
user-supplied b185 glue is

\[
 D=A-P_0AP_0,\qquad
 Q_{\rm glued}=mH_{\rm image}+H_{\rm image}D-D^T H_{\rm image}.
\]

For the `32 x 8` history injection `S_+`, exact inversion forms

\[
 K=S_+^T P_0 (Q_{\rm glued}^{-1})^T S_+,
\]

which is the real-rational form of b107:346–351. Let `U_x` be the induced
one-site cyclic spatial translation on the eight histories. The finite
certificate is:

\[
\begin{gathered}
 P_0H_{\rm image}P_0=H_{\rm image},\quad
 P_0DP_0=-D,\quad P_0Q_{\rm glued}P_0=Q_{\rm glued}^T,\\
 K=K^T,\quad \operatorname{rank}K=8,\quad
 U_x^TKU_x=K,\\
 \Pi_x^2=\Pi_x,\quad \Pi_x(I-U_x)=0,\quad
 \Pi_x^TK=K\Pi_x,\quad \operatorname{rank}\Pi_x=2,\quad
 \operatorname{rank}(I-U_x)=6.
\end{gathered}
\]

This uses only one exact `32 x 32` inverse; every quotient-side operation is at
most `8 x 8`.

### 2.3 Result

All displayed identities pass in SymPy 1.14.0 with exact `Rational`
arithmetic. The `8 x 8` Gram has all 64 entries nonzero. Exhausting all 256
diagonal sign matrices finds exactly two fixed-Gram elements, `+I` and `-I`.
Thus the landed Gram does not support independent sitewise diagonal
sign/lapse gauge transformations in this trial representation.

For the spatial-shift trial, define

\[
 \overline V_x=V_+/\operatorname{im}(I-U_x).
\]

The projector certificate proves that `[v] -> Pi_x v` is well-defined and
identifies `overline V_x` with a two-dimensional invariant span. In the
invariant basis
`b_0=sum_x e_(0,x)`, `b_1=sum_x e_(1,x)`, the exact quotient Gram is

\[
\overline K_x=
\begin{pmatrix}
\dfrac{163789300662954272136506611200}
      {62922325712833513369342157167}&
\dfrac{84443069449353823492351232000}
      {62922325712833513369342157167}\\[6pt]
\dfrac{84443069449353823492351232000}
      {62922325712833513369342157167}&
\dfrac{277507121822165058146000320000}
      {188766977138500540108026471501}
\end{pmatrix}.
\]

Its first leading minor is positive and

\[
 \det\overline K_x=
 \frac{127462980246289585754112000000}
      {62922325712833513369342157167}>0.
\]

Therefore `overline K_x` is exactly positive definite. This certifies the
**first quotient property**: the trial `Z4_x` shift equivalence admits a
representative-independent positive Gram through canonical group averaging.

### 2.4 What this result does not certify; exact next spec

It does not identify `U_x` with the corpus's physical momentum constraint, and
it does not derive a Hamiltonian/lapse constraint, an ADM shift constraint, a
frame-gauge constraint, their brackets, first-class closure, or the physical
gravity constraint quotient. It also does not move a retained obligation.

The next non-speculative computation requires action-derived full-carrier
matrices `C_alpha` for whichever lapse/shift/frame variations the theory
declares gauge. At each exact rational geometry point, perform only:

1. closure: solve exact coefficients in
   `[C_alpha,C_beta]=sum_gamma f_{alpha beta}^gamma C_gamma`;
2. history stability: test `C_alpha V_+ subset V_+`, or transport `V_+` along
   with the frame if covariance is intended;
3. Gram action: test infinitesimally
   `c_alpha^T K+K c_alpha=0`, or the explicitly derived covariance law;
4. reduction: construct the common invariant/constraint kernel or a canonical
   averaging projector `Pi`, verify `Pi^2=Pi`, `Pi C_alpha=0`, and
   `Pi^T K=K Pi`;
5. positivity: compute the exact reduced Gram `B^T K B` and its rational
   Sylvester minors.

Until the `C_alpha` are derived from the action, this is a precise executable
specification, not permission to label a chosen symmetry “the gravity
constraint.”

## 3. Exact five-line stdout

```text
CARRIER dim=32 history_dim=8 arithmetic=SymPy_Rational
GLUE PHP=H:True PDP=-D:True PQP=Q.T:True K=K.T:True rankK=8
TRIAL_ALGEBRA Ux^4=I:True Ux.T*K*Ux=K:True diagonal_sign_stabilizer_order=2
PROJECTOR Pi^2=Pi:True Pi*(I-Ux)=0:True Pi.T*K=K*Pi:True rankPi=2 rank(I-Ux)=6
QUOTIENT dim=2 Kbar00_positive:True detKbar=127462980246289585754112000000/62922325712833513369342157167 positive:True
```

## 4. Ten-line summary

1. B105 uses the requested phrases exactly twice, at lines 524 and 637.
2. It names the gravity constraint quotient as future and unexecuted, not as a defined algebra.
3. Its only defined quotient is the separate frame-chart identification by exact signed transitions.
4. B105 does not say the physical quotient is by frame gauge, lapse, shift, or diagonal signs.
5. B107 puts the quotient after the transfer/polar transporter and the retested two-history Gram.
6. DESIGN places trial constraints on the positive-history span and treats the Gram as preserved structure.
7. Exact SymPy proves the one-site spatial `Z4` shift acts isometrically on the landed Gram.
8. Group averaging yields a rank-two canonical representative space for the shift coinvariants.
9. The resulting exact `2 x 2` quotient Gram is positive definite, while local diagonal signs fail.
10. This is a first quotient-property certificate only; action-derived gravity constraints and closure remain open.
