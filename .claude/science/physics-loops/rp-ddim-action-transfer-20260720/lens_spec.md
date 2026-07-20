# Adversarial lens — d-dim action-level many-body transfer identity

You are a hostile referee. Find errors, over-claims, and false gates.
Report only findings, labeled BLOCKER / MAJOR / MINOR, with exact
quotes and line references. If a claim survives your attack, say so
in one line.

## Files (read all)

- docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md  (the note under review)
- scripts/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.py  (its runner)
- docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md  (the d-dim one-particle surface consumed)
- docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md  (the 1+1d template)
- docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md  (the finite-mode functor authority)

## Attack surfaces (work each; add your own)

1. THE PER-K ALGEBRA. Verify independently: T_2(k) as a function of
   S(k); the scalar square S(k)^2 = (sum sin^2)I from the fold rule;
   the 2x2 collapse on S-eigenlines; det = 1, tr = 2+4R; the
   eigenvalue displays e^{+-2E_d}; multiplicity 2^d each (does the
   minimal-polynomial + trace argument actually pin multiplicities?
   check the arithmetic n_- = (tr - 2^{d+1} mu_+)/(mu_- - mu_+)).
   Is the Hermiticity claim for S(k) right (Gamma_mu real symmetric)?
2. FORWARD SELECTION. Is the claimed dimension-blind/d-dependent
   split honest? Does the note quietly strengthen the RP note's
   finite-norm argument, or weaken it? Is the strict split
   lambda_- < 1 < lambda_+ correctly rederived (the dispersion note
   states no interval)? What happens at sum sin^2 = 0 (p = 0): is
   the note's handling of the minimum E_d = arcsinh(m) right?
3. THE C = 1 CLAIM. The note says C = 1 is DERIVED because the
   coherent kernel's constant term is 1. Attack: is the kernel form
   exp(zbar' lambda z) itself derived from the action at general d,
   or inherited from the 1+1d note's bridge? Does the note claim
   more than "parity with the landed d = 1 status"? Is the
   factorization-over-modes step (no cross terms) justified?
4. THE ASSEMBLY. Are CORNER items (ii)-(v) applied within their
   stated hypotheses (strict positivity for the log; finite
   dimension)? Is the mode count (L/2)^d 2^d = L^d consistent with
   one Grassmann component per site? Is the taste-corner vs
   generation-channel distinction kept clean everywhere ("corner"
   overloading)?
5. RUNNER FORENSICS. For each gate G1-G9: does the checked statement
   match the note's prose? Any tautological or vacuous conjunct
   (note: G8's sign check shares the sign variable between sides —
   the runner label says the sign discrimination lives in G7; is
   that honest and sufficient?)? Is G2's "H_hop = 0 at L = 2" the
   right statement (tau_+ = tau_- at L = 2), and does the gate still
   test anything nontrivial? Does G3's charpoly expectation
   {0 x4, -1 x8, -2 x4} actually match the momentum count at
   d = 2, L = 4? Needles N1-N5: verify the quoted strings exist and
   MEAN what the note uses them for.
6. SCOPE HYGIENE. Free U = 1 only; no locality claims; no gauge;
   a_tau conventional; no species interpretation; no audit verdicts;
   frontmatter deps complete and correctly slugged; any new
   vocabulary not already in the cited notes?

Output: numbered findings, severity first, exact quote, then your
argument. End with a one-line overall verdict.
