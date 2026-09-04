# Local-force inertial-mass bridge — Cycle 202

Date: 2026-07-16

Status: source-grade exact locality plus deterministic finite numerical probe;
audit unset

Authority: none

Companion runner:
`scripts/local_force_inertial_mass_bridge_cycle202_2026_07_16.py`

This note and runner live only on the draft parking branch and draft PR #5389.
They change no foundation, axiom, primitive, registry, policy, audit, or queue
surface.

## Result up front

The independently derived dispersion mass in Cycle 201 is also the inertial
response measured when a literal local intervention pushes a localized
coherent packet.

The intervention is an onsite phase gradient,

```text
K_F(x) = exp(i F x),
```

which shifts lattice momentum locally rather than assigning an acceleration
or consulting a host-side trajectory. The runner composes that kick with two
live candidates:

1. the strict range-one QCA step; and
2. the finite-range generator `H(k)=sin(k) X + m Z`.

For three masses in each route, a broad positive-band packet is prepared at
rest, pushed for 40 lattice-time units, and its centre is fit to
`x(t)=x_0+v_0 t+a t^2/2`. The measured `F/a` agrees to better than 0.3% with
the curvature mass obtained before this trajectory was constructed:

```text
QCA:          M_inertial = m / sqrt(1-m^2),
Hamiltonian:  M_inertial = m.
```

The finite results are:

| route | supplied `m` | measured `F/a` | curvature mass | relative error |
|---|---:|---:|---:|---:|
| strict QCA | 0.25 | 0.257702 | 0.258199 | 0.192% |
| strict QCA | 0.40 | 0.436762 | 0.436436 | 0.075% |
| strict QCA | 0.65 | 0.855769 | 0.855337 | 0.050% |
| Hamiltonian | 0.25 | 0.249479 | 0.250000 | 0.208% |
| Hamiltonian | 0.40 | 0.400467 | 0.400000 | 0.117% |
| Hamiltonian | 0.65 | 0.650838 | 0.650000 | 0.129% |

For `m=0.4`, a separate four-point sequence weakens the force while narrowing
the momentum distribution. The relative error falls monotonically from
`1.42%` to `0.071%` for the QCA and from `1.92%` to `0.078%` for the
Hamiltonian. The agreement therefore has the expected weak-force,
broad-real-space-packet limit rather than occurring at one tuned point.

Thus the Cycle-201 curvature was not merely a label on a graph. It controls
how a locally forced packet moves. The result is conditional on the supplied
candidate process, packet preparation, coordinate/clock map, and external
force profile. The force remains supplied; it is not derived from the current
record law or from gravity.

## Bare-metal construction

On the one-dimensional slice, the paired-Weyl QCA reduces to

```text
U_m(k) = [[n exp(-ik),  i m],
          [i m,         n exp(ik)]],
n = sqrt(1-m^2).
```

The runner does not treat that Bloch matrix as an abstract black box. It
checks equality with the literal real-space update

```text
psi_0(x) <- n psi_0(x-1) + i m psi_1(x),
psi_1(x) <- i m psi_0(x) + n psi_1(x+1).
```

One step reaches only the same site and one nearest neighbour and preserves
norm exactly to numerical precision. The onsite force kick before and after
that step does not enlarge its range.

For the Hamiltonian route, the runner similarly checks that multiplication by
`sin(k) X + m Z` is exactly the onsite-plus-nearest-neighbour stencil in real
space. This establishes locality of the finite-range generator. Its exact
finite-time exponential has longer tails and is not claimed to be a strict
finite-range cellular-automaton step.

## What is independently compared

The two sides of the bridge are produced by different operations:

| coordinate | construction |
|---|---|
| dispersion mass | inverse Hessian of the untouched rest-band phase or energy at `k=0` |
| inertial mass | supplied local force divided by acceleration fit from a finite packet trajectory |

The trajectory code never reads the target mass formula when applying the
force or updating the packet. The formula is used only afterward as the
acceptance comparison. The simulation retains the full two-component state;
it does not project the packet back into the target band at each step.

The final positive-band probability exceeds `0.99999` in every tested case,
norm is preserved, spatial probabilities remain nonnegative, and the packet
stays far from the periodic boundary. This bounds the observed agreement
against interband leakage, wraparound, and renormalization artifacts.

## Record and identity controls

The moving entity here is a coherent packet, not a record and not yet a
self-bound particle. Its normalized lineage through the supplied unitary
process gives a minimal same-object relation across the rest and moving tests,
but it spreads and depends on boundary preparation.

A decoupled two-state factor labelled as a candidate spectator record is
tensored onto the evolved packet. Changing that factor's basis or adding a
second decoupled copy changes neither position density nor inferred inertial
mass. The factor is a redundancy control, not a claim that Record formation
has been derived.

Consequently:

```text
more durable witnesses do not automatically mean more inertia;
the mass belongs to the law-supported coherent sector;
records may certify identity or store a measurement without being the mass.
```

An explicit dynamical record coupling may change the mass sector, as Cycle
201 showed, but then the change comes from that coupling rather than record
count.

## Schedule, deletion, and phase controls

- Applying the QCA kick before, after, or symmetrically around the range-one
  update gives the same low-force inertial limit within the stated finite
  tolerance.
- Halving the Hamiltonian Strang time step leaves the fitted acceleration
  stable.
- Deleting the force removes acceleration in both routes.
- A constant internal basis change leaves spatial density unchanged.
- The tested QCA mixing angle and onsite force phases are generic complex
  phases, not a real-only or Clifford-quarter-turn regression.

The force field is deliberately coordinate dependent because it is an
external laboratory intervention. It is not proposed as the homogeneous
microscopic law. A future internal force must be generated by another lawful
object or field and recover the same response without this supplied profile.

## Cross-lane effect

### O — operational quantum

The packet uses phase-sensitive coherent evolution and a non-Clifford complex
mixing angle. Its future motion cannot be computed from record count alone.
Cycle 202 does not yet execute the full equal-record-fibre state discriminator,
so it does not by itself decide whether complete records reconstruct the
working state or Qualification needs widening.

### T — time

Inertial response inherits the Cycle-201 clock distinction. Under standard
lattice coordinates, the strict QCA recovers `m/sqrt(1-m^2)` while the local
Hamiltonian generator recovers `m`. One operational tick and one generator
time parameter cannot be silently identified; their calibration is physical.

### I — matter

Rest/dispersion mass now controls a second operational test: response to a
local push. This is the first direct bridge from the mass spectrum coordinate
to inertia in the campaign. Missing are autonomous localization, binding,
collisions, conservation/exchange, species, statistics, and selection of the
coefficient `m`.

### G — gravity

Nothing here identifies the external force with gravity or supplies a source
law. The mass-to-gravity map remains open. The next gravity bridge must show
that the same scalar both sources and responds to a generated lapse/resource
field, rather than naming this inertial coordinate gravitational mass.

### B — boundary

The packet and force profile are prepared inputs. The law does not yet derive
why this packet, mass sector, or intervention occurs. Boundary selection and
recurring autonomous preparation remain open.

## What the probe rules in and does not rule out

It rules in two conditional mass packages:

- a strict discrete update whose finite-lattice inertial coordinate is
  `m/sqrt(1-m^2)`; and
- a finite-range Hamiltonian generator whose inertial coordinate is `m`.

It does not choose between them. The two packages use different exact time and
energy maps, and the framework has not yet selected either map. Other
record-derived, relational, boundary-memory, and history-process realizations
remain live.

## Next construction

The optimum next test is to replace at least one supplied ingredient without
losing the mass triangle:

1. generate a compact or self-trapped coherent object from a local interaction
   rather than a prepared free packet;
2. generate its push through a second lawful carrier rather than a coordinate
   phase profile; and
3. couple the same rest/inertial scalar to a local lapse or conservative
   resource equation, testing source and response separately.

A parallel state-fibre test should ask whether two lawful histories with the
same complete records but different coherent packet phase predict different
later position records. That is the direct connection back to the operational
quantum lane.

## Scope boundary

This is a deterministic finite wavepacket experiment plus exact locality
checks. It is not a self-bound particle, autonomous force, scattering law,
continuum theorem, empirical mass, equivalence principle, or gravitational
source. It selects neither a mass value nor a microscopic law. It makes no
minimum-content or no-go claim and supports no axiom conclusion.
