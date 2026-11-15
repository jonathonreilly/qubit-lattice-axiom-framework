# K4MATCH — fourth-source matching on the common Wilson sequence

**Disposition.** The fourth-order chain identity, Gaussian reference
comparison and conditional lower-matching theorem below are **PROVEN** at
their stated scopes. Their interacting Yang–Mills hypotheses remain
**OPEN**. The complete formal relative `O(g_FLOW^2)` coefficient is
identified, including its signs and combinatorial factors. Its actual
renormalized YM value, sign and uniform bound are **OPEN**. In particular,
the requested unconditional perturbative non-cancellation check has **not
been achieved**. A precise sufficient non-cancellation inequality is proved;
no proxy coefficient is substituted for the missing YM calculation.

This is an author reduction under [PROCESS_LIGHT](PROCESS_LIGHT.md), with
the same separated e field as [CUMUL](CUMUL.md) and [COMBO](COMBO.md).
PROVEN does not mean an audit grade. Balaban and Dimock receive credit
for the constructive RG method; no result of theirs supplies an unstated
YM estimate here. Source identities and the read scope are in
[the log](K4MATCH_LOG.md) and [the manifest](checks/k4match_sources.json).

## 1. Exact target and normalization

**PROVEN specification.** Fix `N>=2`, `d=N^2-1`, odd `L>=3`,
`a=L^-K`, `lambda=lambda_m=L^-m`, `k=K-m`, and the actual chain coupling

    u=u_k=g_FLOW,k^-2=2N/g_std,k^2.

Use the original Wilson observable, without replacing it by its quadratic
part or changing its normalization:

    e_a(x)=(4a^4)^-1 sum_(mu!=nu) sum_(p in clover_mu,nu(x))
                                  [1-Re tr(U_p)/N],
    O_i=sum_x a^4 f_(i,lambda)(x)e_a(x),   Z(a)=1.

The four unit-integral bumps are exactly CUMUL (C2): coordinate half-width
`epsilon=1/10000`, centres `c_i=((2i-5)/2,0,0,0)`, product bump made
from `b(s)=exp[-1/(1-s^2)]` on `|s|<1`, normalized to integral one,
and `f_(i,lambda)=lambda^-4 f_i(x/lambda)`. Distinct supports remain
separated after clover thickening when `a/lambda` is sufficiently small.
Their reflection pairs are (1,4) and (2,3). All products are distinct-slot
separated tests; no coincident continuum fourth moment is introduced.

Put

    P=lambda^16 kappa_4(O_1,O_2,O_3,O_4),
    Q=lambda^8 Cov(O_2,O_3),       R4=P/Q^2.                 (1)

Centring each O changes neither quantity. CUMUL (C14)–(C16) gives exact
smooth-test constants `A4=d A/pi^8`, `A2=d B0/pi^4`, with

    3/2<A<5/3,  11<B0<13,
    R0=A4/A2^2=A/(d B0^2),    3/(338d)<R0<5/(363d).       (2)

For clarity, at the centres only, the three curvature cycles give
`96(1/81+1/256+1/20736)=169/108`; the point ratio is
`169/(15552d)`. It is not the smeared ratio R0. The smooth bounds follow
from the whole-support bounds `9971/6480<A<10309/6480` and
`12(2500/2501)^8<B0<12(2500/2499)^8` rebuilt in CUMUL §3.3.

The normalized target is

    R4/R0 = 1+o(1).                                        (3)

We give the stronger sufficient statement

    P=A4 u^-4(1+delta4),  Q=A2 u^-2(1+delta2),
    |deltan|<=rn(m)+hn(k)+vn(R/lambda),  n=2,4,             (4)

where each error tends to zero at infinity, uniformly on the common
trajectory. The order of limits is essential: first fix m and let
`(K_j,R_j)` tend along the common sequence; then let m grow. Equivalently,
(4) implies `lim_m limsup_j |R4_j(m)/R0-1|=0`. A fixed small depth k
would retain its lattice error and would not establish this assertion.
Raw `kappa4/free kappa4 ->1` is obtained using the same u in the free
reference; a ratio alone would not establish that absolute normalization.

## 2. What the shared inputs actually cover

| Input | Shared content and source | Status consumed here |
|---|---|---|
| LGF | Coupling-one free curvature `G^F=d Delta_1^-1 d*`; entrywise `O(r^-5)+O(T^-4)` at order two, LGF (37)–(41) | **PROVEN**, free library only |
| K-dec | `|K_i(p,q)|<=M L^-4i exp(-mu dist/L^i)` and terminal `M L^-4K`; TSE55 §3.2 | **PROVEN implication** of its named linear-response/coercivity inputs; no general-background estimate inferred |
| FLOW-pw / tuning | Pairwise brackets `b_-(n-j)-R_F<=u_j-u_n<=b_+(n-j)+R_F`, a positive lower bound for all u_i; fixed-scale brackets `U_-(m)<=u_k<=U_+(m)` | FLOW §§7–8 are **PROVEN conditional**; realizing their hypotheses for this YM trajectory is **OPEN** |
| Source estimates S | Exact coupling-field tilt, SRCCD55 §5.0 source recursion; SRCAN55 §2.2 tree source holomorphy; SRC2_55 §2.2 S0–S4 and Theorem I | The exact identities are **PROVEN**; tree bounds retain their conditions; the full source representation and its relative-radius matching are **OPEN** |
| TSE55 / PL-1L | Gaussian bubble, fine/coarse scale summation and comparison; WITNESS (E11) is the summed interacting error | Assembly **PROVEN conditional**; PL-1L itself **OPEN** |
| CUMUL | Fixed tests, free four cycles, positive smooth coefficient, fixed-scale witness | **PROVEN** at free/conditional scope; C-4MATCH is **OPEN** |
| Common hierarchy | E-ALG/SEQ and C-ALG/SEQ/MOM; actual all-order OS inputs, common moment convergence and extension | **OPEN** for YM; unchanged by this reduction |

Here “S” denotes the available source machinery just specified, not an
unidentified proved theorem. SRC2_55 already states an **all-n** source
representation. Its n=4 instance is not a new kind of source, but its
conditional upper estimate is not leading-coefficient matching.
An AF-e estimate for the pair (1,4) must also be supplied for (2,3) to
control Q. Extending PL-1L to each of the six fixed pairs costs a finite
maximum of constants **if** its producer is uniform for those tests;
one pair's theorem alone does not imply the other five.

The current coordinator units are inputs only: fixed source radius,
finite-coupling kernel remainder, original-law coercivity and tails,
and source-free interacting selected-core remainder. Their local or
selected-sector results do not establish a source-dependent full-history
fourth derivative. No coordinator file is modified or re-proved here.

## 3. The exact fourth-order RG algebra

### 3.1 A genuine telescoping identity — PROVEN

At finite K,R let `G_i^r=E[O_r|U_i]`, `i=0,...,K`, in the actual
normalized chain. Its Markov property gives
`E[G_i^r|U_(i+1)]=G_(i+1)^r`. Set

    D_i,4=lambda^16 [kappa4(G_i^1,...,G_i^4)
                      -kappa4(G_(i+1)^1,...,G_(i+1)^4)]  (i<K),
    D_K,4=lambda^16 kappa4(G_K^1,...,G_K^4).

Then `P=sum_(i=0)^K D_i,4` exactly. This identity is useful only when
its increments are expanded correctly. For `X_r=G_i^r`, condition on
`Y=U_(i+1)` and write `c_B(Y)=kappa(X_r:r in B |Y)` and
`mu_r=c_{r}=G_(i+1)^r`. All outer cumulants below use the actual
Y marginal. The increment divided by `lambda^16` equals

    E c_1234
      + sum_(4 triples abc; remaining d) Cov(c_abc,mu_d)
      + sum_(3 pair partitions ab|cd) Cov(c_ab,c_cd)
      + sum_(6 pairs ab; remaining c,d) kappa3(c_ab,mu_c,mu_d).
                                                               (5)

In particular it is not just `E c_1234`. None of its fourteen terms
is assigned a positive sign.

**Proof from finite algebra.** In the ring with `z_r^2=0`, write the
conditional log moment polynomial as `C(z;Y)=sum_(B nonempty)c_B(Y)z_B`.
The unconditional moment polynomial is `E exp C(z;Y)`. Its logarithm
is `sum_(q=1)^4 kappa_q(C,...,C)/q!`. The coefficient of `z_1234`
is the sum over all partitions pi of the outer cumulant of the
`c_B`, `B in pi`: each unordered partition occurs q! times, cancelling
the denominator. The 15 partitions have types `4`, `3+1`, `2+2`,
`2+1+1`, `1+1+1+1` with multiplicities `1,4,3,6,1`. Subtracting the
last outer `kappa4(mu_1,...,mu_4)` proves (5). Bounded finite-lattice
observables justify the moment identities without a uniform analytic
radius. This rebuilds Brillinger's conditioning method locally.

A simple algebra check exposes the omitted terms: if `X|T` is centred
Gaussian of variance T, and T is 1 or 3 with probability 1/2 each,
then `E kappa4(X|T)=0` but `kappa4(X)=3 Var(T)=3`. The three `2+2`
terms supply it. This is a conditional-probability example, not a model
of the four separated YM insertions.

### 3.2 Which source representation is needed — PROVEN identity; producer OPEN

The exact tilt remains the same scalar coupling-field perturbation:

    sum_r z_r O_r=sum_p h_z(p)s(U_p),
    h_z(p)=(1/2)sum_(x in corners(p)) sum_r z_r f_(r,lambda)(x),
    u_0(p)=u_0-h_z(p),   s(U)=1-Re tr(U)/N.                (6)

Keep every normalized RG kernel fixed, including its normalizer. Retuning
the kernels when differentiating would change the observable. Define

    Phi_i(z;U_i)=log E[exp(sum_r z_r O_r)|U_i],
    J_i,B=partial_B Phi_i(0;U_i).

The exact recursion `Phi_(i+1)=log E[exp Phi_i|U_(i+1)]` implies

    J_(i+1),B = sum_(pi partition of B)
                    kappa_(|pi|)(J_i,C : C in pi | U_(i+1)). (7)

The proof is the same nilpotent expansion. Initially `J_0,{r}=O_r`
and all higher mixed J vanish. For B of size four, (7) includes
`E J_i,1234`, four `Cov(J_i,abc,J_i,d)`, three
`Cov(J_i,ab,J_i,cd)`, six `kappa3(J_i,ab,J_i,c,J_i,d)`,
and `kappa4(J_i,1,...,J_i,4)`. Integrating the terminal law adds the
same partition mechanism once more. These are source jets of O; the
`c_B` in (5), in contrast, are conditional cumulants of the first images
G_i. Equations (5) and (7) are compatible but are not interchangeable.

The smallest direct jet system retains all 15 nonempty subsets of the
four labels, including triples. The **continuum free-curvature reference**
has vanishing separated third cumulant (CUMUL (C12)); this does not set
finite-lattice or conditional triple jets to zero. A joint four-source
analytic representation is a
sufficient implementation; a controlled jet through degree four also
suffices. There is no necessity claim for a full polydisc or for this
particular RG route. A two-insertion matching estimate supplies none of
the last two jet degrees. For example, the positive finite laws
`P_t(x)=2^-4(1+t x1 x2 x3 x4)`, `|t|<=1`, have identical proper-subset
mixed moments while `kappa4(x1,x2,x3,x4)=t`. This demonstrates the
missing information at the level of moment data, not a failure of YM.

## 4. Reusing the free machinery for four insertions

### 4.1 Mixed-slice reference and its increments — PROVEN

Let `W_r=diag(w_r(p))`, `w_r(p)=(1/4)sum_corners f_(r,lambda)(x)`.
Use the one-colour free slices `mathcal K_i` of TSE55 §2.2 and put

    a_i=mathcal K_i/u_i,  H_i=sum_(j>=i)a_j, H_(K+1)=0,
    F4(H)=16d lambda^16 sum_(c=1234,1243,1324)
                       Tr(W_c1 H W_c2 H W_c3 H W_c4 H),
    Lambda_i,4=F4(H_i)-F4(H_(i+1)),  P_run=F4(H_0).       (8)

Then `sum_i Lambda_i,4=P_run`. Expansion assigns every four-edge
scale tuple to its minimum scale index, so all mixed-slice cycles and
the terminal slice are included. Equivalently, in the independent
Gaussian-slice model the conditional image of each quadratic observable
is its quadratic form in the remaining tail plus a deterministic
constant. Constants drop out of kappa4, giving precisely (8).
This proves that (8) is the Gaussian counterpart of (5), not just an
arbitrary splitting of a polynomial.

The factor 16 per undirected cycle is obtained by assigning the two
curvature legs at each vertex to its two neighbours in `2^4` ways.
There are three undirected Hamilton cycles and one common colour loop.
Normal ordering removes self-pairings; disconnected pairings disappear
in the cumulant. This is the finite Wick proof behind CUMUL (C11).

### 4.2 Running reference versus continuum — PROVEN conditional

Assume exactly K-dec and FLOW-pw as specified in section 2, including
`u_i>=u_min>0` and `u_k>=max(1,2R_F+2)`. All six cross-support
separations have a common positive lower bound in lambda units.
TSE55 §3.4's kernel estimate, with the maximum of the six constants,
therefore gives

    |G_run(p,q)-G^F(p,q)/u|<=C1 L^-4k u^-2,
    |G^F(p,q)|<=C0 L^-4k.                                (9)

For completeness, subtract the slice sums and use
`|u_i^-1-u^-1|<= (b_+|i-k|+R_F)/(u_i u)`. Fine slices have
`u_i>=u/2` and exponential suppression in `L^(k-i)`. On coarse slices
split at `n1=floor((u/2-R_F)/b_+)`: before n1, `u_(k+n)>=u/2`;
after it use u_min, while `L^-4n` beats every fixed power of u.
The terminal slice obeys the same coarse envelope. This proves (9)
uniformly; no exact beta coefficient is needed.

For sufficiently fine `a/lambda`, `sum_p w_r(p)<=12a^-4` for each
unit-integral nonnegative test. Telescope the product of four scalar
kernel entries around each cycle. One changed entry costs
`C1 L^-4k u^-2`, and the other three are bounded by
`(C0+C1)L^-4k/u`. Since `lambda^16 a^-16 L^-16k=1`,

    |P_run-P_free/u^4|<=C_AF,4/u^5,
    C_AF,4=192 d 12^4 C1(C0+C1)^3.                        (10)

Here `P_free=F4(G^F)` in (8)'s convention, at coupling one.
LGF (41) on each cross edge and the fixed separated Riemann sums give

    |P_free-A4|<=C_f [L^-k+(lambda/R)^4].                 (11)

Indeed rescaling `r` to `r/L^k` turns the kernel error into
`O(L^-k)+O((lambda/R)^4)` on this compact separated set. Products of
four bounded kernels preserve this error by telescoping. Replacing
clover-corner tests by point tests and replacing the lattice sums by
integrals costs `O(L^-k)` since the fixed bumps and continuum kernel
have bounded first derivatives there. Choose `R/lambda` large enough
that all relevant displacements and stencils lie within T/4. Constants
depend on the fixed bumps (including epsilon), N,L and the named input
constants, never K,R,m. The same proof with two edges gives

    |Q_run-A2/u^2|<=C_AF,2/u^3
                     +C'_f u^-2[L^-k+(lambda/R)^4].       (12)

Thus **no new interacting or four-point library estimate is hidden in
the free reference step**. It consumes order-two LGF kernel estimates,
not fourth spatial derivatives of a Green function.

### 4.3 What summation can and cannot provide — PROVEN conditional

For some fixed `mu'>0,D>0` determined by the separated supports define

    p_i,4(k)=L^(4(k-i)) exp[-mu' D L^(k-i)]   (i<k),
    p_i,4(k)=L^-16(i-k)                      (i>=k),
    ubar_i=u_(max(i,k)).

The free increments (8) obey
`|Lambda_i,4|<=C ubar_i^-4 p_i,4(k)`. For i<k, expand the
tail difference in (8): it has at least one a_i cross edge, with its
fine exponential, and three tail kernels bounded as in (9). For i>=k,
each tail cross kernel is at most `C L^-4i/u_i`; the four factors give
`L^-16(i-k)`. The latter tail bound follows from the same near/far
split used for (9), now starting at i. This includes the terminal term.

For every fixed s>0,

    sum_i ubar_i^-s p_i,4(k)<=C_s u^-s.                   (13)

The fine sum is `u^-s sum_(n>=1)L^4n exp[-mu'D L^n]`.
The near coarse sum is at most `2^s u^-s/(1-L^-16)`; the far coarse
sum is at most `u_min^-s L^-16(n1+1)/(1-L^-16)` and is bounded by
a constant times u^-s. This is the TSE55 SUM argument with 16 replacing
8. Any fixed positive coarse exponent would suffice for summability.

What is **OPEN** is the interacting estimate

    PL-4JET: |D_i,4-Lambda_i,4|
                   <=E4 ubar_i^(-4-theta4) p_i,4(k), theta4>0. (14)

It must bound the **sum of all fourteen terms** (5) and the terminal
cumulant, with actual normalizers and all histories. Its summed
consequence is CUMUL's PL-4C. Claiming (14) from free coarse decay, or
from an estimate of `E c_1234` alone, would be circular. The full
producer-facing (14) is stronger than the summed target; no implication
from the target back to (14) is asserted.

## 5. A source-norm alternative and the precise lower theorem

### 5.1 Four-source remainder as a usable sufficient input

Set `X_r=u lambda^4 O_r` solely for estimating source coefficients;
this does not change the physical normalization Z(a)=1. Let
`L(t)=log E exp(sum t_r X_r)` and let L_run use the quadratic Gaussian
reference with the same scaling. For any analytic H define

    Pi4 H(t)=sum_(J subset {1,2,3,4})(-1)^(4-|J|) H(t_J),

where inactive coordinates are zero. This kills every term missing a
source, including deterministic means and contact counterterms that
depend on fewer than four supports. It does not discard multiscale
terms meeting all four supports.

**4-SRC-ERR (OPEN sufficient producer):** there are radii
`rho_r>0` independent of K,R,m, a holomorphic branch of both relevant
logs, and a bound on their projected difference on `|t_r|<rho_r`,

    sup |Pi4(L-L_run)|<=E_src u^-theta4.                   (15)

The free analytic radius required here already follows from the shared
inputs. To see this, use positivity of the Gaussian slices and split
`G_run=G_fine+G_coarse` at k. Since `u_i>=u/2` for i<=k and
`sum_i mathcal K_i=P_ex<=I`, `G_fine<=2I/u`. Thus

    u lambda^4 ||sqrt(W_r) G_fine sqrt(W_r)||<=2||f_r||_infinity.

For i=k+n>k, weighted Schur with weights `sqrt(w_r(p))` on the
support of W_r, K-dec and `sum_p w_r(p)<=12a^-4` gives

    u lambda^4 ||sqrt(W_r) G_coarse sqrt(W_r)||
          <=12M sum_(n=1)^m (u/u_(k+n)) L^-4n <=C_co.      (15a)

The last bound is the same FLOW near/far split as (9), including the
terminal slice. Zero entries of W_r can be omitted in Schur's test.
The positive operators `sqrt(W_r)G_run sqrt(W_r)` and
`sqrt(G_run)W_r sqrt(G_run)` have the same nonzero eigenvalues.
Consequently, with
`A(t)=u lambda^4 sqrt(G_run)(sum_r t_r W_r)sqrt(G_run)`,
small fixed radii give `2||A(t)||<1`. The convergent matrix series
`L_run(t)=-(d/2)Tr log(I-2A(t))` defines the free branch. Its complete
trace need not be uniformly bounded as a->0; this argument proves
the radius only. The quantum branch and the uniform **difference**
bound in (15) remain OPEN.

The logs may first be reduced by proper-subset counterterms: only Pi4
and its analytic continuation are needed. By four-variable Cauchy,

    |P-P_run|<=E_src (product_r rho_r^-1) u^(-4-theta4).    (16)

**PROVEN implication.** The mixed derivative is `u^4(P-P_run)`;
Cauchy's multi-index is `(1,1,1,1)` and contributes **no 4!**.
This is also proved by integrating once around each circle. A bound
on L-L_run itself implies (15) with a factor at most 16; these two
norms must not be confused.

In TSE55 §4.4(a)/§5.1's relative-source notation one can choose
`rho_r=rho/||f_r||_infinity`, if that domain is supplied. Adding four
source directions changes a fixed coefficient-field norm bound by at
most their sum (so a factor-four radius reduction suffices at the
level of the **same** norm). It does not prove that this norm/radius
is propagated through the full RG. A fixed absolute bare-source radius
gives radii of order 1/u in t and loses the desired u^-4 gain.
SRC2_55's existing conditional all-n upper bound, or tree-level SA-K,
therefore cannot be used as (15). Full quantum matching, the relative
radius and coarse-scale summability remain additional requirements.

### 5.2 Conditional TS4 theorem — PROVEN

Assume the shared free inputs of section 4, a single actual tuned
trajectory with `U_-(m)->infinity` and finite positive U_+(m), and
either (14), (15), or the summed PL-4C directly. Also assume PL-1L_Sigma
for the denominator pair (2,3), with exponent theta2>0. Combining
(10)–(13),(16) yields (4), with for example

    rn(m)=an/U_-(m)+bn/U_-(m)^thetan,
    hn(k)=cn L^-k,     vn(x)=cn x^-4,     n=2,4.           (17)

All coefficients are fixed positive constants obtained by dividing
the absolute errors by A2 or A4. They are not fitted to YM data.
No sign of a next-order coefficient is needed for this implication.
For `epsn=rn+hn+vn`, `eps2<1`, algebra gives

    R4/R0=(1+delta4)/(1+delta2)^2,
    |R4/R0-1|<=(eps4+2eps2+eps2^2)/(1-eps2)^2.           (18)

This proves (3) in the stated order of limits. To obtain an N5 witness,
choose m_star with rn(m_star)<=1/8 for both n; then choose fixed
depth/radius thresholds making `hn+vn<=1/8`. Keep
`lambda_star=L^-m_star` fixed for the cutoff/volume limit. On the tail,

    kappa4_j >= 3 A4/(4 lambda_star^16 U_+(m_star)^4)>0,
    Cov23_j  >= 3 A2/(4 lambda_star^8 U_+(m_star)^2)>0,
    R4_j/R0 >= (3/4)/(5/4)^2=12/25,
    R4_j > 18/[4225 (N^2-1)].                             (19)

The upper ratio factor is `20/9`. Pass the seven centred coordinates
(S4 and all six S2) along **the same** C-SEQ/MOM sequence; the cumulant
is a polynomial in them, so (19) passes to the limit. Without centring,
use all fifteen subset moments. Bounds on weakly convergent laws alone
would not give moment convergence. Reconstruction still needs the
actual all-order OS hypotheses; this theorem does not produce them.
The polynomial kappa4 supplies the continuous fixed-scale witness;
R4 is used only where Q has the positive margin just proved.

## 6. Perturbative sanity check: the coefficient, its sign and its size

### 6.1 All order-g-squared terms — PROVEN formal identity

Write `h=g_FLOW,k=u^-1/2`. A finite regulated, gauge-fixed Gaussian
expansion, after resolving zero modes, has the symbolic form

    S_eff=S0+h V1+h^2 V2+...,
    X_r=X_r0+h X_r1+h^2 X_r2+....                          (20)

Here the action includes the measure/Jacobian and every effective
counterterm in the chosen formulation; any ghost treatment must be
included consistently. The parity used is: S0 and X_r0 are even under
reversing the Gaussian field, V1 and X_r1 are odd, and V2 and X_r2 are
even. In the microscopic link expansion this follows by expanding
`U=exp(i sqrt(2N) h_0 A)` and `h_0^-2 sum s(U_p)`, with
`h_0=u_0^-1/2`. This does **not** identify the bare h_0 with the
matched h=u_k^-1/2. A supplied effective action, its gauge/IR prescription
and its matching counterterms must carry this parity to (20). Formula
(20) does not assert that the RG has supplied those vertices or a
uniform expansion.

Let kappa0 denote cumulants under the regulated Gaussian law. The
coefficient D4 of h^2 in `kappa4(X_1,...,X_4)` is

    D4 = sum_r kappa0(X_r2, X_s0 : s!=r)
       + sum_(r<s) kappa0(X_r1,X_s1, X_t0 : t notin {r,s})
       - sum_r kappa0(X_r1, X_s0 : s!=r, V1)
       - kappa0(X_10,X_20,X_30,X_40,V2)
       + (1/2) kappa0(X_10,X_20,X_30,X_40,V1,V1).          (21)

All listed arguments in each line belong to one joint cumulant. The
two-insertion coefficient D2 has exactly the same five families with
labels restricted to (2,3). The leading coefficients at a finite
regulator are the corresponding Gaussian cumulants; they tend to A4
and A2 under section 4's free limit. They must not be replaced by A4/A2
before taking that free limit.

**Derivation.** For general t, tilt the Gaussian expectation by
`exp(sum t_r X_r0)` and put `A(t)=sum t_r X_r1-V1`,
`B(t)=sum t_r X_r2-V2`. Expansion of its normalized logarithm gives

    L_h(t)=L_0(t)+h <A(t)>_t
          +h^2[<B(t)>_t+(1/2)kappa_t(A(t),A(t))]
          -the same correction at t=0 +....              (22)

Oddness makes the h term zero. Differentiating the h^2 term with
respect to four distinct sources inserts X_r0 into Gaussian cumulants.
Derivatives hitting one or two explicit source factors produce the
first three lines of (21); the remaining derivatives give its last
two terms. The factor 1/2 cancels the two orderings of distinct
X_r1,X_s1 but remains for the repeated V1. This proves (21) without
assuming convergence of a perturbation series. Parity removes all
odd formal powers; it does not bound the remaining series.

The exact checker independently expands **normalized moments**, then
forms their cumulants, for fixed polynomial control data. It reproduces
all five terms for n=2 and n=4. Omitting the double-cubic term fails.
Those controls check the derivation; their numerical coefficients are
not YM diagrams and are not estimates of D4 or D2 for this problem.

### 6.2 What can be said about sign — partial check; actual sign OPEN

If uniform renormalized coefficients and remainders in (20) were
supplied, set `a=D4/A4`, `b=D2/A2` in the continuum matched scheme.
Then

    P=A4 u^-4[1+a/u+O(u^-2)],
    Q=A2 u^-2[1+b/u+O(u^-2)],
    R4/R0=1+(a-2b)/u+O(u^-2).                            (23)

The signs in (21) are exact **insertion signs**, not signs of the
integrals. Covariance positivity does not fix a joint fourth, fifth or
sixth cumulant. In particular the sign of the absolute correction a
and the sign of the ratio correction a-2b are both **OPEN for YM**.
Neither a positive beta function nor the free leading coefficient
determines them. No number in FLOW evaluates the five source-dependent
families (21) at these four bumps.

There is a useful exact check on the **running-factor part**. With
`u(mu')=u(mu)+b_run t`, `b_run>0`, `t>=0`, the free factors change by

    P_free factor=(1+x)^-4=1-4x+10x^2+...,
    Q_free factor=(1+x)^-2=1-2x+3x^2+...,  x=b_run t/u(mu).

The linear numerator correction is negative, but their ratio is
**exactly one**, including all powers of x. Likewise a common field
factor `1+z/u` shifts a by 4z and b by 2z, leaving a-2b invariant.
These statements do not compute the remaining geometry-dependent
vertex correction. For t growing so that x is order one, truncating
`1-4x` would be invalid; the exact factors or the running u_k must be
used. A common field factor is cancelled algebraically, not assumed
to be the entire renormalization of a product of sources.

### 6.3 A non-cancellation certificate and the missing bound

**PROVEN conditional.** Suppose, in addition to the free limits, one
has uniform constants M4,M2,H4,H2 such that

    |a|<=M4, |b|<=M2,
    |P/(A4u^-4)-1-a/u|<=H4/u^2+eta4,
    |Q/(A2u^-2)-1-b/u|<=H2/u^2+eta2,                    (24)

where eta denotes the cutoff/volume error. Taking

    u>=max(1,16M4,16M2,4 sqrt(H4),4 sqrt(H2)),
    eta2,eta4<=1/8

makes both relative errors at most `1/16+1/16+1/8=1/4`.
Thus (19) holds for either sign of the correction. These constants
must be uniform in K,R and in the matched short scale, with large
logarithms controlled; merely showing a finite coefficient at each
finite cutoff is insufficient. The exact rational margins in (19)
are checked without rounding. A weaker proven error
`O(u^-theta)` with any theta>0, such as (14), would also suffice and
need not establish the sharper order-g-squared expansion.

**Result of the requested actual YM check: OPEN / not passed as a
YM non-cancellation claim.** Formula (21) exposes the full missing
calculation; (24) states the sufficient size threshold. The available
shared inputs supply neither its evaluated YM sign nor its uniform
bound. Numerical checks of algebra, parity or the free running factor
cannot certify (24). Finite-coupling, full-history source estimates are
still needed even after a perturbative coefficient is computed.

## 7. Exact remaining YM obligations and comparison with PL-1L

| Obligation on the original law | PL-1L / AF-e half | Increment for K4MATCH | Status |
|---|---|---|---|
| Common trajectory, coupling dictionary and positive brackets | E-TR and FLOW-pw | Same u_i, no new beta coefficient | **OPEN** realization; shared conditional theorem |
| Original field, moments, extension and reconstruction | E-ALG/SEQ, all-order OS input | Same hierarchy; seven centred coordinates at one fixed four-test tuple | **OPEN** realization; finite moment algebra **PROVEN** |
| Quadratic source with coefficient tending to one | P3, P6 of TSE55 §6.4/E5 | All four single images normalized to the same free weights; product-source mixing also controlled | **OPEN** quantum matching; tree identities shared |
| Source-dependent Gaussian dominance and background covariance | P1, P2; two-source error | Fourth mixed logarithmic derivative or jet; (5)/(7)'s triples and pair-pair terms | **OPEN** |
| Coarse joint curvature law | P4 matches a covariance | Joint moments/cumulants entering products of up to four quadratic images (up to eight curvature legs), not just the curvature covariance | **OPEN** |
| Localization and scale summation | Coarse exponent 8; fine exponential; terminal covariance | All connected four-source terms; sufficient coarse exponent 16 in (14), terminal fourth cumulant and mixed slices | Summation/free reference **PROVEN conditional**; interacting bound **OPEN** |
| Large fields, complement, boundaries, normalizers | P5, all levels and original law | All fourteen increment terms or the full projected source error, with all complete histories, original exterior/reference costs and terminal integration | **OPEN**; coordinator outputs retained only at their declared scope |
| Denominator and disconnected terms | PL-1L for AF pair (1,4) | PL-1L for (2,3); finite bounds for all six pairs and actual moment convergence | **OPEN** producers; finite reuse if provided |
| Perturbative relative correction | Two-insertion source coefficient | Evaluate all five four-insertion families (21); bound remainders uniformly; ratio uses a-2b | Formula **PROVEN formal**, actual sign/bound **OPEN** |

These rows are obligations within one source calculation, not a claim
that all are independent assumptions. PL-4JET or 4-SRC-ERR packages
several rows together; imposing both is unnecessary. The minimal new
observable estimate is the summed PL-4C, once the shared free reference
and the appropriate two-point matching are available. It is essentially
the original matching target with its explicit free reference separated
off, not a solved dynamical theorem. The stronger jet/source formulations
expose what an RG producer must actually estimate.

**ARGUED assessment.** The final witness uses fewer moments/scales than
AF-e, but its dynamical proof does not follow from the AF-e half. The
new content here is the explicit increment and source-jet algebra,
the four-cycle scale allocation, the quantitative transfer of LGF and
FLOW-pw to that reference, and the full perturbative bookkeeping.
The remaining decisive task is a uniform fourth-source error for the
original law, including the mixed conditional terms in (5). No claim
of a no-go theorem, full existence, unrestricted free-net exclusion,
or a physical mass gap is made.

## 8. Verification, provenance and review

[Registration](checks/k4match_criteria.md) preceded the
[exact checker](checks/k4match_exact.py). All **64** registered algebra
assertions and mutation controls passed in
[the guarded run](checks/k4match_results_guarded.json), including exact
partition subtraction, mixed-slice enumeration, five-family perturbative
coefficients and ratio margins. The separately preserved
[first](checks/k4match_results.json) and
[second](checks/k4match_results_rerun.json) attempts failed at the
unsupported macOS RSS-limit call before any scientific assertion.
[The corrected watchdog](checks/k4match_run.py) retained the resource
thresholds. Its [receipt](checks/k4match_run.json) records nice 20,
all five thread counts one in the child, load averages below 2.01,
49% native free memory, and peak combined RSS 41,697,280 bytes.
There was one numerical process, no pools and no sampling.

Conditioning cumulants are credited to
[Brillinger, The calculation of cumulants via conditioning](https://www.ism.ac.jp/editsec/aism/pdf/021_1_0215.pdf);
the needed identity is fully rebuilt in section 3, not imported from
the citation or SRCCD55's memory-labelled statement. Wick/Isserlis
pairing is rebuilt for the four-cycle factor. For method attribution,
[Dimock's exposition of Balaban's RG](https://arxiv.org/abs/1108.1335)
was consulted at abstract scope; its scalar three-dimensional example
is not used as a four-dimensional YM estimate. No memory-only [m]
claim carries any step of this argument, and no literature coefficient
has been inserted into the calculation.

**Fresh independent hostile review: HOLD for brief completion.** The
[separate-context review](checks/k4match_review.md) passes the conditional
reduction, the two corrected wording issues and the added free analytic
radius. It identifies AUTHOR item 3 as outstanding: specify and evaluate
the actual matched YM vertices for these tests, determine the correction's
sign and controlled size, and establish the stated non-cancellation
threshold. The formal identities and proxy algebra do not close that
requirement. This is same-family Codex review, not cross-family review
or an audit grade. The post-review clarification distinguishes bare h_0
from matched h; final source identities are in
[verification](checks/k4match_verification.json).
