# A four-external-port router with two writers and one shared record

New bounded author composition requiring a distinct check. The supplied positive four-port core can be attached through equal 34-edge cables to two disjoint ordinary two-body writers sharing one physical record qubit. The complete stationary scattering matrix, including incidence from the final rays and both record-X sectors, is close to a common-phase reciprocal routing-and-X comparator. This is not a finite-seed device theorem or an all-time completion herald.

ROOT suggested two copies of the checked writer sharing four distinct neighbors of one record. The actual embedding, cable phases, full-fiber feedback equations and bound below are newly reconstructed after that exposure. No prior component check is represented as independent validation of this composition.

## 1. Actual blocks and shared fiber

Use the four-cell core60bc91b6 exactly: four endpoint heads I0,I1,O0,O1, four mediator heads, and twelve distinct program controls. Legal bit p enables the cross matching when p=0 and straight matching when p=1. Each cell is the supplied positive six-qubit cell with j=b^2/D0, a=2j, D1>D0>2b. The complete legal-sector core scattering matrix S_c(k), in I/O ordering, has

    ||S_c(k)-z [[0,C_p],[C_p,0]]||<=e,
    z=exp(ik), C_0=X_path, C_1=I_path,
    e=13eta^2+5zeta, eta=b/D0<=1/8,
    0<zeta=D0/D1<1/2, pi/3<=k<=2pi/3.           (1)

The core acts as identity on the new record. Its true physical scalar is8b, not the former two-port2b. Program encoding is supplied and preserved; arbitrary coherent legal programs and passive references are retained.

Use two geometrically congruent copies of the full 24-head writer93445d7d, with its positive phase-cell repair and four-vertex real Hadamard junction. They share only ONE record qubit R, with no record free Hamiltonian. Each terminal contact is j n_T(I+X_R), a positive two-body block of norm2j on its full support. All four contacts use this same X_R. Record excitation number need not be conserved, but X_R and total head number are conserved. There is no tensor product of two separate physical record qubits and no three-body controlled hopping.

For clarity, a signed hopping h is supplied by the positive block |h|(n_x+n_y)+h(a_x^dagger a_y+a_y^dagger a_x), of norm2|h|. Ordinary h=-j and phase h=-sqrt(2)j blocks, positive phase onsite terms, signed junction blocks and positive vacancies are exactly those checked for the writer. Positivity survives overlap at R; no commutativity of all blocks is required.

In each conserved X_R sector x=+/-1, the two writers are identical scalar head networks on disjoint head vertices. Hence their combined writer scattering matrix is the direct sum in path of the SAME two-port/record matrix, not a product of independent record transformations. With writer port order U (input toward core), F (final), the checked bound is

    ||S_w(k)-h(k) [[0,X_R],[X_R,0]]||<=w,
    h(k)=-i z^22, w=33|k-pi/2|,
    |k-pi/2|<=10^-3.                            (2)

For the two paths jointly, every entry in(2) is tensored with I_path. The stronger exact terminal identity r_terminal=-z X_R is available from its check, but no improved writer constant is inferred here. An initially supplied |0>_R is sent ideally to|1>_R; general input undergoes X_R, not erasure.

## 2. Collision-free cubic geometry with one R

Take R=(0,0,0). Writer A is exactly the source layout. Its first arm is

    (1,0,0),(2,0,0),(2,1,0),(1,1,0),
    (1,2,0),...,(1,8,0),

and its second arm is

    (-1,0,0),(-1,1,0),...,(-1,8,0),
    (-1,8,1),(0,8,1).

Its port heads are U_A=(0,8,0), F_A=(1,8,1). Phase cells on the second arm replace the y=2--3 and y=5--6 bonds. The signed four-edge junction connects the two attachment heads and these two ports in the checked ordering.

Writer B is the image of the finite 24-head A gadget, all its internal hoppings and onsite terms under the cubic isometry

    T(x,y,z)=(z,-y,x).

The record remains at the origin. B uses terminals(0,0,1),(0,0,-1), U_B=(0,-8,0), F_B=(1,-8,1). Its phase cells and junction signs are transported without relabeling their local arm/port ordering. Writer A uses terminals(1,0,0),(-1,0,0). Thus four distinct neighbors of R carry four terminal contacts; the remaining two cubic neighbors of R are unused.

The A heads have y>=0, B heads y<=0. At y=0 the A heads are(1,0,0),(2,0,0),(-1,0,0), while B heads are(0,0,1),(0,0,2),(0,0,-1), so the two head sets are disjoint even there. Neither contains R.

Translate the entire checked core, including its program controls, by(20,0,0), without rotation. Its endpoints are

    I0=(20,0,0), O0=(22,0,0),
    I1=(22,2,0), O1=(20,2,0).

Replace its two O rays by the following lattice paths; each displayed straight segment includes every intervening integer vertex:

    O0 ->(22,-10,0)->(0,-10,0)->U_B,
    O1 ->(20,12,0)->(0,12,0)->U_A.               (3)

Their lengths are10+22+2=34 and10+20+4=34. They use the original allowed outward directions at both O endpoints. At each U they approach through the original writer input-lead neighbor (y=-9 for B, y=9 for A). They are mutually disjoint and do not meet a core program, mediator, writer arm, record or output head. In particular the horizontal cable portions lie at y=-10 and12 beyond the respective writer arms, while their core-side vertical portions lie at x=22 and20 outside both writers.

Install infinite final rays F_A+(n,0,0) and F_B+(n,0,0), n>=1. The B final lead uses its free +x neighbor rather than the +z direction obtained by transporting A's external ray; its endpoint still receives exactly one ordinary j bond, so the radial operator and phase convention are unchanged. Label final logical path F0=F_B and F1=F_A, matching their upstream O0,O1 cables. These rays lie at z=1,y=+8 or-8 and do not hit either cable, whose z=0 throughout. They do not hit the core or its controls at y=0,1,2.

For the two external input rays, use I0->(19,0,0)->(19,0,1)->(19,0,2)->... and I1->(23,2,0)->(23,2,1)->(23,2,2)->... . Their first edges retain the checked core outward directions; subsequent bends preserve a degree-two uniform j lead. They are disjoint from each other and from all listed devices/cables/final rays. Radial n counts edges even around the bends. Every installed interaction is nearest-neighbor. Incidental unused lattice adjacencies install no coupling; their absence is a supplied condition, as in both components.

## 3. Scalar, counts and loads

The core contributes exactly8b I. Each writer's four junction vacancies contributes c_R=4(sqrt(2)-1)j I. Their junction vertices are distinct; sharing R changes none of these identities. All other writer/cable terms have zero vacuum scalar. Thus the exact common physical scalar is

    c_total=8b+2c_R.                            (4)

This identity holds independently of head position, legal program and record state. Subtract it only for the relative stationary analysis; any eventual physical packet comparator must retain exp(-it c_total).

Before counting external I/F ray vertices, the finite network has20 core qubits,48 writer heads, one shared record, and2(34-1)=66 cable-interior heads:135 qubits total. There are28 core positive blocks,2*34 writer blocks, and68 ordinary cable bonds:164 listed positive blocks. Cable endpoints already belong to the core/writers and are not recounted. The external rays are infinite in this stationary model, so these are finite-network counts, not a finite-device resource theorem.

Core endpoint load remains6b+6j; mediator/program loads remain D1+2b,2j,D1-2b. A core O endpoint receives one cable bond instead of one ray bond. Writer terminal load is4j, ordinary arm/cable/ray load4j, a phase-cell endpoint load(4+sqrt(2))j, and a junction vertex load(1+3sqrt(2))j, including its external arm/cable/ray bond. The shared record load is8j, the sum of FOUR norm2j contacts. The record is not duplicated to evade the cubic adjacency or load constraint.

For example D1=Lambda/2, D0=zeta D1, b=eta D0 in the component domain eta<=1/8,zeta<1/2 puts all these sums below Lambda: in particular j=Lambda eta^2 zeta/2<Lambda/256, so8j<Lambda/32. Core loads obey their already checked cap. This is a load-scale existence check without a time claim.

## 4. Exact multiple-reflection composition on the entire external fiber

Fix legal p and retain the full record and passive-reference fiber; equivalently work in each X_R sector then recombine orthogonally. Partition exact scattering matrices as

    S_c=[[A,B],[C,D]] on (I,O),
    S_w=[[a,b_w],[c_w,d]] on (U,F).              (5)

The symbol C in(5) is a block of the actual core, whereas C_p is the ideal path gate. The writer blocks here are direct sums of the same matrix over the two paths, all on the ONE shared record. All block norms are at most1 by real-axis unitarity. Equations(1)--(2) imply

    ||A||,||D||<=e, ||a||,||d||<=w,
    ||B-zC_p||,||C-zC_p||<=e,
    ||b_w-hX_R||,||c_w-hX_R||<=w.               (6)

Each cable has d_c=34 edges, so its exact one-way factor between endpoint reference planes is P=z^34 I_path,record. To verify the reference plane, an outgoing coefficient b at the core has amplitude z^n b along its cable; in writer coordinate m=34-n the same wave is z^-m(z^34 b). Thus the arriving incoming coefficient is P b. No additional free-edge or junction phase is inserted.

Let f_I,f_F be arbitrary external incoming columns. If v is the outgoing O coefficient from the core and u is the outgoing U coefficient from the writer, the exact equations are

    v=C f_I+D P u,
    u=a P v+b_w f_F.

Assume ew<1 and define K=(I-a P D P)^-1. Then ||K||<=1/(1-ew), with its convergent Neumann series representing every repeated round trip. Solving gives the complete four-external-port matrix

    S_IF=[[ A+B P K a P C,       B P K b_w ],
          [ c_w P C+c_w P D P K a P C,
                                      d+c_w P D P K b_w ]]. (7)

Equivalently its lower-left block is c_w P(I-D P a P)^-1 C. This algebra does not omit returns from F incidence or assume a one-way element. All products retain their order, so it remains valid without commuting record/program blocks. Shared X_R sector reduction justifies the local writer direct sum used as its input.

For the ideal matrices, a=d=A=D=0, and the resulting comparator is

    S_ideal(k)=phi(k) [[0,C_p tensor X_R],
                      [C_p tensor X_R,0]],
    phi(k)=z*h(k)*z^34=-i z^57.                 (8)

It is one common momentum phase for both paths, both programs, both record sectors and either direction. At k=pi/2 it equals1. The finite-detuning actual core need not equal its ideal even at band center. For I incidence and record|0>, the ideal outgoing F state carries C_p on logical path, the same record|1>, and no I outgoing component. General record input undergoes X. Incidence from F gives the reciprocal ideal action back to I.

## 5. A full-matrix error bound and internal reconstruction

Let den=1-ew>0. Diagonal blocks in(7) obey

    ||S_II||<=e+w/den, ||S_FF||<=w+e/den.

For the upper-right block, telescope B P K b_w against (zC_p)P(hX_R). The differences of B,b_w contribute at most e+w, and ||K-I||<=ew/den contributes at most ew/den, since B and b_w are contractions. The lower-left block has the same bound by its alternate inverse formula. The norm of a block matrix is at most the norm of its matrix of block-norm ceilings, bounded by the larger row sum here (that matrix is symmetric). Consequently

    ||S_IF-S_ideal||
       <=min{2,[2(e+w)+ew]/(1-ew)}.              (9)

For example the first row sum is2e+w+(w+ew)/den; multiplying by den gives2e+2w+ew-2e^2w-ew^2, at most2(e+w)+ew. The other row follows by interchanging e,w. The cap2 is legitimate because the whole physical scattering matrix and comparator are unitary; real-axis unitarity of the composition also follows directly from conservation of incoming-minus-outgoing flux in the two components, with the unit-modulus internal cable flux canceling. Reciprocity follows from the real symmetric relative Hamiltonian and the same endpoint convention, or from transposing the solved system with reciprocal component matrices. No success-column normalization or postselection is used.

This proves arbitrarily small stationary error by taking eta,zeta and the half-bandwidth small, with ew<1. It does not use the old nominal4e-6 band as a necessary physical constraint; any selected compact band inside |k-pi/2|<=10^-3 satisfying these conditions is covered.

Internal fields are retained, not asserted vacant. For arbitrary external input, (7) reconstructs

    u=K(a P C f_I+b_w f_F), v=C f_I+D P u.

Cable amplitudes are the sum of the two corresponding traveling waves at every integer site. Core mediators are b(psi_u+psi_v)/(D_e-E), with the exact source coefficients. Every writer arm is recovered from its two-port incoming data, the orthogonal mixer, finite transfer recurrences through the two phase cells and its terminal equation. This local recovery has no omitted record sector.

There is no local writer embedded dark state hidden by these port equations on the selected open band: zero amplitudes on both external rays force both port values and their outward neighbors zero; the invertible Hadamard junction then forces both arm attachment values zero. Each attachment recurrence forces its inward neighbor zero and induction along the nonzero hoppings kills the whole arm. The terminal equation completes the same conclusion. The cell concatenation denominators used by the checked writer obey1-3|k-pi/2|>0. Thus local internal coefficients are finite and smooth on a fixed compact band. Core denominators D_e-E and the global inverse K also have explicit nonzero margins. This justifies exact stationary reconstruction; it is not an explicit finite-time bound on internal occupation.

Smooth compact-band integration can therefore use the same packet-specific normalization mechanism as the checked core: exact strong evolution, remote-past incoming separation, and decay of finitely many internal-coordinate oscillatory integrals. This observation needs no global spectral completeness, but no new numerical derivative constants or finite-seed error budget are claimed. Localized spectrum outside the band, and any omitted components of an actual supplied seed, remain obligations for a complete early vector match. Unitarity of the on-shell matrix alone would not pay those components.

## 6. Record meaning and outstanding interfaces

The four external ports and complete record/program/reference fiber are included in(7)--(9). Distinct O channels ensure intended I-to-F transmission traverses one writer after routing, with both logical paths reaching separate final rays. Equal cables and identical writers provide the common phase and preserve logical coherence. This removes the earlier unchanged-two-lead double-crossing premise; it does not turn the record into an irreversible latch.

Stationary output record|1> is an outgoing-channel interpretation. During a terminal visit, j n_T X_R can create record1 while the head remains inside a writer; a returning head can toggle it again. Thus record1 is not yet an all-time certificate of completed routing, vacant apparatus or correct final output. No physical stopping, capture, reset or arbitrary-time heralded correctness follows.

Remaining quantitative interfaces include actual finite I emitters and F cuts; full early seeded matching paying all localized/spectral components; first/second derivatives of the composed matrix and internal maps; finite outer-return control; common normalized finite output with every mediator/writer/cable residual included; and a simultaneous observation-window/load choice. An all-time completion-signal theorem is a further distinct question even after those finite-window steps. No old processor runtime, native Record identification, autonomous initialization/readout, precision tolerance or new physical law is supplied.

## 7. Exact sources and exposure

Read fully and hash-verified for this task:

- common_product_stage_separated_router/PROPOSAL.md:60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182.
- common_product_stage_separated_router_check/REVIEW.md:8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d.
- autonomous_record_route/PROPOSAL.md:93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56.
- autonomous_record_route_check/REVIEW.md:c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a.

The writer's old/source B, converter, spectral selections and runtime ancestry are not imported. Here its external uniform j leads are attached to the explicitly supplied four-port microscopic core. The only extra internal fiber beyond legal program/path is the one shared record and arbitrary passive references; no interacting old closed channels are presumed absent by an inherited theorem.

ROOT supplied the two-writer/shared-R concept. This author reconstructed the explicit disjoint placement, two34-edge cables, reference-plane phase, scalar/count/load bookkeeping and exact feedback composition. Required distinct checks include all coordinate collisions and cubic neighbor uses, writer sign/order preservation under T, both record sectors, every feedback block and norm estimate, internal reconstruction and boundaries of the completion interpretation. Component checks are reused at their stated scopes, not counted as checking this new composition.

Only common_product_stage_record_core/PROPOSAL.md was created. No scientific executable, numerical solver/simulation, sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. No retained status or independent acceptance is assigned.
