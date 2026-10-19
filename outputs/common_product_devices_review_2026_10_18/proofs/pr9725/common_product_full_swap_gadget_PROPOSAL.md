# Twelve simultaneous positive square gadgets on the actual entrance data

New conditional author theorem requiring a distinct check. Twelve independent cat+ squares can simulate the SUM of the twelve four-Pauli entrance terms, on their actual shared six data qubits, with a known scalar and a uniform full-vector remainder. Shared data do not commute at the level of elementary gadget couplers. Their mixed fourth-order paths change the scalar: it is NOT twelve times the isolated scalar. The proof below retains that change.

This theorem is for the joint gadget core with otherwise passive data. It does not yet simulate the router background or even silently add the remaining direct two-body/onsite entrance terms to its propagator. Those require a separate background interface. The construction uses finite-range arbitrary positive two-body Pauli couplers, including complex Y terms, and twelve supplied GHZ+ states. It is not an old nearest-neighbor primitive realization or an autonomous input initializer.

## 1. Joint operator and exact target

Label the two entrance head pairs (i_e,j_e), e=0,1, as in c97b. They share the same physical Q,P. For each triple l=(e,H,A), H in {X,Y}, A in {X,Y,Z}, assign a separate four-cycle of ancillas b_l,1,...,b_l,4 and data operators

    (O_l,1,O_l,2,O_l,3,O_l,4)=(H_i_e,H_j_e,A_Q,A_P),
    Omega_l=product_(r=1..4) O_l,r.

There are L=12 gadgets, 48 distinct ancillas and six data qubits. Set

    H0=Delta sum_(l,r)(I-Z_l,r Z_l,r+1)/2,
    V=nu sum_(l,r) O_l,r X_l,r,
    Hphys=48nu I+H0+V.                                  (1)

Every penalty is positive with norm Delta and every supplied coupler nu(I+O_l,r X_l,r) is positive with norm 2nu on its entire two-qubit support. Data Pauli operators in different gadgets may anticommute. No simultaneous data-column reduction is used below.

Each ancillary X_all,l is conserved. Restrict to their common plus sector, supplied by literal injection

    J psi=psi tensor (cat+)^(tensor12), P=JJ*, Qperp=I-P.

Within this sector H0 has zero subspace exactly P, with arbitrary data/reference multiplicity, and complementary gap >=2Delta. The cat- sectors outside it remain actual ground sectors of the full penalty; they are not removed by a gap argument. Let R=Qperp H0^-1 Qperp.

The exact target decomposition per entrance is

    Q_j0^SWAP = Q_(j0/2)(i_e,j_e)+(j0/2)(n_i_e+n_j_e)
                         -(j0/4) sum_(H,A) Omega_(e,H,A). (2)

Thus matching the fourth-order gadget coefficient requires g=j0/4, not an independently variable strength at fixed Delta and nu.

## 2. Operator perturbation coefficients without commuting columns

Use a formal real perturbation parameter x in H(x)=H0+xV. Let the analytic low invariant subspace be the graph P+X(x), X:P->Qperp, near x=0. Its unnormalized Bloch operator is B=x P V X since PVP=0. The graph equation is

    H0 X+x Qperp V P+x Qperp V X=X B.

Expansion gives

    X1=-RVP,
    X2=RVRVP,
    B2=-A, A=PVRVP,
    X3=-RVRVRVP+R²VP A,
    B4=-PVRVRVRVP+(PVR²VP)A.                            (3)

All intermediate R factors exclude low returns; the displayed product order is part of the formula. The metric on the graph is S=P+X*X=P+x²(PVR²VP)+O(x³). Its normalized effective operator is S^(1/2) B S^(-1/2). At fourth order the possible extra commutator is [PVR²VP,B2]/2. In this problem both factors are scalars, so it vanishes. Therefore (3) is also the fourth coefficient of the normalized real effective operator, without assuming V's data factors commute.

A two-flip return must flip the same ancilla twice. Every single-flip energy is 2Delta and every O_l,r squares to I. Consequently

    A=24nu²/Delta I,
    PVR²VP=12nu²/Delta² I.                              (4)

The normalization correction in (3) is +288nu⁴/Delta³ I.

At order four the final ancillary configuration must have, in every gadget, either no flips modulo two or all four flips. There are exactly three classes:

(a) Four distinct flips in one gadget. The 16 adjacent-pair orders and 8 opposite-pair orders have denominators 8Delta³ and 16Delta³. Their sum is (5/2)/Delta³ times Omega_l; cat+ gives no minus sign. These elementary data factors act on distinct sites within that gadget.

(b) Two distinct ancillas in ONE gadget, each repeated twice. Excluding intermediate P returns leaves the same aggregate denominator count, carrying identity. Summing twelve gadgets contributes 30nu⁴/Delta³ I to PVRVRVRVP.

(c) One ancilla from each of TWO gadgets, each repeated twice. For an unordered pair of elementary terms u,v, allowed orders are uvuv,uvvu,vuuv,vuvu. The orders starting uu or vv return to P at step two and vanish. All four allowed paths have energies (2Delta,4Delta,2Delta). Write O_u O_v=chi O_v O_u, chi=+1 or -1. The two alternating products equal chi I; the other two equal I. Their aggregate is (1+chi)nu⁴/(8Delta³) I. This retains the order of noncommuting shared data operators. It is zero for anticommuting pairs and nu⁴/(4Delta³) for commuting pairs.

There are choose(12,2)*16=1056 cross-gadget elementary pairs. Exactly 132 anticommute: on Q there are four X, four Y and four Z entries, giving 3*4*4=48 unlike pairs; P gives another 48; on each of the four entrance heads there are three X and three Y entries, giving 4*9=36. Operators on different data qubits commute. No such elementary pair is double-counted, and within-gadget data supports are distinct. Thus 924 pairs commute, contributing 231nu⁴/Delta³ I.

Combining (3)--(4), the normalized effective coefficients are

    E_lead=s I-g sum_l Omega_l,
    s=-24nu²/Delta+27nu⁴/Delta³,
    g=5nu⁴/(2Delta³).                                   (5)

Indeed the fourth scalar is 288-30-231=27. The isolated-gadget scalar would instead give -6; the difference 33 is exactly 132/4. No non-scalar mixed-gadget operator survives at this order. This is a direct finite combinatorial proof; no enumeration executable or numerical fitting was used.

## 3. Joint normalized effective operator and full-output remainder

Let alpha=nu/Delta<=1/768 and v=||V||<=48nu. On |z|=Delta/2, ||(z-H0)^-1||<=2/Delta. For complex |x|<=Delta/(8v), the Neumann ratio is <=1/4 and the perturbed resolvent is <=8/(3Delta). Its Riesz projection Pi(x) obeys ||Pi(x)-P||<=1/3. The analytic branch

    C(x)=(P Pi(x)P)^(-1/2),
    E(x)=C(x) P H(x)Pi(x)P C(x)                         (6)

has ||C||²<=3/2 and ||E(x)||<=Delta, from the contour formula ||H Pi||<=2Delta/3. For real x, W(x)=Pi(x)P C(x) is an isometry and E=W*H W. This is the same normalized graph operator used in (3): Pi P=(P+X)S^-1 and P Pi P=S^-1. Thus the coefficients in (5) belong to this explicit analytic operator, not merely to unnormalized eigenvalue equations.

The product of Z over all 48 ancillas conjugates V to -V, commutes with H0, preserves every plus sector and fixes P pointwise. Hence E(x) is even as an analytic operator. The analytic radius is at least 1/(384alpha), so Cauchy bounds and the even tail give

    ||E(1)-E_lead||<=R6,
    R6=Delta(384alpha)^6/[1-(384alpha)^2].              (7)

No data Hilbert-space dimension or reference dimension enters this bound. In particular it covers arbitrary joint occupation states of the six data qubits, not only one moving head.

At x=1 the contour bound gives

    deltaPi<=96alpha/(1-96alpha)<=1/7.

The positive real inverse square root estimates used for the isolated component depend only on deltaPi, not on commuting data columns: ||W(1)-J||<=2deltaPi<220alpha. Paying this difference at both endpoints and applying real self-adjoint Duhamel in the low space yields, for every real t,

    ||exp(-itHphys)J
       -exp[-it(48nu+s)] J exp[+it g sum_l Omega_l]||
                        <=min{2,440alpha+|t|R6}.         (8)

One may replace 440 by the looser 480. This is a complete vector bound with all 48 ancillary outputs retained, arbitrarily reference-extended. The comparator has the literal product of twelve cat+ states; the actual vector is neither projected nor normalized. The scalar 48nu+s is known and retained. Higher-order scalar terms are paid by R6, not silently removed by phase fitting.

For any declared horizon T and error budget epsilon, the finite sufficient conditions 440alpha+T R6<=epsilon, alpha<=1/768, and g=j0/4 are explicit. They need not be simultaneously feasible for an independently fixed j0, cap and arbitrarily small epsilon. No router operating time is selected or certified here. Joint ancillary preparation error adds by the corresponding full-vector or channel contraction estimate; correct marginals alone are insufficient.

## 4. Actual finite-range placement and full-support loads

Use the c97b data coordinates

    i0=(19,0,0), j0_site=(20,0,0),
    i1=(23,2,0), j1_site=(22,2,0),
    Q=(21,1,1), P=(21,1,0).

For gadget number l=1,...,12 choose cyclic ancillas

    (24,4,2l), (25,4,2l), (25,5,2l), (24,5,2l).

Install the four square penalties and four corresponding data-to-ancilla couplers; all unlisted couplings remain absent. Squares are disjoint and their penalties are unit nearest-neighbor edges. The 48 sites have x=24 or25, y=4 or5, z>=2. Original input rays have x=19 or23, final rays y=+/-8,z=1, near-core cables z=0, the core x=20..22,y=0..2, and both writers near x=0 with the transported small z extent. Hence none occupies a new ancillary site, for every finite ray length. There are no old program copies in the single-control inventory.

Data-to-ancilla edges are finite-range two-body supports, not nearest-neighbor edges. Their Manhattan length is at most 35 and Euclidean length at most sqrt(637)<26; the farthest possible assignment is bounded by the first input terminal to (25,5,24). These uniform bounds are independent of ell. The placement does not evade a nearest-neighbor degree restriction: it explicitly changes the permitted range. No mediator routing construction is claimed.

There are 48 new qubits and 96 new positive blocks in this gadget core. Each ancillary incident sum is 2Delta+2nu; each entrance head has six couplers and load 12nu; each of P,Q has twelve couplers and load 24nu. These are full-support loads. For example Delta=Lambda/4 and alpha<=1/768 put these gadget-only loads below Lambda, but an actual installed cap must ADD each data site's remaining background load. The source does not count a background as absent when later attaching it.

The six direct positive blocks needed for the two residual terms in (2) are two Q_(j0/2) bonds and four onsite (j0/2)n terms. They are not included in (1) or its dynamical theorem. Replacing the two original conditional entrance blocks by those six blocks and these 96 gadget blocks would add 100 listed blocks and 48 ancillary qubits to c97b; that is a prospective inventory, not a verified full-router simulation. Its data-load bookkeeping must remove the original two norm-2j0 contacts and insert the residual and gadget loads, and its dynamics must be established independently.

## 5. Remaining interfaces and exact exposure

The ordered calculation above closes the simultaneous twelve-term algebra and isolated joint full-vector remainder. It does not justify appending a noncommuting background to (8). In particular the rest of (2), the existing core's program detunings, and the ray/record terms generally act nontrivially on the shared data; the passive-data proof cannot simply declare them spectators. A separate valid attachment estimate or effective-operator analysis must retain all of them and the physical scalar before importing any runtime gauge comparison. No complete-loader or boundary-input preparation premise is removed by this result.

The arbitrary positive Pauli-product couplers, Ising penalties, complex Hermitian Y terms, finite range and supplied cat+ preparation are explicit changes/assumptions. They have not been derived from the former positive exchange/control/writer primitives or a native law. There is no assertion of real-only implementation, unique ground-state initializer, network compiler, practical accuracy, permanent halt or release.

Fully read primary component source common_product_loader_bond_realization/PROPOSAL.md, SHA256 7e6769927d3138b2812e0b4a0db62df1ef4d1d7096b10acfa2269a5ca8a98d39, and its complete distinct common_product_loader_bond_realization_check/REVIEW.md SHA256 f71cdc4e4039f923f99c8ed1f2abab9baedee9f8f9456c1d77ed6a9978b9fd58. Its commuting single-component coefficient argument is used only for comparison and its general contour estimates are rederived with v=48nu. The new mixed paths and normalized graph calculation are independent author derivations, not inherited from its scalar-column premise.

Target common_product_autonomous_loader_interface/PROPOSAL.md is c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e, with my prior check7a98f648e21cf63b70d481b2cbaba8fac86376763cec0f50678f0ed49e9bd68f. Actual geometry uses the unchanged single-control76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 and stage-record-corec91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729 passages fully inspected in that review. I authored earlier cell/sector/boundary-input work and checked c97b, but did not author the isolated gadget. ROOT suggested the joint mixed-path route and square-layer placement. This is exposed same-model author continuation; no independent validation is claimed. A distinct check should especially challenge (3), the 132 ordered-sign count, normalized effective identification, full-vector constants and actual finite-range coordinates.

After I reported the derived scalar and wrote this proof, ROOT reported a separate matching count and placed an unreviewed ROOT_CROSS_PATH_NOTE.md in this folder. I have not used that note as a premise or distinct check; this additional exposure is recorded. Only this proposal was created by me. No scientific program or enumeration, numerical sweep, W/Git/canonical/checkpoint/editable-prompt/model change, delegation or publication occurred. All coefficients above were derived analytically; no desired operating result was imposed.
