# Uniform real jets for the fixed direct-loader scattering network

New bounded author derivation requiring a distinct check. This supplies explicit outgoing derivatives through order three and the COMPLETE internal map through order one for the actual eleven-stage direct loader with every graph cable length one. It acts on the shared eight-dimensional Q,P,R fiber without globally diagonalizing Q or P. It does not prove a normalized physical packet, finite seed matching, a finite resource policy or a runtime exponent.

## 1. Fixed physical object and uniform domain

Use the exact blocks, port order and graph of stationary source89489 and accepted check9818. There are fourteen cores and sixteen writers, including six scalar writers;496 internal heads and three shared data qubits;920 internal positive blocks; eight exterior rays; eighty internal port ends; eleven stages. Set L_s=1 for all ten gaps, so the common ideal phase is z^105. The range21 embedding is only an exact qubit relabeling and changes none of the following matrices.

Let beta be the core hopping, eta=beta/D0, zeta=D0/D1, j=beta^2/D0, and

    z=exp(ik), e(k)=2(1-cos k), E(k)=j e(k).

Assume

    0<eta<=1/8, 0<zeta<1/2,
    |k-pi/2|<=h<=10^-3,
    delta:=max{13eta^2+5zeta,33h}<=1/22.                 (1)

The last inequality is an explicit uniform-margin restriction, stronger than merely11delta<1. It is compatible with the stationary source's arbitrary-accuracy prescription, whose delta<=1/155. No parameter is differentiated with respect to k. Data have no free Hamiltonian or bias. The true common scalar is

    c=112beta+64(sqrt(2)-1)j.

All matrices below use the scalar-subtracted one-head operator; any eventual physical evolution retains exp(-ict). We do not subtract a data-dependent vacuum term.

Let I_sel be ANY k-independent isometry into the external incoming port/data space. It can select the left a=1 channels while retaining the logical path and all Q,P,R values, or additionally restrict R to its supplied blank. Bounds are proved before that restriction and tensor with identity on arbitrary passive references. No unknown target is reset.

## 2. Actual local outgoing inverse, including the core

For any individual module, let H_v/j be its dimensionless relative internal matrix with the attached ordinary lead's diagonal retained at each port. Let E_v include its port coordinates and P_v=E_v E_v*. Define

    M_v=H_v/j-e(k)I-zP_v,
    G_v=M_v^-1,
    L_v=-2i sin(k)G_v E_v,
    S_v=E_v*L_v-I.                                      (2)

The sign follows from psi_1=z psi_0+(z^-1-z)incoming. Origins are components of L_v. These are exact finite matrices, not effective low-energy replacements.

For each writer, the accepted exact two-chain certificate22bca/d96ed gives ||G_v||<10 on this band. Its X_target=+1 scalar specialization is a literal invariant local sector and inherits the same bound. Recombining both sectors and tensoring unused data factors takes a maximum, not a sum. This local decomposition does not assume globally conserved Q,P,R.

For a core, partition M_v into four endpoint and four mediator coordinates. In a local control sector the mediator block has inverse norm

    d_inv<=eta^2/(1-3eta^2),

since e(k)<=3 and D0/j=eta^-2. Its endpoint-mediator incidence norm is2beta/j=2/eta. Hence

    ||D_med^-1 B*||<=2eta/(1-3eta^2)=:a.

The exact endpoint Schur matrix is z^-1 I-I+V_p(E), with V_p real self-adjoint, so its inverse norm is at most1/sin k<=2. The block inverse is the lifted Schur inverse plus the mediator inverse block; therefore

    ||G_v||<=2(1+a)^2+d_inv.

At eta=1/8 this is2(77/61)^2+1/61=11919/3721<4, and the ceiling increases with eta. Both local program sectors satisfy it. This proves a full core inverse bound, including its actual mediator components, uniformly despite large dimensionless detunings. An effective endpoint-only norm would not suffice here.

Choose the common sufficient bound B=11. Parallel modules within each stage form a direct sum on head coordinates over the same data fiber, so their local inverse/internal-map bounds have no multiplicity factor. Every module scattering matrix is unitary on the real band by its exact boundary equation; this supplies zeroth scattering norm1 separately from ||L_v||<=2B.

## 3. Local real derivatives through order three

Only -eI-zP_v depends on k in M_v, so

    ||M_v^(r)||<=3, r=1,2,3.

The exact ordered inverse derivatives give

    ||G_v'||<=3B^2,
    ||G_v''||<=18B^3+3B^2,
    ||G_v'''||<=162B^4+54B^3+3B^2.                    (3)

For example, the third derivative is

    -G M''' G
    +3G M'' G M' G+3G M' G M'' G
    -6G M' G M' G M' G.

The two mixed terms keep their different orders. These identities require no commutativity of matrix derivatives. Multiplying by -2i sin k and differentiating with the actual binomial coefficients yields

    l0=2B=22,
    s1=6B^2+2B=748,
    s2=36B^3+18B^2+2B=50116,
    s3=324B^4+216B^3+42B^2+2B=5036284.                (4)

Thus ||L_v^(r)||<=s_r for r=1,2,3, and the same positive-order bounds hold for S_v. Set the scattering jet

    s=(1,s1,s2,s3).

The subtraction of I contributes no positive derivative. All quantities in(3),(4) are derivatives in dimensionless momentum; no j factors are suppressed from a time derivative.

## 4. Ordered eleven-stage feedback and explicit uniform outgoing jet

Let S_local be the stage direct sum, partitioned into external/internal blocks. Each restricted block has zeroth norm at most1 and positive derivatives bounded by s_r. With L_s=1, cable pairing is P_c=zP_0 for a fixed unitary permutation P_0. Its derivative norms of every order used here equal1. Put

    A=P_c S_ii, B_c=P_c S_ie, C_c=S_ei, D_c=S_ee,
    R=(I-A)^-1,
    S_net=D_c+C_c R B_c.                            (5)

For nonnegative four-entry vectors define

    (u star v)_r=sum_(m=0)^r binomial(r,m)u_m v_(r-m).

This is arithmetic on norm ceilings for an ORDERED product; it does not replace the actual matrix product by commuting factors. It is associative because it records the repeated Leibniz rule. Let

    a=(1,a1,a2,a3)=(1,1,1,1) star s,
    a1=749, a2=51613, a3=5188877.                    (6)

These bounds apply to A and B_c through third order.

The ideal reflectionless internal transition obeys A0^11=0. From the checked stationary margin,

    ||R||<=11/(1-11delta)<=22=:r0.

Differentiating the actual inverse in its order, with (I-A)'=-A', gives the uniform jet

    r1=r0^2 a1,
    r2=2r0^3 a1^2+r0^2 a2,
    r3=6r0^4 a1^3+6r0^3 a1 a2+r0^2 a3,
    r=(r0,r1,r2,r3).                                (7)

For instance R''' contains six R A' R A' R A' R terms in its norm bound, three terms of each ordered A''/A' type, and R A''' R. Formula(7) bounds all of them. This is a real-domain calculation; no analytic continuation of the network or cutoff is assumed.

Define the following fully explicit arithmetic constants:

    N0=1,
    N_r=s_r+(s star r star a)_r, r=1,2,3.             (8)

Here the vector r in the star expression is the jet in(7), not the derivative index. Equations(5)--(7) and Leibniz give ||S_net^(r)||<=N_r. The zeroth value N0=1 uses the accepted full network unitarity: local flux conservation and unitary cable matching cancel internal flux, and the invertible feedback gives a square external isometry. We do not use the much larger triangle bound for its zeroth norm.

For clarity, the first two expressions in(8) are

    N1=s1+s1 r0+r1+r0 a1,
    N2=s2+s2 r0+2s1 r1+2s1 r0 a1+r2+2r1 a1+r0 a2.

The third is fixed without ambiguity by(8), or by

    N3=s3+s3 r0+3s2 r1+3s2 r0 a1
       +3s1 r2+6s1 r1 a1+3s1 r0 a2
       +r3+3r2 a1+3r1 a2+r0 a3.                    (9)

These are parameter-independent finite integers on domain(1), not symbolic unbounded constants or fitted numerical estimates.

The requested demodulated outgoing operator is

    M(k)=exp(-105ik) S_net(k) I_sel.

Its uniform jet is

    M0=1,
    M1=N1+105,
    M2=N2+210N1+11025,
    M3=N3+315N2+33075N1+1157625.                     (10)

No data operator is moved through another to obtain these inequalities. The demodulation removes only the explicitly prescribed common stationary z^105. It does not fit an input-dependent phase or remove the physical scalar c. Because there is no bias, all external channels have momentum k and the same velocity, and M is already the ordinary-amplitude map; no nontrivial flux Jacobian is required. For any fixed output projection, the same jet ceilings apply by contraction.

## 5. Complete internal map through first derivative

Let x=I_sel xi, and y=R B_c x. The vector of all local incoming coefficients is w=(x,y). Its norm and derivative obey

    ||w||<=v0:=1+r0=23,
    ||w'||<=v1:=r1+r0 a1=378994.                    (11)

The local internal maps L_v include every module head, including all port origins. Their stage/module direct sum L_loc has norm at most22 and derivative at most748. Since all forty cables have one edge, there is NO cable-interior head to add. Every one of the496 internal heads belongs to one and only one local module. Consequently the complete internal stationary coefficient is exactly

    T(k)=L_loc(k) [I_ext ; R(k)B_c(k)] I_sel,

where the bracket denotes the external/internal incoming assembly in the fixed stage port ordering. It includes all Q,P,R fibers on each head coordinate, not separate copies of their data states. Its bounds are

    ||T||<=T0:=22*23=506,
    ||T'||<=T1:=748*23+22*378994=8355072.             (12)

External lead sites start at radial n=1, since their n=0 origins are already in T. This avoids origin duplication in any future physical packet. Tensoring a passive reference does not change(10)--(12). These are full coefficient-map bounds, not finite-time occupancy estimates.

For a normalized cutoff spectrum g with G0=||g||_1 and G1=||g'||_1, an immediate product interface is

    ||Tg||_1<=506G0,
    ||(Tg)'||_1<=506G1+8355072G0.                    (13)

This does not assert that g is physically supplied, nor that an integrated stationary field is a normalized state.

## 6. Conditional phase interface to the existing resonant lemmas

The scalar pole and half-line sources retain their exact real quintic, positive p normalization and compatibility hypotheses. They concern g=chi F/sqrt(p), not an arbitrary C2 amplitude. Their operator amplitude hypotheses now accept(10), on domain(1), without an extra target/reference dimension factor. The fixed ideal column has a constant unitary coefficient and may use jet(1,0,0,0). This is a coefficient substitution interface only.

For orientation, let u=jt and hypothetically place a source at M_source=ell+1 so its incoming phase is(ell-n)k-u e(k). If ell>=100*105, the following phase hypotheses are sufficient; their roles do not establish a finite source/cut theorem:

| Field | Scalar phase and gap interface |
|---|---|
| Incoming three cut levels | d k-u e(k), d=0,-1,-2; exactly the incoming4eb53 scalar interface, provided rho^2<=h/16 |
| Early outgoing positive half-line | (n+ell+105)k-u e(k), n>=0, u<=ell/100;43c0 positive-gap criterion has Qgap=ell+105-2u>=.98ell, Cgap=2 |
| Far outgoing half-line | (n+ell+1+ell+105)k-u e(k), n>=0, u<=7ell/8;43c0 criterion Qgap=.99(ell+1)+ell+105-2u>=.24ell, Cgap=16 |
| Late incoming half-line | -n k+ell k-u e(k), n>=0,3ell/4<=u<=7ell/8; a031 has Q=1.98u-ell>=.485ell, Cgap=16 |
| Ideal nonpositive output tail | -n k+(ell+105)k-u e(k), n>=0 in the same late window; Q>=.485ell-105>=.475ell, Cgap=16 |

For outgoing boundary points n=ell,ell+1,ell+2, their k derivative is at leastell/4+105 through u=7ell/8. The positive gap and derivative ceilings used in b262's generic real-axis pole argument remain sufficient with105 in place of57 under ell>=100*105: n<=ell+2, L<=1.01ell, |Phi'|<=4ell and higher k derivatives <=2u. Its generic coefficient formula may therefore be evaluated afresh from(10), with elastic k_a=k; the old biased network B_net is not reused. There is one full external vector rather than two different threshold momenta. Any finite contact norm/integration and row multiplicities must still be supplied for the actual finite installation.

The physical launch reference's unwanted incoming term uses conjugate(g), which has the favorable opposite pole sign. It must not be replaced by g solely because their moduli agree. The late-negative and adverse-sign lemmas retain their exponential remainders. No complete-time norm or resource improvement is inferred from this table.

## 7. Limits, exact sources and exposure

This certificate is uniform only on the explicit margin domain(1). It supplies real derivative bounds and complete internal coefficients for the stationary loader. It does not normalize a physical packet, match a literal endpoint seed, bound localized seed components, install or analyze finite sources/caps, prove an entire-horizon record branch, or allocate a final accuracy/time/length family. Those are separate author/check tasks.

In particular the new loader's entrance is a microscopic core with literal diagonal3j and beta-sized mediator contacts after scalar subtraction. A future comparison to a2j-diagonal standalone launcher must pay those terms. The cat-preparer splitter's order-j contact bound is not a premise here. Receiving data dynamics, a record bias, head-independent old-environment Hamiltonians or longer graph cables require new matrices or constants. Physical range21 alone does not affect these graph-phase formulas.

Necessary pinned premises, fully read in the preceding coherent work and reused at unchanged hashes:

- Direct loader89489c13a6450f142c8ac2212ee680bc7272addcff30c53fcb01e52dff4ee7a9 / accepted review9818c72551eec2d2be17224dde6e07335f1ff7157b94a91c4a372aff3873343d; actual local matrix, graph, scalar and feedback passages refreshed and hashes verified for this task.
- Writer inverse22bca57ebcbfb8cfabebbe044cd5302e784e585b503cee28d6172afc72e54cf0 / separate checkd96ed6b26856490d802ceed2009f75aa9c0919eb8760bcfffe0389807965d1b5. Its complete recent reads are reused for the actual B<10 premise; no certificate executable was rerun.
- Core60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182 /8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d and exact one-control76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 /549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0. The actual full core inverse is reconstructed in section2, not inferred from a low-energy model.
- Scalar interfaces4eb53a9531fa977e0ef775aadd3a5ca37f4e3d42d83488d44a9fbc6d730150bc, b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80,43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1 and a03139261c649546c00b7a15bef01c4a7387dfa6cc267f5c20e82f88b65f02d9 with their accepted scoped checks5a2e,0071,1fa285,ef273. Their exact installed identities and phase/regularity hypotheses were refreshed in assessment67db6e97066083e1eb94ae0a4dae5f65229665eb601e57403f49ee7204239cce; no old router matrix constant or finite budget is imported.

ROOT requested this bounded derivative bridge after the exposed reconnaissance. I authored the old writer inverse/core and incoming/resource work and checked shared ancestors. The new local third-jet arithmetic, eleven-stage derivative chain, uniform constants and complete internal interface are author derivations requiring a distinct check. This is not independent confirmation of my earlier sources. The finite author is separately addressing physical normalization/seed transfer; none of its unfrozen conclusions is used here.

Only this PROPOSAL.md was created. No scientific executable, simulation, parameter sweep, delegation, source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. No native realization or permanent halt is claimed.
