# C4e — Review

**Reviewer:** a Claude subagent, same model as the author. This is not an independent model. It is a
separate context that implemented the construction blind before reading the author's code or proof.
**Date:** 2026-10-19. **Scope:** NOTE.md claims 1–7, Lemma I, and the range-2 3-magnon certificate
(`c4e_02`). **Not reviewed:** the 1D SAT probe (`c4e_01`) and the novelty paragraph.
**Writes:** only this file and `review_scripts/`. The author's scripts and logs are untouched; the
c4e_02 source was executed in memory with patches only to dump its candidates and matching.

## Verdict summary

| # | claim | verdict | severity of issue |
|---|---|---|---|
| 1 | U = L2∘L1 is a TI, one-qubit, U(1) reversible CA; each L_i an involution on every configuration (Lemma I) | **correct** | — |
| 1' | glider {0,e1+e2} → {e3,(1,1,1)}; face pair ρ moves by v = ρ_bρ_c e_a; all other pairs static | **correct** | — |
| 2 | range: CA radius ≤ 6 (layers 3), empirical ≥ 4; α(A_x) ⊂ A_{B_18(x)} | **correct**; the title's "range ≤ 6" needs a fix | minor (wording) |
| 3 | range-2 monomial 3-magnon extension exists (478/478) | **correct with fix**: the reduction misses α(X_x)-locality, and the "⇔" is false as stated; after the condition is added, an extension still exists | moderate |
| 4 | pair band E = K·v, |v_g| = 1, six dispersive bands, 56 flat near pairs | **correct** | — |
| 5 | single magnons frozen (U and U^{-1}) | **correct** | — |
| 6 | T-covariant (phases included); not O-covariant (axis); not full-action covariant; U C = C U | **correct** | — |
| 7 | 478 connected triples: 403 static / 6 periodic / 69 split / 0 rigid; pair+single 48 transparent / 16 reflected; head-on pairs pass with shift 0–2 | **correct** (all numbers reproduced) | — |
| — | 1D SAT probe; novelty | **unverified** (out of scope; labelled intuition by the author) | — |

**Bottom line.** The constructive result holds. The reviewer's blind implementation reproduces it
exactly. It is an explicit one-qubit-per-site, Z^3-translation-invariant, Q_n-conserving reversible
QCA on Z^3. It is covariant under T, the axis-action vacuum stabiliser, with phases included, and it is
not O-covariant. Its single magnons are frozen, and it has a speed-1 face-diagonal bound-pair
glider. Two statements need fixing:
- (a) "range ≤ 6" is the CA radius. The QCA (automorphism) range is only known to lie in [5, 18].
- (b) The range-2 3-magnon "⇔ matching" reduction omits a necessary condition. The conclusion
  survives once that condition is added (details below).

## Phase A — blind independent implementation (done before reading the proof or the author's code)

The implementation was built from NOTE.md's definitions only (units, the crossing rule (a)/(b)/(c),
N1/N2 within one unit family) and the C4b/C4d definition of the axis action. There are two
implementations by the reviewer:
- `rv_core.py`: sparse, on Z^3. N1/N2 come from offset tables.
- `rv_dense.py`: numpy, on the torus. N1/N2 come from brute-force site sharing.

They agree on 2100 random clusters, k = 2..20, for all four maps L1, L2, U and U^{-1}
(`phaseA_sparse_dense`). Neighbourhood sizes: squares |N1| = 32, |N2∖N1| = 178; tetra-axes
|N1| = 38, |N2∖N1| = 126.

| check | result | log |
|---|---|---|
| (i) L1² = L2² = id and U^{-1}U = UU^{-1} = id, exhaustively for k = 0..4 in a 3³ box (1+27+351+2925+17550 configurations) | PASS | `phaseA_inv` |
| (i) random k = 4 (4³ box, 20000), k = 6 and k = 8 (5³ box, 5000 each); dense tori L = 8, 10, 12 at p = 0.05–0.8 | PASS | `phaseA_inv` |
| (i) stress where Lemma I bears load: all two-face-pair configurations at offsets [−7,7]³ (121362), 60000 two-pairs+magnon, 400 packed-pair configurations with U^{−8}U^{8} = id (30140 crossings) | PASS | `stress` |
| (ii) exact per-layer dependency radius from the definition: 3 and 3 (L = 10, 12); empirical single-flip influence: L1 3, L2 3, U **4**, U^{-1} 3 (bound 6) | PASS | `phaseA_local` |
| (iii) N conserved; TI; U(¬c) = ¬U(c) | PASS | `phaseA_u1` |
| (iv) U, U^{-1} commute with all 12 R ∈ T on random tori (L = 8, 10) and on 3000 k ≤ 4 clusters × 12 R; for all 12 odd R, U P_R ≠ P_R U on {0,e1+e2}; P_R C is not a symmetry either | PASS | `phaseA_sym` |
| (v) single magnons fixed by U and U^{-1} at all sites (L = 8); single holes fixed | PASS | `phaseA_single` |
| (vi) all 9841 pairs with |ρ|∞ ≤ 13: exactly the 6 face orientations move, with v = ρ_bρ_c e_a; 9835 static; 62 near pairs = 6 + 56; 50 ticks gives displacement 50e3; intermediate L1 image {e1,e2} | PASS | `phaseA_pair` |
| (vii) connected triples (Chebyshev-2 graph) modulo Z^3 ⋊ T: **478** orbits; dynamics 403 static / 6 periodic (all period 2) / 69 split / 0 rigid | PASS | `phaseA_triple` |
| (vii) pair + single at (a,b,3), a,b ∈ [−3,4]: 48 transparent, 16 reflected (single unmoved, outgoing (1,−1,0) pair moving −e3); head-on pairs: 50/50 pass through, shifts ≤ 2 | PASS | `collide` |

**On-site action and phases.**
- Even R act by rotations about n. In the n-basis these are e^{iθ_R N} on fixed-N sectors. U is an
  N-conserving permutation, so these phases commute with it, and T-covariance reduces to the
  site-permutation identity checked above.
- Odd R act as P_R∘C up to N-dependent phases. Since UC = CU, O-covariance would require
  U P_R = P_R U, and that fails.
- Full action: an SU(2)-symmetric U would commute with S^-. But U S^-|P⟩ = S^-|P⟩ (singles are
  frozen), while S^- U|P⟩ = S^-|P+v⟩ ≠ S^-|P⟩. So U is not SU(2)-symmetric, and the NOTE's
  full-action statement is right.

**Kept FAIL (reviewer test-design error).** The first `sym` run required odd-R non-commutation on
*every* random torus configuration. That gave FAIL 26/108 and 32/108. Configurations with no active
unit commute trivially, so the requirement was wrong. The test now requires a failure on at least one
configuration. The first run is kept in `logs/phaseA_sym_firstrun_KEPT.txt`.

## Phase B — Lemma I proof and comparison with the author's tables

**Lemma I: checked, correct.** Step by step:
- (i) If S_{Q1} ∩ S_{Q2} ≠ ∅, then Q2 ∈ N1(Q1) and Q2 is a candidate. That contradicts (b) for Q1
  in its current state.
- (ii) Suppose some unit w meets both Q1 and Q2. Then w ∈ N1(Q1), and so Q2 ∈ N2(Q1). Q2 is a
  candidate and Q2 ∉ N1(Q1) ∪ {Q1}, so this contradicts (c) for Q1. Hence N1(Q1)-units never meet
  S_{Q2}, and (a) and (b) for Q1 survive crossing Q2.
  - Take w ∈ N2(Q1)∖N1(Q1) whose content changes. Then w meets S_{Q2}, so w ∈ N1(Q2) or w = Q2.
  - w = Q2 is excluded by (c) for Q1.
  - If w ∈ N1(Q2), condition (b) of Q2, taken over both states of Q2, makes w a non-candidate in
    c′. This is exactly the "state-symmetric (b) protects (c)" step.
- (iii) Q2 stays active. (a) and (b) are symmetric in Q2's state, and the units of N2(Q2)∖N1(Q2)
  do not meet S_{Q2}, so they are unchanged.
- Invariance of the active set, both inclusions: this is a local argument over the finitely many
  active units that meet R(u). It applies to infinite configurations as well.

No gap was found. Two inputs are used implicitly: (b) is evaluated with the rest of c fixed, and N1/N2
are taken within one unit family. Both match the definitions.

**Glider by hand.**
- P = {0, e1+e2} lies in exactly one plaquette and in exactly one B-tetrahedron, the cube −e3 with
  edge {e3, (1,1,1)}.
- X(P) = {e1, e2} is the edge {e1, e2} of B(0) only. L2 maps it to the opposite edge {e3, (1,1,1)}.
- B(k) = k + {e1, e2, e3, (1,1,1)} for every k. Under R ∈ T it maps to the B-set of the image cube.
  Under odd R it maps to the complement, the even-offset tetrahedron. This was checked by hand for
  C2z and C4z and numerically through T-covariance and odd-R failure.

**Tables.** Every number in the NOTE that the reviewer recomputed matches:
- 478 orbits;
- 403/6/69/0;
- 48/16;
- 50/50 with shift 0–2;
- 62 = 6 + 56;
- layer radius 3;
- empirical U radius 4.

## Phase C — what is established, and the overstatements

### What C4e establishes (correct)
U is an explicit reversible QCA in the premise class, and it meets all of the following:
- one qubit per site;
- Z^3-translation-invariant;
- conserves Q_n (axis action);
- covariant under T with the axis action's on-site phases;
- **not** O-covariant (the odd elements fail) and not full-action covariant;
- single magnons exactly frozen (consistent with C4b Lemma 2);
- face-diagonal pairs glide at 1 site/tick along the face normal, while all other pairs are static.

So the C4b/C4c/C4d question "can a bound pair move at all under these premises, at some finite range"
is answered **yes for H = T**. This agrees with C4c Observation M and C4d P1 (glider only under T).

### Fix 1 (minor): "range ≤ 6" is the CA radius, not the QCA range
The title and Result 1 say "range ≤ 6". Under (D-QCA), range means the support growth of the
automorphism α = Ad U.
- What is proved is CA radius ≤ 6 for U and U^{-1}, together with α(A_x) ⊂ A_{B_18(x)}. The 18 is
  correct: α(X_x) acts as d ↦ F(F^{-1}d ⊕ δ_x), whose support is ≤ 2r + r′.
- For permutation QCAs, the QCA range can exceed the CA radius. Example: a partitioned Toffoli
  layer has CA radius 1 and QCA range 2.
- The reviewer found exact Z^3 witnesses showing range(α) ≥ **5** and range(α^{-1}) ≥ 4, at the
  dependence of α(X_0) on a site at distance 5 (`qca_range`, TOTAL: PASS=2 FAIL=0).
- So the QCA range is in [5, 18]. Upper bounds sharper than 18 were not attempted.

**Fix:** write "CA radius ≤ 6 (QCA range between 5 and 18)" in the title and in Result 1. The body
of Result 2 already states this correctly.

### Fix 2 (moderate): the range-2 3-magnon reduction omits α(X_x)-locality
Take a monomial QCA with U|c⟩ = e^{iθ}|πc⟩. Range 2 requires α(Z_x) **and** α(X_x) in A_{B_2(x)}.
- α(Z_x) ⇔ π^{-1} has radius 2. This is c4e_02's G-locality, and F-locality follows similarly.
- α(X_x) acts as d ↦ G_x(d) = π(π^{-1}(d) ⊕ x). It must change only sites in B_2(x), and the change
  may depend only on d ∩ B_2(x).
- c4e_02 imposes F-locality, G-locality and equal stabilisers, but not this "X-locality". So its
  "existence at k ≤ 3 ⇔ equivariant bijection" is only "⇒" (a relaxation).

Evidence:
- **The certificate's own numbers reproduce.** Run in memory, unmodified except for dumping its
  data: 478 sources, 478 targets, 1,191,376 candidates, 9002 orbit edges, matching 478/478 (PASS=4).
- **Assembled map passes F/G-locality.** The reviewer built π from the dumped matching (one witness
  image per orbit edge), the reviewer's own W, the spectator images and Z^3 ⋊ T equivariance. A
  global check of that π passes on all 125,596 translation classes with k ≤ 3 and diameter ≤ 5:
  - π and π^{-1} are radius-2 CAs, with no window conflict among 325,500 windows;
  - π is injective;
  - every one of the 37,466 diameter-≤4 3-classes is hit;
  - stabilisers are consistent;
  - π is T-equivariant.

  Log: `matching_verify`, TOTAL: PASS=7 FAIL=0. **So the certificate is correct as a statement
  about radius-2 reversible CAs.**
- **That same π violates X-locality.** `xlocal` (TOTAL: PASS=1 FAIL=1) finds **336** conflicts on
  k ≤ 3 transitions. Each conflict involves one free C3 choice and forced data. There are 0
  forced–forced conflicts. Example: from d = {0, (0,1,−2)} and x = (0,1,2), the c4e_02-admissible
  image of the C3 class {0, (0,1,−2), (0,1,2)} moves the magnon 0 → (0,2,0). That move depends on the
  magnon at (0,1,−2), at distance 4 from x. For d′ = {0} the same window gives only "add x". This
  witness is a matching that satisfies all of c4e_02's constraints and still is not the 3-sector of
  any range-2 QCA.
- **An X-local extension still exists.** `xfilter` (TOTAL: PASS=2 FAIL=0):
  - The forced data (k ≤ 2 rule plus spectator images) are themselves X-local: 2,545,227
    transitions, 0 conflicts.
  - X-local unary filtering against the forced table keeps 388,024 of 391,669 candidates and 6142
    of 9002 orbit edges.
  - A new maximum matching is again **478/478**.
  - The re-matched π passes the full F/G check (`matching_verify_xfiltered`, PASS=7 FAIL=0). It also
    passes the **full** X-locality check, free–free couplings included, on all 2,578,011 k ≤ 3
    transitions tested (`xlocal_xfiltered`, TOTAL: PASS=2 FAIL=0). Coverage gap: 600 diameter-5
    3-classes whose preimage has diameter 6 were skipped.

**Verdict:** the conclusion of Result 3 holds: a T-equivariant monomial 3-magnon sector compatible
with range 2 exists. The stated reduction and certificate do not establish it, because the
certificate needs X-locality. **Fix:**
- add X-locality to the reduction's constraint list;
- replace "⇔" by the correct statement: necessary conditions F/G/X-locality, generators Z_x and X_x;
- cite the re-matched certificate. It is the reviewer's, built on the author's candidate generator.

The k ≥ 4 caveat stands unchanged. X-locality of transitions into the k = 4 sector is untested, and
it couples to the k = 3 choice.

### Other notes (no change needed)
- **Coverage of random tori.** At random density very few units are active (162 crossings over 320
  configurations at L = 8). The author's `c4e_07` and the reviewer's `stress` cover the regime where
  Lemma I bears load.
- **Provenance.** The NOTE says the work was "checked by an independent implementation (same
  author)". That is accurate. This review adds a second, blind implementation, again by the same
  model.
- **Result 4 sign convention.** E = K·v versus ε = −K·v: both are stated consistently in the NOTE.

## Evidence (review_scripts/logs)

| log | TOTAL |
|---|---|
| phaseA_inv | PASS=11 FAIL=0 |
| phaseA_sparse_dense | PASS=1 FAIL=0 |
| phaseA_local | PASS=5 FAIL=0 |
| phaseA_u1 | PASS=3 FAIL=0 |
| phaseA_sym | PASS=7 FAIL=0 |
| phaseA_single | PASS=3 FAIL=0 |
| phaseA_pair | PASS=6 FAIL=0 |
| phaseA_triple | PASS=2 FAIL=0 |
| phaseA_quad | PASS=1 FAIL=0 |
| collide | PASS=3 FAIL=0 |
| stress | PASS=3 FAIL=0 |
| qca_range | PASS=2 FAIL=0 |
| matching_verify (author matching, F/G) | PASS=7 FAIL=0 |
| xlocal (author matching, X-locality) | PASS=1 FAIL=1 (**finding**, Fix 2) |
| xfilter | PASS=2 FAIL=0 |
| matching_verify_xfiltered | PASS=7 FAIL=0 |
| xlocal_xfiltered | PASS=2 FAIL=0 |
| phaseA_sym_firstrun_KEPT (superseded, reviewer test error) | PASS=5 FAIL=2 |

Current runs, excluding the finding log and the superseded log: **TOTAL: PASS=65 FAIL=0**.
Including the X-locality finding and the kept first run: **TOTAL: PASS=71 FAIL=3**.

Other files in `review_scripts/logs/`:
- `qca_range_dense_probe_ABORTED.txt`: an ineffective dense probe, superseded by the sparse probe.
- `matching_s-1.json`, `candidates_s-1.json`, `matching_xfiltered_s-1.json`: data.
- `author_c4e_02_rerun*.json`: the author's summary output, redirected away from `C4e/logs/`.
- `queue.txt`: job timing.

Reproduce (one core, `OMP_NUM_THREADS=1 nice -n 10`, each job < 20 min), from `review_scripts/`:
- `python3 -B rv_phaseA.py [inv sparse_dense local u1 sym single pair triple quad]`
- `rv_collide.py`
- `rv_stress.py`
- `rv_qca_range.py 700`
- `rv_extract_matching.py`, then `rv_matching_verify.py`, then `rv_xlocal.py`
- `rv_extract_candidates.py`, then `rv_xfilter.py`, then
  `MATCHING_JSON=matching_xfiltered_s-1.json LOG_SUFFIX=_xfiltered python3 -B rv_xlocal.py`

## Correction confirmation (2026-10-19)

I re-read the complete corrected NOTE.md.

- **Fix 1: resolved.** The title, Result 2 and the claim-types table now say CA radius ≤ 6 and QCA
  range in [5, 18]: ≥ 5 from the exact witness in `review_scripts/logs/qca_range.txt`, ≤ 18 proved.
- **Fix 2: resolved.** The reduction is now stated as necessary conditions only, with X-locality
  added, and "⇔" is withdrawn. The 336 conflicts are reported. Result 3 cites the X-filtered
  re-match as its certificate, with the coverage gap (600 skipped classes) and the k ≤ 3 limit
  stated.
- **The citation resolves.** The re-match pipeline and its outputs are all saved in
  `review_scripts/`:
  - scripts: `rv_extract_candidates.py`, `rv_xfilter.py`, `rv_matching_verify.py`, `rv_xlocal.py`;
  - matching: `logs/matching_xfiltered_s-1.json`;
  - logs: `logs/xfilter.txt` (TOTAL: PASS=2 FAIL=0), `logs/matching_verify_xfiltered.txt`
    (TOTAL: PASS=7 FAIL=0), `logs/xlocal_xfiltered.txt` (TOTAL: PASS=2 FAIL=0).
- **No new defect.** One wording nit, not blocking: the bullet "The unknowns are independent" is
  true only for the F/G relaxation. The next bullet says so, because X-locality couples classes.
  Optionally retitle it "independent under F/G only". X-locality of transitions into the k = 4
  sector stays untested; this is already covered by "does not reach k ≥ 4".

**Final verdict:** the construction (claims 1, 1′, 2, 4–7) is **correct**. Claim 3 is **correct with
the applied fix**. No open defects remain.
