<!-- Reconstructed by the lead (Claude Opus 5.5) on 2026-11-14 from the Codex event log ~/ym4d-lead/logs/gap-oddgap-check-astra.jsonl. The laptop runner lost the written file (the lead queued it with a wrong output path, and the next checkout cleaned the tree). This text is Codex's own full read of its report (sed ranges 1, 221); Codex made 1 small edit(s) AFTER that read, whose content the log does not record. So the body may differ slightly from the final version. Final RESULT line (from Codex's own tail, if logged) and final message follow at the end. -->

## Repo search

Terms: `odd[-_ ]gap`, `lambda_odd`, `VAR-SLAB`, `odd[- ]Poincar`,
`force[- ]covariance`, `twist-eating`; then `toron`,
`Fisher.{0,20}(flux|twist)`, `conditional cut gap`, `cut tensorization`,
`commuting quadruples`. Refs: `origin/main`, `pr/10114`, `pr/10133`,
`pr/10134`, `pr/10141` in `/Users/jonreilly/Projects/Physics`.
Each search was one bounded `git grep`, piped to `head` (100 and 60 lines).
The first completed across all refs; the second reached its output cap in
pr/10114, so it proves no absence on the later refs.

Relevant source lines read:

| Source | Exact statement and closeness |
|---|---|
| `origin/main:research/mass-gap/library/gap-skeleton-final.md:69–88` | The sheet-twisted action has an explicit zero-action configuration with seam holonomies `i sigma_1`, `i sigma_2`. This is prior work for F1's twist eater. It does not count frozen-group quadruples or give the odd two-slice gap. |
| `origin/main:docs/COMPACT_U1_WILSON_TO_SOURCE_FREE_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-02.md:246–275` | At spatial momentum zero and nonzero time momentum there are three toron directions; at full zero momentum four flat holonomies remain. Related mode distinction, not G1–G4's compact rotor law. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md:3193–3212` | Flat configurations have commuting cycle holonomies; the sector-wise covariance estimate WC-tor is explicitly OPEN. Different sector and observable; it does not supply this check's target. |

Other first-query hits concern PMNS parameters, unrelated composite-particle
gaps and stress covariance, or the same thin-torus route's chart/port notes.
No matching odd-gap theorem was found by the completed first query.
`library/open-registry.md` has no match for the odd-gap, VAR-SLAB,
force-covariance or gap-fr terms. This is row 933's assigned check, not a new
attack on another owner's open lemma. The requested target-specific prior
note is absent. The older `prior/repo-search-2026-11-08.md` concerns the RG
suppliers, not this target.

Provenance: OpenAI / gpt-6-astra / xhigh, 2026-11-14; checking
`gap-oddgap-max.md` at `5fd05813957ae35266ae03c2282ae17590d94d9c`.
Research text, not an audit; grants no status. Only this report is edited.
Source authors: Claude Fable 5.2 (row 930), Claude Opus 5.5 (row 922),
and Ethan Sussman and Levent Alpoge (outline/account, with Claude and Codex).

The SA-index README, chunk-02 neighbouring rows 90–104 and its obligations
locate SA 2313–2394, read from the pinned source copy. GL8 supplies the
positive gauge-averaged transfer trace; GL10 is a contraction insertion
bound. Neither passage supplies this note's odd-gap estimate. These existing
transfer results are used with credit, not re-derived. No Balaban import is
needed for this finite-cutoff check.

## Checkpoint

Source read in full (620 lines). Check order: (1) G1–G4 and numerical claims;
(2) frozen counts and heat-bath form; (3) Theorem R and its tests;
(4) susceptibility, CUT, RARE and ceilings; (5) consolidated verdict map.
Runs, if any, are GUIDE only. Written arguments decide mathematical verdicts.
Completed: Gaussian identities and hand bounds, frozen counts, contraction,
conditional cuts, susceptibility, ceilings and GUIDE arithmetic. Final
disposition is in section 6. Source revision remains the pinned commit;
no scientific supplier has been closed. Open obligations remain CUT-TYP,
LSI-weak, the averaged force-covariance bound and cutoff uniformity.

## 1. Step A: Gaussian model

**G1, lines 104–151: HOLDS**, on the stated monopole-free, zero-spatial-flux
model, after fixing the harmless gauge-volume and kernel normalization.
Work on the gauge quotient, or normalize the compact exact-gauge factor.
The closed integer lattice has harmonic periods in `2 pi Z^3`.
The cut cochain has harmonic projection `1_i/L_i`; its remainder is exact.
Thus the harmonic quadratic cost is
`beta |B| (Delta Phi_i-2 pi w_i)^2/(2 L_i^2)`.
Periodization gives rotor eigenvalues `exp(-E_i e^2)`,
`E_i=L_i^2/(2 beta |B|)`. Constants in the kernel can be absorbed into P_s;
they cancel from every ratio here. Orthogonality also gives
`|grad Phi_1|^2=L_1/N=kappa`. The transverse kernel and the other two rotors
cancel from R and X and tensor out of the odd variational problem.
This is not a result for full Villain U(1) with monopoles or for noncompact
holonomies on the real line (where this finite rotor trace is unavailable).

The sentence at lines 122–124 needs one qualification: I1–I3 follow from
the stated kernel symmetries and regularity. I5 additionally uses the
differentiable first-step slab factorization and its score, which Model G
does have. An arbitrary symmetric kernel alone does not specify that force.

**G2, lines 153–168: HOLDS.** The odd rotor trace is precisely the printed
odd-integer sum. Poisson summation gives
`1/2-p=(y+y^9+y^25+...)/(1+2y^4+2y^16+...)`.
For `0<y<=1/2`, the denominator is at most `1+4y^4`, and
the numerator is at most `y(1+2y^8)` by geometric tails.
This proves both hand bounds, including the seed and beta=2.3 cube bounds.
The seed's `tau=5/92`, `kappa=1/20` and `y=exp(-2.3 pi^2)` are correct.
The displayed decimal equality for p is an approximation, as its GUIDE
column indicates, not an exact decimal value.

**G3, lines 170–198: HOLDS.** Direct logarithmic differentiation gives
the stated formula for X'. Monotonicity of the image mean m, together with
`m(0)=0`, `m(pi)=1/2`, proves the global bound `|X'|<=pi/(2 tau)`.
For clarity, the small-tau tail estimate can be checked without quadrature.
Put `H(x)=sum_n exp(-(x-2 pi n)^2/(4 tau))`. Then
`integral_circle H^2 >= sqrt(2 pi tau)` by retaining the squared images.
On `|x|<=tau`, `H(x)^2<=1.003`; the image tails are geometric.
For `tau<=1/16`, completing squares in the two nearest images and applying
`integral_b^infinity exp(-x^2/(2 tau)) dx <= (tau/b) exp(-b^2/(2 tau))`
gives
`integral_(pi/2)^pi H^2 <= 1.01 (2 tau/pi) y`.
Indeed the second image and cross term are bounded by
`[(tau/pi)+sqrt(2 pi tau)] y^4`; further images are smaller geometric tails.
Their ratio to `(2 tau/pi)y` is below one percent throughout this range.
Consequently the mass of `tau<=|psi|<=pi/2` exceeds 0.79.
The printed image-mean estimate there gives `X'>=0.82 pi/(2 tau)`;
`0.79(0.82)^2>1/2` proves the lower bound. These are written estimates,
not numerical integration certificates. The exact response is `kappa J`.
The seed interval `[20.8,41.8]` follows from the displayed rational
multiples of pi squared.

**G4, lines 200–233: HOLDS for its exact reduction and hand bounds.**
An odd function has zero conditional mean in the `(phi,phi')` factor at
each value of the other coordinates. Apply its odd inequality fibrewise;
the other gradient energies are nonnegative. Tests independent of those
coordinates give the converse. Thus `lambda_odd=kappa mu_odd` exactly.
The uniform phi' marginal makes `cos phi'` have quotient 1.
For the R test, its quotient is `2D/V`. The preceding tail estimate gives
`D <= [4.04 pi/sqrt(2 pi)] tau^(-3/2)y < 5.1 tau^(-3/2)y`;
`V>1-4.1y` makes `2D/V<10.3 tau^(-3/2)y` on `tau<=1/16`.
At the seed, `tau^(-3/2)<79` and `y<2e-10`, proving `<8.2e-9`.

The Fourier-sector structure at lines 228–233 also **HOLDS**: total
Fourier charge M is conserved, and its form has the additive term `M^2/2`.
Retain the torus compatibility conditions on the remaining psi function.
Thus nonzero-M sectors have bottom at least 1/2. The M=0 trial bound is
below 1/2 in the small-tau range, so the full bottom equals mu_0 there.
The limit `mu_odd -> 1` follows by uniform convergence of the density to
the constant density. The written `1+o(1)` coefficient and claim that R
is almost the eigenfunction are ARGUED, not a proved asymptotic theorem.

**Step-A interpretation, lines 336–374: HOLDS AFTER CORRECTION.**
At the seed both response and gap violate the proposed order-L_1 targets.
Frozen groups below likewise disqualify response smallness alone.
For cubes, however, `FR<=4 pi^2 beta^2/L` proves only a *sufficient*
passing size against `2p_*(3L)`. It cannot prove failure below that size.
The sufficient inequality is `L^2 >= 2 pi^2 beta^2/(3p_*)`.
At `p_*=2e-4`, L=420 suffices at beta=2.3; it does not suffice at beta=2.6
(L=475 suffices). At `p_*=1e-4`, L=594 and 672 respectively suffice.
These safe integers follow using `pi^2<10`; the sharper approximate
thresholds must retain their chosen beta and p_*.

Also `lambda<=L_1/N` fails a demand `lambda>=c L_1` when `c>1/N`.
It does not fail *every* positive proposed lower bound. Nor does Model G
fail the flux half at every coupling: at fixed box, beta tends to zero
and the exact odd trace tends to zero. The all-coupling assertion is valid
only as rejection of that specified order-L_1 lower bound. The stated
Coulomb-window fact test survives these corrections.

## 2. Frozen groups

**F1, lines 259–294: HOLDS.** The omitted bijection can be supplied directly.
For each quadruple, put h_i on the direction-i seam and 1 on other links.
All plaquettes are 1 except the double (0,1) seam, where the value is -1.
Commuting other pairs ensure every other seam intersection is flat.
Conversely, fix a root and a spanning tree. With the tree values fixed,
transport along a path is determined by the four based cycle holonomies:
exchanging adjacent steps inserts the prescribed central plaquette value,
and contracting a cell-boundary path inserts 1. The torus cell relations
are precisely the six stated commutators. This recovers every link and
proves uniqueness. There are `|G|^(#sites-1)` tree assignments in both
ensembles, and the normalized Haar factors also cancel. This uses the
prior seam twist eater credited in Repo search, not a new wall mechanism.

For Q_8 and 2T, distinct maximal abelian subgroups intersect in `{+-1}`.
A noncentral commuting tuple therefore belongs to exactly one of them.
This gives `N_0=16+3(256-16)=736` and
`N_0=16+3(256-16)+4(1296-16)=5856`.
If ab=-ba, conjugation changes each element to its negative; both traces
vanish. The only trace-zero elements in these groups are `+-i,+-j,+-k`.
Each of six choices anticommutes with four others. Their common centralizer
is `{+-1}`, leaving four choices for `(h_2,h_3)`. Hence `N_tw=96`,
`r=3/23,1/61`, `p=10/23,30/61`, and `p/(1-p)=10/13,30/31`.
The pair-count checks `40=8*5`, `168=24*7` and the Z_2 row are correct.

**F2, lines 302–322: HOLDS for the stated single-link heat-bath form at
beta=infinity and sides at least 3.** Each link is fixed by a spatial
plaquette and its other three conditioned links. Every conditional
variance is zero. Nonconstant odd holonomy functions remain, so the odd
gap is zero. No division by that zero gap is allowed. This is distinct
from a heat bath that updates an entire cut at once.

The local excitation costs `6 beta` and `3 beta` follow from the six
plaquettes incident to an isolated changed link in four dimensions.
They do not prove a finite-beta cluster expansion or a tunnelling estimate.
The ARGUED finite-beta conclusions at lines 296–300 and 324–329 remain
unproved; the text supplies neither a Peierls bound nor a freezing-temperature
source. Their recalled decimal temperature is not verified here.

## 3. Theorem R and its consumer

**Definitions and R1–R3, lines 381–412: HOLDS**, with a differentiable
Markov slab, the first-layer score convention in I5, positive gaps and
finite covariance bounds when division is used. Kernel symmetry alone
would not supply the score identity. At beta=0 the trivial R=0 case is
handled separately from formulas dividing by beta.

Here is a direct check using the joint density of `(u,w_1,v)`:

`Z_e^(-1) E_(a-s)(u,v) A_1(u,w_1) E_(s-1)(w_1,v)`.

Its `(u,v)` marginal is `w_e^(s)` and its `(w_1,v)` marginal is
`w_e^(s-1)`. Conditional expectation of `R_(s-1)(w_1,v)` is R_s.
The conditional-variance identity therefore gives exactly
`E Var(M_1)=V_(s-1)-V_s`. All measures in this identity are normalized;
there is no substitution of a free endpoint law for a bridge law.
The score covariance is `grad_u R_s=beta Cov(F,M_1)`, since the endpoint
label's conditional mean given the first layer is M_1. Taking the norm
by duality gives `|grad_u R_s|^2<=beta^2 Gamma_s Var(M_1)`.
Slice-swap symmetry supplies the factor two in the full gradient.
The odd inequality and rearrangement now prove R2 and R3, including the
product starting at s=2 and `V_1<=1`.

**R4, lines 396–398 and 413–419: HOLDS.** Set `g=grad_u R_s`,
`v=Var(M_1)`, `q=1-R_s^2`, and let W denote the within-sector covariance
matrix. Bernoulli mixture algebra gives
`Cov(F)=W+gg^T/(beta^2 q)`.
Apply the preceding Cauchy–Schwarz inequality in direction `g/|g|`:
`|g|^2<=beta^2 ||W|| v+|g|^2 v/q`.
Since `q-v=E(1-M_1^2)>0` for a positive finite-thickness kernel with
s>=2, rearrangement is exactly the last R4 inequality. The response
lower bound follows from `grad log rho=-2g/q`. If g=0 it is immediate.

**Ising test, lines 421–425: HOLDS for R1.** In the ferromagnetic ring
`E_s=lambda_+^s/2`, and the first-spin conditional distribution is the
ordinary one-step kernel, since E_(s-1) is constant. Thus
`Var(M_1)=h^(2s-2)(1-h^2)` pointwise. This tests R1, not a differential
Poincare inequality on a discrete group. It cannot by itself test R2–R4.

**R5, lines 433–439: HOLDS AFTER CORRECTION of one rounded threshold.**
If `Q=[theta/(1+theta)]^4`, the exact consequence is `p<=Q/(1+Q)<=Q`.
For `theta<=1/9`, Q<=1e-4. The condition
`lambda_0>=95.3 Gamma_0` is safely stronger than the exact `95.22`.
The printed intermediate assertion `theta<=0.135` implies `p<=2e-4`
fails as arithmetic from the printed bound: at theta=27/200 it permits

`Q/(1+Q)=531441/2655769282 > 1/5000`,

as `5000*531441=2657205000` exceeds the denominator.
However the final condition `lambda_0>=78.4 Gamma_0` **does suffice**:
`theta<=529/3920`, `theta/(1+theta)<=529/4449<0.11892`, and
`0.11892^2<0.014142`, `0.014142^2<0.0002`.
Retain exact capacity bounds `Gamma_0<=60/95.3` or `60/78.4` when
using the ceiling 60. The numbers 0.63 and 0.76 are rounded descriptions,
not interchangeable exact sufficient inequalities. The ceiling itself
requires the stated assumption `q>=1/4`; ODD-0 alone proves it only
at beta=0. No such positive-coupling q bound is supplied here.

**R-sup, lines 448–455: HOLDS AFTER CORRECTION of range.** At
`tau_s<=1/16`, the image estimate at psi=pi/2 gives
`X'>=0.99 pi/(2 tau_s)`. Substitution in R4 proves
`Gamma_s^*>=0.98 pi^2 N/(4 s^2 L_1)` and the seed lower bound `48/s^2`.
This proves lack of a volume-free supremum for fixed beta,s,L_1 as N
increases. The derivative estimate is false for unrestricted tau_s:
as tau_s tends to infinity, X'(pi/2) is `4 exp(-tau_s)+O(exp(-2tau_s))`,
not of order `1/tau_s`. State the small-tau condition rather than
claiming this proof at every size and coupling.
Likewise G4's numerical half-torus gap bound is for w_e^(a/2);
its direct citation for all the unequal laws w_e^(s) at line 449 is not
an argument for those bounds. The general cos(Phi_1(v)) test still gives
`lambda_s<=kappa` for those laws. Neither qualification hurts the seed
half-torus test or the large-N obstruction just proved.

**Averaged covariance variant, lines 460–465: HOLDS**, with the
zero-denominator case stated. If `E Var(M_1)>0`, define Gamma_eff as
printed and substitute it in R2. If it is zero, the nondivided inequality
gives V_s=0 (when lambda_s>0); no Gamma_eff quotient is needed.
No upper bound on Gamma_eff for actual SU(2) is proved. The comments about
where its weight concentrates in Model G and about the SU(2) supremum
remain hypotheses, not consequences of R1–R4.

## 4. Susceptibility, cuts and rare environments

**6.1, lines 475–485, the SU(2) susceptibility implication: HOLDS.**
Each winding trace is centred by the centre flip. Distinct straight lines
use disjoint links, so the gradient Gram matrix is diagonal with entries
`L_1(1-q)`. Applying the odd inequality to an arbitrary real linear
combination gives the covariance-operator bound and the stated chi_P bound.
This is a necessary consequence of ODD-GAP, not its converse.

**6.1, lines 487–493, Model G: HOLDS for the finite-box identity and bound;
FAILS for the unqualified conclusion of long-range order and unbounded
susceptibility as N grows.** The photon variance v_L is finite in each
finite box. The text supplies no bound on its dependence on the box.
Finiteness does not make `(N/2)exp(-2v_L)` diverge.

There is a counterexample within the stated rectangular geometry. Fix
`L_1,a,L_3>=3` (a even), beta>0, and let `L_2=M` tend to infinity.
Keep only the independent Gaussian photon modes with momenta
`k_0=k_1=k_3=0`, `k_2!=0`, in the difference of two direction-1 line phases.
Writing their line phase as z_j, their action is exactly

`[beta a L_3/(2 L_1)] sum_j (z_(j+1)-z_j)^2`, `sum_j z_j=0`.

On a cycle, the variance of z_j-z_(j+d) is
`[L_1/(beta a L_3)] d(M-d)/M`.
This follows by solving the one-dimensional discrete Poisson equation:
the two paths of lengths d and M-d have conductances 1/d and 1/(M-d),
whose parallel resistance is d(M-d)/M. Independent omitted modes add
nonnegative variance. For `0<=d<=M/2`, the full cosine correlation is
therefore at most `exp(-c d)/2`, `c=L_1/(4 beta a L_3)>0`.
Summing over all transverse sites yields the uniform bound

`chi_P <= (L_3/2)[1+2/(exp(c)-1)]`.

Thus susceptibility need not grow with N, even at beta=2.3. The source's
finite-box lower bound is consistent with this: v_L grows in this family.
For growing square cross-sections, an additional estimate is needed;
the printed argument supplies none. This does **not** refute G4's soft
toron test, which already excludes the specified order-L_1 odd gap without
using winding-line susceptibility. Delete the unqualified “locked winding
lines violate bounded susceptibility” claim from the result line.

**CUT, lines 499–511: HOLDS.** Moving a centre cut differs by a central
gauge transformation on the strip between cuts. Gauge invariance therefore
makes every admissible F odd under each J_k, and makes each conditional
law J_k-invariant. Apply its odd Poincare inequality at fixed environment,
integrate and sum over disjoint cuts. This gives exactly
`D_v(F)>=E[F^2 sum_k gamma_k]` and hence
`lambda_s>=ess inf sum_k gamma_k`. No independence of the cuts is assumed.
At beta=0, cut Haar harmonics odd under the simultaneous sign have at
least one spin-1/2 factor, costing 3; a coordinate attains it. This
recovers the lower bound `3L_1`, with equality by I4's winding trace.

**CUT's Model G test, lines 515–520: HOLDS AFTER CORRECTION of the
“sharp up to 2” range.** On a lifted conditional cut, decompose its link
coordinates into their mean q and zero-sum differences. Uniform cut motion
is closed, so the coexact action and kernel do not depend on q. The toron
factor gives the same periodic density in psi for every environment.
The conditional derivative in q costs `1/N`. Fibrewise odd Poincare,
and tests depending on q alone, give
`gamma_k=mu_0(tau)/(2N)` at s=a/2. Thus CUT returns `kappa mu_0/2`.
It is half the true gap when the full odd bottom is mu_0, in particular
at the seed and for tau<=1/16. It is not always half the true gap:
as tau tends to infinity, `mu_0 -> 2` but `mu_odd -> 1`.
The source states the test at every half-torus without this small-tau
restriction. Its upper bound on gamma remains correct there.

**Uniform-rotation distinction, lines 521–531: HOLDS at its stated
algebraic scope.** The displayed plaquette transformation is correct.
If two transverse links do not commute, their common SU(2) centralizer
is `{+-1}`. A uniform right multiplication preserving each spatial
plaquette interaction must lie there. For U(1), every uniform cut angle
preserves the spatial action. This does not make it a symmetry of the
full conditional two-slice law: its toron kernel has the stated double
well. Nor does a discrete spatial stabilizer give a quantitative gap.
The source explicitly leaves nonuniform motions and the nonlocal kernel
unanalysed; those exclusions must remain.

**RARE, lines 538–557: HOLDS as a conditional implication**, with
`g_0,alpha>0`, `0<delta<1/2`. Normalize `m=E F^2` and put
`nu=F^2 w_e/m`. Binary relative entropy gives
`nu(Bad) log(1/w_e(Bad)) <= H(nu|w_e)+log 2`.
Use LSI for the entropy, and CUT for the mass on Bad's complement:

`m <= D/g_0 + [2D/alpha + (log 2)m]/log(1/delta)`.

Rearrangement is precisely the printed lower bound. If Bad is null,
CUT directly gives lambda_s>=g_0. With `delta=exp(-cN)` and
`alpha>=C g_0/(cN)`, the bound is
`g_0[1-log(2)/(cN)]/(1+2/C)`; “about g_0” means this order bound,
not an asymptotic equality. At the seed, the U(1) cut test makes the
proposed order-L_1 good-environment condition fail everywhere. The
single-link frozen-group form has zero conditional cut gaps and cannot
have a positive LSI constant either. Neither input is proved for SU(2).

**The stopping claims, lines 559–580: HOLDS only as records of attempts.**
No successful lower bound is asserted for CUT-TYP, LSI-weak or the
averaged force covariance. The recalled correlation length of the flat
two-dimensional cut model, and the costs of the proposed canonical paths,
are not established estimates in the given two-slice conditional law.
The loss of single-link flip symmetry at beta>0 is real; it prevents
using the beta=0 orthogonality argument unchanged, not every parity method.

## 5. Ceilings and GUIDE arithmetic

**Ceiling comparison, lines 467–469 and 565–568: HOLDS AFTER CORRECTION
of scope.** Existing hand calculations, read at their source locations,
give these distinct restrictions:

| Input read | Exact restriction |
|---|---|
| `gap-arealaw2-check-astra.md:57–78` | Six-neighbour single-site chord influence is `(beta/4)A`, so its weighted contraction test requires beta<2/3. This is not a universal Poincare ceiling, nor the numerical degree-four cut threshold. |
| `gap-blockcrit-opus.md:264–270` | The specified gauge-fixed vertex-block walk majorant has spectral radius at least `(2+sqrt(10))beta/4`; its certificate fails at `beta>=(2/3)(sqrt(10)-2)`, approximately 0.775. It does not exclude all block methods. |
| `gap-arealaw2-check-astra.md:343–375`; `gap-compress-check-astra.md:69–100,117–147` | Given the named FSS infrared bound, the flat one-layer O(4) law excludes background-uniform exponential two-point decay for beta>4G_3. The decimal 1.0109 is approximate; the existing written bound G_3<1/3 already covers beta>4/3. |

R1–R4, CUT and RARE do not claim any of those certificates. Their
averaged inputs are not ruled out by those results. Conversely, being a
supremum does not by itself identify FORCE-COV with the particular
one-layer two-point observable of the FSS obstruction. SU(2) failure of
the new supremum remains ARGUED in the source. No new result about any
unavailable Balaban paper or the full Villain model is being imported.

**G-num (lines 235–253) and the toron-chain run (426–430): HOLDS as
GUIDE model arithmetic.** The original scripts named under the author's
`/tmp/oddgap-fable-scratch/` are not in the checkout and were not accessed.
A fresh scalar check is at
`/tmp/ym4d-oddgap-check-astra-20261114/guide.py`; its complete output is
`guide.log` in that directory. It uses periodized Gaussian image sums,
one-dimensional Sturm–Liouville shooting for mu_0, and direct periodic
convolution for the conditional moments. This is a different numerical
path from accepting the author's values, but still supplies no proof.
The exact mathematics above does not depend on this run.

| Quantity | Fresh GUIDE value | Source comparison |
|---|---:|---|
| seed 1/2-p | 1.3850840e-10 | matches 1.385e-10 |
| seed FR_u; J | 36.866109; 737.32218 | matches 36.87; 737.3 |
| seed lambda_odd; mu_0 | 2.6364761e-9; 5.2729521e-8 | matches 2.636e-9; 5.273e-8 |
| seed 2D/V | 5.2955662e-8 | matches 5.296e-8; excess over mu_0 about 0.43 percent |
| seed FR_u/(2 lambda_odd) | 6.9915501e9 | matches 7.0e9 |
| seed weight-step loss | 1.3923387e10 | matches 1.4e10 |
| cube beta=2.3: 1/2-p; L FR_u; L lambda_odd | 1.1768959e-5; 174.47788; 0.0015143476 | matches all three entries |
| cube beta=2.6: 1/2-p; L FR_u; L lambda_odd | 2.6778784e-6; 225.49125; 0.00041875435 | matches all three entries |
| toron chain, s=2,3,4,5: E Var(M_1) | 0.3899007294, 0.1663980533, 0.0622838983, 0.0219903225 | matches all four entries and independently integrated differences |
| toron chain, V_s/V_(s-1) | 0.40552286, 0.37437512, 0.37448954, 0.41027344 | matches 0.41,0.37,0.37,0.41 |

The direct conditional mean and analytic score checks differ from R_s and
R_s' by less than 1.1e-15 on this grid; no sampled Cauchy–Schwarz violation
was found. This verifies the reported model arithmetic, not the original
1500-point code, its finite-difference error estimate or its resource log.
The large-tau scalar comparison `exp(-x)<=1/(1+x)` in lines 442–445 is
correct; its claimed force variance remains dependent on the choice of
latent Gaussian score versus the score after winding integration.

Execution limits: one job under a successfully acquired and released
`lab_ops.py numeric-lock`, all four thread variables set to 1, a 100-second
alarm, and an RSS self-stop at 2 GB. Observed maximum RSS was 16,482,304
bytes. The first attempt did not compute results: the sandbox rejected
`nice`, and setting RLIMIT_AS raised `ValueError`. That log is preserved as
`guide-first-attempt.log`. The completed small job used the RSS self-stop;
priority lowering was unavailable. No interval arithmetic, machine
enumeration, quadrature or eigenvalue computation is treated as discharge.

## 6. Verdict map and disposition

Line numbers refer to the pinned 620-line `gap-oddgap-max.md`, not to this
report. This map includes the inline PROVED claims as well as the result
table. A corrected implication still grants no status to its open inputs.

| Statement / source lines | Verdict | What survives or changes |
|---|---|---|
| I1–I3, 71–82 | HOLDS | Exact even variance, weighted energy and `p<=FR_u/(2lambda_odd)` in the stated conventions; reuse row 927. |
| I4, 83–84; ceiling discussion, 96–98 | HOLDS AFTER CORRECTION | ODD-0 and the single-line quotient hold. A positive-beta ceiling 3L_1 needs q>=1/4. |
| I5, 85–87 | HOLDS | First-layer score covariance and martingale; define terminal M_t directly. |
| G1, 104–151 | HOLDS AFTER CORRECTION | Fix gauge/kernel normalization and retain the Markov-score assumption for I5; same exact compact-toron model. |
| G2, 153–168 | HOLDS | Exact trace and theta-series bounds, seed and cube hand bounds. |
| G3, 170–198 | HOLDS | Exact response formula, all-tau upper bound and small-tau lower bound. |
| G4, 200–226 | HOLDS | Exact variational reduction, all-tau soft-coordinate bound and small-tau hand bounds. |
| G4 sector structure, 228–233 | HOLDS | Nonzero-M lower bound, small-tau identification of mu_odd with mu_0, and large-tau limit; asymptotic remainder stays ARGUED. |
| Hand-bound and GUIDE table, 235–253 | HOLDS | All stated hand intervals and rounded GUIDE values; original run metadata unverified. |
| F1 and finite counts, 259–294 | HOLDS | Complete the displayed tree/holonomy bijection as in section 2; both exact p values survive. |
| F2, 302–322 | HOLDS | Zero single-link heat-bath energy and odd gap at beta=infinity. |
| Finite-beta tests, 296–300,324–329 | HOLDS AFTER CORRECTION | Isolated-link costs only; no proved finite-beta phase or tunnelling estimate. |
| Step-A verdict A, 336–374 | HOLDS AFTER CORRECTION | Seed rivals reject the criterion's proposed input pair. Restrict gap comparison to its stated lower target; replace the purported size threshold by sufficient sizes. |
| R1–R3, 388–412 | HOLDS | Exact martingale variance decrement and conditional product contraction. |
| R4, 396–398,413–419 | HOLDS | Mixture covariance splitting and within-sector bound, with positive denominators. |
| Ising kill test, 421–425 | HOLDS | Exact R1 test only. |
| Toron GUIDE test, 426–430 | HOLDS | Stated scalar model and arithmetic; not a proof of R. |
| R5, 433–439 | HOLDS AFTER CORRECTION | Final sufficient ratios 95.3 and 78.4 survive; the intermediate 0.135 rounding does not. |
| R-sup, 448–455 | HOLDS AFTER CORRECTION | Small-tau range and thin-slab large-N limit; half-torus numeric gap cannot simply be cited at every s. |
| Averaged R2/R3, 460–465 | HOLDS | Treat a zero denominator separately. |
| Ceiling comparison, 467–469,565–568 | HOLDS AFTER CORRECTION | Only the named methods/observables are excluded; no universal cut-gap ceiling is supplied. |
| SU(2) susceptibility implication, 475–485 | HOLDS | Necessary covariance and susceptibility upper bounds. |
| U(1) susceptibility identity/bound, 487–489 | HOLDS | Finite-box Gaussian formula and lower bound. |
| U(1) unbounded-susceptibility conclusion, 489–493 | FAILS | Missing uniformity; explicit rectangular-strip counterexample in section 4. G4's toron obstruction remains valid. |
| CUT, 499–511; Haar test, 514 | HOLDS | Conditional odd inequalities sum without independence. |
| CUT Model G test, 515–520 | HOLDS AFTER CORRECTION | Conditional mean factorization holds; the factor-two comparison uses mu_odd=mu_0, including the seed. |
| Spatial uniform-rotation distinction, 521–531 | HOLDS | Algebraic stabilizer distinction only; not invariance of the full U(1) conditional kernel or a quantitative SU(2) gap. |
| RARE, 538–557 | HOLDS | Exact stated implication from positive g_0, alpha and the bad-set bound. |
| Final synthesis, 584–620 | HOLDS AFTER CORRECTION | Keep the corrected Step-A test and conditional reductions; remove the false unbounded-susceptibility conclusion and the unrestricted threshold readings. |

The failures do not invalidate R, CUT or RARE. They invalidate the
susceptibility-based identification of the U(1) mechanism without a
specified thermodynamic limit, and several broader readings of sufficient
bounds. G4 itself supplies the appropriate soft-toron witness. No proof
of an order-one SU(2) odd gap, flux half or mass gap has been supplied.

Only this report was added to the checkout. No source, registry, FINISH row,
ledger or audit record was changed; no post, commit or push was made.
The report remains uncommitted at the requested lane path. The source copy
in `/Users/jonreilly/ym4d-lead/sa` has no Git metadata, so its revision is
the user's supplied `31a47c543775`, not a locally verified HEAD. A lazy
fetch for the absent pinned lab_ops blob failed because network resolution
was unavailable; the existing origin/main tooling was copied to scratch
for the GUIDE lock. No scientific source required a network fetch.

RESULT: HOLDS AFTER CORRECTION overall. G1–G4's Gaussian identities and hand bounds, the frozen Q_8/2T counts and zero heat-bath gap, Theorem R, CUT and RARE survive at the scopes stated here; the GUIDE numbers reproduce. FAILS: the unqualified claim that Model G's winding-line susceptibility must be unbounded as N grows. Correct the box-size, all-coupling, small-tau, unequal-slice and rounded-threshold readings. The Coulomb-window fact test survives through the soft toron gap; order-one SU(2) inputs and cutoff uniformity remain open. Research check only; no status granted.


## Recovery note

Final RESULT line as Codex printed it after its last edit:

RESULT: HOLDS AFTER CORRECTION overall. G1–G4's Gaussian identities and hand bounds, the frozen Q_8/2T counts and zero heat-bath gap, Theorem R, CUT and RARE survive at the scopes stated here; the GUIDE numbers reproduce. FAILS: the unqualified claim that Model G's winding-line susceptibility must be unbounded as N grows. Correct the box-size, all-coupling, small-tau, unequal-slice and rounded-threshold readings. The Coulomb-window fact test survives through the soft toron gap; order-one SU(2) inputs and cutoff uniformity remain open. Research check only; no status granted.

Codex's closing message:

Repo search: searched the five requested refs and credited related prior work; no duplicate odd-gap result found.

Wrote [gap-oddgap-check-astra.md](/Users/jonreilly/ym4d-lead/lane/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-oddgap-check-astra.md).

**HOLDS AFTER CORRECTION overall.** Gaussian and frozen-group calculations, R, CUT and RARE survive; GUIDE numbers reproduce. The unrestricted susceptibility-growth claim **FAILS**, with an explicit counterexample.

The report remains uncommitted. No scientific status granted.
