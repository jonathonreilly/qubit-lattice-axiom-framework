## Repo search

Target terms: `H-DBL`, `JOIN-TH`, `CUT-TH`,
`gap-cutth`, `static.oscillator`, `wall.induced.phase`, and
`free.wall.*(doubl|seed)`. Refs: `origin/main`, `pr/10114`, `pr/10133`,
`pr/10134`, `pr/10141` in `/Users/jonreilly/Projects/Physics`.
Methods: `joining free energy`, `thermal (log.sum|sum).{0,70}doubl`,
`free.wall.{0,70}(transfer|phase)`, `wall.induced`. The bounded completed
searches returned the relevant main-branch hits below and no target-label
hit on any of the five refs. A broader `W.-ENG` search found unrelated
"two-engine" notes; a generic direct-sum search hit its cap and is not
an absence check. The search outside this lane in the present checkout
returned no target-label hit.

All paths in this table are under `origin/main:research/mass-gap/library/`.

| Hit | Exact statement relevant here | Closeness |
|---|---|---|
| `gap-crux-restate.md:174–205` | For symmetric positive trace families, `1+S(a;2b)<=(1+S(a;b))^(2b/(b-a))`; three uses and trace squaring give Theorem S with seed threshold `1/5041`. | Existing torus engine and method, credited and reused; it has traces in both exchanged directions, unlike free walls. |
| `gap-seed-sc.md:7–25`; `gap-vir-sc-check.md:106` | The seed is proved only below `beta=1/12800`; the latter uses `G(4;B;s)<=(4 abs(B)/100)(12800s)^16`. | Prior small-coupling work, not the join comparison. The local tube coefficient below builds on these notes. |
| `gap-seed-check-astra.md:33–43` | SA GL3 supplies positive convolution coefficients; GL8 supplies a positive transfer and its torus trace. | Already available inputs, not a new contribution of row 910 or this check. |
| `gap-skeleton-max-b.md:508,562`; `prior/gap-crux-prior-ym.md:13,104` | The proposed zero-free route needs a box-uniform complex neighbourhood; the limit-state task assumes a common free-box gap. The existing `exp(-24 beta abs(B))` bound is not uniform in the box. | Different conditional routes/consumers; no doubling theorem or two-sector counterexample. |
| `gap-form-exercise.md:469` | A tested compact-Gaussian doubling ratio is explicitly a guide, not a theorem for other masses. | Not used as evidence. |

Refs resolved, in the order above, to `4dcb69a3ce2b`, `f76f6c649cff`,
`89faef229ff6`, `1e70c7211a2c`, `c73ad7b177d9`.
`prior/repo-search-2026-11-08.md` was read in full; it concerns older
RG targets and supplies no check of row 910. The task-specific prior
file is absent. The registry has no target/free-wall/doubling match.
Row 911 expressly owns this check; no duplicate check was found.

OpenAI Codex, configured GPT-6 Astra / xhigh task; source checkout
`cd91ca793b68682bccf4685ddae8519d9948ca69`; 2026-11-13.
Research text, not an audit; this report grants no status.

## Check plan and checkpoint

Read row 910 line by line. Verify Lemma J and its equivalence; both ring
rejections; Theorem C'; the precise class of Theorem 2P; the two-coupling
construction 2P'; Lemma DS and its structural scope; the small-beta sign.
Use written arguments only. Do not use the guide run as proof.
Consult indexed source ranges for any account result used. Preserve the
source note and write findings here as each argument is settled.

Checkpoint complete: the seven requested statements have verdicts below.
The first failing exact formula is Step 4.3's no-flux normalization.
The order-one Wilson JOIN-TH obligation remains open. No source note,
registry, FINISH row or status file was edited.

## 1. Lemma J and H-DBL iff JOIN-TH: HOLDS

Source: `gap-cutth-max.md:62–76`. Write `B_2=B|B`. Directly,

`log W(a;B_2)-2 log W(a;B)-a[e(B_2)-2e(B)]
 = g(a;B_2)-2g(a;B)`.

Thus the constants correspond exactly by `kappa=k-2`, on the same
rectangles and with the same quantifiers. This is an equivalent
reformulation, not a weaker analytic obligation. Requiring `kappa>=0`
restricts to `k>=2`; any valid smaller k can of course be enlarged.

For a positive compact transfer with a nonzero top eigenvalue,
`log Tr M^T/T -> log lambda_0`. To see this without an interchange of
limits, fix a trace-class power q and bound the normalized trace for
`T>=q` between one and `Tr(M/lambda_0)^q`. Dividing its logarithm by T
proves the limit. Apply this to both boxes to obtain
`J_0=lim_T F_join(T)/T`.

At a fixed finite box, the interpolated Wilson kernel is smooth and
strictly positive also at s=0, although it has zero eigenvalues there.
Its Perron eigenvalue is simple and isolated. Differentiating its spectral
projection, then taking the trace-power limit, gives
`e_s'=lim_T (1/T) partial_s log W_s(T)`. Integrating yields J-INT.
Jensen at the independent-box endpoint gives `F_join>=0`, and
`|X_cut|<=a N_x` gives the upper bound; the same bounds pass to J_0.
No ring input is used.

## 2. Both ring forms of CUT-TH: HOLDS AFTER CORRECTION

The rejection as a *group-independent required target* holds. It does
not refute either proposed inequality for Wilson SU(2). The exact
CUT-TH sandwich is `(1-theta)h<=g<=(1+theta')h`, where h is the full
or even ring thermal logarithm, `theta<1` and `theta'` is finite.

Reuse `gap-fw-wilson-check-astra.md:282–363`. In the frozen finite-group
limit the free contractible box has one flat class. A ring has one class
function for each conjugacy class of its holonomy. The full Z_2 trace
tends to two, so h tends to log 2 while g tends to zero. For Q_8 the
central flip exchanges `{1}` with `{-1}` and fixes each of the three
classes `{+i,-i}`, `{+j,-j}`, `{+k,-k}`. Its even trace tends to four.
For 2T, the classes are the two central singletons, one order-four
class, and two pairs interchanged by multiplication by -1. The even
dimension is again `1+1+2=4`. Thus the upper CUT-TH inequality fails
for any fixed theta below one. This uses finite class counts, no run.
The even Z_2 ring is not refuted by this count: its dimension is one.

Correction at source line 80: CUT-TH is not literally “H-DBL PLUS” an
equivalent no-light-ring-state statement. It is a sufficient *two-sided
quantitative comparison* with a ring trace, strictly more than the
engine requires. No converse equivalence is proved. Also, the later
finite-beta negative-kappa assertions are labelled ARGUED in Step 7;
the frozen class count does not prove them.

## 3. Theorem C': HOLDS

Source: lines 85–98. Put `B=4k^6` with `k>=1` and
`0<s_0<1/B`. At level j set x=s_j. Conditional induction gives
`x<=s_0`. For A>=1 and Ax<=1/4,

`(1+x)^A-1 <= exp(Ax)-1 <= Ax/(1-Ax) <= (4/3)Ax`.

The first pre-step sum is x. After one step its sum is less than
`1/(3k^5)<=1/(3k^4)`; after two steps it is less than
`1/(3k^4)`. Therefore each required conditional hypothesis is available
before it is used. The third enlarged sum is at most `2k^3 x`.
Integer trace multiplicities give `S(2a)<=S(a)^2`, hence
`s_(j+1)<=B s_j^2<s_j` and
`B s_j<=(B s_0)^(2^j)`. The first excitation supplies the asserted
gap lower bound. At s_0=0 use the extended convention m=+infinity,
as already specified in check 909. The conclusion concerns dyadic
cubes only; no limit-state theorem is supplied.

The assertion after the theorem about a photon is a separate physical
claim, not a consequence of its induction. The rigorous quantitative
statement is only `m(B)>=log(3k^4)/a` whenever the box is cold.

## 4. Additional exact error: Step 4.3 no-flux formula FAILS as written

The source uses the unnormalized plaquette weight exp(beta x). Therefore
`c_0(beta)=2 I_1(beta)/beta=1+beta^2/8+...`, not one.
If ell is the number of slice links on the joining cut, its own
nonnegative spectral expansion gives

`pi_a(J=0)=c_0(beta)^ell W(a;B)^2/W(a;B_2)`.

Consequently `F_join=ell log c_0(beta)-log pi_a(0)`, not
`F_join=-log pi_a(0)`. For the specified periodic-time slice ell is
linear in a. The extra term cancels against its zero-temperature rate
in `F_join-a J_0`, so the thermal-excess interpretation can be repaired
and Lemma J is unaffected. This correction follows directly from the
positive Bessel series in SA 2215–2231 after undoing its exp(-beta)
normalization; no numerical coefficient evaluation is used.

## 5. Theorem 2P: HOLDS AFTER CORRECTION of the class wording

Source: lines 101–132. The counterexample works in the explicitly stated
mixed class (T), (V), spatial permutation symmetry and bounded FW2 defect.
It does not have symmetric rings. It must not be described as a member
of an all-boundary-pattern class with compatible periodic closures.
Row 898 distinguishes its all-free class at line 412 from the mixed
family at lines 431–437. Check 909 already makes this distinction at
lines 210–225. Preserve that qualification in the RESULT.

Membership is exact. The oscillator Hamiltonian on N=n_X bcd sites has
levels m_X j with multiplicities `binomial(N+j-1,j)`. Its trace is
`(1-exp(-a m_X))^(-N)`. Taking the two-sector direct sum gives (T).
In b the weights are `C_X=exp(-a D_X cd)`, with sum at most one.
The corresponding eigenvalues are the displayed t_X. For any positive
measure of total mass at most one and positive exponents r,s,

`(integral t^r)(integral t^s)
 <= (integral 1)(integral t^(r+s)) <= integral t^(r+s)`.

The first inequality follows by integrating
`(t^r-u^r)(t^s-u^s)>=0`. This proves FW2 directly, without needing
continuity of log W at an artificial zero eigenvalue. Also,
`W(r+s)<=exp(a D_B cd) W(r)W(s)`, because the latter product contains
both same-sector products. This is the required area defect.

Part (i) holds for `s'>0`, `C>0`, `Cs'<1`. Choose
`m_B=log(1/(Cs'))/(2a_0)`, then m_A>m_B so that
`b_0^3 F_(a_0)(m_A)<=log(1+s'/2)`. Choose DD with the B-sector
contribution to the normalized seed at most s'/2. The written formula
then gives S<=s'. On sufficiently large cubes E_B-E_A grows cubically,
so the actual gap is m_B, below the claimed W'-ENG bound.
Correction to the proof's sentence “above b_*”: the gap is
`min(m_B,E_B-E_A)` there and equals m_B only eventually. The theorem
already says “every large cube”, so its conclusion survives.

Part (ii) also holds, including arbitrarily cold input to the failing
step. One exact choice inside the stated interval is
`DD=(7/12)b DF`. On the four rectangles the differences E_A-E_B,
divided by `DF b^3`, are respectively
`3/4`, `11/12`, `2/3`, `-1`.
First choose m_A large. Then choose DF large enough that each
non-vacuum sector contribution is at most `V F_a(m_A)` on the first
three boxes. These are finitely many strict exponential bounds with
positive coefficients of DF, so such a choice exists. On the third box,

`g_pre<=8b^3 F_a(m_A)<=16b^3 exp(-a m_A)`.

On the final cube `g_post>=8b^3 F_a(m_B)>=8b^3 exp(-a m_B)`.
Thus `g_post/g_pre >= exp(a(m_A-m_B))/2`, exceeding any prescribed k.
Taking `16b^3 exp(-a m_A)<=log(1+sigma)` also makes S_pre<=sigma.
The choices can make the initial seed arbitrarily small as well.
No displayed GUIDE number is needed.

The proposed all-free companion is valid on its own terms. For positive
extents it has, in the time variable, vacuum weights
`exp(-D_X bcd)` and eigenvalues `exp(E_X)`. Add the remaining weight
at eigenvalue zero to give Z(0)=1. Use the same oscillator transfers
and a vector supported on the sector vacua and that zero eigenspace.
This yields a four-axis symmetric all-free family and the indicated
single-periodic traces. It supplies no compatibility of two successive
periodic closures: the mixed family's crossed ring is still asymmetric.
Accordingly the counterexample refutes W'-ENG with the stated mixed
axioms, not W'-ENG for a single Wilson measure or for every conceivable
strengthening of row 898's class.

Also narrow line 130's “No finite test at the seed scale detects b_*”.
The suppressed sector contribution is nonzero. The construction proves
that the seed inequality alone does not control later boxes; it does
not make all exact finite seed-scale data indistinguishable. Likewise,
requiring H-DBL at every level does not prove that each level needs an
independent new input: a single uniform theorem could supply them all.

## 6. Theorem 2P': HOLDS, with its stated fixed-size coefficient input

Source: lines 183–194. The premise reused is check 909, lines 478–493:
for each fixed box Q and integer t>=3,
`g_beta(t;Q)=n_s(Q) u_beta^(4t)(1+O(u_beta^2))`,
where `u_beta=I_2(beta)/I_1(beta)` and n_s counts spatial plaquettes.
This is a finite-size small-beta statement, not a uniform ladder estimate.

Membership uses the actual Wilson normalization. In a free direction n,
rewrite its vector form as
`W_n=<K^(-1/2)1,(K^(1/2)B_0 K^(1/2))^n K^(-1/2)1>`.
The constant vector is a K-eigenvector of eigenvalue c_0(beta)^ell,
where ell is the number of slice links. Thus its squared norm is
`c_0(beta)^(-ell)<=1`. The volume factor only rescales eigenvalues;
Lemma DS applies to the wall factors.

The one-link Bessel series gives `u_beta=beta/4+O(beta^3)`; its derivative
at zero is positive. Hence the choices u_B=q u_A with fixed q>1 are
available at sufficiently small positive couplings. After fixing them,
set `Delta phi=L`, `Delta D=(7/12)b L`. The four sector differences are
the four nonzero coefficients in section 5 times `L b^3`, plus the
fixed differences of Wilson vacuum energies. Choose L last. It can
both enforce the claimed vacuum choices and make all unwanted sector
trace contributions `o(u_A^(4a))`, for example at most `u_A^(8a)`.
There are only finitely many boxes and times in this choice. The
source's phrase “as small as one likes” must be read with this relative
error requirement when taking its asymptotic limit.

Thus S on the pre-step box tends to zero, and

`g_post/g_pre -> [n_s((2b)^3)/n_s(2b,2b,b)] q^(4a) >= q^(4a)`.

Choosing `q^(4a)>2k` proves the first claim with a strict margin.
The gap claim also has the correct inequality direction: for normalized
positive eigenvalues with largest excited value rho_1,
`S(2a)<=rho_1^a S(a)`, so
`m<=log(S(a)/S(2a))/a`.
The B-sector coefficient at a and 2a therefore gives
`m_mix((2b)^3)<=4log(1/u_B)+o(1)`. The seed gives the proposed bound
`4log(1/u_A)-log(B n_s(b^3))/a+o(1)`. Choose
`q^(4a)>B n_s(b^3)` as well. The actual upper bound is strictly smaller.
This proves failure of the seed-only sharp conclusion for each B>0;
it does not contradict Theorem C with H-DBL included. As the source
correctly says, 2P' alone does not refute the weaker literal W'-ENG
bound with its fixed threshold s'.

## 7. Lemma DS: HOLDS; structural exclusion: HOLDS AFTER CORRECTION

Source: lines 165–167, 184–194, 198–216 and 239–252. In a free side b,
the wall factor scales spectral values by
`exp(-a D_X(c+d))` and spectral weights by `exp(-a D_X cd)<=1/2`.
The summed weight is therefore at most one. Time transfers form a
direct sum, preserving integer multiplicities. The argument in section 5
then proves super-multiplicativity. If the summands also have bounded
FW2 defects, their sum has such a defect, enlarged by the wall costs.
This proves the stated closure, not a claim that arbitrary direct sums
without the wall factors preserve (V).

For 2P', the surviving axis-exchange and ring claims can be checked
without the oscillator analogy. For a geometry with free-direction
set F define the two-sector weight by

`Z_mix = sum_X exp(phi_X V-D_X sum_(mu in F) V/n_mu) Z_betaX`.

This expression is invariant under permutations of axes and their
boundary labels. In two periodic directions a,n the scalar factor is
`exp(an[phi_X cd-D_X(c+d)])`; hence the rings are symmetric in a,n.
Each reflection-positive unnormalized form remains positive after
summing the sectors. Central twists and the even projection operate
sector by sector. If a nonnegative homogeneous Holder or chessboard
bound has the form `A_X<=product_i B_(iX)^theta_i`, with theta_i>=0
and sum theta_i=1, Holder over X gives exactly the same bound on sums.
These properties, taken alone with (T), (V), cannot imply H-DBL:
2P' satisfies them and violates it.

Keep the source's Step 6c qualification. A shared sector label gives
`sum_X z_X(B)^2` at a decoupled cut, rather than
`(sum_X z_X(B))^2`. The independent-box identity and the Wilson cut
interpolation are not preserved. Strict positivity improving the full
transfer is also lost. The static-label variants do not restore axis
exchange; the source explicitly says so. No written example here
establishes an obstruction using factorisation AND four-axis covariance
together. Nor does a counterexample prove that every possible repair
must be a particular “quantitative single-phase” theorem. The justified
necessary statement is: a successful proof needs some hypothesis not
satisfied by the applicable counterexample. A quantitative single-phase
estimate is a proposed sufficient route, not a proved necessary form.

Step 6c's restricted membership/fixed-box limit claims: HOLDS.
For 2P-tau, the label kernel has eigenvalues `1+exp(-a tau)` and
`1-exp(-a tau)`, both positive. Its displayed inverse quadratic form
is at most one by the stated wall-weight bounds. For the gauge variant,
each `C_j=c_j(beta_A)J+[c_j(beta_B)-c_j(beta_A)]ee^T` is positive by
the Bessel series. Schur products preserve this positivity. On constant
link functions the crossing operator dominates K_label since C_0-J
is positive; inverse order gives the same norm bound. As tau grows,
the common D_A wall term cancels from normalized spectra. Every
nonconstant label configuration on a connected fixed box then has at
least one broken bond and an additional cost tending to infinity.
There are finitely many label configurations, so the unwanted traces
vanish and the strict finite-box counterexample survives. This proves
the stated factorising static-label variants, not their missing axis
exchange or an obstruction with all properties combined.

## 8. Positive join excess at small beta: HOLDS

Source line 149. Using the same fixed-size coefficient as section 6,
write `R=(c-1)d+c(d-1)>0`. Direct plaquette counting gives

`n_s(b)=b(c-1)(d-1)+(b-1)R`,
`n_s(2b)-2n_s(b)=R`.

For fixed `a>=3` and `b,c,d>=2`, therefore
`g(a;2b,c,d)-2g(a;b,c,d)=R u^(4a)+O(u^(4a+2))>0`
for all sufficiently small positive beta (depending on these sizes).
This disproves k=2 even on these arbitrarily cold fixed boxes.
It proves no sign at order-one beta and no uniform small-beta cutoff
for the whole ladder. The statement `k=2+1/(b-1)` is only a leading
coefficient upper bound, as marked in the source; its exact finite-beta
validity does not follow from this expansion.

## Sources, limits and final disposition

The row-910 author is Claude Fable 5.2. The reused tube inputs are from
Claude Opus 5.5 (`gap-sc-box.md:49–78,118–175`), Claude Fable 5.2
(`gap-seed-sc.md:156–181`) and check 909's fixed-size justification
(`gap-fw-wilson-check-astra.md:411–493`). Their polymer count and tube
Haar moment were read, not claimed anew. The coefficient input supplies
only the finite boxes and times explicitly used in sections 6 and 8.

The SA-index README, chunk-01 rows for 1271–1347, chunk-02 rows for
GL3/GL8 and their neighbours, and obligations.md were consulted first.
Target terms also had no hits in its chunk files or CA full index.
The source passages actually read are SA 1271–1347, 2195–2243 and
2313–2336, at the supplied `31a47c543775` source revision. They provide
the conditional rooted polymer theorem and the positive convolution/
transfer construction. Credit Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of that text. No CA result beyond these
outline inputs is imported; no Balaban estimate is used. This is no
claim that a differently named account theorem cannot exist.

The check uses by-hand algebra, spectral inequalities and finite class
counts. No guide, numerical run, machine enumeration or formal checker
was used to discharge a statement. The U(1)/Z_2 transition assertions,
the proposed massive-phase kappa estimate and the finite-beta frozen-group
asymptotics remain ARGUED; this check does not promote them. The source's
unqualified Step 7 “passes” sentences must retain that qualification.
Nothing here proves Wilson doubling at order-one coupling, a gap there,
or the first-passage/limit-state obligations.

RESULT: HOLDS—Lemma J, H-DBL iff JOIN-TH, Theorem C', Lemma DS, Theorem 2P' given the fixed-size coefficient input, and positive fixed-size small-beta join excess. HOLDS AFTER CORRECTION—the ring-target wording, Theorem 2P's class/range and seed-data wording, and the structural exclusion's scope. FAILS—Step 4.3's unnormalized no-flux probability identity; its missing c_0 factor cancels in the thermal excess. The mixed-class counterexamples survive; Wilson JOIN-TH at order one remains open. Research check only; no status granted.
