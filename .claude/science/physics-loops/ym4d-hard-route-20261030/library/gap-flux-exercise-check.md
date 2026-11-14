# Repo search

The target-specific prior note `prior/gap-flux-check-astra.md` is absent.
The lead's `prior/repo-search-2026-11-08.md` concerns earlier RG targets.
Its closest hit is the soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md`,
lines 106–149: a positive one-step plaquette witness, not an even-sector
seed or a periodic/even comparison. I read that source on PR 10114.
The November 8 search does not certify novelty for row 731.

I searched main and the requested PR heads independently. The closest
additional hit is `MIXGFF.md:441–483` on PRs 10114 and 10133:
the mixture-variance method is already there, but not EV-L's twist
mixture, finite-torus bound or seed consequence. Main's centre-even
character-weight note concerns a different operator. No duplicate of
the four precise new contributions was found in these searches.
Exact revisions, queries, full matches and fetch logs are in
`/tmp/ym4d-gap-flux-check-kad0aox0/`; section 6 records the limits.
The registry has no matching owner for this check. The SU(2) inequality
(KP) remains row 733's task; I do not attempt it.

## Provenance and scope

Codex, configured GPT-6 Astra / max, FINISH row 732, 2026-11-11.
Research check of `gap-flux-exercise.md` at
`d56f924eefc64e80e85fda70a3b6b90771686cb6`; not an audit; grants no status.
Author: Claude Fable 5.2 / high, row 731. Only this output file is edited.
All source line numbers below refer to the pinned checkout unless a ref
or external source is stated. Paths without a prefix are in `library/`.

**Finding:** all 20 requested named statements HOLD on their stated domains.
There is no failure of Theorem EV-L (c) or (d).
Its proof uses only the periodic operator and electric twists.
The magnetic-twist construction is checked separately below.
The general admissibility sentence at source line 159 needs correction;
the classification and the small-seed argument supply the properties
that sentence asserts too early. No numerical run discharges any step.

**Checkpoint:** the requested proof checks and novelty comparison are complete.
The three corrections in section 7 concern surrounding assertions, not
a failed named theorem. No seed, (EV-STEP), or SU(2) (KP) is supplied.

## 1. The even-sector limit

### Lemma CB — HOLDS (426–428)

Use the endpoint convention for spatial width in `gap-seed-limit.md:46`.
A support contained in an interval of width at most L−2 uses at most
L−2 starting positions of nu-oriented links. Choose an unused position
r different from 0. Set z(t,x)=−1 for 1≤x_nu≤r in cyclic order,
at **every** time of the slab, and +1 elsewhere.
Then z(x)z(x+nu) is −1 exactly at cuts 0 and r.
For another spatial direction it is +1. For a temporal link it is
z(t,x)z(t+1,x)=+1. Thus temporal links, including the slab's first
and last temporal layers, really are unchanged.

On the support, this gauge transformation equals the cut-0 centre flip.
The other cut is unread. Haar invariance and simultaneous flip invariance
of the slab weights give the asserted kernel identity. At width zero
the same argument applies directly to the multiplier F.
Kernel conjugation then gives C_nu k_F C_nu=k_F.
The use of g for both temporal links and a gauge transformation in the
source is harmless after calling the latter z.

### Lemma MX — HOLDS (436–441)

Positivity here is positivity of a kernel integral, **not** operator
positivity of C^e. Write a_t for the kernel of T_P^t.
For positive slab width and F≥0, the numerator before normalization is

\[
 \iint K_F(Z^e u,v)a_{T-w}(v,u)\,du\,dv\ge0.
\]

At width zero use instead
\(\int F(Z^e u)a_T(Z^e u,u)\,du\ge0\).
Splitting a_T into two kernels justifies this diagonal formula by A0(e).
Strict positivity of a_T gives a positive denominator for every e.
In a common eigenbasis, the signs of C^e are ±1; hence
\(0<\operatorname{Tr}(C^eT_P^T)\le\operatorname{Tr}(T_P^T)\).
There are eight e's, so q_0≥1/8.

Padding a slab by p and q slices replaces k_F by Rn^p k_F Rn^q.
Cyclic trace and [C^e,Rn]=0 remove the padding. Two containing slabs
on the same lift can also be compared through the minimal support slab.
Translating the observable and its slab together leaves their kernel
unchanged. This supplies exactly the consistency and time invariance
used in the average X. Linearity and positivity are used on functions
whose combined support still meets the stated spatial width condition;
the time translates in X have the same spatial support.

Expanding P_0 proves (c). For (d), positivity gives
\(\omega_{\rm per}(X)^2\le\omega_{\rm per}(X^2)\), while
\(\omega_{\rm ev}(X^2)\ge q_0\omega_{\rm per}(X^2)\).
No positivity of the signed operator C^e is inferred.

### Lemma L1-ev — HOLDS (443–447)

Restrict the trace expansion of `gap-seed-limit.md:56–76` to the range
of P_0. CB permits this restriction on both sides of each insertion.
The norm bound K1 is unchanged. For unit-norm observables, put
\(\sigma=S_{\rm ev}(d')\) and \(r=e^{-m_{\rm ev}d}\).
The four trace terms and the one-point errors give

\[
 |\operatorname{Cov}_{\rm ev}(F,H)|
 \le r(1+\sigma)+4\sigma+\sigma^2.
\]

For σ≤1 this is at most r+6σ; for σ>1 positivity bounds the
covariance by 2. The one-point error is at most
\(2\|F\|S_{\rm ev}(T-w(F))\).
There is **no requirement d≤d'**. The wrap-around term is absorbed
in S_ev(d'), even when d is the larger gap.

### Theorem EV-L (c) — HOLDS (449–461)

For r=l−j≥1, translate the pair so that its ranges are [0,w] and
[rδ,rδ+w]. The two free intervals have lengths

\[
 d=r\delta-w\ge r,\qquad
 d'=T-r\delta-w\ge T-N\delta+1.
\]

Both widths are counted: d+d'+2w=T. There are exactly 2(N−r)
ordered pairs at distance r, and N diagonal pairs. With
c=ω_ev(A), X=N^−1∑_j(τ_{jδ}A−c), the diagonal variance is
at most \(\|A\|^2\), and

\[
 \omega_{\rm ev}(X^2)\le\|A\|^2\left[
 \frac1N+\frac2{N^2}\sum_{r=1}^{N-1}(N-r)e^{-m_{\rm ev}r}
 +6\frac{N-1}{N}S_{\rm ev}(T-N\delta)\right].
\]

Bound N−r by N and sum the geometric series. MX(d) multiplies
this variance by 8 before taking the square root. This is exactly (c).
For N=1 the off-diagonal sum is empty, so that case also holds.
Hand check at T=17, w=2, δ=3, N=5: the outermost pair has
d=10, d'=3 and d+d'+2w=17. The stated lower bound on d' is 3.

### Theorem EV-L (d) — HOLDS (453–463)

For fixed F take δ=w(F)+1 and
\(N_i=\lfloor(L_i-n_i-2)/\delta\rfloor\).
Eventually N_i≥1, N_i→∞, N_iδ≤L_i−2, and
L_i−N_iδ≥n_i+2. Thus (c)'s two errors tend to zero.
Also L_i−w(F)≥n_i eventually, so the even/cylinder difference
tends to zero. This compares the three sequences on the **same**
subsequence, rather than asserting uniqueness across subsequences.

On the cylinder the two vectors made by F and H are centre even
by CB. Removing the vacuum leaves norm at most e^−m_ev d.
Pass to the common local limit. Exchange an axis with time on each
periodic cube to obtain the other three directions. The fixed-beta
finite-energy bound and diagonal extraction in
`gap-seed-limit.md:124–126,154` justify bounded Borel test limits.
That compactness argument does not need the stronger whole-space (G).

Consequently no checked statement above takes down EV-L, Corollary EV,
or their lattice limit conclusion. A cutoff-uniform physical gap still
needs the scaling hypotheses and limiting reflection datum; this check
does not establish a seed at any new coupling.

## 2. Twists and classification

### The input (TM-tw), including Pf(k)=1 — HOLDS

The earlier supply is `gap-seed-check.md:30–40,177` and
`gap-crux-fp-check.md:30–38`. Here is the intersection check from the
actual kernel, rather than an appeal to either earlier verdict.
For magnetic m set

\[
 V_m(u)=\beta\sum_{p\ {m spatial}}(1-s_p^m\operatorname{tr}u_p/2),
 \quad M_m=e^{-V_m/2},\quad T_m=P M_m C_{\mathcal E}M_m P.
\]

The potential is continuous, gauge invariant, and between 0 and
6β|B|. The temporal convolution is the same positive trace-class
operator as in `gap-transfer.md:148–166`. Sandwiching and projecting
preserve these properties. Its gauge-averaged kernel is strictly positive.
The finite-volume positive-kernel argument therefore gives a simple top
eigenvalue and a strictly positive eigenfunction for **each** T_m.

Every spatial plaquette contains zero or two links of a centre cut.
Its holonomy, and hence its signed term in V_m, is unchanged.
This remains true when that plaquette belongs to a magnetic stack.
Consequently C^e commutes with M_m, the convolution and P.
In the trace integral, replace the seam's closing spatial slice u by Z^e u.
Only the temporal plaquettes on the electric stacks acquire minus signs.
The spatial half-potentials on both sides of that seam still combine
to V_m(u), since V_m(Z^e u)=V_m(u). Thus

\[
 \operatorname{Tr}(T_m^a C^e)=Z^{e+m}(a,B).
\]

For the decisive example k_12=k_34=1, the 34-stack remains in V_m
and the seam changes only 12-plaquettes. Their intersection creates
neither an additional factor nor a change in the temporal convolution.
The same plaquette-by-plaquette argument covers every e,m, not only
this example. Moving a stack is a centre-link change of variables
whose coboundary changes that plane alone; other signed stacks survive.
Axis permutation then gives the required covariance.

This establishes the operator for the signed-plaquette definition in
source line 111. No continuum bundle construction or flat twist-eater
configuration is assumed.

### Lemma CL1 — HOLDS (477–479)

Fourier inversion in e_3,e_4 contributes 1/4. After the exchange
of axes, its exponent is
χ_3 μ_4+χ_4 μ_3+m_3 ψ_4+m_4 ψ_3=B(x,y).
The Fourier transform in e_2 is invertible and tau fixes that coordinate
and m_2. This proves the equivalence separately on each of the four
(χ_2,m_2) slices, with exactly the stated normalization.

### Proposition CL (a) — HOLDS (481–487)

At the zero slice, G(0)=1 implies ∑G=4. Nonnegativity of G gives
G(x)≤1 through its Fourier formula. Admissibility therefore forces
G to be an indicator. If x is in its support L, all four Fourier
signs on L must be +1. Hence L⊂L^⊥. The sum of two elements
has all four signs +1 too, so it belongs to L. Thus L is an
isotropic subgroup of order four. In particular it cannot be {0}.

### Proposition CL (b) — HOLDS (483–491)

The two delicate steps follow without enumeration.
Let A be the set of single-coordinate pairs allowed by the support.
Permutation of spatial axes makes this the same A on each axis.
CL1 at zero says that a nonnegative slice vanishes if its zero value
vanishes. Thus every supported sector has all three coordinate pairs
in A.

In the zero slice, the intersection of L with either coordinate plane
is exactly an embedded copy of A. Therefore A is a subgroup of
F_2². Also L⊂A×A and |L|=4, so |A|≥2. If |A|=4,
both different coordinate planes would equal L, an impossibility.
Hence A={0,α}; the embedded copies generate A×A=L.

For the nonzero slice α, its zero value is 1: permute its sole α
coordinate into the already determined zero slice. The argument in
(a) applies again, and its support has four elements inside A×A.
It therefore equals A×A, with values 1. Every other slice vanishes.
Thus the complete support is A³, not merely a subset of A³.
The three nonzero α give exactly the three stated sets.
Inverse Fourier transformation gives δ_k0, 1/8 and (−1)^Pf(k)/8.
The three complementary plane pairings are permuted by every axis
permutation, proving the converse too.

## 3. The three seeds

### Lemma W — HOLDS, all four parts (503–505)

The classification supplies **indicator** coefficients, so the operator
in (b) is an ordinary finite direct sum. The zero extension on unused
sectors adds only zero eigenvalues. Positivity and trace class follow
from the commuting projections. Axis symmetry gives (a).
Part (c) follows from (S3), verified below: the periodic even vacuum
is present and no magnetic block has a larger eigenvalue.
Part (c) does not assert simplicity of the whole direct sum.

For (d), there are 6abcd plaquettes and each weight is at least
e^−2β. Thus Z≥e^−12βabcd, λ_0(b,c,d)≥e^−12βbcd,
and W_w(a,b,c,d)≥λ_0(b,c,d)^a. This proves the bound on ell.
No positive lower bound for a signed sum is being guessed.

### Theorem S-w — HOLDS (507–513)

An initially degenerate largest eigenvalue causes no gap in this proof.
List eigenvalues with multiplicity and remove **one** copy of λ_0.
Then S_w(t)=∑_j r_j^t with 0≤r_j≤1, including any remaining
copies r_j=1. It is nonnegative, decreasing, and
S_w(t+u)≤S_w(t)S_w(u), whether or not the top is simple.
The trace limit, convexity, crossing and enlargement proofs in
`gap-crux-restate.md:174–219` require no simplicity.
Only after their bound S_w(t)<1 is obtained does it exclude every
extra copy of λ_0. A nonzero excited eigenvalue r then satisfies
r^t≤S_w(t), giving the stated gap.

Constants, checked by hand: three spatial enlargements give exponent
4³=64. For 0≤x≤1/640,

\[
 (1+x)^{64}-1\le64x e^{64x}\le64x e^{1/10}\le71x.
\]

Indeed \(e^{1/10}\le1+1/10+\tfrac12\sum_{n\ge2}10^{-n}
=199/180<71/64\). Thus the squaring recursion has constant
71²=5041 and gives s_k≤q^(2^k)/5041. For D≤L<2D, each
interpolation exponent is 2L/D<4; three uses give exponent at most
64 and S_w(D/2;L³)≤71s_k≤q^(2^k)/71. Dividing the logarithm
by D/2=2^kN yields at least log(1/q)/N.
For instance N=3,L=13 uses D=12 and exponent 13/6 on each side;
no false representation L=2^k b with integral b is used.

The pressure-defect bound also needs no simple top. The n-th power
of the norm is bounded by the time-n trace, and the time-2n trace is bounded by
λ_0^n times the time-n trace. Applied to the cube of side 2n,
these give 1+S_w(n;(2n)³)≤W_w(n,(2n)³)²/W_w((2n)^4).
Crossing and trace-power inequalities give
W_w(n,(2n)³)≤W_w(n^4)^8. This proves the asserted Phi_w bound.
Finally, for x=19/100000,
e^x−1≤x/(1−x)=19/99981<1/5041, since 19·5041=95779<99981.
The printed threshold 1.9×10^−4 is safe.

### Corollary EV — HOLDS (515–517)

The even block occurs once, and all other sector traces are nonnegative.
Hence S_ev≤S_w. The bound below 1 makes the selected top simple,
and its excited-space gap bounds the even gap from below.
Choose n_i=D_i/2. Then n_i≤L_i/2,
S_ev(n_i;L_i³)≤q^(2^k)/71→0, and the common m_0 is positive.
These are precisely EV-L(d)'s hypotheses. The conclusion applies to
every sequence of sides, because S3' covers every integer L≥2N.

## 4. Crossing of the even trace

### Proposition X16 — HOLDS (527–531)

The three original electric bits become one electric bit and two
magnetic bits. Summing the electric bit inserts 1+C=2P_+;
combining this factor 2 with the original 1/8 gives 1/4.
There are four magnetic choices and four electric characters satisfying
χ_2=0 in each. Thus there are sixteen sectors, exactly X.
The symbols C_1 in line 151 and C_2 in line 531 label the same
crossed first spatial direction under the two axis conventions.

### Corollary SR — HOLDS as the exact sum rule (533)

At a=b the crossed box is the original box. X16 says
\(\sum_{x\in X}Z_x=4Z_{0,0}\). Removing the one even term
gives \(\sum_{x\ne0}Z_x=3Z_{0,0}\).
The fifteen relative weights have mean 1/5. This finite-time weight
identity alone is not an individual energy-gap estimate. Read the
source's qualitative “light or heavy” sentence only in that weight sense.

### Proposition EVL — HOLDS (535–539)

For each positive sector operator, Tr(A²)≤(Tr A)². X16 therefore
gives Z_ev(a;2b,c,d)≤(1/4)∑_x y_x². The square of its
time-b sum is (∑y_x)²/16, so the ratio is exactly Theta,
with no missing factor four. Cauchy–Schwarz on sixteen entries gives
1/4≤Theta≤4. The denominator is positive because X contains
the periodic even vacuum.

Normalization produces exp[a(2κ(b)−κ(2b))]. Keeping only the
even crossed sector gives Z_ev(a;b,c,d)≥λ_0(a,c,d)^b/4;
κ(a)≥κ(b) then yields the stated log 4 loss. At a=b/2,
κ(b)≤(g_ev+log 4)/a and κ(2b)≥0 give the displayed
64(1+S_ev)^4 bound. It is a bound, not a no-go theorem
against all possible inequalities derived using crossing.

### Proposition AS — HOLDS (543–549)

On a periodic Z_2 plane the product of all plaquette holonomies is +1.
A twisted stack makes the signed product −1 in each parallel slice.
There are N_mu,nu such slices, with distinct plaquettes, so every
configuration has Boltzmann weight at most exp(−2βN_mu,nu).
For a single-plane twist the all-plus link configuration attains
this plaquette cost and has normalized measure 2^−E.

On (a,b,c,c), every nonzero electric twist has Z^e≤exp(−2βbc).
On the exchanged torus, the single 13 twist contributes at least
2^−E exp(−2βac). The zero-twist terms agree. The hypothesis
makes the latter contribution exceed the seven former upper bounds.
For an explicit hand choice take a=3,b=4,c=5, E=1200, β=121:
2β(b−a)c=1210>1200 log 2+log 7, using log 2<1 and log 7<2.
No enumeration or numerical value of a partition function is used.
This refutes symmetry in the stated Z_2 class, not specifically SU(2).

## 5. Sector order and surface classes

### (S1) — HOLDS (131)

Fourier inversion gives
\(Z_{0,m}-Z_{\chi,m}=\tfrac18\sum_e(1-\chi(e))Z^{e+m}\ge0\).
The summands use positive partition integrals even when Pf(e+m)=1.

### (S2) — HOLDS (132)

In any frame, Tr(T_m^a C^e)≤Tr(T_m^a), by the simultaneous
spectral decomposition. First remove planes 12,13,14; in frame 2
remove 23,24; in frame 3 remove 34. What remains is k=0.
This proves Z^k≤Z^0 for all 64 twists, including nonzero Pfaffian.

### (S3) — HOLDS (133)

Take a-th roots of Z^m(a,B)≤Z^0(a,B) and let a→∞.
For a positive trace-class operator A, writing its eigenvalues as
λr_j gives \(1\le\sum r_j^a\le\sum r_j^3<\infty\) for a≥3;
the a-th root of this factor tends to 1. Thus λ_m≤λ_0.
The positive top eigenfunction of T_m is fixed by every C_nu:
each flip produces another positive normalized top eigenfunction,
and simplicity for that individual block makes them equal.

### Lemma GS — HOLDS (601–607)

For one complementary pair, sum first over y:

\[
 \sum_{x,y\in\mathbb F_2}(-1)^{xy+ux+vy}
 =2(-1)^{uv}.
\]

There are three independent pairs, so the six-bit Fourier sum is
8(−1)^Pf(h). Inserting it in W_kappa proves all three formulas.
At h=0 the sum is 8; combining this with 64 total elements gives
36 zero-Pfaffian and 28 unit-Pfaffian classes. Consequently
W_per−W_kappa=2∑_{Pf(h)=1}Y_h, with the stated sign and factor.

### Proposition KP-Z2 — HOLDS (609–611)

Expand each plaquette factor as e^−β(cosh β+s_p σ_p sinh β).
Independent normalized link summation kills precisely those selected
plaquette sets with an odd incidence at some link. Every surviving
set has positive weight and the twist sign (−1)^〈k,h(S)〉.
Fourier orthogonality selects its class, so every Y_h≥0.
GS then gives |W_kappa|≤∑_h Y_h=W_per.
This proves the two asserted bounds for β>0. It proves no sign
condition for the SU(2) character-integral weights.

## 6. Step 5: prior work and the four new marks

Searches used every tracked Markdown and TeX path on each ref, excluding
this hard-route folder; the pinned folder was searched separately.
The first pass used the labels and `centre-even`, `center-even`,
`zero-flux`, `Pfaffian`, `Pontryagin`, `dyonic`. The second used
electric/magnetic flux, twist sums, sector crossing, mixtures and
Cesaro/Cesàro averaging. A narrower follow-up removed false matches
such as “center event”. Complete matches are on disk; truncated
discovery output was not used to claim absence.

| Search ref | Commit |
|---|---|
| origin/main | a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc |
| PR 10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| PR 10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| PR 10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| PR 10141 | fb99b4dddc7254e6124ac124887d58eeb3a77802 |
| PR 10144, additional FINISH requirement | 1f20846b8057f6346ebab6c0dbebdabbd9e472a4 |

PR 10144's old local tracking ref rejected a non-fast-forward fetch.
I fetched its current head into `origin/pr/10144-gap-flux-check` and
searched that revision instead; no force update or remote mutation occurred.
The log directory was initially created by macOS's default temporary
directory setting, then moved to the `/tmp` path above. Repository
searches ran only in this checkout; no source search used that directory.

In the next table, **S/** means
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
**R/** means `research/ym4d/` on PR 10141.

| Primary hit read | Closeness and disposition |
|---|---|
| S/MIXGFF.md:413–483, PR 10114 | Its variance identity (18) forces equality of component expectations from a clustering barycenter. Reuse and credit this method; it has no twist-sector weights, q_0≥1/8, or finite-volume rate. |
| S/NGYM.md:883–934, PR 10114 | Requires a Cesaro-decay input for mixture exclusion and explicitly infers no exponential decay or mass gap. A related open consumer, not EV-L. |
| R/library/ph1.md:306–332 | A uniform polynomial plateau bound makes limits of ergodic states ergodic. Related averaging method; no comparison of periodic and even states. |
| S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–10,106–149, PR 10114 | Positive one-step plaquette witness and a separately stated small-beta endpoint. Neither the even-sector limit argument nor the three-seed classification. This is the relevant lead-search hit. |
| `.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md:3194–3212`, PR 10114 | WC-tor is an open conditional covariance estimate over toron variables. Its “sector” is not a centre-flux sector. |
| `docs/THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md:79–106,230–241`, main | Centre-even integer spins in a class-weight Fourier expansion. Different carrier and no six-twist Pfaffian sum or sector-seed classification. |
| `docs/THOOFT_1981_DUAL_SUPERCONDUCTOR_CENTER_VORTEX_CONFINEMENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md:20–32,90–121`, main | Explicitly a vocabulary/bibliography record, with confinement conditional on condensation. It does not supply any checked statement here. |

The primary S/ sources used from PR 10114 also occur in PR 10133;
their matching content was checked by blob identity. Shared snapshots
are not independent proofs. Other broad matches concerned Grassmann
Pfaffians, spin ice, finite clocks, RG action bounds or rotation-flux
currents. These are search exclusions, not full reviews of those topics.

Local sources read directly confirm the reuse entries of Step 5:
`gap-zero-transport.md:34–44` supplies the spatial-loop commutator,
electric-twist projection and even thermal sum;
`gap-mid-max.md:219–234` supplies Identity FL and the crossing sketch;
`gap-crux-fp.md:108–124` supplies the assumption split and full twist sum;
`gap-skeleton-max-b.md:254,362–375` already asserts an even-sector
limit consequence in a different conditional argument.
The two earlier twisted-operator checks were read at the ranges named
by the brief. None is relabelled as a new construction by row 731.

| New-mark group in Step 5 | Verdict on the novelty description |
|---|---|
| EV-L(c),(d), line 260 | **HOLDS AFTER CORRECTION:** the explicit finite-torus domination/variance bound and its periodic-limit application were not found earlier. The mixture-variance mechanism itself is prior work in MIXGFF; the qualitative even-limit claim already appears in max-b:375. Credit both. |
| Kappa set and its Theorem S, lines 264,267 | **HOLDS within the recorded repository search.** No earlier signed six-twist seed or application of Theorem S to it was found. This is not a claim to invent electric/magnetic duality or the global forms named by the author. |
| Three-set classification, line 265 | **HOLDS within the recorded search**, with exactly the admissibility and full axis-permutation hypotheses of CL(b). The earlier crossing sketch does not classify weights. |
| S_kappa≤S_full, line 268 | **HOLDS within the recorded search.** It is the termwise consequence of (S1) for the new kappa choice; no stronger SU(2) comparison with S_per is established. |

These are four groups: the kappa definition and its S theorem count
together. The explicit factor 1/4, sixteen-sector sum rule, slab
extension and all-twist inequalities also survive their checks above.
“Not found” describes this search; it is not worldwide novelty.

## 7. Corrections to surrounding claims

1. **Step 3, line 159 — HOLDS AFTER CORRECTION.** Admissibility alone
   allows noninteger coefficients, for example 3/2 on one nonvacuum
   sector and 1 on the vacuum sector. That is a weighted trace, not
   the asserted direct sum of copies of sectors. Nor does the condition
   what(0,0)=1 alone prove that the largest eigenvalue is simple.
   Replace the sentence with: “For an admissible weight invariant under
   all axis permutations, Proposition CL(b) makes the coefficients
   indicators. Lemma W gives the direct-sum trace and its largest
   eigenvalue. A bound S_w(t;B)<1 makes that eigenvalue simple.”
   The actual proof at line 513 already uses this valid order.

2. **The no-crossing wording, lines 157,557 — HOLDS AFTER CORRECTION.**
   CL(a) excludes an even-only admissible self-dual sector trace;
   EVL gives a lossy inequality. Neither proves that every argument
   using crossing must fail. Replace the unrestricted claim by:
   “The direct substitution of the even trace into Theorem S's
   crossing-symmetric trace method is unavailable; these estimates
   do not supply an even-only seed propagation.” (EV-STEP) stays open.

3. **The open (EV-STEP) consequence, lines 553–555 — HOLDS AFTER
   CORRECTION of the quantifier.** Its displayed conclusion controls
   only one sequence L_i. EV-L(d) then covers limits along that
   sequence. To cover every periodic volume-first limit, require
   (G_ev) along every defining sequence, or add a comparison with
   the particular sequence supplied by (EV-STEP). The three actual
   seeds avoid this issue: Corollary EV controls every large integer L.

None of these corrections invalidates any of the 20 named statements.
The Step 5 provenance correction is separate from a mathematical failure.

## 8. Sources, credits and limits

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for the Wilson convolution and transfer construction.
I fetched each specified pinned source once, as requested:
`YM4_sketch_500.tex` and `theorem_0_complete_account_raw_I.tex`
at `31a47c543775`, saved as `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`.
The index README, matching rows and neighbours in chunks 01 and 02,
and the relevant obligations were read before the outline excerpts.
The specific source reads were SA 588–599, 2195–2231 and 2313–2335.
GL3 and GL8 supply the earlier positive convolution and trace framework;
they do not supply this sector comparison. CA-I 2702–2712 expressly
excludes a mass-gap assertion. The index searches found no centre-flux,
dyonic or Pfaffian-sector theorem; the CA 4.12–4.19 index supplied
no applicable step. No whole outline or complete account was read.

Credit the repository authors of `gap-transfer`, `gap-seed-limit`,
`gap-crux-restate`, Identity FL, the zero-flux notes and MIXGFF for
the inputs identified above; in particular the all-integer enlargement
in E' and S3' is the earlier Codex row 699 result. The present check
does not claim it as new. Row 731 credits Gerard 't Hooft for the
twist/flux framework, and Ofer Aharony, Nathan Seiberg and Yuji Tachikawa
for the global-form terminology. Their primary papers were not read
here; none of the checked finite identities rests on recalling them.
No result of Tadeusz Balaban was imported in this check.

Not checked: numerical guides in Step 8.6; the physical phase beliefs;
the remaining methods of Step 6; a proof of any seed at order-one
coupling; SU(2) (KP); (EV-STEP); or the full continuum reconstruction
dependency closure. The continuum use remains conditional on the
scaling and reflection-datum inputs named in the source. Scripts here
only fetched, searched, compared blobs and recorded provenance.

RESULT: All 20 requested named statements HOLD; EV-L survives. Correct the general admissibility, no-crossing and sequence-scope prose, and credit the earlier mixture argument. No seed or SU(2) (KP) is proved; no status is granted.
