# Uniform plaquette admission for LAYER-THM

Research generation, FINISH row 450 (`adm-pl`), Codex, 7 November 2026.
Checkout: `813a592cf663a1b4614db070fb1ed70a6861b0bc`.
Sussman–Alpoge account and outline: owner-supplied revision `31a47c543775`.
This is research text, not an audit; it grants no status. No numerical run,
automated proof search, or proof checker discharges an assertion below.

## 1. Result and its limits

**The requested unconditional admission theorem for the entire induction is
not established.** In particular, `K109` is sometimes the account's relaxed
three-clause class, not the full CMP 109 space. This distinction persists in
`K_P`, the ambient continuation of the stage spaces, and U34. Membership in
these classes is not, by its name, membership in `S^pl`.

The following additions close bounded parts of the admission problem.

1. The unchanged cube-gauge clause of the layered/post-step space controls
   crossing plaquettes, with coefficient `4 B C M alpha_{0,n}`. Lemma 2
   specifies exactly the necessary gap and read domain. This does not supply
   a missing raw stratum or a new determining set's real reference.
2. Thick aligned cube tests imply the level-graded plaquette clause on all
   complete plaquettes, including level zero when thickness holds there too.
   This extends the carrier-only conclusion of `b98p5-r3`; its existing
   counterexamples and carrier proof are not repeated.
3. A complete small-potential carrier frame has an explicit larger averaging
   ball. This local room is distinct from admission of an actual minimizer
   tube to such frames.
4. S1′ imposed on every retained earlier frame is preserved exactly by
   fixed-real-reference complex layers and hereditary restrictions. This is
   a proved replacement clause, not a claim that the printed classes contain
   it. New frames and changed references need entry proofs.

Section 6 gives one uniform conditional admission theorem. Section 7 locates
the still missing premises in the actual induction. The final table gives A
and L for U01–U34. A missing implication is not called a counterexample to
an actual induction run.

## 2. Sources, scope and notation

`library/prior/adm-pl.md` did not exist at the start. The first substantive
reads were GOAL and FINISH's “Build on published work”, “Working efficiently”
and “Rules”. Outline objects were searched in `sa-index/`, neighboring rows
read, then the cited bounded source ranges consulted. Principal dependencies:

| Index/source | Content used |
|---|---|
| chunk 05; SA 5663–5759 | Simple conditions, both tower rules, hereditary cores and fixed real references; continuation existence is part of core membership. |
| chunk 09; SA 9593–9654, 10111–10139 | Geometry, weights, complete reads and the inner-action convention. Separation is not thickness. |
| chunk 11; SA 11548–11568 | Local gauges and one-step bounds as primitive inputs. |
| chunk 14; SA 15882–15931 | Two-factor curvature and larger-disc tower arguments, indexed as sketched/conditional. |
| `layer-r3` §4 | Exact E, Loc, Avg certificates and U01–U34 census. |
| `b98p5-r3` §§3–4 and its gate | PL, carriers, thick covering, published classes, corrected chart attribution and minimizer tubes. |
| `print-inverse-r2` §3.3, Prop. 3.1 | PI constants and the interior-only cube-cover implication. |
| `lit-balaban`; quotations in the cited notes/account | Bałaban's CMP 98, 99b, 102, 109 and 119 inputs. Original papers were not fetched. |

Source hashes and the recovery record are in
[`../checks/adm-pl/checkpoint.md`](../checks/adm-pl/checkpoint.md).
The adjacent `sa` directory has no Git metadata from which to independently
recover its owner-supplied revision label; its byte identities are verified.

The parent registry row is `LAYER-THM`; this is its assigned admission
subproblem. B98-P5 and PRINT-INVERSE are reused, not reopened. The exceptional
stage-cube problem already has row `O-stage-cubes`. Uniform window,
switch-polydisc and tower suppliers have rows `CW`, `CH`, `L17`/`ER7`.
Those separately registered targets are not re-attacked here. No registry,
ledger, gate, account or outline file is edited.

Write `eta` for fine spacing, `ell_j=L^j eta`, and

\[
 \lambda_F(p)=\min_{x\text{ a corner of }p}\lambda_F(x)
\]

in a specified frame F. A complete read includes all four corners, all four
bonds and any difference stencil used in its proof. Bounds at locations do
not silently extend their stencils. The bond grade in (10) is the minimum
of its two endpoint grades, on the admitted carrier domain. Norms below are unnormalised Frobenius
norms. For either account norm convention in the cited notes,
`||X||_op <= ||X||_F <= sqrt(N)|X|`.

With target ceiling a, the PL clause is

\[
 \|U_r(\partial p)-1\|_F\le
 \sqrt N\alpha(\eta/\ell_{\lambda_F(p)})^2,
 \qquad\alpha\le8a.                                      \tag{PL}
\]

`S^pl` includes S1, S2 and S3 as well: PL alone is not full membership.
S1′ is the stronger account-norm bound with coefficient a. A and L below
mean all of Avg[U] and Loc[U] in `layer-r3` §4.1, on the entire prescribed
complex domain D_U and its reached intermediate images. Neither asserts
E[U] (equation identification/contraction) nor M[U] (the current-word identity).

## 3. Plaquette lemmas

### Lemma 1: a supplied gauge, with its precise reads

Suppose a real gauge contains the four bonds of p and both ordinary difference
pairs, and in that gauge

\[
 U_r=e^{i\eta A},\qquad
 \ell|A|,\ \ell^2|\nabla A|\le r,\qquad\sqrt N r\le1.
\]

Then

\[
 \|U_r(\partial p)-1\|_F
 \le(2\sqrt N r+2Nr^2)(\eta/\ell)^2
 \le4\sqrt N r(\eta/\ell)^2.                              \tag{1}
\]

This is `b98p5-r3`, Lemma 3.3, rebuilt there from the elementary calculation
underlying Bałaban's local gauges. To specify its reads: replace the two
shifted edge potentials by their values at the initial corner. Duhamel's
formula for Hermitian matrices bounds these errors by
`2 sqrt(N) r eta^2/ell^2`. The remaining group commutator, integrated in its
two parameters, is bounded by
`eta^2 ||[A_mu,A_nu]||_F <= 2N r^2 eta^2/ell^2`.
The remaining factors are unitary, and conjugating the plaquette back
preserves its norm. This proves (1).

The account-norm bound is `4r(eta/ell)^2` too: divide the displayed Frobenius
bound by sqrt(N) for normalized HS, or perform the same proof in operator
norm, obtaining `2r+2r^2<=4r`. Ordinary and covariant differences cannot be
interchanged without the separate comparison in the cited lemma.

If this gauge's level is m and the client's plaquette level is q, its PL
coefficient is at most

\[
 4r L^{2(q-m)_+}.                                         \tag{2}
\]

A direct curvature clause of coefficient b at level m contributes instead
`b L^{2(q-m)_+}`. This is the grade-conversion cost when a frozen shell is
read in another frame.

### Lemma 2: the post-step crossing plaquette

Use CA-I 9832–9890 and 9923–9963. Let p be a complete plaquette in Y, with
all corners in `Omega_n`, one outside `Omega_{n+1}` and one inside it, where
`1<=n<=k`. Put `s_n=C M ell_n`, `C in {1,2}`. Assume a nonwrapping local lift
with fine-lattice cubes of this side, `s_n>=2 eta`, and

\[
 \operatorname{dist}_\infty(\Omega_n^c,\Omega_{n+1})\ge s_n,
 \qquad
 \operatorname{dist}_\infty(\Omega_{n+1}^c,\Omega_{n+2})\ge s_n. \tag{3}
\]

An empty deeper region makes the second condition automatic. A graph-distance
lower bound must first be divided by d. The layered-cover geometry quoted in
`b119` §1.3, CA-I 53445–53548, has sup-norm gaps at least `2M ell_n`, hence
supplies (3) for these C. That transfer statement retains its geometric
antecedents; it is not a proof for every later, different stage frame.

Choose a fine-lattice cube Q of side s_n containing all four corners of p.
In its half-open lift every site is at distance strictly less than s_n from
each corner. The inside corner and the first gap imply `Q subset Omega_n`.
The outside corner and the second gap imply `Q cap Omega_{n+2}=empty`.
Also Q meets `Omega_{n+1}^c`. Thus Q is precisely a cube tested by condition
(ii). The supplied gauge is on `Q cap Y`, which contains all four bonds and
both difference pairs. No extension of Y is used.

Its radius is `r_n=B C M alpha_{0,n}`, so Lemma 1 gives

\[
 \|U_r(\partial p)-1\|_F
 \le4\sqrt N BCM\alpha_{0,n}(\eta/\ell_n)^2,
 \qquad\sqrt N BCM\alpha_{0,n}\le1.                      \tag{4}
\]

For a plaquette wholly in one stratum, the direct clause gives coefficient
`F_n alpha_{0,n}`, with `F_n<=1+beta`. Therefore every complete plaquette
just covered obeys PL with

\[
 C_{\rm post}=\max\{1+\beta,4BCM\},\qquad
 \alpha_{\rm post}=C_{\rm post}\sup_n\alpha_{0,n}.          \tag{5}
\]

S1′ on that domain follows from the explicit ceilings

\[
 \sup_n\alpha_{0,n}\le
 \min\{a/C_{\rm post},(\sqrt N BCM)^{-1}\},\qquad
 \sup_n\alpha_{1,n}\le a/(1+\beta).                       \tag{6}
\]

The second inequality supplies the existing twist ceiling, not (4). The
current retains its separate ceiling. The proof holds throughout the
fixed-real-reference complex fibre: its gauge and real plaquette do not move.

**Scope.** The definition starts at n=1. This proof does not provide a raw
n=0 clause, values outside Y, or a real-reference bound for a new minimizer
on another determining set. If a client introduces a raw stratum, its
identification and complete reads remain to be supplied. Full S1 membership
also requires the client's entire S1 cubes to be covered by supplied gauge
domains at the appropriate scales. This is not part of the four-edge proof.
The torus lift/room hypothesis is retained.

### Lemma 3: all-plaquette admission on thick towers

Use (TH) of `b98p5-r3` §3.5 at every level, including zero: `Omega_q` is a
union of cells of side s_q, aligned with the big-block grid of spacing
`g_q=M_b ell_q`, with s_q a multiple of g_q and `s_q>=12g_q`. Keep the cited
gap floors, for example `R>12d`, and the local-lift room. Suppose the size-12
S1 gauges have radius r, `sqrt(N)r<=1`.

Each complete plaquette p has a supplied size-12 gauge cube of index
`q=lambda_F(p)`. Its coordinate ranges have length eta. Every cell met by
their product contains a corner, because the cell grid lies on the fine
lattice. All these cells belong to `Omega_q`. Their product union is a box
inside `Omega_q` with each side at least `12g_q`. The aligned rounding of
`b98p5-r3`, Lemma 3.6, encloses p in a size-12 cube inside this box. A corner
outside `Omega_{q+1}` lies in the cube. Its distance to every cube site is
less than `12g_q`; the gap keeps the cube out of `Omega_{q+2}`. At the top
there is no deeper exclusion. It is therefore a test cube of index q.
Equation (1) gives PL with `alpha=4r`.

Thus `r<=a` supplies `S^pl` once S2 and S3 are supplied; `r<=a/4` supplies
S1′. Level-zero thickness cannot be dropped from this all-plaquette statement
because height-zero averaging is linear. The existing carrier-only result
needs less and is unchanged.

**Two tower rules.** CA-I 32834–32945 distinguishes their block letters.
Rule r2 has cells `M_1 ell_q`, with `M_1/mathfrak M>=R_1`. For S1 tests on
the mathfrak M grid, the allowed floor `M_1/mathfrak M>=12`, divisibility and
the common gap/room floors give this thickness, including q=0 when Z has the
stipulated cube union property. Rule r1 has cells `mathfrak M ell_q`. Raising
R_1 does not make these side-12 cells; maximal erosion is not a proof of
that thickness. Its general admission route is the full real plaquette
clause or a separately supplied carrier/local gauge. The rules cannot be
identified for this purpose.

## 4. Uniform radii and a clause that really is hereditary

Retain the explicit B98 local-port constants of `b98p5.md` (2), with the
repairs in `b98p5-r3-gate`:

\[
\begin{aligned}
 p_0&=8dL,& n_*&=4d(4L+1)^d,& r_0&=(2^{24}p_0)^{-1},\\
 B_*&=2^{24}n_*^2L^d r_0^{-2},&
 \rho&=r_0/(2^{20}B_*),& K_*&=128d^2L^2,\\
 a_B&=\rho/(16\sqrt N K_*).
\end{aligned}                                              \tag{7}
\]

Choose PI/GW constants first, as in `layer-r3` §4.2 and `print-inverse-r2`
§3.3. With PI's radii `a_0^PI,a_1^PI`, choose

\[
 a=\tfrac12\min\{a_B,a_0^{PI},a_1^{PI},(16\sqrt N)^{-1}\}. \tag{8}
\]

The independent current ceiling is the minimum of its source and PI/GW/F4
ceilings. It is separate from a; no equality with the current of U is imposed.
All constants precede the final coupling ceiling and depend on fixed rank
and earlier geometric constants, not depth or volume.

### Lemma 4: actual local averaging room

Suppose the real-reference PL and twist hypotheses of `b98p5-r3`, Cor. 3.5,
hold on a complete carrier E_c of height j>0, with the floor `R M_b>=L`.
Its proved carrier construction supplies a real unitary gauge fixed at U_r,
in which

\[
 W=e^{i\eta B}\text{ on }E_c,\qquad
 \ell_j\|B\|_{\infty,F}<\rho/8.                           \tag{9}
\]

For `ell_j ||v||_F<rho/16`, define `B_v` by the logarithm at the identity of
`exp(i eta v) exp(i eta B)`. With `h=eta/ell_j<=1`, the exponential series
and Frobenius ideal inequality give

\[
 \|e^{i\eta v}e^{i\eta B}-1\|_F
 \le h(3\rho/16)e^{3\rho/16}<h\rho/4.
\]

Since `rho<1/16`, the logarithm series has norm at most twice this bound.
Thus `ell_j ||B_v||_F<rho/2` on the whole larger v-ball, on the specified
branch. This is a genuine inclusion in the local port's potential ball.

Every bond of E_c has grade at least j-1 by the carrier lemma. Consequently
the simultaneous graded Frobenius ball

\[
 r_A=\rho/(64L),\qquad
 \sup_b\ell_{\lambda(b)}\|v(b)\|_F<4r_A                 \tag{10}
\]

lies in these larger carrier balls for every row. The actual ball of radius
r_A has spare Cauchy room. Height-zero rows are linear. The finer collar
must satisfy the complete-read condition in its own indexing; no boundary
sites are adjoined to a half-open coarse block.

Conditional on the B98 local analytic port, this gives the derivative and
transpose estimates throughout the admitted family. The density is the
physical fine-lattice density: in d=4 a counting-coordinate derivative is
`eta^4` times that density. A value estimate on M is not its substitute.
The repaired operator-norm constants are

\[
 c_4=\rho/\sqrt N,\quad C_2=4N/\rho,\quad
 C'=8N/\rho,\quad C_3=16N/\rho.                           \tag{11}
\]

For a prescribed complex gauge with both adjoint norms bounded by K, shrink
r_A to `r_A/K`; the right-logarithmic row derivative loses at most `K^2`.
The Landau-to-axial case K=2 gives the gate's factor 4. An ambient matrix
derivative also needs the output-matrix norm. No arbitrary complex gauge
saturation is asserted.

Equations (9)–(10) prove local averaging room around a background already
in its frame. They do not prove existence, holomorphy or admission of a
separately defined minimizer/response throughout D_U.

### Lemma 5: S1′ on retained frames

At date d let `F_{<=d}` be the actual earlier frames on which a continuation
can be read, including the raw frame, required readings of both tower rules
and specified collars. Add, on the member's one ambient real reference,

\[
 \mathrm{S1'}_{\rm past}:\quad
 |U_r(\partial p)-1|\le a(\eta/\ell_{\lambda_F(p)})^2
 \quad(F\in F_{\le d},\ p\text{ a complete read in }F).    \tag{12}
\]

This is preserved without radius loss by: a defined layer
`W -> exp(i eta H)W` retaining U_r; complete-read restriction; passage to a
subset of retained frames; a unitary gauge; and simultaneous change of
physical units for eta and ell. In the first three cases each needed bound
is literally an old inequality with the same left side. A unitary gauge
conjugates the plaquette. A unit change preserves eta/ell. This proves the
claim without using the existence or size of H to prove other class clauses.

If `lambda_new(p)<=lambda_old(p)`, the old PL bound also implies the new
bound with the same coefficient. If the level rises by g, the transported
coefficient is `L^{2g}a`: retaining a requires a new `L^{-2g}` gain. This is
an exact threshold comparison, not a counterexample to a stage with stronger
curvature hypotheses.

The fixed-reference operations occur at CA-I 10124–10146, 119603–119609,
CA-II 14055–14060 and CA-III 49479–49488. Thus (12) is preserved by these
parts of the induction. It is stronger than adding S1′ only at the current
date and assuming heredity. A new frame or a new real reference at a healing,
completion or minimizer step needs an entry proof. S2 and the current clause
still require their own propagation bounds.

For a finite family of frames on one fixed fine lattice, this repair has a
precise minimal form. Set
`h(p)=max{ell_{lambda_F(p)}: F reads p}` for each read plaquette. Then (12)
is equivalent to `|U_r(partial p)-1|<=a(eta/h(p))^2` for every p: the
strongest of the finite inequalities is the one with largest length.
Likewise the Frobenius bound
`||U_r(partial p)-1||_F<=8 sqrt(N) a (eta/h(p))^2` is necessary and sufficient
for (PL) on all these frames. It is the least additional plaquette condition
for this specified reference and read family; (12) keeps a smaller coefficient
as a reserve. No further intersections of domains are needed for this
plaquette equivalence.
This equivalence concerns one real reference and one cutoff; it does not
identify references or fine plaquettes between cutoffs.

### Lemma 6: an explicit final smallness threshold

The stage radius at CA-I 116601–116641 has the supplied majorant

\[
 \gamma_0^{(k)}\le A t_k^p e^{-t_k/2},\quad
 A=5(1+\beta_0)^2L^2(L+1)C,\quad p=r+q\ge0.               \tag{13}
\]

For a required positive ceiling epsilon it suffices to impose

\[
 t_\gamma\ge T(\epsilon):=
 \max\{4,2p+c_\beta,64p^2,4\log^+(2A/\epsilon)\}.         \tag{14}
\]

Indeed integration of `1/u<=1/sqrt(u)` on [1,t] gives `log t<=2sqrt(t)`.
For `t>=64p^2`, `p log t<=t/4`, so (13) is at most `A exp(-t/4)<=epsilon/2`.
This uses the source's t_gamma and its run-wide lower bound on t_k; it does
not redefine their relation to gamma.

For a direct Q5 read in its own frame, epsilon=a supplies S1′. With a proved
grade loss s, use epsilon=`a L^{-2s}`. For an ordinary gauge of radius at most
`C_g gamma_0^(k)`, use
`epsilon=min{a/(4 C_g L^{2s}),1/(sqrt(N) C_g)}`.
The same method implements (6) whenever its alpha radii have the supplied
envelope. Smallness does not create a missing clause or read domain.

## 5. Real-reference and Loc suppliers

**Full published classes.** The implications rebuilt in `b98p5-r3`, Prop. 3.2,
are retained with their hypotheses:

* Full CMP 109 (i)–(iii), CA-I 32498–32625, bounds every real-reference
  plaquette on X. Its coefficient alpha_0 gives PL in top units with
  `ell_lambda<=1`. S1 conversion also requires
  `c_12 L M B_109 alpha_0<=a`, and the twist/current ceilings.
* A glued window uses that same real factor. It does not use the complex
  window minimizer as a group-valued factor. Full clauses on the entire read
  domain, rather than its eroded interior, are required.
* CMP 102 Theorem 1, quoted in the account, gives the real minimizer in
  `U_k(B_3 epsilon_1)`. Its all-plaquette clause supplies PL with coefficient
  `B_3 epsilon_1` for either admissible tower. S1′ requires
  `B_3 epsilon_1<=a`; PL alone needs `<=8a`.

These are implications from Bałaban's statements as quoted and the cited
local ports. This note does not claim to rebuild unavailable original global
minimizer proofs. For one-power classes, a tower bound on the two-layer-eroded
set does not supply a complete-carrier reference bound in the removed collar
(CA-I 33035–33205).

**Minimizer tubes.** Keep the actual positive constant `C_1^(172)` of CMP 102
Proposition 9. Put `epsilon_2=B_5 epsilon_1`. Let `chi_N=1` for an operator-norm
data ball, and `chi_N=sqrt(N)` for a normalized-HS data ball. A sufficient
external log-datum radius is

\[
 r_{\rm ext}=\min\{1/(2\chi_N),
                       C_1^{(172)}\epsilon_1/(2\chi_N)\}. \tag{15}
\]

Keep the published CMP 98 thresholds as well as

\[
 \begin{gathered}
 B_3\epsilon_1\le8a,\qquad B_5\epsilon_1\le a,\qquad
 48d\sqrt N B_5\epsilon_1\le\log2,\\
 B_3\epsilon_1\le\alpha_0^{(98)},\qquad
 B_5\epsilon_1\le\alpha_1^{(98)}.
 \end{gathered}                                           \tag{16}
\]

The entire prescribed log datum, including shifts, must lie in (15). A
Cauchy argument on twice a tube of radius r_c requires `2r_c<r_ext`, or the
corresponding bound for its nonlinear datum map. If that map has the proved
bound `||B(z)||<=C_dat ||z||`, parameter radius `r_ext/(4 C_dat)` supplies an
open doubled ball. Naming C_dat is not a proof of the bound.

For `r_c=min{a_A/10,c_gamma}` and `epsilon_1=a_A/2`, the branch
`r_c=a_A/10` would need `C_1^(172)>4 chi_N/5` for the doubled-disc comparison.
The source supplies no such normalization. Lowering a_A on this branch
does not change the ratio. A smaller tube satisfying (15) is a valid
replacement domain, not verification on the original one. The bounded
Landau-to-axial gauge comparison and its complete-carrier applicability
remain premises as corrected in `b98p5-r3-gate` §§4.2–4.3.

**Paired real frames.** At CA-II 53798–53811, `C_beta(r_0)` supplies an
ordinary small potential and derivative on each `tilde Delta(y)`.
`b98p5-r3`, Lemma 3.4, gives PL with coefficient `4r_0`, using the gate's
corrected half-open convention. Thus `r_0<=2a` gives PL and `r_0<=a/4`
gives S1′. The finer cutoff must supply the entire family on the free
`Lambda'_0` collar (II 53614–53624). The real-frame fact alone does not
admit complex critical or rippled parents on their prescribed discs.

**Loc.** PI Proposition 3.1 gives interior S1-loc from S1 under thickness at
every level. Its constants are retained literally:

\[
 r_N=7M_t,\qquad \widehat r=(2L+2)M_t,\qquad
 2r_NL+1\le11M_b,
\]
\[
 R_1\ge24,\qquad
 R_1M_b\ge\max\{\rho'_F,4L(\widehat r+L)+1,3\log L/\delta_q\}.
                                                               \tag{17}
\]

M_t is the power of L and multiple of `L M_F` chosen by PI §3.3; M_b is a
power of L and multiple of M_t. Torus and switch room require

\[
 T_{\rm side}\ge\max\{2\widehat r+2,t_FM_F\}\ell_k,
 \qquad S_{\rm switch}/\ell_k\ge
             \max\{4\widehat r+8L,64\kappa/\mu\}.         \tag{18}
\]

For `N(x) not subset Omega_0`, a real gauge on all of N(x) is additional
data. The same is true when a supplied `tilde Delta` is smaller than N(x).
Require S2+ on every coefficient read, including protruding plaquettes and
exterior differences; the independent-current ceiling; literal PI rows and
corner blocks; the field/scalar spaces; and identification of the intended
action/Hessian. The account's inner-plaquette action and PI's whole action
with finite field support are not automatically identical at the boundary.
PL and a small carrier potential do not supply the full ordinary first
derivative on N(x). If `Omega_0=T_eta`, the exterior issue disappears, but
the other conditions remain.

## 6. One uniform admission theorem with its surviving premises

**Theorem UA (complete-read admission and its hereditary replacement).** Fix
(7)–(8), (17)–(18) and the common current/rate ceilings. Quantify over every
actual frame, intermediate base and read of U01–U34 throughout D_U, separately
for each cutoff and both tower rules. Assume:

1. Every reached pair has one specified real reference
   `W=exp(i eta a')U_r`, with S1, S2 and S3 at the common ceilings on the
   required domains. Every complete plaquette has a witness: a direct real
   plaquette bound; a supplied gauge as in Lemma 1; the crossing construction
   of Lemma 2; the thick cover of Lemma 3; or (12). After grade conversion
   (2), each witness coefficient is at most 8a. It is reused only with the
   same real reference and complete reads. Equations (6), (14), (16) provide
   explicit ceilings when their respective source hypotheses hold.
2. Every positive-height row and its transpose has its entire double-block
   carrier in that domain, with the carrier gap and local-lift room. A frame
   supplying (9) directly can replace the PL construction for Avg. Include
   finer collars and the prescribed logarithm branch. For minimizer-supplied
   bases impose (15)–(16) on their actual domains and the prescribed bounded
   gauge comparison.
3. For L, every PI patch is covered by Proposition 3.1 on its matched thick
   tower or by a supplied real gauge on the whole N(x), at S1-loc radius
   `L^2a`. All exterior coefficient reads have S2+. The operator, boundary,
   rate, current and room identifications of section 5 hold.

Then every such pair belongs to `S^pl`. Conditional on the B98-P5 local
analytic port, Avg[U] holds on D_U with the common larger balls (10).
Conditional on PI/GW's inputs for the identified operator, Loc[U] holds there.
The constants are uniform in depth, stage, volume, cutoff and tower rule.
No E[U] or M[U] is asserted.

For the modified classes carrying (12), the real plaquette premise in item
1 is preserved by all fixed-reference, retained-frame operations of Lemma 5.
Only a newly read frame/domain or a changed reference needs a new entry proof.
Already supplied real gauges on retained patches are preserved the same way;
no gauges on enlarged patches are manufactured. Other class clauses still
need their own propagation estimates.

*Proof.* Apply each plaquette's designated witness and (1)–(2), or its direct
bound. Lemmas 2–3 supply the two geometric routes. Item 1 gives PL and
separately S1–S3, hence `S^pl`. The carrier lemma of `b98p5-r3` puts carrier
plaquettes at grades at least j-1 and gives (9) at (7)–(8). Lemma 4 supplies
the larger-ball inclusion; the B98 port supplies physical-density derivative
and transpose bounds there. Item 3 and PI Prop. 3.1 supply exactly Loc's full
patch gauges and coefficient hypotheses, for the identified operator rather
than a different restricted inverse. The same constants work under every
stated quantifier. Lemma 5 proves invariance of (12). No finite enumeration
of instances is used as proof. ∎

This theorem is not a discharge of its premises for the account. In
particular, item 1 cannot be replaced by “belongs to K_P” at the sites below.

## 7. Actual induction: supplied parts and exact stopping points

### 7.1 Post-step space, I 10805, and the two chart entries

I 10805 uses the untwisted post-step space. Lemma 2 repairs the crossing
portion left open in `b98p5-r3`, on its specified domain and gaps, throughout
the fixed-reference complex fibre. Still needed are the embedding of the
consumer's entire S1 cubes and carriers, any raw/exterior reads, the response
entry below, and the induced minimizer/current on each determining set.

**I 10681 and I 10701 are on the post-step branch.** At I 10635 the proof
starts “We prove conclusion (1)”. The references to (K1),(K3),(K8) at 10681
and (K2),(K3),(K8) at 10701 inherit that branch's hypotheses. Alternative
`(2^int)` at 10608–10631 replaces the post-step assumption with the one-power
class and takes two further closure statements as given. Its full CMP 109
clause cannot be imported into the proof of (1). The old PL109 assignments
are misassigned. Their correct route is the post-step admission above, with
its remaining premises. This decides attribution, not the chart theorem.

### 7.2 The class at I 10178

CA-I 10168–10213 states a free-current response at a background “in the
regularity class of that determining set”, and subsequently states a
real-minimizer case using CMP 102 Proposition 9. The phrase at 10178 does
not define the missing complete-read class. Three identifications were tested:

1. CMP 102 real minimizers supply a real reference by Theorem 1 and a tube
   by Proposition 9 only in that subcase, with (15)–(16). They do not identify
   a general pair with independent current.
2. Full CMP 109 gives the desired implication if its actual representative
   belongs on the entire determining set. The quoted phrase is not this
   hypothesis; an eroded tower bound is not a complete-carrier clause.
3. The post-step space supplies Lemma 2 for its own real factor. That does
   not identify this factor with the real reference of every induced
   determining-set minimizer. Induced-real-factor bounds at I 10000ff are
   separate conditions in the account itself.

The established replacement is the explicit UA entry data on that determining
set, or (12) with UA's remaining premises. No unconditional identification
of the unnamed class was proved. This is the exact missing entry, not a
negative conclusion about Proposition 9.

### 7.3 Relaxed K109, K_P and the ambient stage continuation

CA-I 110268–110284 defines K109 by (3.35), (3.37) and an independent-current
bound. I 110313–110317 defines K_P from it. The earlier class at
I 94448–94586 is explicitly relaxed too. These definitions do not include
full CMP 109 (i)–(iv) merely through their names.

The stronger stage space at I 119415–119650 does have Q5 and cube Q8 on its
declared direct domain. Equation (13) controls their radii. Where all carrier
plaquettes and required gauges lie in those reads with matching units,
Lemmas 1–4 and (14) give admission. Crossing a layer boundary is handled by
Lemma 2 or a complete Q5 read; crossing the boundary of a clause's domain
is a different coverage question.

The ambient convention is explicit: `N^(n)(Y)` restricts one pair globally
in K_P, with direct clauses on Y+ (I 119615–119626). It is not a separately
specified local pair whose small-curvature extension may be assumed.
At an unlocalised switch the layer reads the continuation beyond Y+
(I 119642–119650), where the definition supplies only relaxed membership.
Thus the inference

`Q5 on Y+ -> S^pl on every carrier of the whole unlocalised frame`

has not been supplied. It needs carrier containment, an admitted ambient
reference, or a thick/global gauge cover. Locality of the final term does
not localize an intermediate unlocalised inverse.

The three routes were: retain full CMP 109 (not this definition); use Q5/Q8
(valid on complete covered reads); and use relaxed cubes plus separation
(valid in the matched thick case, not arbitrary r1 geometry). Existing
cube-only counterexamples forbid the last general inference. They are not
new counterexamples to the actual induction.

### 7.4 Heredity, raw reads and the registered exceptional cube step

The cube-heredity proof at I 134548–134746 restricts a later gauge from a
containing cube at level `lambda+g`, with `g in {0,1}` and
`w'<=L_0^{2g}w`. Its scale/radius contraction is conditional on that cover.
Its supplier at I 134496–134532 explicitly leaves the case

`C=2, j+1=k, m=k_0+1, N_0>=2`

unproved. At 134506–134517 it does not derive that the `C xi_k` neighbourhood
meets at most one component of `Omega_{k_0+1}^c cap X`. The alternative family
can cost `L_0^4` for g=1 rather than `L_0^2`. The account gives one-box or
separation greater than `4.25 xi_k` as sufficient conditions, but does not
derive them. This is registry `O-stage-cubes`; that separately registered
target is not re-attacked here.

At I 133020ff the raw stratum and G_1 are distinct. I 136750–136770 explicitly
returns G_1 and says raw points enter none of its clauses. Linearity of a
height-zero averaging row does not remove raw plaquettes from S1′, nor raw
and exterior bonds from PI coefficient stencils. Clause (12) includes them
when global PL is required.

For fixed-reference layers, added S1′ propagates by Lemma 5 without cube
nesting. Gauge heredity and Loc still need nesting or another full-patch
supplier. Completion/healing can introduce a real reference or domain that
needs entry; agreement on a core is not a global reference bound.

### 7.5 U34 and exterior patches

CA-III 49200–49288 imposes relaxed (3.35),(3.37) on every earlier frame and
pointwise Q1,Q3,Q5,Q6,Q7 on Y+, with cutoff current. It does not impose the
coupling-small pointwise clause throughout the ambient domain. The heredity
argument at 49454–49502 keeps the real part and its existing gauges fixed,
but takes an interface stencil's treatment from the background-response
theorem. Invoking that theorem at the stencil is exactly where A/L is needed;
it is not an independent proof of admission.

Clause (12) matches U34's existing past-frame quantifier and is preserved
by the same unchanged-reference move. To repair L as well requires real
gauges on every whole N(x), and S2+ on every coefficient read. Cutting J to
zero gives neither. An axial carrier potential does not give the full
gradient bound on N(x). Enlarging the domain requires an admitted ambient
pair and identification of the intended Hessian, not just inversion of a
restricted matrix.

### 7.6 Complex admission without circular use of LAYER-THM

The invariance of Q5 and cube gauges is useful on the whole complex switch
polydisc; CA-II 14055–14060 states it for the all-block dilation. It does
not prove existence, holomorphy, twist or current bounds for its response.
The preceding corollary assumes that holomorphy and layer bound
(II 13888–13974). Likewise I 94846–94935 derives bidisc membership by using
the small-solution theorem. That output cannot be its own admission input
while LAYER-THM is being constructed.

Three larger-domain routes have different outcomes: local averaging room
is proved by Lemma 4; published minimizer continuation gives (15)–(16)
conditionally; finite-dimensional openness gives pointwise room, not a
positive infimum over histories, depths and volumes. SA 15921–15931's
Schwarz argument first needs its larger-disc a priori bound. The existing
ER7 supplier and CW, CH, L17 rows retain their premises and ownership;
neither the outline paragraph nor the layer estimate under construction
discharges them.

No actual induction counterexample is asserted. The exact stopped deductions
are the class identifications, complete reads, marked cube step and tube
comparisons above. Conditional source theorems remain valid implications.
The new invariant clause, explicit ceilings and local admission theorem do
not establish all actual entry premises.

## 8. Recovery checkpoint and verification limits

This final note and the linked source manifest are the current checkpoint.
The new mathematical work is the crossing construction, all-plaquette thick
cover, local larger averaging ball, and invariant past-frame PL clause.
The two chart attributions are corrected here. No original argument or
status is edited.

Next decisions: identify I 10178's class; supply complete ambient and raw
admission in the relaxed stage classes; obtain the registered exceptional
cube supplier if using cube heredity; match PI's exterior/Hessian reads;
and compare the actual minimizer/product tubes with (15). None is a
numerical verification problem. This round has no independent mathematical
review or Lean formalization. Its new arguments use finite set containment,
matrix integral/series inequalities and scalar threshold inequalities; the
analytic literature inputs and domain hypotheses are explicit.

## 9. Final U01–U34 admission table

**P** means proved for the stated operation. **C(...)** means conditional on
the named premises over the whole actual domain. No row is labelled failing
as a mathematical assertion about an actual run: no such counterexample was
established. Failed proof steps are specified in the C entries and section 7.
An inherited call retains all originating conditions. “P, no new call”
certifies only the indicated algebra, not the originating layer.

* **R**: identify the actual real reference and admit its complete reads by
  UA item 1, with the explicit radius/grade inequalities. Relaxed K109 alone
  is insufficient.
* **A0**: UA item 2 and the B98 local port, with all carriers, branches and
  collars. Lemma 4 supplies local larger balls once its frame holds.
* **L0**: UA item 3, with matched PI/GW spaces, (17)–(18), exterior S1-loc/S2+,
  common current and rate ceilings.
* **S**: complete stage/earlier-frame Q5,Q8 reads and grade conversion;
  beyond Y+ an admitted ambient reference or (12). Cube heredity, if used,
  retains the exact exceptional supplier in section 7.4.
* **T**: independent existence and admission of all reached intermediates
  on the prescribed complex domain; for minimizer references, (15)–(16) and
  the bounded gauge comparison. E[U] is not used as its own proof.
* **P2**: paired real-reference families on both cutoffs, including the free
  finer collar, and T for their complex parents/interpolations.

| Use and actual domain | A: full averaging admission | L: full local admission |
|---|---|---|
| **U01**, I 72373–72538: exempted-switch layer on the general determining frame | **C(R,A0,T)** on the full switch domain. Exempting one cube does not admit other rows. | **C(L0,T)** on the literal frame, including all anchors and boundary reads. |
| **U02**, I 73103–73140: four site links with successive membership hypotheses | **C(U01,R,A0,T)** at every link image. A class name does not propagate PL. | **C(U01,L0,T)** at each link's domain. |
| **U03**, I 73546–73633: four-switch chain on `B''_k,B''_k,B_1,B_k` | **C(R,A0,T)** for all four frames. A common scaffold does not identify their complete reads. | **C(L0,T)** for all four operators. |
| **U04**, I 89955–90008: presentation input (i4), furnished layer | **C(R,A0,T)** at the originating call. | **C(L0,T)** there; a presentation hypothesis supplies no missing gauge. |
| **U05**, I 94180–94286: real bases `U_0,U^0` on `B_k(C),B''_k(C)`, shifted bases and bidisc | **C(R,A0,T)** for both references and shifts. `p(U_0)<=1` is not a PL ceiling. | **C(L0,T)**. Thick interiors use Prop. 3.1 after grid matching; exterior patches need additional gauges. |
| **U06**, I 94303–94422: calls with `(0,d^0)` and `(0,f)` | **C(U05,A0,T)** for both calls and the boundary-crossing block-field logarithms. | **C(U05,L0,T)** on both determining sets. |
| **U07**, I 94448–94586: linearized map on the explicit relaxed class | **C(R,A0)**. Linearization does not add PL to that class. | **C(L0)** on the actual linearized operator problem. |
| **U08**, I 94755–94843: scope extension under (c1)–(c3) | **C(R,A0,T)**. Particular cube geometry does not by itself admit all complex carriers. | **C(L0,T)** after matching c1–c3 to PI grids, room, coefficient reads and action. |
| **U09**, I 94846–95085: all of `D(rho_abs)` | **C(U05–U08,T)**. A7 membership invokes the layer theorem and is not its independent admission proof. | **C(U05–U08,T)** for the same reason. |
| **U10**, I 95682–95700: reality at the real zero-datum base | **C(U06)** for the originating call; conjugation/uniqueness adds no averaging premise. | **C(U06)** for that call. |
| **U11**, I 95750–95790: shifted real critical base and own current | **C(R,A0,T)** at the shifted base; the physical subcase uses the published real-minimizer route. | **C(L0,T)** at the base with the physical boundary problem identified. |
| **U12**, I 95872–95908: covariance continued on the fixed-reference fibre | **C(U05–U11,T)**. Unitary covariance preserves PL; the identity principle does not admit the tube. | **C(U05–U11,T)**; only already supplied full patches are carried by covariance. |
| **U13**, I 99780–99796, 99878–99892: common floors/ceilings | **C(U05,U08)** with common R,A0,T on every base. | **C(U05,U08)** with common L0; listing floors is not their geometric verification. |
| **U14**, I 111489–111732: partner of a furnished cut layer | **C(originating call)**; no new average in the partner formula. Its current-word gap is separate. | **C(originating call)**; the stencil formula presupposes its operator. |
| **U15**, I 112180–112230: seminorm/linearity combination of furnished entries | **P, no new call.** Original A dependencies stay with the entries. | **P, no new call.** Original L dependencies stay with the entries. |
| **U16**, I 112580–112650: two weighted Lipschitz calls | **C(R,A0,T)** for each originating base and full data domain. | **C(L0,T)** for each call; weight admission is not base admission. |
| **U17**, I 114790–114880: healing `(W_3,J_3)` on all of `B''_k` | **C(R,A0,T)** on the whole continuation. Equality with real `U_2` on the core does not cover other carriers. | **C(L0,T)** on the full continuation. |
| **U18**, I 115382–115410: inherited T/L size bounds | **C(U16,U17)** for the originating layers and domains. | **C(U16,U17)**; no new patch supplier. |
| **U19**, I 116555–116669: stage B, K_P, `abs(sigma)<=exp(kappa_1)`, datum radius `1.1 C_1 delta'_j` | **C(S,A0,T)**. (13)–(14) settle covered-read smallness; I 119642–119650 leaves ambient carriers beyond Y+ unresolved. | **C(S,L0,T)**. Q8 helps only on a whole covered PI patch; exterior/Hessian identifications remain. |
| **U20**, I 125775–125792: inherited constant `66 B_H K_cv` | **C(U19)**; combining constants adds no domain proof. | **C(U19)**. |
| **U21**, I 131621–131695: frozen frame, enlarged heredity source, raw/starred points | **C(S,A0,T)** on the heredity image. Own-current criticality does not supply omitted regularity. | **C(S,L0,T)** at both raw and starred reads; the source notes missing (3.35)–(3.38) for the direct minimizer invocation. |
| **U22**, I 131725–131746: localized `B_Z` | **C(U21,R,A0,T)** on the new determining set; the extra localized-layer input remains. | **C(U21,L0,T)**; old membership does not identify the new patches. |
| **U23**, I 136750–136770: off-domain continuation and component locality | **C(S,A0,T)**. Added (12) propagates, but the printed G_1 conclusion omits raw clauses. | **C(S,L0,T)** on complete interface stencils. |
| **U24**, I 137562–137603: interrupted terms on `B_Z`, outside earlier geometry | **C(U22,R,A0,T)**. The source takes the exceptional localized continuation/bound as input. | **C(U22,L0,T)** on that geometry. |
| **U25**, I 137978–138001: gluing an arrested continuation | **C(S,A0,T)**. The proof invokes incomplete e4; (12) propagates only its fixed-reference plaquette part. | **C(S,L0,T)** including gluing stencils and the registered cube supplier if used. |
| **U26**, I 138640–138667, 142530–142543: completion and raw/core reads | **C(S,R,A0,T)** at new references and full carriers; a core consumer bound is insufficient globally. | **C(S,L0,T)** on cubes meeting completion and all exterior patches. |
| **U27**, II 13888–14105: all-block dilation, full product domain, `chi_t J^sharp[1]` | **C(U19,S,A0,T)**. Fixed U_r preserves supplied PL for complex amplitudes; the assumed layer bound cannot admit its own input. | **C(U19,L0,T)**, with `delta_0/8` compared to the common rate and (17)–(18). |
| **U28**, II 15390–15404: localization-site product-domain containment | **C(U27,T)** for every contained map. | **C(U27,T)**. |
| **U29**, II 20790–20808: furnished bracket carrier/current formula | **C(originating U27 call)**; linearity in chi adds no admission. | **C(originating U27 call)**. |
| **U30**, II 23160–23177, 23990–24005: brackets and carrier compositions on the core | **C(S,A0,T)** at every intermediate; core bounds must cover each complete read. | **C(S,L0,T)** at those same intermediates. |
| **U31**, II 51814–52070: nonlinear datum `Q_B(W;eta(t+tbar zeta)H^w)` | **C(R,A0,T)** along the full interpolated family; (10) is a sufficient ball if its size bound is supplied. | **C(L0,T)** for the following response on `B_j`. |
| **U32**, II 52107–52186: paired critical parents, complex beta and full b,tbar discs | **C(P2,A0,T)**. Own-averages reality plus the identity principle does not prove (15) or admit the finer collar. | **C(P2,L0,T)** for both cutoff operators and full boundary reads. |
| **U33**, II 52390–52469: rippled parents on full interpolation discs | **C(P2,A0,T)** throughout the chain. The outstanding linear-closeness proposition supplies no admission. | **C(P2,L0,T)**; mismatch/profile bounds do not give missing gauges. |
| **U34**, III 49210–49288, 49454–49502: relaxed earlier-frame class | **C(S,R,A0,T)** outside the direct Y+ clauses. Added (12) propagates but is not printed. | **C(L0,T)** at every earlier frame and boundary patch; the cited response theorem at the crossing stencil is the missing supplier, not its proof. |
