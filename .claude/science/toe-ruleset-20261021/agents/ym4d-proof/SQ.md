# SQ: lane G of the 4D YM proof push. Is the square-function estimate (SQ) needed, the sup-route price, and the linear (SQ) (session 1, 2026-10-28)

Scope. Constructive UV stability of 4D lattice SU(N) Yang-Mills, soft-kernel RG (decision 4, S4' contour averaging). This
file treats HIST.md's open item **(SQ)** (HIST §20.3 (A)) and the coordinator's question (lead's note from REVIEW_HIST_S3):
does RLARGE v2's branch (iii) (coherent-background price) need the energy form (AE) at all? It edits nothing except SQ.md,
SQ_LOG.md and checks/q*. HIST.md, RLARGE.md, PROOF.md, LINEAR_PACKAGE.md are read-only; proposals for them are marked
"proposal for the owner".

Status words as in PROOF.md / HIST.md: PROVEN-HERE (counted or not, said each time), CONDITIONAL (implication proven, its
hypotheses named), ARGUED, OPEN, HYPOTHESIS. "Given H" marks every hypothesis consumed. Literature tags [read],
[read-skim], [read-abs], [not-read]. No imported statement is load-bearing for a PROVEN-HERE claim.

Inputs read this session (read-only): HIST.md §0 (conventions), §15 (cones, E-loc, (AE), CLS-red, §15.5), §20-§23 (MSG,
MSG-loc, MS-HLS, (MS-Sob), (SQ), the k-fold counterexample, (AE) ⇐ MSG + MS-Sob, CLS-cone, (I_k^E)'), §21 (h6);
HIST_LOG.md (tail); checks/h6_criteria.md; LINEAR_PACKAGE.md §1-§3 (S4', Q_root = Q_str - d∘h, Setting SC, Lemmas 2.2-2.5,
Theorem 2.6, Lemma 2.7, Lemma 3.1, Proposition 3.3, Theorem 3.8); RLARGE.md §3.2-§3.4 (branches (ii), (iii), the case
split); REVIEW_HIST_S3.md l.150-175 (MSG questions, MSG-loc GAP S3-2), l.250-320 ((AE) ⇐ MSG + MS-Sob, CLS-cone, the
1e12 remark), l.430-486 (binding fixes, strategic verdict); PROOF.md l.2948-2962 (Lemma NA-alg (a), (b), statements only);
FLOW.md (grep of (SF-bg) only). Nothing in the literature directory was used.

---

## T. Pre-stated targets (written 2026-10-28 01:57 UTC, after reading the inputs above, after the coordinator's lead's
note, and after exploratory reasoning; BEFORE any written derivation (§0 onward) and before any checks/q* file; not
edited after the derivations start; outcomes are pointers in §9)

- **Target G0 (coordinator, first).** Decide whether branch (iii) consumes the energy form (AE)/(SQ), or whether a
  per-scale price under sup conditions suffices. Success: a verdict with a proof of whichever route is valid, at the level
  of named lemmas, with every hypothesis named. If the plain sup route (every-level-small chains, E-loc, sup control of the
  nonlinear terms) fails, say exactly where, and say whether a restricted sup route (minimiser chains) survives.
- **Target G1.** Restate (SQ) self-contained (deviation sources), linear and non-abelian forms.
- **Target G2.** Prove the linear (SQ) with a depth-uniform explicit constant (discrete Littlewood-Paley / multilevel
  Bessel bound for the pair (Q_2, I_2), with residual sources). Not success: a constant that depends on the depth k or on
  the torus side.
- **Target G3.** Say what the non-abelian (SQ) needs beyond G2, and whether (MS-Sob) + MSG ⇒ (AE) can be promoted;
  propose text for HIST's owner if so.
- **Checks (criteria first).** q1: the 1D multilevel Bessel constants of G2 computed exactly across depths, and the 4D
  linear (SQ) ratio on cone boxes at depths 1, 2. q2: the decay-class constant of the LINEAR cone-local minimiser across
  depths (d = 2 depths 1-5, d = 4 depths 1-2), the linear case of the hypothesis that G0's sup route consumes.

## T2. Session-2 pre-stated targets (written 2026-10-28 04:24 UTC (stat mtime 00:24 EDT), after reading REVIEW_SQ_S1 (binding), RTARGET §33 and
§48-49, PROOF.md BNA-F1/F2/F3, Theorem G♯_0-soft, LES-div, (G♯_0-fine) and the [S22] composite-route block (TOWER-VAR, COMP,
(CL-cl)), LINEAR_PACKAGE §1, §3, §4 and HIST §25.5/§26 (A5, AE-red); after exploratory reasoning on paper (a reflection
argument for the free-boundary cone box and a shift identity for residual sources were sketched, not written); BEFORE any
session-2 derivation in §11, before checks/q3_criteria.md and before any q3 script; REVIEW_S22.md did not exist at this time;
not edited after the derivations start; outcomes are pointers in §12)

- **Step 1.** Apply REVIEW_SQ_S1's binding fixes S1-1 … S1-6, §7 and M-1 … M-7, tagged [RSQ1-fix], including Corollary
  DESC-ε written fully. Tally to 6 / 2 / 2 unless a fix changes it.
- **Target Q3 (check q3, criteria first).** Measure, on the LINEAR cone-local chain with prescribed sources of unit weighted
  size, whether the weighted-sup response (the decay-class norm 𝔑 of (REG-min)) grows with the depth k. Three source
  classes, separated because they may behave differently: (A) residual (link) sources at every level, aligned at one coarse
  point; (B) a rough level-0 plaquette source (the Calderón-Zygmund case of BNA-F2); (C) a coarse-Lipschitz level-0 plaquette
  source (control). Reviewer's prediction (REVIEW_SQ_S1 S1-4): linear growth in k. Session-2 owner's prediction from the
  exploratory sketch: (A) depth-flat, (B) growing, (C) depth-flat. Jobs < 20 min, peak < 1 GB.
- **Target G4 (linear (REG-min), uniform in depth).** Prove that the linear cone-local free-boundary minimiser lies in the
  decay class Σ_dec with a depth-uniform constant (pure data), and extend to sources in the norms of RTARGET §33 (level
  weights, Hölder at level 0) as far as can be proven. Not success: a constant depending on k or on the box; a numerical
  constant quoted as proven; an anisotropic- or small-torus use of a LINEAR_PACKAGE theorem without saying so.
- **Target G5.** State exactly what the non-abelian (REG-min) needs beyond G4, item by item, against the B-NA items
  ((G♯), (R♯), BNA-F2, BNA-F3), PROOF [S22]'s COMP / (W1) / (CL-cl), and REVIEW_S22's background-field theorem (BFT) if
  that file exists by then.
- **Failure modes.** (Q3-F1) the (A) response grows (a level-sum loss for residual sources); (G4-F1) the free boundary
  defeats the torus kernels (no reduction to a torus); (G4-F2) the fine level needs more than sup data (only a Hölder or
  Lipschitz version holds).

---

# Derivations (written after §T; §0 started 2026-10-28 02:02 UTC)

## 0. Is (SQ) needed? (the coordinator's question, settled first)

**Verdict (details §0.1-§0.6).** Branch (iii) does NOT consume the energy form (AE) for general chains. It consumes only
a lower bound on the cone-local INFIMUM of the chain energy, i.e. a statement about MINIMISER chains (§0.1). For those, a
sup route exists and is written below: a descent to the finest sup-violation (Lemma DESC, PROVEN-HERE) plus a
linearisation theorem on a geometric-decay class (Theorem SUP-price, PROVEN-HERE given named, already-proven inputs), plus
one OPEN hypothesis, **(REG-min)**: τ-small cone-local minimisers decay geometrically in sup norm. (REG-min) is a
background-field regularity statement in weighted sup norms, the cone-local form of RLARGE's (BG)_k / FLOW's (SF-bg), which
are on the main path anyway (node A). It is subcritical: weighted sup norms make products summable, so Uhlenbeck-type ℓ⁴
criticality does not arise. **So (SQ), (MS-Sob), MSG-loc-dev and the general-chain (AE) leave the critical path for
branch (iii); CLS-red and CLS-cone become off-path results.**
**[RSQ1-fix S1-1, S1-3, S1-4, strategic 2: the four sentences above are corrected as follows; they are kept as written.]**
(1) The infimum form is EQUIVALENT to the every-chain form (a lower bound on an infimum holds iff it holds for every
competitor); what the infimum form buys is a PROOF METHOD (one may examine minimisers, which are attained), not a weaker
statement. (2) (REG-min) is NOT the cone-local form of (BG)_k / (SF-bg): it asks for ONE depth-uniform constant for the
multi-level decay across all levels (effectively (BG)_k's C_I = 1 plus summable corrections, uniformly in depth, on a
free-boundary cone box). It is B-NA-class (multi-scale Schauder, cone-local, free boundary), adjacent to PROOF's (G♯) and
SF's (MIN-reg). (3) "Subcritical" is withdrawn: in the MSG gauge the product rule fails for link × link terms (it loses
L^{k-i}), and a weighted-sup linear estimate with general level-0 plaquette-type sources meets BNA-F2's Calderón-Zygmund
log (§0.3, §11). (4) (SQ)/(MS-Sob) leave the critical path only CONDITIONALLY: DESC-ε (§0.3) derives every consumed
statement from (REG-min), so if (REG-min) is derived from the B-NA items that A5 needs anyway, the open-wall count drops
by one (a merger); until then (REG-min) is a second wall of B-NA difficulty and (SQ-dev) stays a parallel route (not
deleted, not "not consumed"). The plain sup route the note proposes (every-level-small
ARBITRARY chains, E-loc, sup control of the nonlinear terms) does not work as stated: sup bounds on the transported
quadratic errors are not depth-uniform (§0.2). It works once restricted to minimisers, because minimality is what supplies
the decay (§0.3-§0.4). The linear (SQ) is still proven below (§2-§5) as an off-path result. The reviewer's lead found it
"known in kind", and it costs one session.

### 0.1 What branch (iii) consumes (Lemma INF: PROVEN-HERE, elementary, not counted)
RLARGE §3.3 needs, for a level-(k+1) plaquette P with defect ||1 - V_P|| ≥ ε_1, a lower bound on the stage-k joint main term
u_k[Σ_x𝓔_{k,x}(U) + κΦ_k(U, V)] restricted to the cone 𝒞(P). Every term counted there is a term of ONE chain, namely the
minimiser of 𝓔_k(U) completed by V at level k + 1, and lies in 𝒞(P). Put
  **𝓔^{𝒞(P)}(V) := min{E_𝒞(P)(chain) : chains whose level-(k+1) links on ∂P are those of V}**
(cone-local, free boundary; E_𝒞 as HIST §15.1: s for level-0 plaquettes, κφ for kernel terms; the minimum is attained, being
a continuous function on a compact group power). Then the restricted main term is ≥ u_k𝓔^{𝒞(P)}(V). E_𝒞(P) is invariant
under the chain gauge (HIST F6), so 𝓔^{𝒞(P)} depends on V only through the conjugacy class of V_P. **Consequence:** the
consumed statement is (CLS-min): 𝓔^{𝒞(P)}(V) ≥ c_sf·min{||1 - V_P||², ε_1²}, which concerns minimisers of a cone-local
problem. HIST's (AE) (every chain) is strictly stronger than what is consumed.
**[RSQ1-fix S1-1: the last sentence is false and withdrawn.]** (CLS-min) ⟺ the same lower bound for EVERY chain on 𝒞(P)
with top V (if E(ψ) ≥ f for all ψ the infimum obeys it; conversely inf ≤ E(ψ)). Read: "the consumed statement may be
PROVEN by examining minimisers only (the infimum is attained), so regularity properties of minimisers become available".
**[RSQ1-fix S1-1a (definitional).]** "Restricted to the cone" means the SUM OF THE 𝒞(P)-TERMS of the chain (or of a
superset of them), not Σ_x𝓔_{k,x} over the cone's sites: the lexicographic term-to-cube assignment (HIST l.1406-1408) can
send a 𝒞(P)-term to a site outside the cone. INF also needs 𝒞(P) ⊂ 𝒞^♭(Λ_k), i.e. a FULL cone; boundary-adjacent defects
stay in E10.

Below, "level k" is the top of the cone (RLARGE's k + 1); sizes are op norms unless HS is said.

### 0.2 The plain sup route fails for arbitrary chains (method limit, not a counterexample)
Take a chain obeying MSG's hypotheses (i)-(ii) with ε at every level, in the MSG gauge (|a_i| ≤ C_Mε, HIST §20.2). The
exact recursion a_{i+1} = Qa_i - ρ̃_i + e_i (Lemma E2 below) and E-loc's identities give
log U_k(P) = d(Q^ka_0)(P) - Σ_i d(Q^{k-1-i}ρ̃_i)(P) + Σ_i d(Q^{k-1-i}e_i)(P) + (BCH terms at levels 0 and k).
With sup data only, |e_i| ≤ C_e(C_Mε)² per link, and the transported circulation obeys only
|d(Q^me)(P)| = |n_m^{-4}Σ_y∮_{∂sq_y}e| ≤ 4L^m·sup|e| (4n_m links per circulation); sup data carry no cancellation that
would improve this.
The level-0 BCH remainders contribute n^{-4}Σ_yΣ_{p∈sq_y}|R_p| ≤ n²·C_p(C_Mε)² with n = L^k. So the sup bound on the error is
of order (L^k + L^{2k})ε², while |log U_k(P)| ≤ C'ε (Lemma FORCE below): no depth-uniform comparison with √E_𝒞 or with
|log U_k(P)| follows. A depth-uniform bound for arbitrary every-level-ε chains needs an AGGREGATE of the link sizes. HIST
used ℓ⁴ (MS-Sob), and that is where (SQ) entered. A Balaban-style per-scale price at the level-k integration does not
avoid this by itself. In RLARGE's form (I_k^E), the effective action's main term at level k is u_k𝓔_k. Positivity of u_k𝓔_k
at a defect is (CLS-min) at one level. So "per-scale pricing" is (CLS-min), and the only question is how to prove (CLS-min).
**[RSQ1-fix §0.2 wording.]** "|log U_k(P)| ≤ C'ε (Lemma FORCE)": FORCE bounds ||1 - U_k(P)|| ≤ C'ε, and (F1) converts it to
|log U_k(P)|_op ≤ 1.011C'ε. The sentence "per-scale pricing is (CLS-min)" also answers REVIEW_HIST_S4 strategic 4: the
per-scale route avoids (MS-Sob) (through DESC), but not the constants (§0.3, Remark (a) as corrected).

### 0.3 The decay class and the sup-route price
**Definition (decay class Σ_dec(θ; C_D)).** A chain on 𝒞(P) (P a level-k plaquette) with θ := ||1 - U_k(P)|| is in
Σ_dec(θ; C_D) if (D1) ||1 - U_i(p)|| ≤ C_DθL^{-2(k-i)} for every level-i cone plaquette, 0 ≤ i ≤ k - 1, and (D2)
x_c := ||U_{i+1}(c) - W_0(M̄_c(U_i))|| ≤ C_DθL^{-2(k-1-i)} for every level-(i+1) cone link c, 0 ≤ i ≤ k - 1.
(The linear minimiser on the torus satisfies the curvature part with L^{-2} per level and residuals with L^{-3} per level,
LINEAR_PACKAGE Lemma 3.1 (c), Theorem 3.8. q2 measures the cone-local linear case.)

Constants (d = 4): A_d = (d - 1)L(L - 1)/2 (= 9 at L = 3), A_ax := 2(2L - 1) + (d - 3)(L - 1) (= 12; REVIEW_HIST_S3 fix S3-1,
the safe choice), p_L := 5L - 4 links per S4' contour (= 11; REVIEW_HIST_S3 l.252), B_1 := 3.011A_d + 1 + L² (= 37.1),
**K := C_D(1.011A_ax/L + 4B_1/(L - 1)) (= 78.3C_D), K_top := 1.011(K + C_D(1 + (A_d + 1)/L²)) (= 81.3C_D)**.

**Lemma MSG-dec (level-dependent MSG on the decay class): PROVEN-HERE [S1-G] (counted; a corollary of the proof of HIST
Theorem MSG).** Let the chain be in Σ_dec(θ; C_D) with C_Dθ ≤ ε_M (so MSG applies with ε := C_Dθ) and
66A_de^{4C_*C_Dθ}K²θ ≤ 2C_DB_1. Then the MSG gauge g satisfies **|a_i(b)| ≤ KθL^{-(k-i)}** for every level-i cone link,
0 ≤ i ≤ k - 1, and **|a_k| ≤ K_topθ** on P's links (a = log U^g, op norm).
*Proof.* MSG's steps (3)-(5) are inequalities between the sizes in the block pair of b and its coarse cells. They hold with
level-dependent maxima in place of the global ε: with ε^p_i := max level-i cone plaquette size (≤ C_DθL^{-2(k-i)}),
ε^r_i := max residual on level-(i+1) cone links (≤ C_DθL^{-2(k-1-i)} = L²·C_DθL^{-2(k-i)}), α_{i+1} := max_c|a_{i+1}(c)| and
κ_V := max_p||1 - V(p)||: (3)-(4) give ||U^g(b) - V(b)|| ≤ (2A_d + 1)ε^p_i + ε^r_i + A_dκ_V (the NA-alg term 18.4y² ≤ ε^p_i by
MSG's (S2), which holds with the smaller ε^p_i); (5) gives κ_V ≤ L^{-2}(1.011ε^p_{i+1} + 33α_{i+1}²e^{4α_{i+1}}). The quadratic
term is KEPT, not converted into ε (this is REVIEW_HIST_S3's GAP S3-2, avoided). Step (6) with (F3):
  α_i ≤ α_{i+1}/L + 2C_DθL^{-2(k-i)}(2A_d + 1 + L² + 1.011A_d) + 66A_dL^{-2}e^{4α_{i+1}}α_{i+1}².
Write α_i ≤ K_iθL^{-(k-i)}. Step (1) at level k - 1 (complete axial gauge on the top box, ladders of ≤ A_ax plaquettes):
α_{k-1} ≤ 1.011A_axε^p_{k-1} ≤ 1.011A_axC_DθL^{-2}, so K_{k-1} = 1.011A_axC_D/L. Dividing the recursion by θL^{-(k-i)}:
K_i ≤ K_{i+1} + (2C_DB_1 + 66A_de^{4α}K_{i+1}²θ)L^{-(k-i)}. Downward induction with K_{i+1} ≤ K and the smallness hypothesis:
K_i ≤ K_{k-1} + Σ_{m≥1}4C_DB_1L^{-m} ≤ K. α ≤ C_*ε (MSG) bounds e^{4α} by e^{4C_*C_Dθ}. Level k (MSG step (7) with level-dependent
sizes): ||1 - U^g_k(c)|| ≤ ||1 - hol_{U^g_{k-1}}(S_c)|| + (A_d + 1)ε^p_{k-1} + ε^r_{k-1} ≤ Lα_{k-1} + C_Dθ((A_d + 1)/L² + 1), then
(F1). ∎ Gauge invariance of all plaquettes and kernel terms (F6) keeps (D1)-(D2) unchanged by g.

**Lemma E2 (contour linearisation error): PROVEN-HERE [S1-G] (counted) given NA-alg (a) (PROOF.md, PROVEN-HERE there).**
In any chain gauge, let c be a level-(i+1) cone link, m := max|a_i| over the links of c's S4' contours, s := p_Lm, and assume
y_c := √N(s + 2s²e^s) ≤ 1/20 and |ρ̃| ≤ 1/20, ρ̃ := -log(W_0(M̄_c)^{-1}U_{i+1}(c)). Then
  **a_{i+1}(c) = (Qa_i)(c) - ρ̃ + e_i(c), |e_i(c)|_HS ≤ C_e(m² + m|ρ̃|_op), C_e := p_L²(13.3N + 2.2√N) + 8.9Np_L**
(Q the linearised S4' root map, LINEAR_PACKAGE §1.2; C_e = 3790 at N = 2, L = 3).
*Proof.* (i) Each contour T is a product of ≤ p_L factors e^{a_b}. (F5) and (F3) give |log hol(T) - Σ_{b∈T}a_b|_op ≤ 2s²e^s, so
Z_T := log hol(T) has |Z_T|_HS ≤ y_c. (ii) M̄_c = avg_Te^{Z_T}. NA-alg (a) gives W_0(M̄_c) = e^{X_0} with
|X_0 - Z̄|_HS ≤ 9.2y_c², Z̄ := avg_TZ_T, and |Z̄ - (Qa_i)(c)|_HS ≤ 2√Ns²e^s by (i) (Q is the contour average of Σ_{b∈T}a_b).
(iii) U_{i+1}(c) = e^{X_0}e^{-ρ̃}. For A, B in a Banach algebra with σ := |A| + |B|, the order-n parts of e^Ae^B and e^{A+B}
agree except in mixed words, whose total norm is ≤ (σ^n - |A|^n - |B|^n)/n! ≤ |A||B|2^nσ^{n-2}/n!. So
||e^Ae^B - e^{A+B}|| ≤ 2|A||B|e^{2σ}, and (F3) gives |log(e^{X_0}e^{-ρ̃}) - X_0 + ρ̃|_op ≤ 4|X_0||ρ̃|e^{2σ}. (iv) Collect, using
|X_0|_op ≤ |X_0|_HS ≤ 1.5y_c ≤ 1.8√Np_Lm for s ≤ 1/20, e^{2σ} ≤ 1.23 and HS ≤ √N·op: |e_i|_HS ≤ 2.2√Np_L²m² + 13.3Np_L²m² +
8.9Np_Lm|ρ̃|. ∎

**Lemma BCH-p (plaquette): PROVEN-HERE (not counted; (F5) + (F3)).** If the four links of a plaquette p have |a_b| ≤ m ≤ 1/40,
then |log U(p) - da(p)|_HS ≤ C_pm², C_p := 33√N, with log U(p) the principal log and da the oriented link sum.
**[RSQ1-fix M-1: C_p := 34√N.]** At the end of the range (4m = 1/10) the (F5)-(F3) bound is 2·2(e^s - 1 - s) = 33.09m² (op),
so 33√N is 0.3% too small there; C_p := 34√N holds on all of m ≤ 1/40. Every later use of C_p (SUP-price steps (3), (6),
C_err) reads 34√N; in use m ≤ K_topθ ≈ 10⁻⁶, and C_err, θ_0 move by < 3% (the figures of Remark (a) are the corrected ones).

**Theorem SUP-price ((AE) on the decay class, sup inputs only): PROVEN-HERE [S1-G] (counted) given NA-alg (a)-(b), RS (R1)
(ribbon bound, used through MSG), HIST Theorem MSG and E-loc's identities (all PROVEN-HERE in their files).** Let P be a
level-k plaquette (k ≥ 1, any T with level-k side ≥ 3) and a chain in Σ_dec(θ; C_D) with θ ≤ θ_♯(N, L, κ_-, C_D), where θ_♯ is
fixed by MSG-dec's two conditions, y_c ≤ 1/20 and NA-alg (b)'s smallness below, and **θ ≤ θ_0 := 1/(2C_err)**,
  C_err := C_p(K² + K_top²) + 4C_e[K²/(L(L - 1)) + 1.011KC_DL/(L² - 1)].
Then **E_𝒞(P) ≥ θ²/(4C_1), C_1 := ((2L - 1)/(L - 1))·max{2.06N, 32N/κ_-}** (C_1 = 160 at N = 2, L = 3, κ_- = 1).
*Proof.* Work in the MSG gauge of MSG-dec. (1) *Recursion.* Lemma E2 on every cone link, with m_i ≤ KθL^{-(k-i)} and
|ρ̃_i| ≤ 1.011x_c ≤ 1.011C_DθL^{-2(k-1-i)} (F1), gives a_{i+1} = Qa_i - ρ̃_i + e_i with
|e_i| ≤ C_e(K²θ²L^{-2(k-i)} + 1.011KC_Dθ²L^{-(k-i)-2(k-1-i)}). (2) *Linear identities (E-loc steps (1), (2), (4); linear, so
valid verbatim).* da_k(P) = d(Q^ka_0)(P) - Σ_{i<k}d(Q^{k-1-i}ρ̃_i)(P) + Σ_{i<k}d(Q^{k-1-i}e_i)(P), with
d(Q^ka_0)(P) = n^{-4}Σ_{y∈B_n(X)}Σ_{p∈sq_y}da_0(p) (n = L^k). (3) *Main term.* da_0(p) = log U^g_0(p) - R_p with |R_p| ≤ C_pm_0² ≤
C_pK²θ²n^{-2} (BCH-p). The weights n^{-4}#{y : p ∈ sq_y} sum to n², so the R-part is ≤ C_pK²θ². For the log part, E-loc step (3)
(Cauchy-Schwarz twice, any plaquette function) gives |n^{-4}Σ_yΣ_{p∈sq_y}log U^g_0(p)|_HS ≤ a_U, a_U² := Σ_{p∈R_0(P)}|log U_0(p)|²_HS.
(4) *Residual terms.* E-loc step (4): |d(Q^mρ̃_i)(P)| ≤ √8L^{-m}ρ_m, ρ_m² := Σ_{c∈R'_i(P)}|ρ̃_i(c)|²_HS, m = k - 1 - i.
(5) *Quadratic sources, by sup only.* |d(Q^me_i)(P)| = |n_m^{-4}Σ_y∮_{∂sq_y}e_i| ≤ 4L^m·max|e_i| (4n_m links, total weight). With
k - i = m + 1: 4L^m·max|e_i| ≤ 4C_eθ²(K²L^{-m-2} + 1.011KC_DL^{-2m-1}). Summed over m ≥ 0:
≤ 4C_eθ²[K²/(L(L - 1)) + 1.011KC_DL/(L² - 1)]. **This is where decay replaces (MS-Sob): the circulation gain L^m is beaten by the
squared decay L^{-2(m+1)}.** (6) *Top.* |log U^g_k(P) - da_k(P)|_HS ≤ C_pK_top²θ² (BCH-p). (7) *Collect.* With E-loc step (5)
(Cauchy-Schwarz with weights 1 and L^{-m}):
  |log U^g_k(P)|_HS ≤ √((2L - 1)/(L - 1))·(a_U² + 8Σ_mL^{-m}ρ_m²)^{1/2} + C_errθ².
(8) *Energy.* For ||1 - U|| ≤ ½ every eigen-angle t has |t| ≤ 0.506 and t² ≤ 1.03·2(1 - cos t), so
|log U_0(p)|²_HS ≤ 1.03||1 - U_0(p)||²_HS = 2.06N·s(U_0(p)). The plaquettes of R_0(P) are cone terms, each counted once. NA-alg
(b) with V = U_{i+1}(c) (so ρ = log(V^{-1}W_0) = ρ̃) gives φ_c ≥ |ρ̃|²/(2N) - (9.2y_c²/N)|ρ̃|² - e^{|ρ̃|}|ρ̃|³/(3√N) ≥ |ρ̃|²/(4N)
when 9.2y_c² ≤ 1/8 and e^{|ρ̃|}|ρ̃| ≤ 3/(8√N) (part of θ_♯). So 8Σ_mL^{-m}ρ_m² ≤ 32NΣ_cφ_c ≤ (32N/κ_-)Σκφ_c, each residual link
in exactly one R'_i. Hence |log U^g_k(P)|_HS ≤ √(C_1E_𝒞(P)) + C_errθ². (9) θ = ||1 - U_k(P)|| ≤ |log U_k(P)|_op ≤ |log U^g_k(P)|_HS
(|1 - e^{it}| ≤ |t|; conjugation does not change sizes). So θ ≤ √(C_1E) + C_errθ², and θ ≤ θ_0 gives θ ≤ 2√(C_1E). ∎
*Remarks.* (a) The θ-coefficient 1/(4C_1) = 1/640 is the E-loc constant up to the HS/energy conversions. The admissible
range θ_0 is tiny with these crude constants: C_e ≈ 3.8·10³, K ≈ 78C_D, so θ_0 ≈ 10⁻⁸/C_D² at C_D = 2. **No net improvement
over CLS-cone's C_cone ≳ 10¹² is claimed.** The improvement is structural: one depth-uniform constant from sup inputs,
with no ℓ⁴ step. The constants are not optimised (C_e and K are crude by orders of magnitude; h6 measured the MSG constant
at 3.5 against the proven 66). (b) No (MS-Sob) and no (SQ) is used: decay makes every transported source geometric.
**[RSQ1-fix M-6, S1-6: Remark (a)'s figures and its comparison are corrected.]** θ_0 ≈ 3·10⁻⁸/C_D² (the "10⁻⁸/C_D²" above
is 3× low). Recomputed by REVIEW_SQ_S1 (N = 2, L = 3, κ = 1): C_D = 0.45: K = 35.2, C_err = 3.3·10⁶, θ_0 = 1.5·10⁻⁷; C_D = 2:
K = 156, C_err = 6.6·10⁷, θ_0 = 7.6·10⁻⁹; C_D = 2.25: K = 176, C_err = 8.4·10⁷, θ_0 = 6.0·10⁻⁹. With DESC's binding entry
τ_♭ = θ_0/C' (C' = 53) the per-defect price is c_♭τ_♭² ≈ 1.2·10⁻²⁰ (C_D = 0.45), **≈ 3·10⁻²³ (C_D = 2)**, 2.0·10⁻²³
(C_D = 2.25). Against CLS-cone at ε_1 = 0.5 (ε_1²/(2NC_cone) with C_cone ≳ 10¹²-10¹⁵, i.e. 6·10⁻¹⁴ to 6·10⁻¹⁷), **the sup
route is a NET LOSS of 6-9 orders**, not "no net improvement" (its C_cone-equivalent at ε_1 = 0.5 is ≈ 2·10²¹ at C_D = 2).
Under A5's own ε_1 restriction (REVIEW_HIST_S4 strategic 4: CLS-cone price ≈ u_k·10⁻³¹/C_3) the two routes are of the same
order: DESC-ε's threshold η_♭ = c_♭τ_♭²/C'² ≈ 10⁻²⁶ gives ε_1 ≲ 5·10⁻¹⁴/√C_3 and a price ≈ 10⁻³³/C_3. Either way the price is
depth-uniform and g-independent (valid for a proof, with g² below it); a_coh becomes the binding entry of RLARGE §3.4's
a_♯ (a proposal for RLARGE's owner, not edited here). SUP-price itself acts only below θ_0; larger defects are priced
through the descent at τ_♭, which caps the price at c_♭τ_♭². C_e and K dominate C_err (h6 measured MSG at 3.5 against 66), so
optimisation could gain several orders: unclaimed.
**[RSQ1-fix M-2: θ_♯ listed.]** θ_♯(N, L, κ_-, C_D) := the largest θ satisfying all of: MSG-dec's two conditions
(C_Dθ ≤ ε_M and 66A_de^{4C_*C_Dθ}K²θ ≤ 2C_DB_1); y_c ≤ 1/20 at m ≤ K_topθ (y_c = √N(s + 2s²e^s), s = p_Lm); 9.2y_c² ≤ 1/8;
e^{|ρ̃|}|ρ̃| ≤ 3/(8√N) with |ρ̃|_HS ≤ 1.011√NC_Dθ; and BCH-p's m ≤ 1/40 at m = K_topθ. Numerically θ_♯ ≈ 3.5·10⁻⁶ at C_D = 2
(REVIEW_SQ_S1; MSG-dec's quadratic condition and ε_M/C_D bind), so θ_0 binds in DESC.

**Lemma FORCE (a small neighbourhood forces a small plaquette): PROVEN-HERE [S1-G] (not counted; lasso + RS (R1) + NA-alg
(a), as in HIST CLS-red step (β)).** Let q be a level-j plaquette (j ≥ 1). Suppose every level-(j-1) plaquette with vertices
in the endpoint blocks of q's four links has size < τ, and each of q's links has residual x_c < τ, with
τ ≤ τ_F := min{1/(20c'A'), 1/(18.4c'²A'²)} (c' := 4arcsin(¼)√N, A' := 2A_d). Then **||1 - U_j(q)|| ≤ C'τ, C' := L² + 4A_d + 8**
(= 53 at L = 3).
*Proof.* U_j(c) = W_0(M̄_c)·(W_0^{-1}U_j(c)) and ||1 - W_0^{-1}U_j(c)|| = x_c. Telescoping products of unitaries:
||1 - U_j(q)|| ≤ ||1 - Π_cS_c|| + Σ_c(||S_c - M̄_c|| + ||M̄_c - W_0(M̄_c)|| + x_c), S_c the straight centre segments. Π_cS_c is the
holonomy around the L × L square of level-(j-1) plaquettes spanned by the four centres: ≤ L²τ by (F4). Each S4' contour
differs from S_c by a ribbon of ≤ A_d level-(j-1) plaquettes in c's endpoint blocks (RS (R1)): ||S_c - M̄_c|| ≤ A_dτ.
||M̄_c - W_0(M̄_c)|| ≤ 18.4y², y := c'A'τ ≤ 1/20 (HIST §15.4 step (β), via NA-alg (a)), and 18.4y² ≤ τ by τ ≤ τ_F. ∎
**[RSQ1-fix M-3: strict form, and status.]** Let μ < τ be the actual maximum of the listed sizes (finitely many, all < τ).
The proof run with μ in place of τ (μ ≤ τ ≤ τ_F, so every smallness condition holds at μ; 18.4(c'A'μ)² ≤ μ) gives
**||1 - U_j(q)|| ≤ C'μ < C'τ, strictly**. This is the form DESC (a) uses (contrapositive: ||1 - U_j(q)|| ≥ C'τ forces a
listed size ≥ τ), and DESC (iii) uses θ_q ∈ [τ, C'τ). Status: PROVEN-HERE, NOT counted (a component of DESC); l.441's
"[FORCE counted with DESC]" is withdrawn (§10).

**Hypothesis (REG-min) [OPEN; P-weight: it is the cone-local, sup form of RLARGE (BG)_k / FLOW (SF-bg), node A].** There
are τ_R > 0 and C_D < ∞, depending only on (N, L, κ_±), such that for every depth k ≥ 1, every level-k plaquette q and every
minimiser U^q of E_𝒞(q) (cone-local, free boundary, q's four links fixed) whose level-i plaquettes (i < k) and residuals
in 𝒞(q) are all < τ_R: **U^q ∈ Σ_dec(||1 - U(q)||; C_D).**
*Proposed proof architecture [ARGUED, not written as a proof].* Let 𝔑(U) := max_i sup L^{2(k-i)}(plaquette sizes,
residual sizes at level i)/θ, the weighted (decay) norm. It is finite at finite depth. In the MSG gauge (links ≤ C_Mτ_R,
no decay assumed), the Euler-Lagrange equations of the cone energy are the linear soft-chain equations (LINEAR_PACKAGE
Lemma 3.1's system, gauge-invariant form) plus sources quadratic in the fields. Every quadratic source is a product of one
link-type factor bounded in UNWEIGHTED sup by C_Mτ_R and one factor bounded in the weighted norm. Two inputs would then give
𝔑 ≤ C_lin + C·τ_R·𝔑, hence 𝔑 ≤ 2C_lin, by absorption, with no uniqueness and no contraction mapping needed: (α) a weighted-sup
linear estimate (data θ on one plaquette, sources in the weighted norm, response in the weighted norm, uniform in depth),
the cone-local free-boundary form of LINEAR_PACKAGE Theorem 3.8 / Proposition 3.3 / §6.2; (β) the product rule just stated.
This is the subcritical (sup) analogue of Uhlenbeck's absorption. (SQ) needed it in ℓ⁴, where it is critical.
*Linear case.* Not proven here (Theorem 3.8 is the torus version with data on every coarse plaquette). Tested by q2.
**[RSQ1-fix M-4, S1-3, S1-4: statement, label and plan corrected; the text above is kept as written.]**
- *Statement (corrected).* "Residuals in 𝒞(q)" INCLUDES the top residuals on q's own four level-k links (their kernel terms
  are 𝒞(q)-terms; (D2) at i = k - 1 bounds them by C_Dθ). Cone-box and torus conventions as in SUP-price (level-k side ≥ 3;
  the cone 𝒞(q) full, ⊂ 𝒞^♭(Λ_k)). "For EVERY τ_R-small minimiser" is what DESC case (iii) uses ("some minimiser" would not
  suffice there). θ = 0 is consistent (the minimiser is flat).
- *Label (corrected).* NOT "the cone-local, sup form of RLARGE (BG)_k / FLOW (SF-bg)". (BG)_k (RLARGE l.326-328) is ONE level
  (curvature ≤ C_IL⁻²·(coarse) + quadratic; iterating gives C_I^{k-i}L^{-2(k-i)}); (SF-bg) (FLOW l.189-192) is analyticity
  with exponentially local derivatives at the trivial field, not a decay statement. (REG-min) asks for a **depth-uniform
  constant across all levels**. It is B-NA-class (multi-scale Schauder, cone-local, free boundary), adjacent to PROOF's
  (G♯) (BNA-F1: sources at every level need a new estimate) and SF's (MIN-reg) (coarse-unit a-priori closeness of minimisers;
  the decay class is its coarse-unit sup shadow). P-weight: a second wall of B-NA difficulty unless derived from the B-NA
  items (merger, §0 fix (4)). It is also the scale-weighted induction hypothesis (W1) that PROOF [S22] Proposition COMP names
  as a cure of COMP-F1 (cone-local form; §11.6), and the cone-local SIBLING (not a corollary) of REVIEW_S22's BFT-1 (Part 5;
  §11.6 states the exact dependence).
- *Plan: GAP (withdrawn as stated).* "Subcritical", "absorption … with no uniqueness and no contraction mapping needed" and
  the product rule (β) are WITHDRAWN. Two obstructions (REVIEW_SQ_S1 S1-4): **(β) is false in the MSG gauge**: decay-class
  links are only ≍ KθL^{-(k-i)} (one power of L per level), so a link × link source bounded as (unweighted C_Mτ_R) ×
  (weighted) is C_Mτ_RKθL^{-(k-i)} against the curvature weight θL^{-2(k-i)}: it loses L^{k-i}; the correct bound
  K²θ²L^{-2(k-i)} is QUADRATIC in 𝔑, and 𝔑 ≤ C_lin + Cθ𝔑² has a large branch that absorption cannot exclude (the a-priori
  finiteness 𝔑 ≲ τ_RL^{2k}/θ is useless); excluding it needs continuity along a family of minimisers or a contraction
  (uniqueness), which the plan disclaimed. **(α) meets BNA-F2**: a weighted-sup linear estimate with plaquette-type sources
  meets the Calderón-Zygmund failure of sup norms. Session 2 locates where the log enters: only at level 0 (residual sources
  at levels ≥ 1 cost no depth factor; §11.3, q3), where the fine box has L^k spacings, so the log of the box size is ∝ k.
  Re-plan (§11): the linear estimate in the RTARGET §33 Hölder pair (level weights, Campanato at level 0), then the product
  rule there in a smooth gauge and a contraction (which gives uniqueness, (a5-U), at the same time).
  **[RSQ2-fix S2-1a, S2-1b.]** The pointer "(residual sources at levels ≥ 1 cost no depth factor; §11.3, q3)" reads:
  "§11.2 (SHIFT), §11.4 (a); q3 A1 is consistent with SHIFT but is not a test of it (its zeros are exact by construction);
  see REVIEW_SQ_S2 R1". The re-plan's "(level weights …)" reads: "(level weights are needed for general co-closed currents
  j_l, RTARGET §33; not for PAIRED energy-residual sources, SHIFT)". Session 3 replaces this re-plan by §13 (RES-dec,
  STOKES-NA, RED-0).

**Lemma DESC (descent to the finest violation): PROVEN-HERE [S1-G] (counted).** Fix τ ≤ min{τ_F, τ_R, θ_0/C', ε_M/(C_DC'),
θ_♯/C', 1/(73.6Nc'²A'²)}. Order the cone objects by "height": level-i plaquettes have height i, residuals on level-i links
have height i - ½. An object VIOLATES if its size is ≥ τ. Given (REG-min), for every level-k plaquette P and every top datum:
  (a) if ||1 - V_P|| ≥ C'τ, then **𝓔^{𝒞(P)}(V) ≥ c_♭τ², c_♭ := min{1/(4C_1), 1/(2N), κ_-/(4N)}** (= 1/640 at N = 2);
  (b) if θ := ||1 - V_P|| < C'τ, then 𝓔^{𝒞(P)}(V) ≥ c_♭min{θ/C', τ}².
*Proof.* (a) Let U¹ be a minimiser of E_𝒞(P) with top V. Since ||1 - V_P|| ≥ C'τ, FORCE shows that U¹ has a violating object
below the top. Take a violating object ω of minimal height in 𝒞(P). Three cases. (i) ω is a level-0 plaquette:
s(U_0(ω)) ≥ ||1 - U_0(ω)||²/(2N) ≥ τ²/(2N). (ii) ω is a residual x_c ≥ τ on a level-(i+1) link: every level-i plaquette in c's
endpoint blocks has height < i + ½ and does not violate, so the contour spread is y ≤ c'A'τ, and KQ (lower; HIST Lemma KQ)
gives φ_c ≥ x_c²/(2N) - 18.4y²x_c ≥ x_c²/(4N) ≥ τ²/(4N), because x_c ≥ τ ≥ 73.6Ny². (iii) ω = q is a level-i plaquette,
i ≥ 1: every object of 𝒞(q) other than q has height < i and does not violate, so FORCE gives ||1 - U_i(q)|| ∈ [τ, C'τ]. Then
E_𝒞(P)(U¹) ≥ E_𝒞(q)(U¹) ≥ 𝓔^{𝒞(q)}(U¹|_{∂q}) (nesting 𝒞(q) ⊂ 𝒞(P), terms ≥ 0, U¹ is a competitor). Let U² be a minimiser of
the 𝒞(q) problem. If U² has no violating object below q, (REG-min) puts U² in Σ_dec(θ_q; C_D) with θ_q ∈ [τ, C'τ] ⊂ (0, θ_0],
and C_Dθ_q ≤ ε_M. Theorem SUP-price gives E_𝒞(q)(U²) ≥ τ²/(4C_1). Otherwise repeat with U² in place of U¹ inside 𝒞(q). Each
repetition lowers the height of the cone's top strictly, so the descent ends after ≤ 2k steps in case (i), (ii), or
(iii)-with-SUP-price. The inequalities chain. (b) If U¹ has no violating object, (REG-min) and SUP-price apply to U¹ itself:
≥ θ²/(4C_1). Otherwise run (a)'s descent from the first violation. ∎
*Consumption by branch (iii) (Corollary PRICE-iii: CONDITIONAL [S1-G] ⇐ (REG-min)).* With τ := τ_♭ (the maximal admissible τ
of DESC) and ε_1 ≥ C'τ_♭, every level-(k+1) defect P of RLARGE costs u_k𝓔^{𝒞(P)}(V) ≥ u_kc_♭τ_♭², depth-uniformly. In
min-form, 𝓔^{𝒞(P)}(V) ≥ (c_♭/C'²)min{||1 - V_P||², (C'τ_♭)²}. Defect sets at ONE level: the paying cones 𝒞(q*) ⊂ 𝒞(P) inherit
the overlap 24 (HIST §15.1), so the factor is 1/24 as in CLS-cone (c1). Multi-level defect sets still need disjoint
footprints (REVIEW_HIST_S3 fix S3-5 (c3) applies unchanged).

**Corollary DESC-ε (every chain, both AE-red conclusions): CONDITIONAL [S2-G] ⇐ (REG-min) (implication PROVEN-HERE;
reviewer-derived in REVIEW_SQ_S1 S1-2, every step re-checked here; [RSQ1-fix S1-2]).** Write τ_♭ := min{τ_F, τ_R, θ_0/C',
ε_M/(C_DC'), θ_♯/C', 1/(73.6Nc'²A'²)} (DESC's admissible range) and η_♭ := c_♭τ_♭²/C'². Assume (REG-min). Let P be a level-k
plaquette (k ≥ 1, level-k side ≥ 3) whose cone 𝒞(P) is full, and let U be ANY chain on 𝒞(P) (not necessarily a minimiser),
E := E_𝒞(P)(U).
- (i) *Sizes.* If 0 < τ ≤ τ_♭ and E < c_♭τ²/C'², then every object of 𝒞(P) below the top (every level-i plaquette, i < k,
  and every residual on a level-(i+1) cone link, 0 ≤ i ≤ k - 1, including P's four links) has size < τ.
- (ii) *Top.* Under the same hypothesis, θ := ||1 - U_k(P)|| ≤ C'√(E/c_♭).
- (iii) *AE-red's two conclusions.* If E < η_♭, then |log U_k(P)|²_HS ≤ (1.011²NC'²/c_♭)·E, and every level-i plaquette
  (i < k) and every residual of 𝒞(P) has size ≤ (C'/√c_♭)·√E (C'/√c_♭ = 53·√640 ≈ 1.3·10³ at N = 2, L = 3, κ_- = 1).
*Proof.* (i) Suppose some object below the top has size ≥ τ ("violates"); take a violating object ω of minimal height
(DESC's height: level-i plaquettes height i, residuals on level-i links height i - ½). Every term of E is ≥ 0.
Case ω a level-0 plaquette: E ≥ s(U_0(ω)) ≥ ||1 - U_0(ω)||²/(2N) ≥ τ²/(2N) ≥ c_♭τ².
Case ω a residual x_c ≥ τ on a level-(i+1) link c: the level-i plaquettes in c's endpoint blocks have height i < i + ½, so
they do not violate; the contour spread is y ≤ c'A'τ (HIST §15.4 (β)); KQ (lower) gives φ_c ≥ x_c²/(2N) - 18.4y²x_c ≥ x_c²/(4N)
since x_c ≥ τ ≥ 73.6Nc'²A'²τ² ≥ 73.6Ny² (τ ≤ 1/(73.6Nc'²A'²)); so E ≥ κ_-φ_c ≥ κ_-τ²/(4N) ≥ c_♭τ².
Case ω = q a level-i plaquette, 1 ≤ i ≤ k - 1: every object of 𝒞(q) other than q (plaquettes of levels < i, residuals on
links of levels ≤ i, including q's own links, height ≤ i - ½) has height < i and does not violate, so FORCE (strict form)
gives θ_q := ||1 - U_i(q)|| < C'τ, and θ_q ≥ τ since q violates. By nesting (𝒞(q) ⊂ 𝒞(P), HIST §15.1; 𝒞(q) is full because
𝒞(P) is) and nonnegativity, E ≥ E_𝒞(q)(U) ≥ 𝓔^{𝒞(q)}(U|_{∂q}) (U restricted to 𝒞(q) is a competitor). DESC (b) at depth i
(θ_q < C'τ, same τ) gives 𝓔^{𝒞(q)} ≥ c_♭min{θ_q/C', τ}² ≥ c_♭(τ/C')² (θ_q ≥ τ and C' > 1).
In every case E ≥ c_♭τ²/C'², contradicting the hypothesis. (ii) If θ ≥ C'τ, DESC (a) gives E ≥ 𝓔^{𝒞(P)}(U|_{∂P}) ≥ c_♭τ² >
c_♭τ²/C'², a contradiction. So θ < C'τ, and DESC (b) gives E ≥ c_♭min{θ/C', τ}²; the minimum cannot be τ (that would give
E ≥ c_♭τ²), so E ≥ c_♭θ²/C'². (iii) Given E < η_♭, choose δ > 0 with (1 + δ)²E < η_♭ and put τ := C'(1 + δ)√(E/c_♭) if E > 0
(then τ ≤ τ_♭ and E < c_♭τ²/C'²); (i) gives every size < C'(1 + δ)√(E/c_♭); let δ ↓ 0. If E = 0, (i) with every τ ∈ (0, τ_♭]
gives every size 0 and (ii) gives θ = 0. For the log: θ ≤ C'√(E/c_♭) ≤ C'τ_♭ ≤ θ_0 ≤ ½, so (F1) gives |log U_k(P)|_op ≤ 1.011θ
and |·|_HS ≤ √N|·|_op. ∎
**[RSQ2-fix M2-1 (optional sharpening).]** In (iii), level-0 plaquettes obey directly ||1 - U_0(p)|| ≤ √(2N s(U_0(p))) ≤
√(2NE) (= 2√E at N = 2); the stated C'/√c_♭·√E ≈ 1.3·10³√E is valid but crude for them.
*What it discharges (conditionally on (REG-min)).* (iii) is AE-red's statement (HIST l.1784-1789: |X|²_HS ≤ C'_AE·E and the size
clause with √C'', C_♮) with C'_AE replaced by 1.011²NC'²/c_♭ and both size constants by C'/√c_♭, on E < η_♭ in place of
E ≤ η_AE, and with NO (MS-Sob). So every consumer of AE-red's size clause (§0.5) may cite DESC-ε instead. Price of the
replacement: η_♭ ≈ 10⁻²⁶ (C_D = 2) against AE-red's η_AE; the constants are those of SUP-price (crude, unoptimised).
Status words: the implication is PROVEN-HERE [S2-G] (counted as CONDITIONAL, not as PROVEN).

### 0.4 Q_str may replace Q_root in linear computations (used by q2): PROVEN-HERE (not counted)
For the linear chain with top B_k, set λ_0 := 0, λ_{i+1} := avg(λ_i) + h(B_i) (h the slice functional, avg the block
average) and B'_i := B_i + dλ_i. Q_root = Q_str - d∘h and Q_str∘d = d∘avg give Q_strB'_i - B'_{i+1} = Q_rootB_i - B_{i+1}, so
residuals and curvatures are equal and B'_0 = B_0. The top moves by an exact form dλ_k. The Q_str-chain energy is invariant
under (dμ_0, …, dμ_k) with μ_{i+1} = avg μ_i, and avg is onto on the nested boxes. So the Q_str minimum with top B_k + dλ_k
equals the one with top B_k. Hence the two minima, and the curvatures and residual sizes of corresponding minimisers, agree.

### 0.5 What else might consume (AE)/(SQ)
HIST §20.3 (C): (I_k^E)' (a3) is an upper bound (no (AE)); (a4) uses (SF-bg) in local form with MSG as chart gauge (sup);
(b') needs no gauge. RLARGE §3.3 consumes CLS-sf only through branch (iii). Nothing else read this session consumes the
general-chain (AE). [The read covered RLARGE §3, HIST §15-§23; PLD.md was not read; the lead should confirm PLD does not
consume (AE) directly.]
**[RSQ1-fix S1-2: §0.5 was INCOMPLETE; the consumers of AE-red's SIZE clause were not read in session 1. Completed list
(read this session: HIST l.1404-1416, l.1672-1702, l.1784-1800; SF.md l.94-99, l.826-840; HW via REVIEW_SQ_S1 P1).]**
- **HIST Theorem A5 (A)** (HIST l.1684-1702): "every minimiser ψ* of E^♭(·; U) is ε_R-regular", proven via (a3-q) (E_𝒞(P)(ψ*) ≤
  4C_3ε_1² ≤ η_AE) and "Theorem AE-red (§26) and its size clause"; A5 is listed CONDITIONAL ⇐ … + (MS-Sob) "(the last through
  Theorem AE-red, §26)". Consumes the size clause.
- **HIST (I_k^E)' (a4)** (HIST l.1411-1415): "once the minimiser chain there is every-level ε-small (ε-regularity, CLS-red steps
  α-β, ⇐ (AE))". Consumes the size clause.
- **SF.md** l.97-99 ((BG-loc)'s content is A5 (A)-(C), "(i) ⇐ A5 (A) (real regularity via AE-red)", with (MS-Sob) in the
  hypothesis list) and l.838 (the STEP-3 wall list ends "(a3-q) on R_{3ε_1}, (MS-Sob)"). Consumes the size clause via A5.
- **HW TE (ii)** (via REVIEW_SQ_S1 Priority 1: W-bad, W-cb, Proposition FV are lower bounds on ℰ_P, the infimum form).
  Consumes the energy form in infimum form.
- **RLARGE §3.3 branch (iii)**: the infimum form (Lemma INF).
**All five are discharged by Corollary DESC-ε ⇐ (REG-min)** (the size clause and the every-chain energy bound, (iii); the
infimum bound, (ii) applied to a minimiser, or DESC (b)), on E < η_♭. So "(SQ)/(MS-Sob) leave the path" holds
CONDITIONALLY on (REG-min), and only as the merger of §0 fix (4). PLD.md: REVIEW_SQ_S1 grepped PLD.md, FLOW.md, RTARGET.md and
PROOF.md and found no (AE), AE-red, CLS or MS-Sob (not re-checked here).

### 0.6 Net
**[RSQ1-fix S1-3, S1-4, strategic 2: the paragraph below is superseded by: "Branch (iii)'s price and AE-red's two
conclusions ⇐ (REG-min) [OPEN, B-NA-class] + PROVEN pieces (INF, MSG-dec, E2, SUP-price, FORCE, DESC, DESC-ε as an
implication). The wall moves from '(SQ) in ℓ⁴' to '(REG-min)', which is NOT subcritical and is not the cone-local form of a
node-A statement; it is of B-NA difficulty. The move is a gain only as a merger, if (REG-min) is derived from the B-NA items
(§11.6). (SQ) and the general-chain (AE) remain true-in-kind and stay a parallel route."]**
Branch (iii)'s price ⇐ (REG-min) [OPEN] + PROVEN pieces (INF, MSG-dec, E2, SUP-price, FORCE, DESC). The critical-path wall
moves from "(SQ) in ℓ⁴" (critical, multi-session per REVIEW_HIST_S3) to "(REG-min): weighted-sup regularity of small
cone-local minimisers" (subcritical, the cone-local form of a node-A statement). (SQ) and the general-chain (AE) remain
true-in-kind, and are worth having as classical results, but are not consumed.

## 1. (Reserved: §T holds the targets.)

## 2. (SQ) restated, self-contained (Target G1)

**Setting.** d = 4, L ≥ 3 odd, h := (L - 1)/2. P a level-k plaquette. Its cone box at level j is the product of intervals
box_j := Π_μ[0, N_μ^{(j)}), with N^{(j)} = (2, 2, 1, 1)·L^{k-j} (HIST §15.1: W_P^{(j)}). Blocks nest: the level-j site x lies in
the level-(j+1) block ⌊x/L⌋, and the centre of the block X is c_X = LX + h.
- **2-forms, per component.** A level-j 2-form F has six components F^{(αβ)}. The base points of the (αβ)-plaquettes with all
  four vertices in box_j are x with x_a ∈ [0, N_a - 1) for a ∈ {α, β} (IN-PLANE directions) and x_a ∈ [0, N_a) for the two
  TRANSVERSE directions.
- **Q_2 (the plaquette form of the straight average; E-loc step (2), LINEAR_PACKAGE Lemma 2.2 (i)).** Q_2F(P') := L^{-4}Σ_{y∈B(X)}
  Σ_{p∈sq_y}F(p), sq_y the L × L square at y in P''s plane. It is the tensor product Q_2 = ⊗_aB_a of 1D maps: in-plane
  A[X, s] := L^{-1}T_L(s - LX), with T_n(u) := #{(a, b) ∈ [0, n)² : a + b = u}; transverse M[X, s] := L^{-1}1{s ∈ [LX, LX + L)}.
  d∘Q_str = Q_2∘d, and Q_2^m = Q_2^{(L^m)} (kernels L^{-m}T_{L^m}, L^{-m}1_{[0,L^m)}: generating functions,
  T̂_L(z^L)T̂_L(z)/L² = T̂_{L²}(z)/L², etc.; LINEAR_PACKAGE Lemma 2.4).
- **I_2 (the clamped Whitney 2-form interpolation, level j + 1 → j; HIST §20.1 (W3)).** I_2 = ⊗_aJ_a: in-plane
  J_0[x, X] := L^{-1} for x ∈ [LX + h, LX + h + L - 1] (the coarse cell between the centres X, X + 1), and 0 outside the hull of
  centres (W_2 vanishes in a clamped in-plane direction); transverse J_1 = the linear hat interpolation between the centres,
  with constant extension outside the hull. Then d∘I = I_2∘d (W3).
- **Linear chain.** B_{j+1} = QB_j - r_j (Q = Q_root), F_j := dB_j, so F_{j+1} = Q_2F_j - dr_j (dQ = dQ_str). The energy is
  E^lin_𝒞(P) = ½||F_0||²_{box_0} + Σ_j(κ_j/2)||r_j||²_{box_{j+1}}.
- **Deviation sources (level j, 0 ≤ j ≤ k - 2):** D_j := F_j - I_2F_{j+1} (level-j plaquettes of box_j), the residuals r_j, and
  the link source G_{j+1} := (1 - QI)a_{j+1} (level-(j+1) box links; a_{j+1} the linear MSG-gauge field, §5). Top: F_{k-1}.

**(SQ-lin).** Σ_{j=0}^{k-2}(||D_j||² + ||G_{j+1}||² + ||r_j||²) + ||r_{k-1}||² + ||F_{k-1}||² ≤ C_Q^lin·E^lin_𝒞(P), C_Q^lin
independent of k and T.

**(SQ-NA).** In the MSG gauge g, with V_j := exp(Ia_{j+1}) on level-j links (a = log U^g): Σ_j[Σ_p||U^g_j(p) - V_j(p)||² +
Σ_c x_c² + Σ_c||1 - hol_{V_j}(S_c)^{-1}W_0(M̄_c(V_j))||²] ≤ C_Q·E_𝒞(P) on every-level-ε chains, ε ≤ ε_Q. These are the
sources that a deviation-form MSG-loc (MSG-loc-dev, REVIEW_HIST_S3 fix S3-4) would consume (§6). In the linear case they
reduce to D_j, r_j and G_{j+1}.

**Why deviations (HIST's k-fold remark, restated).** ||Q_2F||² ≤ ||F||² with equality on constants (§3.0), so the curvature
sum Σ_j||F_j||² is ≍ (k - 1)||F_0||² for fields smooth at the top scale. D_j removes each level's interpolated coarse part.

## 3. One-dimensional multilevel Bessel lemmas (PROVEN-HERE [S1-G], counted as one item "B1D")

Normalised maps: Ã := L^{-1/2}A, M̃ := L^{1/2}M. Q_2^j = ⊗(normalised maps)^j exactly, because the four factors carry
L^{j/2}L^{j/2}L^{-j/2}L^{-j/2} = 1.

**3.0 Norms (Schur tests).** ||A|| ≤ √L (rows of A sum to L; columns to Σ_XL^{-1}T_L(s - LX) ≤ 1, since the values T_L(r) and
T_L(r + L) at one residue add to L). ||M|| ≤ L^{-1/2}. Hence ||Ã^j||, ||M̃^j|| ≤ 1, so ||Q_2^m|| ≤ 1 on every component.
||J_0||² = L^{-1} (each coarse X feeds L fine positions with weight L^{-1}). ||J_1||² ≤ L + h (Σ of the hat weights at a
coarse site is L, plus h clamped positions at the two ends). So ||J_0A|| ≤ 1, ν := ||J_1M|| ≤ √((L + h)/L) (= √(4/3)), and
||I_2|| ≤ ν².

**Lemma B-box.** φ_{j,X} := n^{-1/2}(1_{[n(X+1), n(X+2))} - 1_{[nX, n(X+1))}), n = L^j, j ≥ 0, X ∈ Z. Then
Σ_{j,X}|⟨φ_{j,X}, f⟩|² ≤ **β_M||f||², β_M := 4 + 8/(√L - 1)** (= 14.93). Note ⟨φ_{j,X}, f⟩ = ∇(M̃^jf)(X).
*Proof.* Schur test on the Gram matrix G: Σ|⟨φ_γ, f⟩|² ≤ ||G||·||f||² ≤ sup_γΣ_γ'|G_γγ'|·||f||². Same level: G = 2 on the
diagonal, -1 at X' = X ± 1, 0 otherwise: row 4. Levels j' < j (m := j - j'): φ_{j,X} is constant on level-j' intervals except
at its three breakpoints nX, n(X+1), n(X+2) (multiples of n, hence of n'), and φ_{j',X'} has zero sum and support
[n'X', n'(X'+2)), whose only interior multiple of n' is n'(X'+1). So G ≠ 0 only for the three X' whose midpoint is a
breakpoint, with |G| = n'^{1/2}·|jump of φ_{j,X}| = L^{-m/2}·(1, 2, 1). Row part 4L^{-m/2}. Levels j' > j: by the same argument
with the roles exchanged (φ_{j,X} sits inside one coarse piece unless its midpoint n(X+1) is a coarse breakpoint, which
happens for ≤ 3 X', with jumps 1, 2, 1): 4L^{-m/2}. Sum: 4 + 2·4Σ_{m≥1}L^{-m/2}. ∎

**Lemma B-tri.** ψ_{j,X} := n^{-3/2}(T_n(· - n(X+1)) - T_n(· - nX)). Then Σ_{j,X}|⟨ψ_{j,X}, f⟩|² ≤
**β_A||f||², β_A := 10 + 6/(√L - 1) + 14/(L^{3/2} - 1)** (= 21.53). Note ⟨ψ_{j,X}, f⟩ = ∇(Ã^jf)(X).
*Proof.* (a) *Summation by parts.* T_n'(· - c - n') - T_n'(· - c) = -Σ_{t<n'}[T_n'(· - c - t) - T_n'(· - c - t - 1)], hence for any g,
⟨g, ψ_{j',X'}⟩ = n'^{-3/2}Σ_{t<n'}Σ_vT_n'(v)(∇g)(v + c + t) and |⟨g, ψ_{j',X'}⟩| ≤ n'^{3/2}·max_{window}|∇g| (Σ_vT_n' = n'²).
(b) T_n has increments in {-1, 0, 1}, so |∇ψ_{j,X}| ≤ 2n^{-3/2}. (c) Entries: |G| ≤ 2L^{-3m/2} for every pair (apply (a) to the
finer functional with g the coarser one); 2 at m = 0. (d) Counts. supp ψ_{j,X} = [nX, nX + 3n - 2]. Same level: X' with
|X' - X| ≤ 2, five entries ≤ 2: row 10. Finer level j' = j - m: ≤ 3L^m + 3 overlapping X', row ≤ 6L^{-m/2} + 6L^{-3m/2}. Coarser
level j' = j + m: the overlapping X' form an interval of length < 4, so ≤ 4 of them: row ≤ 8L^{-3m/2}. Sum over m ≥ 1. ∎

**Lemma B-edge.** χ_{j,s} := n^{-3/2}T_n(· - ns), s ∈ {0, …, h - 1}, on Z_{≥0}. Then Σ_{j,s}|⟨χ_{j,s}, f⟩|² ≤
**β_E||f||², β_E := min{h, 3} + (h(h + 1)/2 + h)/(L^{3/2} - 1)** (= 1.477 at L = 3). The mirror family at the upper end has the
same constant, and the union has ≤ 2β_E. Note ⟨χ_{j,s}, f⟩ = (Ã^jf)(s), the level-j value at the in-plane position s.
*Proof.* Finer level j' = j - m, m ≥ 1: supp χ_{j',s'} ⊂ [0, (h + 1)n' - 2] ⊂ [0, n - 1] (since h + 1 ≤ L - 1 for L ≥ 3). There
T_n(u - ns) = 0 for s ≥ 1 and T_n(u) = u + 1 for s = 0. So the only nonzero entries are
⟨χ_{j,0}, χ_{j',s'}⟩ = n^{-3/2}n'^{-3/2}Σ_v T_n'(v)(v + n's' + 1) = (n'/n)^{3/2}(s' + 1) (the mean of T_n' is n' - 1). By symmetry the
coarser-level entries are (n/n')^{3/2}(s + 1) against s' = 0 only. Same level: ||χ||² = (2n² + 1)/(3n²) ≤ 1, and disjoint
supports for |s - s'| ≥ 2. The row sums give β_E. ∎

## 4. Theorem SQ-lin (the deviation square function, linear chain): PROVEN-HERE [S1-G] (counted)

**4.1 Deviation by gradient (PROVEN-HERE, not counted).** For a level-j 1D function f, put ∇f(u) := f(u + 1) - f(u). Edge(f) :=
Σ of |f|² over the 2h clamped in-plane positions (h at each end), where J_0 vanishes.
- In-plane: for x in the cell of X, (1 - J_0A)f(x) = Σ_sw_s(f(x) - f(s)), with w_s = L^{-2}T_L(s - LX) a probability on
  s ∈ [LX, LX + 2L - 2] and |x - s| ≤ 3h. By Cauchy-Schwarz twice, |·|² ≤ 3hΣ_{u∈W_X}|∇f(u)|², W_X := [LX, LX + 2L - 3]. There
  are L positions per cell, and each u lies in ≤ 2 windows. So **||(1 - J_0A)f||² ≤ 6hL||∇f||² + Edge(f)**.
- Transverse: the same, with the weights (1 - λ)/L, λ/L on the blocks X, X + 1, |x - s| ≤ 3h + 1, and the clamped ends
  inside the windows of the end cells (each u in ≤ 3 windows): **||(1 - J_1M)f||² ≤ 3L(3h + 1)||∇f||²**.
- Four directions. 1 - R_αR_βR_ρR_σ = (1 - R_α) + R_α(1 - R_β) + R_αR_β(1 - R_ρ) + R_αR_βR_ρ(1 - R_σ), the R_a = J_aB_a act
  on separate coordinates and ||R_in|| ≤ 1, ||R_tr|| ≤ ν. So with P := I_2Q_2,
  **||(1 - P)F||² ≤ (3 + ν²)[3L(3h + 1)Σ_a||∇_aF||² + Σ_{a in-plane}Edge_a(F)]** per component (6hL ≤ 3L(3h + 1)).
**4.2 The multilevel gradient and edge sums (PROVEN-HERE, counted with B1D).** For F_j = Q_2^jF_0 (one component),
∇_aF_j = (∇B̃_a^j ⊗ ⊗_{b≠a}B̃_b^j)F_0 = (1 ⊗ ⊗_{b≠a}B̃_b^j)(∇B̃_a^j ⊗ 1)F_0. The first factor is a contraction (§3.0), so
Σ_j||∇_aF_j||² ≤ Σ_j||(∇B̃_a^j ⊗ 1)F_0||² ≤ β_a||F_0||² by B-tri (a in-plane) or B-box (a transverse), applied on each line of
the other three coordinates. The functionals of the box are a subfamily of those on Z, with supports inside the box. The
edge sums are bounded by 2β_E in the same way.
**4.3 Statement.** For the linear chain on the cone box, every k ≥ 2 and T:
  **Σ_{j=0}^{k-2}||D_j||² ≤ C_main||F_0||² + C_res Σ_{j≤k-2}||r_j||²**, summed over components, with
  C_main := 3(3 + ν²)[3L(3h + 1)(2β_A + 2β_M) + 4β_E], C_res := 3[24(1 + ν²)²(L/(L - 1))² + 24ν⁴]
  (= 34203 and 1010 at L = 3; the per-component main constant without the factor 3 is 11401. q1's criteria quote the
  rounded values 34200 and 11400, i.e. 0.01% stricter than proven; disclosed in SQ_LOG).
*Proof.* F_j = Q_2^jF_0 - Σ_{i<j}Q_2^{j-1-i}dr_i and D_j = (1 - P)F_j + I_2dr_j. Main part: §4.1 + §4.2. Residual parts:
Q_2^mdr_i = d(Q_str^{(L^m)}r_i), and a Schur test (each plaquette of P''s plane reads the 4n links of ∂sq_y, each with weight
≤ n^{-4}; each link lies on ∂sq_y for ≤ 2n points y) gives ||Q_2^mdr_i||²_{(μν)} ≤ 8L^{-2m}(||r_{i,μ}||² + ||r_{i,ν}||²). Also
||1 - P|| ≤ 1 + ν², ||I_2|| ≤ ν², and Young's inequality Σ_j(Σ_iL^{-(j-1-i)}a_i)² ≤ (L/(L - 1))²Σa_i². Each link direction lies in
3 of the 6 planes, and (a + b + c)² ≤ 3(a² + b² + c²). ∎
**4.4 The remaining sources (PROVEN-HERE, not counted; constants not computed).** (i) ||r_j||² and ||F_{k-1}||² ≤ ||F_0||² +
C Σ||r||² (contraction, §3.0) are trivially in the energy. (ii) G_{j+1} = (S_c - Q)(Ia_{j+1}) (§5) vanishes on exact forms
(QI∘d = d) and, by LINEAR_PACKAGE Lemma 2.3 (ii) applied to B := Ia_{j+1} with the constant 2-form L^{-2}F_{j+1}(P_c),
|G_{j+1}(c)| ≤ 2(L - 1)L^{-1}·max over the coarse plaquettes near c of |F_{j+1}(P') - F_{j+1}(P_c)| inside the hull, plus
L^{-2}·2L(L - 1)|F_{j+1}(P_c)| for c whose window meets the clamped in-plane layer. So Σ_j||G_{j+1}||² ≤ C(Σ_j||∇F_{j+1}||² +
Σ_jEdge(F_{j+1})), which §4.2 bounds. **So (SQ-lin) holds with an explicit, depth-independent C_Q^lin** (bookkeeping of
the neighbourhood counts for G not carried out; Lemma 2.3 (ii) is PROVEN in LINEAR_PACKAGE).
**[RSQ1-fix S1-5: "explicit, depth-independent C_Q^lin" is an overclaim.]** Read: "depth-independent IN KIND; the counts are
open". Missing: the neighbourhood counts (how many G-links read one coarse plaquette difference), and whether the clamped
layer's coarse positions beyond s < h are covered (f(1) = f(0) + ∇f(0) would handle them). So (SQ-lin) is PROVEN for the
D_j, r_j and top parts with explicit constants, and for the G_{j+1} part in kind only.
**[RSQ1-fix M-5.]** In §3.0, ||I_2|| ≤ ν² holds for the normalised factors J̃_0 := L^{1/2}J_0, J̃_1 := L^{-1/2}J_1 (the
unnormalised product has the same norm, because the L-powers cancel across the four directions).

## 5. Linear MSG-loc in deviation form, and linear (MS-Sob): PROVEN-HERE [S1-G] (counted as one item)
Linear MSG: axial gauge on box_{k-1}, then λ_j at level j with λ_j(c_X) := λ_{j+1}(X) and ∫_{γ_x}(B_j + dλ_j) = ∫_{γ_x}Ia_{j+1}
along the axial paths γ_x inside blocks. With a_j := B_j + dλ_j and δ_j := a_j - Ia_{j+1}:
- intra-block b: δ_j(b) = ∮_{γ_xbγ_y⁻¹}δ_j = Σ_{ladder}±D_j (≤ A_d plaquettes, HIST MSG step (3));
- inter-block b (coarse link c): δ_j(b) = Σ_{ladders}±D_j + ∫_{S_c}δ_j, and ∫_{S_c}δ_j = (S_c - Q)B_j + r_j(c) =
  (S_c - Q)δ_j + G_{j+1}(c) + r_j(c), where (S_c - Q)δ_j = avg over contours of ribbon sums of D_j (≤ A_d plaquettes each) and
  G_{j+1} := (S_c - Q)Ia_{j+1} = ((1 - QI)a_{j+1})(c) by (W2). (Root covariance makes (S_c - Q)dμ = 0.)
So **|δ_j(b)| ≤ 2A_d·max_{block pair}|D_j| + |G_{j+1}(c)| + |r_j(c)|** exactly, with NO quadratic term (linear chain), and
|a_j(b)| ≤ L^{-1}max_{cell}|a_{j+1}| + |δ_j(b)| (W1). Iterating as in MSG-loc and applying HIST's Lemma MS-HLS with x_j := the
local maxima of these sources gives **Σ_{level-i box links}|a_i|⁴ ≤ C_S^lin(E^lin_𝒞(P))², C_S^lin := 24d·S_L·C_nb·(C_Q^lin)²**
(C_nb the neighbourhood-and-indexing factor of REVIEW_HIST_S3 fix S3-3, 5^d·L^d, not optimised). **This is the linear case
of (MS-Sob), depth-uniform.** The non-abelian MSG-loc-dev is not proven here (§6).
**[RSQ1-fix S1-5: status downgraded.]** C_S^lin contains (C_Q^lin)², whose G part is uncomputed (§4.4 fix). So §5 (linear
MSG-loc-dev + linear MS-Sob) is **CONDITIONAL ⇐ the §4.4 G-bookkeeping (neighbourhood counts), NOT counted**. The algebra is
CONFIRMED by REVIEW_SQ_S1 as an identity (intra-block δ = Σ±D_j; inter-block (S_c - Q)δ + G + r with G = ((1 - QI)a)(c) by
(W2); no quadratic term).

## 6. The non-abelian (SQ): status and what it needs (Target G3) — OPEN, off the critical path per §0
- The reviewer's GAP S3-2 stands. In ℓ⁴ (equivalently in the ℓ² square function) the quadratic BCH term of MSG's step (5)
  is a per-level source c_qα²: Σ_j Σ (α_j²)² ≍ Σ_j||a_j||⁴_{ℓ⁴}, which is ≍ k·E² for a field smooth at the top scale (each level
  carries ≍ θ⁴). So per-level absolute bounds on link-squared terms are k-fold lossy, exactly like curvature sources.
- What would close it [ARGUED]: every quadratic source must be shown to be of an admissible product type. Admissible means
  that the pointwise decay per level of the product (each factor bounded by its own MSG-loc-type coarse-dominated sum) is
  < L^{-2}, so that spreading to finer levels gains in ℓ². Admissible: link × curvature (L^{-1}·L^{-2}), link × link-variation
  (L^{-1}·L^{-2}), curvature × curvature, cubic link terms. Not admissible: link × link. The link × link part of BCH must
  cancel structurally between log U_j(p) and L^{-2}W_2(log U_{j+1}): the commutators [Ia, Ia] on fine plaquettes against
  the interpolated coarse commutators. For constant non-abelian links the S4' reflection symmetry kills the linear-in-offset
  commutator of each contour on average (avg_y t_ν = 0), and the W_2 convex combination of commutators differs from the
  commutator of convex combinations by a covariance (variation × variation). Making this a theorem for arbitrary
  every-level-ε chains is the multiscale Uhlenbeck estimate (REVIEW_HIST_S3); not attempted further here, because §0
  removes it from the path.
- MSG-loc-dev (intra-block, non-abelian), [ARGUED]. hol_U(π) - hol_V(π) via the lasso with common tails t_l gives
  ||U^g(b) - V(b)|| ≤ Σ_{p∈S}(||U^g(p) - V(p)|| + 2||t^U_p - t^V_p||·||1 - V_p||). The tail term is ≤ C·A_d·(tail length)·κ_V·max_block||U^g - V||
  and is absorbed (κ_V ≤ 2.02ε/L²). So the intra-block deviation is controlled by plaquette deviations alone. The
  inter-block step needs the Lipschitz bound of W ↦ W_0(avg_σ hol_W(ribbon loops)) at W = V, also lasso-based. Not written
  as a proof.

## 7. (AE) ⇐ MSG + (MS-Sob): proposal for HIST's owner (Target G3)
- Theorem SUP-price (§0.3) is (AE) on the decay class with C'_AE = 4C_1 (HS form |log U_k(P)|² ≤ 4C_1E_𝒞). Its proof is HIST's
  ARGUED (AE) proof with (MS-Sob) replaced by decay. Every error term is now written with a named constant (C_e, C_p, K,
  K_top, C_err), and the closing inequality is explicit: θ ≤ √(C_1E) + C_errθ². **Proposed text:** HIST §20.3 (A) could cite
  SQ.md Theorem SUP-price as the decay-class instance of (AE), PROVEN, and keep the general-chain (AE) ⇐ MSG + (MS-Sob) as
  ARGUED with REVIEW_HIST_S3's closing inequality (i).
- For the general (every-level-ε) chain the promotion still waits for (MS-Sob) in the non-abelian case (§6). Steps (4)-(5) of
  HIST's argument are sound given (MS-Sob) (REVIEW_HIST_S3 confirmed them). The new information here is that steps (4)-(5)
  are the ONLY places that need (MS-Sob), and that sup data with geometric decay replaces it (§0.3 step (5), and the level-0
  term C_pK²θ²).
**[RSQ1-fix §7: STALE; superseded by the following.]** HIST §26 now contains Theorem AE-red, (AE) ⇐ MSG + (MS-Sob), PROVEN as
an implication (HIST l.1784; REVIEW_HIST_S4 P6), so the ARGUED framing above is out of date. Against HIST §26:
- Theorem SUP-price is the decay-class instance of AE-red's energy conclusion, WITHOUT (MS-Sob): on Σ_dec(θ; C_D),
  θ ≤ θ_0, |log U^g_k(P)|_HS ≤ √(C_1E) + C_errθ² and θ ≤ 2√(C_1E). Decay replaces AE-red's ℓ⁴ steps (4)-(5) (transported
  quadratic sources become geometric, SUP-price step (5)).
- **Proposal for HIST's owner (text, not applied):** "HIST §25.5 Theorem A5 (A), (I_k^E)' (a4) and SF (BG-loc) (i) may cite
  SQ.md Corollary DESC-ε as an alternative to AE-red: CONDITIONAL ⇐ (REG-min) instead of ⇐ (MS-Sob), with C'_AE →
  1.011²NC'²/c_♭, size constant → C'/√c_♭, threshold η_AE → η_♭ = c_♭τ_♭²/C'² (≈ 10⁻²⁶ at C_D = 2). (REG-min) is B-NA-class
  (SQ.md §0.3, §11); the replacement lowers the open-wall count only if (REG-min) is derived from the B-NA items A5 needs
  anyway."

## 8. Checks q1, q2 (criteria first: checks/q1_criteria.md 02:00:56 UTC, checks/q2_criteria.md 02:01:15 UTC; scripts written after; records checks/q*_out.txt, q*_time.txt)
Smoke runs of REDUCED scratch copies (q1: L = 3 depths ≤ 6, L = 5 ≤ 3, 4D k = 2; q2: d = 2 k ≤ 3, d = 4 k = 1) under the
lock at 02:50 and 03:34 UTC; both ended in a KeyError in the final summary (the reduced copies lacked the depths that the
summaries index), after printing all their measurements. No criterion was edited.
- **q1 run 1** (lock 03:34:59 UTC) crashed in Part A (ARPACK non-convergence on the triangle family at large J;
  q1_out_firstrun_crash.txt). Crash fix (disclosed, not a criterion change): dense eigvalsh for frame sizes ≤ 2500 and
  ARPACK with ncv = 96 above. **q1 run 2** (lock to 03:51:52 UTC; 378 s; max RSS 782 MB, but the macOS "peak memory
  footprint" was 1052 MB, ABOVE the 1 GB cap; disclosed as a resource-rule breach; load 3.3-3.9, 40% free, nice 10, threads 1).
  **OVERALL: FAIL as pre-registered (A2); A1, B1, B2, B3 PASS.**
  - A1 PASS. Measured largest frame eigenvalues against the proven bounds (L = 3): box 9.29 (≤ 14.93), triangle 4.1053
    (≤ 21.53), edge (both layers) 1.159 (≤ 2.95). L = 5: 6.65 / 4.011 / 1.146 (≤ 10.47 / 16.23 / 4.98).
  - **A2 FAIL (box family only).** λ_box(J) = 3.73, 5.47, 6.66, 7.49, 8.09, 8.52, 8.85, 9.09, 9.29 (J = 1-9). It is still
    rising at J = 9 (λ(9)/λ(6) = 1.09 > 1.05). The increments 0.33, 0.25, 0.19 shrink by ≈ 0.77 per depth, which would put the
    limit near 9.9 [extrapolation, not measured], below the proven 14.93. The slow L^{-1/2} saturation is the box lemma's
    own cross-level decay rate. The criterion did not allow for it. Triangle and edge families are flat (4.1053 from J = 6
    on, to 4 digits; edge 1.155 → 1.159). The FAIL stands as recorded.
    **[RSQ1-fix: the "L^{-1/2} saturation" reading is dropped]**: the increments shrink by ≈ 0.7-0.83 per depth, not
    L^{-1/2} = 0.577; read "slow saturation". REVIEW_SQ_S1 showed the max |Gram| row sum is 4 + 4Σ_{m≤j}L^{-m/2} +
    4Σ_{m≤J-1-j}L^{-m/2} at the best row, so λ_box(J) < 14.93 for every J rigorously; the rising λ_box is not a threat.
  - B1 PASS. R_D ≤ 1.015 on every sample (bound 34200). Adversarial (Lanczos) per-component main-term eigenvalue: 1.1706
    (k = 2), 1.636-1.652 (k = 3), against 11400.
  - B2 PASS. Smooth field: the curvature-source sum R_F goes 1.000 → 1.929 (k = 2 → 3, the k-fold loss), while the
    deviation sum R_D goes 0.238 → 0.285.
  - B3 PASS. Q_2 maps constants to L²·constant exactly; I_2Q_2 reproduces constants on the interior; Q_2∘d = d∘Q_str to
    4.5·10⁻¹⁶.
- **q2** (03:36:41-03:36:48 UTC; 7.8 s, 223 MB, load 3.9, 44% free). **OVERALL: FAIL as pre-registered (C3, its d = 2
  half); C1, C2, C4 PASS.**
  - C1 PASS. All LSQR solves converged (relative normal residual ≤ 1.1·10⁻¹¹).
  - C2 PASS. **The linear cone-local minimiser lies in the decay class with a depth-flat constant.** d = 2:
    C_D(k) = 1.06, 1.87, 2.18, 2.24, 2.25 (k = 1-5), the curvature part dominant and saturating, with residuals ≤ 0.12·L^{-2(k-1-i)}.
    d = 4: C_D = 0.22, 0.45 (k = 1, 2).
  - **C3 FAIL (d = 2 half).** e(k) = E_min/θ² in d = 2 is 0.059, 0.0116, 0.0015, 1.7·10⁻⁴, 1.9·10⁻⁵, falling by ≈ L² per
    depth. That is the d = 2 scaling of the energy (θL^{-2m} on L^{2m} plaquettes), which the criterion did not account for:
    d = 2 is not scale invariant. The d = 4 half PASSES: e = 0.111, 0.105 ≥ 1/40.
  - C4 PASS (0.45 ≤ 2·0.22 + 1).
  - **[RSQ1-fix M-7: disclosure.]** checks/q2_decay_min.py has stat mtime 02:19:28 UTC, against its logged creation at 02:09
    UTC: an edit made after creation and BEFORE any run (first smoke 03:34 UTC), not logged in session 1. Its content is not
    recoverable now; REVIEW_SQ_S1 judged it harmless (the official run reproduces to every digit, and the script matches
    the criteria). [RSQ1-fix: q2 does NOT test (REG-min) with sources: no sources, the BNA-F1 data-kernel case; in d = 4 it
    covers two depths with C_D doubling 0.22 → 0.45; d = 2 is depth-flat but not scale invariant.]
- **Reading (post hoc, labelled).** (i) q1 supports (SQ-lin) strongly: the measured constants are O(1) (R_D ≈ 1, adversarial
  ≤ 1.65), while the proven constants are crude (10⁴). (ii) q2 is the first evidence for (REG-min)'s linear case: geometric
  sup decay with a constant that saturates in depth (d = 2: 2.25 at k = 5; d = 4: two depths only). It is not a proof, and the
  non-abelian case is untested.

## 9. Outcomes against the pre-stated targets (§T) (ADDED AFTER the derivations; pointers only)
- **G0: MET (verdict + proof of the valid route, conditional on one named OPEN hypothesis).** §0: branch (iii) consumes only
  the cone-local infimum (Lemma INF). The plain sup route fails for arbitrary chains (§0.2, method limit). The minimiser sup
  route is written: MSG-dec, E2, SUP-price, FORCE, DESC (PROVEN-HERE) ⇒ Corollary PRICE-iii CONDITIONAL ⇐ (REG-min) [OPEN].
  (SQ) and the general-chain (AE) leave the critical path.
  **[RSQ1-fix: read "leave the critical path CONDITIONALLY on (REG-min), as a merger only (§0 fix (4)); (REG-min) is
  B-NA-class; the infimum form is equivalent to the every-chain form (S1-1)".]**
- **G1: MET** (§2).
- **G2: MET for the D_j part with explicit constants (§3-§4: 34203||F_0||² + 1010Σ||r||²). The G_{j+1} part is reduced
  to the same gradient and edge sums via LINEAR_PACKAGE Lemma 2.3 (ii), with its neighbourhood counts not carried out
  (§4.4).** Depth-uniform, T-uniform. Linear MS-Sob follows (§5).
- **G3: partly MET.** Non-abelian (SQ): OPEN, the obstruction located (link × link BCH terms; §6). (AE) promotion: the
  decay-class instance is Theorem SUP-price (PROVEN-HERE). The general-chain promotion still needs non-abelian (MS-Sob);
  proposal text for HIST's owner is in §7.
- Checks: q1 FAIL as pre-registered (A2, slow saturation of the box family); q2 FAIL as pre-registered (C3 d = 2, energy
  scaling). Every other criterion PASSES; the readings are labelled post hoc.

## 10. Tally (this file) and hypotheses consumed
- **PROVEN-HERE, counted (8):** MSG-dec, E2, SUP-price, DESC, B1D (Lemmas B-box, B-tri, B-edge with §3.0 and §4.2),
  SQ-lin (D_j part), linear MSG-loc-dev + linear MS-Sob (§5), [FORCE counted with DESC]. **PROVEN-HERE, not counted:** INF,
  BCH-p, FORCE (as a component), §0.4 (Q_str ≡ Q_root for minima), §4.1, §4.4 (reduction of G to the gradient and edge sums).
  **CONDITIONAL (1):** PRICE-iii ⇐ (REG-min). **OPEN (2):** (REG-min) [P-weight, node-A-adjacent]; non-abelian (SQ) /
  MSG-loc-dev [off-path per §0]. **ARGUED:** (REG-min)'s proof architecture (§0.3); the non-abelian cancellation mechanism (§6).
  All items unreviewed.
- **Hypotheses consumed.** MSG-dec: HIST Theorem MSG's proof (steps (1)-(7)), RS (R1), NA-alg (a). E2: (F1)-(F5), NA-alg (a).
  SUP-price: MSG-dec, E2, BCH-p, E-loc identities (HIST §15.2 steps (1)-(5)), NA-alg (b). FORCE: (F4), RS (R1), NA-alg (a) via
  HIST §15.4 (β). DESC: FORCE, KQ (HIST Lemma KQ), SUP-price, (REG-min). SQ-lin: LINEAR_PACKAGE §1.2 (Q_root = Q_str - d∘h, root
  covariance), Lemma 2.4 (composites), HIST §20.1 (W1)-(W3) (Whitney forms), E-loc step (2); §4.4 also LINEAR_PACKAGE Lemma 2.3
  (ii). No literature item is load-bearing.
- **Not done / not claimed.** No edit to HIST.md, RLARGE.md, PROOF.md, LINEAR_PACKAGE.md. No commits, PRs, pushes, CL or
  axiom edits. PLD.md was not read (§0.5: the lead should confirm PLD does not consume the general-chain (AE)).
- **[RSQ1-fix: corrected session-1 tally (REVIEW_SQ_S1).]** **PROVEN-HERE, counted: 6** (MSG-dec, E2, SUP-price, DESC, B1D,
  SQ-lin D_j part). **CONDITIONAL: 2** (PRICE-iii ⇐ (REG-min); linear MSG-loc-dev + linear MS-Sob ⇐ §4.4 counts, uncounted
  as PROVEN). **OPEN: 2** ((REG-min); non-abelian (SQ) / MSG-loc-dev). Not counted: INF, BCH-p, FORCE, §0.4, §4.1, §4.4.
  Session 1 claimed 8 counted; its own list had 7. (REG-min)'s P-weight is "B-NA-class, not node-A-adjacent-cheap"; its
  plan is a GAP. Session-2 items are tallied in §12.

---

# Session 2 (2026-10-28 UTC; §T2 targets; derivations in §11 started 04:41 UTC, after q3 and q3b had run)

## 11. Linear (REG-min), uniform in depth (Target G4), and what the non-abelian (REG-min) needs (Target G5)

### 11.0 Setting
d = 4, L ≥ 3 odd, κ_- ≤ κ_i ≤ κ_+, κ̂ := κ_+/κ_-, n := L^k. P a level-k plaquette in the (0,1) plane; its cone box at level j is
box_j := Π_a[0, N_a^{(j)}), N^{(j)} := (2, 2, 1, 1)·L^{k-j} (§2); box_k carries exactly P's four links. Q := Q_str (§0.4; the
argument there is unchanged by the sources below, since B ↦ B + dλ leaves them untouched). The **linear cone-local chain with
sources**: unknowns B_0, …, B_{k-1} on all links of box_0, …, box_{k-1}; data B_k on P's links;
  **E^src(B) := ½||dB_0 + q_0||²_{box_0} + Σ_{i<k}(κ_i/2)||QB_i - B_{i+1} + s_i||²_{box_{i+1}}**
(q_0 a level-0 2-form on the box_0 plaquettes; s_i a level-(i+1) 1-form on the box_{i+1} links). Measured objects:
F̂_0 := dB_0 + q_0; F_i := dB_i (1 ≤ i ≤ k - 1); r̂_i := QB_i - B_{i+1} + s_i. Weighted norm (the decay class of §0.3, θ-free):
  **𝔑(B) := max{max_{i<k}L^{2(k-i)}sup|F̂_i|, max_{i<k}L^{2(k-1-i)}sup|r̂_i|}** (F̂_i := F_i for i ≥ 1).
Data size θ := |dB_k(P)|. Source sizes σ_r := max_iL^{2(k-1-i)}sup|s_i|, σ_0 := L^{2k}sup|q_0|, λ_0 := L^{3k}sup_{3-cells}|dq_0|
(coarse-unit Lipschitz size **[RSQ2-fix S2-2: read "coarse-unit sup of dq_0"; it sees only the exterior derivative]**), and the coarse-unit Campanato seminorm [q_0^c]_α of q_0^c := n²q_0 (RTARGET §33, scales
1/n ≤ ρ ≤ 1). A minimiser exists (a finite-dimensional quadratic form ≥ 0 plus linear terms, bounded below because
E^src ≥ 0). **Lemma TOP (data enter through θ only): PROVEN-HERE (not counted).** Two data with the same dB_k(P) differ by
dμ_k (a 1-form with zero circulation on the 4-cycle ∂P is exact); with μ_i on box_i, avg μ_i = μ_{i+1} (avg, the block
average, maps box_i onto box_{i+1} functions), B_i ↦ B_i + dμ_i preserves every r̂_i (Q∘d = d∘avg) and F̂_0, hence E^src
and every measured object. So one may take B_k := θ_P on the link (0, 0) → (1, 0) of P and 0 on the other three
(dB_k(P) = θ_P, ||B_k||_2 = θ).

### 11.1 Lemma REFL (the free-boundary cone box is the reflection-symmetric sector of a periodic chain): PROVEN-HERE [S2-G] (counted with Theorem REG-lin)
For a configuration (B_0, …, B_k; q_0, s) on the boxes define its extension to Z⁴ at every level by reflecting in each
coordinate a about the half-integer planes x_a = -½ and x_a = N_a^{(j)} - ½ (so with period 2N_a^{(j)}): with
R_a: x ↦ x', x'_a = -1 - x_a: (i) a link in a direction b ≠ a keeps its value at the mirror site; (ii) an a-link (x, x + e_a) is
sent to the a-link from -2 - x_a to -1 - x_a with the opposite sign; (iii) the "crossing" a-links (from -1 to 0 and from
N_a - 1 to N_a, and their periodic images) get 0; 2-forms (q_0) and 1-form sources (s_i) are extended by the same rules
(a component with one index equal to a changes sign; crossing plaquettes and crossing links get 0). Then, at every level:
- (a) ext commutes with Q, with d and with d* (on the full lattice), and ext(B_{i+1}) at level i + 1 is the reflection of
  the level-(i+1) box about the COARSE planes X_a = -½, N_a^{(i+1)} - ½;
- (b) every crossing plaquette has dB + q = 0, every crossing coarse link has QB_i - B_{i+1} + s_i = 0;
- (c) every non-crossing term of the periodic energy over one period cell (2⁴ copies of the box) equals the box term it is
  the image of, so E^per_cell(ext B) = 2⁴E^src(B);
- (d) the extension of a box minimiser is a minimiser of the periodic chain (torus of level-j side 2N^{(j)}) with the
  extended data and sources, and its d*-equations hold at EVERY link of Z⁴.
*Proof.* (a) Under R_a the level-i block LX + [0, L) goes to the block L(-1 - X) + [0, L) (since -1 - (LX + s) = L(-1 - X) +
(L - 1 - s)), so blocks go to blocks and the coarse reflection is X ↦ -1 - X, again about -½; the far plane likewise, since
N^{(i)} = LN^{(i+1)}. Transverse weights of Q are block indicators, invariant. Along a coarse a-link X → X + 1 the fine a-link
weights are L^{-1}T_L(s - LX), s ∈ [LX, LX + 2L - 2]; the mirror coarse a-link is -2 - X → -1 - X, and fine a-links map by
s ↦ -2 - s, with T_L(-2 - s - L(-2 - X)) = T_L(2L - 2 - (s - LX)) = T_L(s - LX) (T_n(u) = T_n(2n - 2 - u)); both sides change
sign, so Q∘ext = ext∘Q. d and d* commute with ext because ext is the pull-back by a lattice automorphism with its
orientation signs. (b) A crossing (a, b)-plaquette (b ≠ a) at x_a ∈ {-1, 0} has its two a-links crossing (value 0) and its
two b-links mirror images (equal values), so dB = 0; q is 0 there by (iii). A crossing coarse a-link c (X_a = -1 → 0): its
fine template s ∈ [-L, L - 2] is mapped onto itself by s ↦ -2 - s with equal weights and opposite values, so (QB_i)(c) = 0;
B_{i+1}(c) = 0 and s_i(c) = 0 by (iii). (c) A non-crossing plaquette lies in one copy. A non-crossing coarse link's fine
template lies in one copy: for an a-link X → X + 1, 0 ≤ X ≤ N_a^{(i+1)} - 2, s ∈ [LX, LX + 2L - 2] ⊂ [0, N_a^{(i)} - 2]; in a
transverse direction, [LX, LX + L) ⊂ [0, N^{(i)}); the other copies by symmetry. (d) The periodic energy E^per is convex and
invariant under the reflection group G (the data and sources are G-symmetric). For any configuration Y with the extended
data, the G-average Ȳ has the same data, lies in the image of ext (crossing values are odd, hence 0 after averaging), and
E^per(Ȳ) ≤ avg_gE^per(gY) = E^per(Y) by convexity. So inf E^per = inf over ext(·) = 2⁴·inf E^src, attained at ext of a box
minimiser. The d*-equations: at a box link (including the faces) the full-lattice d*-sum equals the box sum plus crossing
plaquettes, which vanish by (b); at a crossing link both sides are 0 (the box Euler-Lagrange right-hand sides extend by
(iii) and (a)). ∎
*Use.* REFL removes the free boundary: interior lattice estimates on Z⁴ (LES, LES-sup, LES-div) apply at every point of the
cone box, including its faces and edges. It needs no torus kernel and no lower bound on the torus side.

### 11.2 Lemma SHIFT (residual sources are a change of data): PROVEN-HERE [S2-G] (counted with Theorem REG-lin-src)
Put S_0 := 0, S_{i+1} := QS_i + s_i (S_{i+1} on box_{i+1}), and B̃_i := B_i - S_i (0 ≤ i ≤ k). Then QB_i - B_{i+1} + s_i =
QB̃_i - B̃_{i+1} and dB_0 = dB̃_0, so **E^src(B; B_k, s, q_0) = E^src(B̃; B_k - S_k, 0, q_0)** identically; minimisers
correspond, r̂_i = r̃_i, F̂_0 is unchanged, and F_i = dB̃_i + dS_i (i ≥ 1). Bounds: dS_j = Σ_{i<j}d(Q^{j-1-i}s_i) and, for any
level-l 1-form s and m ≥ 0, |d(Q^ms)(p)| ≤ 4L^m sup|s| (Q^m is the straight average over L^m-blocks, d(Q^ms)(p) =
L^{-4m}Σ_y∮_{∂sq_y}s over L^{4m} squares of 4L^m links: §0.2). So, at level j,
  L^{2(k-j)}sup|dS_j| ≤ 4σ_rΣ_{i<j}L^{2(k-j)+(j-1-i)-2(k-1-i)} = 4σ_rΣ_{i<j}L^{-(j-1-i)} ≤ 4σ_rL/(L - 1),
and in particular the new datum has |d(B_k - S_k)(P)| ≤ θ + 4σ_rL/(L - 1). ∎ *Meaning.* A residual source at level i
is carried by the coarser FIELDS (levels ≥ i + 1 have no curvature term), not by the fine curvature; its effect on the
datum decays like L^{-(k-1-i)}. No level sum arises. [q3 A1 measures this: every source below the top gives fine
response 0.0000 (the centred circulation transports to dS_k(P) = 0 exactly), and N = 4.0000 = its own circulation.]

### 11.3 Theorem REG-lin (linear (REG-min), pure data): PROVEN-HERE [S2-G] (counted; given LES-sup, LINEAR_PACKAGE Lemma 3.2' = PROOF l.2388, PROVEN there with an absolute uncomputed constant C_LES)
For every k ≥ 1, every κ_i ∈ [κ_-, κ_+] and every datum B_k (θ := |dB_k(P)|), with q_0 = 0, s = 0, every minimiser of E^src
on the cone box satisfies, uniformly in k:
- (a) ||r_{k-1}||_2 ≤ θ (so |r_{k-1}(c)| ≤ θ on P's four links);
- (b) sup|r_i| ≤ (κ_{k-1}/κ_i)L^{-3(k-1-i)}θ ≤ κ̂L^{-3(k-1-i)}θ (0 ≤ i ≤ k - 1);
- (c) sup|dB_0| ≤ C_0θn^{-2}, **C_0 := C_LES(√κ_+ + 16κ_+)**;
- (d) sup|dB_l| ≤ (C_0 + 4κ̂L²/(L² - 1))θL^{-2(k-l)} (1 ≤ l ≤ k - 1).
Hence **the linear cone-local minimiser lies in Σ_dec(θ; C_D^lin), C_D^lin := max{C_0 + 4κ̂L²/(L² - 1), κ̂}**, depth-uniformly,
with residual decay L^{-3(k-1-i)} (better than (D2)'s L^{-2(k-1-i)}). No Hölder norm, no level weight and no torus kernel is
needed for pure data.
*Proof.* (a) Lemma TOP and the competitor B_0 = ⋯ = B_{k-1} = 0 (r_{k-1} = -B_k, all else 0): E_min ≤ κ_{k-1}θ²/2. Since
(κ_{k-1}/2)||r_{k-1}||² ≤ E_min, (a) follows. (b) The Euler-Lagrange equation in B_{i+1} (1 ≤ i + 1 ≤ k - 1, no curvature term
at levels ≥ 1): κ_{i+1}Q^Tr_{i+1} - κ_ir_i = 0 on box_{i+1} links (Q^T the transpose of the box-restricted Q). ||Q^T||_{∞→∞} =
max column sum of Q ≤ L^{-3} (columns: Σ_XL^{-1}T_L(s - LX) ≤ 1 along the link, L^{-1} in each of the three transverse
directions, §3.0; the box restriction only removes entries). Iterate from (a). (c) The Euler-Lagrange equation in B_0:
d_box^T dB_0 = J := -κ_0Q^Tr_0 = -κ_{k-1}(Q^T)^kr_{k-1}, so sup|J| ≤ κ_{k-1}L^{-3k}θ by (a), (b). By REFL, F := d(ext B_0) on Z⁴
satisfies dF = 0 and d*F = ext J everywhere, |ext J| ≤ κ_{k-1}L^{-3k}θ. Apply LES-sup on Q_R(x_0), side R := 16n ≥ 16, for any
fine x_0 in box_0: sup_{Q_{R/2}(x_0)}|F| ≤ C_LES[(R^{-4}Σ_{Q_R(x_0)}|F|²)^{1/2} + R·sup|ext J|]. A window of R + 1 consecutive
sites meets ≤ 9 period copies of the box in an in-plane direction (copy length 2n) and ≤ 17 in a transverse one (length n),
so Q_R(x_0) meets ≤ 9²·17² = 23409 copies, each carrying Σ|F|² = ||dB_0||²_box ≤ 2E_min ≤ κ_{k-1}θ² (crossing plaquettes
carry 0). Hence R^{-4}Σ ≤ (16n)^{-4}·23409κ_{k-1}θ², whose square root is ≤ 0.6√κ_{k-1}θn^{-2}, and R·sup|ext J| ≤
16κ_{k-1}θn^{-2}. (d) On the box, d∘Q = Q_2∘d (the Q_2-template of a box_{i+1} plaquette lies in box_i, as for Q), so
F_{i+1} = Q_2F_i - dr_i, F_l = Q_2^lF_0 - Σ_{i<l}Q_2^{l-1-i}dr_i = Q_2^lF_0 - Σ_{i<l}d(Q^{l-1-i}r_i). Row sums of Q_2 are L²
(L^{-4}·L⁴ points·L² plaquettes), so |Q_2^lF_0| ≤ L^{2l}C_0θn^{-2} = C_0θL^{-2(k-l)}; and |d(Q^mr_i)| ≤ 4L^m sup|r_i| ≤
4κ̂L^{m-3(k-1-i)}θ (m = l - 1 - i). The weighted sum is 4κ̂θΣ_{i<l}L^{2(k-l)+(l-1-i)-3(k-1-i)} = 4κ̂θΣ_{i<l}L^{-(k-l)-2(l-1-i)} ≤
4κ̂θL²/(L² - 1). The decay class's (D2) is (b) (x_c is the residual size in the linear case). ∎
*Remarks.* (1) This is the cone-box form of the torus route N2-red/(H1) (PROOF l.2386-2396: LES-sup on the fine curvature
with the local energy and J-str (c)); REFL supplies the free boundary and the competitor supplies the local energy, which on
a cone is the whole energy. (2) q2 measured C_D = 0.22, 0.45 (d = 4, k = 1, 2), consistent with the proven bound, whose
C_LES is not computed. **[RSQ2-fix M2-3: read "not contradicted by" in place of "consistent with"; with C_LES uncomputed the
comparison is vacuous.]** (3) G4-F1 does not occur (no torus is needed); G4-F2 does not occur for pure data.

### 11.4 Theorem REG-lin-src (linear (REG-min) with sources): PROVEN-HERE [S2-G] (counted as one item; (a), (b) given LES-sup; (c) given LES-div, PROOF l.3394, PROVEN there with absolute constants)
Setting §11.0, d = 4, uniformly in k ≥ 1:
- **(a) residual sources at every level (q_0 = 0):** 𝔑 ≤ C_D^lin(θ + 4σ_rL/(L - 1)) + 4σ_rL/(L - 1). No level weights.
- **(b) a coarse-Lipschitz level-0 source (s = 0):** 𝔑 ≤ C_b(θ + σ_0 + λ_0), C_b depending only on (L, κ_±).
- **(c) a coarse-Hölder level-0 source (s = 0), 0 < α < 1:** 𝔑 ≤ C_c(θ + σ_0 + [q_0^c]_α), C_c = C_c(L, κ_±, α).
- (a)-(c) combine linearly (the problem is linear): 𝔑 ≤ C(θ + σ_r + σ_0 + [q_0^c]_α).
- **Boundary compatibility (part of the hypotheses of (b), (c)).** In (b), (c) λ_0 and [q_0^c]_α are those of the REFL
  extension ext q_0 (sup over all 3-cells, resp. all boxes, of Z⁴). A component q_{ab} with an index a normal to a face is
  odd under R_a and 0 on the crossing plaquettes, so ext q_0 is Lipschitz (Hölder) across that face only if those components
  vanish at the face to the same order (|q_{ab}| ≤ λ_0n^{-3} on the face-adjacent plaquettes, resp. the Hölder analogue).
  Without it, the face is itself a jump source (a free-boundary layer); (b), (c) are not claimed then. Components even
  under R_a need nothing.
- **[RSQ2-fix S2-2, S2-3, M2-4.]** (1) *Compatibility is NOT needed for (b).* On a crossing 3-cell (a, b, c) spanning
  x_a ∈ [-1, 0], the two (b, c)-faces carry the even component q_bc with equal values (contributing 0 to ∂_aq_bc) and the
  (a, b)-, (a, c)-faces are crossing plaquettes (0); so d(ext q_0) = 0 on crossing 3-cells and sup|d ext q_0| = sup_box|dq_0|
  for EVERY q_0 (the odd components' jump enters only ∂_aq_{a·}, which d of a 2-form never contains; REVIEW_SQ_S2 P4). (b)
  therefore holds without the compatibility hypothesis, strictly stronger than stated; compatibility is kept for (c), where
  d* contains ∂_a^*q_{a·}. (2) *Scope of (a).* "No level weights" means "no summable extra weights ω_l beyond the decay-class
  weights inside σ_r", for the class of PAIRED energy-residual sources (current κQ^Ts_i at level i with -κs_i at level
  i + 1); it does not cover RTARGET §33's general co-closed currents j_l, nor the unpaired Euler-Lagrange currents of a
  non-abelian minimiser (Remark (1)). (3) *(c) at k ≤ 2 (n < 16):* the finitely many Campanato scales give constants
  depending on L (not "as in PROOF").
*Proof.* (a) SHIFT reduces to pure data B_k - S_k with |d(B_k - S_k)(P)| ≤ θ + 4σ_rL/(L - 1); Theorem REG-lin bounds the
B̃-chain's weighted curvatures and residuals by C_D^lin times that; F_i = dB̃_i + dS_i adds ≤ 4σ_rL/(L - 1) (SHIFT); r̂_i = r̃_i;
F̂_0 = dB̃_0. (b) Competitor 0: E_min ≤ ½||q_0||² + κ_{k-1}θ²/2, ||q_0||²_box ≤ 6·4n⁴·sup|q_0|² = 24σ_0² (6 planes, 4n⁴
sites). Then ||r_{k-1}||_2 ≤ (θ² + 24σ_0²/κ_-)^{1/2} and (b) of REG-lin transports it. The B_0-equation reads
d_box^T F̂_0 = J (same J as before, now with this r_{k-1}), and dF̂_0 = dq_0 =: K, sup|K| = λ_0n^{-3}. REFL (q_0 extended by its
rule) and LES-sup on Q_{16n}, with the copy count of REG-lin (c) and ||F̂_0||² ≤ 2E_min ≤ 24σ_0² + κ_+θ²:
L^{2k}sup|F̂_0| ≤ C_LES[0.6(24σ_0² + κ_+θ²)^{1/2} + 16κ_+ sup|r_{k-1}| + 16λ_0] (the last two are n²·R·sup|J| and n²·R·sup|K|). Levels l ≥ 1: F_l = Q_2^l(F̂_0 - q_0) -
Σd(Q^{l-1-i}r_i), and |Q_2^lq_0| ≤ L^{2l}sup|q_0| adds σ_0 to the weighted bound; the residual part is as in REG-lin (d).
(c) On the period cell (a torus of fine side 2N^{(0)}) let B^C := ext B_0 - dΔ^{-1}d*(ext B_0) (Coulomb representative;
d*B^C = 0, dB^C = d ext B_0). On the flat torus Δ acts componentwise (LINEAR_PACKAGE §1.1), and ΔB^C = d*dB^C =
ext J - d*(ext q_0), i.e. componentwise LES-div's form -Δu = Σ_a∂_a^-g_a + h with g := ±(ext q_0) components and
h := ±(ext J) (the signs are those of d*; only |g|, |h| and [g]_α enter). LES-div on Q_n(x) (n ≥ 16, i.e. k ≥ 3 at L = 3;
for smaller n the Campanato scales are finitely many, as in PROOF l.3432-3437) gives, in coarse units f := n²∇B^C, for
coarse scales 1/n ≤ ρ_c ≤ 1/4, exactly as in PROOF's (G♯_0-fine) conversion (l.3405-3416, every power of n cancelling):
  [f]_{α; ≤1/4} ≤ C_α[ψ^{1/2} + [q_0^c]_α + κ_{k-1}sup|r_{k-1}|], ψ := Σ_{period cell}|∇B^C|² = ||d ext B_0||² = 2⁴||dB_0||²_box
(on the torus Σ|∇B|² = ||dB||² + ||d*B||²), and ||dB_0||² ≤ 2||F̂_0||² + 2||q_0||² ≤ 4E_min + 2||q_0||² ≤ 96σ_0² + 2κ_+θ².
Campanato to sup: telescoping the box means of f from Q_{n/4}(x) down to the single site (as in LES-sup's proof) gives
|f(x)| ≤ |mean_{Q_{n/4}(x)}f| + C_α[f]_α, and |mean_{Q_{n/4}}f| ≤ (|Q_{n/4}|^{-1}Σ_{Q_{n/4}}|f|²)^{1/2} ≤ ((4/n)⁴·n⁴ψ)^{1/2} =
16ψ^{1/2} (|f|² = n⁴|∇B^C|², |Q_{n/4}| ≥ (n/4)⁴; Q_{n/4}(x) lies in one period cell). So n²sup|∇B^C| ≤ C(σ_0 + θ + [q_0^c]_α), and L^{2k}sup|F̂_0| ≤ 2n²sup|∇B^C| + σ_0. Levels l ≥ 1 as in (b). ∎
*Remarks.* (1) (a) is the reason the reviewer's predicted level sum does not occur for residual sources: they are
jointly gauge-orthogonal pairs (current κQ^Ts_i at level i, -κs_i at level i + 1), not levelwise co-closed currents, and
SHIFT telescopes them. For general divergence-form currents j_l = d*G_l at every level, Theorem G♯_0-soft (PROOF l.3363)
does show the marginal count (G0-F1: Ω < ∞ needed); via REFL it should transfer to the cone box, but its torus is then
anisotropic with level-k side (4, 4, 2, 2), and G♯_0-soft is stated for isotropic tori: [inference, not checked; not
claimed]. (2) (b)-(c) need derivative or Hölder control of the level-0 source. With σ_0 alone the LES-sup route gives
L^{2k}·n·sup|K| ≤ 6σ_0n, a loss of n (crude; the true loss for curl-ful sources is expected to be a Calderón-Zygmund
log ∝ k). q3 (B) (d = 3: R_ctr = 0.90, 1.75, 2.67) and q3b (B4) (d = 4: 0.995 → 2.014) show growth for the extremal sign
pattern; q3b (C4) (0.113 → 0.079) and q3's centre value for (C) (0.113, 0.091, 0.100) are flat. G4-F2 OCCURS for level-0
plaquette sources: sup data are not enough, Lipschitz or Hölder data are.
**[RSQ2-fix S2-4d.]** "G4-F2 OCCURS" reads: "G4-F2 is EXPECTED (the classical L^∞ unboundedness of Calderón-Zygmund
operators [literature, not proven here], LES-sup's method loss of n, weak numerics); not proven. sup|q_0| + sup|dq_0|
suffices (REG-lin-src (b))". Remark (1)'s first sentence is scoped as in S2-3 (paired energy-residual sources only).

### 11.5 Checks q3, q3b (criteria first: checks/q3_criteria.md 04:26:02 UTC, checks/q3b_criteria.md 04:38:20 UTC; records checks/q3*_out.txt, q3*_time.txt)
- **q3** (lock 04:29:56-04:31:03 UTC; 66.4 s; peak footprint 203 MB; load 5.4, 40% free). **OVERALL: FAIL as pre-registered
  (QA, QC); Q1, QB PASS.**
  - QA FAIL (its d = 3 half). (A) N_0: d = 2: 4.26, 7.49, 8.73, 8.96, 8.99 (k = 1-5, flat: PASS); d = 3: 2.19, 4.01, 6.26 (grows).
  - QB PASS. (B) R_ctr = 0.897, 1.749, 2.673 (d = 3, k = 1-3).
  - QC FAIL. (C) N_0 = 0.173, 0.203, 0.276 (grows); its centre value R_ctr = 0.113, 0.091, 0.100 is flat.
  - Information. A1: every single-level source below the top gives N_0 = R_ctr = 0.0000 and 𝔑 = 4.0000 (its own
    circulation), at every d and k; the (A) response equals the top-source response to every printed digit. d = 4 (A):
    N_0 = 0.890, 0.840. A2 (random signs) is dominated by the random top datum (e.g. d = 2 N_0 = 0.009 at k = 4, 4.84 at k = 5).
- **q3b** (d = 4, k = 1, 2; lock 04:38:46 UTC, 0.56 s, 87 MB; load 2.3, 56% free; written after q3, disclosed). **OVERALL:
  PASS (R1, RB, RC)**: (B4) R_ctr = 0.995 → 2.014 (grows); (C4) N_0 = 0.113 → 0.079 (flat). Two depths only: a weak test.
- **Reading (post hoc, labelled).** (i) The d = 3 failures are a criterion-design error of the same kind as q2's C3: the
  decay-class weights are the d = 4 (scale-invariant) ones, and in d = 3 the PURE-DATA response itself grows (the (A)
  response is the top-source = top-datum response, by A1 and SHIFT); so d = 3 cannot separate a depth log from d = 3 scaling.
  (ii) A1 is the measured form of Lemma SHIFT: residual sources below the top produce no fine response at all for the
  centred pattern, so the level-sum mechanism predicted by REVIEW_SQ_S1 S1-4 does not occur for residual sources. (iii) For a
  curl-ful level-0 source (|dq| ~ |q|) the weighted response grows with depth in d = 3 (three depths, increments 0.85, 0.92:
  consistent with a log ∝ k, not separable from a power at three points) and in d = 4 (two depths). For coarse-Lipschitz
  sources it is flat in d = 4. Caveat: the (C)/(C4) sources do not satisfy §11.4's boundary compatibility at the in-plane faces
  (their (0,1) component is nonzero there); they are flat anyway, so the boundary layer did not dominate at these depths.
  **Answer to Q3:** the sup-norm decay loses a depth factor for curl-ful level-0 plaquette sources (the BNA-F2 / CZ case,
  located at level 0), and loses NOTHING for residual sources at any level or for pure data.
  **[RSQ3-fix M3-2: read "at any level (paired energy-residual sources; S2-3)" in place of "at any level".]**
  **[RSQ2-fix S2-4a-c, M2-2: the reading above is corrected as follows; kept as written.]** (i') A1's zeros are EXACT BY
  CONSTRUCTION: q3 placed each vortex where the transported weight T_{L^m} ⊗ T_{L^m} is affine (base (M - 1)/2), so its
  transported circulation dS_k(P) = -Δ_2w(p_0)·χ vanishes identically (discrete harmonicity of the bilinear tent). So (A)
  is the top-datum test in disguise: it neither confirms nor refutes REVIEW_SQ_S1's level sum. The primary design error is
  this degenerate placement; the d = 3 choice is secondary (and was foreseeable after q2's d = 2 lesson). (ii') SHIFT's
  non-trivial content is confirmed by REVIEW_SQ_S2 R1 (vortices at the tent peak: c = 1/27 per level at d = 2, response
  = c·(top-datum response) to 4·10⁻¹³, aligned all-level sum bounded), not by q3. Do not cite q3 A1 as a measurement of
  SHIFT. (iii') QB's PASS is as confounded by d = 3 scaling as QA's FAIL; the usable same-dimension signal is (B) R_ctr
  growing (0.90 → 1.75 → 2.67) against (C) R_ctr flat. q3b's B4 doubling (0.995 → 2.014) is matched by q2's provably bounded
  pure-data C_D doubling (0.22 → 0.45): two depths cannot separate growth from saturation; q3b is "consistent", not
  evidence. (iv') The caveat "(C)/(C4) are flat anyway" is FALSE in d = 3: (C)'s N_0 grows (0.173, 0.203, 0.276; QC's FAIL),
  and the argmax is interior, at P's centre lines, distance ≥ n - 1 from every face (REVIEW_SQ_S2 R3); it is attributed to
  d = 3 scaling (post hoc). (C4)'s N_0 is flat over two depths. Boundary compatibility is irrelevant to (b) (S2-2). (v')
  M2-2: q3's "centre of P" (p*_0, X*, the (A) vortices at base ((n - 1)/2, (n - 1)/2)) is the centre of P's CORNER BLOCK
  (under P's vertex (0, 0)), not P's centre (fine n - ½); no verdict changes. (vi') "Loses a depth factor for curl-ful
  level-0 sources" is EXPECTED (CZ), not shown (S2-4d).

### 11.6 What the non-abelian (REG-min) needs (Target G5), aligned with REVIEW_S22's BFT
REVIEW_S22 Part 5 states BFT (clauses 0-5) and records (REG-min) as "a sibling, not a corollary" of BFT-1: the cone-local,
free-boundary analogue for MINIMISERS. Item by item (status words as labelled; nothing below is counted):
- **(NA-0) The decay DESC actually needs [ARGUED].** SUP-price and MSG-dec use (D1)-(D2) only through MSG-dec's recursion
  K_i ≤ K_{i+1} + 2C_DB_1L^{-(θ_w-1)(k-i)} + … and SUP-price steps (3), (5). With curvature and residual decay exponents θ_w > 1
  (in place of 2) the recursion still sums (constant ∝ 1/(1 - L^{1-θ_w})), the links still decay like L^{-(k-i)}, step (5)
  stays geometric and step (3)'s level-0 term stays ≤ C_pK²θ². At θ_w = 1 the recursion grows linearly in depth. So DESC needs
  **BFT-1 with θ_w > 1** (BFT allows θ_w ∈ (0, 2]); θ_w = 2 is what the linear case gives (Theorem REG-lin).
  **[RSQ2-fix M2-5, S2-6.]** K, C_err and τ_♭ degrade like (1 - L^{1-θ_w})^{-1}, so the price → 0 as θ_w ↓ 1. BFT's claim is
  EXISTENTIAL in θ_w ("there exist … θ_w ∈ (0, 2]"); PROOF/N5 needs θ_w = 0, SF θ_w > 0; SQ's θ_w > 1 is the strongest, so
  it must be stated as a REQUIREMENT on lane A (a stated value), not assumed (§13.8).
- **(NA-1) Free boundary [ARGUED].** The nonlinear form of REFL: crossing links := 1, crossing plaquettes then have holonomy 1,
  and a crossing coarse link has a reflection-symmetric S4' contour family, so M̄ is Hermitian near 1 and W_0(M̄) = 1; with
  Palais' symmetric criticality (compact reflection group) a box critical point extends to a critical point of the periodic
  chain. Needs S4' covariance under the half-integer-plane reflections (LINEAR_PACKAGE §1.2 records covariance under
  reflections, check c8; which reflections were checked was not read here).
- **(NA-2) Level 0 without a Calderón-Zygmund log, in covariant form [ARGUED; the two bounds are sketched, not written].**
  Apply LES-sup to F̂ := log U_0 (componentwise in an orthonormal basis of su(N)), in the MSG gauge. K := dF̂ is the
  non-abelian Bianchi defect: the six transported face holonomies of a 3-cell multiply to 1, |Ad_t Y - Y| ≤ 2|t - 1||Y|, so
  |dF̂| ≤ C(m_0 sup|F̂| + sup|F̂|²). J := d*F̂ is, by the Euler-Lagrange equation, a covariant correction of the same size plus
  the soft current κ(DM̄)^Tρ̃. In the decay class (m_0 ≤ KθL^{-k}, sup|F̂| ≤ 𝔑θn^{-2}) both give n²·n·(J_0 + K_0) ≲ K𝔑θ² + κ̂(…)θ:
  quadratic in 𝔑 with a factor θ, and depth-uniform. The point: the BCH remainder R_p = log U_0(p) - da_0(p) is a
  non-closed plaquette source only in the abelianised bookkeeping; its exterior derivative is dR = d log U_0, the covariant
  Bianchi defect (link × curvature). q3 (B)/q3b (B4) test curl-ful sources (|dq| ~ |q|), the abelianised model, not this one.
  So S1-4's obstruction (α) concerns the abelianised (α); in covariant form the level-0 step looks like REG-lin-src (b).
  **[RSQ2-fix M2-6.]** Two caveats: the Wilson Euler-Lagrange equation gives sin-type (P(U_0(p)), the su(N) projection), not
  log-type, currents, a cubic correction; and E_𝒞 (Wilson s + κφ) must be identified with BFT's 𝔉_k restricted to the cone
  (not stated in BFT). §13 replaces (NA-2)'s LES-sup bookkeeping by the reduction RED-0.
- **(NA-3) Levels ≥ 1 [ARGUED].** Residual transport: the Euler-Lagrange equation in U_{i+1} gives ρ̃_i from ρ̃_{i+1} through
  (DM̄)^T; the S4' funnel part (column sums O(1)) is killed in the linear case by co-closedness (J-str); nonlinearly the
  residual is covariantly co-closed (gauge invariance), so the funnel part is ≤ Cm_i|ρ̃_{i+1}| and the per-level factor is
  L^{-3}(1 + CL³m_i), whose product over levels is bounded when Kθ is small. Curvatures at levels ≥ 1: through da (E-loc's
  linear identities, as in SUP-price), with BCH remainders only at the level itself (C_pm_i²), so no level sum.
- **(NA-4) The a-priori inequality [ARGUED from NA-1…NA-3].** For a τ_R-small minimiser already in the decay class with
  θ𝔑 ≤ c_* (needed to run MSG-dec): 𝔑 ≤ C_lin' + C''θ𝔑², hence 𝔑 ≤ 2C_lin' on the small branch.
  **[RSQ2-fix S2-3 (norm).]** In (NA-3)/(NA-4), 𝔑 must carry the residual weight L^{3(k-1-i)} (or L^{(2+δ)(k-1-i)}, δ > 0), not
  (D2)'s L^{2(k-1-i)}: unpaired EL currents j_l ≈ m_l·r̂_l reach J_0 through (Q^T)^l, contributing ≈ L^{3(k-l)}sup|j_l| to
  n³sup|J|; with r̂_l ~ L^{-2(k-1-l)} each level contributes ≈ C_eKθ²L² (a sum of order k), with exponent > 2 the sum is
  geometric (REVIEW_SQ_S2 P4). §13.3 (RES-dec) delivers an exponent > 2 without bootstrap.
- **(NA-5) The large branch: the critical step, NOT removed.** (NA-4) cannot exclude 𝔑 ≳ 1/(C''θ) (S1-4 (β)). Two
  mechanisms exclude it: (i) uniqueness plus continuity, i.e. BFT-0's contraction in 𝔐 together with an a-priori statement
  that every τ_R-small minimiser of E_𝒞(q) lies, after gauge, in BFT's ball (the cone-local form of SF's (MIN-reg)); (ii)
  Uhlenbeck-type ε-regularity [literature: K. Uhlenbeck, CMP 83 (1982) 11 and 31; not-read this session]: the energy is
  small at every scale (E_𝒞 ≤ κ_+θ²/2), and a Coulomb-type gauge with critical Sobolev (ℓ⁴) control of the potential excludes
  the large branch, an (MS-Sob)-type step at a single level. Either way the sup route RELOCATES the critical step into
  (NA-5); it does not remove it. This sharpens REVIEW_SQ_S1's strategic verdict 2.
- **Exact dependence (the merger, stated).** (REG-min) ⇐ **(BFT-cone)**: BFT-0 and BFT-1 (θ_w > 1, the sup part of its
  Hölder norm) for the cone energy E_𝒞(q) with free boundary [via NA-1 this is BFT on the reflection-symmetric sector of a
  torus of level-k side (4, 4, 2, 2): a SMALL anisotropic torus, below BFT's T_0 in general, so BFT as stated does not apply;
  a box form is needed] **+ (MIN-reg)_cone** (every τ_R-small minimiser is in the BFT ball). Then DESC-ε discharges AE-red's
  two conclusions and (MS-Sob) leaves the path. Without (MIN-reg)_cone, BFT gives (REG-min) for the BFT critical point only,
  and DESC case (iii) (which needs EVERY small minimiser) does not run.
  **[RSQ2-fix S2-6 (circularity).]** BFT-0's uniqueness ball is ||X||_𝔐 ≤ C_0ε with 𝔐 weighted by L^{θ_w(k-j)}, so membership
  in it IS the weighted decay: (MIN-reg)_cone with BFT's 𝔐-ball already implies (REG-min) by itself (at rate θ_w, for the
  sup part of 𝔐). "(REG-min) ⇐ (BFT-cone) + (MIN-reg)_cone" is true but nearly tautological: **the whole wall is
  (MIN-reg)_cone**, and DESC needs only "every τ_R-small minimiser is in Σ_dec", no uniqueness. BFT adds identification and
  Hölder regularity, which DESC does not use. Lane A must deliver REVIEW_SQ_S2's items 1-5 (item 4 critical), and θ_w > 1
  must be REQUIRED of BFT (§13.8).
  **[RSQ2-fix S2-5 (box clause), checked on a limited reading.]** The sentence "BFT as stated does not apply; a box form is
  needed" is withdrawn as an assertion. BFT's claim includes "every non-wrapping box with the boundary convention of
  N5-sf0" (REVIEW_S22 l.400-401). On the reading done this session (PROOF l.5443-5460, Theorem N5-sf0's constants and
  background classes), N5-sf0's boxes are the regions Ω^+_□ of an R_*-partition of a torus of side ≥ T_0, carrying local
  real gauges g_□, with the torus field outside: local gauge charts in a periodic problem. I found there no statement for a
  free (Neumann, natural) boundary. So, ON THIS READING, the box clause does not by itself cover the cone's free boundary,
  and either (i) BFT on REFL's reflection torus (level-k side (4, 4, 2, 2), below T_0 in general) or (ii) an explicit
  free-boundary cone-box clause is still needed, together with the data hypothesis admitting box_k = P alone. Not a full
  check: the N5-sf0 convention's text elsewhere in PROOF was not read; lane A should confirm.
  **[RSQ3-fix S3-1 (binding): the two sentences "Not a full check … lane A should confirm" and the phrase "on a limited
  reading" are withdrawn.]** The N5-sf0 convention is a gauge-chart convention inside a torus (PROOF l.5443-5460, l.5818,
  l.5928, per REVIEW_SQ_S3's wider search). BFT_B l.240 records that the box clause is not proven ("Proven on tori T ≥ T_0
  only; BFT's 'every non-wrapping box …' clause is not covered here"). So the free-boundary cone-box clause is genuinely
  missing, not merely unread (§13.8 item (3) stands).
- **What G4 contributes to BFT [PROVEN parts].** Theorem REG-lin is the trivial-background linear content of BFT-1 on the
  cone box with θ_w = 2, in sup, with no Hölder norm and no torus. REG-lin-src (a)-(c) is the linear source-to-response
  estimate (COMP's (CL-2) at the trivial background) for three source classes: residual sources need no level weights;
  level-0 plaquette sources need Lipschitz or Hölder control (G4-F2), consistent with BFT's choice of a Hölder 𝔐. REFL is the
  boundary convention for a cone box.
- **Proposal for PROOF's owner (text, not applied) [inference].** "COMP-F1 (the Π_ex tail on non-closed second-order
  sources) is a statement about the abelianised remainder. Written covariantly, the level-0 remainder enters LES-sup only
  through dF̂ (the covariant Bianchi defect) and d*F̂, both link × curvature (SQ.md §11.6 (NA-2)); (CL-2) should be tested in
  that form before concluding that the plain sup-curvature norm is excluded."

## 12. Session-2 outcomes against §T2 (ADDED AFTER the derivations; pointers only) and tally
- **Step 1: DONE.** REVIEW_SQ_S1's binding fixes S1-1, S1-1a, S1-2 (Corollary DESC-ε, written fully, §0.3; §0.5 completed),
  S1-3, S1-4, S1-5, S1-6, §7, M-1 (C_p := 34√N), M-2 (θ_♯ listed), M-3 (FORCE strict; not counted), M-4, M-5, M-6
  (θ_0 ≈ 3·10⁻⁸/C_D²; price ≈ 3·10⁻²³ at C_D = 2, a net loss of 6-9 orders against CLS-cone at ε_1 = 0.5), M-7 (q2 pre-run edit
  disclosed), the dropped "L^{-1/2} saturation" reading; all tagged [RSQ1-fix]. Session-1 tally corrected to 6 / 2 / 2 (§10).
- **Q3: MET (answered), with q3 OVERALL FAIL as pre-registered (QA, QC: d = 3 scaling) and q3b PASS.** §11.5.
- **G4: MET for pure data and for two source classes; PARTIAL for general sources.** Theorem REG-lin (pure data, sup, θ_w = 2,
  depth-uniform); Theorem REG-lin-src ((a) residual sources, no level weights; (b) Lipschitz, (c) Hölder level-0 sources, with
  boundary compatibility). Not covered: general divergence-form currents at every level on the cone box (G♯_0-soft via REFL
  needs an anisotropic small torus; not claimed). G4-F1 does not occur; G4-F2 occurs for level-0 sources (sup alone loses).
  **[RSQ2-fix S2-3, S2-4d.]** "no level weights" is scoped to PAIRED energy-residual sources; "G4-F2 occurs" reads "G4-F2 is
  EXPECTED (CZ), not proven; sup|q_0| + sup|dq_0| suffices".
- **G5: MET as a statement (§11.6), ARGUED throughout.** (REG-min) ⇐ (BFT-cone) + (MIN-reg)_cone; DESC needs θ_w > 1 only;
  the level-0 log does not arise in covariant form [ARGUED]; the large branch (NA-5) is the critical step, relocated, not
  removed.
  **[RSQ2-fix S2-6.]** Read: "the whole wall is (MIN-reg)_cone; (REG-min) ⇐ BFT is not a reduction while (MIN-reg)_cone is
  unaddressed; nothing in §11.6 is counted".
- **Tally, session 2 (this file; all unreviewed).** PROVEN-HERE, counted (2): Theorem REG-lin (with Lemma REFL); Theorem
  REG-lin-src (with Lemma SHIFT). CONDITIONAL (1): Corollary DESC-ε ⇐ (REG-min). Not counted: Lemma TOP. ARGUED: (NA-0)-(NA-5),
  the BFT dependence, the proposal for PROOF's owner. OPEN unchanged: (REG-min) [B-NA-class; cone-local sibling of BFT-1];
  non-abelian (SQ).
- **File tally after session 2: PROVEN-HERE counted 8 (6 + 2) / CONDITIONAL 3 (PRICE-iii, linear MS-Sob ⇐ §4.4 counts,
  DESC-ε) / OPEN 2.**
- **Hypotheses consumed (session 2).** REG-lin: LES-sup (PROOF l.2388), §0.4, §3.0's column sums, d∘Q = Q_2∘d. REG-lin-src:
  SHIFT, REG-lin, LES-sup, LES-div (PROOF l.3394) and the (G♯_0-fine) unit conversion (PROOF l.3405-3437), the flat-torus
  Weitzenböck identity (LINEAR_PACKAGE §1.1). DESC-ε: DESC, FORCE (strict), KQ, (F1), (REG-min). No literature item is
  load-bearing.
- **Not done / not claimed.** No edit outside SQ.md, SQ_LOG.md, checks/q*. No commits, PRs, pushes, CL or axiom edits.
  RLARGE §3.4 (a_coh binding) and HIST/PROOF texts are proposals only.

---

# Session 3 (2026-10-28 UTC)

## T3. PRE-STATED (session 3) — statements only; the FIRST edit of session 3 (appended before any [RSQ2-fix] edit, before any session-3 proof, criteria file or script). Nothing in §T3 cites a result of this session. Exploratory reasoning while reading (REVIEW_SQ_S2, REVIEW_RLARGE_V3 Part 6, BFT_B §15.0/§18/§19.9-19.13, LINEAR_PACKAGE §1.2-§1.3 and Lemma 3.1, HIST Lemma KQ) preceded this append and is not recorded, so its only claim is file order. Proofs follow in §13, later; outcomes are pointers in §14.

- **Step 1.** Apply REVIEW_SQ_S2's binding fixes S2-1a, S2-1b, S2-2, S2-3, S2-4a-d, S2-5, S2-6 and M2-1 … M2-6, tagged
  [RSQ2-fix], original text kept.
- **Target G6 ((MIN-reg)_cone, REVIEW_RLARGE_V3 top-3 item 3).** Prove, or reduce to one named single-level statement,
  that every τ_R-small cone-local minimiser lies in Σ_dec with a depth-uniform constant. Statements to be proven or refuted:
  - **Lemma CC-NA (exact covariant co-closedness).** At every critical point of the cone energy E_𝒞(P) (free boundary, top
    fixed), the residual current j_l (the left gradient of κ_lφ_c in U_{l+1}(c), c a level-(l+1) cone link) has vanishing
    covariant Neumann divergence at every level-(l+1) site of box_{l+1}, 0 ≤ l ≤ k - 1. [planned: PROVEN-HERE]
  - **Lemma RT-NA (exact homogeneous residual transport).** For 0 ≤ l ≤ k - 2, the Euler-Lagrange equation in U_{l+1}
    expresses j_l linearly in j_{l+1} through the S4' contour derivative, with NO other source term (levels ≥ 1 carry no
    plaquette action), and the M̄-gradient of φ_M(V) = N⁻¹(tr|M| - Re tr(V⁻¹M)) is proportional to the residual. [planned:
    PROVEN-HERE]
  - **Proposition RES-dec (nonlinear residual decay without bootstrap).** There are τ_* = τ_*(N, L) > 0 and C_r = C_r(N, L,
    κ_±) such that every τ-small critical point (every cone plaquette below the top and every residual < τ ≤ τ_*) obeys
    x_c ≤ C_rθ·q^{k-1-l} on level-(l+1) links, q := L^{-3} + C_qτ, so with exponent θ_r := -log_L q > 2 for τ small,
    uniformly in k; no uniqueness, no continuity and no a-priori decay is used. [planned: PROVEN-HERE, via the S4' funnel
    identity Q_root = Q_str - d∘h in nonlinear form plus CC-NA; constants crude]
  - **Lemma STOKES-NA (upward curvature transport without a level sum).** For a level-j cone plaquette q (1 ≤ j ≤ k - 1),
    ||1 - U_j(q)|| ≤ L²f_{j-1} + C_S(f_{j-1}² + f_{j-1}x_{j-1}) + C_xx_{j-1}, f_{j-1} the maximal level-(j-1) plaquette size
    and x_{j-1} the maximal residual in q's four endpoint blocks. [planned: PROVEN-HERE given E2, BCH-p, MSG step (1)]
  - **Theorem RED-0 (reduction to level 0).** Given RES-dec and STOKES-NA: (REG-min) ⟺ **(EPS-0)**: every τ_R-small cone
    minimiser has sup_{level-0 plaquettes}||1 - U_0(p)|| ≤ C_0θn^{-2} with C_0 depth-uniform. [planned: PROVEN as an
    implication in both directions]
  - **Route (a) verdict.** Whether BFT_B's NF-uniq / S_E / (N1-bd) give uniqueness of the cone MINIMISER box by box, or only
    uniqueness of the gauge normal form; and what they contribute to (EPS-0). [planned: stated with proof of whatever is
    claimed]
  - **Route (b) verdict.** Whether (EPS-0) follows from a single-level lattice ε-regularity step (lattice Kato inequality,
    lattice Weitzenböck/Bianchi, Moser iteration with the critical potential |F| ∈ ℓ² small), and where exactly it fails or
    what it needs. [planned: lattice Kato PROVEN-HERE; the rest ARGUED, the exact wall named]
  - **Chain to the consumers.** (CLS-min) ⟸ (REG-min) ⟸ (EPS-0) (+ the PROVEN pieces), and the BFT-1 clause request:
    θ_w > 1 as a stated value (not an existential), the cone-box clause, and the residual exponent > 2.
- **Check q4 (criteria first, checks/q4_criteria.md before the script).** Exact identities only: the invariance
  φ_{aMb}(aVb) = φ_M(V), the gradient formula of RT-NA (M̄-gradient ∝ residual, with its bound), and the opposite-gradient
  relation used by CC-NA, on random SU(2)/SU(3) data, by finite differences. Jobs < 20 min, < 1 GB.
- **Failure modes (pre-stated).** (G6-F1) the EL in U_{l+1} has a source not proportional to the residuals (spread
  gradient): then RES-dec fails as stated. (G6-F2) the nonlinear funnel cancellation leaves an O(1)-column-sum error not
  small in τ: then the exponent θ_r > 2 is not obtained from τ-smallness. (G6-F3) STOKES-NA's main coefficient exceeds L²
  (a ribbon excess per level): then curvature decay at levels ≥ 1 needs a level sum. (G6-F4) (EPS-0) is itself coupled to
  the residual corrections through the level-0 source, so that the reduction does not decouple the large branch.

## 13. (MIN-reg)_cone: reduction of (REG-min) to its level-0 clause (Target G6; derivations written after §T3, after Step 1 and after q4 ran at 10:17:46-10:17:57 UTC)

### 13.0 Setting and notation
Cone 𝒞(P) as in §0.1/§11.0 (d = 4, L ≥ 3 odd, level-k plaquette P, box_j of side (2, 2, 1, 1)L^{k-j}, free boundary, the four
top links V fixed). E_𝒞 = Σ_{level-0 p}s(U_0(p)) + Σ_{l=0}^{k-1}κ_lΣ_{c ⊂ box_{l+1}}φ_{M̄_c(U_l)}(U_{l+1}(c)), s(U) := 1 - N⁻¹Re tr U,
with the kernel term (HIST Lemma KQ's proof; LINEAR_PACKAGE §1.3)
  **φ_M(V) = N⁻¹[Re tr(W_0(M)⁻¹M) - Re tr(V⁻¹M)]**, W_0(M) the maximiser of Re tr(W⁻¹M) over SU(N) (HIST PM).
M̄_c = Σ_Tw_TH_T, H_T := hol(T), over the S4' contours T = T^σ_y = P^σ(c_X → y)S_yP^σ(c_{X'} → y + Le_μ)^† of c = (X, X' = X + e_μ),
w_T = 1/(24L⁴) (LINEAR_PACKAGE §1.2); all contours of c lie in c's two endpoint blocks. Pairing ⟨A, B⟩ := Re tr(A*B) on
su(N), |·| := |·|_HS unless "op" is written. For a function f of one link variable U: the **left gradient** ∇^Lf ∈ su(N),
d/dt f(e^{tμ}U)|_0 = ⟨∇^Lf, μ⟩; then d/dt f(Ue^{-tμ})|_0 = ⟨-Ad_{U⁻¹}∇^Lf, μ⟩. The **residual current** of a level-(l+1) cone
link c is **j_l(c) := ∇^L_{U_{l+1}(c)}[κ_lφ_c]** (0 ≤ l ≤ k - 1). Sizes: x_c := ||U_{l+1}(c) - W_0(M̄_c)||_op (the residual,
§0.3 (D2)); σ_c := max_T||H_T - M̄_c||_op (contour spread); σ'_c := ||M̄_c - W_0(M̄_c)||_op; f_l(c) := the maximal level-l
plaquette size ||1 - U_l(p)|| over c's endpoint blocks. "τ-small" means: every cone plaquette below the top and every
residual (including the top residuals) is < τ.
Two inputs from other files, both PROVEN there: **RS (R1)** (per contour: ||H_T - hol(S_c)|| ≤ A_df_l(c), as used in FORCE),
hence σ_c ≤ 2A_df_l(c); **Lemma PM** (HIST: ||M - W_0(M)|| ≤ 4δ for δ := ||M - S||, S unitary), hence σ'_c ≤ 4A_df_l(c).
**[RSQ3-fix M3-1]** §T3 (l.966) wrote the kernel as φ_M(V) = N⁻¹(tr|M| - Re tr(V⁻¹M)). tr|M| is the U(N) maximum of
Re tr(W⁻¹M); for SU(N) it equals the form above only when the polar factor of M has determinant 1 (always for SU(2), where M
is a real multiple of an SU(2) element; not in general for SU(3)). The SU(N), W_0 form used here is the correct one; §T3's
formula is corrected by this note (not load-bearing).

### 13.1 Lemma K (kernel identities): PROVEN-HERE [S3-G] (not counted; q4 checks (a)-(c))
(a) *Bi-invariance.* φ_{aMb}(aVb) = φ_M(V) for a, b ∈ SU(N) (W_0(aMb) = aW_0(M)b by uniqueness of the maximiser).
(b) *M-gradient.* For every complex N × N δ: d/dt φ_{M+tδ}(V)|_0 = N⁻¹Re tr(Zδ), **Z := W_0(M)⁻¹ - V⁻¹** (envelope theorem: W_0 is
a nondegenerate maximiser, smooth in M, and the derivative of max_W Re tr(W⁻¹M) is Re tr(W_0⁻¹δ)). ||Z||_HS = ||V - W_0||_HS ≤
√Nx. At V = W_0 the M-gradient vanishes. **[RSQ3-fix M3-3: hypothesis of (b): the maximiser is unique (e.g.
||M - S|| < ¼ for some unitary S, Lemma PM's regime); this hypothesis is therefore also one of RT-NA's. CC-NA uses only (c),
which needs no uniqueness: Re tr(W_0(e^{tμ}M)⁻¹e^{tμ}M) is constant in t by (a).]**
(c) *Opposite gradients.* By (a) with a = e^{tμ}, b = 1 (resp. a = 1, b = e^{-tμ}): the left (right) gradient of φ in V is
minus its left (right) gradient in M.
(d) *Two-sided size of the current.* Write V = W_0e^X (X principal log, eigen-angles θ_j, |θ_j| ≤ (π/2)x), A := W_0⁻¹M. By PM
step 3, A = H + ic·1 with H Hermitian and c real, ||H - 1||, |c| ≤ ||A - 1|| = σ'. Then ⟨j, μ⟩ = κN⁻¹Re tr(MV⁻¹μ) =
κN⁻¹Re tr(Ae^{-X}μ'), μ' := Ad_{W_0⁻¹}μ; Re tr(Aμ') = 0 (stationarity), so Re tr(Ae^{-X}μ') = Re tr(A(e^{-X} - 1)μ'). Hence
  **κN⁻¹(1 - x² - σ')x ≤ |j| ≤ κN^{-1/2}(1 + σ')x**
(upper: ||A(e^{-X} - 1)||_HS ≤ (1 + σ')√N||e^{-X} - 1||_op = (1 + σ')√Nx; lower: μ' := X/|X|, Re tr((e^{-X} - 1)X) = Σθ_jsin θ_j ≥
|X|²(1 - θ_max²/6), |Re tr((A - 1)(e^{-X} - 1)X)| ≤ σ'|X|·||e^{-X} - 1||_HS, |X| ≥ x).
(e) *Quadratic lower bound without a linear term (sharpens KQ (lower)).* With U' := V⁻¹W_0, φ = s(U') + N⁻¹tr(Re(1 - U')(H - 1))
+ N⁻¹c·Im tr U' (expand φ = N⁻¹Re tr((1 - U')A), KQ's proof). Re(1 - U') ≥ 0, so |tr(Re(1 - U')(H - 1))| ≤ σ'Ns(U'); Σθ_j = 0
gives |Im tr U'| = |Σ(sin θ_j - θ_j)| ≤ Σ|θ_j|³/6. Hence **φ_M(V) ≥ (x²/(2N))(1 - 2σ' - x²)** for x ≤ ½.
*Proof.* As written in each item. ∎

### 13.2 Lemma CC-NA (exact covariant co-closedness of the residual currents): PROVEN-HERE [S3-G] (counted)
At every critical point of E_𝒞 (top fixed, free boundary), for 0 ≤ l ≤ k - 1 and every level-(l+1) site z of box_{l+1}:
  **(D*j_l)(z) := Σ_{c ∈ box_{l+1} leaving z}j_l(c) - Σ_{c ∈ box_{l+1} entering z}Ad_{U_{l+1}(c)⁻¹}j_l(c) = 0.**
*Proof.* (i) *Non-root sites, l ≤ k - 2.* Vary U_{l+1} ALONE by the gauge e^{tμ} at z (U(c) ↦ e^{tμ}U(c) leaving, U(c)e^{-tμ}
entering). Contour holonomies of level-(l+2) links run root to root, so if z is not a root c_Y they are unchanged (the two
factors at z cancel); levels ≥ 1 carry no plaquette term; only the kernel terms of links at z change, with derivative
⟨(D*j_l)(z), μ⟩. So (D*j_l)(z) = 0. (ii) *Roots, l ≤ k - 2.* For z = c_Y (Y a level-(l+2) site of box_{l+2}) the same
variation also maps M̄_{c'} ↦ e^{tμ}M̄_{c'} for c' ∈ box_{l+2} leaving Y and M̄_{c'} ↦ M̄_{c'}e^{-tμ} for c' entering Y; by Lemma K
(c) the derivative of these terms is -⟨(D*j_{l+1})(Y), μ⟩. So (D*j_l)(c_Y) = (D*j_{l+1})(Y). (iii) *Top.* For a corner Y of P
take the composite gauge equal to e^{tμ} at c_Y (level k - 1), at the level-(k-2) root of c_Y, and so on down to level 0,
and 1 elsewhere (each level's value at the roots equals the next level's value at the site: the composite-gauge rule of
F6). Every kernel term below the top and every plaquette is invariant; the top terms at Y change as in (ii), and V is fixed.
So (D*j_{k-1})(Y) = 0. (iv) Downward induction on l with (i)-(iii). ∎
**[RSQ3-fix M3-4 (wording)]** In (i) read "interior visits of a contour to the gauged site cancel (e^{-tμ}e^{tμ} = 1); only
endpoints count" in place of "(the two factors at z cancel)": a contour can pass through a root in its interior (a funnel
leaving c_Y in the -μ direction followed by S_y running back through c_Y); such visits do not affect (i)-(ii).
*Meaning.* This is the nonlinear form of LINEAR_PACKAGE Lemma 3.1 (a) (d*r_i = 0) and BFT_B Lemma RT (a), with no
smallness hypothesis.

### 13.3 Lemma RT-NA (exact homogeneous residual transport) and Proposition RES-dec (nonlinear residual decay without bootstrap): PROVEN-HERE [S3-G] (counted as one item; inputs RS (R1), PM, the S4' definition)
**Lemma RT-NA.** At every critical point, for 0 ≤ l ≤ k - 2 and every level-(l+1) link b of box_{l+1}:
  **j_l(b) = 𝒯j_{l+1}(b) - e_l(b)**, 𝒯j(b) := Σ_{c'}Σ_{T∋b}w_Tε_TAd_{Q_T}⁻¹j(c'),
  ⟨e_l(b), μ⟩ := κ_{l+1}N⁻¹Σ_{c'}Σ_{T∋b}w_Tε_TRe tr(Z_{c'}Ad_{Q_T}(μ)(H_T - M̄_{c'})),
with ε_T = ±1 the orientation of b in T, Q_T the holonomy of T from its start to the tail of b along T (for a backward
traversal, the prefix times U(b)⁻¹), and Z_{c'} := W_0(M̄_{c'})⁻¹ - U_{l+2}(c')⁻¹. There is no other term.
*Proof.* U_{l+1}(b) enters only its own kernel term (derivative j_l(b)) and the kernel terms κ_{l+1}φ_{c'} of the
level-(l+2) links c' having b in a contour (levels ≥ 1 carry no plaquette action). Under U(b) ↦ e^{tμ}U(b), H_T ↦
Ad_{Q_T}(e^{ε_Ttμ})H_T, so δM̄_{c'} = Σ_{T∋b}w_Tε_TAd_{Q_T}(μ)H_T. Lemma K (b) gives the derivative N⁻¹Re tr(Z δM̄); split
H_T = M̄ + (H_T - M̄); the M̄ part is ⟨∇^L_Mφ, Ad_Qμ⟩ = -⟨κ_{l+1}⁻¹j_{l+1}(c'), Ad_Qμ⟩ by Lemma K (c). The Euler-Lagrange equation
(sum = 0) is the identity. ∎ (Failure mode G6-F1 does NOT occur: the M̄-gradient is ∝ Z, i.e. ∝ the residual, Lemma K (b);
the spread of the contours enters only multiplied by Z.)
**[RSQ3-fix M3-5]** "T ∋ b" counts multiplicity: an axial funnel ending at y by a -μ step re-traverses the first links of S_y
backwards, so b can occur twice in one contour; the sum runs over occurrences, each with its own ε_T and Q_T. The bounds below
are unchanged, since the (s) and (f) counts are per occurrence. (Lemma K (b)'s uniqueness hypothesis, M3-3, is part of RT-NA's.)

**The funnel cancellation.** Classify (c', T) with b ∈ T: (s) b on the straight leg S_y; (f) b on a funnel P^σ(c_Y → ŷ), ŷ ∈ B(Y),
which happens only for b inside block Y. For fixed (σ, ŷ) the funnel P^σ(c_Y → ŷ) is used, with weight 1/(24L⁴), by the
contour (σ, ŷ) of EVERY box_{l+2} link at Y: forward by the outgoing ones (y = ŷ), backward by the incoming ones
(c'' = (Y - e_ν, Y), y'' = ŷ - Le_ν) (same σ at both ends; LINEAR_PACKAGE §1.2). Its prefix to b is Q_b := the funnel holonomy
from c_Y to tail(b) for outgoing c', and H_TQ_b for incoming c'' (the incoming contour reaches c_Y at its end). So the (f)
part of 𝒯j(b) is
  Σ_{(σ,ŷ): b ∈ P^σ(c_Y→ŷ)}(ε_b/(24L⁴))Ad_{Q_b}⁻¹[Σ_{out}j(c') - Σ_{in}Ad_{H_{T(c'',σ,ŷ)}}⁻¹j(c'')],
and the bracket equals (D*j_{l+1})(Y) = 0 (CC-NA) up to Σ_{in}(Ad_{U(c'')⁻¹} - Ad_{H_T⁻¹})j(c''), of norm ≤ Σ_{in}2||U_{l+2}(c'') - H_T||·|j(c'')|
≤ 8 max_{c''}(x + σ' + σ)_{c''}·max|j_{l+1}| (≤ 4 incoming links; ||Ad_Aη - Ad_Bη|| ≤ 2||A - B||·|η| for unitary A, B). The
funnel weight ω(b) := #{(σ, ŷ) : b ∈ P^σ(c_Y → ŷ)}/(24L⁴) is ≤ 1. The (s) part: Ad is an isometry and the straight weights
of b sum to ≤ L·L⁻⁴ = L⁻³ (b lies on S_y only for the ≤ L sites y = tail(b) - ie_μ, 0 ≤ i < L). The remainder: Lemma K (b),
|Z_{c'}| ≤ √Nx_{c'} ≤ (1.1N^{3/2}/κ_{l+1})|j_{l+1}(c')| (Lemma K (d) lower, at x² + σ' ≤ 0.09), σ_{c'} ≤ 2A_df, total weight
Σ_{c'}Σ_{T∋b}w_T ≤ L⁻³ + 8ω(b) ≤ 8.04 (each funnel pair (σ, ŷ) serves ≤ 8 links): |e_l(b)| ≤ κ_{l+1}N⁻¹·(1.1N^{3/2}/κ_{l+1})·
2A_df·8.04·max|j_{l+1}| ≤ 17.7√NA_df·max|j_{l+1}|.
**Corollary (per-level factor).** With f := max level-(l+1) plaquette size, x := max level-(l+2) residual:
  **sup_{level l+1}|j_l| ≤ [L⁻³ + 8(x + 6A_df) + 17.7√NA_df]·sup_{level l+2}|j_{l+1}|** (σ + σ' ≤ 6A_df).

**Proposition RES-dec.** Put C_q := 8 + 48A_d + 17.7√NA_d (= 665 at N = 2, L = 3) and, for 0 < τ ≤ τ_* := (L⁻² - L⁻³)/(2C_q)
(= 5.6·10⁻⁵ at N = 2, L = 3; τ_* also below the thresholds of Lemma K (d), (e)), q := L⁻³ + C_qτ ≤ (L⁻² + L⁻³)/2. For every
τ-small MINIMISER of E_𝒞 with θ := ||1 - V_P||, every 0 ≤ l ≤ k - 1 and every level-(l+1) cone link c:
  **x_c ≤ C_rθq^{k-1-l}, C_r := 1.9Nκ̂^{3/2}**, hence x_c ≤ C_rθL^{-θ_r(k-1-l)}, **θ_r := -log_Lq > 2** (θ_r ≥ 2.37 at L = 3),
uniformly in k, with NO uniqueness, continuity or a-priori decay used.
*Proof.* (1) *Top.* E_𝒞's minimum depends on V only through the conjugacy class of V_P (F6); the competitor U_i ≡ 1 (i < k), in
the top gauge with three top links 1, has E = κ_{k-1}s(V_P) ≤ κ_+(π²/8)θ² (W_0(1) = 1, φ_1 = s; for unitary V, s(V) ≤ θ_max²/2
with θ_max ≤ (π/2)θ). At the minimiser κ_-φ_c ≤ E for each top link c (residuals are chain-gauge invariant), so Lemma K (e)
gives x_c² ≤ 2N(π²/8)κ̂θ²·1.1, x_c ≤ 1.65√(Nκ̂)θ. (2) *Transport.* τ-smallness (x < τ, f < τ) in the Corollary gives
sup_l|j_l| ≤ q·sup_{l+1}|j_{l+1}|, so sup|j_l| ≤ q^{k-1-l}sup|j_{k-1}| ≤ q^{k-1-l}κ_{k-1}N^{-1/2}(1.01)(1.65√(Nκ̂)θ) (Lemma K (d)
upper). (3) *Back to residuals.* Lemma K (d) lower: x_c ≤ 1.1Nκ_l⁻¹|j_l(c)| ≤ 1.1·1.01·1.65N(κ_{k-1}/κ_l)√κ̂θq^{k-1-l} ≤
1.9Nκ̂^{3/2}θq^{k-1-l}. ∎
*Remarks.* (1) Step (1) uses minimality; steps (2)-(3) hold at every τ-small critical point. (2) The decay rate is not L⁻³:
the funnel term costs an ADDITIVE C_qτ per level, because the non-abelian funnel rotates the current by the contour
holonomies Ad_{H_T}, whose spread is ∝ the level-(l+1) curvature (abelian: Ad = 1 and Lemma 3.1's exact L⁻³ returns). G6-F2
therefore occurs in the weak form "the exponent is 3 - O(τ)/log L, not 3", and does NOT occur in the form that matters:
θ_r > 2 from τ-smallness alone. (3) If, in addition, the curvature is in the decay class (f_{l+1} ≤ C_DθL^{-2(k-l-1)}) and the
residuals obey RES-dec, the per-level factor is L⁻³(1 + C_qL³(x + f)) with summable corrections, so x_c ≤ C'_rθL^{-3(k-1-l)},
C'_r := C_rexp(C_qL³(C_r + C_D)θ/(1 - L⁻²)) (residual exponent exactly 3, as in REG-lin (b)).
**[RSQ3-fix M3-6 (stated scope)]** "τ-small" includes "every cone plaquette below the top < τ" at levels ≥ 1: that is a
HYPOTHESIS of RES-dec, not a consequence. At level 0 it is automatic (||1 - U_0(p)|| ≤ √(2NE) ≤ 1.6√(Nκ_+)θ, M2-1). It is the
only place where sup-smallness of coarse curvature enters, and it is the hook of §13.6's feedback.

### 13.4 Lemma STOKES-NA (upward curvature transport, no level sum): PROVEN-HERE [S3-G] (counted) given HIST MSG step (1), Lemmas E2 and BCH-p
Let 1 ≤ j ≤ k - 1, q a level-j cone plaquette, R_q the union of the four level-(j-1) blocks at q's corners (a 2L × 2L × L × L
region, the shape of box_{k-1}; all contours of q's links lie in R_q). Put f̂ := max_{p ⊂ R_q}|log U_{j-1}(p)|_op, x := max
residual on q's four links, and assume m := 1.011A_axf̂ ≤ min{1/(40p_L), 1/C_e}, y_c ≤ 1/20, x ≤ 1/40. Then
  **|log U_j(q)|_op ≤ L²f̂ + 4.044x + C_S(f̂ + x)²**, C_S := L²C_pA_ax'² + 4C_e(A_ax' + 1.1)² + C_p(p_LA_ax' + 2.2)²
with A_ax' := 1.011A_ax, the last term read with ((p_L + 1)A_ax' + 2.2)² (C_S explicit; ≈ 3.8·10⁶ at N = 2, L = 3, crude).
*Proof.* Complete axial gauge on R_q (HIST MSG step (1) on a box of exactly box_{k-1}'s shape): |a_{j-1}| ≤ 1.011A_axf̂ =: m.
E2 on each link c of q: a_j(c) = (Qa_{j-1})(c) - ρ̃_c + e(c), |e|_HS ≤ C_e(m² + m|ρ̃|), |ρ̃|_op ≤ 1.011x (F1). Linear identity:
d(Qa_{j-1})(q) = (Q_2da_{j-1})(q) = Σ_pw_pda_{j-1}(p) with w_p ≥ 0, Σw_p = L² (dQ_root = dQ_str = Q_2d, §2, §11.3 (d)). BCH-p:
|da_{j-1}(p) - log U_{j-1}(p)|_HS ≤ C_pm². So |da_j(q)|_op ≤ L²f̂ + L²C_pm² + 4.044x + 4C_e(m² + 1.011mx). BCH-p on q:
|log U_j(q) - da_j(q)|_HS ≤ C_pm_j², m_j := max|a_j(c)| ≤ p_Lm + 1.011x + |e| ≤ (p_L + 1)m + 2.03x (C_em ≤ 1, |Qa| ≤ p_Lm).
Collect (op ≤ HS). ∎
*Why there is no level sum.* The main coefficient is EXACTLY L² (the Q_2 row sum) when sizes are measured by |log|_op, so
iterating multiplies by L² per level and nothing else; FORCE's L² + 4A_d + 8 (ribbons counted separately) would lose a factor
(1 + 44/L²) per level. The ribbons are inside Q_2's template (failure mode G6-F3 does NOT occur).
**[RSQ3-fix M3-7]** "y_c ≤ 1/20" is Lemma E2's hypothesis (§0.3, l.167: y_c := √N(s + 2s²e^s), s = p_Lm, the bound on the
contour logs |Z_T|_HS entering NA-alg (a)). Under m ≤ 1/(40p_L), s ≤ 1/40 and y_c ≤ 0.0263√N ≤ 1/20 for N ≤ 3; for N ≥ 4 it is
an extra smallness condition on m, kept in the statement.
**[RSQ3-fix S3-2 (recommended): Lemma STOKES-NA (avg).]** The linear identity used is a Q_2-weighted AVERAGE, which the max
form discards. The same proof gives, with no new input,
  |log U_j(q)|_op ≤ Σ_pw_p|log U_{j-1}(p)|_op + 4.044x + C_S(f̂ + x)²
(w_p ≥ 0, Σw_p = L²). Session 4 (§15.3) sharpens it further by making the quadratic error local (Σ_{p⊂R_q}|log U_{j-1}(p)|²
in place of f̂²).

**Corollary STOKES-it.** Let F_j := max_{level-j cone plaquettes}|log U_j|_op and X_j := max residual on level-(j+1) cone links.
Suppose F_0 ≤ 1.011A_0θn^{-2} and X_j ≤ C_rθq^{k-1-j} (RES-dec). Put B_0 := 4.1C_r/(1 - qL²), G := 2(1.011A_0 + B_0) and
θ_S := min{L⁴(1 - L⁻²)/(8C_SG), (1 - q²L²)G/(8C_SC_r²)}. If θ ≤ θ_S and STOKES-NA's smallness holds at every level, then
  **F_j ≤ GθL^{-2(k-j)}** for every j ≤ k - 1, uniformly in k.
*Proof.* G_j := F_jL^{2(k-j)}/θ, so G_0 ≤ 1.011A_0. STOKES-NA with (F + X)² ≤ 2F² + 2X² gives
G_j ≤ G_{j-1} + [4.044X_{j-1} + 2C_SF_{j-1}² + 2C_SX_{j-1}²]L^{2(k-j)}/θ. The three increments, summed over 1 ≤ j' ≤ j, under the
induction hypothesis G_i ≤ G (i < j): (i) 4.044C_r(qL²)^{k-j'} sums to ≤ B_0; (ii) 2C_SF_{j'-1}²L^{2(k-j')}/θ ≤
2C_SG²θL^{-2(k-j')-4} sums to ≤ 2C_SG²θL⁻⁴/(1 - L⁻²) ≤ G/4; (iii) 2C_SC_r²θ(q²L²)^{k-j'} sums to ≤ 2C_SC_r²θ/(1 - q²L²) ≤ G/4.
So G_j ≤ 1.011A_0 + B_0 + G/2 = G. ∎

### 13.5 Theorem RED-0 ((REG-min) ⟺ its level-0 clause): PROVEN as an implication [S3-G] (counted), given RES-dec, STOKES-NA (this section) and DESC-ε's conventions
Define **(EPS-0)**: there are τ_0 > 0, A_0 < ∞ depending only on (N, L, κ_±) such that for every depth k, every level-k
plaquette P and every τ_0-small minimiser of E_𝒞(P): **max_{level-0 p}||1 - U_0(p)|| ≤ A_0θn^{-2}** (n = L^k, θ = ||1 - V_P||).
Then: **(EPS-0) ⟹ (REG-min)** with τ_R := min{τ_0, τ_*, τ_S, θ_S/C'} (τ_S: the size at which STOKES-NA's smallness
conditions hold, since m ≤ 1.011²A_axτ; a τ_R-small minimiser has θ < C'τ_R ≤ θ_S by FORCE (strict form)) and C_D := max{G,
C_r}: (D1) by STOKES-it (||1 - U|| ≤ |log U|_op; F_0 ≤ 1.011A_0θn^{-2} by (F1)), (D2) by RES-dec (q ≤ L⁻²); the top residuals are
step (1) of RES-dec. **(REG-min) ⟹ (EPS-0)** trivially ((D1) at i = 0, A_0 = C_D, τ_0 = τ_R). ∎
**Consequences.** (i) (CLS-min) ⟸ (REG-min) [DESC (b), §0.3] ⟸ (EPS-0). (ii) DESC-ε and AE-red's two conclusions (§0.3, §0.5)
⟸ (EPS-0). (iii) (MIN-reg)_cone in BFT's 𝔐-ball, sup part (REVIEW_SQ_S2 S2-6) ⟸ (EPS-0) at rate θ_w = 2 for curvature and
θ_r > 2 for residuals; BFT's Hölder part and uniqueness are not supplied. (iv) The multi-level wall is now a statement
about the level-0 field alone: **sup decay of the finest curvature of small cone minimisers at the scale of the whole box.**
**[RSQ3-fix S3-3]** RED-0 is a correct implication, but a corollary of the counted items (one direction is a definition, the
other composition). It is NOT a separate counted item. §14's tally is corrected accordingly.
**[RSQ3-fix S3-6 (binding): (EPS-0) restated, old text kept above.]** **(EPS-0)** [conclusion unchanged; hypothesis read
critically]: there are θ_0 > 0 and A_0 < ∞ depending only on (N, L, κ_±) such that for every k, every level-k plaquette P
and every minimiser of E_𝒞(P) that is τ_0-small at levels ≥ 1, with θ = ||1 - V_P|| ≤ θ_0: max_{level-0 p}||1 - U_0(p)|| ≤
A_0θn⁻². Level-0 smallness is automatic (sup ≤ √(2NE); ℓ²-energy ≤ κ_+π²θ²/8 on every sub-box); no other smallness is
assumed. It splits as (REVIEW_SQ_S3): **(EPS-0a)** single-level lattice ε-regularity: there are ε_*, C depending on (N, L)
such that for every level-0 cube B_R of the REFL extension of a cone critical point, if Σ_{B_R}|𝒫|² ≤ ε_* and
R³sup_{B_R}|𝒮| ≤ ε_*^{1/2}, then sup_{B_{R/2}}|𝒫| ≤ C[R⁻²(Σ_{B_R}|𝒫|²)^{1/2} + R·sup_{B_R}|𝒮|]; and **(EPS-0b)** the critical
source bound n³sup_{box_0}|𝒮| ≤ C_𝒮θ for every τ_0-small minimiser, C_𝒮 depth-uniform (residual exponent exactly 3), named
as the real wall. (EPS-0) ⟸ (EPS-0a) at R ≍ n + (EPS-0b). (Session 4, §15, proves (EPS-0a) in a stronger ℓ^q-source form and
replaces (EPS-0b) by an averaged form that suffices.)

### 13.6 Is (EPS-0) decoupled? Route (b): the single-level ε-regularity step [lattice Kato: PROVEN-HERE, not counted; the rest ARGUED]
- **Level-0 equation.** RT-NA's derivation at l = -1 (U_0(b) enters plaquettes and the level-0 kernel terms): the covariant
  Wilson equation (D*_{U_0}𝒫)(b) = 𝒮(b), 𝒫(p) := the su(N) projection of U_0(p) (sin-type), with 𝒮 = -(𝒯j_0 - e_{-1}) and, by
  the funnel cancellation and CC-NA at level-1 sites, n³sup|𝒮| ≤ Cθ(L³q)^k = Cθ(1 + C_qL³τ)^k. Bianchi holds exactly for the
  group-valued plaquettes (the transported face holonomies of a 3-cell multiply to 1).
- **Lattice Kato (PROVEN-HERE).** For any su(N)-valued field u on the lattice and links U: ||u(x)| - |u(x + e)|| ≤ |u(x) -
  Ad_{U(b)}u(x + e)| (Ad isometric), hence Σ_e(|u(x)| - |u(x + e)|) ≤ ⟨u(x)/|u(x)|, (∇*_U∇_Uu)(x)⟩. Exact; no smallness.
- **The ε-regularity architecture [ARGUED].** Kato + a lattice Weitzenböck identity for ∇*∇𝒫 (= D D*𝒫 + D*D𝒫 + commutator
  terms of size C|𝒫|² + C|𝒫|³) give -Δ|𝒫| ≤ C|𝒫|² + |∇𝒮| + (Bianchi-defect terms) on the REFL-extended box (the nonlinear REFL
  of §11.6 (NA-1), still ARGUED). The potential V := C|𝒫| has Σ_{box}V² ≤ 2NC²E ≤ Cθ², small in the CRITICAL norm ℓ² (d/2 = 2),
  uniformly in n; Moser iteration with a small critical potential plus the lattice Sobolev inequality ||u||_{ℓ⁴} ≤ C_Sob||∇u||_{ℓ²}
  on Z⁴ (single level, scale-free) is the 4D ε-regularity mechanism (Uhlenbeck's; [not-read this session]). Its output would be
  sup|𝒫| ≤ C[n^{-2}√E + n·sup|𝒮| + (defect terms)]. Two points are not settled: (b1) the lattice Bianchi identity holds for
  group-valued plaquettes, not for 𝒫, and its defect D𝒫 = O(|𝒫|²) enters through D*(D𝒫), a divergence-form term whose
  drift coefficient is ~ |𝒫| (bounded only by τ in lattice units, supercritical at scale n); (b2) Moser at the critical
  exponent needs an L^{2+} improvement first (standard in the continuum).
  **[RSQ3-fix S3-4 (binding): (b1) as stated is WRONG; corrected, old text kept.]** On the lattice the Bianchi-defect term is
  not a supercritical drift. D𝒫 = O(|𝒫|²) pointwise (BCH of the transported face holonomies), and a lattice difference is
  bounded by neighbouring values, so |D*(D𝒫)(x)| ≤ C(M|𝒫|)(x)², M the neighbour maximum: a POTENTIAL term V·(M|𝒫|) with
  V = CM|𝒫|, Σ_{box}V² ≤ C'E ≤ C''θ², small in the critical norm ℓ². Read as a drift with coefficient |𝒫|, its critical norm
  is ℓ⁴, and on the lattice ||𝒫||_{ℓ⁴} ≤ ||𝒫||_{ℓ²}: small. "|𝒫| ≤ τ in lattice units" is a supercritical norm and the wrong
  yardstick. (b2) is standard (REVIEW_SQ_S3: Uhlenbeck absorption with a potential small in ℓ²). Session 4 (§15.1) proves the
  resulting ε-regularity (Theorem EPS-T).
- **Coupling (G6-F4 OCCURS).** Even granted (b1)-(b2), the source term gives n²sup|𝒫| ≲ θ(1 + C_qL³τ)^k, which is not
  depth-uniform. With curvature in the decay class the funnel corrections are summable (RES-dec Remark (3)): writing
  A := n²sup|F_0|/θ, the closed system is A ≤ C_1 + C_2exp(C_3Aθ), whose small branch A ≤ 2C_1 holds for θ ≤ θ_A, and whose
  large branch A ≳ 1/θ (concentration of level-0 curvature at a scale ≪ n) is NOT excluded by this argument (the a-priori bound
  is only A ≤ τn²/θ). So the large branch of REVIEW_SQ_S1 S1-4 (β) survives, now LOCALISED: it is level-0 concentration, fed
  back through the non-abelian funnel rotation of the residual currents. Excluding it is the genuine content of ε-regularity
  (energy ≤ κ_+θ² ≪ 1 at every scale forbids a concentrated critical configuration) and is not proven here.
  **[RSQ3-fix S3-5 (binding)]** Read "G6-F4 occurs for the sup-norm closure of §13.6 (the large branch is not excluded by
  this argument); no large-branch minimiser is exhibited, and none is expected" in place of "G6-F4 OCCURS" (here, in the
  bullet title, and in §14). The large branch is an artefact of feeding a supercritical a-priori bound (A ≤ Cn² by M2-1) into a
  critical estimate; τ-small cone minimisers have energy ≲ θ² ≪ ε_0 at every scale and plaquettes deep in Lüscher's
  admissible sector, so no instanton, dislocation or bubble lies in the hypothesis class (REVIEW_SQ_S3 Priority 3 (i), reviewer
  ARGUED with cited literature). The wall is not a large-field problem and is not routed to RLARGE's pricing.
- **Exact wall (named).** **(EPS-0)**; equivalently (by RED-0) (REG-min); its sub-wall is the critical single-level step
  "no level-0 concentration in small-energy critical cone configurations" (a lattice ε-regularity theorem robust to the
  funnel feedback). This is single-level in its conclusion and in its Sobolev input (one box, Z⁴ lattice Sobolev), but
  coupled to all levels through 𝒮.
  **[RSQ3-fix S3-6]** The exact wall is restated as (EPS-0a) + (EPS-0b) (§13.5 [RSQ3-fix S3-6]), with (EPS-0b), the critical
  (exponent-3) source bound, named as the real wall; equivalently the multi-level funnel feedback must be summed in a
  Morrey/ℓ¹-averaged norm, not in sup.

### 13.7 Route (a): NF-uniq / S_E / (N1-bd) [verdict PROVEN-HERE as stated; nothing counted]
- **What NF-uniq is.** BFT_B Lemma NF-uniq (§19.9) is uniqueness of the critical point of the box GAUGE functional
  Φ_{U,X}(g) = Σ_b|log U^g(b)|² in 𝒲_δ (a gauge normal form), not uniqueness of a critical point of the ENERGY E_𝒞. It gives the
  box-Coulomb gauge; with Lemma REF/(N1-bd) (PROVEN there given (N1-G)), sup|w^c| ≤ C_B sup|(dw)^c| on Ñ_X: link sizes are
  controlled by curvature in sup, with no log (degree -1). This is the sup analogue of Uhlenbeck's gauge, and it is uniform in
  the level and the depth.
- **Why it does not give minimiser uniqueness box by box.** In any gauge, the Hessian of E_𝒞 at the flat chain restricted to a
  slice has smallest eigenvalue ≍ n⁻² on the level-0 box (Poincaré on a box of side ≍ n), while the nonlinear correction to
  the Hessian at a τ-small configuration is ≍ (link size) + (curvature) in lattice units. Convexity in a ball therefore needs
  level-0 curvature ≲ n⁻², which is (EPS-0) itself: the uniqueness ball is the decay class (REVIEW_SQ_S2 S2-6, now at level 0).
  Nesting the boxes does not help: the level-i sub-problem of the cone (levels < i free, level i fixed) is the same problem at
  depth i, with the same n⁻²-gap at its own level 0.
- **What route (a) contributes.** Once A ≤ 2C_1 (the small branch of §13.6), (N1-bd) converts the curvature bound into a link
  bound sup|a_0| ≤ C_BA θn⁻¹ in the box-Coulomb gauge of each Ñ_X, and NF-uniq makes that gauge canonical (covariant), so the
  linear/quadratic split of §13.6 can be done in that gauge without a log. It does not exclude the large branch.
- **[RSQ3-fix S3-7, M3-8 (binding)]** Relabel: §13.7 is a **reading (CONFIRMED by review); the convexity statement is ARGUED,
  for the sup/gap comparison only**. The sentence "Convexity in a ball therefore needs level-0 curvature ≲ n⁻²" is a
  statement about the METHOD (comparing the cubic correction with the n⁻² Poincaré gap in ||a||²), not a fact: in d = 4 the
  right comparison is with the Dirichlet form, |⟨F, [a ∧ a]⟩| ≤ ||F||_{ℓ²}||a||²_{ℓ⁴} ≤ C_Sob²||F||_{ℓ²}||∇a||², which gives slice
  convexity under small ℓ² curvature GIVEN a lattice Uhlenbeck gauge (small ℓ⁴ connection), which NF-ex does not supply (NF-ex
  needs max n|A| ≤ ε_0, the decay scale; so route (a) is downstream of (EPS-0) in its existence step too). Session 4 §15.4
  examines this route.

### 13.8 BFT-1 clause request (for lane A's owner; text, not applied)
"For SQ's (REG-min)/(MIN-reg)_cone, BFT-1 must be stated with: (1) **θ_w > 1 as a stated value** (SQ's DESC needs θ_w > 1; the
linear case gives 2; the constants of DESC degrade like (1 - L^{1-θ_w})⁻¹), not 'there exists θ_w ∈ (0, 2]'; (2) a residual
(soft-fluctuation) exponent **> 2** (SQ §13.3 delivers θ_r = -log_L(L⁻³ + C_qτ) > 2 at τ ≤ τ_*, and exactly 3 on the decay
class), whose sup part dominates Σ_dec's (D2); (3) a **free-boundary cone-box clause** (data: P's four links only, uniform in
k), either via REFL's reflection torus of level-k side (4, 4, 2, 2) or directly; on SQ's reading N5-sf0's box convention is a
local-chart convention inside a torus, not a free boundary (§11.6 [RSQ2-fix S2-5]); (4) the critical item is unchanged: an
ε-regularity or large-ball clause containing every τ_R-small cone minimiser; by SQ §13.5 it suffices to have it for the
level-0 curvature alone ((EPS-0)); (5) the identification of E_𝒞 with 𝔉_k restricted to the cone."
**[RSQ3-fix S3-6, S3-1 (§13.8)]** Item (3): the box clause is unproven (BFT_B l.240), not merely unread. Item (4): read "(EPS-0a)
+ (EPS-0b), or a critical-norm (Uhlenbeck-gauge) uniqueness clause for small-energy cone minimisers" in place of "an
ε-regularity or large-ball clause". Item (2): θ_r > 2 is DELIVERED (RES-dec); the BFT-side requirement is only that BFT's
residual norm be no weaker than RES-dec's. Items (1), (5) unchanged.

## 14. Session-3 outcomes against §T3 (ADDED AFTER the derivations; pointers only) and tally
- **Step 1: DONE.** S2-1a/b (§0.3), S2-2 (λ_0 renamed; compatibility dropped for (b)), S2-3 (scope of "no level weights";
  𝔑's residual weight), S2-4a-d (q3 reading, G4-F2 → EXPECTED), S2-5 (box clause checked on a limited reading), S2-6
  (circularity), M2-1 … M2-6; all tagged [RSQ2-fix].
- **G6: PARTIAL; the exact wall named.** PROVEN: CC-NA (§13.2), RT-NA + RES-dec (§13.3: the residual half of (REG-min),
  exponent > 2, no bootstrap), STOKES-NA + STOKES-it (§13.4: levels ≥ 1 from level 0, no level sum), RED-0 (§13.5:
  (REG-min) ⟺ (EPS-0)). OPEN: **(EPS-0)**, coupled to the funnel feedback (§13.6; G6-F4 OCCURS). Route (a): gives the canonical
  sup Coulomb gauge, not minimiser uniqueness (§13.7). Route (b): the architecture and its two unsettled points (b1), (b2),
  plus the coupling (§13.6). Chain: (CLS-min) ⟸ (REG-min) ⟺ (EPS-0). BFT-1 clause request: §13.8.
- **Failure modes.** G6-F1 does not occur (Lemma K (b)). G6-F2 occurs only in the weak form (exponent 3 - O(τ), still > 2).
  G6-F3 does not occur (STOKES-NA's coefficient is exactly L²). G6-F4 OCCURS (§13.6).
- **Check q4** (criteria 10:16:34 UTC before the script 10:17:12; lock 10:17:46-10:17:57; 10.6 s, 57 MB peak footprint; load
  5.7): **OVERALL FAIL as pre-registered (K3)**; K1 (8.9·10⁻¹⁶), K2 (3.0·10⁻⁸), K4 (6.0·10⁻⁹), K5 (3.7·10⁻¹¹), K6 (1.7·10⁻⁵) PASS. K3
  max 1.9·10⁻⁸ against 1e-8. Post-hoc diagnostic (scratchpad copy, one more lock hold 10:23:04-10:23:14): the excess occurs
  only for SU(3) (1.2-1.9·10⁻⁸), where W_0 is computed by BFGS; SU(2) (exact polar factor) gives ≤ 1.7·10⁻¹⁰, and the formula
  side is 0 exactly. Reading (post hoc): numerical noise of the SU(3) maximiser at the finite-difference step, not a defect
  of Lemma K (b); the FAIL stands as recorded.
  **[RSQ3-fix S3-8 (binding): the reading's mechanism is corrected; the FAIL stands.]** The K3 excess is the first-order
  error of the SU(3) BFGS maximiser (||ΔW_0|| = 3·10⁻⁸, REVIEW_SQ_S3 R1), which violates q4's own "≤ 1e-13" precondition; with a
  Newton W_0, K3 = 2.5·10⁻¹⁰ (REVIEW_SQ_S3; reproduced post hoc in q4b, §15.6). It does not depend on h and is not
  finite-difference noise. "The formula side is 0 exactly" is withdrawn: it is tautological (Z = W - V with V := the same
  computed W). A future identity check computes W_0 by Newton on the stationarity condition.
- **Tally, session 3 (this file; all unreviewed).** PROVEN-HERE, counted (4): Lemma CC-NA; Lemma RT-NA with Proposition
  RES-dec (one item); Lemma STOKES-NA with Corollary STOKES-it (one item); Theorem RED-0 (an implication in both directions,
  counted as PROVEN since both directions are proven given the counted items). Not counted: Lemma K, lattice Kato, the §13.7
  verdict. ARGUED: §13.6's ε-regularity architecture and the large-branch statement. OPEN: (EPS-0) (= (REG-min) by RED-0),
  non-abelian (SQ) (off-path).
- **File tally after session 3: PROVEN-HERE counted 12 (8 + 4) / CONDITIONAL 3 / OPEN 2 ((REG-min) ⟺ (EPS-0); non-abelian
  (SQ)).**
- **[RSQ3-fix S3-3, S3-5 (binding)]** RED-0 is an uncounted corollary: session 3 counts **3** items (CC-NA; RT-NA + RES-dec;
  STOKES-NA + STOKES-it), and the **file tally after session 3 is 11 / 3 / 2** (all four counted items CONFIRMED by
  REVIEW_SQ_S3). In "Failure modes" and in "G6" above read "G6-F4 occurs for the sup-norm closure only; no large-branch
  minimiser exhibited; none expected" in place of "G6-F4 OCCURS". In "Step 1" read "S2-5 (box clause; settled by S3-1)".
- **Hypotheses consumed (session 3).** RS (R1) (per-contour ribbon), Lemma PM (HIST), HIST MSG step (1), Lemmas E2, BCH-p, (F1),
  the S4' definition (LINEAR_PACKAGE §1.2), dQ_root = Q_2d. No literature item is load-bearing.
- **Not done / not claimed.** No edit outside SQ.md, SQ_LOG.md, checks/q*. No commits, PRs, pushes, CL or axiom edits.

# Session 4 (2026-10-28 UTC)

## T4. PRE-STATED (session 4) — statements only; the FIRST edit of session 4 (appended before any [RSQ3-fix] edit, before any session-4 proof, criteria file or script). Nothing in §T4 cites a result of this session. Reading of REVIEW_SQ_S3 (binding), SQ §13-§14, SQ_LOG, BFT_B §15-§16 and §18.0/§19.8-§19.13, HIST §20.2 (MSG) preceded this append, with exploratory reasoning (not recorded); its only claim is file order. Proofs follow in §15, later; outcomes are pointers in §16.

- **Step 1.** Apply REVIEW_SQ_S3's binding fixes S3-1 … S3-8 and M3-1 … M3-8 (S3-2 as recommended), tagged [RSQ3-fix],
  original text kept. Re-run q4's identity K3 with a Newton-solved SU(N) maximiser W_0 as a labelled POST-HOC check q4b
  (criteria file first); q4's recorded FAIL stays.
- **Notation (session 4).** box_0 := the level-0 cone box (sides (2, 2, 1, 1)n, n = L^k); 𝒫(p) := the traceless part of
  (U_0(p) - U_0(p)^*)/2 (a covariant su(N)-valued 2-form); 𝒮 := D*𝒫 on level-0 links (D* the free-boundary covariant
  co-differential = N × the left gradient of Σ_p s(U_0(p))); F_j(q) := |log U_j(q)|_op on level-j cone plaquettes;
  𝓔_j := Σ_{level-j cone plaquettes}F_j²; q > 4 a fixed exponent.
- **STEP 2 targets ((EPS-0a)).**
  - **Lemma NREFL (nonlinear reflection).** Reflecting U_0 across the faces of box_0 (tangent links copied, normal links
    reversed, crossing links := 1) gives a configuration on the torus 𝕋_R of sides (4, 4, 2, 2)n whose crossing plaquettes
    are flat and whose D*𝒫 equals the reflected box D*𝒫 (in norm) on image links and 0 on crossing links. [planned:
    PROVEN-HERE]
  - **Lemma BIA (Bianchi defect).** For every lattice configuration and every 3-cell c: |(D𝒫)(c)| ≤ C_B·max_{faces}|𝒫|² when
    all face plaquettes are small. [planned: PROVEN-HERE]
  - **Lemma WB (lattice Weitzenböck error).** K := ∇*∇𝒫 - DD*𝒫 - D*D𝒫 (∇*∇ the covariant Laplacian on each plaquette
    orientation class) obeys |K(p)| ≤ C_K·max_{q ∈ N_3(p)}||1 - U(q)||·max_{p' ∈ N_2(p)}|𝒫(p')|. [planned: PROVEN-HERE, with
    a numerical check of the identity and the bound in q5]
  - **Lemma SOB (lattice Sobolev, d = 4).** ||f||_{ℓ⁴(Z⁴)} ≤ C_S||∇f||_{ℓ²} for finitely supported f; and the cube
    Sobolev–Poincaré form. [planned: PROVEN-HERE (Gagliardo–Nirenberg on Z⁴)]
  - **Theorem EPS-T (lattice ε-regularity with an ℓ^q source).** There are ε_*, C depending only on (N, q) such that for
    every SU(N) configuration on a 4D lattice torus and every embedded cube B_R with ||𝒫||_{ℓ²(B_R)} ≤ ε_*:
    sup_{B_{R/2}}|𝒫| ≤ C[R⁻²||𝒫||_{ℓ²(B_R)} + R^{1-4/q}||D*𝒫||_{ℓ^q(B_R)}]. [planned: PROVEN-HERE (Moser iteration with a
    divergence-form source and a critical potential; constants uncomputed)]
  - **Corollary EPS-0a.** REVIEW_SQ_S3's (EPS-0a) for cone critical points on box_0 (via NREFL), in the ℓ^q-source form
    (which implies the sup-source form). [planned: PROVEN as an implication]
- **STEP 3 targets ((EPS-0b), the gauge, and the consumers).**
  - Route (α) (the instructed route: Dirichlet-form convexity in a lattice Uhlenbeck gauge):
    - **Lemma GS (Gaffney–Sobolev on the free-boundary box).** Every 1-form w on box_0 with Neumann d*w = 0 obeys
      ||w||_{ℓ⁴(box_0)} ≤ C_GS||dw||_{ℓ²(box_0)}, C_GS absolute (box shape fixed), depth-uniform. [planned: PROVEN-HERE via
      BFT_B Lemma REF + SOB]
    - **Theorem LU-ap (lattice Uhlenbeck a-priori estimate).** A Neumann-Coulomb representative w = log U_0^g (d*w = 0) with
      ||w||_{ℓ⁴} ≤ η_U obeys ||w||_{ℓ⁴} ≤ 2C_GS||log U_0(∂p)||_{ℓ²}. [planned: PROVEN-HERE]
    - **Lemma GAP.** A critical point of the free-boundary Wilson action on box_0 with energy ≤ ε_G² is flat. [planned:
      PROVEN as an implication of EPS-T + NREFL]
    - **Theorem LU-ex (existence).** Every level-0 configuration on box_0 with Wilson energy ≤ ε_U² has a Neumann-Coulomb
      gauge in LU-ap's small branch, depth-uniformly. [planned: PROVEN given GAP, LU-ap and the convergence of the lattice
      Wilson flow (Łojasiewicz; cited)]
    - **Route (α) verdict.** Whether E_𝒞 (all levels) is strictly convex on the Coulomb slice ball, giving minimiser
      uniqueness; or the exact obstruction. [planned: stated with proof of whatever is claimed]
  - Route (β) (averaged source, Carleson accounting):
    - **Lemma TPL (template).** The straight Stokes template (dQ_str = Q_2d) has weights w(q; p) = L⁻⁴·t(u_μ)t(u_ν) (t a tent of
      height L) on R_q, row sums L², and column sums ≤ L⁻² for every fine plaquette; hence the composed level-0 → level-j
      template W^{(j)} has sup ≤ L^{-2j}, row sums L^{2j}, column sums ≤ L^{-2j}. [planned: PROVEN-HERE; checked in q5]
    - **Lemma STOKES-avg (S3-2 with local errors).** F_j(q) ≤ Σ_pw_pF_{j-1}(p) + C_x·x(q) + C_E·Σ_{p ⊂ R_q}F_{j-1}(p)²
      under STOKES-NA's smallness. [planned: PROVEN-HERE (re-reading of STOKES-NA's proof)]
    - **Lemma LEV-E (level energies).** For every τ-small minimiser with θ ≤ θ_E: 𝓔_j ≤ 4(||F_0||_{ℓ²} + C_Xθ)² for every j,
      uniformly in k. [planned: PROVEN-HERE]
    - **Lemma LOC-T (local residual transport).** |j_l(b)| ≤ [L⁻³ + C_q'ε_l(b)]·max_{c' ∈ 𝒩(b)}|j_{l+1}(c')|, with ε_l(b) the
      local residual/curvature size on a bounded neighbourhood of b's ancestor; and the same for 𝒮 from j_0. Hence
      |𝒮(b)| ≤ C_0θn⁻³exp(C_1Σ_la_l(b)), a_l(b) := the maximal level-l (and level-(l+1)) curvature and residual size on a
      fixed coarse neighbourhood of b's level-l ancestor block. [planned: PROVEN-HERE (localisation of §13.3)]
    - **Lemma CARL (Carleson bound).** For every L-adic block Q of level M: avg_{x∈Q}Σ_{l≤M}a_l(x) ≤ β := C_β(||F_0||_{ℓ²} +
      θ), depth-uniform. [planned: PROVEN-HERE]
    - **Lemma GARSIA (exponential moments).** For a nonnegative adapted sum A = Σ_la_l on a finite filtration with
      E[Σ_{l ≤ M}a_l | F_M] ≤ β for every M: E[e^{λA}] ≤ (1 - λβ)⁻¹ for λβ < 1. [planned: PROVEN-HERE (classical)]
    - **Proposition EPS-0b-avg.** For every τ-small minimiser with θ ≤ θ_G: avg_{box_0}|𝒮|^q ≤ 2(C_0θn⁻³)^q. [planned:
      PROVEN as an implication of the five items above]
  - **Theorem EPS-0 (target).** (EPS-0) of §13.5 holds: EPS-T + NREFL + EPS-0b-avg give max_{level-0 p}||1 - U_0(p)|| ≤ A_0θn⁻²
    for every τ_0-small minimiser with θ ≤ θ_0, A_0, θ_0, τ_0 depth-uniform. [planned: PROVEN as an implication]
  - **Corollaries.** (REG-min) by RED-0; (CLS-min) by DESC (b); the pointwise (EPS-0b) a posteriori (n³sup|𝒮| ≤ Cθ) by
    STOKES-it and LOC-T. [planned: PROVEN as implications, given the reviewed items they cite]
- **Checks (criteria first).** q4b (post hoc, labelled): K3 with Newton W_0. q5: exact/elementary identities only — TPL's
  weights and column sums on a 4D block pair; BIA and WB bounds on random small-field SU(2) configurations on a 4D torus
  (the abelian identity DD* + D*D = ∇*∇ to round-off at U = 1 + linear); NREFL (flat crossing plaquettes, |D*𝒫| equality);
  GARSIA on random adapted trees. Jobs < 20 min, < 1 GB.
- **Failure modes (pre-stated).** (S4-F1) WB's error is first order in a difference of 𝒫, not zeroth order (then EPS-T needs
  a different route). (S4-F2) TPL's column sums exceed L⁻² somewhere (then the composed template sup grows geometrically and
  CARL fails). (S4-F3) LEV-E's recursion compounds ((1 + Cτ)^j). (S4-F4) LOC-T needs non-local maxima (the funnel
  cancellation is not local). (S4-F5) Route (α)'s slice is not coercive in the critical norm (corner pinning by the fixed top;
  kernel spread terms without a curvature-decay factor).

## 15. Session-4 derivations (written after §T4 (11:14:39 UTC), after Step 1 (11:15-11:17 UTC) and after q4b and q5 ran (11:29:41-11:29:50 UTC); post-hoc diagnostics 11:30-11:31 UTC)

Post-proof corrections of §T4's statements are marked **[post-proof correction]** where they occur; §T4 is not edited. In
brief: (1) EPS-T's hypothesis is read on B_R with all local operators evaluated inside B_{R-4} (cutoffs supported there);
(2) LOC-T's neighbourhood is the 2-block neighbourhood of the level-(l+3) ancestor block; (3) GAP and LU-ex need no
Łojasiewicz input (a subsequence of the flow suffices); (4) route (α)'s corner-pinning obstruction (S4-F5, first half) does
NOT occur (§15.4); (5) q5's T2 FAIL is a definition error in the script, not in TPL (§15.5); (6) EPS-T needs, besides small
ℓ² curvature, the scale-invariant smallness of the source R^{3-4/q}||𝒮||_{ℓ^q(B_R)} ≤ ε_* (it holds in every application below).

### 15.0 Conventions (session 4)
- su(N) with ⟨A, B⟩ = Re tr(A*B), |·| = |·|_HS. A 2-form u assigns u_{μν}(x) ∈ su(N) to the plaquette based at x in the
  (μ, ν) plane (u_{νμ} = -u_{μν}); 1-forms α_μ(x) on links (x, x + e_μ); 3-forms on 3-cells (x; λ < μ < ν). For a lattice
  configuration U: **straight covariant operators** (transport along the links at the base point only):
  ∇_λu_{μν}(x) := Ad_{U(x,λ)}u_{μν}(x + e_λ) - u_{μν}(x);
  (D_1α)_{μν}(x) := α_μ(x) + Ad_{U(x,μ)}α_ν(x + e_μ) - Ad_{U(x,ν)}α_μ(x + e_ν) - α_ν(x);
  (D_2u)_{λμν}(x) := ∇_λu_{μν}(x) - ∇_μu_{λν}(x) + ∇_νu_{λμ}(x);
  adjoints D_1*, D_2*, ∇_λ* with respect to Σ⟨·,·⟩ over the region; ∇*∇ := Σ_λ∇_λ*∇_λ (on each orientation class).
  At U ≡ 1 these are the forward-difference d, d and ∂_λ of the cubical complex.
- 𝒫(p) := the traceless part of (U(p) - U(p)*)/2, U(p) = U(x,μ)U(x+e_μ,ν)U(x+e_ν,μ)*U(x,ν)* (a gauge-covariant 2-form). For
  ||1 - U(p)|| ≤ ¼: c_N⁻¹|log U(p)| ≤ |𝒫(p)| ≤ |log U(p)| with c_N depending on N only (eigen-angles θ_j, Σθ_j = 0,
  |sin θ - θ| ≤ |θ|³/6).
- **The true linearisation** D_1^tr: d/dt U_t(p)U(p)⁻¹|_0 = (D_1^trα)(p) for U_t(b) = e^{tα(b)}U(b). Then
  d/dt Σ_ps(U_t(p))|_0 = N⁻¹⟨D_1^trα, 𝒫⟩ (Re tr(AU) = Re tr(A𝒫) for A ∈ su(N)), so **𝒮 := (D_1^tr)*𝒫 is N × the left gradient
  of the Wilson part**, and at a cone critical point the level-0 Euler-Lagrange equation reads 𝒮(b) = -N·(the left
  gradient of the level-0 kernel terms at U_0(b)) (§13.6's equation with this normalisation). D_1^tr differs from D_1 only in
  the transports of the last two terms (paths around ≤ one plaquette), so **|(D_1^tr - D_1)α(p)| ≤ 4||1 - U(p)||·max_{b∈∂p}|α(b)|**
  (||Ad_A - Ad_B|| ≤ 2||A - B||), hence 𝒮 = D_1*𝒫 + R_1 with **|R_1(b)| ≤ 4Σ_{p∋b}||1 - U(p)|||𝒫(p)|**.
- "M_r f(p)" := max of |f| over the objects within ℓ^∞ distance r of p's base point.

### 15.1 STEP 2: (EPS-0a)

**Lemma NREFL (nonlinear reflection): PROVEN-HERE [S4-G]** (checked in q5 R1). Let box_0 = Π_ν[0, S_ν), S = (2n, 2n, n, n),
𝕋_R := Π_ν Z/(2S_νZ), ϱ_ν: z_ν ↦ -1 - z_ν (mod 2S_ν). Every torus site is w = ϱ_Az for a unique box site z and A ⊂ {1..4}.
Define U^R on torus links (w, w + e_μ): := 1 if the link crosses a reflection plane (w_μ ∈ {S_μ - 1, 2S_μ - 1}); := U_0(z, z + e_μ)
if μ ∉ A; := U_0(z - e_μ, z)⁻¹ if μ ∈ A. Then: (a) every plaquette containing a crossing link is flat; (b) every other torus
plaquette has holonomy conjugate to U_0(p) or U_0(p)⁻¹ for a unique box plaquette p, so Σ_𝕋|𝒫|² = 16Σ_{box_0}|𝒫|²; (c) 𝒮^R(b) =
𝒮(b) on box links, |𝒮^R| equals |𝒮| at the preimage on every non-crossing link, and 𝒮^R = 0 on crossing links; so
Σ_𝕋|𝒮^R|^q = 16Σ_{box_0}|𝒮|^q.
*Proof.* (a) A crossing link in direction ν lies in a plaquette (ν, t) whose two ν-links both cross the same plane; its two
t-links are mirror images across that plane, and the assignment rule depends only on (z, A \ {ν} ∩ {t}) — the same for both —
so they carry the same matrix W (or both 1): the holonomy is W·1·W⁻¹·1 = 1. (b) The map ϱ_A is a lattice automorphism
carrying box plaquettes onto the non-crossing plaquettes; reversing the μ ∈ A directions maps the holonomy to its inverse
up to conjugation. (c) A torus plaquette containing a box link is a box plaquette or contains the links leaving the box
from the endpoints of that link, which cross a plane: by (a) it is flat and contributes 𝒫 = 0 and, being flat, zero gradient.
So the torus gradient at a box link is the free-boundary box gradient. Images follow by the automorphism (left and right
gradients of a link and of its inverse have equal norm). A crossing link lies only in crossing plaquettes. ∎
(q5 R1: crossing plaquettes 2.2·10⁻¹⁶, box-link gradients equal to 2.8·10⁻¹⁷, norms on all links to 5.6·10⁻¹⁷, energy ratio
exact.)

**Lemma BIA (Bianchi defect): PROVEN-HERE [S4-G]** (q5 B1). If ||1 - U(f)|| ≤ ¼ for the six faces f of a 3-cell c, then
**|(D_2𝒫)(c)| ≤ C_B·(max_{f ⊂ c}||1 - U(f)||)²**, C_B = C_B(N).
*Proof.* D_2𝒫(c) transforms by Ad_{g(x)} under gauges, so its norm is gauge invariant. Choose the gauge in which the seven
edges 000-100, 000-010, 000-001, 100-110, 100-101, 010-011, 110-111 of the cube carry 1 (a spanning tree). The five other
edges carry V_e = the holonomy of their fundamental cycle, which bounds one face (010-110, 001-101, 001-011, 101-111) or two
faces (011-111: faces y = 1 and z = 0); by the lasso decomposition and bi-invariance ||V_e - 1|| ≤ 2ε, ε := max_f||1 - U(f)||.
Every face holonomy is a product of ≤ 2 of the V_e^{±1} (tree edges are 1), so log U(f) = Σ_{e∈f}±log V_e + O(|log V|²) (BCH), and
Σ_fε_flog U(f) = O(ε²) because each edge lies in exactly two faces with opposite induced orientations (abelian dd = 0). In
D_2 the transports are Ad of edges at x (tree edges: 1), and the faces at x + e_λ are based at a tree-gauge vertex, so
D_2𝒫(c) = Σ_fε_f𝒫(f) exactly in this gauge, and 𝒫(f) = log U(f) + O(|log U(f)|³). Hence |D_2𝒫(c)| ≤ C_Bε². ∎ (q5 B1: R_B :=
|D_2𝒫|/ε² = 3.6, 3.4, 3.1 at η = 0.04, 0.02, 0.01; gauge invariant to 2·10⁻¹³.)

**Lemma WB (lattice Weitzenböck error): PROVEN-HERE [S4-G]** (q5 W1-W3). Let **K := ∇*∇ - D_1D_1* - D_2*D_2** (a linear
operator on 2-forms, depending on U). Then K(u)(p) = Σ_{p' ∈ N_2(p)}k(p, p')u(p') with **||k(p, p')|| ≤ C_K·M_3η(p)**, η(q) :=
||1 - U(q)||, C_K absolute; in particular |K(u)(p)| ≤ C_K'·M_3η(p)·M_2u(p). S4-F1 does NOT occur.
*Proof.* (i) At U ≡ 1, K = 0: on the cubical complex of Z⁴ (or a torus) with forward differences, dd* + d*d = Σ_λ∂_λ*∂_λ on
2-forms componentwise (the Hodge Laplacian of a product complex is the sum of the one-dimensional Laplacians) [standard;
q5 W1: max|K| = 0 exactly at U = 1]. (ii) All three operators are gauge covariant, so K is; hence ||k(p, p')|| is gauge invariant.
(iii) Fix p and the box B of ℓ^∞ radius 3 around its base. In the complete axial gauge of B every link of B carries the
holonomy of a ladder of ≤ 12 plaquettes of B (HIST MSG step (1) on a box of side 7: Σ_{ν>μ}|x_ν| ≤ 3·... ≤ 12 with the order
starting in p's plane; crude), so ||U(b) - 1|| ≤ 12·M_3η(p). Each of ∇*∇, D_1D_1*, D_2*D_2 applied at p is a finite sum (≤ 200
terms) of ±Ad_{γ}u(p'), γ a product of ≤ 4 links of B, p' ∈ N_2(p); write Ad_γ = 1 + (Ad_γ - 1) with ||Ad_γ - 1|| ≤ 2·4·12·M_3η(p).
The "1" parts sum to the abelian expression, which vanishes by (i). ∎ (q5 W2: K = 3.6·10⁻¹⁵ on a Haar-random pure gauge; W3:
||K||_op/η_P = 3.5, 3.5, 3.9 at η = 0.04, 0.02, 0.01, gauge invariant to 1·10⁻¹⁴.) On the lattice "zeroth order" and "first
order with a small coefficient" coincide: every local operator with entries O(η) is a potential term; this is all EPS-T uses.

**Lemma SOB (lattice Sobolev and Sobolev-Poincaré, d = 4): PROVEN-HERE [S4-G] (standard proof, reproduced).** (a) For
finitely supported f on Z⁴ (scalar or vector valued): ||f||_{ℓ⁴} ≤ C_S||∇f||_{ℓ²}, C_S absolute. (b) For a box Q = Π[0, S_ν)
with S_max ≤ 2S_min and any f on Q: ||f - f̄||_{ℓ⁴(Q)} ≤ C_SP||∇f||_{ℓ²(Q)} (differences inside Q only), C_SP := 27C_S. The same
holds on a torus (more differences, same mean). (c) On the lattice ||f||_∞ ≤ ||f||_{ℓ^r} for every r.
*Proof.* (a) Discrete Gagliardo-Nirenberg: |g(x)| ≤ G_i(x̂_i) := Σ_{t}|∇_ig| along the i-th line through x; so |g|^{4/3} ≤
Π_iG_i^{1/3} and the discrete Loomis-Whitney inequality (repeated Hölder over the four coordinates; a combinatorial
inequality, valid on Z⁴) gives ||g||_{ℓ^{4/3}} ≤ Π_i(Σ_x|∇_ig|)^{1/4} ≤ ¼Σ_iΣ_x|∇_ig|. Apply it to g := |f|³:
||a|³ - |b|³| ≤ 3(|a|² + |b|²)|a - b|, so Σ_x|∇_ig| ≤ 3Σ_x(|f(x)|² + |f(x + e_i)|²)|∇_if(x)| ≤ 6||f||²_{ℓ⁴}||∇_if||_{ℓ²}
(Cauchy-Schwarz), and Σ_i||∇_if|| ≤ 2||∇f||_{ℓ²}: ||f||³_{ℓ⁴} ≤ 3||f||²_{ℓ⁴}||∇f||_{ℓ²}, i.e. C_S = 3. (b) Reflect f evenly across all faces of Q to 3Q (z ↦ -1 - z
etc.); differences across reflection planes vanish, so ||∇f^e||²_{3Q} ≤ 81||∇f||²_Q. Take η = 1 on Q, supported in 3Q,
|∇η| ≤ 2/S_min. By (a), ||f - f̄||_{ℓ⁴(Q)} ≤ C_S(||∇f^e||_{3Q} + (2/S_min)||f^e - f̄||_{3Q}) ≤ C_S(9 + 18S_max/(2S_min))||∇f||_Q
(Neumann Poincaré ||f - f̄||_Q ≤ (S_max/2)||∇f||_Q from the path-graph gap 4sin²(π/2S) ≥ 4/S²) ≤ 27C_S||∇f||_Q. (c) trivial. ∎

**Theorem EPS-T (lattice ε-regularity with an ℓ^q source): PROVEN-HERE [S4-G] (counted, with NREFL, BIA, WB, SOB as its
lemmas; constants uncomputed; the Moser iteration is written at the level of its inequalities).** Fix q > 4. There are
ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q) such that for every SU(N) configuration on a 4D lattice torus (or on Z⁴) and every
embedded cube B_R (R ≥ 1) with ||𝒫||_{ℓ²(B_R)} ≤ ε_* **and R^{3-4/q}||𝒮||_{ℓ^q(B_R)} ≤ ε_*** **[post-proof correction (6):
the scale-invariant smallness of the source, the ℓ^q analogue of REVIEW_SQ_S3's R³sup|𝒮| ≤ ε_*^{1/2}, is needed in Stage 2;
§T4 omitted it]**:
  **sup_{B_{R/2}}|𝒫| ≤ C_T[R⁻²||𝒫||_{ℓ²(B_R)} + R^{1-4/q}||𝒮||_{ℓ^q(B_R)}],** 𝒮 = (D_1^tr)*𝒫.
**[post-proof correction (1)]**: all local operators are evaluated at plaquettes of B_{R-4} (the cutoffs below are supported
there); for R < R_0 := 64 the statement is trivial (sup ≤ ||𝒫||_{ℓ²} ≤ R_0²R⁻²||𝒫||), so let R ≥ R_0.
*Proof.* Write u := 𝒫, ε := ||u||_{ℓ²(B_R)}; |u| ≤ ε pointwise on B_R (SOB (c)), so every plaquette of B_R has
η ≤ c_Nε ≤ ¼ and the lemmas apply. Put k := R^{1-4/q}||𝒮||_{ℓ^q(B_R)} (k > 0; k → 0 is a limit) and w := (|u|² + k²)^{1/2}.
(1) *Identity.* With B := D_2u and D_1*u = 𝒮 - R_1 (§15.0): **∇*∇u = D_1(𝒮 - R_1) + D_2*B + K(u)**, |R_1|, |B| ≤ C(M_1u)²
(BIA, §15.0; η ≤ c_N|u|), |K(u)| ≤ C(M_3u)(M_2u) (WB).
(2) *Pairing.* For ψ ≥ 0 on plaquettes supported in B_{R-4}: Σ_λ⟨∇_λu, ∇_λ(ψu)⟩ = ⟨𝒮 - R_1, D_1*(ψu)⟩ + ⟨B, D_2(ψu)⟩ + ⟨K(u), ψu⟩.
For a := u(p), b := Ad u(p + e_λ) (|b| = |u(p + e_λ)|): ⟨b - a, ψ_bb - ψ_aa⟩ = ψ̄|b - a|² + ½(ψ_b - ψ_a)(|b|² - |a|²), ψ̄ := (ψ_a + ψ_b)/2.
Take ψ := ζ²w^{β-1} (β ≥ 1, ζ a cutoff, |∇ζ| ≤ 4/r on its support of radius r): the part ½ζ_b²(w_b^{β-1} - w_a^{β-1})(|b|² - |a|²)
is ≥ 0 (both factors have the sign of |b| - |a|), and the cutoff part is ≤ δψ̄|b - a|² + C_δ|∇ζ|²(w_a^{β+1} + w_b^{β+1}). So
  LHS ≥ (1 - δ)Σψ̄|∇u|² - C_δΣ|∇ζ|²w^{β+1}.
(3) *Right side.* D_1*(ψu)(b) and D_2(ψu)(c) are sums of ≤ 6 covariant differences ∇(ψu) = ψ'∇u + (∇ψ)u (exact discrete
product rule, ψ' a shifted value), and |∇ψ| ≤ 2ζ̄|∇ζ|w̄^{β-1} + ζ²(β - 1)w_max^{β-2}|∇w|, |∇w| ≤ |∇u| (Kato: t ↦ (t² + k²)^{1/2} is
1-Lipschitz and Ad is isometric). Each right-hand term is bounded, by Cauchy-Schwarz and Young, by
δΣψ̄|∇u|² + C_δβ²[Σ_pV(p)ζ̃(p)²w̃(p)^{β+1} + Σ|∇ζ|²w^{β+1}], where ζ̃, w̃ are maxima over N_3(p) and
  **V := C[M_3u + (M_3u)² + |𝒮|_loc²/k²]** (|𝒮|_loc(p) := max of |𝒮| on the links of N_1(p)).
For the source: ψ̄|𝒮|² ≤ ζ̄²w_max^{β-1}|𝒮|² ≤ ζ̄²w_max^{β+1}|𝒮|²/k²; for R_1 and B: ψ̄(M_1u)⁴ ≤ ζ̄²w_max^{β+1}(M_1u)²; for K:
ψ|u|(M_3u)(M_2u) ≤ ζ²w^β·(M_3w)² and w_a^β w_b² ≤ w_a^{β+1} + w_b^{β+1} (Young). The neighbour maxima are moved onto a single
site by w(p)^αw(p')^γ ≤ w(p)^{α+γ} + w(p')^{α+γ} and ζ(p)² ≤ 2ζ(p')² + 2(6/r)² for |p - p'| ≤ 3; the extra (6/r)² terms are of the
cutoff type, since V ≤ C pointwise.
(4) *Energy inequality (all β ≥ 1).* With W := w^{(β+1)/2}: |∇(ζW)|² ≤ C β²ψ̄|∇u|² + C|∇ζ|²W̄² (discrete chain rule: |∇W| ≤
((β+1)/2)w_max^{(β-1)/2}|∇w| and ψ̄ ≥ ½ζ_min²w_max^{β-1}, ζ_max² ≤ 2ζ_min² + C/r²). Hence
  **Σ|∇(ζW)|² ≤ C_1β⁴[Σ_pV ζ̃²W̃² + r⁻²Σ_{supp⁺}W²]**  (★)
(supp⁺: the support enlarged by 3).
(5) *Stage 1 (β = 1): critical absorption.* Split V = V_c + V_s, V_c := C[M_3u + (M_3u)²], V_s := C|𝒮|_loc²/k². ||V_c||_{ℓ²(B_R)}
≤ C'(ε + ε²) (neighbour maxima cost a bounded factor; ℓ⁴ ≤ ℓ² on the lattice). By SOB (a) and Hölder,
Σ V_cζ̃²W̃² ≤ C''||V_c||_{ℓ²}||ζ̃W̃||²_{ℓ⁴} ≤ C'''ε||∇(ζW)||² + (cutoff terms), absorbed for ε ≤ ε_*. For V_s: ||V_s||_{ℓ^{q/2}(B_R)} ≤
C||𝒮||²_{ℓ^q}/k² = CR^{-2+8/q}, and q/2 > 2 = d/2; Hölder with exponents q/2 and q/(q - 2), interpolation of ℓ^{2q/(q-2)}
between ℓ² and ℓ⁴ (2q/(q - 2) < 4) and Young give Σ V_sζ̃²W̃² ≤ δ||ζ̃W̃||²_{ℓ⁴} + C_δR⁻²||ζ̃W̃||²_{ℓ²} (the scaling is exact:
R^{2-8/q}||V_s||_{q/2} = C). With SOB (a) on the left of (★): ||w||_{ℓ⁴(B_{3R/4})} ≤ C R⁻¹||w||_{ℓ²(B_{7R/8})}.
(6) *Stage 2 (β ≥ 1): supercritical potential, finite iteration.* Since kR² = R^{3-4/q}||𝒮||_{ℓ^q} ≤ ε_*, ||w||_{ℓ²(B_R)} ≤
ε + √6kR² ≤ 4ε_*. Now V_c ≤ C(M_3w)(1 + ε) lies in ℓ⁴(B_{3R/4 - 3}) with R||V_c||_{ℓ⁴} ≤ CR·R⁻¹||w||_{ℓ²(B_R)} ≤ C'ε_* (Stage 1),
and V_s as before: both are supercritical (exponents 4 and q/2 > 2) with scale-invariant norms ≤ C. (★)
with Hölder, interpolation and SOB gives, for p_i := 2χ^i (χ = 2), radii r_i := R/2 + R2^{-i-3} and cutoffs between r_{i+1}
and r_i (r_i - r_{i+1} = R2^{-i-4} ≥ 4 as long as 2^{i+6} ≤ R):
  ||w||_{ℓ^{p_{i+1}}(B_{r_{i+1}})} ≤ (C16^iβ_i⁴)^{1/p_i}(R2^{-i})^{-2/p_i}||w||_{ℓ^{p_i}(B_{r_i})},  p_{i+1} = 2p_i, β_i + 1 = p_i,
the standard Moser step ((★) with ||ζW||²_{ℓ⁴} = ||w||^{p_i}_{ℓ^{2p_i}}, the cutoff gradient ≤ 2/(r_i - r_{i+1}), and the
supercritical potentials absorbed by Hölder, interpolation and Young at a cost polynomial in β_i). Iterate for
i < i_* := ⌊log_2R⌋ - 6. The products Π_i(C16^iβ_i⁴)^{1/p_i} converge (Σ_i i/2^i < ∞), and the radius powers multiply to
R^{-Σ_{i<i_*}2/p_i} = R^{-2 + 4/p_{i_*}} with R^{4/p_{i_*}} ≤ R^{256/R} ≤ e^{100} (p_{i_*} ≥ R/64). SOB (c) gives sup ≤ ℓ^{p_{i_*}}. Hence sup_{B_{R/2}}w ≤ C R⁻²||w||_{ℓ²(B_{3R/4})}. (On the lattice the
iteration stops at the lattice scale with sup ≤ ℓ^p; no limit p → ∞ is needed.)
(7) ||w||_{ℓ²(B_{3R/4})} ≤ ||u||_{ℓ²(B_R)} + k(6|B_R|)^{1/2} = ε + √6kR², so sup_{B_{R/2}}|u| ≤ C_T(R⁻²ε + k). ∎
*Remarks.* (i) No sup-smallness beyond |u| ≤ ε (automatic) is used; the Bianchi defect, the true/straight transport
difference and K are potentials small in the critical norm (S3-4 settled). (ii) The source enters in divergence form
through ⟨𝒮, D_1*(ψu)⟩, which is why ℓ^q with q > 4 suffices and why its weight is R^{1-4/q}.

**Corollary EPS-0a (REVIEW_SQ_S3's (EPS-0a), ℓ^q form): PROVEN as an implication [S4-G].** For every critical point of
E_𝒞(P) (top fixed, free boundary) with Σ_{box_0}|𝒫|² ≤ ε_*²/16, n^{3-4/q}(Σ_{box_0}|𝒮|^q)^{1/q} ≤ ε_*/16 and every q > 4:
  **sup_{box_0}|𝒫| ≤ C_T'[n⁻²(Σ_{box_0}|𝒫|²)^{1/2} + n^{1-4/q}(Σ_{box_0}|𝒮|^q)^{1/q}],** C_T' := 2^{2+4/q}·4·C_T.
*Proof.* NREFL gives a torus configuration (sides (4n, 4n, 2n, 2n)) with ||𝒫||_{ℓ²(𝕋_R)} = 4||𝒫||_{box_0} and ||𝒮^R||_{ℓ^q} =
16^{1/q}||𝒮||_{ℓ^q(box_0)}. Every box site is the centre of an embedded cube of radius n/2 (the torus sides are ≥ 2n). Apply
EPS-T with R = n/2. ∎ Since ||𝒮||_{ℓ^q(B_R)} ≤ (6|B_R|)^{1/q}sup|𝒮|, this implies REVIEW_SQ_S3's sup-source form
sup_{B_{R/2}}|𝒫| ≤ C[R⁻²||𝒫||_{ℓ²(B_R)} + R·sup_{B_R}|𝒮|] under the scale-invariant source smallness R³sup|𝒮| ≤ c_qε_*
(the analogue of its hypothesis R³sup|𝒮| ≤ ε_*^{1/2}).

### 15.2 STEP 3, route (β): the averaged source bound (EPS-0b-avg)

Throughout: a τ-small minimiser of E_𝒞(P) (§13.0's meaning, including every cone plaquette below the top < τ; M3-6), with
τ ≤ τ_0 := min{τ_*, τ_S} (RES-dec's and STOKES-NA's thresholds) and θ = ||1 - V_P||. RES-dec gives, for every level-i cone link
c (1 ≤ i ≤ k), **x_c ≤ X_i := C_rθq^{k-i}**, q = L⁻³ + C_qτ ≤ (L⁻² + L⁻³)/2, so qL² ≤ (1 + L⁻¹)/2 < 1. F_j(q) := |log U_j(q)|_op;
for j = 0 these are the level-0 plaquettes of box_0, and ||F_0||²_{ℓ²} ≤ (π²N/2)Σ_ps(U_0(p)) ≤ (π²N/2)κ_+(π²/8)θ², i.e.
||F_0||_{ℓ²} ≤ 2.47√(Nκ_+)θ (s(e^X) ≥ (2/(π²N))|X|²_op; Σ_ps ≤ E_𝒞 ≤ κ_+(π²/8)θ², RES-dec step (1)).

**Lemma TPL (template): PROVEN-HERE [S4-G] (not counted; from §2's explicit Q_2).** The level-(j-1) → level-j template of
STOKES-NA is Q_2 (§2: in q's plane, kernel ⊗ of L⁻¹T_L(s - LX) in the two in-plane directions and L⁻¹1{s ∈ [LX, LX + L)} in the
two transverse ones), and its m-fold composition is Q_2^{(L^m)} (§2; LINEAR_PACKAGE Lemma 2.4). Hence the composed
level-i → level-j template **T^{(j←i)}** (m = j - i) has: **row sums L^{2m}; every entry ≤ L^{-2m}; every column sum ≤ L^{-2m}**
(with equality away from the box faces).
*Proof.* In-plane: max_uT_{L^m}(u) = L^m, Σ_uT_{L^m}(u) = L^{2m}, and Σ_XT_n(s - nX) = n for every s (the two non-zero terms
at u = r and u = r + n, 0 ≤ r < n, are (r + 1) + (n - 1 - r)); with the prefactor L^{-m}: max 1, row sum L^m, column sum 1.
Transverse: max L^{-m}, row sum 1, column sum L^{-m}. Multiply over the four directions. ∎ (q5 T1: exact in integer
arithmetic for m = 1, 2, 3.)

**Lemma STOKES-avg (S3-2 with local errors): PROVEN-HERE [S4-G] (not counted; a re-reading of STOKES-NA's proof).** For
1 ≤ j ≤ k - 1 and every level-j cone plaquette q, under STOKES-NA's smallness:
  **F_j(q) ≤ Σ_pT^{(j←j-1)}(q; p)F_{j-1}(p) + E_j(q),  E_j(q) := 4.1x(q) + C_S''Σ_{p⊂R_q}F_{j-1}(p)²,**
x(q) the maximal residual on q's four links, p ⊂ R_q over all orientations, C_S'' := C_S'(1.011A_ax)², C_S' := L²C_p +
6.1C_e + 2C_p((p_L + 1)² + 4.2) (valid when C_S'x(q) ≤ 0.05).
*Proof.* STOKES-NA's proof, keeping the average: |Σ_pw_pda_{j-1}(p)|_op ≤ Σ_pw_p(F_{j-1}(p) + C_pm²), Σw_p = L²; the other error
terms are L²C_pm² + 4C_e(m² + 1.011mx) + C_p((p_L + 1)m + 2.03x)² ≤ C_S'(m² + x²) (2mx ≤ m² + x²); and m = max|a_{j-1}| over R_q ≤
1.011A_ax·max_{p⊂R_q}F_{j-1}(p), so m² ≤ (1.011A_ax)²Σ_{p⊂R_q}F_{j-1}(p)². ∎

**Iterated form.** Since all kernels are nonnegative: **F_j ≤ T^{(j←0)}F_0 + Σ_{i=1}^{j}T^{(j←i)}E_i** pointwise (T^{(j←j)} = 1).
Two norm facts from TPL: **(N1)** ||T^{(j←i)}v||_{ℓ²(j)} ≤ ||v||_{ℓ²(i)} (Cauchy-Schwarz: (Σ_pTv)² ≤ L^{2m}Σ_pTv², then column sums
≤ L^{-2m}); **(N2)** ||T^{(j←i)}v||_{ℓ¹(Ω)} ≤ L^{-2m}||v||_{ℓ¹(Ω')} and ||T^{(j←i)}v||_∞ ≤ L^{-2m}||v||_{ℓ¹}, hence ||T^{(j←i)}v||_{ℓ²(j)} ≤
L^{-2m}||v||_{ℓ¹(i)} (Ω' := Ω enlarged by the template support, ≤ L^j/2 beyond the corner blocks).

**Lemma LEV-E (level energies are bounded): PROVEN-HERE [S4-G].** Put e := ||F_0||_{ℓ²} + C_Xθ, C_X := 21C_r/(1 - qL²),
c_R := 486 (the number of level-i plaquettes q with a given level-(i-1) plaquette in R_q, crude). If 5C_S''c_Re ≤ 1 and
C_S'X_1 ≤ 0.05, then for every j ≤ k - 1: **𝓔_j := Σ_{level-j cone plaquettes}F_j² ≤ 4e².** S4-F3 does NOT occur.
*Proof.* Split E_i = E_i^x + E_i^F (the x-term and the F²-term). (a) By (N1), ||Σ_iT^{(j←i)}E_i^x||_{ℓ²} ≤ Σ_i||E_i^x||_{ℓ²} ≤
Σ_i4.1·(24L^{4(k-i)})^{1/2}X_i = 20.1C_rθΣ_i(L²q)^{k-i} ≤ C_Xθ (there are ≤ 24L^{4(k-i)} level-i cone plaquettes, and
L^{2(k-i)}q^{k-i} = (L²q)^{k-i}). (b) ||E_i^F||_{ℓ¹} ≤ C_S''c_R𝓔_{i-1}; (c) ||E_j^F||_{ℓ²} ≤ C_S''(max_q Σ_{R_q}F²)^{1/2}(Σ_qΣ_{R_q}F²)^{1/2} ≤
C_S''c_R^{1/2}𝓔_{j-1} (max ≤ sum). With (N1) for F_0, (N2) for E_i^F (i < j) and (c) for i = j:
  𝓔_j^{1/2} ≤ ||F_0||_{ℓ²} + C_Xθ + C_S''c_RΣ_{i<j}L^{-2(j-i)}𝓔_{i-1} + C_S''c_R^{1/2}𝓔_{j-1}.
Induction: if 𝓔_i ≤ 4e² for i < j (true for i = 0: 𝓔_0 = ||F_0||² ≤ e²), then 𝓔_j^{1/2} ≤ e + 4e²C_S''c_R(1/8 + 1) ≤ e + 5C_S''c_Re² ≤ 2e. ∎
*Why there is no compounding.* The main term is the DIRECT transport T^{(j←0)}F_0 (an ℓ²-contraction, (N1)), not a transport
of F_{j-1}; errors made at level i < j reach level j through ℓ¹ → ℓ² with gain L^{-2(j-i)} ((N2)), and the error made at level j
is quadratic. So the recursion is 𝓔_j^{1/2} ≤ e + O(e²), not 𝓔_j^{1/2} ≤ (1 + Cτ)𝓔_{j-1}^{1/2}.

**Lemma LOC-T (local residual transport): PROVEN-HERE [S4-G] (a localisation of §13.3).** For a level-0 link b let Q_m(b) be
the level-m block containing tail(b) and 𝔑_m(b) the union of the level-m blocks at level-m ℓ^∞ distance ≤ 2 from Q_m(b),
intersected with box_0 (𝔑_m(b) := box_0 for m > k). For -1 ≤ l ≤ k - 2 put
  **A_l(b) := max{x_c : c a level-(l+2) cone link in 𝔑_{l+3}(b)} + max{F_{l+1}(q) : q a level-(l+1) cone plaquette in 𝔑_{l+3}(b)}.**
Then, for every τ-small minimiser,
  **|𝒮(b)| ≤ C_0θn⁻³exp(C_qL³Σ_{l=-1}^{k-2}A_l(b)),  C_0 := 1.67Nκ_+κ̂^{1/2}.**
*Proof.* (i) *One step, local.* §13.3's computation at a level-(l+1) link b' (0 ≤ l ≤ k - 2) uses: the straight part, whose
weights sum to ≤ L⁻³ (so it is ≤ L⁻³max|j_{l+1}| over the level-(l+2) links c' having b' in a contour); the funnel part, ≤
8·max(x + σ + σ')·max|j_{l+1}| over the ≤ 8 links at the root c_Y of b''s block (CC-NA at Y is exact); and the remainder
|e_l(b')| ≤ 17.7√NA_d·(local f_{l+1})·max|j_{l+1}| over the same c'. All maxima are over level-(l+2) links whose endpoint blocks
are the level-(l+2) blocks containing or adjacent to those of b', and σ + σ' ≤ 6A_d·(the level-(l+1) plaquettes of those
blocks). So |j_l(b')| ≤ [L⁻³ + C_qa(b')]·max_{c'∈𝒩'(b')}|j_{l+1}(c')|, a(b') := local residual + local level-(l+1) curvature,
𝒩'(b') those links. The same at l = -1 for 𝒮 = -N·(the level-0 kernel gradient), with CC-NA at level-1 sites and M3-3's
uniqueness (τ-small). (ii) *Chains stay local.* Iterating from b (level 0) upward, the level-(l+1) link b_l reached at step l is
within level-0 distance Σ_{i≤l}2L^{i+1} ≤ 3L^{l+1} of b, and the objects entering a(b_l) lie within a further 2L^{l+2}; since
3L^{l+1} + 2L^{l+2} ≤ L^{l+3} for L ≥ 3, they lie in 𝔑_{l+3}(b): a(b_l) ≤ A_l(b). S4-F4 does NOT occur. (iii) There are k factors
(l = -1, …, k - 2), so |𝒮(b)| ≤ N·L^{-3k}Π_l(1 + C_qL³A_l(b))·max_{top}|j_{k-1}|, and max|j_{k-1}| ≤ κ_+N^{-1/2}·1.01·1.65√(Nκ̂)θ
(RES-dec steps (1)-(2)). Use 1 + t ≤ e^t. ∎

**Lemma CARL (Carleson bound): PROVEN-HERE [S4-G].** Put a_m := C_qL³A_{m-3} (a function constant on level-m blocks; for
m ≥ k it is constant on box_0). For every M ≤ k + 1 and every level-M block Q (Q := box_0 for M = k + 1):
  **avg_{x∈Q}Σ_{m≤M}a_m(x) ≤ β := C_qL³[C_1||F_0||_{ℓ²} + C_2θ + C_3e²],**
C_1 := (9/8)·5⁴·49√6·L⁴, C_2, C_3 depending on (N, L, κ_±) only (explicit below); in particular β ≤ C_βθ depth-uniformly.
*Proof.* Let l := m - 3 ≤ M - 3 and j := l + 1. (a) Residual part: Σ_l max x ≤ Σ_lX_{l+2} ≤ 1.1C_rθ pointwise. (b) Curvature part:
max ≤ sum and counting, avg_{x∈Q}max_{q⊂𝔑_{l+3}(x)}F_j(q) ≤ |Q|⁻¹·5⁴L^{4(l+3)}·Σ_{q⊂Q⁺}F_j(q), Q⁺ the 2-block (level-M)
enlargement of Q (𝔑_{l+3}(x) ⊂ Q⁺ since l + 3 ≤ M). By the iterated form and (N2):
Σ_{q⊂Q⁺}F_j(q) ≤ L^{-2j}||F_0||_{ℓ¹(Q⁺⁺)} + Σ_{i≤j}L^{-2(j-i)}||E_i||_{ℓ¹(Q⁺⁺)}, Q⁺⁺ ⊂ a cube of side 7L^M; ||E_i||_{ℓ¹(Q⁺⁺)} ≤
4.1·24·7⁴L^{4(M-i)}X_i + C_S''c_R·4e² (LEV-E). Sum over j ≤ M - 2 with the weight 5⁴L^{4(j+2)}/L^{4M}:
- F_0 term: 5⁴L⁸L^{-4M}Σ_{j≤M-2}L^{2j}||F_0||_{ℓ¹(Q⁺⁺)} ≤ (9/8)5⁴L⁴L^{-2M}||F_0||_{ℓ¹(Q⁺⁺)} ≤ (9/8)5⁴L⁴·(6·7⁴)^{1/2}||F_0||_{ℓ²}
  (Cauchy-Schwarz: ≤ 6·7⁴L^{4M} plaquettes in Q⁺⁺). **This is where the energy controls the multi-scale sum: the ℓ¹ averages
  of the curvature at the scales below Q sum geometrically to the ℓ² norm at the scale of Q.**
- X term: 5⁴L⁸·4.1·24·7⁴C_rθΣ_{i≤j≤M-2}L^{2(j-i)}q^{k-i} ≤ C θΣ_i(qL²)^{M-2-i}·(9/8) ≤ C_2'θ.
- e² term: 5⁴L⁸·4C_S''c_Re²Σ_{j≤M-2}L^{4j-4M}Σ_{i≤j}L^{-2(j-i)} ≤ C_3e².
Add (a). For M = k + 1 the same computation with |Q| = 4n⁴. ∎

**Lemma GARSIA (exponential moments of adapted sums): PROVEN-HERE [S4-G] (classical; Garsia's lemma, reproduced).** Let
F_{k+1} ⊂ F_k ⊂ … ⊂ F_0 be a finite filtration on a finite probability space (here: the uniform measure on the sites of box_0,
F_{k+1} trivial, F_m generated by the level-m blocks; "time" runs from coarse to fine), a_m ≥ 0 F_m-measurable, S_M := Σ_{m≤M}a_m, and E[S_M | F_M] ≤ β for every M.
Then **E[S_M^p | F_M] ≤ p!β^p** for p ≥ 1, and **E[e^{λS_{k+1}}] ≤ (1 - λβ)⁻¹** for 0 ≤ λβ < 1.
*Proof.* S_M^p = Σ_{m≤M}(S_m^p - S_{m-1}^p) ≤ pΣ_{m≤M}a_mS_m^{p-1} (x^p - y^p ≤ px^{p-1}(x - y), x ≥ y ≥ 0). Conditioning, with a_m
F_m-measurable and induction on p: E[S_M^p|F_M] ≤ pΣ_{m≤M}E[a_mE[S_m^{p-1}|F_m]|F_M] ≤ p(p - 1)!β^{p-1}E[S_M|F_M] ≤ p!β^p. Sum the
exponential series. ∎ (q5 G1: three process types, λβ ∈ {0.25, 0.5, 0.9}, all within the bound.)

**Proposition EPS-0b-avg: PROVEN as an implication [S4-G] (counted with LEV-E, LOC-T, CARL, GARSIA as one item).** Let q > 4.
For every τ-small minimiser (τ ≤ τ_0) with θ ≤ θ_G (θ_G := the largest θ with qβ ≤ ½ and LEV-E's conditions; depth-
independent):
  **avg_{level-0 links of box_0}|𝒮|^q ≤ 2(C_0θn⁻³)^q,**  i.e. (Σ_{box_0}|𝒮|^q)^{1/q} ≤ (32n⁴)^{1/q}C_0θn⁻³.
*Proof.* LOC-T: |𝒮(b)|^q ≤ (C_0θn⁻³)^qexp(qΣ_ma_m(tail b)). GARSIA with CARL's β and λ = q: E[e^{qΣa}] ≤ (1 - qβ)⁻¹ ≤ 2. Each
site carries 4 links and box_0 has 4n⁴ sites. ∎
*Reading.* The pointwise (EPS-0b) asks the product Π_l(1 + C_qL³A_l(b)) to be bounded at EVERY b; under τ-smallness alone it can
be n^{δ(τ)} (§13.6). Energy controls it only on average: the multi-scale sum Σ_lA_l is a Carleson (dyadic-BMO) sum with norm
≲ θ, so its exponential is integrable (John-Nirenberg in Garsia's form) but not bounded. EPS-T tolerates exactly this: its
source enters in ℓ^q, q > 4.

### 15.3 Theorem EPS-0 and the consumers
**Theorem EPS-0 ((EPS-0) of §13.5, as restated by S3-6): PROVEN as an implication [S4-G] (not counted separately: a
composition of EPS-T (via Corollary EPS-0a) and Proposition EPS-0b-avg; S3-3's rule).** Fix q := 8. Let τ_0 be as in §15.2 and
θ_0 := min{θ_G, θ_ε}, θ_ε the largest θ with 4·2.47N√κ_+θ ≤ ε_* and 16·32^{1/8}C_0θ ≤ ε_*. For every k, every level-k plaquette
P and every minimiser of E_𝒞(P) that is τ_0-small at levels ≥ 1, with θ = ||1 - V_P|| ≤ θ_0:
  **max_{level-0 p}||1 - U_0(p)|| ≤ A_0θn⁻²,  A_0 := c_NC_T'(2.47N√κ_+ + 32^{1/8}C_0),** depth-uniform.
*Proof.* (Σ|𝒫|²)^{1/2} ≤ √N||F_0||_{ℓ²} ≤ 2.47N√κ_+θ (|𝒫|_HS ≤ |log U|_HS ≤ √N|log U|_op) and, by EPS-0b-avg, n^{3-1/2}(Σ|𝒮|⁸)^{1/8} ≤ 32^{1/8}C_0θ: both hypotheses of
Corollary EPS-0a hold. Its conclusion: sup|𝒫| ≤ C_T'[n⁻²·2.47N√κ_+θ + n^{1/2}(32n⁴)^{1/8}C_0θn⁻³] = C_T'(2.47N√κ_+ +
32^{1/8}C_0)θn⁻². Finally ||1 - U_0(p)|| ≤ |log U_0(p)|_op ≤ c_N|𝒫(p)|. ∎
No bootstrap is used: the hypotheses are τ-smallness at levels ≥ 1 (as in RES-dec) and θ ≤ θ_0; the conclusion is the decay.
No uniqueness, no continuity in V, no a-priori decay. The large branch of §13.6 is thereby excluded for every τ_0-small
minimiser (it was a sup-closure artefact, S3-5).

**Corollaries (PROVEN as implications [S4-G], given the reviewed items they cite; uncounted).**
- **(REG-min)** holds, by Theorem RED-0 (§13.5) with τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'} (FORCE: a τ_R-small minimiser has
  θ < C'τ_R ≤ θ_0) and C_D := max{G, C_r}, G = 2(1.011A_0 + B_0) (STOKES-it): curvature decay at every level with θ_w = 2 and
  residual decay with θ_r > 2.
- Hence the session-1/2 CONDITIONAL items lose their hypothesis: **Corollary PRICE-iii** (branch (iii)'s price) and
  **Corollary DESC-ε** (both AE-red conclusions on every chain), and **(CLS-min)** by DESC (b) (§0.3), each with depth-
  independent constants (crude: the thresholds of §0.3 times those above).
- **(MIN-reg)_cone, sup part** (REVIEW_SQ_S2 S2-6) holds at rates θ_w = 2 (curvature) and θ_r > 2 (residuals) (RED-0
  Consequence (iii)); BFT's Hölder part and uniqueness are not supplied.
- **The pointwise (EPS-0b), a posteriori.** With EPS-0, STOKES-it gives F_j ≤ GθL^{-2(k-j)}, so A_l(b) ≤ X_{l+2} + GθL^{-2(k-l-1)} and
  Σ_lA_l(b) ≤ (1.1C_r + 1.2G)θ for every b; LOC-T then gives **n³sup|𝒮| ≤ C_0θexp(C_qL³(1.1C_r + 1.2G)θ)**, and RES-dec Remark (3)'s
  residual exponent exactly 3 holds. So REVIEW_SQ_S3's (EPS-0b) is TRUE, but it is proven after (EPS-0), not before.

### 15.4 STEP 3, route (α): the lattice Uhlenbeck gauge, and the convexity verdict
**Lemma GS (Gaffney-Sobolev on the free-boundary box): PROVEN-HERE [S4-G].** Every su(N)-valued 1-form w on box_0 with
Neumann d*w = 0 (links leaving box_0 omitted) obeys **||w||_{ℓ⁴(box_0)} ≤ C_GS||dw||_{ℓ²(box_0)}, C_GS := 2C_SP**, depth-uniform.
*Proof.* BFT_B Lemma REF (§19.11; PROVEN there, N1G now proven, §22.2): the reflected form w^R on 𝕋_R is co-closed, each
component w^R_μ is odd under ϱ_μ (mean zero), and dw^R = (dw)^R with crossing plaquettes 0, so ||dw^R||² = 16||dw||². On the torus,
Σ|∇w^R|² = ||dw^R||² + ||d*w^R||² = ||dw^R||² (componentwise -Δ = d*d + dd*, summation by parts). SOB (b) on the torus for each
mean-zero component: ||w^R||_{ℓ⁴} ≤ C_SP||∇w^R||_{ℓ²} = 4C_SP||dw||. And ||w||⁴_{ℓ⁴(box_0)} = ||w^R||⁴_{ℓ⁴}/16. ∎

**Theorem LU-ap (lattice Uhlenbeck a-priori estimate): PROVEN-HERE [S4-G].** Let w = log U_0^g on box_0 with Neumann d*w = 0
and ||w||_{ℓ⁴} ≤ η_U := 1/(2C_GSC_3√24) (≤ ½), C_3 the BCH constant of BFT_B 19.12 (|dw(p) - log U^g(∂p)| ≤ C_3max_{b∈∂p}|w(b)|²). Then
**||w||_{ℓ⁴} ≤ 2C_GS||log U_0(∂·)||_{ℓ²}.**
*Proof.* |log U^g(∂p)| = |log U(∂p)| (conjugation). ||dw||_{ℓ²} ≤ ||log U(∂·)||_{ℓ²} + C_3(Σ_p(Σ_{b∈∂p}|w(b)|²)²)^{1/2} ≤ ||log U(∂·)|| +
C_3√24||w||²_{ℓ⁴} (each link in ≤ 6 plaquettes). GS and ||w||_{ℓ⁴} ≤ η_U give ||w||_{ℓ⁴} ≤ C_GS||log U(∂·)|| + ½||w||_{ℓ⁴}. ∎

**Lemma GAP (small-energy free-boundary Wilson critical points are flat): PROVEN as an implication [S4-G] (of EPS-T, NREFL
and complete-axial BCH).** There is ε_G = ε_G(N) > 0 such that every critical point U of Σ_{p⊂box_0}s(U(p)) on the links of
box_0 (free boundary) with Σ_ps(U(p)) ≤ ε_G² has U(p) = 1 for every p.
*Proof.* 𝒮 = 0. NREFL + EPS-T (R = n/2, source 0): sup|𝒫| ≤ C n⁻²√E, E := Σ_ps. In the complete axial gauge of box_0 (sides
≤ 2n) every link is the holonomy of a ladder of ≤ 6n plaquettes, so |a(b)| ≤ 7n·c_Nsup|𝒫| ≤ C'√E/n. Write 𝒫(p) = da(p) + B'(p),
|B'| ≤ C(√E/n)² (BCH). Then Σ_p|𝒫|² = ⟨d*𝒫, a⟩ + ⟨𝒫, B'⟩ (the abelian d* is the exact adjoint on the box complex, free boundary)
and |d*𝒫| = |d*𝒫 - (D_1^tr)*𝒫| ≤ C max|a|·Σ_{p∋b}|𝒫(p)| ≤ C''E/n³. With ≤ 4·4n⁴ links and ≤ 6·4n⁴ plaquettes:
Σ_p|𝒫|² ≤ C'''E^{3/2}. Since Σ_p|𝒫|² ≥ (N/2)E for small plaquettes, (N/2)E ≤ C'''E^{3/2}, so E = 0 or E^{1/2} ≥ N/(2C'''); take
ε_G < N/(2C''') (and below EPS-T's ε_*). ∎

**Theorem LU-ex (lattice Uhlenbeck gauge in the small-energy regime): PROVEN as an implication [S4-G] (of GS, LU-ap, GAP, and
the implicit function theorem; counted with GS, LU-ap, GAP as one item).** There is ε_U = ε_U(N) > 0 such that every SU(N)
configuration U_0 on the links of box_0 with Σ_ps(U_0(p)) ≤ ε_U² admits a gauge g (g = 1 at a fixed site) with
**Neumann d*log U_0^g = 0 and ||log U_0^g||_{ℓ⁴} ≤ 2C_GS||log U_0(∂·)||_{ℓ²} ≤ C_U(Σ_ps)^{1/2}**, C_U := 2πC_GS(N/2)^{1/2},
depth-uniformly. **[post-proof
correction (3)]**: no Łojasiewicz input is needed.
*Proof.* Let U_t (t ≥ 0) be the gradient flow of E_W := Σ_ps on the compact manifold SU(N)^{links} (global, E_W(U_t) ≤ E_W(U_0)).
Since ∫_0^∞|∇E_W(U_t)|²dt ≤ E_W(U_0), there are t_n → ∞ with |∇E_W(U_{t_n})| → 0; by compactness a subsequence converges to a
critical point with E_W ≤ ε_U² ≤ ε_G², which is flat (GAP), i.e. a pure gauge h. Near the orbit of 1 the Neumann-Coulomb
equation is solved by the implicit function theorem (its g-derivative at (1, 1) on {ξ(c) = 0} is the Neumann Laplacian,
invertible), so for some t_* the configuration U_{t_*} has a Neumann-Coulomb gauge with ||w||_{ℓ⁴} < η_1 := η_U/2. Let 𝒯 := {t ∈
[0, t_*] : U_t has a Neumann-Coulomb gauge with ||w||_{ℓ⁴} ≤ η_1}. Closed: compactness of the gauge group, continuity of the
equation and of ||w|| (|w| ≤ η_1 pointwise keeps log smooth). Open: at t_0 ∈ 𝒯, LU-ap gives ||w|| ≤ C_Uε_U < η_1 for ε_U
small; the Hessian of Φ_t(g) := Σ_b|log U_t^g(b)|² on {ξ(c) = 0} is H(ξ) = H(ξ - ξ̄) ≥ (2 - C(η_1 + η_1²))||dξ||² ≥ ||dξ||² by the
expansion of BFT_B 19.9 with the error terms bounded in the critical norms (Σ|w||ξ'||dξ| ≤ ||w||_{ℓ⁴}||ξ'||_{ℓ⁴}||dξ||, Σ|w|²|ξ'|² ≤
||w||²_{ℓ⁴}||ξ'||²_{ℓ⁴}, ||ξ'||_{ℓ⁴} ≤ C_SP||dξ|| by SOB (b) for ξ' := ξ - ξ̄), so it is nondegenerate and the IFT continues the gauge
to nearby t with ||w|| < η_1. 𝒯 ∋ t_* is open and closed in [0, t_*], so 0 ∈ 𝒯; LU-ap then gives the bound. ∎
**Why this is the lattice Uhlenbeck theorem.** It is the critical-norm (ℓ⁴ ≍ L⁴, d = 4) Coulomb gauge under small ℓ²
curvature, uniform in the box size, with no sup-decay hypothesis (contrast NF-ex: max n|A| ≤ ε_0). Uhlenbeck's dilation path
is replaced by the Wilson flow (energy non-increasing), and the borderline embedding is harmless on the lattice (sup ≤ ℓ⁴).

**Route (α) verdict [ARGUED; not needed for (EPS-0)].** (i) The level-0 Wilson part is strictly convex on the Neumann-
Coulomb slice ball {||a||_{ℓ⁴} ≤ Cθ}: its Hessian is ||dξ||² + O((||a||_{ℓ⁴} + ||F||_{ℓ²})||ξ||²_{ℓ⁴}) ≥ (1 - Cθ)||dξ||² on Neumann-co-closed
ξ by GS (REVIEW_SQ_S3's Dirichlet-form comparison, now with LU-ex supplying the gauge). (ii) **S4-F5, corner half, does NOT
occur:** the near-gauge directions that move the fixed top (point charges q at the corner roots) have Hessian ≍ κ|q|²G_0
(G_0 = the 4D lattice Green function at 0, an absolute constant), comparable to their critical norm, not n⁻⁴|q|². (iii) **The
remaining step (CVX-K) is OPEN:** the kernel terms' second variation at a τ-small chain differs from the flat one by terms
∝ (x_c + σ_c) times quadratic forms in the variations of all levels; uniqueness needs these to be summable against 𝓑 in the
critical norms. With CARL's accounting they are plausibly summable (Carleson with constant ≲ θ), but the second-variation
bookkeeping is not written. Route (α) would add minimiser UNIQUENESS (hence continuity in V), which (EPS-0) does not need.

### 15.5 Checks q4b, q5 (criteria first: checks/q4b_criteria.md 11:17:10 UTC, checks/q5_criteria.md 11:25:21 UTC; scripts after; one lock hold 11:29:41-11:29:50 UTC; records checks/q4b_*, q5_*)
- **q4b (POST HOC to q4; labelled).** **OVERALL: FAIL as pre-registered (P0)**: max stationarity residual 4.3·10⁻¹⁰ > 1e-13.
  K1 5.9·10⁻¹⁶, K2 3.8·10⁻¹⁰, **K3 2.07·10⁻¹⁰ (PASS; q4's 1.89·10⁻⁸ came from the BFGS W_0)**, K4 2.6·10⁻¹¹, K5 3.0·10⁻¹¹, K6 1.7·10⁻⁵ PASS;
  max ||W_Newton - W_BFGS||_op = 4.1·10⁻⁸ (SU(3)). 3.0 s, 57 MB peak footprint. *Post-hoc diagnostic (scratchpad s4diag/diag2,
  lock 11:31:13):* the P0 residual is carried by the **SU(2)** branch: the determinant-normalised polar factor is the SU(2)
  maximiser only on the quaternion line; at M + 10⁻⁵δ with complex δ (K2's and K3's finite differences) its residual is
  2.6·10⁻¹⁰, while the Newton SU(3) branch has ≤ 1.2·10⁻¹⁷ (diag: Newton reaches 5·10⁻¹⁸ in one step from the polar factor). So
  REVIEW_SQ_S3's "for SU(2), q4's polar factor is exact (9·10⁻¹⁷)" holds at the unperturbed M only; its effect on K2/K3 is
  ≤ 4·10⁻¹⁰. Reading: S3-8's diagnosis is reproduced (K3 at 2·10⁻¹⁰ with an accurate SU(3) W_0); a future identity check should
  also solve the SU(2) maximiser exactly off the quaternion line (project M onto the real-quaternion span first). q4's FAIL
  and q4b's FAIL both stand as recorded.
- **q5.** **OVERALL: FAIL as pre-registered (T2)**; T1, W1, W2, W3, B1, R1, G1 PASS. 5.6 s, 211 MB peak footprint.
  - T1: the composed in-plane kernel equals L^{-m}T_{L^m} exactly (m = 1, 2, 3); column sums 1 (in-plane) and L^{-m} (transverse)
    exactly; max entries 1 and L^{-m}. W1: K = 0 exactly at U = 1. W2: max|K| = 3.6·10⁻¹⁵ on a pure gauge. W3: ||K||_op/η_P = 3.53,
    3.48, 3.88 (η = 0.04, 0.02, 0.01), gauge change 1.1·10⁻¹⁴. B1: R_B = 3.57, 3.42, 3.06, gauge change 1.9·10⁻¹³. R1: crossing
    plaquettes 2.2·10⁻¹⁶, box-link gradients 2.8·10⁻¹⁷, norms 5.6·10⁻¹⁷, energy ratio exact. G1: all nine cases within (1 - λβ)⁻¹
    (largest ratio 1.30/1.33 at λβ = 0.25, tower).
  - **T2 FAIL (0.80):** the script's Q_str used straight lines starting at the block FACE with L³ transverse offsets (a literal
    reading of BFT_B §15.0's "s⁻³Σ_transverseΣ_{i<s}"). SQ §2's Q_2 is the template of the straight average over ALL L⁴ starting
    points of the block (its Q_2F(P') := L⁻⁴Σ_{y∈B(X)}Σ_{p∈sq_y}F(p) is exactly d of that average, since ∂sq_y's four sides are the
    four averaged lines). *Post-hoc T2b (scratchpad s4diag/diag.py, lock 11:30:42):* with SQ §2's average, |dQ_stra - Q_2da| =
    2.8·10⁻¹⁶. TPL uses only §2's Q_2 (T1, exact); the FAIL is a script definition error. The face-start operator is NOT the one
    STOKES-NA uses; whether BFT_B's Q_str means the face-start lines is BFT_B's to state (flagged for lane B; not edited).
- Numeric lock: three holds (11:29:41-11:29:50 q4b + q5; 11:30:42 and 11:31:13 post-hoc diagnostics), each one mkdir and one
  rmdir; nice 10, BLAS threads 1, python3 without -I, no `timeout`; no process left running.

## 16. Session-4 outcomes against §T4 (ADDED AFTER the derivations; pointers only) and tally
- **Step 1: DONE.** S3-1 (§11.6), S3-2 (§13.4, recommended), S3-3 (§13.5, §14), S3-4 (§13.6), S3-5 (§13.6, §14), S3-6 (§13.5, §13.6,
  §13.8), S3-7 + M3-8 (§13.7), S3-8 (§14; SQ_LOG session 3), M3-1 (§13.0), M3-2 (§11.5), M3-3 (§13.1), M3-4 (§13.2), M3-5 (§13.3),
  M3-6 (§13.3), M3-7 (§13.4); all tagged [RSQ3-fix]. q4b run (post hoc): K3 reproduced at 2·10⁻¹⁰; q4b itself FAILs its own P0
  (SU(2) polar factor off the quaternion line), recorded.
- **STEP 2 ((EPS-0a)): PROVEN** as Theorem EPS-T (lattice ε-regularity with an ℓ^q source, q > 4), with Lemmas NREFL, BIA, WB,
  SOB, and Corollary EPS-0a on box_0. Post-proof correction (6): a scale-invariant source smallness hypothesis is needed.
- **STEP 3: (EPS-0) PROVEN as an implication (Theorem EPS-0)** via route (β): EPS-T + Proposition EPS-0b-avg (LEV-E, LOC-T, CARL,
  GARSIA, TPL, STOKES-avg). The instructed route (α) delivered the lattice Uhlenbeck gauge (GS, LU-ap, GAP, LU-ex: PROVEN) and
  the level-0 slice convexity [ARGUED], but its multi-level convexity step (CVX-K) is OPEN; (EPS-0) does not need it. The
  pointwise (EPS-0b) holds a posteriori (§15.3).
- **Consumers:** (REG-min) by RED-0; PRICE-iii, DESC-ε, (CLS-min) by §0.3; (MIN-reg)_cone sup part. All as implications of
  reviewed items plus this session's (unreviewed) items.
- **Failure modes.** S4-F1 does not occur (WB). S4-F2 does not occur (TPL: column sums exactly L^{-2m}). S4-F3 does not occur
  (LEV-E: no compounding). S4-F4 does not occur (LOC-T: chains stay in 𝔑_{l+3}). S4-F5: corner half does not occur; kernel half
  open as (CVX-K).
- **Tally, session 4 (this file; all unreviewed).** PROVEN-HERE, counted (3): Theorem EPS-T (with NREFL, BIA, WB, SOB);
  Proposition EPS-0b-avg (with LEV-E, LOC-T, CARL, GARSIA; TPL and STOKES-avg not counted); Theorem LU-ex (with GS, LU-ap, GAP).
  PROVEN, uncounted: Theorem EPS-0 (composition), Corollary EPS-0a, the §15.3 corollaries. ARGUED: route (α)'s level-0
  convexity and the corner computation. OPEN: (CVX-K) (off the critical path), non-abelian (SQ) (off-path).
- **File tally after session 4 (provisional, pending review): PROVEN-HERE counted 14 (11 + 3) / CONDITIONAL 1 (linear MS-Sob ⇐
  §4.4 counts; PRICE-iii and DESC-ε have their hypothesis (REG-min) discharged by §15.3) / OPEN 1 (non-abelian (SQ); (CVX-K) is
  not a target of the file's chain).** If review finds a gap in EPS-T or CARL, (REG-min) ⟺ (EPS-0) returns to OPEN and the
  tally to 14 / 3 / 2.
- **Hypotheses consumed (session 4).** RES-dec, CC-NA, RT-NA (§13, CONFIRMED by REVIEW_SQ_S3), STOKES-NA's proof, HIST MSG step
  (1), §2's Q_2 and Q_2^m (LINEAR_PACKAGE Lemma 2.4), BFT_B Lemma REF (§19.11) and N1G (§22.2), BFT_B 19.8-19.9's expansion of
  Φ, FORCE, RED-0, DESC (b). Literature: none load-bearing (Gagliardo-Nirenberg/Loomis-Whitney, Moser's iteration and Garsia's
  lemma are reproduced at the level written; the Hodge-Laplacian identity of the cubical complex is standard and checked in q5
  W1).
- **For the hostile review (priorities).** (1) EPS-T step (3)-(6): the neighbour-maximum localisation, the critical absorption
  in Stage 1, the finite lattice Moser iteration (radii ≥ 4 apart, sup ≤ ℓ^p). (2) LOC-T (i)-(ii): that every maximum in §13.3's
  per-level factor is local and that chains stay in 𝔑_{l+3}(b). (3) CARL's three sums and LEV-E's induction (the claimed absence
  of compounding). (4) GAP's use of EPS-T with zero source and LU-ex's open/closed argument.
- **Not done / not claimed.** No edit outside SQ.md, SQ_LOG.md, checks/q*. No commits, PRs, pushes, CL or axiom edits.
