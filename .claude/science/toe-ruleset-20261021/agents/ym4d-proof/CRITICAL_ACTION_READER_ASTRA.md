# The actual critical action in joint original-reader norms

This short producer corollary makes explicit the critical-action budget
still separate in CD20 and SN30. It uses FU's existing actual finite-u
critical field; it constructs no new critical point. SA already gives a
connected critical-action increment on its real-coarse/source domain, and
IC already pays scalar contractions on its source-free complex-coarse domain.
The continuation here is their precise joint-domain, original-block match.
Fresh independent review is required. Full four-dimensional continuum
existence and a positive physical continuum mass gap remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit joint-domain original-reader locality and scale accounting for the already constructed actual finite-u critical action."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Existing result and exact domain

[SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md), lines 285--291, already identifies
the lift action and gives a connected O(delta_V^2) increment to its actual
critical field, before division by sigma^2. Its coarse data are real and its
support weights are in R-box units. [IC](INTERACTING_SELECTED_CORE_ASTRA.md),
IC27, already proves the scalar matrix/two-vector marking rule and a more
specific source-free tree/finite-u comparison. It is not a joint Wilson-source
theorem for the present action. [FU](FINITE_U_CRITICAL_FIELD_ASTRA.md),
FU29--FU30, keeps the exact critical value and records SA/FR's real-slice
source-action budget, but does not display the joint-domain scalar family
and explicit original-block budget below. No first-existence or new
scalar-contraction mechanism is claimed.

Fix FU's N>=2, D=N^2-1, odd L>=3, T>=2, real u>=1 and admitted positive
compact kappa interval. Let m0=3L^4+1, n=m0 T^4, n0=Dm0, d=n0 T^4 and
sigma^2=N/u. Fix **the same** geometry-only R and all the subsequently
recomputed FU bounds/radii used by the intended CD/NRR/SN consumer. No R
is enlarged here. The available original-block rate and product domain are

    beta=(16R)^(-4),
    V_c=exp(v_c)Vbar_c, max_c||v_c||HS<eta,
    |epsilon_p|<rho, delta_(Vbar)<=delta_*,
    delta_hat=delta_*+8eta.                               (CA1)

All selected FU17--FU19 constraints and any stricter consumer restrictions
remain. In particular delta_hat<1/2, the fine-coordinate radius obeys
tau<a/8, and the complete-reader critical field satisfies

    b=b_*(V,epsilon), F_epsilon'(b;V)=0,
    V_beta(b)<=t_b:=2 A_G g_*(1+rho)delta_hat<=tau/2.       (CA2)

Here V_beta is the maximum component-root and full marked-incidence sum,
with individual coefficient suprema inside the sums; its atoms include
their scalar output owner and every original data/source reader. All colours,
root modes, crossing links and harmonic directions are retained. The actual
phase is FU1, with no vacuum removed:

    F_epsilon(a;V)=F_0(a;V)+sum_p epsilon_p W_p(a;V),
    F_0=sigma^2[-log w_0(U(a),V)-sum_free e log j_N(a_e)],
    W_p=tr(2I-U_p-U_p^-1)/2, K=F_0''(0;V).               (CA3)

The finite-t normalized compact kernel and Haar logarithm occur once. Only
original Wilson coefficients vary; t=kappa u stays real and fixed. Complex
transposes below are bilinear, without complex conjugation. Joint suprema
use delta_hat; the actual delta_V can replace it only on a fixed real-V slice.

## 2. Hessian atoms uniformly along the actual critical segment

For matrix families use FU's M_beta (maximum absolute weighted row/column
sum), B_beta (weighted sum of all scalar entries through a fixed reader
mark), and Q_beta=M_beta+B_beta. All labels are connected original blocks
containing both field endpoints and complete original readers.

An explicit local family for K follows from its range-two, radius-three
reader stencil. Give entry K_ij the label
`N_3(X_i) union N_3(X_j)`. It is connected and contained in N_5(X_i).
With FU2/FU5's B, gamma and b_abs=n0*5^4*(B+gamma/4), set

    s_K=11^4, k_M=exp(beta s_K)b_abs,
    k_B=n0*11^4*k_M.
    M_beta(K)<=k_M, B_beta(K)<=k_B.                      (CA4)

A mark confines the row owner to N_5 of that mark, giving at most n0*11^4
scalar rows. The envelope already sums every colour and takes each entry's
supremum before summing. Periodic coincidences reduce support sizes and
incidences; no volume factor or diameter substitution is used.

For 0<=s<=1 put H_s=F_epsilon''(s b;V). Rebuild FU16's Hessian composition
by expanding each original local phase vertex first at a=0 and then inserting
the atoms of s b. Each inserted label meets the root at its field slot.
A mark belongs either to that root or to one inserted factor. The actual
finite-t/Haar vertex bounds therefore give, uniformly in s,

    Q_beta(H_s-K)<=D_H(s t_b,rho)<=d_H:=D_H(tau,rho),
    D_H(x,rho)=2d2 exp(beta s0){f''(x)-f''(0)+x f'''(x)
                               +rho[f''(x)+x f'''(x)]},
    f(x)=H(1-x/a)^(-q), q=(8L^4+8)D,
    s0=9^4, d2=q^2(9L^4+5)9^4.                          (CA5)

These are the already paid FU13--FU18 majorants. The first f'' difference
subtracts the source-free K; the source term retains rho f''(0). Equivalently
`H_s=K+H_epsilon+N_0'(s b)+N_epsilon'(s b)`, where
`H_epsilon=sum_p epsilon_p W_p''(0)` is present even at s=0. Kernel and
Haar Hessians are present in K and in the nonlinear derivatives. The
positive Taylor coefficients make the displayed majorant monotone. The
norm of each inserted s b is at most s t_b, and the entire segment lies
inside the common fine chart. No critical principal patch is declared local.

For clarity, the root mark costs f'' and an inserted-field mark costs
x f'''; differentiating twice leaves the q^2 root endpoint count in d2.
There are at most 9L^4+5 local phase vertices per block and a radius-four
reader collar with 9^4 possible roots through a mark. The source belongs to
its original plaquette coefficient. These counts prove CA5 with the same
complete labels as FU; substituted fields are not treated as new independent
data. Uniform absolute convergence also proves joint holomorphy. In particular

    M_beta(H_s)<=k_M+d_H, B_beta(H_s)<=k_B+d_H.           (CA6)

## 3. Exact scalar identity and the three marks

Fix u,V,epsilon while integrating s; neither b nor the kernel parameter
varies with s. For phi(s)=F_epsilon(s b;V), actual stationarity gives
phi'(1)=b^T F_epsilon'(b)=0. Twice integrating a scalar derivative gives

    F_epsilon(b)-F_epsilon(0)
       =-integral_0^1 s b^T H_s b ds.                   (CA7)

Indeed phi'(r)=-integral_r^1 phi''(s)ds, and interchanging the two finite
integrals gives weight s. This fixes the minus sign and factor 1/2 for a
constant Hessian. Only the sum of local first derivatives is stationary;
no individual vertex is assigned zero first derivative.

Expand both b factors and H_s into their actual coefficient families. Each
nonzero scalar contraction sums i,j with labels meeting at those endpoints,
so the union is connected and retains every original reader. For any matrix
family A and vector families h,k the scalar rooted norm obeys

    ||h^T A k||_beta
          <=[2M_beta(A)+B_beta(A)]V_beta(h)V_beta(k).     (CA8)

A mark in the left vector uses its incidence sum, A's row sum and the right
vector's component sum. A mark in A uses its full marked sum and the two
component sums. A mark in the right vector uses the left component sum,
A's column sum and the right incidence sum. Adding these three bounds gives
CA8. The sums include every scalar colour; no total-volume estimate is used.

Insert CA6 and integrate the complete coefficients in CA7. With
C_H=2k_M+k_B+3d_H, the resulting family is

    A_corr=[F_epsilon(b)-F_epsilon(0)]/sigma^2
          =sum_(connected S) a_S(V_S,epsilon_S),
    ||a||_beta<=C_H t_b^2/(2sigma^2)
              <=C_H tau^2/(8sigma^2).                  (CA9)

The majorant is uniform in s, hence integration and the coefficient sums
commute absolutely. The functions are holomorphic on the projected joint
domain and depend only on their original reader labels. This proves the
bounded producer corollary, not an estimate for an interacting measure.

## 4. The exact local lift action and its scalar vacuum

To eliminate normalizer notation ambiguities define explicitly

    z_t=int_SU(N) exp[-t(1-Re tr W/N)]dW, t=kappa u.      (CA10)

This is CB1's N_t(I), with probability Haar. [CB2--CB3](COVARIANT_SOFT_BACKGROUND_ASTRA.md)
show that every actual paired transporter at the lift equals V_c. Only the
fine plaquettes at a double-face intersection are nontrivial; each coarse
plaquette P occurs at exactly L^2 such fine plaquettes, denoted D(P).
Since j_N(0)=1, the exact lift action is

    F_epsilon(0;V)/sigma^2
       =sigma^-2 sum_(coarse P) sum_(p in D(P))
                       (1+epsilon_p) W(V_P)
          +4T^4 log z_t.                                (CA11)

For real V the kernel numerator is one and Haar invariance makes its
denominator z_t. The same identity holds on CA1 by holomorphic continuation
from each real coarse chart, without integrating over complex coarse data.
Every original epsilon_p remains individual. Sources on the other fine
plaquettes have zero lift value exactly; they still enter b and H_s in CA9.

For P near I, `2I-P-P^-1=-(P-I)^2P^-1` gives
`|W(P)|<=N delta_hat^2` when delta_hat<1/2. Assign each fine lift plaquette
term its radius-four original reader about the coarse plaquette root. At
most 6L^2*9^4 such roots/terms meet a fixed mark. Thus the field-dependent
part of CA11 has the explicit rooted budget

    C_W(1+rho)delta_hat^2/sigma^2,
    C_W=6N L^2 9^4 exp(beta 9^4).                        (CA12)

Its original-source vacuum alone costs C_W rho delta_hat^2/sigma^2 and
has not been absorbed into CA9. Assign 4 log z_t to each singleton block;
its rooted budget is 4 exp(beta)|log z_t|. It is kept at its exact real-u
value. The elementary bounds e^(-2t)<=z_t<=1 imply |log z_t|<=2kappa u;
no u-independent bound or asymptotic subtraction of this vacuum is claimed.

Consequently the full critical action has connected original-reader
coefficients at beta, with budget at most

    C_W(1+rho)delta_hat^2/sigma^2
      +4exp(beta)|log z_t|+C_H t_b^2/(2sigma^2).          (CA13)

## 5. Scale and consumer boundary

The constants in CA9 are fixed on the common FU domain, but sigma^-2=u/N
is explicit. This correction is generally not O(1/u). If one additionally
restricts the domain so t_b<=c sigma p, its budget is at most
`(C_H c^2/2)p^2`, which is not a small irrelevant remainder. If sigma p
shrinks with u, imposing that window is a further domain restriction; it
does not follow from FU's fixed positive complex tube. The real-slice
replacement delta_hat by delta_V cannot remove a fixed complex tube radius.

In CD20 or the matching SN30 identity one may now write exactly
`exp[-F_epsilon(b)/sigma^2]=exp[-F_epsilon(0)/sigma^2] exp[-sum_S a_S]`.
The first factor is CA11. The full determinant, h_N^n and
(2pi sigma^2)^(d/2) remain separate, as does the consumer's own small nonlinear
logarithm on its narrower regime. Weakening the present rate beta to a
consumer's beta/2 costs nothing; upgrading it to RD's two-unit margin does
not follow. No new assertion about SN's integral or its proof is used here.

This is bounded connected locality. Extracting relevant terms, proving a
renormalization contraction, matching history/reference normalizers,
returning the entire original cut and establishing effective-level dynamics
are separate obligations. There is no action/determinant cancellation,
new beta-function statement, multiscale existence theorem or physical gap.
Bałaban and Dimock retain architectural credit; the actual existing SA/IC/FU
steps are reused and their needed scalar composition is rebuilt above.
No external theorem is imported and no numerical physics is needed. Source
freeze precedes the compact read/identity packet and fresh independent review;
this author assigns neither an independent LAND nor a retained grade.
