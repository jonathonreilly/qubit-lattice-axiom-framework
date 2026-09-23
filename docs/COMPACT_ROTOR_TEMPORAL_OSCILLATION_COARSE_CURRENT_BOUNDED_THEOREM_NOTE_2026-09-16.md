---
claim_id: compact_rotor_temporal_oscillation_coarse_current_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/compact_rotor_coarse_current_check_2026_09_16.py
claim_scope: "Joint temporal oscillations and conserved integer coarse currents of the supplied compact rotor path law at fixed positive time scale T."
upstream_dependencies: ["compact_rotor_sampled_magnetic_event_bounded_theorem_note_2026-09-16", "compact_rotor_magnetic_excursion_bounded_theorem_note_2026-09-16", "compact_rotor_spatial_ground_path_limit_bounded_theorem_note_2026-09-16"]
---

# Temporal oscillations and closed coarse compact currents

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

Joint temporal oscillations and conserved integer coarse currents of the supplied compact rotor path law at fixed positive time scale T. This is a positive conditional theorem for the explicitly supplied Hamiltonian, geometry and limit order, not a derivation of that Hamiltonian from framework axioms. No audit verdict or retained promotion is asserted.

Load-bearing mathematical parents: [COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md](COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md), [COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md](COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md), [COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md](COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md). These are supplied-model proof dependencies, not retained axioms.

The infinite-volume application uses the full spatial-path-limit proof, including its local compact path specification, together with the sampled-event and excursion proofs.

## 1. A joint bound on full temporal oscillations of links

For a spatial link e and interval I_n=[nT,(n+1)T], set

    O_(e,n)(alpha) = {sup_(s,t in I_n) d_T(theta_e(s),theta_e(t))>=alpha},
                     0<alpha<pi.                            (1)

The circle-distance oscillation is invariant under reversing time or
link orientation. For a free circle Brownian path lifted from its initial
angle, this event requires

    sup_(0<=s<=T)|gW_e(s)|>=alpha/2.

Indeed, if every real increment has magnitude less than alpha/2, each
pair differs by less than alpha, as does its circle distance. Thus

    q_E(g,T,alpha)=min(1,4exp[-alpha^2/(8g^2 T)])             (2)

bounds its probability, uniformly in the starting angle. It includes
paths winding around the circle; a full turn certainly has oscillation
pi. It is not a bound on the absolute, gauge-dependent angle value.

A cube contains four parallel edges of any fixed orientation. Choose
one as a base event support. Reflected spatial dissemination puts that
event on N/4 distinct links, determined by the two transverse coordinate
parities, each repeated four times by the N cells. These links are
already disjoint Brownian coordinates, with no additional checkerboard
selection. Whole-interval dissemination imposes the event in each of
the M intervals of a thermal loop of duration MT, M even.

Let K_D be the actual constrained Feynman-Kac kernel for all those
N/4 link oscillation events in one interval. Drop every nonnegative
plaquette potential. The independent reference link Brownian motions
give row sums <=q_E^(N/4). Time reversal makes K_D symmetric. Its
Hilbert-Schmidt norm is bounded by that of exp(-TH), just as in
the magnetic-excursion note, whether or not K_D is positive semidefinite. The even-power
trace bound and chessboard exponent therefore give

    eps_E(g,T,alpha)=min(1,exp(C0 T) q_E(g,T,alpha)^(1/4)),
    P_ground(all k specified O events of one orientation)<=eps_E^k.
                                                               (3)

For arbitrary link orientations the exponent becomes ceil(k/3).
The inverse-reflected base edge is chosen separately for each event
according to its two transverse anchor parities. Distinct links of
one orientation and intervals occupy distinct anchor cells. the spatial-path-limit note's
path convergence and open-threshold argument transfer (3) to the same
infinite-volume path law mu.

This is an auxiliary temporal-gauge link-path statement for the
full-space Hamiltonian ground representation. It is invariant under
the time-independent gauge transformations of that representation.
No new time-dependent gauge field or projection at each time slice
has been inserted.

## 2. A well-defined coarse four-dimensional compact cochain

Fix T>0, and use the cubic cell complex with three spatial coordinates
and discrete time index n in Z. On its positive spatial links set

    A_i(x,n)=theta_(x,i)(nT) in R/(2pi Z), i=1,2,3,

and on its positive time links set A_0=0 (temporal gauge). Choose real
representatives a_i in [-pi,pi) and a_0=0 only for the following exact
cochain identity. For every positively oriented two-cell p define

    F_p=principal((d a)_p) in [-pi,pi),
    m_p=((d a)_p-F_p)/(2pi) in Z,
    J_c=(dF)_c/(2pi)=-(dm)_c in Z.                         (4)

All cochains extend by linear antisymmetry to negative orientations;
one must not reapply the half-open principal-branch rule to an already
reversed face at the value pi. The cubical identity d^2=0 gives

    dJ=0.                                                  (5)

The Hodge dual of J is consequently a divergence-free integer current
on the dual four-dimensional edges. This is an exact algebraic fact
about the declared coarse path cochain, not a continuum approximation.
Its spatial three-cell component is the principal magnetic cube charge
at the sampled time. Other components track coarse compact branch
changes involving the time direction.

Spatial faces with |F_p|>=alpha are contained in the magnetic excursion
event for their plaquette in the interval starting at that time. For a
face containing time, |F_p| is the circle distance between the endpoint
angles of its spatial link, hence is bounded by its whole-interval
oscillation. Put

    eps_* = max(eps_exc(g,T,alpha),eps_E(g,T,alpha)).         (6)

Among r distinct bad coarse two-cells, at least ceil(r/6) have one of
the six fixed spacetime orientations. Within that orientation, the
dominating path events are distinct. Equations(3) and the magnetic-excursion note(3) give

    mu(all r specified |F_p|>=alpha)<=eps_*^ceil(r/6).       (7)

No independence between electric and magnetic events is claimed.
The factor6 explicitly pays for selecting a common orientation.

## 3. Dilute support of the exact closed coarse current

Set alpha=pi/3. If J_c!=0, at least one of the six boundary faces of
c has |F_p|>=pi/3; otherwise their signed sum has magnitude less than
2pi and cannot be a nonzero integral multiple of2pi. A face in a
four-dimensional cubic complex belongs to four three-cells. Thus for
n specified distinct three-cells, each assignment of a witness face
contains at least ceil(n/4) distinct faces. There are at most6^n
witness assignments. Equation(7) gives

    mu(J_c!=0 on all n specified three-cells)<=p_J^n,
    p_J=min(1,6 eps_*^(1/24)).                              (8)

This assertion holds in every finite even spatial torus, with the
stationary infinite time direction, and in the spatial limit mu.
It bounds the support; coefficients and signs of the integer current
are kept by (4), and are not replaced by independent Bernoulli edges.

Dual four-dimensional lattice edges form an adjacency graph by sharing
an endpoint. Its maximal degree is14. Connected edge sets of size s
containing a specified dual edge number at most14^(2s-2), by the same
spanning-tree traversal bound. Therefore

    mu(nonzero-current component at an edge has size>=s)
                              <=14^(2s-2) p_J^s.            (9)

Whenever196p_J<1, every component is finite almost surely. Together
with integer conservation (5), each finite component can be decomposed
into finitely many oriented cycles with integer multiplicities. This
last statement follows by repeatedly following an outgoing positive
flow, closing a cycle in the finite support and subtracting the smallest
positive flow along it. It is a decomposition, not a unique assignment
of particle trajectories.

The sufficient range is very conservative. At the balanced T of
the magnetic-excursion note, its magnetic bound behaves as exp[-constant/g^2] at fixed T,
and (3) has an even stronger negative exponent. Thus196p_J<1 holds
for a nonempty interval of fixed positive couplings near zero. The
checker evaluates g=0.004, where196p_J<0.02002, and the explicit
sufficient range g<0.004979161143403665... . These are not fitted
physical couplings or sharp transition points.

## 4. Local lifting on good blocks and limits of the conclusion

When a link has oscillation less than alpha<pi throughout an interval,
its path stays in the open circle arc of radius alpha around its initial
value and has a unique continuous real increment lift starting at zero,
with magnitude less than alpha. A nonzero winding cannot be hidden in
such a path. When a spatial plaquette stays at distance less than alpha
from zero throughout the interval, its principal flux is continuous;
relative to these lifted link paths, its integer branch offset is
constant. These are local lifting statements, valid on the specified
good blocks. They supply no globally small raw curl on a torus or on
the complement of a defect cluster.

The construction of (4) matches a concrete temporal-gauge cochain to
the actual ground path representation, and (8)-(9) control its coarse
closed currents. They do not assert a scale-uniform finite-length
microscopic current representation as T->0. Brownian paths can cross
branch surfaces repeatedly, and the magnetic excursion bound used here
is not uniform under arbitrary refinement of T at fixed g. Short loops
within one interval are covered by the excursion events, but need not
appear as separate currents in (4).

Closed compact currents also do not exhaust global harmonic flux or
winding sectors. A globally closed integer sheet need not be exact on
a torus. Nor has the temporal-gauge cochain estimate been promoted to
a fully identified four-dimensional gauge-invariant field theory with
its reconstructed physical electric observables.

Most importantly, a rare closed-current gas is not by itself a proof
of a photon. We still need control of its coupling to the smooth gauge
field and of the long-wavelength transverse response. There is no
axiom change, retained phase
claim or assertion of novelty of integer-current conservation here.

## Evidence and execution boundary

Primary runner: `scripts/compact_rotor_coarse_current_check_2026_09_16.py`. The reflection/path runner jointly supports the magnetic-excursion and spatial-path-limit notes.

The three calculations retain every original fixture, arithmetic operation, assertion and tolerance. Each retains a 120-second timeout. A 512 MiB external process cap is proposed from the bounded representations and library overhead; it is not a measured peak or a completed execution. Each runner reads and hash-pins its declared source-note inputs and writes JSON under `logs/runner-cache/`. `TOTAL: PASS=3 FAIL=0` counts three completed diagnostic families, not three assertions or exhaustive theorem coverage. The JSON separately labels the static source assertion count.

The [historical recovery packet](work_history/repo/review_feedback/pr8165-evidence/README.md) preserves all 88 original paths, modes, blobs and byte hashes, all four full working proofs, all three calculations, eleven mutation histories and the failed Fourier attempt. Historical output is not current-source execution evidence. PR8164 is contextual comparison only; no theorem or status is imported from it.

## No-Go Discipline Gate

**N1 — Actual routes.** Formal negative-packet certification is deferred: the source does not supply five qualifying refuted routes. The actual approach registry and finite countercontrols are preserved; no extra routes are invented. This does not negate the positive supplied-model proofs or the exact finite counterexamples.

**N2 — Shared scope.** One supplied Hamiltonian and the stated compact geometry underlie the chain. Reflection/chessboard is a shared mathematical premise; future source-response, harmonic-sector and microscopic-current obligations are not independent walls proved here.

**N3 — Conditions.** Compact Haar angles, the full thermal trace followed by its neutral ground limit, even L>=4, fixed positive g and T, and the oriented principal branch are explicit. No limiting-state uniqueness, positive-semidefinite constrained kernel or finite-clock Brownian behavior is assumed.

**N4 — Credit and failures.** Biskup supplies the matched chessboard theorem; the finite smooth reversible identity is derived and credited. The failed Fourier cutoff attempt, exact subsequent refinement, eleven mutation outcomes and prior source versions remain recoverable without treating them as current captures.

**N5 — Resolution.** Finite geometry, circle/rotor matrices and integer cochains test the stated identities and constants. Volume-uniform bounds, continuous-path tightness and the infinite-volume specification are analytic proofs, not exhaustive numerical runs. The five execution-scope lines report only the program that actually finishes.

**N6 — Partial closure.** Sampled events, full excursions, a continuous-path spatial limit and a fixed-T current construction are successive positive results. No new primitive is proposed.

**N7 — Strongest boundary.** Rare coarse conserved currents do not by themselves give a photon, a native Hamiltonian, a unique vacuum, microscopic T->0 control, exhaustive harmonic sectors or physical electric reconstruction. These are open extensions, not impossibility claims.

**N8 — Reopening.** Smooth-field/current weighting and source-response control may resolve the remaining physical questions. The periodic spatial subsequence is not equated with the contextual free-box state. No broad negative certification is claimed.
