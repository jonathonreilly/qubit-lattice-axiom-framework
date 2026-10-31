# K4CORR — the relative first correction to the separated fourth cumulant

**Disposition: partial result; the actual Yang--Mills coefficient and a
uniform non-cancellation bound remain OPEN.** The common scale logarithm
in the normalized ratio is zero at relative order `g_FLOW^2`. The
coupling-conjugate action density has a local anomalous dimension starting
at order `g_FLOW^4`, and its integrated multiplicative factor cancels from
the ratio. These statements are **PROVEN formal/conditional** below, not
an evaluation of the remaining finite four-point graphs. In particular,
**no explicit upper bound for the full interacting correction is supplied**.

This author result follows [PROCESS_LIGHT](PROCESS_LIGHT.md). Balaban and
Dimock are credited for the constructive RG method. None of their estimates
is imported to close a hypothesis below. The [log](K4CORR_LOG.md) records
sources, numerical registration, resource controls and independent review.

| Requested item | Result | Status |
|---|---|---|
| Actual relative first correction for the CUMUL tests | `c = a4 - 2 a2`; concrete continuum vertices are specified in section 5, but their renormalized integrals are unevaluated | **OPEN** |
| Common running-coupling logarithms | Numerator coefficient `8 b0`, covariance coefficient `4 b0`, ratio coefficient zero, with `log(mu lambda)` as logarithm | **PROVEN formal**, given the renormalized RG equation |
| Anomalous action-density scaling | `gamma_e = beta_h' - 3 beta_h/h`; local order-h-squared term zero; common integrated factor cancels exactly | **PROVEN conditional**; identification with the original Wilson observable **OPEN** |
| Short-distance rate of the isolated first correction | `c/[2 b0 log(1/lambda)] + O(log log(1/lambda)/log(1/lambda)^2)` in fixed reference units | **PROVEN conditional** on finite c and FLOW's stated hypotheses |
| Actual full-law relative o(1), coefficient sign, explicit magnitude and uniform remainder | No certified finite graph enclosure or original-law remainder obtained | **OPEN** |
| Is the sign needed for eventual positivity? | No: a uniform magnitude/remainder bound suffices, with the exact margins in section 7 | **PROVEN conditional** |

## 1. Observable and coupling conventions

**PROVEN specification.** Keep the original clover density and its centring,

    e_a(x) = (4 a^4)^-1 sum_(mu != nu) sum_(p in clover_mu,nu(x))
                             [1 - Re tr(U_p)/N],       Z(a)=1.

Set `h=g_FLOW`, `g=g_std=sqrt(2N) h`, `u=h^-2=2N/g^2` and
`d=N^2-1`, with N fixed and at least two. Use exactly CUMUL (C2): the four
unit-integral product bumps with coordinate half-width `1/10000`, centred
at `((2i-5)/2,0,0,0)`, and `f_(i,lambda)=lambda^-4 f_i(x/lambda)`.
The choice here is the **unflowed separated** option in the brief.
Distinct supports remain separated after clover thickening as `a/lambda->0`.

With `O_i=O_a(f_(i,lambda))`, retain

    P=lambda^16 kappa4(O_1,O_2,O_3,O_4),
    Q=lambda^8 Cov(O_2,O_3),                 R4=P/Q^2,
    A4=d A/pi^8,   A2=d B0/pi^4,             R0=A4/A2^2,
    3/2<A<5/3,    11<B0<13,
    3/(338d)<R0<5/(363d).                                  (1)

These are the *smeared* constants in CUMUL (C14)--(C16). The point value
`169/(15552d)` is not substituted for R0. LGF controls the free kernel;
it supplies no interacting correction.

For the continuum convention check, let `mathcal F` be the curvature of
the connection appearing in `U=exp(i a mathcal A^a T^a)`, with
`tr(T^a T^b)=delta_ab/2`. A smooth plaquette gives
`s(U_p)=a^4 (mathcal F_mu,nu^a)^2/(4N)+o(a^4)`.
Counting its four clover copies in each ordered plane gives

    e = (mathcal F_mu,nu^a)^2/(4N),
    L = u e/2 = (mathcal F_mu,nu^a)^2/(4g^2).              (2)

Here and below repeated ordered mu,nu are summed. On writing
`mathcal A=g A`, this becomes `e=(h^2/2)(F_can)^2`.
Equation (2) fixes the classical and leading perturbative convention;
it is not a proof of quantum lattice-to-continuum operator matching.

Use distinct notation for the continuous beta function and the FLOW
per-step slope:

    beta_h := d h/d log mu = -b0 h^3 - b1 h^5 + ...,
    b0 = 2N b0_std = 11 N^2/(24 pi^2),
    beta_u := d u/d log mu = -2 beta_h/h^3
                              = 2b0 + 2b1/u + ...,
    B := 2b0 = 11 N^2/(12 pi^2).                          (3)

FLOW section 15 proves the units conversion; its UNIV hypotheses for the
actual soft chain remain conditional, as FLOW section 110 reiterates.
`b1` is symbolic throughout this proof. FLOW F-ll gives a logarithmic
remainder envelope; it does **not** compute this exact two-loop number.
No numerical b1 from literature is used as a premise.

## 2. A local library for the action-density anomalous factor

### 2.1 Explicit premises and derivation — PROVEN conditional

Consider a renormalized, one-coupling, massless action-density sector.
Assume a differentiable beta function, the coupling-insertion identity
`e_R=2 partial L_R/partial u` in the physical separated sector, and the
scale Ward identity for that same action. Identity mixing is removed by
centring. Equation-of-motion and BRST-exact terms must vanish on these
physical separated insertions. Existence of those identities, including
their matching to the Wilson law, is an input, not proved here.

The coupling-insertion commutator is elementary. For
`D=mu partial_mu+beta_u partial_u`,

    [D,partial_u] = -beta_u'(u) partial_u.

Differentiate the RG identity for the action. Modulo the stated redundant
terms, it gives `D e_R=-beta_u' e_R`. Define the sign convention by
`D e_R=-gamma_e e_R`. Changing variables using `u=h^-2` gives

    gamma_e = d beta_u/du = beta_h'(h)-3 beta_h(h)/h
            = -2 b1 h^4 + O(h^6).                       (4)

Equivalently the scale insertion, with the Euclidean sign convention
used here, is

    Theta = (beta_u/2) e_R = -beta_h/h^3 e_R.

Since `D beta_u=beta_u beta_u'`, its derivative vanishes using (4).
This rebuilds the needed Ward-factor algebra rather than importing a
trace-anomaly theorem as an unconditional lattice result. An overall
opposite convention for Theta does not change (4) or the ratio.

For comparison define the canonically normalized scalar
`O_can=2e_R/h^2`. Differentiating this definition gives

    gamma_can = gamma_e + 2 beta_h/h
              = beta_h' - beta_h/h
              = -2 b0 h^2 -4 b1 h^4 + O(h^6).            (5)

Thus using the familiar canonical-F-squared anomalous term for the
unrescaled clover density would introduce an erroneous order-h-squared
term. This conclusion uses the coupling-conjugate normalization in the
premise. Under a finite change `e_R -> F(h)e_R`, its gamma changes to
`gamma_e-beta_h F'/F`; the ratio below is still invariant.

The convention/method attribution is Hiroshi Suzuki,
[*Energy--momentum tensor from the Yang--Mills gradient flow*, sections 2
and 4](https://arxiv.org/html/1304.0533v6), following the trace-Ward work of
Collins--Duncan--Joglekar and Nielsen. Suzuki's gamma_S is the anomalous
factor of the operator (or the opposite convention to gamma_e above).
The differential identities needed here have been derived explicitly;
that reference supplies no Wilson matching or four-point bound.

### 2.2 Integrated scaling and the unchanged Z(a)=1 target

**PROVEN conditional.** Normalize the invariant factor to one at h=0:

    H(h) = -beta_h(h)/(b0 h^3)
         = 1 + (b1/b0)h^2 + O(h^4),
    beta_h H' = gamma_e H,
    E_inv = H(h)e_R,                       D E_inv=0.     (6)

Along a characteristic between h_1 and h_2,
`e_R(h_2)=H(h_1)e_R(h_1)/H(h_2)`. In particular a locally order-h^4
anomalous dimension can accumulate an order-h^2 finite factor over a
UV-to-matched-scale evolution. It is incorrect to discard that accumulated
term just because (4) has no h^2 term.

If the clover source converges to the unit-normalized UV coupling
insertion, the invariant representative at the matched scale is (6).
Equivalently, for an autonomous differentiable flow,
`partial u(mu)/partial u_UV=beta_u(u(mu))/beta_u(u_UV)`;
differentiate the separated-variables flow integral to prove this identity.
As `u_UV->infinity`, this derivative tends to H(h). Actual local source
transport and irrelevant-operator control are still required to apply this
constant-source argument to the four local insertions. **That matching is
OPEN**, consistently with TSE55 P3/P6 and SRC2_55's source-drift caveat.
No new normalization is applied to the requested lattice observable.

For any supplied common nonzero factor F, multilinearity of connected
cumulants gives `P->F^4 P`, `Q->F^2 Q`. Hence R4 is unchanged exactly.
For `F=1+z h^2+O(h^4)`, the relative coefficients shift by
`a4->a4+4z`, `a2->a2+2z`. The net anomalous-factor contribution to
`a4-2a2` is **zero**. This cancels (6), any common finite matching factor,
and deterministic centring; it does not cancel general vertex graphs or
nonmultiplicative operator mixing.

## 3. The running logarithms that can actually be determined

**PROVEN formal**, under section 2's separated RG assumptions. Write
`ell=log(mu lambda)` and let the shape be the fixed CUMUL tuple. At fixed
ell, the even-power notation below additionally assumes the full formal
symmetry `S(-h,-A,bar c,c)=S(h,A,bar c,c)` and
`X_i(-h,-A)=X_i(h,A)`, with regulator, integration prescription and
counterterms preserving it. Change variables A to -A in the normalized
generating functional to prove its evenness. This is a separate premise
on the complete expansion, not a consequence of just its first two
vertices. Without that premise, replace the relative `O_form(h^4)` below
by `O_form(h^3)`; the displayed h^2 coefficient is unchanged.
Use the formal expansions for the action-density representative

    P_R = A4 h^8 [1+h^2(a4+ell L4)+O_form(h^4)],
    Q_R = A2 h^4 [1+h^2(a2+ell L2)+O_form(h^4)].          (7)

`O_form` denotes omitted formal powers, not a uniform asymptotic error.
The separated n-point RG equation is `(D+n gamma_e) C_n=0`.
Using (4), the relative h^2 part is
`L_n-2n b0=0`: the derivative of `h^(2n)` contributes `-2n b0`,
the derivative of ell contributes L_n, and gamma_e starts one order later.
Consequently

    L4=8b0=4B,            L2=4b0=2B,
    R4/R0 = 1+h^2 c+O_form(h^4),    c=a4-2a2,
    L4-2L2=0.                                            (8)

These coefficients use `log(mu lambda)`, not `log(mu^2 lambda^2)`;
the latter convention halves their displayed values. At `mu=1/lambda`
there is no common large logarithm. At a fixed reference mu, a first-order
truncation is not uniform when `h^2 |ell|` is order one; use the running
coupling instead. Indeed the one-loop characteristic gives

    h_*^2 := h(1/lambda)^2 = h(mu)^2/[1-2b0 h(mu)^2 ell]. (9)

Expanding `h_*^8` and `h_*^4` reproduces both signs in (7).
Their common running factor cancels exactly in the ratio.

This does **not** set c to zero. Logarithms of dimensionless distances,
cross ratios, and the fixed bump width can occur in a4 and a2. They are
finite shape data if the renormalized graph integrals exist, and they
remain to be evaluated. Neither the beta function nor scale covariance
determines them: the RG equation through this order permits every finite
pair (a4,a2), hence every c. This is a statement about what these equations
determine, not a no-go statement for a Yang--Mills calculation.

As an additional consistency check, if the next ratio term is written
`h^4[d_R+L_R ell]`, its homogeneous RG equation forces
`L_R=2b0 c`. Thus absence of a scale logarithm in the first coefficient
does not mean absence of running dependence at subsequent orders.

Under a near-identity scheme change `h'=h+alpha h^3+O(h^5)`, the first
ratio coefficient c is unchanged. For numerator and covariance separately
there are compensating shifts from their leading powers. This permits a
continuum scheme to compute c *if* it represents the same scalar operator
up to common finite factors and controlled irrelevant terms. The fixed
conversion from standard to FLOW units remains essential:
`c_FLOW=2N c_std`. Scheme invariance does not prove that matching premise.

## 4. An explicit rate from the supplied FLOW envelope

**PROVEN conditional.** This rate does not require an imported b1 value.
Take `lambda_m=L^-m`, `u=u_(K-m)`, `U=u_K` fixed, and use exactly
FLOW F-ll/F-tune with `U>R_F`. Let

    b_* = B log L,       b_- = beta_- log L > 0,
    A_U=U-R_F>0,
    E_m=U+R_F+C_rho/A_U
              +(C_rho/b_-) log(1+b_- m/A_U).             (10)

F-ll implies `|u-b_* m|<=E_m`. The finitely many small m can be
discarded; since `E_m=O(log m)`, eventually `E_m<=b_* m/2`.
Taking a reciprocal and retaining the denominator gives the explicit bound

    |1/u - 1/(b_* m)| <= 2E_m/(b_*^2 m^2),
    |c/u| <= 2|c|/(b_* m).                              (11)

The proof is simply
`|u-v|/(uv)<=E_m/[v(v-E_m)]<=2E_m/v^2`, with `v=b_*m`.
All constants in (10) remain the conditional FLOW constants, not numbers
claimed to have been enclosed for the actual trajectory.

For a fixed finite coefficient c, the isolated first correction therefore is

    c h_*^2 = c/[B log(1/lambda_m)]
             +O(log log(1/lambda_m)/log(1/lambda_m)^2).   (12)

The reference physical length is one as in FLOW; replacing it by another
fixed reference changes only the subleading constant. If c is nonzero,
`log(1/lambda_m) c h_*^2 -> c/B`. If c is zero this isolated term
vanishes; no nonzero leading asymptotic is asserted.

If, **in addition**, the actual ratio has a uniform error

    |R4/R0 -1-c/u| <= H_R/u^2 + eta_(K,R)(m),             (13)

then the error after subtracting the leading term in (12) is at most
`[2|c|E_m+4H_R]/(b_*^2 m^2)+eta_(K,R)(m)`. First send cutoff and
volume to their common limit at each fixed m, making eta vanish, and
only then take m large. With a merely uniform relative o(1) remainder,
eventual positivity still follows, but the sharper rate for the **full**
ratio does not follow. Neither (13) nor its weaker o(1) counterpart has
been proved for the original law here.

## 5. Concrete vertices for the remaining finite coefficient

### 5.1 Continuum reduction — PROVEN formal; evaluation OPEN

This section specifies more than the symbolic V1/V2 in K4MATCH, but is
still an unevaluated perturbative reduction. Set lambda=1 by scaling,
work in a regulated Euclidean Feynman gauge, and let `s=sqrt(2N)`. Write

    f_mu,nu^a = partial_mu A_nu^a - partial_nu A_mu^a,
    C_mu,nu^a = f^{abc} A_mu^b A_nu^c,
    F_can = f + s h C,
    S0 = (1/4) integral f^2 + (1/2) integral (partial.A)^2
                                      + integral bar c (-partial^2)c,
    V1 = (s/2) integral f C
                       +s integral f^{abc}(partial_mu bar c^a)A_mu^b c^c,
    V2 = (s^2/4) integral C^2 + S_ct,2.                  (14)

The ghost sign follows by integrating `bar c (-partial.D)c` by parts,
with `D c=partial c+s h [A,c]`. Wick expectations for ghosts mean
Grassmann Gaussian contractions, with their closed-loop signs; they
cannot be replaced by a positive scalar Gaussian.
For `X_i=h^-2 O_i` the insertion vertices are

    X_i0=(1/2) integral f_i f^2,
    X_i1=s integral f_i f C,
    X_i2=(s^2/2) integral f_i C^2 + X_ct,i,2.             (15)

These follow by expanding the actual continuum action and the clover's
leading density (2), rather than discarding its cubic/quartic terms.
`S_ct,2` includes the regulator's quadratic counterterms and `X_ct,i,2`
its insertion matching. A complete regulator, IR/zero-mode prescription,
subtraction scheme and their removal must be specified before (14)--(15)
are numerical integrals. The original finite-lattice expansion additionally
has Haar, plaquette discretization and matching terms; (14) is not a
claim to have derived their uniform continuum limit.

For a label set I of size n=2 or 4, put

    D_n = sum_(r in I) kappa0(X_r2, X_s0 : s!=r)
        + sum_(r<s in I) kappa0(X_r1,X_s1, X_t0 : t!=r,s)
        - sum_(r in I) kappa0(X_r1,X_s0 : s!=r,V1)
        - kappa0(X_r0 : r in I,V2)
        +(1/2) kappa0(X_r0 : r in I,V1,V1).              (16)

For D2 use I={2,3}; for D4 use all four labels. Every term is one joint
Gaussian/Grassmann cumulant. To derive (16), tilt the Gaussian by
`exp(sum t_i X_i0)`, put `A_t=sum t_i X_i1-V1`,
`B_t=sum t_i X_i2-V2`, and expand the normalized logarithm through h^2.
Its correction is `<B_t>_t+kappa_t(A_t,A_t)/2` minus its value at zero.
Differentiate the distinct sources. This gives all five terms and the
remaining factor one-half. It proves a formal coefficient, not convergence.

After the prescribed renormalized limit at ell=0, the desired quantities
would be `a4=D4/A4`, `a2=D2/A2`, and

    c = (pi^8/(d A)) D4 - (2 pi^4/(d B0)) D2.            (17)

The first odd term vanishes by reversing A with the ghosts fixed in this
expansion. No assertion about *all* odd orders is inferred from the
displayed through-order-two vertices; section 3 states the needed complete
symmetry separately. A higher-order remainder also needs its own
analytic/asymptotic bound, as REVIEW_K4MATCH B3 emphasizes.

### 5.2 Why no rigorous enclosure is claimed

**OPEN.** No sum of the renormalized integrals (16), with explicit finite
subtractions and uniform removal of both regulators, was evaluated or
enclosed. Consequently (17) is neither a closed evaluated answer nor an
explicit magnitude bound meeting brief item 3. No sign is assigned to it.

Separated external supports remove external coincidence counterterms,
but do not remove internal UV subgraphs. For example the scalar bubble
integrand `1/[p^2(p+k)^2]` is bounded below by `4/(9|p|^4)` for
`|p|>=2|k|`; its radial integral in four dimensions diverges logarithmically.
Taking absolute values of unrenormalized graph families before their
subtractions therefore cannot give a cutoff-independent certificate.
Nor does the common-log cancellation supply the finite part left over.

A locally rebuilt subtraction estimate illustrates what an interval
calculation would need. For C^1 phi and delta>0,

    integral_(|z|<delta) |phi(z)-phi(0)|/|z|^4 d^4z
       <= 2 pi^2 delta sup_(|z|<delta)|grad phi(z)|
       <= 32 delta sup|grad phi|.                        (18)

The mean-value theorem and polar integration prove this, with `pi<4`.
It is a rational bound for one subtracted logarithmic singularity, not
a bound for D4: the full graph forest, tensor numerators, finite local
terms, and the remaining integration regions still need such estimates.
No unevaluated derivative supremum in (18) is presented as a load-bearing
numerical enclosure of the Yang--Mills coefficient.

If a producer supplied `|D4|<=d M4/pi^8`, `|D2|<=d M2/pi^4`, (1)
would give `|c|<=(2/3)M4+(2/11)M2`. The rational conversion is valid;
the missing M4 and M2 cannot be invented or supplied by free checks.
Similarly a positive-flow-time calculation at `t=tau lambda^2` would
have different free constants A4(tau), A2(tau). Its use for this task
requires controlled `tau->0` matching, not a silent substitution.

## 6. Uniformity is a separate obligation

**PROVEN logical distinction.** A finite perturbative coefficient at each
cutoff need not control the original-law limit. For example the scalar
family

    F_J(x)=1-2J x^2/(1+J x^2),        x=h^2>0,

has relative first coefficient zero for every fixed J, yet tends to -1
as J tends to infinity at fixed x. This is an elementary example of
nonuniform remainders, not a Yang--Mills law or a claim about its sign.
It demonstrates why an evaluated one-loop coefficient alone cannot
replace the uniform estimate required in K4MATCH (24).

The named original-law inputs remain: common trajectory; local scalar
insertion matching; complete normalized source derivatives including
the terminal integration and mixed conditional cumulants; uniform
large-field/exterior errors; and the appropriate two-point denominator
matching. Fixed source radius, finite-coupling kernel remainder, and
original-law coercivity/tails are coordinator inputs only. Their
selected-sector results are not re-proved or promoted here.

## 7. Non-cancellation and the exact K4MATCH obligation

**PROVEN conditional.** If the original law satisfies

    P=A4 u^-4(1+delta4),        Q=A2 u^-2(1+delta2),
    |delta4|, |delta2| <= 1/4,

then `P>=3A4/(4u^4)>0`, `Q>=3A2/(4u^2)>0` and

    12/25 <= R4/R0 <= 20/9,
    R4 > 18/[4225(N^2-1)].                              (19)

Monotonicity of `(1+delta4)/(1+delta2)^2` on this rectangle gives
the bounds. Here let `a_n^W` denote the original observable's coefficient
after any required common matching factor (`a_n^W=a_n+n z` for a factor
`1+z/u`); it need not equal the representative's a_n in (7).
If `|a_n^W|<=M_n` and the actual relative remainder is at most
`H_n/u^2+eta_n`, take
`u>=max(1,16M2,16M4,4 sqrt(H2),4 sqrt(H4))` and `eta_n<=1/8`.
Then `M_n/u+H_n/u^2+eta_n<=1/16+1/16+1/8=1/4`.
Both signs of the correction are allowed. These are the sufficient
K4MATCH (24) conditions, not constants established by this paper.

For the continuum witness, choose one sufficiently large m_star, then
pass cutoff/volume along the common moment-convergent sequence with
`lambda_star=L^-m_star` fixed. The absolute fourth-cumulant margin uses
`u<=U_+(m_star)`. This excludes fields Gaussian **on e**; it does not
exclude free theories with composite e, whose free example has the
positive coefficient (1). The rest of the hierarchy and reconstruction
remain their original independent requirements.

**Exact discharge statement.** This note resolves the *universal RG and
anomalous-factor bookkeeping part* of K4MATCH section 6.2 / REVIEW_K4MATCH
R10: those common terms contribute zero to the first ratio coefficient,
and its isolated finite term has rate (12) under FLOW's hypotheses.
It does **not discharge binding obligation B1 / AUTHOR item 3**: the
actual finite Yang--Mills coefficient, a certified magnitude (or sign),
and uniform original-law non-cancellation control remain OPEN. It also
does not discharge CUMUL C-4MATCH, C-2MATCH or PL-4C. An honest completion
verdict for those requested scientific targets is HOLD.

## 8. Verification and review

The registered checks concern exact RG polynomial identities, convention
changes, cancellation, rational free margins, and the reciprocal error
bound. They do not compute any of (16)'s Yang--Mills integrals.
The [criteria](checks/k4corr_criteria.md) precede
[the checker](checks/k4corr_exact.py). All **56 exact assertions within the
registered criteria passed** in [the final run](checks/k4corr_attempt02_results.json),
including the specified mutation controls. The first run had 54 passing
assertions; review found that its reciprocal tests were only finite rational
spot checks. Two generic polynomial denominator checks were added within
the existing registration, and both runs are preserved. The written proof
in (11) establishes the inequality on its whole stated domain.
The [final resource receipt](checks/k4corr_attempt02_run.json)
records one serial child, nice 20, all five thread counts one, all load
averages below 2.198, native free memory 52%, and peak combined RSS
41,975,808 bytes. The four numerical locks were held exclusively; existing
lock files were opened read-only. No numerical run failed. This is algebra
evidence, not a successful interacting-coefficient calculation.

**Fresh same-family hostile review: HOLD for completion of the brief.**
The [independent review](checks/k4corr_review.md) assesses the conditional
calculations and the unresolved finite Yang--Mills calculation separately.
Author or reviewer agreement on the algebra is not retained or audit status,
and does not supply any OPEN dynamical input.
