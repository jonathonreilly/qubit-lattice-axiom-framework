# Repo search

Provenance: OpenAI / gpt-6-astra / xhigh; row 945; source checkout
`a872c6ee2ae0cde91ba0bd375f3bb6c35aab9300`; research-text check, not an audit.
This file grants no scientific status. The source under check is
`library/gap-sgstep-opus.md`, lines 1–508 at that commit.

The requested prior note `library/prior/gap-sgstep-check-astra.md` is absent.
`library/open-registry.md` has no match for `sgstep`, `SG-step`, `etohc`,
`hypercontract`, `HC-vac`, or `LSI-vac`. FINISH rows 944–945 assign this
author/check pair. This is a check of row 944, not a second attack on row 941.

Search in `/Users/jonreilly/Projects/Physics`: refs `origin/main`, `pr/10114`,
`pr/10133`, `pr/10134`, `pr/10141`; terms `SG-step|SGC|HC2|sub.?Gaussian|
hypercontractiv|gap-sgstep`. The first pass reached its 100-line cap, partly
because `HC2` also matches unrelated HC20–HC29 labels. It is discovery only.
Narrower searches and primary-source comparisons follow below.

The completed exact-target search used `SG-step|gap-sgstep|HC-vac|LSI-vac|
Corollary HC2|Hessian.{0,30}log.{0,10}Omega|lower Hessian bound.{0,30}score`
on all five refs, with head 80: no hits. A completed broader pass including
`semiconcav` found the following method antecedents. None supplies this
Wilson slice estimate. Other hits about a Villain or finite-clock *score
field* concern curvature scaling limits, not the conditional transition score.

Refs resolved for this check: `origin/main=3e13676f02af206100abfb2875521904e8f53cda`,
`pr/10114=f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`pr/10133=89faef229ff6e6bde42baad15ed8270c2f4087d8`,
`pr/10134=1e70c7211a2cdbc39001e619f1dd89db45e25851`,
`pr/10141=c73ad7b177d94f89ff37b77386936e3d52b48b05`.

| Primary hit read | Exact statement and proximity |
|---|---|
| `origin/main:docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:142–190` | In its supplied noncompact model, the action Hessian survives a linear tilt. Brascamp–Lieb gives `d² log E exp(sF(f))/ds² <= \|\|f\|\|²/(beta-alpha)`, hence `E exp(sF(f)) <= exp(s²\|\|f\|\|²/[2(beta-alpha)])`. This is the same tilt-and-integrate method as EF (2.1), with a different law and a convexity premise. Reuse the method; it supplies no Wilson vacuum bound. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/NODEA_RES55.md:188–220,302–310` (also found on `pr/10133`) | BL-TILT assumes a convex Euclidean domain, an H-convex potential, a centered quadratic-dominated tilt and `lambda_bar c_bar<1`. It concludes `E exp(lambda_bar a) <= det(I-lambda_bar B)^(-1/2)`. The proposed small-field conditional application remains ARGUED. This is related concentration under curvature control, not (SC) or the full compact slice law. |
| `origin/main:research/mass-gap/library/gap-skeleton-max.md:190–198` | B11 proposes a defective ground-state LSI plus uniform positivity improvement to obtain a cutoff-uniform small-torus gap. It names those estimates as the crux. It supplies neither SG-step nor a one-step proof. |

The older `prior/repo-search-2026-11-08.md` concerns the PI, GW, TPI, history
and localization targets. Its earlier-ref results are not evidence for this
new score claim. The fresh searches above are the relevant coverage.

The index was searched first, including neighbouring rows of chunks 02 and
25, `obligations.md`, and `ca-full/index.tsv`. Direct source reads then gave:

- Outline 2313–2335: the positive trace-class gauge-projected transfer
  operator and `Z_s(0)=Tr L^s` (GL8). This is the existing transfer framework.
- Outline 27493–27529: GCB20–21 dominate linear statistics of the cutoff
  Gaussian law using an even log-concave conditional weight. This is already
  proved there and is not reproved here.
- CA-II 81161–81195 and 81804–81861: the coercive convex-window hypotheses
  and Corollary 8.3:cor-subgaussian-tails. Linear tilting preserves their
  coercivity; their bound is `log nu_H exp(s(F-nu_H F)) <= s²|ell|²/(2 lambda)`.
  The compact Wilson slice law has not been shown to meet those hypotheses.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for those sources; row 931 for the chain and consumers; row 940
and check 942 for E-to-HC and the corrected seed threshold. The local SA
folder has no git metadata: `31a47c543775` is the supplied provenance, not
an independently resolved local HEAD. These bounded searches locate no
duplicate of this check. They do not establish the author's global claim
that the entire account contains no ground-state Hessian bound.

Checkpoint: all seven planned steps are complete. The unresolved Wilson
inputs and the one-box consumer are recorded below. No separate proof
attack or numerical experiment was run.

## Consumer and volume dependence — checked

**Lines 63–73: HOLDS AFTER CORRECTION.** The E-to-HC rate and the two
thresholds are copied correctly from check 942. Require `alpha,sigma>0`,
a smooth *strictly positive* envelope s in HC2, and even integer `a>2`.
For other integer a use `2 floor((a-2)/2)` in place of `a-2`.
The prior SGC correction is the entropy-zero limit `theta down to 0`;
this note neither repeats nor depends on the erroneous limit.

**Lines 74–77, necessity of a box-free sigma: FAILS.** Let
`D(a)=log(72 beta 24³/x)+3 log a`, with x the selected threshold. What the
consumer actually asks on its one box is

`alpha(a)/sigma(a)² >= exp(2D(a)/(a-2))-1`.

For large a the right side is of order `(log a)/a`. For example,
`alpha(a)=1`, `sigma(a)²=sqrt(a)` meet this numerical requirement eventually:
`log(1+t)>=t/2` for `0<=t<=1` gives
`alpha'(a)(a-2)>=(a-2)/(4 sqrt(a))`, which dominates D(a).
This is a counterexample to the claimed *necessary constant scaling*, not
a construction of a Wilson measure with these constants. A box-free ratio
is sufficient; it is not necessary. With bounded alpha and
`sigma²>=c(24a)³`, the sufficient criterion fails for all sufficiently large
a. That asymptotic statement does not prove failure at **every** a, nor
failure of the seed itself when this upper-bound method is inadequate.

**CONS, lines 209–222: HOLDS AFTER CORRECTION.** Write the *optimal global*
score proxy as `Sigma²=sup_u sigma(u)²`. Then `g_tilde=c g` meets SG-tilde
iff `c>=Sigma²`; an arbitrarily chosen valid proxy need not be optimal.
The guaranteed LSI constant rescales as `alpha/c` (the optimal one does too).
No constant rescaling improves this ratio. The product-law l1 obstruction
is correct: linearize the dual-norm LSI at `1+epsilon sum_l(c(u_l)-rho c)`.
It yields `Nv<=1/alpha_inf`. The trace claim is also true: fix a unit
direction in each link, average `Q(sum_l epsilon_l e_l)>=N²` over signs,
and then over three orthonormal choices per link. In fact `tr Q>=3N²`,
stronger than the printed `N²`. Neither trace alone nor the product test
proves an optimal weighted LSI bound for Wilson nu.

**Averaging, lines 224–235 and 484/508: HOLDS AFTER CORRECTION.** RD requires
control along all comparison geodesics. A bound on `E_nu sigma(u)²` alone
does not enter its proof. The actual averaged estimates in row 931 are
`E_nu[Gamma(u) Var_pi_u(f)]` and
`E_nu[sigma(u)² Ent_pi_u(h)]`. These are weighted by the test function's
conditional fluctuation, not products of separate averages. They yield
the claimed contraction only after bounding these products appropriately.
No averaged route to HC is excluded by this observation. Delete the
unsupported parenthesis about typical midpoints' mean plaquette, and replace
“the averaged form does not repair this” by “no repair is proved here”.

## Algebraic statements — checked by hand

All line references in this and later sections refer to the author file.
These verdicts cover the displayed proofs and their repeated summary rows.

| Statement and source lines | Verdict | Check or required correction |
|---|---|---|
| Setting and centered score, 44–60 | HOLDS | Normalize Omega in L²(Haar). For finite beta and finite N, positivity and the eigenfunction equation make Omega smooth and positive. Differentiate `integral p(u,w) nu(dw)=1`. Full support and smooth local tangent frames justify the a.e.-to-every-u passage. |
| TG, 94–117; 479 | HOLDS | Haar change of variables `w'=g.w` gives the product marginal `dg pi_tilde_u`. The conditional mean of the centered raw score is exactly the projected score. Conditional Jensen gives convex domination, hence the SG-proxy inequality. Vertical directions have zero projected score. |
| EF (i)–(iii) and (2.1), 119–130; 480 | HOLDS | Direct differentiation of the finite Laplace transform gives its gradient and covariance Hessian. For either sign of lambda, the centered log MGF is `lambda² integral_0^1 (1-s) Hess A(u+s lambda z)[z,z] ds`. This proves both bounds in (2.1), with no unmentioned factor of two. |
| HV (2.2), 132–142; 481 | HOLDS | Along the product-sphere geodesic, `c_l''(0)=-\|z_l\|²u_l`. The chain rule yields exactly the printed radial correction, whose absolute value is at most `beta \|z\|²`. This is the **temporal-gauge** score variance. |
| HO, 144–152; 482 | HOLDS | For a tilted law on an interval of length D, variance is at most D²/4: subtract the interval midpoint and use that variance minimizes mean square error over constants. Integrating the log-MGF second derivative gives `lambda² D²/8`. Here `D=2 beta sum_l \|z_l\|`. No independence is used. `beta²N` is an upper bound, not a measured growth law for Wilson. |
| RS, 168–176 | HOLDS AFTER CORRECTION | Its positive eigenfunction and transition probability are correct. To meet the stationary **probability** convention, put `Z=integral R(kR) dU`, `Omega=sqrt(R kR/Z)`, and `nu=R(kR)dU/Z`. This does not change pi. The construction has no Wilson local magnetic potential or nontrivial local gauge projection. It tests compactness and bounded forces, not those additional Wilson structures. |
| DW, 178–192 | HOLDS | The two component masses are equal by reflection. Their conditional means of `<z,w>` are opposite and have magnitude `c_epsilon sqrt(N/2)`. Total variance gives the stated lower bound. Concentration of each spherical exponential density near its pole gives `c_epsilon ->1` for fixed beta as epsilon goes to zero. |
| DW's explicit `0.15 beta²N`, 193–194, 483, 508 | HOLDS AFTER CORRECTION | The approximate Bessel evaluation was not a proof of a lower bound. The hand certificate below proves the asserted number at `epsilon=1/beta`, `beta=23/10`. |
| HSS, 239–244; 485 | HOLDS | Taylor's formula gives `p(exp_u(tz),w)/p(u,w) >= exp(t phi-Ht²/2)`. Integrate against pi_u. Completeness supplies the geodesic for every real t. For negative t the integral remainder still has nonnegative weight after reversing endpoints. No stationarity or reversibility is needed for this lemma. |
| SC and SC-Omega, 248–260; 486 | HOLDS | Log-integral differentiation adds a nonnegative gauge variance. The remaining kinetic Hessian is at least `-beta g`. Four factors per plaquette and four spatial plaquettes per link give `\|Hess V[z,z]\|<=16 beta \|z\|²`; thus `Hess(V/2)<=8 beta g` and the constants are `C_F+beta`, `C_Omega+9 beta`. These are implications, not established Wilson bounds. |
| Temporal-gauge converse, 262–270; 487 | HOLDS AFTER CORRECTION | Define `C_* = sup_{u,\|z\|=1} Hess F(u)[z,z]`. Then `C_*-beta <= sup_u sigma_tilde(u)² <= C_*+beta`. The lower inequality fails for an arbitrary loose choice of `C_F` in SC. The box-free equivalence, and its temporal electric-covariance interpretation, are correct with the optimal constant. |
| CEN, 272–278; 489 | HOLDS | At a central slice the stabilizer contains constant SU(2) conjugations. A linear functional fixed by all those rotations vanishes. At a common-U(1) slice the same argument removes the components outside its Cartan direction. It does not assert that the remaining Cartan components are nonzero. |
| CEN consequence, 279–284 | HOLDS AFTER CORRECTION | The exact total-variance identity is `Var(psi)=Var(phi)+E Var(psi\|w)`. At a central slice the first term on the right is zero. `sigma_tilde²` is an MGF proxy, not in general this variance. The equality is an averaged cancellation of variance, not a pointwise Hessian cancellation along a whole geodesic. The proposed ordering scenario remains hypothetical. |
| Bakry–Emery implication, 286–289; 490 | HOLDS AFTER CORRECTION | Require `CD(kappa,infinity)` with **kappa>=0** (positive kappa for the proposed LSI route). Since `Ric=2g`, it implies `Hess log Omega <= (1-kappa/2)g <= g`, hence `sigma²<=1+9 beta`. An LSI without this curvature hypothesis does not supply that Hessian bound. |
| Per-link bound, 296–297 | HOLDS | The tangent projection of `grad_l A=beta E w_l` has norm at most beta. The adjoining semiclassical assertions are not consequences of this bound. |
| EXP, 305–315; 488 | HOLDS AFTER CORRECTION | The exact identity and its iff reformulation of SG-step hold. The expression for `-h` has the printed signs. Keep the central-slice cancellation in the averaged/infinitesimal sense just stated; it is not pointwise cancellation for every w or every point of the geodesic. |

**Hand certificate for the DW number.** Define
`A(r)=E_r t` on S³, with density proportional to `exp(rt)` and t its first
coordinate. Spherical integration by parts gives
`r(1-E_r t²)=3A(r)`, so `A'=1-A²-3A/r`. Also `A(r)>0` for r>0, by pairing
t and -t in the integral. For `b(r)=1-3/(2r)`, b is nonpositive up to 3/2.
At any contact with b beyond 3/2,
`A'-b'=3/(4r²)>0`. A first downward crossing is therefore impossible:
`A(r)>1-3/(2r)` for r>3/2.

Here `d=sqrt(5+2sqrt(2))<14/5`, `r=(23/10)d`, and
`c_epsilon=2A(r)/d`. The function `2/d-30/(23d²)` decreases for
`d>30/23`; our d is in that range. Consequently

`c_epsilon > 2/d-30/(23d²) > 1235/2254`.

Finally `10·1235²=15,252,250 > 15,241,548=3·2254²`. Hence
`c_epsilon²/2>3/20=0.15`. This repairs the proof of the stated number without
a Bessel evaluation or a run. It adds no Wilson conclusion to the example.

**Scope of the reduction.** Lines 317–321 correctly leave the actual Wilson
input open. The implications are `SC => uniform HSS hypothesis => SG-step`;
EXP is a restatement of SG-step, not a weaker unsupplied estimate. No reverse
implication from the projected score to SC was proved. Lines 298–303 and
496–499 overstate the interpretation: bounded susceptibility is not the
same statement as spatial strong mixing, and failure has not been proved
equivalent to two classical extensions tying. These are proposed mechanisms.
They must not become premises or exclusion claims in the next lane.

The ARGUED martingale paragraph (199–207) is not a proved supplier. Its
displayed infinity-norm bound already fails for one non-symmetric bounded
variable: if `X in [-1,1]` has positive mean and full support, then
`||X-E X||_infinity=1+E X>1`. Such a law occurs by a smooth positive tilt on
one sphere. Conditional *range* bounds, with properly defined influences,
can be used instead, but those estimates must be stated and proved. A crude
Dobrushin sufficient criterion failing at beta 2.3 does not prove that every
possible weak-dependence criterion fails there.

## Fact tests

**Photon, 79–80, 154–157, 325–330, 491: HOLDS AFTER CORRECTION of conventions
and scope.** For beta>0 and omega>0 write the displayed kernel as

`T(q,q')=exp(beta q q' - beta cosh(omega)(q²+q'²)/2)`.

Multiplication by `Omega(q')=exp(-beta sinh(omega) q'²/2)` leaves conditional
precision `beta e^omega` and mean `e^(-omega)q`. Therefore

`phi=beta(q'-e^(-omega)q)`,
`log E_pi_q exp(t phi)=t² beta e^(-omega)/2`.

This checks the required constant independently by completing the square.
In line 326, `V/2` must mean the **effective half-potential after absorbing
the two diagonal kinetic terms** into it. It is then
`beta cosh(omega)q²/2`, and `Hess F=beta e^(-omega)` is correct. If V keeps
its original magnetic meaning, `Hess F=beta(e^(-omega)-1)` and the kinetic
Hessian contributes the missing beta. Both conventions give the same score.

For positive-frequency modes the score covariance is diagonal, with largest
eigenvalue at most beta. Frequencies tending to zero make the corresponding
gap tend to zero. Thus SG-step alone gives **no volume-uniform gap**. This
does not assert a zero gap for a single positive-frequency mode, nor use
the nonnormalizable omega=0 Gaussian vacuum. It also says nothing new about
the compact toron factor excluded in check 942.

**Compact U(1), 331–336: HOLDS for the S¹ structural identities; FAILS for
the claimed assignment of its failure to LSI-vac alone.** The tangent,
kinetic-Hessian and plaquette calculations carry over to unit S¹, and HO
gives the finite-box bound `sigma²<=beta²N`. The note correctly leaves a
box-free compact-Wilson SG estimate open. But the formula
`alpha<=2 beta sinh(omega_min)` cited next is proved for the Gaussian photon
model. It is not a proved bound for compact Wilson U(1), and an open SG input
cannot be asserted to be innocent of every failure. The corrected statement
is: *the Gaussian photon test fails through its LSI rate while its score
proxy stays bounded; the compact-Wilson allocation is not established here.*

**Frozen Q_8 and 2T, 337–339: HOLDS as a domain exclusion.** These finite
configuration spaces are outside the connected-manifold differential
setting of HC1/HC2. No discrete replacement for the score or its metric was
defined or checked. Reading a derivative inequality on a zero-dimensional
space vacuously would not help: the zero-gradient LSI fails for nonconstant
functions. The requested positive assertion that frozen groups satisfy an
applicable quantitative SG analogue is therefore **not supplied**.

**SMALL-BOX, 340–342: HOLDS as a non-implication, not a new estimate.** No
SC or SG bound at large beta is proved there. Such a score bound would not
by itself contradict a small gap. The near-Gaussian description is heuristic.

**FT-CEIL, 343–350: HOLDS for the conditioning distinction.** The source
`gap-z2parity-astra.md:130–137,386–442` fixes the SO(3) coordinates of **all**
links, reduces the identity environment to Z₂, and proves its flux test by
the condition `80 exp(-2 beta)<1`. This is not conditioning on one boundary
slice and integrating the future. The prior check's exact threshold is
`beta>log(80)/2`; 2.191 is rounded. It is not an SG refutation. The numerical
ceilings themselves are not premises of any checked lemma here, and were
not recomputed. The claim about a pinned flux implying rigidity remains
ARGUED, not a fact established by this comparison.

**Group-blindness, 351–354: HOLDS AFTER CORRECTION of its domain.** HSS and
EXP are manifold statements. TG is a compact-group averaging statement.
The literal EF/HV/DW formulas use the specified spherical embedding, and
the kinetic Hessian `-beta<u,w>g` is the unit-sphere formula. They hold as
written on S³ and, for the indicated analogues, S¹. An arbitrary compact
connected group needs a chosen representation and its kinetic curvature
bound; changing only the plaquette constant does not make every displayed
formula verbatim. The SU(2) central-slice argument uses the absence of fixed
adjoint vectors. None of these implications selects the SU(2) mass gap.

## GUIDE: stated model, arithmetic, and unavailable artifacts

**Model at 360–369: HOLDS as a description of a finite slab.** The printed
weight is the temporal-gauge transfer product with the terminal half-weight.
After integrating slices 2 through T, the slice-1 density is proportional to

`k(u,w) exp(-V(w)/2) (T_0^(T-1) 1)(w)`,

where `T_0=exp(-V/2) k exp(-V/2)` is the unprojected operator. Its positive
ground state is gauge invariant; on that sector it agrees with the
projected operator's ground state. At fixed finite spatial box, the
normalized positive transfer iteration tends to Omega. This verifies the
stated T-to-infinity target, not that T=6 has reached it uniformly in L.

For even L the stated signs give plaquette -1 in all three spatial planes.
Translations change this boundary by central gauge transformations. Global
conjugation gives zero electric mean and identical colour covariances.
Thus the Fourier normalization `1/(3L³)` and the stated covariance-to-Hessian
inequality are correct for the exact finite-slab law, with F replaced by
its finite-slab log-partition function. They apply to the vacuum F only
after the transfer limit. This distinction persists at the numeric precision.

**Printed arithmetic at 425–441 and 455–465: HOLDS to its stated rounding.**
From the supplied table,

- `4453/4503` lies between 0.988 and 0.990 (the reported 0.989).
- `5496/6069` lies between 0.905 and 0.906 (0.91 to two decimals).
- `3011/2991` lies between 1.006 and 1.007.
- The hot/cold differences at L=6 and 10 are less than one percent of cold.
- Relative to T=6, the T=4 and T=8 deviations are below 2.5 percent.
- `1-3(0.2253)=0.3241<0.57²`. With lambda about 0.45 and beta=2.3,
  `beta² lambda ±0.57 beta` gives the reported rough interval 1.1–3.7.
- `9L³` equals 576, 1944 and 4608 for L=4,6,8. For `d/n=576/10000`,
  `(1+sqrt(d/n))²=(1+0.24)²=1.5376`; `0.450·1.5376=0.69192`, close to 0.690.

These are checks of printed arithmetic, not verification of the measured
covariances, error bars, resources, sampler or equilibrium.

**GUIDE inference, 370–377 and 434–469: HOLDS AFTER CORRECTION.** The safe
central-slice finding is “the reported finite-slab estimates show no growth
on the tested sizes.” A finite ratio G>=4 would not prove unbounded growth
as L tends to infinity, and hence would not establish “SC FAILS” or kill
that route. Likewise agreement at three slab depths is a diagnostic, not
a bound on the error from replacing Omega. “Box-free susceptibility” and
“the mechanism does not occur” must remain descriptions of the observed
finite-size estimates, not mathematical conclusions.

The split-sample interpretation needs a further correction. For an
independently chosen unit v, `v^T Sigma v<=lambda_max(Sigma)` holds for the
**population** covariance. An unbiased estimate of that Rayleigh quotient
is not a certified lower bound: it can overshoot through sampling noise.
Consecutive halves of an MCMC run are not established to be independent.
Even a genuine lower bound that stays flat supplies no upper bound of
order 0.3–0.5 on the top eigenvalue. The Marchenko–Pastur arithmetic is
correct, but its noise-edge interpretation is not proved for this correlated,
non-isotropic sample. Retain only the reported flat tested-direction values.

**Run provenance, 378, 419–423, 446–453, 473–475, 493, 505: HOLDS AFTER
CORRECTION to an explicitly unverified author report.** The allowed checkout
contains neither `slab_E.py` nor `slab_E.log` nor `slab_rand.log`. The stated
paths refer to the author's Mac-mini `/tmp/gap-sgstep-944/`, not supplied
artifacts here. Existing /tmp directories or another machine were not
searched. Run execution, sampler validation, sweep counts, controls and
resource claims are **not verified**. No new GUIDE run was performed.

## Coverage and disposition

Checked line by line by Codex, by written arguments. The first substantive
failure is lines 74–77: the asserted necessity of a box-free score constant.
The algebra after it is logically independent and was checked separately.
Every PROVED or conditional implication in the author text is covered above;
the result-table rows 479–494 repeat those same statements. Section 7's
source attributions hold for the bounded passages read. Its statements that
the Wilson law “has neither” convexity property, or that the entire account
has no such estimate, must instead say that the needed hypothesis or bound
has **not been supplied by these reads**. Recalled literature and ARGUED
physical mechanisms were not promoted to theorems.

The material corrections, ranked by their effect, are:

1. The required ratio is the explicit one-box seed inequality. Volume-free
   constants are sufficient, not necessary; asymptotic failure is not
   failure at every box size.
2. The compact-U(1) failure attribution is unsupported, and the frozen-group
   test is a domain exclusion. The Gaussian photon calculation remains exact.
3. SC is sufficient for the projected score and equivalent to bounded
   temporal susceptibility. It does not establish spatial strong mixing or
   characterize failure by classical two-phase coexistence.
4. HC2 needs a positive metric and a weighted LSI; an average of local
   proxies alone supplies neither. Constant metric scaling changes no ratio.
5. The two-sided SC estimate and the CONS “iff” need optimal constants.
   CEN's cancellation concerns variance in expectation, not a pointwise
   Hessian cancellation or equality of variance and MGF proxy.
6. Normalize RS's stationary probability, specify the photon's effective
   half-potential, keep integer-time/positive-curvature hypotheses, and
   restrict the literal group formulas to their stated geometric models.
7. Use the displayed hand certificate for DW's 0.15 constant. The ARGUED
   martingale infinity-norm bound cannot be used as written.
8. Restrict GUIDE conclusions to reported finite-slab estimates. Split-sample
   values are not certified lower bounds or upper bounds on the top
   eigenvalue. The raw runs and their receipts remain unverified.

The author's final RESULT is **HOLDS AFTER CORRECTION** to these scopes.
In particular its phrase “its variance is the Hessian” must refer to the
**temporal-gauge** score. At a central slice the projected variance is zero,
while a nonzero temporal linear score has positive variance under the
strictly positive density; they cannot be interchanged.

What this delivers: checked elementary reductions and a bounded-force
counterexample for general reversible chains. What it does not deliver:
SG-step, SC, the HC2 weighted LSI pair, or a sufficient one-box seed estimate
for SU(2) Wilson at beta 2.3–2.6. Those remain open and retain their owners.
Only this requested output file was changed. No audit, registry, FINISH row,
source proof, remote ref or scientific status was changed.

RESULT: HOLDS for TG, EF, HV, HO, HSS, the conditional SC implication and CEN; HOLDS AFTER CORRECTION for RS normalization, DW's numerical proof, optimal-constant conventions, EXP's interpretation and the fact-test/GUIDE scopes; FAILS for the claimed necessity of a box-free sigma and for assigning compact U(1)'s failure to LSI-vac alone. The Gaussian photon proxy is exactly beta exp(-omega). SU(2) SG-step and the seed remain OPEN; raw GUIDE runs are unverified; this research-text check grants no status.
