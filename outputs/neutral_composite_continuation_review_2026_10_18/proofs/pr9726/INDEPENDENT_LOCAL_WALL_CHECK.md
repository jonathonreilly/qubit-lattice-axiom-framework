# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_LOCAL_WALL_CHECK.md`, SHA256 `ffa3e85c211d1e57870325148461ce5663964d4d5470eec280321a940fd79765`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Focused local wall proof check

This is an independent mathematical check, not a formal audit or a boundary/closure certificate.

The independently executed exact Fraction control is neutral-wall-local-independent.py (Python 3). It checks all 16 oriented diagonal-color pairs, both diagonal excess and hopping, and full K2/N2 columns on all one-/two-active-rung neighborhoods. It obtains wall excess -13/192 and two-rung wall translation -3/64 exactly. A first invocation of `python` failed because that executable is unavailable; the Python 3 invocation completed successfully.

## Diagonal locality argument

The supplied transverse rung matrix has zero diagonal. Any four-operation path returning to the initial product configuration therefore visits at most two distinct rungs: every visited rung requires at least two operations. The folded fourth-order terms have the same support bound. For nonadjacent active rungs the restricted Hamiltonian separates into two independent single-rung problems, including their fixed-neighbor energies. Their fourth-order energy is additive, so their connected contribution vanishes. All relevant one-step excitation costs at the diagonal wall are positive; a hidden zero-denominator intermediate does not invalidate this factorization.

At a single wall, the full local second-order effective and metric columns are diagonal, independently checked for every pair of active positions in the six-site wall neighborhood and for all 16 colors. Thus the scalar RS fourth-order subtraction used in the root script agrees with the canonical diagonal matrix element here. This column check is important: checking only one off-diagonal matrix element would not generally justify replacing the folded matrix product by E2*N2.

Bulk single-rung contribution is 1/64; bulk adjacent connected contribution is -5/192. A periodic uniform vacuum therefore has fourth-order energy per rung -1/96. The wall replaces two singles by 1/8 each and three connected pairs by -9/64, -1/12, -9/64. Subtracting the five bulk terms gives -13/192. Two walls with each intervening domain at least three rungs long have disjoint changed local terms, giving the ground-subtracted diagonal -13/96. This is an all-length local counting statement under these separation and ordinary periodic-neighbor conditions, rather than extrapolation from a finite-size fit.

## Hopping locality argument

Changing a diagonal-color rung from a to b requires at least two transverse operations; the single-rung native matrix element is zero. A displacement of one wall by two rungs therefore consumes all four operations on exactly those two rungs. The root's active-set restriction loses no direct fourth-order path for that matrix element. The independent control evaluates the full two-site resolvent path exactly and obtains -3/64 for every oriented color pair.

Both endpoint states must remain in the separated-wall bulk regime. K1 annihilates these diagonal-color product states, and their K2 and N2 columns are diagonal by the local checks above; consequently the canonical folded terms have zero off-diagonal matrix element. A translated wall then gives the usual two translations and centered Fourier coefficient -3*cos(q)/32. This proof does not cover a shift into a short domain, coincident walls, or a folded finite-ring endpoint.

## Explicit limitations

The root domain2 exploratory row is not the canonical d2 diagonal: its scalar subtraction omits off-diagonal second-order structure. It must remain excluded from any boundary conclusion. The current control gives no complete classification of other fourth-order output channels, no full invariant dark half-line theorem, and no native resonance or pole statement. Establishing these two bulk coefficients does not discharge those tasks. The operator and bond strengths remain those of the supplied native model; no additional interaction was introduced.

## Source identities (SHA-256)

- `/private/tmp/neutral_wall_connected.py`: `6b5915122edd004a287edd979851ced3e5549648b808efdd6d5efb4474b13c79`

- `/private/tmp/neutral_wall_connected.json`: `a98aa4219a14259c594d6f08276a5b94cab55701ca2caa62f02020e6a5f34a43`

- `/private/tmp/neutral_wall_hop.py`: `33cde33134548ee8cbcfa1290c28f4d8a06c814ae49b038c5d0e506a68faf24f`

- `/private/tmp/neutral_wall_hop.json`: `cd64a6a42bcbc56a7665757f6cbddc5ea236daa2657736934f8aae9e498c88fc`

- `/private/tmp/neutral-wall-local-independent.py`: `ab9850ec2cceb9b6265f3a18a23a2c130a3870e455291e173615aceb2b95e53e`

- `/private/tmp/neutral-wall-local-independent.json`: `1440c24ee857330b003d45d39ec0191ba132f39876567152d762aeaf89c8cabb`

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py`: `c14c817d4067501b136a9818d436550af99f8445f220129152b0e37eebdd095d`
