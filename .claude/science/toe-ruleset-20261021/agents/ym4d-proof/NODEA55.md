Reviewer model: claude-opus-5-5

# NODEA55 — node A / HW interface after REVIEW55_HWPLD: the spectator quantifier, the conditioning quantifier, the j = k_0 and level-0 edges, the weighted-law decoupling, and the multiplicative Δ_sh

UTC start: 2026-10-28T23:05:14Z (first read). This file opened: 2026-10-28T23:44:39Z.
Role: WORKER (Opus 5.5), not a reviewer; the brief's binding rules apply. Check-id prefix: `na55_`.
Files written by this worker: `$L/NODEA55.md` and `$L/checks/na55_*` only. No git command is run. Append-only.

## PRE-STATED (statements only; written after reading the inputs listed below and an unwritten exploratory pass,
## BEFORE any written derivation, any criteria file and any script)

Targets.
- **W1 (repair).** Restate (E2^𝔉′) (HW §37), (CEM^{COL}) (PLD §18.7.1), (ACT′) (PLD §19.5), (LCR^act′) (PLD §19.4-§19.5),
  (EQ-bc)/(BCH-1) (PLD §19.6), the law class 𝔏^buf_k (PLD §18.7.0), PLD §18.6.2 Delta 3 / §18.9 M-7, Cor. E2-RED (PLD §18.7.1),
  HW §37's F_< bullet and HW §38 item 5, with F_< restricted to the capped HISTORY spectators. For each: read its consumer(s) and
  say whether the restricted form is what the consumer passes; say whether REVIEW55 F6's falsifying argument still applies.
  Also test, for each statement, every OTHER universally quantified weight/conditioning function in it by the same standard
  (a free function that can condition on a rare event is suspect for the same reason F_< was).
- **W2 (edges).** (a) j = k_0: decide whether the restricted form recovers it (REVIEW55 F5 (iii)(b) says it should, via GEO (iv)).
  (b) Level 0: decide exactly which level-0 statements TEL-f / Cor. CRC-HW / Theorem CRC-2T′ consume ((0a), (0b), or another
  shape), and reduce or prove what can be reduced or proven.
- **W3 (residual).** State the weighted-law decoupling inside (ACT′)/(CEM^{COL}) with all quantifiers; attempt a proof; test the
  mechanism "the weight's typicality, not the event"; if no proof, state precisely what is missing.
- **W4 (Δ_sh).** List every place the chain used PLD §18.5 (b′)'s depth-free Δ_sh (or §16.6 (b)'s), and give the corrected
  consequence using ‖x(S)‖_sh ≤ 16‖S‖_sh + c|S| (REVIEW55 F9 gives c = 81).

What counts as success / refutation for my own claims.
- A restated statement is acceptable only if (i) every consumer's actual instance lies inside its quantifier range (checked by
  reading the consumer's proof step, quoted by locating string), and (ii) no fixed-volume counterexample of the F6 type exists
  for it. A restated statement is REFUTED (by me) if I exhibit an instance in its quantifier range where the bound fails as g → 0.
- A claimed implication is PROVEN-HERE only if every step is written; a step that uses an unproven input is CONDITIONAL on it,
  named. A claimed counterexample is PROVEN-HERE only if every inequality in it is verified (exactly, where numeric).
- Any "the edge is recovered" claim fails if a single step of the consumed theorem needs a property the restricted class lacks.
- A "missing statement" is acceptable only if it is stated with all quantifiers and it is not a renaming of the statement it
  replaces.
- Numeric checks: criteria file first (no constant derived in this file inside a PASS/FAIL condition), exact integer/rational
  arithmetic, rigorous rational intervals for transcendental functions, a negative control per gate.

(PRE-STATED ends here. Everything below was written after it.)

**Mid-task requirement received from the coordinator (≈ 23:53 UTC, after the PRE-STATED block above):** state, for every
restated item and for (SDP)^A, (PRICE^ℛ), (M-f^A), (LI^F) as far as this scope reaches, whether its constants are uniform in
the cutoff n_♯; say whether the F_< restriction changes that; and if uniformity cannot be shown, say what it needs
(SMALLNESS_DAG.md §3.1, "the n_♯ loop"). Added as target **W5**; answered in Part D. (Recorded here so the order is visible:
W5 was not pre-stated.)

## Inputs read (read-only; files as on disk now; lines located by string)
- REVIEW55_HWPLD.md, all 678 lines.
- HW.md: §0 (l.28-44); §4 (l.159-240: tower energies, TE, W-bad, DJ); §13.1-§13.3 (l.607-707: R_{S,E}, DECL, REL-seq, NA-∅);
  §14-§15 (l.708-800: CAP, (LI^F), H4-red′, (M-f^cap), HW^cap, CAP-dec); §21-§22 (l.1071-1146: TILT, FP, NR, LI^U-0, Cor. LI-0);
  §24 (l.1189-1330: REL-boot, TEL-f, (E1)/(E2), E1-1, E2-1, (CRC-1)); §30.1-§30.7 (l.1468-1665); §34-§41 (l.1737-2411).
- PLD.md: §16.6-§16.7 (l.1445-1500); §17.2-§17.6 (l.1734-1920); §18 (l.1968-2932); §19 (l.2933-3705).
- HIST.md §7.1 (l.450-480: histories, admissibility (A1)/(A2), Lemma H-nest).
- REVIEW_HW_S5.md l.360-440 (S5-16, S5-17, S5-19) and l.580-600 ([RHW5-fix E2-2]); REVIEW_PLD_S5.md l.305-325 (S5-20) and
  l.480-500 (B1-B6). HANDOFF.md in full. SMALLNESS_DAG.md §1 and §3 (for W5). checks/w6_arith.py (HW's inputs, for K1 only).
- Codex reviews: grep of all CODEX_REVIEW_*.md for "CEM", "F_<", "E2^", "PLD", "HW.md", "node A": hits only in DECADES, SYMBOLS
  and KN, none on any item of this task. **No Codex verdict is used in this file.**

## Checks run (criteria written and hashed BEFORE each script; plain python; no float in any verdict)
| id | criteria (md5, time) | script (md5) | result |
|---|---|---|---|
| na55_geo | checks/na55_geo_criteria.md (592b4fc2…, 23:52:24Z) | checks/na55_geo.py (33f150b6…; one pre-run edit, below) → na55_geo_out.txt; 8.4 s, 121 MB, exit 0 | **G1-G5 PASS**; every negative control fired (G1n, G2n 320/320, G3n 240/240, G5n) |
| na55_const | checks/na55_const_criteria.md (fe42e4f1…, 23:52:47Z) | checks/na55_const.py (7b8d49ec…) → na55_const_out.txt; 7.1 s, 19 MB, exit 0 | **K1-K6 PASS**; K3n and K5n fired; K2/K7 records |
- *Disclosure.* na55_geo.py was edited once BEFORE its first run (23:56:30Z; md5 92987891… → 33f150b6…): G3's level-m set
  π(N_8(col 𝒟)) was switched from a per-child box union (≈ 2.4·10⁸ set operations, too slow) to the per-cube box
  [3x−8, 3x+10]⁴ projected to [x−3, x+3]⁴, which is the same set exactly (N_8 and π distribute over unions; π of an axis box is
  the box of the projected corners). No output had been produced. G2 independently tests π(N_8(X)) ⊆ N_3(π X) by direct
  materialisation on 23 samples.
- *Could each gate fail?* G1: yes (its control with ⌊(t+1)/3⌋ fails). G2: yes (N_2 in place of N_3 fails on all 320). G3: yes
  (81 in place of 2401 fails on all 240); and (a) is attained with equality on a sample (2482/2482), so it is sharp, not slack.
  G4: an equality test. G5: yes (the additive form fails at D = 20000: excess 3500081 > 3073362, reproducing REVIEW55's G-B).
  K1: a reproduction of HW's printed 6-figure values (tests the interval code). K3: its control at b = 1/10 fails as designed.
  K4: brute force. K5: control x = 3/4 fails. K2, K6, K7: records (K2/K6 carry only sanity gates), labelled CONFIRMATORY.

---

# PART A — W1: the spectator quantifier, and a second quantifier with the same defect

Conventions as HW §0/§30.1 and PLD §18-§19 (index convention of PLD §19: a level-m cube is an L^d block of level-m sites; a
level-m site is a level-(m−1) cube; 𝔏_m(𝒳) := the level-m links with both endpoint sites in cubes of 𝒳). "R-free" is HW
§30.1's (open column unconstrained). λ_f := 24θ(1 + 2Rg_K²) < 1 throughout (Part F re-derives this constant).

## A.1 The capped history spectators, as a class

**Definition (𝔖^cap_𝔥(k_0)).** For an admissible 𝔥 and k_0 ≥ 0, 𝔖^cap_𝔥(k_0) is the set of products
  **F_< = Π_{Q∈𝒬}F_Q,  𝒬 ⊂ 𝒰_0 ∪ 𝒰_1 ∪ ⋯ ∪ 𝒰_{k_0},**
  F_Q := e^{θX_Q}, X_Q := u_0Σ_{p⊂int Q}s(U_0(p))  (Q ∈ 𝒰_0: the factor of Φ_{−1}, reads U_0 on ℓ(Q));
  F_Q := e^{θmin{π_Q, Y^f_Q}}, π_Q = a_badu_{i+1}, Y^f_Q = 24u_{i+1}F^col_Q(U_i)  (Q ∈ 𝒰_{i+1}, 0 ≤ i ≤ k_0 − 1: the factor of
  Φ_i, reads U_i on 𝔏_i(col_i Q), PLD Lemma READ (i)).
So **Π_{k′<k}Φ_{k′} ∈ 𝔖^cap_𝔥(k)** (𝒬 = 𝒰_0 ∪ ⋯ ∪ 𝒰_k, HW TEL-f's Φ's) and **F_< ≡ 1 ∈ 𝔖^cap_𝔥(k_0)** (𝒬 = ∅). Sub-products are
admitted because they cost nothing and make the class closed under deleting factors.

**Lemma SPEC (three properties of the class): PROVEN-HERE (elementary).** Let F_< = Π_{𝒬}F_Q ∈ 𝔖^cap_𝔥(k_0).
- **(P-lo)** F_< ≥ 1.
- **(P-hi)** θX_Q ≤ λ_f·u_0Σ_{p⊂int Q}s(U_0(p)) (θ ≤ λ_f), and θmin{π_Q, Y^f_Q} ≤ θY^f_Q ≤ λ_f·𝔞^col_Q(U_i) with 𝔞^col_Q PLD
  §19.5's minimised column action (Lemma DOM′; REVIEW55 r55h-30 CONFIRMED it; its constant is re-checked in Part F).
- **(P-dis)** The chain terms entering distinct F_Q, Q ∈ 𝒬, are pairwise disjoint; and for a set A of level-k cubes with
  **[A ∩ A_k(𝔥) = ∅] or [A = 𝒰_k and 𝒬 ⊂ 𝒰_0 ∪ ⋯ ∪ 𝒰_{k−1}]**, no F_Q reads a link of 𝔏_i(col_i A) for any i ≤ k − 1 (and no
  term of 𝔞^col_Q is a term of A's columns).
- **Only clause (A2) of admissibility (HIST §7.1: "𝒰_k ∩ Σ(Ω^c_{k−1}) = ∅") is used, never (A1) (the size clause "more than
  n_♯ cubes").** (This is what Part D needs.)
*Proof.* (P-lo): each factor is ≥ 1. (P-hi): min ≤ second argument, and DOM′; for Q ∈ 𝒰_0 there is no infimum and θ ≤ λ_f.
(P-dis), first clause: HW Lemma DJ ("the term sets used by the bad windows of distinct pairs (k, Q), Q ∈ 𝒰_{k+1}, are
disjoint"), whose proof uses (A2), H-nest (i)-(iii) and nothing else. Second clause: a link read by F_Q (Q ∈ 𝒰_{i′+1}, or
Q ∈ 𝒰_0) has both endpoint sites in level-i′ cubes under Q; it lies in 𝔏_{i′}(col_{i′}A) only if some level-i′ cube lies under
both Q and a cube of A, i.e. only if π^{k−i′−1}(Q) ∈ A (resp. π^k(Q) ∈ A). *Case A ∩ A_k(𝔥) = ∅:* by the claim inside PLD
Proposition FAR (i) (CONFIRMED by REVIEW55 F8; re-derived: y ∈ 𝒰_j ⊂ Ω^c_j gives π(y) ∈ π(Ω^c_j) ⊂ Σ(Ω^c_j) ⊂ A_{j+1}(𝔥), and
π^{m−j}(y) ∈ Σ(Ω^c_{m−1}) ⊂ Ω^c_m (H-nest (i)) gives π^{m+1−j}(y) ∈ Σ(Ω^c_m) ⊂ A_{m+1}(𝔥)), every ancestor of a history cube lies
in A_m(𝔥), hence not in A; if i′ + 1 = k then Q ∈ 𝒰_k ⊂ N_1(𝒰_k) ⊂ A_k(𝔥), so Q ∉ A. *Case A = 𝒰_k:* DJ's second half ("Q′ ⊂
Ω^c_{k′+1} is not a descendant of Q") says no finer history cube lies under a cube of 𝒰_k. Neither step mentions component
sizes. ∎

## A.2 Every consumer of the F_<-quantified statements, read

`grep -n "F_<" HW.md` gives 13 lines: the definition (l.1483), the (E2^𝔉)/(E2^𝔉′) statements (l.1527, 1533, 2111, 2113), the
proof of CRC-2T (l.1584), Corollary CRC-HW (l.1618), and prose (§34, §37 table, §38, §40, §41). The consumers:

| consumer (locating string) | the F_< it passes | in 𝔖^cap? |
|---|---|---|
| Theorem CRC-2T′ (HW §36; proof §30.4 "(5) *Price the animal*": "F_< and 1_{E_Y} read levels ≤ m - 1") | its own F_<, unchanged, to (E2^𝔉′) at j = m − 1 ≥ k_0 | yes iff its callers' are |
| Corollary CRC-HW (HW §30.5: "μ^{(k)} = μ_{R(𝔥)} tilted by F_< := Π_{k′<k}Φ_{k′} (levels < k; Φ_{-1} reads U_0)") | Π_{k′<k}Φ_{k′}, with k_0 = k, to CRC-2T and to (E2^𝔉) at j = k, Γ = 𝒰_{k+1} | **yes** (𝒬 = 𝒰_0 ∪ ⋯ ∪ 𝒰_k) |
| (CRC)_k; RLARGE K8 / EXISTENCE single-cube (HW §36 "[RHW5-fix NIT, item 4.]") | F ≡ 1 | **yes** (𝒬 = ∅) |
| TEL-f's level-0 factor E_μ[Φ_{−1}] (HW §24.2) | none (μ^{(−1)} = μ) | yes |

**Verdict W1 (consumers): CONFIRMED — every instance any consumer passes lies in 𝔖^cap; no consumer needs the universal F_<.**
*One wrinkle, new:* at k = 0 Corollary CRC-HW passes F_< = Φ_{−1}, which reads U_0 = U_{k_0}, while §30.1 requires "a function of
U_0, …, U_{k_0−1}" (no fields at all when k_0 = 0). So the k = 0 instance was outside CRC-2T′'s stated hypothesis. CRC-2T′'s proof
uses the read levels only as "F_< … read levels ≤ m − 1" with m ≥ k_0 + 1 = 1, which Φ_{−1} satisfies, and TILT (ii) admits any
bounded function of the past fields; so stating the hypothesis as **F_< ∈ 𝔖^cap_𝔥(k_0)** covers it with no change of proof.

## A.3 Lemma LT — the fixed-volume Laplace test: what the restriction buys, and what the universal forms lose

**Lemma LT: PROVEN-HERE (elementary; not counted).** Fix K, the torus, the cutoff (any n ≥ 0 in place of n_♯), an admissible 𝔥,
R ∈ 𝔉_𝔥, k ≥ 1, a finite set A of level-k cubes with N_1(col_{k−1}A) R-free and [A ∩ A_k(𝔥) = ∅ or A = 𝒰_k], F_< ∈ 𝔖^cap_𝔥(k_0)
satisfying (P-dis) for A, and a set B of level-(k−1) cubes. Put ν := ν^{R,F_<}_{k−1}, w := h^{R,1}_{k−1}·1{B ∩ D_{k−1} = ∅},
Z_A := Π_{Q∈A}e^{θY^f_Q}. Let g_K → 0 along coupling sequences obeying (F_R) with fixed (β_±, R).
- **(a)** E_{ν^w}[Z_A] ≤ P(u_K) for a polynomial P that depends on the fixed data but **not on the cutoff n**. In particular
  limsup g_K²·log E_{ν^w}[Z_A] ≤ 0: the restricted statements cannot be refuted at fixed volume.
- **(b)** If F_< may be an arbitrary bounded measurable function of U_{<k_0} (k ≥ 2), or if the moment is F-conditioned with F
  an arbitrary bounded measurable function of the fields off the columns of A (k ≥ 1), there are instances with
  liminf g_K²·log(E_ν[Z_A·F·w]/E_ν[F·w]) > 0.
*Proof of (a).* (1) By HW Lemma TILT (ii) ("the same holds with finer spectators inserted in ν"), ν^w is the law of
(U_0, …, U_{k−1}) under the full chain W·1_R·F_<·1{B ∩ D_{k−1} = ∅}, normalised. (2) By (P-hi) and (P-dis),
Z_A·F_< ≤ exp(λ_fΣ_{Q∈A∪𝒬}𝔞_Q) ≤ e^{λ_f𝔄}, 𝔄 := u_0Σ_ps(U_0(p)) + Σ_{m<K}κu_mΦ_m(U_m, U_{m+1}) (PLD §19.3's chain action): each
𝔞_Q is at most the sum of its own terms at the actual fields, the term sets are disjoint, all terms are ≥ 0. (3) F_< ≥ 1.
Hence E_{ν^w}[Z_A] ≤ ∫W e^{λ_f𝔄} / ∫W·1_R·1{B good}. (4) W = e^{−𝔄}·𝔑 with 𝔑 = Π_{m,c}N_{m,c}^{−1},
N_{m,c} = ∫e^{−κu_mφ_{M̄_c}(V)}dV ∈ [c_0(κu_m)^{−3/2}, 1] (φ ≥ 0; on the Haar ball of radius (κu_m)^{−1/2} about the polar part of
M̄_c, κu_mφ ≤ ½); so 1 ≤ 𝔑 ≤ (Cu_max)^{3N_ℓ/2}, N_ℓ the number of links of levels ≥ 1, u_max ≤ u_K + β_+K log L + R.
(5) Numerator ≤ ∫e^{−(1−λ_f)𝔄}𝔑 ≤ (Cu_max)^{3N_ℓ/2}. (6) Denominator ≥ e^{−1}·Haar{𝔄 ≤ 1}: with E_0 := Σ_ps(U_0(p)) +
Σ_mκΦ_m (g-free), 𝔄 ≤ u_max E_0, and {E_0 = 0} (level-0 field flat, every coarser link at the polar part of its centre) carries
no defect at any level (centres of a flat field are flat); the defect sets are closed, so for u_K ≥ u_*(fixed data)
{E_0 ≤ 1/u_max} lies in an open neighbourhood of {E_0 = 0} free of defects — there 1_R = 1 for EVERY cutoff n ≥ 0 and B is
good; E_0 is analytic with a minimum at U ≡ 1, so {E_0 ≤ 1/u_max} contains a Haar ball of radius ≍ u_max^{−1/2}, volume
≥ c·u_max^{−D/2} (D = dimension). (7) Combine: E_{ν^w}[Z_A] ≤ e(Cu_max)^{3N_ℓ/2}u_max^{D/2}/c. ∎
*Proof of (b).* For F: Proposition F-UNIV below (k = 1). For F_< (k ≥ 2), REVIEW55 F6's mechanism made exact: let C be a
level-(k−2) configuration on col_{k−2}(Q) (Q ∈ A) carrying a small uniform abelian flux b in one plane, defect-free, whose kernel
centres on 𝔏 := 𝔏_{k−1}(col_{k−1}Q) are not column-flat (the linearised centre-plaquette functional of a uniform field is
9b = L²b ≠ 0, PLD §17.3 "B3, exact"; nonlinear corrections are O(b²)); F_< := 1{U_{k−2}|_{col_{k−2}Q} within δ of C}. Conditionally
on all other variables, U_{k−1}|_𝔏 has density ∝ Π_{c∈𝔏}k_c(·; M̄_c(U_{k−2}))·1_{R,k−1} (w does not read 𝔏 by Lemma BUF; F_< reads
U_{k−2}); on an η-ball about the centres there is no defect in Q's column, and 1_{R,k−1} is maximal there (adding defects only
enlarges components), so the conditional probability of the η-ball is ≥ its kernel probability ≥ 1 − poly·e^{−c(η)κu_{k−2}}. On
that ball F^col_Q ≥ c_1(b, η) > 0 (F^col_Q is continuous and vanishes only on column-flat fields, since a zero-energy completion
is a flat level-0 field with every link at its centre). So E_{ν^w}[Z_A] ≥ (1 − o(1))e^{24θu_kc_1}. ∎

**Reading.** At fixed volume the restricted forms carry no exponential-in-1/g² obstruction, for every cutoff; the universal
forms do. The dividing line is exactly the two properties (P-lo) "≥ 1: cannot condition on a rare event" and (P-hi) "dominated
by λ_f times the action of disjoint columns: cannot reward energy faster than the measure charges it". That is the precise sense
in which the restriction removes REVIEW55 F6's falsifier: **it does not apply to any member of 𝔖^cap.** (It is not a proof of
the restricted statements: Lemma LT is fixed-volume; the statements need constants uniform in volume, K, 𝔥, R — Part C.)

## A.4 Proposition F-UNIV — the conditioning function F has the same sup strength (NEW)

The statements REVIEW55 lists carry a SECOND free function besides F_<: the conditioning F in "every bounded measurable F ≥ 0 of
the level-≤(k−1) fields OFF the columns of A ∖ A′" ((CEM^{COL})_k, PLD §18.7.1), in NA-PRICE^{E+} (i)'s "every bounded measurable
F ≥ 0 of the level-≤(k-1) fields off the columns of S", in (LCR^act′) (PLD l.3228), in (ACT′)/(BCH-1) (via G = wF), and in the
F-conditioned forms REVIEW_PLD_S5 B3 asked for. sup_F E_ν[ZF]/E_ν[F] over all bounded F ≥ 0 measurable w.r.t. a σ-field 𝔊 is
ess sup E_ν[Z | 𝔊]: **a universal F turns each of these into a bound uniform in the boundary condition** — the bound PLD §19.6
itself calls refuted ("the uniform-in-boundary-condition bound that §18.7.2 (α) refutes", in its "What the charge must be"
paragraph). Nobody connected the two. It is false, exactly:

**Proposition F-UNIV: PROVEN-HERE (elementary; check na55_const K3, K4).** Let k = 1, A = {Q}, A′ = ∅, and let R ∈ 𝔉_𝔥 relax
the open columns of a neighbourhood of col_0(Q) (so the buffer is empty and N_1(col_0 Q) is R-free); ν any law of 𝔏^buf_1(R, A)
of the level-0 generator (ν = ν_0^w, ν_0 = Wilson·1_{R,0}, w = h^{R,1}_0; F_< ≡ 1 is forced at k_0 ≤ 0). Then there is an event
B, measurable w.r.t. the level-0 links with BOTH endpoints outside Q's level-0 block, with ν(B) > 0 and
  **E_ν[e^{θY^f_Q}·1_B]/E_ν[1_B] ≥ (1 − o(1))·e^{24θu_1c_B},  c_B > 0 independent of g.**
So (CEM^{COL})_1 as quantified is false for every θ > 0 and every choice of the law, and with it (ACT′)_1 (it implies (CEM^{COL})_1
by DOM′, PLD Proposition ACT-EQ (i)), (LCR^act′)_1 (it implies (ACT′)_1 by Theorem AT's identity), and (BCH-1)_1 for every charge
𝔟 satisfying (EQ-bc) with any B_0 (since (EQ-bc) forces 𝔟_Q ≥ E_λ[𝔞^col_Q | 𝔉_out] − B_0, which is ≥ c·u_0 on B).
*Proof.* Q's level-0 region is the block 𝔅 := [0, 8]⁴ of level-0 sites (a level-1 cube is 3⁴ level-1 sites = 3⁴ level-0 cubes of
3⁴ sites); F^col_Q(U_0) = Σ of the level-0 plaquettes with all four vertices in 𝔅 (HW §4: no infimum at level 0), and
F^col_Q(U_0) = 0 iff U_0 is flat on 𝔅 (𝔅 is simply connected).
(i) *Boundary data.* Let C be the U(1) ⊂ SU(2) configuration C_{x,1} = e^{−ibx_2σ_3}, C_{x,μ} = 1 (μ ≠ 1), 0 < b < 3/100: every
(1,2)-plaquette has holonomy e^{ibσ_3} (orientation fixed), every other plaquette is trivial. B := {U_0 within δ of C on every link
both of whose endpoints are outside 𝔅 and within ℓ^∞-distance 1 of 𝔅}. The free variables given B are the INSIDE links (both
endpoints in 𝔅) and the CROSSING links (one endpoint in 𝔅); write 𝒜(I) for the action of the plaquettes containing a free link.
(ii) *Flat interiors cost more (planar Stokes on 81 slices).* Fix (x_3, x_4) ∈ [0, 8]². In this (1,2)-slice the square [−1, 9]²
encloses 100 plaquettes: 64 with all vertices in 𝔅 and 36 in the annulus; all 100 contain a free link; its boundary loop γ uses
only links with both endpoints outside 𝔅 (na55_const K4: exactly (100, 64) in all 81 slices, no free (1,2)-plaquette off them,
loop links all outside-outside). If the interior is flat, the 64 inner plaquettes are trivial, and the lasso decomposition of the
holonomy of γ (a product of conjugates of the 100 plaquette holonomies) reduces to the 36 annulus ones, so with
‖1 − Π_iV_i‖ ≤ Σ_i‖1 − V_i‖ and ‖1 − gVg^{−1}‖ = ‖1 − V‖: Σ_{annulus}‖1 − U_p‖ ≥ ‖1 − hol(γ)‖ ≥ 2 sin(50b) − O(δ) (hol(γ) is
within O(δ) of e^{100ibσ_3}). For SU(2), s(U) = 1 − ½tr U = ½‖1 − U‖², so by Cauchy-Schwarz Σ_{annulus}s ≥ (2 sin 50b − O(δ))²/72.
Summing over the 81 disjoint slices: **min_{flat interiors}𝒜 ≥ 81·(2 sin 50b)²/72 − O(δ).**
(iii) *A curved interior costs less.* Completing by C itself (inside and crossing links = C): the only nontrivial plaquettes
containing a free link are the 100 (1,2)-plaquettes of each of the 81 slices, so 𝒜(C) = 81·100·(1 − cos b) + O(δ).
(iv) *Inequality.* (2 sin 50b)²/72 > 100(1 − cos b) for 0 < b < 3/100: with sin x ≥ x − x³/6 and 1 − cos x ≤ x²/2 it reduces to
(1 − 2500b²/6)² > 0.36, i.e. b² < 0.00096; checked with rigorous enclosures at b = 1/1000, 1/100, 3/100, and failing at b = 1/10
as a control (K3).
(v) *Laplace, elementary.* Given an outside configuration in B̄, the conditional law of the free variables has density
∝ e^{−u_0𝒜(I)}·ρ(I) with 0 ≤ ρ ≤ 1 (the constraint 1_{R,0} and nothing else: w and 1_B do not read free links), ρ = 1 on a
neighbourhood of the minimisers of 𝒜 (compactness; b is fixed, the minimisers' plaquettes are ≤ O(b), and the n_♯-cluster
constraint is satisfied by any configuration with finitely many local defects for every cutoff n ≥ 0 when b < ε_1, or for
n ≥ |𝔅| otherwise — take b < ε_1). Let A_c := min{𝒜 : F^col_Q ≤ c}; by (ii)-(iv) and compactness, A_c > min 𝒜 + 2η for some
c, η > 0 (the sets {F^col_Q ≤ c} decrease to the flat interiors). Then P(F^col_Q ≤ c | outside) ≤ e^{−u_0(A_c − min𝒜 − η)}/v(η)
→ 0, v(η) the (g-free) Haar volume of {𝒜 ≤ min𝒜 + η}. Hence E[e^{θY^f_Q} | outside] ≥ (1 − o(1))e^{24θu_1c} uniformly on B̄,
and integrating over B against w: the claim with c_B := c. ∎
*Why this is not REVIEW55 F6 again.* F6 is about F_<, the spectator inside the LAW; F-UNIV is about F, the conditioning function
in the STATEMENT. Restricting F_< does not touch F. **So the repair REVIEW55 names is necessary but not sufficient for
(CEM^{COL}), (ACT′), (LCR^act′), (BCH-1) and NA-PRICE^{E+}'s F-conditioned form: their F must be restricted too.**

**Corollary F-UNIV′ (the F-conditioned (SDP) is false too): PROVEN-HERE given PLD p5 B3's exact linear-order value.** With the
same B, b fixed, the level-1 kernel centres over Q carry curvature ≈ 9b ≫ ε_1 if b > ε_1/8 (p5 B3; take ε_1 < b < 3/100 here —
the defect clusters this creates are local, of bounded size, allowed for every cutoff n ≥ 3⁴), so Q ∈ D_1 with conditional
probability → 1: Theorem NA-PRICE^{E+}'s conclusion E_ν[1{S ⊂ D_k}F] ≤ (C_Ae^{−a_Au_k})^{|S|}E_ν[F] fails for universal F, and so
does the F-conditioned form REVIEW_PLD_S5 S5-20/B3 asked for ("for F measurable on the other columns"). (Its implication from
(CEM^{COL}) is valid; its hypothesis is false.)

**What the consumers actually pass as F, and whether that is safe.**
| statement | consumer and its F | safe? |
|---|---|---|
| (CEM^{COL})_k | NA-PRICE^{E+} step (4): F′ = Π_{Q∈T}1{Q ∉ 𝒞_k}·F, and NA-PRICE^{E+} is called with F := 1 by Cor. E2-RED | **yes, after one edit**: F′ ≤ 1 may be dropped BEFORE the moment (E_{ν′}[Π_{S∖T}e^{θY^f}F′] ≤ E_{ν′}[Π_{S∖T}e^{θY^f}]), so only F ≡ 1 is consumed |
| (CEM^{COL})_{j+1} | Cor. E2-RED (D1): **F := 1{Y ⊔ x(Γ_1) ⊂ D_j}** — defects of cubes ρ-attached to, or in columns adjacent to, the columns of Γ_0 | **no**: conditioning on a rare event next to a column; at fixed volume the conditional law concentrates on the action-minimisers of the event, whose curvature leaks into the adjacent column (the coherent part of the Gaussian regression of a level-j curvature functional is never zero in 4D) — **ARGUED, not proven here**; in any case it is an instance of the universal statement F-UNIV refutes, so E2-RED **as written has no valid input**. Repaired in A.5 by Hölder (E2-RED^H) and avoided altogether on route (4°) (B.2) |
| (SDP)^A F-conditioned | Prop. CD (b) (§17.4), the (J-NS^cd) route | off the route of record (CD (b) dead, (NP-F6)) |
| (SF-cap)^{COL}, (J-NS^cd) | Prop. ONE (a)-(b), NA-PRICE^E (i) | off the route of record; inherit the same F-quantifier |
*[Wording correction to A.4 (v) and Corollary F-UNIV′, appended 00:05 UTC; the text above is left as written.]* In (v) read:
"take 0 < b < ε_1: then no plaquette near 𝔅 reaches ε_1 at level 0 on the relevant configurations, 1_{R,0} = 1 there for every
cutoff n ≥ 0, and (ii)-(iv) hold because their reduction is valid for every 0 < b < 3/100". The phrase "or for n ≥ |𝔅|
otherwise" is withdrawn. In F-UNIV′ read "ε_1/8 < b < ε_1": no level-0 defect occurs; the level-1 defects the forced centres create
lie in N_1(Q), whose level-1 pairs are unconstrained because N_1(col_0 Q) is R-free and π(N_1(col_0 Q)) = N_1(Q) (check G4), so
the constraints do not see them, for every cutoff.

## A.5 The restated statements (each: text, consumer, falsifier, what is delivered)

Throughout: "uniform in the cutoff" means the statement is asserted for every n ≥ 0 in place of n_♯ (the history class and the
constraint family R_{S,E} built with n) with the SAME constants (Part D). 𝔖^cap_𝔥(k_0) is A.1's class.

**(E2^𝔉′_res)_{θ,ρ} [OPEN; owner node A; replaces HW §37's (E2^𝔉′)].** HW §37's statement verbatim except: (i) "every bounded
measurable F_< ≥ 0 that is a function of U_0, …, U_{k_0−1} (universally quantified …)" → **"every F_< ∈ 𝔖^cap_𝔥(k_0)"**;
(ii) "every level j ≥ max{k_0, 1}" → **"every level j ≥ k_0"** (the j = 0 instance is the level-0 clause, B.3); (iii) the
constants C_fc, C_A, a_A ≥ θa_bad, c_A independent of g, K, T, 𝔥, the pattern **and the cutoff**. Kept: R ∈ 𝔉_𝔥; Γ ⊂ level j+1
with Γ ∩ A_{j+1}(𝔥) = ∅ or Γ = 𝒰_{j+1}; Y ⊂ level j outside col Γ with N_1(col Γ ∪ Y) R-free; ν = ν^{R,F_<}_j;
w = h^{R,1}_j·1{Buf^R_ρ(col Γ ∪ Y) ∩ D_j = ∅};
  E_{ν^w}[Π_{Q∈Γ}e^{θmin{π_Q,Y^f_Q}}·1{Y ⊂ D_j}] ≤ C_fc^{|Γ|}(C_Ae^{−a_Au_j})^{|Y|}e^{c_A‖col Γ ∪ Y‖_sh}.
*Consumer:* CRC-2T′ step (5) and Corollary CRC-HW (A.2) — inside the range. *Falsifier:* F6's mechanism needs F_< ∉ 𝔖^cap
(Lemma LT); the statement has no free conditioning function. *Delivered:* j ≥ max{k_0, 1} by Corollary E2-RED^H below; j = 0
OPEN on this route (B.3).

**𝔏^buf_res,k(R, A) [definition; replaces PLD §18.7.0].** For R ∈ 𝔉_𝔥, k ≥ 1 and a finite set A of level-k cubes with
[A ∩ A_k(𝔥) = ∅ or A = 𝒰_k], the laws on (U_0, …, U_{k−1}) obtained by: (1) the past law ν^{R′,F_<}_m of levels ≤ m of R′ = R with
finitely many cubes of A ∪ col_{k−1}(A) declared, with **F_< ∈ 𝔖^cap_𝔥(k_0), k_0 ≤ k, satisfying (P-dis) for A**; (2) the weight
w = h^{R,1}_m·1{B ∩ D_m = ∅}, B any set of non-R-free level-m cubes; (3) the marginal on U_{≤k−1}; with two generator types:
**(G-k)** m = k, hypothesis N_1(A) R-free (Lemma BUF at level k, then COL-DEC's first clause for the marginal — REVIEW55 F4 (D2));
**(G-k−1)** m = k − 1, hypothesis N_1(col_{k−1}A) R-free (Lemma BUF at level k − 1; this is PLD s7's (RING-cc), since
π(N_1(col_{k−1}A)) = N_1(A), check G4). *Changes against PLD:* F_< restricted (and allowed to contain Φ_{k−1} when (P-dis)
permits — needed at j = k_0); PLD s7's blanket (RING-cc) replaced by the generator-specific ring (F4: the closed ring is needed only
for (G-k−1)); B arbitrary (E2-RED's buffer is the patch's, not A's); PLD's "A ∩ 𝒰_k = ∅" replaced by the Γ-clause — **Cor. E2-RED's
Γ = 𝒰_{j+1} case applies (CEM^{COL})_{j+1} with A ⊂ 𝒰_{j+1}, which PLD's clause forbids** (a small new finding; harmless, since
PLD's clause is used only through GEO (iv), i.e. only when Φ_{k−1} is in the law).

**(CEM^{COL}_res)_k [OPEN; owner node A; replaces PLD §18.7.1].** There are c_cem < ∞ and c_A ≥ 0, independent of g ≤ g_0, k, K,
T, 𝔥, R, A, A′, F_< **and the cutoff**, such that for every admissible 𝔥, R ∈ 𝔉_𝔥, k ≥ 1, A, A′ ⊂ A and ν ∈ 𝔏^buf_res,k(R, A):
  **E_ν[Π_{Q∈A∖A′}e^{θY^f_Q}] ≤ c_cem^{|A∖A′|}·e^{c_A‖col_{k−1}(A∖A′)‖_sh},   24θ(1 + 2Rg_K²) < 1.**
**No conditioning function** (F ≡ 1). [Optional strengthening that passes both tests of Part C: F a product of no-defect and
no-bad-centre indicators of cubes off col(A ∖ A′) — symmetric convex events in the linear model. No consumer needs it.]
*Consumers:* NA-PRICE^{E+}_res (below), Corollary E2-RED^H (rates pθ and θ′), and on route (4°) the whole interface (B.2).
*Falsifiers:* F6 — excluded (Lemma LT (a)); F-UNIV — excluded (no F). *Status:* OPEN (Part C).

**NA-PRICE^{E+}_res (i) [CONDITIONAL ⇐ (CLS-min) + (CEM^{COL}_res)_k at a rate θ′; implication PROVEN-HERE as a one-line edit of
PLD §18.7.1's proof].** Standing setting of PLD §18.0. For every admissible 𝔥, R ∈ 𝔉_𝔥, k ≥ 1, S level-k with N_1(S) R-free and
S ∩ A_k(𝔥) = ∅, F_< ∈ 𝔖^cap_𝔥(k_0), k_0 ≤ k, and ν = ν^w the (G-k) law before the marginal:
  E_ν[1{S ⊂ D_k}] ≤ (C_Ae^{−a_Au_k})^{|S|}e^{c_A‖col_{k−1}S‖_sh},  a_A := min{λκε_1²/256, 6θ′a_bad},
  C_A := 2max{n_int(1 − λ)^{−3/2}e^{λκε_1²R/256}, c_cem(θ′)}.
*Proof.* PLD §18.7.1 steps (1)-(3) verbatim with F := 1 (FT^far, KD, CW; F_< reads levels ≤ k − 1, which FT^far's step 2
excludes). Step (4): drop F′ = Π_{Q∈T}1{Q ∉ 𝒞_k} ≤ 1 BEFORE the moment, then (CEM^{COL}_res)_k with A := S, A′ := T for the COL-DEC
marginal of ν′, which is a (G-k) law (COL-DEC's first clause: G′ = Φ_{k−1}·H′ does not read L^∂_{k−1}(S); Φ_{k−1} by GEO (iv),
S ∩ 𝒰_k = ∅ — this is where k_0 = k is admitted). Step (5) verbatim. ∎ *Only F ≡ 1 is consumed*; the F-conditioned conclusion
of PLD's statement is false for universal F (Corollary F-UNIV′) and is withdrawn.

**(ACT′_res)_k and (LCR^act′_res)_m [OPEN; node A].** PLD §19.5's (ACT′) and §19.4-§19.5's (LCR^act′) with: F_< ∈ 𝔖^cap_𝔥(k_0)
(P-dis for S); the weight w of 𝔏^buf_res (no F: G := w); constants (c_act, resp. B) uniform in the cutoff:
  (ACT′_res) E_{ν_0}[e^{λ_f𝔞^col_S}·w] ≤ c_act^{|S|}E_{ν_0}[w];  (LCR^act′_res) E_{λ,w}[𝔞^col_S] ≤ B|S| for all λ ∈ [0, λ_f].
*Consumers:* (ACT′_res) ⇒ (CEM^{COL}_res) by DOM′ (PLD Proposition ACT-EQ (i), CONFIRMED r55h-30); (LCR^act′_res) ⇒ (ACT′_res) with
log c_act = λ_fB by Theorem AT's identity. Both consumers are inside the range. *Falsifiers:* excluded as for (CEM^{COL}_res).
*Not past any impossibility* (REVIEW55 F11 stands): they are well-posed OPEN statements, equivalent in kind to (CEM^{COL}_res).

**(EQ-bc) + (BCH-1), restated honestly.** With F ≡ 1 and F_< restricted, and with the charge DEFINED (REVIEW55 F10 (c): with an
existential charge (EQ-bc) is vacuous) as 𝔟_Q := sup_{λ∈[0,λ_f]}E_λ[𝔞^col_Q | 𝔉_out] (𝔉_out including the outside DEFECTS, because
the column's conditional law carries the n_♯-cluster indicator, REVIEW55 F10 (a)):
  (BCH-1_res) E_{λ,w}[Σ_{Q∈S}𝔟_Q] ≤ B_1|S| for all λ ∈ [0, λ_f], constants uniform in the cutoff.
It implies (LCR^act′_res) (tower property) and is a sup-strengthening of it. **No residual smaller than the weighted-law statement
is isolated by (EQ-bc)/(BCH-1)** — agreeing with REVIEW55 F10.

**Corollary E2-RED^H (the Y-route repair of Cor. E2-RED, by Hölder instead of conditioning): CONDITIONAL ⇐ (CLS-min) +
(CEM^{COL}_res)_{j+1} at rate pθ + (CEM^{COL}_res)_j at rate θ′; implication PROVEN-HERE.** Let 1/p + 1/q = 1,
24pθ(1 + 2Rg_K²) < 1, 24θ′(1 + 2Rg_K²) < 1, and a_A := min{λκε_1²/256, 6θ′a_bad} ≥ qθa_bad. Then (E2^𝔉′_res) holds at every
j ≥ max{k_0, 1} with
  **C_fc^H := c_cem(pθ)^{1/p} + 81C_A^{1/q}e^{θa_badR},  C_A^H := C_A^{1/q},  a_A^H := a_A/q ≥ θa_bad,  c_A^H := c_A.**
*Proof.* (1) Pointwise (HW Lemma CAP (ii)-(iii), as in E2-RED): Π_{Q∈Γ}e^{θmin{π_Q,Y^f_Q}} ≤ Σ_{Γ_0⊔Γ_1}Σ_xΠ_{Γ_0}e^{θY^f_Q}·
Π_{Γ_1}e^{θπ_Q}·1{x(Γ_1) ⊂ D_j} (81^{|Γ_1|} choice functions; 1_{G_Q} ≤ 1 dropped); multiply by 1{Y ⊂ D_j}, the buffer staying in
w. (2) For fixed (Γ_0, Γ_1, x), S := Y ⊔ x(Γ_1), Hölder: E_{ν^w}[Π_{Γ_0}e^{θY^f}·1{S ⊂ D_j}] ≤ E_{ν^w}[Π_{Γ_0}e^{pθY^f}]^{1/p}·
ν^w(S ⊂ D_j)^{1/q}. (3) First factor: (CEM^{COL}_res)_{j+1} at rate pθ with A := Γ, A′ := Γ_1, law ν^w of type (G-j) [N_1(col_jΓ)
R-free is HW's hypothesis; the Γ-clause and (P-dis) hold; F_< reads levels ≤ k_0 − 1 ≤ j − 1]: ≤ c_cem(pθ)^{|Γ_0|/p}·e^{c_A‖col Γ‖_sh/p}.
(4) Second factor: NA-PRICE^{E+}_res at level j for S (N_1(S) ⊂ N_1(col Γ ∪ Y) is R-free; S ∩ A_j(𝔥) = ∅: a non-R-free cube is not
in A_j(𝔥) by persistence, and col_j(Γ) ∩ A_j(𝔥) = ∅ since π(A_j(𝔥)) ⊂ A_{j+1}(𝔥), resp. by (A2) for Γ = 𝒰_{j+1}): ≤
(C_Ae^{−a_Au_j})^{|S|/q}·e^{c_A‖col_{j−1}S‖_sh/q}. (5) Per Q ∈ Γ_1: 81·e^{θa_bad(u_j + R)}C_A^{1/q}e^{−(a_A/q)u_j} ≤
81C_A^{1/q}e^{θa_badR} (a_A/q ≥ θa_bad); per y ∈ Y: C_A^{1/q}e^{−(a_A/q)u_j}; summing the 2^{|Γ|} partitions gives (C_fc^H)^{|Γ|}.
The allowances combine to ≤ e^{c_A‖col Γ ∪ Y‖_sh} (monotonicity, PLD PATCH (i), and ‖col_{j−1}S‖_sh ≤ 16‖S‖_sh + 66|S| from
Part E absorbed into the per-cube constants when c_A > 0; c_A = 0 needs none of this). ∎
*Price* (check K7): θ ≤ min{1/(24p(1 + 2Rg_K²)), 1/(4q(1 + 2Rg_K²))}; best at p = 7/6, q = 7: **θ ≤ 1/28** (against 1/24),
κ ≥ 1/14045 = 7.12·10⁻⁵ at λ = ½, θ = 1/28 (the same κ_crit PLD p6 C2 records for θ = 1/24 there). g-independent; a = θa_bad
falls by 24/28. **E2-RED as written is not repaired by restricting F_<; E2-RED^H is the repair on the Y-route; route (4°) (B.2)
needs neither.**

**Corrected text for the cross-references (none edited here; requests in "For the lead").**
- PLD §18.6.2 Delta 3 and §18.9 M-7: "F_< is FREE … universally quantifiable at zero cost" → "F_< ranges over the capped history
  spectators 𝔖^cap_𝔥(k_0); the universal form is false (REVIEW55 F6; Lemma LT (b)). Free on the law-conversion side, NOT on the
  bound side." The same for §18.12 request 3 and §19.4's (LCR^act′) quantifier "every bounded measurable F_< ≥ 0 of U_{<k_0}".
- HW §37, (E2^𝔉′)'s fifth bullet: "every F_< ∈ 𝔖^cap_𝔥(k_0) (sub-products of Π_{k′<k_0}Φ_{k′}, the capped history spectators)".
  HW §37's D3 row: "ANSWERED: restricted to the capped spectators (the universal form is false)". HW §41 M-7: withdrawn as "DONE".
- HW §38 item 5: "[RHW5-fix E2-2] applied as REVIEW_HW_S5 stated it (the capped product), not reversed" (REVIEW55 r55h-47).
- PLD §18.7.1 Cor. E2-RED and Proposition ONE (d): "(E2^𝔉′) ⇐ (CEM^{COL})" holds only via E2-RED^H (rates pθ and θ′, θ ≤ 1/28),
  not via the F-conditioned (D1).
*[Correction to E2-RED^H's allowance bookkeeping, appended 00:06 UTC; the text above is left as written.]* NA-PRICE^{E+}_res
carries the allowance of the FULL column, e^{c_A‖col_{j−1}(S∖T)‖_sh} ≤ e^{81c_A(|S| + ‖S‖_sh)} (HW Lemma COL′'s first inequality,
whose proof uses no connectedness), not a push-down allowance; the reference to Part E in step (5) is withdrawn. With
‖S‖_sh ≤ ‖col Γ ∪ Y‖_sh (monotonicity), the allowance of (E2^𝔉′_res) delivered by E2-RED^H is **c_A^H := c_A/p + 81c_A/q**, and
the per-cube factor e^{81c_A/q} goes into C_A^H := (C_Ae^{81c_A})^{1/q}. At c_A = 0 (the value every node-A route so far aims at)
nothing changes.

---

# PART B — W2: the edges, on the current route and on a route that removes them

## B.1 j = k_0 on the current (Y-) route: recovered by the restriction — PROVEN-HERE (as an implication)
REVIEW55 F5 (iii)(b): E2-RED needs NA-PRICE^{E+} at level j inside a law whose F_< must read levels ≤ j − 2 (PLD l.2446 "k_0 ≤ k −
1"); with F_< reading U_{<k_0} and j = k_0 that fails. With F_< ∈ 𝔖^cap_𝔥(k_0) and j = k_0, the only factors of F_< reading
U_{j−1} are those of Φ_{j−1}, on the columns of 𝒰_j. Walk of E2-RED^H at j = k_0, step by step:
- (D1) is (CEM^{COL}_res)_{j+1} with F_< reading levels ≤ j − 1 = (j + 1) − 2: the old condition holds; nothing to check.
- (D2) is NA-PRICE^{E+}_res at level j with Φ_{j−1} in the law. Step (1), FT^far: "the only factors reading U_k on ℓ(S) are the
  kernel factors … Φ_{k′}, k′ < k, read levels < k" — Φ_{j−1} reads level j − 1 ✓. Steps (2)-(3): pointwise ✓. Step (4):
  COL-DEC's first clause — "G′ := Φ_{k-1}·H′ … does not read U_{k-1} on L^∂_{k-1}(S)" — is exactly the k_0 = k case (PLD §17.2
  wrote its law with Π_{k′<k}Φ_{k′}); its Φ_{k−1}-part is GEO (iv), which needs S ∩ 𝒰_j = ∅, true (A.5 step (4)). Then
  (CEM^{COL}_res)_j with Φ_{j−1} ∈ F_<: admitted by 𝔏^buf_res because (P-dis) holds for A = S (S ∩ A_j(𝔥) = ∅). Step (5) ✓.
**So E2-RED^H delivers (E2^𝔉′_res) at every j ≥ max{k_0, 1}: REVIEW55 r55h-19's "j = k_0 returns once F_< is restricted" is
CONFIRMED.** The only level left out on this route is j = 0 (B.3).

## B.2 Route (4°): an interface with no Y, no buffer, no (S1), no level-j (SDP), and no j = k_0 edge — PROVEN-HERE (implications)

The Y-decomposition of Theorem CRC-2T's step (4) is what makes the node-A input carry a defect probability (the factor
(C_Ae^{−a_Au_j})^{|Y|}), hence (SDP) at level j, hence the j = k_0 edge and the (0b) level-0 (SDP). It can be replaced by relaxing
a FIXED neighbourhood, paid by the same induction hypothesis.

**Definition (E2^{𝔉°})_{θ,ρ} [OPEN; owner node A; the Y = ∅ instance of (E2^𝔉′_res)].** There are C_fc, c_A, independent of g,
K, T, 𝔥, the pattern and the cutoff, such that for every admissible 𝔥, R ∈ 𝔉_𝔥, every level j ≥ k_0 (j = −1: the level-0 window,
B.3), every finite Γ ⊂ level j + 1 with [Γ ∩ A_{j+1}(𝔥) = ∅ or Γ = 𝒰_{j+1}] and **N_ρ(col_jΓ) R-free** (ρ = 8), and every
F_< ∈ 𝔖^cap_𝔥(k_0), with ν := ν^{R,F_<}_j and w := h^{R,1}_j (no buffer factor: it is identically 1 here):
  **E_{ν^w}[Π_{Q∈Γ}e^{θmin{π_Q, Y^f_Q}}] ≤ C_fc^{|Γ|}·e^{c_A‖col_jΓ‖_sh}.**
*It is a special case of (E2^𝔉′_res)*: take Y = ∅ and R with N_8(col_jΓ) R-free; then N_1(col Γ) is R-free and
Buf^R_8(col Γ) = ∅ (no non-R-free cube within distance 8), so the buffer indicator is 1. **So route (4°) asks strictly less of
node A than the current route.**

**Corollary E2-RED° (PROVEN-HERE, one line):** for j ≥ 0, (E2^{𝔉°})_j ⇐ (CEM^{COL}_res)_{j+1} with C_fc := c_cem, same c_A:
min{π_Q, Y^f_Q} ≤ Y^f_Q pointwise, and the law ν^w is a (G-j) law of 𝔏^buf_res,j+1(R, Γ) (N_1(col_jΓ) ⊂ N_8(col_jΓ) is R-free;
F_< reads levels ≤ k_0 − 1 ≤ j − 1; (P-dis) by Lemma SPEC). **No (CLS-min), no CW, no KD, no NA-PRICE^{E+}, no Hölder, no
F-conditioning, and the rate is θ itself.** (CEM^{COL})'s defect tolerance is what makes the CAP-dec split unnecessary.

**Theorem CRC-2T° ((CRC) for 𝔉_𝔥 from (E2^{𝔉°}); CONDITIONAL; implication PROVEN-HERE as a modification of HW §30.4/§36).**
Assume (F_R) (lower half and u_m ≤ u_{m−1} + R) with g_K² ≤ 1/(2R), SU(2), bad-only history-independent defects, (CLS-min),
max{6θ, 24θ}(1 + 2Rg_K²) < 1, (E2^{𝔉°})_{θ,8}, and, for some c_U ∈ (0, 1],
  **(S2°)** ε_2° ≤ ½ and 2ε_2° ≤ c_U,   **(T°)** (n_♯ + 1)·aβ_−log L ≥ b_D°,
  b_n° := 12401c_U + 810162c_A,  b_D° := 10000c_U + 810000c_A,  C_ℓ := (1 − λ_*)^{−3n_int/2}C_fc,  a := θa_bad,
  ε_2° := 6400^{n_♯}(C_ℓe^{b_n° + aR}e^{−a/g_K²})^{n_♯+1}.
Then for every admissible 𝔥, every F_< ∈ 𝔖^cap_𝔥(k_0), every R ∈ 𝔉_𝔥 and every upward-closed 𝒞′ at levels ≥ k_0 + 1:
  **ρ^F_R(𝒞′) ≤ exp(2ε_2°·#_R(𝒞′)) ≤ exp(c_U·#_R(𝒞′)).**  **No (S1).**
*Proof.* Induction on N(R), exactly as HW §30.4; steps (1), (2), (7), (8) verbatim. Steps (3)-(6) are replaced by:
- **(3°) Relax a fixed neighbourhood of the animal's column.** With m := m_t, X := col_{m−1}(𝒟) and 𝒞″ := Col(N_8(X)) (upward
  closed, levels ≥ m ≥ k_0 + 1): **[𝒟] ⊂ 𝒞″** (for x ∈ 𝒟 and any child y of x, (m, x) = (m, π(y)) and (m + r, π^r x) =
  (m + r, π^{r+1}y); check G3 (b)), so R⁗ := R_{t−1}^{−𝒞″} ∈ 𝔉_𝔥 relaxes everything step (3) relaxed and more; 1_{R_{t−1}} ≤
  1_{R⁗} ((m1)), and the induction hypothesis at R_{t−1} (N(R_{t−1}) ≤ N(R) − 1) gives
    μ^F_{R_{t−1}}(𝒟 ⊂ D_m) ≤ ρ^F_{R_{t−1}}(𝒞″)·μ^F_{R⁗}(𝒟 ⊂ D_m) ≤ e^{c_U|𝒞″|}μ^F_{R⁗}(𝒟 ⊂ D_m).
- **(4°) The count.** Since |⌊u/3⌋ − ⌊v/3⌋| ≤ ⌊(|u − v| + 2)/3⌋ (check G1; this is sharper than the ⌊|u − v|/L⌋ + 1 used in
  HW SH-2), π(N_8(X)) ⊂ N_3(π X) = N_3(𝒟) and π(N_3(B)) ⊂ N_1(πB) (check G2); with π(N_1 B) ⊂ N_1(πB), the level-(m − 1 + r) part
  of 𝒞″ lies in N_3(𝒟) (r = 1) and in N_1(π^{r−1}𝒟) ⊂ Σ^{r−1}(𝒟) (r ≥ 2, HW Lemma SH-1). Hence
    |𝒞″| ≤ 2401n + Σ_{s=1}^{M}|Σ^s(𝒟)| = 2400n + ‖𝒟‖_sh ≤ **12401n + 10000M**  (n = |𝒟| = n_♯ + 1, M = K − 1 − m;
  HW Corollary H-geo′ for ‖𝒟‖_sh; check G3 (a), (c): 0 violations in 240 samples, (a) attained with equality).
- **(5°) Price the animal at R⁗.** HW step (5) verbatim with R″ → R⁗ and Y = ∅: Lemma CH + CAP (ii)-(iii) pointwise; the mismatch
  peel (every cube of 𝒟 is R⁗-free and (m, x) ∉ S_{R⁗} for x ∈ 𝒟, because [𝒟] ⊂ 𝒞″ — the two properties [RHW5-fix NIT] (b)
  separates; F_< reads levels ≤ m − 1); Lemma KS (c); TILT (ii) at level m − 1; then (E2^{𝔉°}) with Γ = 𝒟 (𝒟 ⊂ S^{(m)}_{R_{t−1}} ⊂
  S^{(m)}(𝔥), so 𝒟 ∩ A_m(𝔥) = ∅), j = m − 1, R = R⁗ (N_8(col 𝒟) is R⁗-free by construction):
    μ^F_{R⁗}(𝒟 ⊂ D_m) ≤ (C_ℓe^{−au_m})^n·e^{c_A‖col 𝒟‖_sh},  ‖col 𝒟‖_sh ≤ 81(10002n + 10000M) (HW Lemma COL′).
- **(6°) Collect.** μ^F_{R_{t−1}}(𝒟 ⊂ D_m) ≤ (C_ℓe^{b_n°}e^{−au_m})^n·e^{b_D°M}; there is no Y-sum and hence no (S1).
Step (7) with b_D°, (T°) and u_m ≥ u_K + β_−(K − m)log L − R gives p_t ≤ ε_2° (the factor 2 of HW's ε_2, which came from the
Y-sum's 2^n, is gone); step (8) closes with (S2°). ∎
*Why this is legitimate and was not available "for free" before:* the relaxation 𝒞″ is a fixed set (not configuration-dependent),
upward closed, at levels ≥ k_0 + 1, and bought from the induction hypothesis at a pattern with strictly fewer constrained pairs —
the same non-circularity HW §36 records for its own steps. What it costs is a per-animal count, 2401n + ‖𝒟‖_sh − n, which the
animal's n prices beat exactly as they beat HW's own allowance.

**Corollary CRC-HW° ((M-f^cap) on route (4°); CONDITIONAL; implication PROVEN-HERE).** Under CRC-2T°'s hypotheses, for every
admissible 𝔥: (M-f^cap) under μ_{R(𝔥)} holds with
  **C_fc′ := C_fc·e^{2401c_U + 81c_A},  c_f° := c_U + 81c_A**   (against HW's C_fc′ = 2C_fc e^{6561c_+}, c_f = 6561(c_A + 17c_U)).
*Proof.* TEL-f (finer-first) as HW §30.5. For k ≥ 0: E_{μ^{(k)}}[Φ_k] = E_ν[Φ_kh]/E_ν[h] (TILT (ii); ν = ν^{R(𝔥),F_<}_k,
F_< = Π_{k′<k}Φ_{k′} ∈ 𝔖^cap_𝔥(k), h = h^{R(𝔥),1}_k). With 𝒞°_k := Col(N_8(col_k 𝒰_{k+1})) and h° := h^{R(𝔥)^{−𝒞°_k},1}_k ≥ h
pointwise: E_ν[Φ_kh] ≤ E_ν[h°]·E_{ν^{h°}}[Φ_k] and E_ν[h°]/E_ν[h] = ρ^F_{R(𝔥)}(𝒞°_k) ≤ e^{c_U|𝒞°_k|} (CRC-2T°, k_0 = k; the past
constraints coincide). (E2^{𝔉°})_k with Γ = 𝒰_{k+1}, R = R(𝔥)^{−𝒞°_k}: E_{ν^{h°}}[Φ_k] ≤ C_fc^{|𝒰_{k+1}|}e^{c_A‖col_k𝒰_{k+1}‖_sh}.
Counting as in (4°): |𝒞°_k| ≤ 2400|𝒰_{k+1}| + ‖𝒰_{k+1}‖_sh, and ‖col_k𝒰_{k+1}‖_sh ≤ 81(|𝒰_{k+1}| + ‖𝒰_{k+1}‖_sh). For k = −1:
E_μ[Φ_{−1}] with 𝒞°_{−1} := Col(N_8(𝒰_0)), CRC-2T° at k_0 = 0 with F ≡ 1, |𝒞°_{−1}| ≤ 2401|𝒰_0| + ‖𝒰_0‖_sh, and (E2^{𝔉°})_{−1}
(the level-0 window, B.3). Summing over levels with Σ_k‖𝒰_{k+1}‖_sh + ‖𝒰_0‖_sh ≤ s(𝔥) (union ≤ sum over components). ∎

**Consequences of route (4°), each by the proofs above.**
1. **The node-A input of the whole HW route is (CEM^{COL}_res)_k for k ≥ 1 plus the level-0 window** (B.3). (SDP)^A, NA-PRICE^{E+},
   (CLS-min)-on-node-A's-side, KD, CW, MD and every F-conditioned statement leave the HW route. (HW still uses (CLS-min) for
   Lemma W-bad in its own step (5°).)
2. **The j = k_0 edge does not arise**: (E2^{𝔉°})_j ⇐ (CEM^{COL}_res)_{j+1}, whose F_< reads levels ≤ (j + 1) − 2.
3. **No (S1), no c_att, no Y-sum, no buffer.** (W-𝔉)'s "screening by a good buffer" becomes "the weight is blind to N_8 of the
   column".
4. **Constants** (check K2, informational: none of these decides anything, REVIEW55 F1): at c_U = 1, c_A = 0 (HW §35.7's convention):
   b_n° = 12401, b_D° = 10000, c_f° = 1; g²_CRC° = a/(b_n° + ln 6400) = 8.0582·10⁻⁹¹; n_T° = 4.894·10⁹⁰ < n_H, so (T°) adds nothing;
   the binding ceiling becomes HIST-sum at B_0 = c_f° + 2 = 3: **8.6760·10⁻⁹² (HIST as written; +2.94 decades above 10⁻⁹⁴, +60.54
   above 2.5·10⁻¹⁵²) or 3.3319·10⁻⁹¹ (H-geo′ adopted)** — against HW s6's 2.3337·10⁻⁹⁶ at the ×17 ring (×3.72·10⁴). At c_A = 1:
   3.0988·10⁻⁹³ (HIST as written). **The "breach against 10⁻⁹⁴" disappears on this route.** (These use c_U = c_U^{in} = 1 as HW
   does; c_U is any number in (0, 1] subject to (S2°), and smaller values lower b_n° further.)
5. **What it does NOT change:** the residual. (E2^{𝔉°}) is still a weighted-law moment (Part C); its level-0 instance is OPEN.

## B.3 Level 0: what is consumed, on each route — PROVEN-HERE (consumer analysis and reductions)

There are exactly two level-0 consumers.
- **(L-a) TEL-f's factor k = −1,** E_μ[Φ_{−1}], Φ_{−1} = Π_{Q∈𝒰_0}e^{θX_Q} (HW §24.2), under μ_{R(𝔥)} with no spectator.
- **(L-b) the step j = 0:** Corollary CRC-HW at k = 0 (Φ_0 over 𝒰_1, with F_< = Φ_{−1}) and CRC-2T′/CRC-2T° step (5) at m = 1
  (level-1 animals, columns at level 0).

**On the current (Y-) route.**
- (L-a): Corollary CRC-HW's device at k = −1 decomposes by the cluster Y of non-R(𝔥)-free level-0 defects ρ-chained to P := 𝒰_0
  (the level-0 analogue of col(𝒰_{k+1}): the window X_Q lives on int Q, which plays the column's role). The statement consumed is
  therefore **(0a⁺)**: E_{ν_0^w}[Π_{Q∈Γ}e^{θX_Q}·1{Y ⊂ D_0}] ≤ C^{|Γ|}(C_Ae^{−a_Au_0})^{|Y|}e^{c_A‖Γ ∪ Y‖_sh} (Γ ⊂ level 0, Y ⊂ level 0
  outside Γ, N_1(Γ ∪ Y) R-free, w buffered on Γ ∪ Y). **HW §37's (0a) (Y = ∅) is its special case and does NOT suffice for this
  consumer.** (0a⁺) is HW l.1530's original clause ("Π_{Q∈Γ}e^{θX_Q} for Γ a set of level-0 cubes (Wilson window moment), Y at
  level 0") made well-formed by the patch Γ ∪ Y in place of col(Γ) ∪ Y: **HW §37's withdrawal of l.1530 as "ill-formed" was a
  mis-diagnosis** — only "col(Γ)" was ill-formed. (0a⁺) contains a level-0 defect price, i.e. the level-0 (SDP) PLD §19.7 says
  has no route ("there is no U_{-1} and no kernel to integrate").
- (L-b): (E2^𝔉′_res) at j = 0 = **(0b)** (Γ at level 1, Y at level 0): it needs the level-0 (SDP) for Y and, through the CAP-dec
  split, for the defects x(Γ_1) inside the columns.
- So on the Y-route **both** level-0 consumers need a level-0 defect probability, and **PLD §19.7's "(0a) is the weaker, and
  strictly" / §19.11 item 2's "state the level-0 clause as (0a) only, and drop (0b)" is REFUTED as a recommendation** — agreeing
  with REVIEW55 F12 (r55h-35) on (0b), and sharpened: (0a) with Y = ∅ does not serve (L-a) either.

**On route (4°).**
- (L-a): Corollary CRC-HW°'s device (𝒞°_{−1} = Col(N_8(𝒰_0)), bought by CRC-2T° at k_0 = 0) needs **(0a) exactly as HW §37 states
  it** — Γ ⊂ level 0, the window e^{θX_Q}, Y = ∅ — with the weight blind to N_8(Γ) and an empty buffer.
- (L-b): (E2^{𝔉°})_0 ⇐ (CEM^{COL}_res)_1 (Corollary E2-RED°), and at k = 1 the column energy has no infimum
  (F^col_Q(U_0) = Σ_{p∈𝒫(𝔅_Q)}s(U_0(p)), 𝔅_Q the level-0 region of Q): **(0b°)** is a level-0 Wilson moment on the regions 𝔅_Q
  at rate 24θu_1 ≤ λ_fu_0 (u_1 ≤ u_0 + R and g_0² ≤ 2g_K²), with F_< a sub-product of Φ_{−1}. **No defect probability.**
- Both are instances of ONE statement:
  **(W0)_λ [OPEN; owner node A; single level, finite range, no defect probability].** There are C_0(λ), c_A, independent of g,
  K, T, 𝔥, R and the cutoff, such that for every admissible 𝔥, R ∈ 𝔉_𝔥, every finite family 𝒳 of pairwise disjoint level-0
  regions, each the interior int Q of a level-0 cube Q or the level-0 region 𝔅_Q of a level-1 cube Q, with the cubes satisfying
  the Γ-clause at their level and N_8 of the union of their level-0 cubes R-free, every F_< ∈ 𝔖^cap_𝔥(0) satisfying (P-dis), and
  ν_0 := Wilson·1_{R,0}·F_<, w := h^{R,1}_0:
    E_{ν_0^w}[Π_{X∈𝒳}exp(λu_0Σ_{p∈𝒫(X)}s(U_0(p)))] ≤ C_0(λ)^{|𝒳|}·e^{c_A‖·‖_sh},   0 ≤ λ ≤ λ_f < 1.
  (0a) = (W0)_θ on {int Q : Q ∈ 𝒰_0}; (0b°) = (W0)_{λ_f} on {𝔅_Q : Q ∈ Γ}. **On route (4°) the level-0 clause is one statement,
  needed at two rates, and contains no level-0 (SDP).** PLD §19.7's ranking "(0a) < (0b)" becomes "(0a) and (0b°) are the same
  statement at rates θ ≤ λ_f".
- *Status of (W0).* OPEN. Fixed volume: Lemma LT's argument applies verbatim at level 0 (no exponential obstruction, for every
  cutoff). Gaussian model: a theorem (C.2). Plain Wilson measure without constraint or weight (cutoff ∞, w ≡ 1): reduces by
  reflection positivity to a per-block free-energy difference (C.3, ARGUED). PLD Theorem L0's reduction does not help: its
  (ii) is refuted (REVIEW55 r55h-33, the n_♯-cluster indicator), and its (W0-EQ)/(BCH-0) is a boundary-conditioned statement of
  the kind F-UNIV shows needs a defined charge (A.5's (BCH-1_res) discussion applies verbatim). Its dimension count (645) and the
  window constant (13.7255) stand as REVIEW55 r55h-32 found.

**Net for W2.** j = k_0: recovered on the Y-route by the restriction (B.1), absent on route (4°). Level 0: on the Y-route both
consumers need a level-0 (SDP) [(0a⁺) and (0b)], for which no route exists; on route (4°) both reduce to (W0), a level-0 Wilson
moment with no defect probability — the most tractable object in the family, now for both consumers rather than one.

---

# PART C — W3: the weighted-law decoupling, stated, tested, and what is missing

## C.1 The statement, with every quantifier
On route (4°) the whole node-A input is (E2^{𝔉°}) ⇐ (CEM^{COL}_res) restricted to what route (4°) feeds it:

**(CEM°)_k [OPEN; owner node A].** There are c_cem < ∞, c_A ≥ 0 such that for every g ≤ g_0, K, torus T, k ≥ 1, cutoff n ≥ 0,
admissible 𝔥 (for n), R ∈ 𝔉_𝔥, finite set A of level-k cubes with [A ∩ A_k(𝔥) = ∅ or A = 𝒰_k] and N_8(col_{k−1}A) R-free,
and F_< ∈ 𝔖^cap_𝔥(k_0) with k_0 ≤ k − 1 (so (P-dis) holds by Lemma SPEC), with ν := ν^{R,F_<}_{k−1}, w := h^{R,1}_{k−1},
Z_A := Π_{Q∈A}e^{θY^f_Q} and 24θ(1 + 2Rg_K²) < 1:
  **E_{ν^w}[Z_A] ≤ c_cem^{|A|}·e^{c_A‖col_{k−1}A‖_sh},  c_cem, c_A independent of g, K, T, k, n, 𝔥, R, A, F_<.**
Plus its level-0 instance (W0) (B.3).

**The weight, removed exactly (TILT).** By HW Lemma TILT (ii), E_{ν^w}[Z_A] = E_{μ^{F_<}_R}[Z_A], μ^{F_<}_R := W·F_<·1_R/norm the
full constrained chain on all levels. Hence, with μ_∅ := W·F_</norm (the same chain with NO constraint) and the exact identity
E_{μ_R}[Z_A] = E_{μ_∅}[Z_A·1_R]/μ_∅(R):
  **(CEM°)_k ⇐ (CEM-1^free)_k + (CEM-2^all)_k,  c_cem := c_1c_2, where**
  **(CEM-1^free)_k** [the unconstrained column moment]: E_{μ^{F_<}_∅}[Z_A] ≤ c_1^{|A|};
  **(CEM-2^all)_k** [the decoupling]: E_{μ^{F_<}_∅}[Z_A·1_R] ≤ c_2^{|A|}·E_{μ^{F_<}_∅}[Z_A]·μ^{F_<}_∅(R),
both with the quantifiers of (CEM°). Writing 1_R = 1_{R,≤k−1}·1_{R,≥k} and integrating the future,
E_{μ_∅}[Z_A1_R] = E_{ν_∅}[Z_A·1_{R,≤k−1}·w], so **(CEM-2^all) is exactly "the column tilt Z_A is (almost) anti-correlated with the
product W := (past constraint) × (future likelihood w)"** — the weighted-law decoupling, with the past constraint placed on the
same side as the weight. (PLD's SPLIT puts the past constraint into the reference law instead; that form, (CEM-2) with F ≡ 1 and
F_< restricted, is equivalent in kind but is not the one the model below proves.)

## C.2 Testing "the weight's typicality, not the event"
**(i) The weight is a likelihood, exactly.** TILT shows ν^w is a marginal of a positive measure whose density is the chain's own;
nothing in w can condition on an event the chain does not already weight. That is the precise content of "a likelihood, not an
adversary", and it is an identity.
**(ii) Fixed volume: CONFIRMED (Lemma LT, PROVEN).** For the restricted class every moment is polynomial in u_K, for every
cutoff; for universal F_< or universal F it grows like e^{cu}. So the mechanism works exactly where typicality is not bypassed
by conditioning — and fails exactly where it is.
**(iii) Every volume, in the linear model: CONFIRMED as a theorem.**

**Proposition GAUSS ((CEM°) in the linear-Gaussian, convex-core model): PROVEN-HERE for the model, modulo the Prékopa–Leindler
inequality (cited: A. Prékopa, Acta Sci. Math. 34 (1973) 335-343; the Anderson step is derived from it below).**
*The model.* Gauge-fix and linearise the chain about the trivial field: the fields of all levels become x ∈ R^D on the quotient by
gauge directions and torus zero modes (every functional below is gauge invariant and blind to them); the chain density becomes
e^{−½xᵀMx} with M = Σ_t M_t, one positive semidefinite M_t per chain term t, M > 0 on the quotient; plaquette and centre
curvatures become linear functionals; a defect is {|ℓ_P(x)| ≥ ε_1 for some interior P}; the constraint is replaced by its **convex
core** K := {no defect in any constrained cube, past or future, and none in the buffer set} — an intersection of symmetric slabs;
the spectators are taken uncapped, F_{Q″} = e^{q_{Q″}}; and θY^f_Q =: q_Q(x) = xᵀQ_Qx with **2Q_Q ≤ λ_fM_Q**, M_Q := Σ_{t∈col Q}M_t
(the model's Lemma DOM′: the minimised column energy is a convex quadratic, the minimum of one over the finer fields, and it is
below the column's own terms). The column term sets are disjoint (Lemma SPEC (P-dis)), so M ≥ M_A + Σ_{Q″}M_{Q″}.
*Claim.* E_{model}[Z_A] ≤ (1 − λ_f)^{−r_A/2} with r_A := rank Q_A ≤ 69984|A|, i.e. **(CEM°) holds in the model with
c_cem = (1 − λ_f)^{−34992} and c_A = 0 — log c_cem = 24254.6 at λ_f = ½ (check K6) — uniformly in the volume, K, k, 𝔥, R and A**,
and (CEM-1^free) and (CEM-2^all) hold with c_1 = (1 − λ_f)^{−34992}, **c_2 = 1**.
*Proof.* (1) The spectator-tilted reference is Gaussian: M_s := M − 2Σ_{Q″}Q_{Q″} ≥ M − λ_fΣM_{Q″} ≥ (1 − λ_f)M > 0, and
M_s ≥ M_A (disjointness), so 2Q_A ≤ λ_fM_s. Write Σ := M_s^{−1}, Σ′ := (M_s − 2Q_A)^{−1} ≥ Σ. (2) The model's constrained law is
N(0, Σ) conditioned on K, so E[Z_A] = E_Σ[e^{xᵀQ_Ax}1_K]/P_Σ(K) = E_Σ[e^{xᵀQ_Ax}]·P_{Σ′}(K)/P_Σ(K). (3) **Anderson step.** Σ′ = Σ + Δ
with Δ ≥ 0, so a N(0, Σ′) vector is X + Y with X ~ N(0, Σ), Y ~ N(0, Δ) independent, and P_{Σ′}(K) = E_Y[P(X + Y ∈ K)]. For fixed y,
φ(t) := P(X + ty ∈ K) = ∫1_K(x)f(x − ty)dx with f the (even, log-concave) density of X; (x, t) ↦ 1_K(x)f(x − ty) is log-concave, so
φ is log-concave in t (Prékopa: marginals of log-concave functions are log-concave), and φ is even (substitute x ↦ −x, K = −K,
f(−z) = f(z)); an even log-concave function is maximal at 0, so φ(1) ≤ φ(0). Hence **P_{Σ′}(K) ≤ P_Σ(K)**. (4) E_Σ[e^{xᵀQ_Ax}] =
det(I − 2Σ^{1/2}Q_AΣ^{1/2})^{−1/2}; the eigenvalues lie in [0, λ_f] (from 2Q_A ≤ λ_fΣ^{−1}) and at most r_A are nonzero, so it is
≤ (1 − λ_f)^{−r_A/2}; r_A ≤ Σ_Q rank Q_Q ≤ 3·|𝔏_{k−1}(col_{k−1}Q)|·|A| = 3·23328·|A| (the 9⁴ site block of a column; K6). (5) The
split: E_Σ[Z_A1_K] ≤ E_Σ[Z_A]P_Σ(K) is (2)+(3), i.e. c_2 = 1; (4) is c_1. ∎
**(iv) Why conditioning fails, in the same model — Anderson's hypotheses are exactly the dividing line.** Step (3) needs K
symmetric and convex. F-UNIV's B is a δ-neighbourhood of a NON-ZERO configuration (convex, not symmetric); Cor. E2-RED's
F = 1{Y ⊔ x(Γ_1) ⊂ D_j} is symmetric but NOT convex (a defect is the complement of a slab); a universal F_< can be either. The
future likelihood w_core(x_past) = P(x_fut ∈ K_fut | x_past) is symmetric and log-concave (Prékopa again), the buffer and
past-constraint cores are symmetric convex: they sit on the anti-correlated side. **So the mechanism is confirmed in a precise
form: the bound holds because every factor the law carries is a symmetric quasi-concave function of a (near-)Gaussian field,
and fails as soon as a factor is not.** The buffer-good EVENT is itself one of the harmless factors — not the mechanism (PLD
§18.7.2 (β) is right that it cannot supply the constant; route (4°) does not use it at all).
**(v) The cutoff allowance (cutoff n ≥ 1): ARGUED, not proven.** The true constraint R_n allows components of ≤ n defects, so
1_{R_n} = 1_K + 1_{R_n∖K} is not quasi-concave. In the model, E[Z_A1_{R_n}]/(E[Z_A]P(R_n)) ≤ 1 + P_{Σ′}(R_n∖K)/P(K) is only
fixed-volume; volume-uniformity needs a linked-cluster expansion in the allowed defects: each allowed configuration D carries
probability ≤ (6400e^{−c·u ε_1²})^{|D|}-type activities, and the tilt changes a far defect's probability by a relative amount
governed by Cov(ℓ_y, column of A)², which decays like r^{−8} in 4D (summable against r³). The near defects are suppressed at
rate (1 − λ_f)cuε_1² even under the tilt (Σ′ ≤ Σ/(1 − λ_f)). This predicts c_2 = 1 + o(1) uniformly in n, but it is a
Kotecký–Preiss-type argument for a measure with power-law correlations and is not written here.

## C.3 The tools of the brief, tried
- **Conditional large deviations.** Lemma LT and Proposition F-UNIV (PROVEN): they decide the fixed-volume question completely and
  show which quantifiers are fatal.
- **Reflection positivity / chessboard.** For the plain Wilson measure at level 0 (cutoff ∞, w ≡ 1) the Wilson action is
  reflection positive in lattice planes bisecting links (Osterwalder–Seiler 1978), so the chessboard estimate (Fröhlich–Israel–
  Lieb–Simon 1978) gives E[Π_{X∈𝒳}e^{λu_0Σ_{p∈𝒫(X)}s}] ≤ (Z_λ/Z)^{|𝒳|/N_b} with Z_λ the partition function at coupling (1 − λ)u_0
  on every block interior: the moment becomes a free-energy difference per block, which Theorem AT writes as a mean block action.
  Elementary bounds on log Z(v) (private plaquettes in an axial gauge from above; a near-flat neighbourhood from below) control it
  up to a GLOBAL u^{O(1)} from the torus' flat-connection zero modes [ARGUED; not written in full]. **It does not reach (W0) as
  needed**: 1_{R,0} (the n-cluster indicator) and w are not reflection-positive factors.
- **Cluster/polymer expansion, Kotecký–Preiss.** The allowed-defect expansion of (v) has tiny activities, but the underlying
  measure is not a product and has power-law correlations; KP needs exactly the decoupling it would prove. Not closed.

## C.4 What is missing, precisely (the first-class result of Part C)
For the actual chain (nonabelian, compact, nonlinear), with the constraint R_n for every cutoff n:
- **(M1) = (CEM-1^free) beyond the model:** E_{μ^{F_<}_∅}[e^{λ_f·𝔞^col_A}] ≤ c^{|A|} — a lower bound on the chain's effective action
  in the column by its minimised classical action, with fluctuation terms O(1) per degree of freedom, uniform in k, K, T: PLD
  §18.7.2 (a)/§19.5's "representation domination", unchanged. At level 0 it is the plain-Wilson window moment (C.3).
- **(M2) = (CEM-2^all) beyond the model:** a non-Gaussian Anderson-type peakedness inequality for the chain: tilting by the column
  energy does not raise, beyond c^{|A|}, the probability of the symmetric no-defect events that make up W — together with the
  allowance of (v). For Gaussian and for log-concave perturbations of Gaussian measures this is the classical Anderson/Prékopa
  mechanism; for the compact nonabelian chain it is available at best in the small-field region (where the gauge-fixed density
  is a small perturbation of a Gaussian) and must be completed by large-field suppression.
Neither (M1) nor (M2) is a renaming of (CEM^{COL}): the model proves both with explicit constants, and what is missing is the
passage from the linearised chain with convex-core constraints to the real chain with the cutoff allowance — i.e. the
small-field/large-field content of the constructive RG, at the scale of one column. **Nothing smaller than this has been isolated,
and no route that skips it is known.** Status: (CEM°), (CEM-1^free), (CEM-2^all), (W0): OPEN.

---

# PART D — W5 (the coordinator's requirement): uniformity in the cutoff n_♯

**Where the cutoff enters node A's statements.** (1) Admissibility clause (A1) of 𝔥 ("every *-component of 𝒰_k has more than
n_♯ cubes", HIST §7.1); (2) the constraint R_{S,E} ("every *-component … has ≤ n_♯ cubes", HW §13.1) in every law of 𝔉_𝔥 — the
past constraints in ν, the future ones in w = h^{R,1}; (3) through 𝔥, the index set 𝒬 of the spectators. It does NOT enter the
spectator factors F_Q (θ, a_bad, u and the column fields only), the thresholds (ε_1, ρ = 8, θ, λ_f), or any geometric constant.

**Item by item.**
| item (scope) | constants uniform in the cutoff? | basis |
|---|---|---|
| (LI^F), Theorem LI^U-0 / LI^U-0′ (HW §14, §22, §30.1) | **YES, PROVEN** (c = 0 for every cutoff) | the proofs use persistence (H-nest, (A2)) and "1_{R,m} reads U_m only on links interior to cubes of S^{(m)}" — true of the n-cluster indicator for every n; (A1) is never used |
| the class 𝔖^cap, Lemma SPEC | **YES, PROVEN** | (P-lo), (P-hi), (P-dis) use (A2), DJ, FAR's claim only (A.1) |
| Lemma LT (fixed volume) | **YES, PROVEN** | {𝔄 ≤ 1} ⊂ R_n for every n ≥ 0 (A.3 step (6)) |
| (CEM°), (W0) (route (4°)); (CEM^{COL}_res), (E2^𝔉′_res), (ACT′_res), (LCR^act′_res), (BCH-1_res) | **REQUIRED, stated; OPEN** | they are OPEN statements; uniformity is now part of each statement (A.5, B.2, B.3, C.1) |
| the same, in the linear-Gaussian model | **YES at n = 0 and at n ≥ (number of cubes): PROVEN; 1 ≤ n < volume: ARGUED** | Proposition GAUSS (convex core = n = 0; no constraint = n large); C.2 (v) |
| (SDP)^A via NA-PRICE^{E+}_res | **YES iff c_cem is** | C_A = 2max{n_int(1 − λ)^{−3/2}e^{λκε_1²R/256}, c_cem}, a_A = min{λκε_1²/256, 6θ′a_bad}; FT^far ("on {S ⊂ D_k}, 1_{R,k} = 1_{R′,k}"), KD, CW are cutoff-free. **Not consumed by the HW route on route (4°).** |
| (PRICE^ℛ) (HW §13.2) | off the current route ("(PRICE^ℛ), ℛ_𝔥^↑, Lemma DECL and Lemma REL-seq leave the route", HW §24.1); if revived, YES iff node A's are | — |
| (M-f^A) = (M-f^cap) under μ_{R(𝔥)} (via TEL-f + Cor. CRC-HW°) | **YES iff C_fc, c_A are — provided c_f° is computed with the INPUT c_U^{in}** | C_fc′ = C_fc e^{2401c_U^{in} + 81c_A}, c_f° = c_U^{in} + 81c_A. **Caution:** HW §30.6's "c_U^{out} = 2ε_2 … is what enters c_+ in Corollary CRC-HW" would make c_f → B_0 → n_H → n_♯ → ε_2 → c_U^{out} → c_f a loop; it is broken only by using c_U^{out} ≤ c_U^{in} (fixed first). State c_f with c_U^{in}. |
| CRC-2T°'s own constants b_n°, b_D°, C_ℓ | **YES, PROVEN** (cutoff-free formulas) | 6400^{n_♯} appears only in ε_2°, which (S2°) bounds via g_0 AFTER n_♯ |

**Does the F_< restriction change it? It removes cutoff-dependence; it does not add any.** (a) The restricted class is defined
by properties that never mention the cutoff. (b) The index set 𝒬 depends on the cutoff through (A1), but every restated statement
is uniform over 𝒬: the spectators only lower the coupling in disjoint columns ((P-hi)); in the model they change M to
M_s ≥ (1 − λ_f)M whatever 𝒬 is, and Lemma LT's bound is uniform over 𝒬. (c) Under the universal quantifier, F_< could have been
the indicator of a cutoff-dependent event ("the defect component through x has exactly n_♯ + 1 cubes"); the restriction excludes
exactly that. The same holds for the conditioning F (Proposition F-UNIV): F ≡ 1 cannot encode the cutoff.

**What uniformity needs (the answer to the DAG's question).** On route (4°): nothing beyond the cutoff-uniform versions of the two
node-A statements node A owes anyway, (CEM°)_k (k ≥ 1) and (W0) — i.e. (M1) + (M2) of C.4 for every cutoff — plus the c_U^{in}
reading of c_f. On the Y-route additionally (CEM^{COL}_res) at the two rates of E2-RED^H. **So the only potential cycle in the
hierarchy (SMALLNESS_DAG §3.1) is closed exactly when node A proves its moment with cutoff-uniform constants; no further statement
is needed. With present inputs it is proven at fixed volume (Lemma LT) and, in the linear model, at the two extreme cutoffs; not in
general.** No node-A constant on route (4°) contains a counting factor of the type 6400^{n_♯}: node A's statement is a per-column
moment and counts no animals.

---

# PART E — W4: the multiplicative Δ_sh, everywhere it was used

**Lemma PD (push-down): PROVEN-HERE (check G5).** For a set S of level-k cubes and any choice function x (x_Q a child of Q),
  **‖x(S)‖_sh ≤ 16‖S‖_sh + 66|S|**  (‖S‖_sh over levels k…K−1, ‖x(S)‖_sh over levels k−1…K−1).
*Proof.* r = 0: |x(S)| = |S|. r = 1: Σ(x(S)) = N_1(π x(S)) = N_1(S), ≤ 81|S|. r ≥ 2: Σ^r(x(S)) = Σ^{r−1}(N_1(S)) ⊂ N_1(Σ^{r−1}(S))
(iterate Σ(N_1X) ⊂ N_1(ΣX)), and |N_1(Σ^s S)| ≤ 16|Σ^s S| for s ≥ 1 (Σ^s(S) = N_1(A_s) is N_1-thickened, so N_1 of it is a union of
2⁴ translates — HW Lemma RING's step, CONFIRMED by REVIEW55 r55h-07). Sum: |S| + 81|S| + 16(‖S‖_sh − |S|). ∎ This sharpens
REVIEW55 F9's "+81|S|" to "+66|S|"; the multiplicative 16 cannot drop below 256/81 (REVIEW55). G5: 0 violations on 240 random
samples and on the adversarial family D = 2…60 and D = 20000, whose excess 81 + 175D reproduces REVIEW55's G-B (G5c).

**Every use of the depth-free form, with its correction.**
| place (locating string) | claim | correction | effect |
|---|---|---|---|
| PLD §16.6 (b) "the excess sh(x_Q) - sh(Q) ≤ 81 + 2401·32·80·Σ … is depth-free" | per-cube excess depth-free | false even for one cube: 81 + 175D (G5c) | the sentence "With per-cube shadow sums the recursion closes" falls; §16.6 (b)'s NEGATIVE conclusion stands |
| PLD §16.7 "c_sf := e^{2c_U(81 + Δ_sh)}c_lcr … Δ_sh is a per-cube constant" (and §16.11, §18.8 (i)) | Δ_sh per-cube | the (LI^U) allowance of the column cubes is c_U‖col(A∖A′)‖_sh ≤ 81c_U(|A∖A′| + ‖A∖A′‖_sh): a shadow term | **none on the HW route**: PLD's c_U = 0 there (Theorem LI^U-0; HW [RHW5-fix SYM-1] (c)) and Cor. LAW (b) gives c_sf = c_lcr |
| PLD §18.5 (b′) "‖x(S)‖_sh ≤ ‖S‖_sh + (1 + Δ_sh)·|S| … depth-free. PROVEN-HERE" | additive push-down | Lemma PD (multiplicative) | (b′) false (REVIEW55 F9, CONFIRMED) |
| §18.5 (b′) "Consequence", §18.5 (g) and §18.11 "Compounding is NOT a reason", "UPGRADE … PROVEN" | no compounding | through Lemma MD a level recursion multiplies the shadow-allowance constant by up to 16 per level: c(k) ≤ 16c(k−1) + per-cube terms | **(NP-F6) gains a fourth reason (compounding)**; Proposition CD (b) dead on four counts; the UPGRADE is a downgrade |
| §18.6.1 (iv) PATCH (iv) "Lemma MD contributes … a per-cube depth-free Δ_sh … TRANSMITTED, unchanged" | NA-PRICE^E/E+ transmit | true for E+ (no MD); for E (i) the delivered allowance is c‖x(S_md)‖_sh ≤ 16c‖S‖_sh + 66c|S| | HW uses E+ (Y-route) or neither (route (4°)): **no effect on the HW route** (REVIEW55 r55h-16, CONFIRMED) |
| §18.10 "(b′)'s proof does not use the numerical value of Δ_sh, only that it is finite and depth-free, which §16.6 (b) and p4 D2b supply" | depth-free supplied | depth-freeness false; p4 D2b sampled random positions | — |
| §18.12 request 3 "(b′) supplies the excess line B2 (b) asks for, ready to quote"; REVIEW_PLD_S5 B2 second clause | the line exists | withdrawn (REVIEW55 r55h-56, CONFIRMED) | — |
| HW | none | HW's constants are multiplicative already (SH-att′ 81, COL′ 81, RING 16); §30.2's per-cube depth term and PATCH (iii) are correct | — |
**Net:** no statement live on route (4°), or on the Y-route with E2-RED^H, uses the depth-free form; every use was on a route
already dead or off the HW route, and each is corrected above.

# PART F — Lemma DOM's constant (a small re-check that REVIEW55 F12 asked for implicitly)
REVIEW55 F12 (r55h-29) found PLD's proof of Lemma DOM uses "g_k ≤ g_K for k ≤ K, (F_R)", which (F_R) does not give, and proposed
λ_f := 24θ(1 + 4Rg_K²). The slip is real, but **the stated λ_f = 24θ(1 + 2Rg_K²) is correct by a two-line route**: for i < k,
(F_R)'s lower half gives u_k ≤ u_i + R, so u_k/u_i ≤ 1 + Rg_i²; and u_i ≥ u_K − R gives Rg_i² ≤ Rg_K²/(1 − Rg_K²) ≤ 2Rg_K² for
Rg_K² ≤ ½ (check K5: x/(1 − x) ≤ 2x on (0, ½], violated at ¾). PLD §16.7's own proof already used this route ("u_k ≤ u_{k-1} + R =
u_{k-1}(1 + Rg_{k-1}²) ≤ u_{k-1}(1 + 2Rg_K²)"). REVIEW55's replacement 1 + 4Rg_K² is valid only for Rg_K² ≤ 3/8 (it equals
(1 − x)/(1 − 2x) ≤ 1 + 4x there and diverges at x = ½), not for Rg_K² ≤ ½ as written. Immaterial at Rg_K² ≲ 10⁻⁹⁴R; recorded so
that nobody propagates the 4.

---

# SUMMARY TABLE (every item of this file)

| id | item | status / verdict | where |
|---|---|---|---|
| na55-01 | class 𝔖^cap + Lemma SPEC (P-lo, P-hi, P-dis; only (A2) used) | PROVEN-HERE | A.1 |
| na55-02 | every consumer's F_< lies in 𝔖^cap; no consumer needs the universal F_< | CONFIRMED (CRC-2T′ step (5), Cor. CRC-HW, (CRC), off-route, TEL-f read) | A.2 |
| na55-03 | Cor. CRC-HW at k = 0 passes Φ_{−1} (reads U_0 = U_{k_0}), outside HW §30.1's stated hypothesis | NEW (minor); covered by "F_< ∈ 𝔖^cap" with no change of proof | A.2 |
| na55-04 | Lemma LT (a): restricted forms are polynomial in u_K at fixed volume, every cutoff | PROVEN-HERE | A.3 |
| na55-05 | Lemma LT (b): universal F_< (k ≥ 2) / universal F (k ≥ 1) grow like e^{cu} | PROVEN-HERE (F_< part uses PLD p5 B3's exact linear-order value 9b) | A.3 |
| na55-06 | REVIEW55 F6 / r55h-18: universal F_< makes the five statements false; restrict to the capped spectators | CONFIRMED (now rigorous at fixed volume) — **necessary but NOT sufficient** (na55-07) | A.3-A.4 |
| na55-07 | Proposition F-UNIV: the universal conditioning F makes (CEM^{COL}), (ACT′), (LCR^act′), (BCH-1) false, for every law and every F_< | PROVEN-HERE (NEW; K3, K4) | A.4 |
| na55-08 | Cor. F-UNIV′: NA-PRICE^{E+}'s F-conditioned conclusion, and REVIEW_PLD_S5 S5-20/B3's requested F-conditioned form, false for universal F | PROVEN-HERE given p5 B3; **REFUTES B3 as quantified** | A.4 |
| na55-09 | PLD Cor. E2-RED as written ((D1) conditions on F = 1{Y ⊔ x(Γ_1) ⊂ D_j}) | **REFUTED as a proof**: its input is false as quantified (PROVEN); false at that specific F (ARGUED) | A.4 |
| na55-10 | Cor. E2-RED^H: (E2^𝔉′_res) at j ≥ max{k_0, 1} ⇐ (CLS-min) + (CEM^{COL}_res) at rates pθ, θ′; θ ≤ 1/28 | PROVEN-HERE (implication) | A.5 |
| na55-11 | NA-PRICE^{E+}_res consumes (CEM^{COL}_res) only at F ≡ 1 | PROVEN-HERE (one-line edit) | A.5 |
| na55-12 | E2-RED's Γ = 𝒰_{j+1} case violates (CEM^{COL})'s "A ∩ 𝒰_k = ∅" | NEW (minor); harmless; clause restated | A.5 |
| na55-13 | restated (E2^𝔉′_res), 𝔏^buf_res, (CEM^{COL}_res), (ACT′_res), (LCR^act′_res), (BCH-1_res); corrected Delta 3/M-7, HW §37 bullet 5, §38 item 5 | statements OPEN; consumer fit CONFIRMED; both falsifiers excluded | A.5 |
| na55-14 | j = k_0 on the Y-route | PROVEN-HERE (implication) — **CONFIRMS REVIEW55 r55h-19's prediction** | B.1 |
| na55-15 | route (4°): (E2^{𝔉°}) ⊂ (E2^𝔉′_res); E2-RED°; Theorem CRC-2T° (no (S1), no Y); Cor. CRC-HW° | PROVEN-HERE (implications) | B.2 |
| na55-16 | route (4°) constants: b_n° = 12401c_U + 810162c_A, b_D° = 10000c_U + 810000c_A, c_f° = c_U + 81c_A; binding ceiling 8.676·10⁻⁹² (c_A = 0) | computed (K2); informational | B.2 |
| na55-17 | level 0, Y-route: (L-a) needs (0a⁺) not (0a); (L-b) needs (0b); both need a level-0 (SDP) | PROVEN-HERE (consumer analysis) — **REFUTES HW §37's "l.1530 ill-formed" and PLD §19.7/§19.11 item 2** (sharpens REVIEW55 r55h-35) | B.3 |
| na55-18 | level 0, route (4°): (0a) and (0b°) are one statement (W0) at rates θ ≤ λ_f; no level-0 (SDP) | PROVEN-HERE (reduction); (W0) OPEN | B.3 |
| na55-19 | (CEM°) ⇐ (CEM-1^free) + (CEM-2^all), the weight removed by TILT | PROVEN-HERE (identity); both parts OPEN | C.1 |
| na55-20 | Proposition GAUSS: (CEM°) in the linear-Gaussian convex-core model, c_cem = (1 − λ_f)^{−34992}, c_2 = 1 | PROVEN-HERE for the model (Prékopa–Leindler cited) | C.2 |
| na55-21 | "the weight's typicality, not the event" | **CONFIRMED in a precise form** (LT at fixed volume; Anderson in the model): harmless factors are symmetric quasi-concave; conditioning on non-symmetric or non-convex events is the failure mode | C.2 |
| na55-22 | the cutoff allowance (1 ≤ n < volume) in the model: c_2 = 1 + o(1) | ARGUED | C.2 (v) |
| na55-23 | chessboard for the plain level-0 window moment | ARGUED; does not reach (W0) (constraint and weight are not RP factors) | C.3 |
| na55-24 | (M1), (M2): the missing statements, with quantifiers | OPEN (precise) | C.4 |
| na55-25 | cutoff uniformity: (LI^F)/LI^U-0′, 𝔖^cap, LT, CRC-2T°'s constants — PROVEN uniform; node-A moments — required, OPEN; c_f must be read with c_U^{in} | as stated | D |
| na55-26 | Lemma PD: ‖x(S)‖_sh ≤ 16‖S‖_sh + 66|S| | PROVEN-HERE (G5); sharpens REVIEW55 F9's +81|S| | E |
| na55-27 | every depth-free Δ_sh use; (NP-F6) gains a 4th reason; PATCH (iv) true for E+ only; PLD §16.6 (b) single-cube "depth-free" and §16.7's per-cube Δ_sh false (no effect on the HW route) | CONFIRMS REVIEW55 F9 / r55h-16 / r55h-25 / r55h-56; **REFUTES** §16.6 (b)'s parenthesis and §16.7's per-cube placement | E |
| na55-28 | Lemma DOM's λ_f = 24θ(1 + 2Rg_K²) | CONFIRMED (two-line proof, K5); **REVIEW55 F12's 4Rg_K² correction REFUTED** as unnecessary (and valid only for Rg_K² ≤ 3/8) | F |
| na55-29 | π(N_1(col X)) = N_1(X) (REVIEW55 F4 G-C1) | CONFIRMED (G4, 360 samples) | G4 |
| na55-30 | REVIEW55 F10 / r55h-26: "(CEM-2) dissolved" refuted; residual = the weighted-law decoupling | CONFIRMED; sharpened to (CEM-2^all), proven in the model | C.1 |
| na55-31 | REVIEW55 F11 / r55h-27: (LCR^act′) not past the impossibility | CONFIRMED (restated as a well-posed OPEN statement) | A.5 |

**Counts.** Prior claims re-judged here: **CONFIRMED 10** (na55-02, -06, -14 (prediction), -21 (mechanism), -27 (REVIEW55 F9
items), -28 (DOM's constant), -29, -30, -31, and REVIEW55 r55h-35 inside -17); **REFUTED 9** (PLD Cor. E2-RED as a proof;
REVIEW_PLD_S5 B3's form as quantified; NA-PRICE^{E+}'s F-conditioned conclusion as quantified; (CEM^{COL})/(ACT′)/(LCR^act′)/
(BCH-1) as quantified in F; HW §37's "l.1530 ill-formed"; PLD §19.7's "(0a) strictly weaker" as a consumer ranking and §19.11
item 2; REVIEW55 F12's 4Rg_K²; PLD §16.6 (b)'s single-cube depth-free excess; PLD §16.7's per-cube Δ_sh); **NOT-VERIFIED 0**.
New results: **PROVEN-HERE 14** (na55-01, -04, -05, -07, -08, -10, -11, -14, -15, -17, -18, -19, -20 (model), -26); **ARGUED 2**
(-22, -23); **OPEN statements** (-13, -24, (W0), (CEM°)). Inputs cited, not re-derived here: HW Lemma DJ (for (P-dis) when
A = 𝒰_k), PLD p5 B3's exact linear-order value (for LT (b)'s F_< half and F-UNIV′), the Prékopa–Leindler inequality (for GAUSS).

# FOR THE LEAD

**1. The repair REVIEW55 names is necessary but not sufficient.** Restricting F_< to the capped history spectators is exactly
what every consumer passes (na55-02) and removes F6's falsifier (Lemma LT, PROVEN). But (CEM^{COL}), (ACT′), (LCR^act′), (BCH-1)
and NA-PRICE^{E+}'s F-conditioned form carry a SECOND universal function — the conditioning F — and with it they are false for
every law and every F_< (Proposition F-UNIV, PROVEN, explicit). REVIEW_PLD_S5's binding fix B3 asked for one of these false forms.
Restated with F ≡ 1 (A.5). **Cor. E2-RED as written has no valid input** (its (D1) conditions on rare adjacent defects); on the
Y-route it is repaired by Hölder (E2-RED^H, PROVEN implication, θ ≤ 1/28).

**2. A route that removes the edges (B.2, PROVEN implications).** Replace Theorem CRC-2T′'s steps (3)-(6) by "relax
Col(N_8(col 𝒟)) ⊃ [𝒟], paid by the same induction hypothesis" (|𝒞″| ≤ 12401n + 10000M, checks G1-G3), and Corollary CRC-HW's
Y-device likewise. Then node A owes only (E2^{𝔉°}) — the Y = ∅, empty-buffer instance of (E2^𝔉′), strictly weaker — which follows
in one line from (CEM^{COL}) with F ≡ 1. **(SDP)^A, NA-PRICE^{E+}, KD/CW/MD, every F-conditioned statement, the j = k_0 edge,
(S1) and the level-0 (SDP) all leave the HW route.** Level 0 becomes one statement (W0) at two rates. HW's constants improve
(c_f: 6561(c_A + 17c_U) → c_U + 81c_A; binding ceiling ×3.7·10⁴, check K2) — informational only (REVIEW55 F1: nothing binds).

**3. What PROOF.md's tally / HANDOFF's critical path should say differently.**
- HANDOFF critical path item 3 → *"Node A owes (CEM°)_k (k ≥ 1) and (W0): unconditioned column moments under the weighted past
  law, F_< = the capped history spectators, the weight blind to N_8 of the column, constants uniform in g, K, T, k, 𝔥, R and the
  cutoff n_♯ (route (4°), NODEA55 B.2). Inside it the residual is (M1) + (M2) (NODEA55 C.4): an effective-action domination and an
  Anderson-type decoupling for the actual chain; both are theorems in the linear-Gaussian convex-core model (c = (1 − λ_f)^{−34992})
  and hold at fixed volume; nothing smaller is isolated. The universal F_< AND the universal conditioning F are both false."*
- The "level-0 hole": on the current route it needs a level-0 (SDP) in BOTH consumers ((0a⁺) and (0b)); HW §37's (0a) (Y = ∅)
  does not serve TEL-f's k = −1 factor there. On route (4°) both are (W0).
- PLD's s7 counted item [E7] (3)'s "(0a) is the weaker" should not be counted as a consumer statement (na55-17); REVIEW55 already
  removed (ii).
- SMALLNESS_DAG §3.1: the n_♯ loop closes exactly when node A's moment constants are cutoff-uniform (now part of every restated
  statement), and c_f must be computed with c_U^{in} (HW §30.6's "c_U^{out} … enters c_+ in Corollary CRC-HW" would close a loop
  through ε_2).
- No change to the tally's counted items from this file beyond REVIEW55's (I count nothing; the lead decides).

**4. Requests (not applied anywhere; no other file was touched).**
- HW: adopt route (4°) (B.2) or, if keeping the Y-device, cite E2-RED^H and the (0a⁺)/(0b) level-0 statements; restate H6′ as
  (E2^{𝔉°}) [or (E2^𝔉′_res)]; restate §30.1's F_< hypothesis as "F_< ∈ 𝔖^cap_𝔥(k_0)"; record that l.1530's level-0 clause was
  well-formed with Γ ∪ Y as the patch.
- PLD: restate per A.5 (F_< restricted, F ≡ 1, generator-specific rings, the Γ-clause); withdraw the F-conditioned forms of
  NA-PRICE^{E+}, (SDP)^A, (J-NS^cd), (SF-cap)^{COL}; withdraw §18.5 (b′) and its four echoes (Part E); add (NP-F6)'s fourth reason.
- RLARGE row 10b and critical-path item 1: as item 3 above.
- REVIEW_PLD_S5 B3: record as false as quantified.

**5. Codex verdicts used:** none (no CODEX_REVIEW file touches these items; grep recorded above).

UTC end: see the reply. Files written: NODEA55.md; checks/na55_geo_criteria.md, na55_geo.py, na55_geo_out.txt, na55_geo_err.txt;
checks/na55_const_criteria.md, na55_const.py, na55_const_out.txt, na55_const_err.txt. No git command was run.
UTC end (actual): 2026-10-29T00:13:52Z. NODEA55.md final size recorded by the lead; checks: na55_geo (8.4 s), na55_const (7.1 s), both exit 0.
