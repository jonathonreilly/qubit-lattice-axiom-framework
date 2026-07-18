# Worker Spec — Runner For The Theta Forcing-Property Characterization Note

Bounded execution worker. One deliverable, no git, no other files, no audit
status. python3 + sympy only, exact arithmetic, single process. Mirror the
CheckRunner/print/needle style of
`scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py`
(read it first). The note's Verification total is the literal `__TOTAL__`
placeholder — resolved by the supervisor after your run; do not parse or
match it; do not edit the note. Target roughly 26 gates; no padding.

## Deliverable
`scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py`

## Files you may read (exactly these)
1. `docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md`
2. `docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`
3. `docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
4. `docs/REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`
5. `scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py`

## Gate inventory

### Group C — conjugation and phase functional
- C1: for symbolic nonzero z = r*exp(I*phi) (r positive, phi real):
  arg(conj(z)) = -arg(z) on the principal branch at exact witnesses
  (phi in {0, pi/4, pi/2, 3*pi/4}); symbolic identity conj(r*exp(I*phi)) =
  r*exp(-I*phi).
- C2: odd-and-even elimination: solve [f = -f] -> f = 0 (formal); and a
  function-level version: h(phi) := c1*sin(phi) (generic odd form on the
  witness family) with evenness constraint h(phi) - h(-phi) = 0 forces
  c1*sin(phi) = 0 at generic phi => c1 = 0 (solve-based).

### Group P — the two odd-side consequences (formal eliminations)
- P1 (additivity => odd): with symbols h1, h2, hsum for per-sector phase
  functionals and the disjoint-record additivity equation
  hsum = h1 + h2 together with the conjugation-pair normalization
  h(phi) + h(-phi) = 0 DERIVED as: the two-sector value at (phi, -phi)
  composes to the trivial sector, whose phase content is zero:
  formal elimination h(phi) + h(-phi) = h_trivial = 0. Encode exactly as
  the note states (oddness as the named consequence; do not overreach).
- P2 (homomorphism => odd): the exponent-additivity of characters:
  arg(z1*z2) = arg z1 + arg z2 mod 2pi at exact witnesses inside the
  principal range; k*(phi1 + phi2) = k*phi1 + k*phi2 identically; and
  det block law det(diag(A,B)) = det(A)*det(B) for symbolic 2x2 A, B.

### Group W — the two witnesses
- W1a: r(z) = exp(I*k*arg z), integer k != 0 symbol: phase functional
  k*phi is odd identically; multiplicative composition at exact witnesses
  (phi1 = pi/6, phi2 = pi/3: exp(I*k*(phi1+phi2)) = product).
- W1b: W1 breaks orbit constancy: exp(I*k*phi) != exp(-I*k*phi) at
  phi = pi/(2k)... use exact k-free witness: at phi = pi/2 the values
  exp(I*k*pi/2) and exp(-I*k*pi/2) differ unless sin(k*pi/2) = 0; gate
  with concrete k = 1 (values I vs -I, distinct exactly).
- W1c: W1 registers the phase: values at phi = 0 and phi = pi/2 differ
  (k = 1 witness: 1 vs I).
- W2a: cos(phi) is even identically; not odd (cos(0) = 1 != -1 = -cos(0)).
- W2b: cos breaks the homomorphism: cos(pi) = -1 != 0 =
  cos(pi/2)*cos(pi/2) exactly.
- W2c: cos breaks additivity-oddness: cos(-phi) + cos(phi) = 2*cos(phi)
  != 0 at phi = 0 exactly.
- W2d: cos registers: cos(0) = 1 != -1 = cos(pi).
- W3 (control): the k = 0 character r(z) = |z|^s (s symbolic) is
  orbit-constant, has zero phase functional, and does not register (values
  at phi = 0 and pi/2 equal at fixed |z|) — the detector stays silent.

### Group T — characterization assembly
- T1: forward cell (P-add + P-orb): odd + even => zero (C2 route),
  labeled as the landed mechanism re-derivation.
- T2: forward cell (P-hom + P-orb): within the character family
  exp(I*k*phi), evenness constraint exp(I*k*phi) = exp(-I*k*phi) for all
  phi forces sin(k*phi) = 0 generically => k = 0 (solve at generic
  symbolic phi with k integer symbol; mirror the landed lemma).
- T3: necessity assembly (corollary logic gate): W1 gates witness that
  both odd-side properties without orbit constancy register; W2 gates
  witness that orbit constancy without either odd-side property registers;
  print the conjunction as the characterization corollary.

### Group N — needles (normalized whitespace; copy exact strings from files)
- N1 (obligation): "Derive from the retained framework chain whether the
  charged-lepton `K`/CPT occupancy carrier is the same physical channel"
- N2 (obligation): "similarity, shared notation, and historical decision
  text are insufficient"
- N3 (phase-erasure note): "K/CPT orbit invariance alone gives evenness,
  not phase erasure"
- N4 (registrable note): "homomorphism forces odd; even forces zero"
- N5 (this note): its claim_id; the labels "**(P-add)**", "**(P-hom)**",
  "**(P-orb)**"; the phrase "one transported property".

## Iteration protocol
Write incrementally (C+P, run; W; T+N), never weaken a gate to vacuity,
FLAG loudly if any specified gate is mathematically wrong, report the final
TOTAL line, no cache file.
