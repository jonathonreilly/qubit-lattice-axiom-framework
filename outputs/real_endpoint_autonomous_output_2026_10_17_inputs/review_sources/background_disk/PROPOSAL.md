# Explicit background-disk columns and a proposed deeper complete-output strip

Proposed result, not independently checked: at the unchanged kappa=10^-8 and sigma=10^-6, explicit physical kernel/source gluing appears sufficient for T=4e18, M=2e20, complete infinite operator error <.000323 and finite error <.001323 on [T,2T]. This is a factor1000 reduction in sufficient time/length relative to the published T=4e21 result, with a slightly larger error ceiling. The decisive improvement is a bound on the incoming background column obtained before Dirichlet termination, including the nearly open input-boundary vector. A whole-background Neumann continuation is not used.

Root exposed the disk-column idea before this derivation. This is new source-exposed development, not an independent origin, review or audit. No scientific execution, parameter sweep, inherited code, new agent, model change or W/Git/checkpoint/prompt edit occurred.

## Sources and fixed scope

Canonical note: /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md, SHA256 d17d5e32f3f44f162aff15ced734238ba1543212525d618d36dc95511095c4be, root-reported milestone7dcc98203477cf9868dc9b7f7dd2aeccffeda9a3. Its necessary larger-coupling disk, bridge and source/contour arguments were fully read previously; the physical kernel/filter/port/termination formulas and generic/selected-column bounds were reread for this task. No Git association was independently verified.

All source interval/calibration/kernel and supplied physical premises remain fixed. No band-center construction is used. The old K/W, common scalar, actual f/p0, phase113, product seed and literal output comparator remain the canonical kappa=10^-8 ones. Earlier authored weighted work and component reviews are exposed. This proposal needs a selective independent check, especially of the projected termination source estimate below.

## 1. Background kernels on the already established disks

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

## 2. Direct incoming column before termination

Consider unit incidence from one exterior port of the two-port background. Before filtering, the exact bare contact solve has norm<11, from167*.063; bare open waves have magnitude at most2.002 on the finite retained path, and closed components are obtained by contraction from their contact amplitudes. A generous per-site bound14 therefore covers a bare arm solution on these disks (allowing addition of open and closed estimates). Its restriction to two filter sites has norm<sqrt(2)*14<20.

The filter correction at any site is

    G_bare(s,Fpair) V (I-G_Fpair V)^-1 phi_bare(Fpair).

Its norm is at most sqrt(2)*260*.05*2100*20. Including the unmodified source and allowing a further factor2 for conversion between the two arm and physical-port coordinates gives a uniform per-site pretermination incoming bound <2e6. Every retained contact, arm and input site is included. This is deliberately loose, but follows from the explicit driven matching solution instead of R_bg times a large generic column bound.

The special vector at the deleted input site is much smaller. There is no incoming wave on that port for the chosen output incidence. Its open amplitude is the transmission coefficient times z^(ell+1). On the disks each bare/modified scalar reflection has modulus<1.002: use |r_g|<1.001, scalar mismatch<3e-5 and the analytic closed error<3e-20. Orthogonal U mixing and the common phase exp(90iw) then give the loose bound |tau|<2. Hence

    ||P phi(b)||<3.

The closed part comes from the off-diagonal exterior kernel. The disk Ttilde bound2e7 and the24 filter-to-port plus21 port-to-b powers yield

    ||Pc phi(b)||<=.062*(2e7)*(.15)^45*1.001<1e-25. (2)

Here the factor .062 is the unit-incoming Stone/source factor E'; the open input leg contributes only its bounded phase. There is no free cross-port closed term. This follows from the same outgoing-coefficient/source identity used by the canonical two-port kernel, with the incident port column projected onto its one open channel.

## 3. Projected Dirichlet deletion is the important step

The actual terminated incoming solution is exactly

    x_bg(s)=phi(s)-G(s,b) Gbb^-1 phi(b).             (3)

The incoming amplitude on the surviving output remains one, since the correction is outgoing there. A generic bound23 on Gbb^-1 would unnecessarily enlarge this column. Instead use the canonical disk diagonal approximation D_b0=A+QX0Q. Its OPEN inverse has norm

    |Aopen^-1/(1+R_bg exp(42iw))|<.063.

Its full inverse is<22, and ||Gbb-D_b0||<1.001^2*1e-27. The inverse identity therefore gives

    ||Gbb^-1-D_b0^-1||<23*22*1.001^2*1e-27<6e-25.

Together with(2), ||Gbb^-1 phi(b)||<.063*3+23e-25+6e-25*(3+1e-25)<.2. Thus(3) and the pretermination3e7 kernel ceiling give every site amplitude <2e6+.2*3e7=8e6. Summing over112 sites yields

    X_disk=||x_bg||<sqrt(112)*8e6<1e8.             (4)

All vectors here are finite background core vectors with the exact outgoing boundary attached. They are not l2 norms of analytically continued open waves. Closed tails enter later in C. Equations(2)–(3) and the open inverse estimate, rather than a presumed small whole resolvent, are the essential proposed interface to check independently.

## 4. Deeper strip at the same coupling

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

## 5. Proposed complete runtime and finite window

Keep a0=conjugate(omega_p f), with the paid static outgoing difference, full phase113 and actual reference normalization. On the bottom |a0|<.088/kappa still holds: the exact Dbar imaginary part has both terms negative, with exp(-y), and h is tiny. Side real-part margins stay>.024sigma, giving |a0|<44kappa/sigma. Both sides and the within-parity factor remain paid by

    E_loc(t)<=1.5[sigma*(.088/kappa)*C_b exp(-vth)
                         +(44kappa/sigma)*C_s/(vt)].

Set T_new=4e18. Then vT_new=1e17, vT_new*h=100. The bottom prefactor is2.64e20; using exp(100)>10^30 gives bottom<2.64e-10. The two sides give<3.3e-6. Thus E_loc<3.301e-6 for all t>=T_new.

The incoming and target scalar strips remain the source's h_i=sigma/2 and h_o=kappa^2/(4J^2)>2.5e-14. They do not require continuing C to those heights. The side term88kappa/[sigma sqrt(pi(vT_new-113))] is<1.7e-9 (pi>3 suffices). The target bottom has exponent>(1e17-113)*2.5e-14>2400 and prefactor .012sigma/kappa^2=1.2e8. The previous fourth-power exponential bound is now too loose to justify a2e-9 tail, so it must NOT be reused unexamined. Instead exp(-a)<=10!/a^10 from the positive exponential series gives this bottom <1e-18 for a>2400. The incoming bottom is even smaller. Therefore both scalar norm errors are<2e-9; positive target normalization costs<4e-18.

With unchanged static cost<.000319, the complete infinite sum is

    error<.000319+.000003301+.000000002+4e-18<.000323.

This includes the actual source/core/emitter remainder, all exterior spectral mass, old aging, physical scalar and arbitrary passive references. No phase adjustment or omitted output is used. It does not preserve exactly the older .000320 ceiling, but meets the original .0013 tolerance.

The Hamiltonian itself is unchanged. Its radius18 and distance M+23 transfer therefore apply to M_new=50T_new=2e20. Finite error is<.001323 on [T_new,2T_new], using the same embedded infinite target and M_new+116 qubits. No all-future finite storage is claimed. Unhalved trace ceilings would be .000646 and .002646.

## Next review and limitations

The proposed gain is based on explicit analytic disk gluing, not an execution result. The most important independent review is the full physical incoming solution before termination, its tiny closed component at b, and the open-projected inverse in(3). Check contact/exterior bare blocks, mixed-index junction factors, absolute port phases and source normalization. A failure there invalidates the proposed X_disk and runtime even though endpoint ||G||<36 itself remains valid.

The scalar tail estimate at the new T explicitly uses a stronger exponential-series remainder; this changed step also needs checking. No bare calibration, physical supplier, native preparation, perturbation contract, optimum or retained status is upgraded. No attempt is made to optimize h near the emitter pole or to claim the full rho disk is free of emitter resonances. The chosen h is conservative and distinct from the background-only disk radius.


## Same-tolerance variant at T=10^19

After the initial derivation root pointed out that retaining the already proved exact static expression, rather than its rounded .000319 ceiling, recovers the published error pair at a still shorter time. This is an exposed arithmetic refinement, not independent corroboration.

At T_same=10^19, vT_same=2.5e17 and vT_same*h=250. The localized two-side term from(5) is<1.32e-6. Its bottom is<2.64e20 exp(-250)<3e-55, using exp(250)>2^250>10^75. The scalar incoming and target tails are each<2e-9, since their bounds decrease from the T_new estimates. Positive target normalization remains<4e-18. The actual static expression from the canonical L10 is .000318243241, so

    error<.000318243241+.00000132+.000000002+4e-18+3e-55
          <.000320.

For M_same=50T_same=5e20 the same transfer adds<.001 on [T_same,2T_same], giving<.001320. This preserves the published .000320/.001320 ceilings while reducing sufficient onset and length by400 relative to4e21/2e23. The initially derived T=4e18/.000323 variant remains a separate tolerance tradeoff. Neither is checked until the shared disk-column interface is checked.

Root also suggested a half-disk harmonic-measure bound as an alternative to direct source gluing. It was not needed or verified here and is not a premise of either result. In particular this proposal does not silently infer a real-axis jump bound outside I or assume an unproved harmonic-measure formula.

Source-development correction: the initial draft SHA2567387c6fae9c711f1b7980d47cb30c78885f40a7811d11a4e8d358294afd39b13 used per-site bare12 and pair17. That12 ceiling was not justified by the stated contact and wave bounds. Root identified the missing open subtraction in the exterior continuation. The exact form is psi_n=z^-n u+Q^(n-1)(psi_1-z^-1u), so the contact bound11 and two unit-wave contributions require a ceiling above13 with tiny disk growth. The corrected14/pair20 ceilings above supply it, and 2*(14+sqrt(2)*260*.05*2100*20)<2e6 preserves the pretermination bound used downstream. The initial12 claim is withdrawn; no runtime bound here relies on it. This correction is recorded explicitly rather than treated as a verified earlier estimate.
