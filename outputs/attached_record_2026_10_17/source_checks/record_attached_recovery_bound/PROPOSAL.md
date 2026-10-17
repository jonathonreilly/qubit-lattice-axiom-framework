# Attached record: finite recovery difference and local gate bound

Status: authored conditional real-band derivation, requiring a distinct check. The finite upstream recovery difference DOES inherit a constant closed-return allowance plus linear open detuning. The new gate recovery is bounded but need not share that cancellation. A deliberately loose sufficient envelope on each selected band is

    ||Delta L_up|| < 3e-24 + 2e19 u,
    ||L_up,x|| < 4e16,
    ||L_gate+closedtail,x|| < 11000,
    ||Delta L_gate+closedtail|| < 22000,
    u=|q-pi/2|<=4e-6, x=+,-.                       (1)

These are endpoint-FORCING background Green columns, before multiplication by the emitter coupling or resonant inverse. Their domain is the full eight-dimensional internal endpoint fiber in one parity, not a single selected seed column. The large upstream slope is not a useful small-error certificate. Exact formulas below expose where a sharper source recovery estimate would improve it. No runtime, actual seed mass, spectral synthesis or herald theorem follows from (1).

## Dependencies and exposure

Read the complete frozen attachment `../record_attached_kernel/PROPOSAL.md`, SHA256 `fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457`; my separate check is `../record_attached_kernel_check/REVIEW.md`, SHA256 `7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005`. I authored the check, not that attachment. Read complete root-authored `../record_gate_center_inverse/PROPOSAL.md`, SHA256 `3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82`, and its distinct check `../record_gate_center_inverse_check/REVIEW.md`, SHA256 `cebb4153f1f1f75001614110ad7597fcf5b835ddad2ab15e0d57c1e089f0f67f`. Its local full-fiber recovery ceiling is <26.

The new endpoint source `../record_attached_emitter_bound/PROPOSAL.md`, SHA256 `2b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9`, is used PROVISIONALLY: its distinct check was pending when supplied by root. Only its background same-plane equations and bounds through section 4 are needed, not its emitter or mass conclusions. I read it completely. The source is not my work. Root supplied its availability after I identified the need for terminated-input background bounds.

Also refreshed complete `../bandcenter_converter_composition/PROPOSAL.md` at `1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78`, `../bandcenter_converter_endpoint/PROPOSAL.md` at `22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a`, and wider-domain source `../bandcenter_bandwidth_extension/PROPOSAL.md` at `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`. Unchanged original calibration and finite-block premises remain conditional. I authored the earlier resource check and the abstract operator interface `../record_core_operator_difference/PROPOSAL.md`; this is an exposed actual-device derivation, not independent validation of either my interface or these new bounds.

No numerical/scientific execution, sweep, solver, delegation, Git/W/publication/model/prompt/checkpoint change occurred. Source reads, hashes and this sole proposal only. Applicable unchanged workflow and instructions are reused.

## 1. Common partition and exact recovery identities

Remove the emitter, retaining its input endpoint diagonal 2j. Let V include the entire eight-coordinate input endpoint. Keep all operators relative to the common scalar c_att, with B containing literal K. Work at lambda=b_selected+E(q) on the inherited wider real band; the fixed B projections give one open P and seven closed C. Both record sectors use the SAME lambda. Let U comprise all upstream finite head sites except the cable: 90 arms, 82 old-port sites and 21 new-input sites, totaling 193. The eighteen sites v0,...,v17 will be added explicitly. Source qubits are internal fiber coordinates, not additional head sites or independently duplicated sources.

Let R0 be the emitter-free, input-terminated original background resolvent with its output still free. At output plane v0, write its endpoint-forcing outgoing coefficient B_e, generalized scattering S, and finite recovery from prescribed incoming amplitude K_U. For unit endpoint forcing f,

    b_x=S a_x+B_e f,       a_x=R_x b_x,
    L_U,x f=L_U,0 f+K_U a_x,
    R_x=Q^18 r_gate,x Q^18.                         (2)

All products retain their order. Thus

    Delta L_U=K_U (R_+ b_+-R_- b_-),                (3)

where b_x denotes the operator from f to outgoing coefficients. No commuting of B through the source is used. This is the decisive cancellation: the old finite graph is identical in both sectors, so only its incoming return differs. It does not say that amplitudes inside the gate cancel.

For clarity an exact finite-matrix specification of K_U is available from the two-free-port background G2. With input deletion site d=ell+1=21, Z=G2(d,d), and output origin o0=v0,

    G_D(U,o0)=G2(U,o0)-G2(U,d) Z^-1 G2(d,o0),
    K_U=G_D(U,o0) A^-1,
    L_U,0=G2(U,ell)-G2(U,d) Z^-1 G2(d,ell).         (4)

Here A=[j(Q-Q^-1)]^-1; the multiplication by A^-1 is on the RIGHT. These matrices retain every finite upstream coordinate. They are a reproducible alternative to the loose envelopes below, and do not involve the emitter resonance.

## 2. Source recovery norms and finite-site aggregation

Inherited wider-band constants are ||A||<200, ||A^-1||<21, ||T||<600, ||Z^-1||<24, ||A+X||<201 and ||A^-1 P||=E'(q)<.006. These are full internal bounds, apart from the explicitly selected last one.

The original finite-coordinate recovery bound <2e10 extends here to arbitrary incoming NEW-port vectors, not merely their open restriction. To see why, use the actual full converter matching from the composition source: its diagonal incoming coefficient U_conv has norm <.49, its outgoing coefficient V_conv has norm <2.5, and the old-buffer return inverse has norm <1.000005 on the wider band. Multiplication by Q_old^40 is a contraction. Thus the total prescribed old incoming coefficients have norm <1. The unchanged recovery G_old(core,ports) A_old^-1 then gives <2e10 by the original finite-site/port aggregation. Closed incoming components are included; no flux unitarity is asserted for them.

Old buffers also have a uniform finite norm. Their incoming closed coefficients have the form Q_old^40 c with ||c||<1, obtained by moving Q_old^40 through the converter feedback identity; the middle inverse retains a margin because its open return is <4.88e-6 and its closed sides carry Q_old^40. Therefore Q_old^-m Q_old^40 c is bounded for 0<=m<=40. Outgoing coefficients are bounded by the full old generalized matrix norm times the bounded incident coefficients, <2. Each buffer site is consequently bounded by 3 for unit incident vector; summing 82 sites costs less than 30. Use the convenient combined bound

    ||Phi_oldfinite+buffers|| < 3e10.               (5)

Phi is recovery from incoming new-port coefficients. This explicitly accounts for every old finite head site; it is not a per-site ceiling silently used as a whole-vector ceiling.

For a forcing at a new port or farther along its free ray, the incoming coefficient is A Q^m. Equation (5) yields ||G2(oldfinite+buffers,port_m)||<6e12. Also ||G2(d,o0)||<=600. Hence (4) gives

    ||G_D(oldfinite+buffers,o0)||
       <6e12(1+24*600)=8.6406e16.

Multiplication by A^-1 costs <21 for all columns, but only <.006 for the selected column. The 21 new-input vertices can be bounded directly with the free-port kernel: each block before deletion has norm <=800, and after deletion <800+800*24*800<1.6e7. Orthogonal summation costs sqrt(21)<5. Their addition leaves the simple ceilings

    ||K_U||<2e18,             ||K_U P||<6e14.        (6)

Similarly G2(d,ell)=Q(A+X), of norm <201. Applying (4) to endpoint forcing, and again adding all 21 input sites, gives

    ||L_U,0||<3.1e16.                               (7)

These deliberately waste substantial source conditioning. They are not estimates of a whole infinite real-axis resolvent, and their size must not be hidden when using them downstream.

## 3. Return coefficients and upstream difference

The provisional endpoint derivation supplies, at the SAME v0 plane,

    ||S||<2e8, |S_PP|=1, ||B_e||<3e6,
    ||P B_e||<400, ||C R_x C||<e_C=1e-63,
    |P R_x P|<=rho=33u.

Its ordered closed elimination gives ||N_x||<2 for N_x=(I-S_CC C R_x C)^-1, effective open forcing <400+2e-48 and open return denominator >.99986. It follows directly that

    ||P b_x||<401,
    ||C b_x||<2(2e8*rho*401+3e6)<3e7,
    ||P a_x||<=401rho,        ||C a_x||<3e7 e_C.    (8)

No full generalized-source norm is substituted for its selected reflection modulus. Combining (3), (6), (8) and sector triangle inequalities yields

    ||Delta L_U||
       <(6e14)*802rho+(2e18)*6e7 e_C
       <1.6e19 u+2e-37.                            (9)

Equations (7) and (8) also give ||L_U,x||<3.2e16. All bounds hold on the full endpoint forcing space, although P on the LEFT selects the outgoing channel. There is no maximum-over-eight-input-columns shortcut.

## 4. Cable and its growing closed coefficient

At a retained cable site n=0,...,17 the exact field is

    psi_x(n)=Q^n b_x+Q^-n a_x.                     (10)

Use this formula before taking norms. Bounding Q^-17 alone would destroy the closed-return estimate. Since b_+-b_-=S(a_+-a_-), its outgoing difference, aggregated over all 18 sites, is less than

    5*(2e8)*(802rho+6e7 e_C).

The incoming open difference contributes at most 5*802rho. For each closed root a=|s|<1/60 the checked gate reflection satisfies

    a^(36-n)|r_gate,x|
       <=[a^(36-n)+a^(35-n)/56]/(1-a/56)
       <3*60^(-(36-n)) <=3*60^-19.                (11)

Thus the incoming closed difference aggregated over the cable is <9e8*60^-19<1e-24. The bound follows already from 60^6>4e10. The resulting cable sector difference is <3e13u+2e-24. Adding this to (9) proves the first bound in (1); orthogonal square-sum aggregation would only improve the chosen sum bound.

For absolute cable recovery, (8), (10), (11) give open amplitude <402 per site. The outgoing closed amplitude is bounded by 3e7 at n=0 and must not be called negligible there. Aggregating eighteen sites by sqrt(18)<5 gives the safe total cable ceiling <1.6e8, including incoming terms. Adding this to the preceding <3.2e16 bound still establishes the second bound in (1). These counts exclude the emitter itself, whose full internal block is already separately retained by the operator-interface formula. Root identified this narrow correction after the first draft; PROPOSAL_v1.md preserves that draft at SHA25646785c5a9a9dbdec43d8457dd7c2361eb834431918d4bbdc81fcd4b5fca2ea98. The sector-difference estimate and the gate-boundary estimate at n=17 are unchanged.

## 5. New gate and downstream closed tails

At the last cable site a=v17, (8), (10), (11) imply

    ||psi_x(a)||<402.

For example its open part is <=401(1+rho); its closed part is bounded by 3e7*60^-17+9e7*60^-19. The exact one-output gate recovery is

    psi_gate,x=-j sum_l [D_x^R(lambda-b_l)]^-1
                            e_p P_l psi_x(a).       (12)

The independently checked local open inverse and the checked closed gap give norm <26 for this map into ALL 24 gate sites. The projections P_l are orthogonal, so the full internal direct sum has the maximum block norm, not a sum of eight norms. This gives gate norm <26*402.

For each closed channel the output tail beyond o has amplitudes s_l^r psi_gate,l(o), r>=1. Its squared norm is a_l^2/(1-a_l^2) times the squared port amplitude, bounded by 1/3599 times it. Aggregating all closed fibers and the orthogonal gate coordinates gives combined recovery factor <26*sqrt(1+1/3599)<27. Therefore each-sector gate-plus-closed-tail column is <27*402<11000, and its sector difference is <22000. The propagating downstream ray is NOT included: its stationary column is not square-summable and needs actual spectral synthesis and a target-profile comparison.

No detuning factor is asserted for (12). Even at exact band center the two record sectors may have different amplitudes inside the gate. The small upstream return does not imply small local recovery difference. This is the actual-device version of the uncancelled Delta L term in the abstract operator interface.

## 6. Both spectral lips, arbitrary inputs and use in the interface

All installed hoppings, B, contacts, record-X eigenvectors and coordinate inclusions are real in fixed conjugations. The retarded and advanced recovery columns are consequently related by those conjugations. The same bounds hold on both lips, including sector differences and the energy-dependent closed projection. This is real-structure conjugation of a rectangular column, NOT taking its entrywise imaginary part as a spectral density. The actual density still uses the difference of lower and upper resolvent columns with normalization 1/(2pi i).

For fixed finite-core Q containing upstream sites plus the gate, one sufficient insertion into the operator interface is

    l_D <= sqrt((3e-24+2e19u)^2+22000^2),
    l_+ <5e16.                                     (13)

The same estimates hold when the closed downstream tail is charged separately as above; for that extension the chosen closed projection depends on the energy window and must be kept explicit in spectral synthesis. The actual finite-core Q itself can remain fixed. All old inputs and passive references are allowed. K is retained in the actual shared source and no factor exp(-itK) has been commuted through the resolvent. On a union of distinct old-energy windows these bounds apply to the full fiber on each window; an integrated arbitrary-input conclusion must still follow the operator-valued spectral interface rather than identifying overlapping errors by their largest scalar column.

The direct background term in that interface remains -kappa Delta L T_-; it has only one resonant inverse. Equations (1), (13) do not remove it. They supply finite real-band envelopes, but the conservative upstream constants are too large to imply a competitive small local error without additional sharper recovery work. The useful exact refinement target is K_U P in (4), together with its action on the actual sector return difference, not another scalar endpoint self-energy estimate.

Pending checks include this derivation and its provisional endpoint-background dependency. Actual spectral regularity/jump synthesis, omitted seed spectral amplitudes, emitter bounds, downstream common packet and complete temporal or herald comparison remain separate. No parameter, new observation window or finite output size is selected.
