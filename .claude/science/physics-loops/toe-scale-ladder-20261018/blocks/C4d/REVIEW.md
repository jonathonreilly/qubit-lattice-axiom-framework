# C4d — Independent review

**Reviewer provenance:** a Claude subagent, same model as the author, in a separate context.
It wrote only this file and `review_scripts/`. Theorem P1 was handled blind: the reviewer
derived the unknowns and constraints from the definitions and wrote and ran its own solver
(`rv_p1_blind.py`) before opening the author's `c4d_05` code or logs. No commits.

**Evidence:** `review_scripts/SUMMARY.txt`, which reads **TOTAL: PASS=18 FAIL=0**:

| log | result |
|---|---|
| `rv_p1_blind_T.log` | PASS=5 FAIL=0 |
| `rv_p1_blind_O.log` | PASS=5 FAIL=0 |
| `rv_r2_glider.log` | PASS=3 FAIL=0 |
| `rv_spectator_and_phases.log` | PASS=5 FAIL=0 |
| `rv_p1_blind_C1.log` | scope probe only, stopped on purpose; no TOTAL, not counted |

Every run used one core under `nice 10`, and each took less than 1 minute, apart from the C1 probe.

## Verdict table

| claim | verdict | severity of issues |
|---|---|---|
| (1) Lemma S (spectator), for U and U† | **correct** | none |
| (2) Theorem P1 (T and O, r = 1, pair sector diagonal) | **correct** (blind reproduction) | none; one cosmetic count note |
| (2') T acts by pure permutations on the 2- and 3-magnon sectors (axis action) | **correct** | none |
| (3a) Lemma D | **correct** | cosmetic: W_k is defined only under the inductive hypothesis |
| (3b) Proposition E | **correct with fix** | minor: the "every shell" wording is too broad |
| (4a) The r = 2 face glider passes the 3-magnon test, and the v = 2 glider fails it | **correct**; "open" is honest | none |
| (4b) The k = 3 near-solutions | **correct with fix** (wording) | minor to moderate: the residual is misreported, and item 4 states its conclusion too strongly |

## (1) Lemma S — correct

**Own proof.** Choose UΩ = Ω, which is possible because the vacuum is α-invariant. Then:

U|C∪w⟩ = U σ⁺_C σ⁺_w Ω = α(σ⁺_C) α(σ⁺_w) Ω = e^{iφ} α(σ⁺_C) |w⟩.

- α(σ⁺_C) lies in the algebra of N_r(C), and w ∉ N_r(C). The state |w⟩ agrees with Ω on N_r(C).
  So α(σ⁺_C)|w⟩ = (α(σ⁺_C)Ω) ⊗ |w⟩ = (U|C⟩) ⊗ |w⟩.
- U|C⟩ is supported in N_r(C), so it has no magnon at w, and the tensor product is a legitimate
  configuration.
- For U†, apply the same argument to α⁻¹. Its range is the same, because the inverse
  neighbourhood is −N = N for the Chebyshev ball. The phase becomes e^{−iφ}, and the NOTE leaves
  this implicit.

No translation invariance (TI) or symmetry is used.

**Toy check, my own construction.** I built a non-TI ring with L = 12 and range 3: U = V D V†,
where V is a layer of random U(1) gates and D is a random n_x n_{x+1} phase.
- Singles are frozen to 6e−16.
- Pairs move, with 1 − |⟨xy|U|xy⟩| up to 0.56.
- The identity holds for U and U† in 163/163 cases with dist(w, C) > 3.
- It fails in 989/1082 cases with dist ≤ 3.

**Derivation of (S) and (S†).** I re-derived both independently:
- A configuration p ∪ w with (p, w) valid has a unique valid decomposition. So distinct valid
  pairs (p, w) give distinct configurations.
- Isometry then gives (S). The case w₁ = w₂ reduces to unitarity of W.
- I also checked the NOTE's claim that forward/backward cross-consistency is automatic. Suppose
  σ ∈ supp(W p_a) and σ ∪ w_a = p_b ∪ w_b with w_b ≠ w_a. Then w_b ∈ σ, and σ is a near pair, so
  dist(w_b, σ ∖ w_b) ≤ r. That contradicts the validity of (p_b, w_b).
- This argument holds at **every** r, not only r = 1. That is a harmless strengthening.

## (2) Theorem P1 — correct (blind exact reproduction)

`rv_p1_blind.py` was written from the definitions. It shares no code with the author.

**Unknowns.** ⟨σ|W|p⟩ for near pairs σ and p, with the symmetric Lemma-K support (all four cross
distances ≤ 1, for α and α⁻¹), keyed by orbits of G ⋉ Z³:
- G = T: the 12 signed permutations with even permutation and an even number of minus signs.
- G = O: all 24 signed permutations with det = +1.
- Result: **62 unknowns for T (3 stays) and 36 for O (3 stays)**, which matches the author.

**Constraints.**
- W†W = 1 and WW† = 1.
- (S) and (S†), each enumerated as 80172 raw (p₁, w₁, p₂, w₂) instances. This also matches the
  author's count.
- After de-duplication there are 8566 distinct constraints (T) and 3824 (O). The author's
  "6565 unitarity constraints" is a raw count under a different convention, which is immaterial.

**Elimination rule.** All arithmetic is exact, with integer coefficients. The rule is slightly
more general than the author's single-term rule:
- a constraint whose surviving terms are all |x_i|² with coefficients of one sign, and whose
  constant is zero, forces all of those x_i to zero;
- if that stalls, the solver case-splits on any surviving single off-diagonal monomial.

**Result.**
- **T:** 59 zeros. These are exactly the 59 non-stay unknowns, which is the author's set: both
  sets equal "all non-stay". No branching was needed. No contradiction appears, and no stay is
  forced to zero.
- **O:** 33 of 36 zeros, likewise.
- **Converse:** a diagonal W with random stay phases satisfies all constraints exactly.

**Scope probe C1** (no point group). My rule gives 174 zeros of 679, which matches the author's
"174 zeros, 492 undecided". The branching stage grows exponentially without symmetry, so I
stopped it. This confirms the author's statement that T is load-bearing for the certificate.

**The worked example is valid.** The amplitude {0, e₃} → {−e₁−e₂, −e₁−e₂+e₃} is mapped by the C2z
about (−1, −1, ·) to the same image from p₂ = {−2e₁−2e₂, …}. That element is in T, because its
permutation is the identity and it has two sign flips. In ⟨Wp₁|Wp₂⟩ = 0, every other term is
already zero, which leaves |x|² = 0.

**T acts by pure permutations — correct** (`rv_spectator_and_phases.py`, explicit SU(2) lift).
- Under the axis action, Q(R) = sgn(perm R)·|R| (C4 conventions). Every R ∈ T has an even
  permutation, so Q(R) is a C3 about n = (1,1,1)/√3, or the identity on V4.
- Its SU(2) lift is diagonal in the n-basis to 1e−16. So β_R(σ⁺_x) = e^{−iθ_R} σ⁺_{Rx}, and with
  VΩ = Ω, V|C⟩ = e^{−iθ_R|C|}|RC⟩.
- α commutes with β_R and UΩ = Ω, so V†UV = U. Within a fixed-|C| sector the phases cancel:
  ⟨RC′|U|RC⟩ = ⟨C′|U|C⟩, which is a pure permutation for every |C|.
- The cube-centre convention changes R only by an integer translation (c − Rc ∈ Z³).
- Full action: global SU(2) symmetry turns β_R into the pure site permutation P_R.

**Cosmetic note.** The NOTE's "no-go discipline" hypothesis asks for the 2- *and* 3-magnon matrix
elements to be T-invariant. The proof needs only the pair sector, because (S) and (S†) are
symmetry-free. The weaker hypothesis stated in item 2 is the correct one.

## (3a) Lemma D — correct

The proof checks out:
- x ∉ D, and y ∉ B_r(x) gives |D| ≤ k − 1.
- U†|D⟩ ∝ |D⟩ and U|D∪x⟩ ∝ |D∪x⟩ by hypothesis, so α(σ⁺_x)|D⟩ = U σ⁺_x U†|D⟩ ∝ |D∪x⟩.
- The factorisation across B_r(x) holds.
- The "iff" follows by induction on k, with frozen singles as the base case. At r = 1 the cliques
  are subsets of a 2×2×2 cube, so k ≤ 8.

**Cosmetic fix.** W_{k+1} is an invariant restriction only once sectors ≤ k are diagonal. Say so
in the definition.

## (3b) Proposition E — correct with fix (minor)

I checked each step of the proof:
- (R+t) ∩ A = {p}.
- (λ+t) ∩ A = ∅ because v ∉ λ, so both gates are active on c.
- g_t fills p ∈ S, which disables g₀.
- π(μ) ∩ (R+t) ⊂ (R+t) ∩ A ∖ R = ∅, so g_t g₀ c can only be one of the two listed options.
- Restricted to R, the two results differ (μ versus π(μ)).
- The width argument in steps 3–5 is correct, and the toggled-in λ is non-fixed.

**Fix.** Results item 5 and the Coverage paragraph say "for every finite shell". The theorem
needs a generic ℓ whose two A-extremes lie in S. That is a surrounding shell, for example
S ⊇ vertices of conv A. A partial or one-sided shell, or the empty shell, is not covered. Add
"surrounding" to the summary.

The reduction of "every caterpillar realisation" to the tetrahedral gate assumes R is the
4-site tetrahedron. Gates with untoggled extreme sites, or catalytic sites, are already listed
as escape routes, so the scope is honest once "surrounding" is added.

## (4a) r = 2 glider — correct; "open" is honest

`rv_r2_glider.py` is my own construction and my own conflict test.
- **The glider:** a face pair with zero coordinate a moves by −ρ_bρ_c·s·e_a.
- **Properties** (checked for both signs s): it is T ⋉ Z³-covariant, it has Lemma-K support at
  r = 2, and it is a bijection.
- **Speed 1:** 0 conflicts for (S) and for (S†).
- **Speed 2:** 24 conflicts each. The author reports 16 under a different counting convention;
  both are nonzero.
- **Control:** the same speed-1 glider at r = 1 has conflicts, as Theorem P1 requires.

The NOTE says correctly that this is a statement about W-only constraints. It is not a
construction, and pair–pair and 4-magnon data are not tested. The "open" status is stated
honestly.

## (4b) k = 3 numerics — correct with fix (wording)

**What is right.**
- The exact part (96 zeros, 159 undecided, FAIL kept) is consistent: 260 − 5 − 96 = 159.
- The NOTE's k = 3 section correctly says that it cannot tell whether exact moving solutions
  exist, and that no dispersive triple band is claimed.

**Issues.**
1. **The residual is misreported.** "Residual ≤ 3e−13" (item 4 and the k = 3 section) is the
   scipy `least_squares` cost, ½‖r‖². The actual residual norm is ‖r‖ ≈ 8e−7. The log's PASS line
   "satisfies the W₃-only system to 1e−10" compares the cost, not the residual, against 1e−10.
   - For the off-diagonal case, cost 2e−18 gives ‖r‖ ≈ 2e−9. That is good evidence that exact
     off-diagonal solutions exist.
   - The moving case is only an approximate solution.
   - **Fix:** report ‖r‖ and the max constraint violation.
2. **Item 4 overstates the conclusion.** "So at k = 3 the W-only constraints do not freeze
   triples" is stated as a conclusion. For COM-moving solutions the data are evidence only. The
   cost converges slowly (5e−14 → 3e−13 at μ = 0.2 across runs), and the band variation is not
   converged (3e−3 at 500 evaluations, 1.2e−2 at 4000). The variation is genuine for the
   approximate solution, since ‖r‖ ~ 1e−7 cannot produce 1e−2 eigenphase spread in a near-unitary
   matrix. But an ill-conditioned near-solution need not lie near an exact one.
   - **Fix:** "numerical evidence suggests that the W₃-only constraints admit non-diagonal (and
     possibly COM-moving) solutions".
3. **The log contradicts the NOTE.** The `c4d_10` log line "DISPERSIVE bands for this solution"
   conflicts with the NOTE's "no claim of a dispersive triple band". Relabel it, for example
   "approximate solution has nonflat spectrum".

**Bottom line.** The global "open / not decided" status in the bottom line and the no-go
discipline is honest. Only the item-4 phrasing and the residual metric need correcting.

## Required changes (all minor; none affects a proved claim)

1. Prop. E summary and Coverage: "every finite shell" → "every surrounding shell (∃ generic ℓ
   with both A-extremes in S)".
2. k = 3: report ‖r‖ (≈ 8e−7), not the cost. Soften item 4's "do not freeze triples". Relabel
   the c4d_10 "DISPERSIVE" log line.
3. Optional:
   - Lemma D: define W_k under the inductive hypothesis.
   - P1: note that the hypothesis needs only pair-sector covariance, and that cross-consistency
     is automatic at every r.

The load-bearing Theorem P1 is confirmed by blind independent exact elimination for both T and O.
