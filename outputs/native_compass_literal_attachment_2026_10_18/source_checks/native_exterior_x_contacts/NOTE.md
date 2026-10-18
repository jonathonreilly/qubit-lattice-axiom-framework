# Two exterior x contacts: exact four-site diagnostic

**Status: bounded analytical decision calculation, requiring a distinct check before reuse.** Supplying exterior X eigenstates does not reproduce the isolated-pair nominal gate exactly. It produces a coherent field in one XX sector and none in the other. The error is computed below, not inferred from a large Duhamel upper bound. There is no uniform positive accuracy floor over all J: the nominal-time error tends to zero as J tends to zero. This is not a no-go for an embedded apparatus. A positive finite-box extension is derived below: weak transverse contacts and small J give a complete bound without any special environment preparation.

The source is the compass family pinned in `native_weak_transverse_attachment/PROPOSAL.md`, SHA256 `323817300ff86682cca410da69aca9e99b484474e972bab0d263c9448c1297ed`. Its exact Hamiltonian sources are PR9752 head `33f0af206df4897744a9d5e248c2889fdd6ed1e7`, raw-body SHA `1b579ec1901f2389b4fb058649b8ea78f0d0d0c4737e36c54af1c400bf4f795e`, and PR9747 head `e161fcef330a7cad87a19e3ffcb2fc3b03691083`, raw-body SHA `debd8448a97a982d23074582e983438cebc880a86cb03f44bfe9be57921d4d3d`. Both complete bodies were read in the preceding coherent task. No normal-form theorem is imported. The cube remains frozen.

## Actual four-site model

Take the open chain L,1,2,R, with the literal old sites1,2 and given K=2I+Z1Z2 installed once. Put J=J_x>0 and J_y=J_z=0 as an explicitly declared limiting diagnostic, not the positive-transverse cube theorem. Install

    H=K+J[(I−X_LX1)+(I−X1X2)+(I−X2X_R)].              (1)

This has four qubits and four positive blocks: K of norm3 and three exchange-axis blocks of norm2J. Old incident loads are3+4J, endpoint loads2J. Thus Λ>3 and J≤(Λ−3)/4 suffice. The given K, open chain, vanishing transverse couplings and delivered endpoint states are premises, not derived native suppliers.

Supply χ_ab=|a>_X,L⊗|b>_X,R with a,b∈{+1,−1}, independent of arbitrary old/passive input. These are coherent X-basis product states, not the earlier Z blanks. X_L and X_R commute with H, so this environment remains exactly χ_ab, with all scalar evolution assigned below. The old generator is exactly

    H_ab=K+3J I−JX1X2−J(aX1+bX2).                    (2)

No source A/B Hamiltonian or output head is present. All four sites remain in the complete target, and passive references are untouched.

## Sector reduction and complete error at every time

Let p=±1 be the eigenvalue of X1X2. Each sector is two-dimensional. Within it set Z=Z1Z2 and X=X1; these are anticommuting involutions, and X2=pX. Thus

    H_ab|p=(2+3J−Jp)I+Z−d_p X,
    d_p=J(a+bp),  Ω_p=sqrt(1+d_p²).                 (3)

Exactly one sector is affected: p_*=ab has d_p*=2aJ and Ω=sqrt(1+4J²); the sector−p_* has d=0. Changing a,b changes which sector is affected and the sign of its transverse field, not its norm or spectral frequency.

Let cosθ=3/5, sinθ=4/5, θ∈(π/4,π/2), and W=exp(iθ)exp(iθX1X2). For all t≥0 compare the actual whole-output isometry to the phase-pinned literal target

    T_t ξ=exp[−i(3Jt+θ)] exp(−itK)Wξ⊗χ_ab.          (4)

This retains full elapsed aging exp(−itK), and the common scalar is known in advance. Removing common unitaries, the sector comparison is

    F_p(t)=exp[ipδ] exp(itZ)exp[−it(Z−d_pX)],
    δ=Jt−θ.                                        (5)

The second and third factors have determinant1. Their half-trace is

    c_p(t)=cos t cos(Ω_p t)+(sin t sin(Ω_p t))/Ω_p.

Define φ_p=acos c_p in[0,π]. Their eigenvalues are exp(±iφ_p). The exact induced complete-vector error, including arbitrary passive extensions, is therefore

    E_ab(J,t)=max_(p=±1,σ=±1) 2|sin[(pδ+σφ_p)/2]|. (6)

In the unaffected sector φ=0 identically. In the affected sector use Ω above. This expression is independent of the choice of a,b after maximizing: flipping p or d merely permutes or conjugates the relevant phases. It is an operator-norm formula, not an error computed for a favored old state. Unhalved channel distance is bounded by min(2,2E_ab); no claim of equality for the channel is made.

## Nominal gate time

At τ=θ/J, δ=0, so the unaffected sector agrees exactly. The full error is

    E_ab(J,τ)=sqrt{2[1−cosτ cos(Ωτ)
                         −sinτ sin(Ωτ)/Ω]}.         (7)

Every choice of endpoint signs has the same error. No sign choice removes both sector distortions: making d_+=0 requires a=−b, while making d_−=0 requires a=b. Nonzero a,b cannot satisfy both.

In fact(7)>0 for every finite J>0. To have zero error, the affected SU(2) operator in(5) must equal I. Since d≠0, the coefficient of X in exp[−it(Z−dX)] forces sin(Ωt)=0. Equality to exp(−itZ) then forces sin t=0 and equal signs of the two cosines. At nominal t>0 this requires t=mπ, Ωt=nπ for positive integers m,n of the same parity. But

    (n²−m²)π²=(Ω²−1)τ²=4θ²,

and 0<4θ²/π²<1 because0<θ<π/2. It cannot be an integer n²−m². This argument concerns the phase-pinned operator equality. Allowing another common scalar cannot fix nominal equality either: the unaffected sector already equals the target and fixes that scalar to1.

This is not a J-independent error floor. Put Δ=(Ω−1)τ. Then Δ≤2θJ and

    c=cosΔ+(1/Ω−1)sinτ sin(Ωτ),
    E²≤Δ²+2(1−1/Ω)≤4(θ²+1)J².                    (8)

Here Ω−1=4J²/(Ω+1)≤2J² and1−1/Ω≤2J². Consequently E≤2sqrt(θ²+1)J and E tends to zero for J→0, at a growing timeτ=θ/J. In the opposite J→infinity limit τ→0 and Ωτ→2θ, so E→2sinθ=8/5; that limit need not satisfy a fixed cap. These exact limits show why a large crossing-term Duhamel bound cannot decide accuracy.

## Shifted times and the next decision

Equation(6) remains the exact time-dependent test at shifted observation times. The unaffected sector incurs2|sin(δ/2)| under the specified phase. Exact agreement in both sectors with that phase would require δ∈2πZ and affected SU(2) evolution equal to I, hence the additional integer recurrence conditions above. With a freely changed but common phase, the unaffected sector fixes the allowed phase; one must still solve the affected two-dimensional condition. No theorem about all such J/time choices, rational approximation rates or optimal windows is claimed here.

The constructive weak-J behavior in(8) is a live alternative for further work: sufficiently small J suppresses these static exterior fields in the presence of the given ZZ energy splitting while accumulating the commuting XX gate. A full apparatus claim would still need a finite-window bound, the actual larger exterior model, positive transverse bonds if required, and complete environment outputs. The exterior X-eigenstates remain supplied. This diagnostic neither proves their autonomous preparation nor shows that an infinite interacting exterior stays in these states.

The result therefore narrows the boundary question: simple exterior eigenstates do not preserve the exact isolated gate at its nominal time, but they do not produce a uniform obstruction to approximate operation. The present four-site geometry is a controlled test of two restored x-contacts, not the removal of every open-boundary supplier.

## Positive extension: restore all bonds around an interior old pair

The preceding eigenstate calculation is block diagonal in X_L,X_R. Its norm bound is uniform over all four signs. Hence eigenstate preparation is unnecessary when the reference environment Hamiltonian commutes with X_L,X_R: direct-sum operator bounds apply even to arbitrary superpositions and old/environment/passive correlations. This observation alone does not authorize ignoring actual transverse contacts. The following comparison pays them.

Use the finite open box Ω={−2,−1,0,1,2,3}×{−1,0,1}², with54 sites. The old sites are(0,0,0),(1,0,0); L=(−1,0,0),R=(2,0,0). All four lie away from the x boundary; old sites also have every y/z neighbor. Install ALL compass positive blocks J_a(I−σ^aσ^a) on the45 x-edges,36 y-edges and36 z-edges, plus the given old K once:118 blocks. Set J=J_x>0,s=J_y+J_z>0. Each interior load is4(J+s), with an extra3 at old sites. Thus3+4(J+s)≤Λ suffices. This is still a supplied finite far boundary, not an infinite-lattice realization.

Let S={L,1,2,R}. There are exactly eight y-edges and eight z-edges incident to S: each of its four distinct axial sites has two of each, and none of those edges has both endpoints in S. Define the COMPARISON environment Hamiltonian H_E as the positive compass sum on E=Ω\{1,2} after omitting these16 edges. It contains42 x-edges,28 y-edges and28 z-edges, all E-only, so98 blocks. Its x-bonds from L/R toward the far exterior remain installed. Since no retained y/z edge touches L/R, [H_E,X_L]=[H_E,X_R]=0, even though distant y/z terms remain and need not commute among themselves.

The actual Hamiltonian decomposes EXACTLY as

    H_actual=H_ref+V,
    H_ref=K+J[3I−X1X2−X_LX1−X2X_R]+H_E+8s I,
    V=−J_y Σ_(8 removed y edges) YY
      −J_z Σ_(8 removed z edges) ZZ.                  (9)

H_E is not the actual isolated-environment Hamiltonian: eight of the omitted transverse edges are E-to-E and eight are old-to-E. The whole8st bound pays both changes. Its evolving output is an explicitly chosen comparison environment, not a mislabeled exact actual environment evolution. The word removed refers only to the reference comparison, not the actual installed graph. Their16 positive identity contributions are8s I, retained exactly. Thus||V||≤8s on the full space. H_E is disjoint from the old sites and commutes with the four-site reference through X_L,X_R; no further commutation is assumed.

For any real d, Ω_d=sqrt(1+d²), the normalized axes obey

    ||(Z−dX)/Ω_d−Z||=sqrt(2−2/Ω_d)≤|d|.

Subtract the two exact sine/cosine exponentials at equal frequency Ω_d, then compare frequencies Ω_d and1. For t≥0 this gives

    ||exp[−it(Z−dX)]−exp(−itZ)||
       ≤|d|+(Ω_d−1)t≤|d|+d²t/2.

In each controlled sector d is0 or±2J. Combining the uniform bound with the gate-angle error and full-space Duhamel yields

    ||exp(−itH_actual)−T_full(t)||
       ≤2J+2J²t+J|t−θ/J|+8st,                       (10)

where the exact comparator is the complete unitary

    T_full(t)=exp{−i[(3J+8s)t+θ]}
              [exp(−itK)W]⊗exp(−itH_E).             (11)

Equation(10) holds on the ENTIRE old/environment Hilbert space and after arbitrary passive extension. It therefore permits an arbitrary input-independent environment state, or even initial correlations, provided the target is(11) acting on that SAME joint input. For a product input the environment factor is common; for correlated inputs no false factorization is claimed. No X eigenstate, blank environment, infinite-temperature ensemble or pure-state supplier is required for this operator comparison. The whole environment output is retained.

For0<ε≤1 let

    J≤ε/[128(θ+1)],
    r=s/J≤ε/[256(θ+1)],
    w=ε/(32J), τ=θ/J,
    3+4J(1+r)≤Λ.                                    (12)

Positive transverse coefficients may have any split with this sum. No cancellation coefficient or additional interaction is installed. The window[τ−w,τ+w] is positive. There Jt≤θ+ε/32<θ+1. Thus2J<ε/64,2J²t<ε/64,8st<ε/32, and J|t−τ|≤ε/32. The total is strictly below3ε/32<ε/8. The unhalved complete channel distance is consequently below3ε/16<ε/4.

The parameter domain is nonempty for eachΛ>3: choose positive r obeying(12) and J≤min{(Λ−3)/8,ε/[128(θ+1)]}; r<1 then gives the cap. At fixedΛ and saturating the ε-dependent J bound for sufficiently small ε, τ is O(ε^−1), the absolute half-window w is constant in the model units, and its relative half-width is ε/(32θ). The unit coefficient of ZZ in the given K fixes the energy/time normalization; reducing J is a real ratio change relative to that gap, not a rescaling of physical time. This is a sufficient chosen family, not optimality or a tolerance theorem for fixed arbitrary coefficients. The anisotropic subfamily and calibrated observation time remain supplied.

This extension removes the *adjacent* open-x-boundary and eigenstate-preparation shortcut within this finite model. It does not remove the far finite boundary, derive old K, preserve the original source A/B inventory, or construct physical capture/Record/reset. No original normal-form or infinite-box theorem is used. The reference cuts are merely a comparison proof; all actual117 compass bonds remain. ROOT proposed this extension after seeing the sector diagnostic; the independent reconstruction here counted its edges, checked every commutator and retained both identity scalars.

## Provenance and verification limits

ROOT proposed the restored-contact sector test. I derived(3)–(8) analytically, retaining the actual positive-block scalar, sector sign and common environment. No numerical solver, sweep, scientific runner, Git/canonical/checkpoint change, delegation, model override or editable-prompt change occurred. Only this note was written. This is shared-model/source-exposed author work and needs a distinct check before becoming a theorem dependency. The original compass source and earlier cube/probe files remain unchanged.
