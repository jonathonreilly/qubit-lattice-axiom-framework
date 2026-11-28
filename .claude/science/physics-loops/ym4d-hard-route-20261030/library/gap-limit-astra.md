# Repo search

OpenAI Codex, gpt-6-astra, max (the dispatched runner), 2026-11-11.
Research check at `bb010c2378151c5f95383006a3642d5ba4101826`, FINISH row 723.
This is not an audit and grants no status. No computer-assisted proof is used.
The target is the conditional seed-to-limit implication, not a proof of its
seed, a gap at coupling of order one, or continuum Yang–Mills existence.

The target-specific `prior/gap-limit-astra.md` is absent. The lead's
`prior/repo-search-2026-11-08.md` searches main and PRs 10114, 10133, 10134,
10141, but its thirteen targets predate this check. Its nearest hit is
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`: positive one-step correlation, not
a uniform gap. `gap-transfer.md:6,279` also credits the earlier
`MASS_GAP_CONSTRUCTION_ASTRA.md` finite-volume transfer construction.
The following primary passages were opened, not inferred from that digest:

| Source checked | Closeness and use |
|---|---|
| PR 10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–173` | Positive one-step plaquette correlation. It gives an upper bound on a spectral threshold, not the present lower bound. No new witness is claimed. |
| Same ref and folder, `MASS_GAP_CONSTRUCTION_ASTRA.md:85–213` | Same Wilson transfer, up to a scalar; the earlier Codex/Astra bound is `-log(1-exp(-6 beta L^3))` in lattice units. It degenerates with volume and does not supply the seed. Reused as prior construction. |
| Main at `1f20846b8057f6346ebab6c0dbebdabbd9e472a4`, `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md:1–190` | Prior hand proofs of Wilson character nonnegativity and Gram positivity on a finite slab. These are upstream positivity results, not a seed or a limit-gap theorem. No runner evidence is used. |
| Pinned local CR 213–221 | E'/S3' already supplies every sufficiently large integer cube side from one seed. The all-side conclusion is not new work for this lane. |

The registry has no matching
`gap-seed-limit`, `gap-limit-astra`, `PHYS-SEED`, or mass-gap ownership row.
The assigned cross-provider check is distinct from supplying the seed.

Main's workflow was read at `1f20846b8057f6346ebab6c0dbebdabbd9e472a4`.
Its current entry is `procedures/check.md`; the user's explicit output path
and research-only verdict format govern this report. No registry, source
proof, ledger, audit record, or planning state is being edited.

The outline was fetched once at `31a47c543775` as `/tmp/sa_ym4.tex`, and
CA-I once as `/tmp/sa_ca_I.tex`. The README, matching chunk rows and their
neighbours, and obligations were consulted for the needed objects:
chunk 01 (fixed-spacing limits; mass-gap scope), chunk 02 (GL3/GL8),
obligations 18–29 and 1492–1500; also the CA full-index README and its
opening rows. Relevant source excerpts read were SA 129–143, 418–469,
588–600, 2195–2243, 2313–2335; CA-I 2498–2511 and 2701–2713.
SA already supplies the finite-spacing compactness construction and
positive transfer mechanism. Its polynomial-decay example does not give
a gap; CA-I 2706–2713 explicitly excludes a mass-gap assertion there.
No source inspected supersedes the assigned check of the local
seed-to-limit implication. This is a bounded comparison, not a claim
that the entire external account was searched or independently verified.

## Status and coverage

- Complete: 38 own verdicts written first, then six comparison points
  C1–C6 after reading the earlier check. The core conditional theorem holds.
- Earlier check file: **READ IN FULL AFTER THE OWN-VERDICT CHECKPOINT**.
  Inline lead notes were visible earlier; they were not verdict evidence.
- Scope: all statements in `gap-seed-limit.md`; load-bearing inputs in
  `gap-crux-restate.md` Sections 1 and 3.4 and `gap-transfer.md`, including
  the row-671 corrections; the precise continuum hypotheses where used.
- Not covered: the seed estimate, renormalization construction, continuum
  existence, the free-particle counting guide, or a global optimization of
  the earlier ring example. The all-side extension is reused from row 699,
  not claimed as new work.
- Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
  of their text; Tadeusz Balaban for the upstream constructive program.
  No theorem from Balaban's papers is an input to the spectral argument here.
  The finite-volume transfer and reflection-positivity method also credits
  Konrad Osterwalder, Erhard Seiler, and Martin Lüscher.

## Verdicts written before reading the earlier check

Line references below are to the pinned source, not this report. Write
`SL` for `gap-seed-limit.md`, `CR` for `gap-crux-restate.md`, and `TR` for
`gap-transfer.md`.

### 1. Setting, thermal facts (i)–(iv), (G1)–(G3), (K1)–(K2): HOLDS

SL 32–52. Only positive eigenvalues are enumerated; the kernel contributes
zero at positive time. TR's gauge projection is retained, including for
non-invariant insertions. For positive integers a,b,

\[
 S(a+b)=\sum_j\rho_j^a\rho_j^b
 \le\Bigl(\sum_j\rho_j^a\Bigr)\Bigl(\sum_j\rho_j^b\Bigr).
\]

Monotonicity, \(\rho_1^a\le S(a)\), and
\(Z_T=\lambda_0^T(1+S(T))\) follow term by term. From (G1),

\[
 m(L_k^3)\ge m_0+\frac{\log5041}{n_k}\ge m_0,
 \qquad m_0=\frac{-\log q}{n},\quad q=5041s.
\]

Thus (G3) loses a positive term harmlessly; simplicity (G2) is supplied
separately by TR (4). Pointwise domination of the slab kernel by
\(\|F\|R^{w(F)}\) gives its operator norm at most
\(\|F\|\lambda_0^{w(F)}\), even though the inserted kernel need not be
self-adjoint. Width zero uses multiplication. Ground-state evaluation gives
(K2). No spatial-volume bound follows from TR's kernel floor alone.

### 2. Lemma T: HOLDS

SL 56–66. There are exactly \(w(F)+d+w(H)+d'=T\) time steps.
Integrating the two empty arcs first produces \(R^d,R^{d'}\); integrating
each occupied slab produces its inserted operator. All integrals are finite
and bounded, so the stated trace and the factor \(\lambda_0^{-T}\) follow.
If either width is zero the corresponding insertion is a multiplier, with
no delta kernel asserted to be Hilbert–Schmidt.

For an independent convergence check, fix j and apply Cauchy–Schwarz to
the i sum with \(0\le\rho_i^d\le1\). Its absolute sum is at most
\(\|F\|\|H\|\). Summing against \(\rho_j^{d'}\) is finite because
\(d'\ge1\) and R is trace class. This also justifies both cyclic orders
used later. The one-point formula uses the remaining time \(T-w(F)\),
not T. The onset \(t_0=b_A-a_B\) and the width-zero case are correct.

### 3. Proposition C: HOLDS

SL 68–76. Set \(P_0=|\Omega\rangle\langle\Omega|\) and
\(Q=1-P_0\). Expand each positive-time propagator as
\(R_n^d=P_0+R_x^d\). The four products give exactly \(fh,u,u',v\).
The mixed terms have bounds \(\|F\|\|H\|\rho_1^d\) and
\(\|F\|\|H\|\rho_1^{d'}\). For the last term, operator/trace norm
duality gives

\[
 |v|\le\|F\|\|H\|
 \min\{\rho_1^d\operatorname{Tr}R_x^{d'},
          \rho_1^{d'}\operatorname{Tr}R_x^d\}.
\]

This derives the minimum without discarding multiplicities. The cylinder
interpretations keep the order of the two insertions; they require no
self-adjointness of either insertion.

### 4. Theorem L1 and the one-point error: HOLDS

SL 80–90,110. With unit observable norms, write the two expectations as
\((f+\alpha)/(1+S_T)\), \((h+\gamma)/(1+S_T)\). The numerator after
centering is precisely

\[
 u+u'+v+S_TN-f\gamma-\alpha h-\alpha\gamma,
 \qquad N=(1+S_T)\langle FH\rangle.
\]

In particular \(|S_TN|/(1+S_T)^2\le S_T\), so no squared-denominator
term was lost. Put \(\sigma=S(d')\) and \(r=e^{-md}\).
The seven terms are bounded by \(r+r\sigma+4\sigma+\sigma^2\).
For \(\sigma\le1\), this is at most \(r+6\sigma\); for
\(\sigma>1\), the elementary covariance bound 2 suffices. This verifies
both the precise bound and the constant 6, including complex observables.
The one-point difference is
\((\alpha-fS_T)/(1+S_T)\); its bound is
\(2\|F\|S(T-w(F))\). Both factors 2 are justified.

### 5. (COV), Theorem L2, and the percentage: HOLDS

SL 92–108. Write \(d'=jn_k+r\), \(j\ge1\), \(0\le r<n_k\).
Monotonicity and submultiplicativity give \(S(d')\le s_k^j\), including
r=0 without introducing S(0). Since
\(s_k^j=5041^{-j}e^{-m_0n_kj}\), the second displayed bound follows.
When \(d\le n_kj\), the coefficient is at most

\[
 1+\frac6{5041}<1+\frac2{1000}=1.002,
 \qquad \frac6{5041}<\frac{12}{10000}=0.0012.
\]

The integer checks are \(6000<10082\) and \(60000<60492\).
Thus the error is strictly below 0.12 percent. On a symmetric torus,
\(d'=2n_k-d-w(F)-w(H)\ge n_k\) forces the required comparison with d.
The source's uncontrolled middle interval is correct for this chosen
orientation. Its later sentence SL 256, “no bound when d'<n_k”, must be
read as **no small-error estimate in that orientation**: when
\(d\ge n_k\), exchanging d and d' gives the already stated bound.

### 6. Lemma FE: HOLDS

SL 124–126. A four-dimensional link meets \(2(4-1)=6\) plaquettes.
The Wilson contribution of one plaquette lies between 0 and \(2\beta\).
For a finite link set \(\Gamma\), deleting every incident plaquette
therefore changes the density by a factor between
\(e^{-12\beta|\Gamma|}\) and 1. Integrate the remaining links first:
the claimed upper Haar-density bound follows, with exactly
\(12=2\times6\). Overcounting shared plaquettes only weakens it.
The cylinder bound follows from the already proved fixed-volume time
limit. The constant is uniform in volume at fixed beta and fixed support;
it is not uniform along a continuum sequence with growing beta/support.

### 7. Lemma M: HOLDS

SL 128–130. Each finite time extent differs from the cylinder by at most
\(2\|F\|s_k\) when \(T-w(F)\ge n_k\). The triangle inequality gives
4 for two such extents; an infinite extent contributes zero. Because
\(n_k\ge3\), the earlier requirement \(T-w(F)\ge2\) is satisfied.
This estimate is pointwise in the fixed observable, not uniform over
observables whose widths grow arbitrarily with k.

### 8. Lemma RPc: HOLDS

SL 132–134. Conditional on the shared spatial slice U(0), the cylinder
density splits into two factors. Haar inversion sends the negative-time
link \(g_{-t-1}\) to \((g_{-t-1})^{-1}\). For the reflected slab factor,

\[
 T_0(v,h^{-1}\!\cdot u)=T_0(h\!\cdot v,u)
                       =T_0(u,h\!\cdot v).
\]

Simultaneous covariance gives the first equality; symmetry gives the
second. The negative half therefore integrates to \(\overline{\psi_F}\),
the positive half to \(\psi_G\). Endpoint factors and normalization are
\(\lambda_0^{-2b}\Omega(U(-b))\Omega(U(b))\), so no square root of
Omega is missing. This proves site reflection positivity also for
non-invariant observables and width-zero observables.

### 9. Theorem L3(a): HOLDS

SL 140,154. There are countably many finite link sets, each with a compact
metric configuration space and a countable dense set of continuous tests.
A diagonal subsequence gives convergence on all continuous local tests.
For bounded Borel F on a fixed \(\Gamma\), approximate F in Haar L1 by
continuous tests. Lemma FE bounds every expectation error by
\(e^{12\beta|\Gamma|}\) times that L1 error. Thus the same subsequence
is Cauchy for every bounded Borel local test. There is no unjustified
diagonal extraction over an uncountable class. Fixed beta is essential to
this argument; it does not construct the continuum datum.

### 10. Theorem L3(b): HOLDS

SL 142,156. For a fixed width w, both admissible time sequences eventually
exceed \(n_{k_i}+w\). Lemma M then bounds their difference by
\(4\|F\|q^{2^{k_i}}/5041\to0\). Hence a convergent spatial subsequence
has the same limit for every admissible choice of time extents, including
the cylinders and symmetric tori. This does not assert convergence over
all spatial subsequences.

### 11. Theorem L3(c): HOLDS

SL 144,158. Linear positivity, normalization, the norm bound, and FE pass
through pointwise convergence. L3(b) supplies the symmetric-torus
representation, where every signed axis permutation preserves product
Haar measure and the Wilson action. This gives hypercubic invariance in
the limit. It also supplies the cylinder representation, where RPc
applies; positivity is closed under a scalar limit. Translations move site
mirrors, and axis permutations give all four directions. No O(4)
invariance at fixed lattice spacing is inferred.

### 12. Theorem L3(d): HOLDS

SL 146–150,160. Hold the two local functions and their separation fixed,
then take the symmetric-torus subsequence supplied by L3(b). Eventually
the widths plus d are at most \(n_k\). L2 gives the main term with
coefficient 1 plus \(6s_k\to0\), yielding exactly the stated coefficient
1 in the limit. Signed axis permutations supply each coordinate direction.
For supports in \([-r,r]^4\), the separation is at least
\(\|v\|_\infty-2r\), and
\(\|v\|_2\le2\|v\|_\infty\). Thus the displayed Euclidean rate
\(m_0/2\) and its onset are correct. This is not a proof of rate
\(m_0\) in every Euclidean direction.

### 13. Theorem L3(e): HOLDS

SL 152,162. The reflected form is positive by (c), symmetric under moving
a time translation between arguments, and bounded on translated local
functions by \(\|F\|^2\). These verify (P1)–(P3), not merely formal
reflection positivity. The quotient contraction is therefore defined.

Here is a separate spectral route to the gap, instead of the cited
log-convexity argument. For a centered local vector \(v=Q[F]\),

\[
 \|T_\nu^jv\|^2=u(F,F;2j)\le\|F\|^2e^{-2m_0j}.
\]

If its spectral measure for the bounded self-adjoint \(T_\nu\) gave
positive mass to \(|\lambda|\ge r>e^{-m_0}\), the left side would
be at least that mass times \(r^{2j}\), a contradiction as
\(j\to\infty\). Such spectral projections vanish on every centered
local vector, hence on their dense span and its closure. This proves
\(\|T_\nu|_{\Omega^\perp}\|\le e^{-m_0}\), all its power bounds,
and one-dimensionality of the invariant subspace. The vacuum is unique
up to scalar, as usual. The interval with both signs is correct: the
argument does not need positivity of the one-step reconstructed operator.

### 14. Section 4.4 and (U): HOLDS AFTER CORRECTION

The first unsupported inference is SL 166: “the time limit and the volume
limit can be taken in either order”. The proof of L3(b) requires
\(T_i-n_{k_i}\to\infty\); taking spatial volume to infinity at fixed
T fails that condition. L3 does not justify that reversed iterated limit.
Replace the sentence by:

> Time-first cylinder limits and admissible joint limits have the same
> cluster states as the symmetric tori along the same spatial subsequence.
> No interchange with a fixed-time spatial-volume limit is proved here.

The statements that (U) is not proved, and that a vacuum is unique within
each state rather than across states, hold. The other-side warning at
SL 172(2) is superseded by CR 213–221 (E' and S3', already available).
Correct it to: “(G) alone is indexed by dyadic cubes; E' and S3' extend
the seed conclusion to all sufficiently large integer cube sides.”
SL 172(3) explicitly leaves the DLR argument unwritten; no DLR theorem
is being claimed or supplied by this check.

### 15. Section 4.5, finite-torus spatial bound: HOLDS

SL 176–180. For \(FH,F,H\), changing the time extent to \(2n_k\)
costs respectively \(4s_k\|F\|\|H\|\),
\(4s_k\|F\|\), and \(4s_k\|H\|\). The difference of the products
of the means costs the sum of the last two after multiplying by the
other norm. Thus the total error is \(12s_k\|F\|\|H\|\).
The imposed product width \(w\le n_k\) ensures the symmetric torus
also meets Lemma M. Apply L2 after swapping the axes. This verifies
both 12 and 1.002 on the stated domain.

### 16. Proposition P(a): HOLDS; exact cutoff uniformity

SL 184–190,196. The sufficient data are one physical length unit, a
specified family \((\beta_\iota,a_\iota)\), and constants
\(0<s_*<1/5041\), \(0<\ell_*<\infty\), chosen independently of
\(\iota\). For **every** cutoff, one must supply an integer
\(n_\iota\ge3\) such that

\[
 S_{\beta_\iota}(n_\iota;(2n_\iota)^3)\le s_*,
 \qquad n_\iota a_\iota\le\ell_*.
\]

Then, uniformly in both \(\iota\) and the dyadic enlargement index k,

\[
 \frac{m(\beta_\iota,2^{k+1}n_\iota)}{a_\iota}
 \ge\frac{-\log(5041s_\iota)}{n_\iota a_\iota}
 \ge\frac{-\log(5041s_*)}{\ell_*}=M_*>0.
\]

This is a uniform **physical** gap. The lattice-unit lower bound is
\(M_*a_\iota\), and need not stay away from zero as \(a_\iota\to0\).
A seed for each cutoff with no quantitative margin or physical-size
control does not suffice. More generally, the exact sufficient rate
condition for this argument is
\(\inf_\iota[-\log(5041s_\iota)/(n_\iota a_\iota)]>0\);
the two common constants are one way to ensure it.
TR's finite-volume positivity, or a seed at one fixed beta, supplies
neither condition along a continuum trajectory. All integer cube sides
at least \(2n_\iota\) are also covered if the already existing CR S3'
is invoked explicitly. Cubes below that size are not covered by P(a).

### 17. Proposition P(b): HOLDS

SL 192,196. L3(d), \(m_0(\iota)\ge M_*a_\iota\), and
\(x=da_\iota\) give the stated inequality, with coefficient
\(\|F\|\|H\|\). It is a uniform coefficient only for uniformly
bounded chosen observables. As SL 198 correctly says, renormalized
fields need not satisfy that additional bound.

### 18. Proposition P(c): HOLDS

SL 194,196. For every nonnegative integer t, substitute the same rate
comparison into L3(e):
\(\|T_\nu^t\psi\|\le e^{-M_*ta_\iota}\|\psi\|\).
Unlike the sup-norm estimate, this is an operator estimate on the whole
centered reflected Hilbert space. No identification of Hilbert spaces
at different cutoffs is implicit in it.

### 19. Proposition P': HOLDS, including its positive-time formulation

SL 200–202. A small proof supplement is needed when H2 is assumed only
for positive times, as written here. The cited full H2 in
`gap-os-equiv.md:222` includes time zero; zero-time convergence is not
needed for this conclusion. Fix \(0<s<t\). Choose the even lattice
times \(s_j\to s\), \(t_j\to t\) supplied by positive-time H2.
P(c) and the semigroup law give

\[
 0\le u_j(F_j,F_j;t_j)
 \le e^{-M_*(t_j-s_j)}u_j(F_j,F_j;s_j).
\]

Taking limits yields the same comparison for \(u_\infty\). For any
fixed positive s this is an eventual exponential bound with finite
constant \(e^{M_*s}u_\infty(F,F;s)\). Apply the total-class result
(3), or the spectral argument in verdict 13. This gives the exact norm
bound with rate \(M_*\), a one-dimensional invariant subspace, and,
with (P4), \(\operatorname{spec}H\subset\{0\}\cup[M_*,\infty)\).
It does not rely on the incorrect zero-time-constant claim in (5d).

What remains missing for a continuum application is substantive:

1. (SEED-phys) on the actual cutoff/coupling trajectory, in fixed physical
   units, with the uniform constants of verdict 16.
2. A continuum reflected datum on the desired observable algebra, with
   (P1)–(P3), and (P4) for a Hamiltonian. Lattice hypercubic invariance
   alone does not establish continuum O(4) covariance or all OS axioms.
3. Correctly centered and renormalized lattice representatives whose
   diagonal reflected correlators converge at every positive physical
   time along the same cutoff sequence (H2).
4. Totality (TOT) in the claimed continuum Hilbert space. Totality in
   the scalar action-density sector proves a result only in that sector.
5. Nontriviality if a nonzero excited sector or a nontrivial Yang–Mills
   theory is claimed: a vacuum-only space also satisfies the gap bound.

The dyadic-side matching concern at SL 204(5) is already resolved at the
level of the spectral seed by CR E'/S3'; it must not be listed as a new
open supplier. One must still identify the constructed continuum state's
approximants. Neither divergent sup norms nor lack of convergence at time
zero defeats the positive-time argument above, but neither supplies H2.

### 20. The rate filter: HOLDS AFTER CORRECTION of its last sentence

SL 206. The inequalities themselves hold:

\[
 nm\ge-\log s>\log5041>8.5,
 \qquad m_0\le m-\frac{\log5041}{n}.
\]

For a hand check of the decimal constant, the series for log gives

\[
 \frac{693}{1000}<\log2
 <\frac{842}{1215}+\frac1{6804}<\frac{1733}{2500}.
\]

Here \(842/1215=2(1/3+1/81+1/1215)\); the remaining
\(2\sum_{j\ge3}3^{-2j-1}/(2j+1)\) is at most \(1/6804\).
Use \(x-x^2/2<\log(1+x)<x\) at \(x=7/64\). Since
\(\log71=6\log2+\log(71/64)\), these rational bounds give
\(4.26<\log71<4.27\), hence \(8.52<\log5041<8.54\).
All arithmetic is finite and displayed, not numerically evaluated.

In physical units the source's M must mean the true gap \(m/a\) of
the particular seed cube. Then \(\ell_*\ge na>8.5/M\), and
\(M_*\le m_0/a\le M-\log5041/(na)\le M-8.5/\ell_*\).

The last sentence should say:

> The explicit penalty \(\log5041/n\) tends to zero as n grows. The
> total difference between the true gap and the certified rate need not.

Indeed, if the seed value is exact, the total difference is

\[
 m-m_0=\frac{\log5041}{n}
       +\frac1n\log\!\sum_{j\ge1}e^{-n(E_j-m)}.
\]

The second, nonnegative state-count term is uncontrolled by this sentence.
For illustration of the distinction, a positive finite-rank spectrum with
\(2^n\) excited levels all at \(m=\log4\) has \(S(n)=2^{-n}\).
For \(n\ge13\) it satisfies the seed threshold, yet its certified rate
tends to \(\log2\), not \(\log4\). This is an abstract spectral
example, not a Wilson counterexample or a claim that it has the required
four-direction partition-function compatibility. It shows exactly which
unbounded state-count term the asserted reasoning leaves uncontrolled.

### 21. Proposition N1 and its interpretation: HOLDS

SL 212–216. Every excited level with \(E_j\le E\) contributes at
least \(e^{-aE}\) to S(a), including its multiplicity. Thus
\(N_L(E)\le e^{aE}S(a)\). At \(a=n_k\), (G1) gives
\(N_{L_k}(E)\le e^{n_k(E-m_0)}/5041\). The count is an integer,
so this excludes even E=m0, and in particular all levels below m0.
This is the already existing CR Theorem D(d), properly credited in SL.

### 22. Proposition N2: HOLDS

SL 218–224. The exact layer-cake identity is

\[
 \sum_j e^{-nE_j}
 =\sum_j\int_{E_j}^{\infty}ne^{-nE}\,dE
 =n\int_m^{\infty}N_{2n}(E)e^{-nE}\,dE.
\]

Tonelli applies to nonnegative functions, so it needs no prior integrable
majorant. With (NS), the last expression is at most
\(A e^{-(1-\theta)nm}/(1-\theta)\). This verifies the factor
\(1/(1-\theta)\), the strict threshold for the seed, and the need
for \(\theta<1\). The boundary case \(E_1=m\) causes no extra
term; it is already counted by the integral of the step function.

### 23. Corollary N3, the two-sided bound, and (NS-gap): HOLDS

SL 226–234. Choose \(\varepsilon>0\) below the strict liminf margin.
For arbitrarily large \(n\in I\),
\(\log A_n\le n((1-\theta)m-\varepsilon)\); N2 then gives
\(S(n)\le e^{-\varepsilon n}/(1-\theta)<1/5041\).
Theorem S propagates that seed. The lower bound in SL 230 is N1,
and the upper bound is N2 with
\(A=\sup_{E\ge m}N(E)e^{-\theta nE}\), allowing infinity.
The endpoint \(\theta=1\) supplied by a seed is not the sufficient
\(\theta<1\) assumption. No uniform-gap-to-seed converse for Wilson
is proved. (NS-gap) remains an explicitly proposed input.

The corrected trace-count remark at SL 236 also holds:
\(N(E)\le e^E S(1)\le e^{E+12\beta(2n)^3}\).
Thus \(\theta=1/n\) and \(\log A=96\beta n^3\), not theta=0.
At fixed beta its logarithmic prefactor divided by n grows quadratically,
so this bound cannot meet N3. The free-particle paragraph is marked GUIDE
in substance by its author; it is not a proof input and was not verified.

### 24. The second exact seed form: HOLDS

SL 238–242. CR Lemma X with a=n, b=2n and the other two sides fixed
at 2n gives

\[
 g(n,2n)=2n\kappa(n)-n\kappa(2n)+g(2n,n).
\]

Since \(0\le\kappa(2n)\le\kappa(n)\), the deficit difference
is nonnegative and at most \(2n\kappa(n)\). Strict monotonicity of
log identifies the seed threshold exactly with
\(g(n,2n)<\log(1+1/5041)\). A gap bound controls an excited
eigenvalue ratio; it does not by itself bound this ground-state deficit
or the full thermal sum of the shorter spatial box. The sentence is
correct as a statement of what these estimates do not supply.

### 25. CR Section 1, (TM), (TM-c), Lemma A(a,b), (LB): HOLDS

CR 31–45; TR 34–254, with its row-671 lead note. The transfer and slab
inputs used above are the existing results TR (1a–c), (2a–d), (3),
(4a–d), (5a–c), (6a–b), (8a–d); their domains and normalizations match.
On a rectangular slice, replace \(N^3\) by its three-side product.
The counts remain three spatial links and three spatial plaquettes per
site, and no transfer-kernel step uses equal side lengths. This supplies
the rectangular (TM) needed by the crossing argument. The temporal-gauge
remark repaired in row 671 is not used. TR (7) is not a premise of this
check; TR (8e) remains a cited extension theorem and is not used.

For (TM-c), the commuting center flip on the closing slice changes just
the corresponding temporal plaquette stack. Its term becomes
\(e^{-\beta(1+\operatorname{tr}U_p/2)}\), with the same constant
\(e^{-\beta}\); replacing beta by minus beta would be incorrect.
The twisted integral is positive and axis exchange interchanges mu,nu.
No flux estimate is needed downstream here.

For Lemma A(a), S=0 is immediate. Otherwise, if \(p<q\), put
\(A=(\sum_i\lambda_i^p)^{1/p}\).
Then \(\sum_i(\lambda_i/A)^q\le\sum_i(\lambda_i/A)^p=1\).
Also
\(\lambda_0\le(\sum_i\lambda_i^k)^{1/k}
\le\lambda_0^{1-1/k}(\operatorname{Tr}S)^{1/k}\).
These prove monotonicity and the limit in (a). For (b), sum
\(\lambda_i^{2k}\le\lambda_0^k\lambda_i^k\) and divide by the
positive trace. The stated S≠0 correction is required.

There are six plaquettes per four-dimensional site. Thus
\(-12\beta\le F(n)/|n|\le0\), and the coordinatewise trace-norm
monotonicity makes its infimum f finite. (LB), \(\Delta\ge0\), and
\(\Delta(\ldots,jn_\mu,\ldots)\le j\Delta(n)\) follow.
The final thermal inequalities in CR 45 are those proved in verdict 1.

### 26. CR Lemma K(a)–(d): HOLDS

CR 174–180. (a) is the trace-norm limit from Lemma A. Exchange the two
axes and apply it to the b direction to obtain (b), including
\(\ell=\inf_b e(b)/b\) and \(\kappa\ge0\). For (c),
Cauchy–Schwarz gives
\(W(a,b)^2\le W(a,b-1)W(a,b+1)\); take log, divide by a,
and let a grow. The corrected domain b≥4 keeps all three sizes ≥3.

For (d), a positive increment c of kappa would, by convexity, force
all subsequent increments to be at least c. Then
\(e(b)/b\ge\ell+c/2\) for all sufficiently large b. Choose b1
with \(e(b_1)/b_1<\ell+c/2\); (b) preserves this strict upper bound
at every multiple of b1, a contradiction. The argument also handles
the first increment from b=3 to 4. No differentiability in a box size
or passage through real-valued box sizes is assumed.

### 27. CR Lemma X: HOLDS

CR 182–184. Write the same log partition function in its two transfer
directions, subtract \(\ell ab\), and obtain
\(a\kappa(b)+g(a,b)=b\kappa(a)+g(b,a)\).
For a<b, \(g(b,a)\ge0\) and \(\kappa(a)\ge\kappa(b)\)
give \(g(a,b)\ge(b-a)\kappa(b)\). The sign of this inequality,
which is essential to every enlargement, is correct.

### 28. CR Lemma E: HOLDS

CR 188–190. Doubling b gives \(W(a,2b)\le W(a,b)^2\).
After extracting the leading eigenvalues, this says

\[
 g(a,2b)\le2g(a,b)+a(2\kappa(b)-\kappa(2b))
 \le\left(2+\frac{2a}{b-a}\right)g(a,b)
 =\frac{2b}{b-a}g(a,b).
\]

The second inequality uses both \(\kappa(2b)\ge0\) and Lemma X.
At a=b/2 the exponent is exactly 4.

### 29. CR Theorem S, including every downstream constant: HOLDS

CR 192–203. Three successive spatial doublings multiply the exponents:
\(4^3=64\). Doubling the time then squares the excited thermal sum.
Thus the exact one-step majorant is \(((1+s)^{64}-1)^2\).
For \(0\le x\le1/640\),

\[
 (1+x)^{64}-1\le64x e^{64x},\qquad
 e^{1/10}\le1+\frac1{10}+\frac{(1/10)^2}{2(1-1/10)}
 =\frac{199}{180},\qquad64\frac{199}{180}<71.
\]

The series bound uses \(k!\ge2\) for k≥2. Therefore the recursion
constant is \(71^2=5041\). Since \(1/5041<1/640\), the domain
is preserved. If \(x_k=S(n_k;(2n_k)^3)\), then
\(5041x_{k+1}\le(5041x_k)^2\), so
\(x_k\le q^{2^k}/5041\). Taking the logarithm of
\(e^{-n_km}\le x_k\) gives precisely (G3), with the extra positive
term recorded in verdict 1.

For the sufficient partition-function criterion, CR D(b), lines 92–104,
gives
\(1+s\le Z(n,2n,2n,2n)^2/Z((2n)^4)\le e^{\Phi(n)}\).
Three spatial trace inequalities give the exponent 8 before squaring,
so \(\Phi=16F(n^4)-F((2n)^4)\) has the correct factor 16.
At \(x=19/100000\),

\[
 e^x-1\le\frac{x}{1-x}=\frac{19}{99981}
 <\frac{191}{1000000}<\frac1{5041}.
\]

The last comparison is \(191\cdot5041=962831<1000000\);
the preceding one is \(19000000<19096371\). This verifies the
strict seed margin from the non-strict \(1.9\times10^{-4}\) input.

### 30. CR Corollary S2: HOLDS

CR 205. In two dimensions there is one spatial enlargement, so the
exponent is 4. For \(0\le x\le1/20\),
\(((1+x)^4-1)/x=4+6x+4x^2+x^3\le4+3/10+1/100+1/8000<4.32\)
(use its limiting value at x=0). Also
\(4.32^2=(108/25)^2=11664/625<19\).
The recursion is therefore \(x_{k+1}\le19x_k^2\), and
\(19x_0\le19/20<1\). The stated rate follows by the same
logarithm argument. Its application to a specific O(3) model remains
conditional on that model satisfying the stated transfer hypotheses.

### 31. CR Corollary S3: HOLDS AFTER CORRECTION already supplied in CR

CR 207–211. Its original proof first fails at CR 209: an arbitrary
integer L need not equal \(2^kb\) with integer \(2N\le b<4N\).
The supplied example N=3, L=13 is decisive: an odd L forces k=0,
but 13 is outside [6,12). The recursion for each actual pair (a,b)
with \(a\le b/2\) holds, since its exponent is at most 4.
Correct its proof-only conclusion to sides \(2^kb\); for every
integer side, use the existing E'/S3' below. This is the already recorded
row-699 correction, not a new finding or a reopened proof lane.

### 32. CR Lemma E': HOLDS

CR 213–215. Lemma A gives \(W(a,h)\le W(a,b)^{h/b}\) for
integer \(h\ge b>a\), even when h/b is not an integer. Consequently

\[
 g(a,h)\le\frac hb g(a,b)+\frac{ah}{b}\kappa(b)-a\kappa(h)
 \le\frac hb\left(1+\frac a{b-a}\right)g(a,b)
 =\frac h{b-a}g(a,b).
\]

Only \(\kappa(h)\ge0\) and Lemma X are used. This is the
non-dyadic interpolation missing from the old S3 argument.

### 33. CR Corollary S3': HOLDS

CR 217–221. Select the dyadic integer D with \(D\le L<2D\),
\(D=2^{k+1}N\). At time D/2 each of the three side enlargements
has exponent \(2L/D<4\). Thus the total exponent is below 64,
and the same estimate as in Theorem S gives

\[
 S(D/2;L^3)\le71s_k=\frac{q^{2^k}}{71},\qquad
 m(L^3)\ge\frac{-\log q}{N}+\frac{\log71}{2^kN}.
\]

This proves the stated common rate and the 71 denominator. It is prior
Codex/Astra work from row 699, adopted in the pinned CR source; no new
seed block is needed. The opposite assertion in CR 225 is stale.
The other rigorous numerical remark in CR 226 follows from
\(\log(1+1/5041)\ge1/5042>99/500000=1.98\times10^{-4}\).
The recalled photon/phase examples in CR 227 and the computational guides
in CR 230 are not inputs and are not verified here. An all-sector gap
bound is proved; the word “confinement” in CR 228 is not an additional
area-law or string-tension theorem.

### 34. Independent hand example: HOLDS, with a visible wrap-around term

This is an exact two-state test of the formulas, not an SU(2) seed.
Take spins \(\sigma=\pm1\), \(r=1/32\), and transition weights
\(P(\sigma,\sigma')=(1+r\sigma\sigma')/2\), equivalently
\(P=\frac1{64}\begin{pmatrix}33&31\\31&33\end{pmatrix}\).
Its two eigenvalues are 1,r. Choose n=3, T=6, and insert the spin at
opposite sites 0 and 3, so d=d'=3 and both widths vanish.

Compute the answer by expanding edge factors on the six-cycle, without
using the trace proof. Summing the spins kills any selected edge set
with an odd degree at any vertex. The only surviving sets in the
partition sum are the empty set and the full cycle, giving a factor
\(1+r^6\). With the two spin insertions, the only surviving sets are
the two length-three paths joining them, giving \(2r^3\). Global spin
flip makes each one-point function zero. Hence exactly

\[
 C_{6}(0,3)=\frac{2r^3}{1+r^6},\qquad
 r^3<C_{6}(0,3)<2r^3.
\]

In particular a bound that dropped the backward path and kept only
the cylinder term \(r^3\) would fail. L1 gives \(7r^3\), which
holds. The numerical seed is \(s=r^3=1/32768<1/5041\),
\(q=5041/32768\), and \(e^{-3m_0}=q\). L2 gives

\[
 C_6(0,3)<\frac2{32768}
 <\frac{5047}{32768}
 \le1.002\frac{5041}{32768}.
\]

The final comparison is \(5047000<5051082\). Thus normalization,
both arcs, and the downstream 5041/1.002 constants are hand-tested.
N2 is exact here with \(N(E)=1_{E\ge\log32}\), \(A=1\), theta=0.
For the independent unit check choose a=1/8 and ell*=3/8: then
\(M_*=(8/3)\log(32768/5041)\) and
\(e^{-M_*(3a)}=q\), as P(a–c) require. No script or numerical run
was used to obtain any value in this example.

### 35. Theorem L, numbered conclusion 1: HOLDS

SL 246–252. The seed is strictly positive for the stated Wilson model
at beta>0, by TR (5c). Verdict 29 supplies (G1),(G3); TR (4) supplies
simplicity. The sufficient Phi test and all constants have been derived
above. This is reuse of CR Theorem S, not a new proof of the seed.

### 36. Theorem L, numbered conclusion 2: HOLDS AFTER CORRECTION

SL 254–256. Both displayed estimates, the symmetric-torus four-direction
claim, and the cylinder estimate hold by verdicts 2–5 and 15. Correct
the final scope sentence to:

> This orientation controls the thermal error when d'≥n_k. If instead
> d≥n_k, exchange the two arcs. The seed supplies no corresponding small
> thermal bound here when both arcs are shorter than n_k.

This is already the distinction explained at SL 96; it does not change
either inequality.

### 37. Theorem L, numbered conclusion 3: HOLDS

SL 258–262. L3(a–e) proves the complete claim on every admitted cluster
state. “Depends on the k_i only” means the precise subsequence statement
L3(b), not that all spatial subsequences have one limit. The rate,
coefficient 1, hypercubic invariance, site positivity, and reflected
Hilbert-space gap all hold. A claim about every Gibbs state, every
aspect ratio, or uniqueness across cluster states is not part of it.

### 38. Theorem L, numbered conclusion 4: HOLDS

SL 264–288. Propositions P and P' give the stated conditional physical
rate and its limit transfer. “Every continuum limit” retains all of P':
the datum, positive-time convergence, totality, and time continuity for
the Hamiltonian. The open-list entries for other cube sides and the
compatibility concern must be read with CR E'/S3', as already noted.
No seed at coupling of order one, no continuum existence theorem, and
no status upgrade follow from any verdict in this report.

## Own-verdict checkpoint, before opening the Claude check

Verdicts 1–38 above were written before reading
`gap-seed-limit-check.md`. The saved version is
`/tmp/gap-limit-astra-bb010c237/verdicts-before-claude-check.md`, SHA-256
`a2800c23cde06036e68d87fa3f5aad6e7428cdeadb737081ae239af995d91c23`.
That hash records reading order, not mathematical evidence. The core
conditional implication holds. The new corrections concern scope at
SL 166, 206's last sentence, and 256; the non-dyadic repair was already
present in CR. No constant in the core theorem needs replacement.

## Comparison with the earlier Claude check, read afterwards

Only after the checkpoint above, I read all 227 lines of
`gap-seed-limit-check.md` (Claude Opus 5.5, high, row 703). Call it CK.
The original author of SL is Claude Fable 5.2, medium. The agreements
are A1–A8, A10's conclusions, A12–A13, and the displayed estimates in
A14. CK A12's theta=1/n repair is correct and already applied at SL 236.
CK's different numerical example uses the spectral trace expansion;
verdict 34 was derived first by the edge-subset expansion instead.

### C1. CK A9, line 74: the limit-order sentence needs correction

CK says Section 4.4 correctly states what was proved. That is too broad
for SL 166's “either order” sentence. CK's own A8(b), line 64, uses the
admissibility condition that fails for fixed T and growing spatial
volume. **The correction in verdict 14 is right**; the restricted L3(b)
claim, accepted by both checks, remains right. This is a missing
justification for the wider limit order, not a counterexample to Wilson
limit commutation.

### C2. CK A11, lines 84–86 and table line 218: qualify “the loss”

CK's inequalities and its interpretation of the physical M at line 86
are right. Its blanket HOLDS does not qualify SL 206's final sentence.
**Verdict 20's correction is right**: the displayed constant penalty
tends to zero; the total loss also contains the explicitly displayed
state-count term. No claim about the actual Wilson state count is
refuted. The source must name which loss it means.

### C3. CK A14, line 104 and table line 221: retain the exchanged orientation

The accepted inequalities are right, but SL 256's unqualified no-bound
sentence is not. For example n_k=3, d=4, d'=2 on a width-zero symmetric
torus has d'<n_k, yet the exchanged L2 bound applies with forward gap 2
and backward gap 4. **Verdict 36's wording is right** and agrees with
SL 96 and CK A3, line 38. This changes scope wording, not a constant.

### C4. CK A10, line 82: same verdict; an extra positive-time argument

CK treats P' as a direct instance of (5a–c). The full H2 it cites
includes zero, whereas SL 200 asks for positive times only. **P' is
right**, but its proof on the stated weaker hypothesis needs the
positive-anchor argument in verdict 19. Thus there is no disagreement
about its conclusion; the disagreement is with the unqualified direct
application. One should not strengthen P' by adding zero-time norm
convergence, which is unnecessary.

### C5. CK A15, lines 120 and 130: exact saturation is false

This disagreement was found after reading CK, not used for my earlier
verdicts. Its identities at g→1 are right:
\(S_T=(1+x)^N-1\), \(\alpha=\gamma=(1-x)^N-1\).
But the bound B at CK 118 replaces \(|\alpha|,|\gamma|\) by S_T.
For N=2 and x=1/4,

\[
 S_T=\frac9{16},\qquad |\alpha|=|\gamma|=\frac7{16}.
\]

Thus these thermal estimates are not attained exactly. Also the
\(S_TN_{\rm tr}/(1+S_T)^2\) contribution, with
\(N_{\rm tr}=1+S_T\), in the centered formula is
\(S_T/(1+S_T)<S_T\) at this endpoint. **CK's exact-saturation claim
is wrong**. The appropriate correction is “the corresponding estimates
can agree to leading order in the subsequent small-Nx limit”; the
finite positive-x claim must be removed. This does not challenge L1.

### C6. CK A15, line 126: the equal-arc comparison omits a term

Again this is a post-reading check of CK's example. Put
\(\varepsilon=\rho^d=\rho^{d'}\to0\), with N rings,
\(N\varepsilon\to y>0\) and \(N(1-g^2)\to z\ge0\).
Its own exact formula at CK 116 factors as

\[
 \Delta=g^{2N}\left[
 \left(1+\frac{1-g^2}{g^2}\frac{2\varepsilon}{1+\varepsilon^2}\right)^N
 -\left(\frac{1-\varepsilon^2}{1+\varepsilon^2}\right)^{2N}
 \right].
\]

The logarithms of the two powered factors are
\(2z\varepsilon+o(\varepsilon)\)
and \(-4y\varepsilon+o(\varepsilon)\), respectively, while
\(g^{2N}\to e^{-z}\). From CK 118,
\(B/\varepsilon\to e^y+1+3y\). Therefore the correct limit is

\[
 \frac\Delta B\longrightarrow
 \frac{e^{-z}(2z+4y)}{e^y+1+3y}.
\]

It is not always at most \(4y/(e^y+1+3y)\), as CK 126 asserts.
Take y=1/4 and z=1/2. The ratio is
\(2e^{-1/2}/(e^{1/4}+7/4)\), strictly greater than CK's
\(1/(e^{1/4}+7/4)\), since \(e^{1/2}<2\).
For an explicit valid sequence choose d=d'=2,
\(\rho=(4N)^{-1/2}\) and \(g^2=1-1/(2N)\); the original
positive two-state matrices exist for every N≥1 and T=4.

Maximization over z gives the corrected numerator
\(2e^{2y-1}\) for \(0<y<1/2\), and \(4y\) for \(y\ge1/2\).
**This correction is right; the pointwise comparison at CK 126 is
wrong.** It does not refute L1 or the global rounded 0.61 upper bound.
For y<1/2 the corrected branch increases to
\(2/(e^{1/2}+5/2)<1/2\); thus it does not overturn the larger-y
branch used for that global estimate. No optimization run was made.

### Part B comparison: no further mathematical disagreement

CK B1–B2, lines 134–151, are the already existing CR E'/S3' and their
immediate thermal and gap consequences. They agree with verdicts 32–33.
In B3's Lemma V, lines 155–163, three side enlargements give exactly
\((L/a)^3\). Rounding a downward to a dyadic \(a_i\in(a/2,a]\)
costs at most \(2^3=8\) and changes the exponential to
\(e^{-m_0a/2}\). Convexity gives \(e^X-1\le(e-1)X\le2X\) on
[0,1]. Thus the stated V bounds hold. The threshold
\((6/m_0)\log L\) comes from cancelling \(L^3\) against
\(e^{-m_0a/2}\), since \(3\times2=6\); the remaining factor
\(8/(5041a^3)\) is below 1 for a≥N≥3.

The B4 constants, lines 180–194, also hold:
\(1+6/71<1.085\), because \(6000<6035\);
the one-point comparison still costs two errors of size 2;
the spatial covariance comparison still costs three errors of size 4.
The relaxed time condition makes X tend to zero, while the longer-time
range follows directly from (G-all). Hence B4's all-side port and B5's
removal of dyadic compatibility are correct, with their stated time
admissibility. The comments about the rate filter and the unqualified
no-bound sentence inherit C2 and C3; they are not additional defects.

These are all disagreements found in the 227-line check. Its principal
conditional theorem conclusions survive; its numerical-example comments
at CK 120 and 126 need the explicit corrections above.

## Result and limits

The seed-to-lattice-gap and seed-to-every-admitted-limit implications
hold, with the scope corrections at SL 166, 206, and 256. No downstream
constant changes. P(a) requires a uniform seed margin and physical-size
control, or, more generally, a positive lower bound on
\(-\log(5041s_\iota)/(n_\iota a_\iota)\). P' additionally needs
the continuum datum, positive-time convergence and totality; time
continuity gives its Hamiltonian formulation. None of those physical
existence/seed inputs is supplied here. No gap at coupling of order one
is claimed. No scientific status is changed.

Only this report is a repository output. All mathematical checks and
examples were by hand; scripts were used only for retrieval, hashes,
file writing and mechanical consistency checks. No numeric proof run,
audit, source repair, public post, or Balaban-paper import was performed.

Mechanical verification: verdict headings 1–38 and comparison headings
C1–C6 are present once; display delimiters are balanced; SL, CR, TR,
`gap-os-equiv.md`, and CK remain byte-identical to the pinned commit.
Their hashes are saved in
`/tmp/gap-limit-astra-bb010c237/input-hashes.json`.
The sole new file is this report, on local branch
`research/gap-limit-astra-bb010c237`; it is uncommitted and unpushed.
