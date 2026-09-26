# Relative entropy and the energy flux of the transverse wave sector

Status: primary derivation; separate check pending. Dependencies are the
supplied fifteen-state construction and its exact product current. This is
an effective classical wave-energy identity, not an identification of a
microscopic physical energy, temperature, Planck constant or photon field.

## 1. Exact nonlinear entropy pair

Use the fourteen independent occupied probabilities p, with p0=1-sum p_a.
At full support let C=diag(p)-p p^T and

    h(p)=sum_{a=0}^{14} p_a log p_a,
    theta_a=log(p_a/p0),      D^2 h=C^{-1}.

The construction has Psi_i(p)=gamma (X cross Y)_i and J_i=C grad Psi_i.
Consequently its smooth conservation law has the entropy flux

    q_i(p)=theta dot J_i-Psi_i.

Indeed D q_i=(D theta) J_i+theta D J_i-D Psi_i=theta D J_i,
since (D theta)J_i=C^{-1}C grad Psi_i=grad Psi_i. Multiplying
p_t+sum_i partial_i J_i=0 by theta therefore gives exactly

    partial_t h + div q=0

for a smooth interior solution. No closure beyond the proved continuum
equation is used in this identity; shocks and microscopic trajectories are
outside its stated scope.

Fix the isotropic reference product pbar with masses rho_A,rho_B and vacancy
1-rho_A-rho_B, all positive. Then Xbar=Ybar=0, J(pbar)=0, Psi(pbar)=0 and
grad Psi(pbar)=0. Its relative entropy and relative flux are

    h_rel(p)=sum_{a=0}^{14} p_a log(p_a/pbar_a),
    q_rel,i=(theta-thetabar) dot J_i-Psi_i.

Subtracting the conserved linear functional thetabar dot p gives
partial_t h_rel+div q_rel=0. Strict convexity gives h_rel>=0, with equality
only at p=pbar. This entropy is a function of the local probability profile;
it is not the sum of a fixed energy attached to each microscopic record.

## 2. Quadratic energy and Poynting form

Write p=pbar+epsilon u. Keep arbitrary perturbations of all fourteen fields.
The quadratic entropy is one half the inverse-covariance form. At the
isotropic reference the vector fields have covariances

    C_X=(rho_A/3) I,       C_Y=rho_B I,

and are uncorrelated with one another and with the remaining eight fields.
On the subspace where only X and Y vary, the quadratic part is

    E_wave = 3 |X|^2/(2 rho_A) + |Y|^2/(2 rho_B).

Here X,Y denote first-order field perturbations, with the epsilon^2 factor
suppressed. The full quadratic entropy also contains the positive form of
the other eight fields. Their linear time derivatives vanish. Longitudinal
parts of X,Y are additional static components, bringing the total static
sector to ten directions for each nonzero Fourier vector.

Because Psi is quadratic in the field deviations, the leading terms in
(theta-thetabar) dot J and Psi obey

    (D^2 h u) dot (D J_i u)=u dot D^2 Psi_i u=2 Psi_i(u).

Thus the quadratic relative entropy flux is exactly

    S_wave=gamma X cross Y.

It also follows directly from the linear equations
X_t=gamma rho_A/3 curl Y, Y_t=-gamma rho_B curl X:

    partial_t E_wave
      =gamma [X dot curl Y-Y dot curl X]
      =-div(gamma X cross Y).

After normalization E=X/sqrt(rho_A/3), B=Y/sqrt(rho_B),
the formulas become E_wave=(|E|^2+|B|^2)/2 and
S_wave=c_signed E cross B, where c_signed=gamma sqrt(rho_A rho_B/3).
For positive gamma this is the usual Poynting form for the normalized linear
Maxwell system. Negative gamma reverses the convention for the two curl
equations; changing B's sign makes the speed positive.

For fixed interior pbar and a bounded perturbation direction, Taylor
remainders in both relative entropy and relative flux are O(epsilon^3).
No assertion of an exactly quadratic nonlinear energy or exactly Maxwell
nonlinear dynamics follows. Formation would add the entropy source
(theta-thetabar) dot B_reaction; it need not conserve this wave energy.

## 3. Momentum and the missing physical identification

If the two normalized fields additionally satisfy div E=div B=0, their linear
curl equations imply the usual quadratic Maxwell stress identity. With
positive speed c, define

    P=(E cross B)/c,
    T_ij=1/2(|E|^2+|B|^2) delta_ij-E_i E_j-B_i B_j.

Then partial_t P_i+partial_j T_ij=0. Without the divergence constraints the
right side is -(div E) E_i-(div B) B_i, with these definitions. The linear
system preserves the two divergences but the stationary product does not set
them to zero. Therefore a charge-free momentum interpretation requires a
specified transverse sector; it is not an additional microscopic conservation
law proved for arbitrary configurations.

The exact microscopic conserved quantities of the exchange process are the
fifteen label counts (fourteen independent once volume is fixed). E_wave and
P are quadratic functions of coarse fields, rather than additive fixed
properties of individual labels. The entropy identity provides a natural
positive energy form for the wave sector. Identifying it with measured energy,
coupling it to matter or gravity, or assigning quantum commutators remains a
separate physics obligation. The commuting record fields and their product
Gaussian limit have not acquired quantum commutation relations here.

## 4. Second-order record transport follows changes in wave energy

The exact species current also gives the separate orbit-occupancy currents

    J_rhoA=(1-2rho_A) Psi,    J_rhoB=(1-2rho_B) Psi,
    J_rho=2p0 Psi,           Psi=gamma X cross Y.

Consider a differentiable one-parameter family of smooth interior solutions
near the isotropic background. Suppose its first-order perturbation has only
the X,Y wave fields. Let rho_A^(2),rho_B^(2) denote the coefficients of
epsilon^2 in the density expansion, without a factorial convention. The
exact currents and the quadratic energy identity then imply

    partial_t [rho_A^(2)-(1-2rhobar_A) E_wave]=0,
    partial_t [rho_B^(2)-(1-2rhobar_B) E_wave]=0,
    partial_t [rho^(2)-2pbar0 E_wave]=0.

These identities allow arbitrary time-independent spatial offsets set by
the initial profile. They do not say that record count equals wave energy
for every state. If the initial second-order densities satisfy the displayed
proportionality, they continue to do so at that order. If the initial density
is instead flat, its later perturbation is proportional to the *change* in
wave energy since that initial time.

This is a concrete local relation between permanent-record transport and the
energy flow of the small-amplitude wave. Its coefficient is the chosen
background vacancy fraction, not a universal conversion between record number
and physical energy. Other second-order moments are generally generated and
must not be discarded when computing higher-order dynamics. Existence of the
differentiable smooth solution family is an explicit premise here; this
calculation does not extend the solution through a shock or justify an
unbounded-time perturbation expansion.

## 5. Relation to earlier lattice Maxwell constructions

Recovering a Maxwell-form continuum system from supplied lattice dynamics is
established methodology. Mendoza and Munoz use auxiliary electric/magnetic
vectors and BGK relaxation with selected equilibrium distributions;
Hanasoge, Succi and Orszag use a pseudovector distribution and a BGK scheme.
The relevant construction and moment equations were read in their primary
papers, rather than relying only on abstracts:

- https://arxiv.org/abs/0806.2678v2, Section II, equations (1)-(20).
- https://arxiv.org/abs/1108.2651, construction through equations (7)-(18).

Those methods motivate no novelty claim for a lattice Maxwell limit. The
present bounded question is whether a finite alphabet of immutable labels,
with positive stochastic exchange rates and a proved product fluctuation
limit, can support that linear sector. The cited BGK schemes are not imported
as limit theorems for this different Markov generator.
