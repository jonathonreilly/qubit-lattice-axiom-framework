# No-Go Ledger — poisson-self-bound-source (cycle 713)

Read by proof, not by headline, per the skill's step 4.

## Prior no-gos and negative results in this lane

### PR #5693 (cycle 712), rows U1-U9 — the immediate parent

- **Exact quantified scope.** Under the parent note's own fit window on its own
  Dirichlet operators the `beta` diagnostic is inverted (biharmonic `1.005`,
  Poisson `1.796` at `N=24`). Under a fixed window on a boundary-free torus with
  a **prescribed** localized source, unscreened Poisson uniquely gives the
  Newtonian exponent (`4*pi*r*G -> 0.892` at `N=256`).
- **Supplied premise the refutation leans on.** U9's negative half — "the
  self-consistent construction cannot supply a localized source" — was measured
  for **the propagator density only**, in both of its branches: with the
  per-layer normalization (`RMS/N ~ 0.30`, mass pinned to 1) and without it
  (mass diverging `4.19e6 -> 1.38e20`).
- **Named live route, verbatim.** *"any future self-consistency claim in this
  lane needs a source term that is not the normalized propagator density."*
  That escape is the target of this cycle. U9 is not a no-go against
  self-consistency; it is a no-go against one source.

### PR #5662 (cycle 711), rows S1-S8

- **Scope.** The self-consistent `beta` does not extrapolate to `1.0`
  (`1.2747 +/- 0.0177`, `1.1578 +/- 0.0012`); the ranking is indeterminate
  because the extrapolation families disagree on sign.
- **Mechanism, which is the reusable part.** The fit window lies *inside* the
  source and the enclosed fraction *rises* with the box (`0.5067 -> 0.8449`).
  This cycle's condition 1 (extent converges) is the direct repair of that
  mechanism, and its condition 2 (depth converges) is the part cycle 711 did
  not test.

### PR #5656 (cycle 710), rows R1-R16

- **Scope.** Both of the parent note's operator discriminators are empty: the
  matched point-to-point kernel gives `corr = -0.06` where the note reports
  `0.93`, and after consistent sign normalization all four operators are
  attractive and monotone.
- **Escape it leaves.** R16 retreated to "the `beta` comparison establishes no
  operator as best" rather than "Poisson is not best". That retreat left the
  operator-selection question **open**, not closed — which is what makes a
  positive selection result admissible in this cycle at all.

### `docs/MATTER_SELF_FOCUSING_NOTE.md` (2026-04-07)

- **Scope.** A two-pass self-focusing propagator reduces an equivalence-principle
  deviation from 123% to 44.05% at `lambda = 1` and does not restore
  equivalence; family portability collapses (`R^2` `0.09-0.18`).
- **Supplied premise.** The self-field is built from the **propagator amplitude
  density**, the same object cycle 712 ruled out. Its failure is therefore
  evidence for the successor direction, not against it.
- **Status.** `leaf`, `verdict: null`, in-degree 0. Prior-art evidence, not
  authority.

### `docs/BOUND_STATE_SELECTION_NOTE.md`

- **Scope.** Finite-lattice diagnostics for bound states in an **external**
  Coulomb potential; carries an unretired `missing_bridge_theorem` for the
  finite-to-continuum step, and its own note records that the runner never
  flagged fall-to-center despite the prose claiming it.
- Not a wall for this cycle: the potential there is prescribed, not sourced by
  the state.

## Structurally similar wall retired by a mechanism worth reusing

Cycle 712's wall — "the diagnostic has no far field" — was retired by *fixing
the measurement window in absolute units instead of box units*. The same move is
what turns "the width stops growing" into a real test here: fixing the coupling
and letting the box grow, then demanding that **both** the extent and the depth
have limits. A width-only criterion is exactly the criterion the landed
frozen-stars note used, and it passes for a state that is merely box-squeezed.
