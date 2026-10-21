# A positive two-body component for the conditional loader bond

Bounded author derivation and interface assessment, requiring distinct review. An explicit static nearest-neighbor two-qubit construction below approximates ONE four-qubit Pauli product, with a full-vector leakage/time bound, specified scalar phase, fixed incident cap and supplied four-ancilla GHZ+ state. This is a useful component of the conditional SWAP-hopping target c97b, not a realization of that complete entrance bond or its coupled runtime Hamiltonian.

The displayed two-body couplers are arbitrary positive Pauli-product blocks. Their availability itself goes beyond the campaign's specifically realized head exchanges, diagonal program controls and record contacts. The construction does not silently add them to that primitive inventory. Its entangled ancillary initialization is an additional preparation premise, not a replacement by blank product qubits.

## 1. The exact target and the component selected

The conditional loader target on head sites i,j and ordinary program qubits Q,P is

    Q_j0^SWAP=j0[n_i+n_j
          -(a_j^dagger a_i+a_i^dagger a_j)SWAP_QP].      (1)

Here j0 denotes the intended bond strength, not a site label. Since a_j^dagger a_i+a_i^dagger a_j=(X_iX_j+Y_iY_j)/2 and SWAP_QP=(I+X_QX_P+Y_QY_P+Z_QZ_P)/2, its exact full-space decomposition is

    Q_j0^SWAP = Q_(j0/2)(i,j)+(j0/2)(n_i+n_j)
       -(j0/4) sum_(H in {X_iX_j,Y_iY_j})
                    sum_(D in {X_QX_P,Y_QY_P,Z_QZ_P}) H D. (2)

This retains vacuum and double occupation. The two-body/onsite part alone is not (1). There are six four-body terms with their exact coefficients.

Choose one of them, for example X_iX_j Z_QZ_P. More generally let O_1,...,O_4 be Hermitian unitary single-qubit Pauli operators acting on four DISTINCT data qubits, and put Omega=O_1O_2O_3O_4. They commute because their supports are distinct. The component target is -g Omega, g>0, plus the scalar phase explicitly retained below. Choosing O=(X,X,Z,Z) uses only real matrices and addresses one actual summand of (2). Other choices can require complex Hermitian couplers and are not silently treated as part of a real-block framework.

## 2. Explicit positive nearest-neighbor square

Introduce four ancillary qubits b_1,...,b_4, with cyclic index b_5=b_1, and positive strengths Delta,nu. Define

    H0=Delta sum_(r=1)^4 (I-Z_b_r Z_b_(r+1))/2,
    V=nu sum_(r=1)^4 O_r X_b_r,
    Hphys=H0+nu sum_(r=1)^4 (I+O_r X_b_r)
         =4nu I+H0+V.                                  (3)

Every listed block is positive on its full two-qubit support. A penalty block has norm Delta, and each data/ancilla block has norm2nu. The latter is NOT an assertion that the old supplied primitive set implements arbitrary O_r X_b_r.

A concrete cubic placement is

    b1=(0,0,0), b2=(1,0,0), b3=(1,1,0), b4=(0,1,0),
    data_r=b_r+(0,0,1).

All eight installed interactions are nearest-neighbor edges: four square edges and four vertical edges. Each ancilla has incident norm sum2Delta+2nu; each data terminal has2nu in this isolated gadget. There are eight qubits (four data plus four new ancillas) and eight positive blocks. No timed control is applied.

Let X_all=X_b1 X_b2 X_b3 X_b4. It commutes with H0 and V. Supply the ancillary state

    |cat+>=(|0000>+|1111>)/sqrt(2).                     (4)

It lies in the X_all=+1 sector. Within that reducing sector H0 has a UNIQUE zero-energy ancillary vector cat+, while every orthogonal state has energy at least2Delta. Domain walls on a four-cycle occur in even numbers. Arbitrary data and passive-reference states are retained. Define J psi=psi tensor cat+ and P=JJ^* in this reducing sector.

The full H0 also has the cat- zero state in the other sector. It is not suppressed by (3). Supplying |0000> instead of cat+ populates both sectors and does not meet this lemma's target. Likewise an unspecified ancillary state cannot be called a low-energy blank resource for this purpose. Preparation of (4), its coherence and its error are substantive supplied costs.

## 3. Fourth-order coefficient and the scalar terms

Set Q_perp=I-P and R=Q_perp H0^-1 Q_perp within the plus sector, where the inverse is only on that orthogonal complement. Because each O_r acts on a distinct data qubit, choose their common eigenbasis, with eigenvalues o_r=+-1. Each data column is a nondegenerate ancillary low-band perturbation problem. The energy expansion for H(lambda)=H0+lambda V is even: conjugation by Z_b1 Z_b2 Z_b3 Z_b4 sends V to -V, commutes with H0 and fixes P. Its low effective operator therefore has no odd Taylor coefficient.

The second-order coefficient is -PV R VP=-2nu^2/Delta times the identity. Indeed one flip creates two walls and energy2Delta; only flipping that same ancilla back returns to P at this order. Also PV R^2 VP=nu^2/Delta^2 times the identity.

Expanding the scalar Feshbach equation in each data column gives the fourth-order coefficient

    E4=-(PV R V R V R VP)
                       +(PV R VP)(PV R^2 VP).          (5)

Here R excludes intermediate returns to the low space. This expression follows by expanding (Q_perp H(lambda)Q_perp-E)^-1 on range Q_perp in the exact scalar-column equation E=-lambda^2 PV Q_perp(Q_perp H(lambda)Q_perp-E)^-1 Q_perp VP and inserting E2 at order four. The second term in (5) is therefore a required normalization/energy correction, not a discarded scalar.

A contributing four-flip path either flips all four distinct ancillas, returning to the complementary cat configuration, or flips two distinct ancillas twice, returning to the same configuration without an intermediate P return. For each class there are16 paths with an adjacent pair after two flips and8 with an opposite pair. Their successive nonzero energies are (2Delta,2Delta,2Delta) or (2Delta,4Delta,2Delta). Thus each class contributes

    nu^4[16/(8Delta^3)+8/(16Delta^3)]
                                     =(5/2)nu^4/Delta^3.

The distinct-four class carries Omega and X_all=+1. The double-pair class carries identity since O_r^2=I and different data O_r commute. These exhaust paths whose final head-independent ancillary state lies in P; paths returning after two flips are killed by R. Since the correction product in (5) is2nu^4/Delta^3, the effective operator through fourth order is

    E_lead=s I-g Omega,
    s=-2nu^2/Delta-nu^4/(2Delta^3),
    g=5nu^4/(2Delta^3).                                (6)

Changing the sign of one O_r reverses Omega without changing the scalar or positivity of the corresponding I+O_rX_b_r block. No unknown phase has been absorbed into the target. The actual common physical phase will be exp[-it(4nu+s)].

## 4. Uniform full-vector remainder, not just low eigenvalues

Assume alpha=nu/Delta<=1/64. A conservative analytic bound controls all higher coefficients and the literal cat+ injection. Work throughout in the invariant X_all=+ sector; the uncoupled cat- state is not an unaccounted small denominator. Write v=||V||<=4nu and let Pi(lambda) be the Riesz spectral projection around the circle |z|=Delta/2 for H(lambda). For complex |lambda|<=Delta/(8v), the unperturbed resolvent has norm at most2/Delta and ||lambda V||<=Delta/8, so the perturbed resolvent has norm at most8/(3Delta). The resolvent identity gives

    ||Pi(lambda)-P||<=1/3.                              (7)

The contour isolates the original low band; these norm bounds also ensure no contour spectrum. Put C(lambda)=(P Pi(lambda)P)^(-1/2) on range P, with the analytic branch near identity, and define the effective operator

    E(lambda)=C(lambda) P H(lambda)Pi(lambda)P C(lambda).

For real lambda, W(lambda)=Pi(lambda)P C(lambda) is an isometry from the data code to the exact low subspace, and E=W^*H W. For complex lambda the displayed analytic formula is used, rather than a nonanalytic adjoint construction. The binomial series and (7) give ||C||^2<=3/2. The contour formula for H Pi gives ||H Pi||<=2Delta/3, hence

    ||E(lambda)||<=Delta on that circle.                (8)

The parity symmetry above makes E even in lambda. Cauchy coefficient bounds at radius at least Delta/(32nu), followed by the geometric sum of even powers starting at six, imply at lambda=1

    ||E(1)-E_lead||<=R6,
    R6=Delta (32alpha)^6/[1-(32alpha)^2].                (9)

All dimensions are finite and the bound is uniform over data columns and passive references. The coefficients through order four are (6), because in each commuting data column E is exactly its isolated low eigenvalue; no unverified matrix effective-Hamiltonian rule is being assumed.

For the literal input, the resolvent identity at lambda=1 yields

    deltaPi=||Pi(1)-P||
                   <=(8alpha)/(1-8alpha)<10alpha.

The positive inverse square root and deltaPi<=1/7 give ||W(1)-J||<=2deltaPi<20alpha. For example ||C||<1.081 and ||C-I||<.64deltaPi, so the triangle bound is below2deltaPi. Exact low-space evolution, comparison through W and unitary Duhamel for E(1) versus E_lead now prove for every real physical time t

    ||exp(-it Hphys)J
        -exp[-it(4nu+s)] J exp(+it g Omega)||
                              <=40alpha+|t|R6.         (10)

The first term pays actual ancilla leakage and return mismatch; the second pays the entire remaining effective generator including its scalar part. All eight qubits and arbitrary reference outputs are retained. The ancillas are cat+ in the COMPARATOR, not asserted exactly unexcited in the actual output. No output projection or normalization is applied to the actual state. An initial joint pure-vector error adds by unitarity; a general joint trace error adds to the complete channel bound by contraction. Correct ancillary marginals alone do not provide such a joint preparation guarantee.

## 5. One finite cap/error/time prescription

For 0<epsilon<=1 choose

    Delta=Lambda/4,
    alpha=min{1/64, epsilon/80,
                          sqrt[15epsilon/(16*32^6)]},
    nu=alpha Delta, g=(5/2)alpha^4 Delta.                (11)

For |t|<=1/g, (9) gives

    |t|R6<=(8/15)32^6 alpha^2<=epsilon/2,
    40alpha<=epsilon/2.

Thus (10) is at most epsilon on that horizon. Ancillary incident loads satisfy2Delta+2nu<=Lambda/2+Lambda/128<Lambda, and data loads are2nu<=Lambda/128. The prescription simulates the chosen -g Omega component with a known common phase, not an arbitrarily large fixed g at fixed cap and vanishing error. The sufficient interaction time1/g grows as the accuracy prescription weakens nu. As epsilon tends to zero this explicit isolated family has alpha=epsilon/80 eventually, hence g=Theta(Lambda epsilon^4) and1/g=Theta(Lambda^-1 epsilon^-4). This is not an optimal simulation cost or a loader operating time.

To match the selected term in (2) one would require g=j0/4 and hence choose the target j0 consistently with the gadget strengths, or solve and verify that equality within the cap. The current lemma does not preserve an independently fixed router j while taking alpha arbitrarily small. Scalar4nu+s is large relative to g and must remain in any coherent full-device target; it cannot be declared canceled without supplied compensation and a new phase calculation.

## 6. Why this does not yet realize the entrance bond

The construction is more than a same-support two-body obstruction: it gives a specific eight-qubit mediator Hamiltonian and its actual full-output bound. Its missing transfers are concrete:

1. **Allowed blocks.** The positive couplers nu(I+O_r X_b_r) and ferromagnetic penalties in (3) are a stated arbitrary-positive-two-body class. The displayed old primitives do not automatically supply them. Even the real O=(X,X,Z,Z) case is not identified as a derived head-exchange/control/writer block. Terms containing data Y may need a different real realization or an expressly complex Hermitian block class.
2. **Prepared auxiliaries.** The reducing-sector proof requires one supplied GHZ+ per gadget. Product |0000> has both X_all signs and does not select the same fourth-order coupling. Its preparation, coherent phase and retained-environment error must be paid. Adding an unproved global-X penalty would merely move the multibody problem into the initializer.
3. **Actual terminal geometry.** The explicit gadget has four data terminals on a unit square above its ancillary square. The actual entrance support of c97b consists of two I-ray heads and P,Q at the stated core coordinates, not this terminal geometry. No nearest-neighbor routing or encoded terminal relocation between these geometries is supplied by (10).
4. **Six terms and shared degree.** Equation (2) needs six four-body components per entrance bond, and the architecture has two such bonds sharing P,Q. Six independent copies would attach six ancillary neighbors to each participating data terminal; already for one entrance P would also retain four core-mediator neighbors, exceeding cubic degree six. Identifying auxiliaries or encoding/routing data could change this, but changes the spectral problem. A single-component norm bound does not prove a simultaneous sum, its scalar phase, or its packing/load costs.
5. **The operating background.** Equation (10) is for isolated data with passive spectators. The actual H_router acts on those data and nearby heads while the gadget is operating. It need not commute with the individual O_r. The low-band contour, scalar Feshbach reduction and fourth-order cancellations must be redone with that background, or a verified local simulation theorem must be supplied with its hypotheses checked. The crude global-background norm can grow with system size and is not automatically small relative to Delta under the fixed cap. No claim that such smallness is necessary for every method is made; it is simply not proved by this isolated argument.

These are interfaces to close, not a universal no-go. In particular larger mediators or an autonomous scattering sequence remain possible. Existing router/writer scattering theorems do not by themselves yield the gate-conditioned bond's matrix on every Q/P/head state, its all-output ancillary reset, or a useful background-stable error on the parent's full operating horizon. A timed exchange or a circuit decomposition would not resolve those missing static interfaces.

Even a successful bond realization would only validate the conditional integrated PROGRAM relocation of c97b. Its supplied one-head path encoding, injection energy, blank record, input independence from apparatus quality and retention of old P/environment still have to be preserved. The original complete loader from an energy-certified blank apparatus is not removed by this component.

## 7. Sources, exposure and check obligation

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Exact target source common_product_autonomous_loader_interface/PROPOSAL.md is c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e, authored and fully read in the immediately preceding task; its distinct check was running at assignment. Its enlarged-block status is preserved, not promoted by the present component.

Complete primitive/preparation sources read in that task and reused unchanged are mediated_common_product_program/PROPOSAL.md739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088, common_product_single_control_router/PROPOSAL.md76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01, common_product_biased_record_preparation/PROPOSAL.md9979b614d77b98bf8bc63b6b87b69305beb7cf7607adf5722ae57b759728627e and common_product_energy_blank_interface/PROPOSAL.mde6df21d39a9673b7e396390b64986a9e0deb74223540c975c14675a7f6fec668. Their earlier checked scopes do not certify a new gadget or ancillary state supplier.

ROOT asked for mediators/sequencing rather than a same-support impossibility observation, then confirmed the candidate square path count after receiving the proposed route. That feedback is declared design exposure, not independent validation. This author derived (3)--(11), including the literal-state leakage, scalar correction and analytic remainder. No universal-simulation theorem or external gadget result is imported without proof.

A distinct check should reconstruct the domain-wall path count and Feshbach signs, the conserved plus-sector gap, the complex Riesz bounds and evenness, the normalized real isometry estimate, all scalar phases and full-support norms. Acceptance would support only this isolated positive two-body component with supplied GHZ+, not a simulation of H_router plus all six terms or removal of a loader premise.

Only this proposal was created. No scientific executable, solver/simulation/sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, delegation or publication occurred. Native block/state supply, actual input energy, complete autonomous initialization and permanent output release remain open interfaces.
