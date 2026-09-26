# Formation clocks, acoustic travel, and what a capturing source must store

Personal campaign analysis, 2026-09-21. These are conditional consequences
and model-comparison obligations, not an adopted dynamics or a gravity claim.
The all-density current is separately checked; the growing fluctuation proof
is still a candidate. None of this file is an independent audit result.

## 1. A finite acoustic travel budget under a constant birth clock

For the axis-balanced immutable exchange, an isotropic homogeneous product
has instantaneous linear characteristic speed

`c(rho)=2 |alpha| rho sqrt((1-rho)/3)`.

With a fixed macroscopic per-label birth rate beta>0,
`v(t)=1-rho(t)=v(0) exp(-6 beta t)`. The total remaining characteristic
travel in the candidate linear continuum equation is therefore exactly

`H(t)=integral_t^infinity c(rho(s)) ds`
`    = [2 |alpha|/(3 beta sqrt(3))] [sqrt(v(t))-v(t)^(3/2)/3]`. (1)

Differentiate (1) to obtain H'=-c and use H(infinity)=0. For alpha=1,
beta=.04 and initial density .5 this is approximately 5.6701 macroscopic
length units. A time-dependent hyperbolic equation's finite characteristic
budget is not a hard light cone for the microscopic stochastic process:
exchange diffusion and rare graphical paths are outside this leading Euler
characteristic statement. No uniform-in-time fluctuation limit has been proved.
The fixed-T continuum theorem cannot itself justify exchanging T->infinity
with N->infinity; (1) is a property of the resulting coefficient function.

For a supplied nonnegative time-varying per-label rate beta(t), homogeneous
products still have
`v(t)=v(0) exp[-6 integral_0^t beta(s)ds]`.
The same characteristic calculation gives the explicit criterion
`integral_0^infinity rho(t) sqrt(v(t))dt` for unlimited acoustic travel.
If beta(t)=b/(1+t), b>0, the asymptotic speed is proportional to t^(-3b),
so this integral diverges for b<=1/3 and converges for b>1/3. If total
integrated formation rate is finite and the limiting density is interior,
the speed tends to a positive constant. These are clock-dependent outcomes;
none selects a preferred clock from the axioms. The earlier fixed-positive-
birth-clock fixation theorem and these time-varying examples have different
hypotheses.

## 2. Exact bookkeeping for a finite capturing body

PR #8553 appeared during this campaign at head
`e07ae767d484763bd9446eb2d5c4c9b05643dd1c`, based on main
`5d784d8ccda5268f2b7c056fcdf0d81fdb703319`.
Its complete theorem note and three simulation source files were read at
that revision; the complete PR and its exact runner have not yet been
reviewed. The note explicitly supplies scattering that redraws contents,
a capture clause and a local-equilibrium closure. Those assumptions differ
from the present immutable-exchange constructions.

A finite region B with one record per site has the exact number balance

`N_B(t)-N_B(0)=C_in(t)-C_out(t)+C_birth,B(t)`,                  (2)

provided records are not destroyed and no unmodeled storage is used.
For a body with fixed capacity |B|, no outflow and no internal annihilation,
its cumulative inflow cannot exceed |B|-N_B(0); births consume additional
capacity. If it is intended to capture indefinitely, its storage region must
grow, records must move onward, or another explicit state capacity must be
supplied. Equation (2) identifies the missing construction; it does not rule
out those alternatives.

The checked simulation source
`supervisor_control_block45_inertial.py`, SHA
`7da5bff6e2e91e3191805264b5a477a8cdb1af96d373bbda1c1ffa0ebc8de34f`,
sets the incoming gas site's occupancy to false on capture and adds momentum
and one unit to cumulative counters. It does not instantiate the captured
record at another modeled site. The body geometry stays fixed. The companion
`supervisor_control_block45_bodies.py`, SHA
`da02bf5f3a26d26a99bb944bc0ede53a041c3360c0056d55b9c67ec0d8b091aa`,
resamples an external boundary reservoir, including occupied contents. This
is a legitimate supplied open-system sink/reservoir computation, but it is
not yet a closed realization of permanent records with finite body capacity.
A cumulative capture counter records how much the sink absorbed; it does
not specify an accessible one-record-per-site storage construction.

The representative fixed radius-three body contains 123 solid sites, while
the reported Q about 7.8 over 8000 measured ticks corresponds to about 62400
captured records, before warm-up. Its successful steady gas flow therefore
cannot by itself establish a finite-capacity permanent-record body. No claim
is made that the PR author intended the counters to provide such a body.

## 3. Net flux, gross capture, and formation between surfaces

For a stationary annulus with no births, the flux through its outer surface
is the NET number absorbed by its interior, Q_in-Q_out. If a body's record
count is stationary and its only number changes are capture and emission,
that net is zero even when its gross capture rate is positive. Consequently
reusing the inverse-square NUMBER-wind coefficient requires the net rate,
not silently the gross capture rate. A force from stresses or other channels
is a different question and is not excluded by this number identity.

When new records form in the annulus, (2) instead gives, for inward-oriented
current,

`Phi_in(outer)=Q_net,body - total_birth_rate(annulus)`           (3)

in a stationary state. In a transient state one must also include the rate
of change of the annulus's stored records. Thus a constant radial number flux
is not automatically available in a growing medium. Conservation remains
useful, but the formation and storage terms must be kept.

If captured records add to a body's proposed inertial record count,
`dM/dt=Q_net`. Interpreting a force as absorbed carrier momentum then also
requires a variable-mass momentum equation and a record-to-inertial-mass
bridge. Those are explicit next obligations, not consequences of a 1/r^2
flow profile.

## 4. A known constructive alternative worth keeping distinct

A localized formation source in an infinite symmetric exclusion process can
continue to supply records which diffuse away. In d>=3 the exact one-point
Green-function solution has a positive limiting injection rate. This is
established prior art: P. L. Krapivsky, [Symmetric exclusion process with a
localized source](https://arxiv.org/abs/1208.3250), especially section IV.B.
Its source is spatially supplied and its carrier is diffusive. It is an
available route around finite-source saturation, not a new result of this
campaign or an automatic acoustic/gravitational construction.

The new constructions establish that immutability is compatible with local
formation and, under selected rates, isotropic linear waves. Selecting a
physical clock, a persistent source/storage mechanism, and a response law
for bodies remains the task needed to turn this flexibility into a
predictive physical theory.

## 5. A scoped correction to PR8553's six-axis flux statement

After the initial source comparison above, the complete exact runner and
refuter were also read. The runner's family D and the refuter's W4 check
one-site moments, but their stated conclusion that the six-axis momentum
flux has no g_i g_j term omits the contribution of exchanges. For six-axis
unit-rate streaming the exact full product flux is

`Pi_ij=delta_ij q_i-g_i g_j`.                                 (4)

For an i-edge, a left +i record and a right -i record supply the two possible
streaming attempts. Each accepted exchange transfers v_left-v_right, giving
`p_(+i)(e_i-g)+p_(-i)(g+e_i)=q_i e_i-g_i g`. Homogeneous tilted-product
scattering contributes zero mean current. A rational tilted-product witness
has probabilities (vacancy,+x,-x,+y,-y,+z,-z)

`(18,12,3,18,2,6,6)/65`.

Its occupied weights are proportional to (2,1/2,3,1/3,1,1), so this is within
the note's exp(lambda.s) family, with lambda=(log2,log3,0). It has
`g_x=9/65`, `g_y=16/65`, hence `Pi_xy=-144/4225`, not zero.
`pr8553_six_axis_flux_counterexample.py` enumerates all 49 ordered endpoint
cases directly from event transfers and again through the ORIGINAL refuter's
bond_flux function, with source hashes enforced. Both give the same nonzero
rational value. The original runner's family D still passes its two checks,
demonstrating the missing current-level coverage.

The correct small-tilt tensor is

`Pi = (rho/3) I - g g^T + [3/(2rho)] diag(g_i^2)`
`                       - [|g|^2/(2rho)] I + O(|g|^4)`.

Thus the six-axis anisotropy conclusion remains; the claimed absence of an
off-diagonal product term does not. This witness does not refute the sphere
calculation, local continuity identities, or the measured sink-force data.
No external PR comment or change has been sent, and no full PR approval or
audit verdict is asserted.
