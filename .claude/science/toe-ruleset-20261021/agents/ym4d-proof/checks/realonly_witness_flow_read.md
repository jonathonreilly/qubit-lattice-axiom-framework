# REALONLY: witness and coupling-flow consumer inspection

Author-side source inspection and elementary conversion lemmas, 2026-10-30.
This is neither independent review nor a new audit disposition. Balaban and
Dimock are credited for the upstream constructive RG strategy. No literature
lemma or recalled `[m]` assertion carries a proof below.

Source checkout: `71ff1c12a33734f8ae305540916c117f7fceb664`; cached
`origin/main`: `01589af3faf806b736c42dc2f3bd625e9edead9f`. The assignment pins
this checkout. No fetch, source edit, numerical experiment, commit, audit or
ledger operation was performed. Only this deliverable is edited. Line numbers
below refer to the source hashes in section 7, not to a later moving checkout.

## 1. Exact consumers and classification

**REAL-SUFFICES (PROVEN implication)** applies to the finite witness and flow
consumers below when their specified real derivative/moment estimates are
supplied. **OPEN** applies to producing those estimates for the actual full
normalized Yang--Mills construction. A real supremum bound on a source error
cannot simply replace its complex supremum bound and inherit a Cauchy estimate.

| Consumer | Exact quantity consumed | Source and remaining scope |
|---|---|---|
| AF-e witness | On one normalized Wilson trajectory, `c_- u_k^(-kappa') <= lambda^8 Cov(O_g,O_f) <= C_+ u_k^(-kappa)`, with fixed positive exponents, all sufficiently short fixed scales and uniform cutoff/volume constants | WITNESS:447--503, especially E8/E9 at 474--495. E-ALG and E-SEQ remain separate all-order/common-domain inputs. This witness uses real covariances, not a complex source value. |
| PL-1L summed producer | `abs(sum_i(D_i-Lambda_i)) <= C_err u_k^(-2-theta)` | WITNESS:507--547, E10--E12; primary TSE55:421--441. `D_i=lambda^8 E[Cov(G_i,H_i given U_(i+1))]`, with the terminal covariance retained. This is an absolute matching error, not an error divided by possibly zero/signed `Lambda_i`. |
| PL-1L per-level producer | `abs(D_i-Lambda_i) <= A_1 u_(max(i,k))^(-2-theta) p_i(k)`, `p_i=L^(4(k-i))exp(-mu d L^(k-i))` below k and `L^(-8(i-k))` above k | WITNESS:539--547; TSE55:272--301 and 421--429. FLOW-pw sums it. The finite real conditional-covariance identity is proved in TSE55:242--251. |
| K4MATCH numerator | `abs(P-P_run) <= C u^(-4-theta4)`, where `P=lambda^16 kappa4(O_1,O_2,O_3,O_4)` | K4MATCH:42--74 and 292--302. A summed PL-4C suffices; PL-4JET:294--295 is stronger. The per-level increment contains all fourteen terms in (5), plus the terminal cumulant, not only the averaged conditional fourth cumulant. |
| K4MATCH source alternative | For `X_r=u lambda^4 O_r`, `partial_1234(L-L_run)(0)=u^4(P-P_run)` | K4MATCH:308--371. Its complex 4-SRC-ERR is a sufficient route. A controlled real jet through degree four is explicitly allowed at 176--183. Distinct-source multi-index `(1,1,1,1)` has no `4!`. |
| K4MATCH denominator and limiting witness | Pair (2,3) PL-1L; convergence of S4 and all six S2 after centring, or all fifteen nonempty subset moments without centring; positive lower margin for Q | K4MATCH:373--409. The ratio estimate is `(eps4+2 eps2+eps2^2)/(1-eps2)^2`. The polynomial fourth cumulant, rather than a ratio at a possible zero denominator, is the fixed-scale witness. |
| Coupling extractor | `beta[F]=sum_z z1 z2 Pi^F_12(z)`, with `Pi^F` the real Hessian at the identity; gauge/translation/B4 symmetry and sufficient spatial decay | FLOW:20--33 and 146--182. The derivative required is in real background link coordinates. It is not automatically a cumulant of the clover source. |
| Finite-u flow remainder | `rho_k=-beta[sum_X E_k^(>=2)(X)]+delta_beta_k`, `abs(rho_k)<=C_rho g_k^2`, with returned LF shift bounded by `g_k^6` | FLOW:193--232 and 409--416; FLOW55:503--517. Complex Cauchy is used only to obtain the weighted Hessian bound at this consumer step. |
| Flow brackets/tuning | Positive-slope every-increment one-loop bracket, real remainder bound, continuity, correct infinite-volume/finite-volume correspondence, and noncircular per-level applicability | FLOW:418--470. These arguments are real summation and an intermediate-value argument. Tuning does not require monotonicity or differentiability in the bare coupling. |

The witness reference comparison also consumes K-dec and FLOW-pw, with
`u_i>=u_min>0`, and the free LGF curvature estimate. WITNESS:549--584 and
K4MATCH:216--290 prove the stated free scale comparisons and summations
conditionally on those inputs. Their smallness conclusions do not supply the
interacting matching error or a positive YM lower bound.

The six quantum production costs remain explicit in WITNESS:586--595:
source-dependent Gaussian dominance, background covariance control, image
normalization tending to one, coarse covariance matching, summed two-insertion
large-field errors at all levels, and matching the Gaussian running coupling.
TSE55:480--515 labels its proposed P1--P5 production argument ARGUED, not proved.
K4MATCH:536--557 lists the extra fourth-order joint and mixed-conditional costs.

## 2. Real finite jets give exactly the finite witness coefficients

**PROVEN algebraic implication.** For a finite positive law and real variables
`X_1,...,X_q`, suppose the required joint moments exist. For distinct labels B,

    kappa(X_r : r in B)
      = sum_(pi partition of B) (-1)^(|pi|-1)(|pi|-1)!
                               product_(C in pi) E product_(r in C) X_r. (R1)

This follows by expanding `log(1+w)` in the ring with `t_r^2=0`: the coefficient
of `t_B` uses only degrees at most `|B|`, and each unordered partition with p
blocks occurs p! times, which combines with the logarithm's 1/p to `(p-1)!`.
No analytic neighborhood is required for this finite polynomial identity.
It also proves the conditional/outer cumulant recursion by conditioning the
moment polynomial before taking its logarithm. In particular it reproduces
K4MATCH:130--140 and 159--174 without a complex logarithm.

If real differentiation of the MGF is justified near zero, the same expansion
gives `partial_B log E exp(t.X)|_0 = kappa(X_r:r in B)`. With the physical
normalization unchanged and only the source coordinates rescaled by
`X_r=u lambda^4 O_r`, put `R_q=L-L_run`. Then

    partial_12 R_2(0)   = u^2 [V-V_run],
    partial_1234 R_4(0) = u^4 [P-P_run].                    (R2)

Consequently a **real jet matching** bound
`abs(partial_B R_q(0)) <= A_q u^(-theta_q)` implies the required summed error
`A_q u^(-q-theta_q)`, for q=2,4. There is no factorial loss for these distinct
labels. For a repeated multi-index alpha, the Taylor coefficient is instead
`partial^alpha R(0)/alpha!`.

For RG propagation through order four retain all fifteen nonempty subset jets,
including triples. The real nilpotent calculation gives exactly (7), including
the triple/single, pair/pair and pair/single/single terms. Direct control of the
final fourth derivative needs no chosen RG decomposition; a proof using the
decomposition must include all its terms and actual normalizers. A two-point
theorem does not provide these higher jets (K4MATCH:176--187).

The formal order-`g_FLOW^2` coefficient in K4MATCH:413--464 likewise uses only
finite polynomial/cumulant algebra: all five insertion families in (21),
including the half-weighted double cubic insertion, remain necessary. Real
differentiability with a dominated remainder can implement it, but formal
parity does not establish a uniform expansion, its sign, or its size. The
actual matched YM vertices and uniform bound are still OPEN at 474--534.

## 3. Real supremum errors: failure and a sufficient finite-difference repair

### 3.1 Positivity alone does not repair loss of derivative information

**PROVEN counterexample to that inference, not a Yang--Mills claim.** Let
`mu=N(0,n^2 I_q)`, q=2 or 4, `0<epsilon<1/2`, and define the positive probability
law

    dnu = [1+epsilon product_r sin(X_r/n)] dmu.

The multiplier is positive and integrates to one, by independence and oddness.
Tilting mu by a real t translates its mean to `n^2 t` without changing its
covariance. Integrating the Gaussian sine (or completing the square and its
elementary Fourier Gaussian integral) gives

    M_nu(t)/M_mu(t) = 1+epsilon exp(-q/2) product_r sin(n t_r),
    H(t)=log M_nu(t)-log M_mu(t).

For completeness, if Z is a unit normal, integration by parts gives
`J'(s)=-sJ(s)` for `J(s)=E cos(sZ)`, with `J(0)=1`; hence
`E sin(m+Z)=sin(m) exp(-1/2)`. Applying this independently to each tilted
coordinate proves the displayed ratio using real integrals.

Thus on every real cube `abs(H)<=2 epsilon exp(-q/2)`, H vanishes whenever a
coordinate is zero, but

    partial_1...partial_q H(0)=epsilon exp(-q/2) n^q.       (R3)

Take `n=epsilon^(-1)`. The real log error tends to zero and the matching
derivative grows as `epsilon^(1-q)`. Both MGFs are positive on all real
sources and their individual logarithms are convex. This example has **no
uniform exponential moment or higher-derivative bound**. That missing bound
is exactly what the next sufficient repair adds.

### 3.2 A quantitative real finite-difference lemma

**PROVEN.** Let F be C^(q+1) on the real cube `[0,r]^q`, B all q labels, and
assume `abs(partial_j partial_B F)<=M` there for every j. Define

    Pi_B F(t)=sum_(J subset B) (-1)^(q-|J|) F(t_J).

Repeated one-variable fundamental theorems of calculus give

    Pi_B F(h,...,h)/h^q
      = h^(-q) integral_[0,h]^q partial_B F(s) ds.

The difference from `partial_B F(0)` is at most `q M h/2`, because changing
coordinate j from zero to s_j costs at most M s_j and the cube average of
s_j is h/2. Hence for `0<h<=r`:

    abs(partial_B F(0)) <= epsilon h^(-q)+q M h/2,          (R4a)

if `sup abs(Pi_B F)<=epsilon`. If only the **unprojected** estimate
`sup abs(F)<=epsilon` is given, the correct bound is instead

    abs(partial_B F(0)) <= 2^q epsilon h^(-q)+q M h/2.      (R4b)

The factor is one in (R4a) precisely because the projected error is itself
the alternating sum; equivalently it vanishes on every proper coordinate
face. This is the norm in K4MATCH (15). Neither formula is Cauchy's estimate.
For `epsilon/M` small enough, choosing `h=(epsilon/M)^(1/(q+1))` in (R4a)
gives

    abs(partial_B F(0))
       <= (1+q/2) M^(q/(q+1)) epsilon^(1/(q+1)).           (R5)

If epsilon=0, (R4a) and h tending to zero give a zero derivative. If M=0,
(R4a) instead gives `abs(partial_B F(0))<=epsilon/r^q`; formula (R5) is not
asserted in that case. A uniform Hölder modulus
`abs(partial_B F(s)-partial_B F(0))<=M ||s||_infinity^alpha` similarly gives
`epsilon h^(-q)+M h^alpha`; choosing `h=(epsilon/M)^(1/(q+alpha))` yields
`2 M^(q/(q+alpha)) epsilon^(alpha/(q+alpha))`.

Apply (R4)--(R5) to `F=L-L_run`. A projected real error `O(u^-theta)` plus a
uniform fifth real derivative bound gives `P-P_run=O(u^(-4-theta/5))`.
For the pair it gives `V-V_run=O(u^(-2-theta/3))` with a uniform third
derivative bound. Both have a strictly positive relative exponent, so they
suffice for the conditional witness assembly. They do **not** retain the
original exponent theta; direct real jet matching or proportional derivative
control would be needed for that. Uniformity includes cutoff, volume, matched
scale and every sector used by the chosen producer. A fifth-derivative
constant growing without control does not close this argument.

## 4. Positive real MGFs can supply the finite smoothness and moment limits

**PROVEN sufficient implication.** For q real variables suppose

    E exp(r sigma.X) <= B  for all sigma in {-1,1}^q,       (R6)

with fixed r>0 and B independent of the regulator. Then
`E exp(r sum|X_j|)<=D:=2^q B`, by choosing the sign of each X_j pointwise
and bounding the maximum by the sum. Holder gives `M(t)<=B` on `[-r,r]^q`;
Cauchy--Schwarz applied to `exp(t.X/2)` and `exp(-t.X/2)` gives
`M(t) M(-t)>=1`, hence `M(t)>=B^-1` there.

For `||t||_infinity<=r/2`, a multi-index a of degree n satisfies

    E[abs(X^a) exp(t.X)] <= D a! (2/r)^n,                 (R7)

by the scalar inequality `y^m<=m! (2/r)^m exp(ry/2)` in each coordinate.
An analogous bound on the larger cube of radius 3r/4 (replace 2/r by 4/r)
dominates the difference quotients, so real dominated convergence justifies every fixed finite
derivative. Under the tilted positive law the absolute moment of any ordered
list of n variables is at most `C_n:=BD n! (2/r)^n`. Its logarithmic derivative
is the cumulant (R1), and is therefore bounded explicitly by

    sum_(pi partition of {1,...,n}) (|pi|-1)! product_(C in pi) C_|C|. (R8)

For fixed q, the n=q+1 bound supplies the M in section 3 for a difference of
two logarithms, if both laws satisfy (R6). This proof uses real differentiation
and positive measures, not a complex zero-free assumption.

The same exponential envelope gives uniform integrability of every fixed
polynomial moment: for `S=sum|X_j|`,
`E[S^n 1_(S>A)] <= D sup_(s>A) s^n exp(-rs) -> 0`. Thus weak convergence of
these finite-dimensional laws implies convergence of their fixed joint
moments by truncation. An appropriate moment bound of degree `4+eta`, eta>0,
would already suffice for the fourth-order witness, without an MGF. Mere
bounded fourth moments do not by themselves imply fourth-moment convergence.

**Scope caution.** A uniform full positive MGF bound is an additional input;
it does not follow from existence of a radius or from a bound on the projected
log difference. K4MATCH:326--349 proves a free radius and explicitly says its
complete trace need not be cutoff-uniform. Subtracting proper-subset contact
counterterms from a log can preserve the desired mixed coefficient without
leaving the logarithm of a positive probability MGF. The separated continuum
hierarchy also does not automatically supply ordinary coincident moments.
Consequently (R6) is a sufficient alternative, not an asserted property of the
YM fields or of all the contact-subtracted source functions.

For a real linear tilt of a nonzero positive finite measure,
`Z(t)=Z(0)E exp(t.O)>0` whenever finite. This removes real zeros for the actual
normalized law; it does not give a uniform inverse for an arbitrarily
unnormalized partition function, nor positivity for a signed/complex
activity, reference subtraction, or empty selected sector. Real positivity
also does not imply the coefficient matching or the relative error rate.

## 5. Real replacements at the coupling-flow interface

### 5.1 Weighted real Hessians replace the Cauchy step

**PROVEN conditional replacement of FLOW Lemma F-Pi(ii).** Keep its polymer
geometry, translation covariance and summed gauge/B4 invariance, but assume
only C^2 at the identity and the direct real bound

    abs(partial_(b,a) partial_(b',a) E_k(X;0))
       <= A_2 g_k^2 exp(-kappa_p d(X))                    (R9)

for every pair of links in X, with uniform A_2 and `kappa_p>log 6400`.
Assume the sums represent the actual effective action, including the needed
twice-differentiation/summation interchange. For `b0=(0,e1), bz=(z,e2)`,

    sum_z |z1 z2| |Pi_12(z)| <= C_real A_2 g_k^2,
    C_real=64 M^6 sum_(n>=1) n^3(6400 exp(-kappa_p))^(n-1). (R10)

Proof: a fixed link lies in at most 16 M-cubes; at most `6400^(n-1)` connected
n-cube polymers contain a chosen cube; each has at most `4M^4 n` candidate
second links and `|z1 z2|<=(Mn)^2`; finally `d(X)>=n-1`. Summing these
nonnegative bounds proves (R10) and absolute convergence. The same counting
gives exponential spatial decay with a smaller exponent. This is exactly
FLOW:167--171 with the Cauchy output supplied directly. To match FLOW's
constant verbatim, use `A_2=alpha^-2 E_2`.

With the real C^2 symmetry/transport hypotheses of F-ren retained
(FLOW:285--308), constants have beta zero, earlier renormalized terms have
beta zero, and the actual LF piece has `beta=-delta_beta_k`. Thus

    |rho_k| <= C_real A_2 g_k^2 + g_k^6
             <= (C_real A_2+1)g_k^2,   g_k<=1.             (R11)

This feeds the real arithmetic of F-flow and the continuity-based F-tune.
Uniform real **values** of E_k(X) of size `O(g_k^2)` do not imply (R9).
Finite differences with an unrelated uniform third-derivative bound could
lose the rate to `O(g_k^(2/3))`; that weaker vanishing remainder can still
support suitably changed positive-slope brackets if the spatially weighted
sum remains uniform, but is not FLOW's stated
`O(g_k^2)` remainder or logarithmic refinement.

### 5.2 Producing a background Hessian by real differentiation is conditional

For a fixed-domain positive integral `Z(B)=integral exp(-A(B,x)) dmu(x)`, with
dominated real differentiability through order two, direct quotient
differentiation gives

    partial_ab[-log Z]
       = E_B[partial_ab A]-Cov_B(partial_a A,partial_b A).  (R12)

For example, common integrable envelopes for the first two density
derivatives justify the step. Every measure/Jacobian, normalized-kernel
factor and background-dependent term must be included. Moving hard cut
boundaries require their own differentiation justification. Neither a real
action lower bound nor positivity supplies the uniform spatially weighted
connected estimate in (R9)/(R10). The background derivatives here are not
interchangeable with clover-source derivatives in section 2.

### 5.3 Finite transport jets and the one-loop provider

FLOW55:219--229's Ward identities through order four can be obtained by a
finite real C^4 Taylor expansion of the gauge identity; they do not intrinsically
need a source polydisc. Its small-real-background order-five remainder can
instead be supplied by a real C^5 bound. In the sup coordinate norm, if

    ||D^5 E(X;B)||_op <= 5! A alpha^-5 exp(-kappa_p d(X))

on every segment from 0 to the relevant B, the real integral Taylor formula

    E(B)-sum_(j=0)^4 D^j E(0)[B^j]/j!
      = (1/4!) integral_0^1 (1-s)^4 D^5E(sB)[B^5] ds

bounds the remainder by `A exp(-kappa_p d(X))(||B||/alpha)^5`. The operator
norm is required: a bound on one coordinate derivative does not silently
bound arbitrary directions with a support-independent constant. This
replacement addresses only the cited Taylor step, not a proof of contraction
or a full real RG induction. The jet locality and classification hypotheses
of FLOW55:233--262 remain inputs.

Do not resurrect older OPEN one-loop clauses wholesale. AUDIT:63,73,300
records their scoped supersession. The current provider's exact statement is
UNIFORM_ONE_LOOP_COUPLING_ASTRA:76--86:

    B_n-B_j=beta0(n-j)log L+a_n-a_j,
    |a_n-a_0|<=C_FP,   |B_n-B_j-beta0(n-j)log L|<=2C_FP.

Its section 8 (593--673) gives the every-increment consequence for the
supplied normalized fixed-kappa model, with its linear/jet/residual contracts.
It is a volume-first Gaussian coefficient theorem, not a finite-u or finite-T
bound. Those contracts include spatial locality/complex momentum-strip tools;
the present source inspection does not remove or freshly recertify them.
Complex momentum locality is distinct from complex external-source log
control. Finite-u SF-g, LF return, continuity and volume matching remain
explicit at 668--673 and in FLOW's FI-1 qualification at 459--470.

## 6. Net effect for the lead

The finite witnesses and beta extraction have mathematically sufficient
real-only contracts: exact normalized moments/real jets, matched free
reference, uniform derivative errors with spatial/scale weights, and actual
moment convergence. They impose no intrinsic complex zero-free requirement
on the original positive real tilt. The direct consumer implications are
proved above; no actual YM producer is promoted.

This does not establish that the existing complex-domain RG induction can
be replaced by restricting its sup norms to the real locus. AUDIT:15,55,
57,69,83--85,98 and 188--194 keep the full return, coupled finite-u flow and
actual source/witness estimates open. A real RG replacement must propagate
the norms that genuinely control these derivatives, retain full histories,
complements, denominators and terminal integration, and retain continuity and
finite-volume compatibility. A smaller list of target derivatives alone is
not a construction of that replacement.

## 7. Source identities and read coverage

Paths in the first table are relative to the worktree; paths in the second
are relative to the `ym4d-proof` folder. Hashes identify bytes, not scientific
validation. Relevant argument ranges were read in full; searches over larger
files were only navigation and are not counted as verification of omitted
arguments.

Final deterministic recheck: all thirteen source hashes below agree with the
current files, and HEAD remains the pinned revision. This establishes source
identity only. The new conversion arguments have author checking here and
still require the lane's independent review before substantive acceptance.

| Instruction source | SHA-256 |
|---|---|
| AGENTS.md | `febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0` |
| docs/ai_methodology/SCIENCE_WORKFLOW.md | `71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3` |
| docs/ai_methodology/skills/workhorse/SKILL.md | `a7fcd7d43649e23bf19672e1cce6b4dda175361799765ac792f1c431d54408a2` |
| docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md | `b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0` |

| Source | Read scope | SHA-256 |
|---|---|---|
| PROCESS_LIGHT.md | Complete | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| briefs_q/REALONLY/AUTHOR.md | Complete | `b19b45d85f31015e0ee1dd9747af9035bccc706bb3647a99c13ecd42089930d2` |
| WITNESS.md | 1--220 and 350--659; source consumers are 390--631 | `f545b2b544234e9e2a133fb0957bee18cf2c290912897d5a5028ccadc484ecb8` |
| K4MATCH.md | Complete | `2f795c75609075e6d48096abf5ba8572a80f6271a554889f7212c4be75827604` |
| AUDIT.md | 1--195 and 287--308; inventory 196--286 is not a fresh underlying-proof review | `765abb796087032d950e0db436952c61bd08b100648fa55f2cedbe31a66c619e` |
| TSE55.md | 242--310 and 346--530 | `a894d1b2439a7b83311175c9e6e30f6fb52cc015a74c6be7e839be8192a7869a` |
| FLOW.md | 1--91, 113--237, 285--309, 392--487 | `085cd225228a23847b053650fe8bff4c14529d7e630a74565b301d39855e442f` |
| FLOW55.md | 166--286, 301--332, 503--520 | `56d2707f4b571585db26cf2a077dbaee57bc936c76821cdbc50710e4b36e9d25` |
| UNIFORM_ONE_LOOP_COUPLING_ASTRA.md | 1--86 and 593--674; named provider retained at its explicit scope, not freshly recertified | `b7baa6a711969c8fc96538009bb8f9f9acdde3f14f6d2f570a6ca5b9391516ce` |
