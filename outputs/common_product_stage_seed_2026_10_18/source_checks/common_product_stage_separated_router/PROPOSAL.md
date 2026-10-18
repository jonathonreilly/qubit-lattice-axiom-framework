# A supplied positive four-port core with distinct input and output rays

New authored bounded derivation requiring a distinct check. ROOT proposed a K2,2 arrangement of four common-product cells, and subsequently supplied the commuting-matching algebra as a diagnostic. Both are design exposure. The exact one-head calculation below supports that candidate with explicit shared-endpoint accounting: its full reciprocal scattering matrix approaches exp(ik)[[0,C_p],[C_p,0]] on the central band, with error at most 13eta^2+5zeta under the stated small-parameter conditions. Inputs and outputs are different physical rays. This is not yet a finite-seed device, record attachment, halt theorem or resource improvement.

## Four literal cells and legal program encoding

Order the four port endpoints as I0,I1,O0,O1. There are two perfect matchings:

    R_straight={(I0,O0),(I1,O1)},
    R_cross={(I0,O1),(I1,O0)}.

Install one exact positive six-qubit cell on each of these four edges, sharing only its endpoint head qubits with the other incident cell. Every edge has its own mediator and THREE distinct program qubits. Use the source coefficients b>0, D1>D0>2b, j=b^2/D0, a=2j. Each local cell is exactly

    Q_b(u,m)+Q_b(m,v)+b(I-n_u)+b(I-n_v)
      +[(D0-2b)P0_c_m+(D1-2b)P1_c_m]n_m
      +a P0_c_u n_u+a P0_c_v n_v.                 (1)

Attach one uniform positive Q_j ray at each of the four endpoints, with radial n=0 at its endpoint. All other interactions are absent by supplied installation. All terms in (1) and the leads are positive on their full qubit supports. Head number and every program occupation are conserved.

One global legal bit p is encoded in twelve physical program bits: when p=0 both cross cells are locally 000 and both straight cells locally 111; when p=1 the assignments reverse. Thus each endpoint sees exactly one enabled cell, and the active matching is R_p=R_cross for p=0 or R_straight for p=1. The inactive matching is S_p, the other matching. The program preparation is a supplied correlated encoding; it is not obtained by identifying different cells' program bits. Coherent superpositions of these two twelve-bit strings are mathematically allowed and preserved. Mixed or inconsistent physical program patterns remain legitimate positive dynamics but have no claimed routing contract.

There are eight core heads (four endpoints and four mediators) and twelve program qubits, hence 20 core qubits. Four six-qubit cell inventories would count the four shared endpoints twice; 24 is not the physical count. No dressed-state input is specified or needed for this exact scattering model.

## Explicit nearest-neighbor geometry

Place I0=(0,0,0), O0=(2,0,0), I1=(2,2,0), O1=(0,2,0). The four mediators lie at the corresponding square-edge midpoints (1,0,0), (2,1,0), (1,2,0), (0,1,0). Each cell is a two-edge collinear microscopic path; no direct endpoint bond of length two is installed.

For both straight cells, put their three program controls at +z from their two endpoints and mediator. For both cross cells, put their three controls at -z. Each cell is therefore a rigidly rotated/reflected copy of the source patch, all twelve controls are distinct, and every program/head contact is nearest neighbor. An endpoint has two separate program neighbors, at z=+1 and z=-1. Incidental program-row adjacencies carry no installed interaction.

Choose rays I0,n=(-n,0,0), O0,n=(2,-n,0), I1,n=(2+n,2,0), O1,n=(0,2+n,0), n>=1. They are mutually disjoint and meet the core only at their endpoints. Each endpoint uses two inward mediator neighbors, two program neighbors and one lead neighbor, within the cubic coordination number. All unused geometric adjacencies remain uninstalled. This gives an explicit ordinary one-/two-qubit positive implementation, rather than supplying a three-qubit record-controlled hopping.

## Common scalar and exact one-head Schur complement

Each cell's compensation expansion contributes the true scalar 2b on its entire head Hilbert space. Summing four cells gives 8bI, including when the one head lies anywhere in a lead. At a shared endpoint the two incident Q_b terms contribute 2b n_v, canceled by its two b(I-n_v) terms. The leftover constant is paid once per compensation, not once per shared site. No head-position- or program-dependent scalar is removed.

After subtracting only 8bI, let L be the four endpoint/ray one-head space and Q the four-dimensional mediator space. The exact legal-sector matrix is

    h_p=[[A,B],[B*,D_p]],
    A=K_lead+2j sum_ports |v,0><v,0|,
    B_e=-b(|u_e,0>+|v_e,0>),
    D_p=diag(D_e), D_e=D0 active, D1 inactive.      (2)

The endpoint potential 2j comes from exactly one enabled local program per endpoint. The inactive cell still has its ordinary Q_b diagonals and its compensation; those cancel as just described. Replacing the two incident cells by one or discarding a compensation would give a different A or scalar.

For E!=D0,D1 eliminate mediator amplitudes by m_e=b(psi_u,0+psi_v,0)/(D_e-E). Each matching satisfies

    sum_edges_in_matching (|u>+|v>)(<u|+<v|)=I+R

on the four-port endpoint space. Consequently the exact boundary equation is

    E psi_0=j[I+V_p(E)]psi_0-j psi_1,
    V_p(E)=2I-alpha(E)(I+R_p)-beta(E)(I+S_p),
    alpha=D0/(D0-E), beta=D0/(D1-E).              (3)

Here R_p,S_p also denote their 4-by-4 permutation matrices. They are commuting real symmetric involutions: in the chosen port order they are [[0,I],[I,0]] and [[0,X],[X,0]]. The ideal active matching has V_ideal=I-R_p. At E=0 the inactive cells leave an explicit -zeta(I+S_p) correction; they are not exactly absent at finite D1.

## Exact four-port scattering and error

Let z=exp(ik), E(k)=2j(1-cos k), 0<k<pi. For incoming column f use the common radial convention

    psi_n=(2pi)^(-1/2)[z^-n I+z^n S_phys,p(k)]f.

Substitution in (3) gives

    S_phys,p(k)=[z^-1 I-I+V_p]^-1[(1-z)I-V_p].    (4)

Both factors are functions of the same self-adjoint V_p. The denominator is invertible in the open band because its imaginary part is -sin(k)I. In a simultaneous eigenchannel R_p=r, S_p=s, r,s in {+1,-1}, its real boundary parameter and scalar amplitude are

    v_(r,s)=2-alpha(1+r)-beta(1+s),
    sigma(v;k)=(1-v-z)/(z^-1-1+v).                (5)

Each of the four joint channels occurs once. For real v the numerator and denominator have equal modulus, so the full four-port matrix is unitary. It is symmetric, hence reciprocal. The ideal v_ideal=1-r gives sigma=z r. Therefore the desired full comparator is exactly

    S_ideal,p(k)=z R_p
       =z [[0,C_p],[C_p,0]], C_0=X, C_1=I.        (6)

This describes incidence on all four rays, not just selected successful input columns. I-ray incidence is transmitted ideally to the O rays with C_p. O-ray incidence has the reciprocal map to I rays. No one-way isolator or directional coupling has been assumed.

For central k in [pi/3,2pi/3], impose eta=b/D0<=1/8 and 0<zeta=D0/D1<1/2. Then E<=3j, D0>=64j, and both mediator denominators are strictly separated from zero. The boundary displacement is

    Delta V=-(alpha-1)(I+R_p)-beta(I+S_p),
    ||Delta V||<=2(alpha-1)+2beta.

For arbitrary real v and w=0 or 2, direct subtraction gives

    |sigma(v;k)-sigma(w;k)|
      =2sin(k)|v-w|/[|z^-1-1+v| |z^-1-1+w|]
      <=2|v-w|.

The last denominator with w has modulus 2sin(k/2) or 2cos(k/2), both at least one on this band; the other denominator is at least sin k. Since the actual and ideal matrices share the joint eigenbasis, no operator-Lipschitz assumption is needed. Thus

    ||S_phys,p(k)-zR_p||
      <=4(alpha-1)+4beta
      <=12eta^2/(1-3eta^2)+4zeta/(1-3eta^2zeta)
      <=13eta^2+5zeta.                            (7)

It holds uniformly in both legal programs and arbitrary passive references, with no elapsed-time factor. The sum, rather than the two-port maximum, is needed because one joint channel receives both enabled and inactive-cell corrections. The phase z is retained exactly. This is a full matrix error, so undesired I-to-I reflection and wrong O output are included.

For completeness the four mediator amplitudes are

    m_e=(2pi)^(-1/2) b/(D_e-E)
                  (e_u+e_v)^T [I+S_phys,p(k)]f.   (8)

The unoriented endpoint-edge incidence matrix of this four-cycle has norm 2: its endpoint product is 2I+R_p+S_p with largest eigenvalue 4. Hence the mediator coefficient map has norm at most

    4b/(D0-E)<=4eta/(1-3eta^2)<5eta.              (9)

The factor (2pi)^(-1/2) in (8) belongs to the incoming normalization convention. These are generalized eigenfunction amplitudes; an order-eta mediator component cannot be discarded when seeking a full-output packet estimate of order eta^2+zeta.

## Packet normalization available at this scope

One may build an exact smooth compact-central-band packet by integrating the lead columns in (4) and mediator columns in (8) against exp(ik ell)g(k)xi, with ||g||_2=1, g in C_c^2, and xi an arbitrary four-port/program/reference input. In particular xi may be supported on the two I rays. This normalization step has the same valid mechanism as the microscopic packet sourcec105, with four lead and four mediator coordinates instead of two and one:

* All coefficients and their derivatives are bounded on the compact band by the displayed denominator margins; there are no band poles.
* Full-integer Fourier synthesis and restriction bound the lead maps, and the finite mediator integral is bounded. Differentiation in time is strong in the one-head Hilbert space. Equations (2)-(4) prove exact Schrödinger evolution, hence constant norm.
* As t tends to minus infinity, the incoming half-line components approach their norm-one full-integer incoming state. The outgoing components vanish on the positive rays by nonstationary phase, and all four mediator components vanish by one integration by parts. Smoothness and the positive band velocity give finite constants for those estimates.

Thus this particular packet family is an isometry without asserting global spectral completeness. The physical packet carries exp(-i8bt). This qualitative normalization reuse is justified by the exact equations and margins above; the explicit two-port Q/R derivative constants in c105 are NOT reused numerically for the four-port matrix. Their replacements, needed for a quantitative finite window, remain to be derived and checked.

## Point spectrum and finite-seed obligations

The full operator has continuous leads and additional localized mediator directions. Bound states cannot be assumed absent. Indeed A in (2) is positive with norm <=4j by its absolute row/column sums (endpoint diagonal 3j and outward hopping -j). The four-dimensional pure-mediator trial subspace has Rayleigh values at least D0>4j. The essential spectrum is [0,4j] under the finite-rank core modification, so the min-max principle already supplies at least four above-band eigenvalues counting multiplicity. No claim that their seed overlap vanishes follows. A lower-energy analysis and exact weights may also matter; this note does not claim a complete spectral decomposition.

A packet-specific finite-seed proof can avoid proving global completeness if it supplies a complete early vector match that pays all omitted spectral components, as in c105. But four input/output rays and four mediators require their own exact interfaces. In particular:

1. Choose actual finite I-ray emitters, O-ray output lengths and cap diagonals. The O rays start vacant; no source on them is implied by the present infinite model. Count every physical head and program bit.
2. Prove early launch matching to the exact four-port packet and quantify all mediator/core and undesired-ray amplitudes, uniformly over the two logical I inputs and coherent programs. Equal source phases do not alone establish this match.
3. Derive explicit first/second derivative bounds for exp(-ik)S_phys,p and first derivative bounds for the four-mediator map. Recompute the four-ray finite contact/cut residual and final normalization/vacancy target.
4. Keep the physical scalar 8b and any added source/cap scalars in a common full-output comparison. Do not reuse the old two-port 2b phase or its whole-time cell replacement estimate.
5. Prove a simultaneous finite-time/load construction before asserting resources, a uniform observation window or any benefit over the previous device.

Separate O rays make placement of a record writer after the routing core meaningful: intended I-to-O transmission need not traverse that writer on the incoming launch. This removes the unchanged-two-lead double-crossing premise of the earlier X-cut diagnostic. It does not prove the combined record device. The known ordinary two-body record writer has reflection, phase and internal recovery obligations, and adding it changes the global spectrum and source matching. No record interaction is installed here.

## Full positive block counts and local loads

Under the source's seven-block convention, four cells supply 28 positive blocks. Duplicate endpoint compensation terms may be listed separately; combining them does not remove their incident norm load. With N additional head sites on each ray, the finite inventory would have 20+4N qubits and 28+4N blocks before any emitter modification or record writer. These are core-plus-uniform-ray counts, not a finite-seed performance theorem.

Each endpoint is incident to two full cells and one lead bond. The safe full-space local norm sum is

    2(3b+a)+2j=6b+6j,

not the single-cell load and not a legal-sector shortcut that counts only the enabled programmed projector. Each mediator has load D1+2b; each endpoint program qubit has load a=2j; each mediator program qubit has load D1-2b. Lead interiors have load 4j and a simple finite outer end 2j. These sums use the combined mediator-projector convention; splitting that block requires corresponding recounting. All coefficients and program correlations remain supplied.

A safe scale existence check, without a time claim, is D1=Lambda/2, D0=zeta D1, b=eta D0 with eta<=1/8,zeta<1/2. Then mediator load is Lambda(1/2+eta zeta)<Lambda, and endpoint load is 3Lambda zeta(eta+eta^2)<Lambda. The other listed loads are smaller. This shows the added incident cells do not silently violate that cap domain; it does not establish source/record loads or efficiency.

## Exact sources and exposure limits

The full positive cell and coefficients are from `mediated_common_product_program/PROPOSAL.md`, SHA256 `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`. The previous finite two-port composition is `common_product_finite_seed_router/PROPOSAL.md`, SHA256 `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`. Its finite-seed theorem is NOT transferred by analogy. The exact packet-normalization mechanism is from `common_product_microscopic_packet/PROPOSAL.md`, SHA256 `c105226ebeead1f87bb11c6afcc8dadac59520401d5f8c0fa6dba4ba3ef90e4e`; the matrix-dimensional extension was reconstructed above and needs its own check. These sources were previously fully read in this coherent work.

ROOT proposed the K2,2 architecture and matching Schur formula. I authored the earlier scattering/packet sources and assessed the unchanged-tree record problem; this is exposed author continuation, not an independent review. The new load-bearing steps are the shared-endpoint scalar/potential accounting, twelve-bit legal encoding, literal four-cell layout, complete four-port scattering, error bound and packet-normalization extension. A distinct check is required before integration.

Only this proposal was created. No W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, sweep, publication or delegation occurred. No native block supplier, old-processor transfer, finite record output, irreversible latch, capture/reset or permanent halt is asserted.
