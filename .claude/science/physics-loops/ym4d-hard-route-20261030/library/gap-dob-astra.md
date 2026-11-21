# Repo search

The task-specific prior digest is absent at `442724c96`. The November 8
repo-search digest records searches of main and PRs 10114, 10133, 10134 and
10141; its targets are older RG problems, not this November 11 check.
Its relevant hit is
`pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`.
I fetched PR 10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9` and read
lines 1–35, 100–158 and 223–347. Lines 106–158 give a one-time positive
plaquette witness, not this seed. Lines 225–247 already give Dobrushin
comparison by a heat-bath semigroup; lines 320–342 give a physical-time
gap for beta <= 1/32. Thus neither Dobrushin comparison nor a small-beta
gap is new to this repository. The latter overlaps the example beta = 1/36;
it does not cover the full interval beta < 1/18 or check this text.
Credit that Codex/Astra construction; its full endpoint proof is not checked
again here. The digest records the same file on PR 10133. No additional
target-specific outside-lane hit is supplied in row 724.

During the later comparison I also read the main-branch hit named by the
earlier check:
`docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md`,
lines 31–58, 390–466 and 888–935 at the main revision below. Its
finite-product comparison (lines 440–451) and bare influence contribution
18beta (lines 410–438) are already available. They supply general
comparison machinery, not DOB's cut construction or seed-to-gap argument.
Its provenance credits the historical Codex/Astra notes and Patrick
Rebeschini and Ramon van Handel for broader comparison machinery.

Main's workflow and current rules were read at
`1f20846b8057f6346ebab6c0dbebdabbd9e472a4`. I did not repeat the lead's
whole-repository search. Searches of `open-registry.md` and `open-core.md`
found no matching Dobrushin-gap owner. This is the assigned cross-provider
check, not a new attack on another row's result.

The SA index README, matching chunk rows and neighbours, and obligations
were consulted first. The outline was fetched once at `31a47c543775`.
SA 588–599 explicitly separates clustering from a gap; SA 2094–2110 gives
the Wilson conditional law; SA 2313–2349 gives a positive gauge-averaged
transfer operator and its torus trace identity. These are related inputs,
not the periodic-box seed or DOB's estimate. The Dobrushin search of the
outline index returned no named result. CA-I was fetched once; the
4.12–4.19 index concerns background operators, not this target, and supplies
no premise here. No claim of absence from every account page is made.

## Status and scope

Author: OpenAI Codex, GPT-6 Astra, maximum reasoning, 2026-11-11.
Source revision: `442724c96180a4446f958b8cf5a6f4cc2689e895`.
Research check only; not an audit, and no status is granted.

Complete. No named theorem fails. DC and DOB hold after the lead's proof
corrections; the remaining named statements hold. Section 9 narrows one
remark, and Section 11 records the later comparison and its disagreements.

Scope: `gap-mid-max.md` Sections 8, 10, 4.3 and 5.1, with
its row-709 lead note, the lead note and used shape results in
`gap-seed-shape.md`, and the used inputs of `gap-seed-sc.md` Theorem 1.
No order-one-coupling or continuum mass gap is claimed. Other sections are
not checked in full; the needed trace-continuity and transport steps are
checked below. The full transfer construction and strong-coupling polymer
proof are outside this check. No numerical run discharges a step.

Own verdicts were appended before opening `gap-mid-check.md`; the completed
comparison is Section 11. The source's lead note is an
explicitly supplied correction, not an independent check performed here.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for the indexed outline/account where used; Tadeusz Balaban
for the background RG program. No Balaban estimate is imported by this check.

Checkpoint: requested check complete. No open mathematical obligation remains
within this check's stated conditional scope. The next action belongs to
the lead: use the local corrections and preserve the named input boundaries.
Verdicts below remain in the order in which they were appended.

## 1. Lemma M — HOLDS

Source: `gap-mid-max.md:258–264`. The standing convention is that all
spatial sides are at least 3 (`gap-mid-max.md:38`).

For a spatial link at time j with 1 <= j <= a-2, the four spatial
plaquettes stay in slice j. The other two stay in slabs [j-1,j] and
[j,j+1]. All their links belong to Lambda_0. For a temporal link starting
at j <= a-2, each of its six plaquettes stays in [j,j+1]. Hence the
conditional density depends only on retained links and is unchanged by
the reduction modulo a. The excluded set D contains exactly the seam
links needed for this argument; excluding additional links would also work.

Explicit conditioning check: for bounded h(U_l), let K_h be its integral
against that one-link density. Under the long-torus law,
E[h(U_l) | all other links] = K_h. K_h is measurable with respect to the
retained links other than l. Taking conditional expectation onto that
smaller sigma-field leaves K_h unchanged. Pushing forward by the link
bijection proves the assertion, almost surely. No independence of the
discarded half is assumed. The case a=3 still has the interior spatial
slice j=1 and the stated temporal links.

## 2. Proposition MIX — HOLDS

Source: `gap-mid-max.md:266–272`; input `gap-seed-shape.md:163–172`.

P has |B| plaquettes of each of the three spatial orientations, and |B|
of each of the three temporal orientations. Time translation invariance
therefore identifies its average with the average over all 6a|B|
plaquettes of the short torus, and likewise for the long torus. Spatial
permutation symmetry is not required; rectangular B is allowed. Lemma M's
pushforward identifies each retained plaquette observable with the same
observable of the long torus, including a=3. Averaging the assumed absolute
bound gives |abar_(2a,B)-abar_(a,B)| <= eps(a).

Re-derive the coefficient and its sign. Differentiation of the finite Haar
integral gives F'(t,B;s) = -6t|B| abar_(t,B)(s). Hence

    d/ds [2F(a,B;s)-F(2a,B;s)]
      = 12a|B| [abar_(2a,B)(s)-abar_(a,B)(s)].

At s=0 both partition functions are 1. Integration gives the asserted
upper bound with 12=2*6. Spectral decomposition gives
Phi_B=2g(a;B)-g(2a;B). Since 0<=g(2a;B)<=g(a;B),
g(a;B)<=Phi_B and S(a;B)<=exp(Phi_B)-1. This verifies both conclusions
without any positivity assumption on the integrand. The distance assertion
is the circular-distance calculation in verdict 5 below.

## 3. Lemma DC — HOLDS AFTER CORRECTION

Source: `gap-mid-max.md:282–292`. The inequality is unchanged. Supply
the mass accounting and intermediate-step argument requested by the lead
note. This is Dobrushin's method, also present in the older Codex note
cited in Repo search; no new comparison theorem is claimed.

Line-by-line verdicts:

- Step 1, line 289: HOLDS. Splitting the two integrals first changes the
  function with fixed law, then the law with fixed function. This gives
  delta_k(Gamma_l g)<=delta_k(g)+C(l,k)delta_l(g), with delta_l=0.
- Step 2(a), line 290: HOLDS. Each piece of a given level is removed at
  most once before its descendants acquire the next level. Thus total
  removals at level m-1 are at most total mass created at that level.
  With A_0=Delta(f), induction gives A_m<=alpha^m Delta(f).
- Step 2(b), line 290: HOLDS. Every new level requires one edge of the
  influence graph. This proves the distance bound even for nonsymmetric C.
- Step 2(c), line 290: HOLDS AFTER CORRECTION. Replace its abbreviated
  justification by: **In a sweep, let R be the total removed mass and M
  the initial mass. Each initial piece is removed, so R>=M. Total newly
  created mass is at most alpha R. The end mass is at most
  M-R+alpha R<=alpha M.** This accounts for descendants updated again
  within the same sweep. Finite-step sums have only finitely many levels.
- Step 3, line 291: HOLDS AFTER CORRECTION. **A Markov averaging operator
  cannot increase oscillation. Full-sweep oscillation is at most
  alpha^n Delta(f), so the same convergence holds at every intermediate
  step. Since mu(f_i)=mu(f), sup|f_i-mu(f)|<=osc(f_i) tends to zero.**
- Step 4, line 292: HOLDS. Only updates in D contribute. Each contribution
  is bounded by the mass removed there, necessarily at level >=d. Summing
  A_m for m>=d gives the stated geometric tail. No factor |D| is needed.

Independent algebraic check of the constant (random updates, rather than
the source's ordered sweeps). Put N=|Lambda|, Q=N^(-1)sum_l Gamma_l and
A=(1-1/N)I+C/N. Then delta(Q^n f)<= (A^T)^n delta(f). Row sums of A
are at most 1-(1-alpha)/N<1, so Q^n f converges uniformly to mu(f).
At one step,

    |mu~(h-Qh)| <= N^(-1) sum_(l in D) delta_l(h).

Telescoping and summing the matrix geometric series give

    |mu~(f)-mu(f)|
      <= delta(f)^T (I-C)^(-1) 1_D
       = sum_(m>=0) delta(f)^T C^m 1_D
      <= Delta(f) sum_(m>=d) alpha^m.

The last bound uses the graph distance and C^m 1<=alpha^m 1.
This also checks the matrix orientation: a row-sum bound suffices;
no column-sum hypothesis was omitted. Disconnected support gives zero.
For alpha=0 and d=0 use alpha^0=1; an empty support means constant f.
These conventions handle the degenerate cases without division by alpha.

## 4. Lemma INF — HOLDS

Source: `gap-mid-max.md:294–296`. For l=(x,mu), and each nu!=mu,
the two plaquettes are based at x and x-e_nu. Their other mu-links are
at x+e_nu and x-e_nu; their nu-links start at x, x+e_mu,
x-e_nu and x+e_mu-e_nu. These six links are distinct when all sides
are at least 3. Distinct nu give distinct transverse links and distinct
parallel offsets. Thus there are 3*6=18 distinct neighbours, with each
pair in at most one plaquette. This includes side 3; side 2 would fail.

For a common plaquette, cyclicity and tr(V)=tr(V^(-1)) in SU(2)
put its varying term in the form s Re(q(U_l) dot v), with |v|=1.
Changing the other link replaces v by v', with |v-v'|<=2.
The log-density perturbation g therefore has range at most 4s.
Unshared plaquettes contribute zero perturbation.

Here is the normalization-sensitive TV estimate in full. Along
rho_tau=exp(h+tau g)/integral exp(h+tau g),
partial_tau rho_tau=rho_tau(g-E_tau g). If g lies in [u,v],

    E_tau |g-E_tau g| <= sqrt(Var_tau g) <= (v-u)/2.

The second inequality follows by subtracting the midpoint (u+v)/2:
Var g=E(g-midpoint)^2-(Eg-midpoint)^2<=(v-u)^2/4.
Integrating in tau and using TV=(1/2)L1 gives TV<=osc(g)/4<=s.
Consequently C(l,k)<=s on neighbours, C(l,k)=0 otherwise, and
alpha<=18s. The constants 4, 1/4 and 18 are all re-derived here.

## 5. Theorem DOB — HOLDS AFTER CORRECTION

Source: `gap-mid-max.md:298–304`. Correct the distance sentence at line
304 as in the lead note. All conclusions and constants survive. The
gap implication uses (TM) and Theorem SH, with the source's side convention
L>=3. It is a lattice gap at fixed beta, not a continuum gap.

### 5.1 Distance, plaquette shift, and seed

Corrected text: **Put link positions on the metric circle R/aZ. Adjacent
links in the influence graph have circular distance at most 1.** A space
link has position j, a time link j+1/2. For j=floor(a/2), positions of P
are in [j-1,j]; positions of D are 0, a-1 and a-1/2. Their minimum
circular distance is at least j-1: the route to 0 costs at least j-1,
and the route toward a-1 costs at least a-1-j>=j-1. The circular metric
and triangle inequality now give graph distance d>=j-1. This also covers
a=3, where the bound is zero. The first false sentence in the uncorrected
proof is line 304's assertion about ordinary positions across the seam.

Each of four distinct links changes x_p by at most 2, so Delta(x_p)<=8.
Apply DC and INF at s, then replace 18s by alpha=18beta<1 in the
increasing expression alpha^d/(1-alpha). Averaging over P gives the first
inequality of line 300. MIX multiplies by 12a|B|beta, giving 96=12*8.
For B=(2a)^3, |B|=8a^3; this gives 768=96*8 in line 302.

If this last bound is <=3/5000, then

    S <= exp(3/5000)-1 <= (3/5000)/(1-3/5000)
      = 3/4997 < 601/1000000 < 1/1650.

Here exp(x)<=1/(1-x) for 0<=x<1 follows term by term from its series.
The two strict comparisons reduce to 3000000<3003197 and
991650<1000000. Thus the strict seed is proved, including equality in
the hypothesis on Phi_B.

### 5.2 Shape constants used by DOB and TR1

Inputs read: `gap-seed-shape.md:58–110,114–138`, including its lead note.
The enlargement lemma follows from crossed-direction trace monotonicity
and the nonnegative ground-state deficit, as its proof states. Its
three-direction iteration multiplies the old G_q terms by
beta_1 beta_2 beta_3 and telescopes the added coefficient to
(p/q)(Pi-1). Time multiplication uses integer spectral multiplicities:
sum rho_i^(jt) <= (sum rho_i^t)^j.

For the r=2 to r=4 enlargement at fixed time, the three factors are
4a/(2a-a)=4, so 1+s_1 <= (1+s)^64. With s<=1/1650,
x=64s<=32/825<0.03879. The hand series bound

    exp(x)-1 <= x + x^2/[2(1-x/3)]

holds because n!>=2*3^(n-2) for n>=2. At x=0.03879,
x^2=0.0015046641 and the denominator is 1.97414; the tail is
<0.000763. Therefore s_1<0.039553<0.0396<1/25. Also
s_1<=64s exp(64s)<=66.6s.

For r=4, j=p=2 and q=3: Pi=4^3=64, C=(2/3)(64-1)=42,
so phi(x)=(1+x^2)^8(1+x^3)^336-1. On [0,1/25],
u=log(1+phi(x))<=21.44x^2<=0.034304.
The same series bound gives exp(0.034304)<1.035: its quadratic
remainder is <0.0012/1.97<0.00061. Hence

    phi(x) <=21.44*1.035*x^2=22.1904*x^2<=22.2*x^2.

Thus K=22.2 is valid, with K/25=0.888<1. Its two-stage rate constant
is bounded by 22.2*66.6=1478.52<1479, as stated in the shape table.
These checks use rational series bounds, not decimal evaluation of exp.

For all cube sizes, SH(ii) uses E=(2*4/(4-1))^3=512/27. It gives

    m(L^3) >= [log(1/(22.2s_1)) - 2^(-k)log(eE/22.2)]/a,
    2^k*4a <= L < 2^(k+1)*4a.

Re-derive the numerical slack. 22.2*0.0396=0.87912<0.8792, and
-log(0.8792)>0.1208+0.1208^2/2=0.12809632>0.128.
Further, E/22.2=2560/2997=1-y, where y=437/2997>0.145.
Thus log(eE/22.2)<=1-y-y^2/2<0.85. For k>=4 the loss is at
most 0.85/16=0.053125, so m(L^3)>0.074875/a>0.07/a>0.06/a.
The side condition is exactly L>=16*4a=64a.

The displayed SH bound tends to the positive constant
log(1/(22.2s_1))/a when s_1>0. If s_1=0, use the same recursion with
the positive upper bound 0.0396 in its place; it gives the displayed
finite lower bounds as well. The finitely many smaller cubes with L>=3 have
positive gaps by the simple isolated top eigenvalue in (TM). Taking their
finite minimum gives a uniform positive infimum over all such cubes.
Nothing here asserts the same statement for degenerate sides 1 or 2.

### 5.3 Existence of a and independent hand test

For even a=2n, the seed's left side is a fixed beta-dependent constant
times n^4 alpha^n. Its consecutive ratio is alpha(1+1/n)^4, eventually
strictly below 1. For example, (1+1/n)^4<=1+15/n and
n>=30/(1-alpha) makes this ratio <=(1+alpha)/2<1. Thus the seed holds
for all sufficiently large even a. This proves existence for each fixed
0<beta<1/18, with no uniformity as beta approaches the endpoint.

Independent hand test of the requested example: beta=1/36, a=90 gives
alpha=1/2 and floor(a/2)-1=44. Cancel powers before estimating:

    768*90^4*(1/36)*2^(-44)/(1/2)
      = 3^7*5^4/2^33 = 1366875/8589934592.

This is <1/6250=0.00016, since
1366875*6250=8542968750<8589934592. It is therefore <0.0006
with substantial slack. This exact integer comparison replaces the
source's floating decimal products. The theorem gives m(L^3)>=1/1500
for L>=5760; the preceding slack even gives m(L^3)>7/9000 there.
No calculation script was used.

## 6. Proposition Delta — HOLDS

Source: `gap-mid-max.md:144–148`; definitions and inputs at
`gap-crux-restate.md:31–45`. All three claims hold under (TM), the
permutation symmetry of Z, and Theorem SH.

For nonnegative eigenvalues, the sequence norm (sum lambda_i^t)^(1/t)
decreases with t. One direct proof divides by its a-norm: each normalized
eigenvalue is <=1, so its b-th power is <=its a-th power for b>=a.
This proves the comparison for arbitrary integer b>=a, without requiring
b/a to be an integer. Use it successively in the three spatial directions:

    F(a,b,b,b) <= (b/a)^3 F(a,a,a,a).

Also F(t,b^3)>=f t b^3; taking t to infinity and dividing by t gives
log lambda_0(b^3)>=f b^3. Subtracting a times this bound gives precisely
g(a;b^3)<=(b/a)^3 Delta(a^4). No ground-state equality with f is assumed.

At b=4a the factor is 4^3=64 and
64*(61/100000)=0.03904. The series bound of verdict 5 yields
exp(0.03904)-1<0.03904+0.000775=0.039815<0.0399<1/25:
the squared numerator is <0.001525 and the tail denominator is >1.97.
Thus the claimed seed and SH's uniform gap follow. If the infimum over
all allowed cube sizes were zero, such a seed could not occur: the large
cubes would have a uniform lower bound and the remaining finite collection
would have positive gaps by (TM). This proves the strict lower bound
Delta(a^4)>0.00061 for every a in the stated gapless class.

## 7. Corollary TR1 — HOLDS

Source: `gap-mid-max.md:150–158`. The coupling convention is
0<beta_0<=1/25600, and K has Theorem TR's continuity and nonnegativity
hypotheses. The conclusion is conditional on (VIR_K), Theorem SH, (TM),
and `gap-seed-sc.md` Theorem 1(iii), not a proof of (VIR_K).

Theorem 1's statement was read at `gap-seed-sc.md:30–38`: its supplied
constants are R=1/12800, 0.16, and exponent e(n)=4n for n>=4;
the n=3 exponent is 9 and is not used. The entire polymer proof producing
those constants is outside this check. All constants derived from that
input are checked below.

Monotonicity in each side makes the dyadic cubes cofinal for f. Hence the
finite telescoping identity, followed by its limit, gives

    Delta(n^4)=sum_(k>=0) 16^(-(k+1)) Phi(2^k n)
      <=0.01 n^4 sum_(k>=0) theta^(4n*2^k),  theta=12800 beta_0.

Here 0.01=0.16/16; the factor (2^k)^4 cancels 16^k. Put
q=theta^(4n). Since 2^k>=k+1, the sum is at most q/(1-q).
For n>=4, q<=2^(-16), and 0.01/(1-2^(-16))<0.0101.
The displayed bound on Delta in line 156 therefore holds.

With t_0=ceil(log_2 b)>=8, Proposition Delta gives

    g(t_0;b^3;beta_0)
      <=0.0101 b^3 t_0 theta^(4t_0)
      <=0.0101 b^3 t_0 16^(-t_0)
      <=0.0101 t_0/b.

Because (log_2 b+1)/b decreases for b>=256,
t_0/b<=9/256<0.036. For clarity, its derivative has numerator
1/log(2)-log_2(b)-1<2-9<0; log(2)>1/2 follows by integration.
Thus g<=0.0101*9/256=0.000355078125<0.00037<0.000505.
This also verifies t_0<a=b/2 and all required time domains.

Theorem TR's characteristic tau(s)=t_0 exp(integral K) stays within
[t_0,a]. The two increments in its proof have cancelling upper right
derivatives, by joint continuity of G_t. A continuous function with
nonpositive upper right derivative is nonincreasing: subtract eps*s,
and a supposed increase would have a last crossing of an intermediate
level with nonnegative right upper derivative. This verifies the transport
step used here rather than assuming a differentiable coupling dependence.
Monotonicity in time then gives g(a;b^3;beta_1)<0.000505, and

    S(a;b^3;beta_1)<0.000505/(1-0.000505)<0.00051<1/1650.

The arithmetic and r=2 to r=4 enlargement are those independently checked
in verdict 5. They give a uniform positive infimum for L>=2b=4a and
m(L^3)>0.07/a for L>=64a=32b. Thus both the stated 0.06/a=0.12/b
and the proof's stronger 0.07/a are valid. Each remaining finite cube has
a gap by (TM). The estimates labelled GUIDE in line 158 are not premises
and are not certified by this verdict.

## 8. Theorem CRIT

Source: `gap-mid-max.md:190–207`. Inputs are (TM), trace continuity,
Proposition Delta, Theorem SH and `gap-seed-sc.md` Theorem 1(iii).
(VIR_K) is not needed. Here 0<t'<=1/25 and all couplings are positive.

### 8(a) Sigma(t') is open — HOLDS

For fixed B, p_n(beta)=Z(n,B;beta) is continuous. The identities

    lambda_0=inf_(n>=3) p_n^(1/n)
            =sup_(n>=3) (p_(2n)/p_n)^(1/n)

make lambda_0 both upper and lower semicontinuous. The inequalities and
limits follow by dividing each trace by lambda_0^n; summability at power
3 supplies domination. Thus lambda_0 is continuous and positive.
For each integer a, S(a;(4a)^3;beta)=Z/lambda_0^a-1 is continuous.
Sigma(t') is a union of its strict sublevel sets. This checks line 199(a).

### 8(b) (0,1/12800) is contained in Sigma(t') — HOLDS

Fix theta=12800 beta<1. The same telescoping and geometric majorant as
in verdict 7 give, for a>=4,

    Delta(a^4)<=0.01 a^4 theta^(4a)/(1-theta^(4a)).

This tends to zero: the numerator's consecutive ratio tends to theta^4<1,
and the denominator tends to 1. Proposition Delta then gives
S(a;(4a)^3)<=exp(64 Delta(a^4))-1, eventually below the fixed positive
t'. The whole interval is included, so beta*(t')>=1/12800. This is a
weaker range than DOB now supplies, but is correct as written.

### 8(c) Uniform gap below beta*(1/25) — HOLDS

For 0<beta<beta*, the definition of the supremum gives some b>beta
with (0,b) contained in Sigma(1/25). Thus beta has a seed a with
s=S(a;(4a)^3)<1/25. The r=4 constants in verdict 5 give K=22.2,
K/25=0.888<1. Theorem SH(iii) gives the positive infimum over L>=4a.
Each finite cube outside that range has its own positive gap by (TM).
The bound can depend on beta and on its seed a; no bound uniform as
beta approaches beta* is claimed.

### 8(d) Boundary thermal sums and Delta — HOLDS

If finite beta* belonged to the open set Sigma(t'), a neighbourhood of
beta* would belong too. Together with (0,beta*) from the preceding
supremum argument, this contradicts its definition. Thus every a has
S(a;(4a)^3;beta*)>=t'. For t'=1/25,

    64 Delta(a^4;beta*) >= g(a;(4a)^3;beta*) >= log(1.04).

The strict numerical comparison is hand-checkable:
log(1+x)>x-x^2/2 for x>0, since the derivative of the difference is
x^2/(1+x)>0. At x=1/25 this gives log(1.04)>0.0392.
Hence Delta>0.0392/64=0.0006125>0.00061. This verifies the strict
inequality in line 196, not merely a non-strict version.

### 8(e) Seed sizes diverge at the boundary — HOLDS

If a_j did not tend to infinity, infinitely many a_j would lie in one
finite set of integers. A subsequence would have constant a_j=a.
Continuity from (a) would give S(a;(4a)^3;beta*)<=t''<1/25,
contradicting (d). No monotonicity of S in beta, no monotonicity of a_j,
and no one-sided approach of beta_j are used.

The extensions in line 201 hold for each listed fixed shape and positive
threshold: its finite-volume thermal sum is continuous, the strong-coupling
bound makes it small, and its shape theorem supplies the gap. For a finite
collection, the seed set is again an open union over the finitely many
shapes and countably many sizes. A bounded-size subsequence also has a
constant-shape subsequence, proving the analogue of (e).

The interpretation in lines 203–207 must retain its stated meaning:
beta* is the boundary of this sufficient seed criterion. Clauses (a)–(e)
do not prove that the physical gap vanishes there, or that every uniformly
gapped family has such a seed. No converse is used. (NOCRIT) implies the
gap at every coupling; this conditional implication does not establish
(NOCRIT) for Wilson SU(2).

## 9. The three numbered remarks after DOB

These are at `gap-mid-max.md:306`; they are included so that no numbered
item in Section 10 is silently skipped.

### Remark (1) — HOLDS as the stated conditional improvement

The named prior was read at `gap-zf-box-x.md:39–53,108`. Its B2 is an
L1 bound c(s)=s sqrt(1+9s^2 exp(6s)), so TV is at most c(s)/2.
The same 18-neighbour count gives alpha<=9c(s). At s<=1/10,
exp(0.6)<1.83: the series through degree 3 is 1.816 and the remaining
tail is at most 0.0054/(1-0.12)<0.006137. Consequently
1+9s^2 exp(6s)<1.1647<1.08^2 and 9c(s)<0.972<1.
Thus that input can replace INF in the same argument, including at
beta=1/10. This is reuse of the named sharper input, not a new result or
an endorsement of the rest of its complex-coupling proof. The rough
decimal location "about 0.102" is not used to discharge anything.

### Remark (2) — HOLDS for the certified lower bound

At a=90 the proof's stronger bound 0.07/a=7/9000 exceeds 0.00067.
Thus the quoted lower bound 6.7*10^(-4) is valid using that stronger
bound. It must not be obtained by rounding 0.06/90 upwards. The comparison
with the leading strong-coupling expression 4 log(4/beta) is explicitly
GUIDE; it is not a rigorous value of the mass at beta=1/36.

### Remark (3) — HOLDS AFTER CORRECTION of its scope sentence

For a bounded real plaquette potential w, changing a neighbour changes
the one-link exponent by a function of oscillation at most
2s osc(w). The proof of INF gives C<=s osc(w)/2. Thus DC and the
small-coupling mixing argument extend to compact groups. The seed and
gap implications still require the positive-transfer hypotheses (TM),
as the theorem's conditional gap clause already states.

Replace the last sentence by: **Outside the range certified by the chosen
influence majorant, this proof no longer establishes alpha<1. It does
not prove that the actual influence sum is >=1, or that mixing fails.**
The literal assertion that the influence bound fails above beta=1/18
cannot describe the actual influences: Remark (1)'s own sharper bound
still proves alpha<1 up to beta=1/10. This clarification leaves DOB's
range, constants and conclusions unchanged.

## 10. Own verdicts sealed before the comparison

All requested named statements and CRIT(a)–(e) have verdicts above.
No named theorem fails. DC and DOB hold with the lead's local proof
corrections; M, MIX, INF, Delta, TR1 and CRIT hold. Remark (3) needs
the scope correction just stated. The exact example is checked by hand.
The full earlier Claude report is still unopened at this checkpoint.

The check covers implications from (TM), Theorem SH, and Theorem 1(iii)
of `gap-seed-sc.md`. The used shape constants and their derivations have
been checked here. The full Wilson transfer construction and the polymer
proof behind the supplied 0.16 and 1/12800 constants have not. The input
statements are not thereby independently certified. GUIDE comparisons,
infinite-volume reconstruction, continuum scaling, and order-one-coupling
claims are outside this check. No numerical script or proof assistant ran.

## 11. Comparison with the earlier Claude check

Only after Section 10 was saved did I read `gap-mid-check.md:1–157`.
It was written by Claude Opus 5.5 high. On every named theorem in this
assignment, our verdicts agree: its lines 41–58, 72–101 and 137–146.
Its DC corrections at 85–86 and seam correction at 97 are right.
Its bounds 8, 96 and 768, seed thresholds, and the requested example are
right. My checks use the random-update resolvent and exact rational series
bounds, including a different integer test of (1/36,90).

Points of disagreement or incomplete support, with their resolution:

1. **Remark (3)'s actual-influence reading.** The earlier check says it
   holds without qualification at line 102. The source's last sentence
   at `gap-mid-max.md:306` must instead distinguish a failed sufficient
   majorant from actual failure of alpha<1. On the literal latter reading
   my correction is right: its own sharper input gives alpha<0.972 at
   beta=1/10>1/18. Nothing fails in DOB. If "bound fails" means only
   "the displayed crude certificate stops working", the mathematical
   content already agrees; the replacement removes the ambiguity.
2. **Which constants were independently re-derived.** The earlier check's
   line 148 includes 1/12800 in that list, while line 157 expressly
   excludes checking `gap-seed-sc.md` Theorem 1(iii). Its calculations
   use that radius as an input; they do not derive it. My narrower input
   description in Section 7 is correct. This is a provenance correction,
   not a challenge to Theorem 1 or its constants. The derived constants
   downstream of that input have been checked here.
3. **The extra example's minimum size.** Line 122 concludes that 50 is
   the smallest admissible a at beta=1/54 after checking only 48 and 49.
   Its conclusion is right, but that inference needs a monotonicity
   argument. For H(a)=(64/3)a^4 3^(-(floor(a/2)-1)),
   H(2n+2)/H(2n)=(1+1/n)^4/3. The even sequence rises from 4 to 8,
   then decreases, since at n=4 the ratio is 625/768<1 and falls
   thereafter. H(3)=1728, H(4)>1, and H(48)>1/900>0.0006
   (H(48)=2^22/3^20, with 2^22>4000000 and 3^20<60000^2).
   Odd terms exceed the preceding even term. Thus all a<50 fail,
   and H(50)<0.0006 as its hand test states. The added line repairs
   the support; neither provider has a different numerical conclusion.

The repo-search coverage also differs. The earlier check acknowledged at
line 21 that it had not fetched main. Main and the older PR do contain
comparison proofs, now cited in Repo search. This does not refute its
claim of novelty for the exact combined DOB statement: neither inspected
hit states that seed theorem over the full beta<1/18 interval. It does
prevent treating comparison itself, or any fixed-spacing small-beta gap,
as new here. No general novelty or absence claim is certified.

I agree with its treatment of CRIT's phase-transition interpretation as
an interpretation (line 58), and with the distinction between proof and
GUIDE arithmetic (lines 111–113). Its verdicts on the wider Sections 6–7,
Lemma 4.2, and the unassigned candidate statements are outside this check;
reading those verdicts is not an independent certification of them.
