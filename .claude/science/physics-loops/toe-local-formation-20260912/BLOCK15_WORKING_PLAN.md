# Low-energy operator linearization of the actual native star

2026-09-13, personal derivation-first campaign, no agents. The scalar/spectral
PR8086 now has head7b03ad8d4b160c002f0a0c9bedeba10f8eab02c7. Its author checks
pass, independent source review is pending. Main remains cda8b1445e21b3908a0a520710e0dae57b7bc3a3.

## Selection and novelty

The exact third-star source a814da6cc1178ac015914c9088fc04b2e635963e was reread.
It already gives the simple quadratic diagnostic frequencies
(sqrt(omega²+4m²)±omega)/2 and explicitly refuses its use as the native full
operator. Its L4 filled-six-mode counterexample proves that the full star
operator is not its linear vacuum creator on all active states. Repeating
either observation is not the next target. The older branch named
hybridization-mechanism concerns Dirac–Kahler cutoff rather than this native
star. Preliminary primary-literature searches found general hybridized-band
comparators, but no external result is used as a premise in this route.

Target: for the actual infinite bounded Hermitian odd operator
O=(1/8)sum_disjoint R_C gamma0 R_A, derive a norm estimate for
P_E(O-alpha gamma0)P_E as E→0, where P_E=1_(H0<=E) includes all particle
numbers. A vacuum transition estimate alone is insufficient. The intended
success is a local operator estimate, not a uniform many-body phase theorem
for the extensive sum over centers. The source's high-energy counterexample
must remain valid and outside this energy domain.

Inputs: the same supplied native K, CAR and Gaussian Fock H0; parent
D_A>=h/4 and7<h²alpha<330; Block14's directly derived one-particle amplitude
and remainder. The new low/high split below must establish its own operator
domains, norm bounds and spectral compression. No new physical premise.

## Proposed proof mechanism, before checks

Split the real one-particle space at energy Lambda using the spectral
projector of omega. In the doubled cell it is a scalar band cutoff, so every
site has low-field norm t=sqrt(v(Lambda)),
v=integral_(omega<=Lambda)dk/(2pi)^3<=pi(Lambda/h)^3/48.
For d_A supported on two neighbors, ||d_low||<=2h t. Write g=gH+gL,
d=dH+dL and B=Bhigh+W1+W2, with
Bhigh=i gH dH, W1=i(gH dL+gL dH), W2=i gL dL.
Then ||W1||<=4h t and ||W2||<=2h t².

High/low Fock factorization is graded; all high vacua are even. Taking the
low-vacuum expectation of D>=h/4 shows
Dhigh=Hhigh+Bhigh>=h/4-2h t². The mixed term has zero low-vacuum expectation.
This is stronger than subtracting its full O(t) norm. Hence the high-only
defects retain a gap for a small cutoff.

Introduce complex s, D_A(s)=Dhigh,A+Hlow+sW1,A+s²W2,A,
g(s)=gH+s gL and the high-vacuum expectation of O(s). Choose rho=1/128,
|s|=rho/t. For t<=rho, the perturbation norm is at most
h(4rho+2rho²)<h/16, Dhigh>=h/5, and every inverse norm is at most8/h.
Thus ||O(s)||<=720(1+rho)/h²<726/h². High parity makes its high-vacuum
expectation odd in s. Cauchy coefficient estimates then bound its tail
after the linear coefficient by (4/3)*726*(t/rho)^3/h² for t<=rho/2.
This controls the full soft-mode Fock space, regardless of particle number.

The coefficient linear in s has two inverses and gL, or three inverses,
one W1 and gH (two placements). It still depends on Hlow in its resolvents.
On an input of total free energy<=E, a single low linear field raises the
energy by at most Lambda. Replacing Hlow by0 in these finitely many terms
therefore has error at most
(90/8)*t(E+Lambda)[2(h/8)^-3+24h(h/8)^-4]
=1,117,440*t(E+Lambda)/h³.
The resulting coefficient is a Hermitian linear low field.

Its vacuum one-particle vector differs from the exact low one-particle
component of chi=O Omega by the same tail plus the preceding error atE=0.
The isometry between a Hermitian linear CAR field norm and its vacuum vector
then identifies a linear operator L_Lambda with the exact restricted chi
amplitude. Combining estimates at Lambda=E should give
||P_E(O-L_E)P_E||<=2*tail+3*1,117,440*tE/h³.
Block14 gives ||L_E-alpha g_low||<=95040*pi*tE/(2h³).
Consequently the actual compressed star should obey an O(E^(5/2)) operator
remainder, relative O(E/h) to the norm alpha t of its linear part.

Check carefully: domain of unbounded Hlow; analyticity of the bounded inverse;
graded partial expectation; oddness in s; intermediate low-energy support;
the creation-plus-annihilation norm identification; exact Fourier cutoff and
the difference between a norm on all soft Fock states and the total-energy
projection P_E. This is not a Gaussianity assumption on the input state.

## Decisive verification and limits

Write the proof before the checker. Check the complex-radius constants by
exact rational arithmetic. Use a distinct finite high/low CAR Fock fixture
to test actual partial expectations, parity, the first analytic coefficient,
Neumann tail and energy-support compression. Include a multiple-low-particle
input so the result is not a disguised vacuum-vector check. Verify that an
unrestricted high-energy state still violates the linear replacement.
No native large-volume diagonalization or infrared fit is required.

If the operator estimate succeeds, it improves the local low-energy vertex
control needed for a joint active/spectator treatment. It still does not
control the volume sum, higher electric orders, energy dependence of the
physical Feshbach operator, ground-state reorganization or the interacting
phase. Those are separate obligations, not consequences of a small local
error. Retain all failures and stop at the authorized11:38:24UTC deadline.
