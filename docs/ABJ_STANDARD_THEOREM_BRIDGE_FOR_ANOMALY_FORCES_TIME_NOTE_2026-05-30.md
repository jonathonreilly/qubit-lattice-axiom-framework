# ABJ Standard-Theorem Bridge for Anomaly-Forces-Time

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note records a
bounded standard-theorem bridge; it does not set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_abj_standard_theorem_bridge_for_anomaly_forces_time.py`](../scripts/frontier_abj_standard_theorem_bridge_for_anomaly_forces_time.py)

## Purpose

This note replaces the earlier source-side wording "ABJ accepted premise" with
a narrower and more accurate route:

```text
standard ABJ/Wess-Zumino/Fujikawa theorem
+ in-repo anomaly-trace arithmetic
+ in-repo chirality and single-clock dependencies
=> bounded 3+1 composition theorem.
```

The bridge does not make the Adler-Bell-Jackiw theorem a new framework axiom
and does not claim a full A1+A2-native lattice derivation. It treats the ABJ
anomaly-to-inconsistency implication as a standard theorem of chiral gauge
QFT, cites the primary literature, and checks that the framework's matter
content satisfies the theorem's nonzero-anomaly hypothesis.

## Standard Theorem Packet

**Standard ABJ/Wess-Zumino/Fujikawa theorem.** In a local regularized chiral
gauge quantum field theory, the fermion measure/effective action has a gauge
variation governed by the consistent gauge anomaly. The anomaly obeys the
Wess-Zumino consistency condition. If the perturbative anomaly coefficients of
the chiral matter content are nonzero and the anomaly is not cancelled by the
completed chiral matter representation, no gauge-invariant quantum effective
action with the required Ward identities exists. Equivalently, longitudinal
gauge-boson modes do not decouple and the gauge theory does not close as a
unitary quantum gauge theory.

The theorem packet used here is the standard one:

- Adler computes the axial-vector anomaly in a regulated spinor theory.
- Bell and Jackiw identify the same anomaly in the PCAC problem.
- Bardeen gives anomalous Ward identities for general spinor theories.
- Wess and Zumino prove the consistency/integrability constraints on
  anomalous Ward identities.
- Fujikawa derives the anomaly as the regularized chiral Jacobian of the path
  integral measure.

These are cited as theorem sources, not as observed numerical inputs.

## Framework Hypothesis Check

The framework matter-content surface supplies the left-handed content

```text
(2, 3)_{+1/3} + (2, 1)_{-1}
```

on the `Z^3` spatial substrate; see
[`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md).

The exact rational anomaly traces of this left-handed content are:

```text
Tr[Y]          = 0
Tr[Y^3]        = -16/9
Tr[SU(3)^2 Y]  = 1/3
Tr[SU(2)^2 Y]  = 0
Tr[SU(3)^3]    = 2
```

Therefore three perturbative obstruction traces are nonzero:

```text
Tr[Y^3], Tr[SU(3)^2 Y], Tr[SU(3)^3].
```

By the standard theorem packet above, this left-handed chiral surface cannot
stand alone as a consistent unitary gauge theory. It must be completed by
opposite-chirality matter that cancels the anomaly traces.

## Consequence for the Time-Dimension Bridge

The anomaly-canceling completion is chirally distinguished from the original
left-handed doublets. The framework then needs a chirality grading on the
spacetime carrier. The retained Clifford parity theorem,
[`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md),
proves that such a chirality grading forces total spacetime dimension
`d = d_s + d_t` to be even.

With the spatial substrate `d_s = 3`, even total dimension gives:

```text
d_t in {1, 3, 5, ...}.
```

The single-clock codimension-1 theorem,
[`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md),
then excludes `d_t > 1` on the graph-local arbitrary-data surface. The
intersection is:

```text
d_t = 1.
```

This is the parent 3+1 composition, bounded by the standard ABJ theorem bridge
and by the current audit status of the single-clock theorem.

## How This Differs from the Accepted-Premise Packet

The earlier packet registered the ABJ implication as a named accepted premise.
This note does not do that. It instead makes the ABJ step a cited
standard-theorem bridge with explicit in-repo hypothesis checks.

This matters for audit posture:

- **Not an admitted observed input:** no PDG value, Monte Carlo value,
  plaquette value, fit, or measured spacetime dimension is used.
- **Not a definition:** the ABJ implication is not defined into the framework;
  it is the standard anomaly theorem applied to the framework's chiral
  matter content.
- **Still bounded:** the standard theorem is cited rather than reproved from
  A1+A2 and the finite-lattice action in this note.
- **Next unbounded target:** a framework-native proof would derive the
  regularized chiral Jacobian, Wess-Zumino cocycle, nontrivial anomaly class,
  and no-local-counterterm/BRST obstruction directly on the allowed lattice
  surface.

## Non-Claims

This note does not claim:

- an A1+A2-native derivation of ABJ from the qubit/Cl(3) substrate alone;
- a nonzero index witness for the standard finite even-torus staggered
  `epsilon` operator;
- a bypass of the square-block no-go in
  [`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md`](ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md);
- audit-ratified retained status for the parent 3+1 theorem;
- any numerical claim about the top Yukawa, plaquette, `alpha_LM`,
  Planck scale, PDG inputs, or Monte Carlo data.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_abj_standard_theorem_bridge_for_anomaly_forces_time.py
```

Expected:

```text
TOTAL: PASS=<N> FAIL=0
VERDICT: ABJ standard-theorem bridge passes as bounded theorem support;
no accepted-premise packet is load-bearing for the repaired parent route.
```

## Audit Handoff

```yaml
proposed_claim_type: bounded_theorem
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
target_claim_id: anomaly_forces_time_theorem
target_blocker_text: "ABJ anomaly-to-inconsistency was registered as an accepted premise rather than a cited standard theorem with in-repo hypothesis checks."
reachability_to_target: partially_closes
standard_theorem_dependency:
  id: ABJ/Wess-Zumino/Fujikawa anomaly-to-inconsistency theorem
  status: external_standard_theorem_bridge
framework_native_abj_derivation_closed: false
accepted_premise_packet_load_bearing: false
proposal_allowed: false
proposal_allowed_reason: >
  The bridge removes accepted-premise wording from the parent route, but the
  ABJ theorem itself is cited rather than derived from A1+A2 in this note.
audit_required_before_effective_status_change: true
bare_retained_allowed: false
```

## References

[1] S. L. Adler, "Axial-vector vertex in spinor electrodynamics,"
    Phys. Rev. 177, 2426-2438 (1969),
    <https://doi.org/10.1103/PhysRev.177.2426>.

[2] J. S. Bell and R. Jackiw, "A PCAC puzzle: pi0 -> gamma gamma in the
    sigma model," Nuovo Cim. A 60, 47-61 (1969),
    <https://doi.org/10.1007/BF02823296>.

[3] W. A. Bardeen, "Anomalous Ward identities in spinor field theories,"
    Phys. Rev. 184, 1848-1859 (1969),
    <https://doi.org/10.1103/PhysRev.184.1848>.

[4] J. Wess and B. Zumino, "Consequences of anomalous Ward identities,"
    Phys. Lett. B 37, 95-97 (1971),
    <https://doi.org/10.1016/0370-2693(71)90582-X>.

[5] K. Fujikawa, "Path-integral measure for gauge-invariant fermion theories,"
    Phys. Rev. Lett. 42, 1195-1198 (1979),
    <https://doi.org/10.1103/PhysRevLett.42.1195>.
