## Explicit background-disk columns and a shorter nominal output window

**Checked conditional refinement.** This refinement keeps the exact nominal kappa=10^-8, sigma=10^-6 Hamiltonian and target, and gives complete infinite operator error<.000320 for all t>=T_disk=10^19. A single fixed finite device with M_disk=50T_disk=5e20 output sites has error<.001320 on[T_disk,2T_disk]. This preserves the preceding error pair while reducing sufficient onset and length by400 from T=4e21,M=2e23. An alternate T=4e18 tradeoff, with slightly larger error, is stated separately below.

All inherited interval/calibration/kernel and supplied physical premises remain. The actual f,p0, phase113, old K/W, common scalar, delivered product seed and literal complete-output comparator are unchanged. The new argument bounds the complete background incoming and selected endpoint columns directly on the already established radius10^-12 complex disks. It does not apply a whole-background Neumann estimate at the deeper emitter strip.

These refinements concern exact nominal parameters only. The compensated-precision and structural-precision corollaries retain their separately checked T=4e21 onset unless their perturbed disk-column and complete-output estimates are re-established. No shorter robustness onset follows from this nominal result.

### 1. Background kernels on the already established disks

Use disks |w-k|<=rho=10^-12 centered at every k in I, including endpoints. The canonical larger-coupling proof already gives analytic bare M16 inverse<167, A<41, Tg<208, closed roots<.15, full two-site response inverse<2100, |r_g|<1.001, |R_bg|<2e-5, and endpoint comparison error<2e-21. All projectors remain fixed and matrices complex symmetric. No off-real unitarity is used.

The bare contact-contact blocks are controlled by167. Contact/exterior blocks are the contact inverse times the appropriate decaying/outgoing Q powers from the same block elimination; these have norm at most167 exp(L rho). Exterior/exterior blocks are A Q^|n-m|+Q^(n-1)Tg Q^(m-1). All relevant path distances are finite and below226; exp(226rho)<1.001. Thus a common bare site-block ceiling260 safely covers contact, arm and exterior positions needed below. This is the canonical real <250 argument repeated with its actual disk constants, not analytic continuation of a real norm inequality alone.

The two-site filter update costs at most

    2*260^2*.05*2100=14196000

per site block. Including260 gives <1.5e7. Mixing the two arms by the fixed real orthogonal U costs at most a factor2 for an individual physical block with mixed indices, hence every pretermination physical block needed for the retained core and deleted input site b is <3e7. The same exact identities establish analyticity; no norm-smallness condition on a 896-dimensional inverse is needed. Output-tail self-energy is still the physical outgoing branch.

At end=ell and b=ell+1, the exact pretermination block is G(b,end)=Q(A+X). The canonical disk construction has ||A+X||<42, ||Q||<1.001, and ||Gbb^-1||<23. Consequently every retained selected endpoint block after deletion is bounded by

    ||Gtr(s,end)||<3e7[1+23*1.001*42]<3e10.

There are112 retained background positions, so

    P_disk=||R_bg E_end||<sqrt(112)*3e10<3.2e11.    (1)

This keeps all eight internal coordinates in every block; no factor eight belongs in this block-column norm. Generic terminated blocks are also bounded by3e7+23(3e7)^2<2.1e16, but that larger estimate is unnecessary for the incoming column.

### 2. Direct incoming column before termination

Consider unit incidence from one exterior port of the two-port background. Before filtering, the exact bare contact solve has norm<11, from167*.063. The exterior continuation is psi_n=z^-n u+Q^(n-1)(psi_1-z^-1u). Its contact contribution and two unit-wave contributions, including finite disk growth, give a safe per-site ceiling14. Its restriction to two filter sites has norm<sqrt(2)*14<20.

The filter correction at any site is

    G_bare(s,Fpair) V (I-G_Fpair V)^-1 phi_bare(Fpair).

Its norm is at most sqrt(2)*260*.05*2100*20. Including the unmodified source and allowing a further factor2 for conversion between the two arm and physical-port coordinates gives a uniform per-site pretermination incoming bound <2e6. Every retained contact, arm and input site is included. This is deliberately loose, but follows from the explicit driven matching solution instead of R_bg times a large generic column bound.

The special vector at the deleted input site is much smaller. There is no incoming wave on that port for the chosen output incidence. Its open amplitude is the transmission coefficient times z^(ell+1). On the disks each bare/modified scalar reflection has modulus<1.002: use |r_g|<1.001, scalar mismatch<3e-5 and the analytic closed error<3e-20. Orthogonal U mixing and the common phase exp(90iw) then give the loose bound |tau|<2. Hence

    ||P phi(b)||<3.

The closed part comes from the off-diagonal exterior kernel. The disk Ttilde bound2e7 and the24 filter-to-port plus21 port-to-b powers yield

    ||Pc phi(b)||<=.062*(2e7)*(.15)^45*1.001<1e-25. (2)

For distinct ports a,o the exact kernel is G_ao(m,n)=Q^m T_ao Q^n. Outgoing coefficient extraction gives phi_a(m)=iE' Q^m T_ao u, up to the fixed reference phase: iE' Aopen=1 fixes unit incidence on port o. Since T_ao,PP=Aopen tau, its open part is tau z^m u. Thus the factor .062 bounds the unit-incoming E' source factor; the incident open leg contributes only its bounded phase. There is no free cross-port closed term. This follows from the same outgoing-coefficient/source identity used by the canonical two-port kernel, with the incident port column projected onto its one open channel.

### 3. Projected Dirichlet deletion is the important step

The actual terminated incoming solution is exactly

    x_bg(s)=phi(s)-G(s,b) Gbb^-1 phi(b).             (3)

The incoming amplitude on the surviving output remains one, since the correction is outgoing there. A generic bound23 on Gbb^-1 would unnecessarily enlarge this column. Instead use the canonical disk diagonal approximation D_b0=A+QX0Q. Its OPEN inverse has norm

    |Aopen^-1/(1+R_bg exp(42iw))|<.063.

Its full inverse is<22, and ||Gbb-D_b0||<1.001^2*1e-27. The inverse identity therefore gives

    ||Gbb^-1-D_b0^-1||<23*22*1.001^2*1e-27<6e-25.

Together with(2), ||Gbb^-1 phi(b)||<.063*3+23e-25+6e-25*(3+1e-25)<.2. Thus(3) and the pretermination3e7 kernel ceiling give every site amplitude <2e6+.2*3e7=8e6. Summing over112 sites yields

    X_disk=||x_bg||<sqrt(112)*8e6<1e8.             (4)

All vectors here are finite background core vectors with the exact outgoing boundary attached. They are not l2 norms of analytically continued open waves. Closed tails enter later in C. Equations(2)–(3) and the open inverse estimate, rather than a presumed small whole resolvent, are the essential checked interface; the unchanged source ancestry remains conditional.

### 4. Deeper strip at the same coupling

Choose h=10^-15, which remains inside every established disk. The exact endpoint matrix has ||G||<36 there. Operator Taylor/Cauchy gives

    ||G(k-iy)-G(k)||<=36*.001/(1-.001)<.036037.

The complementary emitter inverse stays<6; its two endpoint Schur corrections together are<1.6e-12. Therefore exact self-energy oscillation is<.037. The real ImDj>12kappa^2 and energy change .062h imply

    ImDj(k-iy)>[12-.62-.037]kappa^2>6kappa^2.

This retains all seven complementary coordinates and uses the actual complex self-energy. The whole-core analytic inverse follows by exact Schur factorization. It is not obtained from .1*2.24e18*h, which would fail.

Using the loose disk G ceiling36, the emitter complementary gap exceeds .18-.062h-36kappa^2, so d_c<6. The rank correction1+kappa^4 d_c^2*36^2 is negligible and

    ||De^-1||<.18/kappa^2 on the bottom.

On either vertical side, v sigma-.061h^2-36kappa^2-6kappa^4*36^2>2.49e-8, hence ||De^-1||<5e7. The selected endpoint column(1) gives sqrt(1+kappa^2 P_disk^2)<3201.

The exact source formula x=[x_bg;0]+V[-kappa De^-1 E_end^T x_bg] consequently yields, with the unchanged complete localized definition ||C||<=3||x||+4,

    C_b<3*1e8[1+1e-8*3201*.18/1e-16]+4<2e19,
    C_s<3*1e8[1+1e-8*3201*5e7]+4<5e11.          (5)

The full904 coordinates and all closed tails are preserved. Roots<.15<1/6 ensure the same uniform holomorphic tail map. Actual R_inst=u^T x-1 enters the algebraic open-wave subtraction; its modulus is not set to one off-real.

### 5. Complete localized escape and scalar tails

Keep a0=conjugate(omega_p f), with its already paid outgoing discrepancy, full phase113 and positive actual reference normalization. At h=10^-15 the exact conjugate denominator has imaginary part

    -sin(x)[2J sinh(y)+(kappa^2/J)exp(-y)].

It is nonzero and gives bottom |a0|<.088/kappa. The cutoff real-part margin stays>.024sigma, giving side |a0|<44kappa/sigma. No1/R_inst derivative enters this paid alternative coefficient. With both vertical sides and the within-parity overlap factor included,

    E_loc(t)<=1.5[sigma*(.088/kappa)*C_b exp(-vth)
                         +(44kappa/sigma)*C_s/(vt)].

The bottom prefactor from(5) is2.64e20. At T_disk=10^19, vT_disk=2.5e17 and vT_disk*h=250, so its contribution is<3e-55, using exp(250)>2^250>10^75. The two-side contribution is<1.32e-6. Different parities are orthogonal and passive-reference tensoring preserves the operator estimate.

For scalar incoming and target tails, keep their separately justified h_i=sigma/2 and h_o=kappa^2/(4J^2)>2.5e-14. C is not continued to these larger heights. The target retains phase113 in v t-113 and both cutoff edges. It is enough to bound these tails at the earlier alternate time T_alt=4e18, since their ceilings decrease thereafter. There vT_alt=1e17 and

    88kappa/[sigma sqrt(pi(vT_alt-113))]<1.7e-9.

The target bottom has exponent>(1e17-113)*2.5e-14>2400 and prefactor .012sigma/kappa^2=1.2e8. The previously used fourth-power exponential estimate is insufficient at this shorter time. Instead the positive exponential series gives exp(-a)<=10!/a^10; for a>2400 this makes the bottom<1e-18. The incoming bottom is smaller still. Consequently both incoming norm error and target negative-tail norm are<2e-9 for t>=T_alt. Positive target normalization costs<4e-18. This is normalization of the target already restricted to the positive half-line, not postselection of the physical state or deletion of its residual spectrum.

### 6. Nominal complete error and one fixed finite device

Retain the canonical exact static expression, rather than rounding it upward to .000319:

    S<1.415*(.000221+.0000016+.0000000454)+.0000032
       =.000318243241.

At T_disk=10^19 the full sum is therefore

    complete infinite operator error
      <.000318243241+.00000132+.000000002+4e-18+3e-55
      <.000320.

It holds for every t>=T_disk. The comparator includes exp(-ic_new t), the same positively normalized actual common beta_t, blank emitter/other-clock/source registers, and exp(-itK)W on the literal old system with any passive reference. Actual exterior point/other spectral mass, full core/source/emitter and closed tails, complex phase and entire elapsed old aging remain charged. No setup duration or column-dependent phase is hidden.

The nominal Hamiltonian is unchanged, so its radius18 and first omitted distance M+23 remain valid. With M_disk=50T_disk=5e20, the canonical finite transfer through2T_disk is

    4 exp[-(M_disk+23)+36T_disk sinh(1)]/[1-exp(-1)]<.001.

Thus the fixed finite device has error<.001320 on[T_disk,2T_disk], with M_disk+116 total qubits. The comparison uses the same infinite target embedded in the infinite space, without finite-waveform renormalization. Unhalved trace ceilings are .000640 and .002640. No all-future finite storage or permanent halt is asserted.

### 7. Separate earlier-time tradeoff

At T_alt=4e18 the same h gives vT_alt*h=100. The localized bottom is<2.64e-10, using exp(100)>10^30, and the two sides are<3.3e-6. Hence localized error<3.301e-6. The scalar tails just proved remain<2e-9 and normalization<4e-18. Even using the looser static ceiling .000319 gives

    infinite operator error<.000319+.000003301+.000000002+4e-18
                            <.000323.

For a separately fixed device M_alt=50T_alt=2e20, finite error is<.001323 on[T_alt,2T_alt]. Unhalved trace ceilings are .000646 and .002646. This alternate tradeoff reduces sufficient onset and length by1000 relative to4e21/2e23, but does not preserve exactly the .000320/.001320 pair. These are sufficient dimensionless model bounds, not measured or optimal resources.

### Source history, independent check and scope

This prose consolidates background_disk_runtime/PROPOSAL.md SHA2562d1da7e51d68377d164f2529f7e6430e36ffb333a1241a694c4e75d9949ebf4c, based on the canonical note SHA256d17d5e32f3f44f162aff15ced734238ba1543212525d618d36dc95511095c4be at root-reported milestone7dcc98203477cf9868dc9b7f7dd2aeccffeda9a3. Root exposed the direct disk-column idea and subsequently the same-tolerance arithmetic refinement. The drafting agent authored the proposal and earlier weighted work and reviewed reused components. This is drafting after development, not another independent verification. The selective same-model independent check background_disk_runtime_check/REVIEW.md (SHA2564789b360ecf4df8116f8735640ad9cb852e9cced24fb11ba1952a508128ddbe1) reconstructed the complete disk/source/deletion and contour implications, including the changed exponential remainder. It was source-exposed and did not independently recertify ancestral calibration or apply an audit verdict.

The initial proposal SHA2567387c6fae9c711f1b7980d47cb30c78885f40a7811d11a4e8d358294afd39b13 used a bare per-site12 and pair17 ceiling. Root identified that the exterior formula includes subtraction of the incoming open wave, so the claimed12 was not justified. The corrected14/pair20 bounds above give

    2*(14+sqrt(2)*260*.05*2100*20)<2e6,

preserving the downstream pretermination ceiling. The initial12 claim is withdrawn and is not a premise here. A separate suggested half-disk harmonic-measure route was not used or verified.

The new background column proof must cover mixed contact/exterior kernels, physical port phases, all internal coordinates, source normalization and the tiny complementary boundary component. Endpoint ||G||<36 alone would not prove the complete runtime conclusion. The full rho disk is not asserted to exclude emitter poles; only the specified narrower h strip is used.

The analytical argument is not a numerical runtime experiment. The current runner corroborates only declared local/scalar arithmetic, with its actual execution record reported separately. No spectral integration, full904-matrix dynamics or parameter sweep verifies this theorem; historical runner evidence is not relabeled as a current check. No native Hamiltonian/state/coefficient supplier, physical Hamiltonian/time/energy/Record identification, general perturbation robustness, capture/reset/reuse, optimum, new topology or retained/audit status is supplied. No physical axiom or editable prompt changed.
