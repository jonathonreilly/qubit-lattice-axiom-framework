# Real positive two-body form of the twelve-square construction

New source-exposed author derivation, requiring distinct review. A fixed ancilla-only onsite gauge makes EVERY listed block of the actual b54 joint gadget and c1cb scaled attachment entrywise real in the physical computational basis. Its supplied ancillas become a specified product of six cat+ and six cat- states, all real. The algebra is an exact unitary conjugacy, not a perturbative approximation or a timed gate. All norms, supports, coefficients, scalars and existing error inequalities are preserved with the correspondingly changed ancillary input/output. This removes complex Hamiltonian entries from this supplied finite-range construction; it does not derive the resulting blocks or cat states from the former primitive inventory.

## 1. Precise onsite transformation

Use the data order and twelve labels l=(e,H,A) of b54: e=0,1, H in{X,Y}, A in{X,Y,Z}, with

    O_l=(H_i_e,H_j_e,A_Q,A_P), Omega_l=product_r O_l,r.

All four data supports in each square are distinct. Define the fixed phase matrix

    S=diag(1,i)=exp(i pi/4)Rz(pi/2),
    Rz(pi/2)=exp(-i pi Z/4).

Direct multiplication gives S X S*=Y and S Z S*=Z. Put S on ancilla b_l,r precisely when O_l,r=Y, and identity on that ancilla otherwise. Let U be the product of these onsite matrices on all48 ancillas, identity on every data, original-head, program, record and reference factor. Its phases are fixed by the gadget pattern, not by the logical input or time.

Conjugation transforms each elementary positive coupler as follows:

    O=X: nu(I+X_data X_anc), unchanged;
    O=Z: nu(I+Z_data X_anc), unchanged;
    O=Y: nu(I+Y_data Y_anc).

These are real symmetric matrices. In particular, in ordering00,01,10,11,

    Y tensor Y = [[0,0,0,-1],[0,0,1,0],
                  [0,1,0,0],[-1,0,0,0]].

The imaginary entries of individual Y factors cancel in their tensor product; replacing Y by a real matrix separately would be incorrect. Each product remains a Hermitian involution, so every displayed I+product block is positive with norm2nu on its full support. The Ising penalties Delta(I-ZZ)/2 are unchanged, positive and real. No new compensation or scalar is introduced: U I U*=I.

Writing V_real for the resulting48 couplers without their identity parts,

    H_gad,real=48nu I+H0+V_real=U H_gad U*              (1)

on the ENTIRE data/ancilla Hilbert space, not merely a one-head or low-energy sector. The onsite gauge is a mathematical specification of the new installed Hamiltonian and supplied state; no physical S gate, timed basis change or conjugating pulse is required by the construction.

## 2. All twelve ancillary states and exact phases

For a square with m occurrences of data Y, applying S on those m ancillas gives

    U_l cat+ = (|0000>+i^m |1111>)/sqrt(2).

The actual paired structure makes m=2*1_(H=Y)+2*1_(A=Y), always even. Thus define sigma_l=(-1)^(m/2); the new supplied state is exactly cat_sigma_l=(|0000>+sigma_l|1111>)/sqrt(2). For BOTH e=0 and e=1 the complete list is:

| H | A | Rotated ancillas | m | Supplied cat sign |
| --- | --- | --- | --- | --- |
| X | X | none | 0 | + |
| X | Y | 3,4 | 2 | - |
| X | Z | none | 0 | + |
| Y | X | 1,2 | 2 | - |
| Y | Y | 1,2,3,4 | 4 | + |
| Y | Z | 1,2 | 2 | - |

There are ten rotated ancillas per entrance, twenty in total, and three minus cats per entrance, six in total. This is a real normalized supplied product across the twelve squares, but each individual square state remains entangled. It is not a product of blank single qubits or a proved low-energy preparation procedure.

For the standard Rz convention rather than S, the exact square identity is

    U_l^Rz cat+ = exp(-i m pi/4)cat_sigma_l.

The square phases in table order are1,-i,1,-i,-1,-i. Their product is -i for each entrance and -1 for all twelve squares. This is one common input-independent global phase, not a phase on program/path branches. With the S convention above there is no such injection phase at all. Equivalently the standard-Rz and S global signs cancel between both sides of every literal-state evolution comparison. Neither convention changes the time phase48nu+s_joint or the physical output phase in c1cb.

Let J append the original twelve cat+ states and J_real append exactly the table's real states. With the S choice,

    J_real=U J.                                         (2)

The corresponding reference-extended injections preserve arbitrary coherent input without changing its basis or phase.

## 3. Correct conserved sectors and low-space correspondence

The transformed conserved operator for square l is

    T_l=U X_all,l U*=
        product_(unrotated r) X_l,r product_(rotated r) Y_l,r.

It commutes with H0 and every transformed coupler; other squares and the original background also commute with it. Its +1 sector is the image of the original X_all,l=+1 sector. On span{|0000>,|1111>}, even m gives T_l=sigma_l X_all,l, so cat_sigma_l has eigenvalue+1 of T_l. This is the sector that must be supplied. It would be wrong to keep cat+ for every square after rotating only the Hamiltonian: for the six minus rows that occupies the opposite transformed sector and does not inherit the intended coupling sign.

Within the common T_l=+1 sector the penalty zero subspace is precisely the image of the old low space, with the same2Delta complementary gap and arbitrary data/reference multiplicity. Outside it the other cat-sign penalty ground states still exist. Since each T_l contains an even number of Y factors it is itself entrywise real; no complex initial-sector selection is hidden.

The parity operator formed from all48 ancillary Z factors commutes with U and still sends V_real to -V_real, fixes J_real pointwise and preserves all twelve transformed sectors. Thus the even analytic perturbation structure is unchanged. More strongly, every Riesz projection, normalized low-space isometry and scalar/Pauli coefficient is exactly conjugated by U. In the original data coordinates,

    E_lead=s_joint I-g sum_l Omega_l,
    s_joint=-24nu^2/Delta+27nu^4/Delta^3,
    g=5nu^4/(2Delta^3)

is unchanged, including the mixed-path scalar27. The data O_l,r were not rotated. The four-ancilla product that mediates Omega_l is now T_l, with the same+1 value on the supplied sector; a spurious extra sigma_l in g would double-count the transformation.

For example the exact isolated bound transfers directly to

    ||exp(-itH_gad,real)J_real
        -exp[-it(48nu+s_joint)]J_real exp(+it g sum_l Omega_l)||
        <=min{2,440alpha+|t|R6},
    R6=Delta(384alpha)^6/[1-(384alpha)^2], alpha<=1/768. (3)

This follows by multiplying the entire old error operator on the left by U, not by repeating or adjusting the perturbation approximation. Actual outputs retain all ancillas; their exact state is not asserted to remain cat_sigma.

## 4. Reality of the actual inherited background

Reality of the rest of the device is a separate premise check, not a consequence of (1). The actual Bbar in c1cb is ancilla-free and consists of the following blocks:

- Ordinary core/lead/cable/source exchanges have real occupation diagonals and real hopping a_x^*a_y+a_y^*a_x. Here a=|0><1| is real in the specified basis. The combined source compensations, caps, vacancies and fixed occupations are real diagonal.
- The single-program mediator blocks are real diagonal combinations of P0 n_m and P1 n_m with real positive coefficients. There is no program-only complex potential.
- The two writer inventories use eighteen ordinary real arm bonds, two real-strength sqrt(2) phase-cell bonds, four SIGNED REAL Hadamard-junction bonds, real diagonal phase repairs/vacancies, and two terminal contacts j n_T(I+X_R) per writer. A positive or negative real hopping remains a real symmetric block. The phase cells generate complex scattering phases dynamically; they are not complex hopping coefficients.
- The remaining direct entrance terms are Q_(jbar/2)(i,j) and (jbar/2)n_i,(jbar/2)n_j, all real. The removed SWAP-conditioned bonds are not part of Bbar; even their target SWAP matrices are real, but no such four-body block is being reintroduced here.
- The one bias kappabar n_R and uniform original-head mubar N are real diagonal. Scaling all these blocks by the same positive scale preserves reality and positivity.

These facts were checked against the complete displayed single-control source76b5, the complete original writer93445 positive inventory and the complete residual-background definition in c1cb. The exact biased packet uses complex Fourier/scattering amplitudes, but these are not installed Hamiltonian entries. No imaginary Peierls phase or one-Y physical term occurs elsewhere in this pinned nominal background. This statement does not cover unlisted arbitrary complex perturbations or a different primitive inventory.

Consequently, with B=scale Bbar,

    Hact,real=B+H_gad,real=U(B+H_gad)U*                 (4)

is a sum of entrywise real, positive, at-most-two-qubit blocks on the full physical space. Since B has no new-ancilla support, [U,B]=0 exactly, without a commutation assumption about B and the DATA operators O_l,r. In particular this works even for X/Y program couplers that fail to commute with background detunings.

## 5. Attached dynamics, resources and complete-output contract

Equation(4) is exact for every real time and every physical input. Therefore any established c1cb rectangular simulation bound transfers with J replaced by J_real and no additional error. Its reference comparison generator

    scale Hbar_new+(48nu+s_joint)I

acts on the original system and is unchanged. The commutator coefficient sum_r||[B,O_r]|| is unchanged. The actual alpha,scale,local cap and time prescription are not modified by the gauge. This algebraic transfer does not independently validate c1cb's finite-operational composition; its theorem and review status remain separate dependencies.

In a complete nominal final target, replace the old twelve-cat+ tensor by the table's cat tensor and keep EVERYTHING else: program relocation from Q to P, old sigma_PE relocated to Q/E, retained logical/reference coherence, finite q-dependent radial profile, original head vacancies and record1. The phase is exactly

    exp{-it[48nu+s_joint+scale*cbar+scale*mubar]}.

The same replacement applies to the ONE unnormalized branch target over the whole certified horizon. Record/F/original-head projectors commute with U, and the cat target projector is conjugated to the real cat projector. Thus nominal joint-event and full-channel bounds, whenever established for c1cb, have identical values. Arbitrary retained environments are tensored by identity; actual joint preparation errors are paid by the same trace-distance contraction. Separate correct ancillary marginals still do not establish the joint preparation contract.

The new required preparation comparator is explicitly

    |vac_other_heads,0_R><...|
       tensor product_l |cat_sigma_l><cat_sigma_l| tensor sigma_PE,

with the same independence from the supplied boundary program/path input as c1cb. No physical conversion of a supplied cat+ source to cat- is assumed free: either the displayed real states are supplied with the required joint error, or a separately accounted preparation construction is needed. The onsite gauge proof is not that construction.

All supports, positions and block norms are unchanged under onsite conjugacy. Thus the twelve-gadget inventory is48 ancillas and96 blocks, with ancillary load2Delta+2nu, entrance-head additions12nu and P/Q additions24nu. Coupler Manhattan range remains at most35; square penalties remain nearest-neighbor, and the long data couplers remain finite-range. In c1cb's full inventory the counts remain175+4ell qubits and389+8ell positive blocks including the original-head penalties, or265+4ell blocks without them. Ancillas receive no original-head chemical potential. All other cap contributions and coefficient magnitudes are exactly those of that source; no pulse/gauge gates are added to the physical inventory.

Reality does not restore conservation of original head number: the actual XX,ZX and YY couplers can create virtual occupation changes. It does not justify transferring the older ground/Gibbs preparation theorems, even though the transformed Hamiltonian is positive and real. Full-space spectrum and dynamics are unitarily equivalent to the complex description, with precisely its existing extra sectors and preparation limitations.

## 6. Exact status, sources and limits

The new result is the exact real-block conjugacy, all-twelve state/phase table, transformed-sector statement, actual-background reality check and conditional preservation of existing error/resource contracts. It removes the need to permit complex Hermitian entries for this specific supplied construction. It does NOT remove arbitrary positive Pauli-product block supply, finite interaction range35, entangled ancillary supply, specified boundary input, joint environment contract, coefficient calibration or observation/readout assumptions. There is no native realization, nearest-neighbor routing, autonomous cat initializer, ordinary-to-dual-rail input converter, old literal processor transfer, capture/reset or permanent halt theorem here.

Exact identities, with full changed/necessary reads and refreshed hashes:

- N/common_product_full_swap_gadget/PROPOSAL.md:b54c6f29ea780efdcad7f33def048a0b5f9436fe8125ce3c2b2b416cabde4436; my preceding complete distinct review6dfaeacb3a3b1b2f2dfdcdf4c2f862b41687dac7a9dc08b35adae1865e4e90e3 is reused at its isolated-joint scope. This gauge is new author work, not part of that check.
- N/common_product_two_body_scaled_operation/PROPOSAL.md:c1cbdb0eb1b7cc4b865c3ad8b8323b646eeff47e195c3239e297f007f0884bb7, completely read here. Its analytic/runtime assertions are adopted only conditionally; this source supplies no independent check of them. Its Bbar definition and physical inventory were inspected for the specific ancilla-free and reality claims above.
- N/common_product_single_control_router/PROPOSAL.md:76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01, completely reread/hash refreshed here.
- W/outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md:93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56, completely reread/hash refreshed here for the actual real signed mixer, phase-cell and terminal-contact blocks. Its historical provisional prose does not supersede the later scoped writer checks; no new scattering estimate is extracted here.
- N/common_product_loader_component_background/PROPOSAL.md:e7d3efb291b47ce6d6265b293ea448de917380ae5a36322664bee857ca7312aa, completely read here while locating the newer attached source; only its ancilla-free background distinction is relevant. N/common_product_autonomous_loader_interface/PROPOSAL.md:c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e and its review7a98 retain their immediately preceding complete reads, for the exact program-relocation/retained-output interpretation.

Here N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934 and W=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree.

ROOT supplied the onsite-Rz candidate and even-Y observation. I reconstructed the signs, all twelve patterns, the global phase, transformed conserved sectors, full-space conjugacy and actual background inventory after that exposure. This is same-model author continuation requiring a distinct check, not an independent confirmation of ROOT's proposal. A reviewer should especially test the Rz convention, cat-minus sectors, background realness on all occupations, physical scalar and joint output/preparation contract.

Only this proposal was created. No scientific executable, numerical sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, delegation or publication occurred. All frozen sources remain unchanged.
