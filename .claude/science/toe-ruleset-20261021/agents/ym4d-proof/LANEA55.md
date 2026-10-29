Reviewer model: claude-opus-5-5

# LANEA55 — re-derivation of the lane-A hidden premise set under the [S26-BANKED] block (session 26, worker file)

UTC at start: 2026-10-29 05:54 UTC. Worker: Opus 5.5 (claude-opus-5-5), max reasoning. No git; this file and `checks/la55_*` only; append-only.

## PRE-STATED (written before any derivation; statements only)

**Targets.** The 16 on-chain R1 items of DICT55 §6.4 "Corrected counts" (LR-pot excluded as off the banked chain unless cheap):
FP (Corollary FP), Lemma Λ, LIN0, CO-upR + Lemma RH, BL-2 (b),(d), BL-C, BL-5 (a), BA-3, COF-size, PW-cc (residual estimates),
YH, W0 (steps 3-5), LE, LES-div (LINEAR_PACKAGE Lemma 3.2″), LES / J-str / N2-lin (LINEAR_PACKAGE Lemma 3.2, Lemma 3.1 (c), Thm 3.8),
LINEAR_PACKAGE Theorem 4.2(ii). Order of treatment: by the number of banked results resting on each (DICT55's "Used by" column
and §8.1), most-used first.

**For each item I will:** (1) locate statement + proof by string (grep, sed ranges); (2) fix which object every symbol denotes
in DICT55's pinned conventions (left gauge action, centred contours, u = 1/g², Hilbert–Schmidt norms, S_E slice / orbit norm);
(3) re-derive the load-bearing steps from primitives, every constant and every quantifier, in the form the banked consumer uses;
(4) give a verdict.

**What counts as each verdict.**
- CONFIRMED: I re-derived the statement in the form the consumer uses (constants may be weaker only if I say so and the consumer
  tolerates it; then the verdict is CONFIRMED with the corrected constant named).
- REFUTED: a constant, quantifier, norm, class or index in the printed statement is false as printed in the form a banked
  consumer uses it — shown by a derivation of the correct value or an explicit counterexample (exact arithmetic). A refutation of
  a printed constant that leaves every uniformity statement intact is still REFUTED (scoped: "constant only"), with the
  consumer impact named.
- NOT-VERIFIED: I could not close the derivation (named missing step), or the proof relies on an input outside this batch that
  I did not re-derive (named).
- A check that could not have failed does not count as evidence.

**Known in advance (to test, not to assume):** DICT55 §8.2 / Codex RLOC R11: BA-3's |q_p| ≤ 9 s_j² as justified gives 144 s_j².
I will re-derive the BCH remainder bound for a plaquette word directly and say which constant the cited argument certifies.

---

## §0. Read record and order of treatment (appended after PRE-STATED)

**Read (by string + sed ranges):** DICT55 §3, §4, §6.4, §7, §8.1-8.2, C1-C10; CODEX_REVIEW_DICT.md (at 05:54 UTC it held only its
PRE-STATED block, 23 lines, no findings — so no Codex verdict on DICT55 is available to me yet); LINEAR_PACKAGE §1-§4; PROOF_session16_snapshot
(the frozen ledger LINEAR_PACKAGE's "l.N" pointers resolve into) for J-str, LES, LES-div, Theorem 6.8; BFT_A §1, §7-§8, §12-§13,
§26, §28; BFT_B §16.2.

**Order.** Every R1 item feeds the same top of the chain (C2-COF/TOP-cc → K^(σ) → BFT-E → NSL → BFT-3/BFT-4 (a)), so "how many
banked results rest on it" is decided by how many *distinct* banked producers call it. Count (DICT55 "Used by" + the proofs I
read): LES-div (EP-rec, EP-int ⇒ GF-E/GV-E/NSL; W0 step 4 ⇒ COF/TOP-cc; NSL Lemma A) > BL-2 (K, EP-rec, W0, CO-upR, COF-size,
Λ, LR-pot) > BL-C (EP-rec, C2-COF, W0, CO-upR, C9's pointwise↔Campanato conversion) > LE, YH, W0 (COF and TOP-cc) > FP (+ its
inputs Λ, LR-pot) > BL-5 (a) > LIN0 > COF-size > PW-cc > CO-upR/RH > BA-3 > LES/J-str/N2-lin > LP Thm 4.2(ii). I treat them
bottom-up in that order (the first ones are inputs of the later ones), so a later CONFIRMED can cite an earlier section here.

**Convention note.** All 16 items except BA-3 live in Setting LIN (BFT_A §7.1: abelian linearisation at the trivial chain, one
real component of su(N) in an HS-orthonormal basis, C5). Gauge-action direction, u = 1/g² and contour centring do not enter
their statements; they enter only BA-3 (non-abelian BCH) and, through positions, the weight constants e^{c·m}.

---

## §1. LA36 — Lemma LES-div (LINEAR_PACKAGE Lemma 3.2″; proof PROOF_session16_snapshot "Lemma LES-div (lattice Campanato step, divergence-form source): PROVEN-HERE") — **CONFIRMED**

**Statement (as used).** u real on Z⁴, −Δu = Σ_a∂_a^−g_a + h on Q_R(x_0), R ≥ 16, Δ = Σ_ρ∂_ρ^−∂_ρ. With
ψ(x;ρ) := Σ_{Q_ρ(x)}|∇u − (∇u)_{Q_ρ(x)}|², [g]_{α;Q_R} the Campanato seminorm over sub-boxes of Q_R, H_0 := sup_{Q_R}|h|: for
x ∈ Q_{R/2}(x_0), 1 ≤ ρ ≤ R/4, ρ^{−4}ψ(x;ρ) ≤ C_α(ρ/R)^{2α}[R^{−4}ψ(x;R/4) + R^{2α}[g]² + R²H_0²], C_α absolute (d = 4, α).

**Re-derivation.** Fix x, ρ ≤ r ≤ R_1 := R/4; Q_r(x) ⊂ Q_R(x_0) since |x − x_0|_∞ ≤ R/4 and r/2 ≤ R/8 (3R/8 < R/2).
1. *Split.* u = w + v on Q_r(x): w = 0 off the interior, −Δw = Σ_a∂_a^−(g_a − ḡ_a) + h inside (ḡ := mean of g on Q_r; constants
   are killed by ∂^−). Testing with w (w vanishes off the interior, so summation by parts has no boundary term; (∂_a^−)^T = −∂_a):
   ‖∇w‖² = −Σ_a⟨g_a − ḡ_a, ∂_aw⟩ + ⟨h, w⟩ ≤ ‖g − ḡ‖_{2,Q_r}‖∇w‖ + ‖h‖_{2,Q_r}·C_Pr‖∇w‖ (Dirichlet Poincaré). So
   ‖∇w‖ ≤ ‖g − ḡ‖_{2,Q_r} + C_Pr‖h‖_{2,Q_r}, and by the definition of the Campanato seminorm (Σ_{Q_r}|g − ḡ|² ≤ r^{4+2α}[g]²) and
   ‖h‖²_{2,Q_r} ≤ r⁴H_0²: ‖∇w‖² ≤ 2r^{4+2α}[g]² + 2C_P²r⁶H_0².
2. *Harmonic part.* v is discrete-harmonic in the interior; Δ commutes with translations, so each ∂_av is harmonic on the box
   shrunk by one. LES step 3 (re-derived below) applied to ∂_av: Σ_{Q_ρ}|∇v − (∇v)_ρ|² ≤ A_0(ρ/r)⁶Σ_{Q_r}|∇v − (∇v)_r|² (ρ ≤ r/4;
   the shrink-by-one is absorbed for r ≥ r_* and the range r ≤ r_* is trivial once A ≥ r_*⁶, since ρ ≥ 1).
3. *One step.* Means minimise Σ|·−c|², so ψ(ρ) ≤ 2Σ_{Q_ρ}|∇v − (∇v)_ρ|² + 2‖∇w‖² and Σ_{Q_r}|∇v − (∇v)_r|² ≤ 2ψ(r) + 2‖∇w‖²:
   ψ(ρ) ≤ A(ρ/r)⁶ψ(r) + B(r^{4+2α}[g]² + r⁶H_0²), and r⁶H_0² ≤ R^{2−2α}r^{4+2α}H_0² (r ≤ R). ψ is nondecreasing in ρ (concentric
   boxes, means minimise).
4. *Iteration* (Giaquinta's lemma, LES step 5; a = 6 > b = 4 + 2α since α < 1): ψ(ρ) ≤ C(ρ/R_1)^{4+2α}[ψ(R_1) + R_1^{4+2α}([g]² +
   R^{2−2α}H_0²)]. Divide by ρ⁴ and use R_1 = R/4: ρ^{−4}ψ(ρ) ≤ C·4^{4+2α}(ρ/R)^{2α}[R^{−4}ψ(R/4) + R^{2α}[g]² + R²H_0²]. ∎
**LES step 3 (the only analytic input), re-derived.** For h harmonic on Q_r: Caccioppoli (test η²(h − c)) gives
Σ_{Q_s}|∇h|² ≤ C(s′ − s)^{−2}Σ_{Q_{s′}}|h − c|²; differences of harmonic functions are harmonic, so five nested applications bound
‖∂_S∂_eh‖_{2,Q_{r/4}} ≤ Cr^{−|S|−1}‖h − c‖_{2,Q_r} for |S| ≤ 4; the tensorised 1D bound |v(x)| ≤ m^{−1}Σ|v| + Σ|∂v| on a box of side m
gives sup_Q|v| ≤ Σ_{S⊆{1..4}}m^{|S|−4}Σ_Q|∂_Sv| ≤ Σ_Sm^{|S|−2}‖∂_Sv‖_2 (Cauchy–Schwarz), so sup_{Q_{r/4}}|∇h| ≤ Cr^{−3}‖h − h̄_r‖_2,
and Σ_{Q_ρ}|h − h̄_ρ|² ≤ ρ⁴(4ρ·sup|∇h|)² ≤ C(ρ/r)⁶Σ_{Q_r}|h − h̄_r|². All constants depend on d = 4 only.

**Consumers checked against this form.** W0 step 4 (BFT_A §28.5: g = G_0 componentwise, h = j_0 − κ_{k−1}(Q_str^{(0→k)})^Tr_{k−1},
R = n, any centre, periodic lift) and EP-int (BFT_B §16.2 Step 3: h = 0, R = n/4, with the small-k cases L^k < 64 handled as
finitely many fixed linear maps) use exactly this statement. The unit conversion in W0 step 4 (n^{2+α}·n^{−α}·n^{−2} = 1 on the
energy term, n^{2+α}[G_0]_{α;fine} = [G^c_0]_α, n^{2+α}n^{1−α}·n^{−3} = 1 on h) I re-did: correct.

**Verdict: CONFIRMED** (constants absolute, uncomputed — as stated; no numerical threshold in the banked block uses C_α).

---

## §2. LA19 — Lemma BL-2 (BFT_A "**Lemma BL-2 (coarse-unit sizes of the chain maps).**", proof §8.2) — **CONFIRMED** (all five parts)

Objects: level-l torus in own units; level-(l+1) site X ↔ block B(X) = LX + {0..L−1}⁴, root c_X = LX + o, o = (L−1)/2; S4′
contour T^σ_y = P^σ(c_X→y)·S_y·P^σ(c_Y→y+Le_μ)^†, Y = X + e_μ, y ∈ B(X); Q_root = avg_{σ,y}∫_{T^σ_y}; h(A)(X) = avg_{σ,y}∫_{P^σ(c_X→y)}A.
- **Root identity Q = Q_str − d∘h, re-derived.** ∫_{T^σ_y} = ∫_{P^σ(c_X→y)} + ∫_{S_y} − ∫_{P^σ(c_Y→y+Le_μ)}; as y runs over B(X),
  y′ = y + Le_μ runs over B(Y) with the same σ, so the average of the third term is h(A)(Y). Hence Q_root A(X,μ) = Q_strA(X,μ) −
  (h(A)(X+e_μ) − h(A)(X)). Root covariance Q(dλ) = d(ev λ): every T^σ_y runs c_X → c_Y.
- **(a)** |Q_strv(X,μ)| = |L^{−4}Σ_{y∈B(X)}Σ_{j<L}v_μ(y+je_μ)| ≤ L‖v‖_own; coarse units L^{k−l−1}·L‖v‖_own = ‖v^c‖. Contractions compose. ✓
- **(b)** Induction: Q_bQ^{(a→b)} = (Q_{str,b} − dh_b)Q_str^{(a→b)} − Q_b d h^{(a→b)} = Q_str^{(a→b+1)} − d(h_bQ_str^{(a→b)} + ev∘h^{(a→b)}),
  unrolling to h^{(a→b)} = Σ_{i=a}^{b−1}ev^{(i+1→b)}h_iQ_str^{(a→i)}. |h_i(w)| ≤ max_y|y − c_X|_1·‖w‖_own = 4·(L−1)/2·‖w‖ = 2(L−1)‖w‖;
  ‖Q_str^{(a→i)}v‖_own ≤ L^{i−a}‖v‖_own; Σ_{i=a}^{b−1}2(L−1)L^{i−a} = 2(L^{b−a} − 1). |d h v| ≤ 2·2(L^{b−a}−1)‖v‖ < 4L^{b−a}‖v‖_own =
  4‖v^c‖ in level-b coarse units (L^{k−b}·L^{b−a} = L^{k−a}); with (a): ≤ 5‖v^c‖. Constants: ∫_T ae_μ = a·(c_Y − c_X)_μ = aLδ_{μν};
  h_l(ae_μ) = a·avg_{y∈B(X)}(y − c_X)_μ = 0 (L odd, centred block). ✓
- **(c)** Q^T = Q_str^T − h^Td*, so Q^T = Q_str^T on co-closed currents; d*Q^T = (Qd)^T = (d ev)^T = ev^Td*, so co-closedness is
  preserved. (Q_str^Tj)(z,μ) = L^{−4}Σ_{i<L}j(X(z − ie_μ),μ) (for each i exactly one block contains z − ie_μ): |·| ≤ L^{−3}‖j‖, equality on
  constants; plain coarse units L^{3(k−l)}L^{−3} = L^{3(k−l−1)}. ✓
- **(d)** dQ_str A(P) for the coarse plaquette P = (X;a,b) is L^{−4}Σ_{y∈B(X)} (circulation of A around the L×L square at y), so
  𝒬H(P) = L^{−4}Σ_{y∈B(X)}Σ_{s,t<L}H(y+se_a+te_b;a,b): L⁶ terms, and in 2-form coarse units (𝒬H)^c = L^{2(k−l−1)}L^{−4}L^{−2(k−l)}ΣH^c =
  L^{−6}ΣH^c — a probability average over same-orientation plaquettes with base points in X + [0, 2 − 2/L] (plane directions, level-(l+1)
  units) × [0, 1 − 1/L] (others). Composite offsets: (2 − 2/L)ρ_bΣ_{m≥0}L^{−m} = 2ρ_b < 3ρ_b. ✓ Transpose: (𝒬^TH′)^c(z) = avg_{s,t<L}H′^c(X(z −
  se_a − te_b)) (L^{2(k−l)}·L^{−4}·L^{−2(k−l−1)}·L² terms), a contraction. ✓
- **(e)** (dv)_p is a signed sum of 4 links: |(dv)^c| ≤ 4L^{2(k−j)}‖v‖_own = 4L^{k−j}‖v^c‖; ∇^c = L^{k−j}×(one difference) ⇒ 2L^{k−j}‖v^c‖;
  Osc_2(H;B) ≤ (avg_B|H|²)^{1/2} ≤ ‖H‖_∞ and ρ ≥ ρ_j ⇒ [H]_α ≤ ρ_j^{−α}‖H‖_∞. ✓

**Verdict: CONFIRMED** as printed (every constant: 2(L^{b−a} − 1), 5, L^{−3}, 3ρ_b, 4L^{k−j}, 2L^{k−j}, ρ_j^{−α}). The composite average
𝒜^{(0→j)} that W0 step 5 / CO-upR / Proposition W use is (d) iterated; it commutes with level-j translations (each 𝒬 commutes with
level-(l+1) translations), which is what makes [𝒜f_0]^∞_α ≤ [f_0]^∞_α in those proofs.

---

## §3. LA20 — Lemma BL-C (BFT_A "**Lemma BL-C (lattice Campanato ⇒ pointwise Hölder).**", proof §8.4) — **CONFIRMED**

**Statement.** For every level-j form H (coarse units, components separately): [H]^∞_α ≤ C_C[H]_α + 2·8^α‖H‖_∞,
C_C := 2^α(8·2^α/(2^α − 1) + 32·4^α). Campanato over boxes of side ρ ∈ ρ_jZ, ρ_j ≤ ρ ≤ 1 (BFT_A §7.2); pointwise over z ≠ z′,
|z − z′|_∞ ≤ 1 (torus distance).

**Re-derivation.** ε := ρ_j, δ := |z − z′|_∞ ≥ ε (distinct level-j base points).
- δ ∈ (1/8, 1]: |H(z) − H(z′)| ≤ 2‖H‖_∞ < 2(8δ)^α‖H‖_∞. ✓ (This also covers every pair when ε > 1/8.)
- δ ∈ [ε, 1/8]: dyadic boxes D_i(z) of side 2^iε (computed in the Z⁴ lift with z′ the lift at torus distance; sides ≤ 1 ≤ T, so they
  project to legal torus boxes), D_0 = {z}, |D_{i+1}| = 16|D_i|. For D ⊂ B: |m_D − m_B| ≤ (avg_D|H − m_B|²)^{1/2} ≤ (|B|/|D|)^{1/2}Osc_2(H;B).
  So |m_{D_i} − m_{D_{i+1}}| ≤ 4[H]_α(2^{i+1}ε)^α, and |H(z) − m_{D_I(z)}| ≤ 4[H]_αε^αΣ_{i=1}^{I}2^{iα} ≤ 4[H]_α(2^Iε)^α·2^α/(2^α − 1).
  I := least i ≥ 0 with 2^iε ≥ δ. Corners of D_I(z), D_I(z′) differ by < δ + 2^Iε ≤ 2^{I+1}ε per coordinate, so both boxes lie in one box
  B* of side 2^{I+2}ε (span ≤ 3·2^Iε); B* is legal: if I ≥ 1, 2^{I−1}ε < δ ⇒ 2^{I+2}ε < 8δ ≤ 1; if I = 0, 4ε ≤ 4δ ≤ 1/2.
  |m_{D_I(z)} − m_{D_I(z′)}| ≤ 2·(4⁴)^{1/2}[H]_α(2^{I+2}ε)^α = 32·4^α[H]_α(2^Iε)^α. Sum: |H(z) − H(z′)| ≤ [H]_α(2^Iε)^α(8·2^α/(2^α−1) +
  32·4^α), and (2^Iε)^α ≤ (2δ)^α (I ≥ 1: 2^Iε < 2δ; I = 0: ε ≤ δ). Hence ≤ C_C[H]_αδ^α with C_C exactly as printed. ∎
- Reverse (C9's other direction): Osc_2(H;B) ≤ sup_{z∈B}|H(z) − H(z_B)| ≤ ρ^α[H]^∞_α. ✓
- Weighted form (Proposition W's "e^{8m}"): every box used lies within ℓ^∞-distance 1 of z (ℓ¹ ≤ 4), so the weighted constant
  e^{8m}(C_C[H]_{α,m} + 2·8^α‖H‖_{∞,m}) is valid (e^{4m} would do). ✓

**Verdict: CONFIRMED**, constant exactly as printed. (Agrees with DICT55 §8.1's R2 re-classification of BL-C via Codex RLOC's
"two successive dyadic means differ by at most 4 Osc_2"; I re-derived it independently of that text.)

---

## §4. LA34 (LE part) — Lemma LE (BFT_A "**Lemma LE (local energy from the sup).**", proof §28.3) — **CONFIRMED** (with its kernel input Lemma TK re-derived)

**Statement (with §28's dated precision 2: every centre x).** For every exact level-0 2-form F on the torus of side Tn (T ≥ 1):
E_∇(F;x)^{1/2} ≤ C_E sup|n²F|, C_E := √192 + 10⁴C_K, where E_∇(F;x) = n^{−4}Σ_{z∈Q_{n/4}(x)}|n²(∇B − ⟨∇B⟩_Q)|², B := d*Δ_0^{−1}F.

**Kernel input re-derived (Lemma TK, BFT_A §18.1, as used: (K0) the torus kernel K of ∇d*Δ^{−1}, symbol entries ν_aν̄_μ/ψ, order
a = 0; |DK(z)| ≤ C_K(1 + |z|_M)^{−5}, C_K independent of the torus side M).** Littlewood–Paley: σ = Σ_{j≥−1}σψ_j with σ_j supported
in |p| ~ 2^{−j}, |∂^βσ_j| ≤ C2^{j(a+|β|)}; N-fold integration by parts in one coordinate gives |k_j(z)| ≤ C2^{j(a−4)}(1 + 2^{−j}|z|)^{−N}
(annulus volume 2^{−4j}); finite Poisson summation K_M(z) = Σ_jΣ_{n∈Z⁴}k_j(z + nM) with only 2^j ≤ M/π present (σ_j vanishes on the
grid otherwise) and p = 0 excluded (σ_j(0) = 0); for |z|_∞ ≤ M/2 and n ≠ 0, |z + nM| ≥ |n|M/2, so the image sum costs a constant
(Σ_{n≠0}|n|^{−5} < ∞ in Z⁴) and |Σ_nk_j(z+nM)| ≤ C2^{j(a−4)}(1 + 2^{−j}|z|)^{−6}; summing j: Σ_{2^j≤r}2^{j(a+2)}r^{−6} + Σ_{2^j>r}2^{j(a−4)} ≤ Cr^{a−4}
(needs −2 < a < 4). A lattice difference multiplies the symbol by e^{ip_e} − 1, lowering a by one (a = −1 > −2 for DK_0). ✓ (C_K is
finite and uncomputed, as the source says.)

**Re-derivation of LE.** Q := Q_{n/4}(x), Q* := {|z − x|_∞ < n}, F = F_1 + F_2, F_1 := 1_{Q*}F; K kills constants (d* does), so KF =
K(F_1 − mean) + K(F_2 − mean).
- *Near.* (KH)^_{aν} = ν_aΣ_μν̄_μĤ_{μν}/ψ; Cauchy–Schwarz |Σ_μν̄_μĤ_{μν}|² ≤ ψΣ_μ|Ĥ_{μν}|², so Σ_{a,ν}|(KH)^|² ≤ Σ_νΣ_μ|Ĥ_{μν}|² = 2Σ_P|Ĥ_P|²:
  ‖KH‖_2 ≤ √2‖H‖_2. Σ_Q|KF_1 − ⟨KF_1⟩|² ≤ 2·6·|Q*|·sup|F|² ≤ 2·6·(2n)⁴sup|F|² = 192n⁴sup|F|² (also when Q* is the whole torus, T ≤ 2).
- *Far.* w ∈ Q, y ∉ Q* ⇒ |w − y|_∞ ≥ |y − x|_∞ − n/8 ≥ (7/8)|y − x|_∞. Each output entry (a,ν) of KF_2 involves the 3 orientations
  (μ,ν), μ ≠ ν. Points of Q are joined by ≤ n unit steps inside Q. With the exact shell count #{|y − x|_∞ = t} = (2t+1)⁴ − (2t−1)⁴ =
  64t³ + 16t ≤ 80t³ and Σ_{t≥n}t^{−2} ≤ 2/n: per entry |KF_2(w) − KF_2(w′)| ≤ n·3C_K(8/7)⁵·80·(2/n)sup|F|, and over the 16 entries
  (Euclidean) ≤ 4·3·80·2·(8/7)⁵C_K sup|F| = (62914560/16807)C_K sup|F| < 3744C_K sup|F| ≤ 10⁴C_K sup|F| (exact rational; check
  la55_1 below). The source's own count (6 orientations, 216t³ shells, no factor 4) gives 2592·(8/7)⁵ < 5054; either way ≤ 10⁴.
- *Assembly.* E_∇ = Σ_Q|∇B − ⟨∇B⟩|² (the n⁴ cancels); Minkowski: E_∇^{1/2} ≤ √192·n²sup|F| + |Q|^{1/2}·10⁴C_K sup|F| ≤ (√192 +
  10⁴C_K/16)sup|n²F|. ∎ No chain enters (a property of exact level-0 2-forms).

**Verdict: CONFIRMED** with C_E = √192 + 10⁴C_K (my count even gives the far coefficient 10⁴/16). Note on symbols: this C_K is
TK's (K0) constant; DICT55's collision list (≥ 13 C_1, …) does not include C_K, and within BFT_A §18-§28 C_K always names TK's
constant (checked by grep of "C_K" in §18.1, §23.4, §28.3, §28.4).

---

**Check la55_1** (criteria `checks/la55_1_criteria.md` written 06:08:51 UTC before `checks/la55_1_constants.py`; output
`checks/la55_1_out.txt`): C1-C7 PASS, the designed-FAIL control FAILs as designed (exit 0). Exact values: 4·3·80·2·(8/7)⁵ =
62914560/16807; 2592·(8/7)⁵ = 84934656/16807; 48·(41/20)⁵ = 347568603/200000 ≤ 1738; 775 + 205·3/2 = 2165/2 ≤ 1083.

---

## §5. LA14 — Lemma Λ (BFT_A "**Lemma Λ (root-to-root holonomy).**", proof §13.11) — **CONFIRMED**, C_Λ = 10

**Statement.** Λ(X,μ) := Σ_{0≤t<n}x_{0,μ}(c_X + te_μ) (straight level-0 sum between the level-0 roots c_X, c_X + ne_μ). For every
configuration: |Λ(X,μ) − (Q^{(0→k)}x_0)(X,μ)| ≤ 10·sup_{B(X)∪B(X+e_μ)}|f_0|, and |Λ| ≤ ‖B_k‖_D + 5Σ_i‖r^c_i‖ + 10‖f_0‖.

**Re-derivation.** Λ_i(Y,ν) := straight level-0 sum from the level-0 root of the level-i site Y to that of Y + e_ν (they differ by L^ie_ν;
the level-0 root of a level-(i+1) site Z equals the level-0 root of its central level-i site c_Z, since L is odd). (Q_iΛ_i)(Z,μ) =
avg_{σ,y} of the level-0 sum along the *assembled* path of T^σ_y (each level-i link replaced by its straight level-0 segment; consecutive
segments share endpoints). The assembled path and the straight segment of Λ_{i+1}(Z,μ) have the same endpoints; their difference is
the circulation around the assembly of the level-i loop T^σ_y ∘ (straight leg)^{−1}, which bounds the ruled surface {γ + te_μ : 0 ≤ t ≤ L}
(γ = P^σ(c_Z→y), the return path is γ + Le_μ for the same σ). Steps of γ along e_μ sweep degenerate (zero) cells — the four segments
cancel as chains — so the surface has ≤ |γ|·L ≤ 2(L−1)L level-i plaquettes, each assembling to a flat level-0 square of L^{2i}
plaquettes: |Λ_{i+1} − Q_iΛ_i| ≤ 2L(L−1)L^{2i}s_0, s_0 := sup|dx_0|. Telescoping Λ_k − Q^{(0→k)}Λ_0 = Σ_{i<k}Q^{(i+1→k)}(Λ_{i+1} − Q_iΛ_i)
with |Q^{(i+1→k)}v| ≤ 5L^{k−1−i}‖v‖_own (§2 (b) in own units) gives |Λ − Q^{(0→k)}x_0| ≤ 10L(L−1)s_0Σ_{i<k}L^{k−1+i} =
10L^k(L^k − 1)s_0 < 10n²s_0 = 10‖f_0‖_∞ (la55_1 C7 checks the sum for L ≤ 9, k ≤ 12; the closed form is exact for all L, k). Every
contour of Q^{(0→k)}(X,μ) and every swept surface lies in B(X) ∪ B(X+e_μ), so the sup localises. Corollary: BL-1 (iii)'s telescoping
B_k = Q^{(0→k)}x_0 − Σ_iQ^{(i+1→k)}r_i and §2 (b) give |Q^{(0→k)}x_0| ≤ |B_k| + 5Σ_i‖r^c_i‖. ∎

**Verdict: CONFIRMED** (C_Λ = 10 exactly as printed, k-free; BA3-F6 indeed does not occur). Agrees with DICT55 §8.1's R2
re-classification (Codex GSHARP's H_i root-line sums); derived here independently.

---

## §6. LA12 — Corollary FP (BFT_A "**Corollary FP (potential half of (G♯_0-field^∇)_m).**", proof §13.13), with its inputs LR-pot (LA15) and Theorem W — **CONFIRMED** (given the banked Proposition W)

**Statement.** T ≥ 3, 0 ≤ m < m_*′: for data and residual-type sources the minimiser in S_tent obeys max_j‖x^c_j‖_{∞,m} ≤
e^{20m}(1083‖x‖_{inv,m} + 40‖B_k‖_{D,m}) ≤ e^{20m}((1083G_D(m) + 40)‖B_k‖_{D,m} + 1083G_R(m)‖s‖_{R,m}), uniformly in k, T, X_0.
FP rests on Lemma LR-pot (so LR-pot is *on* the banked chain wherever FP is: K^(σ)'s TOP♯ (DICT55 §7 A2), W0 step 3, YH steps 3-4,
PW-cc) — DICT55 §6.4's "LR-pot leaves the premise set" is true only for the S_E/EP-rec route, not for FP's consumers. I re-derived it.

**LR-pot re-derived (BFT_A §13.12; tents χ_X = Π_ν max(0, 1 − |z_ν − c_{X,ν}|/n), λ_X(z) = −avg_σ∫_{a^σ(c_X→z)}x_0 on N_X, λ := Σ_Xχ_Xλ_X,
P = composite gauge transform by λ_0 = λ).**
- *Slice.* Σ_Xχ_X ≡ 1 (product of 1D hats of spacing n); χ_X(c_Y) = δ_{XY}, λ_X(c_X) = 0 ⇒ λ vanishes on every level-k root, so
  x ↦ x + (dλ, d ev λ, …) fixes x_k and all residuals (Q∘d = d∘ev). λ_X(Px) = λ_X(x) − λ (λ(c_X) = 0) ⇒ λ(Px) = λ − λ = 0: P² = P. ✓
- *Level 0.* d(χλ)(b) = χ(z+e_μ)dλ(b) + λ(z)dχ(b) and Σχ = 1 give (Px)_0(b) = Σ_Xχ_X(z+e_μ)[x_0(b) + dλ_X(b)] + Σ_Xλ_X(z)dχ_X(b).
  First sum: for each σ the two axial paths to z and z+e_μ agree before coordinate μ and run parallel afterwards; the loop bounds
  ≤ Σ_{ν after μ}|z_ν − c_{X,ν}| ≤ 3n plaquettes: ≤ 3ns_0. Second sum: Σ_Xdχ_X(b) = 0 ⇒ = Σ_X(λ_X − λ_*)(z)dχ_X(b) with χ_*(z) > 0;
  every X with dχ_X(b) ≠ 0 has X − X_* ∈ {−1,0,1}⁴ (I checked the boundary case X_μ − X_{*,μ} = 2: it forces z_μ − c_{*,μ} ≥ n,
  contradicting χ_*(z) > 0); Σ_X|dχ_X(b)| = Σ_{X_μ}|Δhat| ≤ 2/n (transverse hats sum to 1). λ_X − λ_* = ∫_π x_0 − (circulation of a
  closed loop of length ≤ 12n lying within ℓ^∞-distance n of c_X); the loop's circulation is ≤ 12n·3ns_0 = 36n²s_0 (write each link
  as x_0(b′) + dλ^σ_X(b′) − dλ^σ_X(b′): the dλ terms telescope around the loop, each bracket ≤ 3ns_0); ∫_π x_0 = Σ ≤ 4 terms ±Λ.
  Total |(Px)_0(b)| ≤ 3ns_0 + (2/n)(36n²s_0 + 4max|Λ|) = 75ns_0 + 8max|Λ|/n; coarse units ×n: ≤ 75‖f_0‖ + 8max|Λ| ≤ 155‖f_0‖ +
  8‖B_k‖_D + 40Σ_i‖r^c_i‖ (§5). ✓
- *Levels j ≥ 1:* (Px)_j = Q^{(0→j)}(Px)_0 − Σ_{i<j}Q^{(i+1→j)}r_i, so ×5 and +5Σ‖r^c‖: 775, 40, 205. ✓ (la55_1 C6.)
- *Weights e^{20m}:* at level 0 every input for b lies within ℓ^∞-distance ≤ 3 coarse of b (N_X, loops, the π segments and the
  B(X″) ∪ B(X″+e_ν) supports of their Λ bounds), i.e. ℓ¹ ≤ 12; Q^{(0→j)} adds ≤ 8. ✓

**Theorem W re-derived (BFT_A §13.10).** BL-1 (i) (re-derived: (κ_l/2)‖r‖² − ⟨s_l,r⟩ = (κ_l/2)‖r − σ_l‖² − ‖s_l‖²/(2κ_l), and
r_l(y − τ) − σ_l = r_l(y) by τ_{l+1} := Q_lτ_l + σ_l) gives x = y − τ mod gauge with y the source-free minimiser at datum B_k + τ_k;
BL-3 (re-derived: ‖σ^c_i‖ ≤ L^{−θ(k−i)}L^{−(k−1−i)}‖s‖_R/κ_−, Σ_{m≥0}L^{−θ}L^{−(1+θ)(k−j+m)} ≤ L^{−θ}L^{−(1+θ)(k−j)}L/(L−1), so ‖τ^c_j‖ ≤
c_1L^{−θ}L^{−(1+θ)(k−j)}‖s‖_R, c_1 = 5L/((L−1)κ_−); ‖τ‖_inv ≤ (8c_1 + 1/κ_−)‖s‖_R for α ≤ θ). Weighted: with the tight supports
(a level-j link's composite root map draws within ℓ¹ ≤ 5ρ_j; a plaquette's links within 2ρ_j; a Campanato box costs e^{4m}) every
j < k term is ≤ e^{(4 + 7/3)m} ≤ e^{12m}, so G_R(m) = e^{8m}c_1G_D(m) + 8c_1e^{12m} + 1/κ_− is valid as printed (I first suspected a
missing e^{4m} on the Campanato term; with the tight supports it is not missing). Input left as named: **Proposition W**
(G_D(m) = e^{20m}G_D♭), which is banked (DICT55 §8.1: B12 ⊃ CODEX_REVIEW_COFM item 4). ✓

**FP assembly.** ‖x‖_{inv,m} ≥ L^{k−1−i}‖r^c_i‖_{∞,m} ⇒ Σ_i‖r^c_i‖ ≤ (L/(L−1))‖x‖_{inv,m} ≤ (3/2)‖x‖_{inv,m}; ‖f_0‖ ≤ ‖x‖_inv; 775 + 205·3/2 =
2165/2 ≤ 1083. Then Theorem W. ∎

**Consumer match (DICT55 §7 A2, re-checked):** TOP♯ uses FP for the source-free tent-slice minimiser with datum δ_b/κ_{k−1}, weights
centred at b, 0 < m_w < m_*′, T ≥ 3: inside FP's quantifiers (every X_0, 0 ≤ m < m_*′); ‖δ_b/κ_{k−1}‖_{D,m} = 1/κ_{k−1} ≤ 1/κ_−. ✓
T ≤ 2 consumers (W0 step 3, YH Case B) use the periodic lift to T′ = 3T (re-checked in §8: P commutes with coarse translations, so
P(lift) descends).

**Verdict: CONFIRMED** (FP and LR-pot, constants 3, 72, 75, 155, 8, 40, 775, 205, 1083, c_0 = 20 as printed), conditional only on
the banked Proposition W.

---

## §7. LA31 — Theorem YH (BFT_A "**Theorem YH (level-0 dual bounds).**", proof §28.4) — **CONFIRMED** as an implication (given the banked Proposition W; every other step re-derived here)

**Statement.** 𝒬_H* := sup_p sup{|Σ_qG^c(q)dY^p_0(q)| : ‖G^c‖_∞ + [G^c]^∞_α ≤ 1} ≤ C_YH and 𝒩* := sup_p min_λ‖Y^p_0 + dλ‖_1 ≤ C_YN·n,
uniformly in k ≥ 1, T ≥ 1 (Y^p = response to the level-0 divergence-form source δ_p, B_k = 0).

**Load-bearing steps, re-derived.**
1. *Lemma LD (exact decomposition).* g_0 := d*(χω^p), ω^p := Δ^{−1}(δ_p − h_p): d*dg_0 = Δg_0 = d*(χΔω^p + [Δ,χ]ω^p) = d*δ_p − d*G′ with
   G′ := χh_p − [Δ,χ]ω^p (χ(p) = 1). With g_j := Q^{(0→j)}g_0 (all residuals of g vanish) and Y = g + Z, Z_k = β := −Q^{(0→k)}g_0: the level-0
   terms become ½‖dZ_0‖² − ⟨G′, dZ_0⟩ + const, so Y^p = g + Z mod gauge. J := 𝔽^{(0→k)}d*G′ is co-closed (net flux out of a block =
   total divergence inside = 0), so (Q^{(0→k)})^TJ = (Q_str^{(0→k)})^TJ (§2 (c)); BL-1 (iii) turns ⟨(Q^{(0→k)})^TJ, Z_0⟩ into ⟨J,β⟩ +
   residual sources s_i = (Q^{(i+1→k)})^TJ; the rest e := d*G′ − (Q_str^{(0→k)})^TJ is co-closed and equals d*G_e (Lemma PC), whose
   response is Σ_qG_e(q)Y^q by linearity. ✓
2. *Lemma PC* (cube of side q, no wrap): induction on dimension with G_{aν} := −S_ν + 1[z_a ≥ b]W_ν (S = partial sums along axis a,
   W = total transverse flux); (d*G)_ν = e_ν for ν ≠ a, (d*G)_a = e_a by co-closedness (with [RBA5-fix] U2's sign); e_a vanishes for
   z_a ≥ b (co-closedness + compact support), so supp G ⊂ C; Σ|G| ≤ (d − 1)qΣ|e| = 3qΣ|e|. ✓
3. *The contraction ([RBA5-fix] U4′).* (Q_str^{(0→k)})^T𝔽^{(0→k)}j′(b) = n^{−4}Σ_{t<n}(face sums of n³ links) — a probability average of
   j′ over n⁴ links within ℓ¹ distance 4n of b — so |e| ≤ 4n·sup|Dj′| ≤ 4nC_jr^{−6}; supp e in a cube of side q ≤ 2r + 8n + 5 ≤ 2.05r
   when L^c ≥ 260 (r = L^cn); Σ|G_e| ≤ 3q·4q⁴·4nC_jr^{−6} = 48(q/r)⁵C_jL^{−c} ≤ (347568603/200000)C_jL^{−c} ≤ 1738C_jL^{−c} (la55_1 C5),
   ≤ ½ for L^c ≥ max(260, 3476C_j). C_j = 12C_G with |D^iG′| ≤ C_Gr^{−4−i} (Leibniz: |D^iω^p| ≤ C_K(1+|z|)^{−2−i}, |D^iχ| ≤ 2·4^iC_φr^{−i},
   and on supp Dχ, |z − p| ≍ r). ✓
4. *𝒬_H(g), the constant subtraction (Case A step 1).* For ‖G^c‖ + [G^c]^∞_α ≤ 1 put Ḡ_P := G^c_P(z_p) (constant per plane): Σ_qḠ(q)dg_0(q) =
   ⟨d*Ḡ, g_0⟩ = 0. |G^c(q) − Ḡ(q)| ≤ (d_q/n)^α (d_q ≤ n), ≤ 2 otherwise, and = 0 at d_q = 0; |dg_0| ≤ C_d(1+|z−p|)^{−4}, zero beyond r + 2.
   With ≤ 6·216(1+t)³ plaquettes at ℓ^∞-distance t: |ΣG^cdg_0| ≤ 1296C_d[n^{−α}Σ_{t=1}^{n}t^{α−1} + 2Σ_{n<t≤r+2}(1+t)^{−1}] ≤
   1296C_d[(1 + 1/α) + 2(c ln L + 1)] (n^{−α}Σ_{t≤n}t^{α−1} ≤ n^{−α}(1 + n^α/α)). No log n: the k-uniformity is real. ✓
5. *𝒬_H(Z′), 𝒩(Z′) (screened part).* Theorem W at weight m′ = m_*′/3 centred at p's cell, with ‖β_str‖_{D,m′} ≤ C_βe^{4m′(L^c+2)}n^{−2}
   (|Q_str^{(0→k)}v| ≤ n^{−3}Σ over its 2n⁴-link tube; Σ_{|z|≲2n}(1+|z|)^{−3} = O(n)) and ‖s‖_{R,m′} ≤ L^θ|J|e^{4m′(L^c+4)}, |J| ≤ n³·6C_Gr^{−5} =
   6C_GL^{−5c}n^{−2} (ω^R_iL^{2(k−1−i)}L^{−3(k−1−i)} = L^θL^{−(1−θ)(k−1−i)} ≤ L^θ). Sums over level-0 objects: Σ_{z}e^{−m′|z/n − t|} ≤ coth(m′/(2n)) ≤
   n·coth(m′/2) (u·coth u increasing), so Σ_q e^{−m′d(q,p)} ≤ 6n⁴S(m′) with no cell-offset factor. Gives 𝒬_H(Z′) ≤ 6C_Z(c)S(m′) and, via
   FP (§6) on the gauge-equivalent Z′_str, 𝒩(Z′) ≤ ‖(PZ′_str)_0‖_1 ≤ 4C_FP(m′)C_N(c)S(m′)n. ✓
6. *𝒩(g)* ≤ ‖g_0‖_1 ≤ 4·216C_0′(r + 2) ≤ 1728C_0′L^cn. *Closing:* 𝒬_H, 𝒩 are seminorms invariant under composite gauge, so
   𝒬_H(Y^p) ≤ 𝒬_H(g) + 𝒬_H(Z′) + Σ|G_e|·𝒬_H* and likewise 𝒩; both sups are finite at fixed (k,T); take sup_p and absorb ½. ✓
7. *Case B (T < 8L^c):* r = ∞, G′ = e = 0; the same subtraction over the whole torus (diameter < 4L^cn) gives a log of L^c only;
   𝒬_H(Z) ≤ n^{−2}·6T⁴n⁴·G_DC_βn^{−2} ≤ 6(8L^c)⁴G_DC_β; 𝒩(Z) ≤ 4T⁴n⁴·n^{−3}(1083G_D + 40)C_β (FP at m = 0); T ≤ 2 via the lift to 3T,
   whose tent projection commutes with the period shifts, so it descends with the same pointwise bound. ✓

**Inputs not re-derived here:** Proposition W (banked) and, through it, LINEAR_PACKAGE's kernel constants M, M_f, C_α (§15-§16 below);
Lemma TK's C_K (re-derived in outline in §4). The constants are k-, T-uniform but astronomically large (e^{O(m′L^c)}, L^c ≥ 3476C_j,
C_j uncomputed) — exactly as [RBA5-fix] U4 says; no banked threshold uses their size.

**Verdict: CONFIRMED** (as an implication from the banked Proposition W; uniformity in k, T re-derived; constants uncomputed as stated).

---

## §8. LA32 — Theorem W0 (BFT_A "**Theorem W0 ((G♯_0-lev0) at m = 0, trivial background, Setting LIN).**", proof §28.5) — **CONFIRMED** (given the banked Proposition W)

**Statement.** Level-0 sources G_0 (2-form) and j_0 (d*j_0 = 0), B_k = 0, every 0 < α < 1, uniformly in k, T:
‖f_0‖_∞ ≤ C_YH(‖G^c_0‖ + [G^c_0]^∞_α) + C_YN‖j^c_0‖, and ‖x‖_inv ≤ C_W0(‖G^c_0‖ + [G^c_0]_α + ‖j^c_0‖).

**Re-derivation, step by step.**
1. *Duality (Lemma DUAL).* Ê(Y^p, v) = dv_0(p) and Ê(x, v) = ⟨G_0, dv_0⟩ + ⟨j_0, v_0⟩ for all chains with v_k = 0; x and Y^p are such
   chains; symmetry of Ê: dx_0(p) = ⟨G_0, dY^p_0⟩ + ⟨j_0, Y^p_0⟩. ✓
2. *Sup.* n²⟨G_0, dY^p_0⟩ = Σ_qG^c_0(q)dY^p_0(q) (G^c = n²G) ≤ 𝒬_H*(‖G^c_0‖ + [G^c_0]^∞_α); n²⟨j_0, Y^p_0 + dλ⟩ (λ free since d*j_0 = 0)
   ≤ n²·n^{−3}‖j^c_0‖·𝒩* ≤ C_YN‖j^c_0‖. With YH (§7) and BL-C (§3) for [G^c_0]^∞_α ≤ C_C[G^c_0]_α + 2·8^α‖G^c_0‖. ✓
3. *Residuals.* Levels 1..k−1 carry no source: κ_{i−1}r_{i−1} = κ_iQ_i^Tr_i; d* of the level-0 equation d*dx_0 + κ_0Q_0^Tr_0 = d*G_0 + j_0
   gives ev^Td*r_0 = 0 (d*d* = 0, d*j_0 = 0, d*Q^T = ev^Td*), ev^T injective ⇒ d*r_0 = 0, and inductively all r_i co-closed; so
   (Q^{(i+1→k)})^T = (Q_str^{(i+1→k)})^T (§2 (c)), |r_i| ≤ κ̂L^{−3(k−1−i)}sup|r_{k−1}|, ‖r‖_{X_s,Σ} ≤ (3/2)κ̂sup|r_{k−1}|. *Top* (Lemma TOPD,
   re-derived: Lemma TS makes Y^{(b)}_j = y_j for j < k with y the source-free minimiser at datum δ_b/κ_{k−1}; then the same symmetric-
   form argument gives r_{k−1}(x)(b) = ⟨G_0, dY^{(b)}_0⟩ + ⟨j_0, Y^{(b)}_0⟩): Proposition W at weight m′ centred at b's cell gives
   |f_0(y)(q)| ≤ G_D(m′)κ_−^{−1}e^{−m′d(q,b)}, and Σ_qe^{−m′d(q,b)} ≤ 6n⁴S(m′) (§7 step 5's 1D bound coth(m′/(2n)) ≤ n·coth(m′/2)), so
   Σ_q|dy_0| ≤ 6n²G_D(m′)S(m′)/κ_−; FP (§6; T ≤ 2 by the lift) gives 𝒩(Y^{(b)}) ≤ 4n³e^{20m′}(1083G_D(m′) + 40)S(m′)/κ_−. Hence
   sup|r_{k−1}| ≤ C_top(‖G^c_0‖ + ‖j^c_0‖), C_top = (6G_D(m′) + 4e^{20m′}(1083G_D(m′) + 40))S(m′)/κ_− exactly as printed. ✓
4. *Hölder of f_0.* n < 16: ρ_c ≥ 1/n ⇒ [f_0]_α ≤ n^α‖f_0‖ < 16‖f_0‖. n ≥ 16: B := d*Δ_0^{−1}F, F = dx_0 exact ⇒ dB = F (dF = 0), and
   −Δ_{scalar}B = d*F = d*G_0 + h, h := j_0 − κ_{k−1}(Q_str^{(0→k)})^Tr_{k−1}, sup|h| ≤ n^{−3}(‖j^c_0‖ + κ_+sup|r_{k−1}|). LES-div (§1) with R = n at
   any centre on the periodic lift, then units (re-done in §1) and LE (§4) at that centre: ρ_c^{−α}Osc_2(f_0) ≤ 2C_α[C_E‖f_0‖ + [G^c_0]_α +
   ‖j^c_0‖ + κ_+sup|r_{k−1}|] for ρ_c ≤ ¼ (F_{μν} = ∂_μB_ν − ∂_νB_μ, Osc_2 subadditive); ≤ 4^α‖f_0‖ for ¼ < ρ_c ≤ 1. ✓
5. *Upper levels.* f_j = 𝒜^{(0→j)}f_0 − R_j, R_j = Σ_{i<j}𝒜^{(i+1→j)}ϱ_i, ϱ_i := L^{2(k−1−i)}dr_i (from dx_j = 𝒬dx_{j−1} − dr_{j−1} and §2 (d)
   in coarse units). ‖f_j‖ ≤ ‖f_0‖ + 4‖r‖_{X_s,Σ}; [𝒜f_0]_α ≤ [f_0]^∞_α (𝒜 commutes with level-j translations) ≤ C_C[f_0]_α + 2·8^α‖f_0‖;
   Lemma RH termwise [R_j]_α ≤ Σ_{i<j}4L^{α(k−j)}L^{2(k−1−i)}sup|r_i| ≤ 4κ̂sup|r_{k−1}|Σ_{i<j}L^{−(1−α)(k−1−i)} ≤ 4κ̂(1 − L^{−(1−α)})^{−1}sup|r_{k−1}|
   (k − 1 − i ≥ k − j). ✓
Collecting: every component of ‖x‖_inv is ≤ C(‖G^c_0‖ + [G^c_0]_α + ‖j^c_0‖), C independent of k, T. ∎

**Consumer note.** COF / TOP-cc call "W0 steps 3-4" on a plain slot that is not co-closed (BFT_B §35.1 Lemma W0-use). My step 4
uses only sup|h|, never d*h = 0 — confirming W0-use's reading of step 4. Step 2's "for every λ" is the one place d*j_0 = 0 is
essential (W0-use's use (A)); step 3 needs r_{k−1} co-closed (use (B), priced in BFT_B by Lemma FT — not part of this item).

**Verdict: CONFIRMED** (inputs: YH §7, FP §6, LES-div §1, LE §4, BL-C §3, BL-2 §2 — all re-derived here — and the banked Proposition W).

---

## §9. LA21 — Theorem BL-5 (a) (BFT_A "**Theorem BL-5 (the linear estimate at the trivial background for data and residual-type sources).**", proof §8.6) — **CONFIRMED** (given BL-4)

**Statement.** 0 < α ≤ θ, uniformly in k, T: every minimiser with data and residual-type sources obeys ‖x‖_inv ≤ G_D‖B_k‖_D + G_R‖s‖_R,
G_R := c_1G_D + 8c_1 + 1/κ_−; x = y − τ mod gauge; ‖r‖_{X_s} ≤ 4κ̂C_R(‖B_k‖_D + c_1‖s‖_R) + ‖s‖_R/κ_−; f_0(x) = f_0(y).

**Re-derivation.** BL-1 (i) and BL-3 are re-derived in §6. Outputs: f_j(x) = f_j(y) − (dτ_j)^c, r_j(x) = r_j(y) + σ_j (= r_j(y) − r_j(τ)),
f_0(x) = f_0(y) (τ_0 = 0). Each component of ‖·‖_inv is a seminorm, so ‖x‖_inv ≤ ‖y‖_inv + ‖τ‖_inv ≤ G_D‖B_k + τ_k‖_D + (8c_1 + 1/κ_−)‖s‖_R
(α ≤ θ makes every L^{(α−θ)(k−j)} ≤ 1) and ‖τ_k‖_D = ‖τ^c_k‖ ≤ c_1L^{−θ}‖s‖_R ≤ c_1‖s‖_R. X_s line: L^{k−1−j}‖r^c_j(y)‖ ≤ κ̂L^{−(k−1−j)}·4C_R‖B_k + τ_k‖_D
(J-str (c) + N2-lin) and L^{k−1−j}‖σ^c_j‖ ≤ L^{−θ(k−j)}‖s‖_R/κ_−. ✓
**BL-4 (its one input) checked, as far as its own proof goes.** Residuals (J-str (c)), f_0 sup (N2-lin: ‖f_0‖ ≤ C_f sup|dB_k| ≤ 4C_f‖B_k‖_D),
current ‖J^c_0‖ ≤ κ_{k−1}‖r_{k−1}‖, Campanato via LES (R = n, a corner box of side s ≤ n/8 inside the centred Q_{2s}: factor (2⁴)^{1/2} = 4)
giving C_L(α) = max(4·2^αC_α, 16^α), upper levels via 𝒜 and R_j. I re-added the components: j = 0 gives 4[C_f + C_L(C_f + κ_+C_R) + κ̂C_R];
j ≥ 1 gives 4[(1 + 4^α(2·8^α + 2))C_f + 4^αC_CC_L(C_f + κ_+C_R) + (6 + 12 + 1)κ̂C_R]; the printed G_D is their max. ✓ So BL-4 holds *given*
N2-lin's C_R, C_f (LA37, §15) and LES's C_α (§1); its banked form is Proposition W at m = 0 (constant G_D(0) = G_D♭, with C_f, C_R replaced by
M_fS(μ), MS(μ) from LP Lemma 6.7 / Theorem 6.8, i.e. from LP Theorem 4.2′ — §16).

**Verdict: CONFIRMED** (exact consequence of BL-1 (i), BL-3, BL-4; with the banked route the constant is G_D(0) in place of BL-4's G_D,
and G_R changes accordingly — a constant relabelling, no statement changes).

---

## §10. LA16 — Corollary LIN0 (BFT_A "**Corollary LIN0 (gauge-invariant (H-lin^∇) on the pair of BL-7, m = 0, trivial background).**", proof §28.8) — **CONFIRMED** (given the banked Theorem GU)

**Statement.** 0 < α < θ < 1, level-wise co-closed plain currents, uniformly in k, T: ‖x‖_inv ≤ C(‖B_k‖_D + ‖s‖_R + ‖G‖_Y + ‖j^c_0‖ + ‖j‖_{Pc}).

**Re-derivation (superposition; the response is linear and each ‖·‖_inv component is a seminorm).**
- data + (R): BL-5 (a) (§9; needs α ≤ θ). (G) at level 0 and (P0): W0 (§8; d*j_0 = 0 is in the hypothesis). (G) at levels ≥ 1: Theorem GU,
  ‖x(G)‖_inv ≤ C_GU′max_{l≥1}ω_l‖G^c_l‖ for α < θ — **banked** (DICT55 §8.1: B12 ⊃ CODEX_REVIEW_COFM item 1, GU_m at m = 0).
- (Pl-c) via BL-6 (a), re-derived: for co-closed j_l (1 ≤ l ≤ k−1), BL-1 (ii) (re-derived: ⟨v, x_m⟩ = ⟨Q_{m−1}^Tv, x_{m−1}⟩ − ⟨v, r_{m−1}⟩
  iterated) gives the level-0 current (Q^{(0→l)})^Tj_l (co-closed, §2 (c); coarse size ≤ ‖j^c_l‖ ≤ L^{−θ(k−l)}‖j‖_{Pc}) and residual sources
  s_i = −(Q_str^{(i+1→l)})^Tj_l with |s_i| ≤ L^{−3(l−1−i)}‖j_l‖_own = L^{−3(k−1−i)}‖j^c_l‖, so ω^R_iL^{2(k−1−i)}|s_i| ≤ L^{θ(k−i)}L^{−(k−1−i)}‖j^c_l‖ =
  L·L^{−(1−θ)(l−i)}L^{−(k−l)}‖j‖_{Pc} ≤ L·L^{−(1−θ)(k−i)}‖j‖_{Pc}; summed over the ≤ k−1−i levels l > i: ≤ L·sup_m mL^{−(1−θ)m} = L/(e(1−θ)ln L) =
  C_P (max of m·e^{−m(1−θ)ln L} at m = 1/((1−θ)ln L)). Total level-0 current ≤ ‖j^c_0‖ + Σ_{l≥1}L^{−θ(k−l)}‖j‖_{Pc} ≤ ‖j^c_0‖ + ‖j‖_{Pc}/(L^θ − 1),
  co-closed, then W0. ✓
- θ < 1 is used only by C_P; α < θ only by GU; α ≤ θ by BL-5 (a). The "rough currents in the F3 weight" clause (Corollary G♯R) is
  outside the displayed inequality and outside every banked consumer I located (K^(σ)'s TOP♯ G,s part, C2-COF's s-slots, TOP-cc).

**Verdict: CONFIRMED** (given the banked GU; every other piece re-derived in §6, §8, §9 and here). DICT55 §5's note that LIN0 covers
only *level-wise* co-closed currents (not composite-co-closed ones) stands: that is the scope, and COF/C2-COF handle the composite
case separately (BFT_B Lemma SPLIT: each source *slot* is composite-co-closed, and the s-slots use LIN0 with G = j = B_k = 0, which
is BL-5 (a) at B_k = 0 — in scope).

---

## §11. LA29 — Proposition COF-size (BFT_B "**Proposition COF-size.** Under (CC-0) and in the (P0) + (Pl-c) classes", proof §35.4) — **CONFIRMED** (constant as printed), with two precisions

**Statement.** Under (CC-0) (D(S) = 0 as a level-0 function), π_l(j_l) ≤ L^{−θ(k−l)}‖j‖_{Pc} (l ≥ 1), π_0(j_0) = ‖j^c_0‖, θ > 0:
π_0(C(j)) ≤ C_C(‖j^c_0‖ + ‖j‖_{Pc}), C(j) := Σ_l(Q^{(0→l)})^Tj_l, C_C := (1 + 2d(1 − L^{−3})^{−1})(1 + (1 − L^{−θ})^{−1}), k-, T-free.

**Re-derivation.**
1. *Regrouping (Lemma DF-cc (ii), R2 — re-derived here).* Transposing BL-2 (b) (§2): (Q^{(0→l)})^T = (Q_str^{(0→l)})^T − Σ_{i<l}(Q_str^{(0→i)})^Th_i^Tev^{(i+1→l)T}d*.
   Summing over l and exchanging the (i < l) double sum: C(j) = Σ_l(Q_str^{(0→l)})^Tj_l − Σ_i(Q_str^{(0→i)})^Th_i^Tξ_i, ξ_i := Σ_{l>i}ev^{(i+1→l)T}d*j_l.
   Placements compose, so ev^{(0→i+1)T}ξ_i = D(S^j) − Ψ_i; with Lemma RT-cc (a) (re-derived: d* of the Euler–Lagrange equations,
   d*Q_l^T = ev^Td*, injectivity of ev^T, gives ev^{(0→i+1)T}ψ_i = Ψ_i := Σ_{l′≤i}ev^{(0→l′)T}d*j_{l′}) and D(S^j) = D(S) (Lemma SPLIT: G-slots have
   d*d* = 0, s-slots are Ξ-invariant): ev^{(0→i+1)T}(ξ_i + ψ_i) = D(S) = 0 under (CC-0) ⇒ ξ_i = −ψ_i. Hence
   C(j) = Σ_{l=0}^{k−1}(Q_str^{(0→l)})^T(j_l + h_l^Tψ_l) (the l = k−1 funnel vanishes: ψ_{k−1} = R_k(D(S)) = 0). ✓
2. *Funnel size (Lemma FT (i)-(ii), R2 — re-derived).* h_l(w)(X) = avg_σavg_{y∈B(X)}∫_{P^σ(c_X→y)}w: monotone axial paths inside B(X), each link
   used at most once per path with sign ±, so (h_l^Tψ)(b) = c(X(b),b)ψ(X(b)), |c| ≤ 1 (also with the σ-average): ‖h_l^T‖_{∞→∞} ≤ 1. ψ_l(Z) =
   Σ_{l′≤l}(d*j_{l′})(z_Z), |d*j_{l′}| ≤ 2d·sup_own|j_{l′}|, so π_l(h_l^Tψ_l) ≤ 2dΣ_{l′≤l}L^{−3(l−l′)}π_{l′}(j_{l′}) ≤ 2d[(1 − L^{−3})^{−1}L^{−θ(k−l)}‖j‖_{Pc} + L^{−3l}‖j^c_0‖]
   (L^{−θ(k−l′)} ≤ L^{−θ(k−l)} for l′ ≤ l). ✓
3. *Push-down contraction.* (Q_str^Tv)(z,μ) = L^{−4}Σ_{i<L}v(X(z − ie_μ),μ) for any v (co-closed or not): π_0((Q_str^{(0→l)})^Tv) ≤ π_l(v). ✓
4. *Sum.* π_0(C(j)) ≤ Σ_lπ_l(j_l + h_l^Tψ_l) ≤ (1 + 2d(1 − L^{−3})^{−1})[Σ_{l≥1}L^{−θ(k−l)}‖j‖_{Pc} + Σ_{l≥0}L^{−3l}‖j^c_0‖] ≤
   (1 + 2d(1 − L^{−3})^{−1})[(L^θ − 1)^{−1}‖j‖_{Pc} + (1 − L^{−3})^{−1}‖j^c_0‖] ≤ C_C(‖j^c_0‖ + ‖j‖_{Pc}), since (L^θ − 1)^{−1} ≤ (1 − L^{−θ})^{−1} and
   (1 − L^{−3})^{−1} ≤ 2 ≤ 1 + (1 − L^{−θ})^{−1}. ∎ (At d = 4, L = 3: 1 + 8·27/26 = 242/26 = 121/13 ≈ 9.31, matching the printed 9.31.)

**Precisions (no change to COF-size's statement).**
- (P1) *The l = 0 funnel.* BFT_B §27.1 defines "ĵ_0 := j_0", but DF-cc's identity (†) is true only with ĵ_0 := j_0 + h_0^Tψ_0 (step 1: the i = 0
  term (Q_str^{(0→0)})^Th_0^Tψ_0 = h_0^Tψ_0 survives). COF-size's step-2 bound covers it (π_0(h_0^Tψ_0) ≤ 2d‖j^c_0‖), so the conclusion stands;
  but anyone re-using "C(j) = Σ_l(Q_str^{(0→l)})^Tĵ_l" with §27.1's ĵ_0 drops a term.
- (P2) *Lemma FT (iii)'s printed statement* bounds the funnel by 2d(1 − L^{−3})^{−1}·max(L^{−θ(k−l)}‖j‖_{Pc}, L^{−3l}‖j^c_0‖); its own proof (§29.2 (iii))
  gives the **sum**, and the max form is false by up to a factor 2 when the level-0 and upper-level divergences add at one root (allowed
  under (CC-0), with a higher level cancelling them). COF-size uses the sum form — unaffected. (FT is R2, not in my batch; noted.)
- (P3) *Symbol collision (not in DICT55's list):* **C_C** names BL-C's 2^α(8·2^α/(2^α − 1) + 32·4^α) in BFT_A §7.3/§8.4 and COF-size's
  (1 + 2d(1 − L^{−3})^{−1})(1 + (1 − L^{−θ})^{−1}) in BFT_B §35.4; Theorem COF (§35.5) uses both (W0 step 2 / [f_0]^∞_α via BL-C, and
  "max_lπ_l(ĵ_l) ≤ C_C(…)" via COF-size) and lists "C_C" once among C_fun's arguments. Bookkeeping only: both are k-, T-free.

**Verdict: CONFIRMED** (re-derived with its two R2 inputs DF-cc (ii) and FT (i)-(ii)).

---

## §12. LA30 — Theorem PW-cc and its residual estimates (BFT_A "**Theorem PW-cc (co-closed half of the dual (PW-i)).**", proof §38.2) — **CONFIRMED** (given the banked Proposition W)

**Statement.** For co-closed level-l j and every plaquette p: |⟨j, Y^p_l⟩| ≤ C_ccL^{k−3l}‖j‖_∞, C_cc := C_YN + 4κ̂G_D(m′)S(m′)/(κ_−(L² − 1)); the
residual estimates COF consumes are ‖r_{k−1}(Y^p)‖_1 ≤ 4n^{−2}G_D(m′)S(m′)/κ_− and ‖r_m(Y^p)‖_1 ≤ κ̂L^{k−1−m}‖r_{k−1}(Y^p)‖_1.

**Re-derivation.** BL-1 (ii) (§10): ⟨j, Y_l⟩ = ⟨c, Y_0⟩ − Σ_{m<l}⟨(Q^{(m+1→l)})^Tj, r_m(Y)⟩, c := (Q^{(0→l)})^Tj = (Q_str^{(0→l)})^Tj (co-closed, §2 (c)),
‖c‖_∞ ≤ L^{−3l}‖j‖_∞.
- *Level-0 term:* |⟨c, Y^p_0 + dλ⟩| ≤ L^{−3l}‖j‖·𝒩(Y^p) ≤ C_YNL^{k−3l}‖j‖ (YH, §7). ✓
- *Top residual:* TOPD (§8) with the single source G_0 = δ_p: r_{k−1}(Y^p)(b) = dY^{(b)}_0(p) = n^{−2}f_0(Y^{(b)})(p); Proposition W at m′ centred at
  b's cell: |f_0(Y^{(b)})(p)| ≤ G_D(m′)κ_−^{−1}e^{−m′d(p,b)}; Σ over the 4 links per coarse site: Σ_Xe^{−m′d(p,X)} ≤ S(m′) (1D bound
  Σ_ne^{−μ|n−t|} ≤ coth(μ/2) for real t). ✓
- *Lower residuals:* only a level-0 source, so κ_ir_i = κ_{k−1}(Q_str^{(i+1→k)})^Tr_{k−1} (co-closed, §8 step 3); one step of Q_str^T sends each
  coarse link value to L·L⁴ = L⁵ (offset, site) pairs of weight L^{−4}: ‖Q_str^Tu‖_1 ≤ L‖u‖_1, so ‖r_i‖_1 ≤ κ̂L^{k−1−i}‖r_{k−1}‖_1. ✓
- *Residual terms:* |⟨(Q^{(m+1→l)})^Tj, r_m⟩| ≤ L^{−3(l−m−1)}‖j‖·AL^{k−1−m}n^{−2} = AL^{2m+2−k−3l}‖j‖ (A := 4κ̂G_D(m′)S(m′)/κ_−); Σ_{m<l}L^{2m+2} ≤
  L^{2l+2}/(L² − 1), so the sum is ≤ (A/(L² − 1))L^{k−3l}·L^{2−2(k−l)}‖j‖ ≤ (A/(L² − 1))L^{k−3l}‖j‖ (k − l ≥ 1). ✓
- *ℓ¹ form:* max{⟨j, x_l⟩ : d*j = 0, ‖j‖_∞ ≤ 1} = min_θ‖x_l + dθ‖_1 (LP duality: the annihilator of Ran d is Ker d*). ✓
**Consumer match.** Theorem COF (c) (BFT_B §35.5) uses exactly the two residual ℓ¹ bounds above, unchanged, with the regrouped currents
(read with ĵ_l, l ≥ 1); its double sum Σ_lΣ_{a≥0}AL^{−2(k−l)}L^{−2a}π_l(ĵ_l) ≤ A(1 − L^{−2})^{−2}max_lπ_l(ĵ_l) I re-did: correct.

**Verdict: CONFIRMED** (C_cc exactly as printed; inputs YH §7, TOPD §8, banked Proposition W).

---

## §13. LA17 — Theorem CO-upR + Lemma RH (BFT_A "**Theorem CO-upR ((CO-up) for rough currents).** For 1 ≤ j < k:", proofs §23.8-23.9 with [RBA5-fix] U5) — **CONFIRMED** in the configuration-level form K^(σ) uses

**What the banked consumer uses** (KFACTOR_OFF55 §4.2 (3), the LIN^(σ) (3) step of K^(σ)): for every configuration (any sources),
f_j = 𝒜^{(0→j)}f_0 − R_j, ‖f_j‖ ≤ ‖f_0‖ + 4‖r‖_{X_s,Σ}, [𝒜^{(0→j)}f_0]_α ≤ C_C[f_0]_α + 2·8^α‖f_0‖ (BL-C's C_C), and Lemma RH termwise
‖R_j‖_∞, [R_j]_α ≤ Σ_{i<j}4L^{α(k−j)}L^{2(k−1−i)}sup_own|r_i|.

**Re-derivation.** dx_{j+1} = d(Q_jx_j − r_j) = 𝒬_jdx_j − dr_j for every configuration; in coarse units (§2 (d)) f_{j+1} = 𝒜f_j − ϱ_j, ϱ_j :=
L^{2(k−1−j)}dr_j; iterate: R_j = Σ_{i<j}𝒜^{(i+1→j)}ϱ_i (no source hypothesis, no co-closedness). |ϱ_i| ≤ 4L^{2(k−1−i)}sup|r_i| and 𝒜 is a
contraction, so ‖R_j‖ ≤ Σ4L^{2(k−1−i)}sup|r_i| = 4‖r‖_{X_s,Σ} (L^{2(k−1−i)}sup|r_i| = L^{k−1−i}‖r^c_i‖); the Campanato seminorm at level j is over
boxes of side ≥ ρ_j, so [H]_α ≤ ρ_j^{−α}‖H‖_∞ = L^{α(k−j)}‖H‖_∞ and subadditivity gives RH. 𝒜^{(0→j)} commutes with level-j translations (a
shift by L^jv maps level-i blocks to level-i blocks for i ≤ j), so 𝒜f_0(P) − 𝒜f_0(P′) is an average of f_0(w) − f_0(w + (P′ − P)), whence
Osc_2(𝒜f_0; B) ≤ [f_0]^∞_αρ^α and, by BL-C (§3), [𝒜f_0]_α ≤ C_C[f_0]_α + 2·8^α‖f_0‖ (U5's order: BL-C applied to f_0 first). ∎
The theorem's source-specific clauses ("hence [f_j]_α ≤ C(k − l + 1)L^{(2+α)(k−l)}a" via Theorems XR/CO-0R, and RH's "C_RH′η²" via XB) rest
on Theorems XR, XB, CO-0R (BFT_A §18.4-18.5, §23.7), which are **not** in this batch and which no banked consumer I located uses
(DICT55's "Used by" for LA17 is K^(σ) only). Spot-check only: CO-0R's LES application with R = 4max(4, L^l) and the unit bookkeeping
n^{2+α}R^{−α}n^{−2} ≤ L^{α(k−l)} — correct.

**Verdict: CONFIRMED** for the configuration-level identity and bounds (the form the banked K^(σ) uses); the rough-current corollary
clauses are NOT-VERIFIED here (outside the banked chain).

---

## §14. LA24 — Lemma BA-3, plaquette clause (BFT_A "**Lemma BA-3 ((CL-3) in 𝔐^∇).**", proof §3.3) — **CONFIRMED with the coefficient 9** (for link size s_j ≤ 1/40, which BA-3's domain implies); the *justification* printed in BA-3 is the one Codex RLOC R11 refuted (it gives 144) — I supply a direct one

**Statement used by the banked chain** (K^(σ)/BFT-E display (1a), KFACTOR_OFF55 §1.4): ‖x‖ ≤ η ≤ η_0 ⇒ own plaquette logs of e^{x_j}
are ≤ L^{−2(k−j)}(2η + 9η²), via log(e^{x_1}e^{x_2}e^{−x_3}e^{−x_4}) = (dx)_p + q_p, |q_p| ≤ 9s_j², s_j := max_b|x_j(b)|_HS ≤ L^{−(k−j)}η.

**What was wrong (agreeing with Codex RLOC R11 and DICT55 §8.2, re-checked):** BA-3 cites "A1-NA(1) step 1, PROOF [S6]; as
quoted in PROOF l.3512". The cited text is now at PROOF.md l.4311 ("(BCH) If x_1, ..., x_n are anti-Hermitian with s := Σ|x_i| ≤ 1/4,
then |log(e^{x_1}⋯e^{x_n}) − Σ x_i| ≤ 9s²") — **citation drift** (l.3512 is another argument) — and its s is the *total word size*.
For four letters it gives 9(4s_j)² = 144s_j². So the printed justification does not support 9. ✓ (I re-did 9·16 = 144.)

**Direct re-derivation of 9 (link units, HS norm).** a := (x_1, x_2, −x_3, −x_4), |a_i| ≤ s, σ := Σ|a_i| ≤ 4s, P := Πe^{a_i}, Y := P − I.
- *Degree 2 (exact):* the degree-2 part of log P = Σ_m(−1)^{m+1}Y^m/m is Y_2 − Y_1²/2 = ½Σ_{i<j}[a_i, a_j] (la55_2 B4 checks the
  noncommutative identity exactly). |[a,b]|_HS ≤ |ab|_HS + |ba|_HS ≤ 2|a|_HS|b|_HS, six pairs: |Q_2| ≤ ½·6·2s² = 6s².
- *Degree ≥ 3:* with Y = Y_1 + Y_{≥2}, the remainder is R_3 = Y_{≥3} − ½(Y_1Y_{≥2} + Y_{≥2}Y_1 + Y_{≥2}²) + Σ_{m≥3}(−1)^{m+1}Y^m/m. HS is
  submultiplicative and the ordered-word expansion gives |Y_{≥r}| ≤ Σ_{m≥r}σ^m/m!, so |R_3| ≤ f(σ) := (e^σ − 1 − σ − σ²/2) +
  σ(e^σ − 1 − σ) + ½(e^σ − 1 − σ)² + u³/(3(1 − u)), u := e^σ − 1 < 1. f has nonnegative Taylor coefficients from degree 3 (la55_2 B3:
  1, 7/6, 31/20, 131/60, …), so f(σ)/σ² is nondecreasing.
- *Check la55_2* (criteria `checks/la55_2_criteria.md` 06:19:35 UTC, then `checks/la55_2_bch.py`, output `checks/la55_2_out.txt`):
  with a rigorous rational enclosure of e^{1/10}, 6s² + f(4s) ≤ 7.8155·s² < 9s² at s = 1/40 (B1 PASS, exact rationals), hence
  **|q_p|_HS ≤ 9s² for every s ≤ 1/40**; the designed-FAIL control (the same inequality at s = 1/20, where f is too large) FAILs as
  designed. The same proof holds verbatim for complex (sl(N,ℂ)) arguments in HS norm, which is what BFT-2's complexified ball needs.
- *Domain.* BA-3's proof takes η ≤ η_0 := 1/(20p_L) (p_L ≥ 2 the S4′ contour length), and s_j ≤ L^{−(k−j)}η ≤ η/3 ≤ 1/120 < 1/40. ✓
- *Linear part:* (dx)_p = [x_μ(z) − x_μ(z+e_ν)] + [x_ν(z+e_μ) − x_ν(z)], two own-unit differences of parallel links, each =
  L^{−2(k−j)}×(coarse gradient); so |(dx)_p| ≤ 2L^{−2(k−j)}‖∇^cx^c_j‖ ≤ 2L^{−2(k−j)}η, and 9s_j² ≤ 9L^{−2(k−j)}η². ∎ (Corollary WR (a)'s
  ‖q^c‖_∞ ≤ 9η² follows at j = 0: q^c = n²q, s_0 ≤ η/n.)
- BA-3's soft clause (|ρ_j| ≤ L^{−2(k−1−j)}η + C_ρL^{−2(k−j)}η², via NA-alg (a)'s 9.2y²) is **not used** by the banked display (1b), which
  comes from BA-6 + (LA-2) (KFACTOR_OFF55 §1.4); not re-derived here (NOT-VERIFIED, off the banked chain).

**Verdict: CONFIRMED** — the inequality |q_p| ≤ 9s_j² and the display L^{−2(k−j)}(2η + 9η²) are true on BA-3's domain (indeed with
7.82 in place of 9 for s_j ≤ 1/40). **Consequence for DICT55 §8.2 / FL29:** the two banked bullets do not conflict in truth value —
B41's "the cited BCH argument gives 144, not 9" is a correct statement about the *citation*, and B10/B18's displayed 9 is a correct
*inequality*, now certified by a direct argument; DICT55's proposed repair ("write C_q′ := 144") is unnecessary (harmless if
applied). The citation in BA-3 should be replaced by the argument above.

---

## §15. Course correction from the coordinator (06:24 UTC): CODEX_REVIEW_DICT landed — LR-pot is item 17; BA-3's 9 vs 144

**Read:** CODEX_REVIEW_DICT.md as on disk at 06:24 UTC (308 lines, complete: it ends with its summary and "for the lead" lists),
items D4, D5 and its LA-row table.

**LA15 — Lemma LR-pot (BFT_A "**Lemma LR-pot (potential reconstruction in the tent-axial slice).**", proof §13.12) — CONFIRMED**
(item 17; its own verdict, derivation already written in §6 above, constants C_1 = 775, C_2 = 40, C_3 = 205, c_0 = 20 and the level-0
pair 155/8/40 all re-derived; la55_1 C6). **I agree with Codex D4** ("LR-pot is not off the retained premise chain"): I reached the same
conclusion independently in §6 before reading D4 (FP is LR-pot + Theorem W, and FP feeds TOP♯ → K^(σ), W0 step 3, YH steps 3-4 and
PW-cc). D4 leaves LR-pot's uniform estimate "NOT-VERIFIED independently here"; my §6 re-derivation supplies it (pending Codex check).

**LA24 — BA-3, extension (check la55_4, criteria 06:24:45 UTC before its script; output `checks/la55_4_out.txt`).** Codex D5 notes
that Corollary WR (b) (BFT_A "σ ≤ C_q(η/n)·n^{−2}(2η + 9η²) ≤ 3C_qη²n^{−3} for η ≤ 1/9") needs the 9 on the whole range η ≤ 1/9,
i.e. link sizes s_j ≤ η/3 ≤ 1/27, which is larger than §14's radius 1/40. la55_4 E1: 6s² + f(4s) ≤ 8.8821·s² < 9s² at s = 1/27 (exact
rationals; then for all s ≤ 1/27 by la55_2 B3's monotonicity); the designed-FAIL control (s = 1/24, lower enclosure 9.335 > 9) FAILs.
**So |q_p| ≤ 9s_j² holds for every s_j ≤ 1/27, which covers BA-3's domain (s_j ≤ 1/(20p_L) ≤ 1/40), Corollary WR (a)'s ‖q^c‖ ≤ 9η²
and WR (b)'s η ≤ 1/9 step.** Codex D5: **I agree** that the *cited* argument certifies only 144 (word-size units; I re-did 9·16 = 144),
and that "2 + 144η ≤ 3" would need η ≤ 1/144; **I disagree with leaving the sharper 9 NOT-VERIFIED** — it is now derived directly
(degree-2 part exact, ≤ 6s²; degree ≥ 3 tail ≤ f(4s) with a rigorous rational enclosure). This is the "independently proved sharper 9"
D5 says it has no counterexample to; it still needs the Codex check the brief requires before banking. If the lead prefers not to rely on
it, Codex's 144 with η ≤ 1/144 (or BA-3's own η ≤ 1/(20p_L) = 1/220 at L = 3) is a valid fallback; every uniformity statement survives
either way.

**Codex's LA-row table line "LA36, LA37, LA40 package items; LIN0, FP, W0, YH, BL-2, BL-5(a), COF-size, PW-cc, LE, CO-upR/RH:
NOT-VERIFIED mathematical estimates at the claimed uniform scope"** is Codex declining to re-derive them; §1-§13 above are my
re-derivations of those (BL-2, BL-C, LES-div, LE, Λ, FP, LR-pot, YH, W0, BL-5 (a), LIN0, COF-size, PW-cc, CO-upR/RH done; LA37, LA40
next). Per the coordinator, every verdict here is by my own re-derivation, not by the 12/17/15 accounting.

---

## §16. LA40 — LINEAR_PACKAGE Theorem 4.2 (i)-(ii) (LINEAR_PACKAGE "**Theorem 4.2 (N2-exp; l.2735-2772).**"; proofs PROOF_session16_snapshot "Lemma EXP-id", "Lemma EXP-real", "Lemma EXP-strip", "Theorem N2-exp") — **CONFIRMED** (and every printed (η, r_0) pair verified in exact rational intervals); Theorem 4.2′ (sector form, m_*′) NOT-VERIFIED

**Why this item is more load-bearing than DICT55's "Used by: LA1" says.** Proposition W (banked, B12) is "PROVEN-HERE given the package
constants M, M_f": its residual step is LP Theorem 6.8 (a), whose data part is "N2-exp(ii) (torus kernel = periodisation)", and its
f_0 step is LP Lemma 6.7 (KF), also an N2-exp kernel. So every weighted estimate in §6-§12 (FP, YH, W0, PW-cc, TOP♯) rests on this item
through Proposition W; Codex COFM item 4 banked Proposition W with M, M_f as named inputs.

**Re-derivation.**
1. *EXP-id (exact).* With a = κΠ_αδ_α, δ = |D_n|², the K = 0 alias of the G-term is κΠδ·δ_μ/φ = aδ_μ/φ, so P̂_μ = A_μ + κZ_μ + aδ_μ/φ = β_μ/φ;
   D = Σ_νΔ_νP̂_ν^{−1} = φΣ; Δ_α = φ_αδ_α (4n²sin²(p/2n)·sin²(p/2)/(n²sin²(p/2n)) = 4sin²(p/2)) gives aΣ = Σ_μφ_μ(β_μ − φR_μ)/β_μ = φΨ; and the
   Lagrange solution of LED-dual's per-p constrained problem (P̂_μr̂_μ + b̂_μ = tν_μ, Σ_μν̄_μr̂_μ = 0) gives r̂_μ = −P̂_μ^{−1}Σ_νP̂_ν^{−1}ν̄_νF̂_{νμ}/D, hence
   𝓡̂_{μ,(νμ)} = −φν̄_ν/(β_μβ_νΣ) = −aν̄_ν/(β_μβ_νΨ). The 1/φ cancels. ✓ (LED-dual itself re-derived: B_k + Pr ∈ Closed by iterating
   B_{i+1} = QB_i − r_i modulo exact forms, P ≥ I from the m = 0 term, so the minimiser over co-closed zero-mean forms is unique.)
2. *EXP-real (R1)-(R6)* re-derived: |D_n(x)|² ≥ sinc²(x/2) ≥ max(4/π², 1 − x²/12); S_s ≤ S_s(0) = s^{−2} ⇒ 1 ≤ A_μ ≤ 1 + κ̂/(L² − 1); for K ≠ 0,
   φ^{(K)} ≥ 4n²sin²(π/2n) ≥ 9 (= 9 at n = 3, increasing to π²) and Parseval Σ_KΠδ = 1 ⇒ Z_μ ≤ 1/9; β_μ ≥ min_{t∈[0,6]}(κ(1 − t/6) + 4t/π²) =
   min(κ, 24/π²); β_μ ≤ max(π²/4, R̄)β_ν; Ψ = Σ_μ(φ_μ/φ)aδ_μ/β_μ (convex combination) ≥ Ψ_U on |x| ≤ r_0. ✓
3. *EXP-strip (P1)-(P7)* re-derived term by term: (P1) δ(z) − δ(x) = Σ_lw_le^{−ixl/n}(e^{yl/n} − 1), w_l ≥ 0, Σw_l = 1; (P2) φ_α(z) − φ_α(x) =
   2n²[cos a(1 − cosh b) + i sin a sinh b] with |sin a| ≤ √φ_α/n; (P3) S_s = α_s + β_s cos w, 0 ≤ β_s ≤ s^{−2}, |cos z − cos x| ≤ e^{|y|} − 1;
   (P4) per direction Σ_K|δ(z + 2πK)| ≤ e^η and Σ_K|Δδ| ≤ ε(1 + e^η) (Parseval on Z/n: Σ_K|D_n(z + 2πK)|² = n^{−1}Σ_je^{2yj/n}), telescoping
   the five-factor products (z-factors before, real x-factors ≤ 1 after the differing one) gives εe^{4η} + 4e^{3η}ε(1 + e^η) exactly as
   printed; Re sin²(u + iv) ≥ sin²u − sinh²v gives |φ^{(K)}(z)| ≥ λφ^{(K)}(x); (P5)-(P7) by the quotient bookkeeping, β ≥ max(b_*, φ, aδ),
   √φ/max(b_*, φ) ≤ 1/√b_*, Re(1/(1 + f)) ≥ 1/(1 + ρ_β) on |f| ≤ ρ_β < 1. ✓
4. *N2-exp:* under the four conditions all denominators stay away from 0 on S_η(Q) (β_μ by (P5), Ψ near 0 by (P6), Re Σ > 0 away from 0 by
   (P7), φ(z) ≠ 0 away from 0 by the f_0 condition); the symbols are 2π-periodic meromorphic functions (finite alias sums), bounded on
   every 2π-translate of S_η(Q), hence analytic on the strip (Riemann extension across the polar hypersurface); M depends on (L, κ_±)
   only (|a| ≤ κe^{4η}, |β| ≥ b_*/2, |Ψ| ≥ Ψ_U/2, Re Σ ≥ (ψ_0/β_0)br_V). (ii) Paley–Wiener: shift each p_α by +i·m′·sign(X_α) (vertical sides
   cancel by periodicity), |K(X)| ≤ Me^{−m′|X|_1} for m′ < m_*; torus kernels = periodisations (Poisson; absolute summability). ✓
5. *Positivity of m_*:* as η → 0, ρ_β → 0, e_Ψ → 0, br_V → 1/Γ and the f_0 term → 0, so for each κ some η > 0 works; the conditions are
   jointly continuous in (κ, η), so the min over the compact [κ_−, κ_+] is positive. ✓

**Check la55_3** (criteria `checks/la55_3_criteria.md` 06:24:06 UTC, before `checks/la55_3_strip.py`; output `checks/la55_3_out.txt`):
all five printed pairs (L = 3; κ = 1, ¼, 4 at κ̂ = 1; κ = ¼, 4 at κ̂ = 16) satisfy S1-S4 with rigorous rational enclosures of π, e^η,
cosh η (tightest margins: e_Ψ ≤ 0.39395 vs Ψ_U/2 = 0.39870 at κ = 4; br_V ≥ 0.17229 vs 0.16660 at κ = 1); the designed-FAIL control
(η = 0.02 at κ = 1) fails S2-S4 as designed. This independently reproduces REVIEW_S15_CONVERGENCE's 30-digit claim, in exact arithmetic.
Caveat: the printed η_* values are valid lower bounds *at those κ*; "m_* := min over κ ∈ [κ_−, κ_+]" is not tabulated (only positivity
is proven, item 5) — no banked statement uses a numerical m_* (the only numerical rate in use, m_Y = ln 2/(16L^c) ≤ ln 2/4160 < 1.7·10^{−4},
is far below every tabulated η_*).

**Theorem 4.2′ (m_*′, sector conditions (S1)-(S7)):** not read beyond LINEAR_PACKAGE's summary — **NOT-VERIFIED**. It is what the package
says "M" means from §4 on, and Proposition W / YH (m′ := m_*′/3) / FP / TOP♯ quote m_*′. **Every one of those statements survives with m_*
in place of m_*′** (they are existential in the rate; the only explicit rate in use, m_Y, is below m_* at every tabulated κ), with
m′ := m_*/3 in YH. So the banked chain needs only Theorem 4.2, which is CONFIRMED here.

**Verdict: CONFIRMED** (Theorem 4.2 (i)-(ii), uniform in k, T, u; printed pairs exact-verified). Theorem 4.2′: NOT-VERIFIED, not needed.

---
**Precision to §16 (appended after a grep of the banked producers for m_*′):** the banked weighted chain (GV55 l.346 "ln 2/(16L^c) ≤ m_*′/6",
COFM55's row N5 "m_*′/6 ≥ 2.33·10^{−3} > ln 2/4160") uses the numerical condition m_Y ≤ m_*′/6. With Theorem 4.2 in place of 4.2′ the
condition becomes m_Y ≤ m_*/6: at every tabulated pair m_*/6 ≥ 0.0037/6 > 6.1·10^{−4} > ln 2/4160 ≈ 1.67·10^{−4} (exact: 37/60000 >
ln 2/4160 since ln 2 < 7/10 and 7/41600 < 37/60000), so it still holds there; for a general [κ_−, κ_+] one adds L^c ≥ 6 ln 2/(16m_*) to
the choice of c (c is existential), which changes constants only. So "the banked chain needs only Theorem 4.2" stands with this
one added clause in c's choice.

---

## §17. LA37 — LES (Lemma 3.2), J-str (Lemma 3.1), N2-lin (Theorem 3.8) (LINEAR_PACKAGE "**Lemma 3.2 (LES, lattice elliptic step, Campanato form; l.1960-1989).**", "**Lemma 3.1 (J-str, the soft current has no funnel part; l.1941-1959).**", "**Theorem 3.8 (N2-lin, sup forms; l.2502-2516).**"; proofs in PROOF_session16_snapshot) — LES **CONFIRMED**, J-str **CONFIRMED**, N2-lin (H2) **CONFIRMED**, N2-lin (H1) **NOT-VERIFIED in full** (structure re-derived; not on the banked chain)

**LES.** dF = K, d*F = J, |F| ≤ F_0, |J| ≤ J_0, |K| ≤ K_0 on Q_R(x_0), R ≥ 16 ⇒ Osc_2(F;Q_ρ(x)) ≤ C_α(ρ/R)^α(F_0 + R(J_0 + K_0)), x ∈ Q_{R/2}(x_0),
1 ≤ ρ ≤ R/4. Re-derived: (dd* + d*d) = −Δ componentwise (forward/backward differences commute), so u = F_{μν} solves −Δu = (first
differences of J and K; for fixed (μ,ν): ±∂J_ν, ∓∂J_μ and the 2 components of d*K), a divergence-form source with |g|² ≤ 2(J_0 + K_0)²;
Dirichlet split on Q_r: ‖∇w‖_2 ≤ ‖g‖_{2,Q_r} ≤ √2r²(J_0 + K_0) (the source's "4r²" is a valid overestimate), ‖w‖²_2 ≤ Cr⁶(J_0 + K_0)²; harmonic
decay (§1) Σ_{Q_ρ}|h − h̄_ρ|² ≤ C(ρ/r)⁶Σ_{Q_r}|h − h̄_r|²; one-step inequality φ(ρ) ≤ A(ρ/r)⁶φ(r) + B(J_0 + K_0)²r⁶; Giaquinta's iteration (τ ≤ ½ with
Aτ^{(a−b)/2} ≤ 1, iterate along τ^mR_1, fill in by monotonicity) with a = 6 > b = 4 + 2α and φ(R/4) ≤ 6(R/4)⁴F_0² (means minimise Σ|u − c|²).
Dividing by ρ⁴ gives the claim. Integer radii / small r handled as in §1. ✓ **CONFIRMED** (C_α absolute, uncomputed, as stated).

**J-str.** Setting SC, Euler–Lagrange d*dB_0 + κ_0Q^Tr_0 = 0, κ_{i−1}r_{i−1} = κ_iQ^Tr_i. d*d* = 0 and d*Q^T = ev^Td* (root covariance) with ev^T injective
give d*r_0 = 0 and, inductively, d*r_i = 0 (a); Q^T = Q_str^T − h^Td* (§2) then gives r_{i−1} = (κ_i/κ_{i−1})Q_str^Tr_i and J_0 = −κ_0Q_str^Tr_0 (b);
‖Q_str^T‖_{∞→∞} = L^{−3} (exactly L terms of weight L^{−4} per fine link) and telescoping the κ-ratios give sup|r_i| ≤ (κ_{k−1}/κ_i)L^{−3(k−1−i)}sup|r_{k−1}|
and |J^c_0| = L^{3k}|J_0| ≤ κ_{k−1}sup|r_{k−1}|, k-uniform (c). ✓ **CONFIRMED.** (The sourced version is §8 step 3.)

**N2-lin (H2): sup|r_{k−1}| ≤ C_R sup|dB_k|.** 𝓡 (F ↦ r_{k−1}) on *all* 2-forms is exponentially local by Theorem 4.2 (§16, CONFIRMED), so its
torus kernel is ℓ¹ uniformly in k, T and Young's inequality gives (H2) with C_R ≤ 6MS(m′) (six planes). I also re-derived the source's own
route: LED-dual (exact, §16 item 1), the per-p Lagrange formula of LED-symb, Lemma WA (Littlewood–Paley: the j-th annulus piece has ℓ¹ norm
≤ CM2^{−ja}, summable for a > 0), and LED-unif (3)'s cancellation: with u := φ_n − κD_g, v := κD_g, both even with quadratic Taylor term |p|²,
so u = O(|p|⁴) and 𝓡̂ is of type a = 2. (Typo noted: the source writes φ_n/D_g = κ_{k−1} + u/v; it is κ_{k−1}(1 + u/v) — the type is
unchanged.) ✓ **CONFIRMED.**

**N2-lin (H1): sup|f_0| ≤ C_f sup|dB_k|.** Here no exponential F-representative is available (LP Corollary 4.3: 𝒦̂_u + Π_coex has a power
tail), so the proof needs Lemma WA with a = 1 for 𝒦̂_u + Π_coex. I re-derived the decomposition: replacing c_{ρσ} = 1 + O(|p|) by 1 and g_λ
by g_1 (g_λ − g_1 = O(|p|²), g even, g(0) = 1/κ) turns the K = 0 term into e^{ip·u/n}Π_exF̂ plus O(|p|)·O(|p|)·O(|p||F̂|)/(c|p|²) = type 1;
Π_ex + Π_coex = I (dd* + d*d = ψ on 2-forms); (1 − e^{ip·u/n})Π_coex is type 1 uniformly in u (|u/n| < 1); the K ≠ 0 aliases are summable
(Σ_KΠ_α(1+|θ_α|)^{−1}(1+|θ_σ|)^{−1}(1+|θ|)^{−1} ≲ Σ_jj^{−2}(1 + log j)²). **Not rewritten:** the order-≤ 5 derivative bounds of the alias sums
and of the replaced terms, uniform in k and u (LED-unif (2)/(4)'s bookkeeping) — spot-checked only. Hence **NOT-VERIFIED in full**.
**Banked-chain impact: none.** (H1)/(H2) enter only BL-4's printed G_D (and BL-5 (a)'s X_s constant 4κ̂C_R); the banked form of BL-4 is
Proposition W at m = 0, which uses the exponential B_k-kernels M, M_f of LP Lemma 6.7 / Theorem 6.8 (a) — corollaries of Theorem 4.2
(§16; I read Lemma KF's proof in the snapshot: |K_{f_l}| ≤ Me^{8m′}(1 + 6κ̂)e^{−m′d} from f_l = 𝔄f_0 − Σ𝔄ϱ_i) — not C_f.
**LED (local energy) arithmetic re-done:** 3⁴·6·L^{4k} = 486L^{4k} plaquettes, ½·486 = 243; 3⁴·4 = 324 links per level, ½·324 = 162, 162·Σ_mL^{−2m}
≤ 162·9/8 = 182.25 ≤ 183. ✓

**Verdict (LA37):** LES CONFIRMED; J-str CONFIRMED; N2-lin (H2) CONFIRMED; N2-lin (H1) NOT-VERIFIED in full (off the banked chain).

---

## §18. Conventions check across all items (the brief's pinned frame)

- **HS norms / components.** Every Setting-LIN item is proved for one real component in an HS-orthonormal basis of su(N) (C5). For a consumer
  whose sup norm is the HS norm of the su(N)-valued field, the componentwise bounds transfer with at most a factor √(N² − 1) on sup-type
  constants ([RBA3-fix] B3′) — N-dependent, k-, T-free. BA-3 (§14-§15) is proved directly in HS norm (also for complex arguments).
- **Positions / weights.** The weighted constants (FP's e^{20m}, Theorem W's e^{8m}, e^{12m}, Proposition W's e^{20m}) are computed, as in the
  source, with Convention K positions (L^{l−k}·base point). DICT55's canonical Convention C differs by < ½ coarse unit per coordinate, so any
  weighted bound transfers with a factor ≤ e^{2m}·(per two-point comparison); rates and uniformity unchanged (C3: the convention matters only
  for cutoff multipliers at σ > 0, which none of these items involves).
- **Contours / roots.** Centred roots and c_X → c_Y orientation are used (and needed) in BL-2 (b) (h(const) = 0 by centring), Lemma Λ (root of
  Z = root of c_Z), LR-pot (tents centred at roots). Left action, u = 1/g²: not used by any of the 17 items except through BA-3's HS norm.
- **Slices.** FP/LR-pot live in the tent-axial slice S_tent, not S_E. Their consumers (TOP♯, W0 step 3, YH step 4, PW-cc) use them only through
  𝒩(·) = ℓ¹ modulo gauge or through pairings with co-closed currents, which are representative-independent — so the slice mismatch with S_E
  is harmless there (checked at each use).

## §19. Summary table — every claim in this batch with its verdict

| # | Item (DICT55 row) | Verdict here | Inputs left as named (status) | Notes |
|---|---|---|---|---|
| 1 | LA36 LES-div | **CONFIRMED** | none | consumer forms (W0 step 4, EP-int) re-checked |
| 2 | LA19 BL-2 (a)-(e) | **CONFIRMED** | none | all constants as printed |
| 3 | LA20 BL-C | **CONFIRMED** | none | C_C exact as printed |
| 4 | LA34 Lemma LE | **CONFIRMED** | TK's C_K (re-derived in outline) | far coefficient even ≤ 10⁴/16 |
| 5 | LA14 Lemma Λ | **CONFIRMED** | none | C_Λ = 10 exact |
| 6 | LA15 LR-pot | **CONFIRMED** | none | ON the banked chain via FP (agree Codex D4) |
| 7 | LA12 Corollary FP | **CONFIRMED** | Proposition W (banked B12) | Theorem W re-derived; G_R(m) valid as printed |
| 8 | LA31 Theorem YH | **CONFIRMED** (implication) | Proposition W (banked) | LD, PC, U4′ bootstrap, constant subtraction re-derived; constants astronomically large, as stated |
| 9 | LA32 Theorem W0 | **CONFIRMED** | Proposition W (banked) | step 4 needs only sup|h| (W0-use confirmed) |
| 10 | LA21 BL-5 (a) | **CONFIRMED** | BL-4 (banked as Prop W at m = 0) | constant relabelling G_D → G_D(0) on the banked route |
| 11 | LA16 Corollary LIN0 | **CONFIRMED** | Theorem GU (banked B12) | BL-6 (a) and C_P re-derived |
| 12 | LA29 COF-size | **CONFIRMED** | none (DF-cc (ii), FT (i)-(ii) re-derived) | precisions P1 (ĵ_0), P2 (FT (iii) max→sum), P3 (C_C collision) |
| 13 | LA30 PW-cc + residual estimates | **CONFIRMED** | Proposition W (banked) | C_cc exact as printed |
| 14 | LA17 CO-upR + RH (configuration-level form) | **CONFIRMED** | none | rough-current corollary clauses NOT-VERIFIED (off chain) |
| 15 | LA24 BA-3, plaquette clause with coefficient 9 | **CONFIRMED** (direct proof, s_j ≤ 1/27) | none | printed justification REFUTED (gives 144; agree Codex R11/D5); citation drift l.3512 → l.4311; soft clause NOT-VERIFIED (off chain) |
| 16a | LA37 LES | **CONFIRMED** | none | |
| 16b | LA37 J-str | **CONFIRMED** | none | |
| 16c | LA37 N2-lin (H2) | **CONFIRMED** | Theorem 4.2 (here) | also via the source's WA/LED-unif route |
| 16d | LA37 N2-lin (H1) | **NOT-VERIFIED in full** | LED-unif's order-≤5 alias bookkeeping | off the banked chain (BL-4's banked form uses Lemma 6.7/Thm 6.8 kernels) |
| 17 | LA40 LP Theorem 4.2 (i)-(ii) | **CONFIRMED** | none | all 5 printed (η, r_0) pairs exact-verified (la55_3); Theorem 4.2′ NOT-VERIFIED and not needed (m_* suffices; add L^c ≥ 6 ln 2/(16m_*) to c's choice) |

**Counts (17 items; LA37 counted once by its weakest load-bearing part on the banked chain):** CONFIRMED 17 on the banked chain; within them,
the off-chain sub-clauses NOT-VERIFIED are: N2-lin (H1), CO-upR's rough-current corollaries, BA-3's soft clause, Theorem 4.2′. REFUTED: 0
items as statements; 1 printed justification (BA-3's citation, 9 → 144 as cited) — the statement itself is re-certified with 9.

**Checks:** la55_1 (constants; 7 PASS + control fired), la55_2 (BCH tail at s = 1/40; 4 PASS + control fired), la55_3 (strip conditions,
5 pairs PASS + control fired), la55_4 (BCH tail at s = 1/27; 2 PASS + control fired). Criteria files written before each script; exact
rationals throughout; every gate had a designed-FAIL control that fired.

---

## §20. For the lead (nothing here is banked; Codex checks first)

**Counts.** Of the 17 items: **16 CONFIRMED** (LES-div, BL-2, BL-C, LE, Λ, LR-pot, FP, YH, W0, BL-5 (a), LIN0, COF-size, PW-cc, CO-upR/RH in
its configuration-level form, BA-3's plaquette clause with coefficient 9, LP Theorem 4.2 (i)-(ii)); **1 partly NOT-VERIFIED** (LA37: LES,
J-str, N2-lin (H2) CONFIRMED; N2-lin (H1) NOT-VERIFIED in full — off the banked chain); **0 REFUTED** as statements. One printed
*justification* REFUTED (BA-3's citation of the word-size BCH bound certifies 144, not 9 — agreeing with Codex RLOC R11 / DICT D5), and the
statement re-certified by a direct proof. Off-chain sub-clauses left NOT-VERIFIED: CO-upR's rough-current corollaries, BA-3's soft clause,
Theorem 4.2′.

**What should change in PROOF.md's tally / HANDOFF's critical path.**
1. **FL29 resolved in favour of 9.** |q_p| ≤ 9s_j² holds for every link size s_j ≤ 1/27 (§14-§15, la55_2, la55_4): BA-3's display, BFT-1 (1a)
   L^{−2(k−j)}(2η + 9η²), Corollary WR (a) ‖q^c‖ ≤ 9η² and WR (b)'s "2 + 9η ≤ 3 for η ≤ 1/9" all stand. B10/B18's displayed 9 is correct;
   B41's "the cited argument gives 144" is a correct remark about the citation, not a conflicting constant. DICT55's repair "C_q′ := 144"
   is unnecessary (harmless). BA-3's citation (PROOF "l.3512", drifted; the text is now at PROOF.md l.4311) should be replaced by §14's
   argument. *Pending Codex check of §14 (la55_2/la55_4).*
2. **LR-pot is on the banked chain** (with Codex D4) — and is now re-derived (§6), with every constant as printed.
3. **The analytic root of the banked weighted chain is LP Theorem 4.2**, via Proposition W (M, M_f of LP Lemma 6.7 / Theorem 6.8 (a)), not
   only "LA1 via (CO-fun)" as DICT55's Used-by column says. It is now re-derived (§16) with all five printed (η, r_0) pairs verified in exact
   rational intervals (la55_3). Theorem 4.2′ (m_*′) is not verified and **not needed**: replace m_*′ by m_* in Proposition W, FP, YH
   (m′ := m_*/3), TOP♯, and add L^c ≥ 6 ln 2/(16m_*) to c's choice wherever "ln 2/(16L^c) ≤ m_*′/6" is used (GV55 l.346, COFM55 row N5;
   at every tabulated κ it already holds with m_*: 37/60000 > ln 2/4160).
4. **DICT55's hidden premise set:** 16 of the 17 R1 rows now have an Opus 5.5 re-derivation on disk (this file); on DICT55's own scale that
   is R2-pending-Codex, not B. The one input on the banked chain still resting on an unrecorded-model review is **none** after this file,
   except Proposition W / GU / Theorem 6.8 / Lemma 6.7, which are banked or are one-line corollaries of Theorem 4.2 (§16-§17). N2-lin (H1)
   remains un-re-derived but no banked result uses it.
5. **Precisions to enter (bookkeeping, no statement changes):** (a) BFT_B §27.1 "ĵ_0 := j_0" vs Lemma DF-cc (†), which needs ĵ_0 = j_0 + h_0^Tψ_0
   (COF-size covers it); (b) Lemma FT (iii)'s statement has "max" where its proof (and COF-size) has the sum — the max form is false by up to a
   factor 2; (c) **C_C collision** (BL-C's 2^α(8·2^α/(2^α−1) + 32·4^α) vs COF-size's (1 + 2d(1−L^{−3})^{−1})(1 + (1−L^{−θ})^{−1}), both inside
   Theorem COF's constant list) — not in DICT55's collision list; (d) LED-unif (3) typo φ_n/D_g = κ(1 + u/v); (e) LP Theorem 4.2's "min over
   κ ∈ [κ_−, κ_+]" is not tabulated (only positivity is proven; tabulated values are per-κ lower bounds, now exact-verified).

**Codex verdicts used, agree/disagree (each read as on disk at the time stated).**
- CODEX_REVIEW_DICT (06:24 UTC, complete): **D4 — agree** (LR-pot retained; I reached it independently in §6). **D5 — agree** that the cited
  argument gives 144 and that 2 + 144η ≤ 3 needs η ≤ 1/144; **disagree** that the sharper 9 must remain NOT-VERIFIED — derived here (§14-§15).
  **LA-row table "NOT-VERIFIED … LIN0, FP, W0, YH, BL-2, BL-5 (a), COF-size, PW-cc, LE, CO-upR/RH, LA36/37/40"** — not a disagreement: Codex
  declined to re-derive them; this file does (except N2-lin (H1)).
- CODEX_REVIEW_RLOC **R11 — agree** (word-size vs link-size; 144; "not a counterexample to the sharper inequality"); its BL-C mechanism ("two
  successive dyadic means differ by at most 4 Osc_2") — **agree**, matches §3.
- CODEX_REVIEW_COFM items 1 and 4 (GU at m = 0; Proposition W as weighted BL-4) — used as banked inputs; I read GU's and Proposition W's
  proofs (BFT_A §28.7, §13.9) and spot-checked their unit bookkeeping — **agree**, not re-derived in full.
- CODEX_REVIEW_GSHARP (root-line sums for Lemma Λ) — **agree** with the R2 re-classification; §5 derived independently.
- CODEX_REVIEW_KOFF / KFACTOR_OFF55 §4.1-4.2 (consumer forms of FP, LIN0, CO-upR/RH, BA-3) — used to fix the *form* each consumer needs;
  the forms match what is re-derived here.
UTC end: Thu Oct 29 06:30:34 UTC 2026

**Erratum to §20 (append-only):** the last bullet should read "KFACTOR_OFF55 §1.4, §4.1-§4.2 (consumer forms …)": I read the worker file
KFACTOR_OFF55, **not** CODEX_REVIEW_KOFF; no verdict of CODEX_REVIEW_KOFF was used. **Read-record supplement to §0:** BFT_B §27.1, §29.1-§29.2,
§35.1-§35.5; KFACTOR_OFF55 §1.4, §4.1-§4.2; CODEX_REVIEW_RLOC R11 and its disposition table; CODEX_REVIEW_DICT D4, D5 and its LA-row table;
PROOF_session16_snapshot LED-dual, LED-symb, WA, LED-unif, N2-lin, EXP-id, EXP-real, EXP-strip, N2-exp, Lemma KF, Theorem G♯_0-soft;
PROOF.md l.4311 (the cited BCH bound); GV55 l.346 and COFM55 row N5 (m_Y ≤ m_*′/6).
