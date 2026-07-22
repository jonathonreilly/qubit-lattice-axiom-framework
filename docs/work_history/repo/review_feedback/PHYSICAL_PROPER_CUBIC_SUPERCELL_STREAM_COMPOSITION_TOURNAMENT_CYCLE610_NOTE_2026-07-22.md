# Cycle 610 — physical proper-cubic supercell stream/composition tournament

**Authority: none**

**Audit: unset**
**Date: 2026-07-22**

## Result

Route A closes the scoped physical-packing residual left by Cycle 606.  A
translation-invariant `129^3 = 2,146,689`-M2 cubic supercell now contains the
A/B words, equality flag/work, face ports and channels, onsite work, 24
physical one-hot role-orientation M2s, and 24 reusable predicate flag/work M2s.
On the declared code it supplies a literal support-two nearest-neighbor word

`E G_coarse = G_physical E`.

The word is not selected by a Python frame parameter.  The same autonomous
rule is the product of 24 mutually exclusive branches: the same autonomous rule
acts in every lawful orientation sector.  Branch `h` performs an
exact C24X compute of

`P_h = o_h AND (AND_{g != h} NOT o_g)`,

then the accepted Cycle 230 factor order: `P_h`-controlled onsite coin,
controlled Cycle 606 stream (completing `U=S C`), and controlled onsite
contact, followed by exact inverse C24X uncompute.  Each
C24X uses 45 exact Toffoli calls, 46 one-M2 X gates, 22 clean conjunction work
M2s, and one flag M2: 721 already-lowered support-one/two gates for compute and
721 for uncompute.  The orientation M2s are unchanged.  Exactly-one-hot and
nearest-neighbor equality are bounded local constraints; their uniform genesis
is still supplied.

The physical compiler is intentionally enormous, not optimized.  One branch
contains 770,876 lowered primitive gates before bus moves and
102,693,692,972 returned bus SWAPs.  The full 24-branch autonomous product has
18,501,024 lowered primitives and 2,464,648,631,328 returned bus SWAPs per
coarse cell.  This is constant overhead and bounded depth independent of L,
but it is a feasibility construction rather than a plausible economical law.

## Literal routing, rather than a distance count

Every support-two primitive is represented by its ordered endpoint M2s, its
two indices on a Hamiltonian nearest-neighbor bus through all 2,146,689 sites,
the exact opening SWAP interval, the adjacent application edge, and the reverse
interval.  All 2,146,688 bus edges were checked for nearest-neighbor adjacency,
and the coordinate/index inverse had zero failures.  The largest realized bus
distance was 1,168,111.  Move/apply/restore is a conjugation, so intermediate
data are restored even when the bus is not blank.

The one identity-frame word is frozen by a literal route hash.  Each of the
other 23 words is its explicit integer proper-cubic spatial image.  Their
rotation-normalized words agree.  The runner checks all 576 frame products on
1,492 route-generator coordinates, for 859,392 composition checks with zero
failure, as well as 35,808 rotated-bus endpoint/index checks.  Thus all 24
one-hot sectors are accepted by the same covariant rule; no frame is supplied
by host-side control.

The 72 cross-face port SWAPs per branch require both adjacent predicates.  A
source predicate is copied to the clean M2 one step inside its face and the
target predicate is copied to the corresponding target M2.  A literal
five-site line then applies CNOT, exact triple-controlled X, CNOT, after which
both copies are uncomputed.  Its 110 direct nearest-neighbor microsteps have
clean-scratch controlled-SWAP residual `7.80e-16`, scratch leakage `2.16e-16`,
and full-unitarity residual `6.06e-15`.

The physical hash is order-sensitive.  A direct Cycle 230 factor audit gives
`||U-SC||=0` and a `0.5202793649` difference between the accepted
coin -> stream -> contact step and the reversed contact-before-free schedule.
On the seeded random antisymmetric probe, deleting coin, stream, or contact
changes the output by `1.90208`, `1.99689`, and `0.088280`, respectively.  The
contact/free-generator noncommutation witness is `2.39348`.  Thus factor order
is tested content of the compiled word, not prose inferred from separate
fixture preservation.  The fixed microstep order is supplied law content; it
is not physical time.

## Geometry and global controls

The cubic cell has side `K=129` and local coordinates `[-64,64]^3`.  Three
species centers are separated, and source and target routes use disjoint role
families.  Each physical cell is simultaneously the source of one directed
bond and the target of another without sharing port roles.  The exact schedule
serializes operations within a cell; identical cell-bus microsteps run in
parallel because the translated supercell boxes tile the fine torus
bijectively.  Cross-bond five-site supports were checked exhaustively.

For L3, L6, and L7, respectively, the controlled global audit checked 11,664,
93,312, and 148,176 five-line supports over all 24 frames, six directions,
three species, and every cell.  Every vertex conflict, edge conflict,
nearest-neighbor failures, and wrap seam failures were all zero.  Every
coarse translation—27, 216, and 343—was checked.  The earlier explicit flag
shuttle audit also retained zero conflicts across
3,125,952/25,007,616/39,711,168 routed edge instances and
11,664/93,312/148,176 cross edges on L3/L6/L7; each size executed 50,112
frame/direction path-template microsteps.

The schedule is an update factorization: the schedule is not time.  Its depth
is not a causal duration, and its site or gate count is not energy or a gravity
source.

## Semantics and adversarial controls

The declared code is: valid A words; B, path, equality and predicate work
blank; exactly one of the 24 physical orientation M2s hot in every cell with
the same neighbor value; and the inherited exactly-one-carrier-per-species
global sector.  On that code, exactly one controlled branch acts.  Bus routing
and predicate compute/uncompute are exact conjugations, so the already tested
Cycle 606 register permutation is the logical action.

The train/held/held-out-size semantics suite uses L3/L6/L7.  It covers every
site, all three species, and labels 1 through 9; blank-buffer return; exact
inverse; ten random full-space inverse trials per L; deletion of scatter,
clear, and swap macro factors; duplicate-carrier collisions; label order; and
the Cycle 600 exterior/seam fixtures.  All lawful and inverse failures remain
zero.  Duplicate-carrier malformed states remain reversible but leave the
declared code; they are not repaired.

For clean predicate work, zero-hot and multi-hot orientation words activate no
branch, so the selected-action extension is identity and the compute/uncompute
work returns.  Arbitrary dirty predicate work is outside the code; the full
gate product remains unitary, but no identity-extension claim is made there.

The composed one-particle mass fixture is preserved.  The inherited compiled
full-16 coin residual is `8.62e-14`, its cubic symmetry residual is `1.73e-16`,
and clean scratch leakage is `2.89e-15`.  The local contact and inverse-contact
phase residuals are zero.  Cycle 600 coin/contact/local-stream seam E/G
residuals are `1.15e-15`, zero, and zero; the compiled word-coin E/G residual
is `4.03e-13`.  These are exact move/apply/restore composition checks, not a
claim that the inherited beta and contact-g analog angles have been derived.

## Supplied structure

The construction still supplies, explicitly:

1. the `129^3` supercell placement and bounded structural role/color motif;
2. the uniform physical one-hot role orientation and its crystalline phase;
3. blank B/path/equality/predicate work at encoding;
4. the inherited global exactly-one-carrier-per-species sector;
5. the Cycle 230 coin -> stream -> contact order and the scatter/clear/swap
   macro factorization;
6. calibrated beta/contact-g parameterized rotations;
7. periodic L3/L6/L7 fixtures, although the local rule never queries L.

There is no global Jordan-Wigner parity string, parity service, preferred
carrier ordering, host frame selector, origin query, or size query.  The
bounded role motif and uniform one-hot genesis are imports, not derived
features, and must not be hidden by the phrase translation invariant.

## Route disposition

- **Route A — compact double buffer:** constructive success on the declared
  code.  Physical one-hot selection, literal NN selector/control routing,
  dual-neighbor cross control, onsite mass/contact composition, global
  conflicts, all 24 frames, all 576
  frame products, L3/L6/L7, every translation, and wrap seam checks pass.
- **Route B — direction-expanded lanes:** not triggered in Cycle 610.  The
  Cycle 606 register result remains a valid fallback, but its 28-M2 local
  exchange and its own physical packing were not silently credited here.
- **Route C — state-carried phase/time multiplexing:** not triggered.  Its
  uniform phase genesis and physical packing remain imports; no schedule is
  called physical time.

## Six-wall dependency ledger

- `C_ref`: advanced within the compiler lane.  A host-selected frame has been
  replaced by counted one-hot M2 state and a proper-cubic covariant autonomous
  branch product.  Uniform orientation/role genesis is still supplied, so the
  broad reference wall is not retired.
- `C_num`: unchanged.  Beta/contact-g analog angles and finite-precision
  scaling remain open.
- `C_wrap`: unchanged.  Wrapped phase is not called energy.
- `C_int`: advanced.  The exact Cycle 603 mass/contact block and Cycle 606
  stream now compose inside one physical NN word on the declared code; the
  calibrated coupling and malformed collision sector remain.
- `C_local`: the specific Cycle 606 simultaneous physical-supercell packing
  residual is closed constructively.  Economical overhead, autonomous role
  genesis, local particle-sector generation, and collision repair remain.
- `C_source`: unchanged.  Auxiliary, carrier, and gate counts are bookkeeping,
  not a source or gravity derivation.

## N1–N8 no-go discipline

**N1.** Six normalized families remain separated: physical one-hot compact
Route A; direction-expanded Route B; state-carried Route C; co-present 24-copy
orbit coding; cell Hamiltonian-bus composition; and bounded role-color
scheduling.  Route A and the bus composition are the positive result; the
others remain live alternatives or fallbacks.

**N2.** Uniform orientation genesis, the global one-carrier sector, blank work,
analog calibration, and macro factorization are pairwise independent supplied
structures.  Closing physical routing does not close any of them.

**N3.** The hidden-wall scan exposes the one-hot orientation M2s, clean work,
structural motif, empty spacer sites, full bus, exactly-one sector, periodic
fixtures, and calibrated angles.  No Python selector survives in the update.

**N4.** The Cycle 606 physical-packing residual is matched and closed by the
literal controlled word.  The Cycle 603 analog-angle residual and the Cycle
606 malformed duplicate-carrier residual are matched but not closed.

**N5.** “Physical compiler” is restricted to the declared code and supplied
role sector.  “All 24” means mutually exclusive physical predicates, not a host
choice.  A schedule is not time, site count is not energy, and auxiliary state
is not a source.

**N6.** Live partial-closure paths are autonomous preparation of the role
phase, a reversible local collision/syndrome reservoir, certified epsilon
synthesis for beta/g, and a much smaller packing searched under the same
collision certificate.

**N7.** A hostile reviewer should reject any claim that orientation genesis,
particle-number control, analog angles, or the huge overhead are unavoidable.
Ordered phases, orbit/lane codes, syndrome reservoirs, and synthesis are live
constructive counterroutes.

**N8.** Cycles 580, 600, 603, and 606 repeatedly turned apparent services into
bounded objects.  Cycle 610 does the same for physical simultaneous packing.
That cross-cycle echo weighs against an impossibility or minimum-content claim.

No negative claim is shipped.  No shared obstruction is established, and
there is no axiom pressure.

## Next campaign

The highest-value next step is to replace the supplied uniform role-orientation
phase and inherited global one-carrier sector by autonomous local
preparation/syndrome dynamics.  In parallel, search for a smaller covariant
cell using this exact conflict certificate and add a declared volume/horizon
precision budget for beta/contact g.  The current result should be retained as
a constructive upper bound, not mistaken for a minimal architecture.
