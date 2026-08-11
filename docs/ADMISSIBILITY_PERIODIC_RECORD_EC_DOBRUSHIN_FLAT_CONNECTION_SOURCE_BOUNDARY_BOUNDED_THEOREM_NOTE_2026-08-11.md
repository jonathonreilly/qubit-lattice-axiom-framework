---
claim_id: admissibility_periodic_record_ec_dobrushin_flat_connection_source_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the supplied Block-38 ten-label Record/coframe/SO(4)-link fixed-potential law on a fixed nondegenerate cubic geometry background, every nearest-neighbor Record kernel has a universal single-neighbor conditional influence at most tanh(beta/2). At beta=1/5 the six-neighbor Dobrushin row sum is below one, so the full-Z3 Record-label specification has one boundary-independent Gibbs phase. On the homogeneous flat periodic background, the Record-bond connection score cancels by endpoint exchange, the Einstein--Cartan face score cancels linkwise by periodic incidence, and the compatibility/normal/torsion squares have zero first variation; all translated elementary nonabelian cube-Bianchi words also close. A supplied positive zero-sum Record-marginal Fourier perturbation produces a nonzero connection force with pure injected mode support and first-difference sine scaling. This is a fixed-background Record-phase, flat bulk connection, and sourced Palatini-carrier theorem, not a full joint coframe/link phase, coframe-stationarity, displacement-Ward, Einstein-universality, Lorentzian-update, physical-law-selection, gravity no-go, axiom-necessity, or axiom-adoption result."
upstream_dependencies:
  - minimal_axioms
  - admissibility_two_cube_record_ec_overlap_gibbs_connection_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_periodic_record_ec_dobrushin_flat_connection_source_2026_08_11.py
---

# Periodic Record/EC Dobrushin Phase, Flat Connection, And Source Boundary

**Date:** 2026-08-11
**Type:** `bounded_theorem`
**Role:** decide whether Block 38's flat connection force is an open-boundary
artifact, construct the first full-`Z^3` phase of its discrete Record sector,
and test whether an inhomogeneous Record marginal loads the same EC carrier.
**Scope:** fixed nondegenerate coframes and `SO(4)` links; the supplied
ten-label Record site/edge/face potentials; periodic `L=3,5,7,9,11,15`
spatial carriers; exact conditional oscillation bounds, ordered-product
Bianchi identities, connection first variations, and one supplied zero-sum
Fourier perturbation.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_periodic_record_ec_dobrushin_flat_connection_source_2026_08_11.py](../scripts/admissibility_periodic_record_ec_dobrushin_flat_connection_source_2026_08_11.py)

## Result Up Front

The two-cube law has a rigorous full-lattice phase in its discrete Record
sector once the geometry background is fixed. For any nondegenerate coframes
and any `SO(4)` links, the transported Record objects are rank-one projectors.
Consequently every edge log kernel lies in an interval of width at most
`beta`. Changing one neighboring label changes the target site's log odds by
a function whose oscillation is at most `2 beta`. The elementary normalized-
weight inequality proved below therefore gives

```text
c_xy <= tanh(beta/2),
sum_(y nearest x) c_xy <= 6 tanh(beta/2).                         (1)
```

At the supplied `beta=1/5`, the right side is `0.5980079677 < 1`; equivalently
the universal window is

```text
beta < 2 atanh(1/6) = 0.3364722366.                              (2)
```

The one-site conditional map is thus a strict disagreement contraction.
Iterating the influence inequality sends every boundary disagreement to zero
at increasing distance, proving uniqueness of the infinite-volume
ten-label Gibbs specification and boundary-independent convergence of its
local conditionals. The fixed site weights and fixed EC face loads are
one-site fields and do not enlarge the neighbor influence in (1).

This is a significant phase closure, but it is deliberately typed. It proves
the Record-label phase conditional on a fixed geometry background. It does not
integrate the continuous coframes or links, prove their tightness, select a
background, or produce a joint geometry/Record phase.

On the homogeneous flat background, the complete connection tadpole of the
supplied action vanishes in periodic volume for three independent reasons:

1. compatibility, normal, and torsion terms are squares about zero residual;
2. the Record bond score is antisymmetric under exchange of its endpoint
   labels while the unique flat phase has an exchange-symmetric edge marginal;
3. every constant-coefficient EC plaquette curl enters each link from two
   translated faces with opposite orientation.

The runner executes every one of the `81 x 6 = 486` `L=3` link tangents. The
EC cancellation is checked with a translation-uniform but deliberately
non-cubic label marginal, so it is periodic incidence rather than a fitted
orbit average. Removing the wrap faces restores an order-one open-boundary
tadpole. Block 38's flat residual is therefore a boundary artifact for this
connection equation, not evidence that the periodic connection law fails.

All 27 translated elementary cubes also satisfy the transported ordered-
product nonabelian Bianchi identity on a generic noncommuting link field. As
before, that identity is kinematical and is not renamed a displacement Ward
identity or a field equation.

Finally, the EC coupling is not vacuous. On every odd periodic length tested,
the runner supplies the positive label marginal

```text
p_x(a) = 1/10 + epsilon cos(2 pi x_1/L)
                  [delta_(a,0)-delta_(a,4)],   epsilon=1/50.      (3)
```

It is normalized at every site and has zero spatial total. Its connection
force has no zero mode, lies entirely at `k_1=plus/minus 2 pi/L`, doubles when
`epsilon` doubles, and obeys

```text
RMS(g_L) proportional to sin(2 pi/L),   L=3,5,7,9,11,15.         (4)
```

Thus the inherited EC face term transmits a zero-sum Record inhomogeneity into
an honest first-difference Palatini connection load. Equation (4) is not yet
an Einstein response. A coupled coframe/link Hessian, its local-frame quotient,
the base-displacement identity, the second-difference tensor after eliminating
the connection, and universal source coupling remain to be derived from the
same selected law.

No canonical axiom changes in this block, and no fixed TOE percentage moves.

The central executed certificate is

```text
L=3 periodic V/E/F/based loops/cubes             27 / 81 / 81 / 324 / 27
translated generic Bianchi residual max/mean      1.760e-15 / 1.233e-15
universal Dobrushin row sum                        0.598007968
universal beta threshold                           0.336472237
exact flat-kernel oscillation / row sum             0.380725758 / 0.569370271
deterministic conditional TV maximum                0.029258813
bond score antisymmetry / expected score             0 / 1.735e-18
analytic/finite-difference bond-score error          1.982e-11
periodic EC gradient max / norm                      5.551e-17 / 4.079e-16
open-box EC gradient max / norm                      0.654545 / 5.153554
geometry gradient max / minimum coordinate d2        0 / 0.700000
assembled flat connection gradient max / norm        5.573e-17 / 4.083e-16
source RMS at L=3 / L=15                             0.002721655 / 0.001278250
source RMS / sin(2 pi/L)                             0.003142697
source Fourier-mode fraction                         1.000000000000000
source amplitude-doubling error                      1.943e-16
```

A separate runner-free numerical-action reconstruction (`PASS=6 FAIL=0`)
rebuilds the projectors, carrier, holonomies, and centered link derivatives
without importing the primary runner. It obtains flat EC gradient
`5.294e-17`, source RMS `0.002721655`, pure-mode fraction
`1.000000000000000`, and the same exact-kernel influence row sum
`0.569370271`.

## Inputs And Non-Imports

| input | used | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | `Z^3`, six nearest neighbors, translations, proper cubic rotations, one fixed nearest-neighbor Admissibility rule, and permanent Records | the rule's extensional values, coframes, links, projectors, a Gibbs action, source meaning, dynamics, gravity, or time |
| [Block 38](ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the supplied ten-label fixed site/edge/EC-face potentials, corrected fixed coefficient, overlap law, and exact elementary Bianchi word | its open boundary, homogeneous reduced connection ansatz, a full-lattice phase, coframe stationarity, or an Einstein equation |

No observed gravitational datum, Newton coefficient, cosmological coefficient,
continuum target, fitted source response, canonical axiom edit, audit verdict,
or `review-loop` is used.

## 1. Periodic Carrier And Exact Bianchi Translation

For `L>=3`, let vertices be `Z_L^3`. Attach one positively oriented link in
each of three coordinate directions at every site, one positively oriented
square in each coordinate plane at every site, and all four cyclic base
points of each square. At `L=3` this gives

```text
|V|=27, |E|=81, |F|=81, based loops=324, elementary cubes=27.     (5)
```

The lower bound `L>=3` avoids the orientation aliasing of a two-site periodic
cycle. Reverse traversal always means the transpose of the one stored link.

For each elementary cube, transport the six outward face holonomies to its
low vertex in the Block-38 order. The underlying oriented-edge word freely
reduces to the empty word. Translation only relabels the twelve edge symbols,
so the same proof applies to every cube. The runner separately assigns a
generic noncommuting `SO(4)` matrix to every one of the 81 links and evaluates
all 27 matrix identities. This closes periodic kinematical Bianchi exactly;
it says nothing about base displacement redundancy.

## 2. Fixed-Background Record Specification

At a fixed nondegenerate coframe `e_x`, label `a` determines the rank-one
projector

```text
P_x(a) = |e_x r_a><e_x r_a| / ||e_x r_a||^2.                     (6)
```

For an oriented link `U_xy in SO(4)`, the Block-38 bond factor is

```text
K_xy(a,b) = exp[-(beta/2)||P_x(a)-U_xy P_y(b) U_xy^T||_F^2].     (7)
```

The Record weight and the four based EC face loads at a site combine into a
strictly positive one-site field `q_x(a)`. In a finite region, conditioned on
the six neighboring labels,

```text
mu_x(a | eta) proportional to q_x(a)
               product_(y nearest x) K_xy(a,eta_y).              (8)
```

This is exactly the local conditional supplied by the fixed carrier factors;
it is not a new marginal-equality demand.

## 3. Self-Contained Dobrushin Bound

Let two positive normalized weights have the form
`p_a proportional to w_a` and `p'_a proportional to w_a exp(h_a)`. If
`osc(h)=max h-min h=Delta`, shift `h` by its midpoint. Then the likelihood
ratio lies in `[exp(-Delta/2),exp(Delta/2)]`. Splitting its positive and
negative deviations around one, using normalization, gives

```text
TV(p,p') <= (exp(Delta/2)-1)/(exp(Delta/2)+1)
          = tanh(Delta/4).                                      (9)
```

For rank-one orthogonal projectors,
`0 <= ||P-Q||_F^2 <= 2`, including after `SO(4)` transport. Hence
`log K in [-beta,0]`. Changing one neighbor from `b` to `b'` inserts

```text
h_a = log K(a,b)-log K(a,b'),   osc(h) <= 2 beta.                (10)
```

Equations (9)--(10) prove (1). The influence comparison for two boundary
conditions is obtained by changing disagreeing neighbors one at a time. If
`d_x` denotes the maximal local marginal disagreement, then
`d_x <= sum_y c_xy d_y` away from the changed boundary. Iteration over paths
of length `n` bounds the interior disagreement by a geometric factor whose
row norm is `(6 tanh(beta/2))^n`. Below (2) it vanishes as the boundary
recedes. Any two infinite-volume specifications therefore have equal finite
marginals, and finite-volume conditionals converge to that unique phase.

For the exact flat ten-projector table, the runner also reconstructs the
smaller pair-log oscillation and probes 257 deterministic five-neighbor
contexts. Those computations test the implementation; the theorem uses the
larger universal rank-one bound, not the probe.

The proof is uniform in fixed site fields and fixed geometry backgrounds. It
does not survive integration over arbitrary continuous geometry variables by
itself, because then the Record conditional is only one conditional block of
the joint law.

## 4. Flat Record-Bond Connection Score

At the identity link, vary `U=exp(tA)` for `A in so(4)`. Differentiating (7)
gives

```text
D_A log K(a,b)|_(t=0) = beta tr([P_b,P_a] A)
                      = -D_A log K(b,a)|_(t=0).                  (11)
```

The homogeneous flat finite-volume law has identical site fields and the same
symmetric bond matrix on every undirected edge. Reflection of the periodic
graph through an edge midpoint exchanges its endpoints without changing the
label Hamiltonian. Its edge marginal is therefore symmetric in `(a,b)`.
Uniqueness carries this symmetry to the infinite-volume phase. Contracting
(11) with that marginal yields zero for all six link generators. The runner
assembles all 600 analytic label-pair/generator scores, verifies their
antisymmetry, and compares every entry to an independent centered link
difference.

This cancellation uses an accidental reflection symmetry of this supplied
flat Record law; the foundational Lattice axiom itself requires only proper
cubic rotations. An orientation-sensitive extensional Admissibility rule
would need a separate test.

## 5. Periodic EC Curl And Geometry Squares

At identity links, the linearized sine holonomy of a face is its oriented
lattice curl:

```text
delta F_ij(x) = A_i(x)+A_j(x+hat i)
                -A_i(x+hat j)-A_j(x).                            (12)
```

For any translation-uniform one-site label marginal, the expected incidence
coefficient of each based face depends on its plane but not on `x`. Summing
(12) over the periodic carrier telescopes separately in every plane. Each link
therefore receives two equal and opposite contributions. The runner uses the
asymmetric marginal proportional to `(1,2,...,10)` and still obtains zero on
all 486 tangents.

The remaining declared geometry terms are squared compatibility, normal, and
torsion residuals. Every residual is zero at `e_x=E_*`, `U_xy=I`, so their
first variations vanish. Direct centered variation of all 486 coordinates
checks this independently. Combining this fact, (11), and (12) proves the
flat periodic connection equation for the fixed-background Record phase.

On the open `3 x 3 x 3` box, there are only 54 links and 36 faces. The missing
wrap faces prevent the telescoping cancellation and the runner recovers a
large boundary gradient. This is the terminal control that distinguishes the
new theorem from an implementation that merely returns zero at flat links.

The coframe equation is not closed. Translation and cubic symmetry constrain
its homogeneous stress, but canceling that stress would still require a
physically selected common coframe potential or a derived background. This
block does not reverse-engineer one.

## 6. Zero-Sum Record Source And First-Difference Response

Equation (3) changes no site's total probability and has positive minimum
`0.08`. On every odd `L` in the scan its spatial sum vanishes exactly to
floating arithmetic. Substituting it into the expected EC face load and
differentiating every link yields a nonzero force.

The source is a supplied marginal deformation, not a claim that the current
axioms select label `0`, label `4`, its amplitude, or its preparation. Its
purpose is a sharp carrier test: does the same local term that closes in the
vacuum transmit an inhomogeneous Record load, with the momentum order expected
of a first-order connection equation? The answer is yes. Fourier support is
pure, the zero mode remains absent, the response is linear in amplitude, and
the length scan gives the exact `sin(k)` finite-difference symbol in (4).

The next discriminator is not another source fit. One must form the coupled
coframe/link Hessian of this same law, quotient its internal-frame gauge
directions, eliminate the connection, and test whether the resulting coframe
operator has a universal transverse two-derivative Einstein/Regge structure.
If it does not, the residual must be assigned to the extensional law or to a
precisely named missing downstream interface before any axiom amendment is
considered.

## 7. Exact Scope And Axiom Pressure

What is now closed:

- correct periodic carrier counting and every translated elementary Bianchi
  identity;
- a unique, boundary-independent full-`Z^3` phase for the ten-label Record
  conditional at any fixed admissible nondegenerate geometry background;
- the complete flat periodic connection first variation for the supplied
  homogeneous fixed-background law;
- a nonzero, zero-mode-free, first-difference EC load from one supplied
  positive zero-sum Record marginal.

What remains open:

- existence/tightness and phase selection for the continuous joint
  coframe/link/Record measure;
- stationarity and stability of the coframe background;
- a base-lattice displacement Ward identity distinct from internal-frame Ward
  and Bianchi kinematics;
- the gauge-quotiented two-derivative coframe response and universal source
  coupling needed for an Einstein regime;
- derivation of the carrier, measure, coefficients, boundary law, and source
  meaning from Admissibility/Record content;
- a `Z^3 x Z_tau` or other Lorentzian permanent-Record update.

The current axioms assert that one fixed nearest-neighbor Admissibility rule
exists, but intentionally do not specify its extensional form or values. The
Block-38/39 potentials are therefore a supplied downstream candidate. A
sufficient candidate interface would require existing Record content to
determine a nondegenerate geometry observable, oriented transport, and one
normalized translation/proper-cubic-covariant fixed-potential law with its
measure, coefficients, and boundary specification. Whether that interface is
derivable or should be registered is open. This block proves no fifth ontology
axiom necessary and adopts no amendment.

## 8. N1--N8 No-Go Discipline

### N1 — Executed Route Enumeration

| route | class | executed attempt | terminal outcome |
|---|---|---|---|
| fixed-background conditional contraction | direct retained carrier | bound every rank-one edge kernel and sum all six influences | universal row sum below one; unique Record phase |
| exact flat-kernel reconstruction | same carrier, sharper algebra | enumerate all neighbor-label log-ratio oscillations and deterministic contexts | sharper row sum below the universal bound |
| periodic EC incidence | alternate boundary/region | assemble every `L=3` periodic face and all 486 link tangents | flat curvature tadpole cancels linkwise |
| open-box control | alternate boundary/region | remove periodic wrap faces without changing the uniform marginal | nonzero boundary tadpole returns |
| endpoint-exchange Record bond | alternate sector term | assemble analytic pair scores and independent centered differences | antisymmetric score contracts to zero in symmetric phase |
| translated nonabelian Bianchi | alternate identity | free-word reduction plus 27 generic matrix words | every elementary periodic cube closes kinematically |
| zero-sum Fourier source | alternate source/readout | positive label-marginal deformation on six tori | pure nonzero `sin(k)` connection force; no zero mode |

These routes are mechanistically distinct: conditional contraction, region
topology, bond-score symmetry, group-word cancellation, and sourced Fourier
response cannot be counted as reruns of one fit.

### N2 — Wall Independence Audit

| wall | independent of |
|---|---|
| continuous joint geometry phase | fixed-label Dobrushin uniqueness, because integrating coframes/links changes the conditional block structure |
| coframe stationarity | connection-tadpole cancellation, because the coframe derivative contains site/metric stress not removed by a curl sum |
| displacement Ward identity | internal-frame Ward and Bianchi, because it acts on base-lattice placement rather than internal endpoints or group words |
| Einstein tensor structure | nonzero Palatini source carrier, because a first-order force need not yield the universal quotient after connection elimination |
| physical law selection | mathematical consistency of the supplied potentials, because Admissibility leaves extensional values unspecified |
| Lorentzian update | every Euclidean spatial result, because no clock direction, cone, or Record-preserving evolution was supplied |

No pair of these walls is used as duplicate support for a broader negative.

### N3 — Hidden-Wall Scan

- `L>=3` is explicit; the aliased two-site torus is not silently included.
- Geometry is fixed and nondegenerate in the phase theorem; the projectors are
  not extended through singular coframes.
- The exact phase is the ten-label conditional only; continuous geometry
  integration is not hidden inside the word "Gibbs."
- The flat bond cancellation uses endpoint-exchange symmetry of the supplied
  law; it is not attributed to proper-cubic covariance alone.
- The source is a supplied positive marginal deformation, not a realized
  physical mass, stress tensor, or Record-production process.
- `sin(k)` is a first-difference connection force, not an Einstein propagator.
- Finite Euclidean Bianchi is not a dynamics or causality theorem.

### N4 — Residual Source Matching

| residual | exact source |
|---|---|
| extensional rule values and dynamics absent | `docs/MINIMAL_AXIOMS_2026-06-29.md`, Admissibility reading and Relation To Dynamics sections |
| fixed site/edge/face law supplied | Block-38 theorem note, Inputs and Fixed Potentials sections |
| continuous geometry phase unproved | this note, Sections 3 and 7 |
| coframe stationarity unproved | this note, Section 5 |
| displacement/Einstein discriminator unexecuted | this note, Sections 6--7 and primary runner lattice-wide certificate |
| Lorentzian permanent-Record update absent | minimal axioms Relation To Dynamics and this note, Section 7 |

### N5 — Landing Execution Certificate

The source/input-pinned primary cache must show all named checks green, a final
`TOTAL: PASS` line with zero failures, and substantive `per_element`,
`per_site`, `per_mode`, `per_block`, and `lattice_wide` coverage. It executes
the entire `L=3` periodic carrier, the open control, all translated Bianchi
words, all bond scores, every flat link tangent, and every site/link in the
six source tori. Repository cache, graph, premise, vocabulary, invariant, and
changed-evidence checks remain required before delivery.

### N6 — Rhetoric Audit

Permitted conclusions are "fixed-background Record phase is unique," "flat
periodic connection tadpole cancels," and "the supplied zero-sum marginal
loads the EC connection at first-difference order." Forbidden conclusions are
"gravity derived," "Einstein equation," "full joint phase," "axiom forces
this law," "gravity cannot work," "fifth axiom necessary," or "Lorentzian
dynamics." No fixed percentage is changed by rhetoric.

### N7 — Strongest Counterroute

The strongest counterroute is constructive: Dobrushin uniqueness removes the
Record boundary-state ambiguity, periodic incidence removes the open
connection tadpole, and the nonzero `sin(k)` source force can feed a coupled
Palatini elimination. A gauge-quotiented Hessian may therefore produce a
two-derivative coframe operator without new ontology. The next block must run
that route before any negative about gravity or axiom sufficiency can ship.

### N8 — Cross-Cycle Echo

Earlier blocks repeatedly retired apparently terminal gravity walls by
changing the correct mathematical target: free marginal became boundary
conditional, cube-centered connection became translation-compatible, and now
open-boundary force becomes periodic cancellation. The surviving law-selection,
coframe, displacement, Einstein, and Lorentzian walls are kept separate. This
history forbids promoting the present residuals to a universal gravity no-go
or a necessity claim about a fifth ontology axiom.

## Conclusion

The fixed Block-38 Record law now has a unique full-`Z^3` discrete phase at its
supplied coupling, its homogeneous flat connection equation closes in the
periodic bulk, and its EC term carries a positive zero-sum Record
inhomogeneity with the exact first-difference Fourier symbol. This is the
largest gravity-side closure since the one-cube construction because it
removes both the label-phase ambiguity and the measured open-boundary
connection defect.

The decisive next object is the coupled periodic coframe/link response of the
same law. Only after its gauge quotient and connection elimination can the
campaign judge a displacement Ward identity or Einstein/Regge limit. Physical
selection of the carrier and coefficients, continuous joint phase control,
and Lorentzian permanent-Record dynamics remain explicit axiom-interface
obligations, not hidden assumptions and not adopted amendments.
