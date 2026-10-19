# Three mediated bonds: an exact bandcenter critical-ratio interface

Status: new conditional stationary author construction requiring distinct checking. The port-cap replacement below corrects the earlier literal double-addition; that correction requires a scoped recheck. Three fixed-coefficient bipartite mediator paths can reproduce the nominal critical coupling ratios at bandcenter along an integer-length family. Their finite-energy Schur operator is not the old constant-coefficient source. No tolerance, prepared-state or complete-output theorem is transferred.

## Supplied coefficients and integer lengths

Here J denotes the newly supplied mediator strong bond, not the calibrated old-processor J. Use the checked mediator convention: internal strong bonds J>0, weak bonds 0<q<J, negative real hoppings, and gamma_l at BOTH ends of mediator l. All internal one-head diagonals are the same 2j as the four retained endpoints s0,s1,s2,p. Supply fixed positive coefficients satisfying

    gamma2/gamma1=8^(1/4),
    gamma3^4=3sqrt(3) j J gamma1^2.                    (1)

These are length-independent algebraic coefficient correlations. They are premises, not consequences of integer length or native physics. Put r=q/J and a=J-q. For integer m>=1 choose

    n1=n2=2m-1, n3=m,

where mediator l has 2n_l internal sites. Mediate s0--s1, s1--s2 and s2--p respectively, using disjoint internal paths and no additional contacts. Their internal Schur blocks are invertible for |z|<a, with z=E-2j in a scalar sector.

At bandcenter the three induced off-diagonal entries in the PHYSICAL endpoint basis are

    t1=gamma1^2/J * r^(2m-2)>0,
    t2=gamma2^2/J * r^(2m-2)>0,
    t3=(-1)^(m-1) gamma3^2/J * r^(m-1).              (2)

Define lambda_m=sqrt(3)gamma1^2/J * r^(2m-2). Direct algebra gives

    |t1|=lambda_m/sqrt(3),
    |t2|=lambda_m sqrt(8/3),
    |t3|^2=3j lambda_m.                              (3)

Indeed gamma2^2/gamma1^2=sqrt(8), and (1) makes gamma3^4/J^2=3sqrt(3)j gamma1^2/J. The exponent in |t3|^2 is 2m-2, exactly matching t1. No coefficient is varied with m. This supplies only a geometrically spaced lambda_m family, not arbitrary continuous source tuning or an arbitrary prescribed lambda.

## Endpoint signs and seed phase with the port fixed

The positive entries t1,t2 are not already the canonical negative hoppings. Fix the physical port phase to +1 and define endpoint signs

    g_p=1, g_s2=(-1)^m, g_s1=(-1)^(m+1), g_s0=(-1)^m.

Let G_end be this diagonal sign matrix, with identity on old-background coordinates. The transformed endpoint Hamiltonian G_end H_eff G_end has all three bandcenter off-diagonal entries -|t_l|. This follows successively from g_s2 sign(t3)=-1, g_s1 g_s2=-1 and g_s0 g_s1=-1. The transformation does not alter B or onsite terms.

For a canonical seed convention, physical |s0> equals (-1)^m times its canonically signed basis vector. Because the port and downstream basis were fixed, a later physical output comparison must retain this seed-to-port sign (-1)^m. It cannot simply declare the mediated path identical to the old negative-hop source with unchanged global phase. Restricting to even m makes the seed sign +1 but samples every other family member, changing lambda by r^4 between successive allowed even m. Either choice is a supplied family convention, not a phase fit.

A full coordinate gauge can extend G_end by identity on every mediator internal site. It then changes the signs of some endpoint-to-mediator matrix elements in the REPRESENTATION; the physical implemented bonds remain negative Q bonds. Alternatively one can propagate a gauge along each path. One cannot simultaneously insist on unchanged physical negative internal matrix entries and treat endpoint signs as nonexistent. Since the installation is a path, there is no cycle-frustration obstruction; all endpoint/reference-plane signs still matter for a phase-sensitive target.

## Positive full-qubit realization and original port compression

Use Q_b(i,k)=b(n_i+n_k-X_ik) on each of the mediator paths, with internal strong/weak magnitudes J,q and endpoint magnitude gamma_l. The checked emitter-free background H_bg already includes the retained positive port cap j n_p from principal compression of the removed source. Remove that existing cap before installing this path, keeping the original input bond and every other background block. The uncapped base H_bg-j n_p means omission of that positive block, not a negative implemented interaction. Extend shared B and the original scalar once. Add to this uncapped base the path bonds and occupations

    (2j-gamma1)n_s0,
    (2j-gamma1-gamma2)n_s1,
    (2j-gamma2-gamma3)n_s2,
    (j-gamma3)n_p,

and on each mediator site i add (2j-sum_incident b)n_i. Thus every new source/mediator diagonal is 2j. The new port contribution is exactly j n_p, replacing the omitted cap. Together with the unchanged input bond contribution j n_p, its full port diagonal is exactly 2j. Literal addition of these terms to the already capped H_bg would instead give 3j and is not the construction. No vacuum scalar is added by these occupation/Q blocks; the original c_att and the one-head 2j carrier remain.

Sufficient positive-coefficient conditions are

    J+q<=2j, J+gamma_l<=2j for all l,
    gamma3<=j, gamma1+gamma2<=2j, gamma2+gamma3<=2j.

They are compatible with (1): choose supplied 0<q<J<2j with J+q<2j, and then a sufficiently small positive gamma1. Equation (1) fixes gamma2 proportional to gamma1 and gamma3 proportional to sqrt(gamma1); both tend to zero. One may additionally require gamma_l<=a/4 to meet the isolated single-cell dressing premise, although that alone does NOT prove a dressing theorem for the assembled apparatus.

Compression off ALL new source and mediator heads retains exactly j n_p from the added chain-3 endpoint bond plus its port occupation. Thus compression of the corrected installation (H_bg-j n_p)+H_path restores exactly H_bg. The old cap is not counted twice. This is a full-space occupation bookkeeping identity, not a claim that eliminating ONLY mediator heads leaves the old source Hamiltonian: that Schur operation adds finite-energy diagonal terms, including a term at p.

A physical embedding must supply disjoint paths of the stated lengths without unintended contacts. It generally changes source positions and adds sites; the old three coordinates cannot be silently held fixed while inserting arbitrarily many nearest-neighbor sites between them. A straight longer path can realize the abstract chain, with p fixed and the source endpoints placed at its appropriate distances, provided the ambient lattice is available and interaction selection is supplied.

There are 2(n1+n2+n3)=10m-4 mediator sites, four retained local endpoints and 10m-1 local head edges. Thus this local path has 10m heads and at most20m-1 listed positive blocks if all 10m occupations (including p's added occupation) are separately counted. These are local construction counts. External geometry, old qubits and new total apparatus counts require a concrete embedding; no resource saving is claimed.

## Exact finite-energy endpoint Schur functions

For mediator l let A_l be its 2n_l internal positive-weight adjacency and C_l select its two internal ends. The exact two-end self-energy is

    Sigma_l(z)=gamma_l^2 C_l^T(zI+A_l)^-1 C_l
              =s_l(z)I+t_l(z)X.

Its physical sign is inherited from two negative endpoint hoppings. Reflection makes the diagonal entries equal; bipartite symmetry makes s_l odd and t_l even. At zero,

    s_l(0)=0,
    t_l(0)=(-1)^(n_l-1)gamma_l^2 q^(n_l-1)/J^n_l.

Let the positive singular values of JI+qS_l be sigma_l,r, r=1,...,n_l, each at least a. The endpoint cofactor is independent of z, so the exact off-diagonal rational function is

    t_l(z)=t_l(0) / product_(r=1)^n_l (1-z^2/sigma_l,r^2). (4)

This identity follows by dividing the determinant of zI+A_l by det A_l; the eigenvalues pair as +-sigma_l,r. It also checks the parity and signs of (2). For real |z|<a the denominator is positive. Therefore the fixed endpoint gauges above make every finite-band induced hopping negative too, although its magnitude is energy dependent.

The diagonal Taylor coefficient is

    s_l'(0)=-gamma_l^2 d_nl,
    d_nl=J^-2 sum_(r=0)^(n_l-1)(q/J)^(2r).

For complex |z|<=w<a, resolvent-series estimates give explicit absolute envelopes

    ||Sigma_l(z)-Sigma_l(0)||
                      <=gamma_l^2 |z|/[a(a-w)],
    |s_l(z)|<=gamma_l^2 |z|/[a(a-w)],
    |t_l(z)-t_l(0)|<=gamma_l^2 |z|^2/[a^2(a-w)],
    |s_l(z)+gamma_l^2 d_nl z|
                      <=gamma_l^2 |z|^3/[a^3(a-w)],
    ||Sigma_l'(z)||<=gamma_l^2/(a-w)^2.               (5)

The off-diagonal and diagonal-remainder bounds use the even/odd terms of the series; the looser geometric tails displayed are sufficient. Formula (4) additionally gives the relative bound

    |t_l(z)/t_l(0)-1|
                    <=(1-w^2/a^2)^(-n_l)-1.          (6)

For complex z this follows from the product inverse series with positive majorant coefficients; for real z the exact ratio is at least one. Thus absolute hopping error need not be divided by exponentially small t_l(0) to obtain a bound, but relative finite-band variation can grow with length. Smallness of (6) is an additional bandwidth/length condition, not part of (3).

On the retained endpoint order s0,s1,s2,p, the exact scalar added diagonal after eliminating mediators is

    diag(s1, s1+s2, s2+s3, s3),                        (7)

and the three off-diagonal entries are t1(z),t2(z),t3(z). Other endpoint/background couplings remain unchanged. At z=0 (7) vanishes, and after the fixed signs (3) reproduces the critical nominal endpoint hoppings. At finite z these diagonal terms are proportional to energy to leading order and the hoppings vary with energy. They are NOT constant residual detunings r_i or a fixed relative-error tuple covered by an existing tolerance theorem. In particular the port also has s3(z), which the earlier three-source tolerance box does not allow.

## Shared internal fibers and stationary ordering

If this mediator is embedded in the original internal-fiber setting, the requisite additional premise is that the same shared B occurs once and acts identically while the head occupies every mediator site, with no new source-state-dependent contact. Then set

    D=(E-c_att-2j)I-B.

Each mediator function is Sigma_l(D), a genuine reference function of D. The full endpoint Schur matrix has the additions (7) and t_l(D) in their corresponding blocks. These commute with one another as functions of D, but need not commute with the actual processor background Green function or its self-energy. Further elimination must retain the original matrix order. Replacing the functions by their scalar values on a selected channel is not a full-fiber inverse proof.

On an original selected window D=delta, the bounds (5) apply if the additional condition d<a holds, using w=d. On complementary channels the inherited |x|>.185 and J+q<=2j<.006 place x outside the mediator spectrum, giving

    ||(xI+A_l)^-1||<=1/(|x|-(J+q))<1/.179.

Hence the mediator-elimination blocks have no bare internal poles on those windows, including complements. This does NOT exclude zeros of the resulting loaded endpoint Schur matrix, assembled dressed modes, trapped states or outside seed mass. The elimination is stationary; an attached apparatus can change the spectral problem even when individual mediators are gapped.

At bandcenter only the selected D=0 channel has exact critical source ratios. Complementary functions at D=x are their physical real resolvents, not constants from (3). A stationary endpoint theorem would require the whole loaded matrix, including the new port diagonal and all these complementary functions, to be bounded in order.

## Preparation and remaining bridge

The checked single-mediator isolated theorem bounds dressed-pair preparation when gamma_l<=a/4. It cannot be multiplied across the three paths: adjacent endpoints are shared, and the processor is attached at p. The low subspace, source product seed, physical head distribution and spectral measure of the assembled apparatus must be analyzed separately. This proposal supplies no dressed-source preparation error or omitted-state bound for that apparatus.

In particular the old sixth-moment source-prefix proof cannot be reused: the first head hop from the physical seed is now gamma1 into a mediator, not the effective a1. Bare product preparation may populate high-energy mediator components; their probability must be charged or avoided by a separately justified preparation protocol. Similarly the actual dynamical linewidth and source pulse are not determined solely by the zero-energy Schur ratios. Energy-dependent diagonals encode wavefunction/energy renormalization, even though their constant term is zero.

The exact ratio route therefore succeeds as a bandcenter stationary construction, but the claimed advantage is limited: it avoids a length-dependent endpoint diagonal counterterm at exactly bandcenter. It does not eliminate the supplied equal-onsite relation, ordinary bond/occupation correlations, algebraic gamma ratios, graph installation, sign/reference-plane conventions or internal gap/bandwidth obligations. It neither assembles the old processor theorem automatically nor proves continuous coupling tunability, native suppliers, smaller total resources, irreversible output or permanent halt.

## Exact sources and exposure

- `bipartite_mediator_supply/PROPOSAL.md`: `836caee25d87e31c757e8965b4de85d5998a613dcc5862072d6cddc2a380c8dc`.
- `bipartite_mediator_supply_check/REVIEW.md`: `78af05b19696d2cae2cf147c1e666c9c1a39ca0a2ba9c67a8d1746c12c72de8f`.
- `three_site_actual_attachment/PROPOSAL.md`: `4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006`.
- `three_site_actual_attachment_check/REVIEW.md`: `ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d`.
- `three_site_loaded_inverse/PROPOSAL.md`: `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.
- `three_site_loaded_inverse_check/REVIEW.md`: `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`.

I authored the isolated mediator source and read its full distinct root review before this extension. Root suggested the lengths and algebraic ratios; their exponents and signs were verified directly above rather than assumed. I have shared source/phase/inverse ancestry in this campaign. This is new author work, not independent certification, and requires distinct checks of the shared-endpoint installation, port convention, exact rational functions, sign gauge and limitations. No numerical spectrum, parameter sweep, dynamics, solver, scientific runner, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was written.

Correction provenance: ROOT made only the explicit port-cap replacement, clarified the mediator J symbol, and preserved the previous source as ORIGINAL_2972451d.md after reading the complete distinct stationary review. No finite-energy formula, ratios or claimed performance were changed. The scoped correction is awaiting the reviewer’s recheck.
