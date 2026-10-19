<!-- Original PR9814 source SHA256 b4ef42cc8dff5c12b5a008a2fa8f2a86141d289ffa9e32c13a962ccfc760456d. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Original readout of native whole-column features

Status: bounded-support. Root derives static contrast and the first winding
coefficient of the original observable. The supplied Hamiltonian, weak regime,
reference/quasimode family and original readout remain explicit premises.
No added interaction, empirical scalar normalization or gravitational charge.

## 1. Differentiation is bookkeeping, with its connection checked

H=-J sum[ZZ_z+lambda XX_x+lambda YY_y] and
C_Q=V^-1/2 sum_r exp[-iQ.(r+ez)]Z_r Z_(r+2ez).
Introduce a formal real parameter h multiplying a Hermitian component of C_Q
only to differentiate the original operator at h=0. This does not choose a
new physical Hamiltonian or an adjustable coupling. For a canonical real
normal-form U(h), A=(partial_h U)U^dagger and

 partial_h H_eff=C_eff+[PAP,H_eff].                            (1)

The connection must not normally be discarded. In the native word-preserving
gauge on N0, any coefficient of PAP below the minimal whole-column order L
is diagonal by locality/flip count. Being real antisymmetric, it is zero.
The first offdiagonal coefficient is order L, while H_eff on N0 is scalar
below order4. Hence the connection cannot change the first winding order-L
observable coefficient; its first possible contribution is order L+4.
For a proper local diagonal square coefficient the same argument, or an
isolated ordered local reference, establishes the diagonal derivative through
order4. Arbitrary nonlocal h-dependent block rotations are not being admitted.
For complex Fourier C_Q apply the real result to cosine and sine components
and combine linearly.

## 2. Static coefficient and native spatial form factor

A same-z transverse square is the only orientation-dependent four-edge return
word. A proper subset leaves k flipped spins on its four vertices. Its wall
cost is4Jk. For uniform C0 each flipped spin changes two distance-two bonds,
so its source change is -4k/sqrt(V). Holding the transverse interaction Jlambda
fixed, its perturbed denominator is4k(J-h/sqrt(V)). Thus the square's energy
coefficient and source derivative are

 -J^4 lambda^4 P/[128(J-h/sqrt(V))^3],
 -3 lambda^4 P/[128 sqrt(V)] at h=0.                           (2)

Repeated-edge return graphs are orientation independent, as in the direct
local tension proof. Their differentiated denominators also remain independent
of column signs, so they do not supply a competing contrast.

For nonuniform Fourier source, a flipped vertex r changes C_Q by
-4 cos(Qz)exp(-iQ.r)/sqrt(V). Marking each of the four vertices in the24
square orderings gives the same coefficient -3P/512. The root exact rational
control checks all16 column sign patterns and four marked vertices separately.
Consequently the leading orientation-dependent source on wall-free columns is

 C_eff,Q^(4)=-3lambda^4/(128sqrt(V)) cos(Qz)cos(Qx/2)cos(Qy/2)
              sum_(p,z) exp[-iQ.center(p,z)] P_p.              (3)

The plaquette center is displaced by(ex+ey)/2 from its lower corner; its z
coordinate is the layer of the virtual square. This fixes all Fourier phases.
Orientation-independent terms are omitted because they cancel from feature
contrast. Equation(3) is a derived measurement form factor, not a new mode.

## 3. Actual dressed-feature contrast

Use even L~lambda^-p,0<p<4, fixed high normal-form order n, and the large
whole-column rectangles of WHOLE_COLUMN_MODE_PROOF.md. All four bad plaquettes
repeat on every layer. For Qz=0 the contrast of the dressed rectangle relative
to any actual ground vector is

 Delta<C_Q>=3lambda^4 L/(64sqrt(V)) cos(Qx/2)cos(Qy/2)
                 sum_four_corners exp[-iQ.corner]
            +O_n(lambda^5 L/sqrt(V))
            +O_n(lambda^(n-3-7p/2)).                          (4)

For nonzero allowed Qz the expectation of the dressed feature and the actual
ground is exactly zero: both have longitudinal translation character zero.
The source coefficients are proper local and plane invariant; their diagonal
column polynomials satisfy the same row/column even-incidence rule as the
energy. Hence their higher-order contrast is supported near the four corners
and bounded by O_n(lambda^5 L/sqrt(V)), not an extensive-volume error.
The exact-source tail is O_n(sqrt(V)lambda^(n+1)). Replacing the coefficient
ground by any actual ground costs O_n(sqrt(V)r_n/g0), as proved in the
whole-column block; this gives the final error in(4). Uniformity covers
arbitrary ground mixtures. The feature is a specified dressed quasimode,
not an assertion that an isolated exact particle eigenstate exists.

At Q=0, take n40 (or n>=8+4p) so the relative error is O(lambda):

 Delta<C_0>=3lambda^4 L/(16sqrt(V))[1+O_n(lambda)]
           =3Delta_4/(J sqrt(V))[1+O_n(lambda)],              (5)
 Delta_4=J L lambda^4/16.

If n only barely exceeds7+4p, retain the additional relative error
O_n(lambda^(n-7-4p)) instead of absorbing it in O(lambda). In particular n40
allows the displayed O(lambda) throughout0<p<4. At nonzero-Q zeros of the
leading form factor, (4) is an absolute bound, not a relative approximation.
The normalization sqrt(V) belongs to the originally defined C_Q.

Equation(5) is a leading static energy/readout relation for this family.
It does not identify that contrast with a gravitational charge, prove a
universal relation for other modes, or overcome the low-frequency inelastic
darkness already established for the original ground-state readout.

## 4. Exact first winding observable coefficient

Now hold even L>4 fixed. A minimal two-column winding path flips a proper
subset S of rungs, with c(S) cyclic occupied clusters. Define
 d2(S)=#{z:1_S(z)!=1_S(z+2)}.
The same path's energy and original uniform-source differences are
 8J c(S), -4d2(S)/sqrt(V).
Differentiating all L-1 native denominators of the first winding coefficient
-gamma_L gives the aligned-column-basis source term

 C_eff,0,wind=-gamma_L A_L/(2J sqrt(V)) sum_<ij> Xbar_i Xbar_j,
 A_L=S_L^-1 sum_paths [product_k1/c(S_k)] sum_k d2(S_k)/c(S_k),
 S_L=binomial(2L-2,L-1).                                     (6)

The sign and normalization follow directly from differentiating inverse
positive excitation costs: gamma'(0)>0 and the Hamiltonian term is-gamma.
This is an operator matrix element in a reference basis, not automatically
an inelastic transition between exact eigenstates. For an isolated tunneling
doublet the displayed source is parallel to its Hamiltonian and parity diagonal.

## 5. Closed evaluation of the marked Catalan paths

Write n1o,n1e for the numbers of singleton occupied and empty runs. Directly
counting boundaries gives d2=4c-2(n1o+n1e). Reversing a permutation complements
its partial subsets in reverse order. Since c(S)=c(complement S), all path
weights are preserved and the total marked occupied/empty contributions equal.

Deform only the combinatorial recursion denominator to c+eta n1o. Its proper
subset sum factorizes over occupied runs: F_eta(S)=product_a f_(ell_a)(eta),
where f0=1 and

 (1+eta delta_(ell,1)) f_ell=sum_(a=0)^(ell-1) f_a f_(ell-1-a).

This follows by summing removals within each run and then summing runs, which
reconstructs c+eta n1o. At eta0 f_ell is Catalan(ell). The generating function
f(z)=sum f_ell z^ell satisfies
 f=1+z f²-eta z/(1+eta).
Its derivative at0 is G(z)=-z/sqrt(1-4z), so
 f_ell'(0)=-binomial(2ell-2,ell-1).
The completed path sum is L f_(L-1); there is no denominator for the full set.
Therefore the normalized occupied-singleton mark is

 E_weighted sum_k n1o(S_k)/c(S_k)
    =L binomial(2L-4,L-2)/S_L=L(L-1)/[2(2L-3)].

Combining this with the boundary count yields the exact formula

 A_L=6(L-1)(L-2)/(2L-3),
 C_eff,0,wind=-3gamma_L(L-1)(L-2)/[J sqrt(V)(2L-3)]
                     sum_<ij> Xbar_i Xbar_j.                 (7)

This is proved combinatorially, not inferred from the finite numerical list.
It is still a fixed-L Taylor coefficient. Neither(6) nor(7) establishes
uniform dominance in growingL, a transition rate, or a long-time propagator.

## 6. Validation and residuals

Exact rational controls check all marked subset paths throughL16, all16 square
references, and the marked local vertices. A restricted two-column rung model
checks virtual-dressing matrix elements directly in even/odd parity eigenstates;
it is a coefficient control, not a replacement of the full physical lattice.
Independent checks cover source connection, static contrast, and the closed
marked-Catalan proof. No empirical data were calibrated or held out.

Derived here: original-readout static profile and finite-size winding
coefficient, from the same native interaction. Remaining: dynamical access to
a useful light collective field, actual detector identification and preparation,
cosmological state/scale, relativistic propagation and universality across matter.

## 7. Test of an energy-proportional operator interpretation

At fixed even L>4, suppose the wall-free original source were exactly
C_eff=c(lambda)I+g(lambda)H_eff, with regular Taylor g and the same native
unitary for both operators. The order-four nonconstant plaquette term forces
g(0)=3/(J sqrt(V)). The first offdiagonal winding term instead forces
g(0)=A_L/(2J sqrt(V)). For every integer L>4 these disagree:
A_L/2=3(L-1)(L-2)/(2L-3) !=3. Higher Taylor coefficients of g cannot repair
the order-L offdiagonal equality, because H_eff has no offdiagonal term belowL.
Thus that simple universal energy-proportional operator ansatz fails in the
same native effective block. This is not an equivalence-principle test or a
no-go for another detector or emergent field; it identifies precisely which
extra measurement identification has not been derived.
