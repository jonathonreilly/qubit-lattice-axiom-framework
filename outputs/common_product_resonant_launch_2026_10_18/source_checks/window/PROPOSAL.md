# A complete standalone launch window from the resonant profile

New bounded author corollary, conditional on geometric-profile sourcebe2ab and its pending distinct check. The accepted scalar survival bound306174 is combined with the ACTUAL emitter-plus-two-lead-term decomposition to give a normalized complete-output launch estimate on a positive relative-width time window. The target is an explicitly phased, positively normalized geometric profile on the lead with the emitter vacant. No incoming packet is physically supplied or inserted.

This is an empty-half-line SOURCE result. It does not establish a finite router, integrated cut error, microscopic apparatus vacancy, record flag or end-to-end runtime. The source-only time order below must not be transplanted to those different graphs.

## 1. Actual source, exact decomposition and adopted bounds

Use the literal standalone launcher of fb72: emitter s, lead n>=0, the positive combined source block

    B=Q_gamma(s,0)+(2j-gamma)n_s+(j-gamma)n_0,

and uniform positive Q_j lead bonds. Here j>0,0<gamma<j and rho=gamma/j. The one-head generator H_gamma has all diagonals2j, source hopping-gamma and later hoppings-j. The supplied initial state is |s>, with all other heads vacant. Its positive full-support combined-block loads are3j at s,5j at site0 and4j elsewhere; for an optional fixed incident cap Lambda, j<=Lambda/5 suffices. No finite number of lead qubits is claimed: the analytical model is the bounded one-head half-line operator, not an unbounded infinite many-head sum.

With E(k)=2j(1-cos k), the exact complete state is

    exp(-itH_gamma)|s>
        =A(t)|s>+O_tF+I_t conjugate(F),                  (1)

where the outgoing and incoming integrals use exp(+ink-itE) and exp(-ink-itE), respectively, on0<k<pi with factor1/sqrt(2pi), and

    F(k)=-i sqrt(2/pi)rho exp(ik)
                       /[(2-rho^2)cot k-i rho^2].

Its upper-half-circle L2 norm is1 by the checked complete emitter measure. The two lead terms in(1) interfere; they are not two separately normalized physical particles. The complete state in(1) has norm1. The accepted survival source gives, for0<rho<=1/2 and u=jt>=0,

    |A(t)|<=exp[-rho^2 u/sqrt(1-rho^2)]+4rho^2/3.        (2)

The nonzero band-edge remainder in(2) is retained. This is an upper amplitude bound, not an exact exponential decay law.

For clarity, record the exact geometric interface being adopted conditionally. Put a=sqrt(1-rho^2),

    U(k)=i rho/[sqrt(2pi)(1+i a exp(ik))],
    u_n=i rho(-ia)^(-n) for n<=0, and0 for n>0.

The full-integer u has norm1. If f(t) is the full-integer inverse Fourier transform of exp(-itE)1_(0,pi)F and u(t) is the exact free evolution of u, sourcebe2ab proves

    ||f(t)-u(t)||<=delta_rho<=29rho/8, all real t.       (3)

Both spectra are normalized; the lower semicircle is explicitly charged in delta_rho rather than silently filled. For m(t)=floor(2jt+1/2), define

    G_n(t)=exp(-i2jt)exp[i m(t)pi/2] u_(n-m(t)).          (4)

This norm-one integer-translated comparator has the exact rounding phase. The same geometric source proves

    ||u(t)-G(t)||<=D_rho(t)
                  <=rho+2rho(j|t|)^(1/6),               (5)

with an optional cap2. This is a paid nonlinear-dispersion error, not exact rigid propagation. For t>1/(4j), conjugating the full-line outgoing integral and using m(-t)<=-1 gives

    ||I_t conjugate(F)||<=delta_rho+D_rho(-t).            (6)

Bounds(3)--(6) are geometric-source premises pending its separate check; they are not consequences of survival(2) alone.

## 2. Complete raw target and positive normalization

Embed W(t)=P_(n>=0)G(t) on the physical lead with zero emitter amplitude. Equations(3)--(6), restriction contraction and source/lead orthogonality give the COMPLETE estimate

    ||exp(-itH_gamma)|s>-W(t)||<=d_raw(t),
    d_raw(t)=sqrt(R(t)^2+
                    [2delta_rho+D_rho(t)+D_rho(-t)]^2),  (7)

where R(t) is the right side of(2). In particular d_raw is bounded by R+2delta_rho+D_rho(t)+D_rho(-t). Both emitter residue and incoming lead field are charged; they are not removed by observing only outgoing sites.

For t>=0, m=m(t)>=0 and the geometric sum gives explicitly

    ||W(t)||=sqrt[1-a^(2(m+1))]>0.

Define the positively normalized physical target

    beta_n(t)=
      exp(-i2jt)exp(im pi/2) i rho(-ia)^(m-n)
                      /sqrt[1-a^(2(m+1))], 0<=n<=m,
      0, n>m.                                           (8)

The emitter is vacant in this target. No freely adjusted phase, complex normalization or target-dependent physical operation is allowed. The exact common diagonal phase exp(-i2jt), the integer rounding phase and the source factor i are all present. If a separately supplied common scalar cI is added to this source, multiply(8) by exp(-ict).

Whenever d_raw<1, the reverse triangle inequality gives ||W||>=1-d_raw; positive normalization costs at most d_raw. Thus

    ||exp(-itH_gamma)|s>-|0_s>beta(t)||
                           <=min{2,2d_raw(t)}.           (9)

Here |0_s>beta is notation for the one-head lead vector with an empty emitter; it is not a tensor product containing an extra head. Equation(9) includes all physical lead sites and the emitter. The exact formula for ||W|| already shows the target is nonzero; the d_raw condition is used for the useful error guarantee, not to define the state circularly.

The comparator's integer center can jump as time passes a rounding threshold. Its specified phase jumps with it; (7)--(9) hold pointwise on both sides with the prescribed convention. This comparison-function choice is not a switch in the physical Hamiltonian or evolution.

## 3. Simultaneous explicit small-error window

For0<epsilon<=1 let

    L=log(32/epsilon),
    rho=(epsilon/64)^(3/2) L^(-1/4), gamma=rho j,
    u0=rho^-2 L=(64/epsilon)^3 L^(3/2),
    t_minus=u0/j, t_plus=2u0/j.                          (10)

These are explicit supplied source coefficients and analysis times. Since L>1,

    0<rho<=epsilon/512<=1/512<1/2,
    u0>1, t_minus>1/(4j).

All domains of(2)--(6) therefore hold throughout the CLOSED interval[t_minus,t_plus]. Its relative width (t_plus-t_minus)/t_minus is1, not a single selected arrival time.

For u in[u0,2u0], the survival exponential satisfies

    exp[-rho^2 u/sqrt(1-rho^2)]<=exp(-L)=epsilon/32.

Moreover4rho^2/3<=epsilon/1024 using rho<=epsilon/512 and epsilon<=1. Therefore

    R(t)<=33epsilon/1024.                                (11)

For either sign of time, equations(3),(5) give

    2delta_rho+D_rho(t)+D_rho(-t)
       <=(37/4)rho+4rho(2u0)^(1/6).

The parameter choice has the EXACT identity rho^(2/3)L^(1/6)=epsilon/64. Since2^(1/6)<9/8,

    4rho(2u0)^(1/6)
       =4*2^(1/6)rho^(2/3)L^(1/6)<=9epsilon/128,
    (37/4)rho<=37epsilon/2048.

Consequently the entire lead-error allowance is at most181epsilon/2048. Combining this with(11), even the triangle bound for(7) gives

    d_raw(t)<=247epsilon/2048<epsilon/8,
    sup_(t_minus<=t<=t_plus)
       ||exp(-itH_gamma)|s>-|0_s>beta(t)||<epsilon/4.     (12)

The surplus in(12) is deliberate. No bound has been optimized, and the integer translation is not substituted for the true dynamics without paying(5). A single choice of gamma and the full positive-width time window meet all inequalities simultaneously.

The occupied-emitter probability alone is bounded by(33epsilon/1024)^2 from(11). The complete-target estimate also implies probability greater than1-epsilon^2/16 that the head is in the target support0<=n<=m(t), with source empty. This probability statement does not replace the stronger coherent vector comparison and is not a measurement mechanism.

## 4. Coherent paths, references and complete channels

For two disjoint IDENTICAL source/half-line copies, let J_seed place the supplied path qubit at the two emitters and retain arbitrary passive program/reference degrees of freedom. Every other head starts vacant. An arbitrary encoded path input need not be a product across the two emitter sites; that input coherence is supplied. On a basis path the unused apparatus is a product vacancy state.

The two orthogonal branches have exactly the same source amplitude, rho, integer center m(t) and complex beta(t). Thus(12) is the operator bound

    ||U_launch(t)J_seed-J_out[beta(t) tensor I_logical]||
                        <epsilon/4                      (13)

throughout the same window, including arbitrary passive references. No sqrt(2) or reference-dimension factor occurs. Both emitters and every lead site are included, and the comparator has both emitters vacant. Any supplied common scalar phase must multiply the target on every branch equally.

Both maps in(13) are isometries, so their unhalved complete output-channel/diamond discrepancy is less than epsilon/2. This is not a channel obtained after discarding residual sources or conditioning on their vacancy. It does not create a program/path gate: the logical input is transported identically by these two standalone sources.

## 5. Optional central cutoff must still be paid

The target(8) is an unfiltered geometric comparison. A later apparatus proof may need a compact central-band outgoing spectrum, and that restriction is NOT free. For0<sigma<pi/2 and a real chi in C_c^2((0,pi)) with0<=chi<=1, equal to1 on |k-pi/2|<=sigma, let

    p=||chi F||_2^2>0, g=chi F/sqrt(p),
    s_chi=sqrt[2(1-sqrt(p))].

The exact overlap calculation in be2ab gives ||F-g||<=s_chi. If the hard-band mass bound P_sigma<1 is used,

    P_sigma=min{1,4rho^2/[pi(2-rho^2)^2 tan sigma]},
    p>=1-P_sigma, s_chi<=sqrt(2P_sigma).                 (14)

Let W_chi(t)=O_t g, with source coordinate zero. This is the exact free outgoing amplitude with the normalized cutoff spectrum, not the geometric target. Equations(1)--(3),(6) and Fourier contraction give

    ||exp(-itH_gamma)|s>-W_chi(t)||
       <=R(t)+delta_rho+D_rho(-t)+s_chi.                 (15)

On the window(10), its first three terms are bounded by the larger allowance d_triangle=R+2delta_rho+D_rho(t)+D_rho(-t)<epsilon/8. If s_chi<=epsilon/8, then the raw error in(15) is less than epsilon/4, W_chi is nonzero, and its positive normalization has complete-output error less than epsilon/2. A sufficient explicit spectral condition is

    P_sigma<=epsilon^2/128,
    equivalently it suffices that
    tan sigma>=512rho^2/[pi(2-rho^2)^2 epsilon^2].        (16)

The implication in(16) uses the displayed upper bound, not equality to the true tail mass. A fixed central band can satisfy it; a future shrinking band must be checked against its actual required width. No compatibility with a particular router bandwidth, biased channel threshold or finite-distance return window is asserted. Nonanalytic cutoffs are handled by L2 distance, never contour continuation. Neither W_chi nor beta is physically inserted as a packet; they are comparison states for the same emitter seed.

## 6. Source-only cost and excluded transfers

The explicit window lower time in(10) has sufficient order

    t_minus=Theta(j^-1 epsilon^-3 [log(1/epsilon)]^(3/2))

as epsilon tends to zero. Its exact formula uses log(32/epsilon), so it is defined and valid on the whole0<epsilon<=1 domain. The source ratio has order rho=Theta(epsilon^(3/2)[log(1/epsilon)]^(-1/4)). At an optional fixed source-only cap j=Lambda/5, replace j^-1 by5/Lambda; this states no finite apparatus count or optimized performance. Exact source compensation and absent extra couplings remain supplied.

This is a simultaneous standalone launch bound, unlike the earlier survival-only time criterion. It is still NOT a finite-router runtime: changing the distant graph can change source reabsorption and reflections, and a finite graph can recur. A future finite composition must match the complete early vector, pay localized spectral components, control actual boundary Duhamel integrals and incoming/outgoing return geometry, and include all internal/record outputs. The growing dispersion allowance in(5) cannot be assumed small for arbitrary later times or integrated across a boundary without a new argument. The physical packet is not a permanent halted or captured output.

No thermal preparation, bath/cooling, physical packet supplier, new native block, old literal processor theorem, readout/reset/capture, all-time record implication, coefficient tolerance or permanent halt is obtained. The exact one-head seed, supplied logical coherence, local positive Hamiltonian and occupation basis are unchanged assumptions.

## 7. Sources, exposure and review status

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Exact primary sources:

- common_product_endpoint_launch/PROPOSAL.md: fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4, completely reread/hash-refreshed in the immediately preceding geometric task. Its complete measure, decomposition and physical block convention are retained unchanged.
- common_product_geometric_source_profile/PROPOSAL.md: be2ab9da4b62ca7f595c17fea5ec6e62849cdada2c34416154996ad15180538e, authored and fully read immediately before this task; hash refreshed here. Its new comparison and propagation estimates remain a PROVISIONAL dependency pending the assigned distinct check. This corollary does not independently validate those estimates.
- common_product_resonance_tail/PROPOSAL.md:306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002, completely reread in that preceding task. Its common_product_resonance_tail_check/REVIEW.md was completely read/hash-verified here: de9dbd20bf873f194d969ec6570e77224a2dfb192ba3ac4035b0933fc3d610bd, supporting its standalone scalar-survival scope.

ROOT suggested the rho/u scale and requested a complete source-only corollary rather than a finite-runtime extrapolation. This author wrote the geometric, launch and survival sources and has that full source/design exposure. The new simultaneous constants, window, target normalization and complete-output composition are author derivations requiring a distinct check; the accepted survival check does not check their spatial terms. Same model and effort were retained. No blind or independent status is claimed.

Only this proposal was created. No scientific executable, solver/simulation/sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. Frozen sources remain unchanged. No retained status is assigned.
