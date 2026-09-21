# Independent equilibrium Euler fluctuation check

**Result.** The proposed limit holds for both supplied conservative generators
at every fixed full-support homogeneous product law, for fixed Fourier modes
and fixed finite time intervals. The load-bearing estimate is a first-order
equilibrium current replacement. A block argument and forward/backward
martingales prove it for these nonreversible rates without a sector-condition
assumption. This result is independently derived here; it is not inferred from
the previously checked smooth-profile hydrodynamic law.

No new primary fluctuation source or outcome was read before this report was
sealed. The finite controls below support particular identities and
normalizations; the asymptotic conclusion rests on the proof.

## 1. Precise statement and hypotheses

Let Lambda_N = (Z/NZ)^3, V=N^3, and let H_N exchange endpoint states across all
nearest-neighbor bonds. There are seven states, one vacancy and six occupied
labels. The following hypotheses suffice:

1. The rates are translation covariant, have a fixed finite dependence range,
   are bounded above by a constant independent of N, and are independent of N
   apart from their periodic interpretation.
2. Every transposition of unequal endpoint states has rate at least delta>0,
   uniformly over configurations, bonds and N. All colors can be exchanged;
   no vacancy-only or other constrained exchange rule is substituted.
3. The homogeneous product law pi_p is invariant, where all seven
   probabilities are strictly positive and p does not vary with N.
4. The process starts in pi_p, has no births, and is observed with generator
   N H_N. Parameters, a finite time horizon T, and the integer Fourier modes
   are fixed as N tends to infinity.

Pure exchanges preserve the probability of every configuration under every
homogeneous product law. Consequently, pointwise invariance for one
full-support homogeneous product law implies invariance for all such products:
the stationarity identity after division by the product weight is
sum_e [c_e(eta^e)-c_e(eta)]=0, which does not contain p. In particular the local
current expectation J_i(q) is a finite polynomial on the probability simplex,
and can be differentiated in a neighborhood of the chosen p.

Write xi_x=(1_{eta_x=a})_{a=1}^6 and orient the current as

    j_i(x,eta) = c_{x,i}(eta) [xi_x-xi_{x+e_i}],
    J_i(q) = E_{pi_q} j_i(0),       A_i = D J_i(p).

Set C=diag(p)-p p^T, K=2 pi m for a fixed nonzero m in Z^3,
A(K)=sum_i K_i A_i, and U_K(t)=exp[-i A(K)t]. All vector L2 norms below use
the stationary path measure. Then

    sup_{0<=t<=T} ||Y_N(K,t)-U_K(t)Y_N(K,0)||_2 -> 0.       (1)

The supremum in (1) is outside the L2 norm. A maximal sample-path statement
with E sup_t |error(t)|^2 is not asserted. Equation (1) implies L2 convergence
of the vector of errors at any finite selection of modes and times.

For the complex fields the precise two-time covariance is

    E[Y_N(K,t) Y_N(K,0)^*] -> U_K(t) C.                    (2)

The star is conjugate transpose. Without conjugation, the corresponding
nonzero covariance pairs K with -K. This distinction is essential for nonzero
Fourier modes.

For M=ell^3 and a sufficiently large odd ell with N>4 ell, the proof gives

    sup_{t<=T} ||Y_N(K,t)-U_K(t)Y_N(K,0)||_2
      <= C_{T,K,p} [N^(-1/2) + ell/N + M^(-1/2)
                                  + sqrt(M^3 7^M/N)].    (3)

Constants also depend on the fixed local rates, range and floor, but not N
or ell. Choose ell tending to infinity with ell^3 <= log(N)/(2 log 7).
Every term vanishes. The crude block bound suffices; no optimized mixing-rate
claim is needed.

## 2. Applicability to the two actual generators

Both previously checked generators belong to the family

    f_i(a)=v_a dot e_i,       s_i(a)=A n(a)+B f_i(a)^2,
    h_i(l,a,b,r)=u[f_i(a)-f_i(b)]
       + E{[f_i(a)-f_i(b)][s_i(l)+s_i(r)]
              +[s_i(a)-s_i(b)][f_i(l)+f_i(r)]}.

Their rates are either K_0+h_i/2, with a sufficiently large fixed K_0, or
kappa_0+max(h_i,0), with kappa_0>0. The four positions on a coordinate line
are distinct when N>=4. In both cases c_i-c_i^swap=h_i, and the previously
proved periodic telescoping identity sum_{x,i} h_i(x)=0 gives homogeneous
product invariance. The alphabet and context are finite, so the assumed
positive floor also gives fixed finite bounds on all rates. The positive-part
choice need not be differentiable in parameters: its product expectation is
still a polynomial in probabilities.

For occupied label a, put

    rho=sum_a p_a,  m_i=sum_a p_a f_i(a),
    sigma_i=sum_a p_a s_i(a),
    U_i=u+2E sigma_i,          Z_i=u+4E sigma_i.

The imported, previously checked current is

    J_a^i(p)=p_a[U_i f_i(a)+(2E s_i(a)-Z_i)m_i].           (4)

Both rate implementations have this same mean current, since the symmetric
part under endpoint interchange contributes zero to its product expectation.
The earlier context model is A=1,B=0. The all-density axis-balanced witness is
u=0,E=1/2,A=2,B=-3. The proof in Sections 3-6 uses the actual exchange rates,
including their symmetric part; equality of fluxes alone would not suffice.

The prior nonlinear entropy identity gives

    S = diag(1/p_a) + (1/p_0) 11^T = C^(-1),
    S A_i = A_i^T S,          A_i C = C A_i^T.             (5)

This identity will check and interpret the stationary covariance. It is not
used to replace the nonreversible process by a reversible process.

## 3. Nonreversible additive-function estimate

Use the stationary L2 inner product, with conjugation in the first argument.
The adjoint H_N^* is a Markov generator with reverse exchange rates
c_e(eta^e). Let S_N=(H_N+H_N^*)/2. Its Dirichlet form satisfies

    E_S(h):=-<h,S_N h> >= delta E_0(h),
    E_0(h)= (1/2) sum_e E_{pi_p}|h(eta^e)-h(eta)|^2.      (6)

On each global count-vector sector the exchange floor makes the process
irreducible: adjacent transpositions connect every permutation of a multiset
on the connected torus. The kernel of S_N is therefore exactly the functions
of the six total occupied counts.

Let F have zero mean on every sector, and solve -S_N h=F sectorwise. Forward
and stationary time-reversed martingales over the interval [0,t] give

    M_t + Mhat_t = 2N integral_0^t F(eta_{Ns}) ds.

Each martingale has squared L2 norm 2Nt E_S(h). Thus, for complex or real F,

    E |integral_0^t F(eta_{Ns}) ds|^2
       <= (2t/N) <F,(-S_N)^(-1)F>.                       (7)

This follows directly from |M+Mhat|^2<=2|M|^2+2|Mhat|^2. Time reversal is
used only at a fixed interval endpoint; no independence between the two
martingales is required. Equation (7) concerns the original nonreversible
stationary path law. It neither assumes a strong sector condition nor replaces
its dynamics by S_N.

## 4. First-order equilibrium current replacement

The argument applies to each scalar component g of a local current. Let
B_ell be a cube of M=ell^3 sites containing the fixed support of g, and let
I_ell be the set of anchors y for which the entire support of g(translate_y eta)
is inside this cube. Define

    G_ell = |I_ell|^(-1) sum_{y in I_ell} g(translate_y eta),
    q^ell = M^(-1) sum_{y in B_ell} xi_y,
    Phi_M(q^ell) = E[G_ell | block counts],
    Gtilde_ell = G_ell-Phi_M(q^ell).

Normalizing the anchor average by |I_ell|, rather than M, avoids a spurious
boundary loss at fluctuation scale. Given the block counts, sites in the
block are uniformly exchangeable. Every interior anchor has the same
conditional current mean, so Phi_M is also the conditional mean of one copy
of g. The residual Gtilde_ell is bounded and conditionally centered.

### 4.1 The fast conditional residual

A deliberately crude canonical Poincare constant for the M-site cube is

    Var_canonical h <= P_M E_{0,B_ell}(h),
    P_M = 2 M^2 7^M.                                    (8)

One proof orders sites along a nearest-neighbor Hamiltonian path through the
cube. Any two arrangements with the same counts are connected by at most
M^2 adjacent swaps. There are at most 7^M arrangements. Apply Cauchy-Schwarz
to the difference along each such path and sum over ordered pairs of
arrangements. Comparing with the uniformly weighted unit-exchange Dirichlet
form gives (8), with slack in the stated constant. Empty or singleton sectors
have zero variance and cause no exception.

For the translated, normalized field

    F_{N,ell} = V^(-1/2) sum_x exp(-iK.x/N)
                                      Gtilde_ell(translate_x eta),

conditional centering implies orthogonality to every global count function.
For any test h, condition on the outside of each block and its count vector.
The conditional law inside the block is canonical. Cauchy-Schwarz and (8)
give

    |<F_{N,ell},h>| <= C sqrt(P_M M E_0(h)).              (9)

In detail, each summand is at most C sqrt(P_M E E_{0,B_x}(h)); after the
factor V^(-1/2), Cauchy-Schwarz over x leaves the square root of
sum_x E E_{0,B_x}(h). Each global bond belongs to at most M translated
blocks, giving the factor M in (9). Combining (6), the variational definition
of the inverse-form norm, and (7),

    sup_{t<=T} ||integral_0^t F_{N,ell}(eta_{Ns}) ds||_2
          <= C_T sqrt(M^3 7^M/N).                       (10)

This is the only dynamical mixing estimate needed. It applies to the
context-dependent and positive-part rates without an endpoint-only-rate
assumption.

### 4.2 The slow conditional mean and its linear projection

If g has r distinct support sites, sampling these sites from a population
of M sites without replacement can be coupled to independent sampling with
replacement. The chance of repeated population indices in the latter is
at most r(r-1)/(2M). Uniformly over block count vectors,

    |Phi_M(q)-J(q)| <= C/M,                              (11)

where J(q)=E_{pi_q}g. The polynomial J has a bounded Hessian on the closed
simplex. Set

    R_M(q) = Phi_M(q)-J(p)-DJ(p)(q-p).

Taylor's formula and (11) give |R_M(q)|<=C/M+C|q-p|^2.
Under the stationary product law the block counts are multinomial, so

    E |q^ell-p|^4 <= C/M^2,
    E |R_M(q^ell)|^2 <= C/M^2,
    E R_M(q^ell) = 0.                                  (12)

The final equality is exact: E Phi_M=J(p) and E q^ell=p. Residuals on
disjoint blocks are independent. A block overlaps at most C M translates,
so

    ||V^(-1/2) sum_x exp(-iK.x/N) R_M(q^ell(x))||_2
         <= C/sqrt(M).                                 (13)

Stationarity gives the same bound, multiplied by T, for its time integral.
Discarding the linear projection instead of retaining it would generally
leave variance of order 1/M and would not give (13) with a vanishing bound.

### 4.3 Spatial averaging at the correct scale

Define the centered Fourier current field

    G_N(K)=V^(-1/2) sum_x exp(-iK.x/N)[g(translate_x eta)-J(p)].

Product independence outside a fixed distance gives ||G_N(K)||_2<=C,
uniformly in N. Let

    a_{N,ell}=|I_ell|^(-1) sum_{y in I_ell} exp(+iK.y/N),
    b_{N,ell}=M^(-1) sum_{y in B_ell} exp(+iK.y/N).

Translation of the sums shows exactly that the Fourier fields of
G_ell-J(p) and q^ell-p are a_{N,ell} G_N and b_{N,ell}Y_N, respectively.
Both filter errors |a-1| and |b-1| are at most C_K ell/N. Consequently,

    G_N-DJ(p)Y_N
      = (1-a)G_N + F_{N,ell} + DJ(p)(b-1)Y_N
          + V^(-1/2) sum_x exp(-iK.x/N)R_M(q^ell(x)).     (14)

The identity uses the fact that the sum of the nonzero Fourier phases is
zero, true for all sufficiently large N at fixed nonzero m. Combining
(10), (13), stationarity and the uniformly bounded variances of G_N,Y_N,

    sup_{t<=T} ||integral_0^t [G_N(K,s)-DJ(p)Y_N(K,s)] ds||_2
       <= C_{T,K}[ell/N + M^(-1/2)
                                      + sqrt(M^3 7^M/N)].              (15)

A uniform-in-configuration spatial averaging estimate would give the wrong
scale: its error can be of order sqrt(V) ell/N=ell sqrt(N) in dimension
three. The stationary L2 bound and exact Fourier filters in (14) avoid that
failed route. Likewise, an entropy error of o(V) from a hydrodynamic theorem
alone does not provide this central-limit-scale estimate.

## 5. Martingale conservation identity and the limit

Conservation holds configuration by configuration:

    H_N xi_x = sum_i [j_i(x-e_i)-j_i(x)].

With the specified negative Fourier exponential, the drift is therefore

    N H_N Y_N(K) = sum_i d_i^N(K) G_{i,N}(K),
    d_i^N(K)=N[exp(-iK_i/N)-1]=-iK_i+O_K(N^(-1)).        (16)

A single exchange changes the field by at most C_K/(N sqrt(V)). The total
accelerated jump rate is at most C N V. The current-field martingale M_N
thus satisfies

    E sup_{t<=T}|M_N(t)|^2 <= C_{T,K}/N.                 (17)

Apply (15) to all six components of each of the three currents and use
(16). The martingale identity becomes

    Y_N(K,t)=Y_N(K,0)-i A(K) integral_0^t Y_N(K,s) ds
                                       + M_N(t)+R_N(t),

where sup_{t<=T}||R_N(t)||_2 tends to zero with the last three terms in
(3), plus an O(N^(-1)) drift-discretization error. Subtract the corresponding
integral equation for U_K(t)Y_N(K,0). Minkowski's inequality and Gronwall's
inequality give (3) and (1). There is no additional hydrodynamic or
Boltzmann-Gibbs theorem imported into this step: (15) is that replacement
estimate proved directly for the stated generators.

## 6. Stationary Gaussian limit and covariance

Under the initial product law,

    E Y_N(K,0)Y_N(L,0)^* = C 1_{m=n mod N}.

The nonconjugated covariance instead pairs m=-n modulo N. At finitely many
fixed modes there are no accidental aliases for sufficiently large N.
The elementary Lindeberg central limit theorem for the bounded independent
site variables gives the joint initial complex Gaussian limit, with the
reality constraint Y(-K)=overline{Y(K)}. Equation (1) then gives the joint
finite-mode, finite-time Gaussian limit

    Y(K,t)=U_K(t)Y(K,0).

In particular, Cauchy-Schwarz and (1) prove (2) directly, whether or not
Gaussianity is invoked. Equation (5) implies

    U_K(t) C U_K(t)^* = C,
    E[Y(K,t)Y(K,s)^*] = U_K(t-s) C.                     (18)

The same symmetrization is forced by product stationarity for the general
class in Section 1, rather than being an independent hidden hypothesis:
differentiate the product expectation of j_i with respect to the six
chemical potentials. The result is the sum over its finite support of
Cov(j_i,xi_y), equal to A_i C. As N tends to infinity,
E[G_{i,N}(K)Y_N(K)^*] tends to this matrix. Stationarity of
E[Y_N(K)Y_N(K)^*], (16), and the O(N^(-1)) jump bracket then give
A(K)C=C A(K)^T. Taking the coordinate Fourier modes yields (5).
For the two supplied models the previously proved entropy formula is a
separate direct verification.

The invariant product has six fluctuating conserved color counts, not just
a scalar population. A flux eigenvalue of zero means no transport of that
linear combination on this Euler scale; it does not say its microscopic
trajectory is fixed.

## 7. Meaning of the tuned acoustic formulas

This theorem applies at any full-support p, with the full six-by-six
directional matrix A(K). A direction-independent acoustic interpretation
requires the additional isotropic density and tuning conditions previously
derived; it is not a general property at arbitrary p.

At p_a=rho/6, 0<rho<1, let q_i=p_{+i}+p_{-i} and
m_i=p_{+i}-p_{-i}. In the all-density family u=0, B=-3A/2, EA!=0,
or in the old family A=1,B=0 tuned at the chosen density by u=-2E rho,
the longitudinal population/momentum block is

    A_ac(K)=|K| [[0, a], [b, 0]],
    a=2g rho(1-rho),    b=2g rho/3,
    c^2=ab=4g^2 rho^2(1-rho)/3.                        (19)

Here g=EA for the all-density family and g=E for the old tuned family.
The positive speed is c=sqrt(ab); g can have either nonzero sign. The two
propagating eigenvalues are +/-c|K|. There are four zero eigenvalues:
two population anisotropies with sum_i q_i=0 and two moment components
transverse to K. Because C is positive definite and (5) holds, these modes
are semisimple. Omitting them would give the wrong full species covariance.

For the total population field and m_parallel=(K/|K|) dot m, initial
variances are rho(1-rho) and rho/3, with zero cross covariance. Thus (18)
implies, for example,

    lim E[Y_rho(K,t) overline{Y_rho(K,0)}]
         = rho(1-rho) cos(c|K|t).                      (20)

For the fixed witness u=0,E=1/2,A=2,B=-3, g=1 and this formula holds for
every fixed interior rho. In the old model u=-2E rho is a tuning at one
chosen density when u,E are held fixed. The stationary long-wavelength
Euler fluctuation limit is therefore a precise meaning of its acoustic
formula, with all six conserved fields retained.

Equation (20) is not an exact finite-N wave, a nonlinear microscopic wave
theorem, or a statement about damping, broadening or fresh noise on longer
time scales. In this limit the randomness is carried by the initial
Gaussian fluctuation field; (17) makes the Euler-scale dynamic martingale
vanish. No quantum or physical-field identification follows from this
mathematical statement.

## 8. Independent finite controls and failed routes

Run `python3 independent_check.py > RUN.log 2>&1` in this directory. The
completed runner records **75 checks passed, zero failed** in RESULTS.json;
RUN.log is byte-identical to that full JSON output. These checks were written
independently of the primary argument and runner.

1. Four 24-state canonical generators on a four-cycle use the actual rates
   from both models and both rate implementations. The multiset is
   (vacancy,+e1,+e2,-e2). Exact arithmetic confirms stationarity, positive
   rates, genuine nonreversibility, the negative-Fourier conservation sign,
   and the symmetric Poisson equation. Matrix exponentials then check (7)
   at three times. For example the old linear-rate control has
   <F,(-S)^(-1)F>=193/192; at accelerated rate 4 and t=1 the integrated
   variance is approximately 0.484536504, below the bound 193/384.
   This is a directional finite algebra control, not a replacement of the
   three-dimensional theorem by a one-dimensional model.
2. For each rate implementation, direct enumeration over all 7^4 local
   strings agrees with the exact canonical current formula at two count
   vectors. If M sites have empirical means m=<f>, sigma=<s>, tau=<fs>,
   conditional on endpoint label a let
   F=(Mm-f_a)/(M-1), S=(M sigma-s_a)/(M-1), and
   T=[(Mm-f_a)(M sigma-s_a)-(M tau-f_as_a)]/[(M-1)(M-2)].
   The checked formula is
   Phi_{M,a}=q_a{u(f_a-F)+2E[f_a S+s_a F-2T]}.
3. Exact multinomial moments check the conditional projection at rho=1/2
   for M=8,16,32,64. For the +e1 current, the four transverse colors can
   be grouped for this calculation because the observable is unchanged
   by their permutations. The grouped gradient is (1/4,1/12,1/6) in
   both chosen models. The residual is exactly centered and orthogonal
   to all three count deviations. Its variance times M^2 decreases from
   89/756 to 4846/52731 for the old model and from 134/567 to 3400/17577
   for the axis-balanced model. The linear part has variance exactly
   7/(864 M), showing concretely why it cannot be discarded.
4. Exact six-field matrices at isotropic and biased full-support densities
   verify A_i C=C A_i^T. At rho=1/2, K=2 pi(1,2,-1), the two tuned models
   have the same Jacobians, rank(A(K))=2, and A(K)^3=4 pi^2 A(K).
   Exact covariance transport gives total-population covariances
   sqrt(2)/8 and 0 at t=1/8 and t=1/4, respectively.
5. The constant-rate subfamily u=E=0 supplies an exact full
   three-dimensional control. With exchange rate kappa, its Fourier
   covariance is exp[-kappa N omega_N(K)t] C on the Euler scale, where
   omega_N=2 sum_i[1-cos(K_i/N)]. Since J=0, (1) predicts a static limit;
   the exact error covariance is 2[1-exp(-kappa N omega_N t)]C, of
   order N^(-1). On the diffusive scale N^2 t the covariance instead
   tends to exp[-kappa |K|^2 t]C. The difference is a direct check of the
   required time-scale restriction.

Three checker-development failures are preserved, with their logs and source
hashes. The first was a missing parenthesis. The second selected the multiset
(vacancy,+e1,-e1,+e2), which makes every directional h vanish in the old tuned
control; it was therefore an accidentally reversible sector and could not
test nonreversibility. The replacement multiset above fixes that control
without changing the model parameters. The third used structural equality
for differently factored complex symbolic expressions; it was replaced by
entrywise exact simplification. These were corrected before the completed
run. The analytic failed routes—configuration-uniform spatial averaging and
inferring fluctuations from hydrodynamic entropy—are preserved in Section 4.

## 9. Limits, dependencies and seal

The proof covers fixed full-support p, fixed finite T, and finitely many
fixed modes. It does not cover modes or time horizons growing with N,
densities approaching the simplex boundary with N, arbitrary correlated or
nonstationary initial laws, births, vanishing exchange floors, or constrained
exchanges with additional sector invariants. These exclusions identify where
the displayed proof would require new estimates; they are not counterclaims
about every such extension. The K=0 field is exactly conserved, but the
question and phase-cancellation proof above use fixed nonzero modes.

No unresolved proof obligation was found under the stated hypotheses. The
full finite checks do not establish the limiting theorem by themselves.
No formal audit, retention or publication verdict is given.

The only imported scientific sources are my own sealed reports and their
identity seals, unchanged at the time of this check:

| Relative sibling source | SHA-256 |
|---|---|
| independent_context_exchange/REPORT.md | 277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713 |
| independent_context_exchange/PRE_SOURCE_SEAL.json | 7e924cc17d429c64ceb8e1b626f874dc6386ac2618ec7399af2879dce8f4d5f5 |
| independent_context_euler/REPORT.md | 60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3 |
| independent_context_euler/PRE_SOURCE_SEAL.json | 48dda0ccb30539906dd6274bbf8736258727077c0018bb89c604f491164a1fa9 |
| independent_axis_balanced_context/REPORT.md | b9cedcafccb48dfcd2503e5f00569a547288d4dcef0fb7dfca832565aec8f7cf |
| independent_axis_balanced_context/PRE_SOURCE_SEAL.json | 8519e354a43ed16b9c176aa3e7e4672e6b3e6e1101e83af040555323aa3390a2 |

The earlier Euler report supplies only reusable elementary canonical-block
machinery; its hydrodynamic conclusion is not used. The current and entropy
identities are from the other two reports. No external literature or new
primary campaign source was imported. PRE_SOURCE_SEAL.json records all local
artifact hashes and these dependency identities after the completed check.
