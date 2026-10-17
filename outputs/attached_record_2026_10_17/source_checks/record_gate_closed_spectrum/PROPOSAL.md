# Nonnegative isolated record gate after its scalar subtraction

Status: authored exact mathematical proposal, awaiting independent check. For the specified isolated record gate with ordinary semi-infinite j input/output leads, j>0, subtract its declared vacancy scalar c_R=4(sqrt(2)-1)j. In EACH conserved record-X sector x=+1 or-1 the resulting one-head operator H_x is nonnegative. In fact it is unitarily equivalent to a direct sum of two explicitly nonnegative half-line Jacobi chains. Consequently, for every real kinetic energy E<0,

    ||(E-H_x)^-1||<=1/|E|.                              (1)

All matrix elements and compressed boundary/recovery blocks inherit this bound. The spectral bottom is exactly0, so the complete resolvent norm equals1/|E|. No negative bound state remains hidden by the scalar subtraction. This proves an isolated-gate below-threshold inverse statement, not an attached emitter/source theorem or absence of poles above the lead band.

## Source, exposure and scope

The exact local source is ../autonomous_record_route/PROPOSAL.md SHA25693445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56 and its check ../autonomous_record_route_check/REVIEW.md SHA256c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a. Both were previously read completely in the coherent herald-interface task, their hashes were reverified unchanged, and the block inventory/scalar/junction passages were refreshed for this derivation. The local geometry has two eleven-site arms, two separated phase cells on arm1, a four-edge real-Hadamard junction, one shared record, and two ordinary semi-infinite leads. No unspecified connecting cable or attached source interaction is included here.

Parent posed the scalar-subtracted positivity question and its possible use against closed-load poles; no affirmative answer was assumed. I did not author the local gate proposal or its review. This is a new exposed derivation, not independent review of itself. Previously read local workflow/proof discipline is reused. No numerical experiment, sweep, solver, delegation, W/Git/checkpoint/prompt/model edit or publication occurred. Only deterministic source reads/hashes and this deliverable. No editable prompt file changed.

## 1. Subtracting the scalar explicitly

Let gamma=(sqrt(2)-1)j. The four junction vacancies sum to

    sum_v gamma(I-n_v)=4gamma I-gamma sum_v n_v.

Subtract c_R=4gamma from the physical one-head operator. The residual junction contribution is then NEGATIVE onsite -gamma at each of the four square vertices. One cannot infer positivity merely because the original physical blocks were positive.

However, each junction vertex has two incident square edges with magnitudes j/sqrt(2), and one ordinary external arm/lead edge of magnitude j. Their Q-block diagonal contributions sum to sqrt(2)j+j. After the residual -gamma the exact diagonal is

    sqrt(2)j+j-(sqrt(2)-1)j=2j.

There is no further scalar left in this isolated one-head kinetic operator. Its complete coordinate coefficients are:

- Ordinary arm and lead vertices: diagonal2j, incident ordinary hoppings-j.
- The four junction vertices: diagonal2j; arm-to-port hopping block-jU, where U=2^(-1/2)[[1,1],[1,-1]].
- At either terminal in record-X sector x: diagonal j+j(1+x)=2j+jx, with its single inward hopping-j.
- At each endpoint of a phase-cell edge: diagonal j+sqrt(2)j+(2-sqrt(2))j=3j, phase hopping-sqrt(2)j and one neighboring ordinary hopping-j.

The two phase cells have disjoint endpoints, as specified in the source. All other head rows have already been listed. The full isolated operator commutes with the shared X_R, so its x=±1 sector decomposition is exact; there is no duplication or independent choice of record value at the terminals.

## 2. Exact junction reduction to two half-line chains

Write the two lead amplitudes at equal coordinate m≥0 as a two-component vector psi_lead(m), with m=0 at the two port starts. Keep every arm amplitude unchanged, and apply the SAME real orthogonal U to the two lead components at EVERY m:

    phi_lead(m)=U psi_lead(m), m=0,1,2,... .

This defines a unitary on the full two-lead Hilbert space. It is a mathematical basis change, not a new physical coupling, gate or operation on the record.

All lead diagonals are2j I_2 and all between-slice hoppings are-j I_2; these are unchanged by the transformation. At the junction the arm-to-lead block becomes

    (-jU)U^T=-jI_2.

There are no arm-to-arm or port-to-port installed square edges beyond this bipartite block. Hence the signed square has become two independent ordinary-j links, each joining one terminal arm to one transformed semi-infinite lead. Arm0 continues into transformed lead0 and arm1 into transformed lead1. The two physical input/output ports need not remain separately identifiable in this proof basis; unitary equivalence suffices for spectrum and operator norms.

Each resulting chain can be indexed n=0,1,2,... from its terminal. Its terminal is n=0, arm attachment is n=10 and first transformed lead vertex is n=11. All bonds are ordinary-j except the two designated phase-cell bonds on chain1, whose magnitude is sqrt(2)j. The onsite entries are exactly those computed above. This reduction works in both record sectors and can equally be performed before resolving X_R, since the lead mixing acts as identity on the shared record.

## 3. Exact positive quadratic forms

For chain i in{0,1}, let w_i,n be the positive bond magnitude between n and n+1. It equals j except at the two phase-cell bonds on chain1, where it equals sqrt(2)j. Let C_i be the set of phase-cell endpoints; C_0 is empty and C_1 consists of four distinct vertices. For any finitely supported chain vector u,

    <u,H_i,x u>
       =sum_(n>=0) w_i,n |u_n-u_(n+1)|²
        +(2-sqrt(2))j sum_(n in C_i)|u_n|²
        +j(1+x)|u_0|².                                (2)

Expanding the first sum gives off-diagonal entries-w_i,n. At an ordinary interior vertex its diagonal is2j. At a phase-cell endpoint it contributes(1+sqrt(2))j; the displayed extra occupation supplies the difference to3j. At the terminal it contributes j; adding j(1+x) gives2j+jx. Thus (2) reproduces every coefficient of the reduced chain, not merely a lower comparison operator.

Every term in(2) is nonnegative: w_i,n>0, 2-sqrt(2)>0, and1+x equals0 or2. This proves H_i,x≥0 for BOTH record sectors. The finite-degree bounded coefficients define bounded self-adjoint chain operators, so the identity and positivity extend by density to all l2 vectors. The direct sum and inverse unitary transformation give H_x≥0 on the original two-port geometry.

In the unreduced record description the terminal remainder is j|0><0| tensor(I+X_R), which is positive. Thus the same form proves nonnegativity on arbitrary coherent record superpositions as well; resolving sectors is useful for later matching, not necessary for positivity.

The x=-1 terminal is the zero-remainder case, not a negative onsite defect relative to its weighted Laplacian. This is precisely why the lower scalar-subtracted diagonal j at that terminal does not bind a negative state. The strengthened phase bonds likewise cannot be analyzed alone: their accompanying positive occupations produce the exact nonnegative form above.

## 4. Spectral bottom and below-band resolvent

Each reduced chain is an ordinary constant-j half-line sufficiently far out. A normalized constant packet on N consecutive sites, placed beyond all modified sites and away from the terminal, has only its two end jumps contributing to(2), with Rayleigh quotient2j/N. Taking N arbitrarily large shows inf spectrum≤0; positivity gives inf spectrum=0. Bounded self-adjoint spectrum is closed, so0 belongs to the spectrum.

There is no l2 zero eigenvector: zero expectation in(2) requires every positive-weight difference u_n-u_(n+1) to vanish. The resulting constant chain vector is in l2 only when zero. This rules out a zero atom in each chain but is not needed for the E<0 inverse bound. The bottom0 is a threshold, so no positive uniform spectral gap is claimed.

For E<0 and any vector u, positivity gives

    <u,(H_x-E)u> >= |E| ||u||².

The spectral theorem therefore makes E-H_x invertible with norm at most1/|E|; because0 is in the spectrum, the distance from E to spectrum is exactly|E| and the norm is exactly1/|E|. In the stated retarded convention R(E)=(E-H_x)^-1 it is negative definite, while (H_x-E)^-1 is positive. Sign conventions do not alter the norm.

For isometric coordinate inclusions I_b,I_y (including finite blocks),

    ||I_y^*(E-H_x)^-1 I_b|| <=1/|E|,
    ||(E-H_x)^-1 I_b||<=1/|E|.                         (3)

The second bound includes the entire two semi-infinite leads and both finite arms, not just finitely many coordinates. For a known closed kinetic margin E≤-Delta<0 these become≤1/Delta uniformly in both record sectors. For complex z outside[0,infinity), the corresponding bound is1/dist(z,[0,infinity)); on a negative-real vertical line this also supplies an explicit neighborhood free of isolated-gate poles. No analytic continuation into the positive propagating band is inferred.

Exact finite compression of H_x is also nonnegative. A finite lead cut with the required j n_last cap realizes that compression; an arbitrarily changed boundary load is not covered by this observation.

## 5. What this resolves and what it does not

For an isolated gate fiber carrying a fixed internal energy beta and total scalar-subtracted energy lambda, the relevant gate kinetic energy is E=lambda-beta. Whenever that energy is strictly negative with a supplied margin, (1)--(3) exclude isolated-gate poles and control its full resolvent uniformly. If the gate acts as identity on the other internal fibers, this is a direct spectral decomposition statement and retains the common record coherently. A particular attachment must establish the actual lambda-beta margin and the correct common scalar subtraction; the proof supplies no new energy calibration.

The conclusion does not cover a channel closed ABOVE the upper lead band. It does not exclude positive bound states generated by phase-cell modifications, and it does not bound the on-shell propagating resolvent on0<E<4j. It also does not automatically certify a load's generalized reflection-coefficient norm in a growing/decaying-wave normalization: such a coefficient requires its own exact conversion from the resolvent and reference-plane conventions.

Attaching the source/emitter changes the operator. An attachment Schur complement can produce poles even if one isolated component is nonnegative; its coupling, onsite compensation, source energies, all complementary inverses and common energy offsets must be checked together. The present basis change mixes the two isolated leads and is not asserted to diagonalize an asymmetrically attached source. Thus this lemma may supply a below-threshold gate block estimate inside an attachment proof, but it does not prove that proof's full inverse or herald bounds.

The result uses no stationary finite-band approximation or presumed exact reflectionlessness. It follows from the literal installed coefficients after the potentially dangerous scalar subtraction. A separate checker should verify the junction diagonal bookkeeping, the infinite lead unitary, and each term in(2) before using it as a checked closed-energy input.
