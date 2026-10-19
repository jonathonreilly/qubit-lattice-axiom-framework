# Finite seeded routing and a finite-horizon output-record branch

Claim type: bounded_theorem. Conditional mathematical result with selective analytical and exact finite-matrix checks. No retained audit or native realization is asserted.

This construction attaches one shared record to the [finite seeded router with separate input and output stages](COMMON_PRODUCT_STAGE_SEED_BOUNDED_THEOREM_NOTE_2026-10-18.md), parent PR9707 at `9f375bb40cb7bc28209a10387944f7262d7021f8`. It proves a normalized complete output on a positive-width final window and, under a stronger source policy, an absolute record-branch contract over a whole finite horizon. The latter is not permanent halt or uniformly accurate conditioning on a rare early flag.

## Two guarantees and supplied premises

A supplied static positive Hamiltonian on an explicit finite cubic nearest-neighbor qubit graph routes a seeded head according to a preserved twelve-bit legal program. Two output writers couple to one shared record. The construction has two parameter policies, with different guarantees:

- **Policy F:** normalized complete output on a final positive-width window, with isometry error below 3 epsilon/8. The target contains the routed head on the ordinary F output sites, record|1>, the preserved program/reference and vacuum on every other head.
- **Policy A:** the same final-window guarantee, plus absolute error below epsilon/2 for the unnormalized record1 branch throughout the finite horizon [0,t_plus]. One fixed target formula is used before, during and after packet transit; it is never normalized by a possibly small early success probability.

The second statement bounds erroneous flagged internal and wrong-output amplitudes absolutely. It does not claim they are impossible, that a rare record1 outcome always has a uniformly accurate normalized state, or that the guarantee continues after t_plus. Eventual high joint flag/output probability follows separately from the normalized final-window theorem.

Both policies assume the supplied positive local blocks and exact coefficient correlations, one encoded head at the I emitters, a legal correlated program, an initially blank shared record, and vacancy of all remaining heads. Arbitrary path/program coherence and passive-reference entanglement are retained. These are mathematical input and interaction premises, not derived native preparation/readout mechanisms. The source/check chain supports the equations below at its disclosed selective analytical scope; this note supplies no experimental evidence, optimality claim or permanent halt.

## Literal positive device

Write n_v for head occupation, and let

`Q(h)=|h|(n_u+n_v)+h(a_u^dagger a_v+a_v^dagger a_u)`.

This block is positive on its full two-qubit support, with norm 2|h|. Use Q_b=Q(-b), Q_j=Q(-j), j=b^2/D0 and a=2j, with D1>D0>2b. Each of the four core cells is the seven-block inventory

`Q_b(u,m)+Q_b(m,v)+b(I-n_u)+b(I-n_v)`

`+[(D0-2b)P0_c_m+(D1-2b)P1_c_m]n_m`

`+a P0_c_u n_u+a P0_c_v n_v`.

Two straight cells connect (I0,O0),(I1,O1); two cross cells connect (I0,O1),(I1,O0), each through its own mediator and three distinct program qubits. For legal p=0 the cross cells are locally 000 and straight cells 111; for p=1 the assignments reverse. The ideal path operation is C0=X and C1=I. No routing contract is claimed for other twelve-bit patterns, although their Hamiltonian remains positive.

The translated core endpoints are I0=(20,0,0), O0=(22,0,0), I1=(22,2,0), O1=(20,2,0). Mediators occupy square-edge midpoints. The three controls of each straight cell lie at +z from its two endpoints and mediator, and those of each cross cell at -z. All twelve controls are distinct. This core has eight heads and twelve program qubits.

Place the single record R at (0,0,0). Writer A has terminal-to-attachment arms

`(1,0,0),(2,0,0),(2,1,0),(1,1,0),(1,2,0),...,(1,8,0)`

and

`(-1,0,0),(-1,1,0),...,(-1,8,0),(-1,8,1),(0,8,1)`.

Its two ports are U_A=(0,8,0), F_A=(1,8,1). The attachment/port square uses hopping matrix -jU, where U is the real Hadamard matrix [[1,1],[1,-1]]/sqrt(2), retaining the positive sign of its fourth hopping. Ordinary arm bonds are Q_j. On the second arm, bonds y=2--3 and y=5--6 have hopping -sqrt(2)j and positive endpoint occupations (2-sqrt(2))j n. Each junction vertex has vacancy term (sqrt(2)-1)j(I-n). Each terminal has the positive two-body contact j n_T(I+X_R), of norm 2j. No three-body controlled hopping is supplied.

Writer B is the image of all finite writer-A heads and blocks under (x,y,z)->(z,-y,x). It has U_B=(0,-8,0), F_B=(1,-8,1), and terminals (0,0,+/-1), distinct from writer A's terminals (+/-1,0,0). Both writers couple to the same R, not two copies. Each has 24 head vertices and 34 listed blocks. Record-X sectors reduce to scalar head problems; record excitation need not be conserved.

The two equal cables are

`O0 -> (22,-10,0) -> (0,-10,0) -> U_B`,

`O1 -> (20,12,0) -> (0,12,0) -> U_A`.

Each has 34 ordinary j edges and 33 new interior heads. Final rays extend in +x from F_B and F_A, labeled F0 and F1 respectively. Input rays are I0->(19,0,0)->(19,0,1)->(19,0,2)->... and I1->(23,2,0)->(23,2,1)->(23,2,2)->... . Radial coordinates count edges around the bends. The listed paths are disjoint outside their specified endpoints and avoid all controls, writer heads and R. Incidental lattice adjacency does not install an interaction.

The pre-ray finite network has 135 qubits and 164 listed positive blocks. Its 122 head vertices include the four external origins, leaving 118 strict internal head coordinates. Program/record states are fibers, not additional head positions. The true common scalar is

`c_total=8b+2c_R`, with `c_R=4(sqrt(2)-1)j`.

For an integer ell>0 let M=ell+1. Each finite I ray retains n=0,...,M, ordinary bonds through the bond ending at M-1, and the source block replacing the last bond:

`B_I=Q_gamma(M-1,M)+(j-gamma)n_(M-1)+(2j-gamma)n_M`.

Equivalently, the ordinary edge indices are 0,...,M-2 and the weak edge is M-1. Each F ray retains n=0,...,ell with all ell ordinary bonds and cap j n_ell. Source and cap endpoint diagonals are 2j. These additions contribute no scalar. The physical finite counts are

`N_qubits=137+4ell`, `N_blocks=168+4ell`.

The seed puts one head at M on the two I emitters according to the encoded input, preserves the supplied legal program, and supplies R=|0>. Basis seeds are occupation products; arbitrary logical superpositions remain valid inputs. The target head occupies only the ordinary F sites 1,...,ell, excluding both writer origins n=0 as well as every other finite-network head.

## Stationary and packet interfaces

For k in the selected central band, z=exp(ik), eta=b/D0 and zeta=D0/D1, the core full reciprocal scattering error is at most e=13eta^2+5zeta. Each writer's full two-port/record error relative to -iz^22 times port exchange and X_R is at most w=33|k-pi/2|. Equal cables supply z^34, so the complete ideal external matrix has the single common phase

`phi(k)=-iz^57`,

and ideal action [[0,C_p X_R],[C_p X_R,0]] in I/F ordering. With den=1-ew>0, exact repeated-reflection composition gives

`deltaS=min{2,[2(e+w)+ew]/den}`.

This is a full matrix error, including reflected I output, F incidence and both record sectors. No selected success column is renormalized. The physical time phase is exp(-ic_total t), distinct from the stationary momentum phase.

The packet source constructs an exact normalized infinite-ray solution from g in C_c^2, ||g||_2=1, with energy E(k)=2j(1-cos k), phase exp(iell k-itE), the complete external scattering matrix and all 118 strict internal coordinates. Exact evolution plus remote-past incoming separation proves its isometry property. It neither assumes global spectral completeness nor sets a finite seed's localized-state overlap to zero.

Let H_x be the dimensionless 24-head writer matrix after removal of its vacancy scalar in record-X sector x, retaining the external-bond port diagonals, and P its two-port projection. The outgoing boundary matrix is L_x(k)=H_x-2(1-cos k)I-zP. The local writer sharpening proves ||L_x(k)^-1||<10 throughout |k-pi/2|<=10^-3 for both sectors. The actual positive-block matrix is rotated at its two ports into two twelve-site chains. Exact squared inverse Frobenius norms are 72 and 159/2 in the + sector, and 72 and 129/2 in the - sector. Their direct-sum maximum bounds the center operator norm below 9. The perturbation norm is at most 3|k-pi/2|, giving inverse norm below 9000/973<10 on the full interval.

For both policies, use the conservative local choices

`B=10, a0=20, a1=w1=800, w2=56000`.

These follow by substitution into the checked packet formulas 2B,8B^2,56B^3. The separately proved smaller ceilings 620 and 37820 are not used. Every downstream constant is recomputed with these values, as specified explicitly below; no old constants evaluated with B=10^31 are retained. The finite static check supports the parameterized substitution for any separately established fixed B>=1. Combining it with the distinct local B=10 check changes a mathematical estimate, not a physical writer or phase.

### Explicit recomputation of packet constants

The following is the pinned packet prescription with unambiguous names separating internal amplitudes from time. Set d=34, lambda0=1-3eta^2 and, for uniform band ceilings, w=33h and den=1-ew. Define

```text
a_1=2eta^2/lambda0^2
a_2=2eta^2/lambda0^2+8eta^4/lambda0^3
b_1=2eta^2 zeta^2/(1-3eta^2 zeta)^2
b_2=2eta^2 zeta^2/(1-3eta^2 zeta)^2
                         +8eta^4 zeta^3/(1-3eta^2 zeta)^3
v1=2(a_1+b_1), v2=2(a_2+b_2)
l1=1+v1, l2=1+v2
c1=4+8l1
c2=4+16l1+32l1^2+8l2
d0=D0-3j
m0=4b/d0, m1=8jb/d0^2+2b c1/d0

k0=1/den
f1=w1 e+w c1+2dwe
f2=w2 e+w c2+2w1 c1+4d(w1 e+w c1)+4d^2we
k1=k0^2 f1, k2=2k0^3 f1^2+k0^2 f2
l_1=w1+wd+w c1
l_2=w2+wd^2+w c2+2dw1+2w1 c1+2wd c1
U0=k0(w+1)
U1=k1(w+1)+k0(l_1+w1)
U2=k2(w+1)+2k1(l_1+w1)+k0(l_2+w2)
W0=1+e U0
W1=c1+(c1+ed)U0+e U1
W2=c2+(c2+2dc1+ed^2)U0+2(c1+ed)U1+e U2
s1=c1+(c1+d)U0+U1+w1+(w1+d)W0+W1
s2=c2+(c2+2dc1+d^2)U0+2(c1+d)U1+U2
                 +w2+(w2+2dw1+d^2)W0+2(w1+d)W1+W2
q1=s1+57, q2=s2+114s1+57^2

n0=1+U0, n1=d U0+U1
r0=1+W0, r1=d W0+W1
T0=2n0+m0 n0+a0 r0+sqrt(66)(W0+U0)
T1=c1 n0+2n1+m1 n0+m0 n1+a1 r0+a0 r1
                       +sqrt(66)[d(W0+U0)+W1+U1]
```

Here U_r,W_r are scalar ceilings on the cable coefficient maps, not physical unitaries or a change in block notation. q1,q2 bound derivatives of the full scattering matrix after removal of -iz^57; T0,T1 bound the complete finite-coordinate map and its derivative, and hence its strict internal restriction. They depend on the core ratios and fixed writer/cable constants, not on rho, ell or time. In particular choosing a smaller source ratio after computing T0 is noncircular.

## Two source policies and separated time budgets

For 0<epsilon<=1 and a supplied load scale Lambda>0, set

`h=epsilon/10^5`, `eta^2=zeta=epsilon/10^5`,

`D1=Lambda/2`, `D0=zeta D1`,

`b=eta D0`, `j=b^2/D0`.

First recompute the packet constants above, then choose

`rho_F=epsilon sqrt(h)/1024`,

`rho_A=min{epsilon sqrt(h)/1024,[epsilon/(4096(1+T0))]^2}`.

Use the selected rho in the actual source coupling gamma=rho j. Policy F supplies the finite-window contract; policy A additionally pays the uniform internal/origin flag amplitudes. No source coupling or derivative constant from one policy is silently reused in the other.

The real C2 cutoff chi equals one on |k-pi/2|<=h/2, uses quintic 1-10s^3+15s^4-6s^5 across transition width h/4, and vanishes beyond 3h/4. Define

`F(k)=-i sqrt(2/pi)rho exp(ik)/[(2-rho^2)cot(k)-i rho^2]`,

`p_chi=||chi F||_2^2`, `g=chi F/sqrt(p_chi)`.

Write G_r=||g^(r)||_1 for r=0,1,2, with g^(0)=g.

The finite source derives omitted mass P<=3rho^2/h and p_chi>1/2, together with G0<=1, G1<=g1=80/rho, G2<=1200/(h rho^3), and incoming coefficient bound bminus=82/rho. These changing-cutoff estimates are part of the finite check, not inherited fixed-band constants.

Use instead the separately checked sharper ceiling `g2=600/rho^3`. Both policies satisfy rho^2<=h<=10^-3 and p_chi>1/2. Here is the new load-bearing estimate. For q=k-pi/2, c=sqrt(2/pi) and D=-(2-rho^2)tan q-i rho^2, |D|>=sqrt(q^2+rho^4), |D'|<=4 and |D''|<=16h. The exact second derivative of exp(ik)/D contains all four terms -D^-1-2iD'D^-2-D''D^-2+2(D')^2D^-3. Integrating their absolute values bounds ||chi F''||_1 by c(66+24pi)/rho^3. The two transition intervals together have length h/2 and |q|>=h/2; there |F|<=2c rho/h and |F'|<=c rho(2/h+16/h^2). Thus 2||chi'F'||_1<=144c/rho^3 and ||chi''F||_1<=100c/rho^3, using rho^2<=h. Division by the actual sqrt(p_chi)>=1/sqrt(2) gives G2< (2/sqrt(pi))(310+24pi)/rho^3<600/rho^3. This retains the phase and cutoff derivatives, bounding the latter only on their actual support away from the resonance. G1 and bminus remain unchanged. All H2, A_i, A_o, Q_budget, length and time expressions below use this new g2; earlier sufficient prescriptions remain preserved in the evidence bundle.

For policy A, the same normalized amplitude also obeys G0<=16sqrt(rho)<=epsilon/[256(1+T0)]. To obtain this, write a=2-rho^2 and q=k-pi/2. The exact modulus is at most sqrt(2/pi) min{rho^-1,rho/(a|q|)}. Integrating across its crossover |q|=rho^2/a and dividing by the actual sqrt(p_chi)>=1/sqrt(2) gives

`G0<=(4/sqrt(pi))(rho/a)[1+log(ah/rho^2)]<=16sqrt(rho)`.

The first rho bound ensures the crossover lies within h and p_chi>1/2; the second ensures the final uniform amplitude budget. No spectral mass is discarded by this normalization.

Let v_min=2j cos h, v_max=2j and, using the parameterized packet constants above, set

`H1=g1+q1`, `H2=g2+2q1 g1+q2`,

`J0=T0`, `J1=T0 g1+T1`,

`A_i=g2+(12j/v_min)g1+4j/v_min+48j^2/v_min^2`,

`A_o=H2+21H1+154`,

`L=max{1,bminus,g1+1,H1+1,g1+7}`,

`Q_budget=max{1,eta^-1,rho^-2,J1+J0,A_i+A_o}`.

Q_budget is a scalar time-budget coefficient, not a hopping block or scattering operator.

These two maxima are explicit and independent of the subsequently selected time or length. Choose

`u0=10^12 max{1,(L/epsilon)^2,Q_budget/epsilon}`, `ell=ceil(100u0)`,

`t0=u0/j`, `t_minus=3ell/(4j)`, `t_plus=7ell/(8j)`.

This gives L/sqrt(u0)<=epsilon/10^6 and Q_budget/u0<=epsilon/10^12, with sqrt(ell)>=10sqrt(u0) and ell>=100u0. It pays the inverse-time costs through Q_budget without unnecessarily squaring them. The older common-K square was sufficient, not a necessary lower bound. There is no Hamiltonian switch at any of these times. The relative window width (t_plus-t_minus)/t_minus is 1/6.

The finite proof first compares the actual seed to two standalone launchers in a common extended Hilbert space. Its reference retains the entire actual internal/F submatrix, including large mediator and writer terms, while decoupling its I origins. Only the occupied launcher subspace has norm bound 4j. The contact difference has norm at most 2j+sqrt(2)b, including the +j I-origin diagonal mismatch. Reference powers below degree M cannot reach that contact. Ordered Duhamel then pays the early error without bounding the complete actual Hamiltonian by 4j.

After matching to the exact packet, hopping-only perturbations create the actual weak I sources and capped F ends, direct-summed with auxiliary Dirichlet exteriors of diagonal 2j. The added F cap is necessary for this exact identification. Twice-integrated nonstationary bounds control the finite contact residual; no omitted internal writer return is replaced by an effective dynamics approximation. The early full-vector match pays every actual seed component omitted from the packet, including possible localized components.

The exact split prescription preserves the twelve allowances:

| Contribution | Split ceiling |
| --- | --- |
| Early actual/reference comparison | Q_budget/u0 |
| Twice source survival | 2Q_budget/u0 |
| Twice incoming launch remainder | 2L/sqrt(u0) |
| Spectral cutoff loss | 4sqrt(3)epsilon/1024 |
| Right incoming-tail replacement | 8L/sqrt(u0) |
| Early external packet tails | 4L/sqrt(ell) |
| Early internal packet amplitude | 3Q_budget/ell |
| Integrated finite boundary residual | 2Q_budget/u0 |
| Twice late incoming tail | 6L/sqrt(ell) |
| Twice complete scattering error | epsilon/256 |
| Twice late internal amplitude | 56Q_budget/ell |
| Normalized final F truncation | 28L/sqrt(ell) |

Every entry is below epsilon/32; the spectral term is below epsilon/128. Internal coefficients J0+J1 and second-derivative boundary coefficient A_i+A_o remain in Q_budget. No derivative or spectral error is removed. The contact estimate is (2+sqrt(2)/eta)/(5000u0)<=Q_budget/u0. All phase gaps remain valid because u0>=10^12 and ell>=100u0. In particular both late gaps, including the subtraction of 57 at the F origin, exceed ell/4. The same intermediate bounds establish launch normalization, D_L<1/2 and 2tau_F<1 before any normalized target is used. The distinct split check supports this regrouping for both policies.

Define the common scalar outgoing sequence

`B_n(t)=(-i)/sqrt(2pi) integral exp(i[n+ell+57]k-itE(k))g(k) dk`,

and let beta_F(t) be its positive normalization on 1<=n<=ell. With E_seed and J_F denoting the stated input and output isometries, the finite theorem is

`sup_(t_minus<=t<=t_plus) ||exp(-itH_phys)E_seed`

` - exp(-ic_total t)J_F[beta_F(t) tensor C_p tensor |1>_R]|| < 3epsilon/8`.

It is uniform over coherent legal programs, logical paths and arbitrary passive references. The radial vector is independent of those inputs. The phase -i, translation 57 and true physical scalar are fixed. The target includes record|1> and vacuum on all I sites, both emitters, every core/mediator/writer/cable head and both F origins. The actual state is neither projected nor renormalized. The unhalved channel distance is bounded by twice the isometry error at the stated checked scope.

## Policy A: one absolute branch target on the full finite horizon

Let B_fin(t) be the SAME B_n(t) sequence restricted to 1<=n<=ell, without normalization. At every t in [0,t_plus] define

`V_tar(t)xi=exp(-ic_total t)J_F[B_fin(t) tensor C_p xi tensor |1>_R]`,

and let P1=|1><1|_R act on the complete physical output space. P1 denotes a mathematical branch, not supplied measurement or control hardware. Fourier synthesis and restriction give ||V_tar(t)||=||B_fin(t)||<=1. This target is not switched at t0, and may have a small nonzero value at zero.

For the exact infinite packet with blank input record, P1 annihilates its incoming identity component at all times. The complete outgoing error is at most deltaS, while the strict internal flagged amplitude is at most T0G0/sqrt(2pi). After t0, the first eight allowances above give a complete actual-to-packet error E_match<epsilon/4. This comparison is made before P1 and pays all actual spectral components. The F-origin omission is bounded uniformly by G0/sqrt(2pi), since a late-time phase gap is unavailable there during transit. The far-F tail is at most 3L/sqrt(ell). Thus for t0<=t<=t_plus,

`||P1 exp(-itH_phys)E_seed-V_tar(t)||`

`<=E_match+deltaS+(T0+1)G0/sqrt(2pi)+3L/sqrt(ell)`

`<epsilon/4+epsilon/512+epsilon/256+3epsilon/10^7<epsilon/2`.

Before t0 the reference record remains blank; its monotone contact envelope bounds the actual flagged norm by Q_budget/u0. The identical V_tar(t) is an early outgoing tail of norm at most 2L/sqrt(ell). Consequently its discrepancy is below epsilon/32 on 0<=t<=t0. Both comparisons use the same phase, logical map and unnormalized radial sequence. They establish

`sup_(0<=t<=t_plus) ||P1 exp(-itH_phys)E_seed-V_tar(t)|| < epsilon/2`.

For A_t=P1 exp(-itH_phys)E_seed, both A_t and V_tar are contractions. Expanding A_t Z A_t*−V_tar Z V_tar* proves an unhalved diamond/completely bounded trace-norm discrepancy below epsilon between the subnormalized branch maps, including every passive reference. The ideal success probability is ||B_fin(t)||^2, independent of the encoded logical input. This absolute comparison cannot be divided by a possibly tiny success probability to infer uniform normalized conditional accuracy.

On the final window the separate full normalized comparator already has record1 and retained-F support. Orthogonality therefore gives both record1 probability and joint record1/F-support probability greater than 1-(3epsilon/8)^2. This eventual high-success conclusion comes from full-output closeness, not from normalizing the all-horizon bound. Policy F alone has no asserted all-horizon branch guarantee.

## Loads and sufficient resource orders

Full-support incident-block norm sums, including inactive programmed blocks, are: core endpoints 6b+6j; mediators D1+2b; endpoint program qubits 2j; mediator program qubits D1-2b; writer terminals 4j; ordinary arm/cable/ray heads 4j; phase-cell endpoints (4+sqrt(2))j; junction vertices (1+3sqrt(2))j; the single shared record 8j. Source emitter and adjacent-site loads are 3j and 5j, and each F cap endpoint has load 3j. The displayed family places every sum below Lambda. Overlapping positive blocks do not require mutual commutation for positivity.

The supplied magnitudes include

`D0=Lambda epsilon/(2*10^5)`,

`b=Lambda epsilon^(3/2)/(2*10^(15/2))`,

`j=Lambda epsilon^2/(2*10^10)`,

`gamma_F=Lambda epsilon^(7/2)/(2048*10^(25/2))`,

`gamma_A=j min{epsilon sqrt(h)/1024,[epsilon/(4096(1+T0))]^2}`.

Gamma is the smallest displayed positive scalar for either policy. These exact small values and correlations are premises, not manufacturing or precision-tolerance certificates.

At fixed B=10, q1,q2,T0,T1 have bounded finite limits as epsilon tends to zero; T0 has a positive finite limit. For example b/(D0-3j)=eta/(1-3eta^2), so mediator coefficients hide no inverse-j divergence. Policy F has rho=Theta(epsilon^(3/2)), L=Theta(epsilon^-3/2) and Q_budget=Theta(epsilon^-9/2). The competing time terms have powers 5 and 11/2, so Q_budget/epsilon dominates. Policy A eventually selects the second rho term, yielding rho=Theta(epsilon^2), L=Theta(epsilon^-2) and Q_budget=Theta(epsilon^-6); its competing powers are 6 and 7. In each case g2 occurs positively in A_i+A_o, giving the lower bound as well as the upper bound for this chosen Q_budget.

| Policy and contract | Size and jt_plus | Physical t_plus | Source gamma |
| --- | --- | --- | --- |
| F: normalized final-window output | Theta(epsilon^(-11/2)) | Theta(Lambda^-1 epsilon^(-15/2)) | Theta(Lambda epsilon^(7/2)) |
| A: absolute horizon branch plus final-window output | Theta(epsilon^-7) | Theta(Lambda^-1 epsilon^-9) | Theta(Lambda epsilon^4) |

The frozen common-maximum-square prescriptions had sufficient size/time powers 13/15 for F and 16/18 for A. The separated maxima with the older derivative ceiling improved these to 13/2 and17/2 for F, and8 and10 for A. Localizing the shrinking cutoff's derivative support gives the present11/2 and15/2, and7 and9. Each comparison fixes its own source policy, cap, architecture, metric, local inverse bound and relative window. These are sufficient analytical families, not measured speedups, optimal powers or necessary lower bounds. F and A provide different contracts. Large fixed constants and asymptotic crossovers can dominate operating ranges. Local inverse sharpening changes constants; it does not itself change these powers.

## Evidence roles and claim boundaries

The stationary composition and exact packet have separate source-exposed analytical checks at their respective scopes. The sharpening includes an exact SymPy matrix certificate; its distinct check used a different rational-similarity/Gauss-Jordan calculation and recovered every row norm and determinant, followed by an analytical continuum perturbation argument. The finite, absolute-branch, resource-split and localized-cutoff compositions are analytical, with distinct source-exposed checks. No finite-device simulation or empirical experiment supplies their proofs. Their complete sources and reports were read in the coherent tasks preceding this integration. ROOT integrated these exact source identities and their complete checked arguments; integration is not another independent check.

ROOT proposed architectures and proof interfaces. Component authors also authored later compositions; the same checking agent reused prior checked premises and saw source arguments. These are disclosed roles and exposure, not blind or model-independent replication. Formal retained status is not assigned here. A successful exact matrix program checks that finite matrix and its assembly correspondence, not automatically the finite-seed proof or physical implementation.

The strongest present contract is policy A's absolute branch guarantee only through t_plus, together with eventual normalized output and high success. During terminal visits a record1 amplitude may remain internal; this is bounded absolutely, not declared absent. Beyond the finite horizon, returning heads can toggle the record. No indefinitely valid herald, uniformly accurate normalized rare-success state, irreversible latch, stationary output, permanent halt, capture/reset or arbitrary-time readout mechanism follows. Native Record identification, autonomous initialization, measurement/readout, physical units, coefficient supply and error tolerance remain open interfaces. The supplied apparatus does not replace an old literal processor or derive new physical laws.

## Portable evidence and source identities

The [portable source manifest](../outputs/common_product_stage_record_2026_10_18/SOURCES.json) maps every complete source and check to its SHA256 and repository path, including preserved earlier sufficient bounds. The integration record (`outputs/common_product_stage_record_2026_10_18/INTEGRATION_RECORD.md`) documents the synthesis and its limits. The parent manifest and inherited files retain the exact core, launch, normalized spectral and cell premises; historical nonpremise evidence remains marked as such.

The new direct proof chain consists of stationary core c91300a5 / check61de4ee2, packet3477197c / check17029fa3, finite7286105f / check60896f1b, writer sharpening22bca57e / exact programf1deb1c3 / output218168f4 / distinct checkd96ed6b2, flag e7b53eed / checke548a664, split c4086aec / checkd697d3cd, and localized cutoff550946fd / check6a4866e7. Complete hashes, not these display abbreviations, identify the portable files. The actual local writer93445d7d / checkc5f3e1d7 is bundled directly; no earlier literal processor or interacting-channel runtime is imported through it.

Component authors also derived later compositions, checkers reused frozen premises, and ROOT proposed architecture/proof interfaces. The synthesis was drafted by a component checker and reviewed by ROOT. All exposure is disclosed; repeated agreement or report count does not establish independence. The earlier literal apparatus already had a separate fixed-accuracy flag result; this new arbitrary-accuracy family is a supplied encoded controlled router, not a claim of the first record result or a replacement of that literal processor.

## Portable finite controls

Primary runner: `scripts/common_product_program_controls_2026_10_18.py` (timeout: 120 seconds). Its literal declared input closure includes all ten canonical notes and their live proof dependencies. It checks finite physical matrices, complete scattering and explicit sufficient budgets; finite controls corroborate these supplied conditional theorems and do not establish native realization or replace their analytical proofs. Historical statements above about what was executed describe original authorship; this added primary has a separate owner capture.
