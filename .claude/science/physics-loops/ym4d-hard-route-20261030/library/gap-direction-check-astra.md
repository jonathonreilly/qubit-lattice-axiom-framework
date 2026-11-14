# Repo search

Codex check, 2026-11-14, row 938; source checkout
`eb2f10536f3aa261acd61cd90cec3dc47b752988`. Research text, not an audit;
this file grants no status. The dispatch specifies gpt-6-astra/xhigh.
The target is `library/gap-direction-max.md`, all 458 lines.
Source SHA-256: `dbf8d872f64475d3b3e81123a69465cde774f4d9b6c1e98d86f90f5473a9637e`.
`library/prior/gap-direction-check-astra.md` is absent.

Searches ran on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`,
`pr/10141` in `/Users/jonreilly/Projects/Physics`, over `*.md`, `*.tex`.
Initial `ANOM` and `SMALL-BOX` searches hit their caps with unrelated work;
they support no absence claim. The completed narrower search used
`HC-vac|LSI-vac|gap-direction|\(ANOM\)|hypercontract|vacuum.slice.chain|interaction measure|SPLIT.*S_ev`.
It found the following relevant prior work on `origin/main`:

| File and lines | Exact content and proximity |
|---|---|
| `research/mass-gap/library/gap-phys-seed.md:195,224` | Q4 proposes contraction of dimensionless thermal pressure; its non-strict version is positivity of the interaction measure. U(1) passes that non-strict version. This is the prior pressure interpretation, not the finite-box ANOM identity or its seed estimate. |
| `research/mass-gap/library/gap-skeleton-max.md:190–192` | B11 proposes hypercontractivity of the ground-state transfer semigroup as a route to an isolated simple vacuum; its literature input is recalled. This is prior method credit, not a quantitative HC-vac proof. |
| `research/mass-gap/library/prior/gap-crux-lit-2.md:42,126,183` | Martinelli–Olivieri concerns finite-volume mixing-to-hypercontractivity; Rothaus concerns compact-manifold Laplacians. The digest explicitly supplies neither a Wilson vacuum-law bound nor its constants. |
| `research/mass-gap/library/gap-mid-max.md:27` | Coupling-transport and trace-anomaly search record; the time-rate argument must retain its distinct fixed-coupling scope. |

The refs resolved respectively to `4d88da5504d356762deb6b1a1c2695336af9fb81`,
`f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`89faef229ff6e6bde42baad15ed8270c2f4087d8`,
`1e70c7211a2cdbc39001e619f1dd89db45e25851`, and
`c73ad7b177d94f89ff37b77386936e3d52b48b05`.
No target-name match or duplicate of this check appeared in that completed
search. The old `repo-search-2026-11-08.md` concerns RG obligations and
snapshot lineage, not this vacuum-chain comparison. The registry search
for the target, HC-vac, LSI-vac, E-to-HC, SMALL-BOX, split seed and ANOM
found no matching owner. This check does not attack any later proof row.

## Completed checkpoint

The complete target has been read and checked. Sections 1–5 record the
priority proofs, all nineteen rows, remaining interpretations and every
reported fact-test computation. Missing GUIDE artifacts remain unverified.
The next decision is whether the owner of row 931 adopts the SH-only
conclusion or tightens HC's threshold to recover W. The separate proof
tasks keep their existing owners. Only this output file is changed;
the original note, FINISH, registry and scientific status are untouched.
No numerical run is proof evidence.

## 1. Vacuum-chain statements, checked first

Line numbers below refer to the 458-line source at the pinned commit.
The Sussman–Alpoge index was searched before its source: chunk 02,
rows 2315–2335 and their neighbours identify GL8 as a proved transfer-trace
identity. The source at outline 2290–2340 defines
`L=P C^(1/2) exp(-V) C^(1/2) P` and `Z_s=Tr L^s`.
This is prior work, credited to Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text. It supplies the transfer frame,
not HC-vac or an order-one seed. For the positive Wilson kernel used in
this note take instead `T=exp(-V/2) C P exp(-V/2)`; the nonzero spectra
agree by the `AA*`, `A*A` construction. Work on gauge-invariant functions.
An overall positive scalar in T is immaterial. For HOT use the source's
`exp(beta x_p)` convention, absorbing the constant in `1-x_p` into that scalar.

**(5.1), (5.2), (5.3): HOLDS.** Differentiating `T Omega=lambda_0 Omega`
gives `grad log Omega=E_pi G`. Thus the score of pi is centred G,
which proves (5.1). Conditional expectation is an orthogonal projection
in the stationary joint law, giving (5.2). Finally
`integral p_s(u,v)^2 dnu(u)dnu(v)=Tr P^(2s)=1+S(2s)`.
Subtracting one is exactly the joint chi-square divergence. All these
identities include every centre sector, not just the even sector.
Chain lags here and in E1 are positive integers. The Hilbert–Schmidt
spectral identity also holds at real s in its trace domain, but calling
it a probability divergence at fractional s needs positivity preservation
of P^s, which is not assumed. ANOM's real spectral time needs no such input.

**Theorem V: HOLDS.** Assume gamma>0 and finite Gamma-star when dividing.
For each unit tangent z the squared covariance is bounded by
`Var_pi(z.G) Var_pi(f)`. Taking the supremum in z gives
`|grad Pf|^2<=Gamma(u) Var_pi(f)`. Applying the stated Poincare inequality
to the centred Pf yields
`gamma ||Pf||_2^2<=E[Gamma(u) Var_pi(f)]`.
Stationarity then yields `(gamma+Gamma-star)||Pf||_2^2<=Gamma-star||f||_2^2`.
The spectral and energy conclusions follow. If Gamma-star=0, Pf is
constant; interpret the energy conclusion by a limit rather than divide
by zero. Density and smoothing extend the argument from bounded f to L2.
The averaged version in Step 7 is the same nondivided inequality and HOLDS.

**Gaussian equality test for V: HOLDS for one oscillator.** Write
`c=cosh omega`, `sigma_0=sinh omega` (to distinguish it from SG-step's
proxy). Completing the conditional Gaussian square gives mean
`exp(-omega)q`, variance `1/(beta exp omega)`. The score is beta q'
plus a deterministic term, so Gamma=beta exp(-omega). The vacuum law
has precision `2 beta sigma_0`. Hence
`Gamma/(gamma+Gamma)=exp(-omega)/(2 sinh omega+exp(-omega))=exp(-2 omega)`.
The first Hermite mode attains equality. Higher Hermite modes need not.

**Lemma HOT: HOLDS.** With M=beta|B| the positive kernel is between
exp(-6M) and exp(6M), including gauge averaging. Its diagonal integral
is at most exp(6M), while its Rayleigh quotient on 1 is at least exp(-6M).
Thus X(1)<=12M. The eigenfunction equation bounds its oscillation by
exp(12M); normalization gives exp(-12M)<=Omega<=exp(12M).
Since `p_1=T/(lambda_0 Omega(u)Omega(v))`, its supremum is at most
exp(36M). These deliberately crude constants hold for the stated kernel.

**Proposition HC's trace and gap bounds: HOLDS.** For q'=1+delta,
`||g||_(1+delta)<=||g||_infinity^(delta/(1+delta))<=||g||_infinity^delta`
for a probability density. Apply HC to p_1(u,.) with
delta=exp(-2 alpha m), square, and integrate in u. This gives the printed
`X(2m+2)<=72 beta |B| exp(-2 alpha m)`.
For large m, `r_i^(2m+2)<=exp(X)-1<=2X`; taking roots gives E_i>=alpha.
Self-adjoint duality gives exactly q=1+exp(2 alpha m).

**HC's seed consequence: HOLDS AFTER CORRECTION for the SH seed;
FAILS for the stated Form W at those constants.** The hypothesis covers
integer m, hence first take an even a>=2. The exact sufficient condition is
`alpha(a-2)>=log(72 beta 24^3/x_*)+3 log a`.
For odd a use a-3 in place of a-2, or supply fractional-time HC separately.
The conclusion is X(a)<=x_*, hence S(a)<=5/17<3/10: an SH seed.
It does not give `S_ev<=1/10, Q_0<=1/20` on that same box.

Here is the missing distinction, already explicit in Lemma SPLIT
(`gap-crux-core-max.md:265–272`):
`S_ev<=S`, `Q_0<=S/(1+S)`, and
`1+S<=(1+S_ev)/(1-3Q_0)`.
Form W therefore implies X<=log(22/17), but the converse is false.
A spectrum with vacuum 1 and one even excitation of weight 1/5 at time a
has X=log(6/5)<log(22/17), yet S_ev=1/5>1/10.
This is realized by a strictly positive two-state kernel with eigenvalues
1 and `(1/5)^(1/a)` and trivial centre action. If all eight sectors are
required, tensor with an arbitrarily rapidly mixing centre chain; the
strict inequalities persist. This refutes the claimed spectral implication,
not a claim that a particular Wilson box realizes those eigenvalues.
A sufficient same-box repair is X<=log(20/19). Then S<=1/19<1/10 and
Q_0<=1/20. Replace x_* by log(20/19) in HC's size condition. Alternatively
retain x_* and say only that the SH consumer is supplied.

**Theorem E: HOLDS under its named inputs.** Use entropy for unnormalized
h as `Ent_pi(h)=E h log(h/E h)`. For every real lambda, the variational
inequality for the tilted probability h pi/m gives
`lambda E_(h pi/m)(phi-E_pi phi)<=Ent_pi(h)/m+lambda^2 sigma^2/2`.
Optimizing both signs proves
`Cov_pi(phi,h)^2<=2 sigma^2 m Ent_pi(h)`.
Taking the supremum over unit tangents, integrating, and using the exact
entropy chain rule gives
`I_F(Pg)<=2 sigma^2[Ent_nu(g)-Ent_nu(Pg)]`.
LSI gives `alpha Ent(Pg)<=sigma^2[Ent(g)-Ent(Pg)]`, the stated contraction.
For zero densities use positive regularization and truncation; the bounded
smooth positive Wilson kernel allows passage to the limit. This supplies
the stated all-density scope. The pointwise-proxy averaged version HOLDS.

**Corollary E1: HOLDS.** Apply E successively to p_1(u,.), whose entropy
is at most log sup p_1<=36 beta|B|, and integrate in u. This proves
`I(U_0;U_s)<=rho^(s-1)36 beta|B|` for integer s>=1.
In one Gaussian mode alpha=2 beta sinh omega and sigma^2=beta exp(-omega),
so rho=exp(-2 omega). This is the sharp entropy contraction coefficient:
exponential tilts attain it. It is not an equality for every density or
for the mutual information at every lag. Indeed Gaussian mutual information
is `-log(1-exp(-2s omega))/2` per real mode.

**I(U_0;U_s)<=X(2s): HOLDS.** Jensen under density p gives
`integral p log p<=log integral p^2`; Jensen over u and (5.3) complete it.
A small entropy does not control L2: on an interval put a spike of mass
epsilon on a set of length epsilon^3, and keep the remaining mass nearly
uniform. Entropy tends to zero like `2 epsilon log(1/epsilon)`, whereas
the squared L2 norm diverges like 1/epsilon. Thus E1 alone does not close HC.
E-to-HC remains an OPEN implication in the source; this check does not
take over row 940's proof task or treat the recalled Gross theorem as a
discrete-time proof.

## 2. ANOM, elementary lemmas and spectral fact tests

**ANOM: HOLDS as an identity and as an equivalence to X(t_1)<=x_*.**
The spatial box B must stay fixed during differentiation and integration.
For t>1, `E exp(-tE)<=exp(-E)/(e(t-1))` justifies differentiating the
trace; on compact t-intervals higher derivatives follow by the same bound
with higher powers of E. Thus `d log(t^3 X)/d log t=3-tU/X`.
Integration gives ANOM. At B=(24t_1)^3 its right threshold is exactly
`log pi_B(t_0)+log(24^3/x_*)`. Letting t_0 decrease to 1 is valid by
trace-class monotone convergence. A trivial rank-one transfer has X=0;
its seed is automatic and kappa is undefined, so exclude that case from
the identity. The finite positive-beta Wilson transfer is not rank one.

The phrase **“the same form” as Form W FAILS**: section 1 gives the
counterexample to equivalence. ANOM with this threshold is sufficient
for SH, but is neither equivalent to nor stronger than W at the printed
constants. The finite-volume name “pressure” also needs care: X/|B|
is the negative vacuum-subtracted free-energy density divided by temperature.
It need not equal mechanical pressure at finite volume. The usual
thermodynamic interaction-measure dictionary needs its thermodynamic limit.

**Lemma TENS: HOLDS.** The normalized partition functions multiply,
so their logarithms and negative time derivatives add. A common positive
RATE constant passes to products. An arbitrarily large multiplicity at a
fixed excitation energy proves that a gap alone does not bound X.

**Lemma GAPRATE: HOLDS.** The mean excitation energy is at least
`E_1 S/(1+S)=E_1(1-exp(-X))`. Divide by X and use
`exp(-X)<=1-X+X^2/2`. The following prose requires qualification:
the exact lower rate is positive for every finite X, not only X<=1;
what deteriorates at large X is a constant comparable to E_1.
No converse identifies the seed with a positive RATE bound on a whole
hot-to-cold window. Such a bound is a sufficient route, not a necessary
condition supplied by the seed at one time.

**FP lower bound and ANOM deficit: HOLDS for the defined FP model.**
Use row 929's A2, checked in `gap-seam-check-astra.md:48–71`:
26 distinct nonzero integer momenta, two polarizations, and
`a omega<=pi sqrt(3)/12<1/2` give
`X_ev>52 exp(-1/2)>31`. Since X>=X_ev, ANOM misses its exact threshold
by `log(X(t_1)/x_*)>log(31/x_*)>log 120>4.78`.
This holds without computing a black-body integral. It is a test of FP,
not an identification with compact Wilson U(1) across a transition.

**Per-mode X, U and tU<=(1+t omega)X: HOLDS.** Put x=t omega, y=exp(-x).
Use `-log(1-y)>=y` and `x/(1-exp(-x))<=1+x`, the latter following from
`exp(x)>=1+x`. This checks the printed inequality directly.

**“kappa=3 for the photon gas and the toron tower”: FAILS at the stated
finite box, and FAILS for the toron tower even in its continuum model.**
The infinite-spatial-volume continuum photon expression
`X=(pi^2/45)|B|/t^3` has kappa=3. At fixed aspect ratio the continuum
photon expression is instead the discrete sum
`-2 sum_(n!=0) log(1-exp(-2pi t |n|/b))`.
This distinction was already established by
`gap-seam-check-astra.md:137–192`; no new attack is needed.
Even a function of t/b need not be proportional to (t/b)^(-3).
Scale invariance under simultaneous rescaling of t and b is not the
fixed-B derivative in ANOM.

For the full toron factor put `s=t/(2 beta b)`,
`theta(s)=sum_e exp(-s e^2)`. Exactly,
`X_tor=3 log theta(s)` and
`kappa_tor=-s theta'(s)/(theta(s) log theta(s))`.
Poisson summation gives `theta(s)=sqrt(pi/s)[1+2 sum_(n>=1) exp(-pi^2 n^2/s)]`.
As s tends to zero, kappa_tor is asymptotic to `1/log(pi/s)`, hence tends
to zero, not three. At b=24t, beta=2.3, its value is near 0.171, while
X_tor is near 8.77. The identity and the >31 refutation survive; the
“opposite ends kappa=3 versus kappa=0” explanation must be replaced.

**Frozen trace and ANOM failure: HOLDS at each fixed box for sufficiently
large beta.** Reuse the two inequivalent even flat vectors and the norm
bound in `gap-glue-check-astra.md:405–421`, credited there to
`gap-crux-exercise2-check-astra.md:227–266`.
They give S_ev>=1/2, hence X>=log(3/2)>x_*.
The finite-dimensional normalized operator tends to its flat projector;
the flat eigenvalues tend to 1 and the others to 0. Therefore U tends to
zero at fixed t>0 and X tends to log of the flat dimension: kappa tends
to zero. This is not a uniform assertion over all boxes at one finite beta.

**HC's rival tests: HOLDS AFTER CORRECTION of quantifiers.** For photons
the lowest nonzero oscillator frequency tends to zero with b; full FP
also has a toron level 1/(2 beta b). Thus E_1>=alpha rules out a positive
box-uniform alpha for FP. At one seed box it already rules out the
printed size condition: alpha(a-2) is at most (a-2)/(48 beta a) from
the toron, much smaller than 16+3 log a. The frozen finite groups rule
out a beta-uniform positive alpha on a fixed box as beta grows.
They do not, by this fixed-box limit alone, rule out a small positive
alpha at every finite beta, nor prove a volume-uniform frozen phase.

**SG-step and LSI photon tests: HOLDS on the oscillator factors.**
The Gaussian score has proxy beta exp(-omega)<=beta. LSI linearized at
h=1 gives a Poincare inequality, so alpha<=gamma. The Gaussian vacuum
has gamma=2 beta sinh omega. These facts explain the soft photon test.
They say nothing computed here about the toron's score proxy.
Frozen groups have no Lie-algebra gradient; their beta=infinity
single-link heat-bath analogue has gap zero. Do not identify that update
with a simultaneous whole-cut or whole-slice update.

## 3. All nineteen Step-3 rows

Here a “passing form” means a sufficient hypothesis with its quantitative
threshold, not an identity valid in the rival too. The two model columns
must distinguish Gaussian FP/G, beta=infinity, and finite-beta statements.
The current checks of rows 929–930 are available at this pin; their
corrections below supersede the author's unchecked imports.
In particular, `for every fixed box, for sufficiently large beta` does
not imply `for one finite beta, for every box`. The former frozen bound
alone does not refute W's existential choice of a at a fixed finite beta.

| Row | Verdict | Exact surviving statement or correction |
|---|---|---|
| 1, GLUE-FP | HOLDS | FP has X_ev>31. Frozen Q8/2T have S_ev>=1/2 at each fixed box for sufficiently large beta. The target itself is tautologically the weakest condition implying that exact target. |
| 2, CORE | HOLDS AFTER CORRECTION | Model G in the stated Coulomb window and geometry has p near 1/2; frozen values are 10/23 and 30/61. State the window: at fixed geometry G has p tending to zero as beta tends to zero. The frozen conclusion is at infinity, with finite-box continuity, not a proved uniform phase. |
| 3, signed seam average | HOLDS | INS gives exactly `X_ev=3 beta b^3 integral Delta`. Its threshold is equivalent to GLUE-FP, provided the same seam/model is used. |
| 4, SEAM-L1 and SEAM | HOLDS AFTER CORRECTION | Absolute integral and supremum imply the signed bound. The photon path G has positive integrand and fails. Its sup/average grows with a. Retain the fixed-aspect-ratio sums, not row 929's black-body constants, and do not identify the photon path with the uncomputed compact-rotor seam. |
| 5, endpoint alone | HOLDS AFTER CORRECTION | An endpoint value gives no integral upper bound. Row 932 already corrects the 4.8e4 crossover: it is an infinite-space approximation, not a proved crossing size for full FP or compact Wilson U(1). The eventual photon-model failure of endpoint selectivity remains. |
| 6, Z0+COUNT | HOLDS AFTER CORRECTION | The pair is sufficient by G5, with the gap in the complete even sector. A local contractible-observable gap cannot replace it: Q8/2T have additional even flat states (row 896 D3,D6). COUNT alone is not selective. FP's scale-free hot-box count is bounded by its convergent mode sum; its even gap times a stays small. |
| 7, Q's product hypothesis | HOLDS | In the beta window psi_*<1, `y<=psi_*/9` gives `8y/(1-y)<=psi_*`. Take the supremum over the required theta, with n=a-1-2k>=1. This is sufficient, not an equivalence; row 932's k/time qualifications remain. |
| 8, local-sup I1–I3 | FAILS as a blanket ceiling deduction | The cited 2/3 and 0.775 bounds concern specified single-link and vertex-block majorants, not all ways to establish I1–I3. Q avoids those inputs, but does not refute them. Restore each input's actual law (I3 is a seam marginal) and distinguish a capped proof method from a false target. |
| 9, FR alone | HOLDS AFTER CORRECTION | It is nonselective: frozen single-link response is zero, and sufficiently large G cubes meet the proposed absolute response target. The size 420 is only a sufficient size at beta=2.3 and p_*=2e-4; it is not a sharp threshold or a whole-window bound. |
| 10, `p<=FR/(2 lambda_odd)` | FAILS as a passing crux form | This is a valid comparison inequality in the rival too; a large right side does not make the inequality false. The sufficient hypothesis must be `lambda_odd>0` and `FR/(2 lambda_odd)<=1/20` (or the actual consumer threshold). No quotient 0/0 is permitted in the frozen model. |
| 11, R with supremum force bound | FAILS as a CEIL exclusion | A supremum that grows in Model G does not refute its proposed bound for SU(2). That is the desired U1 discrimination, not a SU2 ceiling. The specific bridge-supremum obstruction has small-tau and geometric hypotheses; it differs from V's one-ended conditional law. No cited ceiling excludes all SU2 suppliers of this form. |
| 12, R with averaged covariance | HOLDS AFTER CORRECTION | R is a conditional sufficient implication once its product of contractions meets the required flux threshold. Averaging alone supplies no quantitative bound. If the variance denominator is zero use R's nondivided version. |
| 13, CUT-TYP+LSI-weak | HOLDS AFTER CORRECTION | CUT and RARE supply an odd-gap lower bound. They do not by themselves supply FORCE-COV, so are not stronger than the full row-12 pair without that extra premise. The Gaussian conditional-cut test fails the order-L_1 good-gap target; frozen single-link dynamics has zero gap. |
| 14, KURT or WALL with GLUE | HOLDS AFTER CORRECTION | The stated 2D real-ground-function values are 3/2 for U1 and 4 for Q8; they do not decide the 4D SH-box kurtosis. Circle symmetry guarantees a choice of a real odd eigenvector with kurtosis at least 3/2, not every superposition. With the strong GLUE premise, the checked 1.66 floor is sufficient; GLUE rejects frozen Q8/2T. This does not prove that their 4D kurtosis passes or fails. |
| 15, E17, HA, C2, EXC, DRESS, S1 | FAILS as one common sufficient row | These have different quantifiers and auxiliary premises. In particular `gap-crux-core-max.md:255–259` explicitly says S1 or S2 singly does not reach a consumer. Keep the actual quantitative E17/C2/EXC and DRESS chains and the background qualification for HA; do not promote S1 alone. A statement at all sizes must also attain the target at the seed box. |
| 16, VIR-log/VAC-SUB | FAILS the stated Gaussian U1 column | A coupling-transport inequality is not required to fail in a family with no strong-coupling seed. Gaussian nonzero-mode energies are independent of beta: field dilation unitarily conjugates its transfer operators, so their response excesses are zero. This is already Proposition G of `gap-vacsub-max.md:137–158`. Compact U1 across a transition is a different family and needs the strong-coupling starting seed, transport budget and gapless input. VIR-log and VAC-SUB are not equivalent. |
| 17, free-wall JOIN-TH engine | FAILS as a both-halves periodic-seed form | Row 910 uses H-SEED on free boxes and concludes a gap on free cubes. Its Step 7 explicitly allows the seed and engine in frozen finite groups. A simply connected frozen free box has one flat gauge class; a periodic box has nontrivial flat holonomies. Its seed is not forms 1–2, and its conclusion is not the periodic full seed. The assertion that JOIN-TH alone is nonselective is consistent, but its finite-beta leading-order estimate remains ARGUED. |
| 18, SEED-Delta, SEED-L, CAS | HOLDS AFTER CORRECTION as sufficient routes; FAILS as the printed same-box equivalence | SEED-Delta and SEED-L use other shapes, scales and, in first-passage form, limsup margins. Their checked enlarging/composition results give a seed at a possibly larger size. CAS implies eventual threshold crossing when 0<theta<1, but a seed at a later size does not by itself prove strict decrease at every earlier above-threshold doubling. `gap-mid-max.md:64–67,209–215` supplies no such converse. Keep sufficiency and the actual quantifiers. |
| 19, ANOM | HOLDS as equivalent to its SH full-trace threshold; FAILS as equivalent to W | Section 2 checks the identity and section 1 gives the counterexample to the stronger equivalence. It does pass the FP and fixed-box frozen trace tests. |

**F1: HOLDS AFTER CORRECTION as a description of the inspected sufficient
mechanisms; FAILS as a necessity statement.** Every surviving spectral
criterion has the indicated count or gap input. A list of sufficient
conditions does not prove that every possible passing form must contain
one explicitly. Rows 10, 13, 15 and 17 also lacked the claimed common
consumer before correction. For the kurtosis factor, the 2D counterexample
and unknown 4D value must remain distinct.

**F2 and Form W's “weakest” designation: FAILS at the stated fixed box
and constants.** W implies X<=log(22/17), whereas the converse fails.
The latter is row 19, passes the same trace tests and already suffices for
SH; hence the table itself contains a strictly weaker sufficient spectral
condition. Even SH's S<3/10 permits more than W. If the target is defined
to be W itself, “W is weakest among hypotheses implying W” is a tautology;
then row 19 and HC at the printed constants cease to be sufficient rows.
At an existential larger-size level the established SH propagation may
connect these conditions, but that is a different quantified assertion.
The table proves no global minimality or “no easier handle” theorem.

**F3: HOLDS for its narrow conclusion.** Some forms, including the full
seed itself, pass the stated countermodel tests. It does not follow that
every passing formulation offers no useful method of proof.

**F4: HOLDS for the two exhibited mechanisms, AFTER CORRECTION of its
necessity wording.** R contracts the variance of one bounded odd function,
with `p/(1-p)=Var(R_t)<=1`. V and (5.3) contract a trace only by a factor
per time step; their crude initial estimate has log S(2)=O(|B|).
That estimate would cost time of order |B| at fixed gap. HC avoids this
cost. No theorem here says entropy contraction is necessary for every
proof of the trace bound, or that S(2) actually has the worst allowed size.

## 4. SMALL-BOX, group distinction and ceilings

**SMALL-BOX: FAILS as a proved standing exclusion; HOLDS AFTER CORRECTION
as a proposed conditional test.** The needed premise is, for the actual
fixed-lattice Wilson transfer operator,
`E_1(B,beta)->0` as beta tends to infinity, with B fixed.
If supplied, E_1>=alpha forbids a beta-independent positive HC rate, and
forbids the seed-sufficient rate at fixed a. It does not say that HC with
a beta-dependent rate is false at every large finite beta.

The cited `gap-phys-seed.md:98–113,194` explicitly calls its small-physical-
volume statements RECALLED/GUIDE. Its continuum small-volume expansion
does not establish the fixed-lattice premise above. That source also
retains a factor omitted here:
`exp[-S/g + epsilon_1 T/g^(2/3)]`, with positive epsilon_1 T.
Dropping the second term preserves the leading logarithmic scale -S/g,
but not an “of order” estimate up to constants. No primary small-volume
paper or rigorous lattice remainder is supplied by this check.

The wording “any proof of a slice-law inequality ... that does not tie
the lattice size a to beta ... is wrong” is false. For example Lemma HOT
already bounds the density of nu relative to product Haar between
exp(-24M) and exp(24M). Product S3 Haar has Poincare constant 3
(degree-l harmonics have Laplacian eigenvalues l(l+2), so every nonconstant
product harmonic has eigenvalue at least 3). Therefore, by minimizing
over constants and comparing the two measures,

`Var_nu f <= exp(24M) Var_Haar f`
`<= exp(24M)/3 integral |grad f|^2 dHaar`
`<= exp(48M)/3 integral |grad f|^2 dnu`.

This valid fixed-box inequality needs no size/coupling relation. It is
far too weak to supply the seed. SMALL-BOX must test the **quantitative
rate needed by the seed**, not the existence of a functional inequality.
Nor does a collapsing transfer gap force LSI-vac's gradient constant to
vanish: V/E compare different forms and their force constant may grow
with beta. In the source E-to-HC is still open. The separate claim
“LSI-vac: SMALL-BOX must fail” is therefore not established.

**Group mechanism: HOLDS AFTER CORRECTION at the algebraic level;
FAILS for every-conditional-law and gradient-order wording.** For SU2,
the common centralizer of two noncommuting elements is its centre.
For U1 a common cut rotation preserves the spatial plaquette action.
These are precisely the checked statements of row 933, section 4.
They do not make a one-ended or two-ended conditional temporal law
invariant under rotation of the free endpoint alone. Its rotor kernel
depends on their angular difference. Simultaneous endpoint rotation
is the symmetry. A continuous symmetry on a compact space also need
not force a zero Poincare constant at fixed size: the uniform circle
has constant 1. The soft toron estimate uses its size-dependent metric.

The photon vacuum's gradient Poincare constant behaves as
`2 beta sinh omega ~ 2 beta |k|`, as the source's own Gaussian check
shows. The spatial-action Hessian behaves as |k|^2. They cannot be
identified. Connectedness and finite centre distinguish the named groups;
they are not a proof of an order-one lower bound, nor an exhaustive
necessary condition for all routes or models. The assertion that “only
the box size lifts” the SU2 toron is a physical interpretation, not a
derived estimate here.

**Ceiling imports: HOLDS AFTER CORRECTION to their named criteria.**
The 1/3 barrier is the pointwise Bakry–Emery example at one negative
central link: six plaquettes contribute `-(3 beta/2)|X|^2`, while
Ric contributes `|X|^2/2` in the radius-2 metric. Thus their sum is
negative for beta>1/3 if the blocking weight leaves that link free
(`gap-mid-max.md:240–248`). This is not an optimal single-site mixing
threshold and says nothing by itself about nu's unknown ground-state drift.
The checked 2/3 bound concerns the specified single-link majorant; 0.775
is the approximate value of `4/(2+sqrt(10))` for the specified vertex
majorant. The `4G_3` slab obstruction retains the cited infrared-bound
premise. These are different operators from nu's gradient form and
the one-step score of V/E. The source is right that its averaged V/E
identities do not assume the old worst-case criteria. It is wrong to
describe all the old results as bounds on one common conditioning-slice
supremum, or infer that every possible sup-based supplier is excluded.
No volume-free SU2 bound is proved merely by placing the expectation
inside these formulas. The old “annealed equals worst case” statement
concerns its own AN1 quantifiers, not every averaged inequality.

The recommendations in Step 8 remain proposed research choices. Their
0.95, 0.9 and 0.4 failure probabilities are the author's judgments,
not computations or established probabilities. The 1/4 curvature range
is a range of the cited method, not a theorem that all vacuum-law
criteria fail above it. This check does not pursue the later owners'
LSI-vac, E-to-HC or CUT-TYP proof tasks.

## 5. Arithmetic and GUIDE evidence

No numerical job was run. The author's rotor script and log are named
under the Mac mini's `/tmp/gap-direction-931/`; neither is in this checkout.
A bounded filename search found no saved copy. They were not inspected
outside the permitted trees. The reported grid resolution, random seeds,
eight-case coverage, maxima, memory and lock receipt are consequently
unverified. This is missing evidence, not evidence that the run failed.

| Computation in the source | Verdict and scope |
|---|---|
| 26 momenta, 52 photon terms, X_ev>31 | HOLDS by the displayed hand estimate in section 2; no enumeration. |
| `x_*=log(22/17)=0.2578`, deficit factor >120, `log 120>4.78` | HOLDS with 0.2578 read as an approximation. Use exact x_* in inequalities. |
| ANOM constant 10.89; HOT sufficient values 14.21 at 2.3, 14.33 at 2.6 | HOLDS as rounded descriptions of `log(24^3/x_*)` and `log(12 beta 24^3/x_*)`. Rounded 10.89 is slightly larger than the exact first constant, so is not an exact iff threshold. |
| HC's 16.0+3 log a | HOLDS as a safe sufficient constant at beta=2.3, after the even-a and SH-only corrections. The exact constant is `log(72 beta 24^3/x_*)`; at beta=2.6 it is about 16.12, so 16.0 cannot be used across the whole window. For W use log(20/19), giving about 17.61 instead of 16.0 at 2.3. |
| Full toron sum about 8.8 at beta=2.3 | HOLDS as an approximation: `X_tor=(3/2)log(48 pi beta)+3log(1+2sum_(n>=1)exp(-48pi^2 beta n^2))`. The correction is a geometric tail. It is the full, not centre-even, toron sum. |
| Photon gamma about 4 pi beta/b; Gaussian V/E factors | HOLDS as b-to-infinity asymptotics for the lowest nonzero oscillator; section 1 verifies the exact identities. Full FP's lowest energy can instead be its softer toron level. |
| Model G `p=1/2-1.4e-10`, `lambda_odd<=L_1/N` | HOLDS at the specified row-930 seed geometry, with the decimal approximate. The exact small quantity is governed by `y=exp(-2.3 pi^2)` and the theta-series bounds in row 933. It is not a universal value for every (a,24a,24a,24a) torus. |
| Frozen p=10/23,30/61; Z2 p=1/2 | HOLDS at beta=infinity. For Q8, `N_0=16+3(256-16)=736`; for 2T add `4(1296-16)` to get 5856; both have N_tw=96. Thus `(1-N_tw/N_0)/2` gives the printed fractions. The finite-box low-temperature limits follow, not uniformity over boxes. |
| Frozen S_ev>=1/2 at large finite beta | HOLDS with the existing fixed-box bound `beta>=log(16E(|G|-1)t)/d_G`, d_Q8=1, d_2T=1/2. The source of this bound is credited in section 2; it is not a newly proved phase statement. |
| FR sufficient size about 420 | HOLDS AFTER CORRECTION: at beta=2.3 and p_*=2e-4, `L^2>=2pi^2 beta^2/(3p_*)` suffices. Using pi^2<10 gives L=420; at beta=2.6 use L=475. This is not a necessary threshold. |
| Endpoint crossing 4.8e4 and photon log trace about 3.0e3 | HOLDS only as the additional black-body approximation's arithmetic. FAILS as an exact fixed-aspect-ratio crossing or full compact-model value. Row 932 already supplies the corrected sums. |
| 2D kurtoses 3/2 and 4, floor 1.66 | HOLDS for real normalized ground functions in the stated 2D models. `sqrt(2)cos phi` has fourth moment 4(3/8)=3/2; the Q8 character has values 2,-2,0 on 1,1,6 elements, so its second and fourth moments are 1 and 4. The 1.66 threshold remains conditional on the much stronger GLUE bound, as row 897 checks. |
| 1/3, 2/3, 0.775, 4G_3 about 1.0109, Z2 Peierls 2.191 | HOLDS AFTER CORRECTION of scope and evidence: retain the named criteria, cited infrared/Peierls premises and approximate Green integral. The 1/3 curvature arithmetic is given in section 4. This session does not independently certify the integral or reconstruct the imported phase estimate. None supplies a numerical ceiling for V/E's averaged constants. |
| Rotor V=0, beta=2.3: 0.5496 against 0.6303 | HOLDS as rounded stated-model arithmetic. Uniform nu has gamma=1, r_1=I_1(beta)/I_0(beta); integration by parts gives Gamma=beta r_1. Thus the two exact quantities are r_1^2 and beta r_1/(1+beta r_1). The positive Bessel series below check these digits without using the 600-point run. |
| Rotor double well: 0.536 against 0.998 | The printed inequality HOLDS numerically; the spectral values and quadrature accuracy are unverified. They are reported GUIDE data only, not a checked fact about that chain. |
| All eight V tests; averaged-eigenfunction tests; 40 densities per case; maximum ratio 0.63 | Unverified run claims. HOLDS AFTER CORRECTION only as an author's report, not as reproduced evidence. V and E are checked by their hand arguments above. Random densities would not verify the universal inequality. |
| Infinite proxy at beta=8 | HOLDS that this tests nothing: a finite left side is automatically <=infinity. It provides no usable finite SG-step constant and no test of sharpness. |

For reproducible hand rounding of the elementary logs, use
`log z=2 sum_(j=0)^n w^(2j+1)/(2j+1)+R`, w=(z-1)/(z+1),
`|R|<=2|w|^(2n+3)/((2n+3)(1-w^2))`, reducing z by powers of two.
It gives, for example, 0.25782<x_*<0.25784,
10.8895<log(24^3/x_*)<10.8898, and
15.9990<log(72(23/10)24^3/x_*)<15.9994.
For the rotor put x=529/400. Use
`I_0=sum_(k>=0) x^k/(k!)^2`,
`I_1=(23/20)sum_(k>=0) x^k/(k!(k+1)!)`.
After k=8, each remaining term is at most 1/50 times the preceding
one; bound each tail by its first term times 50/49. Rational summation
gives `0.74137<I_1/I_0<0.74138`, hence
`0.5496294<r_1^2<0.5496444` and
`0.63033<2.3r_1/(1+2.3r_1)<0.63034`.
These are checks of the analytic one-rotor model, not a rerun or
certificate for the absent discretized script.

For Model G specifically, the imported 1.4e-10 uses the earlier seed
with tau=5/92. On this note's b=24a cube instead
`tau=1/(96 beta)` and `y=exp(-12 pi^2 beta)`.
The flux test is even closer to 1/2 there, but the old decimal is not
the new box's value. The lower and upper theta-series bounds above
retain the exact distinction.

Nelson's exponent is a sharp benchmark, not a requirement that every
valid sufficient E-to-HC estimate be optimal. For a Gaussian channel
with correlation r, testing `h(x)=exp(c x)` under a standard normal law
forces `q-1<=r^(-2m)` for a 2-to-q contraction. Thus a claimed faster
rate is refuted. A slower proved positive rate can still suffice for
HC's seed argument; failure to attain equality alone would not refute it.

## 6. Disposition

The source's load-bearing formal comparisons survive: V, HC's exact
integer-time trace estimate, E and E1. HOT, TENS, GAPRATE, ANOM and the
information identities also survive at the stated domains. No hypothesis
of those comparisons is proved here for the order-one SU2 vacuum law.

The corrections which change downstream use are:

1. HC at x_* gives SH, not the two numerical W bounds. Tighten the
   threshold or change the conclusion; keep the integer-time condition.
2. The table mixes identities, incomplete sufficient hypotheses, free
   and periodic boxes, and Gaussian versus compact coupling paths.
3. The fixed-box weakest-form assertion does not follow and conflicts
   with row 19's weaker full-trace threshold.
4. Finite-box scale covariance does not make kappa=3; the toron assertion
   is false. The >31 spectral refutation remains valid.
5. SMALL-BOX needs a proved lattice premise and a seed-sufficient rate;
   the recalled continuum formula and arbitrary-inequality wording do
   not supply either.
6. Spatial rotation symmetry is not invariance of a conditioned temporal
   kernel. The gradient and spatial-action forms have different photon
   scaling. Old ceilings must retain their own criteria and premises.
7. Fixed-box frozen limits and approximate crossover numbers must retain
   their quantifiers, geometry and evidence class.

The GUIDE run is not reproduced. No numerical proof, audit, status change,
commit, push or external post was made. The check is saved locally on
`lanework` at the requested lane path. The source file remains unchanged.

RESULT: HOLDS for Theorem V, Proposition HC's integer-time trace/gap bounds, Theorem E and E1, ANOM and the elementary identities under their named inputs; HOLDS AFTER CORRECTION for the SH seed application, model tests and ceiling scopes; FAILS for the same-box W conclusion at x_*, the weakest-split-seed claim, the indicated Step-3 classifications, kappa=3 for the finite-box photon/toron model, and SMALL-BOX as an unconditional exclusion. GUIDE run claims remain unverified because their artifacts are absent. No order-one seed or mass gap is established; research check only, no status granted.
