# A one-qubit-compatible deformation of the fourteen-label birth law

2026-09-21. Primary conditional construction, not independently checked yet.
This changes the supplied birth kernel, retaining the previous immutable
classical exchange process. It is not the original rank7 law.

The quantum-interface obstruction suggests a constructive alternative.
Define a single Bloch feature s_a=e_a on A-axis labels and s_a=b_a/sqrt(3)
on B-cube labels, and choose

    W_ab=1+j s_a dot s_b,      0<|j|<1,
    birth rate(a at x)=(beta/N) product_(y nearest x)W_(a,eta_y),
    W_a0=1.                                                  (1)

Every W is positive and each single-parent column sums to14. For physical
parent preparations rho_b=(I+s_b dot sigma)/2, the POVM
E_a=(I+j s_a dot sigma)/14 reproduces W_ab/14 exactly. For k unknown
independent quantum parents, positive rate effects

    F_a=(beta/N) tensor_(r=1)^k(I+j s_a dot sigma_r)           (2)

reproduce all the product rates. A sufficiently short observed event
instrument can use sqrt(dt F_a), with no-event sqrt(I-dt sum_a F_a).
This is a positive one-event quantum interface; it disturbs parents and
does not establish the repeated classical waiting law or permanent unknown
physical parent states. Neither the formation clock nor j is selected.

The fourteen unit Bloch vectors obey sum_a s_a=0 and
sum_a s_a s_a^T=(14/3)I. Their equal input ensemble is a qubit projective
two-design at the order needed for average operation fidelity. The same
Kraus trace argument as the earlier six-axis interface therefore gives the
sharp parent-preservation fidelity, averaged over these fourteen inputs,

    F_max=(2+sqrt(1-j^2))/3.                               (2a)

The square-root effects attain it. Exact pure-parent preservation is
impossible for j!=0 in this specified ordinary quantum interface. This
single-operation optimum does not describe a repeated-event physical law.

Use the same raw moment fields X=sum p_a e_a,Y=sum p_a b_a,U=2X,V=Y.
The conditional product-replacement reaction law is now

    B_a=beta p0[1+j s_a dot (X+Y/sqrt(3))]^6.                (3)

At p_a=rho/14 the trajectory is still rho'=14beta(1-rho).
The exchange Maxwell coefficient remains c=2gamma rho/7. Put h=beta j(1-rho).
The complete vector reaction and exchange linearization is

    partial_t (U,V) = c(curl V,-curl U)
                   +4h [[3,2sqrt(3)],[2sqrt(3),4]] (U,V).   (4)

The density reaction eigenvalue is -14beta. The orbit difference, two A
quadrupoles, three B pair characters and B triple character retain zero
linear reaction. Thus all fourteen occupied species directions are still
accounted for; there is no removal of their readable degrees of freedom.

The reaction matrix in (4) has eigenvalues28h and0. Its driven combination
is P=(sqrt(3)U+2V)/sqrt(7); its undriven orthogonal combination can be
Q=(-2U+sqrt(3)V)/sqrt(7). This constant two-field rotation leaves the
antisymmetric curl coupling unchanged. Longitudinal raw components have
reaction eigenvalues28h and0. At a frozen background, each transverse
helicity has the two drift eigenvalues

    14h +/- sqrt((14h)^2-c^2|K|^2).                        (5)

Consequently complex oscillatory instantaneous modes remain when
c|K|>14|h|. At long wavelengths during active formation these frozen
eigenvalues are real. At saturation h=0 and the previous pure wave
frequencies return. With the actual time-dependent rho(t), matrices at
different times generally fail to commute, so (5) is not an integrated
phase formula or a global stability theorem. The finite-time matrix ODE
has to be solved with its time ordering retained.

There is nevertheless a controlled late-time statement about that matrix
ODE. The exchange block is anti-Hermitian in the U,V norm, while the
reaction block has eigenvalues28h and0. For any Fourier solution F(t),

    1 <= ||F(t)||/||F(s)|| <= exp[2j(rho(t)-rho(s))]       (6)

when j>0; for j<0 the same interval is reversed, with
exp[2j(rho(t)-rho(s))] <= the ratio <=1. The integral used here is
integral_s^t28h=2j(rho(t)-rho(s)). Thus transient amplification or damping
is finite even when frozen long-wavelength eigenvalues are real.

Let L_infinity be the pure exchange block at c_infinity=2gamma/7. The
coefficient remainder has the integrable norm bound

    ||L(t)-L_infinity||
      <=v0 exp(-14beta t)[28beta|j|+|c_infinity||K|].       (7)

The interaction-picture field Z(t)=exp(-L_infinity t)F(t) satisfies an ODE
with integrable coefficients and remains bounded by (6). Its integral
equation is Cauchy as t tends to infinity. The same argument for the inverse
fundamental matrix, or Liouville's determinant formula with finite integrated
trace, shows that its limiting linear map is invertible. Consequently every
fixed mode has a finite asymptotic free-wave amplitude Z_infinity, with

    F(t)=exp(L_infinity t)[Z_infinity+O(exp(-14beta t))].   (8)

The constant depends on the fixed mode and parameters. The longitudinal
zero-frequency parts are included; the transverse part oscillates at
|c_infinity||K|. This is a finite-dimensional linear scattering statement,
not a native stochastic fluctuation theorem or a spatial ultraviolet limit.

The curl readouts E=d cross V,B=-d cross U still have exact microscopic
Gauss identities for every event. Their linear reactions are obtained by
applying these curls to (4), with the corresponding fixed change of basis;
no claim that they obey the earlier equal scalar-gain formula is made.

There is a symmetry cost to this deformation under the previous full
polar/axial convention. A cross-orbit term e_A dot b_B/sqrt(3) changes sign
under an improper spatial rotation, since e is polar and b axial. It is
nonzero, for example for e_A=e_x and b_B=(1,1,1). Thus (1) is covariant
under all24 proper cubic rotations, but not under the48-element extension
used for the original law. The minimal axioms ask for the former; any
physical parity requirement is an additional obligation here. A handed
coupling, a different encoding, or a larger carrier changes that question.

This deformation demonstrates that the original rank7 mismatch belongs
to a specific supplied kernel. Positive one-qubit event rates and a
nontrivial classical propagating sector can coexist after changing that
kernel. Exact unknown-parent permanence, repeated quantum histories,
state selection, physical symmetry and field identification remain open.

Because (1) remains strictly positive and has the same equal-label
homogeneous trajectory, the conditional entropy extension and monotone
count argument of the local-curl note apply with these new weights as well.
From a fixed interior equal-label product start, in the same ordered
t->infinity at finite N followed by N->infinity limit, the selected full
occupancy law is again locally product. Its scaled-curl covariance is again
(4/7)(|K|^2I-KK^T). The changed quantum event interface therefore does not
by itself produce either of the desired correlated comparator states.
