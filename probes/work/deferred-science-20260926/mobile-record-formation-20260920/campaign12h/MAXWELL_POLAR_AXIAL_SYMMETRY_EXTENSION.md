# Polar/axial symmetry and physical time reversal of the transverse construction

Status: primary derivation; separate check pending. This extends
`IMMUTABLE_TRANSVERSE_MAXWELL_CONSTRUCTION.md` without changing its generator.
It specifies an additional interpretation of the two label orbits, rather than
inferring a parity action from the framework axioms.

The original note correctly observes that literal inversion of both geometric
tag vectors is not a symmetry of the rates. Electromagnetic electric and
magnetic fields transform differently under inversion. Giving the two record
orbits those different transformation laws restores the corresponding discrete
symmetries in this supplied model.

## 1. Full signed-coordinate group

Keep fifteen labels: vacancy; six A labels with e(a)=+/-e_i and b(a)=0;
eight B labels with e(a)=0 and b(a) in {+/-1}^3. The pair tensor is

    S_i(a,b) = gamma/2 [e(a) cross b(b) + e(b) cross b(a)]_i.

For any signed coordinate permutation R, define the state permutation P_R by

    e(P_R a)=R e(a),       b(P_R a)=det(R) R b(a).

Both finite orbits are closed under this action. It is a group action because
det(R1 R2)=det(R1)det(R2), and the displayed six components uniquely identify
every label. The cross-product transformation rule gives

    S(P_R a,P_R b)=R S(a,b).

Under an orientation-reversing image of a lattice bond, the ordered four-site
word reverses. Its drive h_i=S_i(l,a)+S_i(a,r)-S_i(l,b)-S_i(b,r) changes sign
under that reversal. The two signs therefore cancel, proving covariance of
the local rates under all 48 signed-coordinate transformations, including
improper ones. Both kappa+max(h,0) and K+h/2 have this property.

In particular, spatial inversion sends e to -e but keeps b fixed. It does
not replace b by -b. The earlier failed literal-inversion control remains a
valid counterexample to treating both fields as polar vectors.

This supplies the usual polar/axial parity distinction for the two linear
wave fields. It does not prove full continuous rotation symmetry of the
nonlinear microscopic law or identify either observable with a measured field.

## 2. Generalized time reversal

Define the on-site involution Theta by e(Theta a)=e(a), b(Theta a)=-b(a).
It fixes the vacancy and A labels and pairs the eight B labels. Then

    h_i(Theta eta)=-h_i(eta)=h_i(eta^edge),
    c_i(Theta eta)=c_i(eta^edge).

For any homogeneous full-support product, endpoint exchange preserves its
weight. Pointwise product balance makes the adjoint conservative generator
the jump generator with reversed rates c_i(eta^edge). Consequently, on
functions on a finite periodic lattice,

    L^* = Theta L Theta.

Here the adjoint is in that homogeneous product, and Theta f(eta)=f(Theta eta).
For a stationary path-law time-reversal interpretation, additionally require
the product to be Theta-invariant: p_b=p_{Theta b}. The orbit-isotropic
background used in the Maxwell limit has this property. These assumptions
give the local generalized detailed-balance identity

    pi(eta) c(eta,eta') =
        pi(Theta eta') c(Theta eta',Theta eta),

for an exchange eta'=eta^edge. The total escape rates agree under Theta
because sum_edges h=0, so the waiting-time factors also agree. Hence every
finite stationary trajectory and the trajectory obtained by reversing time
and applying Theta to every state have equal probabilities, including their
jump times. This is an exact finite-process statement; ordinary detailed
balance without Theta generally fails.

The involution is a comparison of histories, not an operation imposed on a
record during forward evolution. Every actual forward jump still only swaps
unchanged labels. The mathematical time-reversal convention treats the B
observable as odd and the A observable as even, as in the linear curl system.

The full fourteen-field linear current matrix A(K) obeys T A(K) T=-A(K),
where T is the induced field involution. The X and Y blocks have signs +1
and -1; the B triple product is also odd, although its linear transport speed
is zero. Together with covariance symmetry, this produces the time-reversal
identities of the finite-mode Gaussian limit. No quantum time-reversal
operator or Lorentz symmetry is asserted.

## 3. What this changes

This construction can support a transverse Maxwell-form linear system with
the appropriate discrete parity and time-reversal assignments while its
records remain immutable. The extra two-vector alphabet and its transformation
assignment remain supplied. The ten zero-speed fields, lack of a microscopic
Gauss constraint, density-dependent wave speed, nonlinear corrections and
missing charged-matter/quantum bridge are unchanged open obligations.

In particular, a thermal full-support product has nonzero longitudinal
fluctuations. The linear equations preserve their divergence; they do not
prepare the charge-free sector. Choosing a transverse initial condition is
a further restriction on states, not a consequence of immutable exchange.
