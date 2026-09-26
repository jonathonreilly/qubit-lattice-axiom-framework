# What can be changed by tuning immutable pair-exchange rates?

Primary derivation, 2026-09-21. This classifies a stated family of stochastic
rules. It neither selects that family from the axioms nor excludes other
moving-record dynamics. It strengthens the transport test by asking which
features depend on the particular streaming proposal and which persist
through the whole specified rate class.

## Assumptions

The local state set is a vacancy 0 and six immutable labels a with vectors
v_a=+/-e_i. All moves exchange the states at the endpoints of a nearest-neighbor
bond; rates depend only on those two states and the bond direction. Write
c_i(a,b)>=0 for the rate at an oriented positive-i bond, with a at its left
endpoint. Reversing the oriented bond means c_-i(a,b)=c_i(b,a). Rates are finite,
translation invariant and covariant under simultaneous proper cubic rotation
of the lattice and content labels. There is no insertion during this
stationary transport probe.

Assume a full-support homogeneous spatial product measure is invariant on
every cubic periodic torus of side at least three. A single side-three torus
already suffices for the necessity proof. This is a real additional premise;
spatially correlated invariant states are not covered.

## Product invariance forces a drift difference

Put h_i(a,b)=c_i(a,b)-c_i(b,a). Exchanging endpoint contents leaves any
homogeneous product configuration probability unchanged. The stationarity
equation at a configuration s is therefore exactly

sum_(x,i) h_i(s_x,s_(x+e_i))=0.

Choose a side-three torus configuration that is constant in the two transverse
directions and has successive layer contents a,b,c along i. The transverse
terms vanish, and stationarity gives

h_i(a,b)+h_i(b,c)+h_i(c,a)=0.

Taking c=0, define f_i(a)=h_i(a,0) and obtain
h_i(a,b)=f_i(a)-f_i(b), with f_i(0)=0. Conversely this condition makes each
line sum telescope, proving stationarity of every homogeneous product law on
all periodic tori. Bounded local dynamics then yields the infinite-volume
product invariant laws. Neither direction assumes an irreducible sector.

This drift-difference condition is the usual product-measure condition for
multispecies particle-exchange processes. See Schuetz and Zahra,
https://arxiv.org/abs/2605.07615v1, section 2, for the one-dimensional family
and exact currents. Here the layer argument makes the needed cubic-lattice
necessity explicit; no theorem for a different rate class is imported.

## Cubic covariance leaves one transport coefficient

Treat f(a)=(f_1(a),f_2(a),f_3(a)). Bond reversal makes its components odd
under direction reversal, and proper cubic covariance gives f(Ra)=R f(a).
A rotation by a quarter turn around v_a fixes the content a, so it fixes
f(a); hence f(a) is parallel to v_a. Cubic rotations act transitively on
the six contents, forcing one common real scalar u:

f(a)=u v_a,
h_i(a,b)=u(v_a,i-v_b,i).

The vacuum anchor removes any common additive drift. The symmetric part of
c_i(a,b) remains free subject to nonnegativity and cubic covariance. It can
change relaxation, fluctuations and finite-wavevector damping. The statement
above only classifies the antisymmetric currents. For any real u the
antisymmetric part is attainable, for example by forward or reversed
immutable streaming at speed |u|, with optional symmetric exchanges.

At homogeneous species probabilities p_a, the exact stationary currents are
therefore universally

J_a=u p_a(v_a-g),       g=sum_b p_b v_b.

This follows by summing p_a p_b h_i(a,b) over b, including the vacancy.
The six-field Euler current Jacobian, and the exact finite-time first spatial
moment of stationary correlations, are u times those in
`IMMUTABLE_STREAMING_DERIVATION.md`.

In particular, at isotropic p_a=rho/6 with 0<rho<1 and u!=0, the conditional
Euler characteristic values along a lattice axis are
+/-|u|sqrt(1-rho/3)|k| and four zeros. Along a body diagonal they are
+/-|u||k|/sqrt(3), each twice, and +/-|u|sqrt((1-rho)/3)|k|, each once.
The exact correlation first-moment identity gives the associated normal-mode
centers at every finite time; narrow waves or hydrodynamic poles still require
more. For u=0 all these first-moment velocities vanish, without excluding
diffusion or other fluctuating behavior.

Thus adding or tuning symmetric content-preserving pair exchanges within this
product-invariant class cannot alter its leading stationary-current symbol
or erase the extra conserved axis-population densities. It can alter terms
not determined by those currents. A claim that such tuning alone yields one
isotropic density sound field needs an additional argument or a changed
premise; the particular directional streaming rate is not the only issue.

## Surviving routes and precise limits

This is not a theorem about all permanent records or all conservative local
motion. Environment-dependent rates, more-than-two-site updates, correlated
stationary states, additional transported carrier variables, a different
content menu, quantum amplitudes, or nonstationary formation can change the
question. No such choice is adopted here. Merely adding a symmetric exchange
rate while retaining all the stated premises is covered by the proof.

The classification is algebraic and finite-local; it does not prove a
three-dimensional hydrodynamic limit, a relativistic field, a physical
speed, a phase transition, or a force. The scalar u remains unselected.
A nonuniform macroscopic law may have correlations beyond product closure.
Those limitations cannot be replaced by more finite PASS cases.

## Checks

The completed primary exact linear system imposes all 105 three-color cycle
conditions and all 24 proper cubic rotations on the 63 antisymmetric bond-rate
coordinates. The cycle constraints have rank 45; the combined system has
rank 62 and nullity one, with basis exactly v_a,i-v_b,i. Eight rate menus,
each with 343 full three-site color states, satisfy the stationary equations
and current formula. An oriented three-color cycle has incoming rate zero
and outgoing rate three at its witness configuration, violating product
stationarity as expected. Results and source identity are in
`PAIR_EXCHANGE_CLASSIFICATION_RESULTS.json`. A separate mathematical check is
still required before packaging a formal claim.
