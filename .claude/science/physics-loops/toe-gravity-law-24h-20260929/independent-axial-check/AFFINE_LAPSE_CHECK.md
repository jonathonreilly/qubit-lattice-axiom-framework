# Independent affine-lapse obstruction check

2026-09-29. This is a new mathematical check of an arbitrary-finite-support argument, separate from the radius-one and radius-two matrix results. It is not a formal review PASS, audit verdict, primitive adoption, or gravitational interpretation.

**Conclusion:** the proposed phase-space evaluation proves the stated obstruction for the fixed sitewise quadratic kinetic lapse density and the regular off-shell mixed-bracket jet. Noncompact smearings and an infinite transverse area are unnecessary. A finite-torus version works for every proposed finite support bound. Cubic-momentum G3 and the allowed momentum-dependent mixing cannot repair this particular identity.

The result depends on the fixed kinetic density. An independently checked intersite kinetic mutation makes the allegedly vanishing bracket nonzero, so this proof does not extend to arbitrary momentum pairings.

## Exact hypothesis and conclusion

Use the independent canonical pairs A,B,C and P,Q,R and

`C1[N]=K sum_x N_x Delta(B+C)_x`,

`T2[N]=sum_x N_x [P_x²+Q_x²+R_x²-2P_x Q_x-2P_x R_x-2Q_x R_x]/(8 alpha)`,

`G1[X]=2 sum_x X_x(P_x-P_(x+1))`.

Here alpha is any finite nonzero real number. K may be any real number, including zero: its value does not enter this proof. The current physical branch originally supplied positive alpha,K. These phase variables, densities, and canonical bracket remain supplied hypotheses, not consequences of the framework axioms or primitives.

Require a regular field-degree expansion with the declared time parity, so C3 contains hhh and hPP and G3 contains hhP and PPP. In the momentum-quadratic part of the degree-two mixed identity require

`{G1[X],T3[N]}+{G2[X],T2[N]}+{G3_PPP[X],C1[N]}`

`= T2[U0(X,N)]+G1[W1(P;X,N)]`.

G2 is an arbitrary hP functional, T3 an arbitrary hPP functional, and G3_PPP an arbitrary PPP functional. Each proposed jet has finite total support; there is no common upper support bound across the class of proposals. The bilinear, translation-covariant kernel U0 also has finite support and satisfies

`U0(X,N)_z=sum_(a,b) u_ab X_(z+a)N_(z+b)`, `sum_(a,b) b u_ab=1`.

The first condition is schematic for any finite list of shifts, including the original edge/vertex staggering. The half-edge offset does not matter when X=1. U0's zeroth moment and its X derivative moment are unnecessary for this argument. W1 may be any regular momentum-dependent kernel in the displayed equation; no moment restriction on it is used. No G2 continuum normalization, cubic kinetic normalization, V2 normalization, CC, GG, or substituted-Jacobi premise is needed.

**There is no such off-shell mixed identity.** This is a theorem for the specified starting generators and regular expansion; it does not assert impossibility of every lattice constraint system.

## Independent proof

Form brackets before restricting the fields. Take h=0, P=R=0, and `Q_x=q delta_(x,0)` with q!=0. For a formal constant shift X=1 and affine lapse N_x=x:

1. `G1[1]` is identically zero as a functional on compactly supported phase fields, by telescoping. Its differential is zero, so its bracket with every T3 vanishes.
2. `C1[x]` is identically zero on compactly supported coordinate fields, by summation by parts and Delta x=0. Its differential is zero, so its bracket with every G3_PPP vanishes.
3. The **entire** differential of T2[x] vanishes at the specified point. It has no coordinate derivative. At an occupied site its P,Q,R derivatives are respectively `-Nq/(4alpha)`, `Nq/(4alpha)`, and `-Nq/(4alpha)`; N is zero at that site. At every other site all momenta vanish. Thus its bracket with any differentiable G2 is zero. This includes the off-diagonal entries of the diagonal DeWitt kinetic matrix; it is not only a statement about the Q derivative.

The left-hand side is zero. On the right, G1[W1] is zero because P is identically zero, even when W1 depends on momenta. At the occupied site

`U0(1,x)_0=sum b u_ab=1`,

so `T2[U0]=q²/(8alpha) != 0`. The required equation is false.

The canonical sign convention cannot rescue this evaluation: every bracket on the left vanishes individually. Reversing a nonzero U0 normalization also leaves a nonzero right-hand side.

## Finite-torus replacement: no noncompact-smearing assumption

Choose an integer R>=1 large enough to contain all slots of the proposed finite-support jet and U0. Use an odd periodic chain of length `L=4R+5`. Label its coordinates by the symmetric representatives `-floor(L/2),...,floor(L/2)`. Set X=1 everywhere and let N equal those representatives. This is a perfectly ordinary periodic lapse with a single sawtooth seam.

The same localized momentum point gives `dT2[N]=0` everywhere, while `G1[1]=0` is an exact polynomial identity on the finite torus. The C1 gradient is supported only at the two seam sites `+/-floor(L/2)=+/-(2R+2)`.

At h=0 and the localized momentum point, a nonzero derivative of a cubic PPP monomial leaves two momentum factors at the occupied site. Its density anchor must be within R of that site, and its differentiated slot is within R of that anchor. Hence `dG3_PPP[1]` has support within distance 2R of the occupied site. It cannot meet the C1 seam. Their Poisson bracket is therefore exactly zero, not just small.

Every U0 input sampled at the occupied site lies within R and sees the affine portion of N, so its value remains `sum b u_ab=1`. The right-hand side is again q²/(8alpha). This construction works for **each arbitrary finite R** by the support argument; the theorem is not an extrapolation from a finite list of numerical radii.

A local coefficient identity on the infinite lattice would descend to this finite torus. Conversely, the constructed counterexample refutes that identity. One may also use compact smearings on the infinite line, with plateaux containing the complete derivative support, but the periodic construction avoids boundary-condition ambiguities. In that alternative, the safe derivative-support bound is twice the density radius, not necessarily one radius.

The theorem does not cover a countably infinite sum with unbounded support merely because each individual monomial has finitely many slots. Summability and domain conditions for genuinely infinite-range kernels would require a separate argument.

## Three-dimensional embedding and omitted components

Use a finite periodic transverse section, set all fields independent of y,z, and let only P_yy=q on the x=0 plane. P_xx, P_zz and all shear momenta vanish; h=0. Take the constant shift in x and the sawtooth x lapse above.

G1 of the constant x shift is identically zero. The C1 shear derivatives contain transverse differences of N and vanish; its diagonal derivatives are supported only at the x seam. A finite-support cubic generator's nonzero derivatives are confined to a bounded neighborhood of the occupied plane, disjoint from that seam. The complete T2 differential vanishes because every occupied momentum site has N=0, and every other momentum is zero. These statements are made for the full fixed generators, so taking the restriction has not discarded a rescuing canonical derivative.

For arbitrary W, the only potentially surviving G1[W] term is

`2q sum_(y,z) D_y^- W_y(0,y,z)`.

It is exactly zero by transverse periodic telescoping, even without assuming that W itself is transverse-constant. The remaining right-hand side is the transverse area times q²/(8alpha), since translation covariance and the prescribed first x-lapse moment give U0=1 on the occupied plane.

Thus an infinite-cubic-lattice finite-support identity fails this valid periodic restriction. This is a necessary-sector contradiction, not a claim that an axial solution would have supplied a 3D lift.

## Independent controls and adversarial tests

`check_affine_lapse.py` imports only the earlier **independent** full finite-functional polynomial and gradient helpers. It does not import or execute the author's assembly or affine-certificate runner. Exact SymPy q and alpha are retained in the evaluations.

| Radius R | Torus L | All PPP basis monomials checked | Largest nonzero PPP-gradient distance | C1 seam sites | U0 basis terms checked |
| --- | ---: | ---: | ---: | --- | ---: |
| 1 | 9 | 56 | 1 | -4,+4 | 6 |
| 2 | 13 | 364 | 3 | -6,+6 | 20 |
| 3 | 17 | 1,140 | 5 | -8,+8 | 42 |

For every row of this table: substituting X=1 annihilates the full G1 polynomial; every kinetic gradient component is zero; every PPP bracket with C1 is zero; and each U0 basis coefficient evaluates to `b*q²/(8alpha)`. Therefore its normalized combination is nonzero. These controls corroborate the general support proof; they do not replace it.

An explicit 13³ control with 169 occupied P_yy sites confirms zero kinetic differential and cancellation of **each independent transverse W_y coefficient** in G1[W]. The forced right-hand side is `169*q²/(8alpha)`.

As a source-bound coefficient control, the script derives new dual weights by phase evaluation on the radius-one and radius-two matrices whose every entry was already independently reconstructed. For a GC2_P2 monomial with two Q factors at the same site, its weight is `8*(N_position-Q_position)`; the U0 first-lapse-moment row gets weight +1. No solving or author witness is used. These independently derived duals cancel all 620 and 2,920 columns, respectively, giving `0=1`. Their full weights are preserved in `affine_lapse_control_results.json`.

To test a load-bearing premise, add the intersite kinetic density `N_x Q_x Q_(x+1)` and choose the allowed quadratic generator density `X_x B_x Q_(x+1)`. At the same phase point, direct independent Poisson differentiation gives

`{sum X_x B_x Q_(x+1), sum N_x Q_x Q_(x+1)}=-q²`.

Indeed the new kinetic derivative at x=-1 is -q and the generator's B derivative there is q. Thus changing the kinetic pairing removes the stationary-point mechanism. This does not establish closure for the mutated system; it demonstrates precisely why the fixed-density theorem cannot be silently generalized.

The witness lies off the full scalar-constraint surface, since T2 is nonzero. It therefore refutes the requested strong constraint-valued identity with regular U0. It does not establish failure of every weakly first-class ideal, every singular constraint redefinition, or a model with additional constraint species. Nonanalytic/singular kernels, a changed quadratic kinetic stencil, a changed G1/C1/phase space, a different continuum kernel normalization, additional clock or embedding variables, and approximate infrared rather than exact microscopic closure remain outside this conclusion.

## Provenance and execution

The independent derivation and torus controls were completed before reading the author's new note. The subsequently read `AFFINE_LAPSE_OBSTRUCTION.md` had SHA256 `88f6308bd33e5e3274824847388b6b29d616cdc2ad629cb40cda076c560bae19`. Its mathematical argument agrees with this check, subject to the two support-wording clarifications above. Later edits to that note are not implicitly covered. The author's new runner was neither read as evidence nor imported/executed. Prior science source and runner identities remain those in `MANIFEST.json` and the earlier reports.

Executed from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/check_affine_lapse.py > .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/affine_lapse_results.txt 2>&1
```

The final execution and exact outputs are recorded alongside this report. Deadline/stop checks were active; the script is a short local single-thread process. No parent script, source, state, Git object, or external service was changed. This establishes the scoped mathematical obstruction, not formal review or an axiom consequence.
