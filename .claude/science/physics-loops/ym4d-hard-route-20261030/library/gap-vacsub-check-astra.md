## Repo search

Terms: `vacuum.subtraction`, `VAC-SUB`, `KF-LEV`, `SUPER-D`, `Ky Fan`,
`thermal.trace.{0,30}transport`, `transport.{0,30}thermal.trace`,
`DEF_K`, `VIR-log`, `Lemma CONC`, `Lemma SLICE`, `Proposition FR`.
All searches used `git grep -n -i -E` on Markdown/TeX in the full repository,
including outside this lane, followed by bounded `head`. Broad searches
hit their caps and are locators only. The boundary-qualified VAC-SUB/Ky Fan
search completed with no hits on all five refs.

Refs read: origin/main `4d88da5504d356762deb6b1a1c2695336af9fb81`;
pr/10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`;
pr/10133 `89faef229ff6e6bde42baad15ed8270c2f4087d8`;
pr/10134 `1e70c7211a2cdbc39001e619f1dd89db45e25851`;
pr/10141 `c73ad7b177d94f89ff37b77386936e3d52b48b05`.

| Relevant hit | Exact statement and proximity |
|---|---|
| origin/main:research/mass-gap/library/gap-mid-max.md:118–172 | Theorem TR transports `G(t_0 exp(integral K);s)` under its thermal derivative inequality. TR1 requires `integral K <= log(b/(2 ceil(log_2 b)))` and gives `S(b/2;b^3)<1/1650`. DEF_K bounds each individual ordered level; VIR-log only tests the characteristic curve. Exact existing consumer, reused. |
| origin/main:research/mass-gap/library/gap-mid-check.md:58; gap-crux-fp.md:228,295; gap-flux-exercise.md:301; gap-form-exercise.md:344; gap-skeleton-final.md:504 | These hits recall the same transport condition and its open deficit bound. They point to row 708, not to an existing check of row 934. |
| origin/main:docs/PHOTON_VACUUM_SUBTRACTION_AND_COSINE_REFERENCE_BOUNDED_THEOREM_NOTE_2026-10-09.md:19–49,76–89,520–526 | The supplied reference has only positive-frequency transverse oscillators. Gradient and harmonic zero modes are explicitly omitted; compact holonomy/winding and full compact spectral identification remain separate. Its order-g^4 coefficient theorem is a different statement, but its domain distinction applies to the Gaussian test here. No coefficient proof is redone. |
| Local gap-target-max.md:247–287 and gap-target-check-astra.md | HF's ingredients, KF, ABS and the prefix/individual-level distinction already exist. Reused with check 914's spectral-order and global-vacuum corrections. |
| Local gap-oddgap-max.md:255–291 | Frozen flat/twisted counts are already `736,96` for Q_8 and `5856,96` for 2T. Reused and hand-checked as finite-group test data, not claimed as new counting. |

The November 8 digest was read whole; it treats earlier ultraviolet targets.
The separate DEF_K/VIR-log search on all four PR refs returned no hits.
The exact transport terms have no hit in `open-registry.md` or `open-core.md`.
No prior copy of this check was found. This checks the assigned new text;
it opens no proof attack on another row's target.

Provenance: OpenAI Codex, gpt-6-astra, xhigh; 2026-11-14;
checkout 9e86cfd16ea67a8ba774c1fe29f65bd799017c13. Research-text check of
row 934, not an audit and no status grant. The requested prior file is absent.

## Checkpoint and sources

Written checks are complete below; unperformed decimal reproduction is
recorded in Section 5. No numerical run can discharge a statement.
At the final check the source blob still matched the pinned commit:
`db151a9bd23e0278539627a14e29658466ce10eb`.

Sources: row 934 whole, rows 913 and 914, row 708:98–197;
index README instructions, chunk-02:78–105, chunk-06:58–70,
obligations:50–74,297–308; then SA:2195–2257,2313–2335,6863–6869
and CA-II:141025–141120. GL3/GL4 give the kinetic spectrum and decay;
GL8 gives the gauge-projected transfer trace. The dilation identity keeps
beta unchanged. Credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text. No Balaban lemma is consumed here.

## 1. Exact transport statement

**HF (row 934 Section 1.2): HOLDS.** With `A=Khat^(1/2) M^(1/2)`,
`That=A* A`, `R=A A*`, and `chi_i=A psi_i/sqrt(lambda_i)`.
Differentiating R gives

```math
R'=\tfrac12\{N,R\}-\widehat K^{1/2}WM\widehat K^{1/2},
\qquad \lambda_i'=\lambda_i(n_i-w_i).
```

The second expectation is `lambda_i w_i`, using
`M^(1/2) Khat^(1/2) chi_i=sqrt(lambda_i) psi_i`. Thus
`Ehat_i'=w_i-n_i` and `rho_i=-D_i'`. This also checks the scalar
normalization: a coupling-dependent common factor cancels from D_i.
The factorial Bessel decay permits differentiation and makes the
eigenvectors smooth. Finite positive eigenvalue clusters have the usual
compressed derivative; ordered branches are locally Lipschitz.
Countably many levels give one common null set for these identities.

**VAC-SUB and its seed consequence: HOLDS AFTER CORRECTION.** Require
`0<beta_0<=1/25600<beta_1`; for the quantified assertion restrict to
beta_1 above that threshold. Smaller positive beta_1 are handled by the
strong-coupling input, or choose `beta_0<min(beta_1,1/25600)`.
The source currently omits strict positivity of beta_0 and says
"for each beta_1" after imposing beta_1 above the threshold.

For one even `b>=256`, one continuous `K>=0`, all m, and almost every s,
the correct condition is

```math
-H_m'(s)=\sum_{i=1}^m\rho_i(s)\le K(s)H_m(s),\qquad
\int_{\beta_0}^{\beta_1}K\le
\log\frac{b}{2\lceil\log_2 b\rceil}.
```

Multiplication by `exp(integral K)` and absolute continuity give the
integrated comparison for **every pair** s<s'. Conversely, differentiating
that comparison at a differentiability point recovers the inequality.
With `q=exp(-integral_s^s' K)`, check 914's identity gives

```math
H_{k-1}(s')-qH_{k-1}(s)
=Dfc_k-kDfc_1+(\theta-q)H_{k-1}(s).
```

This algebra does not require q<=theta. Nonnegative ABS defects do use
its own theta, but restricting q<=theta is unnecessary for VAC-SUB.
The source correctly fixes this and uses the **global** vacuum.

Correct the arrow sentence at source 103–108 to

```math
DEF_K\ \Longleftrightarrow\ LEV_K\ \Longrightarrow\ VAC\!\!\!-SUB_K
\ \Longrightarrow\ \text{thermal transport}.
```

The first arrow reverses with the regularity just proved; the later
reverse arrows are not supplied. The prefix/thermal distinction and its
counterexamples are already in check 914:359–431. No repeat attack is needed.
Abel summation of the prefix inequalities, or Lemma KF, supplies the
thermal inequality. The finite comparisons also give the right-Dini
version on row 708's characteristic curve, not merely an a.e. assertion.

With `t_0=ceil(log_2 b)`, the budget gives `(b/2)q>=t_0`.
KF therefore gives `S(b/2;beta_1)<=S(t_0;beta_0)`. The strong-coupling
bound read in TR1 is `G(t_0;beta_0)<=0.0101 t_0/b<0.00037`.
Since `exp(x)-1<=x/(1-x)` for 0<=x<1, this is below 1/1650.
Theorem SH then gives the stated lattice-gap consequence, **conditional
on precisely the seed/SH inputs**. It gives no continuum gap or
cutoff-uniform physical size.

The local-finiteness remark is valid for this fixed Wilson box. One way
to supply its omitted estimate is to use ABS infinitesimally:
`-EE_k'<=K_el EE_k`. Since `H_m>=m D_1`,

```math
\frac{-H_m'}{H_m}\le K_{el}
+\frac{2|K_{el}\widehat E_0+\widehat E_0'|}{D_1}.
```

On a compact positive-coupling interval the top is simple, D_1 has a
positive minimum, and the displayed quantities are bounded. This is
fixed-box finiteness only; it supplies no budget uniform in b.

**Other exact forms, Section 1.4: HOLDS AFTER CORRECTION.** The
time-matched force identity has the correct sign and factor:

```math
\partial_sG=\frac{t\sum_{i\ge1}\rho_i e^{-tD_i}}{1+S}
=6t|B|(\bar a_\infty-\bar a_t)
=\frac{s}{12}\{\omega_t(Q_t)-tq_\infty\}.
```

The factorial Bessel decay justifies the thermal sums
for the finite Wilson box; the Euclidean force formula is used at integer
t>=3. This is a **consequence** of the prefix condition, not another
equivalent form. In the continuous-time shadow the algebra
`-sD_i'=D_i-2s DW_i` holds. The bound on magnetic **action** is
`DW_i >= -(sK-1)D_i/(2s)`; the source's denominator 2 applies instead
to the magnetic **energy** `s DW_i`.

**BLOW: HOLDS.** It is the same integrated prefix inequality rearranged.
For other weights, assume positive locally absolutely continuous H_m.
Compactness and a simple top alone do not imply parameter regularity.

## 2. Gaussian and frozen-group tests

**Proposition G: HOLDS AFTER CORRECTION.** Direct substitution in the
kernel proves the unitary equivalence for every positive semidefinite Om.
For Om>0 the oscillator operator is compact, its top is an eigenvalue,
and its discrete excitation energies are coupling-independent: rho_i=0.
This is the valid zero-mode-removed free-photon test.

For Om with a zero eigenvalue, Fourier transform in that direction gives
the multiplier `exp(-p^2/(2s))` on L^2(R). Its supremum 1 is not an
eigenvalue and the operator is not compact or trace class. Tensoring with
the transverse oscillators changes none of those facts. Quotienting
periodic gauge gradients leaves the harmonic torons. Also, nonzero
gauge-invariant functions on the unreduced noncompact link space do not
belong to its Lebesgue L^2 space; the quotient measure must be used.
Thus the source's full-photon assertion `rho_i=0, H_m, Rem_m=0` is
undefined, rather than proved, on its stated zero-mode domain.
Compactifying torons would change the model and invalidate the dilation
argument for them. The main-repo photon note already keeps this distinction.

The restricted oscillators pass VAC-SUB_K with K=0, but supply no
strong-coupling seed. The oscillator calculation already in
`gap-seam-max.md:89–113` gives `omega_k=2 asinh(sqrt(kappa_k)/2)`.
For k=(2*pi/b,0,0), `(b/2)omega_k=b asinh(sin(pi/b))<=pi`, so
`S(b/2;b^3)>=exp(-pi)>1/1650`, independently of coupling.
This shows why a local photon test alone cannot
test transport **from a seed**. It does not prove the compact U(1) test.

**FR and its fixed-box budget consequence: HOLDS.** Normalize the link
kernel as a probability on G. At fixed finite box it tends to the identity
convolution; `M_beta` tends to the flat-configuration indicator. Thus
That tends in norm to the flat-subspace projection. Gauge fixing a
spanning tree identifies flat configurations with homomorphisms
`pi_1(T^3)->G`, modulo simultaneous conjugation. Its rank is c_3(G).
Exactly c_3 eigenvalues tend to 1, and all others tend to 0. Hence
`D_1,...,D_(c_3-1)->0`, the other D_i tend to infinity, and
`S(t)->c_3-1` for fixed t>0. Positivity of the finite-beta kernel makes
its top simple. BLOW now forces the rate integral to diverge.

The phrase "all of Section 1 holds" needs the finite-dimensional range
`1<=m<dim H` and the group's own kinetic coefficients. For the two named
groups their positivity and monotonicity can also be checked by hand.
Reuse the odd coefficients of `gap-q8test-opus.md:37–54`; include the
even characters of Q_8/{+-1} and 2T/{+-1} from that same character table.
For Q_8 the nontrivial ratios are
`(cosh beta-1)/(cosh beta+3)` and `sinh beta/(cosh beta+3)`;
their derivative numerators are `4 sinh beta` and `1+3 cosh beta`.
For 2T set C=cosh(beta/2)>1, S=sinh(beta/2), Q=C^2+4C+1.
The four distinct nontrivial ratios are

```math
\frac{(C-1)^2}{Q},\quad\frac{C^2-1}{Q},\quad
\frac{S(C+2)}{Q},\quad\frac{S(C-1)}{Q}.
```

Their C-derivative numerators, after the positive denominators Q^2 or
S Q^2 are removed, are respectively
`6(C^2-1)`, `4(C^2+C+1)`, `2C^3+3C^2+6C+7`, and
`(C-1)(5C^2+8C+5)`. All are positive. Thus the kinetic-rate premise
does hold for Q_8 and 2T. This check makes no blanket claim for an
arbitrary positive-definite finite-group weight.

**Finite counts: HOLDS.** Reuse row 930's counts. Burnside on commuting
triples gives `c_3(G)=#commuting quadruples/|G|`. A noncentral commuting
tuple lies in exactly one maximal abelian subgroup. Consequently

```math
Q_8:\quad N_0=16+3(4^4-16)=736,\quad c_3=92;\\
2T:\quad N_0=16+3(4^4-16)+4(6^4-16)=5856,\quad c_3=244.
```

An anticommuting pair must have zero quaternion scalar part. In these
groups it is an ordered pair from different quaternion axes: 6*4=24.
Its common centralizer is {1,-1}; the remaining two holonomies give
4 choices. Thus `N_tw=96`, and the ratios are `96/736=3/23` and
`96/5856=1/61`. In a comb gauge on the torus, links inside each cut
carry the corresponding generator holonomy. Flat plaquettes force the
commutator relations; replacing one relation by -1 places exactly the
central twist sheet. The tree factors are the same in numerator and
denominator. Thus these are partition ratios, not unweighted orbit ratios.

**Uniform freezing and the claimed VS-1 refutation: FAILS as a deduction
from FR.** The proved quantifiers are `for every b, there exists beta_fr(b)`.
The sentence "for the finite groups no b works above the freezing coupling"
requires the opposite uniform order. Sheet geometry alone supplies no
tunnel-splitting estimate or finite-coupling Peierls theorem.
Keep the quoted freezing temperatures and splitting estimates as GUIDE.
Moreover FR concerns beta tending to infinity. VS-1 permits a different
c on every bounded interval. Already `D(beta)=exp(-beta)` tends to zero
while `-D'=D<= (1+log^+(1/D))D` for all beta>=0. Thus FR cannot refute
VS-1 even on one fixed cube. This is a logical counterexample to that
inference, not a claim about the finite-group spectrum at finite beta.

## 3. Compact U(1), first-order tests, and the scope of NOGO

**Section 2.2(a): HOLDS AFTER CORRECTION.** The contrapositive is sound
if the named rival-model input says that a **uniform periodic-cube gap**
fails at beta_1. Alternatively add a precise seed-to-Wilson-area-law
implication and a theorem excluding that same area law. Theorems S and SH
as read in `gap-crux-restate.md:192–230` and `gap-seed-shape.md:83–110`
give a spectral gap, not an area-law statement by themselves. The source
instead names only "no area law" and silently adds the bridge.
The cited `gap-crux-fp.md:40–43` recalls both masslessness and no area law;
its author explicitly did not check the observable in the power-law theorem.
The prior reading at `prior/gap-crux-lit-nonab.md:85–87` is abstract-only
for Fröhlich–Spencer and records no theorem text from Guth. Thus this
remains a conditional rival test, not a new verification of those papers
or of their precise Wilson/Villain scope.

The numerical strong-coupling estimate used by TR1 must hold for the same
U(1) weight and beta_0. A statement that a cluster expansion exists does
not by itself supply its constant 12800. It can be retained as an explicit
premise, or beta_0 can be chosen in a separately established seed regime.

**Sections 2.2(b,c), 2.3: HOLDS AFTER CORRECTION as GUIDE.** For a
compact zero-mode rotor with energy `n^2/(2s)` the logarithmic rate is
1/s. Photon oscillator energies in the normalized noncompact model do
not move with s. Neither calculation bounds the supremum over all
prefixes defining K_b for compact Wilson U(1). With a renormalized
coupling s_R(s), the flux-level rate is `s_R'/s_R`, not exactly 1/s.
Replacing the lattice photon dispersion by |k| is a low-momentum
approximation. The logarithmic budget comparison is valid as scaling
arithmetic: a level falling from m_0 to C/b costs `log(b m_0/C)`.
It does not locate that loss at beta=1.01 or exclude losses elsewhere.
Delete "must break only where monopoles condense" and "nowhere in the
Coulomb phase" as deductions. The source labels the phase picture GUIDE;
its later assertions cannot promote it to a necessity theorem.

**Section 3.2(a): HOLDS conditionally on its stated quantitative seed,
REG and KF inputs, with beta_0<beta_t<beta_1.** Its actual conclusion is

```math
\int K>\log\frac{b}{4\lceil\log_2 b\rceil},
```

not the budget (B) with 2. Put `t_1=2 ceil(log_2 b)`. The displayed
assumption implies `(b/2)exp(-integral K)>=t_1`, and K>=0 makes this
true throughout the interval. The seed estimate gives
`G<=0.0101 t_1/b^5`. Since t_1<=b for b>=256, this is at most
`0.0101/256^4<1/10^11`. The inequality `exp(x)-1<=x/(1-x)` gives
the asserted `S<1/(2*5041)`. REG then contradicts a kink at beta_t.
This also checks the factors 2, 4 and the exponent 8 in that argument.

To obtain failure of **(B)**, the missing stronger conclusion in the
summary, add the already named SH input explicitly. Here is the short
repair using existing results, not a new proof of them. Under (B), TR1
gives uniformly `S(a;(2a)^3)<1/1650`, a=b/2. Its shape conversion gives
`S(a;(4a)^3)<=0.0396`. SH for ratio 4 gives
`S(a_k;(4a_k)^3)<=q^(2^k)/22.2`, with
`q=22.2*0.0396=0.87912<1` and a_k=2^k a. Choose one k so this
is below 1/200. Time doubling gives
`S(2a_k;(4a_k)^3)<1/40000`, uniformly on the interval. REG now applies
with n=2a_k. This proves the stronger conditional exclusion of (B).

**Application to V and K7: HOLDS AFTER CORRECTION, as conditional
applications only.** For V keep the exact van Enter–Shlosman theorem,
its SU(2)/normalization identification, TM-gen, and the quantitative
strong-coupling seed as inputs; the source explicitly leaves these imports.
For K7 specify a one-parameter weight and its derivative observable.
For a fixed ray `w_s=exp(s phi)` the same proof applies given a kink,
bounded phi, the seed, and REG's hypotheses. An arbitrary curved path
in (beta_F,beta_A) needs its own version of these hypotheses.
The recalled first-order line is not a theorem proved in this note.
HF uses `W_s=partial_s(-log M_s)`, not the Wilson W unchanged.
ABS also needs positive kinetic eigenvalues and its monotone-ratio
hypothesis along that path. Positive character coefficients alone do
not assert their parameter monotonicity. The statement that these
lemmas hold "verbatim for K7" omits those conditions.

**Two-level GUIDE arithmetic: HOLDS AFTER CORRECTION.** For the stated
ansatz set A=ell*|B|>0, delta>0 and x=s_c-s>=0. Then, exactly,

```math
D=\sqrt{A^2x^2+\delta^2},\quad
\rho=\frac{A^2x}{D},\quad
\frac\rho D=\frac{A^2x}{A^2x^2+\delta^2},\quad
\max_{x\ge0}\frac\rho D=\frac{A}{2\delta},\\
\int_{s_c-\eta}^{s_c}\frac\rho D\,ds
=\frac12\log\left(1+\frac{A^2\eta^2}{\delta^2}\right).
```

The maximum follows from `(Ax-delta)^2>=0` and occurs at x=delta/A.
The source's logarithm is the large-A*eta/delta asymptotic, not the
exact integral. A restricted approach interval need not attain the
maximum. With delta of order exp(-sigma|B|) the claimed volume cost
follows in this ansatz. It is not a derivation of that splitting for K7.

**The "exactly on intervals" conclusion (3.4): FAILS.** Failure of a
seed forces failure of a sufficient transport budget, given the common
starting seed. The converse has not been shown. Nor does an integral
lower bound locate a pointwise divergence near a transition. Existing
check 914 already distinguishes sufficient prefix transport from the
weaker thermal condition. Section 3.4 reverses that implication again.

**NOGO: common structural facts HOLD AFTER CORRECTION; the unrestricted
proof-impossibility claim FAILS.** U(1) has the HF construction, KF,
the positive-kernel comparisons with their kinetic hypotheses, and
the same integration-by-parts scheme with Laplacian eigenvalue 4.
The Bessel monotonicity needed here follows from the already available
`gap-q8test-opus.md:157–170`, now starting its product at nu=0.
But the exact U(1) spectrum is `I_n/I_0`, whereas SU(2) uses `I_(2j+1)/I_1`
with different multiplicities and trace algebra. Sharing a form of an
identity, with changed constants and operators, does not make the two
sets of quantitative premises identical. A proof may use that distinction.
Even the force-overlap scalar product has three quaternion-vector
components for SU(2), versus one sine component for U(1).

The valid restricted conclusion is: a universal argument using **only
the common structural inequalities**, with bounds also valid in the
rival and satisfying the same budget, would contradict the repaired
U(1) input. The displayed calculations supply no separating bound.
This is not a proof that every argument from the listed exact SU(2)
objects is impossible. Likewise an expectation of a commutator is an
identity; its linearity alone does not preclude deriving an inequality
from it with additional spectral or positive-square information.

## 4. SLICE, VIR, and CONC

**SLICE(i,ii): HOLDS.** On the compact configuration manifold,
`div(grad W)=Delta W=-12 Wt`. The skew generator of pullback by this
complete vector field, including the square root of its Jacobian, is
`g=d+(div grad W)/2=d-6Wt`. The product rule gives
`[Delta,Wt]=2g`. For real smooth normalized psi,
`<psi,d psi>=-(1/2)<psi^2,Delta W>=6<psi,Wt psi>`, proving (A).
For complex psi use the real part. A real eigenbasis can be chosen.

**SLICE(iii): HOLDS AFTER CORRECTION of the functional's meaning.**
For an observable on several slices, define its transfer insertion
F_{[-r,r]} by integrating those local links, and set
`omega_i(F)=lambda_i^(-2r)<psi_i,F_{[-r,r]} psi_i>` with the endpoint
spatial half-weights included. This is the consistent interpretation
of the source's trace shorthand. The excited-level functional need
not be positive; it is not a positive infinite-volume Gibbs state.
Its finite-cylinder representation has signed boundary factors outside
the differentiated links, so integration by parts still applies.

For the outgoing temporal slab, differentiating the kernel gives
`s omega_i(grad W . grad A_+)=-<psi_i,d psi_i>
-(s/2)<psi_i,|grad W|^2 psi_i>`. Kernel symmetry gives the same incoming
term. The spatial action contributes `s<|grad W|^2>_i`; these two force
terms cancel it. The summed loop equation is exactly
`12(3|B|-w_i)=-2<psi_i,d psi_i>`. It supplies no new inequality.

**VIR and its Gaussian specialization: HOLDS.** Smooth eigenvectors
justify `<psi,[X,That]psi>=0`. Expanding the commutator with
`M^(1/2) Khat M^(1/2)` and using
`[g,M^(1/2)]=-(s/2)|grad W|^2 M^(1/2)` gives precisely (V).
For the positive-frequency Gaussian operator, dilation covariance gives
`[D,That_s]=2s That_s'`, hence lambda_i'=0. Keep the zero-mode correction
from Section 2. The Wilson Hessian does have the displayed diagonal
blocks `sum_(p through l) x_p` times the round metric. Mixed blocks
occur as stated. These observations document a failure to close this
calculation; "closes only for Gaussian weights" and "a commutator
identity cannot produce the sign" are not proved classification results.

**CONC and its corollary: HOLDS, with kinetic exponent th>0.** Let
`Q_k=wedge^k Khat` and let W_k be the sum of the k copies of W on the
antisymmetric subspace. Its spectral measure is nonnegative. For unit v,

```math
f_v(u)=\langle Q_k^{1/2}v,e^{-uW_k}Q_k^{1/2}v\rangle
```

is log-convex by Hölder. Taking the supremum preserves log-convexity:
apply Hölder first to each v and then bound both endpoint integrals by
their suprema. This supremum is the product of the k largest transfer
eigenvalues. Thus EE_k is concave. Its non-decrease follows from the
isospectral order `Khat^(1/2) M_u Khat^(1/2)`, as check 914 requires.
Interchange the two factors for the kinetic exponent proof. At th=0
M alone need not be compact; the ordered-eigenvalue formulation must
either exclude that endpoint or define its limit separately.

For fixed b_t=s, concavity gives
`s partial_u EE_k(s,s)<=EE_k(s,s)-EE_k(s,0)`.
HF subtracts the nonnegative electric expectations on the isotropic
line, proving the right-hand inequality of the corollary. ABS supplies
the left-hand inequality. Subtracting k vacuum expectations gives
exactly the displayed upper bound on the magnetic excess. This is the
wrong direction for bounding rho from above. No volume-asymptotic
size or sign of the vacuum-subtracted curvature is established here.

## 5. ODE, the solvable model, and GUIDE arithmetic

**Proposition ODE: HOLDS given its stated uniform starting gap.** Take
c>=0 (enlarge it if needed). For `y=log^+(1/D_1)`, the chain rule and
the zero derivative a.e. on a Lipschitz function's zero set give
`y'<=c(1+y)`. Integration gives the slightly stronger bound

```math
D_1(s)\ge\exp\{1-(1+\log^+(1/m_0))e^{c(s-\beta_0)}\}.
```

The weaker printed bound follows. This checks the implication; the
uniform starting gap from rows 836/841 remains a named input.
VS-1 concerns **all sufficiently large boxes** with one c on each bounded
coupling interval. VAC-SUB selects one box with an integral budget.
Calling VS-1 the "smallest" remaining VAC-SUB lemma is not a proved
minimality or equivalence: its quantifiers differ and it lacks the
state-count control needed for the thermal seed.

**Proposition N(i,ii): HOLDS for the stated gap equation.** Put x=mu^2
and `u_k=4 sin^2(k/2)`. Integrating the infinite-time momentum yields

```math
\Phi_b(x)=\frac1b\sum_k[(x+u_k)(x+u_k+4)]^{-1/2},\\
-\Phi_b'(x)=\frac1b\sum_k
\frac{x+u_k+2}{[(x+u_k)(x+u_k+4)]^{3/2}}>0.
```

The positive-mass lattice resolvent has a convergent nearest-neighbor
walk expansion with nonnegative coefficients. Periodization and Tonelli
therefore give `Phi_b=sum_n G(nb,0)` and
`-Phi_b'=sum_n(G*G)(nb,0)=sum_(x on cylinder) G_b(x)^2`.
As `D=2 asinh(mu/2)`, `dD/dx=1/(mu sqrt(mu^2+4))`.
Inverse differentiation gives exactly the printed positive formula for
1/K_b. Its n=0 summand is the infinite-plane inverse rate at the **same
mu**, not at the same beta. This qualification is correctly present.

**N(iii): HOLDS; the summary's unrestricted K<=29 needs correction.**
For 0<mu<=2 the disk |p|<=mu lies inside the Brillouin zone and
`phat^2<=|p|^2`. Hence

```math
(G*G)(0)\ge\frac{1}{4\pi^2}
\frac{\pi\mu^2}{(2\mu^2)^2}=\frac1{16\pi\mu^2}.
```

Concavity gives `2 asinh(mu/2)>=mu asinh(1)>0.88 mu`.
For a hand check of the decimal, the exponential series with a geometric
tail gives `exp(22/25)<2411/1000<1+707/500<1+sqrt(2)`.
Thus `1/K_b>=1.76/(16*pi)`, and `K_b<=16*pi/1.76<29`
(even pi<22/7 suffices for the last inequality).

For mu>=2, x>=4 and 0<=u_k<=4 give
`-Phi_b'>=x/(x+8)^3` and D>=log x. Consequently

```math
K_b\le\frac{(x+8)^3}{x^2\log x}
\le\frac{27x}{\log x}
\le\frac{27}{\beta\log(1/\beta)}.
```

The last step uses beta=Phi_b(x)<=1/x, so x<=1/beta, and x/log x
is increasing for x>=4. This supplies the omitted uniform bound for
the small-beta range. In fact beta~1/x and K_b~x/log x as x grows.
There is no global bound 29 all the way to beta=0. The claims in Section 6,
the summary, and RESULT must retain `mu<=2`, or use a constant depending
on the lower endpoint beta_0>0 of the coupling interval.

**N(iv): HOLDS AFTER CORRECTION of the model scope.** For every momentum,
`(partial_x omega_k)/omega_k` decreases as x+u_k increases. Multiplication
by the common positive `-dx/d beta` gives its rate <=K_b. The rate of
a finite sum of particle energies is their energy-weighted average,
so it has the same upper bound. This proves the level assertion in the
assumed free-dispersion model and gives VS-1 on each compact positive-beta
interval with the preceding uniform bound.

The saddle-point gap equation and its identification with the O(N)
model were RECALLED, not derived. At literal N=infinity the infinitely
many particle species also prevent treating its full thermal trace as
a compact finite-multiplicity operator. To invoke VAC-SUB/KF for a trace,
specify a finite-multiplicity free Fock model, or prove a finite-N
statement before taking limits. The algebra for the mass parameter is
not that missing identification or a proof of the original model's
thermal budget.

**Appendix GUIDE: HOLDS AFTER CORRECTION to finite-sample, unverified
execution claims.** The code's derivative is correct: differentiating
`[z(z+4)]^(-1/2)` gives `-(z+2)[z(z+4)]^(-3/2)`.
Its factors 1/b and 1/b^2 are exactly the normalized momentum sums for
a cylinder with one or two finite spatial directions. Its K formula
matches the reciprocal derivative above. It samples **600 masses in
[10^-6,2]**, and only every third mass for the two-dimensional spatial
torus. A maximum of that grid is not a supremum over all masses, rings,
or box sizes. The finite list cannot establish the coefficient 3.3 as
an asymptotic law, or prove failure of VS-1 or of a transport budget.

One hand arithmetic anchor for the table is b=4, mu=2. The four spatial
eigenvalues are 0,2,4,2, so

```math
Q=\tfrac14\left\{\frac6{32^{3/2}}
+\frac{16}{60^{3/2}}+\frac{10}{96^{3/2}}\right\},\qquad
K=\{8\sqrt2\,\log(1+\sqrt2)\,Q\}^{-1}\approx5.13.
```

This agrees with that rounded endpoint entry; it is not a check of the
maximum over its grid. The 2*pi entries are consistent with the
small-mass infinite-plane limit of the formulas. No finite grid proves
the phrase "true supremum 2*pi". The beta=1 values require a root solve
absent from the printed script. The finite-difference value 38.72319
has neither a step size nor a differencing prescription; it is not a
reproducible check as recorded. The relative difference between the two
printed numbers is approximately `0.00097/38.72416`, or 2.5*10^-5;
this alone supplies no accuracy bound.

No numeric job was run in this check. `scripts/lab_ops.py` is absent
in this sparse checkout. Its main-branch lock code was read: it uses
`/tmp/physics-lab`. An attempt to create that directory returned
"File exists". It is therefore not a scratch directory created by this
task and lies outside the user's permitted reading boundary. I neither
read that existing lock nor substituted a private lock that would fail
to coordinate the machine. **The remaining printed decimal entries
were not independently reproduced.** They retain GUIDE/report-only
status; this limitation is not a mathematical refutation of those values.

**Other fact-test arithmetic.**

- Section 1.4's two-loop correction: differentiating the supplied
  `a Lambda=(6*pi^2*beta/11)^(51/121) exp(-3*pi^2*beta/11)` gives
  `-partial_beta log a=3*pi^2/11-51/(121 beta)`. The factors 2.69 and
  0.42/beta are consistent. This checks its algebra, conditional on the
  recalled asymptotic formula; it proves no order-one rate.
- Test 2D-YM: on a ring gauge invariance leaves one holonomy character,
  with transfer ratio `(I_n/I_1)^b`. Hence `D_1=b eps_2` and
  `rho_1/D_1=nu_2/eps_2`. On a compact positive-coupling interval this
  gives a box-independent VS-1 constant. Large b with b eps_2>=1
  show that c must be at least this rate. HOLDS.
- Test DIM: the three-dimensional guide would challenge VS-1 only
  if its asserted growth persists as b tends to infinity in one
  bounded beta interval, after division by `1+log^+(1/D_1)`.
  The finite sample does not prove this. Its four-dimensional numerical
  budget (B) is not automatically a seed criterion for a different
  dimensional model. Keep this as a diagnostic, not a discharged test.
- The proposed small-cube refutation test in Section 6 also omits that
  logarithm. Growth of rho_1/D_1 alone is insufficient. The quantity to
  test is `rho_1/[D_1(1+log^+(1/D_1))]`, uniformly over arbitrarily
  large boxes on a common compact coupling interval. Finite numerical
  growth can guide such a test but cannot refute its uniformity alone.

## 6. Interpretations and final verdicts

The scaling discussion in 5.5 is conditional algebra, not a Wilson
identity. From the supplied Gamma ansatz,
`partial_s G+kappa t partial_t G=-kappa b partial_b G`.
Replacing `b partial_b G` by 3G needs exact extensivity and a continuous
box-size interpolation; it is not exact on a finite lattice. The sign
also needs kappa>=0. Under those added assumptions the pressure formula
holds. Nonnegativity of G alone does not imply `b partial_b G>=0`.
This thermal inequality remains weaker than the prefix condition.
LOC and AMP are proposals, not established estimates for a delocalized
eigenstate. The cited dilation identity keeps beta fixed and supplies
none of these coupling comparisons. A targeted index search establishes
only no hit under its terms, not an absence theorem about the full account.

The O(2)/O(3) calibration cannot identify VS-1 with "no transition".
ODE gives one sufficient quantitative route to a uniform gap. Absence
of a thermodynamic singularity alone is not the reverse implication,
nor does a positive gap by itself control its logarithmic derivative.
Keep the cited physical analogies as ARGUED, with their recalled
theorems and model identifications unverified here.

The table covers the author's numbered summary and the corresponding
statements in the body. HOLDS for a conditional statement checks the
implication and retains its named inputs; it does not certify those
inputs. FAILS also identifies an invalid deduction, not necessarily
a counterexample to the Wilson conclusion.

| Author item | Verdict | Scope or correction |
|---|---|---|
| 1 HF | HOLDS | Global vacuum, matching chi_i, a.e. ordered derivatives. |
| 2 VAC-SUB and placement | HOLDS AFTER CORRECTION | beta_0>0; beta_1 range; DEF_K iff LEV_K; thermal consequence is not an equivalent form. |
| 3 Seed consequence | HOLDS | Given the quantitative strong-coupling seed, KF and SH; lattice conclusion only. |
| 4 Gaussian G | HOLDS AFTER CORRECTION | Unitary equivalence on the full space; level/trace statement only after removing noncompact zero modes. |
| 5 Compact U(1) exclusion | HOLDS AFTER CORRECTION | Add the precise no-uniform-gap input, or the missing area-law bridge, for the same weight and starting seed. |
| 6 Coulomb K_b and location | HOLDS AFTER CORRECTION | Low-mode GUIDE only; no all-prefix bound or proof that all loss is at the transition. |
| 7 BLOW | HOLDS | Positive absolutely continuous prefix sums. |
| 8 First-order rate cost | HOLDS | Conditional smaller-budget statement as printed; beta_t lies inside the interval. |
| 9 V/K7 application and full (B) | HOLDS AFTER CORRECTION | Weight/path hypotheses and source imports remain; SH iteration supplies the missing full-budget argument. |
| 10 Two-level blow-up | HOLDS AFTER CORRECTION | Exact integral is half log(1+(A eta/delta)^2); model only. |
| 11 FR, c_3(Q_8) | HOLDS | Fixed box, beta tending to infinity; c_3(Q_8)=92, c_3(2T)=244. |
| 12 Fixed-box budget failure | HOLDS | Threshold may depend on the box. |
| 13 Frozen uniformity and counts | HOLDS AFTER CORRECTION | Counts hold; uniform finite-coupling freezing remains GUIDE, not a consequence of FR. |
| 14 SLICE | HOLDS AFTER CORRECTION | Specify the signed cylinder insertion functional; it is not a positive excited Gibbs state. |
| 15 VIR | HOLDS AFTER CORRECTION | Identity holds; restrict Gaussian levels, remove the unproved "only" classification. |
| 16 NOGO common identities | HOLDS AFTER CORRECTION | Shared structural forms only; exact spectra/constants differ. |
| 16 No proof from all listed inputs | FAILS | The claimed identical-premise transfer is not established. |
| 17 ODE | HOLDS | Given the uniform starting gap; VS-1 stays OPEN. |
| 17 Fixed-cube VS-1 failure from FR | FAILS | Infinite-coupling collapse does not contradict bounded-interval VS-1. |
| 18 N(i–iii) | HOLDS | Algebra for the recalled gap equation; 29 only for mu<=2. |
| 18 N(iv), full thermal reading | HOLDS AFTER CORRECTION | Branch rates hold; specify finite multiplicities and retain the recalled model identification. |
| 19 GUIDE run | HOLDS AFTER CORRECTION | Code formulas and hand anchor agree; samples are not suprema; remaining decimals not reproduced. |
| 20 CONC and corollary | HOLDS | th>0; left side conditional on ABS; no sign after vacuum subtraction. |
| 20b Scaling/pressure | HOLDS AFTER CORRECTION | Explicit scaling, exact extensivity and kappa>=0 premises; not finite-lattice proof. |
| 21 Calibration as an equivalence | FAILS | No-transition, uniform gap, and VS-1 have not been proved equivalent. |
| 22 Wilson VAC-SUB | HOLDS as an OPEN declaration | No proof or refutation of the Wilson inequality is supplied. |
| 3.4 "fails exactly" and corresponding summary | FAILS | Reverses a sufficient-condition implication. |

Only this check file changed. No source, registry, FINISH row, audit file
or status record changed. No Lean check, numerical proof, commit, push,
or external post was performed. The note is left uncommitted and unpushed
at the requested lane path. The remaining obligation is still a Wilson
vacuum-subtracted response estimate with its stated integral budget;
VS-1 does not replace the missing thermal state count.

RESULT: HOLDS for HF, BLOW, the fixed-box finite-group limit/counts, ODE, the gap-equation identities and CONC; HOLDS AFTER CORRECTION for VAC-SUB's exact placement, the Gaussian/compact-U(1)/K7 applications, SLICE's functional, and the solvable-model scope; FAILS for the unrestricted NOGO, the converse seed/transport claim, and the frozen-group refutation of bounded-interval VS-1. GUIDE formulas were checked, but remaining sampled decimals were not reproduced. Wilson VAC-SUB and VS-1 remain OPEN; this check grants no status.
