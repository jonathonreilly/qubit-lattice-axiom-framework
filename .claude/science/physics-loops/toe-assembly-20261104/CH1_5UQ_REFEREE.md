lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1-5U-q referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3, the referee, of item CH1-5U-q under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen). The date is the one the lane brief sets; the session clock read 2026-11-05 23:25 EST when this file was begun. This session wrote neither pass 1 (`CH1_5UQ_DRAFT.md`) nor pass 2 (`CH1_5UQ.md`). This is one check: one line-by-line read of `CH1_5UQ.md`. It reviews no other review. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status, adopts no law, reading or definition, and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. It does not edit `CH1_5UQ.md`. "Referee closure" (RC) below means a short complete argument written here; it has not been checked by any other session.

**Text refereed.** `CH1_5UQ.md` at commit `1ec3f96a5` (`1ec3f96a55ed18b88b7612bc0075afa84ee12486`, the last commit that touches it, equal to the branch head when read). SHA-256 of the file read: `47ed0b80f977b8dcc8fcaec7ba0d50da704a895aae34b2fa4a4c408bdcfcdf7f`. Line numbers below refer to that file (140 lines).

**Sources read, with commits.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), HEAD | `1ec3f96a5` |

No other branch was read. Files read at that HEAD, with the commit of their last change. This folder: `CH1_5UQ.md` (`1ec3f96a5`) lines 1-140 (all); `CH1_5UQ_DRAFT.md` (`193e7169c`, SHA-256 `ffdae83b1eb076c0d534e645ee058562da095a9d328b27ee1f8955c53014f01d`, equal to the hash `CH1_5UQ.md` records) lines 1-283 (all); `LW1_REFEREE.md` (`5a2a0affe`) lines 1-80 (format); `Y2W_DRAFT.md` (`92e03055c`) lines 1-30 (format); `CH1.md` (`1ec3f96a5`) lines 1-30, 105-145, 177-233 (status with Amendments 1-2, inferred definitions, §4, Lemmas U-T, U-T′, Corollary U-T″, AM-5, §5); `CH1_5U.md` (`271c868a4`, frozen) lines 1-20, and by grep for "CH1-5U-q", "Q1", "light", "prescription" (Theorem 2.2 at 53, GAP Q1′ at 57, R2 at 59-81, R4 at 163-171); `CH1_5U_DRAFT.md` (`ecb2036d9`) lines 228-236 (CH1-5U-q) and by grep for Lemmas Q1 and Q1′ (lines 100, 183); `LW1_5.md` (`271c868a4`, frozen) lines 39-42, 70-100, 121-140, 199-201, 229-270 (inferred definition 4, the law `L5-U`, Theorem U, the L5-O parity statement, Z-U, B1-U); `VC1_5_DRAFT.md` (`2d0adc0c0`) lines 62-100 (Lemma 1.1, Lemma C), 124-153 (Lemmas 2.1-2.5), 209-256 (Theorems U1-U3, Corollary U3′); `VC1_5.md` (`bf95fc909`, frozen) lines 1-62, 93-157, 158-224 (status, definitions, Theorems 2.1-3.2, 5.1-5.6, 7.1, VC1-5U-odd, R1-R4), by grep for its theorem headings; `LIT_SMG.md` (`5d1409d92`) line 152 (§9) by grep; `TOE_ASSEMBLY.md` (`7d2b20d29`) lines 201-220 (§§3.4-3.5) and 397-411 (CH1); `LW1.md` (`4b65c608f`, frozen) line 241 (Theorem B4), by grep for "Gauss". `AGENTS.md` was read for routing. The audit ledger was not read.

**Working set used, by name.** PS-5, PS-6 and PS-6r, only through the law `L5-U` of `LW1_5.md` §2. PS-1c, only through the cell lifts (`LW1_5.md` B1-U; `VC1_5.md` Theorem 2.2). Results used, quoted at the point of use: `LW1_5.md` Theorem U, Z-U, B1-U, inferred definition 4 and the L5-O "Repaired statement" at line 201; `CH1.md` inferred definitions 6 and 8 and Lemma S1; `CH1_5U.md` Theorem 2.2, R2 and R4; `VC1_5.md` Theorems 2.1, 2.2, 3.1, 3.2, 5.2, 5.5, Corollary 5.4 and R4; `LW1.md` Theorem B4 (for `L_cube` in RC7 only). PS-2, PS-3, PS-4 and PS-7 to PS-11 are not used.

**Inputs from outside the working set.** *Standard mathematics, rebuilt where used:* Cauchy-Schwarz for states; the GNS construction; the numerical radius of an operator of square zero; Fourier analysis on a finite-dimensional torus representation with integer weights; Rayleigh quotients of a real symmetric matrix; existence of an irreducible subspace in a nonzero finite-dimensional representation (a minimal nonzero invariant subspace); the Haar average of `u_{a1}\bar u_{b1}` over `U(5)`, which is `δ_{ab}/5` by Schur's lemma. *Physics cited, never load-bearing:* the equal-time two-point function of a free massless Weyl field has modulus a constant times `|r|^{−3}` (as in both earlier passes).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U` is read plainly. No hostile meaning is read into it.

**Method.** Every proof in `CH1_5UQ.md` was re-derived by hand. Verdicts: CORRECT; ERROR (a false or misattributed line, quoted, with the fix); INCOMPLETE (a named missing step or an undefined term, with what is missing). A `[check]` is one tiny scratch computation in `/tmp/toe-ch15uqref/` (described in §3.9). It guides and proves nothing.

---

## 1. Verdict table

**Counts.** 51 items: 45 CORRECT, 3 ERROR, 3 INCOMPLETE. The eight inferred definitions count as eight items. One ERROR changes a displayed operator (item 24); its proof uses the correct operator. No other ERROR or INCOMPLETE item changes the content of a theorem.

| # | Item (`CH1_5UQ.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status and scope (5) | CORRECT | |
| 2 | §0 "Proved" list (7) | CORRECT | Each listed result is proved below, given the fix of item 24. |
| 3 | §0 GAP paragraph (9) | CORRECT | Each gap is real; see §2. The description of the draft is fair: draft line 193 extends the bound to "a dressed light charged fermion" in general. |
| 4 | §0 "Open by name" (11) | INCOMPLETE | The frozen name is CH1-5U-q[𝒫] (`CH1_5U.md` line 11 and R4). After CH1 Amendment 2, CH1-5O-i survives only as CH1-5O-E and "one residual case of reading R-A". The other clauses are correct. |
| 5 | §0 provenance (13) | CORRECT | The draft SHA-256 equals the hash of `CH1_5UQ_DRAFT.md` at `193e7169c`; `193e7169c` resolves to the recorded full hash. |
| 6 | Def 1, sites, modes, register (17) | CORRECT | Agrees with `LW1_5.md` line 87 and the setting of `CH1.md` §4. |
| 7 | Def 2, hop, tick, update form (18) | CORRECT | CH1-5U-i (a) also asks for covariance under `G_U` (`CH1_5U.md` R4); no result here needs it beyond the base tick, which has it (`LW1_5.md` B1-U). |
| 8 | Def 3, charges, invariance, `E` (19) | CORRECT | |
| 9 | Def 4, `S(A)`, `M(A)`, charge vectors (20) | CORRECT | "Equal to matter-number change" is Z-U. |
| 10 | Def 5, quasi-local fields (21) | CORRECT | The "assumed" existence of lifts is supplied: the cell group acts transitively on sites (`LW1_5.md` B1-U). |
| 11 | Def 6, GNS unitary (22) | CORRECT | |
| 12 | Def 7, proposed L1, L2(δ), L3 (23) | INCOMPLETE | L3 says "distant pairs"; it must say `|x_i − y_i| → ∞`, as the draft does (draft line 74). The gloss of L2 should read `‖(Ũ − 1)π(ψ)Ω‖ ≤ δ`. |
| 13 | Def 8, electrically diagonal, locked (24) | CORRECT | |
| 14 | Inputs paragraph (26) | CORRECT | Frozen versions now exist; see edit 13 in §5. |
| 15 | Theorem 2.1, statement (30) | CORRECT | The components lie in the algebra of the support of `A`, since terms of `Q_z` on links outside the support commute with `A`. |
| 16 | Theorem 2.1, proof (32) | CORRECT | |
| 17 | Theorem 2.2, statement (34-42) | CORRECT | Needs only invariance under each `Ad exp(iθQ_z)`. |
| 18 | Theorem 2.2, proof (44) | CORRECT | Uniform in `n`: the charge vectors of `α^n(A_q)` do not move, so no light cone enters. |
| 19 | Remark and GAP after Theorem 2.2 (46) | ERROR | "A gauge-invariant dressing or charge-sector prescription is explicitly contemplated in `CH1.md`, inferred definition 8." `CH1.md` line 30 reads: "Charged correlators require a gauge-covariant dressing or a charge-sector prescription." Fix: quote it. The GAP is real; RC1 shows the tail hypothesis is sharp. |
| 20 | Definitions of `φ_{ℓ,x}`, `K_x`, `F_x`, `P_x` (50-54) | CORRECT | |
| 21 | Theorem 3.1, statement (56-61) | CORRECT | |
| 22 | Theorem 3.1, proof, first paragraph (63) | CORRECT | `[check]` (1): both commutators vanish on 800 sampled basis vectors. |
| 23 | Theorem 3.1, proof, second paragraph (65) | CORRECT | Compressed. The conservation of `Y` uses `U_FY = U′_FP_xY = U′_FY = YU′_F = YU′_FP_x = YU_FP_x = YU_F`, which needs `Y = P_xY = YP_x` and `[U_F, P_x] = 0`; draft Theorem Z0(iii) writes it out. `H′_C` is even, so it commutes with odd `Y` too. |
| 24 | Theorem 3.2, statement (67-74) | ERROR | The display reads `X=c_{x,1}^\dagger c_{x,2}^\dagger c_{x,3} \prod_{s=1}^6`. The third matter factor must be `c_{x,3}^\dagger`, as in the draft (line 145) and as the stated charge 21 at `x` and the proof's "the matter factor creates three at `x`" require. The printed operator has total charge 1 and annihilates the input vector of the proof (`[check]` (4)). The rest of the statement is correct. |
| 25 | Theorem 3.2, proof (76) | CORRECT | `[check]` (4), `m = 3, …, 7`: `Xv = +v′`, both locked, `K_xv = K_xv′ = 0`, end number `n_0 → n_0 + 3`, electric phases equal for odd `m` and unequal for even `m`. For a link with `x` as its target the electric factor is a function of `m − p_{ℓ,x}`; one clause would say so (draft line 157 does). The last step needs no complete reducibility: a minimal nonzero invariant subspace of the finite-dimensional orbit span is irreducible. |
| 26 | Consequences of Theorem 3.2 (78) | CORRECT | True as stated for the single-star examples. RC6 adds: at even `q` the draft's schema is vacuous, and products give witnesses at every odd `q`. |
| 27 | `m ∈ {1,2,8,9}`, pinning, `LIT_SMG.md` (80) | ERROR | "A zero quasi-energy is not a propagating particle pole, residue, mass, or Weyl correlation (`LIT_SMG.md` §9)." §9 (line 152) says only: "Existence of an operator with the right charge does not establish a particle pole, residue or mass." Fix: quote §9 as a warning, and state the pinning as this item's own result (Theorem 2.2, and the clause `h_ℓP_x = P_xh_ℓ = 0` of Theorem 3.1). The first two sentences are correct. |
| 28 | Theorem 3.3, statement (82) | CORRECT | |
| 29 | Theorem 3.3, proof, stationarity and symmetry (84) | CORRECT | `Φ∘β_g` is the state of the locked vector with sets `A_{gx}`; choice independence then gives cell invariance. |
| 30 | Theorem 3.3, proof, purity (86) | CORRECT | Lemma 2.3 is applied to `Φ` with `𝔅 = 𝔄^G`; the compressed algebra is `End(⊗_{x∈S}W_x)^{K_S} ⊗ 1`, on which `Φ` is the vector state of `⊗_xu_x`; Lemma 2.2 gives purity. Frozen form: `VC1_5.md` Theorem 3.1(b), (c). |
| 31 | Remark after Theorem 3.3 (88) | INCOMPLETE | "dark" is not defined in this file. State what is meant: every hop annihilates the underlying product vector and the electric layer acts on it by a phase. The other two sentences are correct. |
| 32 | Theorem 4.1, statement (92-96) | CORRECT | RC2 weakens the hypothesis to number-diagonality. |
| 33 | Theorem 4.1, proof (98) | CORRECT | "The tracial and `ω_t` register states are traces" suffices because `ω_t` is a product of site densities and register traces (`VC1_5_DRAFT.md` Theorem U1). |
| 34 | Remark after Theorem 4.1 (100) | CORRECT | RC2 covers the odd-`m` ice limits of `VC1_5.md` R4, which Theorem 4.1 does not reach; RC3 gives the quasi-local estimate. |
| 35 | Theorem 4.2, statement (102-106) | CORRECT | `[check]` (5): `‖u‖ ≤ 1/2` on 540 random register states, `m = 1, …, 9`; the `m = 5` orbital state gives five singular values `1/2`. |
| 36 | Theorem 4.2, proof, link bound (108) | CORRECT | The bound on `v` also follows from `v_{jk} = \overline{u_{jk}}`. |
| 37 | Theorem 4.2, proof, string bound (110) | CORRECT | The proof uses only that the `L` links are distinct, not that the path is simple. |
| 38 | GAP in the draft's generalization (112) | CORRECT | Each gap is real. RC4 shows the matter factorization cannot be dropped; RC5 gives the exact form of "entangled". |
| 39 | Theorem 5.1, statement (116) | CORRECT | |
| 40 | Theorem 5.1, proof (118) | CORRECT | `[check]` (2): `A_ℓ^3v = (φ_{ℓ,y}^*)^3(φ_{ℓ,x})^3v ≠ 0`, largest coefficient `36`, for `m = 3, …, 7`. |
| 41 | Remark after Theorem 5.1 (120) | CORRECT | "for every `m`" is ambiguous; say "refutes, for `3 ≤ m ≤ 7`, the proposed step that one link cannot carry a triple". |
| 42 | Failed exclusions (122) | CORRECT | |
| 43 | Routes P1-P3, R1-R3 (124) | CORRECT | P1's content ("elementary charge `±1` modes") is the restricted form frozen as `CH1_5U.md` Theorem 2.2 (GAP Q1′ there); cite that, not the unrestricted draft Lemma Q1′. |
| 44 | Implication from CH1-5U-i, and GAP (126) | CORRECT | The GAP is real; RC8 repairs it through `CH1_5U.md` R4. |
| 45 | Four-test introduction (130) | CORRECT | "(2) remains open to further development" paraphrases the draft's "(2) open-ended, so a part can add to it" (draft line 240); quoting it avoids reading (2) as a merit. |
| 46 | Table row L1 (134) | CORRECT | RC1 adds: with `O(R^{−3})` tails the lower-bound clause of L1 is met by a self-overlap of the field. |
| 47 | Table row L2(δ) (135) | CORRECT | |
| 48 | Table row L3 (136) | CORRECT | The draft says "the working reading of sections 4 and 6, not proposed"; "it remains proposed" is the distiller's own label, not a quote. On test (4) see §4. |
| 49 | Table row `F_x` (137) | CORRECT | |
| 50 | Table row CH1-5U-q(L3) (138) | CORRECT | Name it beside CH1-5U-q[𝒫]; see item 4 and RC8. |
| 51 | Closing paragraph (140) | CORRECT | |

---

## 2. The distiller's GAPs

The distiller marks GAPs at lines 9, 46, 112 and 126. Line 9 gathers six; the later three restate parts of them. All six are real. Each entry gives the repaired statement or proof where this report has one.

**G1. The tail (lines 9, 46).** Line 9: "Norm quasi-locality alone supplies no `o(R^-3)` tail. The draft's claim that Corollary G1 decides the original CH1-5U-q as written therefore does not follow." *Real.* The draft keeps the tail hypothesis in Corollary G1 (draft line 100: "So if `f(R) = o(R^{−3})`, the two-point function is `o(|x − y|^{−3})`") and at line 105, but drops it at line 39 ("This decides CH1-5U-q as written") and in its FINISH (line 258: "CH1-5U-q and CH1-5U-i are false under the literal reading L1"). *Repair.* Theorem 2.2 as stated is the correct result. Its hypothesis cannot be weakened to `f(R) = O(R^{−3})`: RC1 (§3.1) gives a quasi-local odd field of charge 3, with `f(R) ≤ (8/7)R^{−3}`, whose undressed correlation in `τ` is at least `(63/64)·2^{−3}|x − y|^{−3}` along a sequence of pairs. Repaired statement: *under the undressed reading L1, CH1-5U-q fails for every field with `f(R) = o(R^{−3})`; for fields with `f(R) = O(R^{−3})` the lower-bound clause of L1 can hold with no dynamics at all; full free-Weyl agreement of such fields is not decided.*

**G2. The literal reading (line 9).** "CH1.md already requires a dressing or charge-sector prescription; calling the undressed reading the text's unique literal meaning is not justified." *Real.* `CH1.md` line 30, inferred definition 8: "Charged correlators require a gauge-covariant dressing or a charge-sector prescription." The frozen statement is CH1-5U-q[𝒫]: `CH1_5U.md` R4 (line 163) reads "Fix a charged-correlator prescription `𝒫` in the sense of `CH1.md` line 26." *Repair.* L1 is the empty prescription. Write CH1-5U-q[∅] for it; G1 says what is decided about it. (The draft says "the text's own" and "the reading of the text", draft lines 39 and 72; "unique" is the distiller's word.)

**G3. The product bound (lines 9, 112).** *Real, in four parts.* (a) *Repeated links.* For a repeated link the expectation is `λ(T_iT_j)` in one register, not `λ(T_i)λ(T_j)`; Theorem 4.2 rightly asks for distinct links. (b) *Times.* Theorem 4.2 bounds the equal-time `B_γ`; L3 allows `α^n(ψ_y)`, which reaches further registers. (c) *Dressings and charges.* Theorem 4.2 concerns one charge-1 bilocal with a string. (d) *Matter.* The draft's "whatever the matter state" (draft line 193) is false as an implication: RC4 (§3.4) gives a state whose restriction to the one register of a one-link string is trivially a product, with `ω(B_γ) = 9/2 > 5·2^{−1}`. *Repair.* Theorem 4.2 as stated, together with RC5 (§3.5): the bound holds on the closed convex hull of the full products `μ ⊗ λ_1 ⊗ ⋯ ⊗ λ_L`. Whether some exponential decay in `L` survives matter correlation is not examined here.

**G4. Entanglement (lines 9, 112).** "Non-product correlations need not be entanglement." *Real.* The draft infers "a dressed light charged fermion needs a stationary state whose link sector is electrically coherent and entangled along long strings" (draft line 193). *Repair.* RC5: for the string bilocal at `n = 0`, exceeding `5·2^{−L}` forces the restriction of `ω` to the endpoint matter and the `L` registers to be entangled across those `L + 1` factors. RC4 shows that this entanglement may sit between matter and a single register, not inside the link sector. For Theorem 4.1 the coherence required is coherence of a site number `N_z`, equivalently, in a gauge-invariant state, of a star end number `P_z = Σ_{ℓ∋z}p_{ℓ,z}` (RC2, §3.2).

**G5. L3 and IR (lines 9, 126).** "The inference from the proposed L3 to the full original IR hypothesis, and conversely from IR to L3, needs a matching prescription and locality assumptions." Line 126: "the original IR field is quasi-local and its charged-correlator prescription is not fixed to L3." *Real.* CH1-5U-q(L3) asks for a local field; IR fields are quasi-local. *Repair.* RC8 (§3.8): with the quasi-local form `L3^q` of L3 as the prescription, `CH1_5U.md` R4 gives CH1-5U-i[`L3^q`] ⇒ CH1-5U-q[`L3^q`] with no further matching, and CH1-5U-q(L3) ⇒ CH1-5U-q[`L3^q`]. RC3 (§3.3) extends Theorem 4.1 to quasi-local fields with `o(R^{−3})` tails. The converse direction, from IR under another prescription to L3, is not claimed by anyone and is not repaired.

**G6. Other gauge laws (line 9).** "The draft's extension to all gauge laws is not proved here." *Real as worded.* The draft (line 107) says "So L1 fails CH1 on every law with exact local gauge invariance, before any dynamics", with a one-line sketch. *Repair.* RC7 (§3.7) proves the undressed vanishing on every law whose fermion parity, on each local operator, is a product of commuting local gauge unitaries over its sites. This covers `L5-U`, `L_cube` (`CH1.md` Lemma S1) and `L5-O` under the register hypothesis of `LW1_5.md` line 201. "Every law with exact local gauge invariance" is not proved; a law whose parity is not of that form is not covered.

**Two further corrections by the distiller, not marked GAP.** Line 78: "the draft's existential quantifier 'for some |q|≥3' cannot be refuted merely by examples at ±3 and ±5." *Correct.* RC6 (§3.6) adds that the draft's schema holds vacuously at even `q`, so no example refutes it as written; restricted to odd `q`, products of separated zero modes refute it at every odd `q`. Line 100: "The conclusion covers the listed states, not every stationary invariant state on file in an unspecified corpus." *Correct*, and needed: the frozen `VC1_5.md` R4 now records odd-`m` ice limits that Theorem 4.1 does not reach. RC2 covers them.

---

## 3. Referee closures

Each closure is written in full. None uses a computation. `τ` is the tracial state; `VC1_5.md` Theorem 3.2 reads: "The normalized local traces define a tracial state `τ` invariant under every automorphism carrying local algebras into local algebras." So `τ` is stationary under every update of `L5-U` form, gauge invariant and cell invariant.

### 3.1 RC1: the tail hypothesis of Theorem 2.2 is sharp

**RC1.** Take any `m`, any update of `L5-U` form, and `q ∈ {1, 3}`. Let `B = c^†_{0,1}⋯c^†_{0,q}` at the base site `0`. For `v ∈ 2Z^3` let `B_v = β_{t_v}(B)`, with `t_v` the translation by `v`; by the lift formula (`VC1_5.md` Theorem 2.2) `B_v = ±c^†_{v,1}⋯c^†_{v,q}`. Put
\[
\psi=B_0+\sum_{k\ge1}2^{-3k}B_{2^ke_1}.
\]
(a) `ψ` is quasi-local and fermion odd. Each partial sum has definite total `U(1)_N` charge `q`. With `ψ_R` the partial sum over `2^k ≤ R`, `ψ_R` is odd, lies in the ball of radius `R`, and `f(R) ≤ (8/7)R^{−3}`.
(b) For `x ∈ 2Z^3`, `K ≥ 1` and `y = x + 2^Ke_1`, the translates `ψ_x = β_{t_x}(ψ)`, `ψ_y = β_{t_y}(ψ)` obey
\[
|\tau(\psi_y^*\psi_x)|\ \ge\ \tfrac{63}{64}\,2^{-q}\,|x-y|^{-3}.
\]
So `ψ` meets the lower-bound clause of proposed L1 (definition 7) at time `0`, at charge 3 and at charge 1. The hypothesis `f(R) = o(R^{−3})` of Theorem 2.2 cannot be weakened to `f(R) = O(R^{−3})`.

*Proof.* (a) `‖B_v‖ = 1` and `Σ_k 2^{−3k} < ∞`, so the series converges in norm. Each term is odd and has total charge `q`. Let `2^{k_0}` be the least power of two above `R`. The tail has norm at most `Σ_{k≥k_0}2^{−3k} = (8/7)2^{−3k_0} < (8/7)R^{−3}`.
(b) Lifts compose up to site sign automorphisms (`VC1_5.md` Theorem 2.2), so `β_{t_x}(B_v) = ±B_{x+v}`. Hence `ψ_x = Σ_u a_x(u)B_u` with `|a_x(x)| = 1`, `|a_x(x + 2^ke_1)| = 2^{−3k}` for `k ≥ 1`, and `a_x(u) = 0` otherwise. For `u ≠ w`, `τ(B_u^*B_w) = 0`: the unitary `(−1)^{N_u}` is even and acts on the matter at `u` only, so it conjugates `B_u^*` to `−B_u^*` and fixes `B_w`, and `τ` is invariant under inner automorphisms. For `u = w`, `τ(B_u^*B_u) = τ(∏_{i≤q}(1 − n_{u,i})) = 2^{−q}`. The double series converges absolutely, so `τ(ψ_y^*ψ_x) = 2^{−q}Σ_u\overline{a_y(u)}a_x(u)`. Both coefficients are nonzero at exactly two sites. At `u = y` the moduli are `1` and `2^{−3K}`. At `u = y + 2^Ke_1 = x + 2^{K+1}e_1` they are `2^{−3K}` and `2^{−3K−3}`. No other site qualifies: `2^K + 2^k` is a power of two only for `k = K`, and `x` is not of the form `y + 2^ke_1`. So `|τ(ψ_y^*ψ_x)| ≥ 2^{−q}2^{−3K}(1 − 2^{−3K−3}) ≥ (63/64)2^{−q}|x − y|^{−3}`. ∎

The correlation is the overlap of the field's own tail with its translate. No dynamics enters. So the lower-bound clause of L1 does not detect propagation once tails are `O(R^{−3})`. Whether such a field can match the full free-Weyl correlation is not examined.

### 3.2 RC2: Theorem 4.1 needs only number-diagonality

Call a state `ω` *number-diagonal* if `ω∘Ad e^{iθN_z} = ω` for every site `z` and every real `θ`. (Four tests: a property of states defined from the law's own operators; it fixes no target, is closed, settles nothing by premise and adds nothing; it is used here as a hypothesis, not proposed as a reading.)

**RC2.** (a) The conclusion of Theorem 4.1 holds for every number-diagonal `ω`, gauge invariant or not: if `ψ` is local and odd, `D` local with `[D, N_z] = 0` for every `z`, and `M(ψ_x) ∩ M(α^n(ψ_y)) = ∅`, then `ω(ψ_x^*Dα^n(ψ_y)) = 0`.
(b) `ω` is number-diagonal in each of these cases: (i) `ω` is gauge invariant and invariant under each `Ad e^{iθP_z}`, with `P_z = Σ_{ℓ∋z}p_{ℓ,z}`; gauge-invariant electrically diagonal states are a special case; (ii) every `N_z` is sharp in `ω`; (iii) on each finite region `ω` has a density that commutes with every `N_z`.
(c) So no local odd field meets proposed L3 in `τ`, in the states `ω_t` (`VC1_5.md` Theorem 5.2), in the two witnesses of `VC1_5.md` Theorem 5.5, in `ω_F` of Theorem 3.3, or in the odd-`m` ice limits `ω∘E` of `VC1_5.md` R4. R4(d) reads: "`Q_x = 3m` and `N_x = 0` on every `|c⟩`; both are gauge invariant, so both are sharp in `ω∘E`." The ice vectors are superpositions of different end-number assignments. Neither R4 nor `CH1_5UQ.md` shows these limits electrically diagonal, so Theorem 4.1 as stated does not reach them; (b)(ii) does.
(d) For a gauge-invariant `ω`, number-diagonality at `z` is equivalent to invariance under `Ad e^{iθP_z}`. So the coherence that L3 needs (local field, fixed `n`) is coherence of some site number `N_z`, equivalently of some star end number `P_z`. Coherence of single end numbers `p_{ℓ,z}` does not suffice while `ω` stays invariant under every `Ad e^{iθP_z}`.

*Proof.* (a) The proof of Theorem 4.1, after its first sentence, uses only invariance under each `Ad e^{iθN_z}`. (b)(i) `e^{iθN_z} = e^{iθQ_z}e^{−iθP_z}`, a product of commuting unitaries. `Q_z` generates the centre of `U(5)_z`, so gauge invariance gives invariance under `Ad e^{iθQ_z}`. Electric diagonality gives invariance under each `Ad e^{−iθp_{ℓ,z}}`, hence under `Ad e^{−iθP_z}`. (ii) In the GNS triple `(H, π, Ω)`, `ω((N_z − n_z)^2) = 0` gives `π(N_z)Ω = n_zΩ`. So `π(e^{−iθN_z})Ω = e^{−iθn_z}Ω`, and `ω(e^{iθN_z}Ae^{−iθN_z}) = ⟨π(e^{−iθN_z})Ω, π(A)π(e^{−iθN_z})Ω⟩ = ω(A)`. (iii) On a finite region `F` containing `z` and the support of `A`, `ω(A) = tr(ρ_FA)`, and `[ρ_F, N_z] = 0` gives `tr(ρ_Fe^{iθN_z}Ae^{−iθN_z}) = tr(ρ_FA)`. (c) `τ` and `ω_t` with finite `t` fall under (iii): their densities on `F` are proportional to `1` and to `e^{−tN_F} ⊗ 1` (`VC1_5_DRAFT.md`, proof of Theorem U1). In `ω_{±∞}` every `N_x` is sharp at `0` or `5`, so (ii) applies. In the witnesses of Theorem 5.5, in `ω_F` and in the R4 limits, `N_x` is gauge invariant and sharp in the underlying product or ice vector, and `E` fixes it; so (ii) applies again. (d) This is (b)(i) read in both directions, using only invariance under `Ad e^{iθQ_z}`. ∎

### 3.3 RC3: quasi-local fields with fast tails

**RC3.** Let `ω` be number-diagonal. Let `ψ` be quasi-local and odd as in definition 5, `D` local with `‖D‖ ≤ 1` and `[D, N_z] = 0` for every `z`, and `n` fixed. Let `r_n` be such that `M(α^n(A))` lies within distance `r_n` of `S(A)` for every local `A` (finite range of the gates, definition 2). If `|x − y| > 2R + r_n`, then
\[
|\omega(\psi_x^*D\,\alpha^n(\psi_y))|\le(2\|\psi\|+f(R))\,f(R).
\]
So if `f(R) = o(R^{−3})`, every such dressed correlation is `o(|x − y|^{−3})` at fixed `n`, and `ψ` does not meet L3 extended to quasi-local fields (`L3^q`, RC8).

*Proof.* `M(ψ_{x,R})` lies in the ball of radius `R` about `x`, and `M(α^n(ψ_{y,R}))` within distance `R + r_n` of `y`, so they are disjoint. RC2(a) gives `ω(ψ_{x,R}^*Dα^n(ψ_{y,R})) = 0`. Lifts and `α^n` are isometric, so the difference of the two bilocals has norm at most `f(R)‖D‖‖ψ‖ + (‖ψ‖ + f(R))‖D‖f(R)`. Take `R = ⌊(|x − y| − r_n)/3⌋`. ∎

### 3.4 RC4: the matter factorization in Theorem 4.2 cannot be dropped

**RC4.** Let `m = 5`, `ℓ = (x, y)` with `x` the source, and `γ` the one-link path from `x` to `y`. Then `B_γ = Σ_{jk}c^†_{y,j}U_ℓ^{jk}c_{x,k}`. There is a state `ω` with `ω(B_γ) = 9/2 > 5·2^{−1}`. Its restriction to the registers of `γ`, one register, is trivially a product over the links of `γ`. So the draft's "a charge-1 field dressed by strings is never light in the sense L3 in a state that is a product over the links of the strings, whatever the matter state" (draft line 193) is false as an implication from link factorization to the bound `5·2^{−L}`.

*Proof.* Put `a_k = r^{ℓ,x†}_kc_{x,k}` and `b_j = c^†_{y,j}r^{ℓ,y}_j`. Then `B_γ = (Σ_jb_j)(Σ_ka_k)`. Each `a_k`, `b_j` is a product of one rishon and one matter operator. Rishons commute with matter, and distinct modes anticommute within each system. So the two-exchange computation of Theorem 3.1 shows that the `a_k`, the `b_j` and their adjoints commute pairwise, except `a_k` with `a_k^*` and `b_j` with `b_j^*`. Also `a_k^2 = b_j^2 = 0`. Let `v_0` be the basis vector with matter at `x` full, matter at `y` empty, `x`-end empty and `y`-end full; its register lies in `Λ^5`. For `K, J ⊆ {1, …, 5}` put `e(K, J) = ∏_{k∈K}a_k∏_{j∈J}b_jv_0`, in any order. `a_k` moves flavour `k` from the matter at `x` to the `x`-end, and `b_j` moves flavour `j` from the `y`-end to the matter at `y`. So `e(K, J)` is `±` a basis vector, distinct pairs give orthogonal vectors, and `e(K, J)` lies in `Λ^5` exactly when `|K| = |J|`. Moreover `a_ke(K, J) = e(K ∪ {k}, J)` for `k ∉ K`, and `0` for `k ∈ K`; likewise for `b_j`. Put `s_a = C(5,a)^{−1}Σ_{|K|=|J|=a}e(K, J)`, a unit vector. Each pair `(K′, J′)` with `|K′| = |J′| = a + 1` arises `(a + 1)^2` times in `B_γs_a`. So
\[
B_\gamma s_a=\binom5a^{-1}(a+1)^2\binom5{a+1}s_{a+1}=(a+1)(5-a)\,s_{a+1},
\]
which is `9s_3` for `a = 2` and `8s_4` for `a = 3`. For `w = (s_2 + s_3)/√2`, `⟨w, B_γw⟩ = (1/2)⟨s_2 + s_3, 9s_3 + 8s_4⟩ = 9/2`. Both `s_2` and `s_3` have five matter fermions at `x, y`, so `w` has definite parity there. Let `ω` be the product of the vector state of `w` with any even state of the other sites and links. ∎

`[check]` (3) agrees: `⟨s_{a+1}, B_γs_a⟩ = 5, 8, 9, 8, 5` and `⟨w, B_γw⟩ = 4.5`. The largest eigenvalue of the `6 × 6` matrix with these off-diagonal entries is `14.16`, so states with `Re ω(B_γ) ≈ 7.08` exist; the proof uses only `9/2`. Theorem 4.2 itself is untouched: `w` is entangled between the matter and the register.

### 3.5 RC5: the exact form of "entangled"

**RC5.** Let `γ` have `L` distinct links. If the restriction of `ω` to the endpoint matter and the registers of `γ` lies in the closed convex hull of the product states `μ ⊗ λ_1 ⊗ ⋯ ⊗ λ_L`, then `|ω(B_γ)| ≤ 5·2^{−L}`. Hence `|ω(B_γ)| > 5·2^{−L}` forces that restriction to be entangled across the `L + 1` factors (endpoint matter; `ℓ_1`; …; `ℓ_L`).

*Proof.* `ρ ↦ ρ(B_γ)` is affine and continuous on the states of this finite-dimensional algebra. Theorem 4.2 bounds its modulus by `5·2^{−L}` on the products, hence on their convex combinations, hence on the closure. Registers commute with matter, so these are ordinary tensor products. ∎

This is the exact content of the draft's "entangled" (draft line 193) for the string bilocal at `n = 0`. It does not place the entanglement inside the link sector: in RC4 it sits between the matter and a single register.

### 3.6 RC6: spectral witnesses at every odd charge

**RC6.** (a) A fermion-odd quasi-local `ψ` of definite total charge `q` has odd `q`. So for even `q` there is no such `ψ`, and the draft's schema "for some `|q| ≥ 3` and some `δ_q > 0`, no stationary, gauge-invariant, cell-symmetric state of an `L5-U` law has a local fermion-odd `ψ` of charge `q` with ..." (draft line 161) holds vacuously at `q = 4`. No example can refute it as written. Restrict it to odd `q`.
(b) Let `q` be odd, `m ∈ {1, …, 9}`, and `τ_E` arbitrary if `m` is odd, `τ_E = 0` if `m` is even. Let `x_1, …, x_{|q|}` be distinct, pairwise non-adjacent sites, and `Ψ^{(1)}_{x_i}` the one-flavour zero mode of line 78 at `x_i` (adjoint if `q < 0`): `Ψ^{(1)} = P_xX^{(1)}Π^{(1)}P_x` with `X^{(1)} = c^†_{x,1}∏_sr^{ℓ_s,x†}_1r^{ℓ_s,y_s}_1`, `Π^{(1)} = ∏_sΠ[p_{ℓ_s,x} = n_0]`, `n_0 = (m − 1)/2` for odd `m` and `n_0 = max(0, m − 5)` for even `m`. Then `Θ = Ψ^{(1)}_{x_1}⋯Ψ^{(1)}_{x_{|q|}}` is local, fermion odd, of total charge `q`, `α(Θ) = Θ` for the base tick, and `τ(Θ^*Θ) > 0`. So CH1-5U-q(L2(δ)) holds for every `δ ≥ 0` at every odd `q` with `|q| ≥ 3` and every `m`.

*Proof.* (a) By Theorem 2.1 and Z-U, every component of a local odd operator with definite charge vector has odd total charge. If `ψ_R → ψ` with `ψ_R` local, project `ψ_R` onto its odd part and its total-charge-`q` part. Both projections are averages over automorphism groups (global matter parity, and the global `U(1)_N` action, which on a local `A` is `Ad ∏_{z∈S(A)}e^{iθQ_z}`). So they are contractions, keep local elements local, fix `ψ`, and do not increase `‖ψ − ψ_R‖`. The projected `ψ_R` is local, odd and of total charge `q`, so it vanishes for even `q`. So `q` is odd unless `ψ = 0`. (b) The one-flavour mode is Theorem 3.2's construction with one flavour. Its locked input has matter `S ⊆ {2, …, 5}` with `|S| = n_0`, `x`-ends `S`, and `y_s`-ends of size `m − n_0` containing flavour 1. The sizes fit: `n_0 ≤ 4`, `1 ≤ m − n_0 ≤ 5`, `n_0 + 1 ≤ 5`. The image is locked with end number `n_0 + 1`. For odd `m`, `n_0` and `n_0 + 1` are symmetric about `m/2`, so the electric phases agree for every `τ_E`. The conservation clause of Theorem 3.1 gives `α(Ψ^{(1)}) = Ψ^{(1)}`, and its charge is `7` at `x` and `−1` at each `y_s`, total `1`. Distinct non-adjacent sites have disjoint stars: they share no matter and no register. `α` is an automorphism, so it fixes `Θ`. A product of an odd number of odd operators is odd, and charge vectors add. Take a basis vector that is the locked input at every `x_i`. Each factor acts only on its own star, so `Θ` maps it to `±` a basis vector. So `Θ ≠ 0`, and `τ` is faithful. ∎

As line 78 says, such products are several separated objects. L2 does not see that.

### 3.7 RC7: the pinned charge on other gauge laws

**RC7.** Suppose a law and a state `ω` have local unitaries `V_z`, one per site, such that: each `V_z` is even and acts only on the matter at `z` and the registers (or `z`-ends) of the links at `z`; the `V_z` commute pairwise; every gate commutes with every `V_z`; `ω∘Ad V_z = ω`; and for every local `A`, `Ad(∏_{z∈S(A)}V_z)` acts on `A` as fermion parity. Then for local `A` fermion odd and local `B` with `S(A) ∩ S(B) = ∅`, `ω(B^*α^n(A)) = 0` for every `n`. The quasi-local estimate of Theorem 2.2 follows with the same proof.

*Proof.* Put `V = ∏_{z∈S(A)}V_z`. Every gate commutes with `V`, so `Ad V` commutes with `α^n`. `Ad V(A) = −A`. A link in the support of `B` at a site `z ∈ S(A)` would put `z` in `S(B)`; so the factors of `V` act on modes outside the support of `B`, and they are even, so `Ad V(B^*) = B^*`. Hence `ω(B^*α^n(A)) = ω(Ad V(B^*α^n(A))) = −ω(B^*α^n(A))`. ∎

*Instances.* (1) `L5-U`, `V_z = e^{iπQ_z}`, a gauge unitary (the central `−1` of `U(5)_z`). On a component with charge vector `q`, `Ad ∏_{z∈S(A)}e^{iπQ_z}` multiplies by `(−1)^{Σq_z}`, which is its matter parity by Z-U: "its matter parity is \((-1)^{\sum q_x}\)". Gates commute with `Q_z` (`LW1_5.md` Theorem U). (2) `L_cube`, `V_z = e^{iπ𝒢_z}`. `LW1.md` Theorem B4: "Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\)." `VC1_5.md` Corollary 5.4's proof: "three outgoing and three incoming links make its spectrum integer even for half-integral spin". `CH1.md` Lemma S1: "For a local homogeneous operator of total charge \(Q\), its matter parity is \((-1)^Q\)." (3) `L5-O`, `V_z` the lift of `−1_{10}` at `z`, under `LW1_5.md` line 201: "If, in addition, the lift of \(-I_{20}\) acts as a scalar on every link register inside \(\Lambda\), then \(-1_{10}\) at every site of \(\Lambda\) acts as fermion parity on operators supported with all their links in \(\Lambda\)"; the same line says this "holds for every irreducible register". Take `Λ = S(A)`.

*Scope.* This proves the draft's sentence at line 107 for these three laws, for local fields and for `o(R^{−3})` tails. RC1 transfers to `L_cube` at charge 1 with the same proof, so there too the tail hypothesis is sharp. A law whose fermion parity is not such a product is not covered.

### 3.8 RC8: the implication from CH1-5U-i, with a quasi-local prescription

Let `L3^q` be proposed L3 with three changes: the field is quasi-local and odd (definition 5); the pairs obey `|x_i − y_i| → ∞`; and the full free-Weyl tensor structure is required, as in CH1-5U-q(L3). Let CH1-5U-q[`L3^q`] be the statement of `CH1_5U.md` R4 with `𝒫 = L3^q`.

**RC8.** (a) CH1-5U-i[`L3^q`] ⇒ CH1-5U-q[`L3^q`]. (b) CH1-5U-q(L3) ⇒ CH1-5U-q[`L3^q`]. (c) So a proof of ¬CH1-5U-q[`L3^q`] refutes CH1-5U-i[`L3^q`] with no further matching; a proof of ¬CH1-5U-q(L3) refutes only the version of CH1-5U-i with local IR fields. (d) In a number-diagonal state, no quasi-local odd field with `f(R) = o(R^{−3})` meets `L3^q` (RC3).

*Proof.* (a) `CH1_5U.md` R4: "For every `𝒫`, CH1-5U-i[`𝒫`] implies CH1-5U-q[`𝒫`]." Its proof uses only that the IR fields of the `10_u` are quasi-local, odd and of charge `u` with `|u| ≥ 3` (`CH1_5U.md` Theorem 2.2), and that their correlations obey `𝒫`. (b) A local field is quasi-local with `f = 0` for large `R`. (c) From (a) and (b). (d) RC3. ∎

*Four tests for `L3^q`* (this report proposes it as the prescription that matches R4; it adopts nothing). (1) Pass: it is a correlator prescription, not a part's target. (2) Pass: one fixed class of fields and dressings. (3) Conditional, as for L3: norm-bounded local dressings may rate charged fields in a phase with a massless gauge field as not light. (4) Conditional, as for L3 (§4): full gauge invariance of the bilocal is more than Theorem 2.2 forces. Relative to L3 it removes one restriction (locality of `ψ`), the one R4 needs.

### 3.9 The `[check]`

Script `/tmp/toe-ch15uqref/check_ref.py` (SHA-256 `9c2d6e2ac19e8e3920eb9d7e1a4313697c45fbf32fa2e78b45084e9d55f7ffad`), output `out.txt` (SHA-256 `6e4edaac4b47ad23585f2154b6c220fda4645fcb99eca46d4864a20c94b71030`). Floating point. Fermion operators act on single basis vectors with Jordan-Wigner signs inside each CAR system (matter; each link register), and the systems commute; one register is also treated as dense matrices of size at most `252`. Run twice after `memory_pressure` showed 65 and 63 percent free: 0.3 s wall, 79 MB peak, identical output. Items: (1) `[φ_{ℓ,x}, φ_{ℓ,y}] = [φ_{ℓ,x}, φ_{ℓ,y}^*] = 0` on 800 sampled basis vectors of one link with its end matter; (2) Theorem 5.1 for `m = 3, …, 7`; (3) RC4; (4) Theorem 3.2 on a full star for `m = 3, …, 7`, including the printed display of line 69; (5) Theorem 4.2. Every item agrees with the hand proofs. It guides and proves nothing.

---

## 4. Four-test check of the readings

The tests: a reading fails if it (1) states or fixes a part's target, (2) is open-ended so a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. These are the referee's assessments. Nothing is adopted; only the owner adopts.

| Reading | (1) | (2) | (3) | (4) | Referee's result |
|---|---|---|---|---|---|
| L1, undressed | pass | pass | fails: with `o(R^{−3})` tails it settles CH1-5U-q negatively by premise on `L5-U`, `L_cube` and `L5-O` (Theorem 2.2, RC7). With `O(R^{−3})` tails its lower-bound clause holds by self-overlap with no dynamics (RC1), so there it measures no propagation | pass | unusable in both tail classes; agrees with both passes, sharpened by RC1 |
| L2(δ), spectral | pass | pass | pass | pass | passes; met by a static defect (Theorem 3.2) and by products at every odd charge (RC6), so it is not a reading of IR |
| L3 | pass | pass | conditional, as both passes say | conditional: the norm bound and the number clause have stated reasons (draft line 76), but full gauge invariance of the bilocal is more than Theorem 2.2 forces. Theorem 2.2 kills only components with a nonzero charge vector. The draft's reason, "The bilocal must be gauge invariant, or Lemma G below kills it", holds for `D = 1` only: with `D = U_ℓ^{11}` the bilocal `c^†_{y,1}U_ℓ^{11}c_{x,1}` has zero charge vector, and in a gauge-invariant state its expectation is that of its gauge average `B_γ/25` | 1, 2 pass; 3, 4 conditional |
| `F_x` | pass | pass | pass | pass | a definition from the law's own operators |
| CH1-5U-q(L3), open | pass | pass | pass | pass | carry it beside CH1-5U-q[`L3^q`] (RC8) |
| `L3^q` (RC8) | pass | pass | conditional | conditional | as L3; it drops only the locality of `ψ`, which R4 needs |
| number-diagonal (RC2) | pass | pass | pass | pass | a hypothesis, not a reading |

The gauge average in the L3 row: at each end the average of `r^{x†}_1c_{x,1}` over `U(5)_x` is `φ_{ℓ,x}/5` by Schur's lemma, and likewise at `y`, so the average of `c^†_{y,1}r^y_1r^{x†}_1c_{x,1}` is `φ_{ℓ,y}^*φ_{ℓ,x}/25`.

---

## 5. Required edits

*Blocking: needed before entry into a frozen part.*

1. Line 69: `c_{x,3}` → `c_{x,3}^\dagger` (item 24).
2. Lines 11, 126, 136, 138: name the open lemma as the frozen `CH1_5U.md` does, CH1-5U-q[𝒫]. State L1 as the empty prescription. Carry CH1-5U-q[`L3^q`] beside CH1-5U-q(L3) (G2, G5, RC8).
3. Line 11: replace "CH1-5O-i" by what CH1 Amendment 2 leaves open: CH1-5O-E and "one residual case of reading R-A".
4. Line 80: replace the attribution to `LIT_SMG.md` §9 by its exact sentence, and state the pinning as this item's own result (item 27).
5. Line 46: quote `CH1.md` inferred definition 8 exactly: "Charged correlators require a gauge-covariant dressing or a charge-sector prescription" (item 19).
6. Line 23: in L3, "distant pairs" → "pairs with `|x_i − y_i| → ∞`"; in L2, write `‖(Ũ − 1)π(ψ)Ω‖ ≤ δ` (item 12).
7. Line 88: define "dark" or replace it by "every hop annihilates the underlying product vector and the electric layer acts on it by a phase" (item 31).

*Recommended: import as referee closures, marked as such.*

8. Line 46 and table row L1 (134): RC1, so that the record states the strongest proved form of what is decided about the undressed reading.
9. Lines 96-100 and 124 (P3): RC2 and RC3. RC2 is the form that reaches the odd-`m` ice limits of `VC1_5.md` R4.
10. Line 112: RC4 and RC5.
11. Line 78: RC6.
12. Line 9, last sentence: the scope of RC7.
13. Lines 26, 74-76, 86, 88, 96, 124, 126: cite the frozen texts where they exist. `VC1_5_DRAFT.md` Lemma 1.1 is `VC1_5.md` Theorem 2.1; Lemma C is Theorem 2.2 (`VC1_5.md` has its own, different "Lemma C", a referee lemma at line 179); Lemmas 2.2-2.3 are Theorem 3.1(b)-(c); Lemma 2.4(a) is Theorem 3.2; Theorems U1, U2, U3 and Corollary U3′ are Theorems 5.2, 5.3, 5.5 and Corollary 5.6. Draft Lemmas Q1 and Q1′ of `CH1_5U_DRAFT.md` are frozen, restricted, as `CH1_5U.md` Theorem 2.2, with GAP Q1′ and R2. Cell covariance of the base tick is `LW1_5.md` B1-U.
14. Line 21: the existence of lifts for the chosen positions follows from site transitivity (`LW1_5.md` B1-U); it need not be assumed.
15. Line 120: "refutes, for `3 ≤ m ≤ 7`, the proposed step that one link cannot carry a triple".
16. Line 76: add the clause for links with `x` as target: the electric factor is a function of `m − p_{ℓ,x}`, and `(m − p − m/2)^2 = (p − m/2)^2`.
17. Line 110: "For a simple path" → "For a path with `L` distinct links".
18. Line 130: quote the draft's test (2), "open-ended, so a part can add to it".

---

## 6. Check against the draft

Every place where `CH1_5UQ.md` names or describes `CH1_5UQ_DRAFT.md` was compared with the draft text.

| `CH1_5UQ.md` | Draft | Match |
|---|---|---|
| 13, hash and date | file hash; line 5 "Written 2026-11-06" | exact |
| 30, "draft Lemma 1.2" | 57-64 | exact content |
| 34, "draft Lemma G and Corollary G1" | 86-102 | exact content; the draft keeps the tail at 100 and 105 |
| 9, 46, "Corollary G1 decides the original CH1-5U-q as written" | 39, 258 | fair: line 39 says so; FINISH 258 drops the tail |
| 9, "the text's unique literal meaning" | 39 "the text's own", 72 "the reading of the text" | fair; "unique" is the distiller's word |
| 46, "the draft's L1 test-3 judgment" | 244 | exact |
| 56, "draft Lemma F1 and Theorem Z0" | 121-137 | exact content |
| 67, "draft Theorem Z and Corollary Z1" | 143-161 | content exact; the display at 69 drops the dagger of the draft's `c^\dagger_{x,3}` (145) |
| 78, "the draft's existential quantifier" | 161 | exact |
| 82, "draft Corollary F2" | 165-167 | exact content |
| 88, "PS-3h5 and VC1 Corollary U3′" | 281 | exact |
| 92, "draft Lemma E and Corollary E1"; 100 | 175-181 ("no stationary state on file") | exact; the caution at 100 is needed (RC2) |
| 102, "draft Lemma W2′ and Corollary W2′.1"; 112 | 185-193 | exact; 193 is the generalization line 112 corrects |
| 116, "draft Lemma T"; 120, check of 36 | 203-205 ("max\|T_ℓ\| = 36") | exact; `[check]` (2) reproduces 36 |
| 124, P1-P3, R1-R3 | 223-232 | exact |
| 126, implication | 221 | exact |
| 130-138, four-test table | 240-248 | exact except the paraphrase of test (2) (edit 18); "not proposed" (246) is reported as "a working reading" |
| 9, extension to all gauge laws | 107 | exact |

No result of the draft is omitted. The draft's remarks on `LIT_SMG.md` §15 (163) and on Lemma U-T for `m ∈ {1, 9}` (207) are context, and their omission loses no claim.

---

## 7. Open statements to carry by name

- **CH1-5U-q[𝒫]** (the frozen name in `CH1_5U.md`), in particular **CH1-5U-q[`L3^q`]** (RC8) and its local form **CH1-5U-q(L3)**. Open after three failed attacks each way. *Attacks to prove it:* P1, quasi-free import, fails because the free tick is "an auxiliary c-number replacement of link operators; it is not the interacting tick or its vacuum" (`LW1_5.md` inferred definition 4), and its elementary light modes carry charge `±1` (`CH1_5U.md` Theorem 2.2; R2 for composites); P2, the frozen zero modes, fail because they are pinned (Theorem 2.2; the hop clause of Theorem 3.1) and `τ` is number-diagonal (RC2); P3, the stationary invariant states on file, fail because `τ`, `ω_t`, the witnesses of `VC1_5.md` Theorem 5.5, `ω_F` and the R4 ice limits are number-diagonal (RC2), and fully factorized string states obey Theorem 4.2 (RC5). *Attacks to refute it:* R1, the light cone, fails at the step from a support bound to a correlation bound; R2, register capacity, fails at Theorem 5.1 for `3 ≤ m ≤ 7`; R3, a charge-weighted spectral bound, fails at Theorem 3.2 (and at every odd charge by RC6). *Proved necessary for a proof:* a stationary, gauge-invariant, cell-invariant state in which some site number `N_z`, equivalently some star end number `P_z`, is coherent (RC2(d)).
- **The charged-correlator prescription of IR** (an owner question). L1 is unusable (§4); L2 decides nothing; L3 and `L3^q` pass tests 1 and 2, with 3 and 4 conditional.
- Inherited, unchanged: CH1-5U-i; AM-5; CH1-ii; CH1-5O-E and the residual case of reading R-A (CH1 Amendment 2); VC1-5U-odd; LW1-5U-PS7; Y2-W.

---

## 8. Recommendation

`CH1_5UQ.md` can enter the frozen part CH1 by a dated amendment once the seven blocking edits of §5 are made. Its proved results are correct. Its GAPs are real and honestly marked. No proved result of `CH1.md`, `CH1_5U.md`, `VC1_5.md` or `LW1_5.md` is reopened. The amendment should record CH1-5U-q[𝒫] as still open, narrowed as in §7. The referee closures RC1-RC8 may be imported marked "(referee closure, `CH1_5UQ_REFEREE.md`)"; no other session has checked them.

Theorem 3.3 is new for VC1: stationary reading-P witnesses at filling `m/2` for even `m`, beside the fillings `0` and `5` of `VC1_5.md` Theorem 5.5 (Theorem 7.1 there claims no stationarity). Entry into VC1 would need its own dated amendment to `VC1_5.md`. That choice is the lead's; this report does not make it.

---

## FINISH

**Proved.** *Checked by hand, as stated in `CH1_5UQ.md` once the display of line 69 is fixed:* Theorems 2.1, 2.2, 3.1, 3.2, 3.3, 4.1, 4.2 and 5.1. *Referee closures of this report (no other session has checked them):*
- RC1: the hypothesis `f(R) = o(R^{−3})` of Theorem 2.2 is sharp. A quasi-local odd field of charge 3 (or 1) with `f(R) ≤ (8/7)R^{−3}` has `|τ(ψ_y^*ψ_x)| ≥ (63/64)2^{−q}|x − y|^{−3}` along `x − y = 2^Ke_1`, at time 0.
- RC2: Theorem 4.1 holds for every number-diagonal state. This covers `τ`, `ω_t`, the witnesses of `VC1_5.md` Theorem 5.5, `ω_F` and the odd-`m` ice limits of `VC1_5.md` R4. In a gauge-invariant state the needed coherence is that of a site number `N_z`, equivalently of a star end number `P_z`.
- RC3: in number-diagonal states, quasi-local odd fields with `o(R^{−3})` tails have `o(|x − y|^{−3})` dressed correlations at fixed `n`.
- RC4: link factorization alone does not give the string bound of Theorem 4.2: `ω(B_γ) = 9/2 > 5/2` for a one-link string at `m = 5`.
- RC5: the string bound holds on the closed convex hull of the full products; exceeding it forces entanglement across the endpoint matter and the `L` registers.
- RC6: odd fields have odd charge, so the draft's spectral schema is vacuous at even `q`; at every odd `q` and every `m`, products of separated one-flavour zero modes meet L2(0).
- RC7: undressed correlations of separated odd fields vanish at all times on every law whose fermion parity, on each local operator, is a product of commuting local gauge unitaries: `L5-U`, `L_cube`, and `L5-O` under `LW1_5.md` line 201.
- RC8: with the quasi-local prescription `L3^q`, `CH1_5U.md` R4 gives CH1-5U-i[`L3^q`] ⇒ CH1-5U-q[`L3^q`], and CH1-5U-q(L3) ⇒ CH1-5U-q[`L3^q`].

**Counterexamples.**
- To weakening the tail hypothesis of Theorem 2.2 to `O(R^{−3})`: RC1.
- To "link factorization, whatever the matter state, gives `5·2^{−L}`" (draft line 193): RC4.
- To the display of Theorem 3.2 as printed (line 69): with `c_{x,3}` the operator has total charge 1 and annihilates the proof's input vector (`[check]` (4)). The draft's `c^\dagger_{x,3}` is correct.
- The draft's schema "for some `|q| ≥ 3` …" has no counterexample as written: it holds vacuously at even `q` (RC6(a)). Restricted to odd `q`, RC6(b) refutes it at every odd `q`.

**Open, by name.** CH1-5U-q[𝒫], in particular CH1-5U-q[`L3^q`] and its local form CH1-5U-q(L3), after three failed attacks each way: to prove it, P1 quasi-free import, P2 frozen zero modes, P3 the states on file and factorized strings; to refute it, R1 light cone, R2 register capacity, R3 spectral bound (§7). The charged-correlator prescription of IR (owner question). Inherited, unchanged: CH1-5U-i; AM-5; CH1-ii; CH1-5O-E and the residual case of reading R-A; VC1-5U-odd; LW1-5U-PS7; Y2-W.

**What changes downstream.**
- `CH1.md`, by a dated amendment after the seven blocking edits: CH1-5U-q under the undressed reading is decided, negatively, only for fields with `o(R^{−3})` tails, and that hypothesis is sharp. L1 is the empty prescription of CH1-5U-q[𝒫]. It is unusable: it fails test 3 for `o(R^{−3})` tails and measures no propagation for `O(R^{−3})` tails.
- `CH1_5U.md`: CH1-5U-q[𝒫] stays open. For `𝒫 = L3^q`, R4 gives the implication from CH1-5U-i with no further matching. A proof needs a stationary invariant state with a coherent site number (RC2(d)); none of the states listed in RC2(c) has one.
- No named failing step for `L5-U` follows. The law stays live under `TOE_ASSEMBLY.md` §3.5.
- VC1: Theorem 3.3 adds stationary reading-P witnesses at filling `m/2` for even `m`. Entry into `VC1_5.md` needs its own amendment.
- GA2 and Y2: the per-register bound of Theorem 4.2 stands. Its string corollary needs full factorization with the endpoint matter (RC4, RC5).
