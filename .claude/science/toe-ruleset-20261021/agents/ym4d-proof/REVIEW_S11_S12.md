# REVIEW_S11_S12: independent hostile review of sessions 11 and 12

Reviewer: an independent agent that did not write the proof.

Inputs:
- PROOF.md, byte-identical to PROOF_session12_snapshot.md (`diff` empty).
- `diff PROOF_session10_snapshot.md PROOF_session12_snapshot.md` (941 lines; hunks at l.1-135, 433-562, 840-853,
  1358-1365, 1467-1469, 1571-1765, 1811-1950, 1952-2440, 3416-3470, 3584-3636), with PROOF.md read by offset.
- RTARGET.md §15-23; LOG.md sessions 11-12 (l.558-649); REVIEW_S9_S10.md (the 13 binding fixes).
- Checks c21 (s11 re-run), c23, c24, c25, c26 (A, B, C and the addendum), c27: criteria, scripts and outputs.
  **All seven were re-run** (below).
- **Primary sources.** Dimock arXiv:1108.1335, extracted text (`rev910/dimock.txt`, the copy REVIEW_S9_S10 fetched;
  identical to the session's `s10/txt/dimock1.txt`). The owner-quote source, the memory file
  feedback_no_permission_except_axioms.md, read directly.
- **Provenance.** The session-11 and session-12 agent transcripts (subagents a41a8d4… and a8ef7cb…; tool-call
  timestamps, UTC). The directory is untracked.

Scratch work is in the scratchpad `rev1112/`:
- `cegeo_indep.py`: an independent exhaustive test of CE-geo';
- `polyenum.py`: an exhaustive polymer enumeration;
- `c27_diag.py`: E3 absolute errors;
- `rdecay.py`: the r-kernel tail on a T = 32 torus;
- all re-run outputs.

No other file was edited.

**Bottom line.**
- All 13 REVIEW_S9_S10 fixes are applied. There are three small residues:
  - a wrong Dimock line citation;
  - a pre-registered criteria file that still says "false";
  - one label nuance in fix 13.
- The 6 new PROVEN-HERE tally items survive. Session 11: CE-geo', N2-E, N2-red, FP-ab. Session 12: N2-lin, PG.
  - **None is WRONG and none is a GAP.**
  - CE-geo', N2-E (through N2-a) and N2-lin need wording or scope fixes.
  - PG is CONFIRMED in every step, and its arithmetic was re-done.
- "Linearised" is kept in the theorem statement and in the tally entry. It is dropped in two summary lines (header
  l.19, tally l.3427), and the header also omits the n ≥ 1 / small-curvature scope.
- Every re-run reproduces the stored outputs exactly, apart from timing and RSS lines. The three failed
  pre-registered criteria (c23 Q3, c26 Q7, c27 E3) are honestly recorded. The c26 addendum is acceptable.
- **New, informational:** the proof's remark that the kernels "have power tails" is only an upper bound. The
  r-kernel I computed decays exponentially (to the precision tested), so the exponential-decay question (N10) is
  open in a favourable direction. It is the decisive next linear question for decision 4.

## [R910-fix] audit (REVIEW_S9_S10 binding fixes 1-13)

| # | Fix | Where | Verdict |
|---|---|---|---|
| 1 | CE-κ attribution, touching reading, finite-difference proof, 0.9997 | PROOF l.40-47, 89-97, 1571-1574, 1612-1622, 1690-1721, 1739-1743, tally 3466; RTARGET l.324; LOG l.564 | Applied, correct. Residues (a)-(b) below |
| 2 | Discrepancy 2 → definitional difference | l.1640-1645, 96, LOG l.570 | Applied |
| 3 | CE-cx inherited constants | l.1726-1729 | Applied, correct (re-derived) |
| 4 | N6 κ requirement | l.1920-1923 | Applied (≈ 457 after [S11]) |
| 5 | BG-b-lin factor 2, n ≥ 1, n = 0 case, κ̂/κ_{k-1}; CR (ii) | l.1763, 1824-1830, 1842 | Applied; 2·625 = 1250 is right |
| 6 | LES small radii | l.1811-1813 | Applied |
| 7 | "iff" → "if" | l.135; LOG appended | Applied |
| 8 | D4-obs OPEN | l.1358-1365, tally | Applied |
| 9 | (DF3') Cauchy margin, \|t\| ~ 1/g | l.1937-1942 | Applied |
| 10 | B-NA (iii) vs R3-fix | l.1876-1879 | Applied |
| 11 | c20 / c22 reporting | l.1467-1469, 1899-1911; c20_time.txt l.19 | Applied |
| 12 | "(linearised)" | l.1949 | Applied |
| 13 | Owner delegation quoted | l.8-10, 116-125, 3433-3436; LOG l.610-619 | Applied; nuance (c) below |

**(1) CE-κ: CONFIRMED-WITH-FIX (residues only).**
- A search for false/refut/wrong near Thm 27, Dimock or c_0 finds no remaining "Thm 27 is false" in PROOF.md or
  RTARGET.md. The only PROOF hit, l.41, reports the withdrawal. LOG l.538 keeps the session-10 sentence, with the
  appended correction at l.564. That is acceptable in an append-only log.
- The credit to Dimock is right: the remark at text l.2224, "(So c0 does depend on κ.)", is on p.40 (page markers 39
  at l.2152 and 40 at l.2240).
- The six-bond proof (l.1700-1715) was re-checked:
  - no branch ambiguity: |log Ξ_S| ≤ 3h² + h⁶ < 4h²;
  - pairing S with S△{b} kills every Y that misses b;
  - d(Y) ≥ 1 for Y ⊇ Y_6 (the outer columns are 1 apart);
  - e^{-(κ-3κ_0-3)d} ≤ e^{-(κ-4κ_0-3)}e^{-κ_0d} for d ≥ 1, which needs κ ≥ 4κ_0 + 3, as stated;
  - Δ = log(1 + t⁶) exactly.
  Correct.
- **Residue (a), l.1697.** "in the proof of his Lemma 21, l.2731 of the extracted text" is wrong twice. The sentence
  "κ ≥ 10(κ0 + 1) which we assume" is at l.1672 of the extracted text. It sits in §4.7 "scaling", after (243)-(244),
  not inside the proof of Lemma 21 (which is stated at l.1629). Fix: "in §4.7 (after (243)), l.1672 of the extracted
  text". REVIEW_S9_S10 itself said "Lemma 21, l.1671-1672"; the line number was right there, the lemma attribution
  loose.
- **Residue (b), checks/c21_criteria.md l.52-53.** The pre-registered session-10 text still reads "So I1 PASS means:
  Thm 27 as stated … is false". Do not edit a criteria file. Append one annotation line to its [S11] addendum: the
  reading is withdrawn per REVIEW_S9_S10 fix 1; I4 now carries the argument; the literal statement's quantifier is
  corrected, as Dimock's p.40 remark does.

**(13) Owner quotes: CONFIRMED-WITH-FIX (label nuance).**
- Both quotes are verbatim from the memory file, including the dates 2026-10-21 and 2026-10-23 and the owner's
  spelling. They are labelled second-hand ("no primary transcript was read").
- **Residue (c).** The delegation in that file is for "the TOE ruleset work" and the CL register. Applying it to a
  proof-technique choice is the lead's inference. The label should say "by inference from".
- The 10-23 quote itself says "(put it in the CL until we have a working TOE)", while the label says decision 4 "is
  not a CL change". The reason given (a proof method, not a TOE rule) is sound. State it as a deliberate reading of
  that parenthesis, so the quote does not appear to contradict the label.

## (1) Session-11 PROVEN-HERE items

### Lemma CE-geo' (l.1957-1984): CONFIRMED-WITH-FIX (scope wording)

The proof was re-derived step by step.
- **The lift.** Order the segments so that each one meets the earlier ones, and lift them to R^d. A torus cube that
  meets τ lifts to a lattice point within sup-distance ½ of τ̃, so the count is surjective, hence ≤.
- **The boxes.** k + [-½, ½]^d ⊂ τ̃ + [-1, 1]^d. The boxes have disjoint interiors, so N ≤ vol(τ̃ + K).
- **Increment.** vol(τ_j + K) - vol(τ_{j-1} + K) ≤ vol(s̃_j + K) - vol(p + K), because p + K ⊂ τ_{j-1} + K.
  - Cavalieri for a segment plus a convex body gives ℓ_j·vol_{d-1}(proj_{u⊥}K).
  - The projection of [-1, 1]^d onto u⊥ has volume 2^{d-1}|u|_1 ≤ 2^{d-1}√d.
- **The result.** N ≤ 2^d + 2^{d-1}√d·ℓ, which in d = 4 is 16(1 + ℓ). It is sharp at ℓ = 0. No T ≥ 3 is needed.
- **Theorem CE constants** (re-derived):
  - (g4'): e^{-16a(|X|/16 - 1)} = e^{κ_0}e^{-a|X|}, so K_0 = e^{κ_0}/6400 with κ_0 = 16 log 12800 = 151.31;
  - Step 1: u ≤ |Y|/16 ≤ 1 + d. With 1 + d ≤ e^d this gives C_K = 32eK_0 and κ_1 = κ - κ_0 - 2;
  - Step 4: needs only |Y| ≤ κ_0(1 + d) and |Y| ≤ κ_0e^d, both true. The n = 1 term needs C_K ≤ κ_0B, which holds;
  - 3κ_0 + 3 = 456.9.
- **Independent test** (`rev1112/cegeo_indep.py`). The data are rational with small denominators, so a float
  tolerance of 1e-9 decides touching exactly. Zero violations in 103,287 instances:
  - d = 2: every segment on the ¼-grid of [-1, 1]²; every 2-segment path and every 3-leg star on the ½-grid;
  - d = 4: every segment on the ½-grid {-½, 0, ½, 1}⁴ (32,640); 3000 random 2-3-segment trees on [-1, 1.5]⁴;
    corner diagonals and zigzags.
  - The maximum of N/(2^d + 2^{d-1}√d·ℓ) is 1.0000, at a corner point. The sharper form N ≤ 2^d + 2^{d-1}Σℓ_j|u_j|_1,
    which the proof actually gives, also has maximum ratio 1.0000. The maximum of N/(3^d(1 + ℓ)) is 0.36 (d = 2) and
    0.20 (d = 4).
- **Polymer enumeration** (`rev1112/polyenum.py`, exhaustive, *-connected polymers containing the origin):
  - d = 2, n ≤ 6: counts 1, 8, 60, 440, 3190, 22992, all ≤ 8^{2(n-1)};
  - d = 4, n ≤ 3: counts 1, 80, 7320, all ≤ 80^{2(n-1)} ((g3)).
  - An exact d(X) for polymers is a Steiner problem and was not computed. The segment test is strictly stronger:
    any τ admissible for X has |X| ≤ N(τ).
- **Fix (scope).** Dimock's (122) has two inequalities, d_M(X) ≤ |X|_M ≤ 3^d(1 + d_M(X)). CE-geo' proves only the
  second. "proves Dimock's (122)" at l.1599, 1957, 1961 and 3445, and in RTARGET §19, should read "proves the upper
  bound in (122)". The first half is not used anywhere, and under the touching reading for *-connected polymers it is
  not obvious. Also note that Dimock works in d = 3; (122) is "here with d = 3".

### Lemma N2-a (l.1993-2028; counted with N2-E): CONFIRMED-WITH-FIX (SU(N) wording)

- **Abelian: CONFIRMED.**
  - The least-squares residual is the projection P^⊥NB_k, which is linear in B_k.
  - Closed data have E_k = 0 by N2-E. So the residuals depend on dB_k only.
- **SU(N), flat case: CONFIRMED.**
  - Flat on the lattice torus means the commutator loops are contractible, so the holonomies commute. They are
    simultaneously diagonalised, with tr Θ = 0 after a 2π shift.
  - The constant field D has the same based holonomies, so V_k = D^h.
  - The commuting lift has M̄_c = Wexp(iΘ_μL/T_i)W^{-1} = V_{i+1,c} ∈ SU(N), so φ_c = 0.
  - Every global minimiser therefore has every term equal to 0.
- **SU(N), "is a function of the coarse gauge orbit" (l.2000, l.2026): CONFIRMED-WITH-FIX.**
  - Step (i) shows that coarse gauge transformations map the SET of global minimisers bijectively, with every
    gauge-invariant quantity preserved.
  - Uniqueness of the global minimiser up to the chain gauge group is not shown for SU(N). So "R_top is invariant" is
    a statement about the set of minimiser values (equivalently, min and max over minimisers).
  - Fix: "the set of values at global minimisers is an orbit invariant". At small curvature, uniqueness is part of
    N2-SU(N) (OPEN). The flat-class statement is unaffected.

### Lemma N2-E (l.2029-2067): CONFIRMED

Every count was re-derived.
- **Fine action.** At most 24L^{4k} fine plaquettes are assigned per cube; the true number is 6L^{4k}, so this is
  harmless. Each coarse plaquette lies in 4 cubes in d = 4, so the fine action is ≤ 96||dB_k||².
- **Residual per link.**
  - The window is a box of sup-side 2L^{-m}, since level-i spacing is L^{-(m+1)}.
  - 2L(L - 1)L^{-2(m+1)} ≤ 2L^{-2m}.
  - (W4) with j = 2 gives the Lipschitz constant 4, so the oscillation is ≤ 8L^{-m}M_C, and the link bound is
    16L^{-3m}M_C.
- **Counts.**
  - 64L^{4m} links per cube: 64·256 = 16384.
  - Boundary links: 8 faces × 4 layers × 8L^{3m} × 4 directions = 1024L^{3m}, each ≤ 16L^{-4m}M'².
  - 16384(1 + 7⁴)L^{-m} = 3.94·10⁷ ≤ 4·10⁷.
  - With 4 cubes per plaquette, 1.6·10⁸.
- **Sum.** Σ_mL^{-m} ≤ 3/2, so E_k ≤ 48 + 1.2·10⁸κ_+.
- No factor of k appears: the centring cancellation gives L^{-m} per level. Correct.

### Proposition N2-red with Lemma LES-sup (l.2069-2084): CONFIRMED

- LES step 5 with b = 4 + 2α gives ρ^{-4}φ(ρ) ≤ C(ρ/R_1)^{2α}[R_1^{-4}φ(R_1) + R_1²(J_0 + K_0)²]. The dyadic
  telescoping to the one-site box is then standard.
- The (H1) arithmetic, including R = 3L^k ≥ 16 for k ≥ 2, and the factors 1/9 and 3κ_{k-1}, is right.

### Lemma FP-ab and its application (l.2132-2179): CONFIRMED

- **The lemma.** The change of variables plus Fubini is right.
- **The group.** Λ = {λ : λ(c_X) = 0} acts freely. ev λ constant is the exact invariance condition, since Qd = d ev and
  Q(const) = L·const.
- **Admissibility.** dim: N_c + (N_f - 2N_c) = N_f - N_c. For χΓ to be injective:
  - h(dλ) = Mλ (since λ(c) = 0), so h(dλ) = 0 gives λ ∈ Λ_res;
  - then ⟨λ, P_resΔ_0λ⟩ = ||dλ||² = 0, so λ = 0.
- **The double fixing.**
  - ∫_{Λ_res}e^{-½||d*A + Δ_0λ||²} = c·e^{-½||(1-Π_r)d*A||²}.
  - rank(1 - Π_r) = (N_f - 1) - (N_f - 2N_c) = 2N_c - 1.
  - The block-constant ψ example is valid: h(dψ) = 0, and ψ ∉ Λ_res + const unless ψ is constant.
  - Such dψ is NOT a symmetry direction (Qdψ = d ev ψ ≠ 0), so W varies on the quotient, and ∫I·W ≠ c∫I for general
    invariant F.
- **The claim that L3g(a)-slice's double fixing is invalid: CONFIRMED** in exactly the form stated, "not legitimate as
  an identity". Its operator inequality on H_0 (PROVEN, S3) is still true; what fails is its use as the gauge-fixed
  fluctuation operator. That is consistent with the R3-fix, which already marked it CONDITIONAL on (FP).
- **The O_FP decomposition.**
  - The cross terms vanish, since Qdλ = d ev λ = 0.
  - The coarse-unit Neumann block eigenvalue 4n²sin²(π/2n) ≥ 4 gives ||P_resΔ_0λ|| ≥ ||dλ||²/||λ|| ≥ 2||dλ||.
  - A^ph ∈ H_0 ∩ (dΛ_res)^⊥ = Phys.
  - So O_FP ≥ min(c, 4). Right.

## (2) Session-12 PROVEN-HERE items

### Theorem N2-lin, with IT-str, LED-dual, LED-symb, WA and LED-unif (l.2186-2350): CONFIRMED-WITH-FIX

- **IT-str.** Re-derived for m = 2:
  - y ∈ B(Y + je_μ) = B(Y) + jLe_μ gives the length-L² straight line;
  - ∪_{Y∈B(X)}B(Y) = L²X + {0..L²-1}⁴, with weight L^{-8}.
  - Q_root^T preserves co-closedness and equals Q_str^T on co-closed forms.
  CONFIRMED.
- **LED-dual.**
  - (i): r_i and J_0 = -κ_{k-1}Q_str^{(n)T}r follow by iterating J-str (b) with IT-str.
  - (ii) zero mean: J_0 ⊥ constants, and Q_str^{(n)}(const) = n·const.
  - (ii) closed: B_k ≡ Q_str^{(n)}Δ^{-1}J_0 - ΣQ_str^{(L^{k-1-i})}r_i mod Closed, using Q_root^m = Q_str^{(L^m)} + exact
    and Q(Closed) ⊂ Closed. This gives -Pr exactly.
  - (iii): P ≥ I (the m = 0 term is the identity), stationarity in CoCl_0 ⟺ Ps + B_k ∈ Closed, and the energy
    identity.
  CONFIRMED.
- **LED-symb.** The Lagrange solution was re-derived:
  - P̂_μr̂_μ + b̂_μ = λν_μ with Σν̄_μr̂_μ = 0 gives r̂_μ = -P̂_μ^{-1}Σ_νP̂_ν^{-1}ν̄_νF̂_{νμ}/D, as stated.
  - The P̂ normalisation matches the c26 criteria (n_m^{2-d} = L^{-2m}).
  - The G-term n^{-2}/φ_f(θ/n) = 1/φ_n(θ).
  - c26 A reproduces r and f_0 to ≤ 4.3e-13, and so did my re-run.
  CONFIRMED.
- **Lemma WA: CONFIRMED-WITH-FIX.**
  - The dyadic piece is O(2^{-ja}) in ℓ¹ (the region |X| ≲ 2^j contributes 2^{-4j}·2^{4j}; the rest is
    2^{-4j}2^{5j}Σ_{|X|>2^j}|X|^{-5} ~ 1). This is summable for every a > 0.
  - **Fix (l.2252 vs l.2265):** the lemma is stated for a ∈ (0, 1], but it is used with a = 2 for 𝓡̂. Either state
    "a > 0" (the proof works) or note that type a = 2 implies type a = 1 on |p| ≤ 1.
  - **Fix (l.2262):** replace "h(0) is the limit h_0(0)" by "the p = 0 mode is irrelevant, since F̂(0) = 0 for
    F = dB_k". The finite-T operator's value at p = 0 (r̂(0) = 0) need not equal the limit.
- **LED-unif.** Checked:
  - |D_s| ≥ 2/π on |θ| ≤ π; φ_s ≥ (4/π²)|θ|² on [-πs, πs]⁴; the only singular alias is p ∈ 2πZ⁴;
  - the alias-sum decay, including the 3D shell sum (log R)²/R², which is summable;
  - P̂ ≥ 1 from the m = 0 term; g_ν(0) = 1/κ_{k-1} exactly, since W(0) = 1 and φ(0) = 0;
  - u = O(|p|⁴), because u is even and both quadratic terms are Σp²;
  - the quotient rule gives type 2;
  - (4): Π_ex + Π_coex = I from dd* + d*d = ψ, so 𝒦̂_u + Π_coex = e^{ip·u/n}I + (1 - e^{ip·u/n})Π_coex + type 1, where
    (1 - e^{ip·u/n}) = O(|p|) with |u/n| < 1. It is uniform in u.
  The closed-data restriction is legitimate: Π_coexdB_k = 0 identically, so the representative changes nothing on
  the data. CONFIRMED.
- **Constants.** 486 = 6·81 fine plaquettes per Ĉ; 324 = 4·81 links per level; 162·(9/8) = 182.25 ≤ 183.
  C_loc = 243C_f² + 183κ̂κ_+C_R². CONFIRMED.
- **Where "linearised" or the scope is dropped:**
  - **Header l.19:** "So BG-b holds for the linearised soft chain with no further hypothesis." Add "at small coarse
    curvature (BG-b (b1) needs M_2 ≤ ε_*), for the levels n ≥ 1; the n = 0 term needs the current step's residual".
    l.2343-2344 has "at small coarse curvature" but not n ≥ 1.
  - **Tally l.3427:** "(LED) is proven" → "(LED) is proven for the linearised chain".
  - The theorem statement (l.2308-2310), the tally entry (l.3420), the L2 note (l.559-561) and N2/N3 (l.1901-1902) keep
    "linearised". They are correct.
- **The power-tail remark (l.2305-2307): CONFIRMED-WITH-FIX (overstated).** "The kernels used here have non-analytic
  terms at p = 0, so the proof gives ℓ¹ bounds (power tails)" should read "the proof gives only power-tail BOUNDS".
  - Type a = 2 is an upper bound on the regularity loss. That u/v is genuinely non-analytic is not shown.
  - Informational (`rev1112/rdecay.py`, using c26's own symbol code, d = 4, κ = 1, T = 32): along a coarse axis the
    max component of the dB_k ↦ r kernel falls 1.1e-7 → 3.1e-8 → 9.4e-9 → 2.9e-9 → 8.9e-10 (x = 10..14). That is a
    constant ratio ≈ 0.30 per coarse unit at k = 1, and ≈ 0.31-0.32 at k = 3, down to ~1e-10.
  - A |x|^{-6} tail would give a ratio of 0.6-0.7 there.
  - So the r map looks exponentially decaying. Only the f_0 representative's (1 - e^{ip·u/n})Π_coex term is
    certainly non-analytic, and another representative on closed F may avoid it. This is exactly the open N10
    question (see the strategic verdict).

### Proposition PG with PG-flux, PG-orbit, PG-ext, PG-line (l.2351-2430): CONFIRMED

- **Definitions.** H_0 = {h = 0} and Phys = {h = 0, d*A ∈ span(δ_{c_X}, 1_{B(X)})} = H_0 ∩ (dΛ_res)^⊥. So the Phys
  element of an orbit is its minimal-norm element, and the PG statement ⟺ the gap. Consistent with FP-ab.
- **PG-flux (a).** d*A summed over a block telescopes to the face fluxes.
- **PG-flux (b).** The tent weights sum to 1 per column, and |a(t) - a(n-1)| ≤ ε√(2n)||∂a||. Cauchy-Schwarz over the
  n³ columns gives 2ε⁴Σ|∂a|² = 2||∂_μA_μ||²_slab, and ≤ 2 slabs per bond gives the 4.
- **PG-orbit.** ψ + Λ_res = {φ : φ(c) = ψ(c), Mφ = Mψ}. A_c ⊥ exact forms, and h(A_c) = r - m since h(dψ) = m - r.
- **PG-ext.**
  - Interpolation: ε⁴(2n + 1)³(n + 2) ≤ (7/3)³(5/3) = 21.2 ≤ 22.
  - The bump: b_n = (n tan(π/(2n + 2)))⁴ ≤ (π/2)⁴, and ||dβ||² ≤ (π/2)^{10}(n + 1)²/n² = 162.5 at n = 3.
  - The spike: 8 bonds × ε⁴/ε² = 8ε², and ||dγ||² ≤ 12.8ε² at n = 3 ≤ 20ε².
  - "Collect" is not itemised. With weights (4, 4, 2) on (φ̃, bumps, spikes): 4·22 + 4·2·163·216 +
    2·2·20·2·(π/2)⁸·216/9 = 4.24·10⁵ ≤ 4.25·10⁵, and the r - m coefficient is 2·2·20·2 = 160. That matches the stated
    lemma; write the split out (recommendation).
- **PG-line.**
  - C_3 ≤ (2/n)Σ|k|^{-2} ≤ 14(n - 1)/n.
  - The legs are in distinct directions, so Σ_legs sums distinct components: 4ε[2ε³ε^{-4}||A||² + 2C_3ε^{-2}||∇A||²]
    = 8||A||² + 8C_3ε^{-1}||∇A||². Right.
- **Main chain.**
  - (1) L3g(a)-glob on co-closed A_c.
  - (2) F(A_c) ⊥ d_cMψ.
  - (3) ||A_c||² ≤ 5||dA||² + 2(||QA|| + 4||dA||)² ≤ 69||dA||² + 4||QA||².
  - (4) 143.2·69 + 4.25·10⁵·8 + 427·14 = 3.416·10⁶ ≤ 3.5·10⁶ for ||dA||², and 573 + 8.5·10⁵ for ||QA||².
- Uniform in n odd ≥ 3 (ε ≤ 1/3) and T ≥ 2. **CONFIRMED.**
- **Scope.** One linearised abelian step with the direct S4' slice. (IT') and (NA) are honestly left OPEN (l.2425-2430).

## (3) Non-item statements

- **(LED) attempt [S11] (l.2085-2100).** Argued, not counted. It was superseded in S12 by a different route, which is
  fine.
- **B-NA.** Not attempted in S12 (RTARGET §22 was optional). Honest.
- **N5 "no longer needs N2's linear half or the abelian gap" (l.2429-2430).** True for the linearised one-level
  inputs. N5's ℓ¹ covariance bound and random-walk expansion still need decay of the actual soft Hessian inverse,
  which is a different object from the chain-response kernels. Keep them separate.
- **Imports.** No [S11]/[S12] PROVEN-HERE item uses an IMPORTED-NOT-YET-REVERIFIED premise:
  - CE-geo' is self-contained;
  - N2-E, N2-red and N2-lin use CR, J-str, LES, the L3g(a)-slice identity and IT-str (all PROVEN);
  - FP-ab is algebra;
  - PG uses L3g(a)-glob (PROVEN) and FP-ab.

## (4) Checks re-run

Setup: laptop, nice 10, OPENBLAS/OMP/MKL/vecLib threads = 1, sequential runs, no `timeout`. Free memory and load were
measured before each run: c24 started at 45% free and load 2.9. Outputs are in `rev1112/`.

| Check | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c21 (s11) | 14/14 PASS | 6.1 s | 34 MB | identical except runtime |
| c23 A | VALID; Q1, Q2 PASS, Q3 FAIL | 72 s | 466 MB | identical except RSS line |
| c23 B | VALID; Q4-Q6 PASS | 280 s | 447 MB | identical except RSS line |
| c24 | VALID; Q1 PASS | 191 s | 1.75 GB | identical except timing |
| c25 | Q1 PASS | 7.6 s | 40 MB | byte-identical |
| c26 A/B/C | A all PASS; B Q5, Q6 PASS; C V3 PASS, Q7 FAIL | 4.9 / 57 / 82 s | 458 / 177 / 846 MB | identical except timing/RSS |
| c27 | E3 FAIL, others PASS | 15 s | 335 MB | identical except RSS |

**Provenance (UTC, from the transcripts).**
- **Session 11.**
  - RTARGET §16-18 at 14:58:00.
  - c21 addendum and c23/c24/c25 criteria at 14:58:41.
  - Scripts: c21 14:59:13, c25 14:59:54, c23 15:01:40, c24 15:10:15.
  - The R910 fixes were applied 15:04-15:06.
  - The derivations were inserted 15:15:23-15:17:27, after every run.
- **Session 12.**
  - RTARGET §20-22 at 15:41:36.
  - c26 criteria 15:45:24, script 15:47:39. Part A 15:48:59, Part B 15:49:15.
  - The addendum at 15:50:55. Part C was appended and run at 15:51:41.
  - c27 criteria 15:53:38, script 15:54:59, run 15:55:25.
  - The derivations went into PROOF at 16:01:40; §23 at 16:02:50.
- **Target weakening.** No target was weakened:
  - §20's "numerics in place of a proof" exclusion is respected;
  - §20 was met in its stronger "sufficient intermediate" form;
  - §16's (N2-c) failure in S11 was recorded as such.
- §20's own header discloses that the lead's exploratory reasoning preceded it. That weakens pre-registration (the
  route was known), honestly.

**c23: CONFIRMED.**
- The Q3 FAIL is a criterion-design flaw (the values decrease in k). It is recorded and not edited.
- Part B's Q4-Q6 directly test the first lemma's claim: residual at the curvature scale, not the field scale.

**c24: CONFIRMED.**
- Informational only, as stated: FP-ab is algebra, and the gap is proven by PG, not by c24.
- The dense-to-sparse pre-run rewrite is disclosed.

**c25: CONFIRMED.**
- Its random trees rarely realise the corner configurations that saturate the bound. My exhaustive grid tests above
  cover them.

**c26: CONFIRMED-WITH-FIX.**
- **Part A tests the load-bearing exact formulas** (LED-dual, LED-symb, the f_0 Bloch formula). The uniform bounds
  (WA, LED-unif) cannot be tested numerically, and Parts B/C are honestly informational.
- **Is the addendum acceptable? Yes.**
  - It was written after Parts A-B, and its idea (the Π_coex representative) was designed in response to Part B's
    T-growth. So Part C is confirmatory of a post-hoc idea.
  - But the criteria V3/Q7 preceded Part C's code and run (15:50:55 < 15:51:41), A/B code was not changed, Q6 is not
    edited, and its limitation is stated.
- **Q7's FAIL** (1.104 > 1.1) is honest. The c/T reading is consistent with WA: a periodised ℓ¹ kernel with an
  |x|^{-5} tail converges like 1/T.
- **Fix (l.2336):** label "fit c/T: a summable |x|^{-5} tail" as an informational reading, not a criterion, as
  c26_time.txt already does.
- Part B's "axis slope(3..7)" is a log-log slope taken up to x = 7 on a T = 16 torus (x ≈ T/2, where periodic images
  matter). Its κ-dependence (-5.1, -7.1, -11.7) shows it is not a power-law exponent. It should not be quoted as a
  tail exponent.

**c27: CONFIRMED.**
- The E3 FAIL is a normalisation flaw. My diagnostic (`rev1112/c27_diag.py`) gives:
  - absolute errors ≤ 1.2e-15 in all 20 cases;
  - relative errors ≤ 2e-13 for every non-pure-gauge vector;
  - the failure is only on the pure-gauge vector, where max|r - m| = 2e-16 to 2e-14.
- The deletion of the two unused helpers before the run is disclosed.

## (5) Overclaims in the header and the tally

- Header l.19: the BG-b scope (small curvature, n ≥ 1). Tally l.3427: "(LED) is proven" needs "for the linearised
  chain".
- l.1599, 1957, 1961, 3445 and RTARGET §19: "proves Dimock's (122)" → "the upper bound in (122)".
- l.2305-2307: "power tails" → "only power-tail bounds".
- l.1697: the Dimock citation (l.1672, §4.7).
- l.2000, 2026: the SU(N) orbit-function wording (set of minimiser values).
- The counts are right: 53 + 2 = 55. No OPEN item closes: the N4 completion keeps (NA)/(IT'), and N2 keeps SU(N) and
  N10.

## Verdict counts

**PROVEN-HERE tally items: 6.**
- 2 CONFIRMED: Proposition N2-red (with LES-sup), Lemma FP-ab (with its application).
- 1 CONFIRMED, with one recommendation (itemise PG-ext's "Collect"): Proposition PG (with PG-flux, PG-orbit, PG-ext,
  PG-line). All its constants were re-derived.
- 3 CONFIRMED-WITH-FIX:
  - Lemma CE-geo': the (122) scope;
  - Lemma N2-E: its own proof is CONFIRMED; the fix is in N2-a's SU(N) wording;
  - Theorem N2-lin: WA's a-range, the p = 0 remark, the power-tail wording, the header/tally scope.
- 0 GAP and 0 WRONG.

**Non-items.**
- The R910 residues (a), (b), (c).
- The c26 labelling fix.
- The N5 decay distinction.

**Corrected tally: 55 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path) + 1
comparison branch.** This is unchanged from the session's own count. Sessions 11-12 are now reviewed.

## Required fixes (binding for session 13)

1. **l.1697.** The citation becomes "§4.7 (after (243)), l.1672 of the extracted text", not "the proof of his Lemma 21,
   l.2731".
2. **checks/c21_criteria.md.** Append (do not edit l.52-53) one annotation: the session-10 "is false" reading is
   withdrawn per REVIEW_S9_S10 fix 1; I4 carries the argument.
3. **Fix-13 label (l.8-10, 120-125, 3433-3436).**
   - Say "by inference from the TOE-ruleset delegation".
   - Explain why the 10-23 "(put it in the CL …)" does not apply to a proof-method choice.
4. **CE-geo' scope.** At l.1599, 1957, 1961, 3445 and RTARGET §19, "proves Dimock's (122)" → "proves the upper
   inequality of (122) (Dimock: d = 3)". Optionally record the sharper Σℓ_j|u_j|_1 form.
5. **N2-a SU(N) (l.2000, 2026).**
   - "a function of the coarse gauge orbit" → "the set of values over global minimisers is an orbit invariant".
   - Uniqueness up to the chain gauge group is part of the OPEN SU(N) N2.
6. **Lemma WA (l.2252, 2262).**
   - "a ∈ (0, 1]" → "a > 0".
   - Replace the h(0) sentence by the F̂(0) = 0 remark.
7. **Power-tail wording (l.2305-2307).** "gives ℓ¹ bounds (power tails)" → "gives only ℓ¹ / power-tail bounds; whether
   the r map is exponentially local is open (numerically it appears to be)".
8. **Scope.**
   - Header l.19 and l.2343: add "for the levels n ≥ 1 (the n = 0 term needs the current step's residual), at small
     coarse curvature".
   - Tally l.3427: add "for the linearised chain".
9. **PG-ext.** Write the "Collect" split (weights 4, 4, 2) and the resulting 4.24·10⁵ and 160.
10. **c26 reporting (l.2336).**
    - Label the c/T fit informational.
    - Do not cite Part B's axis slopes as tail exponents (κ-dependent, x up to T/2).
11. **N5 note (l.2429-2430).** Distinguish the chain-response kernels (N2) from the soft Hessian covariance (N5). N5's
    ℓ¹ / random-walk bounds are still fully OPEN.

## Strategic verdict: the next target

**First a short decisive linear target, "N2-exp": exponential locality of the linearised soft chain on closed data.
Then the SU(N) chain. (IT') is the short parallel item. N5 after; N6 last.**

- **Why N2-exp first.**
  - Theorem CE needs activities |H(X)| ≤ H_0e^{-κd(X)} with κ > 457 in M-units (N6), and N10 needs smooth dependence
    with decay.
  - Under decision 4 those decay rates must ultimately come from the soft background map and the soft covariance. ℓ¹
    kernels with power tails, which is all N2-lin proves, cannot feed a polymer expansion with exponential weights.
  - So the viability of decision 4's soft kernel for N6 hinges on whether the response is exponentially local.
  - The numerics are favourable for r: a ratio of ≈ 0.30 per coarse unit, k-stable, down to 1e-10. The question is
    linear, translation-invariant and Fourier-tractable (Paley-Wiener: analyticity of 𝓡̂ and of some closed-data
    representative of the f_0 map in a strip |Im p| < m, uniformly in k).
  - Concretely: show u/v = (φ_n - κD_g)/(κD_g) is analytic (or isolate a gauge choice for B_k that makes it so).
    Otherwise identify the obstruction.
  - If the answer is negative, decision 4 must be revisited (the soft kernel's κ, or Balaban's hard constraint from the
    comparison branch) BEFORE investing in the SU(N) transfer.
- **Then the SU(N) chain: B-NA (i)-(iii) with constants, and N2-lin(SU(N)).** The route is contraction around the flat
  lift (N2-a (iii)), using the linear kernels. This is easier if they are exponentially local.
- **N4-NA/IT'.** (IT') is linear and short: the composite slice functional h^{(m+1)} = Mh^{(m)} + hQ_root^{(m)}, and
  PG-line for composite funnels. It is a good parallel item. (NA) goes with the SU(N) chain.
- **N5** needs the actual soft Hessian covariance (ℓ¹ and random walk), after N2-exp and N4.
- **N6** comes last (κ > 457).
- **D4-obs** stays listed. Its form also depends on whether decision 4 survives N2-exp.
