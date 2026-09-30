# Independent matrix-pin reconstruction before opening the new proof

September30,2026. Focused check, not formal review/audit. Exposure: parent disclosed the proposed improvement beyond a/(4g), nine-forward-bond form, and need to check boundary/counting/limit order. The new native-physical-cell-lower-route CONTRACT, TARGET_EXTENSION and WORKING_PROOF have NOT been opened. Current landed native source at main30a9461ee19a49b99fa6628fe942f08e504e8903 and the complete earlier checked Neumann report/receipt were read first. This PRE is derived from those actual inputs, not from new author code or expected coefficients.

The actual H0=S+mu Ddiag+W on full site qubits gives a lower positive-row comparison, with a=min(tau,mu/12). Use nine forward fields B_d(x)=b_x b_(x+d), d=2e_i,e_i+/-e_j. Axial centered amplitudes are exp(-ik_i) B_i in Fourier space. For one plane, in the order (plus displacement,minus displacement), the Q_T row is
q_ij(k)=(-(exp(-ik_j)+exp(-ik_i))/2,(exp(ik_j)+exp(-ik_i))/2).
Its squared norm is r=1+cos(k_i)cos(k_j)<=2. Put l(k)=4sum sin²(k_i/2) and P_s(k)=s(k)*s(k)/3, s=(exp(-ik_i))_i. The complete N2 S+W symbol is block diagonal:

    K_ax=2mu P_s+tau l(I-P_s),
    K_ij=2mu I+(tau l-mu)q* q.

The five constant soft vectors are the axial E doublet and one normalized signed plane vector(-1,+1)/sqrt2 per plane. This is a normalization of ACTUAL forward amplitudes, not a pair-boson replacement.

I independently obtain K>=a l I9 and, on each plane, K>=2a l I2. The axial high mass is2mu, with a l<=mu. Therefore for the infinite pin Green matrix G(0)=integral K(k)^(-1)dk/(2pi)^3,

    G_ax(0)<=g/a I3-(1/(24a))integral P_s(k)dk
             =(g-1/72)/a I3,
    G_planes(0)<=g/(2a) I6.

Since g>=1/12, the axial bound is the larger, so lambda_max G(0)<g/a explicitly. For K_epsilon=(1-epsilon)K+epsilon a l I, the same argument gives a safe strict margin

    G_epsilon(0)<=[g-(1-epsilon)/(36(2-epsilon))]/a I9,
    0<=epsilon<1.

This only proves the INFINITE symbol improvement. It does not yet prove the physical finite-cell many-body lower theorem.

Finite-cell obligation: the previously checked regularized complete-row cut
K_cell,epsilon=(1-epsilon)K_cut+epsilon a Delta_N I9
has kernel the five constant soft modes and gap>=epsilon a/(14ell²). Its energy sum is a genuine lower comparison on the full carrier, because each actual positive S/W row is selected at most once and the epsilon part uses the original gradient inequality. It does not delete neighbors inside Ddiag or assume disjoint physical tensor factors for anchor cells.

For a pin set and the complement of those five constant modes, one needs an UPPER bound on the full matrix Green compression, asymptotically lambda_max G_epsilon(0) plus vanishing offdiagonal/boundary errors. A variational trial Green function alone supplies the opposite lower bound and is insufficient. The scalar reflection formula is not available automatically for the forward internal symbol. A naive cutoff can produce an O(ell^-2) high-channel residual from the first derivative of P_s(k), so applying the ell² gap can leave an O(1) error. A high-channel corrector, a local resolvent argument with correct sign, or another complete boundary estimate is necessary. No assertion that this obstacle is solved is made before reading the proof.

If that Green estimate is valid, pin Cauchy gives m||c||²<=B_cell E and the gap gives ||q||²<=14ell² E/(epsilon a). With m<=8ell³/R³, the finite norm denominator is B_cell+112ell²/(epsilon a R³). Each actual isolated dimer removal supplies at least g_j-1 residual pins. The literal sum over output occupations and unique forward edges must be g_j(g_j-1), without a half-factor or a compatibility isometry. Other removals are positive. Particle loss, not energy erasure, is priced by checked <B_R><=C_B R³<H0>/a and the translated boundary strip.

The energy coefficient would be1/[4 lambda_max G_epsilon(0)] before epsilon removal, provided all boundary/variance errors vanish in the ordered limits. Take thermodynamic volume first at fixed density, density to zero with epsilon FIXED, then epsilon down to zero; one must not use an epsilon-dependent gap error uniformly without proving it. Soft pin capacity U*G^-1U might improve further, but a lambda_max bound is sufficient for strict improvement. Neither identifies the coefficient with the actual N4 threshold form, gives a phase, or supplies many-pair compatibility.

Independent check plan: full read all three new files; reconstruct actual row selection and boundary Green UPPER estimate, including finite versus infinite variational directions; check all constant-mode projections and internal normalizations; follow arbitrary-state extraction/particle loss; audit every exponent and limit order. No new heavy computation planned. Parent separately owns literal symbol/small-Green controls. Record all material errors or narrowed hypotheses rather than treating a symbol inequality as the completed theorem.
