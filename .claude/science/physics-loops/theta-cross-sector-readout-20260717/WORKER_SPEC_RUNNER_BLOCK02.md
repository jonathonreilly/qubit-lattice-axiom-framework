# Worker Spec — Runner For The Post-Erasure Collapse Note (theta block02)

Bounded execution worker. One deliverable, no git, no other files, no audit
status. python3 + sympy only, exact arithmetic, single process. Mirror the
CheckRunner/needle structure of
`scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py`
(read it first; it is on this branch). The note's `__TOTAL__` placeholder is
resolved by the supervisor afterward; do not parse or match it; do not edit
the note. Target roughly 20 gates; no padding.

## Deliverable
`scripts/theta_post_erasure_odd_side_collapse_record_facing_tail_2026_07_18.py`

## Files you may read (exactly these)
1. `docs/THETA_POST_ERASURE_ODD_SIDE_COLLAPSE_RECORD_FACING_TAIL_BOUNDED_THEOREM_NOTE_2026-07-18.md`
2. `docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md`
3. `docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
4. `scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py`

## Gate inventory

### Group M — modulus and bridge
- M1: |z1*z2| = |z1|*|z2| for symbolic z_i = r_i*exp(I*phi_i) (r_i > 0).
- M2: exponential bridge both directions: exp(u)*exp(v) = exp(u+v)
  identically; log(x*y) = log x + log y for positive symbolic x, y
  (use sympy expand_log with force=False under positive assumptions).
- M3: change-of-variables consistency: with F(x) = x**s (s real symbolic,
  x positive), G(u) := log(F(exp(u))) simplifies to s*u identically.

### Group T1 — collapse equivalence (formal both directions)
- T1a (mult => additive): formal elimination with symbols
  gF_xy, gF_x, gF_y for log-values: from F(x*y) = F(x)*F(y) and
  positivity, log F(x*y) = log F(x) + log F(y) — encode as the identity
  log(a*b) = log a + log b at positive symbols a, b, plus the
  substitution chain gate.
- T1b (additive => mult): from G(u+v) = G(u) + G(v),
  F(e^u * e^v) = F(e^{u+v}) = exp(G(u+v)) = exp(G(u))*exp(G(v)) =
  F(e^u)*F(e^v): gate the exp-of-sum identity and the chain on symbolic
  witnesses.
- T1c (Cauchy scaffold): reuse the parent runner's hardened
  nonnegative_between squeeze pattern on G with q1 = 1/2, q2 = 2/3 and a
  symbolic t in between: rational homogeneity formal elimination
  (r-fold: 3*G_part + G_rest = G_total pattern) and the interval
  nonemptiness guard. Conclusion gate: G(u) = s*u membership for the
  power family (M3) labeled as the bounded conclusion.

### Group D — degeneracy lemma
- D1: F(1) = F(1)^2 has exactly the solutions {0, 1} (solve-based).
- D2: zero propagation: formal — with symbols f0 = 0 and fq free,
  f0 * fq = 0; plus the concrete instance F(x0) = 0 => F(x) =
  F(x0)*F(x/x0) = 0 encoded as the product identity at symbolic values.

### Group B — pre-erasure boundary witness
- B1: full character r(z) = exp(I*arg z)*|z|^s at fixed modulus 1:
  values at arg z = 0 and pi/2 are 1 and I, distinct exactly (registers).
- B2: block multiplicativity of the full character at exact witnesses
  (phi1 = pi/6, phi2 = pi/3, moduli 2 and 3, s symbolic):
  r(z1*z2) = r(z1)*r(z2) exactly.
- B3: the logarithmic modulus content log|r(z)| = s*log|z| is identical
  at arg z = 0 and pi/2 (fixed modulus): phase-silent, exactly — while B1
  registers. Gate both facts side by side.

### Group N — needles (normalized whitespace; copy exact strings)
- N1 (parent block note): "an independently supplied quark-side odd-side
  ingredient"
- N2 (erasure note): "the invariant\nmembers of this determinant-character
  family are phase-free functions of `|det|`" — copy the exact wording
  from the file (normalize whitespace).
- N3 (this note): its claim_id; the labels "**(P-hom, post-erasure
  form)**" and "**(P-add, post-erasure form)**"; the phrase
  "one supply in two presentations".

## Iteration protocol
Write incrementally (M+T1, run; D+B; N), never weaken a gate to vacuity,
FLAG loudly if any specified gate is mathematically wrong, report the final
TOTAL line, no cache file.
