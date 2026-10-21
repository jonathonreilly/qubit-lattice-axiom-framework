# Structured coefficients preserving the exact loader gauge

New author derivation requiring a distinct check. The global composition f874302 is itself under distinct review at this freeze. This note gives a sufficient family of supplied coefficient symmetries for which the SAME ordered gauge and record projection remain exact. It does not classify all possible coefficient families, derive these symmetries from native physics, or prove fabrication robustness on an open neighborhood of arbitrary blocks. A separate finite-time perturbation bound is stated with explicit hypotheses and a rare-event qualification.

The central result is that uniform scalar matching is unnecessary for exact logical action. Layer-dependent positive hoppings and scalar potentials may change the scalar propagation arbitrarily while leaving the complete spatial-event operation unchanged. They can introduce reflection, trapping and poor success probability. No transfer time or high-probability window is inherited.

## 1. Fixed graph, logical sequence and scope

Retain precisely the 26-layer, four-rail graph of f874302, with the shared ordinary qubits Q,P,R, no free data Hamiltonian and no bypass. There are296 internal heads in74 virtual slices x=0,...,73, with rail labels(a,b). All interlayer cables have one edge. There are eleven diamond layers, fourteen Hadamard layers and one b-permutation layer. The ordered logical gate is

    U_f=I_a tensor[X_R C_P^(b) SWAP_QP],
    G_out=-U_f,
    G_pre=I_a tensor[C_P^(b) SWAP_QP].                  (1)

The last four diamonds alone touch R and their target is X_R. The final layer occupies virtual coordinates70=L,71=B,72=C,73=R_d. The internal head rotations, target labels, signs and chronological gate order are not changed. In particular the old program/environment is retained through SWAP rather than erased. Input has a=1 and R=0 when the record statement is used, but the global operator identity is on the full shared eight-dimensional Q/P/R fiber and all four rails.

This is a one-head gauge statement. Each installed physical block is nevertheless separately positive on its complete one-/two-qubit support and annihilates the head vacuum for arbitrary data. Neither the arm rotation nor the cumulative gauge is an installed physical operation or an all-head local circuit.

## 2. A sufficient nonuniform diamond family

For a diamond layer d choose numbers

    a_L,d>0, a_R,d>0, g_d>0,
    p_L,d>=0, p_A,d>=0, p_R,d>=0.                       (2)

Use the SAME six numbers on all four physical rail diamonds in that layer, including the identity lanes. Different layers may use completely different numbers. Each diamond installs

    Q_+(L,u;a_L), Q_+(L,v;a_L),
    Q_+(u,R_d;a_R), Q_-(v,R_d;a_R),
    g n_u(I+X), g n_v(I-X),
    p_L n_L+p_A n_u+p_A n_v+p_R n_Rd.                  (3)

Here Q_s is the full-support positive block of the diamond source, with norm2a. The last line denotes separate positive onsite blocks when their coefficients are nonzero. X is the prescribed X_D or Z_D for that rail. For an identity lane X=I, install2g n_u and omit the zero v contact. The scalar part and target part of each nontrivial contact in(3) share exactly the coefficient g; the two opposite contacts share that same g. This equality is a sufficient condition, not a derived calibration procedure.

Let c_L,c_R be the actual adjacent ordinary cable/lead weights, equal across rails. Their contributions to the endpoint diagonals must be included once. In the physical L,u,v,R_d basis, the arm diagonals are

    d_A I+gX, d_A I-gX,
    d_A=a_L+a_R+g+p_A.

The endpoint diagonals are

    d_L=2a_L+c_L+p_L,
    d_R=2a_R+c_R+p_R.                                   (4)

Under B=(u+v)/sqrt(2), C=(u-v)/sqrt(2), the exact one-head matrix is

    [d_L I, -sqrt(2)a_L I, 0, 0;
     -sqrt(2)a_L I, d_A I, gX, 0;
     0, gX, d_A I, -sqrt(2)a_R I;
     0, 0, -sqrt(2)a_R I, d_R I].                       (5)

Thus equal left/right coupling strengths are NOT required: a_L and a_R are independent. Equality across the TWO physical arms at a given end is required by this sufficient construction. Equal added onsite potential on u and v makes it a scalar on both B,C. Endpoint potentials may differ from one another and from the arms.

The prefix gauge on L,B is W_pre; the gauge on C,R_d is -X W_pre. It converts(5) to a scalar Jacobi segment with diagonal d_L,d_A,d_A,d_R and negative hoppings

    -sqrt(2)a_L, -g, -sqrt(2)a_R.                        (6)

The gate remains -X regardless of these positive coefficient values. Identity and gated lanes have identical scalar segments. Positivity of all original physical blocks is immediate from a_L,a_R,g>0 and p>=0. The scalar comparator's positivity follows from its unitary equivalence to the positive one-head restriction; it is not an extra independent choice of an arbitrary tridiagonal matrix.

## 3. Nonuniform mixers, cables and site potentials

At a Hadamard layer choose t>0 and common nonnegative endpoint potentials p_left,p_right. Each two-rail mixer has four Q_s bonds of weight t/sqrt(2), with signs prescribed by H. Both parallel mixers use the SAME t and endpoint potentials. Its forward hopping block is -t H on the selected rail bit, and endpoint diagonals are

    d_left=sqrt(2)t+c_left+p_left,
    d_right=sqrt(2)t+c_right+p_right.                    (7)

Cables have common scalar weights c_left,c_right across all four rails. The gauge at the right slice is H times the prefix. Equation(7) is scalar in rail/data space and hence unchanged by that gauge. Scalar uniform matching between neighboring layers is not needed.

For the permutation layer choose t>0, four Q_+(t) bonds realizing X_b, and common onsite potentials p_left,p_right>=0. The forward block is -t X_b and its diagonals are t+c_left+p_left and t+c_right+p_right. No fixed mu repair is required for exact gauge action; such a repair was only part of the uniform-matching special case. Setting p to the appropriate values recovers that special case exactly.

Each interlayer cable can have its own positive weight c_x, the same on all four rails. There is one block per physical edge, not separate attachments counted twice. At any added ordinary lead/cable-interior position with left/right weights c_-,c_+, a common nonnegative onsite p_x gives diagonal c_-+c_++p_x. These scalar quantities can vary with clock position. The present fixed internal graph has no cable-interior heads; they are mentioned only as a permitted scalar extension, with any extra counts paid separately.

Rail-dependent scalar coefficients inside mixed layers are NOT licensed. A diagonal rail matrix generally becomes a data/rail operator under the cumulative gauge, rather than the scalar comparator intended here. A more general commuting family could be considered separately, but none is presumed. In the finite source arrangement of f874, differing left a=0 versus a=1 terminations remain permissible because W=I there, the scalar channels decouple, and the two selected a=1,b inputs have identical scalar terminations. All right terminations are identical. They must not be replaced by independently detuned b-dependent emitters while retaining a common profile claim.

## 4. Complete global identity and phase accounting

After the same44 head-arm rotations A as f874, the forward block at each virtual link is

    H_(x+1,x)=-w_x V_x, w_x>0,                          (8)

with V_x exactly the old gate label: I for ordinary/cable/outer diamond links, H_a/H_b for mixers, X_b for the permutation, and -X_layer for a central diamond link. The scalar values w_x are respectively c_x, sqrt(2)a_L, sqrt(2)a_R, t, or g. Every diagonal is d_x I, with d_x determined by(4)--(7) and the actual incident cable weights. Set

    W_0=I, W_(x+1)=V_x W_x,
    h_str=sum_x d_x|x><x|
              -sum_x w_x(|x+1><x|+|x><x+1|).           (9)

Then the exact ordered identity is

    (A W)* H_one (A W)=h_str tensor I_(rails,QPR).       (10)

Indeed W_(x+1)* V_x W_x=I on each link and W_x* d_x I W_x=d_x I. No noncommuting data operators have been interchanged. All physical arms, origins and shared ordinary qubits remain included. The coefficients affect h_str, not W. Therefore W_out=-U_f and the prefix before the final diamond remains G_pre.

The literal tensor product in(10) assumes identical scalar extensions on all four rails. For the explicitly allowed unequal left a=0/a=1 finite terminations, replace it by the direct sum of their scalar operators over the rail labels, tensor the data identity. The two selected a=1,b channels have the SAME operator h_str and form an invariant scalar subspace; all formulas using a single f below apply on that selected input subspace. This is not an assertion that the unused a=0 scalar chains have the same endpoints.

In an infinite version require uniformly bounded d_x,w_x, so h_str and the physical one-head operator are bounded. In any finite version no such uniform-in-size assertion is necessary; all finite supplied coefficients define self-adjoint matrices. No statement is made about boundedness of an infinite all-head Hamiltonian.

There is generally NO single extracted exp(-i mu t) factor or exact exp(73ik) transmission phase. Use the FULL scalar evolution f(t)=exp(-it h_str)|source> and retain its entire phase. Only if d_x=d_x^0+mu is a common shift may one instead write exp(-i mu t)exp(-it h_str^0), once. The uniform choice a_L=a_R=J/sqrt(2),g=t=c=J, zero diamond/Hadamard onsite, permutation/exterior onsite mu=(sqrt(2)-1)J recovers f874 and its exact common phase convention. Arbitrary choices in(2)--(7) generally reflect incoming waves. No reflectionless or matched-band conclusion is transferred.

For any common scalar left-head input independent of the logical/data state, the complete evolution is

    A sum_x f_x(t)|x> tensor W_x xi.                    (11)

Any spatial right-extension projection therefore factors as its actual scalar profile times -U_f xi, with input-independent probability. Conditional on nonzero probability its normalized operation is exact, even when that probability is small. This remains an exact gate statement, not a probability lower bound or a physical preparation result.

## 5. Exact record projection under the structured family

The final central coefficient g_final may differ from every other g, but its four diamonds share the same coefficients and only their X_R contacts act on the record. Thus at virtual slices70,71,72,73,

    W_70=W_71=G_pre,
    W_72=W_73=-X_R G_pre=-U_f.                          (12)

With initially blank R, every earlier prefix leaves R0. The physical final-arm amplitudes have the SAME gauge mixture, now with the new scalar f:

    psi_u=(f_71 G_pre-f_72 U_f)xi/sqrt(2),
    psi_v=(f_71 G_pre+f_72 U_f)xi/sqrt(2).               (13)

Projection onto R1 kills the f_71 term exactly. Consequently

    P_R1 exp(-itH_one)E_left,R0
       =-J_rec[(f_72|72>+sum_(x>=73)f_x|x>) tensor U_f], (14)

where J_rec embeds coordinate72 into the final physical antisymmetric arm combination and all x>=73 into their corresponding heads, retaining the rail label. The probability is |f_72|^2+sum_(x>=73)|f_x|^2 and is input independent. This is an exact all-time identity for the structured family, with the full h_str phase already in f. It is not obtained by assigning the completed word separately to each unprojected arm.

R=1 still does NOT imply external arrival: the antisymmetric arms and final origin are internal. The external-only event begins at x=74 and has a different scalar profile/probability. The exact logical action for either nonzero event preserves old P/reference correlations; internal vacancy requires the external spatial event. Neither event is an irreversible latch, and returns can undo the record. Additional earlier R couplings, nonblank R or free data dynamics are outside(14).

## 6. Full-support loads, block counts and cap examples

For a diamond in(3), after its actual adjacent cable is included, the full-support incident sums are

    L:4a_L+2c_L+p_L,
    R_d:4a_R+2c_R+p_R,
    gated u,v:2a_L+2a_R+2g+p_A,
    data target D:4g per gated diamond.                 (15)

In an identity diamond u has the same ceiling; v omits2g. A Hadamard endpoint has2sqrt(2)t+2c+p, a permutation endpoint2t+2c+p, and an ordinary scalar interior2c_-+2c_++p. These are sums of FULL-support block norms, not one-head expectations or row norms.

Let S_Q denote the five controlled diamond layers targeting Q (four CZ and one CX), and S_P the five targeting P (two CZ on a, two CX on a, and the CZ on b). Each such layer has two gated diamonds. The exact data loads are

    load(Q)=8 sum_(d in S_Q) g_d,
    load(P)=8 sum_(d in S_P) g_d,
    load(R)=16 g_final.                                 (16)

Thus an explicit cap condition is that every number in(15), the mixer/ordinary bounds and(16) is <=Lambda. This is a finite list of inequalities, not an assumed cancellation of positive terms. A simple sufficient scale box is: all a_L,a_R,g,t,c<=s and every additional onsite p<=s, with s<=Lambda/40. Then Q/P loads are<=40s, R<=16s, diamond heads<=7s and other displayed heads<7s. Exceptional scalar endpoint blocks must separately fit their own incident norms. For the compensated source of f874 with ordinary weight c<=s and gamma<=c, a combined source has norm3c; its adjacent ordinary bond and p<=s give at most6s at the neighboring head, also within40s. This illustrates cap feasibility without fixing a unique uniform matched J.

There are still296 internal heads and three data qubits. Before optional site potentials, the nonzero structural blocks are392 head-head bonds,48 gated head-data contacts and20 identity-diamond onsite contacts, totaling460. Additional p potentials may be represented by at most one separate onsite block at each of296 heads, including equal values on both arms where required. If N_p of these are nonzero, the convention gives460+N_p listed internal blocks, 0<=N_p<=296. The uniform f874 case has N_p=8 and recovers468. Identity-u contact and an extra onsite potential are counted as separate supplied blocks in this convention even if they could be combined; this keeps all full-support loads conservative and explicit. No zero term is counted. Any added exterior heads and terminations bring their actual blocks and onsite potentials, not an unchanged universal finite count.

The range18 fixed-graph placement of f874 still applies because no support or vertex has changed. Equal values at distinct physical sites are a supply constraint, not a geometrically enforced identity. There are still20 distinct neighbors at Q/P, so this does not become nearest-neighbor native physics.

## 7. Which asymmetries are not covered

The family contains many freely variable positive parameters but is not open in the space of arbitrary physical block matrices. Three explicit failures prevent relabeling it as generic fabrication robustness.

First, adding delta n_u to one arm alone adds delta/2 to both B/C diagonals and delta/2 I to their off-diagonal. The gauge transforms the extra central term into a non-scalar data operator. For an isolated diamond, the shortest nonzero right-transfer coefficient becomes

    (H^3)_(R_d,L)=2a_L a_R g X+a_L a_R delta I,          (17)

with endpoint-diagonal contributions cancelling as before. Thus a generic arm imbalance introduces an identity component alongside X. This is an exact counterexample to unqualified exact-gate robustness, not a claim about every possible compensating perturbation.

Second, unequal left-arm or right-arm bond weights need not cancel the order-two transfer: its scalar coefficient is a_(L,u)a_(u,R)-a_(L,v)a_(v,R). When nonzero it precedes the desired gate transition. Third, unequal coefficients g_u and g_v in g_u n_u(I+X),g_v n_v(I-X) give B/C diagonal data part(g_u-g_v)X/2 and central scalar part(g_u-g_v)I/2. These are absent only when the stated equality holds or some separately proved compensation is supplied. Rail-dependent scalar detunings can similarly be conjugated into data/rail-dependent diagonal terms by a noncommuting prefix.

These observations preserve the actual supply gap: the exact result assumes symmetric arms, paired contact coefficients, identical scalar lanes and fixed Hadamard/permutation ratios. It does not derive a calibration, error-correction, fabrication, disorder-tolerance or dynamical symmetry-enforcement mechanism.

## 8. Separate absolute finite-time perturbation bound

This optional extension concerns a FINITE installation and does not preserve exact identities(10),(14). Let H be a member of the structured family and let H_tilde=H+sum_b E_b. Each E_b is a self-adjoint change on one of the same listed one-/two-qubit supports. Require local head-number conservation and annihilation of the local head vacuum for EVERY value of its data factor. The perturbed blocks may be assumed positive if a positive installation is wanted; small full-norm error alone does not guarantee that condition because the nominal blocks have zero eigenvalues. No data-only perturbation is allowed. E_b need not commute with P,Q or X_R, and the bound does not rely on those symmetries or on entrywise reality.

For each physical head i define

    kappa_i=sum_(b whose support contains head i)||E_b||,
    kappa=max_i kappa_i.                                (18)

On the one-head Hilbert space, a head-data/onsite change contributes only a diagonal head-coordinate block with norm<=||E_b||. A two-head change contributes a2x2 head-coordinate matrix with each operator entry norm<=||E_b||; it is zero when the head is elsewhere. Hence the sum of norms in any block row is<=2kappa. Self-adjointness gives the same block-column ceiling. The operator-valued Schur estimate, obtained by bounding the quadratic form with the scalar matrix of block norms, yields

    ||H_tilde_one-H_one||<=2kappa.                      (19)

There is no factor counting all heads or data-neighbor degree. The vacuum-annihilation assumption is what prevents a shared-data perturbation from acting in every head sector. A merely small nonscalar vacuum block would invalidate this local row proof.

For the fixed graph with at most one extra onsite block per head as counted above, a physical head meets at most FOUR listed blocks: two arm bonds plus contact/onsite, or two mixer bonds plus cable/onsite, or the smaller permutation/ordinary variants. The compensated finite source also fits this ceiling. Thus if ||E_b||<=delta for every listed block,

    kappa<=4delta, ||H_tilde_one-H_one||<=8delta.         (20)

Duhamel for exact unitaries then gives, for0<=t<=T,

    ||exp(-itH_tilde)E_seed-exp(-itH)E_seed||<=8delta T.  (21)

This is a complete-vector bound with arbitrary passive references. The unhalved complete-output channel discrepancy is<=16delta T. Any fixed output/record projection contracts the vector bound, so its UNNORMALIZED branch differs by<=8delta T and its subnormalized CP map by<=16delta T. To reserve vector error epsilon_abs on this finite horizon, delta<=epsilon_abs/(8T) is sufficient. There is no claim that a nonzero delta yields a small error uniformly for all time.

Cap bookkeeping is also separate: a physical head's incident load increases by at most4delta, while Q/P have20 contact blocks each and R has8. Thus a nominal installation with cap<=Lambda-20delta remains within Lambda after these changes (assuming that positive perturbed blocks and delta<Lambda/20 are independently supplied). For parameter errors of fixed operator form, the norm changes are2|Delta a| for Q bonds,2|Delta g| for a contact, and|Delta p| for an onsite block. Errors changing the target axis or matrix entries must use the full operator norm in(18), not just a scalar coefficient difference. Correlated changes that stay INSIDE the exact structured family instead obey(10) with their new h_str and need no gate-error Duhamel charge relative to that new scalar comparator.

Finally suppose the ideal structured event has probability p(t)>0. Let eta_t=8delta t. For a normalized purified input, if eta_t<sqrt(p), the actual event is nonzero and the normalized branch-vector distance from its ideal factorized branch is at most2eta_t/sqrt(p). This follows by applying the triangle inequality to a/||a|| and b/||b|| with ||a-b||<=eta_t and ||b||=sqrt(p). Its trace-norm consequence is at most4eta_t/sqrt(p). Event probabilities differ by at most2eta_t because both branch vectors have norm<=1. The perturbed event probability need no longer be input independent, and a normalized postselection is not a linear channel in general. No uniform rare-conditional accuracy follows as p tends to zero; at p=0 no ideal conditional state exists. This separates the exact structured rare-event theorem from a finite-horizon absolute robustness estimate.

## 9. Source identities, exposure and review limits

N is /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- `exact_two_body_direct_loader_composition/PROPOSAL.md`:f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946. Complete source reread for this task. Its distinct global review is pending at this freeze. The present family and record specialization are conditional on that exact graph/word/arm identity; the changed scalar matrix is derived explicitly above. No finite performance claim is adopted.
- `exact_two_body_gate_diamond/PROPOSAL.md`:7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33; accepted checkda5cbc9bcb0f66442da600191c4b863ed7c22a5a4bba0d024a0c683cf71b1945 in its sibling `_check/REVIEW.md`. The immediately preceding full reads are reused. Its symmetry-breaking arm example is retained and generalized in(17), rather than suppressed.
- `exact_two_body_gate_matched_extension/PROPOSAL.md`:a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e; accepted check36a1f3585c9ddde455078c72e7f48dc2b2cd8bfd1165026f4d3f60c6dbc6c77f. Both complete reads from the preceding task are reused; the corrected single scalar-phase convention is maintained. Its uniform matching is only a special case here.

ROOT suggested investigating layer-dependent symmetric arms, paired contacts and scalar mixers/cables and mentioned an optional local perturbation bound. The author shares the global composition and older source/gauge ancestry. This is exposed same-model author work, not independent validation or a native supply derivation. Required distinct checks are the nonuniform diagonal/contact algebra, common-lane assumptions at mixed prefixes, unchanged actual R1 projection, all-head versus one-head distinctions, counts/cap and the local support lemma behind(19). The sufficient symmetry family is not asserted maximal.

Only this PROPOSAL.md was written. No scientific executable, solver, simulation, sweep, delegation, W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. The note proves no useful success probability, finite resource exponent, all-time open-neighborhood robustness, physical preparation, cooling, capture/reset, permanent halt or active old-processor interface. No editable prompt changed.
