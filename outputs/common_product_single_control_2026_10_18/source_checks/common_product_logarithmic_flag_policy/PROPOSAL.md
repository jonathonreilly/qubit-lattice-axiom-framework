# A logarithmic source policy for the finite-horizon flag branch

New bounded author derivation requiring a distinct check. The exact normalized source L1 bound permits an absolute flag-branch family with rho of order epsilon^(3/2), rather than the order epsilon^2 chosen by the earlier square-root L1 ceiling. Using the separately checked localized derivative bound G2<600/rho^3 and split time budgets gives sufficient size order epsilon^(-11/2) and physical time order Lambda^-1 epsilon^(-15/2), while retaining the absolute branch contract on the whole finite horizon and normalized output on its final window. These match the powers of the corresponding finite-output-only family, with different constants and a stronger contract. No optimality, practical performance or native physical interpretation is inferred.

ROOT supplied the logarithmic candidate, inequalities and proposed exponents. I reconstructed the constants, normalization hypotheses and finite interfaces after that exposure. This is newly authored composition, not independent verification. Earlier flag, resource and publication sources remain unchanged. Only this proposal is written.

## 1. Frozen physical object and order of choices

Use the exact finite staged device from finite source7286105: four microscopic core cells with twelve distinct legal program controls, two34-edge cables, two24-head writers sharing one physical record R, two I emitters at M=ell+1, and two F rays capped at ell by positive j n_ell. The source block is

`B_I=Q_gamma(ell,ell+1)+(j-gamma)n_ell+(2j-gamma)n_(ell+1)`.

Its source and neighboring diagonals are2j, as are the capped F end diagonals. The target uses F sites1,...,ell, excluding the two physical writer origins. Exact graph, signed junctions, two phase cells per writer, all scalar compensations and installed-neighbor conventions are unchanged. The common physical scalar is c_total=8b+2c_R, c_R=4(sqrt(2)-1)j. The common stationary phase is -i exp(57ik).

The supplied seed has one head at the encoded I emitters, the legal twelve-bit program, blank R=|0>, and all other heads vacant. Arbitrary encoded path/program coherence and passive references are retained. The desired path action is C_0=X and C_1=I, preserving the program and reference.

For0<epsilon<=1 and supplied Lambda>0, first select

`h=epsilon/10^5`, `eta^2=zeta=epsilon/10^5`,

`D1=Lambda/2`, `D0=zeta D1`, `b=eta D0`, `j=b^2/D0`.

Use the checked writer inverse B=10 and the conservative packet-form constants a0=20,a1=w1=800,w2=56000. Recompute every core, feedback, external derivative and internal-map constant from packet347719 equations(7)--(13): c1,c2,m0,m1; f1,f2,k0,k1,k2; cable-map product derivatives; s1,s2; q1=s1+57,q2=s2+114s1+57^2; and the endpoint/mediator/writer/cable sums T0,T1. The sharper620/37820 local alternatives are not mixed in. No old values computed at B=10^31 are retained.

T0 bounds the strict internal coefficient map (and may be the packet's conservative full122-coordinate bound). These stationary quantities have no dependence on the future rho, gamma, ell or times. Then define

`alpha=[4096(1+T0)]^-2`,

`rho=alpha epsilon sqrt(h)`, `gamma=rho j`.               (1)

This is noncircular. Alpha may depend on epsilon through the already computed T0; it is not assumed constant in finite-epsilon inequalities. Its positive finite limit is established separately for asymptotic counting below. This is a new source policy, not an assertion that either earlier policy's physical source was unchanged.

## 2. Actual source mass, phase and logarithmic L1 estimate

Use the same real C2 cutoff chi: plateau |k-pi/2|<=h/2, quintic1-10s^3+15s^4-6s^5 transition of width h/4, and zero beyond3h/4. Let

`F(k)=-i sqrt(2/pi)rho exp(ik)/[(2-rho^2)cot k-i rho^2]`,

`p_chi=||chi F||_2^2`, `g=chi F/sqrt(p_chi)`,

`G_r=||g^(r)||_1` for r=0,1,2.

The square root is the actual positive normalization; the complex source phase is unchanged. Since T0>=0, alpha<=4096^-2<1/1024. Thus rho<=epsilon sqrt(h)/1024, rho<=1/2, and

`rho^2/h=alpha^2 epsilon^2<=1/1024^2`.

The checked complete source measure gives omitted mass P<=3rho^2/h and p_chi>=1-P>1/2, with p_chi<=1. Also rho^2<=h<=10^-5 and h>=rho^2/(2-rho^2). The latter ensures the resonance crossover lies inside the interval used in the L1 integral. Neither mass normalization nor the crossover is inferred merely from a small bandwidth.

Write q=k-pi/2 and a=2-rho^2>=7/4. The exact amplitude obeys

`|F(k)|<=sqrt(2/pi) min{1/rho,rho/(a|q|)}`,

because its denominator modulus is at least rho^2 and a|q|. Integrating over[-h,h], splitting at |q|=rho^2/a, and dividing by the same sqrt(p_chi)>=1/sqrt(2) yields

`G0 <= (4/sqrt(pi))(rho/a)[1+log(ah/rho^2)]`

`   <= 4rho[1+log(2h/rho^2)]`.                         (2)

The bracket is positive under the crossover condition. This is the already accepted exact-profile inequality of the flag source; no pointwise resonance height is mistaken for a normalized integral.

Substitute(1) and h=epsilon/10^5. Then 2h/rho^2=2/(alpha^2 epsilon^2), so

`G0/epsilon <= (4/sqrt(10^5)) alpha sqrt(epsilon)`

`                 *[1+log2+2log(1/alpha)+2log(1/epsilon)]`. (3)

For every x in(0,1], sqrt(x)log(1/x)<=2/e: put y=sqrt(x) and maximize -2y log y at y=e^-1. Likewise

`alpha log(1/alpha)<= (2/e)sqrt(alpha)`.

Using sqrt(epsilon)<=1 and alpha<=sqrt(alpha), the bracketed product in(3), including the leading alpha sqrt(epsilon), is at most

`[(1+log2)+4/e+4/e]sqrt(alpha)`

`=(1+log2+8/e)sqrt(alpha)<5sqrt(alpha)`.                (4)

For the strict last inequality it suffices to use log2<1 and e>8/3, giving1+log2+8/e<2+3=5. This handles all0<epsilon<=1 even though alpha depends on epsilon. It does not replace alpha by its limiting value.

Consequently

`G0/epsilon < (20/sqrt(10^5))sqrt(alpha)`

`             =20/[4096 sqrt(10^5)(1+T0)]`

`             <1/[256(1+T0)]`.                         (5)

The final constant inequality is simply sqrt(10^5)>5/4. Thus the new logarithmic policy supplies the same uniform internal-plus-origin amplitude budget used by the accepted flag proof:

`(1+T0)G0<epsilon/256`.                                (6)

The smaller epsilon power in rho is possible because(2) was used directly rather than replaced by the coarser16sqrt(rho) ceiling. No logarithmic factor is hidden in the chosen rho; the elementary maximum in(4) pays the entire epsilon interval with a fixed sufficient constant.

## 3. Recomputed source derivatives and split budgets

The separately checked localized-cutoff derivative source550946 applies: rho<=1/2, rho^2<=h<=10^-3 and p_chi>=1/2 have all been established. Retain

`G0<=1`, `g1=80/rho`, `g2=600/rho^3`, `bminus=82/rho`.

Here G1<=g1, G2<g2 and the raw incoming launch coefficient is bounded by bminus. The exact phase derivatives and both cutoff transition intervals are paid in that derivative theorem. No further derivative improvement is assumed. The loose G0<=1 remains available for the finite comparison; the stronger(6) is used only for the uniform flagged/internal/origin terms.

With v_min=2j cos h and v_max=2j, define afresh

`H1=g1+q1`, `H2=g2+2q1 g1+q2`,

`J0=T0`, `J1=T0g1+T1`,

`A_i=g2+(12j/v_min)g1+4j/v_min+48j^2/v_min^2`,

`A_o=H2+21H1+154`,

`L=max{1,bminus,g1+1,H1+1,g1+7}`,

`Q_budget=max{1,eta^-1,rho^-2,J1+J0,A_i+A_o}`.

Then choose

`u=10^12 max{1,(L/epsilon)^2,Q_budget/epsilon}`,

`ell=ceil(100u)`, `M=ell+1`, `t0=u/j`,

`t_minus=3ell/(4j)`, `t_plus=7ell/(8j)`.                 (7)

All coefficients are explicit before u and ell are chosen. Q_budget denotes a scalar budget, not a hopping operator. In particular A_o's constants21 and154 follow from the fixed cut/window ratios, not an unresolved dependence on t_plus. Equation(7) gives

`L/sqrt(u)<=epsilon/10^6`, `Q_budget/u<=epsilon/10^12`,

`sqrt(ell)>=10sqrt(u)`, `ell>=100u`.

The source ratio, all source-dependent derivative bounds, distance, times and outgoing scalar sequence must be recomputed for this policy. Neither previous durations nor old K values are retained.

## 4. Complete finite-output comparison

The checked finite construction's operator comparison is unchanged in form. Its reference keeps the entire actual internal/F submatrix, including mediator energies and shared-record contacts, but the reference seed occupies only the detached launcher subspaces. Their norm bound is4j; no such norm bound is made for the actual device. The contact difference includes the +j I-origin diagonal, removed reference edge and actual mediator couplings, with norm at most2j+sqrt(2)b. Reference powers below degree M cannot reach that contact. Thus the same Taylor/Duhamel estimate gives

`E_early<=(2+sqrt(2)/eta)/(5000u)<=Q_budget/u`.

The actual source/F caps still have diagonal2j. Hopping-only outer perturbations therefore identify the finite generator exactly with a summand of the perturbed infinite network, with auxiliary Dirichlet exteriors. The integrated twice-IBP error is at most2(A_i+A_o)/u<=2Q_budget/u. The newly justified g2 enters both incoming and outgoing second-derivative coefficients; all q1,q2 source-phase terms remain in H2. No actual seed bound-state component is set to zero: the full-vector early comparison pays everything absent from the normalized packet.

All twelve allowances are:

| Allowance | Ceiling |
| --- | --- |
| Actual/reference early contact | Q_budget/u |
| Twice source survival | 2Q_budget/u |
| Twice incoming launch remainder | 2L/sqrt(u) |
| Spectral cutoff tails | 4sqrt(3)epsilon/1024 |
| Right early projection replacement | 8L/sqrt(u) |
| Early lead matching | 4L/sqrt(ell) |
| Early internal matching | 3Q_budget/ell |
| Integrated finite boundary | 2Q_budget/u |
| Twice late incoming tail | 6L/sqrt(ell) |
| Twice complete scattering error | epsilon/256 |
| Twice late internal amplitude | 56Q_budget/ell |
| Final normalized F truncation | 28L/sqrt(ell) |

The spectral term uses rho<=epsilon sqrt(h)/1024, not equality. The scattering bound depends only on e=18epsilon/10^5 and w=33epsilon/10^5, so deltaS<epsilon/512 is unchanged by the new rho. Source survival retains rho^-2 in Q_budget, the microscopic contact retains eta^-1 there, and internal costs retain J0+J1. Every displayed allowance is strictly below epsilon/32 by(7); the spectral term is below epsilon/128. The sum is below3epsilon/8.

Since u>=10^12 and ell>=100u, the early gap ell-2u>=ell/2, t0v_min>2, and t_plus v_max<2ell-2. Both t_minus v_min-ell and t_minus v_min-ell-57 exceed ell/4; the far-cut gap is at least ell/4. The same allocations establish launch normalization, D_L<1/2 and2tau_F<1 before either comparator normalization. The relative final-window width is1/6; there is no physical Hamiltonian switch.

Define at the NEW ell

`B_n(t)=(-i)/sqrt(2pi) integral exp(i[n+ell+57]k-itE(k))g(k) dk`,

`E(k)=2j(1-cos k)`, `B_fin(t)=P_(1<=n<=ell)B(t)`.

Its positive normalization beta_F(t)=B_fin(t)/||B_fin(t)|| exists throughout[t_minus,t_plus]. The proposed complete-output conclusion is

`sup_(t_minus<=t<=t_plus) ||exp(-itH_phys)E_seed`

` -exp(-ic_total t)J_F[beta_F(t) tensor C_p tensor |1>_R]||`

` <3epsilon/8`.                                                   (8)

This is the encoded-input operator norm, uniform over coherent legal programs and arbitrary passive references. The common radial vector is independent of them. Every other head, including emitters, all original finite-network heads and both F origins, is vacant only in the comparator; every actual residual remains in the error. No actual state is projected or normalized in(8).

## 5. One absolute branch target for the whole horizon

At every time in[0,t_plus], use the SAME unnormalized target

`V_tar(t)xi=exp(-ic_total t)J_F[B_fin(t) tensor C_p xi tensor |1>_R]`.

Its norm is at most1 by full-integer Fourier synthesis and restriction. Let P1=|1><1|_R on the full physical output. It is mathematical branch notation, not a supplied measurement operation. The comparator is not set to zero before t0 or switched at matching, and the phases -i,57 and c_total are never fitted away.

For the exact packet, its incoming identity component has record0 and is annihilated by P1 at every time. The full outgoing discrepancy from the ideal routing-and-X map is at most deltaS. Its strict internal flagged vector is bounded uniformly by T0G0/sqrt(2pi). The removed F-origin amplitude is bounded by G0/sqrt(2pi) uniformly during transit; no late-phase-gap estimate is used there. Thus(6) pays the internal and origin terms together.

On[t0,t_plus], the first eight allowances give the complete actual/packet match E_match<epsilon/4 before P1 is applied. The far-F tail is at most3L/sqrt(ell). Consequently

`||P1 exp(-itH_phys)E_seed-V_tar(t)||`

` <=E_match+deltaS+(T0+1)G0/sqrt(2pi)+3L/sqrt(ell)`

` <epsilon/4+epsilon/512+epsilon/256+3epsilon/10^7<epsilon/2`.

On[0,t0], the reference remains recordblank because its internal/F heads are vacant. The monotone actual/reference contact envelope is at mostQ_budget/u. The identical B_fin(t) is an early outgoing tail with norm at most2L/sqrt(ell). Hence the early discrepancy is at mostepsilon/10^12+2epsilon/10^7<epsilon/32. Combining the overlapping intervals proves the proposed stronger contract

`sup_(0<=t<=t_plus) ||P1 exp(-itH_phys)E_seed-V_tar(t)||`

` <epsilon/2`.                                                   (9)

Both maps are contractions, so the usual two-term expansion of AZA*−VZV* bounds the unhalved subnormalized-channel/diamond discrepancy by twice(9), hence below epsilon with arbitrary references. The ideal branch trace ||B_fin(t)||^2 is input independent. No normalized rare-success guarantee is obtained by dividing this absolute error by a possibly small probability.

Separately, (8) and orthogonality give record1 probability and joint record1/retained-F-head probability greater than1-(3epsilon/8)^2 on the final window. These probabilities concern specified projectors, not a physical readout supplier. Internal flag events are allowed during transit and charged absolutely; after t_plus neither(9) nor protection against returning heads is asserted.

## 6. Loads, counts and sufficient orders

For this newly selected ell, the physical counts remain137+4ell qubits and168+4ell listed positive blocks. The same full-support incident sums remain below Lambda: core endpoints6b+6j, mediatorsD1+2b, endpoint controls2j, mediator controlsD1-2b, sharedR8j, ordinary heads4j, phase endpoints(4+sqrt(2))j, junction vertices(1+3sqrt(2))j, source emitter3j, source-adjacent5j and F caps3j. Shrinking gamma leaves the source block norm and cap convention valid. No inactive control or shared record contact is omitted from those sums.

With fixed B=10, the explicit q1,q2,T0,T1 have finite limits as epsilon tends to zero. This follows from the already checked dimensionless core/feedback formulas: mediator ratios such as b/(D0-3j)=eta/(1-3eta^2) remain bounded, and den tends to1. T0 has a positive finite limit T0*. Therefore

`alpha -> alpha*=[4096(1+T0*)]^-2>0`,

`rho=Theta(epsilon^(3/2))`, `gamma=Theta(Lambda epsilon^(7/2))`.

Although alpha varies at finite epsilon, its positive finite limit supplies the matching asymptotic upper/lower constants. Thus

`g1,bminus,L=Theta(epsilon^(-3/2))`,

`g2=600/rho^3=Theta(epsilon^(-9/2))`,

`Q_budget=Theta(epsilon^(-9/2))`.

For Q_budget, all other entries have order at mostepsilon^-3 from rho^-2, epsilon^-3/2 from J0+J1 and first derivatives, or epsilon^-1/2 from eta^-1. The positive occurrence of g2 in A_i+A_o gives the matching lower bound. In(7), (L/epsilon)^2 has order epsilon^-5 and Q_budget/epsilon has order epsilon^(-11/2), so the latter eventually dominates. Hence

`u,ell,qubit_count,block_count,jt_plus=Theta(epsilon^(-11/2))`,

`t_plus=Theta(Lambda^-1 epsilon^(-15/2))`.               (10)

The exact source coefficient is gamma=alpha Lambda epsilon^(7/2)/(2*10^(25/2)), retaining its supplied alpha dependence. Gamma is smaller than the fixed positive j coefficients and the other displayed positive magnitudes. Its magnitude is not a fabrication tolerance or cost model.

For the same fixed B and localized derivative ceiling, finite-output policy F has the same sufficient powers11/2 and15/2 but rho_F=epsilon sqrt(h)/1024. The new logarithmic policy multiplies epsilon sqrt(h) by a much smaller T0-dependent factor to obtain the additional absolute horizon contract. Equality of exponents does not imply equality of prefactors, durations or physical source couplings.

Relative to the earlier square-root-L1 policy A with the SAME localized derivative ceiling, its sufficient size/time powers7/9 become11/2 and15/2 for the same absolute branch plus eventual-output contract. Relative to the older1200/(h rho^3) ceiling the historical powers differ again; they are not silently used here. All comparisons concern sufficient analytical families at the same accuracy convention, cap, architecture and relative window, not a measured speedup of a fixed apparatus, an optimal exponent or a lower bound. Large constants and crossovers can dominate useful epsilon ranges.

## 7. Evidence, chronology and required distinct check

N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. The new necessary derivative argument and its check were read completely and hash-verified during this derivation:

- N/`common_product_narrow_cutoff_derivative/PROPOSAL.md`: `550946fdebc4e68522c997ed914e23a8baf40cb660dfc22e4f09e00add1216a3`.
- N/`common_product_narrow_cutoff_derivative_check/REVIEW.md`: `6a4866e76cc5c6c760284c9a3f6c07c71410f701d727e8765edc8f6a57d328a4`.

Previously complete reads are reused at their unchanged checked scopes:

- Split source N/`common_product_stage_record_resource_split/PROPOSAL.md`, hash refreshed `c4086aec4d338da11dcea256367e34ceea496044ca7ff1bc30ca55ee5489f977`; my distinct split check `d697d3cdb72ee52a62f3508245a87239108937819f41966c120bc149d674befa`.
- Flag source N/`common_product_stage_record_flag_branch/PROPOSAL.md`, hash refreshed `e7b53eeda3fc7df96986d3b55f68d9e5af4f1b6657ba068b6f33d03e18a37ee0`; check `e548a664449546f76fbad2b24d5c7bcf5e0d318ecb6dd75f4234fb078ccdae5a`.
- Finite source7286105ffd9b6b6d0caa97b121c5e79d37dfcf638128d63c6bbc144e9aa2a995/check60896f1b1b4b76d27158ce46e097565d1ed777d45ee4dc1c394b02d52ac71a9f, whose section8 proves the parameterized writer-bound substitution interface.
- Packet3477197cdf54d18ab538c517726d64f3dbc556f6ddb7a6d4b2608b458d34eeb9/my check17029fa32989bae3869c4ffee81def65201edc0f0b996013ede8996ca8cf1453.
- Writer sharpening22bca57ebcbfb8cfabebbe044cd5302e784e585b503cee28d6172afc72e54cf0/my distinct checkd96ed6b26856490d802ceed2009f75aa9c0919eb8760bcfffe0389807965d1b5.
- Stationary sourcec91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729/check61de4ee29dd3838c4fc7c3bd19c49bf0cd4cb4bacf5ad3e8e10ca06c864e27c1, and their actual writer/core inventories.
- Exact launchfb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4 and general derivative378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8 retain the full normalized source and phase premises used in the checked descendants.

The exact local writer matrix certificate and its separate alternative exact computation remain component evidence only. This task executed no scientific program or numerical sweep. Its new claims are analytical composition after ROOT's exposed candidate. I previously checked packet, writer sharpening and split resources and drafted publication notes; those roles are shared exposure, not independent validation of this new source. A distinct reviewer must verify(3)--(5) uniformly with epsilon-dependent alpha, actual normalization/crossover hypotheses, the full recomputation at the new rho, all twelve allowances, unchanged all-horizon target, and asymptotic lower as well as upper bounds. No retained or formal audit status is assigned.

Supplied coefficients and correlations, legal encoding, blank apparatus/record preparation and passive-reference structure remain premises. No old literal processor transfer, native Record law, readout supplier, autonomous initialization, coefficient-error tolerance, indefinite guarantee, irreversible latch, capture/reset or permanent halt follows. Only this `common_product_logarithmic_flag_policy/PROPOSAL.md` was created. Existing e7b53/c408 sources, publication notes and current record PR remain untouched. No W/Git/checkpoint/editable-prompt/model change, publication or delegation occurred.
