# RLARGE: the 4D large-field R-operation for the soft-kernel RG (session 17, 2026-10-27; repaired session 18)

**Session-18 header [R1617-fix].** REVIEW_S16_S17.md (independent hostile review of this file as written in session 17;
that version is kept verbatim as RLARGE_session17_snapshot.md, to which the review's line numbers refer) is applied
here; every change is tagged **[R1617-fix]** with the review's fix label. Session-18 targets were pre-stated in §13
(21:47 UTC) before any repair text and before the c33 criteria. Summary:
- **R-3b (the B_4 step, review verdict GAP): repaired** (§7.2 (iii)). The base-point localisation now uses the
  UNFATTENED supports S = ∪Y_i of cluster tuples; the family {S ∋ x} is genuinely permuted by B_4 about x, and GT-lat' (ii)
  applies. The value of the coupling shift is unchanged (Remark 7.2-B: on the reference data the two localisations agree);
  only the written step was false. c33 (criteria first) exhibits both facts (B PASS; A FAIL as pre-registered on a float
  artefact of the brute-force side, see §9).
- **R-3a, R-4, R-5:** cluster size bounds from (H-ch) (Lemma 7.2-0); torus wrap handled by a width W and a bounded wrap
  term (§7.2 (iv)); TS's hypotheses on the region Δ_* that R1 uses, with g² < a''/3 (§7.3).
- **R-6:** "remainder of irrelevant order" narrowed: of order 𝔯(D), irrelevant for BG-b-regular frozen data only; in a
  sea sample 𝔯 = O(g²) (§7.2 Reading, §7.4). TS is the frozen-background shadow and is not used by RLF-step.
- **R-1, R-8 (two-threshold R-operation), R-2 (Z_ref), complex fields, R-9 (product measure; RS ordering), R-7a/b,
  (P1)/(P4)/§8.5, R-10, CL-1:** §1A (RLF amended; §1 kept verbatim, numbering unchanged, one item (RLF-5) added), §5 (d),
  §7.1, §8.2-§8.5, §9, §11.
- **Tally:** the review's corrected count is 67/2/7/24 + 1 (TS/R1 held at GAP). With R-3a/R-3b/R-4/R-5 written, TS/R1 is
  counted again as PROVEN-HERE [S18-repair, unreviewed]: **68/2/7/24 + 1** (§12).

Scope. Balaban's large-field renormalisation (CMP 122 (1989) 175-202 and 355-392) is [not-read]; no open source states
it (literature/NOTES.md §10: OSTI abstracts [read-abs]; Dimock II p.31 Remark 3 [read]: the R-operation "converts some
large field contributions back to small field contributions" and is "not necessary" for φ⁴_3). Nothing below is
attributed to Balaban. Everything here is for the decision-4 kernel (S4' contour averaging, normalised soft
gauge-covariant constraint; PROOF.md L5 [S9]). Status words as in PROOF.md: PROVEN-HERE (counted or not, said each time),
ARGUED, OPEN, HYPOTHESIS. Imported items are never load-bearing for a PROVEN-HERE claim.

Inputs used (PROOF.md, read by offset this session): LF-count (L6loc [S6]); R2D-iso, R4D-iso, GT (L5 [S7]-[S8]);
D4-norm, GT-lat, R4D-lat, BG-sum, W1-size', W1-LD-cond, (DF) (L5 [S9]); Theorem CE and Lemma CE-geo' (L5 [S10]-[S11]);
the (DF) sub-DAG N1-N12; inequality (B) and E8*/E8** (L6loc); L6; RTARGET.md §0-11 (in particular §7, the W2
pre-statement); REVIEW_S15_CONVERGENCE (critical path, node B-W2); LINEAR_PACKAGE.md §9-10.

File order. §0-§2 were written at 2026-10-27 20:58 UTC, after reading the inputs and after the lead's exploratory
reasoning in this session, BEFORE any written derivation in §3 onward and before the c32 criteria and script. §0-§2 are
not edited after the derivations start; outcomes are pointers in §9, added afterwards.

---

## 0. Conventions fixed for this file

- **Levels.** Level k = after k RG steps; k = 0 is the bare (finest) lattice, k = K the unit lattice. (This matches
  LF-count's N_k = L^{4(K-k)}|T| count; it is the reverse of Setting S1's "resolution" index.) U_k is the level-k field on
  Λ_k, d = 4, L ≥ 3 odd, G = SU(N), N ≥ 2.
- **Action normalisation** (R4D-iso's): s(U) := 1 - N^{-1}Re tr U ∈ [0, 2]; level-k Wilson term (1/g_k²)Σ_p s(U_p).
  Inequality (B): s(U) = ||1 - U||²_HS/(2N) ≥ ||1 - U||²_op/(2N).
- **The exact chain.** e^{-S_0} := Wilson at g_0; e^{-S_{k+1}(V)} := ∫K_k(V, U)e^{-S_k(U)}dU, with the normalised soft kernel
  K_k = Π_c k_c, k_c = exp(-(κ/g_k²)[1 - N^{-1}Re tr(V_c^{-1}M̄_c(U))])/𝒩_k(M̄_c(U)) (D4-norm). ∫K_k dV = 1, so
  Z_K = ∫e^{-S_k}dU_k for every k. The joint law of (U_0, …, U_k) is a Markov chain.
- **Level-k cubes.** A level-k cube □ is a level-k block (L⁴ level-k sites; one level-(k+1) site); N_k := L^{4(K-k-1)}|T|
  cubes. Small-field indicator χ_□ := Π_{p⊂int □}1{||1 - U_k(p)||_op < ε_1} (R4D-iso's cut); ζ_□ := 1 - χ_□.
- **Flow hypothesis (F)** (the AF flow, OPEN as A5 / L4a-flow; the lower half is the one used for summability):
  β_-(k - j) log L ≤ 1/g_j² - 1/g_k² ≤ β_+(k - j) log L for 0 ≤ j ≤ k ≤ K, with 0 < β_- ≤ β_+.
- **Polymers.** A level-k cluster Y is a nonempty *-connected set of level-k cubes (cubes adjacent iff their closures
  meet); |Y| := its number of cubes. *-separated clusters are at cube distance ≥ 2.

## 1. Target 1: the statement RLF (pre-stated)

> **[R1617-fix, session 18] RLF's statement is amended in §1A below.** This pre-stated text is kept verbatim. The item
> labels (RLF-0)-(RLF-4) keep their meaning and numbering; (RLF-1), (RLF-2), (RLF-3) and (RLF-4) are amended, (RLF-0)
> is re-indexed (connected tuple supports instead of cluster shapes), and one item, **(RLF-5) complex fields**, is
> added. Readers of §1 should use §1A.

**What a 4D large-field R-operation must deliver** (the reconstruction target LF-count names, in the soft setting):

**Theorem RLF (target; OPEN).** There are g-independent constants ε_1 > 0, a > 0, κ_d > 0, C, an integer n_* ≥ 0 with
(n_* + 1)aβ_- > 4, and g_0 > 0 such that for every K, every torus T (side ≥ 3 blocks at level K) and every coupling
sequence with g_K ≤ g_0 obeying (F):

- **(RLF-0) Counterterms.** For each level k and each cluster shape Y with |Y| ≤ n_* (shapes up to translation), there
  are a field-independent number c_0(Y; g_k) and a field-independent Ad-invariant quadratic form T_Y(g_k) on
  su(N) ⊗ Λ²R⁴, with |c_0(Y; g_k)| + ||T_Y(g_k)|| ≤ C^{|Y|}e^{-a|Y|/g_k²}, depending only on (Y, g_k, L, N, κ, ε_1) and on
  the shape class (translation covariant; B_4-covariant). The marginal parts combine per level into ONE coupling shift
  δβ_k := Σ_{[Y]}t̄_{[Y]}(g_k) (B_4-orbit averages), with Σ_k|δβ_k| ≤ Ce^{-a/g_K²} uniformly in K and |δβ_k| ≤ g_k^6.
- **(RLF-1) Exact factorisation of the vacuum part.** Z_K = exp(Σ_{k<K}Σ_{Y: |Y|≤n_*}c_0(Y; g_k)) · Z_K^{ren}, where the
  inner sum runs over all placements of all shapes at level k (so the prefactor is a field-independent c-number,
  Σ_k O(N_k e^{-a/g_k²}), the only K-divergent quantity, which LF-count shows to be divergent).
- **(RLF-2) Returned (recycled) contributions.** In Z_K^{ren} every level-k cluster of ≤ n_* bad cubes with a small-field
  collar is returned to the small-field region: its contribution is the remainder R(Y) after subtracting c_0 and the
  T_Y-term, with |R(Y)| ≤ C^{|Y|}e^{-a|Y|/g_k²}·𝔯_k(Y) and 𝔯_k(Y) the GT-lat remainder functional of the level-(k+1)
  background on Y's box, and with exponential tails e^{-κ_d d(X)} in its dependence on the far field; and per final
  unit cell, Σ_{k}Σ_{Y in the cell}|R(Y)| ≤ C sup_k(C e^{-a/g_k²}) uniformly in K (summable against L^{4(K-k)}).
- **(RLF-3) Unreturned large fields.** Clusters with |Y| > n_* (and clusters whose collar is not small-field) stay
  large-field regions, nested as in Dimock II (small-field regions decrease with k), with weights
  ≤ Π_Y(Ce^{-a/g_k²})^{|Y|}, and Σ over all such histories ≤ exp(C|T|e^{-(n_*+1)a/g_K²}).
- **(RLF-4) Output.** |log Z_K^{ren} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} uniformly in K (any a' < a), where Z_K^{sf} is the
  small-field partition function of the soft RG with couplings shifted by δβ_k. Together with the small-field package
  (node A), this is L6-soft modulo the vacuum c-number of (RLF-1).
- **Composition.** With **LF-count**: the divergent per-level sum of LF-count sits entirely in the c-number of (RLF-1).
  With **R4D-iso**: the case |Y| = 1, frozen exterior, is R4D-iso/R4D-lat/D4-norm (c_0 = log(1 + ρ_0), T_Y = c_ρ-term).
  With **Theorem CE**: at level K the remainders R(Y) and the unreturned large-field polymers are activities H(X) obeying
  |H(X)| ≤ H_0e^{-κd(X)} with κ > 3κ_0 + 3 (≈ 457 in M-units) and H_0 ≤ c_0(κ), for g_K small enough (to be made
  explicit).

## 1A. Theorem RLF, amended [R1617-fix, session 18] (target; OPEN)

**Change log against §1** (for every reader of §1, including the sister lane):
1. **One exponent.** a := a_♯ := min{a'', a_♭, a_RS/c_RS} (§7.1), and RLF's integer is n_♯ := ⌊4/(a_♯β_-)⌋, so
   (n_♯ + 1)a_♯β_- > 4 as §1 requires. n_♯ ≥ n_* (§7.1); it is g- and K-independent, and very large for the crude
   constants (§9 C, [inference]).
   **[R1819-fix 8, compatibility with N5]** Theorem N5-sf0's small-field class (PROOF [S19]) requires plaquette curvature
   and soft fluctuation ≤ ε_* (≈ 2·10⁻³²/C_Δ proven, ≈ 1.7·10⁻²⁴/C_Δ with N5-w0), while this file's small-field cubes use
   ε_1 ≤ 2 and ε_loc ≈ 3.5·10⁻³. For the small-field package to cover this file's small-field region, the R-operation's
   thresholds (ε_1, ε_loc) must be ≤ the N5 threshold in matching units. Then a'' ∝ ε_1² and n_♯ become astronomically
   larger, still g- and K-independent. Only finiteness is used, so this is a compatibility condition on the constants, not
   a gap; it is recorded here and in (SF).
2. **(RLF-2)/(RLF-3), fix R-1: two thresholds.** Returned vs unreturned is decided by the defect number alone, not by
   the collar. A level-k **defect configuration** is a *-connected set 𝒟 of level-k cubes each of which is bad
   (ζ_Q = 1) or collar-bad (ε_♭(U; Q) > ε_loc, or (H-ch) fails on Q's box); n(𝒟) := |𝒟|. Every defect configuration
   with n ≤ n_♯ is returned, whether or not its collar is small-field; exactly those with n > n_♯ stay unreturned.
   (§1's (RLF-3) bound for collar-bad clusters with few cubes is false: their weights (Ce^{-a/g_k²})^{small}, summed
   with L^{4(K-k)} placements, diverge, as LF-count says.)
   **[R1819-fix 8]** n_♯ depends on c_RS = 5⁴, which is ARGUED (§7.1); no counted item depends on n_♯ (Theorem R1 holds
   for every cutoff n_c ≥ n_*).
3. **(RLF-0)/(RLF-1): re-indexed and finite-volume-qualified.** Counterterms are indexed by the connected supports S of
   cluster tuples (§7.2), are defined in infinite volume, and are extracted only at levels whose torus side (in level-k
   cubes) is ≥ W := 2n_♯ + 5; the other levels (at most ⌊log_L(W/3)⌋ + 1 of them, at most (81/80)W⁴ cubes in all) give a
   bounded term (§7.2 (iv)).
4. **(RLF-1)/(RLF-4), fix R-2:** Z_K^ref is defined.
5. **(RLF-4), fix R-9:** the hypothesis (SF-last) of §8.2 is added (Theorem CE needs a product measure).
6. **(RLF-5) added:** analyticity in a complex neighbourhood.

**Theorem RLF (amended target; OPEN).** There are g-independent constants ε_1 > 0, a_♯ > 0, κ_d > 0, C, the integer
n_♯ = ⌊4/(a_♯β_-)⌋, and g_0 > 0 such that, for every K, every torus T (side ≥ 3 blocks at level K) and every coupling
sequence with g_K ≤ g_0 obeying (F), with W := 2n_♯ + 5 and T_k := the side of the level-k torus in level-k cubes
**[R1819-fix F2: one convention throughout this file: T is the side of the level-K (unit) torus in level-K sites, so
"side ≥ 3 blocks at level K" reads T ≥ 3, and since a level-k cube is one level-(k+1) site (§0), T_k = T·L^{K-1-k}, the
formula used in §7.2 (iv)]**:
- **(RLF-0) Counterterms.** For each level k with T_k ≥ W and each *-connected cube set S with |S| ≤ n_♯ (up to
  translation) there are a field-independent number c_0(S; g_k) and a field-independent Ad-invariant quadratic form
  T_S(g_k) on su(N) ⊗ Λ²R⁴, with |c_0(S; g_k)| + ||T_S(g_k)|| ≤ C^{|S|}e^{-a_♯|S|/g_k²}, depending only on
  (S, g_k, L, N, κ, ε_1); translation-invariant, and B_4-covariant: c_0(RS) = c_0(S), T_{RS} = Λ²(R)^TT_SΛ²(R). The marginal
  parts combine per level into ONE coupling shift δβ_k := (2N/L⁴)(1/6)Σ_{[S]}tr T_{[S]}(g_k) (sum over translation
  classes), with Σ_k|δβ_k| ≤ Ce^{-a_♯/g_K²} uniformly in K and |δβ_k| ≤ g_k⁶.
- **(RLF-1) Exact factorisation of the vacuum part.** Z_K = exp(𝒱_K^{LF})·Z_K^{ren}, 𝒱_K^{LF} := Σ_{k<K: T_k≥W}Σ_{S}c_0(S; g_k)
  (all placements of all S at level k): a field-independent c-number, the only K-divergent quantity.
- **(RLF-2) Returned contributions.** Every level-k defect configuration 𝒟 with n(𝒟) ≤ n_♯ is returned: its contribution
  after subtracting the c-numbers and the T_S-terms is a remainder R(𝒟) with |R(𝒟)| ≤ C^{n}e^{-a_♯n/g_k²}, local up to
  e^{-κ_d d(X)} tails in the far field, which is an irrelevant small-field polymer activity at level k + 1 in the norm of
  the small-field package. (For BG-b-regular frozen data and 𝒟 without collar-bad cubes, R is of order 𝔯_k(S) of §7.2,
  hence irrelevant; in the fluctuating sea R is what remains after the sea-averaged re-extraction of (W1-ret') in §8.2.
  Its summation over levels and cells is the small-field contraction of node A4, as §10 records.)
- **(RLF-3) Unreturned large fields.** Defect configurations with n > n_♯ stay large-field regions, nested as in Dimock II
  (small-field regions decrease with k), with weights ≤ Π(Ce^{-a_♯/g_k²})^{n(𝒟)}, and Σ over all such histories
  ≤ exp(C|T|e^{-(n_♯+1)a_♯/g_K²}).
- **(RLF-4) Output.** Under (SF-last) (§8.2): |log Z_K^{ren} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} uniformly in K (any a' < a_♯),
  where Z_K^{sf} is the small-field partition function of the soft RG with couplings shifted by δβ_k. **Reference
  normalisation (fix R-2):** Z_K^{ref} := exp(𝒱_K^{LF})·Z_K^{sf,ref}, where Z_K^{sf,ref} is the normalisation with respect
  to which the small-field package (node A) proves its bulk bound exp(-E_-|T|) ≤ Z_K^{sf}/Z_K^{sf,ref} ≤ exp(E_+|T|) (the
  small-field form of L6, as CMP 109's bulk bound (0.30) on E_k is [PROOF L6, read]; that it is a product of per-step
  normalisations is [inference]; its soft-RG definition is part of node A).
  Then (RLF-1), (RLF-4) and node A give exp(-E'_-|T|) ≤ Z_K/Z_K^{ref} ≤ exp(E'_+|T|): **L6-soft for this normalisation.**
- **(RLF-5) Complex fields (new).** The returned remainders R(𝒟), the polymers they feed into E_{k+1}, and the
  large-field factors ℒ_𝔥 are analytic in the coarse field on the complex neighbourhood of the real small-field domain
  that the small-field package uses (N10; Remark CE-cx; the complex tilts of (DF3')), with the bounds of (RLF-2)-(RLF-3)
  up to a factor e^{O(δ)} per cube, δ the complex width. (For one frozen activity r_Y analyticity on SOME neighbourhood is
  ARGUED: the integrands are entire in the complexified data and Den_B > 0 at real data. A g-uniform width is part of
  this requirement and is not shown.)
- **Composition.** With LF-count, R4D-iso and Theorem CE as in §1, except that the level-K step needs (SF-last): Theorem
  CE is a statement about a product probability measure (PROOF L5 [S10], Setting CE), and the level-K integrand is not
  of that form by itself.

## 2. Targets 2 and 3 (pre-stated)

**Target 2: the two-scale case, frozen exterior (W2, extending R4D-iso).** Levels j < k. A level-k cell Δ that is
large-field at level k (some level-k plaquette in Δ has ||1 - U_k(P)|| ≥ ε_1), containing level-j clusters (bad at level j).
Frozen exterior: all variables outside the clusters are given. Claims to prove, with constants stated:
- (T2a) A renormalised identity for each inner cluster with FIXED constants (defined at the trivial background, so
  independent of the level-k field), generalising R4D-iso from one cube to a cluster of ≤ n_* cubes (adjacent cubes allowed).
- (T2b) A bound for the sum of the inner remainders over all inner levels j < k, uniform in j, k and in the size of the
  level-k field, under a precisely stated regularity hypothesis on the frozen data.
- (T2c) A bound pricing the level-k large field by the level-(k-1) variables (one step only; never iterated).
- (T2d) The status of RTARGET §7's failure modes W2-F1 (no smooth background), W2-F2 (inner vacuum depends on the outer
  field), W2-F3 (history combinatorics), each MET / AVOIDED / CIRCUMVENTED-with-a-named-hypothesis.
- Not success: a statement for an isolated single cube only (that is R4D-iso); constants that are not stated.

**Target 3: the inductive step over scales, sea fluctuating.** Assume a representation (I_k) of e^{-S_k} at level k of the
RLF form. Prove (I_{k+1}) as far as possible, conditional only on NAMED hypotheses (each a precise statement: (DF) at
level k, large deviations of the sea, BG-b, the flow (F), history bookkeeping), and prove unconditionally the level
summations (vacuum, coupling shifts, remainders, unreturned clusters). Output: a precise list of what remains, each item
with its inputs and its weight (P = paper-scale, s = session-scale).

**Failure modes (each a valid, precisely named outcome).** (RLF-F1) the per-cube exponent of a cluster of n bad cubes is
not proportional to n (then no finite n_*); (RLF-F2) the cluster counterterms are not field-independent or not
B_4-reducible to a single coupling shift; (RLF-F3) the remainders need the regularity of the large (level-k) field;
(RLF-F4) the outer large field cannot be priced by one step of the chain.

**Check c32** (criteria file first): the re-seeding constants of target (T2c) on explicit SU(2) configurations in d = 4
(L = 3), including configurations that attain the constants; the truncated-cluster combinatorics of (T2a); the n_*
arithmetic (informational, one-loop rate).

---
# Derivations (written after §0-§2)

## 3. The R-operation in the soft setting: what it is (definition-level, exact)

The soft kernel makes the RG an exact Markov chain with positive integrand, so the R-operation can be formulated as an
exact rewriting of one RG step, with no constraint fibres (W3 absent). Fix a level j and write U for the level-j field,
V for the level-(j+1) coarse links, e^{-S}(U) := e^{-S_j(U)}·K_j(V, U) for the step-j integrand (bare form: S_j = Wilson
at g := g_j, as in R4D-iso; effective levels: §8).

- **Notation.** For a set B of level-j cubes, int(B) := the links with both ends in one cube of B; C(B) := the coarse
  links with an endpoint block in B (≤ 8|B|); w_B(U_{int B}; D) := exp(-(1/g²)Σ_{p∩int B≠∅}s(U_p))·Π_{c∈C(B)}k_c, where
  D := U restricted to the links outside int(B), together with V. Every factor of e^{-S} that involves an int(B) link is in
  w_B, so e^{-S} = w_B·w_rest with w_rest independent of U_{int B}.
- **Frozen cluster activity.** r_B(D) := Num_B/Den_B, Num_B := ∫Π_{Q∈B}ζ_Q w_B dU_{int B}, Den_B := ∫Π_{Q∈B}χ_Q w_B dU_{int B}.
  For |B| = 1 this is R4D-iso's ρ (with the D4-norm kernel).
- **The R-operation at level j** (definition). Expand Π_Q(χ_Q + ζ_Q) = Σ_BΠ_{Q∈B}ζ_QΠ_{Q∉B}χ_Q, pass to the frozen activities
  (Proposition CL (a)), take the logarithm of the resulting hard-core gas (Theorem R1 (i)), and split each connected
  term of total cube number N ≤ n_* into (its value at trivial data: a c-number) + (its Ad-invariant quadratic part: after
  B_4-averaging, a coupling shift) + (a remainder of irrelevant order) **[R1617-fix R-6: a remainder of order 𝔯(D) (§7.2);
  this is irrelevant for BG-b-regular frozen data only; in a sea sample it is O(g²) relative to the extracted terms and
  must be re-extracted after the sea average, §8.2 (W1-ret'). R-3b: the connected terms are localised at the base points
  of their UNFATTENED supports, §7.2 (iii). R-1: in the induction the cutoff is n_♯ and collar-bad configurations are
  returned too, §1A.]**. The c-numbers are the vacuum counterterm, the
  quadratic parts are "returned" to the small-field action as the coupling shift δβ_j, and the remainders are small
  local insertions. Terms with N > n_* are kept unrenormalised (they are summable: Lemma LF-n). This is the soft-kernel
  form of "converting large-field contributions back to small-field contributions" (Dimock II p.31 [read]); whether it
  coincides with Balaban's construction is unknown [CMP 122 not-read].

## 4. Lemma GT-lat' (lattice Taylor lemma without point symmetry; B_4 orbit averages): PROVEN-HERE [S17]

*Setting.* As GT-lat (PROOF L5 [S9]): box B̂ = {|x_μ| ≤ R_0} about a block centre 0, R̂ its links, complete-axial tree
paths π_x from 0, P̂_p := log(hol(π_x)U_p hol(π_x)^{-1}), Φ(D) := (P̂_{(0;μ,ν)})_{μ<ν}, ε_2, ε_3 as there. Two changes:
(1) C is ANY finite set of coarse links c (straight segments of length L between block centres inside B̂), not
necessarily from 0 or B_4-symmetric; ε_V := max_{c∈C}||log(V_cS_c^{-1})||_op, S_c the straight fine transporter along c.
(2) F is C³ on {ε_2 + ε_V ≤ r_1} and invariant under all gauge transformations of the data; **no B_4 or ι invariance**.

*Claim.* (i) Put Q_F(Φ) := ½D²F̃_rad(0)(𝓛Φ, 𝓛Φ) (GT's radial chart, 𝓛 GT's linear map). Then Q_F is Ad-invariant, so
Q_F(Φ) = Σ_{a,b}t^F_{ab}⟨Φ_a, Φ_b⟩_HS for a real symmetric 6 × 6 matrix t^F (a, b label the planes μ < ν), and
  |F(D) - F(1) - Q_F(Φ(D))| ≤ C K_F 𝔯(D),  𝔯 := ε_2(ε_3 + ε_V) + (ε_3 + ε_V)² + ε_2³,
with K_F as in GT-lat and C = C(R_0, C).
(ii) For R ∈ B_4 (about 0), (R·D) the rotated data and F∘R(D) := F(R·D): t^{F∘R} = Λ²(R)^T t^F Λ²(R). If a finite family
{F_i} is permuted by D ↦ R·D for every R ∈ B_4, then Σ_iQ_{F_i}(Φ) = c̄·Σ_a||Φ_a||²_HS with c̄ := (1/6)Σ_i tr t^{F_i}.

*Proof.* (i) GT-lat steps 1-3 hold with one addition. In tree gauge a coarse link c from x to x' has S_c = hol of the
closed loop π_x c π_{x'}^{-1}, which bounds a lattice surface of at most A(R_0) plaquettes in B̂ (the box's 2-complex is
simply connected; the count is combinatorial). As for U_b in GT-lat step 1, ||log S_c|| ≤ Cε_2 and
log S_c = Σ±P̂_{p_i} + O(ε_2²). Use the tree coordinate Y_c := log V_c; then ||Y_c|| ≤ ε_V + Cε_2 + Cε_Vε_2. For the
reference data put V^Φ_c := S_c(D^Φ) (so ε_V(D^Φ) = 0). Since log S_c(D) - log S_c(D^Φ) = Σ±(P̂_{p_i}(D) - P̂_{p_i}(D^Φ)) +
O(ε_2²) and ||P̂_p(D) - P̂_p(D^Φ)|| ≤ ε_3 + Cε_2² (GT-lat step 2), |Y_c(D) - Y_c(D^Φ)| ≤ C(ε_V + ε_3 + ε_2²). So step 2's two
estimates |Z(D) - Z(D^Φ)| ≤ C(ε_3 + ε_2² + ε_V), |Z(D^Φ)| ≤ Cε_2 hold. Step 3 is unchanged: a constant gauge
transformation acts on every tree coordinate (links and coarse links) by Ad, so DF̃(0) = 0. Step 4 without B_4: F(D^Φ) =
F̃_rad(𝓛Φ) = F(1) + Q_F(Φ) + R_3 with |R_3| ≤ CK_Fε_2³; D²F̃_rad(0) is Ad-invariant and 𝓛 is Ad-equivariant, so Q_F is
Ad-invariant. Ad-invariant symmetric bilinear forms on su(N) ⊗ R⁶ are ⟨·,·⟩_HS ⊗ t, because su(N) is absolutely
irreducible under Ad (End_Ad(su(N)) = R), exactly as in GT step 5. Combine as in GT-lat step 5.
(ii) GT-lat step 4 proves R·(𝓛Φ) = 𝓛(Λ²(R)Φ) exactly on the lattice (coarse straight links map to coarse straight links).
Hence Q_{F∘R}(Φ) = Q_F(Λ²(R)Φ), i.e. t^{F∘R} = Λ²(R)^Tt^FΛ²(R). If the family is permuted, T := Σ_it^{F_i} commutes with
Λ²(R) for every R ∈ B_4. Λ²R⁴ is absolutely irreducible under B_4 (GT step 5; c19 P1), so T = (tr T/6)·1. ∎

*Remark.* (i) is the general (non-symmetric) cluster version of GT-lat: a cluster of cubes has no point symmetry, and its
quadratic part is a general Ad-invariant form. (ii) says the B_4-orbit sum of the shapes restores a single invariant.

## 5. Proposition CL (frozen cluster activities): PROVEN-HERE [S17]

*Setting.* §3, bare form at level j (Wilson at g, normalised soft kernel D4-norm), g ≤ min(1, √κ). Constants:
n_ℓ := 4L³(L - 1) (links with both ends in one block), n_P := 6n_ℓ, A_d(L) := (d - 1)L(L - 1)/2 (Lemma RS), p_L := 5L - 4
(contour length, NA-lev), r := ε_1/16, c_N the Haar-ball constant (μ{||U - 1|| ≤ δ} ≥ c_Nδ^{N²-1}, δ ≤ 1),
  b_1 := n_P + 12κ(1 + A_d(L))²,  b_0 := 16n_P + 12κp_L²,  ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}.
For a cluster Y, N_1(Y) := the sites of the blocks of Y and of their *-neighbours, and the **completion parameter**
  ε_♭(D; Y) := min over U° ∈ SU(N)^{int Y} of [max_{p ⊂ N_1(Y)}||1 - U°_p||_op + max_{c∈C(Y)}||V_c - S_c(U°)||_op]
(U° completes D on int(Y); the minimum is attained by compactness).

*Claims.*
- (a) **Exact Fubini identity.** For every set B of cubes, Z_B/Z_∅ = ⟨r_B⟩_cut, where Z_B := ∫Π_{Q∈B}ζ_QΠ_{Q∉B}χ_Q e^{-S},
  ⟨·⟩_cut is the all-cut probability measure, and r_B is evaluated on the sample's links outside int(B). Hence
  Z/Z_∅ = ⟨Ξ⟩_cut with Ξ(U) := Σ_B r_B(U) (the frozen gas, evaluated on one sample).
- (b) **Factorisation.** If Y_1, …, Y_m are the *-components of B, then r_B = Π_ir_{Y_i}.
- (c) **Size, per cube uniform.** If ε_♭(D; Y) ≤ ε_loc then, for every *-connected Y of ANY size,
  r_Y(D) ≤ (C_r g^{-p_r} e^{-ε_1²/(4Ng²)})^{|Y|},  p_r := (N² - 1)(n_ℓ + 16),
  C_r := e^{b_0r²}c_N^{-(n_ℓ+8)}e^8κ^{8(N²-1)}r^{-(N²-1)n_ℓ}.
- (d) **Derivatives.** In the tree (or any local Lie) coordinates z of the data, for q ≤ 3 and coordinates z_1..z_q,
  |∂_{z_1}···∂_{z_q}r_Y| ≤ B_q(Λ_1/g²)^q r_Y, Λ_1 := 6 + 8κ(2 + C_𝒩) **[R1617-fix CL-1: was 6 + κ(2 + C_𝒩), asserted;
  the per-link multiplicity 8 is derived in the proof]** (C_𝒩 := Λ'/κ with Λ' from D4-norm (3)), B_q combinatorial.
- (e) **Invariance.** r_Y is invariant under all gauge transformations of D, covariant under translations and under B_4
  about any block centre: r_{RY}(R·D) = r_Y(D).

*Proof.* (a) Z_B = ∫(Π_{Q∉B}χ_Q)w_rest·Num_B: the indicators χ_Q, Q ∉ B, involve only interior plaquettes of Q, hence no
int(B) link. Integrating the all-cut integrand over U_{int B} gives (Π_{Q∉B}χ_Q)w_rest·Den_B. So
Z_B = ∫(Π_{Q∉B}χ_Q)w_rest Den_B·r_B = Z_∅⟨r_B⟩_cut, because r_B depends only on links outside int(B). Sum over B (finite). ∎
(b) For *-separated Y, Y': a plaquette meeting int(Q) has all vertices within sup-distance 1 of the sites of Q, while the
sites of non-touching blocks are at sup-distance ≥ L + 1 ≥ 4; so no plaquette meets both int(Y) and int(Y'). A coarse link's
contours lie in its two endpoint blocks, which touch; so no coarse link is in C(Y) ∩ C(Y'). Hence w_B = Πw_{Y_i} in
disjoint variables, and the indicators factorise. ∎
(c) *Numerator.* On Π_{Q∈Y}ζ_Q every Q ∈ Y has an interior plaquette p_Q with ||1 - U_{p_Q}|| ≥ ε_1, so by (B)
s(U_{p_Q}) ≥ ε_1²/(2N). The p_Q are distinct (disjoint interiors) and all other Wilson terms are ≥ 0, so the Wilson factor is
≤ e^{-|Y|ε_1²/(2Ng²)}. Each k_c ≤ e c_N^{-1}(κ/g²)^{N²-1} (D4-norm (2)), |C(Y)| ≤ 8|Y|, Haar mass 1. *Denominator.* Let U°
attain ε° := ε_♭(D; Y) ≤ ε_loc; restrict to the caps ||U_b - U°_b|| ≤ rg (b ∈ int Y). A plaquette meeting int(Y) has
≤ 4 interior links, so ||1 - U_p|| ≤ ε° + 4rg ≤ ε_1/4 + ε_1/4 < ε_1: every χ_Q = 1, and s(U_p) ≤ ½||1 - U_p||² ≤
(ε°)² + 16r²g²; there are ≤ n_P|Y| such plaquettes. Each kernel term is the mean over contours of
1 - N^{-1}Re tr(V_c^{-1}T^σ_y(U)) ≤ ½||V_c - T^σ_y(U)||² (unitary words; D4-norm's linearity remark), and
||V_c - T^σ_y(U)|| ≤ ||V_c - S_c(U°)|| + ||S_c(U°) - T^σ_y(U°)|| + ||T^σ_y(U°) - T^σ_y(U)|| ≤ ε° + A_d(L)ε° + p_Lrg, by the
ribbon bound of Lemma RS (all plaquettes of the two endpoint blocks lie in N_1(Y)) and p_L ≤ 5L - 4 links per contour.
With (x + y + z)² ≤ 3(x² + y² + z²) and 𝒩 ≤ 1: g²S ≤ |Y|(b_1(ε°)² + b_0r²g²) on the caps. Haar caps give
(c_N(rg)^{N²-1})^{n_ℓ|Y|}. Divide; b_1(ε°)² ≤ ε_1²/(4N) gives the exponent ≥ |Y|ε_1²/(4N). ∎
(d) The data enter polynomially through the Wilson terms (each link in ≤ 6 plaquettes, |∂s(U_p)| ≤ 1) and through the
kernel (|∂ of (κ/g²)(1 - N^{-1}Re tr V^{-1}M̄)| ≤ κ/g² per contour-mean; log 𝒩 by D4-norm (3)); the indicators do not
depend on D. **[R1617-fix CL-1] Multiplicity.** The contours of c = (X, X + e_μ) lie in B(X) ∪ B(X + e_μ) and cross
between the two blocks only along e_μ. So a fine link inside one block B lies in contours of at most the 2d = 8 coarse
links with an endpoint block B, and a link joining B to B + e_ν lies in contours of the coarse link (B, B + e_ν) only. A
fine data link therefore enters at most 8 kernel factors, each through the contour mean (first-derivative factor
≤ 2κ/g²: a contour may back-track along e_μ where its axial part meets the straight leg, as in Lemma RS (R1), so a link
occurs in one contour at most twice, once in each block; M̄_c is a mean) and through log 𝒩(M̄_c) (≤ Λ'/g² = κC_𝒩/g², D4-norm
(3)); a coarse link V_c enters one kernel factor (same bounds). With the 6 Wilson terms: first derivatives of the exponent
are ≤ (6 + 8κ(2 + C_𝒩))/g² = Λ_1/g², and the q-th derivatives of the exponent obey the same bound with a q-dependent
combinatorial factor, absorbed in B_q. Derivatives of the ratio of two positive integrals with D-independent indicators are joint cumulants of
bounded variables under two probability measures, as in R4D-iso step 3. ∎
(e) As R4D-iso step 1 (change of variables on int(Y), Haar invariance; the S4' family and the cuts are B_4-symmetric, L1
re-checks). ∎

*Remark.* (c) is uniform in |Y| because the denominator caps are placed around a completion of the given data, not
around 1 in a tree gauge (whose constants grow with the box). It is the frozen form of the Peierls bound that LF-count's
failure mode (RLF-F1) asks about: **the exponent of a frozen cluster of n bad cubes is ≥ n·ε_1²/(4N) (minus a polynomial
g-loss per cube).** RLF-F1 is AVOIDED in the frozen setting.

## 6. Lemma RS (one-step re-seeding of a coarse large field): PROVEN-HERE [S17]

*Setting.* One soft step from level i to level i + 1 (any i; no hypothesis on S_i). A level-(i+1) plaquette
P = (X; μ, ν) with coarse links c_1 = (X, X+e_μ), c_2 = (X+e_μ, X+e_μ+e_ν), c_3 = (X+e_ν, X+e_μ+e_ν), c_4 = (X, X+e_ν);
V_P := V_{c_1}V_{c_2}V_{c_3}^{-1}V_{c_4}^{-1}. U_4 := the union of the four blocks B(X), B(X+e_μ), B(X+e_ν), B(X+e_μ+e_ν);
η := max{||1 - U_p||_op : p a fine plaquette with all vertices in U_4}. S_c the straight transporter between the block
centres; δ_c := max_{σ,y}||T^σ_y - S_c||_op over the S4' contours of c.

*Claim.*
- (R1) **Ribbon bound.** δ_c ≤ A_d(L)η, A_d(L) := (d - 1)L(L - 1)/2 (= 9 for d = 4, L = 3); hence ||M̄_c - S_c|| ≤ A_d(L)η.
- (R2) **Square bound.** ||1 - S_P|| ≤ L²η, S_P := S_{c_1}S_{c_2}S_{c_3}^{-1}S_{c_4}^{-1}; hence
  ||1 - V_P|| ≤ L²η + Σ_{i=1}^4||V_{c_i} - S_{c_i}||.
- (R3) **Dichotomy.** Put η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}. If ||1 - V_P|| ≥ ε_1 then either η ≥ η_1, or η < η_1
  and some c ∈ ∂P has ||V_c - S_c|| ≥ ε_1/8.
- (R4) **Kernel branch, unconditional.** For every U with δ_c(U) ≤ A_d(L)η_1 and g² ≤ κ,
  ∫_{||V_c - S_c|| ≥ ε_1/8} k_c(V_c, U) dV_c ≤ e c_N^{-1}(κ/g²)^{N²-1} e^{-κε_1²/(256Ng²)},
  and for distinct coarse links the bound multiplies (k = Π_ck_c is a product of conditional densities).
- (R5) **Plaquette branch.** On {η ≥ η_1} some plaquette of U_4 has s(U_p) ≥ η_1²/(2N) (inequality (B)).

*Proof.* (R1) Lasso: if a closed loop ℓ is built by successively attaching plaquettes, hol(ℓ) = Π_iw_iU_{p_i}^{±1}w_i^{-1},
and ||ab - 1|| ≤ ||a - 1|| + ||b - 1|| for unitaries gives ||hol(ℓ) - 1|| ≤ Σ_i||U_{p_i} - 1||. Now T^σ_yS_c^{-1} is the holonomy
of the loop γ·leg(y)·(γ + Le_μ)^{-1}·leg(c_X)^{-1}, where γ = s_1…s_m is the order-σ axial path c_X → y and leg(z) the
straight path z → z + Le_μ; S4' pairing (the same σ at both ends) and translation covariance of P^σ make the far-end path
the translate γ + Le_μ. With γ_t := s_1…s_t and ℓ_t := γ_t·leg(z_t)·(γ_t + Le_μ)^{-1}·leg(c_X)^{-1}, inserting
hol(leg(z_{t-1}))^{-1}hol(γ_{t-1})^{-1}hol(γ_{t-1})hol(leg(z_{t-1})) = 1 gives
hol(ℓ_t) = hol(γ_{t-1})R_thol(γ_{t-1})^{-1}·hol(ℓ_{t-1}), R_t := the holonomy of the 1 × L rectangle spanned by s_t and
leg(z_{t-1}); ℓ_0 is trivial. If s_t is along ±μ the rectangle is degenerate (a back-tracking path) and R_t = 1 exactly.
Otherwise R_t is a product of L conjugated plaquettes. The axial path has Σ_{α≠μ}|y_α - (c_X)_α| ≤ (d - 1)(L - 1)/2 steps off
the μ-direction. All rectangles lie in B(X) ∪ B(X + e_μ) ⊂ U_4. So δ_c ≤ A_d(L)η, and M̄_c is a mean of the T^σ_y. (R2) S_P
is the holonomy of the L × L square through the four block centres, a product of L² conjugated plaquettes of U_4; then
telescope V_P against S_P (unitaries). (R3) If η < η_1 and all four ||V_c - S_c|| < ε_1/8, (R2) gives ||1 - V_P|| <
L²η_1 + ε_1/2 ≤ ε_1. (R4) |N^{-1}tr A| ≤ ||A||_op and (B) give 1 - N^{-1}Re tr(V^{-1}M̄) ≥ [1 - N^{-1}Re tr(V^{-1}S)] -
||M̄ - S|| ≥ ||V - S||²_op/(2N) - δ_c. D4-norm (2) gives 𝒩(M̄) ≥ e^{-(κ/g²)(1 - N^{-1}Re tr V_0^{-1}M̄)}e^{-1}c_N(g²/κ)^{N²-1}
with V_0 the maximiser, and 1 - N^{-1}Re tr(V_0^{-1}M̄) ≤ 1 - N^{-1}Re tr(S^{-1}M̄) ≤ ||M̄ - S|| ≤ δ_c (S is a candidate). So
k_c ≤ e c_N^{-1}(κ/g²)^{N²-1}exp(-(κ/g²)[||V_c - S_c||²/(2N) - 2δ_c]); on the event the bracket is ≥ ε_1²/(128N) -
2A_d(L)η_1 ≥ ε_1²/(256N). Haar mass 1. (R5) (B). ∎

*What RS buys (RLF-F4).* A level-(i+1) large field is pointwise reduced to level-i objects, across ONE step: either a
kernel mismatch, priced unconditionally by the normalised soft kernel at the FINER coupling g_i (1/g_i² ≥ 1/g_{i+1}² under
(F)), or a level-i plaquette ≥ η_1, priced by the level-i action (bare level: Wilson positivity; effective levels: the
large-deviation hypothesis (PLD) of §8). This is the soft-kernel form of the one-step regularity of Dimock QED Lemma 23
(NOTES §4 [read]); it is never iterated, so E8*-ob's obstruction does not apply. The pairing of contour orders (S4') is
what makes the far-end path a translate; without it the ribbon bound needs the area between two different axial paths
(c32 A controls this). **RLF-F4 is AVOIDED.**

*Constants (d = 4, L = 3).* A_4 = 9, L² = 9, η_1 = min{ε_1/18, ε_1²/(4608N)}; kernel exponent κε_1²/(256N).

## 7. Theorem R1 (frozen one-level R-operation) and Theorem TS (two scales, frozen exterior): PROVEN-HERE [S17; R1 (iii), TS hypotheses repaired S18, unreviewed]

### 7.1 Lemma LF-n (cluster-count arithmetic; not counted)
Under (F), with w_i := Ce^{-a/g_i²} and integers n ≥ 1: L^{4(K-i)}w_i^n ≤ C^ne^{-na/g_K²}L^{(4 - naβ_-)(K-i)}. Hence
Σ_{i≤K}L^{4(K-i)}w_i^n ≤ C^ne^{-na/g_K²}/(1 - L^{4-naβ_-}) whenever naβ_- > 4, and (LF-count, the other half) the sum diverges as
K → ∞ when w_i ≥ e^{-a/g_i²} per n-cluster and naβ_+ ≤ 4. *Proof.* Substitute 1/g_i² ≥ 1/g_K² + β_-(K - i)log L. ∎
**Definition.** For 0 < a'' < ε_1²/(4N): **n_* := ⌊4/(a''β_-)⌋**, so (n_* + 1)a''β_- > 4. n_* is g- and K-independent.
Consequence: only clusters of total cube number ≤ n_* need counterterms; LF-count's divergence comes from them alone.

**[R1617-fix R-8, R-10] Definitions for the induction.** a_RS := min{a_η, κε_1²/(256N)} (the two branches of Lemma RS
at effective levels; a_η from (PLD)_k (i)). c_RS := 5⁴ (ARGUED, not written: among n level-(k+1) bad cubes a greedy
choice gives ≥ n/5⁴ whose RS regions, U_4(P) with its 1-neighbourhood, are pairwise disjoint, so RS prices them by
(Ce^{-a_RS/g_k²})^{n/c_RS} ≤ (Ce^{-a_RS/g_{k+1}²})^{n/c_RS}; the joint pricing of the two branches is part of (HIST)'s ordering).
**a_♯ := min{a'', a_♭, a_RS/c_RS}, n_♯ := ⌊4/(a_♯β_-)⌋ ≥ n_*.** Theorem R1 below holds for every cutoff n_c ≥ n_* (its
constants depend on n_c); the induction uses n_c = n_♯. [inference, R-10] With the crude constants of §9 C and a_η taken
at its bare-level value η_1²/(2N) ≈ 1.8·10⁻¹⁰, n_♯ is of order 10¹³. It is finite and g- and K-independent, which is all
Lemma LF-n needs; it is a property of the bounds, not of the theory.

### 7.2 Theorem R1 (one level, frozen background) [R1617-fix: (iii) re-localised (R-3b); (H-loc) derived from (H-ch) (R-3a); torus wrap (R-4); cutoff n_c]
*Setting.* Level j, bare form, a frozen full configuration D (all level-j links and the level-(j+1) coarse links). Fix an
integer cutoff n_c ≥ n_*, put R_* := (n_c + 2)L [R1617-fix: was (16n_* + 2)L, the size needed by fattened polymers; the
localisation below uses unfattened supports], and assume
  **(H-ch)** ε_2 + ε_V ≤ ε_♮ on the box B̂_*(x) of radius R_* about every block centre x,
with ε_♮ := min{r_1(R_*), ε_loc/C_♮(R_*)}, r_1 = GT-lat's chart radius for R_*, and C_♮(R_*) ≥ 3 chosen so that every
point of the GT-lat' chart ball used in (ii) (tree coordinates |Z| ≤ C(R_*)ε_♮) has ε_♭(·; Y) ≤ ε_loc for every Y in the
box [S18 note: session 17 took C_♮ = 3, which covers the data themselves (Lemma 7.2-0) but not the whole ball over which
K_F is a supremum; constants only] **[R1819-fix F1: why C_♮(R_*) exists. On the chart ball, ε_♭(·; Y) is Lipschitz in the
tree coordinates, with a constant C'(R_*) (finitely many links in the box, each entering through smooth functions of
the principal logs, which stay principal on the ball); so for |Z| ≤ C(R_*)ε_♮, ε_♭(Z; Y) ≤ 2ε_♮ + C'(R_*)C(R_*)ε_♮ (the data
bound of Lemma 7.2-0 plus the Lipschitz step), and C_♮(R_*) := max(3, 2 + C'(R_*)C(R_*)) gives ε_♭ ≤ ε_loc on the whole
ball. C' is an existence constant (not computed), like r_1.]**. Session 17's (H-loc) is no longer a hypothesis (Lemma 7.2-0). Fix
a'' ∈ (0, ε_1²/(4N)), a_1 := ε_1²/(4N) - a'', κ := 4κ_0 + 3 with Theorem CE's [S11] κ_0 = 16 log 12800, κ_1 := κ - κ_0 - 2,
and c_0(κ), B, C_K, K_0 those of Theorem CE [S11]. Gas polymers (used for the hard core only): Ŷ := Y + {0, 1}⁴ (cube
coordinates). T_j := the side of the level-j torus in cubes (≥ 3); **W := 2n_c + 5.**
*Hypothesis on g (G1):* θ := 2(C_rg^{-p_r}e^{-a_1/g²})^{1/16} ≤ C_Kc_0(κ)e^{-2κ_1}, and g ≤ min(1, √κ).

**Lemma 7.2-0 (R-3a: completion for clusters of every size).** Under (H-ch), ε_♭(D; Y) ≤ 2ε_♮ < ε_loc for every set Y of
cubes. So Proposition CL (c) applies to every *-connected Y, whatever its size.
*Proof.* Take U° := D's own links on int(Y). Every plaquette p ⊂ N_1(Y) and every coarse link c ∈ C(Y) lies in some box
B̂_*(x) (R_* ≥ 2L). ||1 - U_p||_op ≤ ||log U_p||_op = ||P̂_p||_op ≤ ε_2 (|e^{iθ} - 1| ≤ |θ|; conjugation invariance), and
||V_c - S_c||_op = ||V_cS_c^{-1} - 1||_op ≤ ||log(V_cS_c^{-1})||_op ≤ ε_V. So ε_♭ ≤ 2ε_♮ ≤ 2ε_loc/3. ∎

*Claims.*
- (i) **The gas and its logarithm.** Ξ(D) = Σ_{families of polymers with pairwise disjoint X_i}Π_iz_{X_i}, with
  z_X := Σ_{Y: Ŷ=X}r_Y(D). log Ξ(D) = Σ_XΣ_{N≥1}𝓗^{(N)}_X(D), absolutely convergent, where 𝓗^{(N)}_X collects the terms of
  Theorem CE's 𝓗_X (step 3) whose clusters (Y_1, …, Y_n) have Σ|Y_i| = N, and
  |𝓗^{(N)}_X| ≤ e^{-a''N/g²}·2κ_0Bc_0(κ)e^{-κ_0d(X)}.
  **Tuple form [R1617-fix].** For a tuple τ = (Y_1, …, Y_n) of clusters let G(τ) be its touching graph (edge {i, j} iff
  Y_i ∪ Y_j contains two cubes at sup-distance ≤ 1, i.e. Y_i and Y_j touch or overlap), φ^T(G) := Σ over connected
  spanning subgraphs H ⊂ G of (-1)^{|E(H)|}, supp τ := ∪Y_i (UNFATTENED) and N(τ) := Σ|Y_i|. Then
    log Ξ(D) = Σ_{n≥1}(1/n!)Σ_τφ^T(G(τ))Π_ir_{Y_i}(D),
  absolutely convergent, and for every cube x
    Σ_{τ: supp τ ∋ x}(1/n!)|φ^T(G(τ))|Π_ir_{Y_i}(D)·e^{a''N(τ)/g²} ≤ 2κ_0Bc_0K_0.
- (ii) **Taylor form.** For a cube set S and N ≤ n_c put
    𝓖^{(N)}_S(D) := Σ_{n≥1}(1/n!)Σ_{τ: supp τ = S, N(τ) = N}φ^T(G(τ))Π_ir_{Y_i}(D),
  a finite polynomial in the r_Y (Y ⊂ S), zero unless S is *-connected with |S| ≤ N. For x ∈ S:
  𝓖^{(N)}_S(D) = 𝓖^{(N)}_S(1) + Q^{(N)}_{S,x}(Φ_x(D)) + R^{(N)}_{S,x}(D), with Q^{(N)}_{S,x} = Σt⟨Φ_a, Φ_b⟩ Ad-invariant
  (matrix t^{(N)}_{S,x}) and Σ_{S∋x}|R^{(N)}_{S,x}(D)| ≤ C_*g^{-6}e^{-a''N/g²}𝔯_x(D), 𝔯_x := 𝔯 on B̂_*(x),
  C_* = C(n_c, L, N, κ).
- (iii) **Assembly (re-localised).** If T_j ≥ W, then with N_j the number of level-j cubes
    log Ξ(D) = N_jc̄_0(g) + δβ_j·Σ_ps(U_p) + Σ_xℛ_x(D),
    c̄_0(g) := Σ_{N≤n_c}Σ_{S∋0}𝓖^{(N)}_S(1)/|S|,  δβ_j := (2N/L⁴)c̄_1,  c̄_1 := (1/6)Σ_{N≤n_c}Σ_{S∋0}tr t^{(N)}_{S,0}/|S|
  (both computed on the cubes of Z⁴), |c̄_0| ≤ 2κ_0Bc_0K_0e^{-a''/g²}, |δβ_j| ≤ C_*g^{-6}e^{-a''/g²},
    |ℛ_x| ≤ C_*g^{-6}e^{-a''/g²}𝔯_x + 2κ_0Bc_0K_0e^{-a''(n_c+1)/g²}.
  c̄_0 and δβ_j are field-independent numbers depending only on (g, L, N, κ, ε_1, a'', n_c); Σ_p runs over all level-j
  plaquettes.
- (iv) **Torus wrap (R-4).** If T_j < W, log Ξ(D) = Σ_xℛ^w_x(D) with |ℛ^w_x| ≤ 2κ_0Bc_0K_0e^{-a''/g²} (nothing is
  extracted). Over all levels j < K, the number of level-j cubes on levels with T_j < W is ≤ (L⁴/(L⁴ - 1))W⁴, uniformly in K
  and T, and those levels have g_j ≤ g_K. So the wrap levels contribute in total a field-dependent term of absolute value
  ≤ (L⁴/(L⁴ - 1))W⁴·2κ_0Bc_0K_0e^{-a''/g_K²}, uniformly in K: a bounded boundary-type term, not of irrelevant order, absorbed
  by the C|T|e^{-a'/g_K²} of (RLF-4) (|T| ≥ 1).

*Proof.* (i) **Hard core = disjointness.** For cube sets, Ŷ ∩ Ŷ' ≠ ∅ iff some x ∈ Y, x' ∈ Y' have
x - x' ∈ {0,1}⁴ - {0,1}⁴ = {-1, 0, 1}⁴, i.e. iff Y and Y' touch or overlap (torus side ≥ 3). The *-components of B are
pairwise *-separated *-connected sets, and a family of pairwise *-separated *-connected sets is the set of components of
its union; so B ↦ (components) is a bijection onto families with pairwise disjoint Ŷ_i. With CL (b), Σ_BΠr = Σ_{disjoint}Πz_X.
Ŷ is *-connected (a polymer), |Ŷ| ≤ 16|Y|, d(Ŷ) ≤ 2(|Ŷ| - 1) (a spanning tree of centre-to-centre segments, each ≤ √4 = 2),
and #{Y : Ŷ = X} ≤ 2^{|X|}. **Grading.** Put r'_Y := e^{a''|Y|/g²}r_Y and z'_X := Σ_{Ŷ=X}r'_Y. By CL (c), applicable to every
cluster by Lemma 7.2-0, |z'_X| ≤ 2^{|X|}max(C_rg^{-p_r}e^{-a_1/g²})^{|Y|} ≤ θ^{|X|} (|Y| ≥ |X|/16, base < 1). By (G1) and
C_Kc_0(κ) ≤ 1, θ^{|X|} ≤ C_Kc_0e^{-2κ_1|X|} ≤ C_Kc_0e^{-κ_1d(X)}: z' lies in Theorem CE's polydisc 𝔻 with H_0 = c_0(κ). CE
steps 3-4 (PROVEN, L5 [S10]-[S11]; statements about P(z) = Σ_{disjoint}Πz on 𝔻 for any z ∈ 𝔻) give log P = Σ_X𝓗_X,
𝓗_X = Σ_n(1/n!)Σ_{(X_1..X_n): ∪X_i = X}ρ^T(g(X_1..X_n))Πz_{X_i} (ρ^T on the overlap graph g), with
Σ_n(1/n!)Σ|ρ^T|Π|z'_{X_i}| ≤ 2κ_0Bc_0e^{-(κ-3κ_0-3)d(X)} = 2κ_0Bc_0e^{-κ_0d(X)}. **Tuple form.** Substitute
z_{X_i} = Σ_{Ŷ_i = X_i}r_{Y_i}. By the hard-core equivalence the overlap graph of (Ŷ_1, …, Ŷ_n) is the touching graph G(τ),
so each X-tuple term expands into the τ-terms with Ŷ_i = X_i, and the τ-series is a regrouping of the X-series. Because
r'_Y ≥ 0, |z'_X| = Σ_{Ŷ=X}r'_Y, so the τ-series of the nonnegative terms (1/n!)|φ^T|Πr'_{Y_i} has the same sum as the
X-majorant: absolute convergence, and rearrangements are allowed. Every τ with supp τ ∋ x has ∪Ŷ_i ∋ x (Y ⊂ Ŷ), so
Σ_{supp τ ∋ x}(1/n!)|φ^T|Πr'_{Y_i} ≤ Σ_{X∋x}2κ_0Bc_0e^{-κ_0d(X)} ≤ 2κ_0Bc_0K_0 ((g4) [S11]). If G(τ) is disconnected,
φ^T = 0; if it is connected, supp τ is *-connected. Grouping by N = N(τ): every term of 𝓗^{(N)}_X (and of 𝓖^{(N)}_S) is a
majorant term times e^{-a''N/g²}. ∎(i)
(ii) 𝓖^{(N)}_S involves tuples with n ≤ N and Y_i ⊂ S: finitely many. **Locality.** r_Y depends on D only through the links
of plaquettes meeting int(Y) and the coarse links of C(Y) with their contours, i.e. inside the blocks of Y and their
*-neighbours. S is *-connected with |S| ≤ N ≤ n_c, so S lies within cube sup-distance n_c - 1 of x, and 𝓖^{(N)}_S depends on D
only inside B̂_*(x) (fine sup-distance ≤ n_cL + (L - 1)/2 < R_*). **Invariance.** Each r_Y is gauge-invariant (CL (e)).
**Derivatives.** The product rule over ≤ n_c factors and CL (d) give K_F ≤ B(n_c)(Λ_1/g²)³·sup_{ball}Σ_{supp τ = S, N(τ) = N}
(1/n!)|φ^T|Πr_{Y_i}. On the chart ball every r_Y obeys CL (c) (choice of C_♮), so the bound of (i), whose derivation used only
CL (c), bounds Σ_{S∋x} of these suprema by e^{-a''N/g²}2κ_0Bc_0K_0. Apply GT-lat' (i) to each F = 𝓖^{(N)}_S with C := all
coarse links in B̂_*(x). ∎(ii)
(iii) **Localisation.** Σ_S𝓖^{(N)}_S = Σ_xΣ_{S∋x}𝓖^{(N)}_S/|S|. Fix x. **The family is permuted (the repaired step).** Let
R ∈ B_4 act about the block centre c_x of x: on fine sites z ↦ c_x + R(z - c_x); on cubes y ↦ x + R(y - x) (blocks go to
blocks because c_y = Ly + o); on data D ↦ R·D. Then (a) r_{RY}(R·D) = r_Y(D) (CL (e)); (b) R preserves the sup-distance of
cubes, hence touching, so G(Rτ) = G(τ) for Rτ := (RY_1, …, RY_n); (c) N(Rτ) = N(τ), supp(Rτ) = R(supp τ), |RS| = |S|;
(d) x ∈ RS ⟺ x ∈ S. So τ ↦ Rτ maps {τ: supp τ = S, N(τ) = N} bijectively onto {τ: supp τ = RS, N(τ) = N}, term by term, and
𝓖^{(N)}_{RS}(R·D) = 𝓖^{(N)}_S(D). Hence F_S := 𝓖^{(N)}_S/|S| (S ∋ x) satisfies F_S(R·D) = F_{R^{-1}S}(D): the finite family
{F_S : S ∋ x, |S| ≤ N} is permuted by D ↦ R·D, which is exactly the hypothesis of GT-lat' (ii). (This is the step that is
false for the session-17 assignment: Ŷ = Y + {0,1}⁴ is not B_4-covariant about x, R(Ŷ) = (RY)^ + t_R, and x ∈ Ŷ does not
imply x ∈ (RY)^; REVIEW_S16_S17, R1 (iii); c33 B2-B3.) **Coupling shift.** GT-lat' (ii) gives
Σ_{S∋x}Q^{(N)}_{S,x}(Φ_x)/|S| = c̄_1^{(N)}Σ_a||Φ_{x,a}||²_HS with c̄_1^{(N)} := (1/6)Σ_{S∋x}tr t^{(N)}_{S,x}/|S|. **Translation and
torus.** If T_j ≥ W, each S ∋ x with |S| ≤ n_c, together with B̂_*(x), embeds isometrically into Z⁴ (the box spans
2n_c + 5 = W ≤ T_j cubes per direction, and its fine side 2R_* + 1 ≤ T_jL - 2 for L ≥ 3), the touching relation on it is the Z⁴ one, and the r_Y are the same functions of
the same data. So 𝓖^{(N)}_S(1) and t^{(N)}_{S,x} are their Z⁴ values, which are translation invariant: c̄_0 and c̄_1 do not
depend on x and are the infinite-volume numbers of the statement. **Identification with the Wilson action** (unchanged):
let B_x := the plaquettes with base point in block x (6L⁴ plaquettes; the B_x partition all plaquettes). For p ∈ B_x,
s(U_p) = ||P̂_p||²_HS/(2N) + O(N²||P̂_p||⁴) (1 - N^{-1}Re tr e^Y = ||Y||²_HS/(2N) + O(Y⁴), R4D-iso step 4), and
|‖P̂_p‖²_HS - ‖Φ_{x,a(p)}‖²_HS| ≤ 2Nε_2ε_3. Summing over B_x (L⁴ base points per plane):
Σ_{p∈B_x}s(U_p) = (L⁴/(2N))Σ_a||Φ_{x,a}||² + O(L⁴(ε_2ε_3 + ε_2³)). So Σ_xc̄_1||Φ_x||² = δβ_jΣ_ps(U_p) + O(c̄_1Σ_x𝔯_x). Collect
R^{(N)}, this identification error, and the tail Σ_{N>n_c} (≤ 2κ_0Bc_0K_0e^{-a''(n_c+1)/g²} per x, by (i)) into ℛ_x. The
bounds on c̄_0 and δβ_j follow from (i)-(ii) (N ≥ 1). ∎(iii)
(iv) On a level with T_j < W put ℛ^w_x := Σ_NΣ_{S∋x}𝓖^{(N)}_S/|S|; (i) bounds it. Count: T_j = T·L^{K-1-j} ≥ 3L^{K-1-j}, so
T_j < W only when K - 1 - j < log_L(W/3), and Σ_{such j}T_j⁴ ≤ W⁴Σ_{m≥0}L^{-4m}. For these j, g_j ≤ g_K by (F). ∎
**[R1819-fix F2]** T and T_j as in §1A (T the level-K side in level-K sites, T_j the level-j side in level-j cubes).
**[R1819 note]** W⁴ ≈ (2·10¹³)⁴ is absorbed into the g-independent constant C of (RLF-4); this is legitimate (it is
g- and K-independent) and is the only place the wrap levels enter.

**Remark 7.2-B (the value of δβ_j is unchanged; a second repair route).** On GT-lat' step 2's reference data,
Q_{F,x}(Φ) = ½D²F̃(0)(𝓛_xΦ, 𝓛_xΦ), the Hessian at the identity configuration in per-link Lie coordinates. (a) **Centre
independence.** 𝓛_xΦ - 𝓛_{x'}Φ is the constant su(N)-valued 1-form ½(x' - x)^νΦ_νμ, which on a box is d of a linear
function; and the Hessian of a gauge-invariant F at the critical point 1 is invariant under the linearised gauge action
(expand F(e^{tλ}·exp(sA)) = F(exp(sA)) to second order and use DF̃(0) = 0). So Q_{F,x} = Q_{F,x'}. (b) **Translation.**
Q_{F_{X+a}} = Q_{F_X} by translation covariance. Hence ANY base-point assignment that gives the placements of each
translation class total weight 1 per cube (the fattened one of session 17 included) yields, at every x, the same form
Σ_{classes}Q_{[X]}, the total quadratic coefficient per cube. The class set is B_4-invariant, so this total is scalar by the
argument of GT-lat' (ii). So the session-17 formula for δβ_j gives the right number, and anisotropic marginal terms do not
arise; what was false was the claimed permutation of the family {X ∋ x}, and with it the B_4-invariance of the full
localised functional. c33: A5/B4 (constant data: the two localisations agree), A3/B2 (generic data: the fattened one is
not invariant, the tuple one is). The counted repair is (iii); Remark 7.2-B is ARGUED-level supplementary (not counted).

*Reading [R1617-fix R-6].* Under (H-ch), the whole level-j large-field gas is exactly e^{c-number}·e^{δβ_jΣs}·e^{Σℛ}: every
cluster tuple of total size N ≤ n_c contributes a vacuum constant and its share of ONE uniform coupling shift, and the rest
is ℛ: a local remainder of order 𝔯_x(D) plus an unrenormalised tail of order e^{-a''(n_c+1)/g²} per cube, which Lemma LF-n
sums. **The remainder is irrelevant only for BG-b-regular frozen data** (where 𝔯_x is small with the scale, §7.3 (b1)).
**In a sea sample** ε_V = max||log(V_cS_c^{-1})|| is an O(g/√κ) fluctuation, so 𝔯_x = O(g²), the same order as the extracted
quadratic part, and |ℛ_x| ≤ C_*g^{-4}e^{-a''/g²} per cube. Summed over levels with L^{4(K-j)} cubes this diverges (LF-count).
So in the fluctuating integral the c-number and marginal parts of ℛ must be re-extracted after the sea average: that is
(W1-ret') in §8.2. What R1 gives pointwise in a sea sample satisfying (H-ch) is the exact identity (iii) with these bounds,
not smallness. **RLF-F2 is AVOIDED (frozen, R1 (iii) as repaired):** the counterterms are field-independent and the
B_4 orbit structure of the tuple supports plus the base-point partition B_x reduce all marginal parts to one coupling shift
of the uniform Wilson action.

### 7.3 Theorem TS (two scales; the level-k field may be large; frozen exterior) [R1617-fix R-5: hypotheses on the region R1 uses]
*Setting.* Levels j < k. Δ := one level-(k-1) cube (one level-k site; so Δ lies in a level-k cell that may be large-field
at level k). A frozen multi-level background: for each inner level i ∈ [j, k-1], a full configuration D_i (level-i links
and level-(i+1) coarse links, the latter = the level-(i+1) links of D_{i+1}), with T_i ≥ W (wrap levels: §7.2 (iv)).
Assume:
- **(R1)_i at every inner level i:** D_i satisfies Theorem R1's hypothesis (H-ch) on the whole level-i torus (R1's gas
  identity is a statement about the whole level; frozen exterior means all of D_i is given), and (G1) holds at g_i.
- **BG-b relative to level k-1, on Δ_*.** For i = k-1-n (n ≥ 0) let 𝒬_n(Δ) := the level-i cubes inside Δ (L^{4n} of them)
  and Δ_{*,n} := the level-i cubes within cube sup-distance R_*/L + 1 of 𝒬_n(Δ) (the cubes that meet a box B̂_*(x),
  x ∈ 𝒬_n(Δ)). For Q ∈ Δ_{*,n} let ε_•(Q) be R4D-iso/GT-lat's parameters of D_i on Q's box, and assume
  (b1) ε_2(Q) + ε_V(Q) ≤ M_2σ_n², σ_n := L^{-n}, with M_2 ≤ ε_TS := ε_♮;
  (b2) Σ_nō_n ≤ M_3, ō_n := σ_n^{-2}L^{-4n}Σ_{Q∈Δ_{*,n}}(ε_3 + ε_V)(Q).
- **Coupling window:** g_i² < a''/3 at every inner level (so that w(g) := C_*g^{-6}e^{-a''/g²} is increasing on the inner
  couplings: d log w/dg = -6/g + 2a''/g³ > 0 iff g² < a''/3).
**No hypothesis is made on the level-k field** (it may have ||1 - U_k(P)|| ≥ ε_1 at Δ). The inner integrands are of bare
form at each inner level (frozen model; effective levels: §8).

*Claims.*
- (TS-a) **Fixed counterterms.** At each inner level i the large-field gas satisfies Theorem R1 with the constants
  c̄_0(g_i), δβ_i of 7.2, which do not depend on the level-k field or on any datum.
- (TS-b) **Inner remainders based in Δ, uniformly in j, k.** Σ_{i=j}^{k-1}Σ_{x∈𝒬_{k-1-i}(Δ)}|ℛ_x| ≤ C_TS[w_{k-1}(3M_2M_3 +
  M_2³/(1 - L^{-2})) + e^{-a''(n_c+1)/g_{k-1}²}/(1 - L^{4-(n_c+1)a''β_-})], with w_i := C_*g_i^{-6}e^{-a''/g_i²} and
  C_TS = C(n_c, L, N, κ), including the box-overlap factor (2R_*/L + 3)⁴.
- (TS-c) **Outer suppression, one step.** If Δ's level-k cell has a plaquette P with ||1 - U_k(P)|| ≥ ε_1, then by Lemma RS
  applied to the step k-1 → k: either some level-(k-1) plaquette in U_4(P) has s ≥ η_1²/(2N) (cost e^{-η_1²/(2Ng_{k-1}²)} in
  the level-(k-1) Wilson weight in the bare model), or a mismatch event of conditional probability
  ≤ e c_N^{-1}(κ/g_{k-1}²)^{N²-1}e^{-κε_1²/(256Ng_{k-1}²)}, uniformly in everything (Lemma RS (R4)).
- (TS-d) Both suppressions are kept in product form: the inner levels contribute exp(N-weighted c-numbers + coupling
  shifts + the remainders of (TS-b)) and the outer large field contributes the factor of (TS-c); neither needs the other.

*Proof.* (TS-a) Theorem R1 at level i under (R1)_i; its constants are the infinite-volume numbers (T_i ≥ W).
(TS-b) For x ∈ 𝒬_n(Δ) every cube meeting B̂_*(x) is in Δ_{*,n}. **Box merging.** For the box B̂_*(x),
ε_2(B̂_*) = max_{Q⊂B̂_*}ε_2(Q) (conjugation does not change ||log U_p||), ε_V(B̂_*) = max ε_V(Q), and
ε_3(B̂_*) ≤ C(R_*)max_{Q⊂B̂_*}(ε_3(Q) + ε_2(Q)²): compare the base plaquette of B̂_* with those of a chain of ≤ 2R_*/L + 1
overlapping cube boxes; consecutive base plaquettes differ by ≤ ε_3 + Cε_2² after transport, and changing the transport
path conjugates by a holonomy h with ||h - 1|| ≤ (area)ε_2, which moves a plaquette log of size ε_2 by ≤ 2||h - 1||ε_2. Then
with ε_3 ≤ 2ε_2 and (b1) on Δ_{*,n}, every product in 𝔯_x is bounded by C(n_c)Σ_{Q⊂B̂_*(x)}[3M_2σ_n²(ε_3 + ε_V)(Q) + M_2³σ_n⁶]
(max ≤ sum). Each Q ∈ Δ_{*,n} lies in ≤ (2R_*/L + 3)⁴ of the boxes B̂_*(x). Sum over x ∈ 𝒬_n(Δ) and use L^{4n}σ_n⁴ = 1
(the d = 4 marginality, as in BG-sum) and |Δ_{*,n}|σ_n⁴ ≤ (2R_*/L + 3)⁴ for the M_2³ term: the level-n total is
≤ C[3M_2ō_n + M_2³σ_n²]·w_i, with w_i ≤ w_{k-1} (g_i ≤ g_{k-1} and the coupling window). Sum over n with (b2). The tail:
|𝒬_n(Δ)| = L^{4n} cubes, each ≤ 2κ_0Bc_0K_0e^{-a''(n_c+1)/g_{k-1-n}²}; Lemma LF-n. (TS-c) Lemma RS (R3)-(R5) at the step
k-1 → k; the kernel branch is unconditional (R4); the plaquette branch is a pointwise lower bound on the level-(k-1) Wilson
term. (TS-d) The inner statements use only the inner data; the outer one uses only the step k-1 → k. ∎
**Role [R1617-fix R-6].** TS is the frozen-background shadow of the induction: it shows what the inner remainders cost when
the frozen data are BG-b-regular. Proposition RLF-step (§8.3) does not use TS; it uses R1 pointwise in the sea sample and
re-extracts after the sea average.

### 7.4 Outcome against RTARGET §7 and §2's failure modes (frozen exterior)
- **W2-F1 (no smooth background inside a multi-scale large region): CIRCUMVENTED for BG-b-regular frozen data only
  [R1617-fix R-6], with a named hypothesis.** The inner renormalisation at level i needs only (H-ch), a level-i statement
  about level-i data; the summation over inner levels (TS-b) needs BG-b relative to the LAST level at which the region is
  small-field (k - 1), on Δ_*, never the large level-k field. The Taylor parameter is ε_•(level-i data), not a smooth
  family. Hypothesis: BG-b of the FROZEN data at level k-1. [R1617-fix R-6: session 17 wrote "(= node N2/BG-reg)"; that
  conflates the background minimiser, for which N2/BG-reg would supply BG-b, with a frozen sample. A level-i sea sample
  violates (b1) once L^{-2n}M_2 < g, and then 𝔯 = O(g²): §7.2 Reading.] In the fluctuating integral W2-F1 is carried by the
  sea-averaged re-extraction (W1-ret') of §8.2.
- **W2-F2 (inner vacuum depends on the outer field): AVOIDED by construction.** c̄_0(g_i), δβ_i are defined at the trivial
  datum, in infinite volume.
- **W2-F3 (history combinatorics): AVOIDED in the frozen setting.** Per level, the sum over large-field sets is a hard-core
  polymer gas, exponentiated by CE steps 3-4; tuples with N ≤ n_c carry counterterms, N > n_c are summable (LF-n); inner
  levels decouple from the outer one (TS-d). Across levels in the fluctuating integral it is the bookkeeping (HIST) of §8.
- **RTARGET §7 form.** The "alternatively" form is met in the frozen setting, with the correction that renormalisation is
  level by level relative to the next coarser small-field level; "both suppressions kept" holds in the product form
  (TS-d) rather than as e^{-a/g_j²}e^{-a/g_{j+1}²} per inner cube (inner cubes are renormalised and need no outer factor).
- RLF-F1 AVOIDED (Proposition CL (c) with Lemma 7.2-0); **RLF-F2 AVOIDED (R1 (iii) as repaired [R1617-fix R-3b]; session
  17's proof of this was invalid, Remark 7.2-B)**; **RLF-F3 AVOIDED for BG-b-regular frozen data only** (TS-b uses no
  level-k regularity, but does use BG-b of the frozen inner data); RLF-F4 AVOIDED (Lemma RS).
- **Scope (not success items, as pre-stated):** frozen exterior (the sea is a fixed configuration); bare-form inner
  integrands; (H-ch) on every inner level (in the real integral it fails with density e^{-c/g²}: §8).

## 8. Target 3: the inductive step over scales, sea fluctuating

### 8.1 The inductive representation (I_k)
**(I_k).** There are a field-independent number 𝒱_k, a coupling g̃_k (the flow (F) shifted by Σ_{i<k}δβ_i), and a
decomposition
  e^{-S_k(U)} = e^{𝒱_k}·Σ_{𝔥∈ℋ_k}1_𝔥(U)·exp(-(1/g̃_k²)Σ_{p⊂Λ(𝔥)}s(U_p) + Σ_{X⊂Λ(𝔥)}E_k(X; U))·ℒ_𝔥(U),
where 𝔥 ranges over histories (the unreturned large-field regions created at levels < k, nested as in Dimock II
(145)-(148)), Λ(𝔥) is the level-k small-field region, E_k are small-field polymers in the norm of the small-field
package (irrelevant parts contracted; they include the returned remainders ℛ of earlier levels), and ℒ_𝔥 is the
large-field factor, |ℒ_𝔥| ≤ Π_{i<k}Π_{𝒟 unreturned at i}(C_ℓe^{-a_♯/g_i²})^{n(𝒟)}·e^{B_0|∂Ω(𝔥)|} (boundary terms O(1) per
boundary cube, as Dimock II (218) [read]) [R1617-fix R-8: exponent a_♯, defect number n(𝒟) of §1A].
(I_0) holds with 𝒱_0 = 0, ℋ_0 = {∅}, E_0 = 0, g̃_0 = g_0.
**[R1617-fix R-7b] Scope of (I_k).** (I_k) asserts the Wilson + polymer form of e^{-S_k} on Λ(𝔥) for every U_k, including
cubes where U_k is level-k bad (Proposition CL needs the action there). A small-field package produces effective actions
on small-field domains only. So (I_k) on bad cubes is itself the large-field control of the effective action: it is
named below as (H-pos)_k and weighted [P].

### 8.2 Named hypotheses (each a precise statement; none is proven here)
- **(F)** the flow, §0 (node A5 / L4a-flow).
- **(SF)_k, the small-field package at level k** = (DF1)-(DF4) of PROOF L5 [S9] for the level-k sea with the action of
  (I_k), plus the L4a-form contraction of irrelevant polymers: nodes N2, N4, N5, N6 (A1-A4).
- **(H-pos)_k [R1617-fix R-7b: separated from (SF) and re-weighted [P]].** The representation (I_k) holds on bad cubes
  too, with Σ_{X∋Q}sup|E_k(X)| ≤ E_0 per cube and the C³ bounds of E_k in the data, so that Proposition CL and Theorem R1
  hold at level k with C_r → C_re^{2E_0}, Λ_1 → Λ_1 + E_0. The reduction "(H-pos) ⇒ CL and R1 at level k" is ARGUED (the
  proofs use only positivity of the Wilson part, a per-cube bounded perturbation, and C³ bounds; not written). (H-pos)
  itself is the control of the effective action on large-field cubes, paper-scale content (CMP 122's subject by its title
  [not-read]), not a session-scale item. *Alternative route (not executed):* run CL at level k on the joint
  (U_{k-1}, U_k) integrand, RS-style, so that only small-field effective actions are used.
- **(H-Mayer)_k [R1617-fix R-7a: review gap G1].** Proposition CL (b)'s factorisation needs every factor of the integrand
  to involve the interior links of one *-component only; at effective levels the polymers E_k(X) of (I_k) have arbitrary
  extent and couple distinct components, so r_B ≠ Πr_{Y_i}. Hypothesis: after the Mayer expansion
  e^{ΣE_k} = Σ_{families}Π_X(e^{E_k(X)} - 1), jointly with the bad clusters, the gas is a polymer gas of connected unions
  (bad clusters linked by E_k-polymers) with activities ≤ (Ce^{-a''/g_k²})^{#bad cubes}e^{-κ'd} and κ' > 3κ_0 + 3, so that
  Theorem CE steps 3-4 still exponentiate it, and the frozen activities of the components keep CL (c)-(e). [s given (SF)
  and (H-pos)]
- **(PLD)_k, Peierls large deviations of the level-k sea.** For the all-cut level-k measure of (I_k) on Λ(𝔥): (i) for any
  finite set A of plaquettes with pairwise disjoint 1-neighbourhoods, P(||1 - U_p|| ≥ η_1 ∀p ∈ A) ≤ (C e^{-a_η/g_k²})^{|A|};
  (ii) for any finite set 𝒜 of cubes, P(ε_♭(U; Q) > ε_loc ∀Q ∈ 𝒜) ≤ (C e^{-a_♭/g_k²})^{|𝒜|}; a_η, a_♭ > 0 g-independent,
  uniformly in |A|, |𝒜|, T. For |A| = 1 (resp. |𝒜| = 1) this is W1-LD-cond's (LD) [proven ⇐ (DF1-3')]; the multi-point
  form needs (DF3') for general linear functionals with ℓ¹ control (N9 for general c) and a union bound over disjoint
  supports.
- **(W1-ret')_k, returned defect configurations in the fluctuating sea [R1617-fix R-8: restated; session 17's (W1-ret)
  subtracted only 𝓗(z^s)(1)].** Split r_Y = r_Y^s + r_Y^ℓ with r_Y^s := r_Y·1{ε_♭(U; Q) ≤ ε_loc for Q ∈ N(Y), and (H-ch) on
  the boxes of Y}. Hypothesis: (a) the sea average of the localised graded logarithm of §7.2 (iii), over all defect
  configurations 𝒟 with n(𝒟) ≤ n_♯ (collar-bad ones included: the two-threshold R-operation of §1A), is
    N_kc̄_0^{sea}(g_k) + δβ_k^{sea}Σ_Ps(V_P) + (returned remainders),
  with c̄_0^{sea}, δβ_k^{sea} field-independent (obtained by applying GT-lat' (i)-(ii) to the C³, gauge- and B_4-covariant
  sea-averaged activities as functions of V) and |c̄_0^{sea}|, |δβ_k^{sea}| ≤ Cg_k^{-6}e^{-a_♯/g_k²}; (b) the returned
  remainders are irrelevant small-field polymer activities in V at level k + 1, local up to e^{-κ_d d} tails, C³ in V, with
  the complex extension of (RLF-5); (c) the configurations with n(𝒟) > n_♯ carry (Ce^{-a_♯/g_k²})^{n(𝒟)}; **[R1819-fix G5]
  (d) (R1-loc): the conclusions (i)-(iii) of Theorem R1 hold for the gas of r^s, with (H-ch) required only on the boxes
  B̂_*(x) of the supports used (ARGUED; §8.3 step 2)**. This is the
  multi-defect (strong) form of W1-loc, for clusters, plus the re-extraction after the sea average; for one cube it is
  W1-loc's (LD) + (cl) ((LD) PROVEN ⇐ (DF); (cl) ARGUED [S9]). The re-extraction (a) is new content.
- **(HIST)_k, history bookkeeping for the soft kernel.** The analogue of Dimock II Theorem 3.1 (pp. 29-31 [read]): after
  the step, the unreturned regions of level k join the history (Ω_{k+1} ⊂ Ω_k for the small-field regions), the polymers
  that cross into new large regions become boundary terms bounded by e^{B_0} per boundary cube, the level-k variables
  inside unreturned regions are integrated with the crude bound ∫K_k dV = 1 (exact normalisation of the soft kernel), and
  the characteristic functions are localised (Dimock Rome p.57: "a difficult technical problem" [read-skim]).
  **[R1617-fix R-9] Ordering:** Lemma RS's event involves U_k, so the level-(k+1) large-field indicators must be inserted
  BEFORE U_k is integrated (session 17's step 6 said "at the next step"); (HIST) includes this ordering and the joint
  pricing of RS's two branches over many cubes (c_RS of §7.1).
- **(SF-last) [R1617-fix R-9: review gap G4].** The last small-field step outputs the level-K integrand as a product
  probability measure times small-activity polymers (Theorem CE's Setting CE), or the level-K cluster expansion is done
  relative to a correlated Gaussian, which needs N5's covariance bounds. Theorem CE needs a product measure (PROOF L5
  [S10]), and Wilson + polymers at small g_K is not a small-activity expansion relative to Haar measure. [s given (SF)]

### 8.3 Proposition RLF-step: (I_k) + (F) + (SF)_k + (H-pos)_k + (H-Mayer)_k + (PLD)_k + (W1-ret')_k + (HIST)_k ⇒ (I_{k+1})
with 𝒱_{k+1} = 𝒱_k + 𝒱^{sf}_k + N_kc̄_0^{sea}(g_k), 1/g̃_{k+1}² = flow(1/g̃_k²) + δβ_k^{sea}, and the same constants
(C_ℓ, B_0, E_0, a_♯, n_♯) at every level. **Status: CONDITIONAL.** [R1617-fix: session 17 wrote "a proof modulo the named
hypotheses, with every new estimate it uses proven"; that was false while review gaps G1-G4 were unnamed. They are now the
hypotheses (H-Mayer), (H-pos), the two-threshold (W1-ret'), and (SF-last). With them named, the step below is a proof
sketch modulo the named hypotheses: each step cites what it uses; steps 3-4 and 7 are the hypotheses themselves.]
1. *Exact.* Insert Π_Q(χ_Q + ζ_Q) on Λ(𝔥); Proposition CL (a) with (H-pos), and CL (b) after the Mayer expansion of
   (H-Mayer), give Z-integrand/Z_∅-integrand = ⟨Ξ⟩_cut with the frozen gas Ξ, pointwise in the sea sample.
2. *Frozen R-step.* **[R1819-fix G5: Theorem R1's hypothesis (H-ch) is global on the level (§7.2 Setting), and in a sea sample
   (H-ch) fails with density e^{-c/g²}, so R1 is not applicable as stated "pointwise in the sample". What step 2 uses is
   (R1-loc), named in (W1-ret')_k (d) of §8.2: R1 for the gas of r^s with (H-ch) required only on the boxes B̂_*(x) of the
   supports used. ARGUED: the proof of R1 (ii)-(iii) uses B̂_*(x) only; the Taylor step is applied to the smooth r_Y, not to
   r^s; and the smallness indicator is constant on the chart ball (the F1 argument of §7.2). Read "Theorem R1" below as
   (R1-loc).]** On the locally small part r^s, Theorem R1 (pointwise in the sample, cutoff n_c = n_♯) gives the
   c-numbers, the coupling shift and the remainders ℛ, with the constants of §7 (PROVEN, under (H-pos)). ℛ is of order 𝔯,
   which is O(g²) in a sea sample (§7.2 Reading): it is not small and is passed on to step 3.
3. *Sea average and re-extraction.* (W1-ret')_k (a)-(b): the sea-averaged c-number c̄_0^{sea}(g_k), the coupling shift
   δβ_k^{sea}, and returned remainders that are irrelevant small-field polymers at level k + 1 (fed into E_{k+1}); this
   covers every defect configuration with n ≤ n_♯, collar-bad ones included.
4. *Unreturned configurations.* (W1-ret')_k (c): defect configurations with n > n_♯ form new large-field regions at level k
   with weight ≤ (C_ℓe^{-a_♯/g_k²})^{n} ((PLD)_k (ii) for the collar-bad cubes, Proposition CL (c) for the frozen factor,
   W1-size' with the plug for the collar event).
5. *Small-field step.* (SF)_k integrates the level-k sea on Λ(𝔥) minus the new regions with the shifted action, producing
   E_{k+1}, 𝒱^{sf}_k and the flow.
6. *New level-(k+1) large fields [R1617-fix R-9: ordering].* Before U_k is integrated, insert the level-(k+1) indicators; a
   bad level-(k+1) plaquette is reduced by Lemma RS (PROVEN) to a level-k kernel mismatch (unconditional, (R4)) or a
   level-k plaquette ≥ η_1 ((PLD)_k (i)). These bad cubes are returned or not by the level-(k+1) R-operation like any
   others; RS supplies only their price (exponent ≥ a_RS/c_RS ≥ a_♯ per cube, §7.1).
7. *Bookkeeping.* (HIST)_k.

### 8.4 What is proven unconditionally in the induction (the level summations; not counted) [R1617-fix: (P1), (P2), (P3), (P5) PROVEN as arithmetic; (P4) ARGUED]
- **(P1) Unreturned configurations are summable (arithmetic PROVEN).** Per unit volume,
  Σ_kN_kΣ_{n>n_♯}80^{2(n-1)}(C_ℓe^{-a_♯/g_k²})^n ≤ C|T|e^{-(n_♯+1)a_♯/g_K²} for g_K ≤ g_0 (6400C_ℓe^{-a_♯/g_K²} ≤ ½), by Lemma LF-n
  and #{*-connected sets ∋ □ of size n} ≤ 80^{2(n-1)} ((g3)) [R1617-fix: session 17 cited (g3) but summed (80e)^n; one count
  is used now]. RS-generated level-(k+1) bad cubes are priced with exponent ≥ a_RS/c_RS ≥ a_♯ (§7.1) and enter the same
  sum. [R1617-fix R-8, review gap G3: session 17 summed only n > n_* and left collar-bad configurations with few cubes
  unreturned and uncovered; the two-threshold R-operation returns every configuration with n ≤ n_♯, so (P1) covers all
  unreturned ones.]
- **(P2) Coupling-shift budget (arithmetic PROVEN).** Σ_k|δβ_k| ≤ C_*Σ_kg_k^{-6}e^{-a_♯/g_k²} ≤ C'e^{-a'''/g_K²}/(1 - L^{-a'''β_-})
  (any a''' < a_♯), uniformly in K; and |δβ_k| ≤ g_k⁶ for g_k ≤ g_0. So the returned marginal parts do not disturb the AF flow
  at the order that L4a-flow controls (the one-loop and two-loop terms are O(1), O(g_k²) in 1/g² units).
- **(P3) Vacuum (arithmetic PROVEN, with R-2's Z_ref).** 𝒱_K - Σ_k𝒱^{sf}_k = Σ_kN_kc̄_0^{sea}(g_k) =: 𝒱_K^{LF}, a
  field-independent number, ≥ 0 at leading order and divergent as K → ∞ exactly when LF-count says; it cancels in
  normalised expectations, and in Z_K/Z_K^{ref} with Z_K^{ref} := exp(𝒱_K^{LF})Z_K^{sf,ref} as defined in §1A (RLF-4). This is
  (RLF-1).
- **(P4) Consistency of the nesting: ARGUED [R1617-fix: session 17 listed it as proven].** The counterterms extracted at
  level k are defined at the trivial datum and are never revised at later levels: a level-m unreturned region (m > k)
  containing returned level-k configurations keeps their c-numbers (they are part of the global constant) and carries
  their remainders as boundary/inside polymers bounded by e^{B_0} per cube, which the level-m suppression
  (C_ℓe^{-a_♯/g_m²})^{n}, n > n_♯, absorbs ((P1) with C_ℓ → C_ℓe^{B_0}). This is a structural claim about the nesting; it
  rests on (HIST)'s e^{B_0} boundary bound and is not arithmetic.
- **(P5) Composition with Theorem CE at level K (arithmetic PROVEN; composition needs (SF-last)).** Unreturned polymers X
  (in level-K cubes) have activity ≤ (C_ℓe^{-a_♯/g_K²})^{|X|}. Put H_0 := C_ℓe^{-a_♯/(2g_K²)} and κ := a_♯/(8g_K²). If
  C_ℓe^{-a_♯/(2g_K²)} ≤ 1 then (C_ℓe^{-a_♯/g_K²})^{|X|} ≤ H_0e^{-(a_♯/(2g_K²))|X|} ≤ H_0e^{-κd(X)} (d(X) ≤ 2|X|, with room to
  spare). Theorem CE [S11] needs κ > 3κ_0 + 3, i.e. **g_K² < a_♯/(8(3κ_0 + 3)) ≈ a_♯/3654**, and H_0 ≤ c_0(κ); since
  c_0(κ) ≥ c(κ_0)e^{-2κ} = c(κ_0)e^{-a_♯/(4g_K²)} (each of its three entries is ≥ a κ_0-dependent constant times e^{-2κ}), the
  second condition holds once C_ℓe^{-a_♯/(4g_K²)} ≤ c(κ_0). Both are explicit smallness conditions on g_K. Theorem CE is a
  statement about a product probability measure, so applying it to the level-K integrand needs (SF-last). The returned
  remainders and the small-field polymers need N6's rate (κ > 457 in M-units, M ≳ 1.2·10⁴), which is node A4.

### 8.5 How far the induction goes
- **Proven in the frozen setting, every level:** the R-operation of one level as an exact rewriting (§3, CL (a)-(b)), its
  estimates (CL (c)-(e), Lemma 7.2-0, R1 as repaired), its two-scale form for BG-b-regular frozen data (TS), the one-step
  pricing of coarse large fields (RS); and the level summations (P1), (P2), (P3), (P5) as arithmetic. (P4) is ARGUED.
- **Conditional (sea fluctuating):** Proposition RLF-step, modulo (F), (SF), (H-pos), (H-Mayer), (PLD), (W1-ret'),
  (HIST), and (SF-last) at level K.
- **Hence:** RLF (§1A) ⇐ these hypotheses for all k (uniform constants), by induction on k with (I_0), (P1)-(P5) and (P4)
  as argued; (RLF-4) then follows from (I_K), (P1), (P5), (SF-last) and Theorem CE at level K. This is a reduction of the
  4D large-field R-operation (node B-W2, weighted P×2) to the small-field package plus named large-field statements:
  (H-pos) [P], (HIST) [P], (W1-ret') [s to P; the re-extraction is new], (PLD) [s given SF], (H-Mayer) [s given SF and
  H-pos], (SF-last) [s given SF]. [R1617-fix: session 17 wrote "of which two are multi-defect forms of statements already
  proven for one defect"; for (W1-ret) the one-defect (cl) is ARGUED [S9]: of the two, one is a multi-defect form of a
  proven statement ((PLD) of (LD)), one of an argued one ((W1-ret') of (cl)).]

## 9. Check c32 (criteria first: checks/c32_criteria.md; script checks/c32_rlarge.py; record checks/c32_time.txt)
**All four parts PASS, first and only runs** (laptop, load ≤ 2.5, ≥ 36% free, peak RSS ≤ 41 MB, ≤ 4 s each).
- **A (Lemma RS, SU(2), d = 4, L = 3):** A1-A4 hold on 15 random configurations (t = 0.01-0.2) and three sharp ones. Random
  fields use the constants loosely (max ribbon ratio 1.99 of the proven 9; square 0.80 of 9). **A5 sharpness:** a constant
  abelian flux in the planes (α, 0) gives ribbon ratio 8.99997 and a flux in (0, 1) gives square ratio 8.99997, so
  A_4(3) = 9 and L² = 9 are attained (the area counts are exact, not overcounts). **A6:** with additional flux in the planes
  (1,2), (1,3), (2,3), UNPAIRED contour orders reach 14.9999 > 9 while the S4'-paired ones stay at 9.0000: the S4' pairing
  is load-bearing for the ribbon constant.
- **B (hard core):** B1 fattening ⇔ touching on 4000 pairs in (Z/6)⁴ (1961 touching), B2 components ↔ disjoint fattened
  families (2000 + 2000 instances), B3 the t^N coefficients of log Ξ_T are exactly extensive (c_N/T equal for T = 12, 14, 16 to
  ≤ 2e-12, N ≤ 4): the graded logarithm is local, as Theorem R1 (i) uses.
- **C (arithmetic, one-loop rate [inference]):** n_* = 382 (SU(2), ε_1 = 0.5), 95 (ε_1 = 1), 23 (ε_1 = 2); SU(3): 255, 63, 15.
  So **for every admissible ε_1 (≤ 2) the R-operation is needed (n_* ≥ 15), and n_* is finite and g-independent.**
  **[R1617-fix R-10] This conclusion is also [inference]:** it rests on the one-loop rate and on a'' = 0.9ε_1²/(4N), the
  frozen lower bound on the per-cube cost, not the true cost; n_* is a property of the bound. After R-8 the exponent that
  matters is a_♯ = min{a'', a_♭, a_RS/c_RS}, which makes the relevant integer n_♯ far larger (§7.1). RS at
  N = 2, κ = 1, ε_1 = 0.5: η_1 = 2.7·10⁻⁵, plaquette exponent η_1²/4 = 1.8·10⁻¹⁰, kernel exponent 4.9·10⁻⁴; CL: ε_loc = 3.5·10⁻³.
  These are g-independent but very small (crude constants, recorded as such).
- **D (GT-lat' (ii)):** the full B_4 average of 20 random t is (tr t/6)·1 to 1e-12; the rotation-only average is
  non-scalar in 20/20 (reflections needed, as in c19 P1).
- [R1617-fix] c32 tests none of CL (c), R1 (iii) or TS (REVIEW_S16_S17); c33 below tests R1 (iii)'s localisation step.

## 9A. Check c33 [S18] (criteria first: checks/c33_criteria.md; script checks/c33_bfour.py; record checks/c33_time.txt)
Toy B_4 step (R-3b): explicit hard-core gases with isometry-covariant scalar activities r_Y(D) (depending on D on Y and its
*-boundary), F^tup_x = the repaired tuple-support localisation, F^fat_x = session 17's fattened one.
- **B (d = 4, T = 7, N ≤ 2, all 384 elements of B_4 about x): PASS.** F^tup_x is invariant to ≤ 1.3e-15 (relative); F^fat_x
  changes by 0.68-3.9 (relative) for each of three random fields; the review's case ({x - e_1} has x in its fattening, its
  reflection {x + e_1} does not) confirmed; on constant data F^tup_x = F^fat_x to 2.7e-14 (Remark 7.2-B).
- **A (d = 2, T = 9, N ≤ 3, whole torus, brute-force log Ξ): FAIL as pre-registered** (A1, A4, A5), on the constant seed
  only, where the double-precision brute-force coefficient c_3 = a_3 - a_1a_2 + a_1³/3 cancels ~3 digits (relative errors
  2.9e-9 against the written 1e-10 / 1e-12). On the five random seeds the tuple identity holds (A1, A4 ≤ 5.6e-12); A2
  (tuple localisation invariant under all 8 elements, ≤ 6.2e-14) and A3 (fattened not invariant, 0.61-2.0) hold on every
  seed; A5's F^tup = F^fat on constant data holds (4.8e-13). Post-run diagnostic (not a criterion; c33_diag_mp.py): at 40
  digits the constant seed's tuple totals equal the brute-force coefficients to ≤ 3.0e-34. No criterion edited.
- Scope: toy scalar activities, not Wilson/soft-kernel ones; it tests the combinatorics and the permutation property, not
  GT-lat' (ii) (c32 D).

## 10. Outcomes against the pre-stated targets (§1-§2)
- **Target 1 (RLF stated): MET.** §1 states RLF with all quantifiers in the soft setting; §8.4 (P3), (P5) and §7 give its
  composition with LF-count (the divergence is exactly the vacuum c-number of clusters N ≤ n_*), with R4D-iso (|Y| = 1,
  frozen), and with Theorem CE (explicit condition g_K² < a''/(8(3κ_0 + 3)) for the unreturned polymers). One correction to
  §1 found in the derivation: (RLF-2)'s per-cell summation of the returned remainders is not a separate large-field
  estimate; once returned they are irrelevant small-field polymers, and their summation is the small-field package's
  contraction (node A4). BG-sum/TS-b is its frozen-background shadow.
- **Target 2 (two-scale, frozen exterior): MET as pre-stated, in the frozen setting** (Proposition CL, Theorem R1, Theorem
  TS, Lemma RS, Lemma GT-lat'). Constants are stated (§5-§7, c32 C). W2-F1 CIRCUMVENTED with BG-b at the last small-field
  level; W2-F2 AVOIDED; W2-F3 AVOIDED (frozen); RLF-F1-F4 AVOIDED. Not success items as pre-stated: frozen sea, bare-form
  integrands, local smallness everywhere near Δ.
- **Target 3 (inductive step): PARTIAL, as pre-stated allowed.** Proposition RLF-step is a proof of (I_k) ⇒ (I_{k+1})
  modulo five named hypotheses; the level summations (P1)-(P5) are proven unconditionally; RLF ⇐ the hypotheses for all k
  by induction (§8.5).
- **[R1617-fix] Corrections to the three bullets above (session 18; the bullets are kept as written in session 17).**
  Target 1: RLF needed repairs (§1A: two thresholds, Z_ref, (SF-last), complex fields). Target 2: R1 (iii)'s B_4 step was
  false as written and TS's hypothesis region too small (REVIEW_S16_S17: GAP); both are repaired in §7.2-§7.3, and W2-F1 and
  RLF-F3 are circumvented/avoided for BG-b-regular frozen data only. Target 3: the step was conditional on four further
  unnamed gaps, now named ((H-pos) [P], (H-Mayer), (W1-ret') with the re-extraction, (SF-last)); (P4) is ARGUED.

## 11. Exact remaining walls (weights: P = paper-scale, s = session-scale)
1. **(SF)_k, the small-field package at every level** (N2 BG-reg, N4, N5, N6; L4a-form with the contraction of irrelevant
   polymers; [R1617-fix: (H-pos) is now item 6, separately]): unchanged, [P×3-4] (A1-A4 of the critical path). The R-operation adds to it only the
   requirement that returned remainders (C³ in the data, of order 𝔯) be admissible polymer activities.
2. **(PLD)_k, Peierls large deviations of the sea** (§8.2): multi-point forms of W1-LD-cond's (LD). Inputs: (DF3') for
   general linear functionals with ℓ¹ control (N9 generalised), W1-size' with a product plug over disjoint defects
   (proven for one defect). [s, given (SF)].
3. **(W1-ret')_k [R1617-fix R-8: restated], returned defect configurations in the fluctuating sea** (§8.2): the strong
   (multi-defect) W1 for configurations of size ≤ n_♯ (collar-bad included) plus the collar split, AND the sea-averaged
   re-extraction of the c-number and marginal parts (new content). Inputs: (DF4), Theorem CE with the frozen activities as single-block factors (Proposition
   CL supplies their size and derivatives), the corridor localisation of W1-cl (argued [S9]). [s to P].
4. **(HIST)_k, history bookkeeping for the soft kernel** (§8.2): the analogue of Dimock II Theorem 3.1 (nested regions,
   boundary terms, localisation of the characteristic functions). [P: the size of Dimock II; CMP 122 II's "localization,
   exponentiation" by its title].
5. **(F), the flow** (A5) and the compatibility |δβ_k| ≤ g_k⁶ (proven, P2). [P].
6. **(H-pos)_k [R1617-fix R-7b: re-weighted from [s] to [P]]:** the Wilson + polymer form of the effective action on
   level-k BAD cubes, i.e. the large-field control of the effective action (a small-field package controls it on
   small-field domains only). The step "(H-pos) ⇒ CL and R1 at effective levels" is ARGUED (bounded per-cube perturbation),
   not written [s]; (H-pos) itself is [P]. Alternative route (not executed): CL on the joint (U_{k-1}, U_k) integrand.
6a. **(H-Mayer)_k [R1617-fix R-7a]:** the joint Mayer expansion of the non-local E_k with the bad clusters (§8.2).
   [s given (SF), (H-pos)].
6b. **(SF-last) [R1617-fix R-9]:** the level-K integrand as product measure times small activities, or a correlated-Gaussian
   cluster expansion (needs N5). [s given (SF)].
7. **Constants.** η_1 and ε_loc are tiny (c32 C). η_1 comes from the linear δ_c term in RS (R4); for near-unitary M̄ the
   deviation is quadratic, which would improve η_1 to O(ε_1/L²). Not needed for correctness. [s, optional].
Not a wall: W3 (the main path has no constraint fibres; RLF's kernel branch is unconditional because the soft kernel is a
normalised conditional density).

## 12. Status and tally contribution
- PROVEN-HERE [S17] (unreviewed), counted: **Lemma GT-lat'** (§4); **Proposition CL** (§5, with the Fubini identity and the
  per-cube-uniform size bound); **Theorem TS** (§7, counted with Theorem R1 and the box-merging step); **Lemma RS** (§6).
  Not counted: Lemma LF-n and (P1)-(P5) (arithmetic); §3 (definition); the c32 instances.
- CONDITIONAL: Proposition RLF-step (§8.3). ARGUED: (H-pos) extension of CL/R1 to effective levels.
- OPEN: RLF (§1) itself, now reduced to the walls of §11 (inside L5; no new top-level item).
- L5 stays IMPORTED-NOT-YET-REVERIFIED (CMP 122 not read); RLF is the re-derivation target that would replace it.
- Tally: 64/2/7/24 + 1 → **68 / 2 / 7 / 24 + 1 comparison-branch.**
- **[R1617-fix] Session-18 status.** REVIEW_S16_S17 confirmed GT-lat' and RS, confirmed CL with fix CL-1 (applied, §5 (d)),
  and held Theorem TS + Theorem R1 at **GAP** (corrected tally 67/2/7/24 + 1). Session 18 writes R-3a (Lemma 7.2-0), R-3b
  (§7.2 (iii)), R-4 (§7.2 (iv)) and R-5 (§7.3), the four fixes the review names as restoring the item. So **Theorem TS +
  Theorem R1 is counted again as PROVEN-HERE [S18-repair, unreviewed]: 68/2/7/24 + 1.** Not counted: Remark 7.2-B (a
  second route; ARGUED level), Lemma 7.2-0 (counted with R1), (P1)-(P3), (P5) (arithmetic), (P4) (ARGUED), c33.
- CONDITIONAL [S18]: Proposition RLF-step, modulo (F), (SF), (H-pos), (H-Mayer), (PLD), (W1-ret'), (HIST), (SF-last).


---

## 13. Session-18 targets (pre-stated 2026-10-27 21:47 UTC, after reading REVIEW_S16_S17 and before any written session-18 repair or the c33 criteria)
Binding: REVIEW_S16_S17 "Required fixes" 1-9 for this file, tagged **[R1617-fix]** where applied.
- **A (R-3b, the B_4 step).** Re-localise Theorem R1 (iii) so that the family of localised terms at a base point x is
  genuinely permuted by B_4 about x, and derive the single coupling shift from GT-lat' (ii). **Not success:** a base-point
  assignment that uses Ŷ = Y + {0,1}⁴; an invariance asserted without the explicit permutation of the family.
- **B (R-3a, R-4, R-5).** Cluster size bounds from (H-ch) for clusters of every size; the torus wrap (torus side vs cluster
  size) handled with a uniform-in-K bound; TS's hypotheses stated on the region R1 actually uses; g² < a''/3 stated.
- **C (R-6).** "Remainder of irrelevant order" narrowed to BG-b-regular frozen data, with a statement of what holds in a
  sea sample; TS marked as not used by RLF-step.
- **D (R-1, R-2, R-7a/b, R-8, R-9, R-10, (P1)/(P4)/§8.5, CL-1, complex fields).** RLF's statement repaired in a separate
  amended block (§1A) without renumbering §1; the four unnamed inductive-step gaps G1-G4 named as hypotheses; (P4) ARGUED.
- **E (check c33, criteria first).** A toy instance of the B_4 step: on explicit finite gases with B_4-covariant
  activities, the fattened base-point localisation is NOT invariant under B_4 about x, and the repaired (tuple-support)
  localisation IS, with both summing to the same graded logarithm, checked against brute-force log Ξ.
- **Acceptable outcome if A fails:** the failing step named and the TS/R1 item left at GAP in the tally (67).

## 14. Session-18 outcomes (ADDED AFTER the repairs; pointers only)
- §13 A (R-3b): **met.** §7.2 (iii): tuple localisation on unfattened supports; the family {𝓖_S/|S| : S ∋ x} is permuted by
  B_4 about x (explicit bijection τ ↦ Rτ); GT-lat' (ii) gives one coupling shift. Remark 7.2-B: the session-17 value of δβ_j
  was right (centre independence + translation), the written step was not. c33 B PASS.
- §13 B: **met.** Lemma 7.2-0 (R-3a); §7.2 (iv) wrap term, ≤ (L⁴/(L⁴ - 1))W⁴ cubes in all, uniform in K (R-4); §7.3 on Δ_*
  with (R1)_i global and g_i² < a''/3 (R-5). [S18 note] C_♮ for the chart ball (constants only).
- §13 C: **met.** §7.2 Reading, §7.3 Role, §7.4; PROOF [S17] pointer and LOG session 17 annotated.
- §13 D: **met.** §1A (two thresholds with a_♯, n_♯; Z_ref; (SF-last); (RLF-5)); §8.2 (H-pos) [P], (H-Mayer), (W1-ret'),
  (SF-last), (HIST) ordering; §8.3 status corrected; §8.4 (P1) one count factor and full coverage, (P4) ARGUED; §8.5 wording;
  §9 C [inference]; §5 (d) Λ_1 = 6 + 8κ(2 + C_𝒩); §11 items 1, 3, 6, 6a, 6b.
- §13 E: c33 — B PASS; A FAIL as pre-registered (float cancellation in the brute-force side at the constant seed; A2/A3
  hold; 40-digit post-run diagnostic agrees to 3e-34). §9A.
- Tally: 67 (review) → 68 (TS/R1 repaired, unreviewed). With N5-triv (PROOF [S18], outside this file): 69.

**[S20 note]** REVIEW_S18_S19 fix 8 applied in session 20 (annotations only; §1/§1A numbering unchanged): F1 (§7.2
Setting), F2 (§1A, §7.2 (iv)), G5 ((R1-loc) in §8.2 (W1-ret') (d), §8.3 step 2), the N5 threshold compatibility and the c_RS
dependence of n_♯ (§1A item 1), the W⁴ sentence (§7.2 (iv)). RLF-step stays CONDITIONAL, now also on (R1-loc) (ARGUED).
