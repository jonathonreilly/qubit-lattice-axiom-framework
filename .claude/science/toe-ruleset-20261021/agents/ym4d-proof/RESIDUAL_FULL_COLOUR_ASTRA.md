# Full-colour residual and periodic-consumer bridge

Author continuation; original mathematics in the supplied SU(N) Wilson / normalized soft-kernel model. Status at initialization: **open**, with the charged-root predecessor independently checked. This note does not certify Yang–Mills existence, OS reconstruction or a physical Hamiltonian mass gap.

## 0. Target, premises and decisive criteria

Fix N≥2, odd L≥3, κ>0 and finite depth n≥1; write ell=L^n. The new target is the complete F² coefficient of the actual normalized determinant remainder Δ_n, including the Cartan fluctuations, in the infinite-volume convention consumed by [FLOW, Def F-g](FLOW.md) and [UIR55, Theorem TEL and its final Cartan erratum](UIR55.md). The supplied action and its S4′ contours are premises, not newly adopted physical axioms. No empirical value, new framework primitive, full-colour twist-independence assumption, or physical mass-gap assumption is used.

The immediate success witness is (i) a derivation of the actual neutral contribution with every ghost/Gram weight; (ii) an equality of the **grouped** coefficient with the original infinite-volume consumer, proved by a specified volume/IR/P limit and actual singular-centre estimates; and (iii) a resulting formula or bound for Rho_n with its exact n-dependence. A nonzero individual Wilson or polar tadpole is not a counterexample to cancellation of Δ_n. Conversely, absence of a neutral logarithm does not show its finite coefficient vanishes. A finite-rank deletion is not negligible without a bound on its differentiated inverse factors.

Accepted predecessor scope: the complete [independent actual-vertex report](REVIEW_RESIDUAL_VERTICES_ASTRA.md), read in full before this work, confirms zero residual F² on a paired real antiperiodic charged-root sector for each fixed n, volume first and P→0 second. Its source is [the normalized actual-vertex note](checks/residual_det_vertices_working.md). The [harmonic bridge](checks/residual_det_lattice_bridge_working.md) and [fixed-depth recovery](RECOVERY_UIR_ASTRA.md), together with their scoped reviews, provide finite algebra and local fixed-depth tree jets. The fixed-depth constants may grow with n. All original frozen sources remain untouched.

The actual consumer was reread before constructing this unit: FLOW §0, §1, Def F-g, and its IR-id regulator argument; UIR55 §3.3–3.7, §5–§8 and final erratum E-2; UIR2_55 lines 1–165, including the explicit root-sector antiperiodic setting and the preserved old formula whose limitations are repaired in the predecessor. FLOW defines u from the infinite-volume Hessian; that **definition alone** proves no finite-volume comparison or uniformity. UIR55 explicitly includes finite neutral terms in a^perp. These are the comparison targets.

Methodology is read at current-main ca2bc7ddf64790da96cd43d42017d000fbfe4808, supplied fresh by the coordinator at 15:14Z. The coordinator owns the worktree lock, git, PR and review operations. Science head on dispatch: 94baab819b7eb80087f7616b4eaad799fa1a2541. This worker writes only this note and checks/residual_full_colour_*.

Distinct constructive routes to test: (A) exact abelian gauge-change cancellation followed by the actual neutral quartic residual vertices; (B) fibrewise determinant identities away from singular fibres, with translation-invariant periodic-mode excision and a proved grouped thermodynamic comparison; (C) if the exact coefficient is not zero, an n-dependent bound from the remaining local source tensors, compared with the all-increments requirement. A common mass regulator is not used unless its gauge-identity correction is derived. A global root pin is not substituted for an ordinary Fourier quotient.

Pre-stated failure criteria: any omitted neutral quartic vertex or determinant weight; a domain change treated as a constant Jacobian when it is not; a singular-centre exponent ≥4 without a proved cancellation; a periodic/antiperiodic equality asserted without convergence of the actual grouped terms; a fixed-n constant used as uniform in n; or any internal inverse gap described as a physical spectral gap. Controls must reject at least the false “neutral Hessian is background independent” assertion and an inconsistent zero-mode deletion. Exact algebraic controls will be distinct from the prior charged-root scripts. Numerical checks, if useful, will have declared scope and will not prove an unbounded n/T claim.

Reading/search limits: the first broad landed-source phrase search was killed with exit 137 after unrelated hits, so it is not a completed absence search. The directly relevant prior sources already state the neutral/full-periodic bridge as open; a narrow source search and all actual matches will be recorded before novelty is claimed. This is a new construction attempt, not a claim of literature priority.

## 1. Working derivation

Initialized before the new derivations and controls. Further sections will preserve failed attempts and the exact remaining obligation.


### 1.1 Actual commuting-colour jets: the finite neutral term is present

Write a Cartan link as diag(exp(i a_j)), with sum_j a_j=0, and use a Cartan basis H_A=i diag(h_Aj) normalized by N^-1 sum_j h_Aj h_Bj=delta_AB. All neutral quantum and external fields commute. For a plaquette curvature f_pj, the exact neutral Wilson Hessian is

    H_W^{AB}(a)=d_2* diag_p[N^-1 sum_j h_Aj h_Bj cos(f_pj)] d_2.

Here d_2 is the ordinary link-to-plaquette incidence; d denotes the ordinary site-to-link incidence. Thus H_W d=0 **off shell**, since d_2 d=0, but H_W depends on the background through cos(f). The neutral gauge derivative d and its scalar Laplacian are background independent. These are different statements.

In particular, at a background epsilon a, the first neutral Hessian vertex vanishes and

    [epsilon²] H_W^{AB}=-(1/2)d_2* diag_p[N^-1 sum_j h_Aj h_Bj f_pj²]d_2.

On a periodic fine torus of V_f sites, omit the four constant one-form kernels from W=H_W+dd* and the constant scalar kernel from Delta=d*d, in fixed orthogonal domains. At a=0, W^-1(q)=lambda(q)^-1 I for q!=0. Hypercubic symmetry gives, for every plaquette orientation,

    V_f^-1 sum_{q!=0} (|d_mu(q)|²+|d_nu(q)|²)/lambda(q)
       =(1/2)(1-1/V_f).

The Cartan completeness identity sum_A h_Aj h_Ak=N delta_jk-1 then gives the **actual neutral Wilson transverse-group coefficient**

    beta_neutral[W^perp] = -(N-1)/4 (1-1/V_f),
    a_neutral(Wilson) = -(N-1)/4                         (FC1)

in FLOW's beta[Wilson]=1 normalization. The ghost has no neutral background vertex. This is exact for the quadratic plane-wave coefficient at finite volume whenever the phase average is defined. It disproves the tempting background-independent-neutral shortcut. It is not the coefficient of the remainder Delta_n.

For the actual one-step normalized soft action, let theta_Tj be the commuting phase of a contour, let bar theta_j be its average, z_Tj=theta_Tj-bar theta_j, mu_rj=avg_T z_Tj^r, and delta_j=b_j-bar theta_j. Through total degree four at the trivial field, the supplied normalized phi has

    kappa phi = (kappa/N) sum_j [delta_j²/2
                 +delta_j mu_3j/6 -mu_2j delta_j²/4-delta_j^4/24]+O(6).   (FC2)

Derivation: avg exp(i theta)=exp(i bar theta)[1-mu_2/2-i mu_3/6+mu_4/24+O(5)], so its modulus is 1-mu_2/2+mu_4/24+O(6), its phase is bar theta-mu_3/6+O(5), and multiplying p(1-cos(b-arg M)) gives FC2. The SU(N) constrained maximum differs from this polar expression only at degree six, as established for the actual phi dictionary in the recovery source; equivalently its order-three trace-phase correction is orthogonal to a traceless delta at the relevant order. It cannot remove the displayed quartic polar contribution.

Every contour has the same endpoints and winding. Hence the spread maps a -> z_T annihilate both ordinary gauge gradients and constant one-forms. FC2 is even under simultaneous (a,b)->(-a,-b), and has no cubic neutral tensor. More generally a cubic real-trace tensor with two commuting neutral inputs and any third colour is zero: it is a commutator tensor. Consequently the cubic source for an internal charged fluctuation also vanishes. The neutral quartic value of a minimized finite chain is therefore its actual quartic energy evaluated on the linear stationary chain; there is no cubic-source exchange in this particular commuting restriction. This does **not** remove the charged exchange term from the full theory.

All neutral first background/residual vertices of the Hessian, M, C, H_h and their local massive Schur complements vanish at (1,0). Their second vertices include FC2 and the Wilson cos term. Thus neutral one-loop second variations are complete tadpoles, not zero operators.

### 1.2 Periodic scalar domains and the retained root-mean term

Let the coarse torus have V_c=T^4 sites and V_f=ell^4 V_c fine sites. The following formulas are per neutral colour; tensor them with the Cartan identity. Scalars use the ordinary counting inner products, with unit fine-lattice differences. Let J inject the coarse roots, I inject non-root sites, A=I*Delta_f I and

    L_har=J-I A^-1 I*Delta_f J,
    S=J*Delta_f J-J*Delta_f I A^-1 I*Delta_f J.

Then ev L_har=1, Delta_f L_har=J S, L_har 1_c=1_f, ker S=span(1_c), and A is positive. Write P_c0=1_c 1_c*/V_c and P_cperp=1-P_c0. The coarse h/gauge parameter is **1_c-perp**. The gauge-fixing column Delta_f L_har on that parameter space has Gram (S|1_c-perp)^2. Consequently the exact completed fine fixing is

    Q_per = 1-Delta_f L_har (S|perp)^-2 L_har* Delta_f
          = P_int + J P_c0 J*,                                      (FC3)

where all products with S^-2 are restricted to 1_c-perp. The rank-one term has not been dropped. It is spatially long range; its free Bloch support is the single coarse K=0 fibre.

The scalar Schur pseudodeterminant is

    det' Delta_f = ell^4 det A det' S.                              (FC4)

Proof, including the factor: the unit-determinant scalar shear (I,J)->(I,L_har) makes the quadratic form diag(A,S). Its null vector, normalized on the coarse space, maps to a fine constant of squared norm V_f/V_c=ell^4. The pseudodeterminant congruence therefore has precisely this null-vector Gram factor. Equivalently apply the determinant identity after adding a rank-one lift of the constant kernel and compare its coefficient. This is not det Delta_f on a site-pinned domain.

At rho=0 set R_c=(1+d_c*C d_c)^-1 and define the full periodic neutral row

    Fbar_1=P_int d*+J[P_c0 J*d*+R_c^(1/2)d_c*M],     F_0=d*.          (FC5)

The root summands have orthogonal constant/mean-zero ranges, so Fbar_1*Fbar_1=d Q_per d*+M*d_c R_c d_c*M. Both Fbar_1 d and Delta_f have the **same** constant right and left kernel. In fact Fbar_1*1_f=0, using R_c^(1/2)1_c=1_c. In harmonic scalar coordinates its block matrix is

    [ A             0             ]
    [ P_c0 J*Delta I R_c^(1/2)Delta_c ].

The right null vector is (0,1_c), while its left null vector in these rows is 1_f. Comparing the rank-one lift, exactly as for FC4, yields

    det'(Fbar_1 d)=ell^4 det A det' Delta_c det R_c^(1/2).           (FC6)

The determinant of R_c includes its constant eigenvalue 1, equivalently its determinant on mean-zero scalars. These constants and all Gram/ghost factors are retained before any coefficient is taken. Dropping J P_c0 J* while continuing to use FC6 is an inconsistent quotient.

### 1.3 The four harmonic one-form kernels and their exact Gram factors

The constant one-form space has dimension h=4(N-1). Its persistence is exact for every commuting background and residual, not only at rho=0. Add a constant Cartan one-form a to the fine field and L^j a to level j. Every S4′ contour is multiplied by the same commuting endpoint phase; the normalized phi is unchanged when both of its endpoints are shifted this way. Wilson curvatures are unchanged. Thus the composite soft action is invariant under (U,V)->(U+a,V+ell a), m(U+a)=m(U)+ell a, and rho is unchanged. The complete joint Hessian, including h before its elimination, has a fixed common harmonic kernel. The h component of that kernel is zero. Neutral d, all Hodge projectors, and the root-mean correction are background/residual independent.

Counting norms matter: for a constant fine link value a, ||a||_fine²=ell^4 V_c |a|² and ||ell a||_coarse²=ell² V_c |a|². Thus elimination of the coarse block embeds a normalized fine harmonic vector with squared Gram 1+ell^-2; elimination of the fine block embeds a normalized coarse harmonic vector with squared Gram 1+ell². Both factors are constant in U and rho. They must not be replaced by one another or omitted from finite pseudodeterminant identities.

For a positive block matrix with a fixed kernel which is the graph (-A^-1B z,z) of the null space of its Schur complement, direct rank-one regularization gives

    det' [[A,B],[B*,C]] = det A det'(C-B*A^-1B)
                         det_kernel(1+B*A^-2 B).                  (FC7)

This identity, applied on the fixed neutral gauge quotient, produces exactly the two factors above. The harmonic-lift shear fixes the joint harmonic vectors and their orthogonal complement, so it introduces no further harmonic factor. The h kernel is the fixed constant Cartan scalar and is removed on the same coarse mean-zero space throughout.

Consequently the finite neutral A5 representation of Delta_n uses L_per=H_loc+diag(d Q_per d*,d_c d_c*) and reads

    Delta_n = 1/2 log det' L_per -1/2 log det' W
              +log det' S -1/2 log det' H_h
              +LG -1/2 log det' Delta_c -(h/2)log(1+ell²),          (FC8)

up to the same overall background-independent determinant convention as the original normalized density. The prime on L_per removes its h fixed joint harmonic vectors; on W it removes its h fine harmonic vectors; scalar primes remove the N-1 constants. LG retains all transverse coarse one-forms, including their harmonics. FC8 equals the original Delta_n at the actual saddle; away from it its right side is an auxiliary function, as in the reviewed charged argument.

At rho=0, the coarse-block determinant is det C^-1 det R_c^-1, H_h=G_c, and the exact level quotient identity is LG=(1/2)log det C+(1/2)log det'G_c-(1/2)log det'Delta_c. Coarse elimination in FC8, including its harmonic factor (1+ell^-2)^h, then gives

    R_per(U,m(U)) = Gamma_Fbar1(U)-Gamma_F0(U)-h log ell,
    Gamma_F = 1/2 log det'(H_W+F*F)-log det'(F d).                 (FC9)

Since H_W d=0 off shell in the neutral sector, Gaussian gauge completion gives Gamma_F independent of F on these fixed domains. One can also differentiate it by the Nielsen identity: its right side contains H_W d and is zero. Hence the U-dependent part of FC9 vanishes **exactly**. The finite constant -h log ell is the harmonic measure factor; it has zero background and residual derivatives and vanishes as a per-site density. It is not set equal to zero before the normalized coefficient is formed.

This cancellation retains FC1 and the polar quartic term: their contributions are canceled by the other actual determinants in R at rho=0. Nothing here asserts that W^perp or the neutral level finite part is zero.


### 1.4 Complete neutral residual response and its volume bound

At the actual local h=1 tree section, set R_0(U)=R_per(U,m(U)) and R_rho(U,rho)=R_per(U,m(U)e^rho)-R_0(U). FC9 makes every background derivative of R_0 zero. All first neutral vertices at (1,0) vanish by FC2 and the commuting-colour cubic identity. Therefore the complete second variation of R_rho contains only the mixed and repeated-residual tadpoles, with the same four determinant weights as the charged source:

    L_per: +1/2,    Delta_c: -1,    G_c: +1/2,    H_h: -1/2.       (FC10)

The Delta_c contribution is identically zero in the neutral sector, since d_c is constant. Each of the other three is its full actual second vertex, not its principal symbol. For a weighted log determinant w log det O,

    D_A D_rho = w Tr(G O_A,rho),
    D_rho²   = w Tr(G O_rho,rho),                                (FC11)

because O_A=O_rho=0 at the origin. Equivalently the general formula retains -w Tr(G O_A G O_rho), which vanishes here; its coefficient is not altered. Massive determinants created by a Schur elimination are retained and give analytic tadpoles.

The new neutral mixed vertex has a useful exact Ward zero. A neutral fine gauge change adds d lambda to U and d_c ev lambda to m(U), while rho and all neutral quantum coordinates are unchanged. Thus every O(U,rho) in FC10 is invariant. After composition with the local tree section, differentiating in rho gives

    sum_mu d_mu(P) O_{A_mu,rho}(K;P,-P)=0.

The vertex is a jointly analytic symbol of K,P at fixed n: it consists only of local tensors and massive inverses before the remaining free massless propagator is inserted. Set P=s e_mu and use analyticity to obtain O_{A_mu,rho}(K;0,0)=0 for every K. Compactness of the real K torus gives the uniform bound C_n |P|. The repeated-rho vertex is bounded by C_n. This argument uses the neutral transformation of the residual; it would be invalid for an externally projected nonlocal coefficient.

For L_per, the local part has the reviewed simple-pole free low block and a fixed-depth high gap. The extra root-mean term in FC3 is independent of both background and residual and lives only at coarse K=0. On that fibre the four harmonic vectors are removed; its remaining compression and that of the local part are strictly positive. Adding the nonnegative root-mean correction cannot close that gap. Consequently the difference of their free inverses has bounded norm C_n and rank bounded by the cell size, independent of T. Their second vertices are identical, since that correction has no derivatives. Its entire per-site tadpole difference is bounded by C_n T^-4 times the corresponding vertex norm. This proves negligibility here; spatial finite rank alone would not have proved it.

For G_c and H_h, the constant kernel is fixed, the free inverse has only a |K|^-2 pole off K=0, and the omitted constant is never inverted. Dyadic counting on the periodic mesh, with K=0 omitted, gives

    T^-4 sum_{K!=0} lambda(K)^-1 <= C.

The same bound controls the L_per low block; all high terms are bounded. Combining it with FC11 and the actual local external maps U_1=zeta_n v, rho_1=C_n H_n(P)v=O(P²), gives, at fixed n,

    |[epsilon²] Delta_neutral / (epsilon² Wilson density)|
       <= C_n (|P|+|P|²)                                       (FC12)

for admissible small nonzero periodic P, uniformly in T. Constants depend on n,N,L,kappa, not T. The harmless fixed harmonic constant in FC9 has no epsilon coefficient. The same estimate holds in the thermodynamic limit by Riemann-sum convergence of the single-pole tadpoles. Hence

    Rho_n^neutral=0 for every fixed n.                          (FC13)

This zero is for the **complete remainder**. The finite coefficient FC1 persists in the fine Wilson group, and the analogous quartic neutral tadpole persists in a^perp(J_n). They are included in TEL's finite-part difference. FC13 does not set either finite part to zero or prove it is bounded as n grows.

## 2. Identification with the original infinite-volume full-colour coefficient

### 2.1 Exactly which periodic regulator is compared

FLOW Def F-g is an infinite-volume coupling definition; UIR55's final neutral erratum specifies the a.e. Bloch-fibre version of its determinant split. We compare that Gaussian/Taylor coefficient, not a new nonlinear boundary-condition theory. A Cartan external plane wave makes the actual Hessians and every one-loop vertex block diagonal into the Cartan space and real root pairs. Choose a regular unit Cartan H to avoid accidental zero root charges; the final scalar coupling is determined by that choice because the original full infinite-volume Hessian is globally Ad invariant. No non-Cartan mixed external vertex is inferred from a single twisted pair.

At finite periodic T, use a **translation-invariant Taylor regulator**: at the trivial background each free inverse is its inverse on the orthogonal complement of its exact kernel and zero on that kernel. Retain the actual massive q=0 fine fluctuation block where the soft term fixes the constants, as required by FLOW's RFL3-fix S3-5; do not replace it by a nonexistent massless Wilson inverse. Constants of the scalar Laplacian and the four harmonic modes of the purely massless Wilson/tree vector blocks are treated separately. Vertices are the actual unminimized normalized action jets, and all identities are differentiated with their prescribed Gram and ghost factors before a coefficient is grouped. A compression to a fixed free complement is a Taylor regulator; it is **not** asserted to be the exact nonlinear pseudodeterminant across a charged stabilizer-rank change.

For neutral fields, §§1.2–1.4 already give exact finite periodic fixed-kernel determinants, with a direct uniform bound. For a root pair, the independently reviewed common antiperiodic regulator gives ordinary invertible determinants. The question is whether its limit equals the original a.e. Bloch Gaussian trace and the translation-invariant periodic Taylor regulator just described. The next lemma proves that equality at the needed fixed nonzero external momentum. It makes no assertion about a globally site-pinned Green function, whose constant long-range component could invalidate this proof.

### 2.2 Exceptional-fibre lemma, including the regulator defect

Fix n and P!=0, and choose admissible P_T->P with volume T->infinity. A two-background coefficient contains only momentum transfers 0,+P_T,-P_T. Each local jet is the periodization of a fixed-depth exponentially summable kernel, so its symbol and its derivatives are bounded uniformly in T. Massive free inverses have the same property. Every massless acoustic free inverse off its zero fibre obeys C_n/lambda(K); its value on the zero fibre is the bounded high inverse with the acoustic kernel set to zero.

On fibres for which every intermediate momentum is nonzero, the finite normalized Schur, gauge-row and ghost identities are ordinary matrix identities. Differentiating them twice gives exactly the charged source's grouped expressions, with every cyclic momentum shift accounted for. Periodic mode excision changes inverse identities to

    G_0 O_0=O_0 G_0=1-P_0,                                    (FC14)

with P_0 the **finite-rank Fourier kernel projector**. It is not legitimate to replace the right side by 1. To track the correction, expand the finite sequence of block eliminations and their first/second derivatives, and at each inverse cancellation replace 1 by (1-P_0). Telescoping this replacement expresses the exact discrepancy as a finite sum of cyclic words, each with at least one P_0. The same procedure tracks a fixed-domain compression or a missing kernel Gram: its additional terms contain the corresponding constant-mode projector. This is an algebraic identity for the regulated Taylor coefficient, not a claim that the unregulated identity still holds at K=0.

Crucially, P_0 anchors the loop momentum at an exceptional fibre. Every other factor in that word is evaluated only at 0,+P_T or -P_T (up to the fixed alias identifications). At zero its free inverse is either zero on the omitted acoustic space or bounded on the retained high space. At +/-P_T its inverse norm is bounded by C_n(1+|P|^-2), for T large enough. There is **no** inverse at a distance 1/T from zero in such a correction word. If m_n is the maximum number of inverse factors in this finite twice-differentiated calculation, the sum of these corrections satisfies

    |normalized trace of all exceptional words|
        <= C_n T^-4 (1+|P|^-2)^m_n -> 0.                       (FC15)

Here m_n is finite because the action at fixed depth and its order-four stationary derivatives require finitely many matrix products and inverse differentiations; its value is not used uniformly in n or P. FC15 is a support-and-inverse estimate, stronger than the unjustified assertion “a finite-rank change is negligible.” It explicitly permits divergence as P->0 before volume; that reversed order is not used.

A local derivation of any inverse differentiations needed above is obtained by multiplying the fixed-complement matrix identity and differentiating: dG=-G(dO)G and d²G=G(dO)G(dO)G+G(dO)G(dO)G-G(d²O)G, with the fixed projectors on the outer domains. Thus no derivative of a pseudoinverse with a changing kernel has been assumed. All background derivatives of moving covariant frames in the charged proof remain actual local vertices, already included in its report.

### 2.3 Nonexceptional sums and the order of limits

The actual charged grouping has the proved mixed numerator bounds (1,2), (2,1), (2,0), where (a,b)=|K|^-a|K+P|^-b, and its repeated-residual bubble has at worst (2,2). Each separate centre is integrable in four dimensions for fixed P!=0. The neutral terms have only one |K|^-2 propagator. On either the antiperiodic mesh or the periodic mesh with the singular fibres omitted, dyadic shell counting gives

    T^-4 sum_{0<|K-K0|<r} |K-K0|^-s <= C_s r^(4-s),  s<4.

For the antiperiodic mesh the ball is empty below its first mesh point; for the periodic mesh the centre is omitted. A periodic external momentum translates either mesh into itself. At fixed P the two centres are separated. Away from small balls about them, convergence is ordinary Riemann-sum convergence of the same actual analytic symbols. The displayed estimate makes their small-ball contributions uniformly small. Hence both regulators converge to the **same grouped Brillouin-zone integral**. Adding the exact exceptional correction FC15 does not change the periodic Taylor limit.

Only after this equality is established is P sent to zero. The mixed charged kernels are uniformly integrable also as the two centres merge, by xy²<=(x³+2y³)/3 and its reverse. Their continuity and Ward pairing give zero after multiplication by rho_1=O(P²) and division by the Wilson P² density, as proved in the frozen report. The repeated-residual (2,2) bound is C_n[1+log(1/|P|)] after volume, and its two O(P²) external factors make its normalized limit zero. FC12 handles the neutral block directly.

Thus the paired-root antiperiodic calculations are used as a common regulator for each closed Gaussian block, and are removed before summing the physical infinite-volume coefficient. No assertion that simultaneous -1 twists of all root spaces define a Lie-algebra automorphism, a full SU(N) bundle, or the original nonlinear finite-torus theory is needed or made. The equality is proved by the actual grouped coefficient and FC14–FC15, rather than by an unproved flux-sector equivalence.

Candidate conclusion at this checkpoint:

    Rho_n^full = Rho_n^neutral + sum_{positive roots} Rho_n^{real pair}
               =0,  for each fixed n>=1,                        (FC16)

in FLOW's original infinite-volume/a.e.-Bloch one-loop consumer, with volume first and P->0 second. This is an author result pending independent review of the new neutral/domain/comparison steps. The separately specified periodic Taylor regulator has the same limit. The result does not identify a nonlinear finite-torus stabilizer integral with its Gaussian expansion, supply the SF-infinity polymer bound, or justify a site-pinned regulator. Those claims are outside FC16 and have not been smuggled into the coupling definition.


## 3. Depth dependence and the next constructive producer

### 3.1 What FC16 supplies to the all-increments requirement

The zero in FC16 is a coefficient **after** the prescribed limits at each fixed n. Therefore its values satisfy |Rho_n-Rho_j|=0 for all j,n; no bound on the n-dependent local constants is needed for that particular conclusion. It does not permit interchanging n with either limit. In [the independently checked UIR reduction](CODEX_REVIEW_UIR.md), the remaining one-loop increment is then

    B_n-B_j = beta0_std (n-j)log L + a^perp(J_n)-a^perp(J_j).     (FC17)

Uniform boundedness of the finite parts would give the required additive error. The weaker condition |a^perp(J_n)-a^perp(J_j)|<=r(n-j)log L+C with r<beta0_std would give a positive lower slope beta0_std-r. Neither condition is established by FC16. In particular FC1 is not a substitute for bounding the level-n neutral finite part.

The actual producer hypotheses were reread in [BFT34_55 §§0.2–1.3](BFT34_55.md): H1 is the uniform complex fixed-point/holomorphy package, H2 is its weighted cc-source and data inverse estimate, and H3 is the required weighted source locality. [Recovery §3.4](RECOVERY_UIR_ASTRA.md) and [its independent review](REVIEW_RECOVERY_UIR_ASTRA.md) transfer that package to the common weighted jet class, with the corrected same-link term and a checked smaller rate. The present fixed-depth gaps do not prove those uniform hypotheses.

### 3.2 A genuinely smaller neutral quartic producer

The commuting calculation supplies a new exact formula that removes the nonlinear source/exchange problem from the **neutral quartic** producer. Let a_j(v) be the linear stationary chain with a_n=v, f_0=d_2 a_0, r_j=a_{j+1}-Q_j a_j and z_{j,T}=theta_T(a_j)-avg_T theta_T(a_j). For a Cartan v, the complete homogeneous fourth-order tree value is

    T_{n,4}(v)= -(1/(24N)) sum_{fine plaquettes,c} f_{0,c}^4
       +(kappa/N) sum_{j<n,coarse links,c}
          [ r_{j,c} avg_T z_{j,T,c}^3/6
           -r_{j,c}² avg_T z_{j,T,c}²/4-r_{j,c}^4/24 ].           (FC18)

The proof is stationary power-series substitution: the quadratic energy is stationary on the linear chain; the cubic energy with neutral inputs and every possible internal colour is zero; hence the unknown cubic correction to the chain drops out of the degree-four value. The quartic term is exactly the sum of FC2 and the Wilson quartic on the linear chain. This is a statement about the actual normalized action, not a quartic ansatz. It does not set any displayed term to zero.

This reduces this part of the producer to explicit **linear curvature/residual transfer kernels at the trivial field**. To show precisely what rate would suffice, suppose those scalar response kernels, attached to a level-(j+1) link x and with s=n-j-1, obey weighted row and column bounds

    sup_x sum_y |R_j(x,y)| exp(m dist_n(x,y)) <= A theta^s,
    sup_y sum_x |R_j(x,y)| exp(m dist_n(x,y)) <= A L^(4s) theta^s,
                                                                    (FC19)

for each r_j and z_{j,T}, and the analogous f_0 bounds with s=n. Here all distances are in top-level units, and theta<1/L; A,m,theta must be independent of n,j,T. The contour multiplicities and fixed geometric offsets cost only constants depending on L,N,kappa. Expanding each product in FC18, anchoring one external leg, using the column bound for that leg and row bounds for the other three, and using diam(y_1,...,y_4)<=sum_i dist_n(x,y_i), gives

    |||D^4 T_n(1)|_Cartan|||_m
        <= C(N,L,kappa,m) A^4 sum_{s=0}^n (L theta)^(4s)
        <= C A^4/[1-(L theta)^4].                               (FC20)

Thus a strict curvature-transfer contraction theta<1/L suffices for the neutral quartic jet. The expected engineering scale theta=L^-2 has substantial room; that expected scale is not used as a proved estimate. At the opposite end, bounding only the uncurled one-form response by its engineering amplitude L^-s gives a contribution of order one at every level and only an O(n) bound. That failed absolute-value route does not settle the positive-increment requirement, because its coefficient has not been bounded below beta0_std.

FC18 and the conditional estimate FC20 are constructive leverage, not a claim that FC19 is verified for the actual chain. The first exact linear identity to exploit next is r_j=kappa^-1 H_{j+1} a_{j+1}, from the envelope derivative of the bottom j+1-step quadratic minimum. Each spread z_{j,T} is a fixed plaquette Stokes sum of f_j, since all contours have the same endpoints. Hence the needed responses can be attacked through the actual Gaussian curvature prolongation and H_{j+1}; they do not require guessing nonlinear fourth-order vertices. Deriving the uniform weighted row/column constants for those actual kernels remains the next decision. The full charged cubic/quartic producer still includes its cubic-source exchange and is not closed by the commuting restriction.

## 4. Evidence, preserved failures and review handoff

The exact [first criteria](checks/residual_full_colour_01_criteria.md) preceded [implementation 01](checks/residual_full_colour_01.py). Its single [complete output](checks/residual_full_colour_01_out.json) has **34/34** predicates, with [empty stderr](checks/residual_full_colour_01_err.txt). It constructs a periodic nine-site/three-root scalar graph independently from incidences, checks the two pseudodeterminant definitions, retains the root-mean term, and rejects its omission. It also checks both harmonic graph Gram factors, their differentiated cancellation, the actual 3^4 neutral Wilson tadpole and SU(N) Cartan completeness for N=2,3,4, the actual SU(2) contour modulus expansion and stationary quartic substitution. These exact finite examples support the algebra; the general domains and bounds are proved in the text.

The [second criteria](checks/residual_full_colour_02_criteria.md) preceded [implementation 02](checks/residual_full_colour_02.py). Its single [complete output](checks/residual_full_colour_02_out.json) has **25/25** predicates, with [empty stderr](checks/residual_full_colour_02_err.txt). It constructs the 3^4 periodic Laplacian directly in position space and solves its five radial-orbit equations, then verifies the full rank-one inverse equation. The exceptional words Tr(P_0 V G^r V) are nonzero: 1/6, 1/18, 1/54 for r=1,2,3, before division by 81. Their fixed-P density vanishes, while the P=2pi/T, r=2 density tends to 1/(32pi^4). The latter is an exact rejected order-of-limits shortcut.

The global-pin failure is also explicit: the mean-zero Green diagonal is 104/729, while the normalized trace of the origin-pinned inverse is 208/729. The exact pin formula includes G_perp(x-y)-G_perp(x)-G_perp(y)+G_perp(0). Deleting its constant term fails the inverse equation. This preserves a concrete counterexample to generic finite-rank negligibility; it is not a no-go for a separately proved full normalized pin cancellation. A two-dimensional moving-kernel example also has a nonzero second logarithmic Gram term which a fixed-complement determinant misses. That failed substitution is not used in the neutral fixed-kernel proof or in the explicitly Taylor-regulated charged comparison.

No predecessor helper was imported by either implementation. No unexpected failed predicate or stderr was discarded; the planned wrong-formula controls all reject. The sources, controls and input hashes are bound by [the input snapshot](checks/residual_full_colour_inputs.json) and [the freeze manifest](checks/residual_full_colour_manifest.json). The complete [harmonic-bridge review](REVIEW_RESIDUAL_LATTICE_BRIDGE_ASTRA.md) was reread for its fixed-depth scope and periodic exception. The narrow current-main source search at ca2bc7ddf64790da96cd43d42017d000fbfe4808 for neutral/residual and periodic/excision phrases returned no lane hit; the directly matching open-proposal predecessors were read and identify this exact bridge as outstanding. No claim of literature priority is made.

Author claim certificate: `actual_current_surface_status: exact-support`; `target_claim_type: bounded_theorem`; `trace_class: upstream_support`; `reachability_to_target: partially_closes`; `bare_retained_allowed: false`; independent review of this unit is pending; independent audit remains required before any effective retained status. The accepted model premises are precisely the supplied SU(N), Wilson, normalized phi/S4′ chain and the specified perturbative coupling convention. The current primitive registry was checked at the pinned main revision; its scale, kinetic-form and realized-state primitives supply no missing determinant, uniform source, or physical spectral-gap theorem.

The strongest candidate result is FC16, with FC1–FC15 making its neutral and regulator content explicit. The direct downstream gain would be removal of the full-colour one-loop residual from FC17 after independent review. It does not supply H1/H2/H3, the nonlinear small/large-field remainder, the finite-torus polymer comparison, OS existence/reconstruction or a positive gap of the physical Hamiltonian. The full existence **and physical mass-gap** target remains active. The next constructive calculation is the actual weighted Gaussian curvature transfer in FC19, while the coordinator independently reviews this frozen coefficient unit.
