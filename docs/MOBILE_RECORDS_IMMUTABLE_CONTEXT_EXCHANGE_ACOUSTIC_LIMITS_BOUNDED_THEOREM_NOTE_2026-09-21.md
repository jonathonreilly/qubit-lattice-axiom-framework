---
claim_id: mobile_records_immutable_context_exchange_acoustic_limits_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied seven-state nearest-neighbor exchange process on cubic tori, with immutable occupied labels, four-site collinear context, fixed bounded rates and a positive rate for every unequal-label swap: the displayed polarized feature 2n-3v_i^2 preserves every homogeneous product law, has the stated exact chemical-potential current, and has, for fixed alpha!=0, one nonzero direction-independent acoustic pair at every isotropic interior density, with four zero-speed modes. Given a smooth interior solution, the relative entropy per volume tends to zero on Euler time; microscopic per-label births beta/N give the stated reaction extension. In stationary full-support products without births, every finite collection of fixed Fourier modes and times converges in L2 to the full six-field linear current transport, yielding the stated cosine density covariance. The proofs retain all conserved fields and use canonical-block comparison and forward/reversed martingales. No finite-wave-number damping, nonstationary fluctuation theorem, nonlinear rotational invariance, quantum interpretation, physical clock, gravity or axiom-selected generator is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mobile_records_immutable_context_exchange_acoustic_limits_2026_09_21.py
---

# Immutable local exchanges support an isotropic acoustic limit at every interior density

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

A permanent record can move without changing its content, leaving room for a
fresh record. The construction here shows that such exchanges can also carry
collective density waves. A four-site context removes the density-specific
tuning needed by an occupation-only context. For fixed alpha!=0, the same rates
give a nonzero isotropic linear acoustic pair at every homogeneous density
strictly between zero and one. A separate microscopic fluctuation argument identifies the
long-wavelength density covariance, including the conserved modes outside
that acoustic pair.

This is a conditional mathematical model. The rate, alphabet interpretation
and clock are supplied. The formation extension is uniform per-label birth
at a declared scaling; it is a benchmark, not a derivation of the framework's
neighbor-dependent admissibility law. In particular, this note does not assert
that its selected seven-state process realizes all four minimal axioms.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "Can immutable records support a direction-independent propagating density sector as vacancies are filled, and does that sector correspond to a microscopic long-wavelength limit?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Check growing-product fluctuations and nonlinear rotational corrections while preserving the explicit rate and clock dependencies."
conditional_surface_status: "Positive local generator, exact product currents, all-density acoustic spectrum, conditional smooth-profile limit, and stationary finite-mode fluctuation limit."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit conditional proofs with separately reconstructed load-bearing calculations; no physical identification or primitive adoption."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. Supplied model and exact local identities

Use the torus Lambda_N=(Z/NZ)^3, N>=4. Each site has state 0 (vacancy) or one
of six immutable labels a=+/-e_j. Write v_a for that label vector and v_0=0;
n(a)=1 for an occupied label and n(0)=0. On a positive-i edge (x,x+e_i),
write (l,a,b,r) for the states at x-e_i,x,x+e_i,x+2e_i, and put

```
f_i(a)=v_(a,i),      s_i(a)=2 n(a)-3 f_i(a)^2,
h_i(l,a,b,r)=(alpha/2) {
   [f_i(a)-f_i(b)][s_i(l)+s_i(r)]
  +[s_i(a)-s_i(b)][f_i(l)+f_i(r)] }.
```

Choose either

```
c_i=kappa0+max(h_i,0),       kappa0>0,
c_i=K0+h_i/2,               K0>2|alpha|.
```

Alpha, kappa0 and K0 are fixed as N grows. The generator L_N sums
c_i(x,eta)[F(eta^(x,x+e_i))-F(eta)] over positive coordinate edges. An event
swaps the complete endpoint states. It neither redraws nor deletes a record.
The context has four sites; the update has two. There is at most one record
per site. These dynamics are additional assumptions, not axiom content.

The sharp local bound is |h_i|<=4|alpha|. One can check it over the finite
label alphabet; a coarser finite bound would also suffice for the limits.
Thus 0<c_*<=c_i<=c^* with constants independent of N. Equal-label events do
nothing; every unequal-label transposition has the positive floor.

Endpoint exchange changes the sign of h. For any two single-site functions
f,s, direct expansion and translation of the periodic sums give

```
sum_x {(f_x-f_(x+1))(s_(x-1)+s_(x+2))
      +(s_x-s_(x+1))(f_(x-1)+f_(x+2))}=0.
```

Since c_i(eta)-c_i(eta^edge)=h_i(eta), this is pointwise global balance.
A homogeneous product law gives equal weight to a configuration and any
endpoint swap, so every such product is invariant. This includes boundary
products as finite-volume invariant laws, although the limiting theorems
below require full support. Signed coordinate permutations transform f with
the edge direction and s with its axis; reversing the oriented edge also
reverses the four-site order. The physical rate is therefore covariant under
proper cubic rotations (and this particular choice has the larger signed
coordinate symmetry). The extra symmetry is not an added framework premise.

The construction uses only the lattice geometry and the uniqueness/permanence
portion of Record as motivation. It does not derive the label menu, a physical
qubit readout, a stochastic clock, or an admissibility distribution from
[the minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## 2. Product currents, entropy and the all-density spectrum

For six occupied probabilities p_a, put

```
rho=sum_a p_a,       p_0=1-rho,
g_i=sum_a p_a f_i(a),
q_i=p_(+i)+p_(-i),   S_i=2rho-3q_i.
```

Orient the microscopic species current from x to x+e_i:
j_a^i=c_i(eta)[1_(eta_x=a)-1_(eta_(x+e_i)=a)]. Its exact product mean is

```
J_a^i(p)=alpha p_a [S_i f_i(a)+(s_i(a)-2S_i)g_i],    a occupied,
J_0^i(p)=-2alpha p_0 S_i g_i.                              (1)
```

To derive (1), exchange the two endpoint labels in the product expectation.
The symmetric part of c drops out; averaging h/2 times the indicator
difference over the four independent labels gives the expression. Summing
all seven currents gives zero.

In chemical coordinates theta_a=log(p_a/p_0), the potential is
Psi_i=alpha S_i g_i. The categorical derivative of a single-site mean m is
partial_theta_a m=p_a[m(a)-m]. Thus partial_theta_a Psi_i=J_a^i. With

```
C(p)=diag(p)-p p^T,
A_i(p)=D_p J_i(p),
H(p)=C(p)^(-1)=diag(1/p_a)+(1/p_0)11^T,
```

we have A_i C=C A_i^T, and H A_i=A_i^T H. H is positive definite in the
interior. This is the entropy compatibility used in the smooth-profile
proof; it is not itself a microscopic limit theorem.

The exact density, vector and axis-occupation currents are

```
J_rho^i=2alpha p_0 S_i g_i,
J_(g_j)^i=alpha[delta_ij S_i q_i+(2-3delta_ij-2S_i)g_i g_j],
J_(q_j)^i=alpha g_i[delta_ij S_i+(2-3delta_ij-2S_i)q_j].     (2)
```

Let r_i=q_i-rho/3, with sum_i r_i=0. The identity
S_i q_i=rho^2/3-3r_i^2 cancels linear quadrupole coupling. At an isotropic
product p_a=rho/6, g=0, 0<rho<1, linearization gives

```
delta rho_t+2alpha rho(1-rho) div delta g=0,
delta g_t+(2alpha rho/3) grad delta rho=0,
delta r_i,t=0.                                             (3)
```

For every nonzero wave vector k the six-field matrix has eigenvalues
+/-c_s|k| and four zeros, where

```
c_s^2=4alpha^2 rho^2(1-rho)/3.                              (4)
```

For alpha!=0 the pair is nonzero at every interior density. The four zero
modes are two transverse vector modes and two traceless axis-occupation
modes. Positivity of C and entropy symmetry make the matrix diagonalizable;
these are not hidden Jordan modes. With alpha=1, densities 1/4,1/2,3/4 give
speeds 1/4,1/sqrt(6),sqrt(3)/4. All rates stay fixed as density varies.

The result is linear isotropy. On the slice q_i=rho/3 the exact vector-current
tensor is alpha[rho^2 I/3+2(1-rho)g g^T-3diag(g_i^2)]. The last term retains
nonlinear cubic-lattice anisotropy. Equations (3)-(4) do not establish full
nonlinear rotational invariance.

## 3. Smooth-profile theorem, including slow formation

Fix beta>=0. On macroscopic time the process has generator N L_N+R_N,
where R_N forms each occupied label at rate beta at a vacant site. Equivalently,
the microscopic per-label birth rate is beta/N. Suppose p(t,X) is a given
C^2 periodic solution on [0,T] of

```
partial_t p_a+sum_i partial_i J_a^i(p)=beta p_0,              (5)
```

and all seven probabilities are at least a fixed eta>0. Let nu_t^N be the
product with marginals p(t,x/N). If H(mu_0^N|nu_0^N)=o(N^3), then

```
sup_(t<=T) H(mu_t^N|nu_t^N)/N^3 -> 0.                       (6)
```

At every fixed t, each empirical species profile tested against a continuous
function converges in probability to the prescribed profile. Smoothness and
the interior bound are hypotheses; no global solution or shock-selection
claim is made. This theorem does not imply a central-limit-scale statement.

Here is a proof specialized to the actual context rates. Write V=N^3 and
let pi_N be the uniform seven-state product. With f_t=dmu_t/dpi_N, define
D_N(f)=sum_e E_pi[(sqrt(f^e)-sqrt(f))^2]. Stationarity of pi_N for exchanges,
the rate floor and the elementary logarithmic inequality give

```
dH(mu_t|pi_N)/dt <= -N c_* D_N(f_t)+beta V,
integral_0^T D_N(f_t)dt <= V(log7+beta T)/(N c_*).           (7)
```

For the birth term, R_N^*1 is beta at an occupied state and -6beta at a
vacancy, summed over sites; this supplies the upper bound beta V.

Take a fixed cube B_l with M=(2l+1)^3 sites and N>4l. Given its seven counts,
the uniform reference is uniform over all arrangements. Internal adjacent
transpositions connect each sector. A finite Poincare constant A_l, uniform
over the finitely many sectors, therefore satisfies
E Var(sqrt(g_B)|counts)<=A_l D_B(g_B) for any marginal density g_B. Replacing
the marginal by its count-conditioned uniform arrangement changes its L1
law by at most 2 sqrt(2 A_l D_B(g_B)): condition sectorwise, use the squared
Hellinger estimate, then Cauchy-Schwarz. Marginalization contracts the swap
energy, by the reverse triangle inequality for outside L2 norms. Summing
translated blocks counts each edge at most M times.

For the reverse current j_i^rev=c_i(eta^edge)(xi_x-xi_(x+e_i)), the product
mean is -J_i. Average it over the anchors whose four-site footprints lie
inside B_l, normalizing by the number of anchors. Sampling a fixed r-site
observable without replacement from a block differs from product sampling
at its empirical frequencies q by at most r(r-1)/(2M). For two disjoint
four-site footprints the same coupling, now on at most eight positions,
bounds the covariance by O(1/M); overlapping pairs are only O(M) among O(M^2)
pairs of anchors. Thus the canonical block-average variance is O(1/M), and
its mean is -J_i(q)+O(1/M), uniformly even for boundary count vectors.
Combining this with (7) and the marginal comparison yields

```
V^(-1) integral_0^T sum_x E_mu |bar j_i^rev(x)+J_i(q_l(x))|dt
 <= C T/sqrt(M)+C sqrt(A_l T M(log7+beta T)/(N c_*)).        (8)
```

All constants except A_l are uniform in l,N. First send N to infinity at
fixed l, then send l to infinity. This is the local-equilibrium step; an
inhomogeneous product law has not been assumed to stay product.

For theta=log(p/p_0), psi=dnu_t^N/dpi_N and H_N=H(mu_t^N|nu_t^N), the Markov
relative-entropy inequality is

```
H_N' <= E_mu[(N L_N^*+R_N^*)psi/psi-partial_t log psi].      (9)
```

The swap ratio is exp[(theta_(x+e_i)-theta_x).(xi_x-xi_(x+e_i))]. Pointwise
balance cancels its zeroth-order adjoint term. Smooth expansion leaves
sum_(x,i) partial_i theta . j_i^rev+O(V/N). Exactly,
partial_t log psi=sum_x theta_t.(xi_x-p_x). The part generated by births
cancels R_N^*psi/psi pointwise: both are beta p_0/p_a at occupied label a
and -6beta at vacancy, summed over sites.

For the transport part, theta_t=-sum_i A_i^T partial_i theta, by the entropy
identity. Move the smooth coefficients over blocks at cost O(lV/N), use (8),
and Taylor-expand J_i(q_l) about p_x. The constant term is the Riemann sum of
-sum_i partial_i Psi_i, whose torus integral is zero. Its error is O(V/N).
The terms linear in q_l-p_x cancel. Bounded current Hessians leave at most
C sum_x |q_l(x)-p_x|^2.

Under nu_t^N the sites are independent. Hoeffding and a union bound give
P(M|q_l-Eq_l|^2>z)<=12 exp(-z/3), hence a uniformly bounded exponential
moment for a sufficiently small positive coefficient. The translated cubes
have an overlap graph of degree O(M); color it with O(M) colors and use
Holder across colors and independence within each color. Since the block
mean differs from p_x by O(l/N), this yields, for a sufficiently small fixed a>0,

```
log E_nu exp[a sum_x |q_l(x)-p_x|^2] <= C V/M+C V l^2/N^2,
E_mu sum_x |q_l(x)-p_x|^2 <= a^(-1)H_N+C V/M+C V l^2/N^2.   (10)
```

The coefficient a is independent of l. Equations (8)-(10) give
H_N(t)/V<=H_N(0)/V+C integral_0^t H_N(s)/V ds+C_T/sqrt(M)+C_T/M+o_N(1).
Gronwall with N first and l second proves (6). Product concentration of
empirical test averages and the binary-event entropy inequality transfer
the profile convergence from nu_t^N to mu_t^N. Uniform approximation covers
continuous test functions. This completes the stated fixed-time consequence.

## 4. Stationary microscopic Fourier-fluctuation theorem

Now set beta=0 and start the actual process in a fixed full-support
homogeneous product pi_p, with p independent of N. Fix T<infinity and
K=2pi m for a fixed nonzero m in Z^3. On macroscopic time define

```
Y_N(K,t)=V^(-1/2) sum_x exp(-i K.x/N)[xi_x(t)-p],
A(K)=sum_i K_i A_i(p),       U_K(t)=exp[-i A(K)t].
```

Then

```
sup_(t<=T) E|Y_N(K,t)-U_K(t)Y_N(K,0)|^2 -> 0.              (11)
```

The supremum is outside expectation. Equation (11) also holds jointly for
any finite list of fixed modes and times. In particular,

```
E[Y_N(K,t)Y_N(K,s)^*] -> U_K(t-s) C(p),       t>=s.         (12)
```

At p_a=rho/6 the microscopic density covariance therefore satisfies

```
E[Y_rho,N(K,t) overline(Y_rho,N(K,0))]
 -> rho(1-rho) cos(c_s |K|t).                               (13)
```

This is a correlation limit of the microscopic process, not merely a current
spectrum. The proof follows, separately from the smooth-profile argument.

Let S_N=(L_N+L_N^*)/2 in L2(pi_p). Reverse exchange rates are c(eta^edge),
and D_S(u)=-<u,S_N u> >= (c_*/2)sum_e E|u^e-u|^2. The kernel consists of
functions of global counts: the positive floor connects every arrangement
of a multiset. For F centered on each count sector, solve -S_N u=F.
Forward and reversed stationary martingales on [0,t] satisfy

```
M_t+Mhat_t=2N integral_0^t F(eta_s)ds,
E|M_t|^2=E|Mhat_t|^2=2Nt D_S(u).
```

Consequently

```
E|integral_0^t F(eta_s)ds|^2 <= (2t/N)||F||_(-1,S_N)^2,    (14)
||F||_(-1,S_N)^2=sup_u {2 Re<F,u>-D_S(u)}.
```

No reversibility of L_N or sector-condition hypothesis is needed. The
reversed martingale need not be independent of the forward martingale.

For a scalar component j of a local current, take a fixed block of M sites
containing its footprint and set hat j=E[j|block counts], h=j-hat j. This
conditional law is the uniform arrangement law; hat j is independent of the
product parameter. Fixing the outside and the block counts fixes the global
counts, so h is orthogonal to the kernel above. The canonical Poincare
inequality and Cauchy-Schwarz, followed by counting translated-block overlaps,
give for F_N=V^(-1/2)sum_x a_x tau_x h, |a_x|<=1,

```
|<F_N,u>| <= C sqrt(A_l M/c_*) sqrt(D_S(u)),
||F_N||_(-1,S_N)^2 <= C A_l M/c_*.                          (15)
```

Indeed each summand is bounded by C sqrt(A_l times its internal swap
energy); after the normalization V^(-1/2), Cauchy-Schwarz over anchors
leaves the sum of block energies, with each edge counted at most M times.
Equations (14)-(15) make the integrated conditional residual O(A_l M/N)
in second moment at fixed block size.

Sampling without replacement gives hat j=J(q)+O(1/M), uniformly in the
block frequencies q. The Taylor residual
W=hat j-J(p)-DJ(p)(q-p) has exact product mean zero and
E|W|^2<=C/M^2, using the fourth moment of independent categorical samples.
Translated residuals on disjoint blocks are independent at a fixed time,
with only O(M) overlapping blocks. Thus the variance of their normalized
spatial sum is O(1/M). Stationarity and time Cauchy-Schwarz give integrated
second moment O(T^2/M), without assuming time independence.

For the Fourier coefficients a_x, the Fourier transform of q-p equals
phi_l(K/N)Y_N, with |phi_l-1|<=C_K l/N. The instantaneous product covariance
of Y_N is exactly C, so replacing that block field costs O(T^2 l^2/N^2).
The constant current cancels because the nonzero Fourier phases sum to zero
for sufficiently large N. Hence, for Z_i,N=V^(-1/2)sum_x a_x j_i(x),

```
sup_(t<=T) E|integral_0^t [Z_i,N(s)-A_i Y_N(s)]ds|^2
 <= C_T [A_l M/(N c_*)+1/M+l^2/N^2].                        (16)
```

This is the first-order current replacement required at fluctuation scale.
A relative-entropy error o(V) alone would not supply it. No unaveraged
current is equated pointwise with its mean.

Microscopic conservation gives exactly

```
Y_N(t)=Y_N(0)+sum_i b_i,N integral_0^t Z_i,N(s)ds+M_N(t),
b_i,N=N[exp(-i K_i/N)-1] -> -iK_i.                         (17)
```

A swap changes Y_N by O(1/(N sqrt(V))), while the accelerated total rate is
O(NV); thus E tr<M_N>_T<=C_T/N. Let B_N=sum_i b_i,N A_i. Variation of
constants uses exp[B_N(t-s)], uniformly bounded with its derivative for
fixed T. The martingale convolution vanishes in L2. For each cumulative
current error X_i,N(t)=integral_0^t[Z_i,N-A_iY_N]ds, integration by parts
bounds the weighted error by X_i,N(t) plus a bounded time integral of
X_i,N(s). Equation (16), first N then l, makes it vanish uniformly in t
in L2. Since B_N->-iA(K), this proves (11).

The independent bounded initial site variables obey the Lindeberg central
limit theorem for every finite collection of Fourier modes. Their covariance
is C when integer modes agree, zero otherwise; the nonconjugated covariance
pairs opposite modes. Transport by (11) gives the finite-mode, finite-time
Gaussian limit. Since A_i C=C A_i^T, U_K C U_K^*=C. This proves (12), and
solving the two longitudinal equations (3) proves (13). The four zero-speed
fields are retained in C and U_K. They are static on this leading time scale,
not fixed microscopic trajectories.

## 5. Continuing formation and the limits that must stay distinct

For a homogeneous initial product and uniform microscopic per-label rate
epsilon, the law stays product exactly:

```
p_0(t)=p_0(0)exp(-6epsilon t),
p_a(t)=p_a(0)+p_0(0)[1-exp(-6epsilon t)]/6.
```

An initially isotropic product remains on the all-density sector of (3),
but its coefficients change. On Euler time and epsilon=beta/N the formal
linear response has density drift -6beta delta rho in addition to the
time-dependent acoustic operator. The smooth-profile theorem covers that
reaction scaling. The stationary fluctuation theorem does not cover births;
it cannot justify dropping formation noise or fitting one stationary speed.
A separate growing-product fluctuation proof is outside this claim.

At a fixed positive microscopic epsilon, p_0(Nt) vanishes for each positive
fixed macroscopic t as N grows. This is a different limit. Similarly, the
stationary theorem fixes p,T,K and the swap floor before N grows: it does
not give a rate uniform in growing times or modes, densities approaching the
simplex boundary, or a vanishing floor. It gives no finite-wave-number
damping coefficient, nonlinear wave theorem, infinite-dimensional path
result, or identification with a relativistic or quantum field.

The supplied parameters, current potential, label interpretation and clock
remain open physical choices. This construction resolves a mathematical
compatibility question about immutable transport. It does not select a TOE.

## 6. Evidence, independent checks and prior-art boundary

The primary runner checks the microscopic rate and exact product-current
identities, cubic covariance, complete linear field matrix and limiting
normalizations. Finite enumeration and symbolic matrices support those
steps; the general limiting conclusions rest on the proofs above.

Before access to the primary arguments, one existing checker reconstructed
three relevant units with different proof/implementation paths: the context
current and entropy algebra; smooth-profile convergence with a forward-current
entropy argument and an explicit crude canonical Poincare bound; and the
stationary Fourier fluctuation limit with spatially averaged canonical
currents and nonreversible martingale bounds. Its all-density feature check
also verified applicability of the smooth-profile proof. The reports, exact
source identities, full outputs and failed development attempts are preserved
in the [evidence index](../.claude/science/mobile-record-immutable-waves-20260921/INDEPENDENT_CAPSULES.json).
The [all-density report](../.claude/science/mobile-record-immutable-waves-20260921/independent_axis_balanced_context_REPORT.md),
[smooth-profile report](../.claude/science/mobile-record-immutable-waves-20260921/independent_context_euler_REPORT.md)
and [stationary fluctuation report](../.claude/science/mobile-record-immutable-waves-20260921/independent_context_fluctuations_REPORT.md)
are also available as readable exact copies. The zip capsules preserve the
raw sealed logs byte-for-byte, including interrupted attempts. Agreement is
not a formal audit.
Final publication-source confirmation is a separate gate.

The relative-entropy and fluctuation methods are established mathematics.
[Toth and Valko](https://arxiv.org/abs/math/0210426v2) provide relevant
multi-conservation-law context; their displayed endpoint-rate theorem is
not directly imported for these context rates. [Wu's forward/backward
martingale article](https://www.numdam.org/item/AIHPB_1999__35_2_121_0/)
and [Olla and Xu's Euler fluctuation paper](https://arxiv.org/abs/1808.00306v3)
provide methodological context. The model-specific hypotheses and estimates
needed here have been proved explicitly. No novelty claim is made for those
methods or for hydrodynamic limits in general.

## Reproduction

```bash
python3 scripts/mobile_records_immutable_context_exchange_acoustic_limits_2026_09_21.py
python3 scripts/mobile_records_immutable_context_exchange_acoustic_limits_2026_09_21.py --list-mutations
python3 .claude/science/mobile-record-immutable-waves-20260921/verify_capsules.py
```

The runner requires NumPy and SymPy. Raw campaign simulations are not theorem
premises and are not used to set the speed in (4). No main merge, axiom change,
editable prompt change or independent audit verdict is part of this packet.
