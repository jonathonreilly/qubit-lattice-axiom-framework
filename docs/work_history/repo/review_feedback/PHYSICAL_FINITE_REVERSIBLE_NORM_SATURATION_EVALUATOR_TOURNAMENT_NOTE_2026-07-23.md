# Finite-valued norm/saturation arithmetic and reversible-oracle tournament

Date: 2026-07-23

Authority: none

Audit: unset

Cycle claim: 680 (claimed strictly above the joint visible max 679 at the
2026-07-23 re-fetch: our Record/Born discriminator PR claims 679; campaign tip
`fb0ab5636e` filenames reach 678). Descriptive filenames per the owner
directive; the cycle number appears only in runner, receipt, and note content.

## Frozen question and conjunctive success gate

How much of the supplied continuous arithmetic of the campaign Cycle-626
Route-A normalizer and Route-B saturation can be replaced by EXECUTED
finite-valued arithmetic on a declared value lattice, with an exact reversible
oracle embedding on the value-basis code space, all-24-frame covariance,
support-two lowering of the output-register rotations, and a certified
quantization bound against the continuous reference evaluated on the actual
landed Cycle-576 deficit orbits, without changing the exact-pinned,
audit-unset actuation interface and without selecting any sign, scale,
regulator, or receiver association?

Success was frozen before running and requires all of: an exact reversible
oracle embedding with the represented square/accumulator ancillae restored
exactly; a fully materialized micro integer permutation matrix (unitary,
linear, ancilla exactly unentangled); a derived (not fitted) quantization bound
that is valid on every evaluated input and demonstrably informative; an exact
zero branch at regulator zero; exact all-24 covariance with all 576
label-permutation products; and an actuation endpoint match within the
propagated bound with no refit. A gate-level reversible compiler for the
reciprocal-square-root control logic and Route-B rational arithmetic was not
part of the executed construction and remains open.

## Construction

The value lattice L_Q = {k/Q : |k| <= 2Q} at Q in {64, 256} with input floor
FLOOR = 0.1 is DECLARED SUPPLIED STRUCTURE, as are the regulator grid
eps in {0, 1/2, 1, 2}, the register widths, and the actuation grid. The input
population is the curated set of 24 actual Cycle-576 deficit orbits (the three
non-degenerate source profiles TRAIN_XY / TRAIN_DIAGONAL / BLINDED_HELD_OBLIQUE
on L3/L6/L7 at declared asymmetric sites; orbit norms 0.2092 to 1.1547, all
above FLOOR). The delta-like BLINDED_HELD_POINT_NEUTRAL profile (L7 orbit norm
0.0143, below FLOOR, site-independent) is EXCLUDED from the population and used
as a real-data refusal witness. The 24-frame orbit is the scalar real-space
c576 source value per proper-cubic frame (the rotate-profile idiom); the
momentum-space 15-vector was deliberately NOT scalarised through a chosen
covector, because that choice would smuggle a receiver association.

E1 (Route-A normalizer, finite): integer squares, accumulator, and a certified
integer reciprocal-sqrt-multiply — a = round(Q|k|/sqrt(M)) certified by the
exact integer inequalities 4B^2 < (2a+1)^2 M and (a=0 or (2a-1)^2 M <= 4B^2),
no float in the certificate. The executed map is embedded as the exact oracle
permutation (k,r) -> (k,r+f(k)) on modular output rails. The explicitly
represented square/accumulator work registers are garbage-free after
uncomputation, with residual exactly 0. The control logic that selects the
certified integer a is evaluated by the runner but is not compiled into
reversible primitive gates. The eps=0 zero branch is decided by an exact
integer zero test and produces the exact zero output with no division on that
path. A nonzero input
below FLOOR is refused with a witness, never silently evaluated.

E2 (Route-B saturation, exact rational): r' = r0 + sigma kappa alpha
(r-rho)/(1+alpha|r-rho|) evaluated in exact rational arithmetic over the frozen
sigma/kappa/alpha grid on a 41-point rational r-grid; r0 = 3/10 and rho = -1/5
are declared fixture constants (the c626 fixture derives its receiver values
through unlanded campaign modules, so no landed byte source exists for them).
Observed maximum reduced denominator is 410. Independently of the saturation
implementation, writing r=t/10, rho=-2/10, alpha=A/2, and kappa=K/2 gives a
raw nonlinear denominator 2(20+A|t+2|); after adding r0=3/10 the reduced
denominator divides lcm(10,2(20+A|t+2|)). Its maximum on the frozen grid is
1080. Zero-input and receiver-zero controls are exact; injectivity over the
grid is witnessed. This is exact finite rational arithmetic, not a compiled
reversible Route-B circuit.

The reversible-oracle embedding and its explicitly represented work-register
operations are established in tiers, stated plainly: modular adders are
exhaustively verified bijective for both m = 2Q+1; the squarer as the pair map
(k, c) -> (k, c + k^2) exhaustively bijective and exactly inverted; the
accumulator add); the composition row verifies every gate in the actual
circuit trace is one of the verified primitive kinds; the reduced fixture
(3 registers, Q = 16) is enumerated in full with ancillae restored on every
input and the integer certificate cross-checked against an independent float
reference; and the oracle micro instance (Q = 4, three registers, full state space
D = 78732 with ancilla) is fully materialised as an integer permutation
matrix — bijection, exact unitarity (P^T P - I has zero nonzeros), linearity
and norm preservation on seeded complex superpositions, and EXACT ancilla
unentanglement (amplitude weight on nonzero-ancilla basis states exactly 0.0
on a superposition of two distinct actual quantized orbits). The full
24-register instance is evaluated with the represented work registers restored
on every population orbit plus adversarial boundary inputs. Full oracle
bijectivity follows from retaining k and modularly adding f(k) to the output
register; the full state space is NOT exhaustively materialized. This does not
prove a gate-level compiler for the certified-round selection logic.

Support-two output-rotation lowering: every modular rotation add-by-j on the micro register
decomposes into adjacent rail transpositions with exact recomposition
(exhaustive over all j; max word length within the m(m-1)/2 bound), matching
the campaign unary idiom in which a modular increment is a SWAP word. The
output-rotation SWAP budget is derived from the explicit-operation trace (24
modular output adds per evaluation) times the verified per-rotation bound:
198,144 (Q=64) and 3,151,872 (Q=256), within the declared 10^7 cap. This
budget excludes the reciprocal-square-root control logic, square/accumulator
work, and Route-B compilation; it is not a full-evaluator gate budget.

Quantization bound: B(eps, Q) = (sqrt(24)/(2Q)) (L + 1) with L = 1/FLOOR at
eps=0 (domain-floored) and L = 1/eps otherwise, derived from the Lipschitz
constant of the normalizer on the declared domain plus output rounding.
Validity holds on every evaluated input at both Q; the bound is informative
(max observed-error/bound ratios 0.26-0.71 across the eps x Q grid, well
above the 1/8 informativeness threshold); B(256)/B(64) = 1/4 exactly and the
observed maxima scale consistently.

Actuation interface (unchanged from c626 Route A): H_A = b sigma kappa
(|0><n| + |n><0|) on the one-excitation block, driven by the finite
evaluator's output. Lambda enters INPUT-SIDE, faithful to the c626 member
loop (it scales the orbit before normalization; the magnitude cancels only
at eps=0). For this endpoint lane only, the population is thinned to the first
valid orbit in frozen enumeration order for each declared length L=3,6,7; the
covariance and quantization-bound lanes use the full 24-orbit population. The
improvement axis c is DECLARED-ABSENT: c626's improvement
vector is the spatial trace vector of the unlanded Cycle-620 module
contracted with the momentum, so the c grid is not executable off main and
no substitute semantics were invented. Endpoint deltas |P_finite - P_exact|
reach at most 1.81e-3 (Q=64) and 3.85e-4 (Q=256), inside the propagated bound
2 t max|b sigma kappa| B(eps,Q) for every grid member; both quadrature signs
occur; the zero-coupling deletion control is quiet.

## Preregistered falsifiers (all fired as designed)

- F1 garbage retention: the uncompute-skipping variant FAILS the cleanliness
  certificate with nonzero amplitude weight on nonzero-ancilla states, while
  the clean evaluator's weight is exactly 0.0.
- F2 irreversibility: the truncating (input-overwriting) variant produces the
  explicit collision pair (-2,-2,-2) and (-1,-1,-1) mapping to the same
  output rails.
- F3 zero branch: the all-zero orbit yields the exact zero output through the
  full circuit at eps=0.
- F4 below-floor refusal: the synthetic 1/64 input is refused with a witness;
  the real BLINDED_HELD_POINT_NEUTRAL L7 orbit (norm 0.0143) lands in the
  exact-zero branch under quantization with its true norm strictly inside
  (0, FLOOR); healthy population orbits are evaluated, not refused.
- F5 no refit: one frozen TOL table; FLOOR, grids, and bound constants frozen
  at the top of the runner.

## Supplied, derived, and open

Supplied: the landed c576 source profiles, 24 proper-cubic frames and
frame-sector permutation machinery; the value lattice, FLOOR, register
widths; the regulator/saturation/actuation grids; r0 and rho as declared
fixture constants.

Derived or executed: the certified integer reciprocal-sqrt-multiply; the exact
reversible-oracle embedding with represented square/accumulator work registers
restored; exact covariance across all 24 population orbits and all 24 frames
(4608 integer comparisons) and all 576 label-permutation products; the derived
quantization bound with validity, tightness, and 1/Q scaling; the exact-rational
saturation with denominator census, analytic raw-denominator bound, and exact
controls; the materialised oracle permutation matrix with exact unitarity,
linearity, and ancilla unentanglement; the support-two output-rail SWAP
recomposition with a trace-derived output-rotation budget; the actuation
endpoint match within the propagated bound.

Open: arbitrary-precision and continuum evaluators and non-lattice inputs;
gate-level reversible compilation of the reciprocal-square-root selection
logic, work-register arithmetic, and Route-B rational map; support-two
lowering and a resource bound for the full controlled evaluator;
selection of every sign, scale, regulator, saturation scale, and lambda (the
full grid survives); the declared-absent improvement axis pending a landed
Cycle-620; endogenous source profiles; any physical identification (this
tournament is arithmetic-wall closure, not gravity — see firewalls).

## Firewalls

Constructive finite-arithmetic and reversible-oracle support on the declared
lattices only; the full gate-level finite-evaluator compiler, arbitrary-
precision evaluator, and continuum evaluator remain open. Support-two lowering
and its SWAP budget cover the output-register rotations only; reciprocal-
square-root control logic, work-register arithmetic, and Route-B gate
compilation are not supplied. No sign, scale, regulator, saturation-scale, or
lambda is selected; branch selection remains open. No shared-code 3/4 DELAY
association is derived; the PR5557 acceptance harness is untouched; the 5/4
ADVANCE count-edit interface is not driven. This is not gravity, not physical
stress, not energy, not a source law, not a causal rate, not an event, Record,
or Born claim; a contact-sensitive response is not energy, stress, source, or
gravity. The value lattice, FLOOR, register widths, and grids are declared
supplied structure; no axiom, primitive, or premise class is added.

## No-go discipline

No negative claim is frozen by this tournament: the result is bounded exact
support on declared lattices. The missing gate-level compiler is recorded as
an open proof obligation, not an impossibility claim. The prior walls it leaves
intact (sign/scale selection, the open/periodic domain join, the DELAY
association, the ADVANCE count-edit) remain read-only campaign context and are
not re-proved here.

## Evidence anchors and pins

Landed hard import (verified on disk at run time after the parent review
repair): the Cycle-576 runner (7980bff1...), note (5822c14b...), and receipt
(bc719ca8...). These exact-pinned bytes remain Authority none / Audit unset.
Read-only
campaign evidence anchors at campaign head fb0ab5636e (recorded, transcribed,
never imported or executed): the Cycle-626 note (1346e9c5...), runner
(a775cb75...), and receipt (ab8489e9...), whose Route-A/B reference residuals
and deletion floors are transcribed in the runner's pin block for context.

## Cold run

The canonical runner
`scripts/physical_finite_reversible_norm_saturation_evaluator_tournament_2026_07_23.py`
closes 32/32 rows with zero failures (exit 0) on current main after the
Cycle-576 review repair; the paired receipt and cold transcript are frozen
alongside this note. The terminal label reports bounded arithmetic/oracle
support, not closure of the gate-level local-evaluator compiler.
