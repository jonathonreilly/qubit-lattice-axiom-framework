# Fixed-graph effective Omega sources have bounded phase trace density

Separate root analytical supplement. Scope is the supplied effective W0 rotor law from bare Omega, at ONE fixed finite graph, fixed positive K,delta,kappa and compact physical source-time interval[0,T]. It is not the full finite-spin/continuously forced microscopic process and supplies no uniformity in volume or spin. The full source-containment hypothesis of CONDITIONAL_POLYNOMIAL_TAIL remains UNPROVED. No scientific execution.

Set V=1+sum_e|E_e| on the actual physical electric basis. The exact W0 no-event generator is L_r=-i K D_r+i delta Q_r-kappa R_r/2. D_r is diagonal in that basis and commutes with every V power. Q_r,R_r and each complete original jump b_mu have bounded finite electric-shift range; there are finitely many local terms and matter sectors at fixed graph. For every finite integer m, V^m Q_r V^-m, V^m R_r V^-m and V^m b_mu V^-m are therefore bounded, since a shift of l1 size a has weight ratio at most(1+a)^m. Charge/occupation projections commute with V. No individual path replaces a coherent channel in this estimate.

Duhamel/Dyson expansion around exp(-i K D_r t), which is unitary in the weighted norm as well as the original norm, gives

    ||V^m S_r(t) V^-m|| <= exp(C_m t), 0<=t<=T.          (1)

This uses the bounded conjugated perturbation and can first be justified on finite electric words and then completed in the weighted Hilbert norm. It does not assume bounded D_r. The existing domain estimates in WORKING_PROOF use this same commuting-diagonal/finite-shift structure.

In the positive original quantum-jump expansion from Omega, each history has a finite product of these no-event maps and complete b_mu. There are finitely many labels at fixed graph; each birth raises N_B by two, so at most floor(n/2) births are possible from the bare state. The weighted squared norm of each history is bounded by exp(2 C_m T) times a finite product of the conjugated jump norms. Summing the finite label sets and integrating the bounded time simplexes yields

    sup_(0<=s<=T) Tr[V^(2m) rho_eff(s)] <= C_(m,T,graph). (2)

An upper exponential series bound would suffice even without the finite birth cutoff. The nonnegative trace expansion justifies interchanging sums/integrals; truncated weights and monotone convergence give the unbounded weighted-trace statement. The finite-field initial Omega has every V moment. These are actual state estimates, not a changed preparation.

Each complete formal source T_(h,mu)=-F_h j_mu F_h also has bounded finite electric-shift range and bounded V-conjugates. Consequently its ACTUAL positive effective source

    tau_h(s)=sum_(mu at h) T_(h,mu) rho_eff(s) T_(h,mu)*

obeys the same fixed-graph compact-time bound(2), with a new finite constant and the proper output number sectors. Summing all h remains finite at this fixed graph.

Choose an actual integer Gauss spanning-tree section whose chord fields vanish. In every matter sector the cycle coordinates ell are exactly the chord electric fields, hence |ell|_1<=sum_e|E_e|. Let d_c be the finite number of chords. For integer m>d_c/2, Fourier Cauchy-Schwarz for a vector psi in the physical field Hilbert space gives

    esssup_theta ||psi(theta)||²
       <= C_(m,d_c) sum_ell (1+|ell|²)^m ||psi_ell||²
       <= C_(m,d_c) ||V^m psi||².                       (3)

The convergent scalar series is sum_ell(1+|ell|²)^(-m); matter components are kept in the vector norm. Apply(3) termwise to a positive rank-one decomposition of tau_h(s), and then Tonelli. Its positive fiber trace density satisfies

    sup_(s in[0,T]) esssup_theta Tr R_h(s,theta)
                                      <= C_(m,T,graph). (4)

This does not identify a trace-class operator with a diagonal multiplication operator. Off-diagonal phase coherences remain in the original state; its decomposable semigroup trace legitimately uses the density in(4).

Thus the bounded-density assumption in the conditional tail proof is verified for these ACTUAL effective W0 Omega sources, at fixed graph and compact source time. Conditional on the still-missing full formal-source containment, that proof would give a polynomial fast-age survival bound uniform over s in[0,T] for this effective source family. The exponent and constants depend on the full graph/sector and the actual nonzero minor. The weak exponent establishes no finite residence, energy UI, physical source/clock selection, volume-uniform estimate or full microscopic result. This supplement does not prove the containment or a new theorem about the original finite-spin law.
