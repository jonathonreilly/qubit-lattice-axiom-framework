# Worker Spec — Primary Runner For The Scaled-Projector Menu Note (block02)

You are the bounded execution worker. Supervisor plans, reviews, lands. Your
single deliverable is one python3 runner, written incrementally and executed
to a clean PASS total. No git actions. No other file created or edited. No
audit status anywhere.

## Deliverable

`scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py`

python3 + sympy only; exact rational/symbolic arithmetic; no numpy; no
randomness; single process; one-site M_2 objects only. Each check prints
`PASS: <gate-id> <short description>` or `FAIL: ...`; end with exactly
`TOTAL: PASS=<n> FAIL=<m>`, exit 0 iff m == 0. Mirror the structure and
print discipline of `scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py`
(read it first), including its CheckRunner class shape and needle-check
style. NOTE: the source note's Verification section ends with the literal
placeholder `TOTAL: PASS=__TOTAL__ FAIL=0` — that placeholder is resolved by
the supervisor AFTER your run; do NOT write a gate that parses or matches
that number, and do NOT edit the note.

## Files you may read (exactly these)

1. `docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md` (the note this runner certifies)
2. `docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md` (parent block note — quote source)
3. `scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py` (style anchor; reuse the hemisphere_weight, bloch_projector, forced_trace_value patterns)
4. `docs/MINIMAL_AXIOMS_2026-06-29.md` (quote source)

## Conventions

- `P(n) = (I + n1*sx + n2*sy + n3*sz)/2`; directions stored `(n_x,n_y,n_z)`;
  hemisphere rule tests the tuple `(n_z, n_y, n_x)` lexicographically
  (copy the parent runner's implementation exactly, including tie handling).
- Formal weight bookkeeping = sympy symbols for unknown w-values, equations
  = menu normalizations only, conclusions by solve/eliminate. Never assume
  the conclusion.
- "Element of S" checks: an operator is c*P(n) iff Hermitian, PSD, and its
  exact eigenvalue multiset is {c, 0} (rank 1) — recover c = trace, n from
  the traceless part; c*I iff eigenvalues {c, c}.

## Gate inventory

### Group D — domain and parameter recovery
- D1: for symbolic unit n and c in (0,1]: trace(c*P(n)) = c and the
  traceless part recovers c*n/2 coefficients — parameter recovery identity.
- D2: distinctness: c*P(n) (c>0) never equals c'*I (eigenvalue multisets
  {c,0} vs {c',c'} differ for c>0); and c*P(n) = c'*P(n') forces c=c',
  n=n' (via trace and traceless part).

### Group T1 — menu characterization
- T1a: symbolic identity: sum_k c_k P(n_k) + sum_j d_j I = I  iff
  sum_k c_k n_k = 0 (vector) and sum_k c_k/2 + sum_j d_j = 1 (scalar).
  Implement as: expand a generic 3-element + 1-coin family symbolically and
  show the residual matrix vanishes exactly iff both conditions hold.
- T1b witnesses (each verified summing to I exactly): projective
  {P(n),P(-n)} symbolic; coin {c I, (1-c) I}; same-direction split
  {l*P(n), m*P(n), (1-l-m)*P(n), P(-n)} symbolic; coplanar three-element
  menu {(2/3)P(n_k)} with n_1=(1,0,0), n_2=(-1/2, sqrt(3)/2, 0),
  n_3=(-1/2, -sqrt(3)/2, 0).
- T1c axis-cancellation menus: generic positive octant (nx,ny,nz > 0
  symbolic, unit assumption): elements {c0 P(n), c0 nx P(-e_x),
  c0 ny P(-e_y), c0 nz P(-e_z)} with L = nx+ny+nz, c0 = 2/(1+L): verify sum
  = I identically and every coefficient in (0,1]. Rational witnesses: one
  per octant (all eight sign patterns) using n = (±3/7, ±6/7, ±2/7); one
  zero-component witness n = (3/5, 0, -4/5) (element for the zero component
  omitted); axis witness n = e_z (menu degenerates to {P(e_z), P(-e_z)}).
- T1d rejector: a family violating the vector condition (e.g. drop one
  axis element) does NOT sum to I and the menu checker detects it.
- T1e non-membership: diag(1/2, 1/4) is an effect whose eigenvalue multiset
  {1/2, 1/4} matches neither {c,0} nor {c,c} — not in S.

### Group T2 — forcing
- T2a ray additivity: formal elimination from the two split menus'
  normalizations: h(l) + h(m) = h(l+m). Also gate the split-menu validity
  (T1) used here.
- T2b monotone + rational homogeneity + squeeze: mirror the parent runner's
  B-group (including the interval-nonemptiness guard in the squeeze
  helper — copy that hardened pattern) on h with q1=1/2, q2=2/3 and a
  symbolic t in (1/2, 2/3); rejector: non-monotone toy detected.
- T2c complement: formal from {P(n), P(-n)}.
- T2d axis-cancellation affinity: with symbols g_xp, g_xm, g_yp, g_ym,
  g_zp, g_zm for g(±e_a) constrained ONLY by the three complement
  identities, and h-linearity from T2a (encode h(c,direction) = c *
  g_direction), eliminate the axis-menu normalization (positive octant
  symbolic) to derive g(n) = (1 + n·s)/2 with s_a = 2*g_ap - 1. Verify the
  same identity on the eight rational octant witnesses and the
  zero-component witness numerically-exactly (sympy rationals).
- T2e coins: formal elimination f(c) + f(c') = f(c+c') from coin menus;
  conclude f(c) = c on rationals; squeeze scaffolding reference gate (reuse
  T2b helper).
- T2f state + uniqueness: from g(n) = (1+n·s)/2 and 0 <= g <= 1 at
  n = -s/|s| (symbolic with |s| != 0 assumption): (1 - |s|)/2 >= 0 forces
  |s| <= 1; sigma = (I + s·σ)/2 has trace 1 and eigenvalues (1±|s|)/2 >= 0;
  representation identity Tr(sigma * c*P(n)) = c*(1 + n·s)/2 and
  Tr(sigma * c*I) = c symbolically; uniqueness: two Hermitian sigma agreeing
  on {P(e_x), P(e_y), P(e_z), I} traces are equal (4-value determination).

### Group T3 — paired boundary
- T3a paired normalization of the rogue extension: with symbols g_i and
  complement constraints g_i + g_i_c = 1, the paired-menu sum
  sum_i l_i*(g_i + g_i_c) + sum_j d_j reduces to sum_i l_i + sum_j d_j = 1
  under T1's scalar condition (formal elimination; generic 2-pair + 1-coin
  paired menu).
- T3b hemisphere rogue values: reuse the parent runner's hemisphere rule:
  g(e_x) = g(e_z) = 1, g(u) = 0 for u = (1/sqrt(2), 0, -1/sqrt(2));
  three-direction forcing: trace form with value 1 at e_x, e_z and trace 1
  forces 1/2 at u (copy forced_trace_value pattern); affine control stays
  consistent (non-detection gate).
- T3c unpairedness witnesses: the split menu's element multiset (l, m,
  1-l-m on side n; 1 on side -n, for l=1/5, m=1/4) admits no equal-weight
  antipodal pairing (check: no perfect matching of equal weights across
  antipodal directions — implement as an exact multiset comparison for this
  witness); the positive-octant axis menu has four pairwise non-antipodal
  directions (verify a·c != -1 for all pairs exactly at the rational
  octant witness).
- T3d corollary logic gate: paired subfamily admits the non-trace rogue
  (T3a+T3b) => any forcing must use an unpaired menu; label as corollary,
  printing which unpaired schemas T2 used.

### Group N — needle checks (open the files, assert exact substrings; copy
the exact strings from the files you read, normalized-whitespace matching
as in the parent runner)
- N1 (axiom memo): "Only records are readable. A readout value is
  determined by record content alone."
- N2 (parent block note): "classical mixtures of projective menus and other
  intermediate families"
- N3 (parent block note): "Whether the physical registration supplies menus
  at projective grade, at effect grade, at neither, or at some intermediate
  family is underived and is not decided here."
- N4 (this note): its claim_id string; the labels "**(F1)" and "**(F2)";
  the phrase "no literature bridge input"; the phrase "paired" (in the T3
  heading sentence "The paired subfamily does not force").

## Iteration protocol

Write incrementally (D+T1 first, run; then T2; then T3; then N), never
weaken a gate to vacuity, fix mathematics honestly, and FLAG loudly in your
final message if any specified gate is mathematically wrong as stated.
Report the final TOTAL line. Do not write a cache file.
