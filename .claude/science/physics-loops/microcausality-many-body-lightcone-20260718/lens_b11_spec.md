# Adversarial lens — block11 (graph-metric class + d=3 second-quantization discharge)

You are a hostile referee. Your job is to find errors, over-claims, and
false gates. Do NOT summarize; report only findings, each labeled
BLOCKER / MAJOR / MINOR, with exact quotes and line references. If a
claim survives your attack, say so in one line.

## Files (read all)

- docs/MICROCAUSALITY_GRAPH_METRIC_CLASS_AND_D3_SECOND_QUANTIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-20.md  (the note under review)
- scripts/microcausality_graph_metric_class_and_d3_discharge_2026_07_20.py  (its runner)
- docs/MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md  (block07 — the chain claimed metric-agnostic)
- docs/MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md  (block08 — the Z^3 shell feed consumed at d=3)
- docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md  (block10 — the two open items claimed answered)
- docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md  (the d-dim one-particle surface)
- docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md  (the intertwiner authority)

## Attack surfaces (work each; add your own)

1. METRIC-AGNOSTIC CLAIM. The note asserts every load-bearing block07
   step uses only max-pairwise diameter + triangle inequality + the
   supplied kappa. Read block07's actual proofs and try to find a step
   that secretly uses Z^3 structure (bond geometry, shell counts,
   coordinate axes, unboundedness of the metric, infinite volume).
   Check the note's honesty rows: are the slack ladder and kappa_3D the
   ONLY Z^3-bound items, or are there more?
2. TORUS MATH. Verify independently: (Z/6)^3 l1 spheres at r=1,2,3;
   (Z/8)^3 l_inf spheres; the conversion d1 <= 3 d_inf on the torus;
   coordinatewise quotient-metric domination; the seam-bond diameter.
   Does the quotient metric on (Z/L)^d actually satisfy the triangle
   inequality used by the chain lemma? Is "first deficit exactly at
   r = L/2" right?
3. WRAP DISSOLUTION. The note says block10's open-boundary restriction
   "dissolves in the torus class" because the wrap term has torus
   diameter 1. Is this a sleight of hand? Specifically: block07's
   theorem with the TORUS metric gives decay in TORUS distance — does
   the note anywhere imply decay in AMBIENT distance for the periodic
   system? Is the lightcone-wrap caveat stated strongly enough?
4. THE MANY-BODY d-DIM OBJECT. The dispersion note is explicitly
   one-particle-only. The note builds T_hat^2_d := Gamma(t_d) via the
   intertwiner-pinned functor. Attack: (a) is this a DEFINITION
   masquerading as a theorem? Does the note admit it (steelman (a))?
   (b) mode-set bookkeeping: 2^d taste corners per reduced momentum vs
   "single mode per site" in position space — is the total mode count
   consistent (L^d sites = (L/2)^d reduced momenta x 2^d corners)?
   (c) is the claimed factor tracking (-log T_hat^2 = 2 a_tau dGamma(h_d),
   NO d-dependent factor) actually forced, or could a d-dependent
   normalization hide in the two-step blocking?
5. THE d=3 DISCHARGE. (a) NORM CONSISTENCY: the dispersion note's
   kernel bound is in ||z||_inf; block08's shell chain assumed WHICH
   norm for the kernel and WHICH for the activity weight? Verify the
   3mu in x = e^{-(eta - 3mu)} is exactly the d1<=3d_inf conversion and
   that K = C_3 slots into the same hypothesis shape. (b) Is C_d's
   validity window eta < arcsinh(m) carried everywhere it is used?
   (c) Does the runner's G9 gate block08's actual display or a
   strawman? (d) The note claims "no CT-note dependency at U = 1" —
   check the dispersion note really supplies the bound natively.
6. FIBER/SCALAR CLAIM. "Single mode per site, so scalar-fiber pairs,
   no fiber factor at U = 1." True for staggered fermions? Could the
   2^d taste components reappear as a fiber factor in the position-
   space pair family?
7. RUNNER FORENSICS. For each gate G1-G10: does the checked statement
   match the note's prose claim? Any tautological (self-subtraction)
   gate? Any gate that passes vacuously (empty loop, wrong quantifier)?
   G4's ring enumeration: does it actually test the chain lemma's
   content or something weaker? Needles N1-N7: open each source file
   and verify the quoted strings exist and MEAN what the note uses
   them for (quote-mining check).
8. BOUNDARY HYGIENE. Does the note stay off the Record/Born bridge
   surface? Does it set or predict any audit verdict? Any new
   vocabulary not already in the family? Frontmatter/deps complete?

Output format: numbered findings, severity first, exact quote, then
your argument. End with a one-line overall verdict.
