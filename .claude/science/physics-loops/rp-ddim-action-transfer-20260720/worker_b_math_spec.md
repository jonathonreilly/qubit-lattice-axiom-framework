# Worker B spec — mathematics (d-dim action-level transfer identity)

> **SUPERSEDED 2026-07-24 (review-loop round 2, PR #5549).** Preserved
> unedited as provenance. This prompt instructed the worker to treat
> the coherent kernel as DERIVING the overall normalization; that
> instruction was wrong and its conclusion was RETRACTED before
> landing. `C = 1` is fixed by the SUPPLIED normalized kernel form,
> not derived from the action, and supplying that form IS the
> coherent-state form of the operator identification. See
> `REVIEW_HISTORY.md` "Round 2".

You are a bounded mathematics worker. Derive, with full displayed
algebra, the d-dimensional free-staggered many-body two-step
transfer identity, following the numbered items below. You may read
EXACTLY these files for conventions (no others):

1. docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md
2. docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md
3. docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md

Write your report to
.claude/science/physics-loops/rp-ddim-action-transfer-20260720/worker_b_math_report.md
Your final message: one line, "report written, N items".

Use the dispersion note's OWN conventions throughout (quote each one
you rely on). Free `U = 1`, one Grassmann component per site, even
spatial periods, `m > 0`, `a_tau = 1` unless the sources say
otherwise (flag whatever they say).

## Items

1. **Per-k classical structure from the action.** Starting from the
   d-dim staggered mode equation (the dispersion note's own), derive
   the per-reduced-momentum two-step classical block. State its
   dimension, why the taste corners couple, and show the two-step
   block is a function of the corner matrix S(k) whose square is
   diagonal with entries `Σ_μ sin² p_μ` (or correct this if the
   note's algebra differs — DO NOT force it). Conclude the per-mode
   2x2 recursion identical to d = 1 with `sin² p -> Σ_μ sin² p_μ`,
   eigenvalues `e^{±2E_d}`, taste-degenerate. Show every step.
2. **Forward-channel selection at general d.** Generalize the RP
   note's Step 3b verbatim-in-structure: explicit spectral
   projectors per mode, the finite-norm/finite-action argument
   killing the growing channel, and the conclusion that the forward
   one-particle two-step kernel is `t1(2)_d = diag over modes of
   e^{-2 E_d}`. Identify exactly which sentence of the argument is
   dimension-blind and which needs the d-dim mode decomposition.
3. **Per-mode coherent-state -> exterior bridge with C = 1.** For a
   single fermionic mode with kernel `<z̄'|T|z> = exp(z̄' λ z)`,
   derive the induced operator on the 2-dim exterior algebra:
   exactly `diag(1, λ)`. Make the vacuum matrix element = 1 explicit
   (the constant Grassmann term), and state why this DERIVES the
   overall normalization (no scalar ambiguity) once the many-body
   kernel factorizes over modes. Then state the factorization of the
   quadratic blocked action's coherent kernel over the S(k)
   eigenmodes (why cross terms vanish: diagonal quadratic form).
4. **Assembly.** Using the landed corner-note's finite-mode theorem
   (quote items used: canonical intertwiner, positive log, trace,
   direct sums), assemble: `T̂²_d = Γ(t1(2)_d) = ⊗_modes diag(1,
   e^{-2E_d}) = B†B`, `Ĥ_d = −log(T̂²_d)/(2 a_tau) = dΓ(E_d) ≥ 0`,
   `Tr T̂²_d = det(1 + t1(2)_d) = Π_modes (1 + e^{-2E_d})`, and the
   mode count `(L/2)^d · 2^d = L^d`. Display the defining
   intertwiner at general d.
5. **Exact-gate designs (sympy, no floats as inputs).** Design gates
   a fresh runner can implement:
   - classical rebuild: d = 2 and d = 3 at L = 2 per direction
     (plus one d = 2, L = 4 one-particle spot), phases from the
     action, two-step block eigenvalues vs `e^{±2E_d}` SYMBOLIC;
   - projector identities per mode (symbolic);
   - one-mode bridge (symbolic Grassmann/2x2);
   - full Fock at d = 2, L = 2 (16-dim): Γ built from occupation
     action, intertwiner vs each a†_j (dense exact), −log/(2a_tau)
     = dΓ(E) exact, trace = det exact, B†B exact;
   - d = 3, L = 2 (256-dim): STRUCTURED gates only — diagonal
     occupation products, intertwiner via action on basis VECTORS,
     no dense 256x256 matrix products; say exactly how;
   - discrimination probes (what mutation would each gate catch).
6. **LIMITS.** Every assumption, convention fork, or step where the
   sources under-determine the object; anything that would make the
   d-dim identity WEAKER than the d = 1 landed one (e.g. if the
   dispersion note's per-k block is not literally a time-recursion
   monodromy, say so and give the honest bridge).

Rules: complete displayed algebra (no "similarly"); flag every
uncertainty; no file writes other than your report; do not run code;
your report must be self-contained for a supervisor who has the
sources open.
