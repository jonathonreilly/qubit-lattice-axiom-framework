# Worker A spec — source scout (d-dim action-level transfer identity)

You are a bounded extraction worker. Read EXACTLY these files (no
others):

1. docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md
2. docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md
3. docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md
4. docs/MICROCAUSALITY_GRAPH_METRIC_CLASS_AND_D3_SECOND_QUANTIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-20.md  (if absent on this branch, note that and skip)
5. scripts/free_staggered_two_step_dispersion_d_dimensional_2026_06_12.py  (or the dispersion note's actual runner path from its header — read the header first)

Write your report to
.claude/science/physics-loops/rp-ddim-action-transfer-20260720/worker_a_scout_report.md

Your final message: one line, "report written, N sections".

## Extraction tasks (quote VERBATIM, with context)

(a) The dispersion note's d-dimensional ACTION and staggered-phase
convention: the exact phase definitions (temporal and each spatial
axis; which coordinates each phase depends on), the lattice/period
assumptions (even periods sentence), and the mass window.
(b) The fold/corner algebra: how the note reduces to reduced
momentum k and taste corners (quote the definitions: reduced domain,
p_r = k + pi r, what operator shifts corners, the per-k block
structure and its DIMENSION). State exactly what finite matrix the
note derives per k (call it the per-k two-step block) and what its
eigenvalues are shown to be, with the note's own displays.
(c) The note's positivity/decaying-channel statements: what it says
about e^{-2E_d} in (0,1], any forward/backward channel language, any
projector construction, and its ONE-PARTICLE-ONLY boundary sentences
(quote all of them).
(d) The RP note's Steps 3b and 4 displays verbatim: the projector
formulas, the finite-norm forward-selection argument sentence, the
one-mode coherent-state kernel sentence, the induced exterior
operator sentence, the defining intertwiner display, the assembly
display, the B^dag B display, and its 1+1d-only scope sentences.
(e) The landed corner-note's finite-mode theorem items 1-5 verbatim
(functoriality, canonical intertwiner, positive logarithm, trace
identity, direct sums) and its "Open problems" sentences about fixed
gauge backgrounds and locality.
(f) From block11's note (file 4): the construction-status sentences
and the scalar-ambiguity caveat (the sentences this block would
discharge).
(g) The dispersion note's runner: how it BUILDS the per-k block from
the action (function names, the matrix construction, what it checks)
— summarize the construction pipeline in 10-20 lines with exact
formula quotes, so a fresh runner can rebuild the same object
natively.
(h) GAP LIST: exactly what a d-dim many-body action-level derivation
needs that is NOT in any of these sources (be adversarial — e.g.,
does the dispersion note derive the per-k block as a TRANSFER
recursion in time, or only as a dispersion relation? Is there a
forward-channel selection at general d anywhere? Is there any
many-body object at general d anywhere?).
(i) LIMITS: anything in these files that would BLOCK or rescope the
plan (convention mismatches between the three sources — e.g., phase
conventions, a_tau, mode normalization, momentum domains; anything
the plan's ground-truth item 3 gets wrong).

Rules: verbatim quotes with enough surrounding text to relocate
them; no synthesis beyond the gap/limit lists; no file writes other
than your report; do not run code.
