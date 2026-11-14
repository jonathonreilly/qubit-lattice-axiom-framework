<!-- Reconstructed by the lead (Claude Opus 5.5) on 2026-11-14 from the Codex event log ~/ym4d-lead/logs/gap-seam-check-astra.jsonl. The laptop runner lost the written file (the lead queued it with a wrong output path, and the next checkout cleaned the tree). This text is Codex's own full read of its report (sed ranges 1, 146, 291); Codex made 3 small edit(s) AFTER that read, whose content the log does not record. So the body may differ slightly from the final version. Final RESULT line (from Codex's own tail, if logged) and final message follow at the end. -->

# Repo search

Refs searched in `/Users/jonreilly/Projects/Physics`: `origin/main`
`4d88da5504d356762deb6b1a1c2695336af9fb81`; `pr/10114`
`f76f6c649cff7dffbab664d8976e680e8f287fe9`; `pr/10133`
`89faef229ff6e6bde42baad15ed8270c2f4087d8`; `pr/10134`
`1e70c7211a2cdbc39001e619f1dd89db45e25851`; `pr/10141`
`c73ad7b177d94f89ff37b77386936e3d52b48b05`.

The completed exact-target query
`cut.and.reglue|Proposition INS|SEAM\)_a|gap-seam-max|gap-seam-check-astra`
on all five refs, `*.md`, `*.tex`, head 15, found **no hits**.
Broader queries included `(SEAM)`, word-bounded `S_ev`, `Delta_theta`,
`Mehler`, `frozen Q_8`, and `frozen 2T`. They reached their caps and are
locators only. Their relevant sources, read at the cited ranges, are:

| Source | Exact statement and closeness |
|---|---|
| main, `docs/FINITE_STEP_GAUSSIAN_GAUGE_CANONICAL_LOGARITHM_AND_COULOMB_COST_BOUNDED_THEOREM_NOTE_2026-09-14.md:76–110` | B1–B3 give the Gaussian transfer kernel with frequency `2 asinh(sqrt(beta_s lambda/beta_t)/2)` and zero-point energy omega/2; the zero mode needs a separate prescription. This is the same oscillator method used by M, already present. It does not evaluate the two-copy seam or the compact flux sum. Credit this earlier derivation; M is a specialization, not a new method. |
| main, `research/mass-gap/library/gap-crux-fp.md:319–345` | COV bounds the covariance of bounded layer observables by `2(1+sigma)r^(d-1)+5sigma`, assuming `sigma=S(D/2;D^3)<=1/2`. It uses the vacuum/complement trace decomposition and Hilbert–Schmidt Cauchy–Schwarz. Same method as Q, different seam and a supplied small trace. |
| lane, `gap-crux-skeleton-max.md:104–122,190–198` | I1 is the vacuum Doob chain; I2 is `S(2s)=||p_s-1||_2^2`; B1 is the adjacent-pair law `Omega T Omega/lambda`. These are existing inputs to J and Q, reused without another attack. |
| lane, `gap-glue2-opus.md:111–182` and `gap-glue2-check-astra.md:41–166` | S1/S2, INS, C1/C3 and BR provide the seam operator, endpoint traces, normalized change of law and derivative of F. Existing inputs, with row 921's corrections retained. |
| lane, `gap-crux-exercise2-check-astra.md:227–260` | Two distinct centre-even flat vectors give FG1–FG2 for Q8/2T. Exact prior fact test, reused in section 7 below. |

The November 8 digest was read; its seam hits concern retained covariances
and rotation defects, not this seam. The existing `gap-seam-check-opus.md`
checks row 796's twist cochain, not row 929. No duplicate row-932 check or
registry owner was found. FINISH row 932 has no additional "Repo prior work"
line. This is a check of row 929, not an attack on a separately owned seed.

Provenance: Codex, row 932 (requested gpt-6-astra, xhigh), checking
`gap-seam-max.md` at `bc2b3762f5119a2fa10474441c6a95ea66dd403f`.
Research text, not an audit; no scientific status is granted.
The target-specific `library/prior/gap-seam-check-astra.md` is absent.
The registry search found no owner for this check or its new statements.
The author note is not edited. No computer run will discharge a claim.

## Checkpoint

All proof statements have verdicts below. Mathematical checks use displayed
Gaussian integrations, gauge averages and spectral identities, not runs.
GUIDE run reproduction is limited as stated in section 8. Only this output
file is changed. The remaining scientific obligations are the full rotor
seam profile, the compact-Wilson comparison, XM and the SU(2) order-one seed.

## 1. Exact free-photon trace — HOLDS

Source: row 929, lines 96–138 (M, F, A1, A2). These statements hold for
the explicitly **defined tensor-product model FP**. Its identification with
a particular compact Villain lattice measure is only argued in the source.
No such identification is needed for the tensor-product calculation.

For a mode set `c=1+kappa/2=cosh(omega)` and `sigma=sinh(omega)`.
Completing the square against `exp(-beta sigma q'^2/2)` gives the ground
eigenvalue `lambda=(2pi/beta)^(1/2)exp(-omega/2)`. Integrating the diagonal
of the displayed n-step kernel gives
`Tr(T^n)/lambda^n=1/(1-exp(-n omega))`.
The Gaussian convolution prefactor in M agrees at n=1 and at each
convolution. Fourier transformation of the periodic Gaussian in F gives
the ratio `exp(-|e|^2/(2 beta b))`; projection by the three pi shifts keeps
`e=2j`. Thus A1's product, including its compact electric-flux factor, holds.

A2 uses 26 distinct momenta and two polarizations each. Its inequality
`a omega <= pi sqrt(3)/12 < 1/2` follows from `sin x<=x` and
`asinh x<=x`. Hence `log(1+S_ev)>52 exp(-1/2)>31` by hand. For the last
strict inequality one can bound `exp(1/2)<5/3` by its series.
For beta>=1, `exp(-1/(12 beta))>=1-1/12=11/12`; the flux factor alone is
at least `(17/6)^3>22`. No numerical enumeration enters these conclusions.

## 2. Path G — HOLDS AFTER CORRECTION of domain and model coverage

Source: lines 140–186, Proposition G(a)–(d). The two 2-by-2 blocks obtained
by taking symmetric and antisymmetric endpoint coordinates give exactly
the printed determinant factors. Logarithmic differentiation gives the
printed G(theta), with the correct sign. Both differences are positive:
`alpha_-<eps_-`, `alpha_+>eps_+`, and `eps_+/2>1`. Their integral is
`-log(1-exp(-a omega))`, since the reference determinants agree at the ends.
These are exact photon-mode identities for **a>=2**. The formulas containing
`tanh((a-1)omega/2)` do not literally define the a=1 case. That case needs
the diagonal seam constraint u'=u. It has the continuous limiting values
`h_-=(c-1)(E-1)/(c+E-2)`, `h_+=E+1` in G(c). Substitution in its
integral gives `-log(1-exp(-omega))` again. This explicitly extends the
photon conclusion to a=1; it does not define the omitted rotor seam.

The exact endpoint and interior values need no numerical evaluation. They
also admit a check independent of the four-by-four determinant:

`G(0)=coth(omega)/(exp(a omega)-1)`,

`G(1)=coth(omega) exp(-a omega)`.

Indeed, the vacuum Doob chain has covariance
`c_j=exp(-j omega)/(2 beta sinh(omega))`: completing its conditional
Gaussian square gives mean `exp(-omega)q` and ground variance
`1/(2 beta sinh(omega))`. On the length-a ring the adjacent covariance is
`[exp(-omega)+exp(-(a-1)omega)]/[2 beta sinh(omega)(1-exp(-a omega))]`.
At theta zero subtract c_1 and multiply by beta, giving G(0).
At theta one the ring segment lies between vacuum half-lines; the two
mismatched covariances are c_(a-1) and c_(a+1). Their sum times beta gives
G(1). These formulas also hold with the diagonal convention at a=1.

For the interior put `u=eps_-/2`, `v=eps_+/2`:

`2G(1/2)=1/(h_-+1/2)-1/(u+1/2)+1/(v-1/2)-1/(h_+-1/2)`.

Summing twice over k and dividing by `3 beta b^3` gives the exact photon
contribution at all three requested theta values.

Both endpoints fail the photon SEAM test at **every** a. For each of A2's
26 momenta, `omega<1/(2a)`, `coth(omega)>=1/omega` and
`exp(-a omega)>3/5`. Thus `G(1)>(6/5)a` and G(0)>G(1). With two
polarizations, `3 beta b^3 Delta^G_1>(312/5)a`. Since log(1.1)<1/10,
each endpoint exceeds psi by more than **624a**. Moreover G is strictly
convex and G(0)>G(1), so the photon supremum is exactly Delta^G_0.
This is a hand bound in the stated photon model, not a Wilson endpoint claim.

**Coverage defect.** The seam family is defined only for transverse
oscillators. No theta-dependent compact-rotor seam is specified or evaluated.
Consequently its exact Delta values are not the full FP Delta, although A1
counts those rotors. Also the quantity labelled `Delta_0^cpt` is an
anisotropy derivative of the photon trace. Lemma E for compact Wilson
plaquettes does not identify it with an endpoint of path G. The source
correctly distinguishes the two endpoints but supplies no compact model
with both the asserted spectrum and that Wilson seam observable.

The photon sector alone already has log trace greater than 31. For its
path G, the integral identity and positivity prove failure of both SEAM
and SEAM-L1, by more than `31/log(1.1)>325`, for every integer a>=1,
using this diagonal convention at a=1. For the full FP
model the same average argument applies to **any specified** interpolation
with these endpoint traces and INS normalization; it does not compute
the missing rotor profile. Compact Wilson U(1) remains a separate GUIDE
claim, as the source itself acknowledges.

## 3. Fixed-shape limits — FAILS as printed

Source: lines 139, 188–200, 219–243. At b=24a, the rescaled momentum mesh
is fixed: `a k=2pi n/24`. It does not tend to a continuum mesh. Therefore
the displayed infinite-volume black-body constants are not the exact
a-to-infinity limits in the stated geometry. They are further large-aspect-
ratio approximations. The exact photon trace limit is instead

`C_24=-2 sum_(n in Z^3, n!=0) log(1-exp(-2pi |n|/24))`.

The full FP trace also retains the nonzero, a-independent term

`C_24=-2 sum_(n in Z^3, n!=0) log(1-exp(-2pi |n|/24))`.

The full FP trace also retains the nonzero, a-independent term
`3 log sum_j exp(-j^2/(12 beta))`. Calling this term negligible does not
remove it from an exact asymptotic coefficient. Corrected coefficients
are as follows. Put R=24, `q_n=2pi |n|/R`, and sum over nonzero integer
triples. For photon quantities only,

`beta a^3 average(Delta^G) -> C_R/(3R^3)`,

`beta a^2 Delta^G_0 -> (2/(3R^3)) sum 1/[q_n(exp(q_n)-1)]`,

`beta a^2 Delta^G_1 -> (2/(3R^3)) sum exp(-q_n)/q_n`,

`beta a^4 Delta^G_theta -> (1/(6R^3)) sum q_n [exp(-q_n)/theta^2 + 1/((exp(q_n)-1)(1-theta)^2)]`

for fixed 0<theta<1. The photon anisotropy-derivative quantity has
`beta a^4 D_0 -> (1/(3R^3)) sum q_n/(exp(q_n)-1)`.
Thus the powers a^-3, a^-2 and a^-4 survive, but their printed constants
and the exact ratio `3/(2a)` do not. The ratio's coefficient is
`sum q_n/(exp(q_n)-1)/C_R`, before adding any rotor derivative.

To check these limits, use `omega=q_n/a+O(a^-3)` for each fixed n and
`h_-=omega(1-exp(-q_n))/2+O(a^-2)`,
`h_+=1+omega/[2(1-exp(-q_n))]+O(a^-2)` in G(c).
For centred lattice representatives, `sin(pi |n_i|/b)>=2|n_i|/b`;
`asinh(x)/x` has a positive minimum on `[0,sqrt(3)]`. Hence
`a omega>=c|n|/R` with c>0 independent of a. These bounds dominate the
tails by convergent polynomial-times-exponential sums and justify passage
to the limits. Replacing these sums by integrals is a separate R-to-infinity
limit and gives the source's black-body coefficients.

Each endpoint layer carries half the limiting photon log trace: integrate
the first reciprocal difference on theta of order 1/a and the second on
1-theta of that order. Each gives `-log(1-exp(-q_n))/2` per mode.
The supremum grows relative to the average by order a. Each G is strictly
convex, so its maximum is at an endpoint; the sum has the same property.
These structural statements hold without the erroneous fixed-shape constants.
The interior limiting function has positive derivative at theta=1/2,
because `1/(exp(q)-1)>exp(-q)`. Its minimizer is not exactly 1/2.
Read the table's "least at theta=1/2" only as its least **sampled** entry.
The claimed crossover sizes 4.8e4 and 1.8e5 are therefore large-R heuristic
estimates, not exact failure thresholds for the stated fixed-shape model.

## 4. Junction symmetry — HOLDS AFTER CORRECTION

Source: lines 293–316, Lemma J(a)–(c). The raw identity
`K_theta(U,W;U',W')=K_theta(U',W';U,W)` at lines 293–294 **FAILS**.
Inverting g and h makes the crossed plaquettes exchange their temporal
variables; it does not put the shared variables back into the same rows.

There is a small-coupling counterexample within the SU(2) configuration
domain, on b>=3. Write x(V)=tr(V)/2. Haar integration gives
`integral x(Ah)x(Bh) dh=x(AB^-1)/4`. The cross term between the two
plaquettes in each row of the seam therefore contributes

`[beta^2 theta(1-theta)/2] sum_l x(U'_l^-1 W'_l)`

to K_theta. All other second-order terms are configuration-independent.
The reversed kernel has U,W in this sum. Take U=W=U'=1 and set just one
link of W' to -1. The second-order coefficients differ whenever 0<theta<1.

The needed conclusion, symmetry of **Nt_theta**, does survive. Here is the
missing argument. Its integrated W,W' weights and its U,U' magnetic
weights are separately gauge invariant. Nt is separately gauge invariant
in U and U': for U absorb its gauge change into g; for U' change W' by the
same gauge and change g,h. Thus Nt may be computed using the seam kernel
averaged over independent gauges of all four external slices.

In that averaged kernel the four temporal transports at each site can be
written `v_ij=a_i b_j^-1`, with two independent Haar a's and two independent
Haar b's (one common redundancy is harmless). Time reversal sends
`v_ij` to `v_ji^-1=b_i a_j^-1`. Swapping the Haar families preserves their
law and the symmetric weights `w_11=w_22=1-theta`, `w_12=w_21=theta`.
Trace cyclicity and inversion preserve each real plaquette trace.
The averaged kernel is symmetric. Integrating its second copy against
psi on both ends proves Nt symmetry. This repairs the trace-square step
without assuming the false pointwise identity.

Now put `A_k=That^k N_theta That^k`. Its pair density is
`A_k(Y',Y)/(n(theta) Omega(Y')Omega(Y))`. Extending each vacuum half-line
uses `That Omega=Omega`, so outward evolution is the product Doob chain
P tensor P and gives J(a), J(b)'s density and J(c)'s conditional
independence. Direct integration gives
`1+X_theta(k)=||A_k||_HS^2/n(theta)^2=Tr(A_k^2)/n(theta)^2`,
using the repaired symmetry only at the last equality. N_0=That and
N_1=|Omega><Omega| give `X_0(k)=S(4k+2)` and `X_1(k)=0`.
Even without a symmetry proof the valid formula would be `Tr(A_k* A_k)`.

## 5. Proposition Q — HOLDS

Source: lines 318–333. Set n=a-1-2k>=1. The common near-seam conditional
law gives `Delta E[q]=E[(delta-E delta)(q-1)]`, with q=pbar_n.
The extension of C3 from k>=1,n>=2 to k=0 or n=1 causes no problem:
at k=0 it is C1, and at n=1 there is still one ordinary transfer edge.
All kernels are bounded at a fixed compact box; Omega has a positive
minimum. Thus the needed L2 integrals exist.

Under the product measure nu tensor nu, the even off-vacuum expansion
of q-1 has squared norm S_ev(2n). Conditional expectation gives
`H=(E[delta|Z_k]-E delta) kappa_(theta,k)`, with integral zero and
`||H||_2<=8 sqrt(1+X_theta(k))`. Cauchy–Schwarz proves the printed
`|Delta| E[q]<=8y`. In fact the denominator bound is the sharper
`E[q]>=1-sqrt(S_ev(2n)X_theta(k))`; weakening it to 1-y is valid.
No bound uniform in box size or coupling is supplied by this algebra.

## 6. Q1–Q4, SP and other implications

**Q1 — HOLDS in the requested coupling window.** The condition y<=psi/9
implies `8y/(1-y)<=psi` when psi<=1. This holds at beta in [2.3,2.6]
and b=24a. For a statement at arbitrary positive beta, replace psi/9 by
`psi/(8+psi)`. The new sufficient hypotheses are global; they do not
prove that the earlier local hypotheses hold or cannot be useful.

**Q2 — HOLDS AFTER CORRECTION.** Its two implications hold, with Q1's
qualification. The time 2a-2-4k is later than a only if
`k<(a-2)/4`, not for every allowed k. The sufficient thermal product
must be below `(psi/9)^2`, which scales as b^-6 at fixed beta. This is
an additional strength requirement; it is not just a change of time.

**Q3 — HOLDS AFTER CORRECTION as a diagnosis of this bound alone.**
For `Y=sup_theta y_theta<1`, INS and Q give
`log(1+s)<=24 beta b^3 Y/(1-Y)`, s=S_ev(a).
Cauchy–Schwarz on the same fixed-box eigenvalues gives
`s^2<=S_ev(2a-2-4k)S_ev(4k+2)<=y_0^2<=Y^2`.
Thus the right side is at least `24 beta b^3 s/(1-s)` when s<1.
In the requested window this exceeds s, while log(1+s)<=s. The lower
bound on Y therefore yields no upper bound on s. This is not a theorem
that Q together with an independently supplied small upper bound on Y
cannot prove the glue half: Q1 explicitly does exactly that.

**Q4 and the repeated "no easier handle/no input below a seed" conclusion
— FAILS as an exclusion or minimality theorem.** An alternative sufficient
pair of global estimates does not prove necessity, equivalence, or the
impossibility of a useful local supplier. X is a normalized two-seam
partition function, not an ordinary thermal trace for intermediate theta.
Retain only: this session did not supply a smaller SU(2) estimate.

**SP — HOLDS.** Expand the trace in the even transfer eigenbasis and
divide by `lambda^(a-1)<Omega,Nt_theta Omega>`. The vacuum term is one;
the remaining terms are exactly those printed at lines 368–374. Boundedness
of Nt and trace class of T^(a-1) justify the expansion for a>=2.
The endpoint coefficients are r_i and zero. No positivity of intermediate
diagonal matrix elements is asserted or needed.

**Lipschitz formulation and SEAM-L1 (lines 257–267) — HOLDS.** The
derivative identity gives the claimed bound on F'. Integrating |Delta|
is a sufficient condition, weaker than its supremum bound. Only the
signed integral is equivalent to the trace target. Positivity of G makes
the photon L1 integral equal its signed integral. Reparametrizing a path
changes its supremum but preserves these integrals.

**Conditional XM implication (lines 415–423) — HOLDS.** If XM is supplied,
substitute X(k)<=S(4k+2) into Q1, with the same threshold qualification.
Hölder does bound the unnormalized two-seam numerator by
`(1+S(4k+2))^(1-theta)`. Convexity gives n(theta)<=1, so dividing by
n(theta)^2 does not prove XM. Neither XM nor equivalence with a thermal
seed is established.

## 7. Fact tests and remaining route statements

**Photon spectral test (lines 362–366,440–441) — HOLDS AFTER CORRECTION.**
At t=2n<=2a the same 52 soft oscillators give
`log(1+S_ev(t))>52/e>19`, hence the proposed y is greater than one.
This exactly refutes Q1's small-thermal-product hypothesis in FP.
However Q's proof uses `|delta_l|<=4`. The Gaussian path-G score is an
unbounded quadratic function. Q is not thereby proved for path G; only
its proposed spectral sufficient condition is being fact-tested there.
J's Gaussian integrability would also need its own domain checks before
using X. None is needed for the photon failure established in section 2.

**Frozen Q8 and 2T (lines 435–439) — HOLDS at a fixed box.** Reuse FG2,
not a new enumeration. For E=3b^3,

`beta >= d_G^-1 log(16 E (|G|-1)t)` implies `S_ev(t;B)>=1/2`,

where d_Q8=1 and d_2T=1/2. Apply it separately at t=a for failure of
GLUE, SEAM and SEAM-L1, and at t=2n for failure of Q1's hypothesis.
For both simultaneously use t=max(a,2n) in the sufficient beta bound.
The latter gives y>=1/sqrt(2), far above psi/9, but does **not** by itself
give y>=1. At strictly infinite beta the simple-vacuum hypotheses are
lost; use the displayed finite-beta statement. No fixed-beta, all-size
claim or conclusion at beta 2.3–2.6 follows from FG2.

**Frozen Z2 (lines 442–444) — HOLDS as a conditional statement.** The
source `gap-es1-opus.md:157–168` gives the fixed-box bound
`S_ev(t)<=C_B exp(-8 beta t)`. If X_theta(k) stays bounded along the
limit, Q forces Delta_theta to zero. Uniform boundedness over theta
would give the corresponding uniform conclusion. Neither boundedness
assertion is proved by the note, and it labels this omission OPEN.

**Group-blindness (lines 430–434) — HOLDS AFTER CORRECTION.** J/Q/SP apply
to the compact Wilson models with their bounded score and the common
conditional law. The symmetry proof must be replaced as in section 4.
For Q8/2T, powers of the restricted fundamental character are tensor-product
characters with nonnegative multiplicities, so the exponential weight is
of positive type. This supplies positive semidefinite transfer operators;
strict positivity of every eigenvalue is not needed for the argument.
Do not extend the bounded-score assertion to FP.

**Ceilings (lines 283–286,402–403,445–449) — HOLDS AFTER CORRECTION of
their scope.** The source passages read give these exact restrictions:

| Input read | Exact ceiling and domain |
|---|---|
| `gap-arealaw2-check-astra.md:111–134` and its exact single-site barrier | The specified six-neighbour single-site criterion has row sum 6(beta/4) and requires beta<2/3. Its specified in-star Green-function bound gives `30c^2/(1-6c^2)<1`, c=beta/4, again beta<2/3. |
| `gap-blockcrit-check-astra.md:332–355` | The chosen vertex-block majorant has a submatrix with spectral radius `(beta/4)(2+sqrt(10))`. Its Neumann criterion fails at `beta>=4/(2+sqrt(10))`, approximately 0.775. This is not a lower bound on the optimal block response. |
| `gap-arealaw2-check-astra.md:342–378` | Given the stated Fröhlich–Simon–Spencer infrared bound, the flat-slab magnetization obeys `M^2>=1-4G_3/beta`. Thus background-uniform, volume-uniform exponential slab two-point decay fails for beta>4G_3. Here `G_3=(2pi)^-3 integral 1/[2 sum_i(1-cos p_i)] dp`; 1.0109 is an approximate value. |

These restrictions concern their named criteria. They neither cap Q's
averaged identity nor exclude every worst-case block supplier for S_ev
or X. Correct the last sentence of section 7 to name the three specific
criteria. The FSS premise is retained as a cited conditional input; this
check neither rebuilds it nor certifies the decimal integral by a run.

**Routes 6.2 — HOLDS AFTER CORRECTION as failed attempts, not exclusions.**
The Hilbert–Schmidt derivative inequality holds if R is the even
off-vacuum transfer power, tau=t+2d+1, and its derivative norm is finite.
Integrate the endpoint difference and apply Cauchy–Schwarz; the lower
bound on the supremum of the derivative norm is its endpoint distance.
It does not prove that every other derivative estimate is empty.
The hypothetical iteration `s(a)<=A sqrt(s(2a-c))` gives the stated
limit for a>c only when it holds at every iterated time on **one fixed
box**, with the same A,c and spectrum. No such estimate is supplied.
The Hölder/convexity discussion is sound; a difference of convex log
partition functions has no prescribed curvature. The curvature route
supplies no new order-one bound.

Two physical readings need narrowing. SU(2)'s centre removes the conserved
integer flux label of FP; it does not remove all centre-even multi-torelon
states. The abelian angle identity holds modulo 2pi for compact phases
(exactly for chosen noncompact lifts). Mode decoupling follows from the
**quadratic Gaussian action**, not from that identity for a general compact
U(1) weight. The source's XY-seam and SU(2)-seam crossover discussions
remain heuristic proposals, with no quantitative conclusion to certify.

## 8. GUIDE arithmetic and evidence limits

No numerical job was run. The author's scripts and logs are in another
machine's `/tmp/gap-seam-max-929/`, not in the permitted source trees.
They were not opened. `scripts/lab_ops.py`, required by FINISH for the
machine numeric lock, is absent from this pinned checkout. Thus the
reported run agreement, residual tolerances, maxima and resource figures
are **not reproduced or certified** here. This is a limitation, not a
claim that the recorded runs failed. The following checks are by hand.

| Source computation | Verdict on its stated formula/arithmetic; limit |
|---|---|
| A2's 26 modes, 52 terms, >31 and flux factor >22 | HOLDS, by section 1. |
| Section 4 thresholds | HOLDS to displayed rounding. Their denominators are 6,104,678.4; 95,385,600; 349,920,000. Use the exact log(1.1) thresholds for implications. |
| Section 4 average and all bracketed ratios | HOLDS as arithmetic from the displayed entries: average=C/(3 beta b^3), average/psi=C/log(1.1), and each other ratio is its entry divided by psi. Rounded mantissas need not reproduce a final digit computed before rounding. |
| Section 4 photon trace, anisotropy derivative and path-G sum entries | HOLDS as the exact finite-sum formulas A1/G and the photon derivative at lines 184–186. The printed evaluations themselves are unverified GUIDE digits; they are not upgraded by checking the formula. In particular the column called compact endpoint must be renamed photon anisotropy derivative. |
| Section 3.1 even-flux 6.69 and 6.82 | HOLDS at two-decimal precision: Poisson summation gives `3 log theta=1.5 log(12pi beta)+3 log(1+2 sum_(m>=1) exp(-12pi^2 beta m^2))`. The remainder is exponentially tiny for beta=2.3,2.5. |
| Optional magnetic-flux 0.79 and 0.68 | HOLDS AFTER CORRECTION to a specified extra factor `theta(exp(-2pi^2 beta a/b))^3`. This is a different model. It is unused; no magnetic sector appears in A1. The displayed figures are low-precision approximations, not certified rounded values. |
| Black-body 3031.94, factor about 3.2e4, coefficient about 0.76a, and 4.8e4/1.8e5 crossover estimates | HOLDS as arithmetic of the further infinite-spatial-volume approximation; FAILS as exact a-to-infinity constants or crossing guarantees at b/a=24. Section 3 gives the correct sums. |
| G determinant run: five parameter pairs, 12-digit agreement | Exact algebra HOLDS by section 2; the run and its precision are not verified. |
| Q toy thermal traces 0.004301033, 0.1848260, 0.002312535 | Exact stated-model formulas: for Z4, `log(1+tanh(beta/2)^(4a))`; for Z6, `log(1+2[(cosh beta-cosh(beta/2))/(cosh beta+2cosh(beta/2))]^(2a))`. Z2 has zero even excitation exactly. These follow from the two-link convolution eigenvalues, not an SU(2) computation. No claimed floating-point precision is certified. |
| Toy endpoint identities, X_0 and INS | HOLDS analytically in the compact toy model by S2, repaired J and INS, without enumeration. The finite-grid errors and largest Q ratio 0.020 are not verified. |
| Toy interior maximum, 5.270e-2/3.369e-2 | HOLDS as a ratio about 1.56. This does not locate or certify the maximum, nor reproduce row 920's different quadrature-grid maximum 1.585. |
| XM's 24-of-24 cases, n(theta) minimum 0.065 | The claimed computation is not verified. XM remains OPEN; the conditional implication alone HOLDS. |

The source's constants 0.051,0.050 and 0.035,0.034 follow from its rounded
endpoint entries times beta a^2; its interior and derivative rescalings
also agree at their printed precision. Those checks do not repair the
wrong limiting coefficients or establish uncomputed compact seam values.

## 9. Source scope and final verdicts

The SA-index README, the GL8 neighbouring rows in chunk 02, and searches
of all chunk files and obligations.md were used first. The query
`cut.and.reglue|centre.even|center.even|thermal.sum|Mehler|chi.square|electric.flux`
found no hits there. GL8's source was then read at outline lines 2313–2352:
it constructs a positive trace-class gauge-projected transfer and states
`Z_s(0)=Tr L^s`, proved by integrating temporal bonds and trace cyclicity.
This is an existing input, credited to Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text. The on-disk SA directory
has no Git metadata; its revision is the user-supplied 31a47c543775.
No new CA-I–III theorem is claimed, and these bounded reads are not a
full absence theorem across those accounts. No estimate from Balaban's
original papers enters the new finite-volume algebra; those papers were
not read.

| Statement in row 929 | Verdict |
|---|---|
| M; F; A1; A2; failure of GLUE in defined FP | HOLDS |
| G(a)–(d); exact photon Delta; positivity; photon SEAM failure | HOLDS AFTER CORRECTION: photon family, diagonal convention at a=1 |
| Exact full-FP Delta or compact-Wilson endpoint identified by the photon spectrum | FAILS as a supplied exact calculation; rotor seam and compact identification are absent |
| Fixed-shape Riemann limits and exact endpoint/average ratio 3/(2a) | FAILS; replace by fixed-aspect-ratio sums |
| Order a^-2 endpoint values in layers of width order 1/a, order a^-4 interior, growing sup/average | HOLDS AFTER CORRECTION of constants and model scope |
| Lipschitz formulation; SEAM-L1 sufficient condition | HOLDS |
| Raw seam-kernel time-reversal identity | FAILS |
| J(a)–(c), including trace square | HOLDS AFTER CORRECTION: gauge-average symmetry proof |
| Q | HOLDS |
| Q1 | HOLDS in beta 2.3–2.6; general threshold correction given above |
| Q2; Q3 | HOLDS AFTER CORRECTION of time range and claimed exclusion |
| Q4/minimality/no easier method; equivalence to thermal sums under XM | FAILS as asserted deductions |
| SP; conditional XM sufficient condition | HOLDS |
| Photon failure of the proposed spectral condition | HOLDS; Q itself needs its bounded-score domain |
| Frozen Q8/2T test; conditional Z2 limit | HOLDS in the stated fixed-box domains |
| Ceiling imports and exclusion of all worst-case suppliers | HOLDS AFTER CORRECTION to the named criteria and FSS premise |
| GUIDE evidence | Formula/arithmetic verdicts and unreproduced evaluations are distinguished in section 8 |

RESULT: Row 932: the exact defined-FP thermal sum and photon-path SEAM failure hold (both photon endpoints exceed the threshold by more than 624a); the full compact seam profile is not computed, the fixed-aspect-ratio constants and raw-kernel symmetry claim fail, J holds after the gauge-average repair, Q and SP hold, and Q1–Q4 require the domain and non-exclusion corrections above. Frozen-group tests retain their fixed-box scope; GUIDE run precision is unverified. The SU(2) order-one seed remains OPEN. Research check only; no status granted.


## Recovery note

Codex's last edit came after its final full read; its final RESULT line was not printed separately.

Codex's closing message:

Wrote [gap-seam-check-astra.md](/Users/jonreilly/ym4d-lead/lane/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-seam-check-astra.md).

Both Gaussian photon endpoints fail SEAM at every size. Q and SP hold; J needs a symmetry-proof repair. Fixed-shape constants and broader exclusion claims fail.

GUIDE runs remain unverified. Only the report changed; it is local and uncommitted.
