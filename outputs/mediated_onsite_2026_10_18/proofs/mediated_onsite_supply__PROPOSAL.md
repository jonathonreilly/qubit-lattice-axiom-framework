# Onsite supply in the positive-bond mediator implementation

Status: new conditional analytical interface requiring a distinct check. The exact phase-covariance statements and finite-matching perturbation bounds below are proved within the supplied one-head apparatus. A chiral/common-carrier constraint is a proposed physical supply requirement, not a derived native protection mechanism. The scalar sensitivity example concerns a specified resolvent observable; it is not a complete-output failure theorem or a universal precision lower bound.

## 1. What the positive blocks actually protect

For each finite new edge use P_w=w[I-(XX+YY)/2], with positive scalar w. The checked full-space identity is

    H_P(w)=H_base+sum_(v in N) 2j n_v-sum_newedges w_e X_e+C(w)I,
    C(w)=sum_newedges w_e.

Here N consists of all 10m-1 added heads, including the three source vertices and mediator interiors, excluding the old port p. H_base retains its original port cap. There is NO additional 2j n_p. This is the positive-P implementation; replacing the original port cap a second time or adding another port occupation changes the apparatus. Scalar bond errors change the adjacency and the known full-space scalar C(w), but not its centered diagonal. The old internal operator, literal old-energy shifts, record sectors and source reference planes remain as in the checked construction.

Now allow independently supplied occupation errors V_N=sum_(v in N) d_v n_v. They are not canceled by the P identity. If 2j+d_v remains nonnegative, their realization still uses nonnegative occupation blocks; a negative d_v denotes a reduction of an existing positive coefficient, not a required negative block. This observation establishes realizability of the stated error model, not a native coefficient supplier.

There are three different meanings of a common shift.

* Adding delta I to the FULL operator changes only exp(-it delta), including the vacuum. Spectral windows shift by delta.
* Adding delta times the total head number changes only exp(-it delta) on the invariant ONE-head sector. On a finite apparatus this is a full operator statement with vacuum phase zero and multihead phase exp(-it delta N). For an infinite apparatus the assertion here is restricted to its one-head space. The shift must cover the old processor and the entire receiver as well as the new heads.
* Adding delta sum_(v in N) n_v shifts only the added region. It is not identity on the physical one-head space and cannot be incorporated into C(w). The background resolvent remains G(E), whereas the finite new-region pencil changes from E-A to E-A-delta I. Even a perfectly common new-region supplier therefore leaves a relative source/background detuning.

The second possibility is a covariance of a modified whole apparatus, not permission to change the original processor while claiming it unchanged. A fixed nominal complex target must include the actual common phase. Substitution of a nominal scalar for an actual scalar costs exactly 2|sin(t delta/2)| in vector norm for unit targets; global-phase-insensitive observables are a different metric.

## 2. A sufficient symmetry constraint, and its missing physical premise

For an isolated bipartite mediator let Gamma alternate signs between its two sublattices. Arbitrary real positive bond errors preserve Gamma A Gamma=-A for the carrier-subtracted adjacency A. If a supplied cell Hamiltonian satisfies this anticommutation exactly after subtraction of a common carrier, its diagonal is exactly zero in that site basis. The even gapped chain consequently retains zero bandcenter diagonal selfenergy and the checked product expression for its offdiagonal coupling, including unequal left/right slope sums under independent bond errors.

Thus an exact common carrier shared with the original background, together with exact centered chiral structure of the added paths, is a sufficient stationary protection constraint. The positive blocks preserve that constraint under their allowed scalar coefficient errors. This is an algebraic implication, not an implementation of the constraint. A cell with chiral center mu has its cancellation at E=mu; it does not acquire the original background center 2j by naming the symmetry. No global chiral symmetry of the old processor is asserted.

Head-number conservation does not exclude d_v n_v. Reflection or a common supplier within the added region can make all d_v equal without making the third case in section 1 harmless. The P construction removes hopping-dependent compensation control, but leaves a carrier-matching/diagonal-supply obligation. No claim is made that other encodings, calibration schemes or physical symmetries cannot meet it.

## 3. An actual full-matching sufficient tolerance interface

Fix a finite admissible tuple w, either the exact nominal tuple or a bond-perturbed tuple whose full matching and comparison bounds are already certified. Work after subtracting its actual C(w). Retain the SAME two physical windows I_b=c_att+2j+b+[-rho,rho], b=1,3. Put xi=max_v |d_v| and retain the entire finite new-head fiber, including all complementary channels. On each lip define

    S_0(E)=E-A_w-w_p^2 J G(E) J*,
    K_0=S_0^-1, u_0=K_0 V_seed, z_0=-w_p J* u_0.

J injects the full port fiber at the last new vertex. The sign is fixed by the negative physical hopping. The perturbed matrix is EXACTLY

    S_d=S_0-D_N,  ||D_N||<=xi,
    u_d-u_0=K_d D_N u_0, z_d-z_0=-w_p J*(u_d-u_0).

No commutation with G or selected-channel replacement has been used. Choose finite uniform bounds k_*>=sup ||K_0|| and u_*>=sup ||K_0 V_seed|| over both windows, both lips and all conserved sectors. Under the sufficient gate xi k_*<1,

    e_N=k_* xi u_* /(1-xi k_*),  e_z=w_p e_N.                 (1)

The inherited finite analytic background matching, local root branches and this strict gate imply local continuation of the perturbed finite inverse on a compact cover of the windows. The seed measure there, including endpoints, is absolutely continuous. A real-axis value envelope alone would not establish this regularity. No spectral type or absence of atoms outside the windows is assumed.

Using the unchanged full background recovery L0=14000 and physical outgoing row bound 461 gives the retained evolution difference

    B_d=(4rho/pi)(e_N+14000 e_z)
                           +4*461 sqrt(2j rho/pi) e_z.       (2)

The first term includes all added source/mediator heads and all finite background heads and closed tails. Its factor counts both windows and both Stone lips. The second term counts both outgoing and incoming physical coefficients with the exact j/pi flux conversion, adding the two windows conservatively. The incoming coefficient uses the real physical Stone conjugation at the same time, not a conjugated programmed target. Window-dependent output decompositions are embedded in fixed physical spaces before taking norms. Thus (2) is a full prepared-input retained-state bound, valid with passive references, rather than a selected resolvent estimate.

The constants are explicitly defined finite inverse quantities, not numerical estimates newly supplied here. This proves a nonzero sufficient onsite tolerance at each fixed strictly admissible finite tuple, but does not prove a useful tolerance or a length-uniform tolerance. In particular, a norm gate involving the full resonant inverse can be very restrictive.

## 4. Actual outside state, paid once

For the fixed unperturbed tuple w, use its checked first-cell trial vector

    Y=V_seed-gamma_L A_cell^-1 C_L iota,
    Y*Y=(1+c_L)I, c_L=gamma_L^2 ||A_cell^-1 C_L||^2,
    X=Y/sqrt(1+c_L).

Its residual at each literal prepared old energy has norm |t_1|/sqrt(1+c_L), where t_1 is the exact first-cell zero-energy cofactor. This uses the actual possibly unequal endpoint bonds of w. The original first-cell gap is required to construct Y; Y need not be an eigenvector or zero-energy dressing for the onsite-perturbed cell.

Since X is supported on N and is isometric, adding D_N increases the residual by at most xi. The original product-seed distance and two-window spectral inequality therefore give

    o_d=min{1, sqrt(2[1-1/sqrt(1+c_L)])
             +(sqrt(2)/rho)(|t_1|/sqrt(1+c_L)+xi)}.           (3)

This bounds the FULL actual prepared-input amplitude outside the original union, including any atoms. It is not an emitter compression bound. The sqrt(2) accounts conservatively for the two old-energy inputs; internal/parity copies and passive references are retained. The bounded perturbation is scalar on internal fibers, so literal old-energy labels in this trial argument are unchanged.

Let b_0(t) be the checked nominal RETAINED-window-to-normalized-target allowance, with its nominal outside allowance removed at the explicit synthesis level. If w is nominal, the resulting complete conditional bound is

    ||exp(-it H_P(w,d))V_seed-exp(-it C(w))T_0(t)||
                                <=o_d+B_d+b_0(t).           (4)

If w already has a checked retained bond-error allowance B_bond to that same nominal packet, add B_bond on the right. Do not also add the old outside allowance o(w); (3) replaces it. T_0 retains its original phase, old aging, programmed unitary, receiver packet and one physical-halfline normalization. Equations (1)-(4) do not change lambda, fit the target to d, or import an old nominal temporal theorem as actual perturbed dynamics. They compose only where the stated nominal scalar normalization and b_0(t) are certified. No new time, receiver length or performance point is asserted.

## 5. An exact, limited linewidth-sensitivity benchmark

The following calculation isolates why absolute onsite size and relative bond accuracy are different questions. It is for the supplied critical three-source scalar reference with its exact semi-infinite j lead, not a claimed replacement for the mediated full inverse.

At its bandcenter, the physical lead Weyl value is -i/j. With a1=lambda/sqrt(3), a2=sqrt(8/3)lambda and kappa^2=3j lambda, the exact retarded source pencil is

    S(0)=[[0,a1,0],[a1,0,a2],[0,a2,3i lambda]].

Its determinant is -i lambda^3, and its 00 cofactor is -(8/3)lambda^2. Consequently r_0(0)=-8i/(3lambda). Add a real occupation v only at source0. Exact rank-one inverse subtraction gives

    r_v=r_0/(1-v r_0),
    [-Im r_v(0)]/[-Im r_0(0)]=1/[1+(8v/(3lambda))^2].       (5)

For this specified center-density observable, retaining a fraction at least 1-eta is equivalent to

    |v| <= (3lambda/8) sqrt(eta/(1-eta)),  0<eta<1.          (6)

For example v=lambda gives the exact fraction 9/73. This uses the exact finite-band Weyl value at center, not a Markov or infinite-band approximation. It demonstrates sensitivity in a declared model/observable; it does NOT prove a required accuracy for every complete-output certificate, an actual mediated output failure, or a universal obstruction to onsite protection. For the mediated apparatus, sections 3-4 instead use its entire physical matching and keep all outputs.

## 6. Scope, exposure and source identities

The proved bridge is conditional on the exact inherited background, scalar occupation errors on the added heads, the finite inverse gate, analytic matching and the original one-head preparation. Errors on the old background require new matching bounds; nonscalar internal/block-shape errors need a separately specified model. Neither native P blocks nor exact/accurate occupations are derived. An exact common-carrier/chiral supply is a candidate physical constraint; a mechanism enforcing it remains open. No negative general theorem is offered.

I authored the positive-bond and stationary precision ancestry and several scalar/complete components, and previously checked loaded, regularity and publication interfaces. This is new author work with that exposure, not independent confirmation of my own ancestors. Root posed the onsite-supply question without supplying an accepted conclusion. Distinct checking of this bridge remains necessary.

Exact source identities (paths relative to the renewal directory):

- mediated_positive_bond_precision/PROPOSAL.md: 8cadb35ee3c41e02b984906030297c2e1a5d5daf5a576ef0e2dfb4531f3da616; check REVIEW.md: 65719cf16109c9cc397890ebcffbf592979a09299a872f9c26ed213b7fad23e0.
- mediated_nonuniform_complete/PROPOSAL.md: b06b088a789ad3230f32c8d4c30dab804b97f82af05b0d0c00f011111e868570; check: 8d6d452445b2e7e69be4294a57cc52e3189e22c30166594281bf7d1f3a36dd7e.
- mediated_loaded_inverse_interface/PROPOSAL.md: 5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22; scoped check f6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3.
- mediated_finite_point_candidate/PROPOSAL.md: 243c172226f2a509ce9ba11686763ebc2e754f52a8b5a4e98d6ab4424c0ca20d; baseline context only, no new point evaluated.
- mediated_bond_error_dynamics/PROPOSAL.md: 594461345ee6546318179e1ef649dcbeac9ea64a1b8f5cd7907c40ee5c7640ac; check 462c76bd07091ce7a18c5efc6bbe89911271583368c9081c5f510cda68211ba9. Its full finite-matching, Stone/flux and trial-vector argument supplies the precise adapter reconstructed in sections 3-4.
- mediated_seed_regularity/PROPOSAL.md: f8153ddb6a86a58e04e9d69a1ef98d13feefe8f0171ba3cbb3e98cf35ae4522b; scoped check 9d837417cc295e6d96fcaf1c8db5aad508d618f90cd57bcb9d560bb70640ea6d.
- three_site_product_source/PROPOSAL.md: a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823; only its exact critical scalar conventions enter section 5.

The positive implementation and full coarse matching proof were refreshed completely; the unchanged nonuniform/loaded/baseline arguments and checks were fully read in preceding coherent tasks and reused at their exact scope, with key source hashes refreshed. No numerical solver, sweep, scientific runner, new hardware point, canonical/W/Git/PR/checkpoint/prompt/model edit or delegation occurred. Only this proposal was written.
