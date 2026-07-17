# Worker Spec — Primary Runner For The Effect-Menu Born-Form Note (2026-07-17)

You are the bounded execution worker. The supervisor owns planning, review,
and landing. Your single deliverable is one python3 runner file, written
incrementally and executed to a clean PASS total. Do not commit, push, stage,
or touch git. Do not create or edit any other file. Do not apply audit
status anywhere.

## Deliverable

`scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py`

Requirements: python3 + sympy only (exact rational/symbolic arithmetic; no
numpy, no network, no randomness, single process, dimensions 2 and 4 only).
Every check prints one line `PASS: <gate-id> <short description>` or
`FAIL: ...`, and the script ends printing exactly
`TOTAL: PASS=<n> FAIL=<m>` and exits 0 iff m == 0. Mirror the general
structure/print discipline of the existing runner
`scripts/born_form_composite_gleason_bridge_2026_07_04.py` (read it first),
including its needle-check style that opens repo docs and asserts exact
substrings.

## Files you may read (exactly these, nothing else)

1. `docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md` (the source note this runner certifies)
2. `docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`
3. `scripts/born_form_composite_gleason_bridge_2026_07_04.py`
4. `docs/MINIMAL_AXIOMS_2026-06-29.md`
5. `docs/BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`

## Mathematical conventions

- Pauli matrices `sx, sy, sz`; `P(n) = (I + n1*sx + n2*sy + n3*sz)/2` for a
  Bloch direction `n = (n1, n2, n3)` (unit norm where assumed).
- Lexicographic hemisphere rule (must match the 2026-07-04 note's R1
  verbatim semantics): `g(n) = 1` iff the tuple `(n_z, n_y, n_x)` is
  lexicographically positive (first nonzero entry positive), else 0; extended
  by `g(0) = 0`, `g(I) = 1`. Note the tuple order is `(n_z, n_y, n_x)` while
  the direction is stored `(n_x, n_y, n_z)`.
- "Effect" means Hermitian `E` with `0 <= E <= I` (exact eigenvalue checks).
- Weight bookkeeping gates are FORMAL LINEAR ELIMINATION: introduce sympy
  symbols for the unknown weight values (e.g. `w1, w2, w12, wR`), impose only
  the menu-normalization equations of the named menus, and solve/eliminate to
  derive the target identity. Never assume the conclusion.

## Gate inventory (implement all; group headers as comments)

### Group A — partial additivity from menu normalization (formal)
- A1: from menus `{E1, E2, R}` (`R = I - E1 - E2`) and `{E1+E2, R}`:
  eliminate to `w(E1+E2) = w(E1) + w(E2)`.
- A2: from menu `{E, I-E}`: complement law `w(E) + w(I-E) = 1`.
- A3: effect-cone witness: a NONCOMMUTING exact rational pair `E1, E2` on
  `M_2` with `E1 + E2 <= I` (verify: `[E1,E2] != 0`; eigenvalues of `E1`,
  `E2`, `I-E1-E2` all in `[0,1]`, exact). Also one witness at `d=4`.
- A4 (rejector): a pair with `E1' + E2' <= I` FALSE; the menu-validity
  checker must detect the negative eigenvalue of `I - E1' - E2'` (the gate
  PASSES because detection works).

### Group B — homogeneity and monotonicity
- B1: from menu `{E/3, E/3, E/3, I-E}` plus A2: eliminate to
  `w(E/3) = w(E)/3`; generalize check at `r=5`.
- B2: monotonicity as formal consequence: given effects `E <= F`, from
  `w(F) = w(E) + w(F-E)` (A1 with `E1=E, E2=F-E`) and `w >= 0` symbolically
  conclude `w(F) - w(E) = w(F-E) >= 0`.
- B3: squeeze scaffolding on an exact witness: `E = diag(1/2, 1/4)` in the
  computational basis, symbol `t` with assumption `1/2 < t < 2/3`: verify
  `(t - 1/2)*E` and `(2/3 - t)*E` have nonnegative eigenvalues (symbolic,
  under the assumption), i.e. `q1*E <= t*E <= q2*E` for `q1=1/2, q2=2/3`;
  then formal chain: `q1*w(E) <= w(t*E) <= q2*w(E)` via B1/B2 symbols.
- B4 (rejector): explicit non-monotone toy table on a two-effect chain
  violates the B2-derived inequality; the checker detects it.

### Group C — linear extension bases
- C1: `d=2` effect family `{I, (I+sx)/2, (I+sy)/2, (I+sz)/2}`: each is an
  effect; the 4x4 trace-pairing Gram matrix is nonsingular (exact det != 0).
- C2: `d=4` effect family `{I} ∪ {(I + s_a⊗s_b)/2}` over the 15 nonidentity
  Pauli products: each an effect; 16x16 Gram det != 0 exact.
- C3: cancellation well-definedness: for a concrete quadruple of positive
  rational `M_2` matrices with `A + D = C + B`, the cone-additivity symbols
  give `F(A) + F(D) = F(C) + F(B)` by formal elimination (use scaled effect
  values; scale factor `s = 2` suffices for the witness you pick).

### Group D — trace representation and reconstruction
- D1 (`d=2`): with symbolic basis values `w_I=1, w_x, w_y, w_z` on the C1
  family, solve `Tr(sigma * B_k) = w_k` for Hermitian `sigma`; verify it
  equals the landed Bloch display
  `sigma = (1/2)[I + sum_a (2*w(P_a^+) - 1) * s_a]`.
- D2 (`d=2`): for a GENERIC symbolic Hermitian effect
  `E = e0*I + ex*sx + ey*sy + ez*sz`, verify `Tr(sigma*E)` equals the linear
  extension `e0*... ` computed from the basis expansion of `E` (formal
  identity in all symbols).
- D3 (`d=4`): same pipeline with the 16-element basis: solve the 16x16
  linear system with symbolic values, verify `Tr(sigma*E)` reproduces the
  linear extension on a generic symbolic Pauli-product combination.
- D4: uniqueness: `Tr(sigma*B_k) = Tr(sigma'*B_k)` for all basis k forces
  `sigma = sigma'` (Gram nonsingularity route, both dims).

### Group E — state property
- E1: `w(I) = 1` gives `Tr(sigma) = 1` (formal from reconstruction).
- E2: for symbolic `psi = (alpha, beta)` (complex symbols, no normalization
  needed): `<psi|sigma|psi> = Tr(sigma * |psi><psi|)` identically.
- E3: therefore `w(P_psi) >= 0` for all unit `psi` forces `sigma >= 0`;
  gate the 2x2 principal-minor logic: symbolic Hermitian with
  `<psi|sigma|psi> >= 0` for the four vectors `(1,0),(0,1),(1,1),(1,i)`
  giving diagonal nonnegativity plus the real/imag off-diagonal bounds; plus
  determinant condition from generic psi: implement as: solve that
  `<psi|sigma|psi>` as quadratic form has nonneg values iff eigenvalues
  nonneg (2x2 exact eigenvalue check on a witness family). Keep this gate
  honest: it certifies the STATED implication on the witness family and the
  exact eigenvalue criterion, labeled as such.

### Group T2 — rogue non-extension at one site
- T2a: hemisphere values: `g(e_x) = 1`, `g(e_z) = 1`, `g(u) = 0` for
  `u = (1/sqrt(2), 0, -1/sqrt(2))` (tuple order care: `(n_z,n_y,n_x)`).
- T2b: trace-form forcing: symbolic Hermitian `sigma` with
  `Tr(sigma*P(e_x)) = 1`, `Tr(sigma*P(e_z)) = 1`, `Tr(sigma) = 1` forces
  `Tr(sigma*P(u)) = 1/2` exactly (solve; unique value). Hence conflict with
  `g(u) = 0`.
- T2c (control): the affine assignment `h(n) = (1 + n·s)/2` with `s=(0,0,1)`
  does NOT trigger the contradiction (its forced value test is consistent);
  the contradiction detector must stay silent on it.
- T2d: complement law of the hemisphere rule on exact witnesses including
  tie directions: pairs `±(3/5, 0, 4/5)`, `±(0, 1, 0)`, `±(1, 0, 0)`,
  `±(0, 0, 1)`: `g(n) + g(-n) = 1` each.

### Group T3 — product-menu boundary on the bonded pair
- T3a: `Tr(P(a)P(c)) = (1 + a·c)/2` identically (symbolic units); and for
  unit vectors `a·c = -1` iff `c = -a` (Cauchy-Schwarz equality gate: solve
  `a·c = -1` together with unit norms on symbolic reals — verify the
  solution set forces `c = -a`; a clean route: `|a + c|^2 = 2 + 2*a·c = 0`).
- T3b: product orthogonality:
  `Tr((P(a)⊗P(b))(P(c)⊗P(d))) = (1+a·c)(1+b·d)/4` identically.
- T3c: three-antipodal impossibility: `b1·b2 = b1·b3 = b2·b3 = -1` with unit
  norms is contradictory (`b2 = -b1` and `b3 = -b1` force `b2·b3 = +1`).
- T3d: product-projector ranks on the pair are in `{0,1,2,4}`; rank-3 is
  impossible (enumerate rank(A)*rank(B) for ranks in {0,1,2}).
- T3e: below-forcing: `Tr(P(-a)P(c)) = 1` iff `c = -a` (route:
  `(1 + a·c)/2` with sign — compute `Tr(P(-a)P(c)) = (1 - a·c)/2 = 1` iff
  `a·c = -1` iff `c = -a`); conclude a rank-1 product below `P(-a)⊗I`
  carries first slot `-a`.
- T3f: mixed rank-2 sum is not the identity: `P(a)⊗I + I⊗P(b) != I` — gate
  via the vector `|a_perp>⊗|b_perp>`: use `a=(0,0,1), b=(1,0,0)` exact and
  show the operator annihilates `|1> ⊗ |->` while `I` does not; also generic
  trace-of-square mismatch as a second check.
- T3g: tree-menu normalization is formal-symbolic: with symbols
  `g1a, g2b, g2c, g1d, g2bp` etc. constrained ONLY by complement identities
  `g(n) + g(-n) = 1`, verify sum = 1 identically for: the site-1-rooted
  4-menu `{(a,b),(a,-b),(-a,c),(-a,-c)}` with product weights
  `W = g1(·)*g2(·)`; the site-2-rooted 4-menu `{(a,b),(-a,b),(d,-b),(-d,-b)}`;
  the (2,1,1) menus `{P(a)⊗I, P(-a)⊗P(d), P(-a)⊗P(-d)}` and its site-swap;
  the (2,2) menus; and the trivial `{I}`.
- T3h: non-Born restriction: pair-state affinity — for symbolic Hermitian
  `rho` on `M_4`: `Tr(rho*(P(n)⊗I)) = (Tr(rho) + m·n)/2` with
  `m_i = Tr(rho*(s_i⊗I))`, identically; then the T2b forcing applied to the
  restriction values (1 at `e_x`, 1 at `e_z`, trace 1) forces `1/2` at `u`,
  conflicting with `W(P(u)⊗I) = g1(u) = 0`.
- T3i: Bell projector is not a product: reshape `|Phi+><Phi+|`'s vector to a
  2x2 matrix and verify rank 2 (exact), so entangled projections are outside
  every product menu; print as the consistency gate with the landed H4-strength
  route.

### Group T5 — finite-group zero-information limit
- T5a: symbolic Hermitian `sigma` invariant under conjugation by each of
  `sx, sy, sz` forces `sigma = c*I` (solve exact).
- T5b: with `Tr(sigma) = 1`: `sigma = I/2`; embedded binary menu weights are
  `1/2` each.

### Group N — needle checks (exact substring assertions, open the files)
- N1 (axiom memo): "Only records are readable. A readout value is determined
  by record content alone."
- N2 (axiom memo): "These axioms state only their named primitive content."
- N3 (2026-07-04 note): "Gleason's theorem is imported as named classical
  mathematics."
- N4 (2026-07-04 note): "Three directions plus normalization refute every
  `2x2` trace form at once"
- N5 (2026-07-04 note): "Without this full projection-measure strength a
  partial menu assignment is not a frame function and Gleason does not apply"
- N6 (2026-07-04 note): "adjacency alone pays for nothing here without H4's
  strength"
- N7 (bridge note 2026-06-05): the substring "(2 m(P_a^+) − 1)" (unicode
  minus as in the file; read the file and copy the exact codepoints).
- N8 (this note): its own claim_id string, the hypothesis labels "**(E1)"
  and "**(E2)", and the phrase "no literature bridge input".

Where a needle string in this spec might differ from the file by
whitespace/unicode, ALWAYS copy the exact string from the file you read, and
keep the assertion meaningful (a full distinctive clause, not one word).

## Iteration protocol

1. Write the file incrementally: setup + Group A first, run it, then extend
   group by group, running after each group.
2. If any gate FAILs, fix the gate's mathematics or implementation — never
   weaken a gate to vacuity, never assert a conclusion as its own check.
3. Finish with all gates passing; report the final `TOTAL:` line and the gate
   count in your final message. Do not write a cache/log file; the supervisor
   regenerates it.
4. If a specified gate is mathematically WRONG as stated, do not fudge it:
   implement the correct exact statement, and FLAG the discrepancy loudly in
   your final message for supervisor review.
