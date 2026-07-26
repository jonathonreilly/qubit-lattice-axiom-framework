# Promotion Value Gate — Cycle 707

## Prior-art sweep

- Ref refreshed; searched commit `922b9b12a6`.
- Searched on the statement:
  - `"first.order perturbation.*(linear|exponent|p = 1)"`, `"degenerate perturbation.*(sqrt|half)"` → **zero hits**
  - `"(derive|theorem).*exponent.*(power of f|f-power)"`, `"why.*linear in f"` → **zero hits**
  - `"additive.*(linear response)"`, `"potential.*enters.*linear"` → **one hit**, the heuristic bullet in `GRAVITY_FULL_SELF_CONSISTENCY_NOTE` that this note cites as its conditional premise
  - `"neutral sector|zero mode|constant mode"` → hits, none about `G_0`'s existence on the torus
- Classification: `ACTION_UNIQUENESS_NOTE` is the parent observation and is cited, not restated; `ACTION_POWER_3D_OPERATOR_CAUCHY_NOTE` shows the continuum lift of these classes fails via the `h→0` operator-Cauchy lane — a **different** lane from this note's lattice-native perturbation argument, so not blocking.

## V1 — the claim in one sentence

The weak-field mass-law exponent is a positive **integer** whenever the field
enters as a self-adjoint perturbation (so the sublinear `p=1/2` rival is
excluded outright), it equals 1 unless the first-order matrix element
vanishes, and P4's named rival `S = L√(1-φ)` is in the `p=1` class, not the
`p=1/2` class.

## V2 — new at the searched commit?

Yes at `922b9b12a6`. The universality classes are landed as an **observation**
on one family, explicitly "not promoted to a closed formula or a universal
theorem". No landed note supplies the perturbation-theoretic mechanism, the
integer-power exclusion, or the correction.

## V3 — load-bearing?

Yes, on a `critical` row with **773 transitive descendants** and `deps: []`
(a root). Admission (c) is currently selected by empirical match to `F~M = 1`;
this note (i) shows the stated discriminator compares two members of the same
class, (ii) excludes the sublinear class by self-adjointness, and (iii)
collapses admission (c) into the same unforced coupling premise the A2
heuristic already uses — reducing two independent gaps to one.

## V4 — cost

No axiom, no primitive, no dimensionless import, no counting convention.
Rellich/Kato is used as a proof skeleton and re-earned on finite matrices by
the runner, per the exercise skill's literature rule, not imported as
authority.

**The one premise carried:** the additive coupling `H(φ) = H + φ`, which the
source note labels heuristic. The note says so in its first Scope line and
scopes Theorems 3–4 as conditional on it. Theorems 1–2 do not need it.

## V5 — would a reviewer call it thin?

Defences: it targets a named admission on a root critical row rather than a
residual; it produces an unconditional exclusion plus a correction to a landed
support note; the arithmetic is exact rational where it matters (row H is a
27×27 exact resolvent); and three drafting errors caught by the runner are
recorded in the note rather than fixed silently.

**Risks I would flag myself:** (1) the additive coupling is not derived, so the
headline `p=1` is conditional — stated up front; (2) the seam between the
propagator response and the *path action* used by the landed harness is not
closed, and is named as the remaining seam; (3) Theorem 2 is finite-dimensional.

## Verdict

Proceed to cluster-cap evaluation. 8 PASS / 0 FAIL, cold-run at `4a52949d69`,
PIN MATCH `5b70b2f3…`.
