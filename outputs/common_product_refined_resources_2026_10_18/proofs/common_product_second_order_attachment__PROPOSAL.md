# A second-order non-isometric comparison map for the finite router

ROOT-authored candidate requiring a distinct check. This uses the exact supplied finite Hamiltonian of composition3a195efc (published in PR9700), on its total-one-head domain with legal program sectors. It is not a generic transfer to other processors, multi-head domains or arbitrary attachments. The purpose is to improve the accumulated microscopic-cell error from order s eta to order s eta^2 without preparing a dressed input. All outputs, actual phase and time are retained. No spectral gap theorem, asymptotic series or numerical evidence is assumed.

## Exact block decomposition

In one fixed legal program p, after subtracting the physical common scalar2b, separate the logical one-head space L (all finite head sites except mediator m) and the one-dimensional mediator space Q. The exact physical matrix is

    h = [[A,B],[B*,D]],
    B=-b(|u>+|v>), D=D_p,
    A=K+a_p(|u><u|+|v><v|), a_0=2j, a_1=0,
    j=b^2/D0, D1>D0>2b.

Here K is exactly the two finite positive port sums of composition equation1, zero on the mediator. Its endpoint diagonal is j and its one-head norm is <=4j. No component of K acts on program qubits. The literal injection is Jx=(x,0). Define the bounded self-adjoint logical matrix

    hbar=A-BB*/D.

For p=0 this equals h_F,0=K+Q_j(u,v), exactly. For p=1 it is K-(b^2/D1)(|u>+|v>)(<u|+<v|). Thus

    ||hbar-h_F,p|| <= 2b^2/D1 = 2j zeta,
    zeta=D0/D1,

uniformly in p, with zero difference in p=0. Moreover ||hbar||<=4j in both sectors. To check this sharper bound directly: in p=0 it is the known finite router. In p=1 the two central endpoint diagonals are j-j zeta>0, their cross-port hopping is -j zeta, and their radial hopping is -j, giving absolute row sum2j. Every other row is the unchanged finite port row with sum<=4j. The same column bound holds. Positivity of hbar is not required; its self-adjointness is.

The actual full positive microscopic Hamiltonian remains unchanged. All block bounds here are restricted to one head; there is no implicit full-Fock norm claim.

## An exact polynomial intertwining residual

Define a bounded map T:L->L directsum Q by

    Tx=(x,Xx),
    X= -B*/D -B* hbar/D^2.

T is NOT an isometry and is never an actual preparation or physical map. This causes no problem for the following rectangular Duhamel identity: h and hbar are self-adjoint, and multiplication on both sides of a bounded residual by their unitary propagators preserves the operator-norm estimate. The target is still the literal J, which is an isometry.

Direct multiplication, with all orders retained, gives

    hT-T hbar = [ -BB* hbar/D^2 ; B* hbar^2/D^2 ].       (1)

Indeed the top block is A+BX-hbar=-BB* hbar/D^2 because A-BB*/D=hbar. The bottom block is B*+DX-X hbar=B* hbar^2/D^2. No commutativity of B, K or hbar has been invoked.

With eta=b/D0, ||B||=sqrt(2)b, D>=D0 and ||hbar||<=4j,

    ||T-J||=||X|| <= sqrt(2) eta (1+4eta^2),
    ||hT-T hbar||
       <= (||B||^2 ||hbar||+||B|| ||hbar||^2)/D^2
       <= j(8eta^2+16sqrt(2)eta^3).                      (2)

For the last term use j/D0=eta^2, so b j/D0^2=eta^3. The two residual blocks have orthogonal ranges, but their sum bound suffices. These are finite uniform bounds independent of M, not neglected higher-order terms.

For every t>=0, rectangular Duhamel and the two replacements T<->J give

    ||exp(-ith)J-J exp(-it hbar)||
       <=2sqrt(2)eta(1+4eta^2)
                    +jt(8eta^2+16sqrt(2)eta^3).           (3)

No factor ||T|| is missing: Duhamel bounds the difference exp(-ith)T-T exp(-it hbar) directly by t||hT-T hbar||, and the two endpoint replacements use ||T-J||. Both propagators are unitary even though T is not isometric.

Ordinary Duhamel between hbar and h_F,p gives an additional 2jt zeta. The two target maps exp(-ith)J and J exp(-it h_F,p) are isometries, so the final comparison may be capped by2. Taking the direct sum over legal program sectors, reinstating the common scalar and tensoring any passive reference gives

    ||exp(-it H_phys)J-exp(-i2bt)J exp(-it h_F)||
       <= e_cell_second(t)
       := min{2,2sqrt(2)eta(1+4eta^2)
                         +jt(8eta^2+16sqrt(2)eta^3+2zeta)}. (4)

The program-dependent T is solely a proof map. The actual literal J is common to both programs, and no program-dependent preparation is introduced. The distance to the literal target charges the mediator output, including its coherence with every logical site.

## Use in the already checked finite-seed composition

The ideal finite router h_F, its initial emitter seed, normalization, source packet, early-time comparison, boundary-return budget and final encoded output target are identical to composition3a195efc. Only its whole-time physical-cell replacement estimate is changed. Therefore, conditional on (1)-(4) surviving distinct checking, replace e_cell(tf) by e_cell_second(tf) in composition equation15. For the uniform interval1ea1943e, use e_cell_second(tplus); its uncapped expression is nondecreasing in t and the cap preserves monotonicity. Every other term, fixed phase and premise stays exactly the same. The time is the entire duration from the original endpoint seed, not tf-t0.

This is a stronger available sufficient certificate in a suitable parameter range, not a claim that its envelope is smaller than the earlier envelope for all parameters. The earlier exact kappa endpoint estimate can be smaller at short times. One may take the minimum of the independently valid whole-time cell bounds after this one is checked; no improvement of actual physical error is proved solely from comparing envelopes.

## Consequence to investigate, not yet a resource theorem

At eta<=1/8, the elementary bounds 2sqrt(2)(1+4eta^2)<3.01 and 8+16sqrt(2)eta<11 give the conservative sufficient envelope

    e_cell_second(t) <= min{2,4eta+11s eta^2+2s zeta}, s=jt.

This suggests choosing eta of order sqrt(epsilon/s) while keeping zeta of order epsilon/s, subject also to eta=O(epsilon) for the initial mismatch. With D1=Lambda/2, D0=zeta D1 and b=eta D0, the unchanged positive construction has j=Lambda eta^2 zeta/2. A complete explicit combined scaling family still has to check all launch/packet errors and small-parameter conditions; no runtime exponent is asserted here. The incident-cap domain from the existing theorem remains eta<=1/8, zeta<1/2, and no new physical block has been installed.

## Sources and verification limits

Exact premises already fully ROOT-read:
- common_product_finite_seed_router/PROPOSAL.md SHA3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b, and distinct check5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9.
- common_product_finite_window/PROPOSAL.md SHA1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b, and distinct check1337df4d94e3d6b555a88167945e5e8490e9df978b1fbc3e140db17622e36cbb.
- microscopic positive cell739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088; the exact one-head block decomposition is restated here, not inferred from a favorable review summary.

ROOT proposed and authored the polynomial comparison map and all new algebra. A distinct check must reconstruct the exact block orders, residual, operator bounds, isometry endpoint cap, coherent program/reference extension and actual finite K scope. No scientific executable, numerical simulation, symbolic solver, formal audit, native-law derivation, permanent halt, capture/reset or old processor transfer is claimed. No editable prompts, axioms, canonical files or Git were changed by this derivation.
