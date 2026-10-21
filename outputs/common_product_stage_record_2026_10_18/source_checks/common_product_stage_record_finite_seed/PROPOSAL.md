# Finite emitter seeds for the staged shared-record router

New bounded author composition requiring a distinct check. This proposal uses the frozen stationary network c91300a5 and the explicit packet bounds3477197c, both now supported at their exact component scopes by distinct checks. The new finite composition still requires its own distinct check. It constructs actual positive finite I-ray emitters and F-ray ends, proves full seed-to-packet matching and finite boundary comparison, and gives a simultaneous sufficient family with a normalized common F output throughout a positive-width window. It is not an all-time completion/herald theorem.

ROOT requested finite composition and suggested the early contact strategy. All parameter choices and allocations below are reconstructed here. The packet's conservative writer inverse B=10^31 is retained. A separately suggested sharper inverse and an all-time flagged-branch route are not premises and are not claimed here.

## 1. Actual finite positive device and input

Use the exact cubic core/two-writer/shared-R network of c91300a5, including its two34-edge cables and modified external I/F paths. The finite network before rays has135 qubits and164 positive blocks. Both I and F radial coordinates start at the already existing core/writer port heads n=0. Let ell be a positive integer, M=ell+1.

On each I ray retain sites n=0,...,M, ordinary Q_j bonds through n=M-2, and the positive source block

    B_I=Q_gamma(M-1,M)+(j-gamma)n_(M-1)
                                      +(2j-gamma)n_M.

On each F ray retain sites n=0,...,ell, every intervening ordinary Q_j bond, and add the positive terminal occupation j n_ell. Thus the last F site's one-head diagonal is2j, not j. The I source and its adjacent site also have diagonal2j. All unlisted interactions remain absent. Geometric paths are prefixes of the disjoint infinite rays already supplied by c91300a5, so no new collision or nonlocal edge is introduced.

The exact true scalar is c_total=8b+2c_R, c_R=4(sqrt(2)-1)j. Sources and F caps introduce no extra scalar. Write h_F=H_phys-c_total I on the invariant one-head/legal-program/record space.

The supplied seed E_seed xi puts its single head at emitter M on I0 or I1, with arbitrary logical path/program/reference input xi, the twelve-bit legal program encoding, and the ONE shared record in|0>. Every other head is vacant. Arbitrary logical coherence is supplied, while basis path/program seeds with blank apparatus are occupation products. The target will preserve the program and passive reference, apply C_p to logical path, set this same record to|1>, and have its one head only on F ordinary sites1,...,ell. In particular both I emitters, both core I origins, both F writer origins, all mediators/writer/cable heads and other I sites are vacant in the comparator. Actual output is never projected or renormalized.

Counts are137+4ell qubits and168+4ell listed positive blocks: two I extensions add2M sites and2M combined source/bond blocks, and two F extensions add2ell sites and2ell+2 bond/cap blocks. External-ray infinity is removed physically; auxiliary spaces used below are not resources.

## 2. Complete early comparison to actual standalone launchers

For comparison only, extend the finite I rays through negative n<=-1 by independent Dirichlet half-lines, and extend beyond every finite outer cut with independent Dirichlet lines. All auxiliary onsite diagonals are2j. Retain the physical internal heads and record/program fibers.

Define h_ref by two independent reversed standalone launchers, each with emitter M, lead coordinate x=ell-n>=0, and lead continuation through the negative I coordinates. On the remaining internal/F subspace retain the ENTIRE actual h_F submatrix, including its mediator energies, writer phase cells, terminal/record contacts and F caps. Decouple only its connections to the two I origins; retain the same diagonal entries on the internal/F subspace. Auxiliary positive exteriors remain decoupled. This reference is self-adjoint and bounded for fixed parameters; no4j bound is asserted for its full norm.

The reference seed evolves entirely within the two launcher spaces, where the norm bound is4j. Its remaining heads are vacuum. After subtraction of the common scalar, all rest-submatrix terms annihilate that head vacuum, including j n_T X_R; the initially blank record is therefore unchanged by the reference. Large mediator or writer coefficients are not dropped from an actual evolution: they are in the common rest block, which is unoccupied in this reference trajectory.

The actual-reference difference V consists of a +j diagonal change at each I origin (its actual diagonal3j versus reference2j), deletion of its reference edge to n=-1, and its actual two mediator hoppings-b. The two I origins meet disjoint pairs of mediator heads. The contact diagonal/edge matrices [[j,j],[j,0]] have norm<2j, and the mediator incidence has norm sqrt(2)b. Thus

    ||V||<=2j+sqrt(2)b, V=V P_contact.

From emitter M, reference powers below degree M cannot reach contact. With u0=j t0_time, ordered Duhamel using the actual full unitary yields

    E_early=min{2,u0(2+sqrt(2)/eta)
                          sum_(r>=M)(4u0)^r/r!}. (1)

This pays the full microscopic contact strength. No actual H norm or writer norm is falsely bounded by4j. For ell>=100u0, the factorial tail is <2*8^-M<=2/M^2, hence

    E_early<=(2+sqrt(2)/eta)/(5000u0).          (2)

All reference subspaces and vacuum qualifications are explicit. This comparison makes no assertion about finite-device spectral completeness or absence of localized components.

## 3. Narrow-band launch costs, derived for this family

Fix0<epsilon<=1 and choose

    h=epsilon/10^5,
    eta^2=zeta=epsilon/10^5, eta>0,
    rho=epsilon sqrt(h)/1024,
    D1=Lambda/2, D0=zeta D1, b=eta D0,
    j=b^2/D0, gamma=rho j.                     (3)

Use one real C2 cutoff chi with plateau |k-pi/2|<=h/2, a quintic1-10s^3+15s^4-6s^5 transition of width h/4, and zero beyond3h/4. Its support lies strictly within the conservative band |k-pi/2|<h. Its derivative bounds are K1<=8/h, K2<=100/h^2. Both phases and the actual positive normalization of

    F(k)=-i sqrt(2/pi)rho exp(ik)/[(2-rho^2)cot(k)-i rho^2],
    p_chi=||chi F||_2^2, g=chi F/sqrt(p_chi)

are retained from the exact standalone launcher.

The checked general-cutoff spectral estimate gives

    P<=4rho^2/[pi(2-rho^2)^2 tan(h/2)]
       <=3rho^2/h,
    p_chi>=1-P>1/2.                            (4)

Here tan(h/2)>=h/2 and2-rho^2>=1. The last strict normalization condition follows directly from(3). The general derivative formulas of378086 apply with L=tan h<=2h, S=sec^2 h<=2. Substituting K1,K2 into their explicit constants, and using2/sqrt(pi)<2, gives the safe NEW ceilings

    G0<=1,
    G1<=g1=80/rho,
    G2<=g2=1200/(h rho^3),
    B_minus<=bminus=82/rho.                    (5)

For example the G1 constant is at most2[4h(8/h+1)+pi]<80. The G2 constant is at most

    2[4h(100/h^2+16/h+1)+(16/h+2)pi+8h+16]
       <=1200/h,

in the stated h-domain. The derivative source's sufficient rho-domain is satisfied because rho<=1/2 and rho^2<=pi tan(h/2)/8. The raw incoming coefficient equals sqrt(p_chi)[G1+sec(h)G0], so its bound in(5) follows. The extra h^-1 in G2 is explicitly paid. No fixed-wide-cutoff constant is reused unchanged.

For t0_time>0 the original checked launch bounds give

    delta_launch=sqrt[R0^2+(L0+2sqrt(P))^2],
    R0<=min{1,1/(rho^2 u0)},
    L0<=bminus/sqrt(u0),                        (6)

when u0>=1, since v_min=2j cos h>=j. A sharper survival envelope is not needed or imported. Reversing x=ell-n identifies the launched target with the positive normalization of the full-integer incoming profile restricted to n<=ell, with the exact phase exp(iell k).

## 4. Explicit constant prescription and early microscopic match

Compute every scattering/internal constant from packet347719 equations(6)--(13) using(3), with its valid B=10^31, and denote its final q1,q2,t0,t1 by q1,q2,T0,T1 to avoid confusion with t0_time. Use the actual packet velocity v_min=2j cos h and v_max=2j. Define sufficient amplitude coefficients from(5), not unknown fitted norms:

    G0bar=1, G1bar=g1, G2bar=g2,
    H0bar=1, H1bar=g1+q1,
    H2bar=g2+2q1 g1+q2,
    J0bar=T0, J1bar=T0 g1+T1,
    A_i=g2+(12j/v_min)g1
                      +(4j/v_min+48j^2/v_min^2),
    A_o=H2bar+21H1bar+154.

Finally choose the explicit finite maximum and times

    K=max{1,eta^-1,rho^-2,bminus,
          g1+1,H1bar+1,J1bar+J0bar,
          A_i+A_o,g1+7},
    u0=(10^6 K/epsilon)^2,
    ell=ceil(100u0), M=ell+1,
    t0_time=u0/j,
    t_minus=3ell/(4j), t_plus=7ell/(8j).          (7)

There is no circular dependence: packet constants depend only on eta,zeta,h and fixed cables/writers; A_i,A_o likewise do not depend on ell or the observation times. All constants are explicit algebraic functions of supplied quantities and the fixed enormous B. In particular u0>=10^12 and ell>1000.

The geometry has early matching gap ell-t0_time v_max>=ell/2. Packet347719 equation(16), the normalized-launch comparison, and replacement of its right-tail projection give an actual early full-vector error bounded by

    E_early+2R0+2L0+4sqrt(P)+2d_right
                           +e_leads+e_internal, (8)

where safe ceilings are

    2d_right<=4(g1+2)/sqrt(u0),
    e_leads<=2[(g1+1)+(H1bar+1)]/sqrt(ell),
    e_internal<=(2J1bar+J0bar)/ell.

To see the first bound, the right incoming-tail gap1+t0_time v_min is at least u0, so the packet Tail formula bounds d_right by2(g1+2)/sqrt(u0). For the two lead early gaps at least ell/2, the square-root tail factor is at most2/sqrt(ell), and2jt0_time/q<=1; the phase57 only increases the outgoing gap. For the internal term use q>=ell/2 and u0<=ell/100. All auxiliary negative-coordinate tails are charged; the two final compared vectors are physical finite/infinite-network vectors with zero auxiliary negative support.

This full-vector initial match pays every actual spectral component absent from the normalized packet. No bound-state seed weight is set to zero, and no finite/infinite spectral projections are identified. The same bound is an isometry bound for arbitrary supplied xi and passive references with blank sharedR.

## 5. Exact finite boundary perturbation and integrated residual

On each I ray of the infinite staged network add

    Delta_I=(j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2),

and on each F ray add

    Delta_F=j Adj(ell,ell+1).

These modify hoppings only. The infinite relative generator plus their sum equals the actual finite h_F direct-summed with exterior Dirichlet lines of diagonal2j. The added physical F cap j n_ell is precisely what makes this identity true. The perturbation has norm at most sqrt(2)j and is zero on every core/writer/internal coordinate. Each contact vector uses at most the three radial levels ell,ell+1,ell+2 over the four ports, so the square-root counting factor is sqrt(3), not the sum over four ports.

For the exact packet, incoming phase derivatives at contact have magnitude at least q_i(t)=t v_min-1; the outgoing derivatives, with their actual phase57, have magnitude at least q_o(t)=2ell-t v_max. For t0_time v_min>2 and t_plus v_max<2ell-2 both are positive on the interval. Twice integration by parts gives the same explicit contact envelope structure as the microscopic packet, now with G and H from this narrow-band composed packet. Its integrated Duhamel ceiling is

    E_boundary <=sqrt(3)sqrt(2)j/sqrt(2pi) * {
      (A_i/v_min)[1/q_i(t0_time)-1/q_i(t_plus)]
     +(A_o/v_max)[1/q_o(t_plus)-1/q_o(t0_time)] }
      <=2(A_i+A_o)/u0.                         (9)

For the outgoing coefficient, the general twice-IBP numerator is bounded by H2bar+(6jt_plus/q_o(t_plus))H1bar
 +(2jt_plus/q_o(t_plus)+12j^2t_plus^2/q_o(t_plus)^2)H0bar.
Since q_o(t_plus)=ell/4 and jt_plus=7ell/8 this is exactly at most A_o. The incoming numerator A_i follows from the contact incoming gap and |E''|,|E'''|<=2j. The prefactor is <j, q_i(t0_time)>=u0/2, v_min>=j and v_max=2j. These facts give2A_i/u0+2A_o/ell, hence the last safe inequality in(9).

The squared-derivative calculation can also be verified directly: after two integrations the numerator has bounds ||f''||/q^2+3||f'|| |phi''|/q^3+||f|| |phi'''|/q^3+3||f|| |phi''|^2/q^4. Compact C2 support eliminates both boundary terms. Applying this with the incoming/outgoing phases gives the stated conservative coefficients. No internal writer boundary, omitted return or elapsed effective-cell replacement is hidden in(9). The exact full packet evolves under the microscopic network; the perturbed unitary propagates the entire initial error.

## 6. Common normalized final output throughout the window

Let B_n(t) be the packet source's common scalar outgoing sequence

    B_n(t)=(-i)/sqrt(2pi) integral
                       exp(i[n+ell+57]k-itE)g(k)dk.

The target radial state beta_F(t) is its positive normalization on1<=n<=ell. This excludes n=0 at both writer final ports, so all finite-network heads are vacant in the target. It is shared by both logical paths, both programs and the one record. The proposed physical comparator is

    exp(-ic_total t) J_F[beta_F(t) tensor C_p xi tensor|1>_R].

The order of the program/path/reference factors follows the seed encoding; no reference factor is acted on. The common -i, shift57 and physical scalar are never fitted away.

On the whole window, t_minus v_min-ell>ell/4 and
t_minus v_min-ell-57>ell/4. The latter follows from cos(h)>.99 and ell>1000. Also2ell-t_plus v_max=ell/4. Mixed-endpoint packet envelopes therefore give

    d_L<=3(g1+7)/sqrt(ell),
    m_L<=(4J1bar+28J0bar)/ell,
    D_L=d_L+deltaS+m_L,
    deltaS<epsilon/512.                        (10)

The last inequality follows from e=18epsilon/10^5, w=33epsilon/10^5 in the exact feedback ceiling, with ew<=594/10^10. This preserves the writer's bandwidth error as well as both detuning errors.

The omitted outgoing coordinates consist of n=0 and n>=ell+1. For n=0 use the late phase gap t_minus v_min-ell-57 and the numerator bounded using t_plus; for the far tail use the outgoing gap2ell+57-t_plus v_max. A sufficient sum is

    tau_F<= (4g1+28)/ell+3(g1+7)/sqrt(ell)
          <=7(g1+7)/sqrt(ell).                 (11)

The scalar full outgoing norm is at least1-D_L by exact packet normalization. If D_L<1/2, then normalized truncation error is at most2d_cut, where d_cut<=2tau_F. Thus the total final output comparison is bounded uniformly by

    E_early+2R0+2L0+4sqrt(P)+2d_right
      +e_leads+e_internal+E_boundary
      +2d_L+2deltaS+2m_L+4tau_F.                (12)

Every target normalization is positive if the bounds below hold. Actual source, record, internal and external outputs remain in the norm; only the mathematical comparator is normalized or truncated.

## 7. Twelve allocations and simultaneous existence

Equation(12) has twelve nonnegative allowances. From(7), K/sqrt(u0)=epsilon/10^6 and K/u0<=epsilon^2/10^12. Using sqrt(ell)>=10sqrt(u0) and ell>=100u0, safe ceilings are:

| Allowance | Ceiling |
|---|---|
| E_early | K/u0 |
| 2R0 | 2K/u0 |
| 2L0 | 2K/sqrt(u0) |
| 4sqrt(P) | 4sqrt(3)epsilon/1024 |
| 2d_right | 8K/sqrt(u0) |
| e_leads | 4K/sqrt(ell) |
| e_internal | 3K/ell |
| E_boundary | 2K/u0 |
| 2d_L | 6K/sqrt(ell) |
| 2deltaS | epsilon/256 |
| 2m_L | 56K/ell |
| 4tau_F | 28K/sqrt(ell) |

Each is strictly below epsilon/32 (the spectral term is below epsilon/128). The first uses2+sqrt(2)/eta<4K and(2). The m_L bound uses J0bar+J1bar<=K. Hence the total is below3epsilon/8<epsilon. Before any normalization is invoked, these same ceilings prove delta_launch<1 and D_L<1/2, and2tau_F<1. The positive normalized finite target is consequently defined throughout[t_minus,t_plus]. The relative window width is1/6. There is no Hamiltonian switch at t0_time or either window endpoint.

This is the complete conditional theorem:

    sup_(t_minus<=t<=t_plus)
    ||exp(-itH_phys)E_seed
      -exp(-ic_total t)J_F(beta_F(t) tensor C_p tensor|1>_R)||
       <3epsilon/8<epsilon.                    (13)

It is an operator norm on the encoded input and extends to every passive reference. The unhalved channel bound is at most twice the displayed isometry bound. The scalar-source, incoming, scattering, internal, boundary and truncation terms have all been paid; no all-time flag implication follows.

## 8. Load and sufficient asymptotic scale

The source's emitter and adjacent loads are3j and5j; the F cap site's load is3j. All other loads remain those of c91300a5, including sharedR8j and core endpoint6b+6j. With(3), every listed incident norm sum is strictly below Lambda. The exact coefficients include

    D0=Lambda epsilon/(2*10^5),
    b=Lambda epsilon^(3/2)/(2*10^(15/2)),
    j=Lambda epsilon^2/(2*10^10),
    gamma=Lambda epsilon^(7/2)/(2048*10^(25/2)).

These are exact supplied magnitudes and correlations, not tolerance or manufacturing-cost certificates. In particular gamma is the smallest displayed positive scalar by the same direct comparisons with j,j-gamma,b,D0-2b and all fixed positive j multiples.

The time prescription is explicit through K. Its deliberately loose asymptotic orders can also be stated honestly: as epsilon tends to zero at fixed Lambda, the packet feedback, scattering derivative and internal-map constants remain bounded by fixed (enormous) constants, since B=10^31 is fixed, den is bounded away from zero, eta,zeta tend to zero, and all dimensionless core ratios are bounded. Meanwhile g1=Theta(epsilon^-3/2), g2=Theta(epsilon^-11/2), rho^-2=Theta(epsilon^-3). The definition of K contains A_i+A_o>=g2 and all its other terms have order at most epsilon^-11/2. Therefore

    K=Theta(epsilon^-11/2),
    u0,ell,qubit_count,jt_plus=Theta(epsilon^-13),
    t_plus=Theta(Lambda^-1 epsilon^-15),
    gamma=Theta(Lambda epsilon^(7/2)).           (14)

These are sufficient orders for THIS coarse choice, not optimality or practical performance. This architecture includes four distinct external ports and a shared record writer and is not compared as a speed improvement over the different frozen two-port device. The fixed writer inverse and time constants are enormous. No smaller exponent is inferred from a proposed sharper writer inverse or source resonance bound.

## 9. Sources, exposure and open boundaries

The exact stationary source is common_product_stage_record_core/PROPOSAL.md,c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729. Its distinct stationary check61de4ee29dd3838c4fc7c3bd19c49bf0cd4cb4bacf5ad3e8e10ca06c864e27c1 was fully read and hash-verified during this task; that report does not check this finite construction. The packet source is common_product_stage_record_packet/PROPOSAL.md,3477197cdf54d18ab538c517726d64f3dbc556f6ddb7a6d4b2608b458d34eeb9, authored and fully read in the immediately preceding task. Its distinct review17029fa32989bae3869c4ffee81def65201edc0f0b996013ede8996ca8cf1453 was fully read and hash-verified during this task. It supports the exact packet, derivative chain and internal envelopes at their stated conditional scope; it does not check the new finite-seed composition. The launchfb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4 and general derivative378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8 are reused at their previously fully read/checked scopes. All changed cutoff constants are derived explicitly here.

ROOT proposed the finite interface and gave further exploratory suggestions; the latter are not evidence or imported results. This author also authored the stationary composition and packet source, so this is exposed author continuation, not independent checking. A distinct check must reconstruct the reference-vacuum invariant subspace, all actual finite diagonals, the narrow cutoff costs, boundary coefficients, F-origin exclusion, twelve simultaneous allocations, cap/counts and asymptotic orders.

The supplied positive law, coefficient correlations, vacancy preparation, legal program coherence, shared blank record and encoded input remain premises. Output record1 is certified only in the stated final window. Early or returning record1 is not a completion herald; no permanent halt, capture/reset, old literal processor replacement, native Record identification, physical readout supplier or allowed coefficient error is derived.

Only common_product_stage_record_finite_seed/PROPOSAL.md was created. No scientific executable, numerical solver/simulation, parameter sweep, source/W/Git/publication/checkpoint/axiom/editable-prompt/model change or delegation occurred. No retained status or independent acceptance is assigned.
