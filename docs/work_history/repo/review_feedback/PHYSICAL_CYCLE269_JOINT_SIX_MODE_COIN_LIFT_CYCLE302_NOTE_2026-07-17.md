# Physical Cycle-269 joint six-mode coin lift — Cycle 302

**Authority: none. Audit: unset.** This is a bounded constructive probe on the
existing draft parking branch. It does not edit axioms, foundation,
Qualification, primitives, registries, policies, queues, or audit status.

## Result

The actual Cycle 219 six-mode proper-cubic matter coin has an exact local
code-space lift on the fixed-Wilson Cycle 269 reference-relative face code
with the collision-safe auxiliary ports. The encoding uses a coherent
five-ray shell for each logical direction. For body direction `d`, the
reference ray `a` ranges over the five non-antipodal rays. Each of the thirty
orthogonal physical ray states contains exactly two face-code occupations:
the body port `(x,d)` and the outer neighbor reached through `(x,a)`. Its two
port tags change jointly with those occupations, so every state obeys
`B_v Z_port(v)=+1`.

Let `E` be the normalized 30-by-6 shell isometry and `C` the Cycle 219 coin.
First define the 30-by-30 coefficient block

`u = I - E E^dagger + E C E^dagger`.

This dense block is not by itself called the physical update.  With the local
matrix units `M_ij` defined below and `Pi_shell=sum_j Pi_j`, the bounded
physical polynomial is

`U_physical = I - Pi_shell + sum_ij u_ij M_ij`.

It acts as `u` on every one of the thirty locally labelled sectors and as the
identity on all other local tag patterns.

The runner obtains, to machine precision,

`E^dagger E = I`, `E C = U_physical E`, `U_physical^dagger U_physical = I`,

with zero decoded leakage. This includes a genuinely coherent held vector
with nonzero amplitude in all six local directions, not merely six classical
fixtures. The beta values `-0.2,-0.3,-0.4` and held `-0.35` all pass. The
encoded uniform-direction eigenstate retains the Cycle 219 rest-mass fixture
exactly. This preserves that fixture; it does not independently rederive the
dispersion, inertial, or exchange-mass probes without a physical stream lift.

## Local physical realization

This is not a global-vacuum rank projector disguised as a local gate. Write
`W_i` for the bounded joint face/tag Pauli representative of ray sector `i`
and `Pi_i` for the projector onto its twelve local tag bits. The local matrix
units are

`M_ij = W_i W_j^dagger Pi_j`.

The thirty tag patterns are distinct.  The executable projector-transport
audit verifies `W_i W_j^dagger Pi_j = Pi_i W_i W_j^dagger`,
`M_ij M_kl=delta_jk M_il`, and `M_ij^dagger=M_ji`, including exact action on
the physical representatives.  Each twelve-bit projector generator commutes
with all local auxiliary constraints and fixed-sector generators.  Thus the
displayed 30-by-30 coefficient block has an exact finite-dimensional unitary
matrix-unit completion on the physical neighborhood, with identity on the
other 4,066 local tag patterns. Every transition
`W_i W_j^dagger` commutes with every affected `B_v Z_port(v)`, so the update
preserves the local auxiliary/gauge constraints rather than checking them on
the host after the fact. There is no tag copying: the gate coherently
mixes joint face/tag sectors, and there is no separate tag-copy step or
host-side direction service.

At the origin convention the union support is thirty face M2 plus twelve port
M2, hence forty-two M2.  The adversarial all-anchor sweep found that translated
graph-order representatives use 30, 34, 38, or 42 face M2 plus the same twelve
port M2.  Therefore the exact theorem is bounded support of 42, 46, 50, or 54
M2—at most fifty-four M2—in a body-and-neighbor neighborhood.  Each
representative word uses 14 or 15 M2, not uniformly fourteen.  All anchors at
both `L=3` and held `L=6` were checked.  The installed overhead remains
twenty-one M2 per cell: fifteen Cycle 269 face M2 and six auxiliary port M2.
Support and overhead are independent of lattice size.

## Cubic covariance and the phase cocycle

The raw equal-phase five-ray shell fails to transform coherently in 108 of
the 144 frame/direction columns because the existing Cycle 269 incident-order
Clifford repair contributes ray-dependent signs. This is a phase-convention
failure of the raw candidate, not a substrate obstruction.

The full binary GF(2) cocycle system has 720 equations, equally split between
raw `+1` and `-1` phases.  Its coefficient and augmented ranks are both five.
It has exactly two six-bit solutions, `010101` and `101010`, which differ by
one global sign.  Thus the GF(2) cocycle repair is unique up to the irrelevant
global ray phase.  Choosing `010101` multiplies a ray
representative by `-1` precisely when its reference ray is a positive
coordinate ray, and by `+1` on a negative coordinate ray. This convention
uses ray orientation but no preferred axis order. After dressing, all 19,440
joint state-ray tests (30 rays at every one of 27 L=3 body cells under all 24
proper-cubic frames) have zero face-phase and zero tag-permutation mismatch.
The shell isometry intertwines the ordinary six-direction permutation
representation, all 576 frame group products pass exactly, and the lifted
Cycle 219 coin is invariant under all frames. All 27 L=3 translations also
pass for the joint face/tag representatives. Held L=6 reproduces the
occupation, constraint, orthogonality, bounded-support, and overhead results.

## Deletion and lawful-domain controls

- Setting the logical coin to identity makes `U_physical` exactly identity.
- The beta=0 block exactly lifts the Cycle 219 massless field endpoint.
- Deleting the port tags makes every one of the thirty rays violate its
  required occupation/tag match and is rejected.
- Deleting the orientation phase dressing reproduces the 108 frame-column
  failures above.
- Deleting the largest nonzero local matrix-unit coefficient produces
  intertwining residual `0.06060683411028461` and unitarity residual
  `0.19077362394740982`.
- Antipodal direct-shell labels, invalid port labels, and periodic `L=2` are
  rejected rather than silently reinterpreted.

## Supplied structure and exact boundary

Supplied here are the fixed +++ Wilson sector and reference vacuum, the Cycle
269 pyramid cellulation and framing repair, the six auxiliary port M2 and
their local constraints, the five-ray shell ansatz, one global phase-origin
convention, and the Cycle 219 coin coefficient matrix. Derived here are the
rank-five GF(2) dressing solution class, the local matrix-unit completion, the
isometry, exact intertwining, inverse/unitarity, zero code-space leakage,
projector transport, constraint preservation, bounded support, translation
covariance, proper-cubic covariance, and rest-mass-fixture preservation.

Absolute vacuum preparation remains open. Coherent position remains open:
this probe coheres directions at one supplied body cell but does not yet
superpose or autonomously address different body cells. Full-Fock compilation
remains open, as do a primitive-gate synthesis of the dense local coin block,
stream/contact composition on this shell, and collision rules for multiple
simultaneous shells. These are residual compiler seams, not shared substrate
obstructions.

The wrapped eigenphase retained from Cycle 219 is not physical energy, the
local gate or any generator element is not a rate, and this result supplies no
gravity/source semantics. It makes no Record claim. It is a reference-relative
matter/auxiliary compiler advance only.

## N1–N8 discipline boundary

- **N1 alternatives:** diagonal reference pairs, the retained five-ray shell,
  an antipodal six-ray path completion, and a local matrix-unit block were
  considered. The five-ray construction avoids a copied direction reference
  while retaining a direct bounded path for every term.
- **N2 wall independence:** no constitutional wall is inferred; the remaining
  stream, position, Fock, and primitive-synthesis tasks are distinct seams.
- **N3 hidden-wall scan:** global vacuum preparation, coherent addressing,
  simultaneous-shell collisions, and the supplied dense block are explicit.
- **N4 residual matching:** the theorem is only the local six-direction coin
  plus auxiliary constraints in the declared reference-relative sector.
- **N5 rhetoric audit:** this is not called a full physical-site compiler,
  energy, rate, Record, gravity law, or law-selected mass spectrum.
- **N6 partial closure:** the prior six-mode-coin residual is closed at exact
  local code-space level while the named composition seams remain.
- **N7 steelman:** the matrix-unit construction makes the block a bounded
  physical operator rather than only a 30-by-30 numerical analogy.
- **N8 cross-cycle echo:** earlier route-specific phase and localization
  failures are not promoted into a repeated no-go premise.

There is no no-go claim and no axiom pressure from this result.
