# Original microscopic local comparison: narrowed residual and constructive partial results

The full volume-uniform local microscopic-to-original-rotor process comparison remains unproved. This route establishes a checked microscopic defect/count bound, a separate effective-spin-to-rotor local transfer, and a source-specific low-excitation fast absorption mechanism. The latter two author proofs are frozen for focused reading, not independently endorsed here. No counterexample to convergence from bare Omega was found. No source, primitive, audit status or native physical selection is changed.

## Contract, law and prior proof boundary

CONTRACT.md freezes fixed K,delta,kappa>0, integer S with epsilon^2 S(S+1)=delta/K, bare Omega, all even cubic tori L>=6 and a finite observed region/mark set. The required error must tend to zero uniformly in volume. The microscopic carrier and dynamics are supplied: A/B qutrits, normalized spin links, physical div E=q-1_A, the exact gate-dependent compensation and original resolved or unnormalized coherent-edge formation maps. The target is the original P rotor GKSL process with every later birth, not a harmonic, photon or counting proxy.

The exact laws are

    H_micro=delta epsilon^-4(W+epsilon T_S+epsilon^2 C_S),
    L_(m,micro)=sqrt(kappa)epsilon^-1 j_(m,S),
    C_S=sum_a(F_a^*F_a+D_a/[S(S+1)])Q_a,
    T_S=-sum_a(F_a+F_a^*),

and the final rotor target is

    h=KD-2delta sum_(unordered dist2 a,c)(F_c F_a P)^*(F_c F_a P),
    L_m=sqrt(kappa)Pj_m F_aP.

The compensated finite-graph elimination source proves uniformity in S at a FIXED graph. Its exact all-cluster rotation has graph-dependent bounds and includes the necessary O(epsilon^-1) off-block dissipative loss through a coherence correction. The closest uniform-local ring theorem instead uses dressed preparation and slow beta=beta0 epsilon^(2d), not the present bare preparation and beta=kappa epsilon^-2. The exact cited sources and read scopes are bound in SOURCE_IDENTITIES.json; no title-only prior theorem is imported. Main was refreshed to30a9461ee19a49b99fa6628fe942f08e504e8903 and the scoped open-proposal search is recorded there. No exhaustive novelty claim is made.

## 1. Checked microscopic hole density and original local counts

DEFECT_LEMMA.md is frozen at fbbf36c26413f3f678f071d610338c0fcc78ea9fa587c6874c4b19791d8351af. Its finite-color local normal form gives

    H'=delta epsilon^-4W+delta epsilon^-2D2+delta D4
                   +delta epsilon^2D6+R_H,
    [D_(2r),W]=0,  ||R_H||_local=O(delta epsilon^3).

Each ACTUAL transformed original jump J has positive W-grade component starting at epsilon^2. The exact phase-averaged drift identity is

    P_W sum_m D[J_m]^*(W)=sum_(m,r) r J_(m,r)^*J_(m,r).

Two local Hermitian observable corrections K1=O_local(epsilon^3), K2=O_local(epsilon^5) cancel the leading off-grade drift and its next off-grade transport. The remaining drift is at most C epsilon^2 per center plus a nonpositive negative-grade activity term. Local projection estimates price the bare preparation and convert back from the dressed frame. With constants independent of S and volume,

    Tr(w_a rho_micro(t))<=C epsilon^2(1+t),
    E N_F([s,t])<=C kappa |F| integral_s^t(1+u)du.     (M1)

An overflow event N_F([0,T])>M has probability at most C kappa|F|(T+T^2/2)/(M+1). This is an unconditional count bound. It is not a conditional hazard bound or an observation of jump grades.

The complete independent receipt is ../independent-microscopic-defect-check/REPORT.md, SHA6ba247842db37d73cf8310b2ffe8fad169e5eb7ca836ae3b9e05bdfff22eabcc as bound in SOURCE_IDENTITIES.json. It reconstructed the mechanism before author-proof exposure and executed a different exact nine-state physical graph control. It found no material error in(D1)-(D10) at the supplied scope. It explicitly did not check microscopic local convergence, the target-spin transfer or electric moments. The author six-state star control is separate evidence: eight rows, actual resolved/coherent output maps, two correction-omission/sign controls,0.035395CPU seconds and56.3MB peak RSS. Its largest corrected identity discrepancy was2.16e-13; no volume conclusion is inferred from that floating control.

## 2. A completed separate spin-target to rotor limit

The exact finite-spin effective Hamiltonian contains the additional term

    -(delta/(2C))sum_(ordered c=a or dist2){M_(a,S),D_c},
    M_(a,S)=PF_(a,S)^*F_(a,S)P, C=S(S+1).

SPIN_TARGET_LOCAL_LIMIT.md keeps this term. Extending D_c/C by its diagonal spin-box indicator makes the off-box proof extension bounded, local and strongly vanishing while preserving the actual physical spin box. The electric term KD is unchanged. Actual uniform per-center bounds are

    ||A_(a,S)||<=3960delta,  ||Gamma_(a,S)||<=80kappa,
    sum_(m at a)||L_(m,S)||^2<=108kappa.

Electric conjugation enlarges support only once, to a129-site radius-four neighborhood. Strong/ultraweak local integrals, not norm-Bochner continuity on B(rotor Hilbert space), give a connected-string localization bound. Its common small-time parameter is

    a_star=16641(7920delta+160kappa).

Choose a finite spatial patch from its explicit scalar tail independently of S and total torus volume. On that fixed patch the bounded coefficients converge strongly on trace class in the common electric interaction picture. FINITE_PATCH_RESOURCE.md supplies the explicit alternative

    error_patch <=(mu/C)sum_(n=1)^n0
             n(4n+8)^2 beta^(n-1)T^n/n!
                  +2sum_(n>n0)(beta T)^n/n!,
    beta=n_A(7920delta+160kappa),
    mu=n_A(50000delta+2000kappa), S>=4n0+8.           (M2)

Together with spatial localization this proves a volume-uniform local reduced-trace-norm effective-spin-to-rotor limit. Uniform unit-ball CP localization followed by finite-patch comparison extends the conclusion to each finite T. This is not a fixed-volume-first diagonal sequence.

For the original monitored marks, no-monitored-event propagators retain all true losses and all unobserved exterior gains. A COMMON history reference measure uses9kappa per resolved label or18kappa per coherent edge, total mass exp(108kappa|F|T). Fixed-word trace convergence, spatial localization and the factorial record tail prove convergence of the full finite-region timestamp quantum output in integrated trace norm, hence of the requested fixed-bin instrument. The coherent sign is never exposed. Uniform TARGET local field moments pass the actual target local energy/current forms. None of these moment bounds is attributed to the fast microscopic process.

## 3. Exact dark-word test and a limited positive absorption mechanism

DARK_WORD.md derives the actual second transformed-jump positive-grade coefficient

    J_(m,+1)^(2)=-F_a j_m F_a.

Its total squared coefficient on Omega is360 per A center, for either original instrument, so positive-grade creation starts at360kappa epsilon^2. The exact sparse cubic word control constructs a Gauss-compatible one-hole output with seven occupied B sites and G=sum j^*j=0. It also verifies an actual H2 matrix element+1 into a state with G=8. Thus the often tempting pointwise absorption inequality G>=cW is false; no invariant dark mode or failure from Omega follows.

FAST_ONE_HOLE_ABSORPTION.md proves a genuinely different estimate for the leading rotor fast coefficient H2=C+[F,F^*] in W=1, GLOBAL N_B<=9. Actual occupation support gives ||H2||<=1092 independently of volume/fields. Every dark input has six axial unit-amplitude outputs with G>=4. A B occupancy mask with<=9 particles has at most one dark A star, and same-hole B reshuffles cannot reach these outputs. This rules out cancellation and proves

    G+H2 G H2 >= 2/(1092^2+1) I.                    (M3)

An explicit two-term unitary observability argument then gives

    ||exp[u(-i delta H2-kappa G/2)]||<=C0 exp(-gamma u)

with fully specified positive constants independent of volume and fields. A finite-band exponential-weight argument also controls electric moments of both surviving amplitudes and the original marked absorbing output. The tiny geometry check corroborates4,526 masks and27,156 axial rows on the relevant local sets, plus exact L6/8/10 star intersections, in0.42659CPU seconds/19.5MB. It is not a Hilbert-space spectral computation. The crude constants are not feasible-time predictions.

This theorem applies to a fixed low-GLOBAL-excitation sector of the rotor leading fast law. It does not describe the entire finite-spin microscopic process or extensive B occupation at positive physical time, and it does not justify independent excursions or a volume-uniform decay gap in every sector. Its weighted bound therefore cannot simply be inserted as the missing microscopic moment theorem.

## 4. Exact remaining obligation

Let I_micro,L^F be the actual original finite-bin marked output with the finite regional quantum output retained, and let I_eff,S,L^F be the corresponding canonical finite-spin effective instrument with its anticommutator correction. The unresolved estimate is

    sup_(L>=6 even) ||I_micro,L^F(Omega)
               -P_embed I_eff,S,L^F(Omega)P_embed^*||_(cq,1;X)
                   <=f_(X,F,T)(S),  f_(X,F,T)(S)->0.  (M4)

It includes the empty monitored set for local state comparison. Count overflow can now be removed uniformly using(M1). Given the independently derived spin-target transfer, (M4) is target-equivalent to the remaining original contract, not a weaker theorem being hidden under a new name.

Small defect density alone leaves a possible O(1) integrated contribution from epsilon^-2 W-preserving motion. The exact penalty phases do not average away Pi_r rho Pi_r populations. A useful sufficient continuation would control their local transport and jump/loss coherences under the ACTUAL ensemble, with electric uniform integrability for the weighted extension. No claim is made that this particular sufficient mechanism is logically necessary; cancellations could establish(M4) differently. APPROACH_REGISTRY.md records the attempted global/local normal-form, absorption and connected oscillatory routes and their precise failed inferences.

Finally, the actual microscopic initial stored energy is6delta epsilon^-2 per A center, while the target mean is-618delta. The task cannot be closed by identifying those energies, imposing an unprovided energy cap, or replacing Omega by a dressed input. Quantum dynamics, carrier, compensation, couplings and original instruments remain explicit supplied premises, not selections by the native M2 foundation.

## Evidence and freeze

All author files are confined to this directory. No source or shared authority was edited, no external message/PR/commit/push was issued, no additional agent was spawned and no heavy job was used. Total author control cost is below0.5CPU seconds; maximum observed RSS56.3MB. Frozen contract and defect proof bytes remain unchanged. The first control's original metadata inputs are preserved with exact matching hashes and explicit reconstruction provenance in history/star-control-bound-inputs; its result was not rebound to later metadata. All ten current science-source bodies were rechecked against their recorded main hashes, and remote main remained30a at final packaging. MANIFEST.json binds the final author inventory, source identities and run outputs. The two new theorem proofs and the quantitative patch appendix need focused independent checking before high-fanout reuse; only the defect/count result currently has the specific independent receipt described above. This is discovery evidence, not formal review or audit status.
