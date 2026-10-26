---
claim_id: regge_action_per_cell_and_the_conditional_gravity_coupling_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite deterministic diagnostics on supplied Kuhn cubic and coned D4 Regge carriers: sampled ratios of quadratic metric forms, a static point-source response on a finite torus, and the conditional algebra G = a^2/(8 pi kappa) if the supplied Regge action is matched to an Einstein-Hilbert action with the stated metric, source, sign and unit conventions. No continuum convergence theorem, carrier-independence theorem, value of kappa, induced coupling, physical Newton constant or Planck identification is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/regge_action_per_cell_and_the_conditional_gravity_coupling_2026_10_21.py
---

# Finite Regge diagnostics and a conditional gravity coupling

Claim type: bounded_theorem.
Primary runner: `scripts/regge_action_per_cell_and_the_conditional_gravity_coupling_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight.
This calculation supplies a Regge action, a metric reading and a source law
and compares their finite numerical response with a supplied Euclidean
Einstein-Hilbert (EH) comparator. Record and lossless-response language does
not establish a physical Einstein operator here. The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) select neither these carriers,
this dynamics, the source law nor kappa.

## Supplied units and matching conditions

The unit convention measures energy E in phase radians per tick and chooses
hbar = 1, top speed = 1 and cell spacing a = 1 for the numerical calculations.
The tick direction, energy interpretation, source placement and relation of
metric perturbations to edge lengths are supplied choices. Restoring a
length a below is a dimensional convention, not a determination of a
physical lattice scale. Equating a deficit radian with a phase radian does
not determine the coefficient kappa.

## Finite Regge versus EH comparison per cell

Let Q(k) be the Bloch Hessian of sum A delta over edge lengths, evaluated
at the flat supplied geometry. Schlaefli gives its flat-background expression
sum_t dA_t (x) d delta_t. The supplied line-integrated metric reading maps Q
to the 10x10 form K(k). The Euclidean comparator is the quadratic part of
sqrt(g) R,

    -1/4 (d h)^2 + 1/2 (div h)^2 - 1/2 div h . d tr h + 1/4 (d tr h)^2,

up to divergences. With h = Re(H exp(ikx)), the Regge quadratic cell average
is H^dag K H / 4 and the EH quadratic cell average is H^dag F H / 2.
Consequently the computed Rayleigh ratio K/F represents
**2 Hess(Regge) / Hess(EH)** for the same perturbation, not its reciprocal
normalization.

The runner evaluates four seeded random directions and perturbations on
each carrier at |k| = 0.05 and 0.025, and applies a two-point Richardson
estimate. Those finite estimates are within 4e-4 of one for Kuhn cubic
(15 edges, 50 hinges per cell) and within 2e-5 for coned D4 (72 edges,
208 hinges). A transverse-traceless sample at |k| = 0.01 is within 3e-5
on Kuhn cubic. A separate supplied analytic-derivative implementation at
|k| = 0.002 and 0.001 gives a sampled discrepancy below 3e-7.
These are finite diagnostics of the proposed factor one half; they do not
prove a limit, continuum action identity, or carrier independence.

**Conditional coefficient algebra.** If one additionally supplies the
matching sum A delta = (1/(2a^2)) int sqrt(g) R in the intended continuum
regime, and identifies the oriented action -kappa sum A delta with
-(1/(16 pi G)) int sqrt(g) R using the same metric, source and unit
conventions, then

    kappa/(2a^2) = 1/(16 pi G), hence G = a^2/(8 pi kappa).

This algebra is exact under that matching condition. The finite samples do
not establish the matching condition or a physical gravitational coupling.

## A supplied point-source response

For the real quadratic metric variables, the response uses the signed action

    S[h] = -(kappa/2) h^T K h - (E/2) h_tt.

With the stated pseudoinverse prescription this gives
h = -(E/(2 kappa)) K^+ e_tt and S_on = -E h_tt/4 on the sourced nongauge
subspace. The zero mode is omitted in the torus response. At zero tick
momentum h_tt is gauge invariant in the supplied linearized metric model.
For the Euclidean comparator and k = q e_0, the pseudoinverse solution has
h_tt = E/(kappa q^2) and transverse spatial diagonal entries
h_11 = h_22 = -E/(kappa q^2); the spatial and tick signs are not equal.

At |k| = 0.02 along three selected spatial directions, the two carriers'
computed k^2 h_tt values are within 4e-5 of E/kappa. Conditional on the EH
matching above, this comparator normalization is 8 pi G E/k^2 in a = 1
units. This is a sampled comparison, not a proved small-k limit.

On the supplied 24^3 torus with kappa = 1, fitting
h_tt = 8 pi c E G_lat(r) + const over 4 <= r <= 9 gives c = 0.03965 with
relative residual 1.9% on coned D4, against 1/(8 pi) = 0.03979, and
c = 0.03976 after 2^3-block averaging. The **raw Kuhn counterexample to a
good unaveraged fit is preserved**: c = 0.0392 with residual 78%, dominated
in this fixture by soft zone-boundary modes near (pi,pi,pi). After 2^3-block
averaging it gives c = 0.03981 with residual 1.3%. Averaging changes the
readout; it does not repair or erase the raw discrepancy. These finite
fits do not establish a universal inverse-distance law.

## Conditional normalization choices

Choosing kappa = 1 gives c = 1/(8 pi); choosing kappa = 1/(2 pi) gives
c = 1/4 under the same conditional matching. These are alternative supplied
coefficients, not selected physical constants. Within the signed quadratic
source model the on-shell dressing is X E^2/kappa, with X = -0.05258 in the
coned D4 24^3 fixture. A prescription |dressing| = 1 would therefore give
kappa = |X| E^2 for that fixture; it is not a state-independent selection
of kappa. No selection of a share size or a physical coupling is established
by this calculation.

## Scope and recovery

Supplied inputs include carriers, flat Euclidean lengths, metric reading,
action sign, tick index, source law, phase/deficit identification, area units,
torus, fit window and pseudoinverse cutoff. Counting areas at a different
rung changes the conditional coefficient in site units: if a is twice the
site spacing and kappa = 1, the formula gives G = 1/(2 pi) in site-length
squared units. This is conditional dimensional bookkeeping.

The two imported geometry modules provide computational definitions used
here; their broader physical or continuum conclusions are not inherited.
The canonical runner imports the tracked helper directly and binds its
transitive source and declared context. No ambient d4cone_lib is consulted.
No continuum convergence, carrier independence, induced coupling, physical
Newton constant or Planck identification is established. Original PR9856
source, numerical output and raw Kuhn result remain recoverable at commit
`0c360d6316bc71f0baeda69bb6c0f4a9d4adbbfd`.
