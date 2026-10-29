Reviewer model: claude-opus-5-5

# ALIGN55 — (ALIGN-ℓ): a level-local alignment with regularity across levels, for the background transfer (R2) on 𝒞_glob

## PRE-STATED (written 2026-10-29T01:33:54Z, before any derivation in this file; only BGT55.md and REVIEW_BRIEF_55.md read so far)

Role: worker (Opus 5.5), scope given by the lead. Write-set: this file and `checks/al55_*` only. No git.
The Balaban paper directory /Users/jonBridger/Documents/balaban-cmp/ was EMPTY when checked (2026-10-29T01:33Z); CMP 99:75 is not
available to me locally. Anything I say about it below is from the lane's own extracts (BALABAN_EXTRACT.md), labelled as such.

### Targets
- T1. State (ALIGN-ℓ) precisely: every quantifier (k, T, background, ε), every norm, and exactly which inequality each of Theorem GA's
  inputs (A1) [t_+, t_*, invertibility] and (A2) [δ_Υ] consumes from it, in the transport-weighted pair (|||·|||_♯ → N).
- T2. Construct a candidate alignment: starting from the per-level slice functional Γ_PL (GSHARP55 Lemma PL-adm), and/or an
  axial-in-blocks construction adapted to the soft scheme; explain how it avoids (or fails) the two recorded axial failures
  (global axial: factor T, Dirac string; within-cell axial: sup budget fails by L^k — NLOC.md).
- T3. Prove regularity across levels uniformly in k and T in the transport-weighted norm — or isolate the exact obstruction,
  as a precise statement with a witness or a power count, and say which.
- T4. Assemble: Theorem GA + (ALIGN-ℓ) ⇒ (R2) on 𝒞_glob, as an implication, every input named with its status.

### What would count as a refutation of my own construction (stated in advance)
- R-a. The candidate Λ_W fails to be a left inverse (Λ_WΞ_1 ≠ −1 on Λ_0), or Υ_W fails exact alignment Υ_WΞ_1 = Ξ_ZA —
  tested in exact rational arithmetic on a small multi-level model.
- R-b. A level-l unit datum (charge, or level-l link field) whose image under the candidate's completion map (Λ_W^T on sources,
  or Λ_W on fields) has a coarse size that grows with k (e.g. ≍ L^{3l} spikes, the S_E failure) or with T (Dirac string).
- R-c. An explicit chain x with |||(Ξ_z − Ξ_1)Λ_W x|||_♯ ≥ c·η·f(k,T)·|||x|||_♯ with f unbounded — i.e. the cross-level regularity
  fails in the transport-weighted norm.
- R-d. Any step where a level-l gauge value depends on data at level l′ ≠ l in a way not dominated by a geometric factor in |l − l′|
  (in the transport weight), when level-locality is claimed.
- R-e. Any constant that depends on k, T or volume where uniformity is claimed.
- R-f. Silent use of S_E's completion (BGT55 §6.4 refuted it as an alignment at levels ≥ 1 by power count) or of a refuted input
  (relative-Hessian series, (GAP-Z) as input, TRANSP slot transport).

### Gate discipline
Any numeric check: `checks/al55_<id>_criteria.md` with pre-registered PASS/FAIL written before the script; exact rational
arithmetic only (python fractions), no floats for verdicts.

---

## RESUMED 2026-10-29T02:47:08Z

Resumed by claude-opus-5-5 (same model ID as the first line; no extra model line needed). The draft above stops after the PRE-STATED
block: it contains no derivation, so there is nothing of it to build on or to put in errata. The PRE-STATED targets T1-T4 and
refutation tests R-a..R-f stand unchanged and are the targets of this resumed run.

**Read before anything below (in this order).** CODEX_REVIEW_BGT.md: §6 in full first (6.1-6.4), then "Exactly what may be banked"
(items 1-7), then §1-§5 and §7-§10 in full (file complete on disk: it ends with banking item 7; 396 lines). BGT55.md in full (623 lines).
GSHARP55.md §5.4-§5.6. /Users/jonBridger/Documents/balaban-cmp/ checked again at 02:46Z: still EMPTY — CMP 99:75 is not available to me;
the open-corpus analogue Dimock arXiv:1410.2798 (Covariant Axial Gauge) is used instead, as data.

**Constraints inherited from CODEX_REVIEW_BGT (I build on none of the refuted items):**
- §6.3: literal (ALIGN-ℓ)(β) ("level-l values of Λ_W x depend only on x_l") is IMPOSSIBLE (nested-root contradiction), and Λ_PL does not
  satisfy it. Anything below uses a **hierarchical** dependence (level-l values may depend on x_l, x_{l+1}, …, x_{k−1}), with its coefficients
  and bounds proved, not asserted "by construction".
- §6.2: the "exact BCH factorisation" ρ_c = Ψ̃_c·r^full_c is REFUTED (sign at first order; W_0 dropped). I do not use it. Where the soft
  linearisation enters I use only Dρ(0)u = Q_l u_l − u_{l+1} = r_l(u) at the trivial chain (Codex §6.2) and the true covariance
  Dρ(z)Ξ′_zλ = −[λ(c′), ρ(z)] with the positive-d generator Ξ′_z = J(z)Ξ_Z (Codex §4, sign corrected).
- §6.1: the S1-S3 power conversions are upper bounds conditional on own-unit estimates; "the transfer must be run in |||·|||_♯" is NOT a
  necessity theorem. I use |||·|||_♯ because it is the pair in which RW♯ (banked, item 5) is available, not because it is forced.
- §6.4 / §2: the S_E obstruction is NOT-VERIFIED (neither proved nor refuted), and BGT55's level-0 formula for Λ_E^T is REFUTED (missing
  pinned-root term; sign). I do not claim S_E fails; I also do not use it as the alignment.
- §6.4: GA-slice's defect identity holds **on W only**; turning a bound on W into (A2) needs a representative bound [·]-to-W, which I must
  state as a separate item.

## 1. Symbols pinned (systemic defect 1), and the Dimock reading

**Symbols (this file only).** d = 4, odd L ≥ 3, κ_j ∈ [κ_−, κ_+], 0 < α < θ < 1 (θ = the class exponent of CC-INV/RT-cc, never θ_w).
Levels 0..k; ρ_l := L^{−(k−l)} (one level-l step in coarse units); **q := k − 1 − l** (depth). Level-l sites are the sublattice of
level-0 sites that are roots (block centres, nested) — so ev^{(l)} is restriction to that sublattice and level-l ⊂ level-1 for l ≥ 1.
- X: chains x = (x_0..x_{k−1}), x_k = 0. Λ_0: level-0 su(N)-functions vanishing at the level-k roots. Ξ_1λ := (d ev^{(l)}λ)_{l<k};
  Ξ_Zλ := (d_{Z_l} ev^{(l)}λ)_{l<k}, (d_Zλ)(b) := Ad_{Z(b)}λ(head b) − λ(tail b) (BGT55 §1 / KER_Z convention).
- r_l(x) := Q_lx_l − x_{l+1} (flat; Q_l the linearised S4′ root map, Q_l∘d = d∘ev); r^Z_l := the linearisation at Z (BFT_B §12.0).
- **|||x|||_{1,♯}** := ‖x‖_{𝔐^∇} + max_{0≤i≤k−2}L^{(1+θ)(k−1−i)}‖r^c_i(x)‖_∞ + N_res(x) (BGT55 §6.2, Codex-confirmed RW♯ pair);
  **[x]_{1,♯}** := inf_{λ∈Λ_0}|||x + Ξ_1λ|||_{1,♯}. |||·|||_{Z,♯}, [·]_{Z,♯}: the covariant versions (transported differences, r^Z).
  The residual terms and N_res are Ξ_1-invariant (r_l(Ξ_1λ) = 0 for all l < k), so [x]_{1,♯} = ‖[x]‖_{𝔐^∇} + residual terms.
- **N_1(y)** for a general (not necessarily cc) source y: inf over flat slot representations y = Σ_l[d^TG_l + j_l + r_l^Ts_l] of
  ‖G^c_0‖_∞ + [G^c_0]_α + ‖j^c_0‖_∞ + ‖j‖_Pc + ‖G‖_Y + ‖s‖_R (COFUN_CC §1, located "**N(S)** :="), with π_l(j) := L^{3(k−l)}sup_own|j|,
  ‖j‖_Pc := max_{1≤l≤k−1}L^{θ(k−l)}π_l(j_l), ‖s‖_R := max_lL^{θ(k−l)}L^{k−1−l}‖s^c_l‖_∞, s^c_l = L^{k−1−l}s_l. **N_Z**: the same infimum over
  covariant representations y = Σ_l[d_{Z}^TG_l + j_l + (r^Z_l)^Ts_l]; N_ℛ(y) denotes the N-expression of one representation ℛ.
- **Twisted charge** of a source: τ_Z(y) := (Ξ_Z − Ξ_1)^Ty ∈ Λ_0^*. For y ∈ cc_Z: Ξ_1^Ty = −τ_Z(y). For every w: Ξ_1^TH_Zw = −τ_Z(H_Zw).
- A **left inverse** is a linear Λ_W : X → Λ_0 with Λ_WΞ_1 = −1; W := Ker Λ_W; **Π_W := 1 + Ξ_1Λ_W** (projection onto W along Ran Ξ_1;
  Π_WΞ_1 = 0, so Π_Wx depends only on the class of x); **Υ_W := 1 − (Ξ_Z − Ξ_1)Λ_W** (GA-slice; Codex-confirmed: Υ_WΞ_1 = Ξ_Z,
  Υ_W = 1 on W, Υ_W^TS = Π_W^TS for S ∈ cc_Z, E_{Υ_W}u = Π_W^T(H_Z − H_1)u for u ∈ W).
- Collisions avoided: my alignment map is Υ (never T, the torus side); C_♯ is RW♯'s constant only; η := C_0ε the background size in
  𝔐^∇ (BGT55 §6.1); S_0 below is a scalar subdivision operator (never the S_E slice, never the level-l chain coefficient S_l of COFUN_CC).

**Dimock arXiv:1410.2798 (Covariant Axial Gauge), read as data (grep + sed ranges; §2.2, §3.1-§3.6).** Three facts bear on the task:
(a) The multiscale axial gauge there is imposed on the **averaged** fields: δ_{X_k}(A) = Π_{j<k}δ(τQ^jA) (§3.1, eq. (29)), τ the
permutation-averaged axial path functional inside each block (eq. (27)). Its role is to make the gauge-fixed integral and the
Faddeev–Popov change of variables well defined (Props. 2-4).
(b) **Regularity is not obtained in the axial gauge.** §3.5 passes to a Feynman/Landau form (Prop. 5) and records that the axial
minimiser H^x_k differs from the Landau minimiser H_k by a gauge term ("H^x_k = H_k + dD_k", item 2 after (84)), and that the
regularity and decay statements (kernels of H_k, ∂H_k, δ_α∂H_k) are for H_k. In words: gauge-invariant quantities are computed in
the axial gauge but **estimated in the Landau gauge**.
(c) The lower bound of §3.6 (Prop. 6) uses the axial condition only inside one block (Stokes over the averaged surfaces, eq. (91)),
i.e. it is a per-block statement with L-dependent constants.
**Reading for this task:** the hard-scheme axial-in-blocks gauge is a level-local *gauge fixing*, not a regular *representative*;
the scheme never needs the axial representative to be C^{1,α} across block seams. That is exactly the split this file finds
necessary below (§3: the source half forces hierarchical dependence; §4: the field half forces a smooth, Coulomb-consistent
interpolation across levels). CMP 99:75 itself was not available (directory empty), so nothing below attributes a statement to it.

## 2. T1 — (ALIGN-ℓ) restated in a form that survives CODEX_REVIEW_BGT §6, and the exact reduction to it

**Statement (ALIGN-ℓ♯).** There are, for every k ≥ 1 and T ≥ T_0, a left inverse Λ_W given by one rule, and constants C_Π, C_P, C_tw
depending only on (N, L, κ_±, α, θ), such that:
- **(H) hierarchical dependence:** ev^{(l)}Λ_Wx depends only on (x_l, …, x_{k−1}), for every l (Codex §6.3's repair of the refuted
  literal (β); it is not used as a hypothesis below — §3 shows a quantitative form of it is *necessary* for (P2-tw)).
- **(P1) representative bound:** |||Π_Wx|||_{1,♯} ≤ C_Π·[x]_{1,♯} for every x ∈ X.
- **(P2-tw) twisted-charge completion:** for every background in the class with ‖z‖_{𝔐^∇} ≤ η ≤ η_0, every source y and every covariant
  representation ℛ of y: N_1(Λ_W^Tτ_Z(y)) ≤ C_tw·η·N_ℛ(y).
together with five **slice-independent background estimates** (they involve Z but not W):
- **(NC)** |||w|||_{Z,♯} ≤ (1 + C_NCη)|||w|||_{1,♯} (all w);   **(NS)** N_1(y) ≤ (1 + C_NSη)N_ℛ(y) (all y, all covariant ℛ);
- **(HD)** N_1((H_Z − H_1)w) ≤ C_HDη|||w|||_{1,♯};   **(FW)** N_ℛ(H_Zw) ≤ C_FW|||w|||_{Z,♯} for one covariant representation ℛ of H_Zw;
- **(AC)** |||(Ξ_Z − Ξ_1)μ|||_{1,♯} ≤ C_ACη‖μ‖_Λ, where ‖μ‖_Λ := |||Ξ_1μ|||_{1,♯} (a norm on Λ_0, Ξ_1 injective).

> **Lemma RED (exact reduction). PROVEN-HERE.** Assume (P1), (P2-tw), (NC), (NS), (HD), (FW), (AC) and (C_Π + 1)C_ACη < 1. Then Υ_W
> is invertible, Υ_WΞ_1 = Ξ_Z (A = 1), and Theorem GA's hypotheses hold in the pair (|||·|||_♯ → N) with
>   **t_+ ≤ C_Π(1 + C_NCη),  t_* ≤ 1 + (C_NS + C_tw)η,  δ_Υ ≤ C_Π[C_HD + C_twC_FW(1 + C_NCη)]·η.**
> Consequently, with (B_1♯) = Corollary RW♯ (CODEX_REVIEW_BGT banked item 5: [x]_{1,♯} ≤ C_♯N(S), Ker H_1 = Ran Ξ_1), Theorem GA gives
> (N1-nd) at Z and [x]_{Z,♯} ≤ t_+t_*C_♯(1 − C_♯δ_Υ)^{−1}N_Z(S) for every S ∈ cc_Z, as soon as C_♯δ_Υ < 1.

*Proof.* (1) *Alignment and invertibility.* Υ_WΞ_1 = Ξ_1 − (Ξ_Z − Ξ_1)Λ_WΞ_1 = Ξ_Z. By CODEX_REVIEW_BGT §2, Υ_W is invertible iff Λ_WΞ_Z is
invertible on Λ_0. Λ_WΞ_Z = −1 + Λ_W(Ξ_Z − Ξ_1), and for μ ∈ Λ_0, with u := (Ξ_Z − Ξ_1)μ: ‖Λ_Wu‖_Λ = |||Ξ_1Λ_Wu|||_{1,♯} = |||Π_Wu − u|||_{1,♯}
≤ (C_Π + 1)|||u|||_{1,♯} (P1 and [u] ≤ |||u|||) ≤ (C_Π + 1)C_ACη‖μ‖_Λ (AC). So ‖Λ_W(Ξ_Z − Ξ_1)‖_{Λ→Λ} < 1 and Λ_WΞ_Z is invertible (Neumann).
(2) *t_+.* For every x, Υ_Wx + Ξ_ZΛ_Wx = x + Ξ_1Λ_Wx = Π_Wx, so [Υ_Wx]_{Z,♯} ≤ |||Π_Wx|||_{Z,♯} ≤ (1 + C_NCη)|||Π_Wx|||_{1,♯} ≤ (1 + C_NCη)C_Π[x]_{1,♯}.
(3) *t_*.* For S ∈ cc_Z: Υ_W^TS = Π_W^TS = S + Λ_W^TΞ_1^TS = S − Λ_W^Tτ_Z(S). For any covariant representation ℛ of S,
N_1(Υ_W^TS) ≤ N_1(S) + N_1(Λ_W^Tτ_Z(S)) ≤ (1 + C_NSη + C_twη)N_ℛ(S); take the infimum over ℛ.
(4) *δ_Υ.* E_ΥΞ_1 = 0 (Codex §1) and x − Π_Wx ∈ Ran Ξ_1, so E_Υx = E_Υw with w := Π_Wx ∈ W. GA-slice on W: E_Υw = Π_W^T(H_Z − H_1)w =
(H_Z − H_1)w + Λ_W^TΞ_1^T(H_Z − H_1)w = (H_Z − H_1)w + Λ_W^TΞ_1^TH_Zw (Ξ_1^TH_1 = 0) = (H_Z − H_1)w − Λ_W^Tτ_Z(H_Zw) (Ξ_Z^TH_Z = 0, KER_Z).
Hence N_1(E_Υx) ≤ C_HDη|||w|||_{1,♯} + C_twηC_FW|||w|||_{Z,♯} ≤ [C_HD + C_twC_FW(1 + C_NCη)]η·C_Π[x]_{1,♯}. (5) GA (Codex §1, banked item 1). ∎

*What the reduction shows.* Of the three Codex §6.4 estimates, **the alignment enters only through the flat slice W: (P1) on the field
side and (P2-tw) on the source side.** Everything that involves the background — (NC), (NS), (HD), (FW), (AC) — is slice-independent
and is the corrected form of BGT55 §6.3's table (which Codex §6.2 refuted in its printed BCH form). Codex §6.4's quotient objection
("a bound on W … yields A2 only if one controls the chosen W representative") is exactly (P1); its chart objection is (NC).
*Why the ♯ pair:* (FW) fails in plain 𝔐^∇ (the s-slot κr_l(w) carries L^{θ(k−l)}·L^{k−1−l} against 𝔐^∇'s L^{k−1−l}; ARGUED in BGT55 P10's
remark) and holds in ♯ with C_FW ≤ C(1 + κ_+L^θ): ‖κ_lr_l(w)‖_R ≤ κ_+max_lL^{θ(q+1)}L^qL^{−(1+θ)q}|||w|||_♯ = κ_+L^θ|||w|||_♯. This is a
sufficiency reason (Codex §6.1: not a necessity theorem). (FW)'s G-slot (curvature of w) and N_res parts are routine; its status is ARGUED.

## 3. The source half forces hierarchical dependence; the S_E alignment fails (A1) — a dual witness (Codex §2's open item, settled)

CODEX_REVIEW_BGT §2 left "failure of a uniform estimate for the prescribed S_E alignment" NOT-VERIFIED and listed what a proof needs: an
admissible whole cc_Z source (caveats 1-2), a lower bound valid on every slot representation of N (caveat 3), and charges off the
level-k roots (caveat 4). All four are supplied below. The mechanism is not BGT55 §6.4's Green-function spike count.

> **Lemma DW (a dual witness for N_1). PROVEN-HERE.** Let y_0 be a level-1 site, v′ ∈ su(N), φ := v′δ_{y_0} (a level-0 function),
> and x^φ := (dφ, 0, …, 0) ∈ X. For every general source y,
>   **|y(x^φ)| ≤ 2d|v′|·L^{2−(2+θ)k}·N_1(y)**   (all k ≥ 1, 0 ≤ θ < 1).

*Proof.* Fix any flat representation y = Σ_l[d^TG_l + j_l + r_l^Ts_l]. Then y(x^φ) = Σ_l[⟨G_l, dx^φ_l⟩ + ⟨j_l, x^φ_l⟩ + ⟨s_l, r_l(x^φ)⟩]. Here
dx^φ_0 = ddφ = 0; x^φ_l = 0 for l ≥ 1, so dx^φ_l = 0, ⟨j_l, x^φ_l⟩ = 0 and r_l(x^φ) = Q_l0 − 0 = 0 for l ≥ 1; r_0(x^φ) = Q_0dφ − x^φ_1 = d ev^{(1)}φ
(root covariance), which is ±v′ on the 2d level-1 links at y_0 (y_0 is a level-1 site) and 0 elsewhere; dφ is ±v′ on the 2d level-0
links at y_0. So |y(x^φ)| ≤ 2d|v′|(sup|j_0| + sup|s_0|). Now sup|j_0| = L^{−3k}‖j^c_0‖_∞ and, from the l = 0 term of ‖s‖_R,
sup|s_0| = L^{−(k−1)}‖s^c_0‖_∞ ≤ L^{−(k−1)}L^{−θk}L^{−(k−1)}‖s‖_R = L^{2−(2+θ)k}‖s‖_R. Since (1 − θ)k + 2 > 0, L^{−3k} ≤ L^{2−(2+θ)k}, and
‖j^c_0‖_∞ + ‖s‖_R ≤ (the N-expression of the representation). Take the infimum over representations. ∎

> **Lemma LC (covariant line currents are cc_Z). PROVEN-HERE.** Let 1 ≤ l ≤ k − 1, γ = (b_1, …, b_n) the closed level-l line through a
> level-l site in direction μ (all links positively oriented, n = TL^{k−l}), hol := Z_l(b_1)⋯Z_l(b_n), and v ∈ su(N) with Ad_{hol}v = v
> (the centraliser of hol in su(N) is nonzero for N ≥ 2). Put j(b_1) := v, j(b_{i+1}) := Ad^{−1}_{Z(b_i)}j(b_i), and S(x) := ⟨j, x_l⟩. Then
> S ∈ cc_Z (indeed every covariant site charge vanishes), **N_Z(S) ≤ L^{(3+θ)(k−l)}|v|**, and its flat charge at the site y_i entered by b_{i−1} is
> **q(y_i) := (d^Tj)(y_i) = (1 − Ad^{−1}_{Z(b_{i−1})})j(b_{i−1})**, so Ξ_1^TS = Σ_iq(y_i)δ_{y_i} (placed at level 0).

*Proof.* ⟨j, d_Zλ⟩ = Σ_b⟨Ad^{−1}_{Z(b)}j(b), λ(head b)⟩ − ⟨j(b), λ(tail b)⟩ (Ad orthogonal for the invariant pairing), so the covariant charge at
y_i is Ad^{−1}_{Z(b_{i−1})}j(b_{i−1}) − j(b_i) = 0 for i = 2..n, and at y_1 it is Ad^{−1}_{Z(b_n)}⋯Ad^{−1}_{Z(b_1)}v − v = Ad^{−1}_{hol}v − v = 0. Hence
⟨S, Ξ_Zλ⟩ = 0 for all λ. The representation ℛ = (0, j, 0) has N_ℛ = ‖j‖_Pc = L^{θ(k−l)}L^{3(k−l)}|v| (|j(b_i)| = |v|). The flat charge is
⟨j, dλ⟩'s coefficient j(b_{i−1}) − j(b_i). ∎

> **Proposition NEC (what uniform t_* demands of any alignment Υ_W). PROVEN-HERE.** For every left inverse Λ_W, every background Z, every
> S, γ, v as in Lemma LC and every y_0 ∈ γ that is not a level-k root:
>   **N_1(Υ_W^TS) ≥ |Σ_{y∈γ}⟨q(y), (Λ_Wx^φ)(y)⟩|·L^{(2+θ)k−2}/(2d|v′|),**  hence
>   **t_*(Υ_W) ≥ |Σ_{y∈γ}⟨q(y), (Λ_Wx^φ)(y)⟩|·L^{(2+θ)k−2−(3+θ)(k−l)}/(2d|v′||v|).**
> If Λ_W reads only the level-0 field — **S_E does (BFT_B §15.0: λ^E_X is defined from x_0 alone)** — then Λ_Wx^φ = −φ and
>   **t_*(Υ_W) ≥ |⟨(1 − Ad^{−1}_{Z(b_in)})j(b_in), v̂′⟩|·L^{(2+θ)k−2−(3+θ)(k−l)}/(2d|v|),**  b_in the link of γ entering y_0.

*Proof.* Υ_W^TS = Π_W^TS (S ∈ cc_Z), and (Π_W^TS)(x^φ) = S(x^φ + Ξ_1Λ_Wx^φ) = ⟨j, x^φ_l⟩ + ⟨j, d ev^{(l)}Λ_Wx^φ⟩ = 0 + Σ_{y∈γ}⟨q(y), (Λ_Wx^φ)(y)⟩.
Apply Lemma DW to y = Π_W^TS, then divide by N_Z(S) (Lemma LC). If Λ_W reads only x_0: x^φ and Ξ_1φ have the same level-0 component dφ, and
φ ∈ Λ_0 (y_0 is not a level-k root), so Λ_Wx^φ = Λ_WΞ_1φ = −φ; the sum is −⟨q(y_0), v′⟩; choose v′ parallel to q(y_0). ∎

> **Corollary NEC-E (S_E is not a k-uniform alignment; neither is any level-0-only alignment). PROVEN-HERE.** Take l = k − 1 and any
> background whose level-(k−1) line through y_0 has a link b_in with (1 − Ad^{−1}_{Z(b_in)})j(b_in) ≠ 0 — e.g. every small pure gauge 1^G,
> G = e^g with g smooth in coarse coordinates and [∂_μg, v] ≠ 0 at y_0 (there hol = 1, so every v is admissible). Then
>   **t_*(Υ_E) ≥ c_N·|[z^c_{k−1}(b_in), v̂]|·L^{(2+θ)k−6−θ}/(2d)·(1 + O(|z_{k−1}|)),**
> where z^c_{k−1} = L·z_{k−1} is the coarse-unit background link. At fixed background size this grows like L^{(2+θ)k}: **(A1)'s source
> bound fails for Υ_E uniformly in k**, at backgrounds where GA-PG's own alignment M_G is exact (E_{M_G} = 0, t_± = 1). The same holds for
> every alignment whose gauge function reads only x_0, and (with the general inequality) for every alignment whose response to a level-0
> datum reaches level-l sites with O(1) values when (2+θ)k − 2 > (4+θ)(k−l).

*Reading.* (i) BGT55's verdict "S_E is the wrong Υ" (N15, ARGUED by a P0 spike count) is **CONFIRMED by a different, complete argument**;
its printed power count and its Λ_E^T formula stay as Codex left them (NOT-VERIFIED / REFUTED). The cost is not a level-0 spike: it is that a
level-0 pure-gauge datum is moved, by any level-0 slice, onto **coarse-level** sites, where it pairs with the background-twisted charges of a
level-(k−1) current; the dual price of a level-0 datum is only L^{2−(2+θ)k} (its s_0 slot), while the twisted charge of a level-(k−1) current
of unit N-size is ≍ |z^c_{k−1}|L^{−(4+θ)}. (ii) The general inequality is a quantitative form of (H): **an alignment with k-uniform t_* must
not let level-m data reach much coarser sites**. A strictly hierarchical Λ_W (ev^{(l)}Λ_Wx independent of x_m for m < l) makes the sum vanish
identically for x^φ (its level-l values are those of Λ_W0 = 0, l ≥ 1). (iii) Nothing here refutes Theorem GA, (R2), or GA-slice: it removes
one alignment.

**Check al55_nec (record).** Criteria `checks/al55_nec_criteria.md` written 03:55:36Z, before the script (`checks/al55_nec.py`). One run,
03:57:25Z, `nice 10`, `python3 -I -B`, Fractions/ints only, 0.16 s, 20.5 MB (`checks/al55_nec_out.txt`, `checks/al55_nec_err.txt`). No
criterion edited. **A1-A8 PASS; C1-C5 all FIRE** (d = 2, L = 3, k = 2, T = 2, su(2) with rational SO(3) Ad). Exact values: q(y_0) =
(−1328/4485, −112/69, 10624/4485); (Π^TS)(x^φ) = −1712/897 for both level-0 forest left inverses and 0 for the hierarchical one (A5, A6).
The script decides the identities of Lemmas DW, LC and Proposition NEC (including root covariance of the contour-built Q_0 and that no slot
other than j_0, s_0 sees x^φ); it decides nothing about k-growth (that is the exact power count in the corollary) or about S_E's boxes.

## 4. A sharper reduction: the field half needs C^{1,θ} gauge functions, not a C^{1,α} representative

Lemma RED asks for (P1), a bound on the slice representative Π_Wx in 𝔐^∇. That is more than GA needs, and §5 shows that every hierarchical
gauge with in-block integration fails it. Using S_E only as a *reference representative* removes it.

**Norm on gauge functions.** ‖λ‖_𝒞 := max_{0≤l<k}[ sup|λ_l| + ‖∇^cλ_l‖_∞ + [∇^cλ_l]^∞_θ ], λ_l := ev^{(l)}λ on the level-l sublattice, ∇^c the
coarse difference quotient over one level-l step, [·]^∞_θ the pointwise Hölder seminorm (separations ≤ 1 coarse) — **exponent θ, the
residual-weight exponent, not α.**

**(P1′) gauge regularity across levels:** ‖Λ_Wx‖_𝒞 ≤ C_𝒞·|||x|||_{1,♯} for all x ∈ X.
**(AC𝒞)** |||(Ξ_Z − Ξ_1)μ|||_{Z,♯} + |||(Ξ_Z − Ξ_1)μ|||_{1,♯} ≤ C_ACη‖μ‖_𝒞 (slice-independent).
**(E)** the S_E reference: |||Π_Ex|||_{1,♯} ≤ C_E[x]_{1,♯} (EP-bd/GF-E: CODEX_REVIEW_GSHARP items 1-2, CONFIRMED; residual terms are
Ξ_1-invariant) and ‖Λ_Eu‖_𝒞 ≤ C_{E𝒞}|||u|||_{1,♯} (box-Neumann Schauder; ARGUED).

> **Lemma RED′. PROVEN-HERE (exact reduction).** Assume (P1′), (P2-tw), (AC𝒞), (E), and (NC), (HD) on S_E-representatives, (NS), (FW), with
> (C_𝒞 + C_{E𝒞})C_ACη < 1. Then Υ_W is an invertible aligned congruence (A = 1) with
>   t_+ ≤ (1 + C_NCη)C_E + C_ACC_𝒞C_Eη,   t_* ≤ 1 + (C_NS + C_tw)η,
>   δ_Υ ≤ η·C_E{[C_HD + C_twC_FW(1 + C_NCη)] + C_FWC_ACC_𝒞(1 + (C_NS + C_tw)η)}.

*Proof.* Fix x, put x_E := Π_Ex (so x = x_E − Ξ_1Λ_Ex) and λ := Λ_Wx_E, u := (Ξ_Z − Ξ_1)λ.
(t_+) Υ_WΞ_1 = Ξ_Z gives Υ_Wx = Υ_Wx_E − Ξ_ZΛ_Ex, and Υ_Wx_E = x_E − u. So [Υ_Wx]_{Z,♯} ≤ |||x_E|||_{Z,♯} + |||u|||_{Z,♯}
≤ (1 + C_NCη)C_E[x]_{1,♯} + C_ACηC_𝒞|||x_E|||_{1,♯}.
(t_*) Unchanged from RED (it never used P1).
(δ_Υ) E_ΥΞ_1 = 0 gives E_Υx = E_Υx_E. For every y, Υ_W^TH_Zy = Π_W^TH_Zy (Ξ_Z^TH_Z = 0), and Π_W^TH_1x_E = H_1x_E (Ξ_1^TH_1 = 0). Hence
E_Υx_E = Π_W^TH_Z(x_E − u) − H_1x_E = Π_W^T(H_Z − H_1)x_E − Π_W^TH_Zu, and Π_W^Ty = y − Λ_W^Tτ_Z(y) whenever Ξ_1^Ty = −τ_Z(y), which holds for
y = (H_Z − H_1)x_E and y = H_Zu (Ξ_1^TH_1 = 0, Ξ_Z^TH_Z = 0). So N_1(E_Υx) ≤ N_1((H_Z − H_1)x_E) + N_1(Λ_W^Tτ_Z(H_Zx_E)) + N_1(H_Zu) +
N_1(Λ_W^Tτ_Z(H_Zu)) ≤ C_HDη|||x_E||| + C_twηC_FW|||x_E|||_{Z,♯} + (1 + (C_NS + C_tw)η)C_FW|||u|||_{Z,♯}; insert (NC), (AC𝒞), (P1′), (E).
(Invertibility) For μ ∈ Λ_0 and u := (Ξ_Z − Ξ_1)μ: u = Π_Eu − Ξ_1Λ_Eu, so Λ_Wu = Λ_WΠ_Eu + Λ_Eu and ‖Λ_Wu‖_𝒞 ≤ (C_𝒞 + C_{E𝒞})|||u|||_{1,♯}
≤ (C_𝒞 + C_{E𝒞})C_ACη‖μ‖_𝒞 < ‖μ‖_𝒞; so Λ_WΞ_Z = −1 + Λ_W(Ξ_Z − Ξ_1) is invertible on (Λ_0, ‖·‖_𝒞), and Υ_W is invertible (Codex §2). ∎

*Why θ appears (the cross-level regularity exponent, located).* (AC𝒞)'s only delicate term is the ♯-weighted residual of u = (Ξ_Z − Ξ_1)μ:
r^Z_l(u) = −(r^Z_l − r_l)(Ξ_1μ) ∓ [μ(c′), ρ_l(z)] (r_l(Ξ_1μ) = 0; the commutator is Codex §4's corrected covariance, TR-1-small). By CEN2
(BA-4, polarised) the part of (r^Z_l − r_l)(dμ) bilinear in (z, dμ) vanishes when both are constant on the contour support N(X, μ), so what is
left is ≲ C p_L²[ |z_l|·osc_N(dμ_l) + osc_N(z_l)·|dμ_l| ] + O(p_L³|z|²|dμ|) + BCH terms ([z_{l+1}, r_l(·)] relative; [·, ρ(z)] TR-1). With
osc_N(dμ_l) ≤ ρ_l·2^θρ_{l+1}^θ[∇^cμ_l]_θ (own units) the first term contributes, after coarse units (×L^q) and the ♯ weight (×L^{(1+θ)q}),
  Cp_L²L^{−2}·L^{(1+θ)q}·L^{q}·L^{−(q+1)}L^{−(q+1)}L^{−θq}·|z^c_l|[∇^cμ_l]_θ = Cp_L²L^{−2}|z^c_l|[∇^cμ_l]_θ,
**uniform in q exactly because the Hölder exponent of ∇μ equals θ**; with exponent β the factor is L^{(θ−β)q}. The other terms decay like
L^{−(1−θ)q}. So **(AC𝒞) is ARGUED (power count, every input named) and the regularity (P1′) must hold with Hölder exponent ≥ θ.** C^{2,α}
(what P1 would give) is more than needed; C^{1,α} (what 𝔐^∇ gives a field) is less than needed, since α < θ.

## 5. T2 — four candidates, against (H)/NEC on the source side and (P1′) on the field side

| candidate | (H) | NEC (source half) | (P1′) (field half, C^{1,θ} across levels) |
|---|---|---|---|
| S_E (box Coulomb, level 0) | no (reads x_0 only) | **FAILS** (Cor. NEC-E, PROVEN-HERE) | holds (Λ_Ex_E = 0; Λ_E smooth — (E)) |
| multiscale axial-in-blocks (Dimock 1410.2798 form) | yes | passes | **FAILS by L^{k−l−1}** at level l (Prop. AX-SEAM, below) |
| per-level slice Γ_PL (GSHARP55) | yes (Codex §6.3) | passes | **NOT-VERIFIED** — isolated question (5.3) |
| hierarchical Coulomb-detail gauge Λ_HC (new, 5.4) | yes | passes | ARGUED, reduced to three standard lemmas (§6) |

### 5.1 S_E — done in §3: the field half is free, the source half fails.

### 5.2 Multiscale axial-in-blocks: hierarchical, but it moves the axial seam into every level

*Definition (the soft-chain transcription of Dimock's δ_{X_k}).* For a level-(l+1) site Y and y ∈ B(Y) let τ_l(x_l)(Y, y) := (1/d!)Σ_σ∫_{P^σ(Y→y)}x_l
(permutation-averaged axial integral inside the block, Dimock eq. (27) with x_l in place of Q^lA). Put λ_k := 0 and, top-down,
**λ_l(y) := λ_{l+1}(Y) − τ_l(x_l)(Y, y)** (y ∈ B(Y)); Λ_axx := λ_0. Equivalently λ_l(y) = −Φ_l(y), **Φ_l(y) := Σ_{i=l}^{k−1}τ_i(x_i)(Y_{i+1}(y), Y_i(y))**,
the integral of x along the *hierarchical path* (Y_i(y) the level-i ancestor root of y, Y_l(y) = y).
*Algebra (PROVEN-HERE).* τ_l(dν_l)(Y, y) = ν(y) − ν(Y), so Λ_axΞ_1ν = −ν (ν = 0 at level-k roots); level-l values depend on x_l..x_{k−1} only (H);
NEC is passed (Λ_axx^φ vanishes at level ≥ 1 sites).
> **Proposition AX-SEAM. PROVEN-HERE (identity); growth PROVEN-HERE for linear fields.** For adjacent level-l sites y, y′ (link b = (y, y′)):
>   **(x + Ξ_1Λ_axx)_l(b) = −[Φ_l(y′) − Φ_l(y) − x_l(b)] = the integral of x around the open hierarchical path c → y → y′ → c′,**
> where c, c′ are the level-s roots at which the two hierarchical paths start (s = the first level at which the ancestors coincide; if they never
> do below k, c and c′ are distinct level-k roots and λ vanishes at both). For a field that is linear in coarse coordinates with constant
> curvature F (componentwise), lattice Stokes is exact and the right side is F times the signed area of the region swept between the two
> hierarchical paths, which is ≍ ρ_sρ_{s−1} (the two top segments fan out from a common level-s root to level-(s−1) ancestors at distance
> ρ_{s−1}); in coarse units the representative's link value is ≍ |F^c|ρ_sρ_{s−1}/ρ_l, i.e. **≍ |F^c|L^{k−l−1} on links crossing level-k cell
> boundaries.** The same quantity is the jump of the coarse gradient of λ_l across that link, so **‖∇^cλ_l‖_∞ ≥ c|F^c|L^{k−l−1}: (P1′) fails, and
> (P1) fails a fortiori** (check al55_ax computes the area exactly for k = 2, 3).
*How this relates to NLOC.* The global axial gauge (NL-7) fails by T because its integration lines wrap the torus; hierarchical paths have total
coarse length ≤ Σ_iρ_{i+1}d < d·L/(L−1), so **the factor T is avoided**. The within-cell axial gauge (NL-9) fails the sup budget by L^k on
cell-crossing links; the multiscale version **does not avoid this**: it reproduces it at every level-s seam with the factor ρ_sρ_{s−1}/ρ_l. This is
consistent with Dimock §3.5 (and with BALABAN_EXTRACT §4.1: CMP 109's estimates use "Landau via u_k"): the axial-in-blocks gauge is used to
*define* the integral; regular representatives come from a Landau-type transformation. For the alignment that means: **axial-in-blocks gives the
source half, not the field half.** A Landau-type regularisation of it is what 5.4 builds directly.

### 5.3 Γ_PL: what is proved, and the one open question
- (H) and NEC: pass (top-down triangular system; Codex §6.3's mechanism is exactly hierarchical dependence).
- Its homogeneous inter-level step E_PL (x_i = 0: root values inherited, block mean = root value, P_resΔν = 0) **reproduces Π_1 and the harmonic
  quadratics but not |y|²**: h(d(½y_1²))(X) = avg_{B(X)}½y_1² − 0 = (L² − 1)/24 ≠ 0 in own units (PROVEN-HERE, one line). And P_resΔν = 0 means
  Δν ∈ span{1_{B(X)}, δ_{c_X}} per block, so E_PL places **point sources at every root** (Green's-function singularities |y − c|^{2−d}).
- Consequence (literature as comparator only: a stationary scheme with C^m limits must reproduce Π_m — Cavaretta–Dahmen–Micchelli, Mem. AMS 453
  (1991); Dyn–Levin, Acta Numerica 2002): E_PL cannot deliver the C^{2,α} gauge functions (P1) would need. **(P1) is not needed (Lemma RED′).**
- **Open, stated exactly:** does E_PL, iterated top-down, keep ‖·‖_𝒞 (C^{1,θ}) bounded uniformly in the number of levels? The root sources have
  gradient amplitude O(a·ρ_i) at level i when the second-derivative content a is bounded, which is harmless; the decisive number is the
  amplification of second-derivative content near a root from one level to the next (a heuristic count gives a factor ≍ c_GL^d per level near
  each root, c_G a lattice Green's-function constant, which would compound). Not computed here. **Verdict on GSHARP55 §5.5's hole and BGT55's
  "(α) is exactly GSHARP55 §5.5's open hole": CONFIRMED as open; sharpened to this one number.**

### 5.4 The hierarchical Coulomb-detail gauge Λ_HC (the candidate)
*Ingredients.* A 1D L-adic **interpolatory** stationary subdivision scheme s (mask a, (sc)_{Lj} = c_j) reproducing Π_1, with derived scheme
s^{[1]} (Δ∘s = s^{[1]}∘Δ); S_0 := s^{⊗d} (level l+1 → l, on functions), S_1 := s^{[1]} ⊗ s^{⊗(d−1)} on links — BFT_B §15.0's Construction CP
(commuting pair: d∘S_0 = S_1∘d). R := restriction to the coarse sublattice, so RS_0 = 1. Δ_l := d_l^*d_l on the level-l torus, inverted on
mean-zero functions.
*Definition.* λ_k := 0; for l = k − 1, …, 0:
  **λ_l := S_0λ_{l+1} + μ_l(x_l),  μ_l(x_l) := −(1 − S_0R)Δ_l^{−1}d_l^*x_l;  Λ_HCx := λ_0.**
> **Lemma HC-1 (algebra). PROVEN-HERE.** (i) ev^{(l)}Λ_HCx = λ_l for every l (RS_0 = 1 and R(1 − S_0R) = 0), so λ_0 ∈ Λ_0 (λ_k = 0).
> (ii) (H): λ_l depends only on x_l, …, x_{k−1}. (iii) Λ_HCΞ_1 = −1: for x = Ξ_1ν, Δ_l^{−1}d_l^*d_lν_l = ν_l − mean, (1 − S_0R) kills constants, so
> μ_l = −ν_l + S_0ν_{l+1}, and by induction λ_l = −S_0ν_{l+1} − ν_l + S_0ν_{l+1} = −ν_l. (iv) NEC is passed: Λ_HCx^φ vanishes on level-1 sites.
> (v) Transpose: Λ_HC^Tq = (c_0, …, c_{k−1}) with plain level-m currents **c_m = −d_mΔ_m^{−1}(1 − R^TS_0^T)S^{(m→0)T}q** (S^{(m→0)} := S_0^m); for q
> supported on level-l sites, c_m = 0 for m < l (S_0^TR^T = 1). So level-l charges are completed at levels ≥ l only — the transpose form of (H).
> (vi) Homogeneous step: x_l = 0 gives λ_l = S_0λ_{l+1} — pure smooth subdivision; **no root sources** (contrast E_PL).
*Proof.* Each item is one line as indicated; (v): ⟨q, Λ_HCx⟩ = Σ_m⟨S^{(m→0)T}q, μ_m(x_m)⟩ and μ_m^T = −d_mΔ_m^{−1}(1 − R^TS_0^T). ∎
*Design principle (why this and not Γ_PL).* (1) Inherit coarse values by a smooth interpolation, so the homogeneous step cannot create
singularities. (2) Fix the level-l detail by a rule that is **exact on degree-1 data in the Coulomb sense**: for x_l affine, Δ^{−1}d^*x_l is a
quadratic plus a constant, and (1 − S_0R) kills it when s reproduces Π_2 (and leaves O(ρ_{l+1}²) when s reproduces Π_1). (3) Keep the transpose
level-local ((v)). (1)+(2) are what the field half needs, (3) is what the source half needs.

**Checks al55_sub, al55_hcg, al55_ax (records).** Criteria written before each script (sub 04:10:40Z; hcg and ax 04:12:07Z; ax's Amendment A1
04:12:35Z, before its script existed — reason stated in the file). All runs `nice 10`, `python3 -I -B`, Fractions/ints only, stdout only.
- **al55_sub.** Run 1 (04:11:20Z) aborted at an internal transcription `assert` (zero mask entries kept as dict keys) before any criterion was
  evaluated (`checks/al55_sub_err_run1.txt`); one-line fix (drop zero keys); run 2 (04:11:32Z, 0.10 s) is the record (`checks/al55_sub_out.txt`).
  **P1, P2, P4a, P4b PASS; P3 FAIL; C1, C2 FIRE.** The ternary 4-point Deslauriers–Dubuc scheme s3 reproduces cubics (σ_3^4 | a, σ_3^5 ∤ a) and is
  **certified C^{1,β} with β > 1/2**: ‖S_c^5‖_∞ = 875065/14348907 gives ‖S_c^5‖²·3^5 = 0.9038 < 1; at n = 7, ‖S_c^7‖_∞ = 122416585/10460353203, so
  β ≥ −log_3(‖S_c^7‖^{1/7}) ≈ 0.578 (β > 3/5 not certified at n = 7). **P3 FAIL (recorded, pre-registered): the 5-adic 4-point DD scheme is not
  certified at n ≤ 5** (norm²·5^n = 1.686 at n = 5, decreasing) — (SUB) is certified for L = 3 only.
- **al55_hcg.** One run, 04:15:12-04:15:44Z, 31.6 s, 62 MB (`checks/al55_hcg_out.txt`); two coding errors were corrected **before** the first run
  (a triple-counted periodisation weight and a sign in the discrete adjoint — patch recorded in the script's comments "pre-run fix").
  **H1-H8 PASS (models MA: d = 2, k = 2, T = 2; MB: d = 2, k = 3, T = 1); K1-K5 all FIRE** (K2: the non-interpolatory B-spline keeps the left
  inverse but breaks nested restriction — H1 ok, H2 fails — as Lemma HC-1's proof predicts).
- **al55_ax.** One run, 04:17:46Z, 0.8 s (`checks/al55_ax_out.txt`). **X1, X2, X4 PASS at k = 2, 3, 4; X3′ PASS; XC1 FIRES.** Exact seam values on the
  link (C + h, C + h) → (C + h + 1, C + h) (s = k − 1 seam, unit curvature): rep^c = 0, −2/27, −20/81 at k = 2, 3, 4 (ratio 10/3 from k = 3 to 4).

### Errata to §3 and §5 (append-only; found on re-derivation and by al55_ax)
- **§5.2, Proposition AX-SEAM, the area scale is wrong by one level.** The two top segments run from the common level-s root to level-(s−1)
  children inside its block, i.e. over a distance ≤ dρ_{s−1}, not ρ_s. The swept area is **≍ ρ_{s−1}²** (not ρ_sρ_{s−1}), so the representative's
  link value and the gradient jump of λ_l are **≍ |F^c|ρ_{s−1}²/ρ_l: L^{k−l−4} on interior level-(k−1) seams (s = k − 1, a closed loop: exact for
  linear fields), and on level-k cell boundaries (s = k) the curvature part is ≍ L^{k−l−2} plus the chord term (the open root-to-root integral,
  ≍ ‖r^c_{k−1}‖ + Q-defect) times L^{k−l}.** al55_ax confirms the s = k − 1 scaling: rep^c/L^{k−4} = −2/9 at k = 3 and −20/81·L^0 = −(2/9)(10/9)
  at k = 4 (the 10/9 is the next-finer level's contribution). The conclusion — (P1′) and (P1) fail, unboundedly in k − l — is unchanged; the
  printed exponent "L^{k−l−1}" in the §5 table and in AX-SEAM should read L^{k−l−2} (cell boundaries) / L^{k−l−4} (interior seams).
- §3, Corollary NEC-E: "c_N" is 1 + O(|z_{k−1}|) ((1 − e^{−ad_z})v = [z, v] + O(|z|²|v|)); no other constant is hidden.

## 6. T3 — regularity across levels for Λ_HC: (P1′) and (P2-tw), reduced to named lemmas

### 6.1 The field half (P1′)
> **Lemma DET (detail size). ARGUED (complete except the cited lattice Green's-function bounds).** Let s reproduce Π_3 (s3 does: al55_sub P1).
> For every l < k and every level-l 1-form x_l,
>   **sup|μ_l| ≤ C_D·ρ_{l+1}^{2+α}·‖x_l‖_{C^{1,α}},**  ‖x_l‖_{C^{1,α}} := ‖x^c_l‖_∞ + ‖∇^cx^c_l‖_∞ + [∇^cx^c_l]_α (the level-l part of 𝔐^∇),
> with C_D = C_D(L, s), uniform in l, k, T.
*Proof.* In own units at level l, μ_l(y) = −Σ_bK(y, b)x_l(b), K := (1 − S_0R)Gd^*, G the lattice Green's function (periodised). (a) S_0 = s^{⊗4}
reproduces every polynomial of total degree ≤ 3, so (1 − S_0R) acts on smooth functions as a fourth-order difference at scale L; with
|∂^jG(n)| ≤ C_j(1 + |n|)^{−2−j} (d = 4; standard lattice potential theory, cited as comparator, to be rebuilt) this gives |K(y, b)| ≤ C(1 + |y − b|)^{−3}
for |y − b| ≤ 2L and ≤ CL^4|y − b|^{−7} beyond. (b) K annihilates affine 1-forms: Gd^*P is, up to a harmonic remainder that vanishes in the cutoff
limit (by the r^{−7} decay), a polynomial of degree ≤ 2, killed by (1 − S_0R). (c) Taylor at y in coarse units: x^c_l(y + n) = P_y(n) + R_y(n),
|R_y(n)| ≤ C[∇^cx^c_l]_α(ρ_l|n|)^{1+α} for ρ_l|n| ≤ 1 (Campanato ≅ Hölder at lattice scales), and |R_y(n)| ≤ 2‖x^c‖_∞ + 2‖∇^cx^c‖_∞ρ_l|n| beyond.
(d) |μ_l(y)| = ρ_l|Σ_nK(n)R_y(n)| ≤ Cρ_l^{2+α}[∇x]_α(Σ_{|n|≤2L}|n|^{−3}|n|^{1+α} + L^4Σ_{|n|>2L}|n|^{−6+α}) + CL^4ρ_l^4‖x‖_{C^1}
≤ C′L^{2+α}ρ_l^{2+α}‖x_l‖_{C^{1,α}} = C′ρ_{l+1}^{2+α}‖x_l‖_{C^{1,α}} (sums over Z^4 shells: Σ_{|n|≤2L}|n|^{α−2}|n|^3/|n| ≍ L^{2+α}; the far sum converges
since −6 + α + 3 < −1). ∎
> **Lemma HB (hierarchical reconstruction in C^{1,θ}). ARGUED-standard.** Let s generate C^{1,β} limits, β > θ, with Π_1 reproduction, and let
> |μ_m| ≤ Mρ_{m+1}^{2+α} (m ≥ l), μ_m vanishing on level-(m+1) sites. Then λ_l := Σ_{m≥l}S^{(m→l)}μ_m has ‖λ_l‖_{C^{1,θ}(level l)} ≤ C_HM, uniformly.
*Proof.* S^{(m→l)}μ_m = Σ_yμ_m(y)Φ_y^{(m→l)}, Φ_y^{(m→l)} := S^{(m→l)}δ_y, supports of diameter ≤ C_sρ_m with bounded overlap, and (from the certified
contraction ‖S_c^n‖ ≤ Cb^{−nβ}, c = ba/σ_b² — the content of al55_sub) sup|Φ| ≤ C, sup|∇^cΦ| ≤ Cρ_m^{−1}, [∇^cΦ]_β ≤ Cρ_m^{−1−β}, uniformly in m − l.
Then sup|∇^cλ_l| ≤ CMΣ_mρ_{m+1}^{2+α}ρ_m^{−1} ≤ C′M; at separation h: terms with ρ_m ≥ h give ≤ CMρ_m^{2+α}ρ_m^{−1−β}h^{β−θ} (sum over ρ_m ≥ h
dominated by ρ_m ≈ 1 since 1 + α − β > 0, total ≤ CMh^{β−θ} ≤ CM), terms with ρ_m < h give ≤ 2CMρ_m^{1+α}h^{−θ} (sum ≤ CMh^{1+α−θ}). ∎
> **Proposition P1′(HC). ARGUED** (from DET, HB and the certified (SUB)). For L = 3, s = s3 and any class exponent θ ≤ 1/2 (indeed θ < 0.578):
>   **‖Λ_HCx‖_𝒞 ≤ C_𝒞·max_l‖x_l‖_{C^{1,α}} ≤ C_𝒞|||x|||_{1,♯}**, uniformly in k ≥ 1, T ≥ T_0.
*Proof.* Lemma HC-1 gives λ_l = Σ_{m≥l}S^{(m→l)}μ_m (induct on the recursion); DET gives M = C_Dmax_m‖x_m‖_{C^{1,α}}; HB gives the C^{1,θ} bound at every
level; sup|λ_l| is part of HB. ∎ **This is the "regularity across levels, uniformly in k and T" the task asks for, in the exact form GA consumes
(through RED′): C^{1,θ} gauge functions, Hölder exponent θ.** For odd L ≠ 3 the scheme input (SUB) is not certified here (al55_sub P3 FAIL for
the 5-adic 4-point scheme at n ≤ 5): a higher-order L-adic DD scheme or a deeper certification is needed — a decidable computation.

### 6.2 The source half (P2-tw)
> **Proposition P2-tw(HC). ARGUED (power counts; every input named).** At a background with ‖z‖_{𝔐^∇} ≤ η ≤ η_0 satisfying (TR-1), for every source y
> and covariant representation ℛ = (G, j, s): **N_1(Λ_HC^Tτ_Z(y)) ≤ C_tw·η·N_ℛ(y)**, C_tw = C(N, L, s, κ_±, α, θ, A_s, A_j).
*Structure of τ_Z, slot by slot (identities, PROVEN-HERE).* j-slot: τ_Z(j_l) = ev^{(l)T}ϑ_l, ϑ_l(y) = Σ_{head b = y}(Ad^{−1}_{Z(b)} − 1)j_l(b) — point charges,
own |ϑ_l| ≤ 2d(1 + O(η))|z_l||j_l|. G-slot: ⟨d_Z^TG, (Ξ_Z − Ξ_1)λ⟩ = ⟨G, d_Zd_Zλ⟩ − ⟨G, (d_Z − d)dλ⟩ (ddλ = 0), so τ_Z(d_Z^TG_l) = ev^{(l)T}[κ_F^TG_l −
d^TJ_G], J_G := (d_Z − d)^TG_l (own ≤ C|z_l||G_l|), κ_F the curvature action (own ≤ C|F_Z||G_l|). s-slot: τ_Z((r^Z_l)^Ts_l) = (λ ↦ r^Z_l(Ξ_Zλ))^Ts_l −
((r^Z_l − r_l)∘Ξ_1)^Ts_l; the first is the commutator with ρ_l(z) (Codex §4, TR-1-small point charges), the second has the CEN2 structure of §4
(coefficients bilinear in (z, dλ) with the constant–constant part cancelled), i.e. charges of divergence form with coefficients ≤ Cp_L²|z||s|.
*Completion (Lemma HC-1 (v), checked al55_hcg H5).* Λ_HC^Tq = (c_m)_{m≥l}, c_m = −d_mΔ_m^{−1}(1 − R^TS_0^T)Q_m, Q_m := S^{(m→0)T}q (the coarsened charge).
(A) *Point charges* of own size ≤ a at level-l sites: own |Q_m| ≤ C_sL^{4(m−l)}a; the detail (1 − R^TS_0^T)Q_m is neutral with vanishing moments ≤ 3
at scale ρ_{m+1}, so its Coulomb gradient has own sup ≤ C(L)·max|Q_m| (near field Σ_{|n|≲L}|n|^{−3} ≍ L, far field ∝ L^4Σ|n|^{−7}|n|³, plus the
root-placement factor of R^TS_0^T — all L-dependent constants); hence π_m(c_m) ≤ C(L)L^{3(k−m)}L^{4(m−l)}a.
(B) *Divergence charges* d^TJ with own |J| ≤ b at level l: the commuting pair gives S_0^Td^T = d^TS_1^T (checked al55_hcg H8), so Q_m = d^T(S_1^{T(m−l)}J)
with own |S_1^{T(m−l)}J| ≤ C_sL^{3(m−l)}b (bounded transposed iterates of the convergent derived scheme), and the local Helmholtz-detail of a
divergence is sup-bounded with C(L)(1 + log L); hence π_m(c_m) ≤ C(L)π_l(J) (no growth: the FLUX mechanism, COFUN_CC Lemma FLUX, at every level).
*Insert the sizes.* j-slot: a = 2d|z_l||j_l| = 2d|z^c_l|L^{−4(k−l)}π_l(j_l), so L^{θ(k−m)}π_m(c_m) ≤ C|z^c_l|L^{−(1−θ)(k−m)}π_l(j_l) ≤ Cη·L^{−θ(k−l)}‖j‖_Pc
(and the P0 analogue at l = 0). G-slot: π_l(J_G) ≤ C|z^c_l||G^c_l|, so the weighted cost is ≤ CL^{θ(k−l)}|z^c_l||G^c_l| ≤ Cη‖G‖_Y; curvature point charges
are smaller by |F^c|ρ_l. s-slot: the TR-1 point charges have own size ≤ a_qηL^{−θ(q+1)−5q}‖s‖_R (|s_l| ≤ L^{−θ(q+1)−2q}‖s‖_R, |ρ_l(z)| ≤ a_qL^{−3q}η), so
the weighted cost is ≤ Ca_qηL^{4−θ−(1+θ)q}‖s‖_R (a_q linear in q is beaten by L^{−(1+θ)q}); the divergence part costs ≤ C|z^c|L²‖s‖_R ≤ Cη‖s‖_R. Every term
is k-, T-uniform. ∎(ARGUED)
*Why the hierarchy is what makes this work (contrast with §3).* For S_E the same twisted charges are completed at level 0, and a level-0 test datum
sees them with the dual price L^{2−(2+θ)k} (Lemma DW) — the source of Corollary NEC-E's L^{(2+θ)k}. For Λ_HC, level-l charges never reach levels below
l (c_m = 0 for m < l), and the cost of carrying them up is paid in coarser slots whose weights L^{θ(k−m)} are smaller.

### 6.3 What is still missing for T3 (exact list)
(i) DET's lattice Green's-function derivative bounds in d = 4 with explicit constants (cited, must be rebuilt in note + runner per the owner's rule);
(ii) HB's discrete constants from the certified contraction (standard; not written with numbers); (iii) (SUB) for odd L ≠ 3; (iv) the
Helmholtz-detail locality bounds (A)-(B) with constants; (v) a **weighted** version: Λ_HC's detail kernel decays like r^{−7}, not exponentially,
so (R2) with e^{m·dist} weights (BFT-3) is NOT covered — an exponentially local detail rule that keeps the exact left-inverse property is OPEN
(a massive (Δ + M)^{−1} breaks Λ_HCΞ_1 = −1; a partition-of-unity interpolation loses Π_1 reproduction).

## 7. T4 — assembly: Theorem GA + (ALIGN-ℓ♯) ⇒ (R2) on 𝒞_glob, every input named with its status

> **Theorem R2-glob♯ (an implication). PROVEN-HERE as a reduction (Lemma RED′ + Theorem GA); its inputs carry the statuses listed.**
> Fix d = 4, L = 3, N, κ_±, 0 < α < θ ≤ 1/2. There are ε_b > 0 and C′_b, depending only on (N, L, κ_±, α, θ), such that for every k ≥ 1, T ≥ T_0 and
> V ∈ 𝒞_glob(ε), ε ≤ ε_b, at the critical background Z = Z(V) of BFT-0: Ker H_Z = Ran Ξ_Z on {x_k = 0}, and for every S ∈ cc_Z the solution set of
> H_Zx = S is x_* + Ran Ξ_Z with **[x]_{Z,♯} ≤ C′_b·N_Z(S)**, C′_b = t_+t_*C_♯/(1 − C_♯δ_Υ) (t_±, δ_Υ of RED′ with W = Λ_HC) — **provided:**

| # | input | status (file, locating string) |
|---|---|---|
| 1 | BFT-0 on 𝒞_glob with ‖z‖_{𝔐^∇} ≤ η = C_0ε | CONDITIONAL on (H-lin^∇), (H-rem^∇), (FP♯′) — BFT_A §3.9 "Theorem BA" |
| 2 | (B_1♯) = Corollary RW♯ | CONFIRMED (CODEX_REVIEW_BGT banked item 5) |
| 3 | Theorem GA; GA-slice; KER_Z | CONFIRMED (CODEX_REVIEW_BGT items 1, 2, 4) |
| 4 | Lemma RED′ (this file §4) | PROVEN-HERE (exact reduction; unreviewed) |
| 5 | (E) S_E reference: ‖Π_Ex‖_𝔐 ≤ C_rec(‖x‖_inv + N_res(x)) | CONFIRMED (CODEX_REVIEW_GSHARP banked item 1; with x_k = 0 its right side is ≤ C[x]_{1,♯}) |
| 6 | Lemma HC-1 (left inverse, (H), transpose, nested restriction) | PROVEN-HERE; exact check al55_hcg H1-H8 PASS, K1-K5 FIRE |
| 7 | (SUB): s3 reproduces Π_3, is C^{1,β}, β ≥ 0.578 > θ | CERTIFIED for L = 3 (al55_sub P1, P2); **not** for the 5-adic 4-point scheme (P3 FAIL) |
| 8 | (P1′) for Λ_HC: DET + HB | ARGUED (§6.1; lattice Green's-function bounds cited, HB standard) |
| 9 | (P2-tw) for Λ_HC: slot structure + completion bounds (A), (B) + CP | ARGUED (§6.2; slot identities PROVEN-HERE; CP checked al55_hcg H8) |
| 10 | (TR-1) at z, all orders | CONFIRMED as a named-input implication (CODEX_REVIEW_HIGHER, cited by CODEX_REVIEW_BGT §6.4 "Dependency freshness"; I did not re-read HIGHER) |
| 11 | (AC𝒞) | ARGUED (§4 power count; inputs CEN2 = BFT_A BA-4 PROVEN, TR-1, Codex §4's corrected covariance) |
| 12 | (NC), (HD) on S_E representatives; (NS); (FW) | ARGUED (the corrected form of BGT55 §6.3's table: its printed BCH factorisation is REFUTED by Codex §6.2, so the term list must be re-derived from the true linearisation with KOFF's corrected LA-1) |
| 13 | smallness C_𝒞C_ACη < 1 (invertibility, using (P1′) for all x) and C_♯δ_Υ < 1 | holds for ε ≤ ε_b once 1-12 hold |

*Proof.* Items 4-13 give (A1)-(A2) of Theorem GA in the pair (|||·|||_♯ → N) with the constants of RED′; GA (item 3) with (B_1♯) (item 2) gives the
conclusion; item 1 supplies the background. ∎
**Net change against BGT55 §6.5.** BGT55's "one OPEN item (ALIGN-ℓ)" (whose literal (β) is refuted) is replaced by: an explicit hierarchical
alignment Λ_HC whose algebra is proved and checked, whose field half is reduced to two standard lemmas (DET, HB) plus a certified scheme
input, and whose source half is reduced to completion bounds of a local, hierarchical form. **Not claimed:** any ARGUED item as proven; L ≠ 3;
θ > 0.578; anything outside 𝒞_glob ((LOC-GA) stays OPEN, BGT55 §7.2); the weighted version (§6.3 (v)); a constructive 4D Yang–Mills theorem.

## 8. Findings on prior claims bearing on (ALIGN-ℓ) (verdict, file + locating string, reason)

- **F1. BGT55 §6.4 "S_E must not be used as the alignment" / N15 "The S_E alignment is not k-uniform at levels l ≥ 1": CONFIRMED in conclusion
  (new proof: §3, Corollary NEC-E, with a dual witness and an exact cc_Z source); the printed mechanism ("spikes ≍ 2dL^{3l}π_l") is NOT-VERIFIED
  (not re-derived; Codex §2's caveats stand), and BGT55's level-0 formula "Λ_E^Td^Tj_0 =" is REFUTED (Codex §2; agree, not used).**
- **F2. BGT55 §6.4 (β) "the level-l values ev^{(l)}Λ_W(x) are computed from x_l" and "(β) holds by construction" for Γ_PL: REFUTED** (agree with
  CODEX_REVIEW_BGT §6.3; re-derived: ev^{(1)}Λ_Wx is a function of Λ_Wx, so literal level-locality at levels 0 and 1 forces RΛ_W = 0, contradicting
  Λ_WΞ_1 = −1 at level-1 non-roots). Correct statement: hierarchical dependence (H), which §3 shows is necessary in a quantitative form.
- **F3. BGT55 §6.4 "(α) is exactly GSHARP55 §5.5's open hole": CONFIRMED as open, and sharpened** (§5.3: the C^{1,θ} stability of E_PL under
  iteration; E_PL does not reproduce |y|² and places root point sources — PROVEN-HERE).
- **F4. BGT55 §6.5 "Theorem R2-glob … PROVEN as a reduction; one OPEN input (ALIGN-ℓ)": NOT-VERIFIED as stated** (agree with Codex §6.4: literal
  (β) impossible, quotient and chart estimates missing). Replaced by Theorem R2-glob♯ (§7).
- **F5. BGT55 §12 item 3(d) "The candidate alignment is the per-level slice functional Γ_PL (or Balaban's axial-in-blocks gauge, CMP 99:75)":
  REFUTED for axial-in-blocks** (§5.2 AX-SEAM + errata: the field half fails by L^{k−l−2} at level-k seams and L^{k−l−4} at interior level-(k−1) seams;
  al55_ax); **NOT-VERIFIED for Γ_PL** (§5.3). Correct statement: a hierarchical alignment with smooth inter-level interpolation (Λ_HC).
- **F6. BGT55 §6.3 (F-♯) "So the transfer must be run in the transport-weighted response norm": NOT-VERIFIED as a necessity** (agree with Codex §6.1);
  the sufficiency reason is located: (FW) holds in ♯ and its s-slot part does not in plain 𝔐^∇ (§2).
- **F7. GSHARP55 §5.5 "I estimate the level-i correction at O(ρ_i^{1+α}) … which is summable over levels": NOT-VERIFIED** — the estimate is per
  level; its propagation through the triangular system (E_PL) is exactly what is not controlled (§5.3).
- **F8. GSHARP55 §5.5 "The hole: how a level-i correction propagates to finer levels through the triangular system is not written": CONFIRMED.**
- **F9. GSHARP55 §5.5 Lemma PL-adm (bijectivity of Γ_PLD): CONFIRMED** (spot-check: the top-down injectivity and the count dim Λ_0 = N_0 − N_k =
  Σ_i(N_{i+1} + N_i − 2N_{i+1}) re-derived; agrees with CODEX_REVIEW_GSHARP §8).
- **F10. GSHARP55 §5.5 "No live consumer needs the transfer": CONFIRMED in its scope** (transfer of responses to the per-level slice); the alignment
  use is a different consumer and is served by Λ_HC, not by Γ_PL.
- **F11. NLOC Proposition NL-9 (within-cell axial gauge meets ℓ¹, fails sup by L^k): CONFIRMED in direction and extended** — the multiscale
  axial-in-blocks reproduces the seam failure at every level (§5.2). **NL-7 (global axial fails by T): consistent, spot-checked only** — the
  hierarchical paths have bounded total coarse length, so the factor T does not arise there (§5.2).

## 9. Codex verdicts used — agree or disagree, explicitly (files as on disk at 02:46-04:20Z; both complete, ending with their banking lists)

- **CODEX_REVIEW_BGT §1 / item 1 (Theorem GA CONFIRMED; universal condition-number necessity REFUTED): AGREE.** Used as the engine of §2, §4, §7.
- **§2 / item 2 (GA-slice CONFIRMED, identity only on W; S_E obstruction NOT-VERIFIED; BGT55's Λ_E^T formula REFUTED): AGREE with all three.** BGT55's
  evidence did not establish the S_E obstruction; §3 here supplies a different, complete argument (dual witness + exact cc_Z source + non-root
  charge), so the S_E alignment's failure of (A1) is now PROVEN-HERE (pending Codex). The defect identity is used only on W (RED, RED′ step δ_Υ).
- **§3 / item 3 (GA-PG): AGREE**; used only as context (NEC-E operates at pure gauges where M_G is exact and Υ_E is not).
- **§4 / item 4 (KER_Z, SF_Z; the soft-covariance sign must be −[λ(c′), ρ(z)] with the positive-d generator): AGREE**; the corrected sign is the
  one used in §4 and §6.2 (only its size enters).
- **§5 / item 5 (RW♯): AGREE**; it is (B_1♯).
- **§6.1 (power conversions are upper bounds, not necessity theorems): AGREE** (F6).
- **§6.2 (exact BCH factorisation REFUTED): AGREE**; nothing here uses it; (HD) is listed as needing re-derivation from the true linearisation.
- **§6.3 (literal (β) and "Γ_PL satisfies (β)" REFUTED; hierarchical repair plausible): AGREE** (F2); the repair is (H), and §3 proves a
  quantitative form of it necessary for (A1)'s source half.
- **§6.4 (R2-glob NOT-VERIFIED; the three intrinsic estimates; the quotient and chart issues): AGREE**; Lemmas RED/RED′ are the reduction of those
  three estimates to (P1′), (P2-tw) and slice-independent background estimates, with the quotient issue handled through the S_E reference
  representative and the chart issue named as (NC).
- **§7-§10 / items 6-7: AGREE** (not otherwise used).
- **CODEX_REVIEW_GSHARP banked items 1, 2 (flat reconstruction with C_rec; GF-E) and 7 ("the original per-level transfer … NOT-VERIFIED"): AGREE**;
  item 1 is input (E); item 7 is consistent with F7/F8.

## 10. Summary table

### 10.1 Results of this file (status words; none has had a Codex check)
| id | statement (section) | status |
|---|---|---|
| A1 | (ALIGN-ℓ♯) stated with every quantifier and norm GA consumes (§2) | statement |
| A2 | Lemma RED: (P1) + (P2-tw) + slice-independent estimates ⇒ GA's (A1)-(A2) with explicit t_±, δ_Υ (§2) | PROVEN-HERE |
| A3 | Lemma RED′: (P1) replaced by (P1′) = C^{1,θ} gauge functions across levels, using S_E as reference (§4) | PROVEN-HERE |
| A4 | Lemma DW: a level-0 pure-gauge datum has dual N-price ≤ 2d|v′|L^{2−(2+θ)k} (§3) | PROVEN-HERE (al55_nec A7) |
| A5 | Lemma LC: covariant line currents are exactly cc_Z, N_Z ≤ L^{(3+θ)(k−l)}|v| (§3) | PROVEN-HERE (A1, A2) |
| A6 | Proposition NEC + Corollary NEC-E: t_*(Υ_E) ≥ |[z^c_{k−1}, v̂]|L^{(2+θ)k−6−θ}/(2d)·(1 + O(|z|)); every level-0-only alignment fails (A1) uniformly (§3) | PROVEN-HERE (A3-A6) |
| A7 | Prop. AX-SEAM: multiscale axial-in-blocks — seam identity; field half fails by L^{k−l−2} (cell seams, curvature part) / L^{k−l−4} (interior seams) (§5.2 + errata) | identity PROVEN-HERE (al55_ax X2); growth PROVEN-HERE for linear fields, exact at k = 3, 4 (X3′) |
| A8 | E_PL reproduces Π_1 and harmonic quadratics, not |y|²; places root point sources (§5.3) | PROVEN-HERE |
| A9 | Γ_PL's (P1′): C^{1,θ} stability of E_PL under iteration (§5.3) | **OPEN** (isolated question) |
| A10 | Lemma HC-1: Λ_HC is a hierarchical left inverse with nested restriction, smooth homogeneous step, level-local transpose (§5.4) | PROVEN-HERE (al55_hcg H1-H8, K1-K5) |
| A11 | (SUB): s3 reproduces Π_3 and is C^{1,β}, β ≥ 0.578 (§6.1) | CERTIFIED (al55_sub P1, P2); 5-adic 4-point scheme NOT certified (P3 FAIL) |
| A12 | Lemma DET: sup|μ_l| ≤ C_Dρ_{l+1}^{2+α}‖x_l‖_{C^{1,α}} (§6.1) | ARGUED (lattice Green's-function bounds cited) |
| A13 | Lemma HB: hierarchical reconstruction in C^{1,θ} (§6.1) | ARGUED-standard |
| A14 | Proposition P1′(HC): ‖Λ_HCx‖_𝒞 ≤ C_𝒞|||x|||_{1,♯}, k-, T-uniform, L = 3, θ ≤ 1/2 (§6.1) | ARGUED |
| A15 | Proposition P2-tw(HC): N_1(Λ_HC^Tτ_Z(y)) ≤ C_twηN_ℛ(y) (§6.2) | ARGUED (slot identities PROVEN-HERE) |
| A16 | (AC𝒞): the ♯ weight forces Hölder exponent θ on ∇μ (§4) | ARGUED (power count) |
| A17 | Theorem R2-glob♯: (R2) on 𝒞_glob ⟸ items 1-13 of §7 (§7) | PROVEN-HERE as a reduction; inputs as listed |
| A18 | weighted (e^{m·dist}) version of the alignment (§6.3 (v)) | OPEN |

### 10.2 Verdicts on prior claims (§8)
| id | claim (file, locating string) | verdict |
|---|---|---|
| F1a | BGT55 §6.4/§12 "S_E must not be used as the alignment" (conclusion) | CONFIRMED (new proof, §3) |
| F1b | BGT55 §6.4 "spikes ≍ 2dL^{3l}π_l" (mechanism/power count) | NOT-VERIFIED |
| F1c | BGT55 §6.4 "Λ_E^Td^Tj_0 =" (formula) | REFUTED (Codex §2; agree) |
| F2 | BGT55 §6.4 (β) "computed from x_l"; "(β) holds by construction" | REFUTED (Codex §6.3; agree, re-derived) |
| F3 | BGT55 §6.4 "(α) is exactly GSHARP55 §5.5's open hole" | CONFIRMED (open; sharpened) |
| F4 | BGT55 §6.5 "Theorem R2-glob … one OPEN input" | NOT-VERIFIED (agree Codex §6.4); replaced by A17 |
| F5a | BGT55 §12 3(d) "(or Balaban's axial-in-blocks gauge)" as the alignment | REFUTED (A7) |
| F5b | BGT55 §12 3(d) "the per-level slice functional Γ_PL" as the alignment | NOT-VERIFIED (A9) |
| F6 | BGT55 §6.3 "So the transfer must be run in the transport-weighted response norm" | NOT-VERIFIED as a necessity (agree Codex §6.1) |
| F7 | GSHARP55 §5.5 "O(ρ_i^{1+α}) … which is summable over levels" | NOT-VERIFIED |
| F8 | GSHARP55 §5.5 "The hole: how a level-i correction propagates …" | CONFIRMED |
| F9 | GSHARP55 §5.5 Lemma PL-adm | CONFIRMED (spot-check) |
| F10 | GSHARP55 §5.5 "No live consumer needs the transfer" | CONFIRMED (in its scope) |
| F11 | NLOC NL-9 (within-cell axial fails sup by L^k); NL-7 (global axial fails by T) | CONFIRMED in direction and extended (NL-9); spot-checked (NL-7) |
**Counts (§10.2): CONFIRMED 6 (F1a, F3, F8, F9, F10, F11), NOT-VERIFIED 5 (F1b, F4, F5b, F6, F7), REFUTED 3 (F1c, F2, F5a).**

### 10.3 Outcome against the PRE-STATED targets and refutation tests
- **T1** done: §2 (ALIGN-ℓ♯ with (P1)) and §4 (the sharper (P1′)); every quantifier, norm and the inequality each GA input consumes are in RED/RED′.
- **T2** done: §5 — S_E (source half fails), multiscale axial-in-blocks (field half fails; it avoids NLOC's factor T but reproduces NL-9's L^k at every
  level), Γ_PL (open question isolated), Λ_HC (new; algebra proved and checked).
- **T3**: for Λ_HC the regularity across levels, uniformly in k and T in the transport-weighted pair, is **reduced to DET + HB + certified (SUB)**
  (ARGUED); the exact Hölder exponent required (θ) is derived (§4); for Γ_PL the obstruction is isolated to one decidable number (§5.3).
- **T4** done: §7, Theorem R2-glob♯, every input named with its status.
- **R-a** (left inverse/alignment): tested exactly — al55_nec A3, al55_hcg H1/H2, al55_ax X1 — not refuted. **R-b** (completion growing with k): occurs
  for S_E (NEC-E, the S_E refutation) and on the field side for axial-in-blocks (AX-SEAM); for Λ_HC not found (transpose is level-local, H5;
  power counts §6.2). **R-c** (|||(Ξ_Z − Ξ_1)Λ_Wx|||_♯ ≥ f(k,T)η|||x|||): occurs for axial-in-blocks (seams); for Λ_HC excluded by P1′ + AC𝒞 (ARGUED).
  **R-d**: Λ_HC's dependence of λ_l on x_m (m > l) is through S^{(m→l)}μ_m with |μ_m| ≤ Cρ_{m+1}^{2+α} — geometric in coarse units; not refuted.
  **R-e**: Λ_HC constants depend on (L, s) only (ARGUED). **R-f**: S_E's completion is not used (S_E enters only as the banked reference
  representative); neither the refuted BCH factorisation, (GAP-Z), nor TRANSP is used.

## 11. For the lead — what changes

1. **(ALIGN-ℓ) restated so that it survives CODEX_REVIEW_BGT §6:** (H) hierarchical dependence + **(P1′) C^{1,θ} gauge functions across levels** +
   **(P2-tw) twisted-charge completion**, plus five slice-independent background estimates; Lemma RED′ (PROVEN-HERE) turns these into GA's
   (A1)-(A2) with explicit t_±, δ_Υ. A C^{1,α} slice representative (P1) is **not** needed; the regularity exponent GA needs is θ, not α.
2. **S_E is definitively out as GA's alignment** (Corollary NEC-E, PROVEN-HERE, exact check): t_*(Υ_E) grows like L^{(2+θ)k} at every background with a
   non-commuting level-(k−1) link, including small pure gauges. S_E stays in as the reference representative (banked EP-bd).
3. **Balaban/Dimock's multiscale axial-in-blocks is out as the alignment** (AX-SEAM): hierarchical (source half fine) but its seams fail the field half
   by L^{k−l−2}; consistent with Dimock §3.5 (regularity is done in Landau gauge, not axial).
4. **New candidate Λ_HC** (hierarchical Coulomb-detail gauge: smooth interpolatory subdivision of coarse values + a Coulomb detail at each level):
   algebra PROVEN-HERE and checked; field half ARGUED via DET + HB with the scheme input CERTIFIED for L = 3 (β ≥ 0.578 > θ = 1/2); source half
   ARGUED. **HANDOFF critical path for (R2) on 𝒞_glob:** rebuild DET's d = 4 lattice Green's-function bounds; write HB's constants; prove the
   completion bounds (A)-(B); re-derive (HD)'s term list from the true linearisation (Codex §6.2); then Codex-check RED′ + NEC + HC-1 first (short,
   algebraic), DET/HB second.
5. **Still OPEN:** Γ_PL's (P1′) (one number: amplification of root sources under E_PL); (SUB) for odd L ≠ 3; a weighted (exponentially local)
   alignment for BFT-3; (LOC-GA) outside 𝒞_glob; BFT-0's conditional inputs.
6. **Tally:** I did not read or change PROOF's tally; nothing here is proposed for banking before a Codex check.

Files written by this worker: ALIGN55.md (appended after the pre-existing first line and PRE-STATED block); checks/al55_nec_criteria.md,
al55_nec.py, al55_nec_out.txt, al55_nec_err.txt; checks/al55_sub_criteria.md, al55_sub.py, al55_sub_out.txt, al55_sub_err.txt,
al55_sub_err_run1.txt; checks/al55_hcg_criteria.md, al55_hcg.py, al55_hcg_out.txt, al55_hcg_err.txt; checks/al55_ax_criteria.md, al55_ax.py,
al55_ax_out.txt, al55_ax_err.txt. Scratch timing probe (not a check, outside the repository): scratchpad/al55/time_solve.py. No git command was run.
UTC end stamp: 2026-10-29T04:23:39Z

## 12. Errata found on the final read (append-only; content above unchanged)
- §6.1, Lemma DET proof (d): the shell-sum display "Σ_{|n|≤2L}|n|^{α−2}|n|^3/|n|" is garbled. Correct: Σ_{n∈Z^4, |n|≤2L}|n|^{−3}|n|^{1+α} ≍ ∫_1^{2L}r^{α−2}r^3dr
  ≍ L^{2+α}, and the far part L^4Σ_{|n|>2L}|n|^{−7}|n|^{1+α} ≍ L^4∫_{2L}^∞r^{α−3}dr ≍ L^{2+α}. The near-field kernel bound should read
  |K(y, b)| ≤ C(1 + |y − b|)^{−3} + CL^{−3} for |y − b| ≤ 2L (the S_0R part); its contribution is of the same order L^{2+α}. Conclusion unchanged.
- §4, Lemma RED′, invertibility: when (P1′) holds for all x (as Proposition P1′(HC) states), the direct bound ‖Λ_Wu‖_𝒞 ≤ C_𝒞|||u|||_{1,♯} suffices and
  the condition is C_𝒞C_ACη < 1 (as used in §7 item 13); the route through Λ_E (needing (E)'s ARGUED second half) is then unnecessary.
- §3, "Reading" (i): "the twisted charge of a level-(k−1) current of unit N-size is ≍ |z^c_{k−1}|L^{−(4+θ)}" is an own-unit upper size (π_{k−1}(j) ≤ L^{−θ},
  |j|_own ≤ L^{−3−θ}, |z_{k−1}|_own = L^{−1}|z^c|); the witness of Lemma LC attains it up to the factor |[ẑ, v̂]|.
UTC stamp of this block: see the last line.
UTC end stamp (final): 2026-10-29T04:24:28Z
