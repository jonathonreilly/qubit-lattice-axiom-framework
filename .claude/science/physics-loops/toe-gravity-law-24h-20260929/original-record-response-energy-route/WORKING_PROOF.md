# Actual-source response energy: positive fast-period corrector

This is an authored analytic route, not yet independently checked. Science is selected at fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7; procedure at7146fe17a76de41badcaca3c3c7cac6d11eb2a00. The compensated finite-spin law, original resolved or unnormalized coherent marks, exact finite-depth Y and bare Omega are unchanged. Tests are neutral in these exact normal-form coordinates; their physical representatives are Y* O Y, not tests evolved by an undressed replacement generator. The positive maps below are proof devices, not new physical preparations or an effective law. Algebraic identities hold at every finite allowed spin and epsilon; actual-source bounds retain the supplied coupling epsilon² S(S+1)=delta/K and their original time domain.

## 1. Exact algebra and the first product defect

Work first on a finite safe torus and finite spin, with a fixed original capped/binned history register and a passive reference. On an interval on which the specified record updates are constant, write the exact rotated adjoint generator as

    L=H0+B0+V, H0=i omega[W,.], omega=delta epsilon^-4,
    B0=P_super L-H0, V=(1-P_super)L, alpha=1/omega.

Here P_super is averaging by conjugation with exp(i theta W), as a projection on SUPEROPERATORS. B0 is a GKSL generator with Hamiltonian H_diag-omega W and every equal-grade jump, including positive grades. The exact nonpositive D is H0+B0-Pplus, where Pplus is the full positive-grade dissipator. This identity, not a leading bare generator, is used throughout. The established local strengths are B0=O(epsilon^-2), V=epsilon^-1 C1+O_local(1); the exact Hamiltonian off-grade remainder is included in V. Both have fixed finite interaction range, bounded uniformly in spin. Constants in local expansions can depend on the fixed input support but not the torus or spin.

Let V_q denote superoperator grade q: [H0,V_q]=i omega q V_q. Define the full linear extension

    S1=i alpha sum_(q!=0) V_q/q.                         (1)

On a neutral test O, this is exactly the previous K1(O)=i alpha I_W(1-P_W)L(O). It is Hermiticity preserving and S1(I)=0. It is not presumed positive or a derivation. For any Hermitian neutral O define beta_S1(O)=S1(O²)-S1(O)O-O S1(O). Since multiplication by O preserves grades,

    beta_S1(O)=i alpha I_W(1-P_W) Gamma_L(O),             (2)
    Gamma_L(O)=L(O²)-L(O)O-O L(O).

Hamiltonians cancel from Gamma. Put L_(mu,r)=sqrt(kappa)epsilon^-1 J_(mu,r) for ALL grades, and X_(mu,r)=U_mu(O)L_(mu,r)-L_(mu,r)O. The original update U_mu is multiplicative on this classical-register algebra. For either original instrument each J_mu is kept coherent; r is only an algebraic expansion. Thus

    beta_S1(O)=alpha sum_mu sum_(r!=s)
                         i/(s-r) X_(mu,r)* X_(mu,s),
    Gbar(O)=sum_mu,r X_(mu,r)*X_(mu,r).                  (3)

The Hermitian matrix h_rs=i/(s-r), h_rr=0, has norm at most pi on every finite set of integer grades. A self-contained proof is to set f(theta)=pi-theta on (0,2pi). Its normalized Fourier coefficient against exp(i k theta) is i/k for nonzero integer k, and zero for k=0. Hence for arbitrary Hilbert-space-valued x_r,

    sum_(r,s) h_rs <x_r,x_s>
       = integral_0^(2pi) f(theta)||sum_r exp(i r theta)x_r||²
                                                       dtheta/(2pi).

Parseval and |f|<=pi give both inequalities. Therefore, as OPERATOR forms, with no source or darkness hypothesis,

   -pi alpha Gbar(O)<=beta_S1(O)<=pi alpha Gbar(O).       (4)

The extension(1) has the same signed Kossakowski matrix, so(3)-(4) also hold for its product defect on arbitrary Hermitian tests; neutrality is needed to identify it with the previous restricted K1. This is a relative quadratic-form estimate, not a norm estimate for a growing-support observable. Gbar includes positive grades. Dropping them would change(4).

The correction is genuinely indefinite. In the two-grade principal matrix r=-1,0, h has eigenvalues+1,-1. The actual original j/A cross term realizes that block: take the finite-graph neutral observable N_B. Its jump gradients have factors1 for j,2 for A,0 for d, from their true W/Ntot gradings. On bare Omega the leading term of(3) is

    beta_S1(N_B) Omega
        =2i kappa epsilon³/delta sum_mu j_mu* A_mu Omega
                                                  +O_G(epsilon4)
        =20i kappa epsilon³/delta F Omega
                                                  +O_G(epsilon4).     (5)

After a helper hop the five remaining vacant edges have bare loss10 at zero eligible fields, for both original instruments. The helper's shifted edge is ineligible. Thus F Omega!=0 and the displayed off-diagonal coefficient is nonzero, including at every integer S>=1. Hermiticity and opposite grades give a positive and a negative eigenvalue on a suitable two-dimensional compression for sufficiently small epsilon at fixed graph. One may divide N_B by |B| to make it a bounded contraction. This is an actual-operator test of the correction map, not a claim about a nonzero beta expectation in the actual Omega ensemble or about failure of microscopic convergence.

## 2. Two completely positive completions; only one is an actual-source average

First, S1+pi alpha B0 is a legitimate GKSL generator on the finite carrier. Its jump coefficient matrix for each SAME original mu is alpha(pi I+h), which is positive semidefinite by(4). Its Hamiltonian is

    pi alpha(H_diag-omega W)+i alpha I_W(H_off),

which is self-adjoint. Diagonalizing the finite positive coefficient matrix mixes only Kraus branches attached to that original mu; it does not resolve the coherent signs into new records. This constructs a mathematical CP completion without an inverse spin weight. Its local strength is O(epsilon²), since its diagonal completion is larger than the O(epsilon³) first off-grade correction. The completion cannot be silently omitted when differentiating a backward test.

A more useful exact CP map requires no changed generator at all. Let p=2pi/omega be one penalty period and set

    Q_t=exp(t L) exp(-t H0),
    Q=(1/p) integral_0^p Q_t dt.                        (6)

Both factors in Q_t are unital CP: the first is the exact ORIGINAL marked evolution; the second is an onsite unitary automorphism. Consequently Q is unital CP, including arbitrary references. The penalty has integer W spectrum, so exp(p H0)=I exactly. It does not act on the classical marks. All marks occurring in exp(t L) remain the original physical marks with their original coherent amplitudes; no grade, period index or auxiliary outcome is observed.

In the interaction picture Q_t'=Q_t B(t), where

    B(t)=exp(t H0)(B0+V)exp(-t H0)
        =B0+sum_(q!=0)exp(i omega q t)V_q.

The fixed-support connected Dyson expansion has integrated local strength O(p epsilon^-2)=O(epsilon²). Uniformly in spin and safe volume, for a FIXED local/register test O,

    Q O=O+S1 O+pi alpha B0 O+O_O(epsilon4).              (7)

Indeed the first ordered integral averages to p B0/2 plus i alpha sum V_q/q; two or more interactions cost O_O(epsilon4). At each order only interactions touching the growing support survive, because every local generator annihilates I. The ordinary factorial/time-simplex bound converges for p times the local interaction norm sufficiently small. This justifies the stated remainder without using the global generator norm. It does not give a support-independent bound on arbitrary retarded tests. Nor does it identify Q with exp(S1+pi alpha B0) beyond this stated local first expansion.

There is a particularly strong exact source identity. Define the positive normalized proof state tau_s=Q_* sigma_s, where sigma_s is the actual rotated microscopic state. For ANY neutral bounded observable Z,

    Tr tau_s Z=(1/p) integral_0^p Tr sigma_(s+t) Z dt.    (8)

This is exact on the common constant-update interval: exp(-t H0)Z=Z and the actual Markov evolution composes. The identity includes positive extensions with passive references. Tau is an anticipative mathematical time average, not a causal state assigned to the original history at time s, and it does not evolve under D. No separate GNS states or different preparations have been identified.

Every previously checked neutral positive ACTUAL-source estimate transfers to tau through(8), within its original time range. In particular, for the exact common-mark-gauged tangent score Ndot_mu from the previous route,

    integral_0^T Tr tau_s Ndot_mu ds
       <= integral_0^(T+p) Tr sigma_u Ndot_mu du
       <=C[(T+p)²+epsilon²]<=C'(T²+epsilon²),            (9)

for 0<T<=1-p and small epsilon. The score is neutral, including its exact same-grade terms. Local hole and ordinary first-field bounds transfer in the same manner; there is no conditional field or dark-excursion assumption. The actual source theorem is not inserted into a D-forward channel formula.

## 3. Exact CP energy identity and its remaining signed defect

Differentiating Q_t and integrating yields the exact superoperator identity

    L Q-Q H0=(M-I)/p=:A_p,   M=exp(p L).                (10)

A_p is itself a GKSL generator: a Poisson process applying the unital CP channel M has this generator. This is an auxiliary mathematical generator, not the microscopic law or a new observed clock. In particular

    Gamma_Ap(O)=[M(O²)-M(O)²+(M(O)-O)²]/p>=0             (11)

for Hermitian O. The first term is nonnegative by the elementary Kraus/Stinespring Schwarz inequality; all expressions keep the full original register.

For neutral exact-D backward tests O_s, dot O_s=-D O_s, define the EXACT intertwining defect

    E_Q=L Q-Q D.

Because H0 O_s=0,

    E_Q O_s=A_p O_s-Q(D-H0)O_s.                         (12)

Differentiating the squared test in the ACTUAL state gives

 integral_0^T Tr tau_s Gamma_D(O_s) ds
   =Tr tau_T O_T²-Tr tau_0 O_0²
                    -integral_0^T Tr sigma_s E_Q(O_s²)ds. (13)

The left side is positive, and both endpoints lie in[0,1] for a Hermitian contraction. Unlike applying the signed K1 to an energy, Q(Gamma_D) is positive on the complete carrier. Equation(13) therefore removes a real positivity ambiguity in a corrected energy method. It does NOT bound the signed last term. E_Q has not been shown relatively bounded by this energy in the actual source.

There is an exact, informative expression for that defect. Put Pplus=B0-(D-H0). On neutral inputs,

    E_Q O=Q Pplus O
              +(1/p)integral_0^p Q_t V(t)O dt.          (14)

The bare average of V(t) is zero. Its first interaction term is

    -B0 S1 O + P_super(V S1)O,                          (15)

as follows from the exact integer-frequency integrals. The first term is off-grade and of local order epsilon; the second has neutral leading term epsilon² T. The remainder after the first interaction is O_O(epsilon³): two B insertions and one V cost p² epsilon^-5=O(epsilon³); the connected local expansion provides the same uniform fixed-support bound as in(7). P_super in(15) projects the superoperator grade-zero part, not an assumed dark state. The exact positive-grade term Q Pplus is retained.

For clarity the integral coefficients are: for an outer V_r(t), r!=0, the inner B0 contributes p/(i omega r) before division by p, hence -B0 S1; an inner V_q contributes only q+r=0 and coefficient p/(i omega q), hence P_super(V S1). These signs match [H0,S1]=-V. Truncating Q at(7) before multiplying by the O(epsilon^-4) penalty would NOT reproduce(15); its higher off-grade coefficients are then of relevant order.

Consequently the simple positive completion alone does not close the energy estimate. Its exact residual contains a fast transport applied to the first corrector, not merely the already priced jump score. Removing this off-grade term by another homological step recreates a higher product/transport obligation; positivity of that further map is not inherited by assertion. Positivity of(11) likewise does not compare Q Gamma_D with Gamma_D in sigma: a CP map need not dominate its input in Loewner order. A trace-local O(epsilon²) closeness of Q to I cannot be applied to the unbounded-in-epsilon quadratic response class.

At history-bin boundaries, (6)-(15) are used only inside a constant-update interval. Concatenation retains the actual squared-test and corrected-test boundary terms. A future interval of length p crossing a bin must instead use the exact time-inhomogeneous propagator and its explicit derivative/boundary terms. No boundary window is discarded on a growing-support energy estimate. This packet claims neither their uniform response price nor a fictitious periodicity of the chosen local coloring.

## 3A. A positive triangular filter removes the leading off-grade defect

The single-prefix failure in(15) has a constructive repair. Let t=t1+t2 with t1,t2 independent uniform variables on[0,p], and define

    Q2=E_t Q_t.

This is a deterministic convex integral defining a proof channel, not an added random clock or an observed variable. Its density is t/p² on[0,p] and(2p-t)/p² on[p,2p]. Q2 is exactly unital CP for the same reasons as Q. Its characteristic function has a DOUBLE zero at every nonzero integer penalty frequency:

    phi(q omega)=E exp(i q omega t)=0,
    E[t exp(i q omega t)]=0, q!=0; E t=p.               (16)

These identities follow either by multiplying the two uniform characteristic functions or directly by integrating the triangular density. No averaging in volume, spin, fields or preparation is involved. Consequently

    Q2 O=O+S1 O+2pi alpha B0 O+O_O(epsilon4).            (17)

More importantly, its EXACT intertwining defect on a neutral test is

    E2 O:=(L Q2-Q2 D)O
         =Q2 Pplus O+E_t[Q_t V(t)O].                   (18)

Expand ONLY the last expression, retaining the exact D. The zero-interaction term vanishes by phi(q omega)=0. The term with one B0 insertion is B0 V_r E[t exp(i r omega t)] and vanishes by the second identity in(16). With one V_q insertion and the outer V_r(t), both q,r nonzero, the coefficient is

 E[(exp(i(q+r)omega t)-exp(i r omega t))/(i q omega)]
                      =1_(q+r=0)/(i q omega).

It therefore contributes exactly P_super(V S1), with the same plus sign as the previously checked feedback. All terms with at least two inner B insertions cost O_O(p² epsilon^-5)=O_O(epsilon³), by the uniformly bounded fixed-support interaction-picture expansion. The interval is at most2p; this changes only its constant. Also Q2 Pplus-Pplus is O_O(epsilon4), since Pplus has local strength O(epsilon²). We obtain

    E2 O=Pplus O+P_super(V S1)O+R2(O)
        =Pplus O+epsilon² T(O)+R3(O),
    ||R2(O)||+||R3(O)||<=C_O epsilon³.                 (19)

The second remainder includes the exact difference P_super(V S1)-epsilon²T. These are uniform SPIN/VOLUME bounds for a declared FIXED local/register input. They are not bounds independent of its support, and no uniform backward-test estimate is asserted. The positive-grade generator Pplus is exact in(18) and retained in(19); replacing its leading local coefficient, if desired, creates another explicitly priced local remainder.

Thus Q2 is a genuine completely positive actual-law substitute for the SIGNED two-corrector observable map through the leading feedback order. Its diagonal O(epsilon²) term is real and cannot be deleted. This is a proof map; it does not prove that the effective generator D+epsilon²T is GKSL, identify the actual state with a D state, or modify the physical preparation.

Set tau2_s=(Q2)_* sigma_s. For every neutral positive test its expectation is exactly E_t Tr sigma_(s+t)Z. Consequently all the source transfers in(9),(27) hold with T+2p in place of T+p. Tau2 is positive and includes every original mark, but remains an anticipative proof state. For the exact-D backward test,

 integral Tr tau2_s Gamma_D(O_s) ds
  =Tr tau2_T O_T²-Tr tau2_0 O_0²
                         -integral Tr sigma_s E2(O_s²)ds. (20)

This is the new positive energy identity through the true feedback order. The first corrector's indefinite product defect no longer requires a guessed positivity assumption, and the leading off-grade transport from(15) has been canceled by a positive filter. The remaining signed consumer is explicitly

 -integral Tr sigma_s [Pplus(O_s²)+epsilon²T(O_s²)
                                      +R3(O_s²)]ds.     (21)

A small fixed-support norm for R3 does not price R3(O_s²) on the fast spatially growing response. Nor is a bound for tau2 energy automatically the sigma energy required by(28). These are still substantial missing estimates. The correction therefore moves the positivity/intertwining step but does not close the full forced output.

There is also an exact boundary identity: if M=exp(p L), then

    L Q2-Q2 H0=((M-I)/p) Q.

It follows by integrating the triangular density by parts and using Q_(p+u)=M Q_u. Unlike A_p alone, the product A_p Q is not asserted to be a GKSL generator. The precise identity is sufficient, and its failure to provide a further positivity comparison is not hidden.

All interval, original-history and endpoint qualifications following(15) remain, with future delay at most2p. No crossing-bin contribution is discarded. The source bound applies whenever the actual process is supplied through T+2p; this is a smaller local extension of the same preparation, not a separate initial condition.

## 3B. A bounded-output bin repair, not an energy repair

There is a limited actual-state boundary statement. Fix the FINITE observed original-label set F and finitely many prescribed physical bin edges. Compare the true prefix of length at most2p from an ACTUAL input sigma_s with a prefix using the same exact quantum trajectory and marks but routing every observed mark according to the bin containing s. Outside a crossing prefix they agree. Within it they differ only if an F mark occurs after a crossed bin edge. Unobserved original marks remain in the quantum law; their spatial labels are not newly read.

The checked actual intensity bound gives expected F count in an interval of length2p at most C_(F,T) p. Couple the two classifications on the same ORIGINAL trajectory instrument. On every no-misclassified-event branch the quantum and classical output is identical; the remaining CP branches have total trace at most that event probability. Therefore the full quantum/classical output difference, after any passive-reference extension and any further common CP readout, is at most

    2 Prob(actual observed mark in the crossing window)
                                           <=C_(F,T) p. (22)

This is a CP branch/probability estimate, not a square-root gentle estimate for a coherent quantum truncation. The original labels were already classical in the actual instrument. Quantum paths, coherent signs WITHIN each original mark, fields and all unobserved events are identical in the coupling. No conditional intensity bound is used. Summing over all declared bin edges multiplies the constant by their finite number. Post-prefix W rotations preserve the trace estimate.

Thus the source-time identity(8) and its triangular version admit an O_(F,T)(p) actual-state repair on BOUNDED neutral joint outputs if a frozen-bin prefix is used across a boundary. This does not bound Q2 Gamma_D, E2(O_s²) or the derivative of that prefix: their relevant operator/form norms may diverge as epsilon decreases and the backward support grows. Nor does(22) bound the retarded response integrated over a boundary window merely from its length. The main intertwining/energy theorem remains the homogeneous-register-interval theorem, with those energy boundaries explicit.

## 4. Eliminating the independent connection current, with its real price

There is a separate exact improvement of the previous two-part consumer. It applies to the COMPLETE tangent based at exact D, in the ACTUAL sigma, before any darkness compression. Define

    a_mu=J_(mu,0)/epsilon, d_mu=J_(mu,-2)/epsilon,
    b_mu=J_(mu,-1), B_eps=sum(a_mu*M_mu a_mu-d_mu*M_mu d_mu),
    h_eps=(kappa/2)(Btilde-B_eps).                       (23)

The local summands of h_eps have norm O(epsilon), but are retained exactly. They include the mismatch between the exact same-grade jumps and their leading coefficients. No term in D is replaced. The checked comparison family's exact derivative is

 dot D(O)=i kappa sum[a_mu*[U_mu(O),M_mu]a_mu
                              -d_mu*[U_mu(O),M_mu]d_mu]
          +(i kappa/2)[B_eps,O]
          +kappa sum C_(b_mu,i v_mu)(O)+i[h_eps,O].     (24)

Here v is the full previously checked local corner coefficient, and C is the complete polarized marked dissipator. Formula(24) follows directly by differentiating the exact jump phases, exact grade-1 variation and its stated Hamiltonian. It retains both loss terms and every full-test corner. It is independent of the scalar phase convention for a dilation.

For a normalized positive actual joint state sigma and a Hermitian contraction O set

    a_x=||x sigma^(1/2)||_2,
    e_x=||(U_mu(O)x-xO) sigma^(1/2)||_2,
    b_a=||(M_mu-10)a_mu sigma^(1/2)||_2.

The letters a_x are norms, not operators. The following elementary estimates hold pointwise, with the appropriate mu understood:

 |<i a_mu*[U(O),M]a_mu>|<=2 b_a a_a,
 |<i[a_mu*M a_mu,O]>|
                  <=20 a_a e_a+2 b_a(a_a+e_a),
 |<i d_mu*[U(O),M]d_mu>|<=2m a_d²,
 |<i[d_mu*M d_mu,O]>|<=2m a_d(a_d+e_d), m=10,
 |<C_(b,i v)(O)>|<=a_b e_v+a_v e_b.                    (25)

For the first line subtract the scalar10 from M and use Hermiticity on both sides. For the second write a O=U(O)a-nabla_a O. The scalar part has a real U(O) expectation and costs20 a_a e_a; the remaining part puts M-10 on the INPUT source column and costs2b_a||aO sigma^(1/2)||. The latter is at most2b_a(a_a+e_a). This keeps arbitrary output phase sensitivity; it does not assume [U(O),M]=0. The d estimates use ||M||<=m. The final line is the complete four-column polarized identity followed by Hilbert-Schmidt Cauchy-Schwarz. In particular it requires e_v; a bound on a_v alone does not replace it.

For positive fixed weights w_mu let S_w=sum_mu w_mu. Define

 E_D=integral_0^T sum_(mu,r<=0) w_mu^-1
                 ||nabla_(L_mu,r) O_s sigma_s^(1/2)||_2² ds,
 E_v=integral_0^T sum_mu w_mu^-1
                 ||nabla_(v_mu) O_s sigma_s^(1/2)||_2² ds. (26)

The actual-source proofs, with the exact normalized jumps in(23), give

 integral sum w a_a²<=C T S_w,
 integral sum w b_a²<=C(T²+epsilon² T)S_w,
 integral sum w a_d²<=C epsilon² T S_w,
 integral sum w a_b²<=C epsilon4 S_w,
 integral sum w a_v²<=C epsilon² T S_w.                 (27)

The a bound is its uniform local norm. The b_a bound is the checked five-eligible-link source score, retaining the O(epsilon) exact-a correction. The d and v bounds use their exact negative grades, their bounded local support and the actual local hole estimate. The b bound uses the LOCAL actual bare-j budget and J_-1-j=O(epsilon²). Thus(27) is valid in the actual source, for 0<T<=1, without a D-forward expectation or a postselected field hypothesis.

Since L_0=sqrt(kappa)a, L_-2=sqrt(kappa)d and L_-1=sqrt(kappa)epsilon^-1 b, combining(24)-(27) yields

 |integral_0^T <dot D(O_s)> ds|
 <=C sqrt(T S_w E_D)+C epsilon² sqrt(S_w E_v)
       +C S_w(T^(3/2)+epsilon T+epsilon² T)
       +|integral_0^T <i[h_eps,O_s]>ds|.                (28)

No connection variance or independent connection-current hypothesis remains in(28). Both response quantities are explicit POSITIVE gradient energies in the SAME actual sigma. This is a real consumer reduction, not a claim that either energy is bounded. It loses the stronger T²-only score in the first term because the linked Hamiltonian requires ordinary grade-zero activity, of order T. That cost is displayed rather than hidden by a scalar phase convention.

The physical tangent parameter is lambda_epsilon=epsilon² kappa/(2delta). For a fixed summable weight with S_w bounded independently of volume, sufficient response prices in this family are

    E_D=o(epsilon^-4), E_v=o(epsilon^-8),
    epsilon² integral <i[h_eps,O_s]> ds ->0.             (29)

The last current is an exact coefficient remainder already present in the previous local tangent comparison. Its local strength O(epsilon) alone does not price its sum over an expanding test. Equation(29) is sufficient for THIS tangent contribution. Transfer from dot D to the actual feedback T still requires its stated dark-input comparison and its higher local remainder/boundary estimates. Nothing in(28) promotes that compression to an all-state identity.

The positive average tau in section2 can also be used in(25)-(28), because all source squares in(27) are neutral and transfer by(8). This does not identify the resulting tau-gradient energy with the sigma-gradient energy: that additional comparison is not established. The exact energy identity(13) refers to tau, while the original retarded consumer refers to sigma. Keeping both labels is essential.

## 4A. Fixed local hole tests do not suffer a rescaled endpoint ambiguity

The positive filter adds a diagonal O(epsilon²) term to the old signed corrector. For general local neutral outputs that term cannot be discarded at epsilon^-2 rescaling. There is nevertheless a limited ACTUAL-source endpoint bound on the original hole-corner class.

Let Z be a fixed bounded neutral local/register test with Z=Q_U Z Q_U, where Q_U excludes all A sites in a fixed cone being filled. Enlarge the cone to include every local term acting on it. The exact expansion is

    L Z=epsilon^-2 B2 Z+epsilon^-1 C1 Z+O_Z(1).

B2 preserves grades and cannot create a hole from a completely filled enlarged input: its neutral Hamiltonian preserves W and its bare jumps have negative W grade. Therefore B2 Z is a neutral two-sided hole-corner operator on the enlarged cone. C1 Z has only nonzero grades and hence has zero filled-filled compression. The actual local defect bound gives

    |Tr sigma B2 Z|<=C_Z epsilon²,
    |Tr sigma C1 Z|<=C_Z epsilon,
    |d Tr sigma_s Z/ds|<=C_(Z,T).                       (30)

The second inequality is the ordinary Cauchy-Schwarz off-corner bound, not a conditional state estimate. Remainders and observed updates have their stated fixed local norms. This holds piecewise on the same register intervals and for actual positive history/reference extensions. Averaging over the triangular delay consequently gives

    |Tr(tau2_s-sigma_s)Z|<=C_(Z,T) p=O_Z(epsilon4).      (31)

For a fixed hole-corner test the difference is therefore small even after epsilon^-2 rescaling. This uses actual source input; it is not a norm identity Q2=I+K1+K2D or a result for every positive test. In particular its constants cannot be used unchanged on an expanding exact-D backward observable. It removes a fixed-test endpoint ambiguity only.

## 5. Why the direct closures do not follow

First, the complete connection cannot be removed just by calling the jump tangent a martingale. The earlier exact overlap Gamma=Im sum L*dot L-dot H still holds. Equation(28) handles that term by a specific factorization and pays a new v-gradient. It does not assert a noise-only bound.

Second, using a source estimate in O sigma O is unjustified. A bounded contraction need not satisfy O sigma O<=sigma. For a pure state psi, an observable can rotate its support into an orthogonal direction. In this model neutrality preserves total W, but does not fix the position of holes, the B pattern, negative charges or fields within that W block. In particular the term ||v O sigma^(1/2)|| cannot be replaced by ||v sigma^(1/2)||. The exact energy E_v in(26) is where that right-action sensitivity is retained. This algebraic warning is not an assertion that an arbitrary rotated state is an actual Omega preparation.

Third, applying a signed corrected observable to O² without its product defect is incorrect. The exact form(2)-(5) supplies both its size and an actual original-operator indefinite example. The first CP completion(6) resolves positivity but leaves the fast transport(15). The triangular refinement cancels that leading off-grade term and yields(19)-(21). The unproved inequality needed to close the refined identity is a signed, ACTUAL-source relative-form bound, for example an absorbable estimate on

    -integral Tr sigma_s E2(O_s²) ds

in terms of the positive left energy plus a volume-uniform remainder at the scaling required by(29). Merely naming this as an energy estimate is target-equivalent at the stated retarded class. A sufficiently strong separate bound on the exact R3 quadratic-response remainder, together with the displayed positive-source/feedback form and the tau2-to-sigma energy comparison, would be a stronger sufficient package, not an already proved consequence of ordinary fields or counts. The single-prefix -B0 S1 obstacle was actually removed, not merely renamed.

Fourth, the monodromy channel's positivity does not imply the similarity generator Q^-1 L Q is GKSL. At fixed finite volume Q may be invertible for sufficiently small epsilon, but its inverse need not be positive and its global smallness radius can depend on volume. No inverse Q, spectral gap, finite excitation cap or changed initial state is used in the proof.

A concrete original-carrier test shows why a usual scalar energy chain rule is unavailable. The exact identity

    nabla_L(O²)=U(O)nabla_L O+(nabla_L O)O

implies at most the two-sided estimate Gamma_D(O²)<=2 Gamma_D(O)+2 O Gamma_D(O) O for a Hermitian contraction. The second term probes O sigma O, not the actual source. There is no uniform epsilon-independent replacement by C Gamma_D(O), even for neutral, number-preserving local tests on the physical carrier.

Here is an explicit finite-support embedding on safe even tori L>=16. Let the only A hole be the origin. Occupy the six B neighbors +/-e_i and the additional B site3e_1. Assign negative charges to -e_1,-e_2,-e_3, positive charges to the other four B sites, and positive charges to every other occupied A site. Call this word psi. Its total charge equals |A| and it has W=1,N_B=7. On every positively oriented star edge set E=-1, and superpose a flow E=-1 along the positive-axis path0 to3e_1. The shared edge0 to e_1 then has E=-2. This gives div E=q-1_A: the six star charges sum to zero and the extra path transfers the remaining unit divergence from the hole to3e_1. All other fields are zero.

Let phi have exactly the same charges and add a unit closed circulation around the plaquette with base(0,3,0), directions e_1,e_2. It is a distinct orthogonal physical word. Both psi and phi are dark for EVERY bare original j: the only A hole has all six B neighbors occupied. Let chi instead move the positive charge at e_1 to the empty B site5e_1 and add E=-1 along the path e_1 to5e_1. The added path changes divergence by -1 at e_1 and+1 at5e_1, so chi is physical, has the same W,N_B,Ntot, and has the vacant edge(0,e_1). All fields in these words have magnitude at most2. For S>=4, a resolved positive birth on that edge in chi has squared normalized amplitude1-2/[S(S+1)]>=9/10; the coherent original mark is also nonzero. No spin boundary was replaced by a rotor value.

Embed the words in a finite patch containing those paths/plaquette and fix all crossing fields to zero. Outside it all three words have the same bare background. The following local matrix units leave every boundary field unchanged and preserve the exact Gauss sector:

    O=(|phi><psi|+|psi><phi|+|chi><phi|+|phi><chi|)/sqrt2.

Extend by zero on other patch words and identity outside the patch. Its norm is1, it is Hermitian, and it commutes with W and Ntot. It has no record dependence. We have

    O psi=phi/sqrt2, O² psi=(psi+chi)/2,
    j_mu psi=j_mu O psi=0 for ALL mu,
    j_(0,e1) O² psi=j_(0,e1)chi/2!=0.                  (32)

For exact D, J_-1=j+O_local(epsilon²). All fast-jump gradients of O in psi are therefore O(epsilon) after normalization by epsilon^-1. The exact grade0/-2 normalized jumps are bounded; all other negative grades are O(epsilon). Only finitely many cones touch the fixed patch. Hence

    <psi,Gamma_D(O)psi><=C,
    <psi,Gamma_D(O²)psi>>=c epsilon^-2                 (33)

for sufficiently small epsilon, with constants uniform in S>=4 and safe L. The second inequality follows from the single displayed normalized grade-1 jump gradient, equal to -sqrt(kappa)j chi/(2epsilon)+O(epsilon). It remains true along the required coupled spin sequence. Thus no uniform all-state chain-rule constant can feed(28) for O_s² into the energy for O_s automatically.

This is an exact physical-word counterexample to that UNIVERSAL form shortcut. The input psi and the constructed O are not asserted to have a specified bare-Omega process weight or to equal a D-backward image of a prescribed local readout. A source-specific signed energy estimate could still hold. The example does not refute such an estimate, the actual microscopic limit, or any positive-time cluster theorem.

These are failures of particular closures, not evidence of physical divergence. No statement here compares different infinite-volume representations or asserts a late-time rotor approximation at arbitrary backgrounds. The unclosed physical-time spatial response, full-test dark comparison, electric tail and history-boundary prices remain the original obligations.

## 6. Approach portfolio and scope

The first family is a signed Kossakowski/Hilbert-kernel form calculation. It gives a support-, volume- and spin-independent relative product estimate and an explicit CP completion. The second is an exact short-period ORIGINAL-channel average; it supplies a positive actual-source proof state, exact transfer of neutral source bounds, and a positive energy identity with an explicit signed defect. The third is a direct source-column treatment of the complete tangent: it replaces the previously independent connection current by exact D and v gradients plus the unchanged coefficient remainder. These are distinct mathematical mechanisms; none is a finite-gap or static-cluster argument.

The strongest new results are(4),(6)-(10),(28) and the triangular refinement(16)-(21), with the limitations stated there. They close a positivity ambiguity and a source-current decomposition, not the required uniform response energies. One small literal physical-word control corroborates(32); it does not test the exact-D asymptotic theorem or any response limit. No imported theorem, formal review/audit or microscopic-limit claim is made. All calculations are exact finite-carrier algebra followed only by the declared fixed-support local expansion. A focused independent check is required before reuse.

## 7. Literal control and resource accounting

The code and expected identities were frozen before execution in CONTROL_PREFLIGHT.json. The sole run independently encodes psi,phi,chi and both legal original-sign outputs on L=16,S=4. It checks20,480 exact Gauss rows, W=1,N_B=7,total charge2048, the sole bright star edge, and every input field bound. The two squared spin weights are9/10 and7/10, so the bare squared-O gradient squares are9/40 for the resolved plus mark and2/5 for the ORIGINAL coherent mark. The two original sign outputs have distinct charge words and are orthogonal, so their squared norms add for the SAME coherent Kraus operator; no sign outcome is newly observed. The 3-by-3 rational calculation verifies O² is a projection; no numerical eigenvalue solver or full carrier is used.

The guarded entire child used0.131867 CPU seconds and0.139456 wall seconds under the5CPU/30wall/60MiB ceiling. Its scientific section used0.021291 CPU seconds and0.021395 wall seconds; these narrower figures are NOT the whole-child cost. Peak RSS was21,020,672 bytes. All four thread settings were1, original deadline and STOP guards passed, and there was no failed run or resource kill. The finite control verifies the listed words and bare-gradient coefficients only. Exact J/D conclusions in(33), the Fourier kernel and the CP/filter identities remain analytic proofs, not extrapolations from this fixture.
