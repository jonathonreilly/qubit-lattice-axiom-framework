# Distinct check of the finite-router polynomial comparison map

Disposition: conditional support for the complete source `common_product_second_order_attachment/PROPOSAL.md`, SHA256 `a322e3689a5b58cd56c173d22df93c68199ead8cf04af88cb101af305798468c`. No required mathematical correction found. The exact residual gives the stated full-time literal-map comparison on the specified finite one-head router. This report establishes no new combined runtime exponent and does not transfer the result to arbitrary attachments or multiple heads.

## Exact pins and exposure

The complete new source was read and its SHA256 checked. The following premises were previously read completely in this coherent session and their identities were refreshed for this check:

* Microscopic cell: `mediated_common_product_program/PROPOSAL.md`, `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.
* Finite composition: `common_product_finite_seed_router/PROPOSAL.md`, `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.
* Uniform interval: `common_product_finite_window/PROPOSAL.md`, `1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b`.
* Composition check: `common_product_finite_seed_router_check/REVIEW.md`, `5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9`.
* Interval check: `common_product_finite_window_check/REVIEW.md`, `1337df4d94e3d6b555a88167945e5e8490e9df978b1fbc3e140db17622e36cbb`.

ROOT authored the proposed map and algebra. I did not author this source, but saw the proposed construction before checking it. I previously authored the boundary and interval extensions and conservative scaling certificate and checked the supplied-packet router. Those shared sources and same-model ancestry are explicit exposure; this is a distinct analytical check, not blind or model-diverse replication. The recorded component reviews are reused at their exact scopes, not recertified here. The publication reference in the source was not independently checked and is not a mathematical premise of this report.

## Physical block reconstruction and the logical norm

The microscopic source expansion after subtracting its common scalar 2b is a_p n_u+D_p n_m+a_p n_v minus the two mediator hoppings of coefficient b. In the total-one-head space, all external-head columns have zero cell-relative energy and mediator-vacancy injection. The finite K acts only on logical head sites, vanishes on the mediator column, and has no program dependence. Therefore separating the mediator gives exactly

    h=[[A,B],[B*,D]],
    A=K+a_p(|u><u|+|v><v|),
    B=-b(|u>+|v>), D=D_p,
    Jx=(x,0).

The scalar remains 2b when the head is on an emitter, lead site or cell endpoint; the decomposition does not remove a location-dependent energy. K includes the fixed-diagonal emitter blocks of the finite composition, not the earlier Laplacian-deletion variant.

Let U=|u>+|v>. Then BB*=b^2 UU* has norm 2b^2. In the enabled sector a_0=2j and b^2/D0=j, so

    hbar=K+2j(|u><u|+|v><v|)-jUU*
        =K+j(|u>-|v>)(<u|-<v|)=h_F,0.

In the disabled sector a_1=0, so hbar=K-j zeta UU*, with zeta=D0/D1 in (0,1). The exact disabled target difference has norm 2j zeta, since ||U||^2=2. The uniform bound is consequently zero in the enabled block and 2j zeta in the disabled block; taking their maximum, rather than summing, is correct.

For the disabled hbar, each central endpoint diagonal is j(1-zeta)>0, its radial off-diagonal entry is -j and its cross-port entry is -j zeta. Their absolute row sum is 2j exactly. Every remaining row has the unchanged finite port diagonal and hoppings, with absolute sum at most 4j. The same bound holds for columns because hbar is self-adjoint. The Schur bound proves ||hbar||<=4j. In the enabled sector hbar is the finite positive router and the same row/column bound holds. Positivity is not needed for the disabled hbar; bounded self-adjointness suffices. Finite matrix bounds remain uniform in M because no row gains an M-dependent number of contacts.

## Exact ordered residual

Write X=-B*/D-B*hbar/D^2 and T=(I,X)^T. D is a positive scalar within the fixed program block, so its placement is harmless; there is no reason to commute hbar with B or BB*. Direct multiplication gives

    top(hT-T hbar)=A+BX-hbar
                     =-BB*hbar/D^2,

    bottom(hT-T hbar)=B*+DX-Xhbar
       =B*-B*-B*hbar/D+B*hbar/D+B*hbar^2/D^2
       =B*hbar^2/D^2.

This reconstructs equation (1) with its precise product orders. It is an exact identity, not a truncated expansion with an unbounded remainder. In particular the top block is BB*hbar, not a symmetrization or an expression obtained by commuting BB* through the finite port generator.

Because T-J has only the lower block X, its operator norm is ||X||. Using ||B||=sqrt(2)b, D>=D0 and j/D0=eta^2 gives

    ||T-J||<=sqrt(2)(b/D0)(1+4j/D0)
             =sqrt(2)eta(1+4eta^2).

For the rectangular residual R, the two blocks occupy orthogonal output spaces, so a square-sum bound is possible, but their norm sum is a valid upper bound. It gives

    ||R||<=2b^2(4j)/D0^2+sqrt(2)b(16j^2)/D0^2
           =j(8eta^2+16sqrt(2)eta^3).

The second equality uses b*j/D0^2=eta^3. Thus both powers of eta and the overall physical frequency j in equation (2) are correct. The bounds neither presume K commutes with the cell nor hide a norm proportional to the number of lead sites.

## Rectangular Duhamel and literal endpoints

For any bounded rectangular T and bounded self-adjoint h,hbar, differentiate exp[-i(t-s)h]T exp[-is hbar]. The derivative is i exp[-i(t-s)h](hT-T hbar)exp[-is hbar]. Integrating and reversing the endpoint order gives

    exp(-ith)T-T exp(-it hbar)
       =-i integral_0^t exp[-i(t-s)h] R exp[-is hbar] ds.

Both exterior factors are unitary. Therefore the norm is at most t||R|| without a factor ||T||. There is no isometry assumption in this identity. Replacing T by J at the initial and final ends adds at most 2||T-J||, which proves equation (3).

T is not an isometry: T*T=I+X*X. Accordingly a generic cap 2 would not follow for the T-comparison itself. The source correctly postpones its final cap until the maps are exp(-ith)J and J exp(-it h_F,p). These are isometries, so their difference has norm at most 2. Ordinary unitary Duhamel from hbar to h_F,p adds t||hbar-h_F,p||<=2jt zeta. Combining these statements gives exactly the uncapped expression and cap in equation (4). There is no renormalization of T, which would change the residual and require a separate argument.

The legal program sectors are conserved and mutually orthogonal. Taking their direct sum makes the error norm their maximum. A program-dependent auxiliary T is allowed because the actual initial and final maps use the same literal J in both sectors. Tensoring arbitrary passive references preserves each operator norm. Restoring exp(-i2bt) is necessary and gives the physical comparison at its stated phase. The mediator output, and its coherence with all external head positions, remains in the full output norm.

## Valid use and resource boundary

The comparison is uniform on the entire allowed logical one-head space, so in particular it applies to the source's literal emitter seed map. It charges the entire elapsed t from the initial seed, including launch. The ideal h_F and every normalization, cutoff, early tail, finite boundary and final packet construction are unchanged. Thus replacing only the physical-cell allowance in the pinned composition is valid once this new bound is accepted. For the uniform observation interval, the uncapped expression is nondecreasing in nonnegative t and capping preserves that property, so evaluating it at tplus is sufficient.

The endpoint term remains of order eta and need not improve the earlier exact-kappa endpoint bound. The accumulated term is of order s eta^2 plus s zeta, with s=jt. This establishes an additional sufficient certificate, not smaller actual error or an envelope improvement for every parameter and time. The minimum of independently valid literal-map bounds is legitimate.

For eta<=1/8, 2sqrt(2)(1+4eta^2)<=17sqrt(2)/8<3.01<4 and 8+16sqrt(2)eta<=8+2sqrt(2)<11. Consequently the suggested 4eta+11s eta^2+2s zeta envelope is valid. The source correctly leaves any combined accuracy/resource exponent unproved: a choice eta proportional to sqrt(epsilon/s) must also pay the endpoint requirement eta=O(epsilon), preserve the cap domain and satisfy every ideal error budget. This report supplies no new exponent.

The physical Hamiltonian and all full positive blocks are unchanged, so the existing finite qubit/block/load counts remain applicable at their same parameters. The proof relies on this particular scalar mediator block, its rank-one B, and the explicitly bounded finite K. Multiple heads, non-scalar or interacting mediator sectors, other attachments, or additional program couplings require new block and residual analyses. No native-law identification, supplied-coefficient mechanism, capture/reset, permanent output or old processor transfer follows.

Only this review was created. No scientific program, numerical dynamics, symbolic solver, sweep, upstream source edit, Git/canonical/publication/checkpoint/editable-prompt/model change or delegation occurred. Hashing was source-identity bookkeeping. No formal audit or retained status is assigned.
