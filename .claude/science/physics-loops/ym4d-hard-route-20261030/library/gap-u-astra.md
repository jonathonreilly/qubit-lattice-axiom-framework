# Repo search

The lead's November 8 digest covers other YM4D targets. Its relevant transfer
hit is the older soft-route construction, not the coupling derivative checked
here. The source note's Section 1 points to the closer main-branch hit:
`docs/NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md`.
I fetched `origin/main` (`1f20846b8057f6346ebab6c0dbebdabbd9e472a4`)
and read its claim boundary and lines 42–138. It already
derives the product-rule/Hellmann split for a finite SU(3) packet. Credit that
repository derivation for this method. It neither supplies nor refutes the
SU(2), untruncated, all-level inequalities below. No numerical result from that
note is used. `gap-transfer.md` supplies the Wilson operator and its bounds;
its lead note credits the earlier Codex/Astra transfer construction in
`MASS_GAP_CONSTRUCTION_ASTRA.md`, PR #10114. I fetched that PR at
`f76f6c649cff7dffbab664d8976e680e8f287fe9` and read lines 84–216 of
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CONSTRUCTION_ASTRA.md`.
It has the same full transfer construction, up to a scalar normalization,
and a stronger finite-volume gap bound. It has no coupling-derivative bound
in that passage. These are existing inputs, not new results of this check.

`library/prior/gap-u-astra.md` is absent. The registry search for this target,
VIR/LEV and the transfer derivative found no other owner of this check.
The assigned row 725 is a check of row 710, not a new attack on BAND-sc.

## Status and provenance

Written by OpenAI Codex, GPT-6 Astra, maximum reasoning, 2026-11-11.
Source checkout: `017810761410125809889f38ab4ea0f4e1848c4b`.
Research check, not an audit; this file grants no status.

**Complete.** The mathematical conclusions in scope hold. B1 needs the
continuity-attribution correction already recorded in the source's lead note.
Its Peter–Weyl input is sufficient but can be removed by the argument below.
Scope: `gap-vir-sc.md` Sections 2–4, lines 33–119, with its
lead note at line 8; `gap-transfer.md` Notation and Sections 1–4. Each verdict
was saved as work proceeded. The earlier Claude check was opened only after
all initial verdicts and the hand test were on disk. The mandatory lead note
had already revealed its aggregate verdict and two input-mark corrections;
that exposure is disclosed.

Not covered: the numerical run, Sections 5–9, BAND-sc, a volume-uniform rate
outside the stated range, or any mass gap at coupling of order one or in the
continuum. Rellich–Kato (RK) and Schur representation facts remain named inputs;
their consequences, not a reconstruction of those general theorems, are checked.
No computer-assisted proof or numerical run is used.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for GL3/GL4 and the transfer construction GL8. The index locators
are `sa-index/chunk-02.md:88–103`, including neighbouring rows. GL3 is already
proved there; the present work checks our source's use, rather than claiming
a new derivation. Tadeusz Balaban's renormalization work is background to this
project; no Balaban estimate enters this finite-box check and no paper of his
is imported here.

All source line numbers below refer to the pinned checkout unless prefixed SA.

The requested upstream files were each fetched once at `31a47c543775`:
`/tmp/sa_ym4.tex` (32992 lines) and `/tmp/sa_ca_I.tex` (166711 lines).
After searching the outline index and its obligations, I read only SA
2195–2257 and 2313–2335. No CA-I statement enters this check; its body and
the index for items 4.12–4.19 were not needed. No whole manuscript was read.

## Initial verdicts, recorded before the earlier check

### Setting and constants (source 35–41): HOLDS

Write v = |B| and d = |E| = 3v. There are three positively oriented
spatial links and three spatial plaquettes per vertex. Each plaquette action
lies in [0,2]. Thus 0 <= V_1 <= 6v, M_s >= exp(-3sv), and each of the d
kinetic factors is at least exp(-2s). The full, gauge-averaged transfer kernel
therefore lies between exp(-12sv) and 1. Rayleigh's quotient on the constant
function gives lambda_0 >= exp(-12sv); the kernel norm gives lambda_0 <= 1.
This rederives 3, 6 and 12, including the two half-potentials.

The arguments in `gap-transfer.md` N.1–N.8 and Sections 1–4 were read.
Counting works unchanged on a rectangular periodic box with each side >= 3.
The trace identity is for integer time >= 2; later real-time expressions are
spectral definitions, not an additional lattice trace identity.

### Lemma J(a) (44, proof 51): HOLDS

Independently, expand exp[(s/2)(z+z^(-1))] as the product of two exponential
series on |z|=1. Its z^n coefficient is
sum_{k>=0}(s/2)^(n+2k)/(k!(n+k)!) = J_n.
Both series converge absolutely and uniformly on the circle. Fourier
orthogonality and evenness convert that coefficient to the stated integral
on [0,pi]. This also checks the n=0 normalization, where the cosine norm differs.

### Lemma J(b) (45, proof 51): HOLDS

Integrate the derivative of exp(s cos x) sin(nx) over [0,pi]. Its boundary
values vanish. The product-to-sum formula gives
n J_n = (s/2)(J_(n-1)-J_(n+1)) for n>=1.
Differentiating J(a) gives J_n'=(J_(n-1)+J_(n+1))/2 for n>=1.
Elimination gives s J_n'=n J_n+s J_(n+1). For n=0 the same derivative identity
is J_0'=J_1. Differentiation under the integral is justified on compact
s-intervals by a bounded exponential. This checks both recurrences by an
integral route, separate from the source's coefficient shifts.

### Lemma J(c) (46, proof 51): HOLDS

Divide J_(n+1)'s positive series by J_n's series. The ratio is the weighted
mean of s/[2(n+k+1)], with weights proportional to J_n's k-th summand.
Every weight is positive, and each summand ratio is <= s/[2(n+1)].
This proves strict positivity and the claimed upper bound for every s>0.
The inequality is actually strict at the upper end since k=1 has positive
weight. This is also Sussman–Alpoge GL4, SA 2232–2239; no novelty is claimed.

### Lemma J(d) (47, proof 51): HOLDS

For a polar angle x on S^3, normalized Haar measure has class density
(2/pi) sin^2 x. Multiplication by chi_j=sin((2j+1)x)/sin x and
2 sin x sin((2j+1)x)=cos(2jx)-cos((2j+2)x) give
(2j+1)c_j = exp(-s)(J_(2j)-J_(2j+2)).
J(b) then gives c_j=2 exp(-s)J_(2j+1)/s, with no remaining dimension factor.
All terms of J_(2j+1) are positive. This is the already-proved GL3 of
Ethan Sussman and Levent Alpoge, with Claude and Codex as text authors,
SA 2205–2231, read at the pinned upstream revision. It is an input check.

### Lemma J(e) (48, proof 51): HOLDS

Put m=2j. From J(d),
s(log c_j)'=-s-1+s J_(m+1)'/J_(m+1)=m-s+s r_(m+1).
For 0<s<=4, J(c) gives 0<r_(m+1)<=s/[2(m+2)]<=s/4<=1.
Thus m-s <= -s eta_j' <= m. The endpoint s=4 is permitted here;
the later division by log(4/s) correctly excludes it.

### Lemma J(f) (49, proof 51): HOLDS

Again m=2j is a nonnegative integer. Factor its leading power in J(d):

c_j = exp(-s)(s/2)^m sum_{k>=0}(s/2)^(2k)/[k!(m+k+1)!].

The factorial is at least (m+1)! k!. The remaining sum is the diagonal
part of (sum_{k>=0}(s/2)^k/k!)^2=exp(s), and is no larger than that square.
Consequently c_j <= (s/2)^m/(m+1)! <= (s/4)^m, since the m factors
2,...,m+1 are all at least 2. This is valid for every s>0. For m=0 it
also gives c_0<=1. Thus eta_j>=m log(4/s), including eta_0>=0.
Separately, |chi_j|<=m+1 and 0<c_s<=1 show 0<c_j<=1 for every j,s.
That last bound will justify the infinite energy sums in U(iii).

### Lemma C (55–59): HOLDS, given the stated Schur facts

There is a direct kernel check of the possible missing complement.
`gap-transfer.md` (2d) gives an absolutely uniform character expansion.
Schur orthogonality identifies its coefficient as d_j c_j, d_j=2j+1.
The addition identity
chi_j(uv^(-1))=sum_{a,b} D^j_ab(u) conjugate(D^j_ab(v))
then identifies each convolution summand as c_j Pi_j. The uniform kernel
sum is the whole kernel, so it acts as zero on Y, the common orthogonal
complement. Tensor products give the stated C_s. This checks the claim
without assuming Y=0. The source's alternative trace argument is also valid:
sum_j d_j^2 c_j=c_s(1)=1 and positivity leave zero trace on Y.

The kernels and their difference quotients converge uniformly on compact
s-intervals. Thus C_s' exists in operator norm, is c_n' on H_n and zero
on the fixed Y. For any f, sum_n |c_n'| ||Pi_n f||^2
<= ||C_s'|| ||f||^2, so the derivative form is absolutely convergent.
Left and right translations preserve each representation space. Gauge
averaging therefore commutes with Pi_n. No completeness theorem is needed
for this statement. Strict injectivity, used later in the source, is a different assertion.

### Input RK setup (61): HOLDS; the spectral theorem remains an input

The gauge-averaged kernel is an integral of exp(-s A(u,v,h)), with
0<=A<=12v. Its power series converges uniformly on every complex compact
set, including after any s-derivative. Hence it is entire in Hilbert–Schmidt
norm and self-adjoint for real s. Nonzero eigenvalues of this compact
operator are isolated and have finite multiplicity, as RK requires.
The local analytic eigenvector theorem attributed to Rellich and Kato is
RECALLED, not proved by this check. The following verdicts are conditional
on that explicitly named theorem.

### RK consequence (1) (63): HOLDS, given RK

Differentiate T psi=lambda psi and take its inner product with psi.
Self-adjointness changes <psi,T psi'> to lambda <psi,psi'>, which cancels
the corresponding term on the right. Thus lambda'=<psi,T'psi>.
This proof works for a chosen analytic branch through a multiple eigenvalue.
It does not assign a unique derivative to every vector in that eigenspace.

### RK consequence (2) (63): HOLDS, given RK

Ordered compact-positive eigenvalues satisfy
|lambda_i(A)-lambda_i(B)|<=||A-B||. Indeed the variational formula
lambda_i(A)=inf_{dim F=i} sup_{f perpendicular F, ||f||=1}<f,Af>
changes by at most ||A-B|| in each direction. This proves continuity without
using `gap-mid-max.md` Lemma 4.1, which concerns lambda_0, not lambda_1.

For a level bounded below by delta>0 on a compact coupling interval, a small
neighbourhood of each point contains only finitely many relevant RK branches.
Each pair is identical locally or has isolated zeros of its analytic
difference. Shrink that neighbourhood so it has no crossing except possibly
at its centre. The ordered level is then one branch on each side. A finite
cover of the compact interval gives a finite subdivision with this property.
The positive lower bound prevents accumulation into the zero spectrum.

### RK consequence (3) (63): HOLDS, given RK

Simplicity of lambda_0 leaves just one local eigenvalue branch in RK.
Neighbouring branches patch because they both equal the unique largest
eigenvalue. Thus lambda_0 is real analytic on s>0. The assertion is local
real analyticity patched along the real axis, not an entire complex branch.

### Theorem U(i) (68, proof 74): HOLDS

Put f=M_s psi. Since P psi=psi and the factors preserve H_inv,
lambda=<f,C_s f>=sum_n c_n q_n. Thus sum_n w_n=1, with w_n>=0.
Orthogonality alone gives Q:=sum_n q_n<=||f||^2=<psi,exp(-s V_1)psi><=1.
Also Q>0 because lambda>0. In particular no Peter–Weyl completeness claim
is hidden in this step, and weights with q_n=0 are assigned w_n=0.

### Theorem U(ii) (69, proof 75): HOLDS

Differentiate the two multiplication factors first. Since M_s'=-V_1 M_s/2
and M_s C_s M_s psi=lambda psi on H_inv, their two expectations sum to
-lambda <psi,V_1 psi>. The remaining expectation is sum_n c_n' q_n.
Consequently

s DD = -s⟨V_1⟩_psi + sum_n w_n s c_n'/c_n
     = ⟨N⟩_w - s⟨V_1⟩_psi - s⟨R⟩_w.

There is no derivative of the gauge projection: it is independent of s.
For convergence put a=s/4<1. J(f) gives c_n<=a^N, so
⟨N⟩_w <= [sup_{k>=0} k a^k] Q/lambda < infinity.
Thus the displayed separation into N and R is valid, not a subtraction of
infinite quantities. J(e) gives 0<=R<=d=3v and 0<=V_1<=6v.
They produce exactly -9sv<=s DD<=⟨N⟩_w. The constant 9 is 3+6.
An arbitrary eigenvector at a crossing has this expectation formula;
DD becomes a branch derivative only for a branch eigenvector as in RK(1).

### Theorem U(iii) (70, proof 76): HOLDS

The infinite log-sum step needs integrability, which holds here. Since
0<c_n<=1, eta_n=-log c_n>=0 and c_n eta_n<=1/e (maximize x exp(-x)).
Hence ⟨eta⟩_w<=Q/(e lambda)<infinity. For q_n>0,
log(w_n/q_n)=-eta_n-log lambda. Its w-average is absolutely convergent.
Averaging this identity therefore gives the claimed exact energy formula.

For an independent sign check, set p_n=q_n/Q. It is a probability law and
D(w,q)=D(w,p)-log Q. Jensen's inequality for log gives
sum_n w_n log(p_n/w_n)<=log(sum_n p_n)=0.
Thus D(w,q)>=-log Q>=0. Finally eta_n>=log(4/s) N(n) by J(f), and
log(4/s)>0 on the stated domain. This also verifies the direction of the
energy inequality; q is a subprobability measure, not a probability measure.

### Theorem U(iv) and its branch conclusion (71–72, proof 77): HOLDS

Combine U(ii) and U(iii): s DD<=⟨N⟩_w<=Ehat/log(4/s).
Under RK(1), DD=(log lambda)'=-Ehat'. Writing L4=log(4/s),

(Ehat/L4)' = Ehat'/L4 + Ehat/(s L4^2) >= 0.

The sign is correct. At crossings, ordered positive levels inherit the
integrated monotonicity by RK(2). This is an unsubtracted level statement.
It does not say Ehat-Ehat_0 obeys this same inequality. The source's two
numbered remarks at 79–80 correctly retain that distinction; the claimed
volume order in remark (2) is an upper-bound scale, not a proved asymptotic.

### Proposition EL (82–85): HOLDS for the positive levels defined at 41

With M=1, the invariant part of H_n has eigenvalue c_n. The positive spectrum
is exhausted by these spaces even without deciding Y=0. If j>0 and s<=2,
J_(2j+1)/J_1 is a product of 2j ratios, each <=s/4<=1/2. Hence the
constant state is the unique top state. Its subtraction gives exactly
E=sum_l log(J_1/J_(2j_l+1)).

Let k be the number of nontrivial links. Since each contributes 2j>=1,
k<=N. Differentiation gives
-s E'=N+s sum_{j_l>0}(r_(2j_l+1)-r_1).
For each such link r_(2j+1)<=s/6. Discarding -r_1 therefore gives
-s E'<=N+k s^2/6<=N(1+s^2/6). This rederives the denominator 6.

For m=2j>=1, the factors in (m+1+k)!/(m+1)! are at least 2, so
J_(m+1)<=[(s/2)^(m+1)/(m+1)!] exp(s^2/8).
Together with J_1>=s/2 and (m+1)!>=2^m, this gives
log(J_1/J_(m+1))>=m log(4/s)-s^2/8.
Summing over the k nontrivial links and using k<=N gives the stated bound
E>=N[log(4/s)-s^2/8]. The 8 is 4 from (s/2)^2, times 2 from the
factorial bound. On (0,2] the bracket decreases and is at least
log 2-1/2>0 (integrate 1/x on [1,2]). The quotient K(s) follows.
At degeneracies, the explicit analytic label branches give the same
integrated inequality for ordered levels. No RK theorem is required.
The sentence about *all* eigenvalues can equivalently say *all positive
eigenvalues*, consistent with the file's level convention. To assert no
zero eigenspace, retain Peter–Weyl as in the lead's B1 correction.

### Corollary U' (89–91): HOLDS

U(iv) gives s DD(psi)<= (E+Ehat_0)/L4. The kernel bound checked above gives
Ehat_0<=12sv. U(ii) gives -s DD(psi_0)<=9sv. Adding yields exactly

s[DD(psi)-DD(psi_0)] <= E/L4 + sv(9+12/L4).

No cancellation of the two vacuum bounds is available. The positive error
has the indicated sign and grows with the box volume. The factors 9 and 12
have already been derived from link/plaquette counting, not fitted.

### Theorem B1 (93–100): HOLDS AFTER CORRECTION of the input attribution

The lead note already gives a sufficient correction. Replace the input line by:

> Given Corollary U', RK (including consequence (2) for continuity of
> lambda_1), and `gap-mid-max.md` Lemma 4.1(b) for joint continuity of G_t.
> Peter–Weyl, if used to assert injectivity, is an additional recalled input.

The first incorrect attribution is line 93, repeated as an alternative at 97:
Lemma 4.1 does not prove continuity of lambda_1 or of m. This does not break
the theorem, since RK(2) supplies it. The following checks its three claims.

**Continuity of K_B: HOLDS.** On a compact subinterval of (0,4), lambda_0
and lambda_1 are continuous and positive, with lambda_1<lambda_0. Thus
m=log(lambda_0/lambda_1)>0 and K_B is continuous and nonnegative.

**LEV_K: HOLDS.** On an excited analytic branch, E>=m. Divide U' by s to get
-E'<=E/(s L4)+v(9+12/L4)<=K_B E.
Therefore (exp(integral K_B) E)' >= 0 on every branch piece. RK(2) patches
these inequalities across crossings without changing their direction.
This also proves the vacuum case, E_0=0, trivially without taking log E_0.

**VIR_K at real t>=4: HOLDS.** Termwise LEV gives
G(t exp(A_h);s+h)<=G(t;s), A_h=integral_s^(s+h) K_B.
Subtract G(t;s+h), apply the ordinary mean-value theorem in t, then use
A_h/h -> K_B(s). The result is precisely the upper-right derivative
inequality, not an assumed differentiability in s of an infinite trace.

Here is a separate check of the real-time regularity, avoiding the source's
moment-measure argument. On a compact coupling interval lambda_0>=c>0 and
sum_i lambda_i<=1, hence lambda_i<=1/(i+1) and rho_i<=c^(-1)/(i+1).
For large i and t>=4, |rho_i^t log rho_i|<=rho_i^3/e. These summable bounds
are uniform in s and in compact t-intervals. Ordered-eigenvalue continuity
therefore gives joint continuity of both the thermal sum and its t-derivative.
The t-derivative is nonpositive, so increasing K preserves VIR_K.

**Peter–Weyl is sufficient, but not necessary here.** Lemma C already gives
arbitrarily many positive eigenvalues on H_inv. For each spin j, the loop
character around one elementary spatial plaquette is a nonzero invariant
vector in the label space with spin j on its four links and zero elsewhere.
Distinct spins give orthogonal vectors by one-link Schur orthogonality.
Their C_s eigenvalues are positive for all s>0. For any finite-dimensional
span F of these vectors, M_s^(-1)F is invariant under gauge transformations
and <f,T_s f> >0 for nonzero f in that span's inverse image. Min–max yields
arbitrarily many positive eigenvalues of T_s at every s>0. Each fixed ordered
lambda_i is consequently positive throughout a compact interval and has a
positive minimum there. These positive levels exhaust the trace, regardless
of any zero eigenspace. This removes the need for injectivity in the LEV-to-VIR
argument. It does not purport to prove the general Peter–Weyl theorem.

### Theorem B (102–106): HOLDS, given the named seed theorem

The imported statement is `gap-seed-sc.md` Theorem 4 (57–59, proof 216–218).
It requires n>=4, theta=12800s<1, n theta^n<=0.18 and b>=2n.
At n=4, s<=10^(-6), theta<=8/625<1/4, so
4 theta^4<1/64<9/50=0.18. Also b>=8=2n. Its conclusion is

m >= 4L - 4 log 12800 - (4 log 4 + log 1614)/4,  L=log(1/s).

Here is a hand proof of m>=L that avoids rounded logarithms. Use
12800=2^7 10^2, 1614<2^11, L>=6 log 10. Then

m-L > 10 log 10 - (131/4) log 2 > 23-917/40 = 3/40 > 0.

The last comparison needs only log 10>23/10 and log 2<7/10. For completeness:
e^(7/10)>1+7/10+49/200+343/6000=12013/6000>2.
For e^2, the sum through order 7 is 155/21; the tail starting at order 8
is at most (2/315)/(1-2/9)=2/245. Their sum is 5431/735<37/5.
For e^(3/10), the sum through order 3 is 2699/2000; its tail is at most
(27/80000)/(1-3/50)=27/75200<1/2000. Thus e^(3/10)<27/20 and
e^(23/10)<(37/5)(27/20)=999/100<10. These are rational series estimates,
not computed enclosures.

Also log 2=integral_0^(1/3) 2/(1-x^2) dx>2/3. Therefore
L4=L+2 log 2>69/5+4/3=227/15>15,
so 9+12/L4<49/5<10. Since L4>=L and m>=L,

K_B <= 1/(sL)+10 b^3/L = (1+10s b^3)/(sL).

This rederives 10. On s b^3<=1/10 the numerator is <=2, giving exactly
the stated K=2/(sL). Both LEV_K and VIR_K persist under a larger K;
for VIR_K the reason is G_t<=0. Real t>=4 is justified in B1 above.
No bound uniform in the box is inferred after this volume restriction fails.

### Independent hand test: one loop at s=1/2 in the electric-only model

This tests EL and U by Haar moments, not by numerical diagonalization or a
Bessel evaluation. It is not the full Wilson model at this coupling.
Take B=3^3, d=81, V_1=0, and psi=chi_(1/2)(U_p) around one plaquette.
Haar integration on any one of its four distinct links shows ||psi||=1.
It is gauge invariant, orthogonal to the constant vacuum, and lies in the
label space with four j=1/2 links. Thus N=4 and
lambda=c_(1/2)^4 c_0^77, lambda_0=c_0^81.

Put x=(tr g)/2 and A=<exp(sx)>_Haar, Bx=<x exp(sx)>_Haar,
C=<x^2 exp(sx)>_Haar. Direct character integration gives
c_0=exp(-s)A, c_(1/2)=exp(-s)Bx. Therefore, without differentiating J,

E=4 log(A/Bx),   -s E'=4s(C/Bx-Bx/A).

The density of x is (2/pi)sqrt(1-x^2). Integrate the derivative of
x^(2k-1)(1-x^2)^(3/2) to get
(2k+2)<x^(2k)>=(2k-1)<x^(2k-2)>.
Thus the first moments are 1, 1/4, 1/8, 5/64; odd moments vanish.
At s=1/2, positive Taylor terms and |x|<=1 give the following rational bounds:

- 33/32 < A <= 1+1/32+1/3072+7/321120 < 129/125.
- 49/384 < Bx <= 49/384+7/26720 < 16/125.
- 17/64 < C <= 17/64+5/24576+7/321120 < 267/1000.

For the first and third tails, the first omitted exponential term is
1/46080 and all later term ratios are <=1/224. Their geometric majorant is
7/321120. For the second tail, the first term is 1/3840 and the ratios
are <=1/168, giving 7/26720. All bounds are hand-checkable fractions.

They imply 1/10<Bx/A<512/4125<1/8 and C/Bx<21/10. Also
C/Bx-Bx/A > 2125/1024-512/4125 >39/20;
the last comparison reduces to 2644125>2621440. Consequently

39/10 < -s E' < 4,             E > 4 log 8.

EL predicts -s E'<=4(1+1/24)=25/6 and
E>=4(log 8-1/32). Both pass with a strict margin.
For the exact U identity, integration of
(d/dx)[exp(sx)(1-x^2)^(3/2)] gives A-C=3Bx/s.
At s=1/2, J(b) identifies r_1=Bx/A and r_2=C/Bx-2.
Direct differentiation of lambda gives
s DD=-81/2+(77/2)r_1+2(C/Bx)
     =4-(1/2)[77(1-r_1)+4(1-r_2)],
exactly U(ii) with N=4, V_1=0 and 81 links. Subtracting the vacuum gives
the same independently obtained -s E'. No script evaluated these quantities.

### Constants imported through the seed theorem: arithmetic checked

These are checks of the existing inputs' constants, not a recheck of their
polymer or spectral-recursion theorems. Their dependencies remain attached.

- `gap-sc-box.md:122–138,157–170`: one-plaquette normalization gives activity
  size x=4|s|. Six plaquettes per link and four links per plaquette give
  adjacency degree <=4(6-1)=20. The existing rooted traversal count gives
  20^(2(n-1))=400^(n-1). Choose 1600x_*=1/2, so x_*=1/3200 and
  R=x_*/4=1/12800. The incompatible sum is
  24(4x_*)/(1-1600x_*)=192x_*=3/50. The logarithm bound is
  N(2x)/(1-1/4)=(32/3)|s|N. This traces the radius 12800 to the actual
  activity/counting estimates, rather than treating it as a physical scale.
- `gap-seed-sc.md:140–146`: the two torus terms contribute
  16(32/3)6+(32/3)96=2048. Dividing by 12800 gives 4/25=0.16.
  The exponent 4n is the imported winding-order statement for n>=4.
- `gap-crux-restate.md:192–203`: the three spatial doublings yield
  4^3=64. On x<=1/640,
  (1+x)^64-1<=64x exp(1/10)<=71x.
  Indeed exp(1/10)<=11/10+(1/200)/(1-1/30)=641/580<71/64.
  Squaring gives 71^2=5041. This verifies that numerical amplification;
  the spectral comparison underlying the three doublings remains the input.
- The seed threshold follows from
  (4/25)(9/50)^4=26244/156250000<19/100000.
  For Phi<=19/100000, exp(Phi)-1<=Phi/(1-Phi)<=19/99981<1/5041,
  since 19*5041=95779<99981.
- `gap-seed-sc.md:216–218`: q=5041 S<=5041*2 Phi, and
  5041*2*(4/25)=40328/25=1613+3/25<1614. Therefore
  m>=4 log(1/theta)-(4 log n+log 1614)/n, exactly the input used by B.

### Remaining numbered remarks and Section 4 consequences

**U Remark (1), line 79: HOLDS.** Its first-order identity and inequality
have exactly the domain and the unsubtracted meaning verified above.

**U Remark (2), line 80: HOLDS as a statement of the available bounds.**
The extensive scales are upper bounds from 12sv and 9sv. They do not prove
an extensive asymptotic or a cancellation after vacuum subtraction.

**Integral and range at 109–110: HOLDS.** Substitution L=log(1/s) gives
integral_(beta_0)^(beta_1) 2/(sL) ds=2 log(L_0/L_1).
Also 10*256^3=167772160, and 6*167772160>10^9; hence the restricted
endpoint is below 6*10^(-9). This is only range accounting, not an extension
of the seed. The asymptotic interval-size discussion at 111 is heuristic,
with log(1/s) treated as comparable across the interval; it is not needed.
The cancellation discussed at 112 remains the desired improvement. It has
not been established by bounding the two states separately. Line 113's
exclusion of side lengths 4–7 from Theorem B is correct; B1 still covers them.

### Initial verdicts complete

All requested verdicts and the independent hand test above were saved before
opening `gap-vir-sc-check.md`. No mathematical conclusion fails. B1's input
attribution needs the correction already identified in the lead note.
A separate argument above shows that its added Peter–Weyl input is sufficient
but unnecessary for the positive-level/thermal statements. The comparison
with the earlier check follows below and will not overwrite these verdicts.

## Comparison with the earlier Claude check

Only after the initial verdicts and hand test were saved did I read all
154 lines of `gap-vir-sc-check.md`. The pre-comparison file is saved at
`/tmp/gap-u-astra-20261111/initial-verdicts.md`, SHA-256
`47e5bfb915d716074065565ed8e36fe202c84715acf4e5a8dae7015acc71c2c6`.
That hash records sequencing, not mathematical evidence.

The theorem verdicts agree throughout the assigned scope. Both checks find
the continuity attribution in B1 wrong and its mathematical conclusion right.
The following are the points where my reading differs:

1. **Peter–Weyl necessity: my stronger implication is right.** The earlier
   check at 89 says VIR_K is unproved without Peter–Weyl; it repeats this at
   99, 126, 142–143 and 154. The source proof at 98 does invoke Peter–Weyl,
   so recording it is a faithful sufficient input list. But injectivity is
   not needed to pair the ordered *positive* eigenvalues. The loop-character
   argument in my B1 verdict gives infinitely many positive levels for every
   s>0; min–max and compactness bound each fixed indexed level away from zero
   on [s,s']. A zero eigenspace contributes nothing to G. Thus the categorical
   necessity claim is too strong. Use the corrected continuity attribution
   and either retain Peter–Weyl as a sufficient input, or insert the explicit
   positive-rank argument above. This changes no K or conclusion.
2. **Vacuum orthogonality: the earlier explanation at 79 needs correction.**
   E>=0 already follows from lambda<=lambda_0 for every positive eigenvalue.
   Orthogonality to the simple vacuum gives E>0. The sentence should read:
   “Orthogonality is unnecessary for U'; it restricts the application to
   excited levels.” This affects no displayed inequality.
3. **A rounded denominator reverses an intermediate inequality.** At earlier
   check line 100, for b=256 the exact 10 b^3=167772160 is less than
   1.678*10^8. Hence its reciprocal is greater, not smaller. The exact
   comparison in my Section 4 consequences is right and still proves
   1/(10 b^3)<6*10^(-9). The conclusion is unchanged.

The earlier check's line 31/125 recommendation to name Schur's lemma and
irreducibility explicitly is a useful description of the source's proof.
I agree with that clarification. My direct kernel proof of C instead uses
full matrix-coefficient Schur orthogonality and the given character expansion;
it does not introduce a new completeness premise. Corrected descriptive mark:
“Given the SU(2) Schur representation facts (matrix-coefficient orthogonality;
irreducibility and Schur's lemma if following the source's scalar argument).”

The earlier hand test at 27 also uses semicircle moments. I discovered this
after fixing my test. My test is at s=1/2 and checks a four-link level and
its derivative; theirs is at s=1 and checks a single-link coefficient.
The shared moment method is not counted as a second independent method.
The independent paths here are the Fourier coefficient/integration-by-parts
check of J, the direct kernel check of C, the trace-tail regularity argument,
and the rational proof of B's constants. The provider change alone is not
mathematical evidence. Sections 9–11 of that check contain claims beyond
this task; their other conclusions are not endorsed or contradicted here.

## Completed result and limits

| Statement at the pinned source | Final verdict |
|---|---|
| Lemma J(a), (b), (c), (d), (e), (f) | HOLDS, each |
| Lemma C | HOLDS given the stated Schur representation facts |
| RK setup; consequences (1), (2), (3) | HOLDS, each consequence given RK |
| Theorem U(i), (ii), (iii), (iv), branch form | HOLDS, each |
| U Remarks (1), (2) | HOLDS with the bound interpretation stated above |
| Proposition EL | HOLDS for the positive levels in the setting |
| Corollary U' | HOLDS |
| Theorem B1 | HOLDS AFTER CORRECTION of its continuity attribution; the lead's added Peter–Weyl input is sufficient and can be removed by the argument above |
| Theorem B | HOLDS given its seed input, with all local constant arithmetic checked |

No first failing mathematical line was found in the named conclusions.
The first bad input attribution is source line 93, repeated at 97.
The constant and trace checks do not rebuild RK, the general Schur theorems,
or the full dependency closure of the seed theorem. No numerical run was
made; the older GUIDE run was neither used nor repeated. No mass gap at a
Wilson coupling of order one or in the continuum follows. BAND-sc is unchanged.

This file checks an existing argument. It neither closes a new open science
lemma nor grants audit or retained status. Only this output file was written
in the checkout. The sources, registry, FINISH, ledgers and audit files were
left as read.
