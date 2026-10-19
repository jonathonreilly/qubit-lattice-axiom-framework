# C4f independent review

Reviewer provenance: a Claude subagent, same model as the author (not independent of the
author's model). Inputs: repo docs + C4f/C4e NOTE definitions; reviewer code written from scratch
in `review_scripts/` (no author or C4e scripts imported or copied).

## Phase A — symmetry derived before reading C4f Step 1

Source of the action. Soldering menu note (docs/THE_SOLDERING_MENU_..._2026-09-22.md, Thm 1) and
its runner convention (scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py,
`Q(M,'axis') = perm_sign(M)*|M|`): axis soldering sends g in O to the Bloch rotation
rho(g) = s(g)|g|, with |g| the axis-permutation matrix and s(g) its sign. The occupation basis is the
n.sigma eigenbasis with n = (1,1,1)/sqrt3 (C4b Lemma 2: the only rho(O)-invariant line).

Derivation.
1. rho(g)n = s(g)n since |g| fixes (1,1,1). The kernel of g -> s(g) is the tetrahedral group T
   (identity, three coordinate pi-rotations, eight body-diagonal 2pi/3 rotations: exactly the even
   axis permutations). Odd elements (six quarter-turns, six edge pi-rotations) have s = -1.
2. g in T: rho(g) = |g| is a rotation about n by 0 or +-2pi/3, so the SU(2) lift is
   exp(-i theta n.sigma/2): diagonal in the n basis, = global phase x omega^{+-n} (omega = e^{2pi i/3};
   V4 elements act trivially).
3. g odd: rho(g) = -|tau|, tau a transposition; this is a pi-rotation about an axis perpendicular to n
   (e.g. swap(x,y) -> pi about (1,-1,0)/sqrt2). Lift = -i a.sigma, which in the n basis is
   off-diagonal: u_g = (global phase) * omega^{k n} * C, C = |0><1| + |1><0| (particle-hole), with k in
   {0,1,2} fixed by which of the three perpendicular axes is used.
   Checked numerically: `review_scripts/rA_onsite_action.py` -> `logs/rA_onsite_action.log`,
   TOTAL: PASS=49 FAIL=0 (all 24 lifts reproduce rho; 12 diagonal with phase ratio a cube root of
   unity; 12 off-diagonal, phase ratios in one coset c{1,omega,omega^2}).
4. Covariance of a TI QCA U with [U,N] = 0 (N = sum n). V_g = (tensor u_g) pi_g, where pi_g permutes
   sites. For g in T, tensor u_g = c^|L| omega^{+-N} commutes with U, so V_g U V_g^dag = U iff
   [U, pi_g] = 0. For odd g, tensor u_g = c^|L| omega^{kN} C_glob with C_glob = tensor C; omega^{kN}
   commutes with U, so covariance iff [U, C_glob pi_g] = 0. Since odd = g0 T and C_glob commutes with
   every pi, the T conditions plus one odd g0 imply all twelve odd conditions. Global phases cancel
   in conjugation. (If covariance is only required up to a scalar, the conditions above are
   sufficient; this review checks the strict form.)

Conclusion of Phase A: my independent derivation agrees with the C4f claim
"odd R act as Q_n-phase x C o pi_R; O-covariance <=> [U,pi_R]=0 for R in T plus [U,C pi_R]=0 for
one odd R". Caveat to record: this assumes [U,N]=0 (used to drop the omega^{kN} phases); the
reduction is not valid for a non-U(1) U, and rotation centre must be compatible with U's
translation structure (site vs cube centre) — checked in Phase B below.

Comparison with C4f Step 1 (read after the above was written): Step 1 states the same thing
(beta_R = gamma o C o pi_R for odd R; T acts by Q_n phases; equivalence with [alpha,pi_R]=0 on T and
[alpha, C pi_R0]=0 for one odd R0, valid for Q_n-conserving alpha). Same occupation axis
n = (1,1,1)/sqrt3, same conventions (C4f: magnon = +n spin, vacuum = -n; my phase checks use that
labelling). **Verdict: correct.**

## Phase B — reviewer's own implementation

`review_scripts/rlib.py` implements U = L2 o L1 from the NOTE definitions only (squares with
D, D' diagonals; tetra-axis units (B,j,k): S = B(k), D/D' split by x_j, Gamma = A(k) empty;
(A,j,k): S = A(k), Gamma = B(k) full; N1 with both F_w∩S_u and F_u∩S_w clauses; N2; activity
(a)(b)(c)). No author or C4e code was imported or copied. Neighbour-template sizes come out
independently as N1/N2 = 32/178 (squares) and 149/588 (controlled tetra-axes), matching the NOTE.
The on-site action used for covariance is my Phase-A lift (`rA_onsite_action.py`), applied with the
full product phase over all L^3 sites. Rotations were tested both about a site and about a cube
centre, plus random translations. Tori: L = 8, 10, 12 (L must be even for the parity of sites to
be defined; neighbourhood lists assert no wrap-around).

| check | log | result |
|---|---|---|
| on-site lifts, 24 R (Phase A) | `logs/rA_onsite_action.log` | PASS=49 FAIL=0 |
| Lemma I′: L1²=L2²=id, U⁻¹U=id, N conserved, U⁻⁶U⁶=id; random densities 0.01–0.99 + packed planted-unit stress on empty/full/half/slab/random backgrounds, L = 8, 10, 12 | `logs/inv.log` | PASS=8 FAIL=1 (see note) |
| same, L = 8, 5× more stress (828 configs; crossings L1 345, B 66, A 72) | `logs/inv_more.log` | PASS=3 FAIL=0 |
| k ≤ 4 magnons in the O-closed box [−1,1]³ **and** all complementary k ≤ 4 hole configs (41,708 configs, 12,864 moved): involutions, U⁻¹U, N, injectivity; covariance V_gU = UV_g for all 24 g with phases (0 mismatches); witnesses [U,π_R] ≠ 0 for 12/12 odd R and [U,C] ≠ 0; direct covariance k = 3,4 in [−2,2]³ (5760 pairs, site- and cube-centred) | `logs/sectors.log` | PASS=6 FAIL=0 |
| covariance (24 g × 2 centres, phases) + translation on random finite-density/stress configs, L = 8, 10, 12 | `logs/sym_random.log` | PASS=3 FAIL=0 |
| covariance on isolated planted units (genuine crossings of all three kinds), L = 8, 12 | `logs/sym_planted.log` | PASS=2 FAIL=0 |
| single magnon and single hole fixed by U and U⁻¹; **all** pair relative positions (whole torus at L = 8; \|ρ\|∞ ≤ 4 at L = 10, 12) for 3 ticks: exactly the 12 face relative vectors (6 unordered orientations) move by v = ρ_bρ_c e_a per tick, all others static; hole pairs move by −v | `logs/pairs.log` | PASS=12 FAIL=0 |
| exact structural dependency radius per layer = 3 | `logs/radius.log` | PASS=3 FAIL=0 |
| targeted single-flip influence: L1 3, L2 3, U 5 (reproduces the author's ≥ 5 witness) | `logs/influence.log` | PASS=1 FAIL=0 |
| parity step (structural): R ∈ T maps B→B, A→A; odd R maps B↔A; Γ→Γ; {D,D′}→{D,D′} (3888 images); squares → squares | `logs/structure.log` | PASS=3 FAIL=0 |
| Step-2 counts | `logs/rC_pairmoves.log` | PASS=6 FAIL=0 |

`logs/SUMMARY.txt`: **TOTAL: PASS=96 FAIL=1.**

The one FAIL is a reviewer coverage threshold, not a property failure. At L = 8 the first `inv` run
crossed only 25 B-units and 25 A-units, under my own threshold of 50. Every involution check in that
log passed. The log is kept unmodified, and `inv_more.log` (separate file) adds coverage at L = 8.

Reviewer disclosure (the same evidence-preservation point I raise against the author): my first
`pairs` run printed FAIL=6. That was my own wrong expected count: I expected 6 moving relative
vectors, but each unordered face pair appears twice as ρ and −ρ, so the correct number is 12. The
mismatch counts were never printed. I fixed the expectation, and the rerun overwrote that log. It is
recorded here, not preserved.

## Phase C — proofs

**Lemma I′ (read-set involution).** I checked each step.
- (i) Q2 ∉ N1(Q1), from (b) at Q1's actual state. This gives F_{Q1}∩S_{Q2} = ∅ (the second clause;
  it protects Q1's own candidacy) and F_{Q2}∩S_{Q1} = ∅.
- (ii)(b) A unit w ∈ N1(Q1) whose candidacy changes must have F_w∩S_{Q2} ≠ ∅. By the first clause,
  w ∈ N1(Q2). By symmetry of N1, Q2 ∈ N1(w), so Q2 ∈ N2(Q1), which contradicts (c). In fact
  N1(Q1) ∩ N1(Q2) = ∅. The step uses both clauses, through the symmetry of N1.
- (ii)(c) and (iii) are correct as written. In (iii)(c), units of N2(Q2) are outside N1(Q2) ∪ {Q2},
  hence F∩S_{Q2} = ∅. Γ∩S = ∅ holds for both controlled kinds.
- The global step A(Lc) = A(c) is C4e's argument, and it carries over unchanged.

**Verdict: correct.**

Probe (`logs/rC_variants.log`, L = 8, 400 packed configs, informational):
- C4e's site-sharing N1 applied to the controlled layer fails L2² = id on 56/400 configs. So the
  read-set extension is load-bearing.
- One-sided variants (only F_w∩S_u, or only F_u∩S_w) gave 0/400 failures.
- The NOTE's "must include both" is therefore true of the proof, not shown necessary for the
  involution. No action needed beyond the wording ("the proof uses both").

**Parity step.** For z ∈ K(k), the image cube's lower corner k′ has par k′ ≡ par k + #sign flips;
odd R have an odd number of flips. It follows that odd R maps B(k) → A(k′) and A(k) → B(k′), with
the control set going to the control set. C swaps "Γ empty" ↔ "Γ full" and D ↔ D′. So Cπ_R maps
the candidate structure onto itself. This was confirmed structurally (`structure.log`) and
dynamically (`sectors`, `sym_*`). **Correct.**

**SU(2) remark (monomial pairs static).** The argument uses [U,S⁻] = 0 and frozen singles, which
give {x′,y′} = {x,y}. **Correct** for the monomial case, as scoped. Not separately run.

**Step 2 counts.** I reimplemented the criterion myself: near pair, four cross distances ≤ r,
fixed by Stab(c) in G⋉Z³, COM change. I reproduced every entry: r=1 T 6/13, O 0/13; r=2 56/62,
36/62; r=3 162/171, 132/171. **Correct.** The reading "under axis-O the in-sector constraint is
T" follows from Step 1.

## Per-claim verdicts

| # | claim | verdict | severity of issues | fix |
|---|---|---|---|---|
| 1 | Step 1: odd R = phase·C∘π_R; O-axis ⟺ T-perm + one Θ (for Q_n-conserving α) | correct (independently derived first) | — | — |
| 2 | Θ maps k-magnon ↔ k-hole sectors; no extra in-sector constraint beyond T | correct | — | — |
| 3 | Lemma I′ (L1, L2 involutions, any configuration) | correct | informational | say "the proof uses both N1 clauses"; one-sided variants did not fail in tests |
| 4 | U TI, bijective, U(1), O-covariant with axis phases (site- or cube-centred) | correct | — | state that the torus needs even L (parity), and L ≥ 8 suffices for the neighbourhood lists |
| 5 | frozen single magnons / single holes | correct | — | — |
| 6 | two-magnon sector = C4e glider (speed 1, v = ρ_bρ_c e_a), others static | correct | informational | "6 move" counts unordered pairs (12 ordered relative vectors) |
| 7 | hole pairs glide at −v | correct | — | — |
| 8 | per-layer CA radius 3; U radius ≤ 6; influence witness ≥ 5 | correct (reproduced) | — | — |
| 9 | QCA range ≤ 18 | correct as a bound (C4e's crude 2r+r′ argument, re-read, not recomputed) | — | — |
| 10 | parity step | correct | — | — |
| 11 | Step-2 counts r ≤ 3 | correct (reproduced) | — | — |
| 12 | SU(2) ⇒ monomial pairs static | correct (proof read) | — | — |
| 13 | interface reflection; head-on pairs (descriptive) | unverified (not re-simulated) | — | — |

## Evidence-preservation issue (recorded)

The first `c4f_01` Part-B log, with the wrong orbit-restricted criterion and one FAIL, was
overwritten. It is also absent from git: the first checkpoint containing that log (4e2e24332,
06:53Z) already shows PASS=10 FAIL=0. The NOTE and WORKLOG disclose this, which is the right
minimum.
- **Severity: low** (process). The replaced criterion is C4c's, and I independently reproduced its
  counts, so no result depends on the lost log.
- **Fix:** record the superseded FAIL line verbatim in WORKLOG, or regenerate it under a
  `*_superseded` filename. Going forward, write logs no-clobber (timestamped) and checkpoint before
  re-running.

Separately, commit a38983208 replaced a passing `c4f_02_sym` log (30 configs) with a stronger run
(200 configs). The old version is in git history. This is a strengthening, not a hidden failure.

## Overall

The C4f constructive claim stands: an axis-O-covariant (phases included), TI, U(1), one-qubit QCA
on Z³ with frozen singles and holes, a speed-1 face-pair glider, and the −v hole glider. It was
reproduced from the definitions by independent code, and no load-bearing error was found. Not
established, as the NOTE itself states: range 2, k ≥ 3 dynamics beyond the involution and covariance
checks above, and the interface results.
