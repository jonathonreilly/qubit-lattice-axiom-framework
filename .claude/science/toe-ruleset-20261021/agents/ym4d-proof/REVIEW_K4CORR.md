**Independent hostile review of K4CORR.md — 2026-10-30**

**Disposition: HOLD for completion of the author brief.** The formal and
conditional calculations pass. The finite Yang–Mills correction is neither
evaluated nor rigorously bounded, and the actual-law uniform remainder is
missing. The manuscript accurately marks these gaps OPEN. Its algebraic
progress does not complete the requested calculation or non-cancellation
estimate. I found no additional mathematical repair necessary to preserve
the present manuscript as a conditional research result.

This is a fresh, same-family Codex review, independent of authorship, under
the supplied reviewer brief and PROCESS_LIGHT. I re-derived the steps below,
checked the cited source locations and primary literature conventions, and
reran the registered algebra checks without writing their outputs to disk.
The earlier `checks/k4corr_review.md` was inspected afterward for its scope
and provenance, not used to establish the mathematics. This review is the
only file created or edited. No commits or audit-status changes were made.

All manuscript line numbers refer to the 461-line `K4CORR.md`, SHA-256
`e7d63ea8071f8f9c7eeadfb4f7c02ce0efc2435809096f8c30099c2dc094d689`.

| Author item | Verdict and manuscript lines | Fix required for completion |
|---|---|---|
| 1: actual relative first correction in the specified observable, including running logarithms and anomalous scaling | **PARTIAL / OPEN** overall. The normalization at 28–79, conditional anomalous identities at 85–168, and formal logarithms at 172–228 pass. The finite coefficient at 275–343 remains unevaluated. | B1: supply the matched, renormalized finite coefficient or the explicitly permitted rigorous magnitude enclosure. The displayed vertices and the identity `c=a4-2a2` alone do not do this. |
| 2: relative short-distance smallness, exact rate, and relevance of the sign | **PASS CONDITIONAL** for the isolated `c/u` rate, 232–261, and the sign-independent sufficient bound, 398–417. **OPEN** for the actual full ratio, 263–273 and 388–394. | B2: establish a uniform remainder and the original-observable matching needed to apply the conditional estimate. Keep the sharper full-ratio rate conditional on (13). |
| 3: explicit rigorous upper bound when a closed form is unavailable | **HOLD / OPEN**, 338–372. Neither `M4` nor `M2` in the proposed graph-bound conversion is supplied. | B1: enclose the complete finite coefficient, with exact or validated arithmetic for every decisive number. The local subtraction inequality is not such an enclosure. |
| Exact K4MATCH obligation discharged | **PASS as a partial-discharge statement**, 427–435. Only common RG and anomalous-factor bookkeeping in K4MATCH §6.2 / REVIEW_K4MATCH R10 is resolved conditionally. | Retain the explicit failure to discharge REVIEW_K4MATCH B1, C-4MATCH, C-2MATCH and PL-4C until B1–B2 below are established. |

**R1. Observable, coupling units and smooth leading coefficient — PASS.**
Locations: lines 28–79, equations (1)–(3).

The trace expansion gives one plaquette contribution
`a^4 mathcal F_mu,nu^a mathcal F_mu,nu^a/(4N)`. Its four copies in each
ordered clover plane cancel the factor four in the observable definition.
The Wilson action sums unordered planes, giving density
`u mathcal F^2/(8N)=u e/2`. Equating this with `mathcal F^2/(4g_std^2)`
therefore gives `u=2N/g_std^2`. With `mathcal A=g_std A`, the observable
becomes `h^2 F_can^2/2`, exactly CUMUL's free quadratic normalization.
This agrees with TSE55 lines 129–144, CUMUL lines 173–192, and FLOW
lines 573–593. Differentiating the coupling conversion gives
`b0=2N b0_std` and `B=2b0`; no factor of two or of N is missing.

I also checked the free input rather than treating its positivity as an
interacting estimate. Differentiating `1/(4 pi^2 |z|^2)` gives the
two-form covariance `Lambda^2(I-2zz^T/|z|^2)/(pi^2 |z|^4)`.
The two-point quadratic cumulant has two Wick pairings and trace six.
At four quadratic vertices, a connected pairing is one of three cycles,
with sixteen leg assignments per cycle and one colour loop. At the four
centres this gives `96(1/81+1/256+1/20736)=169/108` and the point ratio
`169/(15552d)`. These are checks on the kernel, not replacements for the
smooth coefficients.

CUMUL lines 293–322 bound every edge displacement error by `1/2500`,
the rescaled edge-matrix error by `1/250`, and the four-factor trace error
by `6/60`. Thus A lies between `(169/108)(59/60)=9971/6480` and
`(169/108)(61/60)=10309/6480`. The stated B0 enclosure follows from
`12(2500/2501)^8 <= B0 <= 12(2500/2499)^8`. Unit-integral nonnegative
bumps preserve these support bounds. Dividing positive bounds gives
exactly `3/(338d)<R0<5/(363d)`. CUMUL (C2), (C14)–(C16) are correctly
identified. LGF lines 488–542 supply a free curvature kernel only.

Fix: none. Keep quantum operator matching and the actual-chain beta
coefficient conditional; FLOW lines 4833–4851 still list open UNIV inputs.

**R2. Anomalous dimension and trace-factor convention — PASS CONDITIONAL.**
Locations: lines 85–134, equations (4)–(5).

For `D=mu partial_mu+beta_u partial_u`, differentiating its coefficient
gives `[D,partial_u]=-beta_u' partial_u`. With the expressly assumed
coupling-insertion identity, RG identity and removal of redundant terms,
this yields `D e_R=-beta_u' e_R`. Independently, changing variables in
`beta_u=-2 beta_h/h^3` gives

    d beta_u/du = (-h^3/2) d(-2 beta_h/h^3)/dh
                 = beta_h' - 3 beta_h/h.

For the stated formal beta expansion this is `-2b1 h^4+O(h^6)`.
The scale insertion is invariant because
`D(beta_u e_R)=beta_u beta_u' e_R-beta_u beta_u' e_R=0`.
Differentiating `O_can=2e_R/h^2` instead gives
`gamma_can=gamma_e+2 beta_h/h=-2b0 h^2-4b1 h^4+O(h^6)`.
The distinct canonical and connection normalizations are essential.

The literature locator is correct: Suzuki's equations (2.15), (2.21)
and (4.7) concern the connection-normalized scalar and its trace factor;
his `gamma_S` has the opposite sign to the manuscript's `gamma_e`.
Equation (4.19) also displays the accumulated order-g-squared effect.
His references 26–27 identify Nielsen and Collins–Duncan–Joglekar.
These checks verify attribution and conventions, not a Wilson-law
matching theorem. See [Suzuki, Energy–momentum tensor from the Yang–Mills
gradient flow, sections 2 and 4](https://arxiv.org/html/1304.0533v6).

Fix: none to the conditional identities. The premises at lines 85–91
must remain explicit. No numerical two-loop beta coefficient was imported.

**R3. Integrated factor, source transport and cancellation — PASS CONDITIONAL.**
Locations: lines 138–168, equation (6).

Logarithmic differentiation of `H=-beta_h/(b0 h^3)` gives
`beta_h H'/H=beta_h'-3 beta_h/h=gamma_e`. Consequently `H e_R` is
RG-invariant and `e_R(h2)=H(h1)e_R(h1)/H(h2)`. Its expansion permits an
order-h-squared accumulated factor despite a local order-h-fourth gamma.
For an autonomous flow, differentiating
`integral_(u_UV)^u dv/beta_u(v)=log(mu/mu_UV)` at fixed scale ratio
gives `partial u/partial u_UV=beta_u(u)/beta_u(u_UV)`. The UV limit
is `beta_u(u)/(2b0)=H(h)`.

This constant-source identity does not prove transport of four local
sources. The manuscript says so at lines 157–159. The cited limitations
are present in TSE55 P3, lines 496–502, its P6 addition at 639–643, and
SRC2_55 lines 451–460. No selected-sector estimate is silently promoted.

For a common deterministic factor F, connected cumulants of orders four
and two scale as F^4 and F^2; their ratio is invariant. Deterministic
centring changes only the linear term of the log generating function.
For `F=1+z h^2+...`, the first coefficients therefore shift by `4z` and
`2z`, cancelling in `a4-2a2`. This does not remove a general mixing or
vertex correction, as lines 167–168 correctly warn.

Fix: none. B1–B2 must address the still-open local matching before these
identities are asserted for the original `Z(a)=1` observable.

**R4. Running logarithms, parity and scheme dependence — PASS FORMAL.**
Locations: lines 172–228, equations (7)–(9).

In `(D+n gamma_e) C_n=0`, the leading `h^(2n)` contributes
`-2n b0 h^(2n+2)`, while differentiating the first `ell=log(mu lambda)`
term contributes `L_n h^(2n+2)`. Gamma contributes only at the next
relative order. Hence `L4=8b0`, `L2=4b0`, and the ratio log coefficient
is zero. Integrating `d(h^-2)/d log mu=2b0` gives
`h_*^2=h^2/(1-2b0 h^2 ell)`, confirming the sign and the logarithm
convention. A fixed-mu truncation is not uniform for large `h^2|ell|`.

At the next ratio order, D applied to `1+c h^2+h^4(d_R+L_R ell)`
has coefficient `L_R-2b0 c`, so `L_R=2b0 c`. Substituting
`h=h'-alpha h'^3+...` shows that the first ratio coefficient is
unchanged by a near-identity scheme change. The fixed rescaling instead
gives `c_FLOW=2N c_std`.

The complete reversal symmetry is explicitly assumed at lines 174–181.
It makes the normalized generating function even in h by the A-to-minus-A
change of variables with ghosts fixed. The displayed first vertices alone
would establish only the vanishing first odd term; lines 332–336 retain
that distinction. Thus K4MATCH's inherited all-odd wording problem is
not repeated here. Neither parity nor RG fixes the finite pair `(a4,a2)`.

Fix: none. Retain the formal-error notation and the stated full symmetry
premise; neither provides an analytic bound on the remainder.

**R5. FLOW envelope and rate — PASS CONDITIONAL.**
Locations: lines 232–273, equations (10)–(13).

FLOW F-ll, lines 425–429, bounds
`|u-U-b_*m|` by `R_F+C_rho/A_U+(C_rho/b_-)log(1+b_-m/A_U)`.
Adding U gives exactly E_m in (10). F-tune, lines 433–453, supplies the
conditional fixed terminal coupling and uniform constants. Since
`E_m=O(log m)`, eventually `u>=b_*m-E_m>=b_*m/2`. With `v=b_*m`,

    |1/u-1/v| = |u-v|/(uv)
               <= E_m/[v(v-E_m)] <= 2E_m/v^2.

Multiplication by a fixed finite c and
`b_*m=B log(1/lambda_m)` proves (12), including its log-log envelope.
For nonzero c the scaled limit is c/B; zero c gives no nonzero leading
term. This uses the geometric sequence specified in section 4 and does
not compute c or establish its existence as a matched YM coefficient.

If (13) is additionally assumed, `u^-2<=4/(b_*^2m^2)` gives precisely
`[2|c|E_m+4H_R]/(b_*^2m^2)+eta`. A mere uniform relative o(1) error
would suffice for eventual positivity but would not establish that
sharper full-ratio rate. The manuscript keeps these conclusions separate.

Fix: B2 for the actual-law conclusion; none to the reciprocal argument.
Keep cutoff/volume removal at each fixed m before the short-distance limit.

**R6. Continuum vertices and the five cumulant families — PASS FORMAL;
finite coefficient OPEN.** Locations: lines 275–343, equations (14)–(17).

Expanding `(f+s h C)^2/4` gives the cubic coefficient `s/2` and the
quartic coefficient `s^2/4` in the action. Expanding the normalized
insertion `(f+s h C)^2/2` gives coefficients `1/2`, `s`, and `s^2/2`
in (15). Integration by parts of `bar c(-partial.D)c` gives the stated
ghost vertex. Its contractions must retain Grassmann signs. The unknown
quadratic action and insertion counterterms are not numerical inputs.

For the Gaussian tilted by the leading sources, expand the normalized
logarithm as

    L_h(t)=L_0(t)+h <A_t>_t
       +h^2[<B_t>_t+kappa_t(A_t,A_t)/2]
       -the same corrections at t=0+... .

Distinct-source differentiation produces one X2 insertion, two distinct
X1 insertions, one X1 with -V1, one -V2, and two V1 insertions. The two
orders cancel the factor one-half for distinct X1s and the cross term;
it remains for the repeated V1. This reproduces all five families in
(16), including the signs and connected normalization, for n=2 and n=4.
It also yields `c=D4/A4-2D2/A2`, exactly (17), after the specified limit.

The regulator, subtraction and IR prescriptions and the actual lattice
matching are still unspecified at lines 304–309. The mathematical
identity does not evaluate the integrals, determine their sign, or prove
their uniform limit. This is the substantive missing part of author item 1.

Fix: B1. Insertion signs cannot substitute for the signs or magnitudes of
the integrated connected graph sums.

**R7. Local subtraction estimate and proposed coefficient bound — PASS
at stated scope; author item 3 OPEN.** Locations: lines 345–372.

For `|p|>=2|k|`, the triangle inequality gives `|p+k|<=3|p|/2`, hence
the scalar bubble lower bound `4/(9|p|^4)`. Four-dimensional radial
integration diverges logarithmically. This demonstrates why external
separation alone does not justify absolute estimates of unsubtracted
internal graphs; it is not a theorem forbidding a renormalized calculation.

For (18), the mean-value theorem bounds the subtracted numerator by
`|z| sup|grad phi|`; the four-dimensional radial measure then gives
`2 pi^2 delta sup|grad phi| <=32 delta sup|grad phi|`. The non-strict
last inequality includes constant phi. It is a valid local bound and
contains no certified supremum for the complete graph problem.

If the stated D4 and D2 magnitude bounds were supplied, division by
`A>3/2` and `B0>11` would give
`|c|<=(2/3)M4+(2/11)M2`. Neither number is supplied. The warning that
positive flow time changes the free constants is also correct; its
use would require the separate small-flow-time matching asserted there.

Fix: B1. Do not describe the bubble example, the local subtraction lemma,
or the rational conversion as a coefficient enclosure or a YM obstruction.

**R8. Uniformity, positivity and the comparator — PASS CONDITIONAL.**
Locations: lines 376–425, equation (19).

The example `F_J(x)=1-2Jx^2/(1+Jx^2)` has no term linear in x at each
fixed J but approaches -1 as J increases at fixed positive x. It refutes
the inference from a first coefficient to a uniform remainder; it says
nothing about the actual YM sign. The stated original-law inputs include
terminal integration, mixed conditional cumulants, local matching and
large-field/exterior terms, as CUMUL lines 464–500 require.

On `|delta4|,|delta2|<=1/4`, monotonicity gives
`(3/4)/(5/4)^2=12/25` and `(5/4)/(3/4)^2=20/9`.
Multiplication by the strict lower bound on R0 gives `18/(4225d)`.
The threshold in line 414 makes the two coefficient/remainder terms
at most `1/16` each; adding `eta_n<=1/8` yields `1/4`.
Both coefficient signs are allowed. The distinction between the original
coefficient `a_n^W` and the representative coefficient is correctly made.

Keeping m_star fixed and using `u<=U_+(m_star)` gives a positive absolute
fourth-cumulant margin. It passes along the assumed common moment-convergent
sequence. A nonzero fourth cumulant excludes a field Gaussian on e;
it does not exclude a free field with a quadratic composite e. The explicit
qualification at lines 422–425 agrees with CUMUL lines 337–355 and avoids
the comparator problem identified in REVIEW_K4MATCH B2.

Fix: B2 for the missing actual-law inputs; none to the conditional
threshold or comparator scope. The other reconstruction requirements remain.

**R9. Evidence, source identities and status discipline — PASS within
algebraic scope.** Locations: lines 12–24 and 427–461.

All ten source digests in `checks/k4corr_sources.json` match the current
files. All fifteen artifact digests in `checks/k4corr_verification.json`
match. The criteria precede both preserved checker files by their current
timestamps, and the recorded original checker hash matches the preserved
attempt-01 source. The only checker change is the two generic denominator
certificate assertions. Both saved stderr files are empty; attempt 01
records 54 passing assertions and attempt 02 records 56.

I reran the current registered checker under an external watchdog at
2026-10-30T05:16:05Z. All 56 assertions passed, and their complete records
exactly match the saved final run. All four numerical lock files were
opened read-only and held exclusively. Effective nice was 20, all five
thread settings were 1, native free memory was 52%, all load averages
were below 2.295, and peak combined RSS was 43,532,288 bytes. There was
one serial numerical child, no pools, no new criteria, and no output-file
write. The run took about 0.070 seconds. This reproduces the arithmetic
evidence, not any interacting coefficient or remainder estimate.

The prior same-family review ends HOLD and binds this same manuscript
hash. Its status is represented accurately. The paper's closing discharge
statement agrees with K4MATCH lines 474–534 and REVIEW_K4MATCH R10/B1.
The differences between formal identities, conditional estimates, and
actual-law results are maintained. No GO, NO-GO or retained audit grade
is established or claimed. HOLD records incomplete scientific work, not
an obstruction theorem. Balaban and Dimock retain the author's constructive
RG method credit; neither supplies an estimate closing the missing input.

Fix: retain these scope and provenance distinctions. Passing the checker
or another review cannot supply B1–B2.

**Binding fixes before the requested scientific deliverable is complete.**

1. **B1 — actual finite coefficient or rigorous magnitude bound.** At
   lines 304–343 and 367–369, specify the regulator, gauge/IR and zero-mode
   prescription, finite subtractions and matching to the chosen unflowed
   clover observable. Evaluate or rigorously enclose the full connected
   four-source correction and the denominator correction, or their complete
   renormalized combination. Include the action, ghost and composite
   insertion terms and justify regulator removal. Supply an explicit finite
   bound with exact or interval certification for decisive numerical values.
   Under this author's item-3 alternative, a sufficient magnitude bound
   need not determine the sign; any unevaluated sign claim remains OPEN.
2. **B2 — uniform control on the original law.** At lines 263–273 and
   388–417, establish matching and a uniform error bound sufficient to
   prove actual relative o(1) and reach a positive denominator and cumulant
   margin on the common tuned trajectory. K4MATCH (24) is one sufficient
   formulation; a proved weaker uniform relative o(1) estimate can establish
   positivity but cannot by itself establish the stated sharper full-ratio
   expansion. Account for the complete source normalization, mixed and
   terminal terms, large fields, exterior errors and the common moment limit.

Until B1–B2 are supplied, preserve the OPEN labels and completion HOLD.
No edit that merely renames the existing formal reduction can complete
the finite Yang–Mills calculation or its uniform non-cancellation proof.

VERDICT: HOLD
