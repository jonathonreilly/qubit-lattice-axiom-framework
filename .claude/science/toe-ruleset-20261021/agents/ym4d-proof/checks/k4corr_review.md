# Independent hostile review of K4CORR

Reviewed 2026-10-30 under [PROCESS_LIGHT](../PROCESS_LIGHT.md).
This is **same-family review: Codex reviewing Codex**, performed in a fresh
reviewer context. Independence here means an independent derivation and
adversarial check, not a different model family.

The reviewed [K4CORR.md](../K4CORR.md) has 461 lines and SHA-256
`e7d63ea8071f8f9c7eeadfb4f7c02ce0efc2435809096f8c30099c2dc094d689`.
I read the author brief, PROCESS_LIGHT, K4MATCH sections 1 and 6,
REVIEW_K4MATCH R9/R10 and B1--B3, CUMUL's normalization and smooth free
constants, FLOW F-norm/F-ll/F-tune and its final UNIV status, TSE55's
matching scope, LGF's free-kernel scope, and SRC2_55's source-drift caveat.
The derivations below do not depend on the author checker. I inspected its
code, stored results and resource receipts; I did not rerun it or run any
unregistered numerical test. This review is the sole file I created. I did
not edit the manuscript, any existing source, coordinator, audit or ledger
file, and made no commit.

**Completion finding: HOLD.** The conditional/formal calculations pass
after the repairs described below. The actual finite Yang--Mills coefficient
has not been evaluated or rigorously bounded, and no uniform original-law
remainder has been obtained. Honest OPEN labels preserve useful research
progress; they do not complete the requested author brief.

| Author target | Review finding |
|---|---|
| Item 1: actual relative first correction, including logarithms and anomalous scaling | Common-log and anomalous-factor algebra pass at their stated conditional scope. The finite coefficient `c=a4-2a2` remains OPEN. |
| Item 2: relative short-distance o(1), rate and sign relevance | The rate of an isolated finite `c/u` passes conditional on FLOW. An asymptotic estimate for the actual full ratio remains OPEN. Either sign is compatible with the sufficient positivity bound. |
| Item 3: rigorous explicit magnitude bound if no closed form | OPEN. Neither the graph bounds nor the uniform remainder constants have numerical or analytic certified values. |
| Exact K4MATCH discharge | Only the universal RG and common anomalous-factor bookkeeping in section 6.2/R10 is discharged conditionally. Binding scientific obligation B1, C-4MATCH, C-2MATCH and PL-4C remain OPEN. |

**R1. Observable, coupling units and free normalization -- PASS.**
Locations: section 1, equations (1)--(3).

For one plane, expanding the trace gives
`s(U_p)=a^4 mathcal F_mu,nu^a mathcal F_mu,nu^a/(4N)+o(a^4)`.
Four clover copies cancel the prefactor four in e; the ordered-plane sum
then gives `e=mathcal F^2/(4N)`. The Wilson action sums unordered planes,
so its density is `u mathcal F^2/(8N)=u e/2`. Matching to
`mathcal F^2/(4g_std^2)` gives `u=2N/g_std^2`, hence
`g_std=sqrt(2N)h` and `e=h^2 F_can^2/2`. This reproduces CUMUL's
`u^-1 sum_(mu<nu,a) F_mu,nu^a F_mu,nu^a`, without a hidden factor of two.

Differentiating `g_std=sqrt(2N)h` gives
`b0=(2N) b0_std=11N^2/(24 pi^2)`, and differentiating `u=h^-2`
gives the distinct slope `B=2b0=11N^2/(12 pi^2)`. FLOW F-norm supplies
exactly this conversion. FLOW's final section still has OPEN ingredients
for realizing its universal slope on the actual chain; K4CORR preserves
that conditional status and does not manufacture a two-loop coefficient.

The smooth constants are kept distinct from the point values. CUMUL's
support enclosures imply `3/2<A<5/3` and `11<B0<13`, whence
`3/(338d)<A/(d B0^2)<5/(363d)`. The continuum insertion `X_i0` in
section 5 therefore has the correct free coefficients A4 and A2 for the
chosen unflowed separated bumps. LGF supplies only the free-kernel limit.

**R2. Action-density anomalous convention -- PASS CONDITIONAL.**
Locations: section 2.1, equations (4)--(5).

The statement requires the coupling-insertion identity and RG/Ward identity
in the same physical separated sector. It does not follow merely from the
classical plaquette expansion. With those premises, commuting
`D=mu partial_mu+beta_u partial_u` past `partial_u` gives
`[D,partial_u]=-beta_u' partial_u`. Applying this to the action identity,
modulo the expressly assumed redundant terms, gives
`D e_R=-beta_u' e_R`.

An independent variable-change calculation gives

    d beta_u/du
      = [d(-2 beta_h h^-3)/dh]/(-2h^-3)
      = beta_h' - 3 beta_h/h.

For `beta_h=-b0h^3-b1h^5-b2h^7`, this is
`-2b1h^4-4b2h^6`; the order-h-squared coefficient is exactly zero.
For `O_can=2h^-2 e_R`, direct differentiation instead gives
`gamma_can=gamma_e+2 beta_h/h=beta_h'-beta_h/h`, namely
`-2b0h^2-4b1h^4-6b2h^6`. Substitution of the canonical convention for
the clover convention would be a real error. The manuscript avoids it.

I checked the attribution against [Suzuki, sections 2 and 4](https://arxiv.org/html/1304.0533v6).
Its equation (4.7) uses `gamma_S=-beta'+3 beta/g`, opposite to the
manuscript's convention `D e_R=-gamma_e e_R`; the attribution is accurate.
That source is not evidence for lattice matching. The commutator calculation
above rebuilds the conditional identity needed here. Balaban and Dimock
retain the constructive-method credit given by the author; no estimate
from them is imported as a completed dynamical input.

**R3. Ward factor, integrated evolution and matching -- PASS CONDITIONAL.**
Locations: section 2.2, equation (6).

Set `H=beta_u/(2b0)=-beta_h/(b0h^3)`. Its logarithmic derivative obeys
`beta_h H'/H=beta_h'-3 beta_h/h=gamma_e`, so
`D(H e_R)=0`. Equivalently `Theta=(beta_u/2)e_R` is invariant with the
stated trace-sign convention. Integrating gives
`e_R(h2)=H(h1)e_R(h1)/H(h2)`. Since
`H=1+(b1/b0)h^2+...`, the locally order-h-four anomalous dimension can
indeed accumulate an order-h-squared finite factor; neglecting it in
individual correlators would be unjustified.

For an autonomous flow, the initial-value derivative J solves
`dJ/dlog(mu)=beta_u'(u)J`. The quotient
`beta_u(u(mu))/beta_u(u_UV)` solves that same equation with initial value
one. Its UV limit is H. This proves the constant-source sensitivity
identity. It does not prove the transport of local sources, irrelevant
operator estimates or the identification with the unchanged `Z(a)=1`
Wilson observable. TSE55 P3/P6 and SRC2_55's drift discussion leave precisely
these issues open; the manuscript does not promote them.

Multilinearity gives `P->F^4P` and `Q->F^2Q`, so a supplied common nonzero
factor cancels from `P/Q^2` exactly. At first order the shifts are
`a4->a4+4z`, `a2->a2+2z`, and their difference remains unchanged.
This argument removes neither general insertion mixing nor finite vertex
contributions. The limitation is stated correctly.

**R4. Running logarithms and scheme changes -- PASS FORMAL.**
Locations: section 3, equations (7)--(9).

For a separated n-point cumulant with leading factor `h^(2n)`, the
relative h-squared part of `(D+n gamma_e) C_n=0` is
`L_n-2n b0=0`: `partial_ell` acts on the explicit logarithm and
`beta_h partial_h` acts on the leading power. The gamma term begins two
relative powers later. Thus `L4=8b0`, `L2=4b0`, and
`L4-2L2=0`. Division gives the undetermined finite coefficient
`c=a4-2a2`. For every finite c the equation admits this first-order form;
the RG equation cannot determine the actual c.

Integrating the one-loop beta function from mu to `1/lambda` gives
`1/h_*^2=1/h^2-2b0 ell`, verifying the sign in (9).
The binomial expansions of `h_*^8` and `h_*^4` reproduce both logarithms.
At fixed reference coupling this truncation is not uniform for large
`h^2|ell|`; the running-coupling qualification is necessary and present.
The homogeneous ratio equation at order h-four gives
`L_R-2b0 c=0`, including its sign.

For `h'=h+alpha h^3+...`, inversion gives `h=h'-alpha h'^3+...`.
The individual coefficients shift by `-8alpha` and `-4alpha`, so c is
unchanged. The fixed conversion instead gives `c_FLOW=2N c_std`.
These facts justify scheme bookkeeping conditional on representing the
same observable; they cannot establish that matching premise.

**R5. Gauge, ghost and insertion vertices -- PASS FORMAL; actual matched
calculation OPEN.** Locations: section 5.1, equations (14)--(17).

Expanding `F_can=f+s h C` in `integral F_can^2/4` gives the cubic
coefficient `s/2` and quartic coefficient `s^2/4`. Expanding
`e/h^2=F_can^2/2` gives insertion coefficients `1/2`, s and `s^2/2`.
Thus the insertion's cubic and quartic terms have not been dropped.
For the displayed adjoint-derivative convention, integration by parts in
`bar c(-partial.D)c` gives the positive coefficient
`s f^{abc}(partial_mu bar c^a)A_mu^b c^c` in V1. The FP determinant
requires Grassmann contractions and their loop signs, as stated; replacing
it by a positive bosonic law would change the calculation.

Expand the normalized generating logarithm about the Gaussian source tilt.
With `A_t=sum t_i X_i1-V1` and `B_t=sum t_i X_i2-V2`, its h-squared
term is `<B_t>_t+kappa_t(A_t,A_t)/2`, minus the zero-source value.
Differentiating distinct labels gives respectively one X2, two X1's,
one X1 with -V1, one -V2, and two V1's. The two orderings cancel the
one-half for distinct X1's and for X1/V1; it remains for V1/V1.
Equation (16) contains all five families with the correct factors and
normalization subtractions. The same derivation with labels {2,3} supplies
the denominator correction. This independently confirms the formal
content of REVIEW_K4MATCH R9.

The counterterm symbols are not specified finite integrals. Neither a full
regulator/subtraction prescription nor its uniform removal has been
supplied, and the finite-lattice Haar and matching contributions have not
been reconstructed. Consequently (17) is a coefficient formula, not a
computation or bound for c. Insertion signs do not fix signs of joint
cumulants. This is the remaining R10/B1 failure of completion.

**R6. Parity scope -- PASS AFTER REPAIR.**

The initial reviewed text used relative `O_form(h^4)` while declining to
assume a complete even expansion. The displayed first two vertices only
prove that the order-h term vanishes. The final section 3 expressly adds
the full simultaneous h/A reversal symmetry, including the regulator,
counterterms and integration prescription. Changing A to -A, with ghosts
fixed, proves evenness of the normalized generating function under that
premise. Without it, the text now uses a possible `O_form(h^3)` remainder.
This resolves the inherited B3 issue without claiming that a formal parity
argument is a uniform error bound. Section 5.1 is consistent with this
distinction.

**R7. FLOW-based reciprocal rate -- PASS CONDITIONAL.**
Locations: section 4, equations (10)--(13).

Applying F-ll with `j=K-m`, `n=K`, and fixed `u_K=U>R_F` bounds
`|u-U-Bm log L|` by
`R_F+C_rho/A_U+(C_rho/b_-)log(1+b_-m/A_U)`.
Adding U gives exactly E_m in (10), uniformly in the named cutoff/volume
parameters under FLOW's hypotheses. E_m is `O(log m)`, so eventually
`E_m<=V/2` with `V=B m log L`.

If `u=V+v` and `|v|<=E_m`, then
`|1/u-1/V|=|v|/[V(V+v)]<=E_m/[V(V-E_m)]<=2E_m/V^2`.
Also `1/u<=2/V`. This proves (11) for both signs, not merely for the
checked rational examples. Since `m log L=log(1/lambda_m)`, (12) follows.
It is the rate for an isolated fixed finite coefficient c. It neither
proves c finite for the actual theory nor controls the remainder.

Under the separate hypothesis (13), `H_R/u^2<=4H_R/V^2` gives exactly
the stated combined error. The prescribed fixed-m cutoff/volume limit
precedes the m limit. A merely relative o(1) remainder is enough for
eventual positivity, but does not imply the sharper full-ratio rate.
The manuscript keeps those quantifiers and distinctions.

**R8. Positivity certificate and comparator -- PASS CONDITIONAL.**
Locations: section 7, equation (19).

On `|delta2|,|delta4|<=1/4`, the ratio factor increases with delta4 and
decreases with delta2. Its extrema are
`(3/4)/(5/4)^2=12/25` and `(5/4)/(3/4)^2=20/9`.
Multiplying the lower bound by `3/(338d)` gives `18/(4225d)`.
The stated thresholds allocate at most `1/16+1/16+1/8=1/4` to the first
correction, remainder and cutoff/volume error. Neither sign of the first
correction is excluded.

The final text correctly uses `a_n^W` after any common matching factor
for this absolute certificate. Cancellation of a factor in R4 does not
allow its contribution to the separate P and Q errors to be ignored.
The constants M2, M4, H2 and H4 are still absent for the original law.

Fixing m_star before taking the common moment-convergent limit, and using
the upper bound `u<=U_+(m_star)` for the absolute lower margins, gives
the stated conditional fixed-scale witness. It excludes a field Gaussian
on e. A free theory with composite e can already have the positive free
fourth cumulant, so unrestricted free-theory exclusion would be false.
The explicit comparator qualification repairs the inherited B2 scope
problem for this note.

**R9. Divergences, finite bounds and nonuniformity -- PASS at stated scope.**
Locations: sections 5.2 and 6.

For `|p|>=2|k|`, the triangle inequality gives
`|p+k|<=3|p|/2`, hence the displayed scalar bubble is at least
`4/(9|p|^4)`. Its four-dimensional radial integral diverges. External
separation therefore cannot justify taking absolute values of unsubtracted
internal graphs. The mean-value theorem bounds a subtracted numerator by
`|z| sup|grad phi|`; polar integration gives
`2 pi^2 delta sup|grad phi|`. The final non-strict rational inequality
is valid also for constant phi. Its earlier strict version failed in that
zero-gradient case and was repaired. This local bound contains no finite
enclosure for D4 or D2.

The proposed conversion from supplied graph bounds to
`|c|<=(2/3)M4+(2/11)M2` is correct using the free denominators. No graph
values are actually supplied. Likewise the scalar example
`F_J(x)=1-2Jx^2/(1+Jx^2)` has zero first coefficient at each fixed J but
tends to -1 at fixed positive x as J grows. It correctly demonstrates
why a finite perturbative coefficient does not establish a uniform
original-law remainder; it is not offered as a YM counterexample.

**R10. Registered evidence and provenance -- PASS within algebraic scope.**

The registration precedes the original checker: preserved filesystem times
are 04:58:09 UTC and 05:05:30 UTC. All ten source digests in
`k4corr_sources.json` match current files. The unchanged criteria hash is
`93d98e599b58de25af139683ea0175e385ef28bdad3d05a80b967b6fd2b58dda`.
The preserved first checker has the hash recorded by attempt 01; the
current checker and runner have the hashes recorded by attempt 02.
Both stored stderr files are empty.

Attempt 01 records 54 passing assertions. Inspection found that criterion
6's denominator implication had only finite rational spot checks. This
was a coverage gap, not a failed assertion or a new scientific criterion.
The author preserved that attempt and added the registered generic
polynomial certificate: for `t=E/V<=1/2`,
`2(1-t)-1=1-2t`; substituting `t=(1-r)/2` leaves the nonnegative r.
Together with the denominator argument in R7, this covers the full
stated domain. Attempt 02 records all 56 assertions passing.

The final receipt records one serial child, no pools, effective nice 20,
all five thread limits one, four exclusive locks, native free memory 52%,
maximum recorded load below 2.198, and peak combined RSS 41,975,808 bytes,
below the registered 800 MiB cap. The runner opens the three existing
locks read-only. Both runs and the correction are disclosed in the final
manuscript and log. These statements report inspected author evidence;
they are not a claim that this reviewer independently reran the checker.
The checker contains no interacting YM integration, and its passing
mutation controls cannot discharge any OPEN dynamical estimate.

**Binding completion requirement.** Supply the actual matched finite
coefficient or a rigorous explicit magnitude enclosure for the complete
renormalized four-source and two-source contributions, with every
load-bearing numerical bound certified. Separately supply enough uniform
original-law error and matching control to make the relative correction
o(1) and reach the stated positivity threshold. A coefficient sign alone
would not do this; a sufficient magnitude and remainder bound would.
Until those results exist, retain the OPEN labels and the completion HOLD.
No further algebraic repair to the reviewed final manuscript is required
to preserve it as conditional research progress.

VERDICT: HOLD
