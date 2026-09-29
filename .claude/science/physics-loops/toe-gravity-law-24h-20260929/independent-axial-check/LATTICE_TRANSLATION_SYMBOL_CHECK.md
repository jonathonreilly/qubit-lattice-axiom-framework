# Independent mixed-bracket matrix-symbol check

2026-09-29. This is a separate check of the proposed extension to arbitrary finite-range quadratic momentum pairings. The fixed-density affine-lapse theorem in `AFFINE_LAPSE_CHECK.md` does not itself imply this result. No formal review PASS, audit verdict, physical interpretation, or axiom adoption is conferred.

**Conclusion:** the two-component matrix argument is valid with an explicitly generically invertible TT kinetic symbol. It rules out the specified regular, canonical, finite-support, proper-cubic, exactly mixed-closing jet even after allowing arbitrary finite kinetic pairings and density centering. Both TT components must be retained. A nonzero but singular kinetic block is insufficient for the matrix inversion step; an exact stress example below shows that distinction matters.

The proof can allow an arbitrary zeroth U0 moment. Only its nonzero first lapse moment is needed. The original normalization gives that moment equal to one.

## Hypotheses actually used

Retain the six independent canonical tensor pairs, the fixed linear C1 and G1, regular field-degree jets, time parity, and proper cubic covariance from the campaign contract. Replace the fixed T2 by any real, translation-covariant quadratic momentum functional **linear in its lapse** whose complete kernel has finite support. Each proposed generator and U0 kernel has finite total support, with no common bound across proposals.

Require the same off-shell mixed degree-two equation, including arbitrary PPP terms in G3 and regular same-order mixing `G1[W1]`. No CC, GG, F0, cubic ADM normalization, or G2 continuum normalization is used in this proof. Extra constraint species, singular redefinitions, and a different canonical/background carrier are outside it.

Let

`mu0=U0(1,1)`, `mu1=sum_(a,b) b u_ab`,

so translation covariance and bilinearity give `U0(1,x)=mu0*x+mu1`. Require mu1!=0; the supplied scalar-lapse action sets mu1=1. Mu0 may be arbitrary.

The kinetic hypothesis is that the axial TT uniform-lapse symbol F has `det F(z)` not identically zero. The supplied long-wavelength normalization is sufficient: in the canonical TT coordinates used below,

`F(1)=(1/(4alpha)) I_2`, alpha!=0.

This does not require F to be invertible at every lattice momentum or positive definite for every momentum. It does require a generically nondegenerate two-component block. Merely saying that F is nonzero would be weaker and would not justify the proof.

## Canonical projection and proper C4

The axial TT variables are

`q1=(h_yy-h_zz)/2`, `q2=h_yz`,

`p1=P_yy-P_zz`, `p2=P_yz`.

Their brackets are `{q_i,p_j}=delta_ij`. On this block `h_yy=q1`, `h_zz=-q1`, `P_yy=p1/2`, `P_zz=-p1/2`. The source's shear momentum is the independent canonical P_yz, not the full symmetric-matrix entry P_yz/2. Keeping this distinction gives T2's continuum value `(p1²+p2²)/(8alpha)` and the F(1) above.

A proper 90-degree rotation around x acts as -I on **both** TT components. The scalar complement has eigenvalue +1 and the x-transverse vector complement has eigenvalues +i,-i. Thus proper C4 isolates a two-dimensional block; it does not split the two TT variables into separate irreducible lines. An invariant cross-block matrix M would satisfy `M(R_other+I)=0`, and `det(R_other+I)=8`, forcing M=0. This applies to the uniform and affine kinetic forms and to the constant-x-shift bilinear generator. Off-diagonal, chiral, and noncommuting TT matrix kernels remain allowed.

Use transverse zero Fourier modes with canonical normalization, or equivalently carry the transverse area in both functionals and the reduced symplectic form; that common area cancels. The restriction is not assumed to be canonical without this normalization. The vertex/yz-face staggering does not create a half-x displacement in these two TT components.

For arbitrary x profiles of the TT momenta, all linear momentum constraints vanish after transverse periodic summation: they contain transverse differences, while P_xx,P_xy,P_xz vanish. Therefore `G1[W1]=0` on this sector for arbitrary W1. The fixed linear functionals G1[1], C1[1], and C1[x] have zero differential for constant shift and uniform/affine lapse. Consequently neither T3 nor G3 can rescue the following momentum-quadratic equations. At h=0 they reduce to G2 and T2 alone.

## General density and canonical bracket

Write, on the TT block,

`G2[1]=p^T D q`, `T2[1]=(1/2)p^T F p`, `T2[x]=(1/2)p^T B p`.

D and F are finite matrix convolution operators. Their symbols are 2x2 Laurent-polynomial matrices. Define `M^sharp(z)=M(1/z)^T`; reality and symmetry of the kinetic quadratic form give `F^sharp=F`. No condition `D^sharp=-D` is assumed.

Every finite translation-covariant density linear in N has

`B=X F+A`,

where X multiplies by the integer coordinate and A is a finite matrix convolution. To check this without a midpoint or lapse-placement assumption, consider a general symmetrized density pair

`(1/2) sum_x N_x [p_(x+a)^T M p_(x+b)+p_(x+b)^T M^T p_(x+a)]`.

Its uniform symbol and affine offset are

`F(z)=M z^(b-a)+M^T z^(a-b)`,

`A(z)=-a M z^(b-a)-b M^T z^(a-b)`.

All other lapse placements can be translated to this form, with changed finite a,b. Finite sums exhaust the allowed quadratic density. The formula also gives `A-A^sharp=z F'`, ensuring B is self-adjoint. A need not itself be self-adjoint, and no centering convention is imposed.

Canonical differentiation, with `{q,p}=+1`, gives

`{p^T Dq,(1/2)p^T Fp}=(1/2)p^T(D F+F D^sharp)p`.

Indeed the q derivative of the first functional is D^sharp p; its contraction with Fp is p^T D Fp, whose symmetric quadratic matrix is the displayed sum. This fixes the sign independently of a comparator convention.

Since the identity holds for every compactly supported real TT momentum, its symmetric quadratic matrices must agree. The uniform and affine equations are therefore

`D F+F D^sharp=mu0 F`,

`D B+B D^sharp=mu0 B+mu1 F`.

## Matrix elimination and contradiction

With B=XF+A, substitute the uniform equation into the affine one. The terms proportional to X cancel, leaving

`[D,X]F+D A+A D^sharp-mu0 A=mu1 F`.

Since det F is not the zero Laurent polynomial, invert F over the commutative rational-function field. This is an algebraic elimination; it does not assert a bounded physical inverse operator or exclude isolated zeros on the unit circle. The uniform equation gives

`D^sharp=mu0 I-F^(-1) D F`.

Multiplication on the right by F^-1 then yields

`[D,X]+[D,A F^(-1)]=mu1 I_2`.

Thus mu0 cancels even if it was not normalized to zero. If `(S f)_x=f_(x+1)` and `D=sum_r D_r S^r`, direct application to a test sequence gives `[S^r,X]=r S^r`. Hence the exact symbol identity is

`z D'(z)+[D(z),A(z)F(z)^(-1)]=mu1 I_2`.

Take the ordinary **finite 2x2 matrix trace**, not an infinite operator trace. The rational-matrix commutator has trace zero. Therefore

`z (tr D)'=2 mu1`.

For every finite Laurent polynomial `tr D=sum_r d_r z^r`, its logarithmic derivative is `sum_r r d_r z^r`; the z^0 coefficient is exactly zero. The right-hand side has nonzero constant coefficient 2mu1. This is impossible.

The trace argument uses neither simultaneous diagonalization, reflection symmetry, commutation of D with F, nor a scalar TT reduction. It includes every finite density-centering term through A. The contradiction is independent of K: the linear curvature generators vanished in the two selected smearing tests.

## Domain and finite-boundary check

The affine operator X is unbounded on an infinite sequence space, but the proof initially uses finitely supported fields and finite kernels, so all displayed functionals and derivative pairings are finite sums. Constant and affine smearings can also be replaced by compact plateaux containing the relevant field and derivative supports. For each fixed proposed kernel, choose the plateau after its finite support radius is known. Boundary derivatives of G1 and C1 then lie outside the differentiated T3 and G3 supports.

This yields the two operator identities on arbitrary compactly supported TT profiles and therefore their local matrix coefficients on the infinite lattice. No limit of a periodic sawtooth is being treated as an exact global affine operator. An explicit large periodic-box control below uses profiles far enough from its seam that every composed operator stays in the affine region.

The transverse projection may be performed on a finite periodic cylinder and normalized as above. A translation-covariant finite-support 3D identity would descend to that sector. This is a necessary-sector obstruction, not 3D sufficiency and not a claim about every possible lattice phase space.

## Attempts to break the claim and exact controls

The initial one-dimensional TT-irrep proposal was not valid under proper C4: both TT variables share eigenvalue -1 and can mix. The two-component argument above repairs that issue without assuming an additional reflection.

A second stress test shows why generic invertibility must be explicit. Let

`F=[[1,0],[0,0]]`, `D=[[0,1],[0,0]]`, `A=[[0,1/2],[1/2,0]]`.

Then `DF+FD^T=0` and `DA+AD^T=F`, so both uniform and affine equations hold with mu0=0,mu1=1 despite D'=0. This A is realizable by adding the lapse-difference density `(N_(x+1)-N_x)p1_x p2_x/2` to `N_x p1_x²/2`. The example has singular F and does not match the supplied nondegenerate TT continuum normalization. It is not a complete mixed algebra for arbitrary lapse, nor a physical countermodel; it demonstrates that the inversion hypothesis cannot be replaced by the word “nonzero.”

`check_translation_symbol.py` independently verifies:

- the canonical TT pairing and the actual proper 90-degree rotation of a symmetric tensor;
- the absence of a -1 eigenspace in the complement;
- F^sharp=F and A-A^sharp=zF' for a fully symbolic 2x2 density pair with distinct offsets;
- the generic noncommuting 2x2 rational-matrix elimination, including cancellation of arbitrary mu0 and the zero commutator trace;
- a direct finite-position construction of the uniform and affine kinetic Hessians on a 17-site, two-component chain, using nonsymmetric coefficient matrices and a compactly supported momentum profile away from the seam;
- the sign and normalization of the canonical gradient contraction against that affine Hessian;
- the exact singular-F stress example;
- the zero constant coefficient of the derivative of a generic finite Laurent trace.

All checks pass exactly. The generic-symbol and finite-position controls test different descriptions of the algebra; no author assembly, author symbol runner, or expected primary output is imported. The elementary all-finite-Laurent proof is stated above, rather than inferred from the finite polynomial degree used in the control.

## Scope, provenance, and execution

The independent derivation and controls were completed before reading the author's `KINETIC_PAIRING_ESCAPE.md`. Its argument agrees with this reconstruction, with the optional improvement allowing nonzero mu0 and the transverse canonical-normalization clarification. The source hash at reading is recorded in the companion manifest update. The literature-context paragraph in that note was not independently checked and is not used as a premise here.

This theorem excludes only the specified finite-support regular canonical jet with the fixed linear generators, proper-cubic TT isolation, generically nondegenerate TT kinetic block, and exact nonzero mixed lapse moment. A degenerate TT branch, additional carriers/constraint species, a different linear gauge seed, singular redefinitions, infinite-range symbols, or approximate infrared covariance changes a hypothesis. The proof does not certify any such alternative; it also does not rule it out. Discrete lattice translation covariance itself is not being rejected: the incompatible requirement is the supplied exact microscopic mixed constraint identity with nonzero scalar-lapse derivative normalization.

Executed from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/check_translation_symbol.py > .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/translation_symbol_results.txt 2>&1
```

Exit 0, elapsed 1.41 seconds. Exact result metadata is saved in `translation_symbol_control_results.json`; full outputs and source hashes are preserved. Deadline and stop checks were active. All writes stayed in the assigned independent-check directory; no source, parent runner, state, Git, or external-service mutation was performed.
