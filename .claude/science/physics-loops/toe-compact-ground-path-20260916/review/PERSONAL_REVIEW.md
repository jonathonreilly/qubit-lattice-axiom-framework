# Personal mathematical review and evidence

This is an author review, not an independent reviewer or audit verdict.
The four complete notes were reread after drafting. The carrier/sector,
conditional reflection-square proof, arbitrary even rectangular chessboard
use, repeated boundary events, Schur norm, trace powers, ground limit,
path tightness, local bridge specification, Portmanteau direction and
integer-current orientation were checked analytically. No load-bearing
numerical result is substituted for these arguments.

## Findings and corrections

1. Whole-interval constrained kernels have nonnegative entries but may
   have negative eigenvalues. The proof uses the Hilbert-Schmidt bound
   on even trace powers, without assuming positive semidefiniteness.
   The explicit two-state visit-event kernel has eigenvalues about
   -0.08610725 and0.85356309 and supplies a separate finite countercontrol.
2. A first Fourier cutoff pair32/48 failed the predeclared1e-10 refinement
   check at g=.08 (difference about7.56e-8). Its exact source, stderr and
   diagnostic refinement values are preserved. Cutoffs48/64 satisfy the
   same criterion; no tolerance was loosened. Positive finite-difference
   meshes384/768/1536 independently approach the Fourier result, with
   final relative differences from about7.86e-7 to8.49e-4. These are
   convergence checks, not rigorous Fourier-tail enclosures.
3. Cold reading found an omitted scalar in the prose explaining the
   ground limit for a constrained time window. The corrected expression
   is exp[-(beta-W)(H-E0)] -> ground projector, leaving exp(W E0) times
   the window kernel after thermal normalization. The event bound and
   all constants are unchanged.
4. Decimal illustrations were changed to conservative short bounds;
   80-digit parameter evaluation independently checks the margins.
   Exact formulas, rather than rounded time values, define T.
5. Occupied magnetic cells are defined by a finite union of continuous
   face-supremum events. This covers every cube-charge excursion and
   avoids an unnecessary measurability claim about an uncountable-time
   existential statement for a discontinuous principal-branch charge.
6. The four-dimensional current uses principal values on fixed positive
   orientations and extends them antisymmetrically. Reapplying a half-open
   principal convention after reversing a face at pi would be incorrect.
7. Temporal cochains are explicitly attached to the full-space
   temporal-gauge ground path representation. A full physical electric
   observable/gauge reconstruction is not asserted.

## Reproducible primary checks

Run from repository root:

```sh
python3 .claude/science/physics-loops/toe-compact-ground-path-20260916/evidence/block01_geometry_and_rotor_check.py
python3 .claude/science/physics-loops/toe-compact-ground-path-20260916/evidence/block02_reflection_and_path_check.py
python3 .claude/science/physics-loops/toe-compact-ground-path-20260916/evidence/block03_coarse_current_check.py
python3 .claude/science/physics-loops/toe-compact-ground-path-20260916/evidence/challenge_formula_faults.py
```

Each primary source declares AUDIT_TIMEOUT_SEC=120. Paired FINAL stdout
contains the source SHA256; raw stderr is paired and retained. Raw stdout
is author evidence, not a canonical runner-cache envelope. Pre-metadata
sources and prior outputs are preserved as history, with their own hashes.

The geometry checker reconstructs oriented periodic faces for L=4,6,8,
both normal-face choices and all orientations; it checks actual reflection
maps, no plaquette crossing of a vertex reflection plane, face duplication2,
N/4 edge-disjoint packing and temporal endpoint duplication2. Numerical
trial integrals independently check norm, gradient and variance formulas.
A one-face compact Fourier Hamiltonian is compared with a positive
finite-difference generator, with the correct four-link diffusion metric.

The reflection checker constructs the full4096-state Hamiltonian of a
12-link binary-clock strip and independently its16-state reduced flux
Hamiltonian. At three parameter pairs, ground probabilities agree within
5.5e-15 and residuals are below3.2e-14. The128-dimensional reflection
matrix includes every shared-boundary half-link indicator. Its minimum
eigenvalues are above-1.1e-17; all15 nonempty face subsets satisfy the
corresponding finite chessboard test. This is a structural challenge only;
the strip is not the three-dimensional rotor model.

The same checker verifies the indefinite constrained-kernel example and
even-power trace inequality, free circle fourth moments, and nine
interacting single-rotor moments at two Fourier cutoffs. The largest ratio
to the proposed fourth-moment bound is about0.24745. Its binary plaquette
countercontrol has bad-flux probability asymptotic to4g^8; a finite-clock
jump process is therefore not used to justify the Brownian exponential
estimate in the notes.

The current checker uses exact integer arithmetic on five declared
four-dimensional compact field arrays to check branch integrality,
dJ=0, an independently assembled dual divergence, and all nonzero-cell
face witnesses. It enumerates the fourfold face/three-cell incidence,
degree14 dual-edge adjacency, and fourfold edge dissemination. It does
not sample the ground measure. 80-digit arithmetic gives196p_J about
0.02001985632 at g=.004; the explicit sufficient threshold is about
0.0049791611434. No sharp phase threshold is inferred.

## Fault sensitivity

Eleven specified formula faults were run on preserved scratch copies and
all produced a nonzero exit with the actual failed assertion/lookup kept:
reflected face orientation; trial variance; plaquette diffusivity;
reduced clock edge count; shared-boundary reflection; constrained path
kernel; ground-path diffusivity; binary-clock tail coefficient; cubical
boundary sign; dual Hodge sign; and current witness exponent. The shared
boundary fault is rejected by symmetry before the eigenvalue test, and
the cochain sign fault by integrality before the conservation test.
Those failures are not misreported as sensitivity of later assertions.

## Independent-review and landing obligations

Highest priority: verify that the algebraic chessboard theorem applies to
these link/path cell algebras with all shared boundaries and arbitrary
even rectangular periods. Then inspect the fixed-T/full-time distinction,
physical sector and limiting path specification. Geometry and toy tests
alone do not prove that theorem application.

Canonical note/runner registration, restricted packets, canonical caches,
any formally applicable N-gate certificate and the combined landing
pipeline are pending. No author artifact asserts retained status. The
packet's exact source/receipt identities are checked by the focused
verification report and the manifest, not by this prose count alone.
