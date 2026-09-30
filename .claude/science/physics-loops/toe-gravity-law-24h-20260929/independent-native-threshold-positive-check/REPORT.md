# Focused check of strict threshold-form positivity

2026-09-30. No blocking discrepancy was found in the dependent extension
`native-threshold-positive-extension/REPORT.md`, SHA256
`5b795a11ca2450033acea3e896877c606027d160162f3281d93c1246a34e0f81`.
For the same supplied Hamiltonian, infinite cubic lattice, N=4, total
momentum zero, and fixed mu,tau>0, its relaxed fifteen-channel threshold
form is strictly positive on every nonzero constant incoming vector.
This is a focused mathematical check, not formal review, audit, retained
status, a numerical matrix evaluation, or an on-shell scattering theorem.

## Dependencies and independence

This is a dependent extension of the already source-bound threshold check,
not an independent reconstruction of its entire Green construction again.
I reread the complete short extension, its bindings, the load-bearing
threshold and previous-check sections, and the actual density-source
operator, positivity and spectator-pin proof. The full threshold proof and
independent derivation had been read and frozen in the preceding check.
No author code was run or imported, and no new numerical job was needed.

The reused results are precise: H is bounded nonnegative on the N=4
translation-zero fiber; the Q compression has gap mu; the free exterior is
the actual nine-component two-bond Dirichlet problem; its three-dimensional
compact-source Green kernel is finite and decays at large separation;
the finite physical core Schur matrix is strictly positive. They imply a
finite compact-source inverse form and pointwise full response, with
decaying exterior correction. They do not imply a bounded inverse on l2.

The bound density proposal has SHA256
`84c2188063d91af9364b35ae459b8f413eae8a61a3200a058f6fd0f907b6d3fb`.
I also compared it to the observed origin/main source, whose SHA256 is
`7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0`.
Only the final evidence/landing paragraph differs; the operator, SOS and
pin arguments are byte-identical. The current source comparison does not
confer audit authority. Full input hashes are in SOURCE_BINDINGS.json.

## Zero relaxed energy gives pointwise zero SOS rows

Write H=L*L, where L collects the literal local positive-square rows,
including the diagonal D rows with their positive weights. This notation
uses the actual hard-core occupation carrier. In the translation-zero
fiber, rows are organized modulo simultaneous translations; every fixed
physical row is a finite linear functional on orbit coefficients. The
positivity identity descends to this fiber, so its absolute square is
bounded by a positive constant times the full fiber energy. No sum over
infinitely many identical translations is being included in that energy.

For a prescribed constant incoming profile Phi=Phi_z, the previously
checked construction has L Phi of finite relative support. Thus the
affine energy for any l2 correction u is unambiguously

    ||L Phi+L u||^2 = E(Phi)+2 Re<F,u>+<u,H u>,  F=H Phi.

The cross identity follows from finite support of L Phi and boundedness
of L; it does not require Phi itself to be square-summable. F has finite
relative support and a finite inverse quadratic form.

Let R_e=(H+e)^(-1), u_e=-R_e F. Direct expansion gives

    E(Phi+u_e)=E(Phi)-<F,R_e F>-e||R_e F||^2.

The last term tends to zero. In spectral measure dmu_F(lambda), write
its integrand as [e lambda/(lambda+e)^2] dmu_F(lambda)/lambda.
The bracket is at most 1/4 and tends to zero for lambda>0; the inverse
form is finite and has no zero-energy atom. Dominated convergence applies.
If T(z)=0, therefore, the full nonnegative row energy tends to zero.

The already constructed Green response gives u_e a finite pointwise limit
u_0=-G_H(0)F on each orbit. Since each row has finite input support,
L_row(Phi+u_e) converges to L_row(Phi+u_0). Its energy tending to zero
forces every one of these limiting rows to vanish. No l2 convergence of
u_e, or even square-summability of u_0, is used.

## The spectator pin excludes this pointwise row kernel

Fix a residual two-site occupation word eta. Lift the orbit amplitudes
to a simultaneous-translation-invariant function of actual occupation
configurations. Put f_A(x)=(Q_A(x)psi_0)(eta), where psi_0=Phi+u_0.
The W rows give f_A(x+e_k)=f_A(x) for all x,k, so each f_A is constant
on the connected infinite lattice. This conclusion is pointwise and
does not depend on a torus or summability.

Let the two constant E amplitudes be a,b. The singlet row supplies
d_1+d_2+d_3=0 at every center, and elementary inversion gives

    d_1=a/sqrt2+b/sqrt6,
    d_2=-a/sqrt2+b/sqrt6,
    d_3=-2b/sqrt6.

Thus each bare axial output amplitude is constant in x. In any plane,
the complement rows set the four signed bare amplitudes v_r equal.
Since Q_T=(1/2)sum_r v_r, each is Q_T/2 and is also constant.
The signs are the actual signed plane words; replacing them by unsigned
pair amplitudes would not be this argument.

Choose y occupied in eta. For a given bare type with endpoints x+u,x+v,
choose x=y-u. Its output at eta is exactly zero: annihilation at y
leaves y empty and cannot output a word that occupies y. This uses the
hard-core tensor-factor annihilator, not a dilute or bosonic approximation.
Constancy then forces that bare amplitude to be zero for every center.
It applies separately to every residual word and all fifteen bare types.

There are two valid ways to finish. The extension uses the stationary
equation and the original expression for H: all collective pair actions
vanish, leaving (4mu+V3)psi_0=0. Stationarity follows pointwise from the
finite-row resolvent equation and the existing pointwise limit.

An independent, slightly shorter finish needs no stationary equation.
Every configuration containing a G edge can have that edge removed by
one of the actual bare annihilators. Its amplitude must therefore vanish.
If a configuration has no G edge, all four graph degrees are zero and
D=4. Its diagonal positive row, already zero, also forces its coefficient
to vanish. Hence the pointwise common row kernel is zero in N=4.
This proves psi_0=0 using only the SOS rows and the pin.

## The prescribed incoming vector survives at infinity

At zero pair momentum, the five normalized vectors are E1,E2 and the
three T vectors divided by sqrt2, in the actual orthonormal nine-bond
cell. Let U be the 9-by-5 isometric matrix of these vectors. A constant
incoming z in Sym^2 C^5 maps injectively to the symmetric tensor UZU^T,
with the usual sqrt2 factors in the off-diagonal symmetric coordinates.
Multiplying by a left inverse of U on each factor proves injectivity;
this is valid for complex z and does not confuse transpose with adjoint
in the symmetric tensor embedding.

Consequently a nonzero z has a nonzero coefficient for some pair of
physical internal bond types. Take their separation to infinity. Beyond
the finite collision hole, the two disconnected edges have a unique
matching, so the actual occupation profile has this fixed nonzero
amplitude, up to the fixed positive exchange normalization. The matching
sum cannot cancel it there. Removing a finite hole cannot remove this
sequence. The response G_H(0)F decays on that sequence by the already
checked exterior Green construction. Hence psi_0 cannot be identically
zero. This contradicts the pin conclusion if z is nonzero.

## Consequence and limits

The exact finite Hermitian form therefore satisfies T(z)>0 for z!=0.
Compactness of the unit sphere in its fifteen-dimensional incoming space
then gives a positive smallest eigenvalue for each fixed mu,tau>0. This
argument gives no numerical eigenvalue, practical conditioning estimate,
or lower bound uniform as either coupling tends to zero. No new equality
between bare pulse quartics and relaxed threshold data has been asserted.

The existence of the decaying threshold response is essential. A local
pin excludes pointwise zero SOS solutions, but alone would not exclude
a zero infimum approached without such a limit in an affine scattering
class. Here the earlier three-dimensional inverse construction supplies
that missing compactness and asymptotic control. The proof does not
transfer automatically to another dimension, total momentum, coupling
boundary, or infinite incoming channel space.

There is no assertion about positive-energy flux normalization, on-shell
cross sections, asymptotic completeness, a dilute-gas expansion, a phase,
tensor modes, physical records, or adoption of the supplied Hamiltonian.
Only the precise constant-channel threshold form is strengthened from
semidefinite to positive definite. No source files were changed.
