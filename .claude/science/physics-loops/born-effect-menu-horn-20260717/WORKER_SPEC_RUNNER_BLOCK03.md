# Worker Spec — Primary Runner For The Outcome-Threshold / Mixed-Projective Note (block03)

Bounded execution worker. Single deliverable, no git, no other files, no
audit status. python3 + sympy only, exact arithmetic, no numpy, single
process, one-site M_2 objects. Mirror the CheckRunner/print/needle style of
`scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py`
(read it first; REUSE its bloch_projector, is_effect-style helpers, and the
hardened nonnegative_between pattern where needed). The note's Verification
total is the literal placeholder `__TOTAL__` — resolved by the supervisor
after your run; do not parse or match it; do not edit the note. Target
roughly 40 gates; prefer fewer, stronger gates over padding.

## Deliverable
`scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py`

## Files you may read (exactly these)
1. `docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md`
2. `docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`
3. `docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`
4. `scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py`
5. `docs/MINIMAL_AXIOMS_2026-06-29.md`

## Gate inventory

### Group F — the witness function f(t) = t^3/(t^3+(1-t)^3)
- F1: complement f(t)+f(1-t)=1 identically; f(0)=0; f(1)=1.
- F2: denominator identity t^3+(1-t)^3 = 3(t-1/2)^2 + 1/4 (so >= 1/4).
- F3: exact values f(1/4)=1/28, f(1/2)=1/2, f(5/8)=125/152, f(3/4)=27/28.

### Group T1 — binary boundary
- T1a: with sigma0 = (I + (1/2)sz)/2: Tr(sigma0*P(n)) = (2+nz)/4
  identically (symbolic direction).
- T1b: binary normalization of w0 = f(Tr(sigma0*E)) as the f-complement
  composed with the trace complement: for symbolic Hermitian effect E,
  Tr(sigma0*(I-E)) = 1 - Tr(sigma0*E); combined with F1 conclude
  w0(E)+w0(I-E)=1 (formal composition gate).
- T1c: three-point non-affinity: affine-in-nz prediction at nz=1/2 from
  values at nz=0,1 equals 41/56; actual 125/152; exact inequality
  (cross-multiplication gate).
- T1d: exact ternary violation: elements (1/4)I, (1/4)I, (1/2)I sum to I;
  w0-sum = 1/28+1/28+1/2 = 4/7 != 1.
- T1e (rejector/control): the affine control w(E) = Tr(sigma0*E) passes
  binary normalization AND the ternary menu (sum = 1 exactly) — the
  detector must not flag it.

### Group T2 — ternary threshold
- T2a: step-(A) elimination re-gate: from symbols and the two menus
  {E1,E2,R} (ternary) and {E1+E2,R} (binary), eliminate to additivity
  (formal, as in the parent runners); flag in the gate description that
  the ternary menu is the only new input.
- T2b: effect-cone witness for the elimination (noncommuting rational
  pair E1, E2 with E1+E2 <= I; reuse the parent pattern).

### Group T3 — mixed-projective forcing
- T3a: split-menu presentation check: {l*P(n), m*P(n), (1-l-m)*P(n),
  P(-n)} sums to I under l+m+r=1 (symbolic); note this is one component
  with split + outcome.
- T3b: merge-lemma elimination: symbols wA, g1, g2, a1, a2 with the menu
  normalization wA + a1*(1-g1) + a2*(1-g2) + (1-a1-a2) = 1 eliminating to
  wA = a1*g1 + a2*g2 (formal; also the 3-direction version).
- T3c: decomposition invariance instance: the halved axis identity —
  (c0/2)*[axis-cancellation sum] = I/2 = (1/2)P(m) + (1/2)P(-m):
  verify both operator identities symbolically (positive octant + one
  rational witness; reuse/adapt the parent runner's axis_cancellation_menu
  with explicit sign branches), and coefficient masses are each exactly 1.
- T3d: affinity elimination through the merge lemma: from
  (c0/2)g(n) + sum (c0|na|/2) g(-sign e_a) = 1/2 (merge lemma applied to
  both decompositions, complement substitutions), eliminate to
  g(n) = (1 + n.s)/2 with s_a = 2g(e_a)-1 (positive octant symbolic; one
  rational witness in another octant).
- T3e: representation on merged elements: with sigma = (I + s.sigma)/2
  (symbolic s), Tr(sigma * (a1*P(n1)+a2*P(n2))) = a1*(1+n1.s)/2 +
  a2*(1+n2.s)/2 identically — merged values are the matching sums.

### Group T4 — incomparability
- T4a: merged element M = (1/2)P(e_z) + (1/2)P(e_x): exact eigenvalues
  (2+sqrt(2))/4 and (2-sqrt(2))/4, both nonzero, distinct; and the
  scaled-projector membership test (eigenvalue multiset {c,0} or {c,c})
  fails — reuse the parent runner's scaled_projector_parameters logic
  (reimplement locally; do not import).
- T4b: coplanar menu {(2/3)P(n_k)} with n1=(1,0,0),
  n2=(-1/2,sqrt(3)/2,0), n3=(-1/2,-sqrt(3)/2,0): sums to I; pairwise dot
  products all equal -1/2 exactly (not -1) — the parallelism obstruction
  gates.
- T4c: rank-1 piece condition: for a rank-1 projector element Q and a
  piece p*P(m) with p>0, Q >= p*P(m) (i.e. Q - p*P(m) PSD) forces m
  parallel to Q's direction: gate via exact eigenvalue check that
  P(n) - p*P(m) has a negative eigenvalue whenever m != n at an exact
  witness family (e.g. n=e_z, m=(sin a, 0, cos a) with rational
  cos a = 3/5, p = 1/2), plus the identity-piece case: P(n) - p*I has a
  negative eigenvalue for p>0 (exact).
- T4d: coin-into-rank-1 exclusion at the exact coplanar menu: (2/3)P(n1)
  - p*I has a negative eigenvalue for p = 1/10 (exact witness).

### Group T5 — scaled binary characterization
- T5a: eigenvalues of I - c*P(n) are {1-c, 1} (symbolic c in (0,1));
  match against {c',0} forces c=1; match against {c',c'} impossible for
  c in (0,1) (solve-based gates).
- T5b: coin complements stay scaled: I - c*I = (1-c)*I (trivial identity
  gate with the membership test).

### Group N — needles (normalized-whitespace substring, copy exact
strings from the files)
- N1 (axiom memo): "Only records are readable. A readout value is
  determined by record content alone."
- N2 (block01 parent): "(E2) finite effect menus are eligible."
- N3 (block02 parent): "The paired subfamily does not force"
- N4 (this note): its claim_id; the labels "**(G1)", "**(G2)", "**(X1)";
  the phrase "threshold for the effect-grade forcing is exactly three".

## Iteration protocol
Write incrementally (F+T1, run; T2+T3; T4+T5; N), never weaken a gate to
vacuity, FLAG loudly if any specified gate is mathematically wrong, report
the final TOTAL line, no cache file.
