# HW: lane H of the 4D YM proof push. The history weight hypothesis (H-w) (session 1, 2026-10-28)

Scope. Constructive UV stability of 4D lattice SU(N) Yang-Mills, soft-kernel RG of decision 4 (normalised S4' kernel,
D4-norm). Target: HIST §7.4's hypothesis **(H-w)**, the per-history weight bound that Theorem HIST-sum consumes, and
RLARGE v2 integration conflicts **K5** (RS-joint is a probability bound, branch (iii) an integrand bound; their combination
over many cubes is not written) and **K3** (extraction-collar cost over levels). This file edits nothing else; its log is
HW_LOG.md, its checks are checks/w*.

Status words as in PROOF.md: PROVEN-HERE (counted or not, said each time), CONDITIONAL (an implication proven, its
hypotheses named), ARGUED, OPEN, HYPOTHESIS. "Given H" marks every hypothesis a statement consumes. Literature: none is
load-bearing here; Balaban CMP 122 and Dimock's large-field papers are not used. One classical inequality is used
(Chebyshev's integral inequality for monotone functions), with its one-line proof written out (§6).

Inputs read this session (read-only; md5 at 01:51 UTC: HIST.md fd756e0b…, RLARGE.md 24a73553…, PLD.md 4db9b142…, FLOW.md
2e77959e…): HIST.md §0, §2-§3, §7 (all), §8, §12, §14.0-§14.1, §15.1-§15.4; RLARGE.md v2 §0-§8 (Appendix A not re-read);
PLD.md §15.2-§15.3 (per-history measures, (SG^fl), Lemma HS-net, PLD-SG, INH, PLD-desc); REVIEW_HIST_S1.md on (H-w) and
HIST-sum (l.280-312); REVIEW_PLD_S3.md on SG-1 and branch (iii) (l.196-215, l.470-500). ~~REVIEW_HIST_S3 is not present.~~ **[RHW1-fix H-11] That remark was false: REVIEW_HIST_S3.md
(mtime 01:38:51 UTC) existed before this read (01:51 UTC) and was missed; its N-4 (C_cone) and S3-5 (cone dilution) are
applied in session 2 (fixes W-2, H-5). Correction also appended in HW_LOG.**
FLOW.md is used only through RLARGE v2 §0's statement of (F_R).

File order. §0-§1 were written at **2026-10-28 01:52 UTC**, after reading the inputs and after exploratory reasoning, and
BEFORE any written derivation (§2 onward) and before any w-check criteria file. They are not edited after the
derivations start; outcomes are pointers in §10, added afterwards.

---

## 0. Conventions (RLARGE v2 §0 and HIST §0, §7.1, unchanged; additions marked)

- Levels k = 0 … K; U_k the level-k field; the chain W(U_0, …, U_K) = e^{-S_0(U_0)}Π_{k<K}K_k(U_{k+1}, U_k), S_0 = u_0Σ_ps(U_p),
  K_k = Π_ck^{(k)}_c, k^{(k)}_c(V; M) = e^{-κu_kφ_M(V)}/∫e^{-κu_kφ_M} (HIST (3.0)), u_k := 1/g_k². ∫K_k dU_{k+1} = 1, Z_K = ∫W.
- History 𝔥 = (𝒰_0, …, 𝒰_{K-1}), shadows sh, Σ, regions Ω^c_k(𝔥), Λ_k(𝔥), admissibility (A1)-(A2), Lemma H-nest, Lemma
  H-geo: HIST §7.1-§7.2 verbatim. **Λ^pre_k(𝔥) := all level-k cubes ∖ Σ(Ω^c_{k-1}(𝔥))** (Λ^pre_0 := all).
- (F_R) along the chain's own sequence: β_-(m - j)log L - R ≤ u_j - u_m ≤ β_+(m - j)log L + R (0 ≤ j ≤ m). In particular
  **u_{k+1} ≤ u_k + R** (one step, j = k, m = k + 1).
- Tower and cones (HIST §14.0, §15.1): Φ_i(U, V) = Σ_cφ_{M̄_c(U)}(V_c); the equalised chain energy E(chain) = Σ_ps(U_0(p)) +
  κΣ_iΦ_i(U_i, U_{i+1}); the cone 𝒞(P) of a level-k plaquette P and its cone energy E_𝒞(P).
- *Addition.* **Defect sets.** D_j is the set of level-j cubes that are defects (bad: ζ_Q = 1; collar-bad: the clause of
  RLARGE v2 §2.2 in force), computed by fixed history-independent rules from (U_{j-1}, U_j) (from U_0 at j = 0).

*[RHW1-fix S-2, added in session 2; §1 below is the frozen session-1 text]* Failure mode **(HW-F5)**: rate degradation across
levels in a moment ⇒ price ⇒ moment loop (a price at rate θ obtained from moments at a larger rate one level down, fed back
as a moment). Treated in §15.

## 1. Pre-stated targets (2026-10-28 01:52 UTC)

### Target W1: (H-w) in the three-way-pricing language
State (H-w) as: history weight ≤ (small-field reference ratio) × Π over defects of the product of the three branch prices,
with every quantifier, and with the reference object named precisely (what Z^sf is, what "small-field partition function
ratio" means). Say exactly how it relates to HIST §7.4's form, and whether HIST-sum's proof consumes it unchanged.

### Target W2: (H-w) given the three branch bounds, and K5
- Write the three branch bounds as named hypotheses (each with an owner file), in a currency in which they COMBINE.
- Prove the combination over many defects and many levels: the product over defects of all levels, with every
  constant independent of g, K, T and the history.
- Resolve K5 precisely: what the probability form (RS-joint, PLD-desc) and the integrand form (branch (iii)) each are, why
  (or whether) they do not combine as written, and the exact statement that makes them combine. **Failure modes to watch:**
  (HW-F1) a per-cube normalisation of log(1/g) entering B_0 (HIST (HI-F2)); (HW-F2) a greedy/independence factor that
  grows with the level or with n; (HW-F3) a bound that is relative to Z_K rather than to a small-field reference (it
  would make HIST-sum vacuous); (HW-F4) circularity between the branch hypotheses and (H-w) itself.
- Success: a CONDITIONAL theorem "(H-w) ⇐ named hypotheses", proven, with the hypotheses strictly smaller than (H-w) or
  identical to existing named items. Partial success: a proven reduction with one new named hypothesis stated precisely.

### Target W3: K3
Decide whether the extraction-collar cost of HIST's pointwise R1_Λ route sums over levels, separately for the part
attached to large-field regions and the part inside the sea; prove what can be proven (arithmetic), and state what it
means for E3 (extraction after the sea average).

### Check w1 (criteria first: checks/w1_criteria.md, then the script)
A small numerical check of whatever elementary inequality or combinatorial count the derivation makes load-bearing
(candidates: a kernel moment bound, a multiplicity count), with a negative control. Informational, never a proof.

---
# Derivations (written after §0-§1; started 01:57 UTC)

## 2. The exact history representation

**Lemma HR (indicator form of the history sum): PROVEN-HERE (elementary, not counted).** For a chain configuration
c = (U_0, …, U_K) define recursively, for j = 0, 1, …, K - 1,
  𝒰_j(c) := the union of the *-components of D_j(c) ∩ Λ^pre_j(𝒰_0(c), …, 𝒰_{j-1}(c)) that have more than n_♯ cubes.
Then 𝔥(c) := (𝒰_j(c))_j is admissible, and for every admissible 𝔥, 1_𝔥(c) := 1{𝔥(c) = 𝔥} = Π_j1^𝔥_j(U_{j-1}, U_j) with
  1^𝔥_j := 1{the union of the *-components of D_j ∩ Λ^pre_j(𝔥) with > n_♯ cubes equals 𝒰_j},
a function of (U_{j-1}, U_j) for fixed 𝔥. Σ_𝔥1_𝔥 ≡ 1. Hence **Z(𝔥) := ∫W·1_𝔥 ≥ 0 and Σ_𝔥Z(𝔥) = Z_K.**
*Proof.* (A1) holds by construction; (A2) because 𝒰_j(c) ⊂ Λ^pre_j = complement of Σ(Ω^c_{j-1}). If 𝒰_i(c) = 𝒰_i for i < j then
Λ^pre_j(c) = Λ^pre_j(𝔥), so 𝒰_j(c) = 𝒰_j iff 1^𝔥_j = 1; induct on j. Each c has exactly one history. ∎
*Remarks.* (1) **[RHW1-fix H-1]** Z(𝔥) is *defined* as ∫W·1_𝔥; that is all (H-w) needs (some decomposition Z_K = ΣZ(𝔥),
Z(𝔥) ≥ 0). [inference, not used:] the R-operation (CL^J (a)-(b), R1^J, the sea average) rewrites ∫W·1_𝔥 with the returned
components summed inside the event, so that Z(𝔥) would be HIST §7.4's history weight once the defect rules are fixed; that
every R-operation term lands in the same 𝔥 is not checked. (2) If the defect rule near Σ(Ω^c_{j-1}) is history-dependent
(RLARGE's two-threshold collar rule), D_j = D_j(c; 𝒰_{<j}) and the proof of HR is unchanged. **[RHW1-fix H-2] Lemma RX (ii)
and (iii) below, and the consequence Z(∅) ≤ Z(R(𝔥)), use the history-independent convention of §0;** with a history-dependent
D_j, D_j differs between 𝔥 and ∅ and (ii) can fail. Theorem HW and everything after it use only that convention.

**Lemma RX (the relaxed event): PROVEN-HERE (elementary, not counted).** For admissible 𝔥 put
  R(𝔥) := ∩_j{every *-component of D_j ∩ (Λ^pre_j(𝔥) ∖ N_1(𝒰_j)) has ≤ n_♯ cubes},  Z(R) := ∫W·1_R,  μ_R := W·1_R/Z(R).
Then (i) {𝔥(c) = 𝔥} ⊂ R(𝔥) ∩ {𝒰_j ⊂ D_j ∀j}; (ii) {𝔥(c) = ∅} ⊂ R(𝔥); (iii) R(∅) = {𝔥(c) = ∅}
(**[RHW1-fix H-2] (ii) and (iii) for history-independent D_j, §0**; (i) for any defect rule). In particular
  **Z(𝔥) = Z(R(𝔥))·μ_{R(𝔥)}(𝔥),  Z(∅) ≤ Z(R(𝔥)).**
*Proof.* (i) On {𝔥(c) = 𝔥} the components of D_j ∩ Λ^pre_j are 𝒰_j's components and components with ≤ n_♯ cubes; distinct
components are *-separated (cube distance ≥ 2), so the small ones miss N_1(𝒰_j), and D_j ∩ (Λ^pre_j ∖ N_1(𝒰_j)) is their union.
(ii) A *-component of D_j ∩ S (any set S) is *-connected inside D_j, hence lies in a component of D_j, which has ≤ n_♯ cubes on
{𝔥(c) = ∅}. (iii) Λ^pre_j(∅) = all cubes. ∎

## 3. Target W1: (H-w) in the three-way language, and what its reference must be

### 3.1 The currency: (H-w) is a ratio statement
**Proposition PF (plain-chain probabilities are the wrong currency): PROVEN-HERE (elementary, not counted).** P(𝔥) := Z(𝔥)/Z_K
is a probability on histories (Lemma HR). Suppose a family of bounds of the Z_K-relative form Z(𝔥) ≤ Z_K·Π_{(j,𝒟)}v(j, 𝒟), i.e.
(H-w) with Z^sf := Z_K. Then HIST-sum's conclusion Σ_{𝔥≠∅}Z(𝔥) ≤ Z_K(e^S - 1), S := C_H|T|e^{-(n_♯+1)a/g_K²}, is implied by
Σ_𝔥P(𝔥) = 1 alone as soon as S ≥ log 2, and for every T with S ≥ log 2 it carries no information on Z_K/Z(∅).
*Proof.* Σ_{𝔥≠∅}Z(𝔥) ≤ Z_K ≤ Z_K(e^S - 1) when e^S ≥ 2. ∎
**[RHW1-fix H-3]** Z_K-relative per-history bounds give no lower bound on P(𝔥 = ∅) at all: a law with one large defect
component at a uniformly random position has P(𝔥) = 1/|T| ≤ w for every fixed w once |T| ≥ 1/w, and P(∅) = 0.
*Reading (failure mode HW-F3).* (RLF-3)-(RLF-4) need Z_K ≤ Z^sf·e^{S} for EVERY torus, with Z^sf a small-field object
(Z^sf ≤ e^{o(|T|)}·Z(∅) at least). So every branch bound must reach (H-w) as a bound **relative to a reference whose
normalisation does not see the defects**, never relative to Z_K. RS-joint (HIST §7.3) is proven under W/Z_K (plain chain):
however sharp its constant (even c_RS = 1), it cannot be multiplied into (H-w) as it stands. PLD's per-history law μ_{𝔥,ω} is
of the right (relative) type, but with ω frozen. Lemma RX supplies the relative law that works for all levels at once: μ_{R(𝔥)},
the chain conditioned on "no unreturned defect outside 𝔥's own regions".

### 3.2 (H-w), restated
Two references are admissible for HIST-sum (which uses only Z(∅) ≤ Z^sf and the per-history bound): **(ref-a) Z^sf := Z(∅)**
(the exact all-small-field history weight; then (RLF-4)'s comparison with node A's small-field partition function is a
separate statement about Z(∅)), or **(ref-b)** node A's explicit small-field partition function with shifted couplings
(RLARGE (RLF-4)), with Z(∅) ≤ Z^sf part of node A's output.

**Lemma HS' (HIST-sum with per-component shadow sums): PROVEN-HERE (one line, not counted).** Theorem HIST-sum holds verbatim
if (H-w)'s factor exp(B_0Σ_k|Ω^c_k(𝔥)|) is replaced by the larger exp(B_0Σ_{(j,𝒟)}Σ_{k=j}^{K-1}|sh_k(𝒟)|) (sum over the
components 𝒟 of the 𝒰_j). *Proof.* HIST-sum's step (2) bounds Σ_k|Ω^c_k| by exactly this double sum and uses nothing else of
it. ∎ Call this form **(H-w')**; it is weaker than (H-w) and is what is proven below.

**(H-w)³ (the three-way form; definition of the target).** There are θ ∈ (0, 1], a_D > 0, C_mis, C_fine ≥ 1 and B_0 ≥ 0,
independent of g, K, T, 𝔥 and n_♯ (for g_K ≤ g_0(n_♯)), such that for every admissible 𝔥
  Z(𝔥) ≤ Z^sf · exp(B_0Σ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|) · Π_jΠ_{Q∈𝒰_j}[ e^{-θa_D(u_j - R)} · C_mis^{n_int/2} · C_fine^{1/2} ],
  n_int := dL^{d-1}(L - 1) (= 216 at d = 4, L = 3; the links of a cube's interior).
Read per defect cube Q of level j: **coherent-energy price** e^{-θa_D u_j} (the deterministic energy threshold, §4), times the
**mismatch factor** C_mis^{n_int/2} (branch (i): the kernel exponents of Q's links, a moment), times the **fine factor**
C_fine^{1/2} (branches (ii) + (iii) together: the tower energy of the finer fields under Q, a moment); and the **small-field
ratio** Z(R(𝔥))/Z^sf ≤ exp(B_0·shadow sums). It is (H-w') with **a := θa_D, C_ℓ := e^{θa_DR}C_mis^{n_int/2}C_fine^{1/2}**, so
HIST-sum consumes it unchanged (with Lemma HS'). The difference from RLARGE §3.4's reading (each defect priced by ONE branch, the
prices then multiplied) is the point of §5: the suppression is one energy price per defect, and the branches enter as moment
constants of one joint law. In the "assignment" reading, Π_Q(π^i_Q + π^ii_Q + π^iii_Q) is recovered by Lemma CH with
X_Q := the window of the branch that fires (§5, Corollary).

**Theorem HW-split: PROVEN-HERE (elementary, not counted).** (H-w') ⇐ (PRICE) + (REL), with B_0 = B_1 + B_2, where
- (PRICE): μ_{R(𝔥)}(𝔥) ≤ Π_{(j,𝒟)}(C_ℓe^{-au_j})^{|𝒟|}·exp(B_1Σ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|);
- **(REL)_B**: Z(R(𝔥)) ≤ Z^sf·exp(BΣ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|). Under (ref-a) this is **μ_{R(𝔥)}(∅) ≥ exp(-B·shadow sums)**
  (relaxing the small-field constraint on 𝔥's regions costs at most e^B per shadow cube per level). At 𝔥 = ∅ it reads Z(∅) ≤ Z^sf.
*Proof.* Lemma RX: Z(𝔥) = Z(R(𝔥))μ_{R(𝔥)}(𝔥). ∎
*Owner of (REL).* **[RHW1-fix S-1: superseded under (ref-a), see §13; the session-1 attribution follows, kept as written.]**
Node A / (SF^J) and (RLF-4): it is HIST §7.4's B_0 list (a)-(d) (top-down ∫K = 1, polymers meeting Ω^c,
normalisation mismatch, unextracted ℛ^∂ and vacuum/coupling-shift corrections near Ω^c) with NO defect price in it. In the
route of §5 the removed-cone normalisation of branch (iii) is NOT part of (REL); it is the moment (M-f). **[RHW1-fix H-4] The
next sentence is [inference, not used]:**
(REL) is self-consistent with (H-w): Z(R(𝔥))/Z(∅) = Σ over histories 𝔥' ⊂ R(𝔥) of Z(𝔥')/Z(∅), whose unreturned components all
meet N_1 of 𝔥's regions, and (H-w) for those gives a factor exp(O(e^{-a/g²})) per shadow cube; this is a bootstrap, not a proof
(the 𝔥' are not smaller than 𝔥).

## 4. The deterministic part: energy windows on defect events

**Definition (tower energies).** For a level-m plaquette P (m ≥ 1) and a level-m field V:
- ℰ_P(V) := inf{E_𝒞(P)(U_0, …, U_{m-1}, V)} over the finer fields (HIST §15.1 cone energy, equalised units);
- ℰ^<_P(U_{m-1}) := inf over U_0, …, U_{m-2} of the sum of the non-top terms of 𝒞(P) (for m = 1: the level-0 plaquette terms,
  no infimum).
The top terms of 𝒞(P) are the four kernel terms φ_{M̄_c(U_{m-1})}(V_c), c ∈ ∂P (HIST §15.1), and M̄_c(U_{m-1}) reads U_{m-1} only in
c's endpoint blocks, inside W_P^{(m-1)}. So ℰ_P(V) depends on V only through V|∂P, and ℰ^<_P on U_{m-1}|W_P^{(m-1)}.
- For a set A of level-(k+1) cubes, the **column energy** F^col_A(U_k) := inf over U_0, …, U_{k-1} of the sum of all chain terms
  of levels ≤ k lying in the column of A (level-0 plaquettes with all vertices in A's level-0 descendants; kernel terms of
  level-(i+1) links, i + 1 ≤ k, with both endpoints in A's level-(i+1) descendants). For k = 0, F^col_A(U_0) := Σ of the level-0
  plaquettes in A (no infimum).
All three are infima of continuous functions over compact sets, hence continuous, nonnegative and bounded.

**Lemma TE (tower-energy splitting): PROVEN-HERE [HW-1] (counted, with W-bad).**
- (i) ℰ_P(V) ≤ κΦ_{∂P}(U, V) + ℰ^<_P(U) for every level-(m-1) field U, Φ_{∂P}(U, V) := Σ_{c∈∂P}φ_{M̄_c(U)}(V_c).
- (ii) **[RHW1-fix W-2 + lane-G switch, session 2] Given (CLS-min)_{c_pr,t_pr}** (below) and level-m torus side ≥ 3:
  **ℰ_P(V) ≥ c_pr·min{||1 - V_P||²_op, t_pr²}** for every V. *(Session-1 text: "Given (AE): s(V_P) ≤ C'_cl·ℰ_P(V) with
  C'_cl := max{C_loc, 2/η_E}"; that constant was the superseded (AE)'s, REVIEW_HIST_S3 N-4.)*
  **(CLS-min)_{c,t}** [SQ §0.1's consumed statement]: for every m ≥ 1, every level-m plaquette P (level-m side ≥ 3) and every
  top V, the cone-local free-boundary minimum ℰ_P(V) = 𝓔^{𝒞(P)}(V) satisfies ℰ_P(V) ≥ c·min{||1 - V_P||², t²}. Two sources:
  - **(primary) (CLS-min) ⇐ (REG-min)** [OPEN, P; SQ §0.3, the cone-local sup form of (BG)_k / (SF-bg), node A], by SQ's
    Lemma DESC with Theorem SUP-price and Corollary PRICE-iii (SQ session 1, PROVEN-HERE there given (REG-min); not yet
    reviewed): c_pr = c_♭/C'², t_pr = C'τ_♭ (c_♭ = 1/640, C' = 53 at N = 2, L = 3; τ_♭ the maximal admissible τ of DESC,
    τ_♭ ≤ θ_0/C' with SQ's θ_0 ≈ 10⁻⁸/C_D²).
  - (alternative) (CLS-min) ⇐ (AE) [HIST §15.3; CONDITIONAL ⇐ (MS-Sob) by Theorem AE-red, HIST §26, CONFIRMED as such by
    REVIEW_HIST_S4] via Theorem CLS-red in its RH3-fix N-4 form s ≤ C_cone·E_𝒞(P), C_cone := max{C'_AE/(2N), 2/η_E} = 2/η_AE
    = 1.1-2.3·10¹⁵ (N = 2; h7 C), and s(V) ≥ ||1 - V||²_op/(2N): c = 1/(2NC_cone), t = 2.
- (iii) For a level-(k+1) cube Q with interior plaquettes 𝒫(Q) and every level-k field U:
  Σ_{P∈𝒫(Q)}Φ_{∂P}(U, V) ≤ 2(d - 1)Φ_{int Q}(U, V) (Φ_{int Q} the sum over the n_int links of int Q), and
  Σ_{P∈𝒫(Q)}ℰ^<_P(U) ≤ 24F^col_Q(U); likewise Σ_{p}ℰ_p(U) ≤ 24F^col_A(U) over the level-k plaquettes p in the column of A.
*Proof.* (i) E_𝒞(P) = κΦ_{∂P}(U_{m-1}, V) + (non-top terms), so ℰ_P(V) = inf_U[κΦ_{∂P}(U, V) + ℰ^<_P(U)] ≤ the value at any U.
(ii) ℰ_P(V) is by definition (§4) the infimum of E_𝒞(P) over the finer fields with top V, i.e. SQ's 𝓔^{𝒞(P)}(V) (cone terms
read the finer fields only inside the cone and V only on ∂P), so (ii) is (CLS-min) verbatim. [For the alternative source:
CLS-red gives s(U_m(P)) ≤ C_coneE_𝒞(P) for every chain; take the infimum.] **Only the infimum is used** (the lane-G question,
answered in §12A). (iii) A link of int Q lies in ≤ 2(d - 1) plaquettes. The non-top terms of
𝒞(P), P ∈ 𝒫(Q), have their vertices in W_P^{(·)}, which descends from P's corners, sites of Q: they are column terms of Q. A
term lies in ≤ 24 cones (HIST §15.1 overlap). All terms are ≥ 0, so Σ_P inf(·) ≤ inf Σ_P(·) ≤ 24·inf(column sum). The same for the
cones 𝒞(p) of level-k plaquettes p in A's column (their top terms are level-k kernel terms, column terms of A). ∎

**Lemma W-bad (windows for bad cubes): CONDITIONAL [HW-1] (proven ⇐ (CLS-min), i.e. ⇐ (REG-min) or (AE)); its level-0 case
PROVEN-HERE.** Let k ≥ 0, Q a
level-(k+1) cube with ζ_Q(V) = 1 (V = U_{k+1}), and put
  X_Q := u_{k+1}Σ_{P∈𝒫(Q)}ℰ_P(V).
Then X_Q ≥ a_bad·u_{k+1}, **a_bad := c_pr·min{ε_1², t_pr²}** [RHW1-fix W-2; session 1 had ε_1²/(2NC'_cl)], and, if
g_k² ≤ 1/R, for every level-k field U:
  X_Q ≤ 12κu_kΦ_{int Q}(U, V) + 48u_kF^col_Q(U).
For a level-0 cube Q with ζ_Q = 1, X_Q := u_0Σ_{p⊂int Q}s(U_0(p)) ≥ u_0ε_1²/(2N), by (B) alone.
*Proof.* Some P ∈ 𝒫(Q) has ||1 - V_P||_op ≥ ε_1, and TE (ii) gives ℰ_P(V) ≥ a_bad. Upper bound: TE (i) and (iii) give
X_Q ≤ u_{k+1}[2(d - 1)κΦ_{int Q} + 24F^col_Q], and u_{k+1} ≤ u_k + R ≤ 2u_k (§0, (F_R); Ru_k^{-1} = Rg_k² ≤ 1). ∎
*Reading.* The coarse plaquette is priced by its OWN tower energy at its own coupling u_{k+1} = u_j: no RS dichotomy is needed
for the lower bound. The three branches reappear in the UPPER bound: the coarse coherent energy is at most the stage-k kernel
mismatch energy (branch (i)) plus the fine tower energy of the column (fluctuation (ii) and coherent background (iii) together).
The split of the fine part into fluctuation and background (PLD-desc's B_V) is not needed anywhere below.

**Lemma W-cb (windows for collar-bad and non-quiet cubes): CONDITIONAL [HW-1, uncounted] (⇐ (CLS-min) and (TC)).** Reading of RLARGE
v2 §2.2 used here: σ_Q = 0 means (α) some level-k plaquette p ⊂ N_1(Q) has ||1 - U_p|| > ε_loc/2, or (β) some c ∈ C(Q) has
||V_c - S_c(U)|| > ε_loc/2, with C(Q) and the endpoint blocks of its links inside N_1(Q) [reading of PLD §9.1, not re-checked];
non-quiet (joint route) means some level-k plaquette of R_k(Q) is ≥ η_q. Put X^cb_Q := κu_kΦ_{C(Q)}(U, V) + u_kΣ_pℰ_p(U) (p over
the level-k plaquettes in the column of N_1(Q)). If **(TC) ε_loc/2 ≥ (16N + 3)A_dη_q**, then on {Q collar-bad or non-quiet}
  X^cb_Q ≥ a_cb·u_k,  a_cb := min{c_pr·min{ε_loc²/4, t_pr²}, κε_loc²/(64N), c_pr·min{η_q², t_pr²}}  [RHW1-fix W-2/lane-G switch],
and X^cb_Q ≤ κu_kΦ_{C(Q)} + 24u_kF^col_{N_1(Q)}.
*Proof.* (α) and non-quiet: TE (ii) at level k (k = 0: ℰ_p = s exactly, and (B): s ≥ ||1 - U_p||²/(2N) ≥ c_pr||1 - U_p||² when
c_pr ≤ 1/(2N), true for both sources). (β) If both endpoint blocks of c are quiet
(< η_q), δ := ||M̄_c - S_c|| ≤ A_dη_q ≤ δ_0 (RS (R1)), so Lemma PM gives ||W_0 - S_c|| ≤ 3δ and ||M̄_c - W_0|| ≤ 4δ; with
t := ε_loc/2 and x := ||V_c - W_0|| ≥ t - 3δ ≥ max{16Nδ, t/2} by (TC), Lemma KQ (lower) gives φ_c ≥ x²/(2N) - 4δx ≥ x²/(4N) ≥
t²/(16N) = ε_loc²/(64N). If a block is not quiet, the non-quiet case applies. Upper bound: TE (iii). ∎ (The same algebra at
t = ε_1/8 reproduces RS-lin (b)'s exponent κε_1²/(1024N), and at t = ε_loc/2 RLARGE §3.1's κε_loc²/(64N); whether RLARGE's
ε_loc obeys (TC) is for the owner of the thresholds.)

**Lemma DJ (disjointness of bad windows): PROVEN-HERE (elementary, counted with W-bad).** For an admissible 𝔥, the term sets
used by the bad windows of distinct pairs (k, Q), Q ∈ 𝒰_{k+1}, are disjoint: the links of int Q and the column terms of Q.
*Proof.* Same level: distinct cubes have disjoint interiors and columns. Levels k' < k, Q' ∈ 𝒰_{k'+1}: Q ∈ Λ^pre_{k+1}, so the
level-k cubes under Q are in Λ_k (the argument of H-nest (ii): N_1(Q) ∩ π(Ω^c_k) = ∅) and, by H-nest (iii), every descendant of Q at a level ≤ k lies in the small-field
region of its level; Q' ⊂ Ω^c_{k'+1} is not a descendant of Q, so neither its interior links nor its column meet Q's column. ∎
(Collar windows of neighbouring cubes overlap: a level-k cube lies in N_1(Q) for ≤ 3⁴ = 81 cubes Q.)
**[RHW1-fix H-5]** DJ is exactly the selection that makes the bad windows of a history disjoint across levels, so Theorem HW is
not hit by REVIEW_HIST_S3 S3-5's (24k)⁻¹ dilution of multi-level cone charges. DJ is not used by Lemma CH (which needs no
disjointness); the moment hypotheses' multiplicity 1 depends on it. (Returned defects inside a history cube's column are NOT
covered by DJ; this is where §15's wall sits.)

## 5. Target W2: the combination over many defects and many levels (K5)

**Lemma CH (exponential-Markov combination): PROVEN-HERE [HW-2] (counted).** Let 𝔥 be admissible, θ ≥ 0, and for every defect
cube Q of 𝔥 (Q ∈ 𝒰_j, any j) let X_Q ≥ 0 be a bounded measurable function of the chain with X_Q ≥ π_Q on {Q ∈ D_j}. Then
  **Z(𝔥) ≤ Z(R(𝔥)) · exp(-θΣ_Qπ_Q) · E_{μ_{R(𝔥)}}[exp(θΣ_QX_Q)].**
*Proof.* Lemma RX (i): 1_𝔥 ≤ 1_{R(𝔥)}Π_Q1{Q ∈ D_j}, and pointwise 1{Q ∈ D_j} ≤ exp(θ(X_Q - π_Q)) (the right side is ≥ 1 on the
event and ≥ 0 off it). Multiply, integrate against W ≥ 0, divide and multiply by Z(R(𝔥)). ∎
No probability, conditional independence, greedy subfamily or disjointness of supports is used; the defects of all levels enter
one pointwise product (failure mode HW-F2 avoided).

**Lemma EQ (the moment is the removed-window normalisation): PROVEN-HERE (exact, not counted).** For a probability μ and a
bounded measurable X ≥ 0, with μ^{(t)} := e^{tX}μ/E_μe^{tX}: log E_μe^{θX} = ∫_0^θE_{μ^{(t)}}[X]dt. If μ ∝ e^{-X}ν (X a window
energy carried by the density), μ^{(t)} ∝ e^{-(1-t)X}ν is the law with the window softened to 1 - t, and E_μe^{θX} is the ratio of
the softened to the unsoftened partition function. *Proof.* d/dt log E_μe^{tX} = E_{μ^{(t)}}X (X bounded), value 0 at t = 0. ∎
*Corollary (what the three branch forms are).* (iii) RLARGE §3.3's integrand bound "on the event, e^{-X} ≤ e^{-θπ}e^{-(1-θ)X}; the
removed-cone integrand is then absorbed" is Lemma CH with the removed-cone normalisation = E_{μ_R}e^{θX} (Lemma EQ). (i), (ii) A
probability bound μ(E) ≤ p is Lemma CH's output for a single law. **So the three branches are Chernoff bounds whose moments are
computed under three different laws: RS-joint under W/Z_K (plain chain), PLD-desc under μ^+_{𝔥,ω} (**[RHW1-fix H-6]** forward:
U from μ_{𝔥,ω}, exterior frozen, then V from the kernel; only its hypothesis (SG^fl) is conditional on V, and only for good
V ∈ 𝒱^sf; Proposition FV does not refute it), branch
(iii) under an unnamed law. That is K5 precisely: no single law carries all three moments, so the prices cannot be multiplied.
They combine as soon as the moments are stated jointly under μ_{R(𝔥)} (Lemma CH), and then the combination is one inequality.**
Failure mode HW-F1 in this language: a per-window normalisation of log(1/g) means E_{μ^{(t)}}[X] ∝ log(1/g); a Gaussian-like
window has E[X] ≈ (number of degrees of freedom)/(2(1 - t)), g-independent.

**Proposition FV (the fixed-coarse-field reading is false): CONDITIONAL (proven ⇐ (CLS-min); [RHW1-fix: RECOUNTED as
uncounted], a two-line corollary of TE).** For every k, every
level-(k+1) cube Q, every V with ζ_Q(V) = 1 and EVERY level-k field U:
  κΦ_{int Q}(U, V) + F^col_Q(U) ≥ a_bad = c_pr·min{ε_1², t_pr²}.
Hence for every family of conditional laws of U_k given U_{k+1} = V, and every λ > 0,
  sup_V E[exp(λu_k(κΦ_{int Q} + F^col_Q)) | U_{k+1} = V] ≥ exp(λa_bad/g_k²) → ∞ as g_k → 0.
*Proof.* TE (ii), (i): a_bad ≤ ℰ_P(V) ≤ κΦ_{∂P}(U, V) + ℰ^<_P(U) ≤ κΦ_{int Q}(U, V) + F^col_Q(U) (Φ_{∂P} ≤ Φ_{int Q}; the non-top
terms of 𝒞(P) are column terms, all ≥ 0). ∎
*Reading.* Mismatch plus fine energy cannot be small uniformly over the coarse field: its smallness is the rarity of bad V, a
statement about V's law. This is Proposition INH / CF (PLD §15.3, HIST §6) in the energy currency, now for every V and every U
(given (CLS-min); "every U" comes from TE (i), which is unconditional, not from a general-chain bound). It rules out the RG-direction ("integrate U_k at fixed U_{k+1}") version of branch (iii)'s normalisation. It does
NOT rule out the **forward** version: under the plain chain, V is drawn from K_k(·, U_k) given U_k, and the joint moment factorises
as (kernel moment given U_k, exact) × (moment under the level-k marginal), Lemma KS-chain below. "In-step" in RLARGE §3 is
therefore to be read forward: stage k consumes the level-k effective density and the stage-k kernel, never a fixed-V law.

**Lemma HÖ (splitting the joint moment by branch): PROVEN-HERE (Cauchy-Schwarz, not counted).**
E[e^{θ(Y_1 + Y_2)}] ≤ (Ee^{2θY_1})^{1/2}(Ee^{2θY_2})^{1/2}.

### 5.1 The branch hypotheses in the joint currency (each named, with owner)
Fix 𝔥; sums run over the defect cubes Q ∈ 𝒰_{k+1} (k ≥ 0) of 𝔥; level-0 cubes are listed under (M-f) with k = -1, u_{-1}F^col_Q :=
u_0Σ_{p⊂int Q}s(U_0(p)).
- **(M-i)_λ [branch (i), mismatch; owner: HIST H-4, a form of it in the indicator representation [RHW1-fix H-8]; plain-chain
  case PROVEN for SU(2), Lemma KS-chain].**
  E_{μ_{R(𝔥)}}[exp(λΣ_Qκu_kΦ_{int Q})] ≤ C_mis(λ)^{n_int·#Q}.
- **(M-f)_λ [branches (ii) + (iii), fine fields; [RHW1-fix S-2] OPEN [P]; small-field half: (I_k^E) / (SF^J) (node A);
  large-field-tail half (returned finer defects): owned by this file since session 2, §15].** E_{μ_{R(𝔥)}}[exp(λΣ_Qu_kF^col_Q(U_k))] ≤ C_fine(λ)^{#Q}.
  **[RHW2-fix SDP-1]** Both halves are node A's: the capped form actually consumed is (M-f^A)_θ ⇐ (SF-cap)^A + (SDP)^A (§18.1);
  "large-field-tail half: owned by this file" is withdrawn.
- **(CLS-min)** [through TE (ii) only; ⇐ (REG-min) (SQ, OPEN, P, node A's (BG)_k/(SF-bg) in cone-local sup form), or
  ⇐ (AE) (off the critical path)]. *Session 1 listed (AE) here.*
- **(REL)_B** [[RHW1-fix S-1] under (ref-a): ⇐ the moment hypotheses over the relaxed family by Lemma REL-seq (§13); node A
  keeps only the torus-wide comparison Z(∅) ↔ Z^sf (§13.3)]: Theorem HW-split.
The constants C_mis, C_fine, B must be independent of g, K, T, 𝔥 and n_♯; (M-i), (M-f) are allowed an extra factor
exp(cΣ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|) (absorbed into B_0 by Lemma HS').

**Theorem HW ((H-w) given the three branch bounds): CONDITIONAL [HW-2] (implication PROVEN-HERE, counted).** Assume (F_R) with
g_K² ≤ 1/(2R), (CLS-min) [session 1: (AE)], (M-i)_{24θ}, (M-f)_{96θ} and (REL)_{B_2}, for some **θ ∈ (0, 1/96)**
[RHW1-fix W-1; session 1 wrote (0, 1/24), vacuous on [1/96, 1/24) because (M-f)_λ needs λ = 96θ < 1, §6's own
(1 - λ)^{-dof/2} heuristic], with the defect notion D_j := {Q : ζ_Q = 1}
(bad cubes; the collar clause is added below). Then for every admissible 𝔥,
  Z(𝔥) ≤ Z^sf·exp(B_2Σ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|)·Π_jΠ_{Q∈𝒰_j}[e^{-θa_bad u_j}·C_mis(24θ)^{n_int/2}·C_fine(96θ)^{1/2}],
i.e. **(H-w)³ and (H-w') hold with a = θa_bad, C_ℓ = C_mis^{n_int/2}C_fine^{1/2} (no e^{aR} factor in the defect price: the
bad window is priced at the coupling u_j of its own level), B_0 = B_2.** Consequently (Theorem HIST-sum with Lemma HS'), for
n_♯ ≥ n_H(a, B_0) and 6400C_ℓe^{aR}e^{38417B_0}e^{-a/g_K²} ≤ ½: Σ_{𝔥≠∅}Z(𝔥) ≤ Z^sf(exp(C_H|T|e^{-(n_♯+1)a/g_K²}) - 1), uniformly
in K, **with C_H computed from C_ℓe^{aR} in place of C_ℓ [RHW1-fix W-4: HIST-sum's step (5) under (F_R), RLARGE v2-F]**.
*Proof.* g_k² ≤ g_K²/(1 - Rg_K²) ≤ 2g_K² ≤ 1/R for all k ((F_R), u_k ≥ u_K - R), so Lemma W-bad applies at every level. Lemma CH
with π_Q := a_bad u_j and the windows X_Q of W-bad; then X_Q ≤ Y^mis_Q + Y^fine_Q with Y^mis_Q := 12κu_kΦ_{int Q}, Y^fine_Q :=
48u_kF^col_Q (level 0: Y^fine_Q := X_Q); Lemma HÖ with the parameters 24θ and 96θ; (M-i), (M-f); then (REL). ∎
*With collar-bad and non-quiet cubes.* The same proof with Lemma W-cb's windows: a_D := min{a_bad, a_cb}, the price e^{-θa_D(u_j - R)}
(collar windows are at the coupling u_k = u_{j-1} ≥ u_j - R), (TC) added, and (M-i), (M-f) for the collar sums
Σκu_kΦ_{C(Q)}, Σu_kF^col_{N_1(Q)} (multiplicity ≤ 81 + 1). **[RHW1-fix W-3]** Because collar windows overlap up to 82 times,
Σ_QF^col_{N_1(Q)} can reach 82× the column energy of the union, so the collar extension is stated with **θ ∈ (0, 1/(96·82))**
(equivalently: (M-f) for the collar sums is assumed at rate 96θ with the multiplicity carried in the hypothesis). The reduction of (M-i) to (LI) below does NOT cover collar links,
which are also read by the neighbours' collar clauses inside R(𝔥) (Conflict K2's territory); for them (M-i) is consumed as stated.

### 5.2 What is proven about (M-i): Lemma KS, KS-chain, and the reduction of H-4
**Lemma KS (SU(2) kernel moments and softening): PROVEN-HERE [HW-4] (counted).** G = SU(2). Let ||M||_op ≤ 1 with M a real
combination of SU(2) elements (as M̄_c is: an average of contour transporters), so M = rŴ, r = ||M||_op ∈ [0, 1], Ŵ ∈ SU(2). Put
b := κur ≥ 0 and 𝒩(b) := ∫_0^πe^{-b(1-cos α)}(2/π)sin²α dα. Then:
- (a) for r > 0, W_0(M) = Ŵ and φ_M(V) = r(1 - cos α) = r||V - W_0||²_op/2, α the rotation angle of V⁻¹Ŵ; the kernel is
  k_c(V; M) = e^{-b(1-cos α)}/𝒩(b) in the angle variable;
- (b) **b·E_b[1 - cos α] ≤ 3/2 for every b ≥ 0** (E_b under the density ∝ e^{-b(1-cos α)}sin²α on [0, π]), with equality in the
  limit b → ∞;
- (c) for λ ∈ [0, 1): ∫k_c(V; M)e^{λκuφ_M(V)}dV = 𝒩((1-λ)b)/𝒩(b) ≤ (1 - λ)^{-3/2}, uniformly in M, u, κ;
- (d) (integrand form) on {||V - W_0||_op ≥ t}: k_c(V; M) ≤ (1 - λ)^{-3/2}e^{-λκurt²/2}k^{[(1-λ)κ]}_c(V; M), k^{[κ']} the normalised
  kernel at stiffness κ'.
*Proof.* (a) For a unit quaternion Ŵ, Re tr(W⁻¹rŴ) = r·Re tr(W⁻¹Ŵ) ≤ 2r with equality iff W = Ŵ; V⁻¹Ŵ has eigenvalues e^{±iα}, so
φ = ½(2r - 2r cos α) and ||V - Ŵ||_op = |1 - e^{iα}| = 2sin(α/2); the Haar law of α is (2/π)sin²α dα; the factor in (3.0) gives the
kernel. (r = 0: the kernel is Haar and everything below is trivial.) (b) Substitute w := 1 - cos α ∈ [0, 2]: sin²α dα =
√(w(2 - w))dw. Let ν_b be the probability on [0, 2] with density ∝ e^{-bw}√w. Chebyshev's integral inequality (for f increasing
and h decreasing, ∫∫(f(x) - f(y))(h(x) - h(y))dν(x)dν(y) ≤ 0, i.e. E[fh] ≤ E[f]E[h]) with f = w, h = √(2 - w) gives
E_b[w] = E_ν[wh]/E_ν[h] ≤ E_ν[w]. Again with f = w, h = 1{w ≤ 2} under the Gamma(3/2, b) law γ on (0, ∞): E_ν[w] =
E_γ[w1]/E_γ[1] ≤ E_γ[w] = 3/(2b). Laplace's method gives bE_b[w] → 3/2. (c) The kernel integral is 𝒩((1-λ)b)/𝒩(b) by (a);
(log 𝒩)'(s) = -E_s[w], so log 𝒩((1-λ)b) - log 𝒩(b) = ∫_{(1-λ)b}^bE_s[w]ds ≤ ∫(3/(2s))ds = (3/2)log(1/(1 - λ)) by (b). (d) On the
event w ≥ t²/2, e^{-bw} ≤ e^{-λbt²/2}e^{-(1-λ)bw}, and e^{-(1-λ)bw}/𝒩(b) = [𝒩((1-λ)b)/𝒩(b)]k^{[(1-λ)κ]}_c. ∎
*Remarks.* (1) The exponent 3/2 = dim SU(2)/2 is sharp (b), so the softening ratio is g-independent and not better: this is
HW-F1 avoided for kernel windows, exactly. (2) Compared with RS-lin (b), (d) has no polynomial prefactor (κ/g²)^{N²-1}: the
prefactor came from bounding the normalisation from below separately (KQ global); the ratio form cancels it. **[RHW1-fix H-7]**
(d)'s suppression exponent λκurt²/2 carries r = ||M̄||, so it is weak for degenerate M̄ (r small); Theorem HW uses only (c).
(3) **(KS-N) for SU(N), N ≥ 3 [HYPOTHESIS, s]:** sup_{||M||≤1, β≥0}βE_{β,M}[φ_M] =: c_N < ∞ (then (c) holds with exponent c_N).
For M = rŴ (scalar polar part) it is a statement about the class function 1 - N⁻¹Re tr X, checked numerically for N = 3 in w1 B;
for general M (degenerate polar parts) it is not checked.

**Lemma KS-chain (plain-chain mismatch moments): PROVEN-HERE for SU(2) (counted with KS).** For every finite set 𝒦 of links
(any levels) and λ_c ∈ [0, 1): E_{W/Z_K}[Π_{c∈𝒦}exp(λ_cκu_{k(c)}φ_c)] ≤ Π_{c∈𝒦}(1 - λ_c)^{-3/2}.
*Proof.* The special case R = everything (h ≡ 1, c_k = 0) of Lemma H4-red below; it needs only Lemma TD and Lemma KS (c). ∎

**Lemma LI-a (the relaxed event does not read the interior links of 𝔥's cubes): PROVEN-HERE (definition-level, not counted).**
Write 1_R = Π_j1_{R,j}(U_{j-1}, U_j). Let Q ∈ 𝒰_{k+1}. Then no factor 1_{R,j} reads the links of int Q, provided the defect clauses
read only: ζ_{Q'} the interior plaquettes of Q'; σ_{Q'} and quietness data in the column of N_1(Q') (levels j - 1, j) and the
links C(Q') ⊂ N_1(Q').
*Proof.* j ≤ k: these factors read levels ≤ k. j = k + 1: 1_{R,k+1} reads D_{k+1} on Λ^pre_{k+1} ∖ N_1(𝒰_{k+1}), whose cubes Q'
have cube distance ≥ 2 from Q, so N_1(Q') ∩ Q = ∅. j = k + 2: a cube Q'' of Λ^pre_{k+2} has distance ≥ 2 from π(Ω^c_{k+1}) ∋ π(Q),
so N_1(Q'') ∌ π(Q), and the level-(k+1) data it reads are not under π(Q) ⊃ Q. j ≥ k + 3: these read levels ≥ k + 2. ∎
So the int Q links influence the future only through the kernel K_{k+1}(U_{k+2}, U_{k+1}) (the M̄ of the 2d level-(k+2) links at the
site that Q is), and from there along the kernels above 𝔥's persistent shadow [inference for levels ≥ k + 3].

**Hypothesis (LI) (future insensitivity; a precise form of H-4 in the indicator representation [RHW1-fix H-8]: HIST's H-4
concerns the effective-density tilt e^{Σρ}, expected 1 + O(e^{-a''/g²}); (LI) concerns the exact future probability h and
allows e^{c_LI} per shadow cube per level) [OPEN; owner: this file; weight s to P].** With
h_{k+1}(U_{k+1}) := ∫Π_{i>k}K_i(U_{i+1}, U_i)Π_{j≥k+2}1_{R,j}dU_{k+2}⋯dU_K (the conditional probability of R's future given U_{k+1}),
for every k and all V, V' that differ only on the links of int(𝒰_{k+1}): h_{k+1}(V) ≤ e^{c_k}h_{k+1}(V'), with
c_k ≤ c_LIΣ_{𝒟∈comp(𝒰_{k+1})}Σ_{m≥k+1}|sh_m(𝒟)|, c_LI independent of g, K, T, 𝔥.

**Lemma H4-red ((M-i) ⇐ (LI)): PROVEN-HERE [HW-5] (counted).** G = SU(2). Assume (LI) and the data-reading of Lemma LI-a. For
λ ∈ [0, 1) and sets 𝒦_k ⊂ links of int(𝒰_{k+1}):
  E_{μ_{R(𝔥)}}[Π_kΠ_{c∈𝒦_k}e^{λκu_kφ_c}] ≤ Π_ke^{c_k}·(1 - λ)^{-3|𝒦_k|/2}.
So (M-i)_λ holds with C_mis(λ) = (1 - λ)^{-3/2} and the shadow factor exp(c_LI·shadow sums) (absorbed in B_0, Lemma HS').
*Proof.* Let k_1 be the largest level with 𝒦_{k_1} ≠ ∅ and G_k := Π_{c∈𝒦_k}e^{λκu_kφ_c}. By the Markov structure of W,
∫W1_RΠ_kG_k = ∫e^{-S_0}Π_{i<k_1}K_iΠ_{j≤k_1}1_{R,j}Π_{k<k_1}G_k·I, I := ∫K_{k_1}(V, U_{k_1})1_{R,k_1+1}G_{k_1}h_{k_1+1}(V)dV.
Split V = (V_𝒦, V_rest). By LI-a, 1_{R,k_1+1} does not depend on V_𝒦. By (LI), h_{k_1+1}(V) ≤ e^{c}h̲(V_rest), h̲ := inf over V_𝒦.
Since K_{k_1} = Πk_c with the links independent given U_{k_1}, Lemma KS (c) gives
  I ≤ e^{c}(1 - λ)^{-3|𝒦|/2}∫dV_restΠ_{rest}k_c1_{R,k_1+1}h̲ ≤ e^{c}(1 - λ)^{-3|𝒦|/2}∫K_{k_1}1_{R,k_1+1}h_{k_1+1}dV
(h̲ ≤ h and ∫Π_{𝒦}k_cdV_𝒦 = 1). The last integral is I with G_{k_1} := 1. Repeat for the next level down; divide by Z(R). ∎

### 5.3 Outcome for K5
K5 is resolved as follows. **(1)** The three branch prices are Chernoff bounds (Lemma CH, Lemma EQ) whose moments were stated
under three different laws; that, and not "probability versus integrand", is why they did not combine. **(2)** Stated as joint
moments under the single relaxed law μ_{R(𝔥)}, they combine over all defects and all levels by one pointwise inequality
(Lemma CH), with no greedy or independence factor; the deterministic input is one energy threshold per defect (Lemma W-bad,
⇐ (CLS-min); session 1: (AE)), and the branches enter through the upper splitting of that energy (TE, HÖ). **(3)** The moments cannot be stated at a
fixed coarse field (Proposition FV); they are forward objects. **(4)** Branch (i)'s moment is PROVEN for the plain chain (SU(2),
KS-chain) and reduced in-history to one named hypothesis (LI) (H4-red); branches (ii)+(iii) merge into one fine-field moment (M-f),
owned by the small-field package. **(5)** Not consumed by Theorem HW: RS-joint, (PLD-q)_k, (SG^fl)_k, PLD-desc, (BG)_k, the
case split of RLARGE §3.4, and the boundary family E10 (bad windows lie in the cube's own column, inside the small-field
columns by Lemma DJ's argument, so no extension of (SG^fl) to ∂Λ(𝔥) is needed in this route).

## 6. Status of the remaining moment and reference hypotheses

**(M-f) [[RHW1-fix S-2] OPEN [P] (session 1: ARGUED, not confirmed). Small-field half: (I_k^E)/(SF^J), node A. Large-field-tail
half (returned finer-level defects in Q's column, allowed under μ_R): owned by this file, §15.] [RHW2-fix SDP-1: tail half
re-owned to node A as (SDP)^A; the capped form is (M-f^A) ⇐ (SF-cap)^A + (SDP)^A, §18.1.]** The bullets below concern
the small-field half only; the "UV-dominated" heuristic does not address the tail. [RHW1-fix H-9: the localisation (a) cited
below has been replaced in HIST by (a') and the analytic main term of §25 (RH3-fix S3-6); the reduction is an upper bound and
survives with the current form.]
- *Reduction to the main term (PROVEN-HERE given (I_k^E)(a)'s localisation; uncounted).* If 𝓔_{k,x} assigns to the level-k cube x
  exactly the terms of the global tower minimiser lying over x (HIST §14.1 (a)), then F^col_Q(U_k) ≤ Σ_{x under Q}𝓔_{k,x}(U_k): the
  global minimiser restricted to Q's column is a competitor in F^col's infimum. So (M-f) under the plain chain follows from
  E_W[exp(λu_kΣ_{x∈A}𝓔_{k,x})] ≤ C^{|A|}, which by Lemma EQ is the ratio of the level-k partition functions with u_k → (1 - λ)u_k on
  the main term over A: a **local coupling response** of the small-field package. For a Gaussian-like density it is
  ≈ (1 - λ)^{-(dof in A)/2}e^{O(E_0)|A|}, g-independent [ARGUED: it needs node A's cluster expansion with an inhomogeneous coupling,
  and GAP S2-1 (𝓔_{k,x} defined only for globally small fields) is inherited].
- *Not (SG) in disguise [ARGUED, one-loop heuristic].* F^col is a sum of nonnegative local energies. A coherent background from
  levels m > k contributes ≈ u_k·g_m²L^{-4(m-k)} per level-k cube (curvature scales by L^{-2} per level), summable in m; PLD's
  Finding 1 obstruction concerns aligned LINEAR functionals, whose variance g(ℓ)² grows with the region. So (M-f) is UV-dominated
  and is not obstructed by asymptotic freedom in the way (SG^ph)/(SG^net) are.
- *In-history.* Under μ_{R(𝔥)} the fine column of Q influences R's future through U_{k+1} on Q, the same channel as (M-i); an (LI)-type
  reduction is plausible and not written. R does read the column (it imposes "returned only" there): that conditioning is the
  small-field restriction (I_k^E) is about, not an obstruction.
- *Level 0.* (M-f) at level 0 is E_{μ_R}[exp(λu_0Σ_{p∈A}s(U_0(p)))] ≤ C^{|A|}; OPEN as stated even for the plain Wilson measure
  uniformly in u_0 [the first moment E[u_0s(U_p)] ≤ C on a torus follows from translation invariance and a two-sided bound on the
  Wilson partition function in axial gauge, inference, not written].

**(REL) [[RHW1-fix S-1] superseded under (ref-a): (REL) ⇐ the moment family by Lemma REL-seq (§13); node A owns only the
single comparison Z(∅) ↔ Z^sf (§13.3). Session-1 text kept:] [OPEN, P; owner node A / (RLF-4)].** Content: HIST §7.4's B_0 items (a)-(d) without any defect price. §7 below settles the
K3 part of item (d). Item (c)'s fragility (HIST RH1-fix H-11) now sits here alone: a log(1/g) per relaxed cube per level in
Z(R(𝔥))/Z^sf would make n_H infinite. In the route of §5 the removed-cone normalisation of branch (iii) has moved out of B_0 into
(M-f), where it is a moment of a nonnegative local energy.

**(LI) [OPEN].** Lemma LI-a shows the only channel is the next kernel's M̄ at the site Q, then the kernels above the persistent
shadow. The allowance c_LI per shadow cube per level is what HIST-sum can absorb (Lemma HS'); a bound growing with the depth of
the shadow faster than its size would not be absorbable.

**Circularity (HW-F4).** None of (AE), (M-i), (M-f), (LI), (REL) consumes (H-w) or HIST-sum. (REL) is only self-consistent with
(H-w) (bootstrap, §3.2), which is not used.

## 7. Target W3: K3, the extraction-collar cost over levels

**[RHW1-fix H-10]** ∫W·1_𝔥 contains no extraction, so K3-a and K3-b bear only on representation-based derivations
((ref-b), and an RG-side derivation of (M-f) through (I_k^E)); Theorem HW's B_0 = B_2 has no K3 content.
HIST's RLF-step^J step 2 extracts R1_Λ's c-numbers and δβ^J_k pointwise in the sea sample on Λ^in only; the cost of not
extracting on the extraction collar (width w_* ∝ n_c) has two parts.

**Lemma K3-a (the part attached to large-field regions is summable over levels): PROVEN-HERE (arithmetic, not counted) | HIST
§7.6 (TS_K's ℛ^∂ bound), §7.5 (P2) [RH2-fix N-1].** Let c_∂(g) := 2κ_0Bc_0K_0(2w_* + 1)⁴e^{-a''/g²} + |δβ|12L⁸(2w_* + 1)⁴ (the
per-cube bound on the unextracted tuple terms and on the missing shift near Ω^c_i ∪ N_1(𝒰_i)). If g_K is so small that
82·c_∂(g_i) ≤ 1 for every i (**[RHW1-fix K-1]** it suffices that 82c_∂(g) ≤ 1 for ALL g² ≤ 2g_K², since (F_R) gives only
g_i² ≤ g_K²/(1 - Rg_K²) ≤ 2g_K², and c_∂ is increasing for g² < a''/3; c_∂ now also contains (P3)'s vacuum correction near
Ω^c, ≤ C(n_♯)e^{-a''/g²} per cube, HIST l.586-588, which changes nothing in kind), then
  Σ_iΣ_{x near Ω^c_i}(ℛ^∂ and missing-shift costs) ≤ Σ_i|Ω^c_i(𝔥)| ≤ Σ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|,
so this part adds at most 1 to B_0 and is summed over levels by HIST-sum's persistence arithmetic (Lemma HS').
*Proof.* |Ω^c_i ∪ N_1(𝒰_i)| ≤ |Ω^c_i| + 81|𝒰_i| ≤ 82|Ω^c_i| (𝒰_i ⊂ Ω^c_i, |N_1(A)| ≤ 3⁴|A|); multiply by c_∂(g_i) ≤ 1/82; Σ_i|Ω^c_i| ≤ the
shadow sums (union bound, as in HIST-sum step (2)). ∎ *Non-circular:* the increment is 1, independent of n_♯; n_H is fixed from
B_0, then n_♯ ≥ n_H, then w_* ∝ n_♯, then g_0(n_♯) (REVIEW_HIST_S1's order for item (d)).

**Lemma K3-b (the in-sea part is not summable as bookkeeping): PROVEN-HERE (arithmetic, not counted; the P4-div mechanism).**
Suppose the in-sea extraction-collar cost is carried as a per-cube term, bounded per collar-bad level-(k+1) cube by
c_k := C_1e^{-a''_Ju_k} (polynomial factors ≥ 1 dropped), and the density of collar-bad cubes is bounded only by p_k := C_2e^{-a_cbu_k}
(PLD-SG (iii): a_cb = a_♭/7⁴). Then the per-final-cell bookkeeping bound B_cell(K) := Σ_{k<K}L^{4(K-1-k)}p_kc_k obeys, with
a := a''_J + a_cb,
  B_cell(K) ≥ C_1C_2e^{-a(u_K+R)}L^{-aβ_+}Σ_{m=0}^{K-1}L^{(4 - aβ_+)m},
which tends to ∞ as K → ∞ whenever aβ_+ ≤ 4.
*Proof.* (F_R) upper half: u_k ≤ u_K + β_+(K - k)log L + R; put m := K - 1 - k. ∎
*Reading.* With the constants of h4 (a_♯ ≈ 2·10⁻¹¹; a''_J, a_cb of the same order), aβ_+ ≪ 4: HIST's pointwise route cannot carry the
in-sea collar cost as a bookkeeping term. The missing shift δβ_kΣ_{collar}s(U_p) is a MARGINAL operator, not an irrelevant one, so
it is not contracted by the small-field steps either; it must be re-extracted, i.e. absorbed into the sea-averaged c̄_0^{sea}, δβ_k
at V = 1 (E3, RLARGE v2 §2.4 (γ)), with the collar-bad family 𝓗^{cb} inside the sea average. **K3 outcome: the Ω^c-attached part
is settled (summable, ≤ 1 in B_0); the in-sea part is not summable as bookkeeping (proven, for the bound), which supports E3;
the residual is I-tay^J (the two-field W1R-tay), unchanged.** (As for P4-div, this is a statement about the bound, not a lower
bound on the true contribution.)

## 8. Lemma DAG of this file

```
(H-w') ⇒ HIST-sum (Lemma HS')                                 [HIST-sum CONFIRMED conditional, REVIEW_HIST_S1]
(H-w') ⇐ Theorem HW-split: (PRICE) + (REL)                    [PROVEN, elementary]
(PRICE) ⇐ Lemma CH (Chernoff, PROVEN) + windows + joint moment
   windows: Lemma W-bad ⇐ TE (i) [PROVEN] + TE (ii) ⇐ (CLS-min) ⇐ (REG-min) [SQ, OPEN, P] (or ⇐ (AE))      (level 0: PROVEN by (B))
            Lemma W-cb ⇐ the same + PM, KQ, RS (R1) [PROVEN, HIST/RLARGE] + (TC) [threshold condition]
   joint moment ⇐ Lemma HÖ [PROVEN] + (M-i) + (M-f)
      (M-i) ⇐ Lemma H4-red [PROVEN, SU(2)] ⇐ Lemma KS [PROVEN, SU(2)] + LI-a [PROVEN, definition-level] + (LI) [OPEN]
            (plain chain: Lemma KS-chain, PROVEN, SU(2), no hypothesis; SU(N ≥ 3): (KS-N) [HYPOTHESIS, s])
      (M-f) [OPEN, P; session 2: §14-§15] small-field half ⇐ (I_k^E) (node A); large-field tail: §15
      [RHW2-fix SDP-1] capped form (M-f^A) ⇐ CAP-dec + (SF-cap)^A + (SDP)^A, both node A, per level (§18.1, §19)
(REL) [session 2] ⇐ (M-i)/(M-f)-type moments over the relaxed family, Lemma REL-seq (§13); node A: Z(∅) ↔ Z^sf only
Proposition FV [⇐ (CLS-min); uncounted]: the fixed-coarse-field form of (M-i) + (M-f) is false; Lemma K3-b: in-sea collar cost not summable
```

## 9. Check w1 (criteria first: checks/w1_criteria.md 02:02:25 UTC; script checks/w1_kernel_moments.py; records checks/w1_out.txt, checks/w1_time.txt)
**Result: PASS** (A1-A4, C1-C3; B informational I-PASS). Two identical runs (deterministic, fixed seed; disclosed in HW_LOG),
02:49:47 and 02:49:55 UTC, each 2.3 s, load ≤ 2.41, ≥ 34% free, peak RSS 278 MB.
- A1: max_b bE_b[1 - cos α] = 1.49999996 (Bessel form, b up to 10⁷) and 1.49996 (quadrature, b ≤ 10⁴); the two agree to
  2.6·10⁻¹²; g(10⁷) = 1.49999996: Lemma KS (b)'s constant 3/2 holds and is approached, as proven.
- A2: max over the grid of 𝒩((1-λ)b)/𝒩(b) ÷ (1-λ)^{-3/2} = 0.999999998 ≤ 1 (Lemma KS (c)).
- A3 (negative control): the false bound with exponent 1 fails (ratio up to 10.0 at λ = 0.99), so the check discriminates.
- A4: φ_M(V) = r||V - W_0||²/2 to 2·10⁻¹⁵ (Lemma KS (a)); no random W beats W_0 = Ŵ; Monte-Carlo 𝒩(b) matches the Bessel form,
  |z| ≤ 0.50.
- B (informational, (KS-N) scalar case, SU(3)): max_b bE_b[f] = 3.9999 → 4 = dim/2 from below on b ∈ [10⁻³, 10⁴]; consistent with
  c_3 = 4 for M = rŴ. Degenerate polar parts are not checked.
- C1: n_int = 216; ≤ 6 interior plaquettes per interior link (TE (iii)). C2: 24 plaquettes per corner (HIST overlap). C3: 81
  cubes Q with y ∈ N_1(Q); max |N_1(A)|/|A| = 81 (K3-a, W-cb multiplicity).
Scope: the inequalities on grids and samples; not a proof (the proofs are §5.2, §4).

## 10. Outcomes against the pre-stated targets (§1) (ADDED AFTER the derivations; pointers only)
*[RHW1-fix, session 2] Session-1 outcomes, kept as written; REVIEW_HW_S1 recounted W2 with the residual re-identified: (AE) →
(CLS-min) (lane-G switch, §12A), (REL) → REL-seq (§13), (M-f) → OPEN [P] (§14-§15). Current status: §16-§17.*
- **W1: MET.** (H-w)³ (§3.2), with the reference named (ref-a/ref-b) and the Z_K-relative currency excluded (Proposition PF);
  HIST-sum consumes it unchanged in the weaker per-component shadow form (Lemma HS'); split into (PRICE) + (REL)
  (Theorem HW-split).
- **W2: MET as a CONDITIONAL theorem with new named hypotheses (partial success in the §1 sense).** *[superseded, §16-§17;
  [RHW2-fix H-12]: "(AE)" read (CLS-min); "(REL) is OPEN [P]" read ⇐ REL-seq; current status §18-§19]* Theorem HW: (H-w) ⇐ (AE) +
  (M-i) + (M-f) + (REL) [+ (F_R)], combination over all defects and levels by Lemma CH; HW-F1 avoided for kernel windows (KS),
  HW-F2 avoided (no greedy factor), HW-F3 diagnosed (PF), HW-F4 none. K5 resolved precisely (§5.3). (M-i) is PROVEN on the plain
  chain (SU(2)) and reduced in-history to (LI); (M-f) is ARGUED; (REL) is OPEN [P]. The hypotheses are not all strictly smaller
  than (H-w): (REL) is (H-w)'s B_0 half unchanged, and (M-f) is new in form (a local coupling response of the small-field
  package). Collar-bad cubes: conditional on (TC) and with (M-i) unreduced.
- **W3: MET.** K3-a (boundary part summable, ≤ 1 in B_0); K3-b (in-sea part not summable as bookkeeping; supports E3; residual
  I-tay^J).
- **Check w1: PASS** (§9).

## 11. Tally and hypotheses consumed
**[RHW1-fix] Counted PROVEN-HERE / CONDITIONAL items, session 1 (4; was 5):** [HW-1] Lemma TE + Lemma W-bad (CONDITIONAL ⇐
(CLS-min); level 0 and TE (i), (iii) unconditional); [HW-2] Lemma CH + Theorem HW (CONDITIONAL, implication proven; θ < 1/96);
[HW-4] Lemma KS (SU(2), unconditional) with KS-chain; [HW-5] Lemma H4-red (CONDITIONAL ⇐ (LI); SU(2)). ([HW-3] Proposition FV is
recounted as uncounted, a corollary of TE.) Session-2 items: §17.
**Uncounted (elementary/definition-level):** Lemmas HR, RX, PF, HS', HW-split, DJ, EQ, HÖ, LI-a, W-cb, K3-a, K3-b, Proposition FV;
the (M-f) reduction to the main term (given (I_k^E)).
**OPEN [P] (session 2 relabel):** (M-f). **ARGUED:** the channel description in LI-a for levels ≥ k + 3; (REL)'s bootstrap
self-consistency.
**Hypotheses consumed, by statement:**
- Theorem HW: (F_R) with g_K² ≤ 1/(2R) [FLOW, P]; (CLS-min) [⇐ (REG-min), SQ, P; or ⇐ (AE)]; (M-i)_{24θ} [this file; ⇐ (LI)
  for bad windows]; (M-f)_{96θ} [OPEN, P]; (REL)_{B_2} [⇐ REL-seq, §13]; for collar cubes also (TC), the σ_Q reading of PLD §9.1,
  and θ < 1/(96·82).
- Lemma W-bad, TE (ii), Proposition FV: (CLS-min) only (the cone-local infimum; §12A); level-k side ≥ 3.
- Lemma W-cb: Lemmas PM, KQ (HIST, CONFIRMED), RS (R1) (RLARGE, CONFIRMED), (TC).
- Lemma H4-red: (LI); Lemma TD; Lemma KS; the data-reading of LI-a. SU(N ≥ 3): (KS-N) in place of KS.
- Lemma K3-a: HIST TS_K's ℛ^∂ bound and (P2)'s collar bound (as stated there); K3-b: the upper half of (F_R).
**Not consumed:** RS-joint, (PLD-q)_k, (SG^ph/net/fl)_k, PLD-desc, (BG)_k (except through (REG-min), its cone-local sup form), RLARGE §3.4's case split, E10's extension of (SG^fl),
Balaban CMP 122 (not read), any literature result. **No edits** outside HW.md, HW_LOG.md, checks/w1_*.

---
# Session 2 of lane H (2026-10-28)

Inputs read for session 2 are listed in HW_LOG (session 2, first two entries). REVIEW_HW_S1.md is BINDING. Fixes to §0-§11
are made in place and tagged **[RHW1-fix X]** (X the review's label); nothing else in §0-§11 is changed. The pre-stated
targets below (§12) were written at **2026-10-28 03:53 UTC**, after reading the inputs and after exploratory reasoning, BEFORE
the [RHW1-fix] edits, before any session-2 derivation (§13 onward) and before any w2 criteria file. They are not edited after
the derivations start; outcomes are pointers in §17.

## 12. Session-2 pre-stated targets (2026-10-28 03:53 UTC)

### Target S1 (STEP 1): apply the binding fixes of REVIEW_HW_S1
W-1 (θ < 1/96), W-2 (C_cone of HIST RH3-fix N-4; a_bad's size; the false "REVIEW_HIST_S3 absent" remark corrected in place
and in HW_LOG as an appended correction), W-3 (collar windows: θ divided by the multiplicity ≤ 82), W-4 (C_ℓe^{aR} in
HIST-sum's constant under (F_R)), H-2 (RX (ii)-(iii) need history-independent D_j), H-6, H-8, H-11, K-1 (all g² ≤ 2g_K²;
(P3)'s vacuum term), S-1/S-2 (status lines, after S2/S3), FV recounted as uncounted, tally 4. Recommended fixes where cheap.

### Target S2 (STEP 2): Lemma REL-seq, re-derived
Prove, at the level of HW's lemmas, that under (ref-a) (REL)_B holds with B → 0 as g_K → 0: add the small-field constraints
back one relaxed (level, cube) pair at a time; bound each step's failure probability by the union bound over *-connected
defect sets of n_♯ + 1 cubes and Lemma CH under the intermediate relaxed law. State the exact moment family consumed, check
whether (M-i) on it still reduces to (LI) (LI-a fails on constrained cubes, REVIEW_HW_S1), and check the depth term of the
shadow allowance against the LF arithmetic. **Failure modes:** (S2-F1) a step whose bad event is not contained in a
"(n_♯ + 1)-defect animal through the added cube" event; (S2-F2) a per-step cost that is not small (B not → 0) or carries a
depth factor e^{c(K - j)} not beaten by the running; (S2-F3) hidden use of a fixed ordering. Then state exactly what node A
still owes (the torus-wide comparison of Z(∅) with its small-field partition function), with the quantifiers of (RLF-4).
Success: REL-seq PROVEN as an implication from named moment hypotheses; (REL) removed as an independent residual.

### Target S3 (STEP 3): (M-f), now owned here
(M-f)'s exponential moment contains the tail of returned finer-level defects, and the moment → price → moment loop loses
≥ 4× in rate per level. Find a non-inductive route or name the exact wall. Routes to try, in order: (a) remove the rate
loss at its sources (Hölder's 2, W-bad's u_{k+1} ≤ 2u_k, the energy-unbounded moment) by capped windows min{X_Q, π_Q} and by a
mismatch peel that carries the fine factors as spectators; (b) the LF-count question: with whatever per-level loss remains,
is it summable against the logarithmic running (u_{k-1} - u_k ≈ β log L)? Prove the arithmetic either way; (c) a single
global Chernoff over all levels (HIST-sum-style count), including the returned defects; say what its entropy count gives.
**Failure modes:** (S3-F1) a rate that degrades geometrically with depth; (S3-F2) constants that grow geometrically with
depth (entropy of the column, 81 cubes per level) even if the rate does not; (S3-F3) bookkeeping of the returned gas,
whose density per final cell may diverge (the K3-b mechanism); (S3-F4) circularity with (H-w) itself. Success: (M-f) PROVEN
from strictly smaller named inputs; partial success: a proven reduction to one named statement that is not degraded by
depth, with the exact wall (the inequality that fails, and by how much) stated.

### Check w2 (criteria first: checks/w2_criteria.md, then the script)
Informational. Candidates: the capped inequalities; the REL-seq step bound on an exactly enumerable toy (independent and
correlated defect laws) with a negative control; the arithmetic of the loop/entropy conditions at the recorded constants.

# Session-2 derivations (written after §12; started 03:54 UTC)

## 12A. STEP 1 record, and the lane-G question: does HW need the general-chain (AE)? (answered 03:57 UTC)
The [RHW1-fix] edits are in place in §0-§11 (W-1, W-2, W-3, W-4, H-1 … H-11, K-1, S-1, S-2, FV recounted, tally 4). The lead's
lane-G note (SQ.md §0, read-only: §0.1 Lemma INF, §0.3 MSG-dec, E2, SUP-price, FORCE, (REG-min), DESC, Corollary PRICE-iii)
asks, use by use, whether HW consumes the general-chain (AE) or only the cone-local infimum.

**Answer: every use is the infimum. No use needs the general-chain bound.** By definition (§4) ℰ_P(V) := inf of E_𝒞(P) over
the finer fields with top V; E_𝒞(P) reads the finer fields only inside 𝒞(P) and V only on ∂P, so ℰ_P(V) is SQ's free-boundary
cone minimum 𝓔^{𝒞(P)}(V). Use by use:
- **TE (ii)**: session 1 derived "s(V_P) ≤ C·ℰ_P(V)" from CLS-red's every-chain form by taking the infimum; only the infimum is
  stated and used. Now TE (ii) is (CLS-min) itself.
- **Lemma W-bad** (lower bound X_Q ≥ a_bad u_{k+1}): X_Q = u_{k+1}Σ_Pℰ_P(V), a sum of infima. Infimum only.
- **Lemma W-cb** (α)/non-quiet: ℰ_p(U) at level k for one plaquette above threshold. Infimum only. (β) uses KQ/PM, no (AE).
- **Proposition FV** ("for EVERY V and EVERY U"): the lower bound is ℰ_P(V) ≥ a_bad (infimum, for every top V); "every U" comes
  from TE (i), ℰ_P(V) ≤ κΦ_{∂P}(U, V) + ℰ^<_P(U), which is unconditional (an infimum is below its value at any U). No general-chain
  bound enters.
- §15 below uses F^col_Q(U_k) ≥ ℰ_P(U_k) (again an infimum).
So HW now consumes **(CLS-min)_{c_pr,t_pr}** (TE (ii)), primary source **(REG-min)** via SQ's DESC + SUP-price + PRICE-iii
(c_pr = c_♭/C'², t_pr = C'τ_♭; SQ session 1, PROVEN there given (REG-min), not yet reviewed), alternative source (AE) via
CLS-red [N-4] (c = 1/(2NC_cone)). Theorem HW's hypothesis list is updated (§5.1, §11). Scope notes: (a) PRICE-iii is for cone
tops at level ≥ 1; level 0 stays on (B). (b) SQ remarks that multi-level defect sets need disjoint footprints (S3-5 (c3)); for
HW's bad windows DJ supplies this, and Lemma CH needs none. (c) **Size of a_bad (fix W-2's record):** via (AE),
a_bad = ε_1²/(2NC_cone) = (1.1-2.3)·10⁻¹⁶ε_1² at N = 2 ((0.4-0.7)·10⁻¹⁶ε_1² at N = 3); via (REG-min), when ε_1 ≥ C'τ_♭,
a_bad = c_♭τ_♭² ≤ (1/640)(θ_0/C')² ≈ 5·10⁻²³/C_D⁴ [arithmetic from SQ's stated θ_0 ≈ 10⁻⁸/C_D²; SQ claims no improvement in the
constant]. a_bad stays g-independent and depth-uniform either way; its smallness matters in §15.

## 13. Target S2: Lemma REL-seq (re-derived; adopted)

Throughout: (ref-a) Z^sf := Z(∅); history-independent D_j (§0); for §13.2 the defect notion is bad-only, D_j = {ζ = 1}
(as in Theorem HW; ζ_Q reads only the interior plaquettes of Q at its own level).

### 13.1 The relaxed family and two elementary facts
For level-wise cube sets S = (S^{(j)})_j ("constrained") and E = (E^{(j)})_j ("declared defects") put
  **R_{S,E} := ∩_j{every *-component of (D_j ∪ E^{(j)}) ∩ S^{(j)} has ≤ n_♯ cubes},  R_S := R_{S,∅},  ℛ := {R_{S,E} : Z(R_{S,E}) > 0}.**
- (m1) *Monotonicity.* S ⊂ S' ⇒ R_{S',E} ⊂ R_{S,E}; E ⊂ E' ⇒ R_{S,E'} ⊂ R_{S,E}. (A *-component of A ∩ S lies in a *-component of
  A' ∩ S' whenever A ⊂ A', S ⊂ S'.)
- (m2) R(𝔥) = R_{S(𝔥)}, S^{(j)}(𝔥) := Λ^pre_j(𝔥) ∖ N_1(𝒰_j), and R(∅) = R_{all} (Lemma RX (iii)). Z(∅) > 0 (the defect conditions
  are closed, their complement contains a neighbourhood of U ≡ 1, and W is continuous and positive), so every R_S ∈ ℛ.

**Lemma DECL (declaring defects): PROVEN-HERE (elementary, not counted).** For R_{S,E} ∈ ℛ, a level j and a set 𝒟 of level-j
cubes, with E' := E ∪ 𝒟 (at level j):
  μ_{R_{S,E}}(𝒟 ⊂ D_j) ≤ μ_{R_{S,E'}}(𝒟 ⊂ D_j)   (the right side := 0 if Z(R_{S,E'}) = 0),
and for the bad-only defect notion, 1_{R_{S,E'}} reads no link of int Q, Q ∈ 𝒟.
*Proof.* On {𝒟 ⊂ D_j}, D_j ∪ E^{(j)} = D_j ∪ E'^{(j)}, so 1_{R_{S,E}}1{𝒟 ⊂ D_j} = 1_{R_{S,E'}}1{𝒟 ⊂ D_j}; integrate against W and use
Z(R_{S,E'}) ≤ Z(R_{S,E}) (m1). Second claim: with 𝒟 declared, the level-j factor reads ζ_{Q'} only for Q' ∉ 𝒟, i.e. interior
plaquettes of other cubes (whose links are disjoint from int Q, the cubes being disjoint site blocks); the factors of other
levels read other fields (bad-only). ∎
*Consequence.* REVIEW_HW_S1 noted that on cubes the intermediate law constrains, LI-a fails. After DECL the cubes being priced
are declared, LI-a holds for every law of ℛ (bad-only), and the mismatch moment reduces to (LI) over ℛ by H4-red (or H4-red',
§14). The remaining in-history content is (LI)'s future insensitivity over ℛ, not a new mismatch hypothesis.

### 13.2 Lemma REL-seq
**Hypothesis (PRICE^ℛ)_{a,C_ℓ,c} [named; consumed].** For every R ∈ ℛ, every level j and every set 𝒟 of level-j cubes declared in
R (i.e. R = R_{S,E} with 𝒟 ⊂ E^{(j)}):  μ_R(𝒟 ⊂ D_j) ≤ (C_ℓe^{-au_j})^{|𝒟|}·exp(c·Σ_{m=j}^{K-1}|sh_m(𝒟)|).
(Sources: Theorem HW's proof applied to the single-level defect set 𝒟 under μ_R with the moments over ℛ (Hölder form, θ < 1/96,
a = θa_bad), or Theorem HW^cap (§14) with (LI^F)^ℛ and (M-f^cap)^ℛ (a = θa_bad, no Hölder). The shadow allowance c is the (LI)
allowance c_LI plus the moments' own.)
**[RHW2-fix RS-1] Family restricted.** ℛ contains S = ∅ (the plain chain W/Z_K), for which (PRICE^ℛ) would be a plain-chain
multi-cube Peierls bound, i.e. the large-field problem itself. The proof below consumes (PRICE^ℛ) only on the laws that occur:
  **ℛ_𝔥^↑ := {R_{S,E} : S ⊇ S(𝔥), S reached from S(𝔥) by level-first ascending relaxation, E ∋ the step animal 𝒟}.**
(PRICE^ℛ) is hereby assumed ONLY on ℛ_𝔥^↑ (for each 𝔥). Under level-first ascending order, when level j is relaxed every finer
level i < j is already fully constrained (S^{(i)} = all, the constraint of R(∅)), so the fine columns priced carry only
small components. Wherever "ℛ" is written below as the law family of (PRICE^ℛ), (M-f)^ℛ, (LI)^ℛ, (LI^F)^ℛ, read ℛ_𝔥^↑.

**Lemma REL-seq: CONDITIONAL [HW-6] (implication PROVEN-HERE; counted; unreviewed).** Assume (F_R) (lower half suffices here,
with its R), (PRICE^ℛ)_{a,C_ℓ,c}, and n_♯ ≥ n_H computed with B_0 ≥ c (so (n_♯ + 1)aβ_-log L ≥ 38416c). Put
  **ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c}**
and suppose ε_♯ ≤ ½. Then for every admissible 𝔥, under (ref-a),
  **Z(R(𝔥)) ≤ Z(∅)·exp(164ε_♯·Σ_{(j,𝒟)}Σ_{k=j}^{K-1}|sh_k(𝒟)|),**
i.e. (REL)_B with **B = 164ε_♯ → 0 as g_K → 0** (n_♯ fixed).
*Proof.* (1) *Telescoping.* List the relaxed pairs P(𝔥) := {(j, x) : x ∉ S^{(j)}(𝔥)} in level-first ascending order
[RHW2-fix RS-1; session 2 wrote "ANY order"] (j_1, x_1), …, (j_N, x_N), and put
S_0 := S(𝔥), S_i := S_{i-1} ∪ {x_i at level j_i}; S_N = all. By (m1)-(m2), R_{S_N} = R(∅) ⊂ … ⊂ R_{S_0} = R(𝔥), all in ℛ, and
  Z(∅)/Z(R(𝔥)) = Π_{i<N}Z(R_{S_{i+1}})/Z(R_{S_i}) = Π_{i<N}μ_{R_{S_i}}(R_{S_{i+1}}).
(2) *The bad event of a step (S2-F1).* Let c ∈ R_{S_i} ∖ R_{S_{i+1}}, (j, x) := (j_{i+1}, x_{i+1}). Only the level-j constraint changed, so
some *-component C of D_j ∩ S^{(j)}_{i+1} has > n_♯ cubes. If x ∉ D_j then D_j ∩ S^{(j)}_{i+1} = D_j ∩ S^{(j)}_i and c ∉ R_{S_i}; so
x ∈ D_j, and if x ∉ C then C ⊂ S^{(j)}_i is a component of D_j ∩ S^{(j)}_i, again contradicting c ∈ R_{S_i}. So x ∈ C. A connected
graph with ≥ m vertices has, through any vertex, a connected induced subgraph of exactly m vertices (grow a breadth-first tree
from x and stop at m). Hence C ⊃ 𝒟 ∋ x, 𝒟 *-connected, |𝒟| = n_♯ + 1, 𝒟 ⊂ D_j:
  R_{S_i} ∖ R_{S_{i+1}} ⊂ ∪_{𝒟 ∋ x, |𝒟| = n_♯+1, *-conn}{𝒟 ⊂ D_j}.
(3) *Step price.* The number of such 𝒟 is ≤ 6400^{n_♯} ((g3)). For each, DECL then (PRICE^ℛ) (𝒟 declared in R_{S_i,𝒟} ∈ ℛ, or
the term is 0):
  μ_{R_{S_i}}(𝒟 ⊂ D_j) ≤ (C_ℓe^{-au_j})^{n_♯+1}exp(c·Σ_{m≥j}|sh_m(𝒟)|) ≤ (C_ℓe^{-au_j})^{n_♯+1}e^{c(38417(n_♯+1) + 38416(K-1-j))}
(Lemma H-geo (iv)). With u_j ≥ u_K + β_-(K - j)log L - R ((F_R) lower half):
  p_i := μ_{R_{S_i}}(R_{S_i} ∖ R_{S_{i+1}}) ≤ 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-au_K})^{n_♯+1}·e^{38416c}·L^{-(K-j)[(n_♯+1)aβ_- - 38416c/log L]}
  ≤ ε_♯   (the bracket is ≥ 0 by the threshold condition; K - j ≥ 1).
**The depth term e^{38416c(K-1-j)} of the shadow allowance is beaten by the running exactly by HIST-sum's arithmetic (S2-F2).**
(4) *Product.* -log(1 - p) ≤ p/(1 - p) ≤ 2p on [0, ½], so Z(∅)/Z(R(𝔥)) ≥ exp(-2ε_♯N). (5) *Count.* N = Σ_j|Σ(Ω^c_{j-1}) ∪
N_1(𝒰_j)| ≤ Σ_j(|Ω^c_j| + 81|𝒰_j|) ≤ 82Σ_j|Ω^c_j| (H-nest (i): Σ(Ω^c_{j-1}) ⊂ Ω^c_j; 𝒰_j ⊂ Ω^c_j), and Σ_j|Ω^c_j| ≤ the shadow sums
(HIST-sum step (2)). ∎
*Order of constants (non-circular).* a, C_ℓ, c (from the moments and (LI)) → B_0 := B_1 + c + 1 (B = 164ε_♯ ≤ 1 once g_K is small)
→ n_H → n_♯ ≥ n_H → g_0(n_♯) with ε_♯ ≤ min{½, 1/164}. ~~*S2-F3:* the order of relaxation is arbitrary (REVIEW_HW_S1's
level-first order is not needed; it only changes which laws of ℛ occur, and (PRICE^ℛ) is assumed on all of ℛ).~~
**[RHW2-fix RS-1]** The order is level-first ascending and (PRICE^ℛ) is assumed on ℛ_𝔥^↑ only. Other orders are valid only
as implications from the strictly stronger hypothesis (PRICE^ℛ) on a larger family; that is not a feature of the lemma.
[Recommended fixes, REVIEW_HW_S2:] in (3) and in ε_♯ the factor e^{38416c} is an over-estimate (the identity has e^{-38416c},
i.e. the displayed lines hold with "≤" by a margin e^{76832c}). At the recorded a ≈ 10⁻¹⁷, n_H ≈ 10²² (w2 C1 prints
9.45·10²¹), so g_0(n_♯) is astronomically small; legitimate, since every constant in the chain is g-independent.

**Corollary (Theorem HW with (REL) discharged): CONDITIONAL.** Under (ref-a), Theorem HW (or HW^cap, §14) with Lemma REL-seq gives
(H-w') with B_0 = B_1 + 164ε_♯ ≤ B_1 + 1, from (F_R), (CLS-min), and the moment hypotheses over ℛ ((M-i)^ℛ ⇐ (LI)^ℛ via DECL +
H4-red; (M-f)^ℛ, or (LI^F)^ℛ + (M-f^cap)^ℛ). **(REL) is no longer an independent residual** [RHW1-fix S-1 adopted after
re-derivation].

### 13.3 What node A still owes
HIST-sum (with REL-seq) gives, for g_K ≤ g_0(n_♯), uniformly in K and T:
  Z(∅) ≤ Z_K ≤ Z(∅)·exp(C_H|T|e^{-(n_♯+1)a/g_K²}),  so |log Z_K - log Z(∅)| ≤ C_H|T|e^{-(n_♯+1)a/g_K²}.
RLARGE's (RLF-4) asks |log Z_K^{ren} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} (any a' < a_♯), Z_K^{sf} the soft-RG small-field partition
function with shifted couplings. **What node A owes is therefore exactly one torus-wide two-sided statement:**
  ~~**(NA-∅)** |log Z(∅) - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} uniformly in K~~ **[RHW2-fix NA-1; the session-2 form omitted the
  vacuum constant and is false in kind by Remark GAS below]:**
  **(NA-∅)** |log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} uniformly in K, equivalently a two-sided comparison of Z(∅)
  with Z_K^{ref} = exp(𝒱_K^{LF})·Z_K^{sf,ref} (RLARGE (RLF-1), (RLF-4)), 𝒱_K^{LF} := Σ_{k<K: T_{k+1}≥W}N_{k+1}c̄_0^{sea}(g_k),
  with Z(∅) = ∫W·1{every *-component of every D_j has ≤ n_♯ cubes},
with the same normalisation conventions for Z^{ren} as RLARGE §1A. No per-history B_0 item is left: HIST §7.4's (a)-(d) are
artifacts of the R-operation representation and do not occur in ∫W·1_𝔥. [For a bound in the ratio form only the upper half
Z(∅) ≤ Z^ref·e^{C|T|e^{-a'/g²}} feeds (RLF-3); the lower half is (RLF-4)'s. [RHW2-fix NA-1: Z^ref = e^{𝒱_K^{LF}}Z^{sf,ref}, session 2
wrote Z^sf.]]
**Remark GAS (the returned gas in Z(∅) must be extracted, not bookkept): PROVEN-HERE (arithmetic, not counted; the K3-b
mechanism).** Z(∅) contains every configuration of returned components at every level. If their contribution relative to a
no-defect reference were carried as bookkeeping, at most p_j := C_2e^{-a_ru_j} per level-j cube (a_r > 0), the per-final-cell
bound Σ_{j<K}L^{4(K-1-j)}p_j ≥ C_2e^{-a_r(u_K+R)}L^{-a_rβ_+}Σ_{m=0}^{K-1}L^{(4-a_rβ_+)m} diverges as K → ∞ whenever a_rβ_+ ≤ 4 (proof
as K3-b). With a_r of the size of a_bad this is the case. So (NA-∅) cannot be proven by comparing Z(∅) with the defect-free
partition function per cube; the returned gas is part of node A's object (RLARGE's Z^ref := exp(𝒱_K^{LF})Z^{sf,ref}, the R1
extraction). This is a statement about the bound, not a lower bound on the true gas free energy. **[RHW2-fix NA-1]** Read
together with (NA-∅): GAS is the reason the vacuum constant 𝒱_K^{LF} must appear in (NA-∅); 𝒱_K^{LF}/|T| is not O(e^{-a'/g_K²}).

## 14. Target S3 (a): removing the rate loss at its sources: capped windows and the spectator peel

The 96 = 2·48 of Theorem HW has three sources: Hölder's 2; W-bad's u_{k+1} ≤ 2u_k (a further 2); and the moment being of an
energy that is unbounded relative to the price. All three are removable for bad cubes (SU(2), given (LI) in a weighted form).

**Lemma CAP (capped windows): PROVEN-HERE (elementary, not counted).** (i) For a, b ≥ 0, π > 0: min{π, a + b} ≤ a + min{π, b}.
(ii) Lemma CH holds verbatim with X_Q replaced by X^cap_Q := min{X_Q, π_Q}. (iii) For a bad level-(k+1) cube Q (k ≥ 0) and every
level-k field U, with TE (i), (iii) used without the step u_{k+1} ≤ 2u_k:
  X^cap_Q ≤ Y^mis_Q + min{π_Q, Y^f_Q},  Y^mis_Q := 6κu_{k+1}Φ_{int Q}(U, V),  Y^f_Q := 24u_{k+1}F^col_Q(U).
*Proof.* (i) If b ≥ π the right side is a + π ≥ π; otherwise it is a + b. (ii) On {Q ∈ D_j}, X_Q ≥ π_Q, so X^cap_Q = π_Q and
1 ≤ e^{θ(X^cap - π)}; off it the right side is > 0. (iii) X_Q = u_{k+1}Σ_Pℰ_P ≤ u_{k+1}[2(d - 1)κΦ_{int Q} + 24F^col_Q] (TE), then (i). ∎

**Hypothesis (LI^F) (future insensitivity with spectator weights) [OPEN; owner: this file; a strengthening of (LI)].**
*[RHW4-fix status pointer, session 5: under μ_{R(𝔥)} (LI) and (LI^F) are PROVEN with c = 0 for any bounded spectators, Cor. LI-0
(a), §22; §19 interface item A4 likewise.]* (LI)
holds with the same c_k when the future h_{k+1} is weighted by any product F^> = Π F_Q over Q ∈ 𝒰_{m+1}, m ≥ k + 1, of bounded
functions F_Q ≥ 0 of U_m restricted to the links with both endpoints in Q's level-m descendants (Q's column at level m):
h^F_{k+1}(V) := ∫Π_{i>k}K_iΠ_{j≥k+2}1_{R,j}F^>dU_{k+2}⋯dU_K. (F ≡ 1 is (LI).) Same channel as (LI) (LI-a); the weights are
local functions in the columns of history cubes, which by DJ are disjoint from every int(𝒰) link set.
**[RHW2-fix LI-1] Restricted statement (the one consumed).** "Any bounded F_Q ≥ 0" is withdrawn: a sup-ratio for all
weights is a pointwise Radon-Nikodym bound on the conditional law of the far-future data, strictly stronger than (LI) and
than needed. (LI^F) is stated ONLY for the capped weights F_Q = e^{θmin{π_Q, Y^f_Q}} ∈ [1, e^{θπ_Q}] (π_Q = a_bad u_{m+1},
Y^f_Q = 24u_{m+1}F^col_Q(U_m)), or the monotone family they generate, over the laws of ℛ_𝔥^↑ (RS-1) as well as R(𝔥). The
plausibility argument (same channel as LI-a; columns disjoint by DJ) is [inference]. Lemma H4-red' below is applied only with
these F_Q (Theorem HW^cap), so its proof is unchanged.

**Lemma H4-red' (mismatch peel with spectators): PROVEN-HERE [HW-7] (counted; unreviewed).** G = SU(2), bad-only defects, the
data-reading of LI-a, (LI^F). For λ_k ∈ [0, 1) and every family F_Q (Q ∈ 𝒰_{k+1}, k ≥ 0) as in (LI^F) (F_Q a bounded nonnegative
function of U_k on Q's column; for Q ∈ 𝒰_0 a function of U_0 on int Q):
  E_{μ_{R(𝔥)}}[Π_kΠ_{c∈int 𝒰_{k+1}}e^{λ_kκu_kφ_c}·Π_QF_Q] ≤ Π_ke^{c_k}(1 - λ_k)^{-3n_int|𝒰_{k+1}|/2}·E_{μ_{R(𝔥)}}[Π_QF_Q].
*Proof.* As H4-red, peeling the top level k_1 first. Every spectator reads a level ≤ k_1, because the spectator of Q ∈ 𝒰_{m+1}
reads U_m and 𝒰_{m+1} = ∅ for m > k_1; so at the first peel all spectators lie outside I and the step is H4-red's. At the peel
of level k < k_1 (V = U_{k+1}): the spectators of Q ∈ 𝒰_{k+2} read V on Q's level-(k+1) descendants, which are not in 𝒰_{k+1}
(DJ / H-nest (ii)), so their links are disjoint from V_𝒦 = int(𝒰_{k+1}); they are functions of V_rest. The spectators of
higher levels sit in the weighted future h^F_{k+1}(V). (LI^F): h^F_{k+1}(V) ≤ e^{c_k}h̲^F(V_rest); LI-a: 1_{R,k+1} is free of V_𝒦;
Lemma KS (c) on the independent links V_𝒦; then h̲^F ≤ h^F and ∫Π_𝒦k_c = 1. The level-0 spectators read U_0, never a V_𝒦. ∎

**Hypothesis (M-f^cap)_θ (capped fine moment) [OPEN, P; §15].** For every admissible 𝔥 (and, for REL-seq, every R ∈ ℛ):
E_{μ_R}[Π_{k≥0}Π_{Q∈𝒰_{k+1}}e^{θmin{π_Q, Y^f_Q}}·Π_{Q∈𝒰_0}e^{θX_Q}] ≤ C_fc^{#Q}·exp(c_f·shadow sums), C_fc independent of g, K, T, 𝔥.
(Level-0 cubes have no finer level; their factor is the level-0 Wilson moment of HW §6, uncapped or capped.)
It is weaker than (M-f)_{24θ(1+2Rg_K²)} (e^{θmin{π,Y}} ≤ e^{θY} and u_{k+1} ≤ (1 + Rg_k²)u_k), and every factor is ≤ e^{θπ_Q}.

**Theorem HW^cap ((PRICE) with no rate loss): CONDITIONAL [HW-7] (implication PROVEN-HERE; counted with H4-red';
unreviewed).** Assume (F_R) with g_K² ≤ 1/(2R), (CLS-min), SU(2), bad-only defects, (LI^F) and (M-f^cap)_θ, with
  **λ_* := 6θ(1 + 2Rg_K²) < 1.**
  **[RHW2-fix CAP-1]** λ_* < 1 is the mismatch condition only. The fine factor carries TE (iii)'s overlap 24 inside
  Y^f = 24u_{k+1}F^col_Q, so (M-f^cap) is a rate-24θ(1 + 2Rg_K²) moment on defect-free columns, g-uniform (by §6's
  (1 - λ)^{-dof/2} heuristic) only for 24θ(1 + 2Rg_K²) < 1. **The condition in force is max{6θ, 24θ}(1 + 2Rg_K²) < 1**
  (i.e. 24θ(1 + 2Rg_K²) < 1), assumed together with (M-f^cap)_θ.
Then for every admissible 𝔥:
  Z(𝔥) ≤ Z(R(𝔥))·exp((c_LI + c_f)·shadow sums)·Π_jΠ_{Q∈𝒰_j}[e^{-θa_bad u_j}(1 - λ_*)^{-3n_int/2}C_fc].
*Proof.* Lemma CAP (ii) with π_Q := a_bad u_j; CAP (iii) pointwise; e^{θY^mis_Q} = Π_{c∈int Q}e^{λ_cκu_kφ_c} with λ_c := 6θu_{k+1}/u_k
≤ 6θ(1 + Rg_k²) ≤ λ_* ((F_R): u_{k+1} ≤ u_k + R; g_k² ≤ 2g_K²); Lemma H4-red' with F_Q := e^{θmin{π_Q, Y^f_Q}} (a function of U_k on
Q's column: F^col_Q(U_k) reads only the level-k links with both endpoints in Q's descendants); then (M-f^cap). ∎
*Reading.* Against Theorem HW: no Hölder (the mismatch is peeled exactly, the fine part rides as a spectator); no
u_{k+1} ≤ 2u_k; and the fine moment is capped at the price, so the fine column only has to be controlled at ONE energy level,
π_Q. ~~θ ranges up to ≈ 1/6.~~ [RHW2-fix CAP-1: withdrawn; the range is max{6θ, 24θ}(1 + 2Rg_K²) < 1. What is removed
against Theorem HW is Hölder's 2 and W-bad's 2 (96 → 24) and the depth degradation; a = θa_bad is a factor 4 below the
withdrawn claim.] With Lemma REL-seq this gives (H-w') with a = θa_bad and C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc. The price:
(LI^F) instead of (LI). The collar extension (W-cb windows) is not covered: collar links are read by R (as in §5.1).

## 15. Target S3 (b)-(c): (M-f^cap), the loop, and the exact wall

Fix k ≥ 1 and A ⊂ 𝒰_{k+1}. For Q ∈ A let G_Q := {no level-k cube of Q's descendants is in D_k} (Q has 81 level-k descendants).

**Observation SAT (one finer defect saturates the cap): PROVEN-HERE (elementary, not counted) ⇐ (CLS-min).** If some level-k
descendant x of Q is bad, then Y^f_Q ≥ 24π_Q > π_Q. *Proof.* x has an interior plaquette P with ||1 - U_k(P)|| ≥ ε_1; 𝒞(P)'s
terms are column terms of Q, all ≥ 0, so F^col_Q(U_k) ≥ ℰ_P(U_k) ≥ a_bad (TE (ii)), and Y^f_Q = 24u_{k+1}F^col_Q ≥ 24a_bad u_{k+1}. ∎
(This sharpens REVIEW_HW_S1's "F^col_Q ≳ a_bad/24": a single cone suffices, no overlap division.)
**[RHW2-fix SAT-1]** SAT is a statement about the upper split X_Q ≤ Y^mis + Y^f evaluated at the actual finer field, NOT about
the coarse event: X_Q is a function of V = U_{k+1} alone, and a returned finer defect changes the coarse holonomy only through
dilution (~ε_1/L² per level; INH, CF, SQ's class (D1)). It does not make the coarse plaquette bad.

**Lemma CAP-dec ((M-f^cap) in one step from two level-k statements, no Hölder): PROVEN-HERE (elementary; [RHW2-fix] RECOUNTED
as uncounted, session 2 wrote [HW-8] counted; CONFIRMED by REVIEW_HW_S2).**
Pointwise, Π_{Q∈A}e^{θmin{π_Q,Y^f_Q}} ≤ Σ_{A'⊂A}Π_{Q∈A∖A'}(e^{θY^f_Q}1_{G_Q})·Π_{Q∈A'}(e^{θπ_Q}1_{G^c_Q}). Hence, for a law μ in the
family, (M-f^cap)_θ on A holds with **C_fc = c_sf + 81C_sde^{θa_bad R}** given
- **(SF-cap)_θ [small-field half; owner node A]:** for all A' ⊂ A, E_μ[Π_{A∖A'}e^{θY^f_Q}1_{G_Q} · Π_{A'}1_{G^c_Q}] ≤
  c_sf^{|A∖A'|}·μ(∩_{Q∈A'}G^c_Q) (the fine moment on defect-free columns, uniformly under conditioning on finer defects in other
  columns);
- **(SDP)_θ [single-defect Peierls; large-field-tail half; ~~owner this file~~ [RHW2-fix SDP-1] owner node A, as (SDP)^A, §18.1]:**
  for every set S of level-k cubes,
  μ(S ⊂ D_k) ≤ (C_sde^{-θa_bad u_k})^{|S|}.
*Proof.* On G_Q, min ≤ Y; on G^c_Q, min ≤ π; expand the product of the two-term sums. Take E_μ; (SF-cap) bounds each term by
c_sf^{|A∖A'|}e^{θπ(A')}μ(∩_{A'}G^c_Q). The event ∩_{A'}G^c_Q is contained in the union over choice functions Q ↦ x_Q (a bad
descendant of Q; 81^{|A'|} choices; the x_Q are distinct because columns of distinct Q are disjoint) of {x_Q ∈ D_k ∀Q ∈ A'}, so by
(SDP) μ(∩_{A'}G^c_Q) ≤ (81C_sde^{-θa_bad u_k})^{|A'|}. With e^{θπ_Q} = e^{θa_bad u_{k+1}} and u_{k+1} - u_k ≤ R: Σ_{A'}c_sf^{|A∖A'|}
(81C_sde^{θa_badR})^{|A'|} = (c_sf + 81C_sde^{θa_bad R})^{|A|}. ∎ [Recommended note, REVIEW_HW_S2: e^{θπ_Q}e^{-θa_bad u_k} =
e^{-θa_bad(u_k - u_{k+1})} ≤ L^{-θa_badβ_-}e^{θa_bad R}, a gain not used here.]
**The rate does not degrade:** (SDP) is needed at the SAME rate θ, at the finer level's own coupling (the running even helps:
u_{k+1} ≤ u_k + R). This answers HW-F5 at the level of rates.

### 15.1 Why the moment ⇒ price ⇒ moment loop cannot be closed level by level
**Lemma LOOP-div (uncapped loop; rate): PROVEN-HERE (arithmetic, not counted).** Consider any scheme in which (a) the price of a
level-(k+1) defect at rate θ_{k+1} (price e^{-θ_{k+1}a_bad u_{k+1}}) is obtained from an uncapped fine moment (M-f)_{λ_k} at level k
with λ_k ≥ ρ_0θ_{k+1}u_{k+1}/u_k (ρ_0 = 96 for Theorem HW; 24 with the sharp constants and no Hölder), and (b) (M-f)_{λ_k} is
obtained from the level-k defect price, which needs θ_k ≥ λ_k (by SAT, a returned level-k defect contributes ≥ e^{λ_ku_k a_bad};
on such a defect F^col can be as large as F_max = 2n_intκ, so an energy-graded tail would in fact need θ_ka_bad ≥ λ_kF_max), with
θ_k < 1/ρ_0 at every level. Then θ_{K-m} ≥ ρ_0^mθ_K·u_K/u_{K-m} ≥ ρ_0^mθ_K·u_K/(u_K + β_+m log L + R), which exceeds 1/ρ_0 for all
m ≥ m_*(ρ_0, θ_K, β_+g_K², Rg_K²) < ∞. So for K > m_* the scheme fails, for every ρ_0 > 1.
*Proof.* Chain (a)-(b): θ_k ≥ ρ_0θ_{k+1}u_{k+1}/u_k; multiply over k = K - m, …, K - 1 (the u-ratios telescope to u_K/u_{K-m}); upper
half of (F_R). The right side grows like ρ_0^m/m. ∎
**Answer to the LF-count question for the rate.** The running enters the loop only through u_{k+1}/u_k = 1 - O(g_k²log L), whose
product over m levels telescopes to u_K/u_{K-m}, polynomial in m. It cannot absorb any fixed per-level factor ρ_0 > 1: the
logarithmic running is additive in u, the loss is multiplicative in the rate. (The reviewer's ≥ 4 is confirmed as a lower
bound; with SAT the true loss of the uncapped route is ≥ ρ_0, and ≥ ρ_0F_max/a_bad for the energy-graded tail.) Capping
(§14, CAP-dec) removes the rate loss entirely (ρ_0 → 1).

**Lemma LOOP-const (capped loop; constants): PROVEN-HERE (arithmetic about the bound, not counted).** Suppose (SDP) at level k is
derived by the capped route at level k (Theorem HW^cap's single-level form for 𝒟 = S under the relaxed laws, with (SF-cap) and
(LI^F)) from (SDP) at level k - 1. The constant this produces is
  C_sd(k) = K_m·(c_sf + 81C_sd(k-1)e^{θa_bad(u_k - u_{k-1})}),  K_m := (1 - λ_*)^{-3n_int/2}e^{c_LI'} ≥ 1,
so, by the upper half of (F_R) (u_{k-1} - u_k ≤ β_+log L + R),
  C_sd(k) ≥ G·C_sd(k-1),  **G := 81·L^{-θa_badβ_+}e^{-θa_bad R},**  hence C_sd(k) ≥ G^kC_sd(0) → ∞ geometrically in depth unless
  **θa_bad(β_+log L + R) ≥ log 81 = 4log L.**
*Proof.* Lemma CAP-dec at level k - 1 feeding Theorem HW^cap at level k; drop c_sf ≥ 0 and K_m ≥ 1. ∎
*[RHW2-fix SDP-1/CAP-1] Reading corrected in §18.1: LOOP-const is LF-count (K3-b, GAS) at n = 1 and shows (SDP) is NOT
derivable by column induction; it is not a new wall. Also K_m ≫ 1, so even G < 1 would need K_mG < 1. With CAP-1 (θ < 1/24)
the shortfall below grows by a further factor 4.* *Size.* θ < 1/6 and a_bad ≤ 2.3·10⁻¹⁶ε_1² (via (AE)) or ≈ 5·10⁻²³/C_D⁴ (via (REG-min)) give θa_bad(β_+log L + R) ≤ 10⁻¹⁶ for
β_+, R = O(1): G = 81(1 - O(10⁻¹⁶)), and the inductive (SDP) constant grows like 81^k (check w2 C2). **The rate loop is controlled; the
constant loop is not [wording, session 3].** The obstruction is the column entropy (81 descendants per level), which the running beats only at
per-cube exponent θa_badβ_+ ≥ 4: the one-cube analogue of HIST-sum's n·aβ_- > 4 + c_B. HIST-sum beats the same L⁴ per level
because a component of n > n_H cubes multiplies the running gain by n; a saturation chain (Q bad because of x below, x bad because
of y below, …) has one cube per level.
*Mechanism [inference, consistent with SAT].* Unrolled, the capped scheme proves P(coarse defect) ≲ Σ_r81^re^{-θa_bad u_{k-r}},
i.e. "≤ the expected number of finer defects anywhere in the column"; by Remark GAS that number is not small in the continuum
limit (it grows like Σ_rL^{(4-aβ)r}). Any bound in which a coarse window's fine part is read through the actual finer field is
saturated by a single finer returned defect (SAT), so it can only charge the coarse defect to "some finer defect below".

### 15.2 The global-count route (Target S3 (c))
A single Chernoff over all levels at once, with the returned defects inside the product and HIST-sum's count:
- the returned defects far from 𝔥 must be summed; as bookkeeping their per-final-cell sum diverges (Remark GAS, the K3-b
  arithmetic, for any per-cube exponent a_r with a_rβ_+ ≤ 4). So they cannot enter a global Chernoff as bookkeeping; they
  belong to the reference (R1 extraction, node A).
- the returned defects inside 𝔥's columns change 𝔥's prices only through saturation (SAT). Summed globally, every saturation
  chain from a history cube down r levels carries entropy 81^r and pays only at its bottom, e^{-θa_bad u_{k-r}}: per history cube
  Σ_r(81L^{-θa_badβ_-}e^{θa_bad R})^r, the same divergent factor as LOOP-const, now with no n-enhancement (each chain has one cube
  per level, the 81 descendants of distinct cubes being distinct).
- DJ makes the windows of history cubes disjoint across levels (§4, fix H-5). It does not apply to returned defects inside a
  history cube's column: those windows are nested in the history window. Disjointness across nested scales is exactly what is
  missing; dividing the shared terms by the nesting depth (S3-5's (24k)⁻¹) turns the price into e^{-θa_bad u_j/(K-j)}, whose
  exponent tends to θa_badβ log L, constant in depth, and the level sum Σ_mL^{4m}·(that) diverges.
So the global count does not by itself avoid the wall; it relocates it to the same arithmetic.

### 15.3 The exact wall
**[RHW2-fix SDP-1] The heading below is superseded: (SDP) is not HW's wall. It is re-owned as (SDP)^A, a per-level output of
node A's R-operated representation (§18.1, §19). Text kept as written; in "Sufficiency" read θ under CAP-1.**
**Wall (SDP)_θ [OPEN, P; owner: this file].** For every law of the relaxed family (R(𝔥), ℛ), every level k ≥ 0 and every set S of
level-k cubes: μ(S ⊂ D_k) ≤ (C_sde^{-θa_bad u_k})^{|S|}, with C_sd independent of g, K, T, k and the law.
- *Sufficiency (PROVEN):* (SDP)_θ + (SF-cap)_θ [node A] + (LI^F) + (CLS-min) ⇒ (M-f^cap)_θ at every level in ONE step (CAP-dec)
  ⇒ (PRICE) by Theorem HW^cap ⇒ (with REL-seq) (H-w') with a = θa_bad, θ < 1/(6(1 + 2Rg_K²)), no rate loss.
- *What fails (PROVEN as arithmetic about the bounds):* (SDP) by level-by-level induction through the capped route (LOOP-const:
  constant ×81(1 - O(θa_badβ_+)) per level), or through an uncapped loop (LOOP-div: rate ×ρ_0 per level). Short of the needed
  inequality θa_bad(β_+log L + R) ≥ 4log L by a factor ≈ 10¹⁶ (via (AE)) or ≈ 10²³ (via (REG-min)).
- *What a proof of (SDP) has to contain:* a bound on single defects at level k that does not charge a finer returned defect
  anywhere below it: either (i) a non-saturating window split (a coarse window whose fine part is not read through the actual
  finer field, so that SAT does not apply: a dilution statement, "a returned finer defect raises the coarse window's fine part
  by less than π_Q"), or (ii) a direct large-deviation bound on the level-k marginal at the ONE threshold ε_1 with a universal
  constant (REVIEW_HW_S1's target 3, but needed only at one threshold and at rate θa_bad, far below the action scale ε_1²/(2N)
  of a single defect) [inference: so (SDP) is expected to hold with a large margin; the difficulty is depth-uniformity of the
  constant, not the rate]. (SDP) is the small-component counterpart of (H-w) itself; it is not strictly smaller in kind
  (S3-F4: it does not consume (H-w) or HIST-sum, so there is no circularity, but it is not a reduction to a small-field object).
- *A sharpened corollary of LOOP-const (one-cube LF arithmetic):* the walls move if the per-cube exponent of single defects is
  raised to a_sd with a_sdβ_+ > 4 (e.g. defects at curvature O(1) on a whole cube, whose action is O(n_int)/g²). For ε_1-threshold
  defects with prices from tower-energy windows, a_sd = θa_bad, which is far too small. [inference] A two-threshold defect notion
  (single-cube returned defects charged at a large threshold, history defects at ε_1) is the natural next attempt; it is not
  written here.

## 16. Check w2 (criteria first: checks/w2_criteria.md 04:00 UTC; script checks/w2_relseq_toy.py 04:02-04:04 UTC; records w2_out.txt, w2_time.txt)
**Result: OVERALL PASS as pre-registered** (one run; lock acquired 04:04:44, released 04:04:45 UTC by one rmdir; load 2.81,
43% free; nice 10, threads 1; 1.06 s, peak RSS 146 MB). Two pre-run script edits (vectorised component table; a per-animal cache
removed for memory), disclosed in HW_LOG; no edit after the run.
- A1, A2 PASS (Lemma CAP (i), (ii): 0 violations in 10⁶ samples); A3 control fails as required (332415 violations of the false
  split).
- B (Lemma REL-seq on the exact 4×4 toy, 2¹⁶ configurations, n_♯ = 1, 2, Bernoulli and attractive Ising laws, two relaxation
  orders): B1 telescoping identity PASS; B2 step containment (S2-F1) PASS; B3 log(Z(all)/Z(S_0)) ≥ -2Σp_i PASS in all 28 cases,
  tightness 0.35-0.50; Lemma DECL PASS; B4 control (animal count removed) fails as required; B5 both orders PASS.
- C1 PASS (the depth term is absorbed at n_H). C2 PASS: G = 81 to 15 digits at every recorded constant (LOOP-const), G¹⁰⁰ ≥
  7·10¹⁹⁰. C3 PASS but **uninformative** [post hoc]: θ_K = 1/(2ρ_0) was chosen so large that m_* = 1 in every case; the
  criterion did not test the regime θ_K ≪ 1/ρ_0. C4 PASS (the GAS sums diverge for aβ_+ < 4, ≈ 2.37 at 4.5).
- D: *-animals in Z⁴ through the origin: 1, 80, 7320 for n = 1, 2, 3, below 6400^{n-1}.
Scope: B tests the logic of REL-seq (telescoping, containment, union bound, DECL) on a toy defect law, not the chain; C is
arithmetic. Nothing numeric bears on (SDP), (LI^F) or (SF-cap).

## 17. Outcomes against the session-2 targets (§12) (ADDED AFTER the derivations; pointers only)
- **S1: MET.** [RHW1-fix] edits in §0-§11 (W-1 θ < 1/96; W-2 C_cone and a_bad's size, §12A; W-3 θ < 1/(96·82) for collars; W-4
  C_ℓe^{aR}; H-1 … H-11; K-1; S-1; S-2; FV uncounted; tally 4). HW_LOG carries the appended REVIEW_HIST_S3 correction. Lead's
  lane-G question: every (AE) use is the cone-local infimum; HW now consumes (CLS-min) ⇐ (REG-min) (§12A).
*[RHW2-fix: superseded where marked; current status §18-§19: RS-1 (level-first, ℛ_𝔥^↑, not "any order"), NA-1 (𝒱_K^{LF} in
(NA-∅)), CAP-1 (θ range max{6θ, 24θ}(1 + 2Rg_K²) < 1, not ≈ 1/6), SDP-1 ((SDP) re-owned to node A), CAP-dec uncounted.]*
- **S2: MET.** Lemma REL-seq (§13.2) PROVEN as an implication from (PRICE^ℛ) with B = 164ε_♯ → 0, any order of relaxation, the
  depth term beaten by HIST-sum's arithmetic; Lemma DECL restores LI-a on the relaxed family (bad-only defects), so the
  mismatch half reduces to (LI) over ℛ. (REL) is removed as an independent residual. Node A owes (NA-∅) only (§13.3), and
  Remark GAS shows the returned gas in Z(∅) must be extracted, not bookkept.
- **S3: PARTIAL SUCCESS in the §12 sense.** The rate loss is removed (Lemma CAP, H4-red', Theorem HW^cap: no Hölder, no
  u_{k+1} ≤ 2u_k, capped fine moment; θ up to ≈ 1/6; Lemma CAP-dec: (M-f^cap) in one step at the same rate θ). The LF-count
  question is answered by proven arithmetic: no per-level rate loss ρ_0 > 1 is absorbable by the logarithmic running
  (LOOP-div), and with the rate loss removed the constants still grow ×81 per level (LOOP-const) unless θa_badβ_+ ≥ 4, missed by
  ≈ 10¹⁶. The global-count route relocates to the same arithmetic (§15.2). **Exact wall: (SDP)_θ**, a single-defect Peierls
  bound with a depth-uniform constant at rate θa_bad (§15.3); the mechanism is SAT (one finer returned defect saturates a
  coarse capped window), i.e. missing disjointness across nested scales.
- **Check w2: PASS** (§16; C3 uninformative).

**Session-2 tally (unreviewed; [RHW2-fix] corrected in §18.3: 6 counted in total, CAP-dec uncounted, (SDP) re-owned).** Counted: [HW-6] Lemma REL-seq (CONDITIONAL, implication proven); [HW-7] Lemma H4-red' with
Theorem HW^cap (CONDITIONAL ⇐ (LI^F), (M-f^cap), (CLS-min); SU(2), bad-only); [HW-8] Lemma CAP-dec (CONDITIONAL ⇐ (SF-cap),
(SDP)). Uncounted: Lemmas DECL, CAP, Observation SAT, Lemmas LOOP-div, LOOP-const (arithmetic about bounds), Remark GAS, §12A.
New named hypotheses: (PRICE^ℛ) [consumed by REL-seq; supplied by HW / HW^cap over ℛ], (LI^F) [OPEN, this file], (M-f^cap)
[OPEN, P], (SF-cap) [OPEN, node A], **(SDP) [OPEN, P, this file: the wall]**, (NA-∅) [node A]. Switched: (AE) → (CLS-min) ⇐
(REG-min) [SQ, OPEN, P]. Not consumed this session: RS-joint, PLD-desc, (SG^·), any literature result. **No edits** outside
HW.md, HW_LOG.md, checks/w2_*.

---
# Session 3 of lane H (2026-10-28): consolidation

REVIEW_HW_S2.md (md5 363fb1ae…) is BINDING. Session 3 is a consolidation session: no new frontier work, no numeric jobs, no new
counted items. The binding fixes are made in place in §5-§17 and tagged **[RHW2-fix X]** (X the review's label); this section
records them and states what HW now consumes from node A. Inputs read (read-only) are listed in HW_LOG, session 3.

## 18. [RHW2-fix] record

### 18.1 SDP-1: (SDP) re-owned as (SDP)^A, a per-level output of node A
**Premise corrected.** RLF does price each returned cluster: once, in-step, at its own level ((RLF-2), RLARGE §1.2;
(W1-ret'^J)_k (c), RLARGE §4.2 #5; HIST §14.1 (b), returned large-field terms at O(e^{-a_♯/g_k²}) per cube [as quoted by
REVIEW_HW_S2 §5.1]). What LF-count, K3-b, P4-div and Remark GAS forbid is summing those prices across levels as bookkeeping,
Σ_kL^{4(K-k)}e^{-au_k} with aβ ≪ 4. The correct reading is: **each returned cluster is priced in-step at its own level with
level-uniform constants; their sum is renormalised (c̄_0^{sea} into 𝒱^{LF}, δβ_k into the flow), never bookkept.**

**(SDP)^A_θ [OPEN, P; owner node A].** For every admissible 𝔥, every law μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}} (RS-1), every level k ≥ 0 and
every set S of level-k cubes in Λ_k:
  μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·exp(c_A·shadow sums),  a_A ≥ θa_bad,  C_A, c_A independent of g, K, T, k and the law.
It is a per-level OUTPUT of node A's R-operated representation, proven at each level k separately from: the stage-(k-1)
representation (I_{k-1}^E)' in its two-field form (d); (CLS-min) for the in-step window; (W1-ret'^J)_{k-1} (c); (SC)_{k-1};
R1^J's gas convergence (an activity bound turned into a probability); the (LI)-type future tilt. **It is never derived from
(SDP)^A at level k - 1.** If a_A < θa_bad, θ is lowered to a_A/a_bad and nothing else changes. [Which shadow sums carry c_A
(𝔥's, absorbed by Lemma HS', is the reading HW needs) is a detail of node A's statement, not fixed here.]

**(SF-cap)^A_θ [OPEN; owner node A; the small-field half, content unchanged from CAP-dec's (SF-cap)].** c_sf at rate
24θ(1 + 2Rg_K²) < 1 on defect-free columns, uniformly under conditioning on finer defects in other columns. Source: the
main-term localisation F^col_Q ≤ Σ_{x under Q}𝓔_{k,x} (§6, with HIST's (a')/§25 form, H-9) plus node A's local coupling response.

**(M-f^A)_θ (restated).** For every 𝔥 and R ∈ ℛ_𝔥^↑ ∪ {R(𝔥)}, every k and A ⊂ 𝒰_{k+1}:
  E_R[Π_{Q∈A}e^{θmin{π_Q, Y^f_Q}}] ≤ C_fc^{|A|}·e^{c·shadow sums},  C_fc = c_sf + 81C_Ae^{θa_bad R}, the SAME constant at every level;
  **(M-f^A)_θ ⇐ (SF-cap)^A_θ + (SDP)^A_θ** by Lemma CAP-dec (elementary, uncounted), with (SDP)^A in place of (SDP).
This replaces "(M-f) large-field-tail half: owned by this file" (§5.1, §6, §8, §15.3, §17).

**Consequences for HW.**
- **LOOP-const does not arise in HW.** There is no recursion C_sd(k) ← C_sd(k-1); the constant is level-uniform because node
  A's representation is. The ×81 per level was produced only by the column induction of §15.
- **LOOP-const's reading.** It is LF-count (K3-b, GAS) at n = 1: cross-level bookkeeping of the returned gas inside one column.
  It proves that (SDP) is not obtainable inside the unrenormalised representation ∫W·1_𝔥 by column induction. It is not
  evidence that (SDP) is false, and not a new wall.
- **The difficulty moves to node A; it is not dissolved.** If node A's in-step returned price were itself argued through the
  column-window Chernoff of §14-§15, LOOP-const would return there verbatim. Node A has to use the non-saturating split its
  R-operation encodes: a returned finer cluster enters the coarse problem as c_0(Y) (field-independent) + T_Y·(coarse
  curvature)² (marginal) + R(Y)𝔯 (irrelevant), i.e. (W1-ret'^J) (a)-(b) + I-tay^J + (SF-irr). This is §15.3's option (i) with
  an owner and a mechanism; option (ii) (a pointwise density bound, (D1-b)) is not needed, since what is consumed is the
  integrated in-step price.
- **The unreturned condition (n_♯ + 1)aβ_- > 4 + c_B does not settle LOOP-const.** It controls HIST-sum's count of unreturned
  components only. LOOP-const's chain has one cube per level and consists only of returned cubes (DJ, H-nest (iii)).
- **Remark (REVIEW_HW_S2 §2).** (SDP)^A on ℛ_𝔥^↑, applied with S = 𝒟, already gives (PRICE^ℛ) at one level with a = a_A,
  C_ℓ = C_A, c = c_A; so REL-seq ⇐ (SDP)^A directly. (SDP) is of (PRICE) strength at one level, which is a second reason it
  cannot be HW's residual.
- **Net statement (CONDITIONAL; implications already proven in §13-§15, no new proof):** (H-w') ⇐ (F_R) [g_K² ≤ 1/(2R)] +
  (CLS-min) + (LI^F) [capped weights, LI-1] + (M-f^A)_θ, via Theorem HW^cap and Lemma REL-seq on ℛ_𝔥^↑, with a = θa_bad,
  C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc and max{6θ, 24θ}(1 + 2Rg_K²) < 1. Scope: SU(2) (SU(N ≥ 3) needs (KS-N)), bad-only defects
  (the collar extension is not covered by HW^cap).

### 18.2 The other binding fixes (pointers)
- **RS-1** (§13.2): (PRICE^ℛ) assumed only on ℛ_𝔥^↑ (S ⊇ S(𝔥), level-first ascending); "any order" withdrawn as a feature.
- **NA-1** (§13.3): (NA-∅) := |log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²}; Remark GAS is the reason 𝒱^{LF} is there.
- **CAP-1** (§14, §15.1, §15.3, §17): the condition is max{6θ, 24θ}(1 + 2Rg_K²) < 1; "θ up to ≈ 1/6" withdrawn.
- **LI-1** (§14): (LI^F) stated only for the capped weights F_Q = e^{θmin{π_Q, Y^f_Q}} (or their monotone family).
- **Recount**: Lemma CAP-dec is elementary, uncounted.
- **W2-1, W2-2**: appended corrections in HW_LOG (session 3); §16's "B2 step containment PASS" is on a strided subsample of
  ≈ 2000 configurations per step whenever more fail (w2_relseq_toy.py l.120), not on all configurations as the criterion says;
  B2's content is proven in REL-seq (2) anyway.
- Recommended, applied: H-12 (§10 W2 marked superseded), SAT-1 (§15), REL-seq e^{±38416c} and n_H ≈ 10²² notes (§13.2), CAP-dec's
  unused gain (§15), LOOP-const K_m ≫ 1 (§15.1).

### 18.3 Corrected tally (all sessions)
**Counted: 6** = session 1's 4 ([HW-1] TE + W-bad; [HW-2] CH + Theorem HW; [HW-4] KS + KS-chain; [HW-5] H4-red) + [HW-6] Lemma
REL-seq (CONDITIONAL, with RS-1) + [HW-7] Lemma H4-red' with Theorem HW^cap (CONDITIONAL ⇐ (LI^F) capped, (M-f^cap), (CLS-min);
with CAP-1, LI-1). Session 2's "[HW-8] CAP-dec" is uncounted. Session 3 adds no counted item.
Status lines: (SDP) → **(SDP)^A [OPEN, P; owner node A]**; (M-f)'s tail half → node A via (M-f^A); (LI), (LI^F) [OPEN; HW];
(NA-∅) [node A, NA-1 form]; (CLS-min) ⇐ (REG-min) [SQ, OPEN, P].

## 19. HW as a consumer of node A (interface list for RLARGE v3)

What Theorem HW^cap + Lemma REL-seq + Lemma CAP-dec (with Lemma HS' into HIST-sum) need, item by item. Owner files are as named
in RLARGE §4.2 and SQ, read this session; the wiring itself is the integrator's.

| # | item HW consumes | precise statement | owner file(s) | status | consumed by |
|---|---|---|---|---|---|
| A1 | **(SDP)^A_θ** | §18.1 | node A: RLARGE.md (RLF-2) §1.2 and §4.2 #5 (W1-ret'^J)_k (c) [HIST §8; PLD §9 Prop. W1R], #5a (SC)_k [PLD §9.4], #4 (I_k^E) [HIST §14.1], #15 I-tay^J [PLD/HIST]; R1^J [HIST §5] | OPEN [P]; not written anywhere as a probability bound under μ ∈ ℛ_𝔥^↑ (new interface item) | CAP-dec → (M-f^A); directly REL-seq (Remark §18.1) |
| A2 | **(SF-cap)^A_θ**, rate 24θ(1 + 2Rg_K²) < 1 | §18.1; CAP-dec (§15) | node A: (I_k^E) main term, HIST §14.1 (via §6's reduction); (SF^J)_k, RLARGE §4.2 #3 [HIST §6, §8; PROOF N2, N4, N5, N6] | OPEN | CAP-dec → (M-f^A) |
| A3 | **(NA-∅)** (NA-1 form, with 𝒱_K^{LF}) | §13.3 | node A: RLARGE.md (RLF-1), (RLF-4) §1.2 (Z_K^{ref} := exp(𝒱_K^{LF})·Z_K^{sf,ref}; "its soft-RG definition is part of node A") | OPEN | converts HIST-sum's Z(∅)-relative output (ref-a) into (RLF-4)'s comparison |
| A4 | **(LI)** and **(LI^F)** (capped weights only, LI-1) | §5.2, §14 | **HW.md** (HW's own interface); not identical to RLARGE §4.2 #12 H-4 [HIST §7.3] (H-8: H-4 is the effective-density tilt, (LI) the exact future probability) | OPEN | H4-red (Theorem HW), H4-red' (Theorem HW^cap), over R(𝔥) and ℛ_𝔥^↑ |
| A5 | **(CLS-min)_{c_pr,t_pr} ⇐ (REG-min)** | §4 TE (ii), §12A | (CLS-min): consumed by HW; the implication from (REG-min): SQ.md (DESC, SUP-price, PRICE-iii; SQ session 1, unreviewed); (REG-min): SQ.md §0.3, "the cone-local, sup form of RLARGE (BG)_k / FLOW (SF-bg), node A" [SQ l.203]; (BG)_k is RLARGE §4.2 #8 [PLD §15.2]. Alternative ⇐ (AE): HIST §15.3, §26 (off the critical path) | (CLS-min) ⇐ (REG-min): implication PROVEN in SQ, unreviewed; (REG-min) OPEN [P] | TE (ii) → W-bad, W-cb, SAT, FV |

Also consumed, not new: **(F_R)** with g_K² ≤ 1/(2R) [FLOW §4, §7, §18, §23; RLARGE §4.2 #1, node A5].

**Notes for the integrator (facts about the statements, not wiring decisions).**
- **Exponent.** RLARGE (RLF-3) is written with the price (C_ℓe^{-a_♯/g_j²})^{|𝒟|}. HW delivers (H-w') with a = min{θa_bad, a_A}
  (= θa_bad when a_A ≥ θa_bad), far smaller than a_♯ at the recorded constants, and in the per-component shadow form of Lemma HS'
  with C_ℓ → C_ℓe^{aR}. HIST-sum consumes it unchanged (n_H computed from this a).
- **Reference.** HW works under (ref-a), Z^sf := Z(∅); (RLF-3)'s Z_K^{sf} is reached only through A3.
- **Scope.** SU(2) (KS); SU(N ≥ 3) needs (KS-N) [HYPOTHESIS, s]. Bad-only defects; RLARGE §2.2's collar-bad clause is covered
  only by Theorem HW's W-cb extension ((TC), θ < 1/(96·82), (M-i) unreduced), not by HW^cap.
- **Non-circularity to check [inference].** A1 at level k is built from node A's stage-(k-1) representation. The integrator
  should confirm that this representation does not itself consume (H-w') or HIST-sum at levels ≥ k; HW's own hypotheses do not
  (HW-F4, §6).
- **What does not move into node A.** HW keeps (LI)/(LI^F) and the consumption of (CLS-min). LOOP-div, LOOP-const, §15.2 stay
  as proven arithmetic about bounds; LOOP-const marks what A1's proof must avoid (column induction).

---
# Session 4 of lane H (2026-10-28): the merged future-insensitivity statement (LI^U)

REVIEW_RLARGE_V3.md (md5 38b26eda…) is BINDING for this session: gap S-1 (the node-A moments are stated under laws that carry
the future constraint; the bridge, the "future tilt", is unowned and cannot be carried by (LI^F)), S-2 (bounding the tilt is a
statement about coarser levels; it needs its own top-down proof, new check (d)), Part 6 item 1 ((LI^U), owned by HW).

## 20. Session-4 pre-stated targets (2026-10-28 10:19 UTC; statements only, written before any session-4 derivation)
*[RHW4-fix P-1, session 5]* Read: "statements only, written before any WRITTEN session-4 derivation (key ideas reasoned before;
HW_LOG session 4, first entry)".

Notation. For R = R_{S,E} in 𝔉_𝔥 := ℛ_𝔥^↑ ∪ {R(𝔥)} (§13.1-§13.2) and a level k, the **weighted future** is
  h^{R,F}_k(U_k) := ∫Π_{i≥k}K_i(U_{i+1}, U_i)·Π_{j≥k+1}1_{R,j}·F^{>k} dU_{k+1}⋯dU_K,
F^{>k} a product of HW^cap's capped spectator weights of levels > k (F ≡ 1 allowed). The **future tilt** of the brief is
H_k(U_k) := ∫K_k·1_{R,k+1}·h_{k+1}dU_{k+1} (REVIEW_RLARGE_V3 S-1). For a set A of level-k links, its **influence column**
I_m(A) (m > k) is the set of level-m cubes some 1_{R,m}-clause or spectator could read through the kernels from A (to be
determined exactly in the derivation), and #_R(A) := Σ_{m>k}|I_m(A) ∩ S_R^{(m)}| counts its CONSTRAINED cubes.

### Target U1: state (LI^U)
**(LI^U) [statement under test].** There is c_U independent of g, K, T, 𝔥 and the law such that for every R ∈ 𝔉_𝔥, every k,
every set A of level-k links, every admissible spectator family F, and all U, U' that agree off A:
  h^{R,F}_k(U) ≤ exp(c_U·(|A| + #_R(A)))·h^{R,F}_k(U').
It is to cover: (LI) (A = int(𝒰_{k+1}) at level k+1, F ≡ 1), (LI^F) (the same with capped spectators), and the future tilt
H_k on every link set the node-A inputs (SDP)^A, (SF-cap)^A read (defect sets S, history-cube columns), not only
history-cube interiors.

### Target U2: prove (LI^U) top-down, or name the exact wall
- (a) Identify H_k exactly in terms of h (the relation between the brief's tilt and HW's h_{k+1}).
- (b) Determine I_m(A) exactly from the kernel data-reading; prove the case #_R(A) = 0 (influence column inside the
  relaxed set) with the best constant, by an argument that reads only kernel locality, the defect clauses and the
  spectators, and consumes no statement about levels > k.
- (c) The case #_R(A) > 0: prove (LI^U) TOP-DOWN (from h_K ≡ 1 down), using only kernel locality, declaration-type
  monotonicity, the product structure of K_i, and (if needed) forward-chain estimates, without (H-w′), HIST-sum or (RLF-3′)
  at levels > k; or prove (LI^U) false in this case and state the weakest true form; or name the exact wall.
- (d) Decide, consumer by consumer (H4-red′, CAP-dec's (SDP)^A and (SF-cap)^A, REL-seq's (PRICE^ℛ), RLARGE K8), which case
  of (LI^U) each actually consumes, and whether the HW route can be arranged to consume only the case of (b).

### Target U3: check (d) written explicitly
State check (d) as a list of the statements about levels > k that each level-k input of the HW route consumes, with the
induction direction of every proof, and decide for each: non-circular (proof given), or open (exact residual named).

### Target U4: Theorem HW's hypothesis list restated with (LI^U)
The complete hypothesis list of (H-w′) on the HW route after U1-U3, each item with its law, its owner and its status.

### Check w4 (criteria first: checks/w4_criteria.md, then the script)
A finite combinatorial check of the influence-column geometry of U2 (b) on small multi-level lattices with random
histories, with a negative control (a kernel whose contours leave the two endpoint blocks) and a control on a constrained
column. Informational, never a proof.

# Session-4 derivations (written after §20; started 10:50 UTC)
*[RHW4-fix P-1, session 5]* Read: "typed from 10:50 UTC; reasoned from 10:00 UTC, partly before §20".

Conventions of §0, §13 unchanged; bad-only, history-independent defect notion throughout (as Theorem HW^cap). A level-m cube
is a level-(m+1) site; π maps a level-m cube to the level-(m+1) cube containing it. For an admissible 𝔥 and a level m ≥ 0 put
  **A_m(𝔥) := Σ(Ω^c_{m-1}) ∪ N_1(𝒰_m)** (the cubes R(𝔥) does not constrain at level m), S^{(m)}(𝔥) = all ∖ A_m(𝔥) (§13.1 (m2)),
and s(𝔥) := Σ_{(j,𝒟)}Σ_{k=j}^{K-1}|sh_k(𝒟)| (the shadow sums of Lemma HS′).

## 21. U2 (a): the future tilt is HW's own h

**Lemma TILT (exact): PROVEN-HERE (elementary, not counted).** For R with 1_R = Π_j1_{R,j} and a bounded spectator product F^{>k}
of levels > k, put h^{R,F}_k(U_k) := ∫Π_{i≥k}K_iΠ_{j≥k+1}1_{R,j}F^{>k}dU_{k+1}⋯dU_K (h_K ≡ 1). Then:
- (i) h^{R,F}_k = ∫K_k(U_{k+1}, U_k)·1_{R,k+1}·F_{k+1}·h^{R,F}_{k+1}dU_{k+1} (F_{k+1} the spectators reading U_{k+1}). So the brief's tilt
  H_k = ∫K_k1_{R,k+1}h_{k+1} is **h^{R,1}_k**, and HW's h_{k+1} of (LI), (LI^F) is the same family one level up.
- (ii) Let ν^R_k be the law of (U_0, …, U_k) with density ∝ e^{-S_0}Π_{i<k}K_iΠ_{j≤k}1_{R,j} (the **past law**: constraints of
  levels ≤ k only). For every bounded f(U_0, …, U_k): E_{μ_R}[f] = E_{ν^R_k}[f·h^{R,1}_k(U_k)]/E_{ν^R_k}[h^{R,1}_k]. The same holds
  with finer spectators inserted in ν and coarser ones in h.
- (iii) h^{R,1}_k(U) is the probability, for the forward kernel chain started at U_k = U, that every constraint of levels
  ≥ k + 1 holds.
*Proof.* ∫K_idU_{i+1} = 1 for every i and Fubini. ∎
*Reading.* (LI), (LI^F) and the future tilt are ONE function family h^{R,F}_k; they differ only in the level and in the link set
on which insensitivity is asked. This is the merge asked for by REVIEW_RLARGE_V3 Part 6 item 1.

## 22. U2 (b): the influence column, and the exact zero on relaxed columns

**Lemma FP (influence column): PROVEN-HERE (counted [HW-9] with Theorem LI^U-0).** Kernel data-reading as in HIST l.964
("S4' contours of c stay in c's two endpoint blocks"): a level-(m+1) link c = (X, X + e_μ) reads a level-m link only if both
of its endpoints lie in the blocks X ∪ (X + e_μ). For a set A of level-k links let F_k := A and F_{m+1} := the level-(m+1) links
that read some link of F_m. Let ℓ ∈ A have its endpoints in the level-k cubes x_1, x_2 (equal or adjacent). Then for every
m ≥ k + 1:
- (i) every link of F_m(ℓ) has an endpoint at a level-m site of π^{m-k-1}({x_1, x_2}) (level-(m-1) cubes read as level-m sites);
- (ii) a level-m cube containing both endpoints of a link of F_m(ℓ) lies in π^{m-k}({x_1, x_2});
- (iii) a level-(m+1) cube onto which both endpoint cubes of a link of F_m(ℓ) project equals π^{m-k+1}(x_1) or π^{m-k+1}(x_2).
*Proof.* (i) m = k + 1: c reads ℓ only if x_1, x_2 ∈ {X, X + e_μ}, so c is incident to the site x_1 (and x_2). Step: a link of F_m
has endpoints s, s′ with s ∈ π^{m-k-1}({x_1, x_2}); a level-(m+1) link reading it has both π(s), π(s′) among its endpoints, so it
is incident to π(s) ∈ π^{m-k}({x_1, x_2}). (ii) A cube containing both endpoints contains s, so it is π(s). (iii) The endpoint
cube of s is π(s); its projection is π²(s) ∈ π^{m-k+1}({x_1, x_2}). ∎

**Lemma NR (noise representation): PROVEN-HERE (classical measure theory, not counted).** For each level-(m+1) link c there is a
measurable Ψ_c with Ψ_c(M, ξ) ∼ k_c(·; M) for ξ uniform on [0, 1] (randomisation lemma for a probability kernel into the standard
Borel space SU(N)). With i.i.d. ξ_{m+1,c}, U_{m+1,c} := Ψ_c(M̄_c(U_m), ξ_{m+1,c}) realises the forward chain from U_k, because
K_m = Π_ck_c (independent links given U_m). Consequently, by induction on m, **U_m restricted to the links outside F_m(A) is a
measurable function of (U_k off A, ξ), not of U_k on A** (a link c ∉ F_{m+1} has M̄_c reading only links outside F_m).

**Theorem LI^U-0 (exact future insensitivity on relaxed columns): PROVEN-HERE [HW-9] (counted).** Let 𝔥 be admissible, k ≥ 0,
and A a set of level-k links each of whose endpoint cubes x satisfies **π(x) ∈ A_{k+1}(𝔥)**. Let F be any product of bounded
measurable spectators F_{Q″}, Q″ ∈ 𝒰_{m+1}, m ≥ k + 1, each a function of U_m on the links whose two endpoint cubes project to
Q″. Then h^{R(𝔥),F}_k(U) = h^{R(𝔥),F}_k(U′) whenever U, U′ agree off A.
*Proof.* Step 1 (persistence). For m ≥ k + 1, π(A_m(𝔥)) ⊂ Σ(Ω^c_m): π(Σ(Ω^c_{m-1})) ⊂ π(Ω^c_m) (H-nest (i)) ⊂ Σ(Ω^c_m), and
π(N_1(𝒰_m)) ⊂ N_1(π(𝒰_m)) ⊂ N_1(π(Ω^c_m)) = Σ(Ω^c_m) (|⌊u/L⌋ - ⌊v/L⌋| ≤ 1 if |u - v| ≤ 1). Iterating, for x as in the
hypothesis: π^{m-k}(x) ∈ A_{k+1} at m = k + 1 and π^{m-k}(x) ∈ Σ(Ω^c_{m-1}) ⊂ A_m for m ≥ k + 2; and π^{m-k+1}(x) ∈ Σ(Ω^c_m)
for m ≥ k + 1. Step 2 (nothing reads the footprint). Constraints: 1_{R,m} (bad-only) reads U_m only on links interior to cubes
of S^{(m)}(𝔥); by FP (ii) a footprint link interior to a cube lies in π^{m-k}(x) ∈ A_m, not in S^{(m)}. Spectators: by FP (iii) a
footprint link read by F_{Q″} has Q″ = π^{m-k+1}(x) ∈ Σ(Ω^c_m), and 𝒰_{m+1} ∩ Σ(Ω^c_m) = ∅ by (A2). Step 3. By NR, every factor
Π_{j≥k+1}1_{R,j}·F is a function of (U_k off A, ξ); integrate ξ. ∎

**Corollary LI-0 (what it discharges): PROVEN-HERE (not counted separately).**
- (a) **(LI) and (LI^F) hold under μ_{R(𝔥)} with c_k = 0, for ANY bounded spectators** (LI-1's restriction to capped weights is
  not needed): apply the theorem at level k + 1 to A = the links of int(𝒰_{k+1}); their endpoint cube is Q ∈ 𝒰_{k+1}, and
  π(Q) ∈ π(Ω^c_{k+1}) ⊂ Σ(Ω^c_{k+1}) ⊂ A_{k+2}. Hence Lemmas H4-red and H4-red′ hold under μ_{R(𝔥)} with no shadow factor:
  **(M-i) under μ_{R(𝔥)} is PROVEN for SU(2)** with C_mis = (1 - λ)^{-3/2}, c_LI = 0.
- (b) ~~**The future tilt on history columns is exactly absent.**~~ **[RHW4-fix LI0-1] The future tilt does not read the history
  columns; it enters only as a weight that is a function of the far field** (it still reweights the column through the column's
  correlation with the far field under the past law; that is why H6-H7 are stated under a weighted past law). Put L^far_k(𝔥) := the level-k links with an endpoint cube x with
  π(x) ∈ S^{(k+1)}(𝔥). Then h^{R(𝔥),1}_k is a function of U_k restricted to L^far_k(𝔥) only. In particular it does not read U_k on the
  level-k column of N_1(𝒰_{k+1}) (π(x) ∈ N_1(𝒰_{k+1}) ⊂ A_{k+1}), nor on Ω^c_k and its Σ-collar (π(x) ∈ Σ(Ω^c_k) ⊂ A_{k+1}).
- (c) [Remark for K15 (i), PROVEN as geometry] If the relaxed collar N_1(𝒰_m) is replaced by N_2(𝒰_m), Step 1 survives:
  π(N_2(B)) ⊂ N_1(π(B)) for L ≥ 3 (|⌊u/L⌋ - ⌊v/L⌋| ≤ ⌊2/L⌋ + 1 = 1). So the future side of the collar extension is case 0 too;
  what K15 (i) still needs is the SAME-level reading of C(Q) by neighbouring collar clauses (unchanged).

**Answer to S-1.** REVIEW_RLARGE_V3 is right that (LI^F) as stated (int(𝒰_{k+1}) only) cannot carry the tilt on a defect set S.
On the sets HW's node-A inputs actually read (~~§23~~ [RHW4-fix nit: Cor. LI-0 (b), §22]: the history columns), the tilt is not carried by any bound: it is exactly
a function of the far field (Corollary LI-0 (b)), and Lemma TILT (ii) turns (SDP)^A, (SF-cap)^A into past-law statements
weighted by a function of L^far_k. What this costs node A is §24.

## 23. U2 (c): constrained columns. The pointwise statement is false

**Proposition LI-pw (pointwise (LI^U) fails on constrained columns): ARGUED (not counted; one ingredient [inference]).** For every
c_U < ∞ and all g small enough there are an admissible 𝔥 (𝔥 = ∅ suffices), a level k, a level-k cube x with π(x) ∈ S^{(k+1)}(𝔥),
A := the links of int x, and U, U′ agreeing off A, with every interior plaquette of x trivial in both, such that
h^{R(𝔥),1}_k(U′) > exp(c_U(|A| + #(A)))·h^{R(𝔥),1}_k(U).
**[RHW4-fix LP-1]** The level is restricted: **k ≤ K − 2 with K − k held fixed** while g_K → 0 (k = K − 2 suffices; at
k = K − 1, h_k ≡ 1 since there are no constraints above level K − 1, and for K − k growing the allowance's #(A) ≤ K − k and
u_k ≈ u_K + β(K − k)log L change together). In (β) the cube x is chosen with the plaquette interior to π(x), i.e. x away from
∂π(x). In (γ) "probability ≥ ½" is replaced by **"probability → 1 (as g → 0) under both U and U′"**, the n_♯ cubes being
*-connected among themselves; then h(U) → 0, while h(U′) stays bounded below because the n_♯ cubes form a component of size
n_♯ without π(x) (with "≥ ½" the argument gives only a factor ≈ 2, not a divergent ratio).
*Mechanism.* (α) [inference: the S4' contour family is not re-derived here] Take U on int x pure gauge, U_{yz} = g(y)g(z)^{-1},
with g = 1 near the faces of x in direction ν and g = G ≠ 1 near the faces in direction μ; crossing links stay fixed. All interior
plaquettes of x are trivial (x is good at level k); the straddling plaquettes carry the curvature, which no bad-only clause reads.
The contour transporters of the two level-(k+1) links at the site x in directions μ, ν acquire relative factor G, so the coarse
holonomy W_0(M̄) of a level-(k+1) plaquette at x differs from that of U′ (g ≡ 1) by O(|G - 1|) ≫ 2ε_1. (β) Lemma KQ / RS-lin
concentration (HIST §3): V lies within O(g_k) of W_0(M̄) except with probability e^{-cκε_1²/g_k²}; so π(x) is bad with
probability → 1 under U and → 0 under U′ as g → 0. (γ) Choose U off A with the same device on n_♯ other level-k cubes so that,
with probability ≥ ½ under both, a *-connected set of n_♯ bad level-(k+1) cubes of S^{(k+1)} adjacent to π(x) appears, and let
coarser levels be otherwise unconstrained in effect. Then h(U) ≤ P(π(x) good | U) + ½·(…) is driven to 0 relative to h(U′) at rate
e^{-cε_1²/g²}, while the allowance is g-independent.
*Reading.* (1) The row-10g form proposed in REVIEW_RLARGE_V3 S-1 (a ratio bound for all U, U′ differing on S's links, on
constrained S) is **false as a pointwise statement** at bad-only defects, even with U, U′ both good on S: goodness at level k does
not control the coarse holonomy (coherent or pure-gauge-relative transport). (2) What can hold on constrained columns is an
averaged statement. Its natural form is the **column re-constraining cost**
  **(CRC)_k:** for every admissible 𝔥 and every set B of level-k cubes, with R^{-B} := R(𝔥) with the cubes π^{m-k}(B) (m > k)
  removed from S^{(m)}: Z(R^{-B}) ≤ exp(c_U·#(B))·Z(R(𝔥)), #(B) := Σ_{m>k}|π^{m-k}(B) ∩ S^{(m)}(𝔥)|,
which by Theorem LI^U-0 applied to R^{-B} turns a μ_{R(𝔥)}-probability of an event on B's links into a past-law probability with a
far weight, at the price e^{c_U#(B)} (μ_R(E) ≤ μ_{R^{-B}}(E)·Z(R^{-B})/Z(R) since R ⊂ R^{-B}). **[RHW4-fix CR-1]** Theorem LI^U-0
as stated is for R(𝔥); its use for R^{-B} is Theorem LI^U-0′ (§30.1: R-free endpoint cubes, spectators off the relaxed columns,
or F ≡ 1), whose spectator step is the one that changes. (CRC)_k is a statement about levels > k
(it is the probability, under R^{-B}, that the relaxed column's constraints hold). Its top-down analysis is §24.3.

**Consumers, case by case (U2 (d)).**
| consumer | link set whose tilt is used | case | status after this session |
|---|---|---|---|
| H4-red′ in Theorem HW^cap under μ_{R(𝔥)} | int(𝒰_{k+1}) at level k+1 | relaxed | c_k = 0, PROVEN (Cor. LI-0 (a)) |
| CAP-dec's (SDP)^A, (SF-cap)^A under μ_{R(𝔥)} | level-k columns of 𝒰_{k+1} | relaxed | tilt exactly far-only (Cor. LI-0 (b)); node-A form §24 |
| REL-seq's (PRICE^ℛ) on ℛ_𝔥^↑ | the step animal 𝒟 at level j: int(𝒟) and its columns; π^{m-j}(𝒟) ∈ S^{(m)}(𝔥) for m > j | constrained | consumes the case of Prop. LI-pw; **REL-seq is replaced by REL-boot (§24.1), which needs no ℛ-law** |
| RLARGE K8 / EXISTENCE union bound (single cube under P_K or μ_{R(∅)}) | one constrained cube | constrained | off the HW route; needs (CRC) (for the RLARGE / EXISTENCE owners) |
So the HW route can be arranged to consume only the relaxed case (U2 (d): yes), provided REL-seq is replaced.

## 24. The HW route without constrained tilts

### 24.1 Lemma REL-boot ((REL) from the per-history bound alone)
**Lemma REL-boot: CONDITIONAL [HW-10] (implication PROVEN-HERE; counted; unreviewed).** Assume, for EVERY admissible 𝔥′ (bad-only),
  **(PH)** Z(𝔥′) ≤ Z(R(𝔥′))·e^{c_1 s(𝔥′)}·Π_{(j,𝒟)∈𝔥′}(C_ℓe^{-au_j})^{|𝒟|}
(Theorem HW^cap's conclusion, with c_1 := c_LI + c_f = c_f by Cor. LI-0 (a)). Assume (F_R) (lower half), put B_* := c_1 + 1,
  r := 6400·C_ℓe^{38417B_* + aR}e^{-a/g_K²},  ε′ := 2·6400^{n_♯}(C_ℓe^{38417B_* + aR}e^{-a/g_K²})^{n_♯+1},
and suppose (n_♯ + 1)aβ_-log L ≥ 38416B_*, r ≤ ½ and 164ε′ ≤ 1. Then for every admissible 𝔥, under (ref-a),
  **Z(R(𝔥)) ≤ (4/3)·Z(∅)·exp(164ε′·s(𝔥)).**
*Proof.* (1) *A priori finiteness.* T and K are finite, so there are finitely many histories; Z(∅) > 0 (§13.1 (m2)). Hence, with
B := 164ε′ ≤ 1, M := max_𝔥 Z(R(𝔥))/(Z(∅)e^{Bs(𝔥)}) is a finite number ≥ 1 (𝔥 = ∅).
(2) *Decomposition.* Z(R(𝔥)) = Σ_{𝔥′}∫W1_{𝔥′}1_{R(𝔥)} ≤ Σ_{𝔥′∈H(𝔥)}Z(𝔥′), H(𝔥) := {𝔥′ : {𝔥(c) = 𝔥′} ∩ R(𝔥) ≠ ∅} (Lemma HR). ∅ ∈ H(𝔥)
contributes ≤ Z(∅). **Every component 𝒟′ (level j) of 𝔥′ ∈ H(𝔥) meets A_j(𝔥):** 𝒟′ ⊂ D_j is *-connected with > n_♯ cubes; if
𝒟′ ⊂ S^{(j)}(𝔥) it lies in one *-component of D_j ∩ S^{(j)}(𝔥) with > n_♯ cubes, contradicting R(𝔥).
(3) *Per-history bound.* For 𝔥′ ≠ ∅: Z(𝔥′) ≤ Z(R(𝔥′))e^{c_1s(𝔥′)}Π(…) ≤ M·Z(∅)·Π_{(j,𝒟′)∈𝔥′}w(j, 𝒟′),
  w(j, 𝒟′) := (C_ℓe^{-au_j})^{|𝒟′|}exp((B + c_1)Σ_{k=j}^{K-1}|sh_k(𝒟′)|)  (s and the product are additive over components).
(4) *Anchored sum.* A history is determined by its set of pairs (j, 𝒟′); so
  Σ_{𝔥′∈H(𝔥)∖∅}Π w ≤ Π_{(j,𝒟′) meeting A_j(𝔥)}(1 + w) - 1 ≤ exp(Σ_{(j,x): x∈A_j(𝔥)}Σ_{𝒟′∋x}w(j, 𝒟′)) - 1.
For x of level j ≤ K - 1, with (g3) (≤ 6400^{n-1} *-animals of n cubes through x), H-geo (iv), B + c_1 ≤ B_* and
u_j ≥ u_K + β_-(K - j)log L - R:
  Σ_{𝒟′∋x, |𝒟′|=n}w ≤ 6400^{n-1}(C_ℓe^{38417B_* + aR}e^{-au_K})^n·exp((K - j)[38416B_* - naβ_-log L]) ≤ r^n/6400  (n ≥ n_♯ + 1),
so Σ_{n>n_♯} ≤ 2r^{n_♯+1}/6400 = ε′ (r ≤ ½). And Σ_j|A_j(𝔥)| ≤ 82Σ_j|Ω^c_j| ≤ 82s(𝔥) (REL-seq step (5)). Hence the sum is
≤ e^{82ε′s(𝔥)} - 1.
(5) *Fixed point.* Z(R(𝔥))/(Z(∅)e^{Bs}) ≤ e^{-Bs} + M·e^{-Bs}(e^{82ε′s} - 1) = y² + M(y - y²) ≤ 1 + M/4, y := e^{-82ε′s} ∈ (0, 1].
Maximise over 𝔥: M ≤ 1 + M/4, so M ≤ 4/3. ∎
*Consequences.*
- **(REL) holds with B = 164ε′ and the constant 4/3**, from (PH) alone. With Theorem HW^cap: **(H-w′) with B_0 := c_f + 164ε′ +
  log(4/3)** (s(𝔥) ≥ n_♯ + 1 ≥ 1 for 𝔥 ≠ ∅ absorbs the 4/3).
- **No relaxed family is used**: (PRICE^ℛ), ℛ_𝔥^↑, Lemma DECL and Lemma REL-seq leave the route (they stay proven
  implications). REVIEW_RLARGE_V3 S-3 (law family too wide) and S-4 (uniformity over R_{S,E}) dissolve **[RHW4-fix CR-2: on the
  (E1) route only]**: every law on the route is μ_{R(𝔥)} for an admissible 𝔥. Under (E2) + (CRC) node A's inputs are needed
  uniformly over a pattern family (the column-relaxed family 𝔉_𝔥 of §30), so S-4 returns there in an explicit form. Fix R3-1 (B_0 ≥ c from (PRICE^ℛ)) is superseded by the B_0 above.
- **Order of constants (non-circular):** a, C_ℓ, c_f (node A + KS) → B_* := c_f + 1 and B_0 := c_f + 2 ≥ c_f + 164ε′ + log(4/3)
  → n_H(a, B_0) → n_♯ ≥ n_H (then (n_♯ + 1)aβ_-log L ≥ 38416B_*) → g_0(n_♯) with r ≤ ½, 164ε′ ≤ 1.
- *Why this is a proof and §3.2's remark ("a bootstrap, not a proof") was not:* M is finite before the argument, and the
  inequality M ≤ 1 + M/4 has coefficient < 1; the 𝔥′ need not be smaller than 𝔥.
- *[RHW4-fix RB-1, recommended]* REL-boot is HIST-sum's anchored-sum argument applied to Z(R(𝔥)) in place of Z_K. Its
  quantifier: (PH) is consumed for EVERY admissible 𝔥′, i.e. through Theorem HW^cap, node A's H6-H7 for every 𝔥′ (not circular:
  node A consumes no (H-w′)).

### 24.2 Finding J-1 and Lemma TEL-f (the joint fine moment)
**Finding J-1 (binding for HW; new).** Theorem HW^cap consumes **(M-f^cap)** jointly over ALL levels (one expectation of
Π_kΠ_{Q∈𝒰_{k+1}}e^{θmin{π_Q,Y^f_Q}}, §14). Lemma CAP-dec is stated for one level ("Fix k ≥ 1 and A ⊂ 𝒰_{k+1}", §15), and (M-f^A),
(SDP)^A, (SF-cap)^A (§18.1) are per-level. The step "per-level ⇒ joint" is not written, and is not a consequence of the
per-level statements: a Markov peel from the top makes the level-k_1 factor a one-step forward quantity given U_{k_1-1}, which is
column induction (LOOP-const); a peel from the bottom conditions on the coarse field (Proposition FV).
**Lemma TEL-f (telescoping over levels): PROVEN-HERE (exact; not counted).** Let Φ_{-1} := Π_{Q∈𝒰_0}e^{θX_Q} and
Φ_k := Π_{Q∈𝒰_{k+1}}e^{θmin{π_Q,Y^f_Q}} (k ≥ 0), and μ^{(k)} := (Π_{k′<k}Φ_{k′})·μ/E_μ[Π_{k′<k}Φ_{k′}]. Then
E_μ[Π_kΦ_k] = Π_kE_{μ^{(k)}}[Φ_k]. *Proof.* Φ ≥ 1 bounded; E_μ[Π_{k′≤k}Φ_{k′}] = E_μ[Π_{k′<k}Φ_{k′}]·E_{μ^{(k)}}[Φ_k]; induct. ∎
So **(M-f^cap) under μ_{R(𝔥)} ⇐ CAP-dec at each level k under μ^{(k)}_{R(𝔥)}** (μ_{R(𝔥)} with the FINER capped spectators
inserted), i.e. ⇐ (SF-cap) and (SDP) at level k under μ^{(k)}_{R(𝔥)}. By Lemma TILT (ii) and Cor. LI-0 (b), for an event or
function E of the level-k column of 𝒰_{k+1} (and finer fields):
  **E_{μ^{(k)}_{R(𝔥)}}[E] = E_{ν^{(k)}_k}[E·h_k]/E_{ν^{(k)}_k}[h_k],  h_k = h^{R(𝔥),1}_k a function of U_k on L^far_k(𝔥) only,**
ν^{(k)}_k := the past law of levels ≤ k (constraints of levels ≤ k of R(𝔥)) with the finer capped spectators inserted. The
insertions are at levels < k only, so ν^{(k)}_k is built bottom-up, inside node A's own order of integration.
**[RHW4-fix TF-1, adopted for the (E1) form] Coarse-first telescoping.** Put μ^{[k]} := (Π_{k′>k}Φ_{k′})·μ/E_μ[Π_{k′>k}Φ_{k′}]. Then
E_μ[Π_kΦ_k] = Π_kE_{μ^{[k]}}[Φ_k] (the same identity, inducted downward from k = K - 1; every Φ ∈ [1, e^{θπ}]). The coarser factors
Φ_{k′}, k′ ≥ k + 1, are functions of U_{k′} on the columns of 𝒰_{k′+1}: exactly the spectators Theorem LI^U-0 allows. By TILT (ii)
(coarser spectators in h), μ^{[k]}_{R(𝔥)} restricted to U_{≤k} is **the plain past law ν^{R(𝔥)}_k (constraints of levels ≤ k, no
spectator) weighted by h^{R(𝔥),F^{>k}}_k**, and by Theorem LI^U-0 this weight is a function of U_k on L^far_k(𝔥) only. So on the (E1)
route node A's law is PLD §16.0's past law ν^μ_k verbatim, with a far weight. (REVIEW_HW_S4 TF-1; the finer-first form above stays
valid as an identity.) **[session 5, §30.5] On the (E2) + (CRC) route the FINER-first order is the one used**, because there (CRC)
is applied with the spectator weight inside the partition functions, and the coarser spectators Φ_m (m ≥ k + 1) can read the
interior of a level-m animal lying in the column of a level-(m + 1) history cube, which breaks the H4-red′ peel; finer spectators
never read a level at which an animal is priced.

### 24.3 What node A must deliver, and the exact wall
**(SDP)^{A,far}_θ and (SF-cap)^{A,far}_θ [OPEN, P; owner node A; replace (SDP)^A, (SF-cap)^A of §18.1 on the HW route].** For every
admissible 𝔥, every k ≥ 0, every set A ⊂ 𝒰_{k+1} and every set S of level-k cubes in the columns of A, the bounds of CAP-dec
((SDP): ν(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}e^{c_A s_k(𝔥)}, a_A ≥ θa_bad; (SF-cap): rate 24θ(1 + 2Rg_K²) < 1, uniformly under
conditioning on finer defects in other columns, allowance e^{c_sf′s_k(𝔥)}) hold for **ν = ν^{(k),w}_k := w·ν^{(k)}_k/E[w]** with w = h_k. Level 0 (k = -1):
the level-0 Wilson window moment of Φ_{-1} under the past law of level 0 weighted by h_0 (the same case-0 argument: π(Q) ∈ Σ(Ω^c_0)).
**Whose shadow sums (REVIEW_RLARGE_V3 S-1, load-bearing):** ~~the allowance at level k must be the level-k SLICE
s_k(𝔥) := Σ_{(j,𝒟), j≤k}|sh_k(𝒟)| (Σ_ks_k = s(𝔥)), because TEL-f applies the level-k bound once per level; an allowance e^{c·s(𝔥)}
per level would give e^{Kc·s(𝔥)}. With the slice, c_f := c_A + c_sf′ in Theorem HW^cap.~~ **[RHW4-fix SL-1]** The slice is
mis-indexed (the level-k factor concerns 𝒰_{k+1}'s columns; for 𝔥 with components only at level k + 1, s_k(𝔥) = 0) and PLD §16.5
NA-PRICE does not deliver it. The allowance at level k is **S's own coarse shadow sum ‖S‖_sh := |S| + Σ_{m>k}|sh_m(S)| (union form)
for S under 𝒰_{k+1}** (and ‖A∖A′‖_sh-type sums for (SF-cap), PLD §16.5), which is affordable by:
**Lemma SL (shadows of sets under 𝒰_{k+1}): PROVEN-BY-REVIEW (REVIEW_HW_S4 Priority 5; elementary, not counted; re-read here).**
For S ⊂ the level-k descendants of 𝒰_{k+1}: sh_{k+1+r}(S) ⊂ N_1(sh_{k+1+r}(𝒰_{k+1})) for r ≥ 0 (sh_{k+1}(𝒰_{k+1}) := 𝒰_{k+1}).
Hence |sh_m(S)| ≤ 81Σ_{𝒟⊂𝒰_{k+1}}|sh_m(𝒟)| (m ≥ k + 1), and with one S_k per level (TEL-f), **Σ_k‖S_k‖_sh ≤ Σ_k|S_k| + 81·s(𝔥).**
*Proof (the reviewer's).* r = 0: Σ(S) = N_1(π(S)) ⊂ N_1(𝒰_{k+1}). Step: Σ(N_1(X)) = N_1(π(N_1(X))) ⊂ N_1(N_1(π(X))) = N_1(Σ(X))
(|⌊u/L⌋ - ⌊v/L⌋| ≤ 1 for |u - v| ≤ 1); |N_1(X)| ≤ 81|X|. ∎
The |S_k| part goes into C_A^{|S|} (CAP-dec's 81^{|A′|} count is already there); the s(𝔥) part is Theorem HW^cap's c_f with
**c_f := 81(c_A + c_sf′)**, read so in H6-H7 and in B_0. (On the HW route c_U = 0 exactly (Theorem LI^U-0), so PLD's c_A = 4c_U +
c_f + c_ns reduces to c_ns there: REVIEW_HW_S4 X-2, a cross-lane note for PLD, not an HW edit.)
Two sufficient forms:
- **(E1) far-uniform form:** the bounds hold for every bounded measurable w ≥ 0 of U_k on L^far_k(𝔥) (equivalently, for the
  conditional law of ν^{(k)}_k given U_k on L^far_k(𝔥)). It contains no information about levels > k.
- **(E2) good-buffer form + (CRC):** the bounds hold for every w supported on far fields with no level-k defect within the
  N_1-column collar of A (buffer of one level-(k+1) cube), and the far defects next to the collar are priced through (CRC)_k
  (Proposition LI-pw's reading (2)): μ(S ⊂ D_k) ≤ μ(S ⊂ D_k, buffer good) + Σ_y μ(S ∪ {y} ⊂ D_k), the second term by (CRC)_k for
  {y} and the past-law bound for S ∪ {y} (a Peierls series in the far defects).
*[inference, not used]* (E1) in its sup form is doubtful at the recorded thresholds: a far returned component carrying O(1)
holonomy at distance one level-(k+1) cube (9 level-k sites) from a history column can force curvature ≥ ε_1 (≈ 7·10⁻⁴⁰) inside it
under the conditional law (Stokes: the flux spreads over the spanning surfaces). Such far fields are rare, which is (E2)'s
content; whether the rarity survives the weight h_k is exactly (CRC).
**[RHW4-fix E1-1] (E1) is EXPECTED FALSE in sup form [inference; REVIEW_HW_S4 Priority 6].** The mechanism is energetic, not
topological (the Stokes reading above is struck as the reason: the complement of a 4D blob is simply connected): a far field
with O(1) curvature 2-3 level-(k+1) cubes from 𝒰_{k+1} is admissible; under the past law the far U_k pulls the finer fields below
the far blocks through the kernel likelihood (∝ e^{-κu_{k-1}φ}), whose own action is also ∝ u, so at small g the conditional law
concentrates near the minimiser of a g-independent variational problem, whose interpolation into the column has curvature
c_0·dist^{-p} ≫ ε_1 at fixed distance (classical lattice gauge fields do not screen). So no g-uniform (SDP)^{A,far} holds in sup
form. **The route of record is (E2).**
**[RHW4-fix E2-1] The buffer, defined.** For A ⊂ 𝒰_{k+1}:
  **Buf_k(A) := {level-k cubes y : π(y) ∈ S^{(k+1)}(𝔥), dist_∞(π(y), A) ≤ 2}** (level-(k+1) index distance),
the first ring of FAR columns (the level-k cubes under N_1(𝒰_{k+1}) are in relaxed columns, π(y) ∈ A_{k+1}, and need no (CRC)).
(E2) reads: the bounds hold under ν^{(k),w}_k for every bounded measurable w ≥ 0 of U_k on L^far_k(𝔥) with w = 0 unless
Buf_k(A) ∩ D_k = ∅ (D_k is a function of U_k for bad-only defects, and the links of int y, y ∈ Buf_k(A), lie in L^far_k(𝔥)).
**The real content of (E2) is screening**: a buffer whose interior curvature is < ε_1 everywhere must screen the column from the
far field to within the (SDP)/(SF-cap) constants. That is plausible but not shown, and E1-1's mechanism is not obviously
stopped by a good buffer [inference, session 5]: bad-only goodness reads only the INTERIOR plaquettes of the buffer cubes, so
far curvature can sit on the straddling plaquettes between buffer cubes or between the buffer and the column (the LI-pw
mechanism). The form of node A's input actually consumed in §30 is weaker than any sup form: it is stated for the one weight
h^{R,1}_k of each pattern R, with a good buffer of radius ρ (§30.3 (E2^𝔉)). The general fine-unit buffer Buf^R_ρ of §30.3 with
ρ := 3L - 1 contains Buf_k(A). [Recommended by the reviewer, not adopted: relaxing N_r(𝒰_m) for r > 1 (Cor. LI-0 (c)); it
suppresses (CRC) uses but does not remove them.]

**Top-down analysis of (CRC) (U2 (c)).** **[RHW4-fix CR-2] Status: ARGUED (one paragraph, no displayed inequality chain), not a
written induction.** It re-introduces relaxed constraint patterns (R(𝔥) with relaxed columns) and prices animals under them, so
node A's inputs are needed uniformly over a pattern family (REVIEW_RLARGE_V3 S-4). Superseded on the (E2) route by §30 (Theorem
CRC-2T: one induction on the number of constrained pairs, the family named exactly). Order: k = K - 1 first ((CRC)_{K-1} is trivial: no level above), then k = K - 2, ….
Step for (CRC)_k: re-constrain the cubes of ∪_{m>k}π^{m-k}(B) ∩ S^{(m)} in level-ascending order (REL-seq's telescoping, steps
(1)-(4), PROVEN); a failing step at (m, y) contains an (n_♯ + 1)-animal 𝒟′ ∋ y of level-m defects (REL-seq step (2)); price it by
relaxing 𝒟′'s own column (R ⊂ R^{-𝒟′}: one factor (CRC)_m, m > k, available top-down) and Theorem HW^cap for 𝒟′ under the
column-relaxed law (all tilts case 0, Theorem LI^U-0 with the relaxed column as part of A_m) with node A's level-(m-1) inputs for
𝒟′'s columns. The step costs ≤ 6400^{n_♯}(C_ℓe^{…}e^{-au_m})^{n_♯+1}e^{(c_f + c_U)·(shadow of 𝒟′)} ≤ ε′-type, so c_U := 2ε′ (tiny,
depth-uniform: the shadow allowance of 𝒟′ is beaten by its own n_♯ + 1 prices, as in REL-boot (4)).
- Under (E1): nothing else enters; **(CRC)_k follows from (CRC)_{m}, m > k, by a written top-down induction.** [The
  induction's laws are R(𝔥) with finitely many relaxed columns above the current level; node A's (E1) must hold uniformly over
  this pattern family, which differs from R(𝔥) only above the level being integrated.]
- Under (E2) only: the level-(m-1) inputs for 𝒟′'s columns need (CRC)_{m-1} for far defects next to those columns. For
  m ≥ k + 2 this is (CRC) at a level > k (available). **For m = k + 1 it is (CRC)_k itself: the induction does not close.**

**Wall (CRC-1) [OPEN; exact residual of check (d) when node A delivers only (E2)].** The level-(k+1) step of (CRC)_k: a level-(k+1)
animal 𝒟′ through π(B) is priced with node A's level-k column inputs, which under (E2) need (CRC)_k for level-k far defects next to
𝒟′'s columns. The regress is SAME-level (k ↔ k + 1 ↔ k), each round adding one level-k far defect (price C_Ae^{-a_Au_k}) and one
level-(k+1) (n_♯ + 1)-animal (price ≤ ε′); it is a cluster expansion between returned level-k defects and coarse animals,
plausibly convergent [inference], not written. Not available: column induction (LOOP-const); a full-cone Chernoff from a fixed
level-k field (equipartition over L^{4(m-k)} links, HW_LOG session 1 item (3)); Theorem GS / Corollary PLD-G^S (free Gaussian,
unconditioned; EXISTENCE §14.2), whose non-abelian conditioned extension is EXISTENCE's open T14.

## 25. U3: check (d)

**Check (d) (REVIEW_RLARGE_V3 S-2), written.** For each level-k input of the HW route: the statements about levels > k it
consumes, the direction of its proof, and the verdict.
| input at level k | what about levels > k it consumes | direction | verdict |
|---|---|---|---|
| Lemma CH, CAP (i)-(iii), W-bad, TE (static) | none | pointwise | non-circular (proof given: §4, §14) |
| (CLS-min) ⇐ (REG-min) | none (static, cone-local) | — | non-circular |
| H4-red′ (mismatch peel) | h_{k+1} on int(𝒰_{k+1}): exactly constant (Thm LI^U-0) | top-down peel; no estimate on h | **non-circular, PROVEN** (c_k = 0) |
| TEL-f + CAP-dec | none (exact identity; pointwise expansion) | bottom-up telescoping | non-circular (proof given) |
| (SDP)^{A,far}, (SF-cap)^{A,far} at level k | h_k, exactly a function of U_k on L^far_k(𝔥) (Cor. LI-0 (b)); no (H-w′), HIST-sum, (RLF-3′) | node A bottom-up | **(E1): non-circular** (the statement quantifies over all far weights). **(E2): coarser information enters through (CRC)_k only; top-down induction closes for its levels ≥ k + 2 and stops at (CRC-1)** |
| REL-boot | (PH) for every admissible history (all levels), via a finite-torus fixed point | none (no induction over levels) | non-circular: M is finite a priori; consumes HW^cap, not (H-w′) or HIST-sum |
| HIST-sum + HS′ | (H-w′) at all levels (assembly) | assembly only | as before (§5, RLARGE §5.2) |
| (NA-∅) | none from HW | node A | unchanged (RLARGE row 10d) |
**Single entry point of coarser information on the HW route:** the factor h_k(U_k|_{L^far_k}) in the node-A column inputs. Under
(E1) check (d) is passed with no residual; under (E2) its residual is exactly (CRC-1). Nothing on the route consumes (H-w′),
HIST-sum or (RLF-3′) at levels > k.
**[RHW4-fix, check (d) CONFIRMED-WITH-FIX]** (1) With TF-1 the entry point on the (E1) route is h^{R(𝔥),F^{>k}}_k (coarser
spectators included), still far-only. (2) The "(E1): non-circular" verdict is logical only: (E1) is expected false in sup form
(E1-1). (3) REL-boot row: add "(PH) for every 𝔥′ ⇒ H6-H7 for every 𝔥′". (4) Session 5: the (E2) row's residual (CRC-1) is
replaced by Theorem CRC-2T (§30), whose own inputs are (E2^𝔉) (node A, uniformly over the column-relaxed family 𝔉_𝔥, with the
finer spectators inserted) and proven implications; its induction is over the finite number of constrained pairs of a pattern,
not over levels, and consumes no (H-w′), HIST-sum or (RLF-3′).

## 26. U4: Theorem HW, hypothesis list restated

**Theorem HW (session-4 form) ((H-w′) on the HW route): CONDITIONAL (implications PROVEN-HERE: Theorem HW^cap [HW-7] with
Cor. LI-0 (a) in place of (LI^F), Lemma TEL-f, Lemma CAP-dec, Lemma REL-boot [HW-10]).** For every admissible 𝔥, under (ref-a):
  Z(𝔥) ≤ Z(∅)·exp(B_0·s(𝔥))·Π_jΠ_{Q∈𝒰_j}C_ℓe^{-au_j},  a = θa_bad (θ lowered to a_A/a_bad if a_A < θa_bad),
  C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc, C_fc = c_sf + 81C_Ae^{θa_badR}, B_0 = c_f + 164ε′ + log(4/3),
given:
| # | hypothesis | law / form | owner | status |
|---|---|---|---|---|
| H1 | (F_R), g_K² ≤ 1/(2R) | chain's own sequence | FLOW (RLARGE row 1) | as RLARGE §4.2 row 1 |
| H2 | (CLS-min)_{c_pr,t_pr} ⇐ (REG-min) | static, cone-local | SQ (row 9) | OPEN, P |
| H3 | SU(2) (Lemma KS); SU(N ≥ 3): (KS-N) | kernel | HW (row 10e) | KS PROVEN; (KS-N) HYPOTHESIS, s |
| H4 | bad-only, history-independent defects | definition | — | scope (K15 / row 10f excluded) |
| H5 | max{6θ, 24θ}(1 + 2Rg_K²) < 1 | — | — | choice |
| H6 | **(SF-cap)^{A,far}_θ** at every level k (and the level-0 window moment) | ν^{(k),h_k}_k on history columns; sufficient: (E1) | node A | OPEN |
| H7 | **(SDP)^{A,far}_θ** at every level k, a_A ≥ θa_bad | the same | node A | OPEN, P |
| H8 | n_♯ ≥ n_H(a, B_0); r ≤ ½; 164ε′ ≤ 1 (g_K ≤ g_0(n_♯)) | arithmetic | — | choice |
| H9 | if only (E2) is delivered for H6-H7: (CRC)_k, i.e. the wall (CRC-1) | μ_{R(𝔥)} | HW | OPEN (§24.3) |
*[RHW4-fix SL-1: in H6-H7 the allowance is S's own ‖S‖_sh (Lemma SL), and B_0 is read with c_f := 81(c_A + c_sf′). H9 is not a
mere contingency: by E1-1, (E2) is the expected case, so (CRC) is in practice ON the route. Session 5 restates the list in §32.]*
**No longer hypotheses of the route:** (LI), (LI^F) (PROVEN, c = 0, Cor. LI-0 (a)); the future tilt on history columns (~~exact~~
[RHW4-fix LI0-1] it does not read the columns and enters only as a far weight, Cor.
LI-0 (b)); (REL) (Lemma REL-boot); (PRICE^ℛ) and the family ℛ_𝔥^↑ (not used); the per-level → joint step of (M-f^cap) (Lemma
TEL-f). **The proposed row 10g ((LI^U) as a pointwise ratio bound on arbitrary S) is not a hypothesis:** on relaxed columns it is
Theorem LI^U-0 (c_U = 0); on constrained columns it is false pointwise (Proposition LI-pw, ARGUED), and its averaged content is
(CRC), needed only under (E2) (H9) and by off-route consumers (RLARGE K8 / EXISTENCE's single-cube union bound).
Then (RLF-3′) by HIST-sum + HS′ as in RLARGE §5.2, and (RLF-4) via (NA-∅) (row 10d), unchanged.

## 27. Check w4 / w4b (criteria first: checks/w4_criteria.md 10:21:45 UTC, checks/w4b_criteria.md 10:38:40 UTC)
- **w4 (script checks/w4_footprint.py): OVERALL FAIL as pre-registered** (run 2, 10:35:28-10:35:56 UTC, 28.1 s, 77 MB): A and B
  PASS, C FAIL (d = 4: no constrained column sampled) and D FAIL (negative control never reached a constrained cube). Cause: its
  random histories relaxed almost every cube (a test-design flaw). Run 1 (10:23:23-10:33:57) was aborted by me (too slow).
- **w4b (checks/w4b_footprint.py; post-hoc redesign of the history generator and link sampler only, criteria unchanged and
  disclosed): OVERALL PASS** (run 2, lock 10:50:17-10:50:21 UTC, 3.8 s, 17 MB; run 1 aborted by me, generator loop without a
  cap). d = 2 (K = 5): A 1440 links, 0 exceptions; B 983 relaxed-column links, 0 constraint or spectator reads; C 297 constrained
  links, all read at level k + 1; D: the widened kernel reads a constrained cube or spectator for 19 of 40 relaxed links.
  d = 4 (K = 3): A 180 / 0; B 134 / 0; C 21 / all read; D 14 of 40.
- Scope: combinatorics of Lemma FP and Step 2 of Theorem LI^U-0 on random sparse histories ((A1) not imposed); nothing about the
  measure, Lemma NR, REL-boot or Proposition LI-pw. D shows the containment depends on the endpoint-block reading of HIST l.964.
- **[RHW4-fix P-2] Undisclosed parameter changes, disclosed.** "w4b changes ONLY the history generator and the link sampler"
  (here and in checks/w4b_criteria.md) is incomplete: `diff w4_footprint.py w4b_footprint.py` also shows **nhist 2 → 3 (d = 4),
  nlinks 25 → 30 (d = 4), and the D sample cap 25 → 40**. None can turn a FAIL of A or B into a PASS (those counts are exceptions,
  and they stayed 0). checks/w4b_criteria.md is not edited (frozen record); this line and HW_LOG session 5 carry the disclosure.
- **[RHW4-fix P-3] Scope.** Criterion **C is tautological** under the reading rule: a level-k link interior to x is read by every
  level-(k+1) link incident to the site x inside π(x), and at least d of the 2d incident links are interior to π(x) when L = 3, so C
  checks that the rule is coded, not that it is non-vacuous. In d = 4 the top torus has side 3, so N_1 of any nonempty set covers
  all of level K - 1 = 2; hence S^{(2)} = ∅, and B and D are informative there only at k = 0.

## 28. Outcomes against the session-4 targets (§20) (ADDED AFTER the derivations; pointers only)
- **U1: MET with a correction.** (LI^U) stated (§20); its content splits: relaxed influence columns, Theorem LI^U-0 (exact,
  c_U = 0, any spectators); constrained columns, the pointwise form is false (Proposition LI-pw, ARGUED) and the averaged content
  is (CRC). (LI), (LI^F) and the tilt are one family h^{R,F}_k (Lemma TILT).
- **U2: PARTIAL.** (a) MET (Lemma TILT). (b) MET (Lemma FP, NR, Theorem LI^U-0 [HW-9], Cor. LI-0: (LI), (LI^F) PROVEN with
  c_k = 0 under μ_{R(𝔥)}; tilt on history columns exactly far-only). (c) the pointwise statement refuted (ARGUED); top-down
  induction for (CRC) written; closes under node A's form (E1), stops at the named wall (CRC-1) under (E2). (d) MET: the HW route is
  re-arranged to consume only the relaxed case, by Lemma REL-boot [HW-10] (replaces REL-seq and the family ℛ_𝔥^↑). New finding
  J-1 (joint versus per-level fine moment) repaired by Lemma TEL-f.
- **U3: MET** (§25). Single entry point of coarser information: h_k on L^far_k in node A's column inputs.
- **U4: MET** (§26).
- **Check w4: FAIL (design); w4b: PASS** (§27).

**Session-4 tally (unreviewed).** Counted: **[HW-9]** Lemma FP with Theorem LI^U-0 (PROVEN-HERE); **[HW-10]** Lemma REL-boot
(CONDITIONAL ⇐ (PH); implication PROVEN-HERE). Total counted, all sessions: 6 + 2 = **8**. Uncounted: Lemma TILT, Lemma NR
(classical randomisation lemma), Corollary LI-0, Lemma TEL-f, Proposition LI-pw (ARGUED), Finding J-1. Status changes: (LI),
(LI^F): OPEN → PROVEN under μ_{R(𝔥)} (c = 0; SU(2) consequence (M-i) under μ_{R(𝔥)} PROVEN); (REL): discharged by REL-boot from
(PH); (PRICE^ℛ), ℛ_𝔥^↑, REL-seq, DECL: off the route; (SDP)^A, (SF-cap)^A → (SDP)^{A,far}, (SF-cap)^{A,far} [OPEN, node A];
new: (CRC) [OPEN, HW; only under (E2) and for off-route consumers], wall (CRC-1). No literature result is load-bearing
except the randomisation lemma of measure theory (Lemma NR). No edits outside HW.md, HW_LOG.md, checks/w4*.

---
# Session 5 of lane H (2026-10-28): [RHW4-fix], and (CRC-1) as a two-type polymer gas

REVIEW_HW_S4.md (md5 72c02d80…) is BINDING for this session (six binding fixes; TF-1; SL-1's slice bound, proven by the
reviewer; E1-1; E2-1; CR-1, CR-2; P-1, P-2, P-3).

## 29. Session-5 pre-stated targets (2026-10-28 11:12 UTC; statements only, written before any WRITTEN session-5 derivation;
key ideas reasoned before, see HW_LOG session 5)

### Target V1 (STEP 1): the [RHW4-fix] edits
Apply the six binding fixes of REVIEW_HW_S4 (SL-1, LI0-1, LP-1, CR-1/CR-2, E1-1/E2-1, P-1/P-2), each tagged [RHW4-fix], appended
or struck, not silently rewritten; adopt TF-1 (coarse-first TEL-f) with the reviewer's slice lemma (sh_m(S) ⊂ N_1(sh_m(𝒰_{k+1})),
Σ_k‖S_k‖_sh ≤ Σ_k|S_k| + 81s(𝔥)) recorded as PROVEN-BY-REVIEW (REVIEW_HW_S4 Priority 5), not as new work of this lane; define
(E2)'s buffer Buf_k(A) precisely; disclose the w4b sample-size changes; mark w4/w4b criterion C tautological.

### Target V2 (STEP 2): (CRC-1) as a two-type polymer gas
- (a) Write the same-level regress of (CRC-1) as a gas of two species: γ = (1, y), y a level-k cube in a far (constrained)
  column next to a history column ("far defect"); γ = (2, 𝒟), 𝒟 a *-connected set of n_♯ + 1 level-(k+1) cubes ("animal");
  with a stated compatibility relation (collar linking) and stated activities z(γ) ≥ 0, such that the ratio
  Z(R^{-B})/Z(R(𝔥)) of (CRC)_k (§23) is bounded by the gas's partition-function ratio, or by its polymer sum.
- (b) State a joint activity bound of the form z(1, y) ≤ ε_1^{gas} and z(2, 𝒟) ≤ ε_2^{gas}·e^{-…|𝒟|}, with every constant
  named, and prove convergence of the gas (log of its partition function, or the polymer sum through a fixed set) by a cluster
  expansion adapted from Theorem CE / CE-col (PROOF l.1946; SF §9.3): two species, collar linking, per-type decay; say exactly
  which steps of Theorem CE are used and which are not (the product-measure steps vs the abstract gas steps).
- (c) State the needed activity smallness as explicit inequalities, and check them against the recorded constants: Theorem CE /
  CE-col's κ_0, K_0, κ̃_0, K̃_0 (SF), the node-A price C_Ae^{-a_Au_k} (PLD §16.5), ε′ (§24.1), a_ret (PLD §16.8), n_♯, g_K.
- (d) Outcome: (CRC)_k PROVEN-HERE as an implication from named inputs (the inputs strictly smaller than (CRC)_k, each with
  owner), or the exact wall named (the inequality or representation step that fails, with the reason).
- Failure modes to watch: (V-F1) activities that are conditional probabilities under laws that themselves depend on the gas
  (circular activity); (V-F2) a depth factor e^{c(K-k)} per far defect that the per-type decay does not beat; (V-F3) a global,
  non-local factor (e^{c·s(𝔥)}) entering the ratio, as in the reviewer's direct REL-boot bound; (V-F4) a nonlinear bootstrap
  whose a-priori value is not in the contracting basin.

### Target V3 (STEP 3): Theorem HW's hypothesis list after V2
The complete hypothesis list of (H-w′) on the HW route after V1-V2: each item with law, form, owner and status.

### Check w5 (criteria first: checks/w5_criteria.md, then the script)
(i) Exact arithmetic (log space) of every activity inequality of V2 (c) at the recorded constants, with a negative control
(a parameter choice at which the inequality must fail). (ii) An exact small two-species hard-core toy gas (enumeration) testing
the convergence / ratio bound of V2 (b) against the exact partition functions, with a negative control (activities above the
stated threshold, where the bound must fail or the expansion must diverge). Informational, never a proof.

# Session-5 derivations (written after §29; STEP 1 edits [RHW4-fix] applied in place 11:24-11:29 UTC; typed from 11:30 UTC)

## 30. STEP 2: (CRC-1) as a two-type gas, and Theorem CRC-2T

Conventions as §20-§24; bad-only, history-independent defects; SU(2) (SU(N ≥ 3): (KS-N)); L ≥ 3 (numbers at L = 3), d = 4.
A level-j link's endpoints are level-j sites; its **endpoint cubes** are the level-j cubes (blocks) containing them (§22).

### 30.1 The column-relaxed family and Theorem LI^U-0′
- A set 𝒞 of (level, cube) pairs is **upward closed** if (m, x) ∈ 𝒞 ⇒ (m + 1, π(x)) ∈ 𝒞 (m + 1 ≤ K - 1). The **open column** of a
  level-i cube y is Col(y) := {(m, π^{m-i}(y)) : i < m ≤ K - 1}; its **closed column** is [y] := Col(y) ∪ {(i, y)}. For a set X of
  cubes of one level, Col(X), [X] are the unions. Both are upward closed.
- **𝔉_𝔥 := {R^{-𝒞} := R_{S(𝔥)∖𝒞} : 𝒞 finite and upward closed}** (§13.1 notation, no declarations: E = ∅). For R ∈ 𝔉_𝔥:
  R(𝔥) ⊂ R (m1), so **Z(R) ≥ Z(R(𝔥)) ≥ Z(∅) > 0**; N(R) := |S_R| (the number of constrained pairs) is finite (finite torus); for
  R = R^{-𝒞} and an upward-closed 𝒞′, R^{-𝒞′} := R_{S_R∖𝒞′} ∈ 𝔉_𝔥, ρ_R(𝒞′) := Z(R^{-𝒞′})/Z(R) ≥ 1, #_R(𝒞′) := |𝒞′ ∩ S_R|.
  For a set X of cubes write ρ_R(X) := ρ_R(Col(X)) (open) and ρ_R([X]) (closed). **(CRC)_k of §23 is ρ_{R(𝔥)}(B) ≤ e^{c_U#(B)}.**
- A level-j cube x is **R-free** if (m, π^{m-j}(x)) ∉ S_R for every m with j < m ≤ K - 1 (its open column is unconstrained). For
  R = R(𝔥) and π(x) ∈ A_{j+1}(𝔥), x is R-free (persistence, Step 1 of Theorem LI^U-0).
- With F_< ≥ 0 a fixed bounded weight that is a function of U_0, …, U_{k_0-1} (finer spectators; F_< ≡ 1 allowed), put
  Z^F(R) := ∫W·F_<·1_R, μ^F_R := WF_<1_R/Z^F(R), ρ^F_R(𝒞′) := Z^F(R^{-𝒞′})/Z^F(R). All relaxations below are at levels ≥ k_0 + 1.

**Theorem LI^U-0′ (exact future insensitivity on R-free cubes): PROVEN-HERE (counted with [HW-11] below; the proof of Theorem
LI^U-0 with one change).** Let R ∈ 𝔉_𝔥, k ≥ 0, A a set of level-k links all of whose endpoint cubes are R-free, and F a product of
bounded measurable spectators F_{Q″}, Q″ ∈ 𝒰_{m+1}, m ≥ k + 1, none of which reads a level-m link both of whose endpoint cubes
project into π^{m-k}(x) for an endpoint cube x of a link of A (in particular F ≡ 1). Then h^{R,F}_k(U) = h^{R,F}_k(U′) whenever U, U′
agree off A.
*Proof.* Lemmas FP and NR are statements about the kernels only and hold verbatim. Step 2 (constraints): 1_{R,m} reads U_m only on
links interior to cubes of S_R^{(m)}; by FP (ii) a footprint link interior to a level-m cube lies in π^{m-k}(x) for an endpoint cube
x, and (m, π^{m-k}(x)) ∉ S_R because x is R-free. Spectators: excluded by hypothesis (FP (iii)). Step 3 as before. ∎
(For R = R(𝔥) and π(x) ∈ A_{k+1}(𝔥), (A2) gives the spectator hypothesis for all history spectators: Theorem LI^U-0.) **This is
REVIEW_HW_S4's binding CR-1**: for R^{-B} the spectator step needs spectators off B's column, or F ≡ 1.

### 30.2 Two geometric lemmas
**Lemma SH-att (shadow of an attached cluster): PROVEN-HERE (elementary, not counted).** L ≥ 3, d = 4. Let P, Y be sets of
level-j cubes, ρ ≥ 1, such that every y ∈ Y is joined to P by a chain y = y_0, y_1, …, y_s ∈ P with y_0, …, y_{s-1} ∈ Y and
consecutive ℓ^∞ index distance ≤ ρ. With ‖X‖_sh := |X| + Σ_{r≥1}|sh_{j+r}(X)| (union form, levels ≤ K - 1):
  **‖P ∪ Y‖_sh ≤ 6561·‖P‖_sh + c_att(ρ)·|Y|,  c_att(ρ) := 1 + 2401·64·ρ = 1 + 153664ρ.**
*Proof.* sh_{j+r} commutes with unions (π and N_1 do). Choose for each y a parent at distance ≤ ρ along a chain (a forest whose
trees τ_i each contain one anchor z_i ∈ P and the cubes Y_i ⊂ Y, Σ|Y_i| = |Y|); join centres by segments (Euclidean length ≤ 2ρ in
d = 4): τ_i has length ℓ_i ≤ 2ρ|Y_i|. Scale level j + r boxes to unit cubes (HIST H-geo (ii)'s device): the scaled τ_i has length
ℓ_iL^{-r}. (a) If ℓ_iL^{-r} < 1, every point of τ_i is within Euclidean distance < 1 of the box of π^r(z_i), so π^r(Y_i) ⊂
N_1(π^r(z_i)); H-geo (i) (whose proof holds for any set) gives sh_{j+r}(Y_i) ⊂ N_3(π^r(Y_i)) ⊂ N_4(π^r(z_i)) ⊂ N_4(sh_{j+r}(P))
(π^r(P) ⊂ sh_{j+r}(P), since Σ(X) ⊇ π(X)). (b) If ℓ_iL^{-r} ≥ 1 (r ≤ r_i := ⌊log_Lℓ_i⌋), CE-geo′ (g1′) gives |π^r(Y_i)| ≤ 16 + 32ℓ_iL^{-r},
so |sh_{j+r}(Y_i)| ≤ 2401(16 + 32ℓ_iL^{-r}). Hence |sh_{j+r}(P ∪ Y)| ≤ 9⁴|sh_{j+r}(P)| + Σ_{i: r≤r_i}2401(16 + 32ℓ_iL^{-r}), and
Σ_{r≥1} of the second sum ≤ Σ_i2401(16r_i + 16ℓ_i) ≤ Σ_i2401·32ℓ_i ≤ 2401·64ρ|Y| (L ≥ 3; log_Lℓ ≤ ℓ for ℓ ≥ 1). The r = 0 term is
|P ∪ Y| ≤ |P| + |Y|. ∎
*Reading (per-type decay of species 1).* A far-defect cluster attached to P carries NO depth term of its own: its shadows merge
into P's after ≈ log_L(ρ|Y|) levels. A detached cube y carries 81 + 256(K - j - 2) (one 4⁴-block per level, L = 3), which is
what fails per cube (PLD §16.6 (b)); attachment is what removes it.

**Lemma COL (shadows of a column): PROVEN-BY-REVIEW + H-geo (not counted).** For a *-connected set 𝒟 of n level-m cubes and
col(𝒟) its 81n level-(m-1) descendants: ‖col 𝒟‖_sh ≤ 81n + 81(38417n + 38416(K - 1 - m)), and |[𝒟] ∩ S_R| ≤ 38417n + 38416(K - 1 - m).
*Proof.* Lemma SL (§24.3, with 𝒰_{k+1} ↔ 𝒟, sh_m(𝒟) := 𝒟) and H-geo (iv) with M = K - 1 - m; the closed column of 𝒟 is contained
in ∪_{r≥0}sh_{m+r}(𝒟) (π^r(𝒟) ⊂ sh_{m+r}(𝒟)). ∎

### 30.3 The node-A input, in the form the gas consumes
For R ∈ 𝔉_𝔥 and a set P of R-free level-j cubes, the **buffer** Buf^R_ρ(P) := {b level-j : b not R-free, dist_∞(b, P) ≤ ρ}. Fix
**ρ := 3L - 1** (= 8): then for A ⊂ 𝒰_{k+1}, R = R(𝔥), P = col(A), Buf^R_ρ(P) ⊇ Buf_k(A) of §24.3 (a cube y with
dist(π(y), A) ≤ 2 is within fine distance 2L ≤ ρ of col(A)).
**(E2^𝔉)_{θ,ρ} [OPEN; owner node A; replaces H6-H7 on the (E2) route].** There are C_fc, C_A, a_A ≥ θa_bad, c_A, independent of g,
K, T, 𝔥 and of the pattern, such that for every R ∈ 𝔉_𝔥 (every upward-closed relaxation at levels ≥ k_0 + 1), every level j ≥ k_0,
every finite set Γ of level-(j+1) cubes and every finite set Y of level-j cubes outside col(Γ) with col(Γ) ∪ Y R-free, with
ν := ν^{R,F}_j (the past law of levels ≤ j of R, with the finer spectators F_< inserted) and w := h^{R,1}_j (a function of U_j on the
links with a non-free endpoint cube, Theorem LI^U-0′):
  **E_{ν^w}[Π_{Q∈Γ}e^{θmin{π_Q,Y^f_Q}}·1{Y ⊂ D_j}·1{Buf^R_ρ(col Γ ∪ Y) ∩ D_j = ∅}] ≤ C_fc^{|Γ|}(C_Ae^{-a_Au_j})^{|Y|}e^{c_A‖col Γ ∪ Y‖_sh},**
and the level-0 clause with Π_{Q∈Γ}e^{θX_Q} for Γ a set of level-0 cubes (Wilson window moment), Y at level 0.
*What it is.* CAP-dec's combination of (SF-cap) and (SDP) (C_fc = c_sf + 81C_Ae^{θa_badR} as in §15) for an R-free patch with a
good buffer, under the past law of a column-relaxed pattern, weighted by that pattern's own far weight. Γ = A ⊂ 𝒰_{k+1}, Y = ∅,
R = R(𝔥), F_< the finer history spectators: the (E2) form of §24.3 (buffer now explicit). Two features, both named: it is asked
**uniformly over 𝔉_𝔥** (REVIEW_RLARGE_V3 S-4 / REVIEW_HW_S4 CR-2: the past law at level j feels relaxations at levels ≤ j), and
the allowance is the union-form ‖col Γ ∪ Y‖_sh of the WHOLE patch (a per-cube depth allowance on Y would not be affordable,
§30.2 Reading). It is weaker than any sup form: it is asked for the one weight w = h^{R,1}_j, and only on good buffers; node A's
natural proof route is still the screening statement of §24.3 (E2-1).

### 30.4 The two-type gas, and the theorem
**The gas (the regress of (CRC-1), written).** Polymers of two species, at levels ≥ k_0:
- species 1, **far defects**: level-j cubes y that are not R-free, y ∈ D_j, activity z_1(j) := C_Ae^{-a_Au_j}·e^{(c_A + c_U)c_att(ρ)};
- species 2, **animals**: (m, 𝒟), 𝒟 a *-connected set of n := n_♯ + 1 level-m cubes, m ≥ k_0 + 1, all of 𝒟 ⊂ D_m, activity
  z_2(m) := (2C_ℓe^{b_n}e^{-au_m})^{n}·e^{b_D(K-1-m)}, C_ℓ := (1 - λ_*)^{-3n_int/2}C_fc, a := θa_bad;
- **linking**: an animal (m, 𝒟) is linked to a relaxed pair (m, x) (or to a far defect y at level j < m) if x ∈ 𝒟 (resp. π^{m-j}(y) ∈ 𝒟)
  ("column linking": the animal is what a re-constrained column cube can fail by); a far defect y (level m - 1) is linked to an
  animal (m, 𝒟) if it is ρ-chained to col(𝒟) through far defects ("collar linking": the buffer of the animal's column);
- **per-type decay**: species 2 carries the depth term e^{b_D(K-1-m)} and beats it with its own n prices (condition (T) below);
  species 1 carries no depth term (Lemma SH-att), only the per-cube factor e^{(c_A+c_U)c_att}.
Constants: c_+ := c_A + c_U, **b_n := 531441·38418·c_+ + 38417c_U** (531441 = 6561·81), **b_D := 38416·(531441c_+ + c_U)**,
Δ_ρ := (2ρ + 1)⁴ - 1, **x_* := C_Ae^{a_AR + c_+c_att(ρ)}e^{-a_A/g_K²}**, **ε_2 := 6400^{n_♯}(2C_ℓe^{b_n + aR}e^{-a/g_K²})^{n_♯+1}.**
Activity smallness:
  **(S1)** Δ_ρ²·x_* ≤ ½;  **(S2)** ε_2 ≤ ½ and 2ε_2 ≤ c_U;  **(T)** (n_♯ + 1)·aβ_-log L ≥ b_D.

**Theorem CRC-2T ((CRC) for the column-relaxed family, from one node-A input): CONDITIONAL [HW-11] (implication PROVEN-HERE;
counted; unreviewed).** Assume (F_R) (lower half and u_{m} ≤ u_{m-1} + R) with g_K² ≤ 1/(2R), SU(2), bad-only history-independent
defects, (CLS-min), max{6θ, 24θ}(1 + 2Rg_K²) < 1, (E2^𝔉)_{θ,ρ} with ρ = 3L - 1, and (S1), (S2), (T) for some c_U ∈ (0, 1]. Then for
every admissible 𝔥, every R ∈ 𝔉_𝔥 and every upward-closed 𝒞′ of pairs at levels ≥ k_0 + 1 (in particular Col(B) for a set B of
level-k cubes, k ≥ k_0):
  **ρ^F_R(𝒞′) ≤ exp(2ε_2·#_R(𝒞′)) ≤ exp(c_U·#_R(𝒞′)).**
In particular **(CRC)_k holds with c_U := 2ε_2** (F ≡ 1, k_0 = k, R = R(𝔥)), uniformly in g ≤ g_0, K, T, 𝔥.
*Proof.* Induction on N(R) over all R ∈ 𝔉_𝔥 (fixed 𝔥, torus, K; the claim with the constant c_U). If #_R(𝒞′) = 0 then R^{-𝒞′} = R
and ρ = 1; this covers N(R) = 0. Let #_R(𝒞′) = N′ ≥ 1 and assume the claim for every pattern with fewer constrained pairs.
(1) *Telescoping, finest level first.* List 𝒞′ ∩ S_R as (m_1, x_1), …, (m_{N′}, x_{N′}) with m_1 ≤ m_2 ≤ …; R_0 := R^{-𝒞′} and R_t := R_{t-1}
with (m_t, x_t) re-constrained, so R_{N′} = R. The relaxed set of R_{t-1} is 𝒞 ∪ {(m_s, x_s) : s ≥ t}, upward closed (the remaining
pairs are the coarser part of 𝒞′), so R_{t-1} ∈ 𝔉_𝔥 and **N(R_{t-1}) ≤ N(R) - 1**. Then
  ρ^F_R(𝒞′) = Π_t Z^F(R_{t-1})/Z^F(R_t) = Π_t[1 - p_t]^{-1},  p_t := μ^F_{R_{t-1}}(R_{t-1}∖R_t).
(2) *Step event (REL-seq step (2), verbatim with no declarations).* R_{t-1}∖R_t ⊂ ∪_{𝒟}{𝒟 ⊂ D_{m_t}}, the union over *-connected
𝒟 ∋ x_t of n cubes (≤ 6400^{n_♯} of them, (g3)): some *-component C of D_{m_t} ∩ S^{(m_t)}_{R_t} has > n_♯ cubes; if x_t ∉ C then C is a
*-connected set of > n_♯ defects in S^{(m_t)}_{R_{t-1}}, contradicting R_{t-1}; so x_t ∈ C ∩ D_{m_t}, and C contains such a 𝒟.
(3) *Relax the animal's closed column.* With m := m_t and R′ := R_{t-1}^{-[𝒟]} ∈ 𝔉_𝔥: 1_{R_{t-1}} ≤ 1_{R′}, so
  μ^F_{R_{t-1}}(𝒟 ⊂ D_m) ≤ ρ^F_{R_{t-1}}([𝒟])·μ^F_{R′}(𝒟 ⊂ D_m) ≤ e^{c_U(38417n + 38416(K-1-m))}μ^F_{R′}(𝒟 ⊂ D_m)
by the induction hypothesis for R_{t-1} and Lemma COL. In R′, every cube of 𝒟 is unconstrained at levels ≥ m.
(4) *Decompose by the attached far-defect cluster.* For a configuration let Y(c) be the set of level-(m-1) cubes that are not
R′-free, are in D_{m-1}, and are joined to col(𝒟) by a ρ-chain of such cubes. On {Y(c) = Y}: Y ⊂ D_{m-1}, and every non-R′-free
b ∉ Y within distance ρ of col(𝒟) ∪ Y is not in D_{m-1}. In R′′ := R′^{-Col(Y)} ∈ 𝔉_𝔥, col(𝒟) ∪ Y is R′′-free and the non-R′′-free
cubes are among the non-R′-free ones, so {Y(c) = Y} ⊂ E_Y := {Y ⊂ D_{m-1}} ∩ {Buf^{R″}_ρ(col 𝒟 ∪ Y) ∩ D_{m-1} = ∅}, a function of U_{m-1}.
With 1_{R′} ≤ 1_{R″} and the induction hypothesis for R′ (N(R′) < N(R)):
  μ^F_{R′}(𝒟 ⊂ D_m) ≤ Σ_Y ρ^F_{R′}(Col(Y))·μ^F_{R″}({𝒟 ⊂ D_m} ∩ E_Y) ≤ Σ_Y e^{c_U‖col 𝒟 ∪ Y‖_sh}·μ^F_{R″}({𝒟 ⊂ D_m} ∩ E_Y)
(#_{R′}(Col(Y)) ≤ Σ_{r≥1}|π^r(Y)| ≤ ‖col 𝒟 ∪ Y‖_sh). The term Y = ∅ has ρ = 1.
(5) *Price the animal (Theorem HW^cap at one level, under μ^F_{R″}).* Lemma CH with Lemma CAP (ii)-(iii) (π_Q := a_badu_m; W-bad ⇐
(CLS-min)): 1{𝒟 ⊂ D_m} ≤ Π_{Q∈𝒟}e^{-θπ_Q}e^{θY^mis_Q}e^{θmin{π_Q,Y^f_Q}} pointwise. The mismatch peel (H4-red′'s step, one level):
under μ^F_{R″} the links V of int 𝒟 at level m enter only through K_{m-1} (independent links given U_{m-1}), 1_{R″,m} (which does not
read them: 𝒟 is unconstrained at level m in R″), and h^{R″,1}_m (which does not depend on them: Theorem LI^U-0′ at level m, every
cube of 𝒟 being R″-free, F ≡ 1); F_< and 1_{E_Y} read levels ≤ m - 1. Lemma KS (c): ∫Π_{c∈int𝒟}e^{λ_cκu_{m-1}φ_c}k_c dV ≤
(1 - λ_*)^{-3n_int|𝒟|/2} (λ_c = 6θu_m/u_{m-1} ≤ λ_*). Then Lemma TILT (ii) at level m - 1 (finer spectators in ν) and (E2^𝔉) with
Γ = 𝒟, j = m - 1, R = R″:
  μ^F_{R″}({𝒟 ⊂ D_m} ∩ E_Y) ≤ (C_ℓe^{-au_m})^{n}·(C_Ae^{-a_Au_{m-1}})^{|Y|}e^{c_A‖col 𝒟 ∪ Y‖_sh}.
(6) *Sum over Y.* By Lemma SH-att with P = col(𝒟) and Lemma COL,
  c_+‖col 𝒟 ∪ Y‖_sh ≤ c_+[531441(38418n + 38416(K - 1 - m))] + c_+c_att|Y|,
so with x := C_Ae^{-a_Au_{m-1}}e^{c_+c_att} ≤ x_* (u_{m-1} ≥ u_K - R): Σ_Y x^{|Y|} ≤ Π_{b∈N_ρ(col𝒟)}(1 + Σ_{Y′∋b}x^{|Y′|}) (assign each
ρ-component of Y one of its cubes within ρ of col(𝒟); distinct components get distinct cubes) ≤ exp(|N_ρ(col 𝒟)|·x/(1 - Δ_ρ²x))
(≤ Δ_ρ^{2(s-1)} ρ-connected sets of s cubes through b: (g3)'s walk encoding with degree Δ_ρ) ≤ exp(2·81(2ρ + 1)⁴n·x) ≤ 2^n, using (S1)
(Δ_ρ²x ≤ ½, and 162(2ρ + 1)⁴x ≤ Δ_ρ²x·162(2ρ + 1)⁴/Δ_ρ² ≤ log 2). Collecting (3)-(6):
  μ^F_{R_{t-1}}(𝒟 ⊂ D_m) ≤ (2C_ℓe^{b_n}e^{-au_m})^{n}e^{b_D(K-1-m)} = z_2(m).
(7) *Per-type decay of species 2.* (F_R): u_m ≥ u_K + β_-(K - m)log L - R. So
  p_t ≤ 6400^{n_♯}(2C_ℓe^{b_n + aR}e^{-au_K})^{n}·e^{(K-m)[b_D - naβ_-log L]} ≤ ε_2  by (T) (K - m ≥ 1, u_K = 1/g_K²).
(8) *Close.* By (S2), p_t ≤ ½ and -log(1 - p) ≤ 2p, so ρ^F_R(𝒞′) ≤ e^{2ε_2N′} ≤ e^{c_U#_R(𝒞′)}. ∎
*Why this is not REVIEW_HW_S4's nonlinear bootstrap (V-F4).* The induction is over the FINITE number N(R) of constrained pairs:
every inner use of the hypothesis is for a pattern with strictly fewer constrained pairs (the step relaxes the current pair; (3)
and (4) relax more), so no a-priori value of a supremum is needed and the closing condition 2ε_2 ≤ c_U is a fixed inequality on
constants, checked once. The family is closed under the operations used because every relaxation is upward closed and the
telescoping is finest-first. *V-F1 (circular activities):* the activities are bounded by (E2^𝔉), stated for all of 𝔉_𝔥, not by
laws depending on the gas. *V-F2 (depth per far defect):* removed by attachment (SH-att) and the union-form allowance. *V-F3
(global factor):* none; every factor is local to the animal's column and its attached cluster.
*Relation to Theorem CE / CE-col.* Theorem CE's Steps 1-2 (Mayer expansion; integration against a product measure) have no
analogue here: there is no product structure and no polymer representation of 1_R. They are replaced by the exact relaxation
inequality 1_R ≤ 1_{R^{-𝒞}}, the telescoping identity, Theorem LI^U-0′ and the node-A input. What is kept is the abstract part: a
gas of linked polymers with per-type decay whose rooted linked trees are summed from the leaves inward; here the leaf summation
is the induction (steps (3)-(6) are one generation: an animal's column spawns animals, its collar spawns far defects), i.e. the
inductive (Kotecký–Preiss-type) form of the convergence [the KP name is cited for orientation only; nothing of it is used beyond
what is written]. No exponentiated expansion exp(ΣH#) is claimed; (CRC) needs only the ratio. Theorem CE's activity condition
(decay κ > 3κ_0 + 3 ≈ 457 per unit tree length, amplitude ≤ c_0(κ) ∝ e^{-2κ}; CE-col: κ > κ_0 + 2κ̃_0 + 3 ≈ 588) would, transcribed
per cube, ask a/g_K² - b_n - log(12800C_ℓ) ≥ 457-588 — weaker than (S2)'s requirement a/g_K² > b_n + log(12800C_ℓ) + aR only by these
additive constants, which b_n ≈ 2·10¹⁰c_+ dwarfs. So the certified CE / CE-col constants are not binding; b_n is.

### 30.5 Consumption on the HW route, and what it costs
**Corollary CRC-HW ((M-f^cap) on the (E2) route): CONDITIONAL (implication PROVEN-HERE; not counted separately).** Use TEL-f in the
FINER-first order (§24.2): E_μ[Π_kΦ_k] = Π_kE_{μ^{(k)}}[Φ_k], μ^{(k)} = μ_{R(𝔥)} tilted by F_< := Π_{k′<k}Φ_{k′} (levels < k; Φ_{-1}
reads U_0). By TILT (ii), E_{μ^{(k)}}[Φ_k] = E_ν[Φ_kh]/E_ν[h], ν := ν^{R(𝔥),F}_k, h := h^{R(𝔥),1}_k. Decompose by the cluster Y attached
to P := col(𝒰_{k+1}) (as in step (4), relative to R(𝔥) at level k): h^{R(𝔥)}_k ≤ h^{R(𝔥)^{-Col(Y)}}_k pointwise and
E_ν[h^{R(𝔥)^{-Col Y}}_k]/E_ν[h^{R(𝔥)}_k] = ρ^F_{R(𝔥)}(Col(Y)) (the past constraints coincide), so with Theorem CRC-2T (k_0 = k) and
(E2^𝔉) (Γ = 𝒰_{k+1}, R = R(𝔥)^{-Col Y}):
  E_{μ^{(k)}}[Φ_k] ≤ Σ_Y e^{c_U‖P∪Y‖_sh}C_fc^{|𝒰_{k+1}|}(C_Ae^{-a_Au_k})^{|Y|}e^{c_A‖P∪Y‖_sh} ≤ (2C_fc)^{|𝒰_{k+1}|}·e^{6561c_+‖col 𝒰_{k+1}‖_sh}
(SH-att; the Y-sum as in step (6), |N_ρ(P)| ≤ 81(2ρ + 1)⁴|𝒰_{k+1}|, (S1)). By Lemma SL, Σ_k‖col 𝒰_{k+1}‖_sh ≤ 81Σ_k|𝒰_{k+1}| + 81s(𝔥), so
  **(M-f^cap) under μ_{R(𝔥)} holds with C_fc′ := 2C_fc·e^{531441c_+} and c_f := 531441·c_+**, c_+ = c_A + c_U (c_U := 2ε_2 ≤ 1).
*Why the finer-first order here (the TF-1 caveat).* In coarse-first order the weight inside the partition functions is
F^{>k} = Π_{k′>k}Φ_{k′}, and a level-m animal (m ≥ k + 1) can lie in the level-m column of a history cube Q ∈ 𝒰_{m+1} (those columns
are constrained in R(𝔥): A_m(𝔥) does not contain them); Φ_m reads U_m on that column, i.e. int 𝒟, and step (5)'s peel fails. In
finer-first order every spectator in Z^F reads a level < k ≤ m - 1. So TF-1 stays the order of record for the (E1) form, and the
(E2) route uses the finer-first order; node A's (E2^𝔉) is then asked with the finer spectators inserted in its past law (which
is the law HW §24.2 originally wrote, ν^{(k)}_k, now extended to 𝔉_𝔥).

### 30.6 STEP 2 (c): the activity smallness against the recorded constants (arithmetic; check w5 A)
Recorded inputs (quoted, not re-derived): a = θa_bad ≲ 1.0·10⁻⁸⁶, a_bad ≈ 2.5·10⁻⁸⁵, β_- ≈ 0.186 at N = 2 (RLARGE l.612); L = 3;
a_ret ≈ 2.0·10⁻⁹¹ at ε_1 = 6.7·10⁻⁴⁰ and the (RLF-δ) ceiling g_K² ≲ 10⁻⁹⁴ (PLD §16.8); n_H ≳ 2·10⁸⁷ (RLARGE l.612); Theorem CE /
CE-col constants κ_0 ≈ 151.3, κ̃_0 ≈ 217.05 (PROOF l.1953, SF §9.3). Node A's C_fc, C_A, c_A are NOT certified (PLD §16.7: c_lcr not
certified), so they stay symbolic; the arithmetic below is in c_+ = c_A + c_U and log C.
- **(S2) is the binding inequality.** For n_♯ large it holds iff a/g_K² > b_n + aR + log(12800C_ℓ), i.e.
  **g_K² < g²_CRC := a/(b_n + aR + log(12800C_ℓ)) ≈ 1.0·10⁻⁸⁶/(2.04·10¹⁰c_+) ≈ 4.9·10⁻⁹⁷/c_+** (w5 A1 computes it exactly).
  This is BELOW the recorded (RLF-δ) ceiling 10⁻⁹⁴ and the n_H ceiling 2.7·10⁻⁹¹ by a factor ≳ 2·10², times c_+. At the recorded
  g_K² ≈ 10⁻⁹⁴, a/g_K² ≈ 10⁸ < b_n: **(S2) FAILS there** (w5 A3, the negative control). It is a g-independent ceiling, so the
  theorem applies with g_0 lowered; nothing is circular (order below).
- **(T)**: n_♯ + 1 ≥ b_D/(aβ_-log L) ≈ 2.04·10¹⁰c_+/(2.0·10⁻⁸⁷) ≈ 1.0·10⁹⁷·c_+, against n_H ≳ 2·10⁸⁷: **n_♯ grows by ≈ 10¹⁰.**
- **(S1)** holds once a_A/g_K² ≥ a/g_K² exceeds log(2Δ_ρ²C_A) + a_AR + c_+c_att (Δ_ρ² ≈ 7.0·10⁹, c_att(8) = 1229313): implied by (S2)
  whenever log C_A ≤ log C_ℓ + 2·10¹⁰c_+ (b_n ≫ c_att c_+). If node A instead prices far defects at the returned rate a_ret (not
  the route of PLD §16.5, recorded for comparison): (S1) needs g_K² < a_ret/(c_+c_att + log(2Δ_ρ²C_A)) ≈ 1.6·10⁻⁹⁷/c_+, the same
  order as g²_CRC. **a_ret does not enter (S2) or (T).**
- **Order of constants (non-circular):** node A's C_fc, C_A, a_A, c_A → c_U := 1 (any value in (0, 1]) → b_n, b_D, c_att, C_ℓ →
  n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)} → g_0 with g_K² < g²_CRC, (S1), (S2), and REL-boot's r ≤ ½, 164ε′ ≤ 1 → then
  c_U^{out} = 2ε_2 (→ 0 as g_K → 0) is what enters c_+ in Corollary CRC-HW. (c_U^{in} = 1 inflates b_n only through c_+ ≤ c_A + 1.)
- **The size of b_n** is pure geometry × allowance: 6561 (SH-att's N_4) × 81 (column) × 38418 (H-geo (iv)) per unit of c_+. It is
  a constant, so it costs a lower g_0 and a larger n_♯, not uniformity. A sharper SH-att or column bound lowers it; not needed.

### 30.7 The exact residual (wall) after Theorem CRC-2T
The same-level regress (CRC-1) is resolved as an implication: Theorem CRC-2T treats level-k far defects and level-(k+1)
animals (and all coarser levels) in ONE induction. What remains is exactly:
- **(W-𝔉) [node A]: (E2^𝔉)_{θ,ρ}**, i.e. CAP-dec's combination for an R-free patch with a good ρ-buffer, under the past law of
  every pattern of 𝔉_𝔥 (with finer history spectators inserted), weighted by the pattern's own far weight, with a union-form
  allowance on the whole patch. Its content is screening by a good buffer (E2-1), now for the one weight h^{R,1}_j and uniformly
  over upward-closed column relaxations. [inference] Relaxation of columns at levels ≤ j changes the past law only by allowing
  larger defect components inside the relaxed columns at finer levels; whether node A's proof (FT + KD + CW + (SF-cap) + (J-NS),
  PLD §16.5) is uniform over such patterns is a node-A question; nothing in HW decides it.
- Nothing else new: (CLS-min) (H2), (F_R) (H1), SU(2) / (KS-N) (H3) as before.

## 31. Check w5 (criteria first: checks/w5_criteria.md 11:32:52 UTC, one pre-script wording edit of B3; script checks/w5_crc2t.py
11:33:48 UTC; records checks/w5_out.txt, checks/w5_time.txt)
- One run under the numeric lock (acquired 11:34:05, released 11:34:07 by one rmdir); load 2.54; nice 10; BLAS threads 1; 1.7 s;
  44 MB peak RSS; exit 0; no process left. **OVERALL PASS (A1-A5, B1-B3, C1-C3).**
- A (arithmetic, 50-digit): g²_CRC·c_+ = 4.898·10⁻⁹⁷ at every scanned (c_A, C_ℓ, R) (A1); at g²_CRC/2, log ε_2 < log ½ and (S1) holds
  (A2); **at the recorded g_K² = 10⁻⁹⁴, (S2) fails at every scanned point** (A3, negative control: log ε_2 ≈ +2·10¹⁰⁷); n_T/c_+ =
  9.99·10⁹⁶ (A4); g²_ret·c_+ = 1.63·10⁻⁹⁷ (A5). b_n(c_A = 0) = 20416938755, b_D(c_A = 0) = 20415875872, c_att(8) = 1229313,
  Δ_ρ² = 6.98·10⁹.
- B (Lemma SH-att, exact shadows on Z⁴, L = 3, ρ = 8, M = 10, 160 samples): 0 violations of the lemma (B1) and of the sharper
  excess form (B2); the largest observed excess per Y-cube is 193, against c_att = 1229313 (the lemma's constant is loose by
  ≈ 6·10³; informational). B3 (negative control): a detached cube's excess is 1106 at M = 5 and 2386 at M = 10, i.e. it grows by
  256 per level, the per-cube depth term that attachment removes.
- C (two-level monotone toy, 27 grid points, exact enumeration of 2¹²·3⁴ configurations): the step containment has 0
  exceptions over the 5222 configurations of R^{-B}∖R (C1); the two-species bound ρ ≤ 1/(1 - 2z²) holds everywhere (C2); with the
  finer-defect contribution dropped (z_0 = q) it is violated at 18 of 27 points (C3, negative control: the collar link between the
  species is load-bearing).
- Scope: A is arithmetic of §30.6 (symbolic node-A constants scanned, not known); B tests Lemma SH-att only; C is a monotone toy in
  which Harris' inequality replaces node A and the induction, so it tests the step containment and the two-species activity
  formula, not Theorem CRC-2T's induction or (E2^𝔉). Nothing about the measure of the YM chain.

## 32. STEP 3: Theorem HW, hypothesis list after (CRC-1)

**Theorem HW (session-5 form) ((H-w′) on the HW route): CONDITIONAL (implications PROVEN-HERE: Theorem HW^cap [HW-7] with Cor.
LI-0 (a), Lemma TEL-f, Corollary CRC-HW ⇐ Theorem CRC-2T [HW-11], Lemma REL-boot [HW-10]).** For every admissible 𝔥, under (ref-a):
  Z(𝔥) ≤ Z(∅)·exp(B_0·s(𝔥))·Π_jΠ_{Q∈𝒰_j}C_ℓe^{-au_j},  a = θa_bad (θ lowered to a_A/a_bad if a_A < θa_bad),
  C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc′,  C_fc′ = 2C_fc·e^{531441c_+},  c_f = 531441·c_+,  c_+ = c_A + 2ε_2,  B_0 = c_f + 164ε′ + log(4/3),
given (route of record: (E2)):
| # | hypothesis | law / form | owner | status |
|---|---|---|---|---|
| H1 | (F_R), g_K² ≤ 1/(2R) | chain's own sequence | FLOW (RLARGE row 1) | as RLARGE §4.2 row 1 |
| H2 | (CLS-min)_{c_pr,t_pr} ⇐ (REG-min) | static, cone-local | SQ (row 9) | OPEN, P |
| H3 | SU(2) (Lemma KS); SU(N ≥ 3): (KS-N) | kernel | HW (row 10e) | KS PROVEN; (KS-N) HYPOTHESIS, s |
| H4 | bad-only, history-independent defects | definition | — | scope (K15 / row 10f excluded) |
| H5 | max{6θ, 24θ}(1 + 2Rg_K²) < 1 | — | — | choice |
| H6′ | **(E2^𝔉)_{θ,ρ}**, ρ = 3L - 1 (§30.3): CAP-dec's combination for an R-free patch col(Γ) ∪ Y with a good ρ-buffer, union-form allowance e^{c_A‖col Γ ∪ Y‖_sh}, at every level j, and the level-0 window clause | past law ν^{R,F}_j of every R ∈ 𝔉_𝔥 (finer history spectators inserted), weighted by h^{R,1}_j | node A | **OPEN** (replaces H6-H7; content: screening by a good buffer, uniformly over 𝔉_𝔥) |
| H8′ | n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L) - 1}; (S1); (S2) (g_K² < g²_CRC ≈ 4.9·10⁻⁹⁷/c_+ at the recorded a); REL-boot's r ≤ ½, 164ε′ ≤ 1 | arithmetic | — | choice (g_K ≤ g_0) |
| ~~H9~~ | ~~(CRC)_k, the wall (CRC-1)~~ | — | HW | **discharged as an implication**: Theorem CRC-2T [HW-11] ⇐ H1-H5, H6′, H8′ |
**Alternative (E1) route (coarse-first TF-1):** H6-H7 of §26 in the (E1) form under the plain past law with the far weight
h^{R(𝔥),F^{>k}}_k, allowance ‖S‖_sh (SL-1), no (CRC) needed; **expected false in sup form (E1-1)**, kept as a logically sufficient
alternative only.
**No longer hypotheses of the route:** (LI), (LI^F) (Cor. LI-0 (a)); the future tilt on history and R-free columns (Theorems LI^U-0,
LI^U-0′: it does not read them, it enters as a far weight); (REL) (REL-boot); (PRICE^ℛ), ℛ_𝔥^↑ (not used); the per-level → joint
step (TEL-f); **(CRC) and the same-level regress (CRC-1) (Theorem CRC-2T).** Then (RLF-3′) by HIST-sum + HS′ as in RLARGE §5.2, and
(RLF-4) via (NA-∅) (row 10d), unchanged.
**Constants against the record (§30.6, w5 A).** The (E2) route lowers the coupling ceiling to g_K² ≲ 4.9·10⁻⁹⁷/c_+ (below the
recorded (RLF-δ) ceiling 10⁻⁹⁴ and n_H ceiling 2.7·10⁻⁹¹) and raises n_♯ to ≳ 10⁹⁷c_+; REL-boot's r ≤ ½ with B_* = c_f + 1 =
531441c_+ + 1 gives the same order of ceiling (38417B_* ≈ 2.04·10¹⁰c_+), and n_H(a, B_0) the same order of n_♯. All are
g-independent. a_ret does not enter (S2) or (T).

## 33. Outcomes against the session-5 targets (§29) (ADDED AFTER the derivations; pointers only)
- **V1: MET.** SL-1 (§24.3 with Lemma SL recorded PROVEN-BY-REVIEW, c_f := 81(c_A + c_sf′)), LI0-1 (§22, §26), LP-1 (§23), CR-1
  (§23 → Theorem LI^U-0′, §30.1), CR-2 (§24.1, §24.3: top-down analysis ARGUED), E1-1 and E2-1 (§24.3: (E1) expected false in sup form;
  Buf_k(A) defined; screening named as (E2)'s content, with a session-5 doubt [inference]), P-1 (§20, §20's derivation header),
  P-2 and P-3 (§27); TF-1 adopted (§24.2) with the caveat that the (E2) route uses the finer-first order (§30.5); RB-1, the (LI^F) /
  A4 status pointer, the §22 nit; check (d) fixes (§25).
- **V2: MET as an implication.** (a) The gas written (§30.4: far defects, animals, column and collar linking, per-type decay). (b)
  **Theorem CRC-2T [HW-11]: (CRC) for every column-relaxed pattern, CONDITIONAL ⇐ (E2^𝔉)**, by one induction over the finite number of
  constrained pairs (not a nonlinear bootstrap); Theorem CE's Steps 1-2 are not used (no product measure), its tree/leaf
  summation appears in inductive form. (c) Activity smallness (S1), (S2), (T) explicit; the binding inequality is (S2), g_K² <
  g²_CRC ≈ 4.9·10⁻⁹⁷/c_+, which FAILS at the recorded ceiling 10⁻⁹⁴ and needs g_0 lowered; CE / CE-col constants not binding; a_ret
  not entering (w5 A). (d) **Exact residual: (E2^𝔉)** (node A, uniformly over 𝔉_𝔥, union-form allowance, good ρ-buffer).
- **V3: MET** (§32).
- **Check w5: OVERALL PASS** (§31).

**Session-5 tally (unreviewed).** Counted: **[HW-11]** Theorem CRC-2T with Theorem LI^U-0′ (implication PROVEN-HERE; CONDITIONAL
⇐ (E2^𝔉)). Total counted, all sessions: 8 + 1 = **9**. Uncounted: Lemma SH-att, Lemma COL, Lemma SL (PROVEN-BY-REVIEW), Corollary
CRC-HW, the TF-1 caveat (§30.5). Status changes: (CRC) / wall (CRC-1): OPEN → CONDITIONAL ⇐ (E2^𝔉) (implication proven); H6-H7 on
the (E2) route → H6′ = (E2^𝔉) [OPEN, node A]; (E1): expected false in sup form [inference]; constants: g_0 lowered to
g_K² ≲ 4.9·10⁻⁹⁷/c_+, n_♯ ≳ 10⁹⁷c_+. No literature result is load-bearing beyond Lemma NR's randomisation lemma and Harris'
inequality inside the toy check (not in any proof). No edits outside HW.md, HW_LOG.md, checks/w5*.

---
# Session 6 of lane H (2026-10-28): the ×6561, restated CRC-2T, and (E2^𝔉) renegotiated

REVIEW_HW_S5.md is **BINDING** for this session (11 binding fixes [RHW5-fix CST-1, CST-2, CST-3, SH-1, E2-2, TF-2, GAS-1,
SYM-1, W5-1, SC-1, NIT]). This session is APPEND-ONLY: it alters no line of §0-§33. Every fix therefore appears below as an
**erratum entry** naming the line it corrects and stating the correction; the corrected text itself stays where it is.

## 34. Session-6 pre-stated targets (2026-10-28 12:53 UTC; FIRST edit of the session; statements only, written before any
session-6 derivation and citing nothing produced in session 6)

### Target W1 (STEP 1, the main effort): remove or reduce the multiplicative factor in Lemma SH-att
REVIEW_HW_S5 (S5-12, S5-14) localises the whole session-5 tightening of the coupling ceiling in ONE number: the ×6561 that
Lemma SH-att's N_4 step (l.1506-1508) puts into c_f = 6561·81·c_+ = 531441c_+ and hence into b_n, b_D, B_*, B_0.
- (a) Verify the reviewer's free one-line gain (sh_{j+r}(P) ⊇ N_1(π^r(P)) ⇒ N_3 for N_4, i.e. 2401 for 6561) and take it.
- (b) Decide the reviewer's conjecture that the multiplicative factor is **removable altogether**, i.e. whether
  ‖P ∪ Y‖_sh ≤ ‖P‖_sh + c(ρ)|Y| holds with c independent of K. PROVE it or REFUTE it with an explicit configuration.
  The reviewer's evidence is B2 (0 violations, max excess 193/Y-cube) plus re-runs at M = 20/40/80 and an adversarial
  sampler (max 257.25), all depth-stable; the missing lemma the reviewer names is
  "π^r(Y) ⊂ N_1(π^r(P)) ⇒ Σ^{r+c}(P ∪ Y) = Σ^{r+c}(P) for a fixed c".
- (c) Whichever way (b) goes, state and prove the best constant obtainable, as a lemma with a complete proof, and give the
  resulting g²_CRC, n_T and the comparison against the recorded (RLF-δ) ceiling and against REL-boot / HIST-sum / n_H.
- (d) Report the breach honestly in both directions: per REVIEW_HW_S5 S5-13 the binding programme ceiling is
  g_0² ≈ 2.5·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 l.335, RLARGE l.618, REVIEW_RLARGE_V3 l.61 "It still does not bind against DX′"), so
  session 5's "the smallness condition fails ⇒ lower g_0" is an over-reaction; HANDOFF's instruction to lower g_0 and
  recheck the SF thresholds is to be withdrawn in FOR OTHER FILES.
- Failure modes to watch: (W-F1) a "sharpening" that silently changes the hypothesis of SH-att (the chain/attachment
  condition) so that step (6) of Theorem CRC-2T can no longer apply it; (W-F2) an improvement proved only for a single
  anchor and then used for a union over trees; (W-F3) a constant improved in HW while the SAME geometric constant is left
  unsharpened in HIST/REL-boot, so that the binding inequality merely moves to another lane's copy of it; (W-F4) a
  per-level gain that is multiplied by the number of levels and so reintroduces a depth term.

### Target W2 (STEP 2): claim the right theorem — restate Theorem CRC-2T as what it is
Per S5-8/GAS-1: §30.4's "two-type gas" is a bestiary (no partition function, no compatibility relation, no Mayer identity,
no Kotecký-Preiss criterion) and §29's Target V2 (a) ("bounded by the gas's partition-function ratio, or by its polymer
sum") is NOT delivered. Restate Theorem CRC-2T, without weakening it, as an **induction on the finite number N(R) = |S_R|
of constrained pairs** with the telescoping exact and step (4)'s event algebra proven, i.e. as the thing that closes the
m = k+1 step REVIEW_HW_S4 said could not close; drop the gas framing and record V2 (a) as not delivered.

### Target W3 (STEP 3): hand (E2^𝔉) back in the shape node A can owe
Per S5-16/E2-2 and S5-19/TF-2, (E2^𝔉) as stated at l.1524-1530 is strictly stronger than what node A owes, in three
undeclared ways: the allowance currency (PLD gives the slice s_k(𝔥) at PLD l.1856 or ‖S‖_sh at PLD l.1408; (E2^𝔉) wants the
union form over the attached patch); the level range (PLD l.1905 covers k ≥ 2 only, (LCR)_0 OPEN) against (E2^𝔉)'s level-0
clause, which is itself mis-levelled; and F_< as a free unquantified symbol. Restate (E2^𝔉) asking node A only for what
node A can owe: quantify F_<, fix the level-0 clause, declare the deltas, and either justify switching TF-1 off for the
route of record or restore it. State the real wall precisely (the union-form allowance e^{c_A‖col Γ ∪ Y‖_sh} over the whole
attached patch) even if it cannot be proven here; a correct statement is the deliverable. Record also the favourable
narrowing S5-17 (§24.3's straddling-plaquette doubt does not transfer, LI-pw being pointwise and (E2^𝔉) an expectation).

### Target W4 (STEP 4): process debt
- Record as a BREACH of binding rule 2 that checks/w5_criteria.md contains b_n, b_D, c_att derived in session 5, and that
  A1/A4/A5's PASS bands were drawn around §30.6's own hand values (reproduction checks, not pre-registrations). Do not
  repeat it: no w6 criteria file may contain a constant derived in session 6.
- §29's promised check-(ii) negative control (activities above the stated threshold, where the bound must fail or the
  expansion must diverge; max 2z² was 0.783) was never run: run it or record it as not run.
- Correct the stale n_H comparator at l.1643 and the two ceiling factors at l.1640.
- End the session with a "## FOR OTHER FILES (not edited)" section (the brief's rule 8, breached since session 4).

### Check w6 (criteria first: checks/w6_criteria.md, then the scripts; exact integer arithmetic, no numeric lock)
(i) Exact shadow computations on Z⁴ (L = 3, floor blocking) testing the inequality forms of W1 (a)-(c) and the
refutation/confirmation of W1 (b) at increasing depth, including positions chosen adversarially rather than at random.
(ii) The negative control §29 promised and never ran: the two-species toy at activities above the stated threshold.
Informational, never a proof. Every criterion is to be labelled either PRE-REGISTERED (outcome unknown when written) or
CONFIRMATORY (a check of a statement proven earlier in the session), per [RHW5-fix W5-1].

# Session-6 derivations (written after §34; typed from 12:58 UTC. Lane-H inputs read before writing: REVIEW_HW_S5.md in
full; PLD.md §18 (session 6 of lane E, which landed during this session — §18.4 Lemma BUF, §18.6 Proposition PATCH,
§18.9 M-1…M-7, §18.12's four requests to this lane) as relayed by the lead and then read directly at l.2188-2240,
l.2347-2440, l.2694-2722, l.2732-2760. Nothing of PLD.md, HIST.md, RLARGE.md or HANDOFF.md is edited here.)

## 35. STEP 1 (Target W1): the multiplicative factor of Lemma SH-att

### 35.1 The question, localised (and the reviewer's localisation verified)
REVIEW_HW_S5 S5-12 reports that at the session-5 constants four quantities coincide: (S2)'s ceiling 4.89789·10⁻⁹⁷,
REL-boot's own r ≤ ½ ceiling at B_* = c_f + 1, HIST-sum's own condition at B_0 = c_f + 2, and (T)'s threshold against
n_H(a, B_0). **I reproduced all four independently in plain-Python `Decimal` at 120 digits** (check w6 A4, no mpmath, no
BLAS, no lock): 4.897894·10⁻⁹⁷, 4.898021·10⁻⁹⁷, 4.898012·10⁻⁹⁷ and n_T = 9.991038·10⁹⁶ against n_H = 9.991019·10⁹⁶.
**CONFIRMED, and the consequence is accepted: (S2) and (T) impose nothing beyond H8′'s pre-existing r ≤ ½ and
n_♯ ≥ n_H(a, B_0), and the entire session-5 tightening is the factor that Lemma SH-att's N_4 step puts into
c_f = 6561·81·c_+ = 531441c_+.** So there is exactly one lever, and §30.6 l.1652's "A sharper SH-att or column bound lowers
it; not needed" is wrong on the second clause — erratum [RHW5-fix SH-1] below.
What follows replaces the factor 6561 by **81**, the per-level shadow constants 2401/38416/38417 by **625/10000/10001**, and
c_att(8) = 1229313 by **320001**; and it **REFUTES** the reviewer's conjecture that the multiplicative factor is removable.

### 35.2 Three shadow lemmas
Throughout: level-j cubes are indexed by Z⁴ (floor blocking), π(X) = coordinatewise ⌊·/L⌋, N_t(X) = the ℓ^∞ radius-t
neighbourhood, Σ(X) := N_1(π(X)), sh_{j+r}(X) := Σ^r(X) (HIST §7.1 l.455-457), ‖X‖_sh := Σ_{r≥0}|Σ^r(X)| over levels
≤ K − 1. Σ, π, N_t are monotone under inclusion and distribute over unions. X is an ARBITRARY finite set of level-j cubes
(no *-connectedness is used in §35.2).

**Lemma SH-1 (the shadow contains a collar of its projection): PROVEN-HERE (elementary, not counted).** For every X and
every r ≥ 1, **Σ^r(X) ⊇ N_1(π^r(X))**.
*Proof.* r = 1 is the definition. If Σ^r(X) ⊇ N_1(π^r(X)) ⊇ π^r(X), then by monotonicity of N_1∘π,
Σ^{r+1}(X) = N_1(π(Σ^r(X))) ⊇ N_1(π(π^r(X))) = N_1(π^{r+1}(X)). ∎
(This is the ingredient of the reviewer's free lever (a), S5-14 (1). Taken; it is subsumed in Lemma SH-att′ below, which
gives 81 rather than the reviewer's 2401.)

**Lemma SH-2 (the shadow radius is 2, not 3): PROVEN-HERE (elementary, not counted; it SHARPENS HIST Lemma H-geo (i)).**
For every X and every r ≥ 1, **Σ^r(X) ⊆ N_2(π^r(X))**.
*Proof.* For integers u, v, |⌊u/L⌋ − ⌊v/L⌋| ≤ ⌊|u − v|/L⌋ + 1, so |u − v| ≤ 2 and L ≥ 3 give
**π(N_2(B)) ⊆ N_1(π(B))**. Hence Σ(N_2(B)) = N_1(π(N_2(B))) ⊆ N_1(N_1(π(B))) = N_2(π(B)): radius 2 is a fixed point of
the collar-plus-projection recursion, where H-geo (i) used radius 3 (t ↦ ⌊t/L⌋ + 2 fixes t = 2 as well as t = 3). Now
r = 1: Σ(X) = N_1(π(X)) ⊆ N_2(π(X)). Step: Σ^{r+1}(X) = Σ(Σ^r(X)) ⊆ Σ(N_2(π^r(X))) ⊆ N_2(π^{r+1}(X)). ∎
*Optimality.* Radius 1 does NOT work: Σ^r({x}) can be a box of side 4 (not 3) about π^r(x) — one 4⁴-block per level, the
256 of §30.2's Reading — so N_1(π^r(X)) can fail to contain Σ^r(X). Check w6 G1 confirms both halves on 320 samples at
depths 5/10/20/30: **t = 2 and t = 3 have 0 violations, t = 1 has 9076.** So 2 is the smallest radius with this property.
**Corollary H-geo′ (the per-level shadow constants, re-derived): PROVEN-HERE (elementary, not counted).** For a *-connected
set 𝒟 of n level-j cubes and m ≥ 1, with CE-geo′ (g1′) as in H-geo (ii) (|π^m(𝒟)| ≤ 16 + 32(n − 1)L^{−m}):
  **|sh_{j+m}(𝒟)| ≤ 625·(16 + 32(n − 1)L^{−m})**  and  **Σ_{m=0}^{M}|sh_{j+m}(𝒟)| ≤ 10001n + 10000M**  (L = 3, d = 4),
in place of H-geo (iii)'s 2401(16 + 32(n−1)L^{−m}) and H-geo (iv)'s 38417n + 38416M.
*Proof.* |N_2(A)| ≤ 5⁴|A| = 625|A| with Lemma SH-2 and H-geo (ii) gives the first. For the second: the m = 0 term is n;
Σ_{m≥1}625·16 = 10000 per level; Σ_{m≥1}625·32(n−1)L^{−m} = 20000(n−1)/(L−1) = 10000(n−1); total
≤ n + 10000M + 10000(n−1) ≤ 10001n + 10000M. ∎
(625·16 = 10000 and 625·32/(L−1) = 10000 at L = 3, exactly as 2401·16 = 38416 and 2401·32/2 = 38416 before. **HIST.md is not
this lane's file: H-geo (i), (iii), (iv) are RE-DERIVED here, not edited there, and the request to HIST is in FOR OTHER
FILES. Everything in §35 that uses 10001/10000 is therefore proven HERE; everything that quotes HIST's own 38417/38416 —
REL-boot's r ≤ ½, HIST-sum's condition, c_B and n_H — is reported BOTH ways in §35.7, because a constant sharpened in HW
and left unsharpened in HIST merely moves the binding inequality to HIST's copy of it. That is pre-stated failure mode
(W-F3), and it materialised: see §35.7.**)

**Lemma COV (translate covering): PROVEN-HERE (elementary, not counted).** For every set A of cubes of one level,
  **N_2(A) = ⋃_{t∈{−1,1}^d}(N_1(A) + t),  N_3(A) = ⋃_{t∈{−2,0,2}^d}(N_1(A) + t),  N_4(A) = ⋃_{t∈{−3,0,3}^d}(N_1(A) + t),**
hence **|N_2(A)| ≤ 2^d|N_1(A)| = 16|N_1(A)|** and **|N_3(A)|, |N_4(A)| ≤ 3^d|N_1(A)| = 81|N_1(A)|** in d = 4.
*Proof.* "⊇" is immediate (|t_i| + 1 ≤ the radius). For "⊆" fix a ∈ A and x ∈ N_s(a) and choose t coordinatewise: for
s = 2, t_i := −1 if x_i ≤ a_i and +1 otherwise, so x_i ∈ [a_i + t_i − 1, a_i + t_i + 1]; for s = 3, t_i := −2, 0, +2
according as x_i ≤ a_i − 1, x_i = a_i, x_i ≥ a_i + 1; for s = 4, t_i := −3, 0, +3 according as x_i ≤ a_i − 2,
|x_i − a_i| ≤ 1, x_i ≥ a_i + 2. In each case x ∈ N_1(a) + t ⊆ N_1(A) + t. ∎
*Minimality.* Three translates per coordinate are needed at radius 3 (two 3-point intervals cannot cover 7 points) and two
at radius 2. Check w6 G2: the three identities hold with exact set equality on every sample, and the 2-per-coordinate
variant of the N_3 identity succeeds on none. **This single lemma is where the whole factor 81 comes from**: it converts
"the attached cluster's shadow sits in a radius-3 or radius-4 collar of P's shadow" from a volume ratio 7⁴ = 2401 or
9⁴ = 6561 into a COVERING by 3⁴ = 81 translates of a set already counted in ‖P‖_sh.

### 35.3 Lemma SH-att′: the multiplicative factor is 81
**Lemma SH-att′ (shadow of an attached cluster, sharpened): PROVEN-HERE (elementary, not counted; replaces Lemma SH-att
l.1498-1510 with the same hypotheses).** L ≥ 3, d = 4. Let P, Y be sets of level-j cubes and ρ ≥ 1 be such that every
y ∈ Y is joined to P by a chain y = y_0, y_1, …, y_s ∈ P with y_0, …, y_{s−1} ∈ Y and consecutive ℓ^∞ index distance ≤ ρ
(the hypothesis of Lemma SH-att, unchanged — pre-stated failure mode (W-F1) is avoided by changing nothing in it). Then
  **‖P ∪ Y‖_sh ≤ 81·‖P‖_sh + c′_att(ρ)·|Y|,  c′_att(ρ) := 1 + 40000ρ  (c′_att(8) = 320001).**
*Proof.* Take the forest of Lemma SH-att verbatim: trees τ_i, each with one anchor z_i ∈ P and cube set Y_i ⊂ Y,
Σ_i|Y_i| = |Y|, each τ_i a connected union of segments through the centres of its cubes of Euclidean length
ℓ_i ≤ 2ρ|Y_i| (ℓ² ≤ √d·ℓ^∞ = 2ρ per step in d = 4), and τ_i meets the box of every cube of π^r(Y_i) and of π^r(z_i).
Put r_i := ⌊log_L ℓ_i⌋ (ℓ_i ≥ 1 whenever Y_i ≠ ∅). Σ^r distributes over unions, so for each r ≥ 1
  Σ^r(P ∪ Y) = Σ^r(P) ∪ ⋃_i Σ^r(Y_i),
and we split the trees at level r into (a) ℓ_iL^{−r} < 1, i.e. r ≥ r_i + 1, and (b) r ≤ r_i.
*(a) — this is the step that carried the 6561.* Scaling level-(j+r) boxes to unit cubes, τ_i has length ℓ_iL^{−r} < 1 and
meets the unit box of π^r(z_i), so every point of τ_i is at Euclidean distance < 1 from it and
**π^r(Y_i) ⊆ N_1(π^r(z_i)) ⊆ N_1(π^r(P))**. By Lemma SH-2,
  Σ^r(Y_i) ⊆ N_2(π^r(Y_i)) ⊆ N_2(N_1(π^r(P))) = N_3(π^r(P)),
and by Lemma SH-2 again Σ^r(P) ⊆ N_2(π^r(P)) ⊆ N_3(π^r(P)). So the WHOLE of Σ^r(P) together with ALL case-(a) trees at
that level lies in N_3(π^r(P)) — one set, no per-tree multiplicity, so pre-stated failure mode (W-F2) is avoided. By
Lemma COV and then Lemma SH-1 (r ≥ 1),
  |N_3(π^r(P))| ≤ 81·|N_1(π^r(P))| ≤ 81·|Σ^r(P)|.
*(b).* By Lemma SH-2 and (g1′) applied to the scaled τ_i, |Σ^r(Y_i)| ≤ 625|π^r(Y_i)| ≤ 625(16 + 32ℓ_iL^{−r}), so
  Σ_{r=1}^{r_i}|Σ^r(Y_i)| ≤ 10000r_i + 625·32ℓ_i/(L−1) = 10000r_i + 10000ℓ_i ≤ 20000ℓ_i ≤ 40000ρ|Y_i|
(using log_Lℓ ≤ ℓ for ℓ ≥ 1, L = 3).
*r = 0.* |P ∪ Y| ≤ |P| + |Y| ≤ 81|P| + |Y|.
Summing over r ≥ 0 and over i: ‖P ∪ Y‖_sh ≤ 81Σ_{r≥0}|Σ^r(P)| + |Y| + 40000ρ|Y| = 81‖P‖_sh + (1 + 40000ρ)|Y|. ∎
*Gain.* 6561 → **81** on the multiplicative factor (the reviewer's free lever (a) gave 2401; Lemma COV gives 81, a further
×29.6) and 1229313 → **320001** on c_att(8) (×3.84, from Lemma SH-2). Check w6 G4: **0 violations** of
‖P∪Y‖_sh ≤ 81‖P‖_sh + c_att(8)|Y| on 320 samples at depths 5/10/20/30, including samples whose base point is on the
all-ones base-3 orbit (the adversarial POSITIONS of §35.4, which no earlier run used); the session-5 inequality has 0
violations too. The largest excess per Y-cube observed anywhere was 4235 (at depth 30), well inside c′_att(8) = 320001.
*Honest note on check w6 G5.* G5 was pre-registered as "max (‖P∪Y‖_sh − c_att|Y|)/‖P‖_sh" to record how loose the
multiplicative factor is. It came out 0.0000 and is **uninformative as pre-registered**: with the session-5 c_att = 1229313
the subtracted term exceeds the whole norm on every sample, so the quantity is ≤ 0 identically. Reported as a defective
criterion, not as evidence. The informative number is in §35.4: the samples force a multiplicative factor ≥ 5.714.

### 35.4 Proposition SH-neg: the factor CANNOT be removed (the reviewer's conjecture is REFUTED)
REVIEW_HW_S5 S5-14 (2) and S5-24 conjectured, from B2's 0 violations and depth-stability at M = 10/20/40/80 plus an
adversarial sampler (max excess 257.25 per Y-cube), that **‖P ∪ Y‖_sh ≤ ‖P‖_sh + c(ρ)|Y|** holds with c independent of the
depth, which would have taken g²_CRC to ≈ 3.2·10⁻⁹³/c_+. It does not.

**Proposition SH-neg (no additive form exists): PROVEN-HERE (counted with [HW-12] below).** Let L = 3, d = 4, ρ ≥ 8. For
every M ≥ 2 put ζ := (3^{M+1} − 1)/2 (all base-3 digits 1), z := (ζ, ζ, ζ, ζ), y := z + 8e_1, P := {z}, Y := {y}; Y is
ρ-attached to P at ρ = 8 and |Y| = 1. Then, with ‖·‖_sh summed over the levels j…j+M,
  **‖P ∪ Y‖_sh − ‖P‖_sh = 27M + 55**  and  **‖P ∪ Y‖_sh / ‖P‖_sh → 108/81 = 4/3.**
Hence no inequality ‖P ∪ Y‖_sh ≤ ‖P‖_sh + c(ρ)|Y| can hold with c independent of the number of levels, and no
multiplicative constant below 4/3 is possible in Lemma SH-att′.
*Proof.* Work coordinatewise: Σ, π and N_1 act independently on the four coordinates, so Σ^r of a product set is the
product of the one-dimensional Σ^r's. In one dimension write ζ_r := π^r(ζ). Since (3^m − 1)/2 = 1 + 3·(3^{m−1} − 1)/2, we
have ζ_r = (3^{M+1−r} − 1)/2 exactly, and **ζ_r ≡ 1 mod 3 for r ≤ M − 1**; so ζ_r − 1 = 3ζ_{r+1}, ζ_r = 3ζ_{r+1} + 1,
ζ_r + 1 = 3ζ_{r+1} + 2 all project to ζ_{r+1}.
(i) *P's shadow is minimal at every level.* C_r := {ζ_r − 1, ζ_r, ζ_r + 1}: Σ({ζ}) = N_1(ζ_1) = C_1, and if Σ^r({ζ}) = C_r
with r ≤ M − 1 then π(C_r) = {ζ_{r+1}} and Σ^{r+1}({ζ}) = N_1(ζ_{r+1}) = C_{r+1}. So Σ^r({z}) = C_r⁴, of size 3⁴ = 81, for
1 ≤ r ≤ M, and ‖P‖_sh = 1 + 81M.
(ii) *Y's shadow is one cube wider, for ever.* η := ζ + 8 = 3(ζ_1 + 3), so π(η) = ζ_1 + 3 and Σ({η}) = {ζ_1+2, ζ_1+3,
ζ_1+4}, disjoint from C_1. Next, ζ_1 + 2 = 3(ζ_2+1), ζ_1 + 3 = 3ζ_2+4, ζ_1 + 4 = 3ζ_2+5 all project to ζ_2 + 1, so
Σ²({η}) = {ζ_2, ζ_2+1, ζ_2+2} and Σ²({η}) ∖ C_2 = {ζ_2 + 2}. Then {ζ_2, ζ_2+1, ζ_2+2} projects to {ζ_3, ζ_3+1} (the last
element is 3(ζ_3+1)), giving Σ³({η}) = {ζ_3−1, …, ζ_3+2}, and the 4-element form **D_r := {ζ_r−1, ζ_r, ζ_r+1, ζ_r+2}** is
invariant: π(D_r) = {ζ_{r+1}, ζ_{r+1}+1} and N_1 of that is D_{r+1}. So for 3 ≤ r ≤ M, Σ^r({η}) = D_r and
Σ^r({η}) ∖ C_r = {ζ_r + 2}, exactly one element; at r = 2 also one; at r = 1, three.
(iii) *Assembling.* Σ^r({z, y}) = Σ^r({z}) ∪ Σ^r({y}) = (Σ^r_{1D}({ζ}) ∪ Σ^r_{1D}({η})) × C_r³, so
|Σ^r({z,y})| − |Σ^r({z})| = |Σ^r_{1D}({η}) ∖ C_r|·|C_r|³ = 27 for 2 ≤ r ≤ M and 81 at r = 1, and 1 at r = 0. Summing:
the excess is 1 + 81 + 27(M − 1) = 27M + 55, and ‖P∪Y‖_sh/‖P‖_sh = (1 + 108M + 55)/(1 + 81M) → 4/3. ∎
*Check w6 G3 (the decisive pre-registered test).* Computed exactly for M = 2…30: the excess is 109, 190, 325, 595, 838,
**865** at M = 2, 5, 10, 20, 29, 30, i.e. **27M + 55 exactly**; every slope E(M+1) − E(M) equals **27**; there is no
constant tail; E(30) = 865 exceeds 258, the largest per-Y-cube excess any prior run recorded. **Pre-registered verdict:
REFUTED.** On adversarially POSITIONED samples with |Y| > 1 at depth 30 the excess reached 4235 per Y-cube and the ratio
‖P∪Y‖_sh/‖P‖_sh reached **5.714**, so the proven factor 81 is loose by at most ≈ 14 on the evidence, not by ≈ 5·10³.
*Why the reviewer's evidence pointed the other way (diagnosis).* B2 and the reviewer's re-runs sampled POSITIONS at random
and only the DIRECTION of attachment adversarially. The excess is depth-stable at a generic position, because π's floor
dynamics drives both shadows to the same attracting 4⁴-block within O(log) levels. The all-ones base-3 position is the
exception: there P's shadow stays on the minimal 3⁴ orbit at every level, and the attached cube's never joins it. The
mechanism is exactly the one the reviewer asked for ("π^r(Y) ⊂ N_1(π^r(P)) ⇒ Σ^{r+c}(P ∪ Y) = Σ^{r+c}(P) for a fixed c")
and it is **false**: in the construction π^r(y) stays at distance 1 from π^r(z) for ever, and the shadows never merge.

### 35.5 Lemma COL′: the column bound at the sharpened constants
**Lemma COL′: PROVEN-HERE (elementary, not counted; replaces Lemma COL l.1515-1518).** For a *-connected set 𝒟 of n
level-m cubes and col(𝒟) its 81n level-(m−1) descendants, with M := K − 1 − m:
  **‖col 𝒟‖_sh ≤ 81·(n + ‖𝒟‖_sh) ≤ 81·(10002n + 10000M)**  and  **|[𝒟] ∩ S_R| ≤ 10001n + 10000M.**
*Proof.* π(col 𝒟) = 𝒟, so Σ^r(col 𝒟) = Σ^{r−1}(N_1(𝒟)) for r ≥ 1. The r = 0 term is |col 𝒟| = 81n = 81|Σ⁰(𝒟)|; the r = 1
term is |N_1(𝒟)| ≤ 81|𝒟| = 81|Σ⁰(𝒟)|. For r ≥ 2, iterating π(N_1(B)) ⊆ N_1(π(B)) gives π^{r−1}(N_1(𝒟)) ⊆ N_1(π^{r−1}(𝒟)),
so by Lemma SH-2, Lemma COV and Lemma SH-1 (at r − 1 ≥ 1)
  |Σ^{r−1}(N_1 𝒟)| ≤ |N_2(N_1(π^{r−1}𝒟))| = |N_3(π^{r−1}(𝒟))| ≤ 81|N_1(π^{r−1}(𝒟))| ≤ 81|Σ^{r−1}(𝒟)|.
Summing, ‖col 𝒟‖_sh ≤ 81|𝒟| + 81Σ_{s≥0}|Σ^s(𝒟)| = 81(n + ‖𝒟‖_sh), and Corollary H-geo′ bounds ‖𝒟‖_sh by 10001n + 10000M.
For the second claim, [𝒟] ∩ S_R ⊆ ∪_{r≥0}π^r(𝒟) and |π^r(𝒟)| ≤ |sh_{m+r}(𝒟)|, so Corollary H-geo′ again. ∎
(Against l.1516: 81(38418n + 38416M) → 81(10002n + 10000M), and 38417n + 38416M → 10001n + 10000M. The factor 81 is Lemma
SL's and is unchanged; what changed is the per-level constant, by Lemma SH-2.)

### 35.6 The extra R-free ring node A needs (PLD §18.4), and a cheaper price for it
PLD session 6 proves **Lemma BUF** (PLD l.2190-2197): if every cube of N_1(𝒜) is R-free then L_w ∩ X_j(𝒜) = ∅ for
w = h^{R,1}_j, by **this lane's Theorem LI^U-0′** with F ≡ 1 — so Lemma FT^far and Lemma COL-DEC apply to HW's own weight on
FAR sets, which is what (E2^𝔉) needs and what review S5-26 (PLD's reviewer) had recorded as unavailable. The hypothesis is
one ring stronger than §30.3's "col(Γ) ∪ Y R-free". PLD §18.12 request 1 asks this lane to buy it and to confirm that
nothing else in Theorem CRC-2T reads R″ specifically. **Both are done here.**

**(a) The purchase (accepted).** In step (4) of Theorem CRC-2T replace R″ := R′^{−Col(Y)} by
  **R‴ := R′^{−(Col(Y) ∪ Col(N_1(col 𝒟 ∪ Y)))} ∈ 𝔉_𝔥.**
**(b) Lemma RING (the price is ×17, not ×82): PROVEN-HERE (elementary, not counted).** For every set X of level-j cubes,
  **|sh_{j+r}(N_1(X))| ≤ 16·|sh_{j+r}(X)|  (r ≥ 1),  hence  #_{R′}(Col(N_1(X))) ≤ 16·Σ_{r≥1}|sh_{j+r}(X)| ≤ 16‖X‖_sh,**
so step (4)'s allowance e^{c_U‖X‖_sh} becomes **e^{17c_U‖X‖_sh}** and **c_+ = c_A + c_U becomes c_+ := c_A + 17c_U**, in
place of PLD §18.4's e^{82c_U‖X‖_sh} and c_A + 82c_U.
*Proof.* PLD's own step, iterated, gives Σ^r(N_1(X)) ⊆ N_1(Σ^r(X)). For r ≥ 1 put A_r := π(Σ^{r−1}(X)), so that
Σ^r(X) = N_1(A_r) **is itself N_1-thickened**; then by Lemma COV at radius 2,
  N_1(Σ^r(X)) = N_1(N_1(A_r)) = N_2(A_r) = ⋃_{t∈{−1,1}^4}(N_1(A_r) + t) = ⋃_{t∈{−1,1}^4}(Σ^r(X) + t),
a union of 2⁴ = 16 translates of a set already counted. For the second claim, Col is the OPEN column, so only r ≥ 1 enters:
#_{R′}(Col(Z)) ≤ Σ_{r≥1}|π^r(Z)| ≤ Σ_{r≥1}|sh_{j+r}(Z)| at Z := N_1(X). ∎
PLD's 81 is the bound |N_1(W)| ≤ 3^d|W| applied per level; it is correct but does not use the fact that the level-r shadow
is already a union of 3⁴-blocks, which is what gives 2^d. Check w6 G6 (pre-registered): **0 violations** of
|sh_r(N_1 X)| ≤ 16|sh_r(X)| on 320 samples at depths to 30; the observed maxima are 3.373 per level and 2.783 for the whole
r ≥ 1 sum, so even 17 is loose by ≈ 5 and the true price is nearer ×4.
**(c) Nothing else in Theorem CRC-2T reads R″ (PLD §18.12 request 1, confirmed here by walking the proof).**
- *Step (4)'s decomposition.* Y(c) is defined relative to **R′**, before the extra relaxation, so the partition of
  configurations by {Y(c) = Y} is untouched. R‴ ∈ 𝔉_𝔥 (Col(·) is upward closed and a union of upward-closed sets is upward
  closed; the torus is finite), and 1_{R′} ≤ 1_{R‴} pointwise by (m1).
- *The event E_Y.* col(𝒟) ∪ Y is R‴-free (it was R″-free and R‴ relaxes more), and every non-R‴-free cube is non-R′-free, so
  the two clauses used at l.1574-1576 survive verbatim; Buf^{R‴}_ρ ⊆ Buf^{R″}_ρ, so the buffer clause of E_Y is WEAKER and
  the inclusion {Y(c) = Y} ⊆ E_Y still holds. E_Y is still a function of U_{m−1}.
- *The induction hypothesis.* It is applied at R′ to the upward-closed set Col(Y) ∪ Col(N_1(col 𝒟 ∪ Y)), with
  N(R′) < N(R) unchanged; the two #-counts add, which is where Lemma RING's 16 and step (4)'s own 1 combine into 17.
- *Step (5)'s peel.* It needs every cube of 𝒟 to be R-free at level m and 𝒟 unconstrained at level m; R‴ relaxes a superset
  of what R″ relaxed, so both hold, Theorem LI^U-0′ applies as before, and 1_{R‴,m} still does not read int 𝒟's level-m
  links. (E2^𝔉) is then applied at R = R‴, where its new hypothesis "N_1(col Γ ∪ Y) R-free" is satisfied by construction.
- *Steps (6)-(8).* Unchanged: the Y-sum, (S1), (T) and −log(1 − p) ≤ 2p read only the constants, which §35.7 re-reads.
**Status.** Lemma RING: PROVEN-HERE. The purchase inside Theorem CRC-2T: PROVEN-HERE as a modification of step (4) whose
only effect on the proof is the constant c_+ = c_A + 17c_U. **CONDITIONAL on nothing of HW's; it is required only because
node A's route needs it, so a lane that later discharges (E2^𝔉) without Lemma BUF may delete the ring and recover §35.7's
no-ring column.**

### 35.7 The constants after §35.2-§35.6, and the honest ledger (check w6 A, Decimal 120 digits)
The session-5 formulas are unchanged in SHAPE. Writing C_sh for Lemma SH-att′'s multiplicative factor, 81 for Lemma SL's
column factor, (h_n, h′_n, h_D) for the per-level shadow constants and c_+ for the allowance,
  **b_n = C_sh·81·h_n·c_+ + h′_n·c_U,  b_D = h_D·(C_sh·81·c_+ + c_U),  c_f = C_sh·81·c_+,**
with (C_sh, h_n, h′_n, h_D) = (6561, 38418, 38417, 38416) in session 5 and **(81, 10002, 10001, 10000)** here, and
c_+ = c_A + c_U with no ring, c_A + 17c_U with §35.6's ring, c_A + 82c_U at PLD's price. At c_A = 0, c_U = 1, C_ℓ = 1, R = 0:
| scenario | c_+ | b_n | b_D | c_f | **g²_CRC** | **n_T** |
|---|---|---|---|---|---|---|
| session 5, no ring | 1 | 20416938755 | 20415875872 | 531441 | 4.89789·10⁻⁹⁷ | 9.99104·10⁹⁶ |
| session 5, ring ×82 | 82 | 1674185866133 | 1674098709808 | 43578162 | 5.97305·10⁻⁹⁹ | 8.19264·10⁹⁸ |
| **session 6, no ring** | 1 | 65633123 | 65620000 | 6561 | **1.52362·10⁻⁹⁴** | **3.21128·10⁹⁴** |
| **session 6, ring ×17 (§35.6)** | 17 | 1115603075 | 1115380000 | 111537 | **8.96376·10⁻⁹⁶** | **5.45840·10⁹⁵** |
| session 6, ring ×82 (PLD's price) | 82 | 5381106005 | 5380030000 | 538002 | 1.85835·10⁻⁹⁶ | 2.63286·10⁹⁶ |
At every ring value the session-5 → session-6 gain is **×311.1 on g²_CRC, ÷311.2 on n_♯ and ÷81 on c_f** (the ×81 of Lemma
COV and the ×3.84 of Lemma SH-2 multiply). Also c_att(8): 1229313 → 320001; (S1)'s ceiling 1.83822·10⁻⁹³ (so (S1) is still
implied by (S2), as §30.6 said); g²_ret = 3.67644·10⁻⁹⁸; Δ_ρ² = 6.9756·10⁹ unchanged.

**(i) Against the recorded (RLF-δ) ceiling 10⁻⁹⁴ (check w6 A3, pre-registered).**
- session 5, no ring: BELOW by ×204.17 — session 5's headline, reproduced.
- session 6, **no ring: ABOVE by ×1.52** — i.e. the breach would have disappeared outright for c_+ ≤ 1.52.
- session 6, ring ×17: **BELOW by ×11.16**. session 6, ring ×82: BELOW by ×53.81.
- session 5 carrying the same ring: BELOW by ×3470.9 (×17) or ×16741.9 (×82).
**So the answer to Target W1 (b)-(c) is: the breach against 10⁻⁹⁴ is reduced from ×204 to ×11.2, and it does NOT
disappear.** Two independent reasons, and both must be said: the multiplicative factor is **not removable** (Proposition
SH-neg), and node A's buffer ring costs ×17 on top. Even the unattainable additive form would give 3.2·10⁻⁹³/82 ≈
3.9·10⁻⁹⁵ after the ring, still below 10⁻⁹⁴. **The reviewer's "the breach simply disappears" (S5-14 (2)) is withdrawn, and
so is the hope attached to it.**
**(ii) Failure mode (W-F3) materialised: the gain is HW-internal until HIST moves.** With HIST's own 38417/38416 left in
place, REL-boot's r ≤ ½ (B_* = c_f + 1) and HIST-sum's condition (B_0 = c_f + 2) give **2.33375·10⁻⁹⁶** at the ×17 ring —
BELOW g²_CRC = 8.96·10⁻⁹⁶, so **they, not (S2), become the binding inequality** (breach ×42.85 against 10⁻⁹⁴), and
n_H = 2.09688·10⁹⁶ exceeds n_T = 5.4584·10⁹⁵ by ×3.84. With Corollary H-geo′'s 10001/10000 substituted in HIST's own
statements, all four coincide again — spread **1.0001** — reproducing S5-12's coincidence at the new constants
(check w6 A2, pre-registered; the answer was not known when the criteria were written). **Hence: ÷81 on c_f is HW's
unconditionally (it is Lemma COV, used inside HW's own Corollary CRC-HW), and the further ×3.84 on the programme's ceilings
is CONDITIONAL on HIST adopting Corollary H-geo′** — FOR OTHER FILES item 2. Until then the honest programme number at the
×17 ring is **2.33·10⁻⁹⁶/c_+**, still ×4.77 above session 5's 4.898·10⁻⁹⁷.
**(iii) Against the ceiling that actually binds ([RHW5-fix CST-2], and this is the point of the exercise).**
REVIEW_RLARGE_V3 l.61 ("It still does not bind against DX′"), REVIEW_SF_S7 l.335 and RLARGE l.618 record the binding
programme ceiling as **g_0² ≈ 2.5·10⁻¹⁵²/C_Ω**. At c_+ = 1, C_Ω = 1, session 6's g²_CRC with the ×17 ring exceeds it by
**×3.5855·10⁵⁶**, and g²_CRC ≥ 2.5·10⁻¹⁵² holds while **c_+ ≤ 6.0954·10⁵⁷** (check w6 A5). Session 5's own number already
had ×1.96·10⁵⁵ of slack. **So (S2) costs the programme nothing at the recorded constants, in session 5 or in session 6**,
and the open risk is that c_A is uncertified (PLD l.1902), not that g_0 must move. **HANDOFF's "g_0 therefore has to be
lowered. Recheck the downstream constants, including the SF thresholds" is an over-reaction and is withdrawn** (FOR OTHER
FILES item 1). This is a bookkeeping event, not a crisis, and §30.6/§32/§33's framing implies a crisis that does not exist.
**(iv) What session 5's headline becomes.** "(S2) FAILS at the recorded ceiling and needs g_0 lowered" (l.1641, l.1724,
§33) is **half withdrawn**: the arithmetic failure against 10⁻⁹⁴ survives (×11.2 with the ring), but (a) its ATTRIBUTION to
(S2) is wrong — (S2) ≡ REL-boot's r ≤ ½ ≡ HIST-sum's own condition, all of which predate this route (S5-12, reproduced in
w6 A4); (b) its SIZE was an artefact of two geometric constants, now reduced by ×311; (c) its CONSEQUENCE ("lower g_0,
recheck the SF thresholds") is withdrawn, there being ≈ 56 orders of slack against DX′; and (d) the one new real cost is
node A's ring, which session 5 did not know about. **Nothing in the chain is in crisis and nothing downstream needs to
move.**

## 36. STEP 2 (Target W2): Theorem CRC-2T restated as what it is

**[RHW5-fix GAS-1, applied as an erratum.]** §30.4's heading "The two-type gas, and the theorem" and §33 l.1720's "(a) The
gas written" overstate. **The correction, binding and accepted:** §30.4 describes a two-species bestiary — far defects,
animals, column and collar linking, per-type decay — and **no polymer partition function, no compatibility (hard-core)
relation, no Mayer identity and no Kotecký-Preiss criterion is constructed or used anywhere in §30** (l.1610 already says
the KP name is cited for orientation only). Consequently **§29's Target V2 (a) — "the ratio … is bounded by the gas's
partition-function ratio, or by its polymer sum" — is NOT DELIVERED**, and §33's "V2: MET as an implication" should read
"V2 (a): NOT DELIVERED as written; (b)-(d) MET as implications". §30.4's symbols z_1, z_2 are retained only as names for
the two per-step bounds (x in step (6), the step bound in steps (6)-(7)); they are not polymer activities of any gas that
is summed.
**What the session actually proved is better than what V2 (a) asked for**, and that is the claim to make: it needs **no
polymer representation of 1_R**, which REVIEW_HW_S4 Priority 6 identified as the real obstruction ("The obstruction is the
representation, not convergence"), and it closes the m = k + 1 step that REVIEW_HW_S4 l.1321 said could not close ("For
m = k + 1 it is (CRC)_k itself: the induction does not close"). Accordingly:

**Theorem CRC-2T′ ((CRC) for the column-relaxed family, by induction on the number of constrained pairs): CONDITIONAL
[HW-11, re-labelled; implication PROVEN-HERE in §30 and re-constanted here; counted once, not twice].** Assume (F_R) (lower
half and u_m ≤ u_{m−1} + R) with g_K² ≤ 1/(2R), SU(2) (SU(N ≥ 3): (KS-N)), bad-only history-independent defects,
(CLS-min), max{6θ, 24θ}(1 + 2Rg_K²) < 1, **(E2^𝔉′)_{θ,ρ} of §37 with ρ = 3L − 1**, and (S1), (S2), (T) **at the constants
of §35.7** for some c_U ∈ (0, 1]. Then for every admissible 𝔥, every R ∈ 𝔉_𝔥 and every upward-closed set 𝒞′ of pairs at
levels ≥ k_0 + 1 (in particular Col(B) for a set B of level-k cubes, k ≥ k_0),
  **ρ^F_R(𝒞′) ≤ exp(2ε_2·#_R(𝒞′)) ≤ exp(c_U·#_R(𝒞′)),**
and in particular **(CRC)_k holds with c_U := 2ε_2** (F ≡ 1, k_0 = k, R = R(𝔥)), uniformly in g ≤ g_0, K, T, 𝔥.
*Proof.* §30.4's proof verbatim, with four replacements: Lemma SH-att → **Lemma SH-att′** (§35.3) in step (6); Lemma COL →
**Lemma COL′** (§35.5) in steps (3) and (6); step (4)'s R″ → **R‴** with Lemma RING (§35.6), which is the only change to
the argument and changes only c_+; and the constants b_n, b_D, c_att, c_+ read from §35.7. Nothing else moves (§35.6 (c)
walks every step). ∎
**The accurate description of the proof, for the record.** It is an **induction on the finite integer N(R) := |S_R| ∈ ℕ**,
the number of constrained (level, cube) pairs of the pattern, at fixed (𝔥, T, K) and with a FIXED constant c_U; the base is
#_R(𝒞′) = 0; every inner use of the hypothesis — step (1)'s R_{t−1}, step (3)'s R_{t−1} with 𝒞′ = [𝒟], step (4)'s R′ and
(now) the ring — is at a strictly smaller value of N; the telescoping
ρ^F_R(𝒞′) = Π_t Z^F(R_{t−1})/Z^F(R_t) = Π_t[1 − p_t]^{−1} is an **exact identity**; step (2)'s containment and step (4)'s
event algebra are proven set inclusions; step (6) is a Mayer-TYPE factorisation used only as an over-counting inequality,
with (S1) the standard Δ²z ≤ ½ criterion for the far-defect species and the reverse cross-species direction paid by the
induction's own c_U and closed by 2ε_2 ≤ c_U; and the closing condition is a fixed inequality on constants, checked once —
**not a nonlinear bootstrap (V-F4) and not a fixed-point problem**, since c_U := 1 may be taken on input. The proof is
therefore **neither a cluster expansion nor a convergence proof for a gas**; it is the inductive (Kotecký-Preiss-SHAPED,
not Kotecký-Preiss) leaf-summation written as a recursion on constrained pairs. l.1605-1614's "Relation to Theorem CE /
CE-col" is accurate and stands.
**[RHW5-fix NIT, item 4.]** Theorem CRC-2T′ with F ≡ 1 also serves the **off-route consumers** named in §23's table —
RLARGE row K8 and EXISTENCE's single-cube union bound — since those ask (CRC) for R = R(𝔥) and single cubes, a special
case of 𝒞′ = Col(B), |B| = 1. §32's list does not say so; it should (one clause, free).
**Not added, and not claimed:** a cluster expansion, a polymer gas, a Kotecký-Preiss criterion, any partition-function
bound of the gas, or any reduction in the programme's binding coupling ceiling (§35.7 (iii)).

## 37. STEP 3 (Target W3): (E2^𝔉) restated so that it asks node A only for what node A can owe

PLD session 6 (lane E) landed during this session and settles most of this. Its three load-bearing results for this lane
are **Lemma BUF** (PLD §18.4, which uses THIS lane's Theorem LI^U-0′), **Proposition FAR** (PLD §18.2: HW's far Y and
animal columns satisfy the only clause of (C_S) that GEO (i), (iii), (iv), FT^far and COL-DEC use, namely S ∩ 𝒰_j = ∅ — so
the SET class was never the obstruction; the obstruction is GEO (ii), i.e. the WEIGHT), and **Proposition PATCH** (PLD
§18.6.1), whose finding is the valuable part: **Theorem NA-PRICE^E/E+ generate no allowance at all, they only TRANSMIT the
small-field hypothesis's**, so the patch allowance is a **clause of the hypothesis**, which is exactly why no PLD §16-§17
statement has that shape. §37's statement is written to PLD's shape, not invented here.

**(E2^𝔉′)_{θ,ρ} [OPEN; owner node A; replaces (E2^𝔉) of l.1524-1530 and H6-H7 on the (E2) route].** There are C_fc, C_A,
a_A ≥ θa_bad and c_A, independent of g, K, T, 𝔥 and of the pattern, such that for
- every R ∈ 𝔉_𝔥 (every upward-closed relaxation at levels ≥ k_0 + 1),
- every level **j ≥ max{k_0, 1}** (see the level clause below),
- every finite set Γ of level-(j+1) cubes with **Γ ∩ A_{j+1}(𝔥) = ∅ or Γ = 𝒰_{j+1}** (Proposition FAR (ii)'s hypothesis,
  which Theorem CRC-2T′ supplies: Γ = 𝒟 is a set of constrained cubes in step (5), Γ = 𝒰_{k+1} in Corollary CRC-HW),
- every finite set Y of level-j cubes outside col(Γ) with **N_1(col(Γ) ∪ Y) R-free** (one ring more than l.1526 asked;
  bought inside Theorem CRC-2T′ by §35.6 at ×17 on c_U), and
- **every** bounded measurable F_< ≥ 0 that is a function of U_0, …, U_{k_0−1} (**universally quantified**; free on node A's
  side, PLD §18.6.2 Delta 3 / M-7),
the following holds with ν := ν^{R,F}_j (the past law of levels ≤ j of R with F_< inserted) and w := h^{R,1}_j times the
buffer indicator (the "buffered weight" of PLD §18.4 (d)):
  **E_{ν^w}[Π_{Q∈Γ}e^{θ min{π_Q, Y^f_Q}}·1{Y ⊂ D_j}·1{Buf^R_ρ(col Γ ∪ Y) ∩ D_j = ∅}]
      ≤ C_fc^{|Γ|}·(C_Ae^{−a_Au_j})^{|Y|}·e^{c_A‖col Γ ∪ Y‖_sh}.**
**How the allowance clause is to be read (the renegotiation, PLD §18.12 request 2).** What node A must PROVE is **not** the
displayed union form. It is: *node A's small-field moment carries at most a per-cube constant and no shadow sum* — form
**(P0)** (no allowance, c = 0) or **(P1)** (e^{c|A∖A′|}, absorbed into c_sf^{|A∖A′|}) of PLD Proposition PATCH (v). The
displayed e^{c_A‖col Γ ∪ Y‖_sh} then follows **free**, by monotonicity of ‖·‖_sh (PATCH (i)): every set node A actually
prices — Y ⊔ x(Γ_1) for a choice function x, which is what the CAP-dec expansion produces — is a SUBSET of the patch
col(Γ) ∪ Y, and ‖·‖_sh is monotone. The forms node A must NOT be asked for, and HW does not ask for, are **(P2)** per-cube
union sums e^{cΣ_{Q}‖{Q}‖_sh} (which carry the per-cube depth term 81 + 256(K − j − 2) of §30.2's Reading, unaffordable at
a_A ≈ 10⁻⁸⁶ at any coupling) and **(P3)** the slice s_k(𝔥) (**incomparable** to both the union and patch forms, in both
directions: PATCH (ii)). **So the currency dispute is closed: HW's requirement is "per-cube constant, no shadow sum, never
the slice, and never per-cube depth"; the patch form is a consequence, not a request.** And if the moment comes with (P0),
node A delivers **c_A = 0**, which is strictly stronger than HW asks and lowers HW's own constants by (c_A + c_U)/c_U
(PLD §18.7 (5) claims exactly this).
**The level clause ([RHW5-fix E2-2], and l.1530's clause is withdrawn as ill-formed).** l.1530 put Γ and Y both at level 0
while the body has Γ at level j+1 and Y at level j, where at level 0 there is no finer level and col(Γ) is undefined. The
two consistent readings are **(0a)** Γ a set of level-0 cubes with the Wilson window Π_{Q∈Γ}e^{θX_Q} and **Y = ∅**, or
**(0b)** Γ at level 1 with Y at level 0. PLD delivers **j ≥ 1** (PLD §18.7; §17 alone gives k ≥ 2, PLD l.1905) and
**neither (0a) nor (0b)**: level 0 is OPEN on both sides ((LCR)_0 / the level-0 Wilson window moment, PLD §16.5 "Level 0",
§18.9 M-3). Since Lemma TEL-f needs every level, **the interface is NOT delivered, and the bottom two levels are a named
hole, not a detail.** Theorem CRC-2T′ and Corollary CRC-HW are therefore CONDITIONAL on a hypothesis that is OPEN at j = 0
even after PLD session 6, and §32's H6′ row did not flag the level restriction at all.
**The deltas, now all declared (S5-16, and their status after PLD §18).**
| delta | (E2^𝔉)'s demand | node A's position after PLD §18 |
|---|---|---|
| D1 allowance currency | union form over the attached patch (≠ PLD l.1408's ‖S‖_sh, ≠ PLD l.1856's slice) | **ANSWERED**: Proposition PATCH — the patch form follows from a per-cube-constant moment by monotonicity; the slice is incomparable and is the wrong object (M-1) |
| D2 level range | every j ≥ k_0, plus a level-0 clause | j ≥ 1 delivered (PLD §18.7); **j = 0 OPEN**; HW's level-0 clause was mis-levelled and is replaced above (M-3) |
| D3 F_< free symbol | unquantified at l.1528 | **ANSWERED**: universally quantifiable at zero cost (M-7); done above |
| D4 set class (far Y) | the price of a FAR set | **ANSWERED**: (C_S) was not the obstruction (Proposition FAR); GEO (ii) was, and Lemma BUF closes it for one extra R-free ring, bought here at ×17 (M-2) |
| D5 family uniformity over 𝔉_𝔥 | uniform in the pattern | not an obstruction for the law conversion (Lemma BUF is applied once, before the declaration); still open for the two open halves, which PLD §18.6 states over 𝔉_𝔥 |
| D6 weight class | the one weight h^{R,1}_j (not "any w") | **in HW's favour**: PLD §17's "any w" is STRONGER than HW asks and is expected false (E1-1, M-4); PLD §18.7 restricts to 𝔏^buf_k, which is HW's class |
| D7 form | ONE joint expectation (Γ-moment and Y-probability together) | PLD §17.4 states an unconditioned probability; PLD §18.7's Cor. E2-RED states the F-conditioned joint form, which is what CAP-dec and (E2^𝔉′) consume (M-6) |
**[RHW5-fix TF-2], recorded with BOTH positions, not absorbed.** REVIEW_HW_S5 S5-19 holds that §30.5's finer-first order
switches TF-1 off and thereby **reinstates** the node-A law mismatch TF-1 was introduced to remove (no PLD statement being
written under laws carrying the finer capped spectators). **Node A denies this** (PLD §18.6.2, §18.12 request 5): PLD §17.2
builds ν^{(k)}_k with the finer capped spectators Π_{k′<k}Φ_{k′} already inserted, and Lemma GEO (iv) is the clause that
handles Φ_{k−1}; so "the law PLD §17 is written for IS HW's finer-first law". **On the evidence I can check, node A is
right and the review's S5-19 is to be narrowed**: the law class in PLD §18.7.0 is HW's, and HW's F_< reads only levels
≤ k_0 − 1 ≤ j − 1, strictly finer than the links FT^far/COL-DEC are about. What TF-1 protected was the **(E1)** form, which
E1-1 expects false for independent reasons. I therefore do **not** propagate S5-19's conclusion; §30.5's "TF-1 caveat" is a
presentational caveat, not a node-A regression. **This is a disagreement between two binding documents and is flagged for
the lead** (FOR OTHER FILES item 5); nothing in §35-§37 depends on which way it is resolved.
**[RHW5-fix NIT, item 5: the favourable narrowing of §24.3's doubt, accepted.]** l.1298-1302's session-5 doubt (bad-only
goodness reads only the INTERIOR plaquettes of the buffer cubes, so far curvature can sit on the straddling plaquettes —
the LI-pw mechanism) is **correct as an observation about LI-pw and does not transfer to (E2^𝔉′)**: Proposition LI-pw is a
POINTWISE statement exhibiting two configurations, while (E2^𝔉′) is an EXPECTATION under ν^w for the one weight
w = h^{R,1}_j ∈ [0, 1], and a buffer configuration carrying O(1) straddling holonomy at level j costs level-j action of
order u_j = 1/g_j², i.e. has ν-probability e^{−c/g_j²}. The measure suppresses exactly the configurations LI-pw constructs.
**So the straddling-plaquette worry is not an obstruction to (E2^𝔉′), and l.1298-1302 is narrowed accordingly** (erratum;
the struck-through discipline cannot be applied from an appended section, so this paragraph is the correction of record).
**What is left is a different and better-posed difficulty**, and both lanes have now reached it from opposite sides:
ν^w(·) ≤ ν(·)/E_ν[w] with E_ν[w] = Z^F(R)/Z^F(past), so (E2^𝔉′) fails unless conditioning on the coarser constraints costs
no volume factor — a **positivity-of-density statement with a boundary allowance**, which is what the patch allowance
encodes. Node A's own session-6 verdict is the same statement from the other side: their single biggest obstruction is
**(CEM-2)**, a decoupling across one R-free ring that is **not obtainable from the buffer-good event alone** (the event
bounds curvature by ε_1 where a g-independent constant needs ≈ g_K, a gap they measure at 4.489·10¹⁵), so the mechanism
must be the weight's **typicality under the measure** — i.e. a decoupling under the measure, not a deterministic geometric
statement about buffer-good configurations. **That is the exact residual of the whole HW route, and it is one statement,
owned by node A.**

## 38. STEP 4 (Target W4): the eleven binding fixes as errata, and the process debt

This session cannot edit §0-§33, so each binding fix is recorded here as an **erratum naming the line it corrects**. All
eleven are applied; none is declined.

| # | fix | line(s) corrected | correction of record |
|---|---|---|---|
| 1 | **[RHW5-fix CST-1]** | l.1638-1643, l.1709-1712, §33 l.1723-1725 | **§35.1.** (S2) is numerically the SAME inequality as REL-boot's r ≤ ½ at B_* = 531441c_+ + 1 (4.898021·10⁻⁹⁷) and as HIST-sum's own condition at B_0 = 531441c_+ + 2 (4.898012·10⁻⁹⁷), against (S2)'s 4.897894·10⁻⁹⁷; and (T)'s n_T = 9.991038·10⁹⁶ is numerically n_H(a, B_0) = 9.991019·10⁹⁶. All reproduced in independent Decimal-120 arithmetic (w6 A4). **So (S2) and (T) imposed nothing new, and the entire session-5 tightening was the ×6561 of SH-att's N_4 step entering c_f.** §30.6's "(S2) is the binding inequality" is correct only as an identity with constraints H8′ already carried. |
| 2 | **[RHW5-fix CST-2]** | l.1640-1642, l.1709-1712; HANDOFF l.57-59 | **§35.7 (iii).** The binding programme ceiling is g_0² ≈ 2.5·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 l.335; RLARGE l.618; REVIEW_RLARGE_V3 l.61 "It still does not bind against DX′"). g²_CRC exceeds it by ×3.59·10⁵⁶ at c_+ = 1 (w6 A5), and the proviso is c_+ ≲ 6.1·10⁵⁷. **So (S2) costs the programme nothing**; the open risk is that c_A is uncertified (PLD l.1902). HANDOFF's "g_0 therefore has to be lowered. Recheck the downstream constants, including the SF thresholds" is **WITHDRAWN** (FOR OTHER FILES item 1 — HANDOFF is the lead's file). |
| 3 | **[RHW5-fix CST-3]** | l.1643 and l.1640 | l.1643's comparator **n_H ≳ 2·10⁸⁷ is STALE**: the reviewed value is n_H ≥ 1.810·10⁹¹ (REVIEW_RLARGE_V3 Part 4, fix N3-1: "the dominant term is c_B, not 4"), and at HW's own B_0 = 531441c_+ it is 1.0·10⁹⁷c_+ ≈ n_T. **"n_♯ grows by ≈ 10¹⁰" is struck**; the honest figure is the c_f jump (≈ 6.6·10³ against session 4's own value), and on session 6's constants n_H(a, B_0) = 2.09688·10⁹⁶ at the ×17 ring EXCEEDS n_T = 5.4584·10⁹⁵, i.e. **(T) adds nothing to H8′ at all**. l.1640's "a factor ≳ 2·10²" hides a difference of 2700×: the two factors are **204.17** (against 10⁻⁹⁴) and **5.5126·10⁵** (against 2.7·10⁻⁹¹); both are now ×311.1 smaller. |
| 4 | **[RHW5-fix SH-1]** | l.1498-1510 (Lemma SH-att), l.1651-1652 ("not needed") | **§35.2-§35.5.** l.1652's "A sharper SH-att or column bound lowers it; not needed" is **RETRACTED**: it was the only thing needed. The reviewer's free lever (2401 for 6561) is taken and superseded: Lemma COV gives **81**, Lemma SH-2 gives 625/10000/10001 for 2401/38416/38417, and c_att(8) = 1229313 → 320001. The reviewer's second gain (the additive form, "the breach simply disappears") is **REFUTED** by Proposition SH-neg, with the missing lemma it named shown to be FALSE. |
| 5 | **[RHW5-fix E2-2]** | l.1524-1530, l.1699 (H6′) | **§37.** F_< universally quantified over bounded measurable functions of U_{<k_0}; the level-0 clause replaced ((0a)/(0b), both OPEN) and the level restriction j ≥ 1 flagged; seven deltas declared in a table; the allowance clause restated as the per-cube-constant requirement with the patch form derived by monotonicity. |
| 6 | **[RHW5-fix TF-2]** | §30.5 l.1626-1631, l.1699 | **§37**, with BOTH positions recorded: the review's S5-19 (the finer-first order reinstates the node-A law mismatch) and node A's denial (PLD §18.6.2: PLD §17.2's law already carries the finer capped spectators). I judge node A right and do not propagate S5-19; flagged for the lead. |
| 7 | **[RHW5-fix GAS-1]** | §30.4 heading, l.1605-1614, §33 l.1720 | **§36.** "The gas described"; no partition function, compatibility relation, Mayer identity or KP criterion is constructed or used; **§29 V2 (a) NOT DELIVERED**; the induction is better than the expansion asked for because it needs no polymer representation of 1_R. |
| 8 | **[RHW5-fix SYM-1]** | l.1273/l.1373 vs l.1690 (c_f); l.1543 vs l.1690 (C_ℓ); l.1549 vs PLD l.1417 (c_U) | (a) **c_f**: SL-1's c_f := 81(c_A + c_sf′) is **superseded** by §32 l.1690's 531441c_+ and now by §35.7's C_sh·81·c_+; **(E2^𝔉′)'s c_A stands for c_A + c_sf′**, c_sf′ having been absorbed into the single node-A constant. (b) **C_ℓ**: §30.4 l.1543's UNPRIMED C_ℓ = (1−λ_*)^{−3n_int/2}C_fc is the one ε_2 and (S2) need; §32 l.1690's PRIMED C_ℓ (with C_fc′ = 2C_fc e^{c_f}) is the one REL-boot's r and B_0 need. **Two values, one symbol: an integrator must not feed the primed value into ε_2.** The difference is additive ≈ 5.3·10⁵c_+ in the log and immaterial against b_n. (c) **c_U**: HW's c_U is the (CRC) constant; PLD's c_U is the (LI^U) ratio constant of PLD l.1417's c_A = 6c_U + c_ns. **PLD's c_U is 0 on this route (Theorem LI^U-0; REVIEW_HW_S4 X-2) and is a DIFFERENT SYMBOL from HW's**, so §30.6's "Order of constants (non-circular)" is non-circular; and PLD's own session-5/6 form has no c_U at all (c_A = c_cd, now c_A = 0 in PLD §18.7). Read **c_+ ≤ c_A + 17c_U** wherever the derivation needs the input value (c_U^in = 1), the output being c_U^out = 2ε_2. |
| 9 | **[RHW5-fix W5-1]** | §31 l.1665-1683 | **§38.1** below (the w5 defects, disclosed) and **§39** (w6's own criteria labelled PRE-REGISTERED or CONFIRMATORY, with the criteria file's md5 recorded in HW_LOG as the review asked). |
| 10 | **[RHW5-fix SC-1]** | the absence of the section since session 4 | **§41**, the required "## FOR OTHER FILES (not edited)" section. |
| 11 | **[RHW5-fix NIT]** | l.1484, l.1572, l.1477-1479, §32, l.1298-1302 | (a) **l.1484**: read "F_< ≥ 0 a fixed bounded weight **with Z^F(∅) > 0**"; it is automatic in the application (Φ ∈ [1, e^{θπ}] ≥ 1) but not from "F_< ≥ 0 bounded" alone. (b) **l.1572**: step (5) needs BOTH that every cube of 𝒟 is R‴-free (for h^{R‴,1}_m) AND that (m, x) ∉ S_{R‴} for x ∈ 𝒟 (for 1_{R‴,m}); both hold because the relaxation is of the CLOSED column [𝒟], not the open one, and "R-free" (open column) and "unconstrained at level m" are different properties. (c) **l.1477-1479**: a pair (m+1, π(x)) in the upward closure of 𝒞 need not lie in S(𝔥), so 𝒞 ∪ {…} is not literally upward closed as a set of pairs; immaterial because R_{S(𝔥)∖𝒞} = R_{S(𝔥)∖(𝒞 ∪ anything off S(𝔥))}, so one may replace 𝒞 by its upward closure WLOG. (d) off-route consumers: §36. (e) §24.3's doubt narrowed: §37. |

### 38.1 The process debt, recorded honestly
- **Binding rule 2 was BREACHED in session 5 (CONFIRMED, S5-3).** checks/w5_criteria.md l.8-12 defines its PASS conditions
  in terms of **b_n, b_D and c_att(ρ)**, all three first derived in §30.2/§30.4 of the SAME session (HW_LOG l.150-151 says
  so plainly and does not call it a breach). Worse, **A1's band [4.0·10⁻⁹⁷, 5.5·10⁻⁹⁷], A4's [5·10⁹⁶, 2·10⁹⁷] and A5's
  [1.0·10⁻⁹⁷, 2.0·10⁻⁹⁷] are brackets drawn around §30.6's own hand values** (4.9·10⁻⁹⁷, 1.0·10⁹⁷, 1.6·10⁻⁹⁷). **A1, A4
  and A5 are therefore REPRODUCTION checks of §30.6's hand arithmetic, not pre-registrations**, and §31's "A (arithmetic,
  50-digit)" and §33's "Check w5: OVERALL PASS" present them as pre-registered verdicts. A2 and A3 are genuinely
  informative. The criteria file stays frozen; this paragraph is the disclosure. **Not repeated here:
  checks/w6_criteria.md contains no constant derived in session 6** (it says so, and lists every constant it uses with its
  prior source), and §39 labels every w6 criterion PRE-REGISTERED or CONFIRMATORY.
- **§31's other defects, disclosed (S5-23, S5-25).** (a) §31's "Exact arithmetic (log space)" should read "50-digit";
  mp.dps = 50 cannot represent ceil(n_T) − 1 at the 10⁹⁷ scale, so w5's n_♯ is effectively n_T (an error of 1 part in
  10⁹⁷, immaterial). (b) "OVERALL PASS (A1-A5, B1-B3, C1-C3)" is literally true and reads as success, while **A3's PASS
  records a FAIL of (S2) at the recorded coupling**; the OVERALL line should say so. (c) §31's scope line claims C "tests
  the step containment and the two-species activity formula"; it has **no coverage of step (6), Lemma SH-att, (S1) or
  Δ_ρ²**, so **(S1)'s convergence had no numerical coverage in w5 at all** beyond A2's arithmetic.
- **§29's promised check-(ii) negative control was never run (S5-25, scope defect 1), and is RUN HERE.** §29 l.1462-1464
  pre-registered "(ii) … with a negative control (activities above the stated threshold, where the bound must fail or the
  expansion must diverge)". No w5 grid point had 2z² ≥ 1 (the maximum was 0.783 at (p, q, q′) = (0.3, 0.1, 0.9), which I
  reproduce exactly), and criterion C3 (dropping the finer contribution) is a DIFFERENT control; the substitution was
  nowhere disclosed. **Check w6 N runs the promised one in the same toy, in exact Fraction arithmetic**: see §39 N, where
  it PASSES as pre-registered and where I also record what it does and does not show.
- **No numeric lock was taken this session and none was needed**: every w6 computation is exact integer, exact Fraction or
  plain-Python Decimal arithmetic, single-threaded, with no numpy and no BLAS (the brief's rule 6; the same ground on
  which REVIEW_HW_S5's Part 8 re-derivations were run).

## 39. Check w6 (criteria checks/w6_criteria.md 13:01:43 UTC, md5 060c532292f0953042fafd4b2d559760, written BEFORE every
script; scripts checks/w6_shadow.py 13:02:23, checks/w6_arith.py 13:04:21, checks/w6_gas.py 13:05:08; records
checks/w6_{shadow,arith,gas}.{out,err})
Three independent runs, all exact (integer sets / Fraction / Decimal-120), plain Python, single thread, no numpy, no BLAS,
nice 10, **no numeric lock taken and none needed** (brief rule 6); 36.1 s + 0.01 s + 0.0 s; exit 0 each; empty stderr each;
no process left. **Every criterion is labelled below as the criteria file requires.** OVERALL: **G PASS, A PASS, N PASS** —
and, as [RHW5-fix W5-1] demands, the substantive content behind those words is: **G3's PASS records the REFUTATION of the
reviewer's conjecture**, and **A3's report records that g²_CRC still breaches the recorded 10⁻⁹⁴ ceiling by ×11.16 once
node A's ring is bought** (it exceeds it by ×1.52 without the ring).
- **G1 (PRE-REGISTERED) PASS.** 320 samples (S-rand and the adversarially positioned S-adv) at depths 5/10/20/30:
  Σ^r(X) ⊆ N_t(π^r(X)) has **0 violations at t = 3 and t = 2, and 9076 at t = 1** (first witness at depth 5, r = 2, where
  |Σ²(X)| = 192 against |N_1(π²X)| = 81). Confirms Lemma SH-2 and its optimality.
- **G2 (PRE-REGISTERED) PASS.** The three translate identities of Lemma COV hold with **exact set equality** on every
  sample; the 2-translates-per-coordinate variant of the N_3 identity succeeds on **none**, so 3⁴ is minimal at radius 3
  and 2⁴ at radius 2.
- **G3 (PRE-REGISTERED; THE DECISIVE TEST) PASS = the additive form is REFUTED.** For P = {z}, Y = {z + 8e_1} at the
  all-ones base-3 position: E(M) = 109, 190, 325, 595, 838, 865 at M = 2, 5, 10, 20, 29, 30, i.e. **exactly 27M + 55**;
  every slope E(M+1) − E(M) = **27**; no constant tail; E(30) = 865 > 258 (the largest per-Y-cube excess any prior run
  recorded); ‖P∪Y‖_sh/‖P‖_sh = 1.3558 at M = 30, falling to 4/3. On S-adv samples with |Y| > 1 at depth 30 the excess
  reached 4235 per Y-cube and the ratio reached **5.714**.
- **G4 (CONFIRMATORY) PASS.** 0 violations of ‖P∪Y‖_sh ≤ 81‖P‖_sh + c_att(8)|Y| (session-5 c_att) on all 320 samples, and
  0 violations of the session-5 inequality. A reproduction check of Lemma SH-att′, not a pre-registration.
- **G5: REPORTED AS DEFECTIVE, not as evidence.** The pre-registered quantity max (‖P∪Y‖_sh − c_att|Y|)/‖P‖_sh came out
  0.0000 because with c_att(8) = 1229313 the subtracted term exceeds the whole norm on every sample; the criterion is
  identically ≤ 0 and carries no information. The informative looseness figure is G3's 5.714.
- **G6 (PRE-REGISTERED) PASS.** 0 violations of |sh_r(N_1 X)| ≤ 16|sh_r(X)| (r ≥ 1) and |N_1 X| ≤ 81|X|; the observed
  maxima are **3.373** per level and **2.783** for the whole r ≥ 1 sum, against PLD §18.4's quoted price 82 and §35.6's
  proven 17. So Lemma RING is right and still loose by ≈ 5.
- **A1, A6 (CONFIRMATORY) PASS; A4 (CONFIRMATORY) PASS.** §35.7's table is reproduced to all printed digits, and session
  5's own four numbers reproduce the review's S5-12 values (4.897894·10⁻⁹⁷ / 4.898021·10⁻⁹⁷ / 4.898012·10⁻⁹⁷ /
  9.991019·10⁹⁶ against 9.991038·10⁹⁶), with b_n = 20416938755 identical as an integer.
- **A2 (PRE-REGISTERED) PASS, and the answer was not knowable from the criteria.** At the session-6 constants the S5-12
  four-way coincidence **survives only if HIST's per-level constants are sharpened too**: spread **1.0001** with
  10001/10000, spread **3.8415** with HIST's 38417/38416 (where REL-boot and HIST-sum become binding at 2.33375·10⁻⁹⁶ and
  n_H = 2.09688·10⁹⁶ exceeds n_T by ×3.84). Pre-stated failure mode (W-F3), materialised and reported.
- **A3 (PRE-REGISTERED) PASS as a report.** Six scenarios: session 5 no ring 4.89789·10⁻⁹⁷ (BELOW 10⁻⁹⁴ by ×204.17);
  session 5 ring ×17 2.88112·10⁻⁹⁸ (×3470.9); session 5 ring ×82 5.97305·10⁻⁹⁹ (×16741.9); **session 6 no ring
  1.52362·10⁻⁹⁴ (ABOVE by ×1.52)**; **session 6 ring ×17 8.96376·10⁻⁹⁶ (BELOW by ×11.16)**; session 6 ring ×82
  1.85835·10⁻⁹⁶ (BELOW by ×53.81).
- **A5 (PRE-REGISTERED) PASS as a report.** Slack against DX′ (C_Ω = 1) at c_+ = 1: **×3.5855·10⁵⁶** (session 6, ×17
  ring); g²_CRC ≥ 2.5·10⁻¹⁵² while c_+ ≤ 6.0954·10⁵⁷. Session 5's own slack was ×1.9592·10⁵⁵.
- **N1, N2 (PRE-REGISTERED) PASS — §29's promised control, finally run.** Exact Fraction enumeration of the w5 Part-C toy
  at three grid points with 2z² ≥ 1 (2z² = 1.0614, 1.2661, 1.9583) and three with 2z² < 1 (0.7828, 0.9960, 0.9997, the
  first being w5's own maximum, reproduced). At every point above the threshold the bound 1/(1 − 2z²) is **VACUOUS**
  (1 − 2z² ≤ 0) while the exact ratio stays finite (1.956, 2.397, 13.370); below the threshold the exact ratio satisfies
  the bound everywhere. **So the pre-registered alternative "the bound must fail or the expansion must diverge" is
  realised as the DIVERGENCE OF THE BOUND.**
  **What this control does NOT show, stated plainly:** the exact ratio does not diverge at 2z² = 1 — at the near-threshold
  point 2z² = 0.9997 the bound is 3311 while the exact ratio is 2.152. The threshold 2z² < 1 is therefore an artefact of
  the per-step union bound, not a transition of the model. The control verifies that the stated threshold is where the
  BOUND stops being informative; it is weak evidence about the gas and no evidence at all about the YM chain.
- **Scope of w6, stated as §31's should have been.** G is exact geometry of ‖·‖_sh on Z⁴ and tests Lemmas SH-1, SH-2, COV,
  SH-att′, RING and Proposition SH-neg only. A is arithmetic of §35.7 with node-A constants scanned symbolically. N is a
  monotone toy in which Harris' inequality replaces node A and the induction. **Nothing in w6 touches Theorem CRC-2T′'s
  induction, (E2^𝔉′), (S1)'s convergence at the real constants, or the measure of the YM chain.**

## 40. Outcomes against the session-6 pre-stated targets (§34), status changes, and tally

- **W1 (a): MET and superseded.** The reviewer's free lever (6561 → 2401) is verified (Lemma SH-1) and then beaten:
  **Lemma COV gives 81** (§35.3).
- **W1 (b): DECIDED, in the negative.** **Proposition SH-neg (PROVEN-HERE)**: the additive form
  ‖P∪Y‖_sh ≤ ‖P‖_sh + c(ρ)|Y| is **FALSE**, with an explicit one-cube configuration whose excess is exactly 27M + 55 over
  M levels; the lemma the reviewer named as the missing step ("π^r(Y) ⊂ N_1(π^r(P)) ⇒ Σ^{r+c}(P∪Y) = Σ^{r+c}(P) for a
  fixed c") is false in the same configuration, where the two projections stay at distance 1 for ever. No multiplicative
  constant below 4/3 exists; the proven one is 81 and the samples force ≥ 5.714.
- **W1 (c): MET.** §35.7's table and ledger; **g²_CRC = 1.52362·10⁻⁹⁴/c_+ without node A's ring and 8.96376·10⁻⁹⁶/c_+
  with it (×311.1 on session 5 either way), n_♯ ≳ 3.21·10⁹⁴ resp. 5.46·10⁹⁵ (÷311.2), c_f ÷81.**
- **W1 (d): MET.** §35.7 (iii): ≈ 56 orders of slack against DX′; the breach is a bookkeeping event; HANDOFF's
  lower-g_0 instruction withdrawn (§41 item 1).
- **W2: MET.** §36: Theorem CRC-2T′ restated as an induction on N(R) = |S_R|, nothing weakened, the gas framing dropped,
  **§29 V2 (a) recorded NOT DELIVERED**, the off-route consumers named.
- **W3: MET, and largely by node A.** §37: (E2^𝔉′) with F_< quantified, the level-0 clause replaced and j = 0 recorded
  OPEN on both sides, seven deltas tabulated (five answered by PLD §18, one in HW's favour, one OPEN), the allowance
  clause restated as PLD Proposition PATCH's per-cube requirement with the patch form derived by monotonicity, the TF-1
  question recorded with both positions, and §24.3's doubt narrowed per S5-17.
- **W4: MET.** §38's eleven errata and §38.1's process debt; §29's never-run control run in §39 N.
- **Check w6: G PASS, A PASS, N PASS** (§39), with G3's PASS being a refutation and A3's a persisting breach.

**Session-6 tally (unreviewed).** Counted: **[HW-12]** the sharpened shadow geometry and the refutation of the additive
form — Lemmas SH-1, SH-2, COV, SH-att′, COL′, RING (all PROVEN-HERE, elementary) together with **Proposition SH-neg**
(PROVEN-HERE), which is what makes the package a result rather than a bookkeeping improvement. Total counted, all
sessions: 9 + 1 = **10**. [HW-11] is **re-labelled** (Theorem CRC-2T → CRC-2T′) and **not re-counted**. Uncounted:
Corollary H-geo′ (a re-derivation of HIST's own lemma), the verification of PLD §18.12 request 1 (§35.6 (c)), and the
erratum table.
**Status changes.** Lemma SH-att → superseded by **Lemma SH-att′** (6561 → 81; c_att(8) 1229313 → 320001). HIST H-geo (i),
(iii), (iv) → **sharpened and re-derived here** as Corollary H-geo′ (N_3 → N_2; 2401/38416/38417 → 625/10000/10001);
**HIST.md itself is NOT edited** and the request is §41 item 2. The additive form of SH-att: the reviewer's open conjecture
→ **REFUTED**. Theorem CRC-2T step (4): R″ → R‴, buying node A's extra R-free ring at **×17** on c_U (PLD's own price was
×82; Lemma RING). Constants: **g²_CRC 4.898·10⁻⁹⁷/c_+ → 8.964·10⁻⁹⁶/c_+** (with ring) **or 1.524·10⁻⁹⁴/c_+** (without),
**n_♯ 9.99·10⁹⁶ → 5.46·10⁹⁵ or 3.21·10⁹⁴**, **c_f 531441c_+ → 6561c_+**. §29 V2 (a): MET → **NOT DELIVERED**.
HANDOFF's "lower g_0, recheck the SF thresholds": **withdrawn**. REVIEW_HW_S5 S5-19 (TF-1 reinstates a node-A law
mismatch): **not propagated**, node A contradicting it; flagged for the lead. **H6′ = (E2^𝔉′) remains OPEN, and j = 0
remains OPEN on both sides — that, and not any constant, is the residual of the HW route.**
No literature result is load-bearing in §35-§38 beyond CE-geo′ (g1′) (PROVEN-HERE in PROOF L5 [S11]) and Harris'
inequality inside the toy control (not in any proof). No edits outside HW.md, HW_LOG.md, checks/w6*.

## 41. FOR OTHER FILES (not edited) — [RHW5-fix SC-1]

Nothing below is applied anywhere. Session 6 wrote only HW.md (appended), HW_LOG.md (appended) and checks/w6_*. No git
command of any kind was run; no commit, push or PR; no axiom edited; no other lane's file touched. **This section has been
missing since session 4 although §30.3, §30.7 and §32 raised demands on PLD and on RLARGE — that was a breach of the
brief's rule 8, and this is the repair.**

**1. To the lead (HANDOFF.md).**
- l.57-59 reads "The smallness condition tightens. The binding condition is g_K² < 4.9e-97/(c_A + c_U), and it fails the
  recorded ceiling of 1e-94. — g_0 therefore has to be lowered. — Recheck the downstream constants, including the SF
  thresholds." **Please withdraw the two instructions.** The honest replacement: *"This route's ceiling and threshold move
  by g-independent constants only. After session 6 the condition is g_K² < 8.96·10⁻⁹⁶/c_+ (c_+ = c_A + 17c_U), which is
  ×11.2 below the recorded (RLF-δ) ceiling 10⁻⁹⁴ but ×3.6·10⁵⁶ ABOVE the ceiling that actually binds the programme,
  g_0² ≈ 2.5·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 l.335, RLARGE l.618, REVIEW_RLARGE_V3 l.61). Nothing downstream needs to move and
  the SF thresholds do not need rechecking; the open risk is that c_A is uncertified (PLD l.1902)."*
- The disagreement to adjudicate: **REVIEW_HW_S5 S5-19 vs PLD §18.6.2 / §18.12 item 5** on whether §30.5's finer-first
  order reinstates a node-A law mismatch. §37 records both and sides with node A; nothing in §35-§38 depends on it.
- For the next review's brief: the single live wall in this lane is **one node-A statement** — the small-field moment under
  the exactly-converted law with a per-cube constant and no shadow sum, plus its level-0 case. Everything else in §30-§38
  is either proven or arithmetic.

**2. To HIST.md (owner of Lemma H-geo).** §35.2 proves, for an ARBITRARY set X of level-j cubes and every m ≥ 1,
**Σ^m(X) ⊆ N_2(π^m(X))** — radius 2, not H-geo (i)'s radius 3 — because π(N_2(B)) ⊆ N_1(π(B)) for L ≥ 3 makes radius 2 a
fixed point of the collar-plus-projection recursion. The proof is three lines and strictly sharpens; nothing weakens.
Consequences, if adopted: **H-geo (iii)** |sh_{j+m}(𝒟)| ≤ **625**(16 + 32(n−1)L^{−m}) in place of 2401(…); **H-geo (iv)**
Σ_{m=0}^{M}|sh_{j+m}(𝒟)| ≤ **10001n + 10000M** in place of 38417n + 38416M; hence **c_B := 10000B_0/log L** in Theorem
HIST-sum (HIST l.550), n_H and γ_H in proportion, and HIST l.551's condition
6400C_ℓe^{**10001**B_0}e^{−a/g_K²} ≤ ½. **Why it matters to this lane:** with HIST's 38417/38416 left in place, REL-boot's
r ≤ ½ and HIST-sum's own condition become the binding inequalities at 2.33·10⁻⁹⁶/c_+ instead of HW's 8.96·10⁻⁹⁶/c_+, i.e.
the ×3.84 that Corollary H-geo′ buys is lost at the lane boundary (check w6 A2, spread 3.8415 vs 1.0001). This is the
pre-stated failure mode (W-F3) and it has materialised. The optimality note is also worth recording: radius 1 does NOT
work (a single cube's shadow is a 4⁴-block, not a 3⁴-block), so 2 is the end of the line.
**Also for HIST's record:** §35.4's Proposition SH-neg shows that the per-level shadow of an attached cluster does **not**
merge into its anchor's: at the all-ones base-3 position two cubes at distance 8 have shadows that differ by 27 cubes at
every level, for ever. HIST §7.2's Reading ("its size settles at ≤ 2401·16 cubes per level") is unaffected, but any future
claim that attached shadows merge should cite this counterexample.

**3. To RLARGE.md (row 10g / critical-path item 1).** REVIEW_HW_S5 grepped RLARGE.md and found **no occurrence of "CRC" or
"(E2^𝔉)" at all**, while row 10g / critical-path item 1 still reads as "(CRC-1), a two-species cluster expansion". Three
corrections:
- **(CRC-1) is dissolved as a wall**: Theorem CRC-2T′ closes the same-level regress by inducting on the number of
  constrained pairs. It should be **struck from the critical path** — but note that (CRC) itself is NOT discharged: it is
  CONDITIONAL on (E2^𝔉′), so no file may write "(CRC) PROVEN" or treat H9 as closed.
- **The critical-path item should be re-labelled** "**(E2^𝔉′)**: good-buffer screening under the past law of every
  column-relaxed pattern, for the one weight h^{R,1}_j, with node A's allowance asked as a **per-cube constant with no
  shadow sum** (the union-form patch allowance then following by monotonicity), for levels j ≥ 1 — level 0 OPEN." It is
  **one node-A statement, not a cluster-expansion project**.
- **M-5 (PLD §18.9, agreed here).** Row 10b still asks for every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}} and every S ⊂ Λ_k. **Neither
  §24.3 nor §30.3 nor §37 asks that**, and neither PLD §17 nor §18 delivers it; the row should be restated to the
  (E2^𝔉′) form. Also: the coupling-ceiling rows that quote 4.9·10⁻⁹⁷ or 10⁻⁹⁴ for this route should quote §35.7's table.

**4. To PLD.md / node A (lane E) — the seven mismatches answered by number, and three deliverables from this side.**
- **M-1 (allowance; binding) — ACCEPTED AND IMPLEMENTED.** (E2^𝔉′) now asks the allowance as Proposition PATCH (v)'s
  **(P0) or (P1)**: *the moment carries at most a per-cube constant and no shadow sum*. HW derives the patch form itself by
  monotonicity (PATCH (i)); it is no longer a request. The slice is agreed to be **incomparable** and is not asked for by
  anyone. If §18.7 delivers **c_A = 0**, HW's constants improve by (c_A + 17c_U)/(17c_U) — please keep that claim visible,
  it is now the largest remaining lever on HW's ceiling.
- **M-2 (set class) — ACCEPTED, and the ring is BOUGHT, at a cheaper price than §18.4's.** §35.6 buys the extra R-free
  ring in step (4) (R‴ := R′^{−(Col(Y) ∪ Col(N_1(col 𝒟 ∪ Y)))}) and walks every subsequent step of the proof: **nothing
  else in Theorem CRC-2T reads R″ specifically** (§18.12 request 1's confirmation, now given — Y is fixed relative to R′
  before the extra relaxation; Buf^{R‴}_ρ ⊆ Buf^{R″}_ρ so E_Y only weakens; step (5)'s peel only gains). **And the price
  is ×17, not ×82: Lemma RING** (§35.6 (b)) proves |sh_r(N_1 X)| ≤ **2^d** |sh_r(X)| = 16|sh_r(X)| for r ≥ 1, because
  sh_r(X) = N_1(π(sh_{r−1}(X))) is **already N_1-thickened**, so N_1(sh_r(X)) = N_2(π(sh_{r−1}X)) is a union of 2⁴
  translates of sh_r(X) (Lemma COV at radius 2) rather than 3⁴. §18.4's 81 is |N_1(W)| ≤ 3^d|W| applied per level, which
  does not use that. Only the OPEN column enters #_{R′}, so the m = 0 term never appears and the clean statement is
  **c_+ = c_A + 17c_U**. Check w6 G6: 0 violations, observed maxima 3.373 per level and 2.783 in the r ≥ 1 sum — so even
  17 is loose by ≈ 5. Please re-read §18.4's "×82" as "×17" when quoting HW's constants.
- **M-3 (levels) — AGREED, and HW's own clause is FIXED.** §37 replaces l.1530's mis-levelled level-0 clause by (0a)
  Γ at level 0 with the Wilson window and **Y = ∅**, or (0b) Γ at level 1 with Y at level 0, and records that **node A
  delivers neither** and that j = 0 is OPEN on both sides. HW agrees this is the largest residual after the moment itself,
  because Lemma TEL-f needs every level: **the interface is not delivered**, and §32's H6′ row failed to flag it.
- **M-4 (weight class) — AGREED, and it cuts in HW's favour.** HW asks only for the one weight h^{R,1}_j (times the buffer
  indicator), i.e. PLD §18.7.0's 𝔏^buf_k. The "any w" / (E1) sup form is **not to be proven**: HW's own E1-1 expects it
  false, and §37 does not ask for it. Please do not spend labour there.
- **M-5 — see item 3 above (it is RLARGE's row, not HW's).**
- **M-6 (form) — AGREED.** (E2^𝔉′) is ONE joint expectation (the Γ-moment and the Y-probability under the same ν^w), which
  is what CAP-dec consumes; Cor. E2-RED's F-conditioned form is the right shape.
- **M-7 (F_<) — DONE.** (E2^𝔉′) now reads "for **every** bounded measurable F_< ≥ 0 that is a function of U_0, …,
  U_{k_0−1}". Free on both sides, as §18.6.2 Delta 3 says.
- **Three things from this side that node A may use.** (i) **Lemma RING** above (×17 for the ring). (ii) **Lemma COV** (a
  radius-s neighbourhood is a union of translates of the radius-1 one: 2^d at s = 2, 3^d at s = 3, 4) — it is what reduced
  HW's own 6561 to 81 and may do the same wherever PLD multiplies by |N_s|/1 rather than covering. (iii) **Corollary
  H-geo′** (per-level shadow 625/10000/10001), which shortens PLD's own quoted per-cube depth term from
  81 + 256(K − j − 2) only in its 2401-derived parts; PLD §18.6.1 (iii)'s 81 + 256(K−j−2) is the single-cube value and is
  unaffected, and PLD §18.6.1 (iii)'s quotation of HW's lemma should be updated to **‖P ∪ Y‖_sh ≤ 81‖P‖_sh + 320001|Y|**.
- **One warning for node A's §18.11 reading of HW's constants.** PLD §18.6.1 (v) and check p6 B2 quote b_n, b_D and
  g²_CRC in their session-5 form (531441·38418c_+ + 38417c_U, 4.8979·10⁻⁹⁷). Those are superseded by §35.7; the shape is
  unchanged, so "÷82" becomes "÷17" and the base value becomes 1.52362·10⁻⁹⁴/c_+.

**5. To whoever writes REVIEW_HW_S6.** Three places to attack first: (i) **Lemma COV's use in Lemma SH-att′ case (a)** —
it is where the factor 81 comes from, and the step that must be checked is that the WHOLE of Σ^r(P) together with ALL
case-(a) trees lies in the one set N_3(π^r(P)) (no per-tree multiplicity); (ii) **Proposition SH-neg's ζ_r ≡ 1 mod 3
claim**, which holds only for r ≤ M − 1 and which the whole refutation rests on; (iii) **§35.6 (c)'s walk of steps (4)-(7)
with R‴**, which is a proof-reading claim about text this session may not edit, and so is exactly the kind of claim that
should be re-walked by someone else. The arithmetic of §35.7 is reproduced in checks/w6_arith.py and is cheap to redo
independently in any exact-decimal toolchain.
