lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CN1MOD referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). The lane was launched in the pass-1 lane format; its job is pass 3, the referee, under PR #10138's method. This session wrote neither pass 1 (`CN1MOD_DRAFT.md`) nor pass 2 (`CN1MOD.md`). This is one check: one whole-part, line-by-line read. It reviews no other review.

**Text read.** `CN1MOD.md` at commit `37bc873ee` (branch `claude/toe-assembly`; the last commit that touches it). SHA-256 `ed0d75d80ad272857bbc4d294919e3bd6b3b2b58b09a19ddff3e077d77ecfff8`. Line numbers below refer to that file.

**Sources read.** `CN1MOD_DRAFT.md` at `a1f1ffc91`, all 372 lines (section 0). Every other source, with its commit and lines, is in the section "Prior work used". All folder files were read at `37bc873ee`; two `docs/` notes were spot-checked on `origin/main` at `f5af11cd0`.

**Counts.** 66 items: 63 CORRECT, 2 ERROR, 1 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. Of the distiller's ten GAPs, nine are real and one (G7) is not.

**Working set used, by name.** None. Every item checked here is mathematics conditional on hypotheses that the file displays. Working-set and open-item names (H-PHOTON, GA1-5-Φ, GB1-U1, R2-a/H-TICK, ST1, R1-OBS, R-CS^str, ZM1-INV) are checked only as labels in the bridge list (item 60).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms are read plainly. No axiom is read for a hostile meaning. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged and was not needed.

**Method.** Every proof was re-derived by hand. A `[check]` is a small scratch computation in `/tmp/toe-CN1MODref/`, under a minute and a few MB. It guides and never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix); INCOMPLETE (a named missing step, with a repair where one is found). A "referee closure" is a short complete argument for a missing step. It is author-side mathematics and is itself unrefereed.

---

## 0. Sources checked, and the gauge-sign check

**Pass-1 source.** `CN1MOD_DRAFT.md` at commit `a1f1ffc91`, SHA-256 `67f7e50b173bebba1137876710d244aea2a7a5256ee0932da6d0d64654ef4c9a`. This equals the hash that `CN1MOD.md` line 13 records. All 372 lines were read.

**Gauge sign (CN1MOD line 25), checked against the draft.** The draft's line 107 reads: "`S_F` is invariant under `ψ_a(x) → e^{ieq_aχ(x)}ψ_a(x)`, `ψ̄_a(x) → e^{−ieq_aχ(x)}ψ̄_a(x)`, `A_μ(x) → A_μ(x) + χ(x+μ̂) − χ(x)`". Under that map the hop `ψ̄(x)U_μ(x)ψ(x+μ̂)` with `U_μ = e^{ieqA_μ}` picks up the phase `exp(2ieq[χ(x+μ̂) − χ(x)])`. That is not one for general `χ`. The phase cancels exactly when `A_μ(x) → A_μ(x) + χ(x) − χ(x+μ̂)`. The reverse hop `ψ̄(x+μ̂)U_μ(x)^*ψ(x)` gives the same condition. So the distiller's sign is right and the draft's is wrong. The draft never uses the wrong sign in a proof step. Its later uses (exchange covariance, Ward identities in attack B) need only that some local gauge map leaves `S_F` invariant.

**Infinite-volume covariance (CN1MOD line 23).** The draft's line 103 writes the photon covariance as a Brillouin-zone integral on the torus `Λ_T`. On `(Z/TZ)^4` the correct kernel is `T^{-4}Σ_k` over `k ∈ (2π/T)Z_T^4`. The distiller's GAP is real. It changes no later statement, since every later statement is either abstract (Theorems 1 and 3, Lemma 2, Proposition 5) or about a continuum integral (Lemma 6).

**Other sources** are listed in the section "Prior work used".

---

## 1. Verdict table

Items follow `CN1MOD.md` in order. "Draft" means `CN1MOD_DRAFT.md`.

| # | Item (CN1MOD line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | Scope matches what is proved below. |
| 2 | §0 "Proved here" list (7) | CORRECT | Each listed result is proved below (items 20-53). The word "discrete estimate and its window" fits Theorem 1. |
| 3 | §0 GAP paragraph (9) | ERROR | "The last-scale prefactor in the draft's proof of Theorem 3 needs the correction given below" is false: the draft's constant works at every `k` (section 2, G7). Fix: delete the sentence (edit E2). Every other GAP in the paragraph is real (section 2). |
| 4 | §0 "Open by name" (11) | CORRECT | Every named item is open in this file or in its source. "B1; B2; C1" match §5. |
| 5 | §0 provenance (13) | CORRECT | Draft hash matches (section 0). Prior-digest hash checked in section 1a. |
| 6 | §1 lattice, species, Wilson action (17-21) | CORRECT | Matches draft lines 93-97 verbatim in content. |
| 7 | §1 free symbol and Wilson mass (23) | CORRECT | Fourier transform of `S_F` at `A=0` gives `μ_a+Σ_μw_{aμ}[(1−cos p_μ)+iγ_μ sin p_μ]`; at a corner with `p_μ∈{0,π}` the mass is `μ_a+2Σ_{μ:p_μ=π}w_{aμ}`, positive at nonzero corners when `μ_a=0`. |
| 8 | §1 photon covariance, torus sum, `N` (23) | CORRECT | GAP on the torus sum is real (section 0). `m≤L^{−2}` gives `N≥2`. |
| 9 | §1 GAP gauge sign and symmetry list (25) | CORRECT | Sign checked in section 0. The massive Feynman weight is not gauge invariant: `δ_{μν}/(\hat k^2+m^2)` is not annihilated by the longitudinal projector. |
| 10 | Definition 1, exact scale integration (31) | CORRECT | A definition; existence is correctly left as hypothesis. |
| 11 | Definition 2, Banach space, σ, speed (32) | CORRECT | |
| 12 | Definition 3, norm identity `‖X−σX‖=2\|Δ\|+E` (33) | CORRECT | Draft (3.1), line 117. With an `ℓ^1` speed block, `(X−σX)` has speed entries `±Δ`. |
| 13 | Definition 4, box `B′` (34) | CORRECT | |
| 14 | Definition 5, holomorphic coordinates (35) | CORRECT | |
| 15 | Definition 6, `N`-independent constants (36) | CORRECT | |
| 16 | Definition 7, cutoff prescription for the quartic (37) | CORRECT | Section 2, GAP G10, shows the prescription covers more than the file says. |
| 17 | R1″-MOD[d] (39-41) | CORRECT | Matches draft line 137-141. Notation: the contraction constant `c` clashes with the photon speed `c`; rename (edit E3). The draft's window `k_β≤k<N−k_β` is replaced by "N-independent end margins"; this is right, because Theorem 1's window ends at `N−max(k_β,k_m)`. |
| 18 | UB″ (43-49) | CORRECT (as a proposal) | Matches draft lines 143-150. Open. |
| 19 | Remarks after UB″ (51) | CORRECT | `mL^k=mL^N·L^{−(N−k)}≤L^{−(N−k)}` since `L^N≤1/m`. The exchange-covariance remark is right: σ-covariance kills a source only at `σX=X`. |
| 20 | Formula (1): `F` and `F_s′` (55-60) | CORRECT | Numerator `(4s²+3s+1)(1−s)=−4s³+s²+2s+1`. With `D=(1+s)²`: `N′D−ND′=(1+s)[(−12s²+2s+2)(1+s)−2(−4s³+s²+2s+1)]=(1+s)(−4s³−12s²)`, so `F_s′=−4s²(s+3)/(6π²(1+s)³)<0` for `s>0`. The source formula for `P` is checked in item 29. |
| 21 | `Λ` representation, bounds, consensus value (62) | CORRECT | Mean value form `F(s_1)−F(s_2)=(s_1−s_2)∫_0^1F′`, and `s_1−s_2=Δ/c`. On `B′=[v_−,v_+]`, `s∈[v_−/v_+,v_+/v_−]`, so `Λ≥min\|F′\|/v_+>0`. `\|F′(1)\|=16/(48π²)=1/(3π²)`. Positivity of the one-loop drag at every ratio also holds pointwise: `P=F/(c(1−s))=(4s²+3s+1)/(6π²c(1+s)²)>0` for all `s>0`. |
| 22 | Theorem 1, statement (64-78) | CORRECT | Matches draft lines 158-170. |
| 23 | Theorem 1 proof, bulk step (80) | CORRECT | `δ_{k+1}≤(1−λG_k+Kη_k+κKG_k²)\|Δ_k\|+(1+κθ)E_k`; `G_k²≤η_k`; `1+κθ≤κ(1−λG_k)` is `κ(1−θ−λG_k)≥1`, true as `λG_k≤λG_0≤(1−θ)/2` and `κ=2/(1−θ)`. The factor `1−λG_k` is positive. |
| 24 | Theorem 1 proof, threshold step (80) | CORRECT | `KG_k+κKG_k²≤K(1+κ)G_k` for `G_k≤1`; `1+κθ≤κ` is `κ(1−θ)=2≥1`. |
| 25 | Theorem 1 proof, three sums (81-83) | CORRECT | U4 gives `G_0/(1+b_+G_0k)≤G_k≤G_0/(1+b_−G_0k)`. Both bounds are decreasing in `k`, so sum-integral comparison gives `ΣG_k²≤G_0²+G_0/b_−` and `Σ_{k<n}G_k≥b_+^{−1}log(1+b_+G_0n)`. The two exponential sums are geometric. |
| 26 | Theorem 1 proof, product (83) | CORRECT | `(1+x(N−k_m))(1+xk_m)=1+xN+x²k_m(N−k_m)≥1+xN` for `N≥k_m`. |
| 27 | Theorem 1 proof, window (83) | CORRECT | In the window: `K′G_k²≤K′G_0G_k≤λG_k/4`; `K′G_ke^{−βk}≤λG_k/4` for `k≥k_β`; `K′G_ke^{−β(N−k)}≤λG_k/4` since `N−k>k_β`. Sum `≤3λG_k/4`. |
| 28 | Lemma 2 (85-87) | CORRECT | For `Y` on the segment and unit `u`, `ζ↦ρ(Y+ζu)` is holomorphic and bounded by `M` on `\|ζ\|<r`; Cauchy gives `\|Dρ(Y)u\|≤M/r`; integrate along the segment. The involution plays no role in the proof: the bound holds for any two points `X,X′` whose segment has a bounded holomorphic `r`-neighbourhood. |
| 29 | Import claim for (1): "The imported one-loop flow of `CN1.md` §§3–5 gives increment `hG_kq²F(v,c)`" (55) | CORRECT | `CN1.md` line 69 (in its §4, display (OL)) reads "`P(v,c)&={4v^2+3vc+c^2\over6\pi^2c(v+c)^2}`", with flow `v_a'=Gq_a^2P(v_a,c)(c-v_a)` per unit log-scale (line 67). Then `P(c−v)=c²(4s²+3s+1)·c(1−s)/(6π²c·c²(1+s)²)`, which is (1). One RG step has log-length `h`, so the increment is `hGq²F`. `CN1.md` line 101 uses the same `F=P(c−v)` and `Λ=−∫_0^1∂_vF(v_2+tΔ,c)dt`; this equals the file's `c^{−1}∫_0^1\|F_s′\|dt`. The import is conditional, as the file says (line 62). |
| 30 | Remark on prior steps (89) | CORRECT | `CN1_REFEREE.md` line 204, item 36: "If `ρ₂(v₁,v₂,·) = ρ₁(v₂,v₁,·)` and `ρ₁` has Lipschitz constant at most `KG^2/2` in `(v₁,v₂)` for the `ℓ^1` norm, then `\|ρ₁ − ρ₂\| ≤ KG^2\|Δ\|`." That is the Lipschitz-to-pair step. Lemma 2 supplies the Lipschitz constant `M/r` from a size bound. `CN1.md` Theorem 3 (lines 119-127) is the continuous-flow use. "Neither supplies U2" is right. |
| 31 | Lemma 3a, statement (91-96) | CORRECT | Matches draft line 197-199. Only the lower half of U4 (`b_−`) is used. |
| 32 | Lemma 3a, proof (98) | CORRECT | The moves are convex combinations because `hG_kq_a²P≤hG_0p̄≤1` and `hG_kΣ_bn_bq_b²R≤1` (`G_k≤G_0` by U4; `P,R≥0`). Then `D_{k+1}≤D_k+2K(G_k²D_k+φ_k)`. Grönwall with `Π(1+2KG_j²)≤e^{2K(G_0²+G_0/b_−)}` gives `D_k≤D̄`. Each endpoint moves by at most `KΣ_j(G_j²D_j+φ_j)≤K[(G_0²+G_0/b_−)D̄+Φ]≤m_0/2`. Induction closes because `p̄` is a maximum over `B′²`. |
| 33 | Remark after Lemma 3a (100) | CORRECT | `CN1.md` Theorem 3 proof: "Dini estimates give `D⁺M≤KG²D+f` and `D₊m≥−KG²D−f`. Grönwall yields `D≤e^a(D(0)+2F)` ... Hence the solution stays in `[m(0)/2,M(0)+m(0)/2]⊂B′`". Lemma 3a is its discrete form. U2 constrains only the `v_1` line, so U2-U4 say nothing about the photon line `c` or the common mode. U5 is independent. |
| 34 | Theorem 3, statement (102-104) | CORRECT | Two notes. (a) R1″-MOD[d] is written with `(1+G_0k)^{−γ}`; the theorem gives `(1+b_+G_0k)^{−γ}`. Add the step `(1+b_+G_0k)^{−γ}≤max(1,b_+^{−γ})(1+G_0k)^{−γ}` (edit E4). (b) The enlargement "at least `2k_m`" is harmless but not needed (GAP G7). |
| 35 | Theorem 3 proof, difference identity (106) | CORRECT | U1 gives `[R_k(X)]_{v_2}=[σR_k(X)]_{v_1}=[R_k(σX)]_{v_1}`; σ swaps `v_1,v_2` and fixes `G,c` (Definition 2). U2 at `X_k` and at `σX_k` and the definition of `Λ` give `Δ_{k+1}=(1−hG_kΛ_k)Δ_k+ρ(X_k)−ρ(σX_k)`. |
| 36 | Theorem 3 proof, hypotheses of Theorem 1 with `K_1` (106) | CORRECT | `0≤1−hG_kΛ_k≤1−λG_k` by `hG_*Λ_max≤1` and U5. Lemma 2 gives the bracket `≤(M_k/r)(2\|Δ_k\|+E_k)`. For `G_k≤1`, `η_k≤3G_k`, so the `E_k` coefficient `M_k/r≤3KG_0/r≤1`. The `\|Δ_k\|` coefficient is `≤1−λG_k+K_1η_k` (bulk) and `≤1+K_1G_k` (threshold), as `K_1≥2K/r`. U3 holds with `K_1≥K`. |
| 37 | Theorem 3 proof, `δ_0` bound (106) | CORRECT | `δ_0≤(1+κK)\|Δ_0\|≤(1+K)κ\|Δ_0\|` as `κ≥2`. |
| 38 | Theorem 3 proof, intermediate `k` and `C_*` (106) | CORRECT | Every sentence is true. The repair is not needed: Theorem 1's own constant works at every `k≤N` (referee closure in GAP G7). |
| 39 | Scope remark after Theorem 3 (108) | CORRECT | `LZ1I.md` line 188, Theorem 12: "If `a+b=λκ₀/(1+Wκ₀ℓ)` ... then `Δ(ℓ)=Δ(0)(1+Wκ₀ℓ)^{−λ/W}`. At `ℓ=log(1/(a_lat\|k\|))`, a nonzero difference is not `O((a_lat\|k\|)^p)` for any `p>0`." Theorem 3's bound has the same form in `k`. |
| 40 | Proposition 4 (112-114) | CORRECT | Cauchy on `\|z\|=r′<r`, then `r′→r`: `αN−β≤\|F′(0)\|≤B/r`. Notation: `F`, `B` and `β` here clash with the drag `F`, the speed set `B` and the rate `β` of UB″ (edit E3). |
| 41 | Corollary 4′ (116-120) | CORRECT | `∂_zΔ_N\|_0=hN[F(v_1,1)−F(v_2,1)]+hΣ_k[F(v_1,1)ε_k^1−F(v_2,1)ε_k^2]=−hΛ_0NΔ_0+e`, `\|e\|≤h(\|F(v_1,1)\|+\|F(v_2,1)\|)c_1`. Proposition 4 with `α=hΛ_0`, `β=\|e\|/\|Δ_0\|` bounds `N`. The input is the one-loop coefficient (imported, conditional), as the title says. |
| 42 | Remark on matching and the coupling line (122) | CORRECT | If `1/G_N=1/z+S_N+g_N(z)` with `g_N(z)=O(z)` for each `N`, then `G_N=z−S_Nz²+O(z³)`; Cauchy gives `\|S_N\|≤B/r²`. No uniformity of the `O(z)` term in `N` is needed. |
| 43 | Corollary 4″, coupling part (124, 126) | CORRECT | `\|G_N′(0)\|=1≤B/r`. For `\|z\|≤r/2`, `\|G_N″\|≤2B/(r/2)²`. Taylor: `\|G_N(x)−x\|≤4Bx²/r²≤x/2` for `x≤r²/(8B)≤r/2`. U4 gives `0<G_N(x)≤x/(1+b_−xN)<x/2` once `N>1/(b_−x)`. Realness is not needed: `\|G_N(x)\|≥x/2` already contradicts U4. This part uses U4, whose `b_−>0` is the sign of the one-loop vacuum polarisation; it is a UB″ hypothesis, not an imported number. |
| 44 | Corollary 4″, pair part (124, 126) | CORRECT | `F_N(0)=1` gives `B≥1`; `\|F_N′\|≤2B/r` on `\|z\|≤r/2`; `\|F_N(x)−1\|≤2Bx/r≤1/2` for `x≤r/(4B)≤r/2`. So `\|F_N(x)\|≥1/2`, against `C(1+xN)^{−γ}→0`. This part uses no coefficient at all: only the normalisation `Δ_N(0)=Δ_0` and the decay that R1″-MOD[d] asserts. Realness on the real axis is again not needed. |
| 45 | Remark on scope of the obstruction (128) | CORRECT | The draft's line 237 sentence "no proof can establish UB″ (or any bound on the scale-`N` speeds) by analytic bounds on a fixed complex disc" is true only for bounds that yield a bounded holomorphic `G_N` or `Δ_N/Δ_0` with the stated normalisation; line 128 says exactly that. |
| 46 | Proposition 5, statement and set (130-136) | CORRECT | `Re(1/G)≥1/r_0` with `G=x+iy` is `x²+y²≤r_0x`, the closed disc `\|G−r_0/2\|≤r_0/2`, minus `0`. |
| 47 | Proposition 5 proof, the `w`-step (138-139) | CORRECT | `\|u\|≤b\|G\|+K\|G\|²≤(b+K)\|G\|≤1/4` (as `\|G\|≤r_0≤1`). `w_{k+1}=w_k/(1−u)`, so `w_{k+1}−w_k−b=−R_k/G_k²+u²/((1−u)G_k)`, bounded by `K\|G_k\|+(4/3)(b+K)²\|G_k\|≤C_0\|G_k\|≤C_0r_0≤b/2`. `G_{k+1}=G_k(1−u)≠0`. |
| 48 | Proposition 5 proof, (i) and (ii) (140) | CORRECT | (i) `\|G_k\|≤1/Re w_k≤r_0` keeps the hypothesis alive; induction. (ii) Real `w` rises by `[b/2,3b/2]` per step from `−1/t≤−1/r_0`; after `⌈2/(bt)⌉` steps `w≥0`; a jump across `(−1/r_0,1/r_0)` needs `2/r_0≥8(b+K)>3b/2`. |
| 49 | GAP TD (142) | CORRECT | Gap real (section 2, G8). |
| 50 | Lemma 6, statement (146-147) | CORRECT | Matches draft lines 260-263. |
| 51 | Lemma 6 proof, Clifford step and trace (149-150) | CORRECT | `\not a\not p=2(p·a)−\not p\not a` gives `X²=2(p·a)X−p²a²`. Then `tr X⁴=4(p·a)²tr X²−4(p·a)p²a²tr X+p⁴a⁴tr 1` with `tr X=4p·a`, `tr X²=8(p·a)²−4p²a²`, `tr 1=4`. Result `32(p·a)⁴−32(p·a)²p²a²+4p⁴a⁴`. |
| 52 | Lemma 6 proof, moments, substitution, Fubini (151) | CORRECT | `E g_1²=1=4E ω_1²`; `E g_1⁴=3=24E ω_1⁴` (`E R⁴=E(χ²_4)²=8+16`). After `p′=p_v` (Jacobian `v^{−3}`) and `p′=ρω`, the integrand is `ψ(ρ𝒩′(ω))ρ^{−1}T(ω)dρdω`. The substitution `t=ρ𝒩′(ω)` uses `𝒩′(ω)>0`. `∫\|T\|<∞` and `∫\|ψ\|dt/t<∞` give Fubini. Average `\|Ã\|⁴(4−8+4)=0`. `[check]` not rerun; the hand proof is complete. |
| 53 | Remark on the box term and GAP (153) | CORRECT | The identification needs "when integrable": for a pure ultraviolet cutoff with `χ(0)=1`, `∫χ⁴dt/t` diverges at `t→0` (the massless box is infrared logarithmic). The GAP is real but smaller than stated (section 2, G10). |
| 54 | Quartic forms allowed by symmetry (155) | CORRECT | `Q(e_1)=1−½`; `Q(½(1,1,1,1))=¼−½`. `Q` is of the form `a_1A_0⁴+a_2ΣA_i⁴+a_3(ΣA_i²)²+a_4A_0²ΣA_i²`, which spatial cubic symmetry, time reflection and charge conjugation allow. The file's "cubic symmetry" should read "spatial cubic symmetry and time reflection" (M″ is not hypercubic when `v_a≠1`). |
| 55 | Attack A and its GAP (159) | CORRECT | Failure at Corollary 4″ is proved for any version that yields a bounded holomorphic `Δ_N/Δ_0` (or normalised `G_N`) on a fixed disc. The GAP is real (G5). The draft's supporting reason (draft line 289, "every local four-fermion term has scaling dimension six, so the fermionic localisation at scale `k` contains no term that could carry a running `G_k`") is wrong in general; CN1MOD rightly does not repeat it. See G5. |
| 56 | Attack B, B1, B2 and GAP (161) | CORRECT | B1 and B2 are named unpassed steps; the draft records a written partial attempt (axial gauge plus a Neumann series inside one block, draft line 301). The GAP is real (G6). Read "at each scale" as governing all three items of the GAP sentence: for the whole fermion integral at fixed `A`, exact lattice Ward identities do follow from covariance of `S_F` (section 2, G6). |
| 57 | Attack C, C1 and GAP (163) | ERROR | "If a quartic polynomial is negative along a real field direction, exp(−V) grows quartically there" is false as written: along that direction `exp(−V)` grows like `exp(a\|A\|⁴)`, the exponential of a quartic. Fix: "`\|exp(−V)\|` grows like `exp(a\|A\|⁴)` there". The draft (line 311) has it right ("`e^{c\|A\|⁴}`"). The rest is correct; the GAP is real (G9). |
| 58 | Earlier attacks 1-4 (165) | CORRECT | Matches `CN1_OUTLINE.md` 295-298 as quoted by the digest. |
| 59 | "Already in the repository" (167) | CORRECT | `CN1.md` Theorems 1-3 and Proposition 4 and `LZ1I.md` Theorems 11-12 are as described (items 29, 33, 39). The `docs/` notes are cited through the digest, as the line says. |
| 60 | Framework bridge, five items (169) | INCOMPLETE | Each item is real and open. The list says "at least", so it is not false. Missing: (a) the R2 inputs that `CN1.md` line 54 already names, "Required inputs include a Clifford photon GA1-5-Φ, R-CS, ZM1-I1[INV], Y2-W, VC1 and a specified plaquette class", and R2-b, R2-c; Y2-W and the plaquette class appear nowhere in CN1MOD. (b) A matter item: the law's light charged modes must realise M″'s species (Dirac content, charges `q_a`, multiplicities, node and tensor structure). Label: R2-a/H-TICK is the tick-loop coefficient computation (`CN1.md` lines 54, 58); the reflection-positive transfer identification is ST1 route B (`TOE_ASSEMBLY.md` line 351, "reflection positivity of its Euclidean form"). Item (4) should name them as two inputs. Edit E7. |
| 61 | §6 statement of the four tests (173) | CORRECT | Same four tests as the lane brief. |
| 62 | Four-test row, M″ (177) | CORRECT | "P, C, P, C" is supported. Test 2 is C because boundary conditions and counterterm conditions are not fixed; see G2 for a closure of the free zero mode. |
| 63 | Four-test row, R1″-MOD[d] (178) | CORRECT | "C, P, P, C" is supported: it fixes the form of a target (test 1), and its window clause adds the `κE_k` structure that CN1's R1″-MOD does not state (test 4), although Theorem 1 shows that structure is needed for a one-step contraction. |
| 64 | Four-test row, UB″ (179) | CORRECT | The verdict is defensible. Note: each of U0-U5 and each term of `η_k` is used in Theorem 3 (items 35-37), so test 4 could be P; "not shown necessary or minimal" is not what test 4 asks. |
| 65 | Four-test row, TD (180) | CORRECT | "F as stated" is right: the clause "equivalently on a fixed disc of the running couplings" is not needed by Proposition 5 and is false as an equivalence (G8). Without that clause TD passes test 4. |
| 66 | Closing paragraph (182) | CORRECT | The supported version is exactly what items 33-55 confirm. |

---

## 2. The distiller's GAPs, one by one

**G1. Gauge sign (lines 9, 25). Real.** The draft's map gives the phase `exp(2ieq[χ(x+μ̂)−χ(x)])` on each hop (section 0). The file's repaired map `A_μ(x)↦A_μ(x)+χ(x)−χ(x+μ̂)` is right. No proof step used the wrong sign.

**G2. Torus covariance and zero modes (lines 9, 23). Real.** Repaired statement: on `Λ_T`, `C_{μν}(x−y)=δ_{μν}T^{−4}Σ_{k∈(2π/T)Z_T^4}e^{ik·(x−y)}/(\hat k^2+m^2)`. The Brillouin-zone integral is its `T→∞` limit. *Referee closure for the free zero mode.* For `D=m(p)+iΣ_μw_μ sin p_μ γ_μ` with real scalar `m(p)=μ+Σ_μw_μ(1−cos p_μ)`, the cross terms cancel and the anticommutators give `D^†D=m(p)²+Σ_μw_μ²sin²p_μ`. At `μ_a=0` this vanishes only at `p=0`. With periodic boundary conditions `p=0` is allowed, so the free massless kernel is singular. With antiperiodic boundary conditions in `x_0` (`p_0∈(2π/T)(Z+½)`) it is invertible for every `T`. This closes only the free case. Zero modes of the interacting measure at `μ_a≠0`, and uniformity in `T`, stay open as the file says.

**G3. UB″ unproved; sufficient, not equivalent (line 9). Real.** The draft's FINISH writes "UB″, equivalently (by Theorem 3) R1″-MOD[d]" (draft line 363). Theorem 3 proves one direction only. The file's line 108 states the supported version.

**G4. R1″-MOD[d] versus CN1's interpolated R1″-MOD (lines 9, 41, 108). Real.** `CN1.md` line 52 asks that "interpolated coefficients obey (OL+ρ) with the §5 bounds", and line 58 extends this to R1″. An interpolation of the discrete coordinates would need the class-`𝓡` bound (R-i), `|ρ_a|,|ρ_0|≤KG²D+f`, for every speed line, the photon line included. UB″ constrains only the `v_1` line (U2) and the box (U5). So UB″ does not give CN1's form, and no repair is available from UB″ alone.

**G5. "The asserted failure of every bare-coupling expansion" (lines 9, 159). Real.** What is proved is Corollary 4″: on any fixed disc, uniform in `N`, on which `Δ_N/Δ_0` is holomorphic, bounded, and `1` at `z=0`, the decay of R1″-MOD[d] fails. That uses no coefficient. What is not proved is that "integrate the photon, then expand in the fermions" must produce such a disc. The draft's reason (line 289) is that no fermionic local term can carry a running `G_k`, because local four-fermion terms have dimension six. That reason fails. Split the massive kernel as `D=Σ_{j≤N}D_j`, with `D_j` of range `L^j` and size `O(L^{−2j})`. At scale `j` the current `J=ψ̄γψ` scales as `L^{−3j}`, so `∫∫J D_j J` scales as `L^{8j}·L^{−2j}·L^{−6j}=1`. Each scale carries a marginal current-current coupling, which fermion bubbles renormalise. `CN1_OUTLINE.md` line 300 says the same of the massive kernel: it "keeps the marginal coupling across `N` scales". An expansion that renormalises these couplings is an expansion in running couplings, and Corollary 4″ does not reach it. So attack 2 in its massive form is not settled; the draft's FINISH line "Attack 2's failure for the massive case is now a theorem" is unsupported.

**G6. "The exact gauge-invariant block flow for the massive model" (lines 9, 161). Real. Referee closure, partial.** (i) For fixed real `A`, the change of variables `ψ↦e^{ieqχ}ψ`, `ψ̄↦e^{−ieqχ}ψ̄` has Jacobian one and maps `S_F(A)` to `S_F(A+χ−χ(·+μ̂))`. So the fermion integral at fixed `A` obeys exact lattice Ward identities, and `det D_{A−dχ}=det D_A` with `(dχ)_μ(x)=χ(x+μ̂)−χ(x)`. (ii) With `κ_μ=e^{ik_μ}−1`, the lattice Hodge Laplacian on 1-forms is `(δdA+dδA)_ν=|κ|²A_ν=\hat k^2A_ν`. So the covariance `δ_{μν}/(\hat k^2+m^2)` equals `(Δ_1+m²)^{−1}` and commutes with the projections onto exact, coexact and harmonic forms. Hence `A=A_ex+A_rest` with independent Gaussian parts. (iii) For every gauge-invariant fermionic observable `O`, the inner integral is a function of `A_rest` only. So M″ equals the model with covariance `(1−P_ex)/(\hat k^2+m^2)`; the exact part decouples. The remaining weight is gauge invariant on orbits, but its mass term `m²|A_coex|²=m²⟨F,Δ_2^{−1}F⟩` is nonlocal in the curvature `F=dA`. So a gauge-covariant block RG faces either a nonlocal invariant photon action or a Stueckelberg field, as the file says. The speed coordinates are gauge-fixed charged data and are not covered by (iii). This narrows G6 and does not close it.

**G7. "The last-scale prefactor ... needs the correction given below" (lines 9, 106). Not real.** The draft's claim (line 215) that Theorem 1's constant `C` works at every `k≤N` is true. *Referee closure.* Fix `0≤k≤N` and run Theorem 1's product over the first `k` steps, with the original `N`-dependent `η`. Let `k′=min(k,N−k_m)` count the bulk steps; at most `k_m` threshold steps remain. The three `η`-sums over `j<k` are bounded as in Theorem 1, so `δ_k≤exp[K′(G_0²+G_0/b_−+2G_0/(1−e^{−β})+k_mG_0)](1+b_+G_0k′)^{−λ/b_+}δ_0`. If `k′=k`, this is at most `C(1+b_+G_0k)^{−λ/b_+}δ_0`. If `k′=N−k_m<k` and `k≥k_m`, then `k′≥k−k_m` and `(1+x(k−k_m))(1+xk_m)≥1+xk` give the same bound. If `k<k_m`, the factor `(1+b_+G_0k_m)^{λ/b_+}(1+b_+G_0k)^{−λ/b_+}≥1` absorbs everything. So `|Δ_k|≤C(1+K)κ(1+b_+G_0k)^{−λ/b_+}|Δ_0|` with Theorem 1's `C` (with `K_1`). The file's enlarged `C_*` is also valid. `[check]` (`/tmp/toe-CN1MODref/check.py`, part d): 300 random parameter sets, `N` up to 3000, recursions run with equality; the largest ratio `δ_k/[C(1+b_+G_0k)^{−λ/b_+}δ_0]` over all `k` was `0.974`. Guide only.

**G8. GAP TD (lines 9, 142). Real.** Proposition 5(i) gives one direction: if `Re(1/G_0)≥1/r_0`, every `G_k` lies in the tangent disc `Re(1/G)≥1/r_0+bk/2`. The converse fails. A fixed running disc `|G|≤r_0` contains `(−r_0,0)`, and Proposition 5(ii) shows a real orbit starting at `−t` leaves it within `2/(bt)+1` steps. So the set of bare couplings whose orbit stays in a fixed running disc for `N` steps depends on `N`; it is not the tangent disc for any fixed `N`. Repaired statement: "On the tangent disc of the bare coupling, the abstract recursion keeps every running coupling in a fixed disc; per-step bounds posed on that running disc therefore compose over all `N` steps for the scalar recursion." Proposition 5 says nothing about the other UB″ coordinates, whose U2 neighbourhoods live in `𝔛_k`. Sufficiency of TD for UB″ stays open.

**G9. "The claimed necessity of quartic positivity in every BBS-type scheme" (lines 9, 163). Real.** A referee observation supports the GAP. For real `A`, `|U_{aμ}|=1`, and `‖½(1±γ_μ)‖=1`, so `‖D_a(A)‖≤|μ_a|+3Σ_μw_{aμ}` for every real `A`. Hence `|det D_a(A)|≤(|μ_a|+3Σ_μw_{aμ})^{4T^4}` uniformly in real `A`. The fermion-induced weight of M″ never grows like `exp(a|A|⁴)` along a real direction. A negative quartic in a localised polynomial `V_k(A)` is a property of polynomial localisation in the non-compact variable `A`, not of M″'s weight. This does not show that some scheme avoids C1. The draft's own suggested repair (localisation in compact variables) still meets B1, as the draft says.

**G10. The quartic identification needs the cutoff prescription (lines 9, 37, 153). Real, and narrower than stated. Referee closure.** Suppose the continuum propagator of speed `v` is split multiplicatively, `S=Σ_jχ_j(𝒩(p))S_0(p)` with `S_0=(i\not p_v)^{−1}` and one homogeneous `𝒩`, and the scales are integrated from the ultraviolet down. For a constant field, the vertex carries no momentum, so all four propagators of a box carry the same `p`. After the scales `j≤k` are integrated (low modes at zero), the quartic vacuum term is the box with `ψ=χ_{≤k}⁴`, `χ_{≤k}=Σ_{j≤k}χ_j`. The increment at step `k` is the box with `ψ=χ_{≤k}⁴−χ_{≤k−1}⁴`. This sum contains every mixed-scale assignment of the four propagators. Whenever `∫|ψ|dt/t<∞` (for example, when the increment is supported in a shell), Lemma 6 gives zero. So "mixed propagators" are covered for such splits. What stays outside Lemma 6: lattice propagators (the `sin p_μ` symbol and the Wilson term), the Peierls seagull vertices, and splittings that are not a multiplicative function of one homogeneous `𝒩`. The lattice sign stays open, as the file says.

---

## 3. Decisions on the items the brief names

**3.1 Theorems 1 and 3, Lemma 2: correct.** UB″ implies R1″-MOD[d] for M″ with constants independent of `N` (items 22-38). Two precisions. First, the scale-by-scale contraction is of `δ_k=|Δ_k|+κE_k`, with factor `1−λG_k/4`, in a window `k_β≤k<N−max(k_β,k_m)` whose margins do not depend on `N`. The file states this correctly; `|Δ_k|` alone has only the power bound at every `k`. Second, Theorem 1's own constant serves every `k≤N` (G7). The bound reaches R1″-MOD[d]'s `(1+G_0k)^{−γ}` form after the one-line conversion of edit E4.

**3.2 Positivity of the one-loop drag at every speed ratio: correct.** From `CN1.md` (OL), `P(v,c)=(4s²+3s+1)/(6π²c(1+s)²)>0` and `F_s′=−4s²(s+3)/(6π²(1+s)³)<0` for every `s=v/c>0`. So `Λ≥Λ_min>0` on every compact box of positive speeds (items 20, 21, 29). The coefficients are imported and conditional, as the file says. `[check]` part a: `F_s′` agrees with a numerical derivative to `3·10^{−10}`, and `|F_s′(1)|·3π²=1`.

**3.3 Proposition 4, Corollaries 4′ and 4″: correct.** The coefficient-free claim holds in this exact form. *If, for every `N`, `z↦Δ_N(z)/Δ_0` is holomorphic on `|z|<r`, bounded by `B` there, and equal to `1` at `z=0`, then `|Δ_N(x)|≥|Δ_0|/2` for all `N` and all `x∈[0,r/(4B)]`; so the decay `|Δ_N(x)|≤C(1+xN)^{−γ}|Δ_0|` fails at every `x∈(0,min(G_*,r/(4B))]` once `N` is large.* No one-loop coefficient enters, and realness on the real axis is not needed (item 44). The coupling half of 4″ uses U4, a UB″ hypothesis. Corollary 4′ uses the imported coefficient, as its title says. Proposition 4 is Cauchy's estimate. The obstruction concerns bounded holomorphic coordinates on a fixed disc. It says nothing about the real-axis flow and does not show that every bare-coupling representation has those properties (G5).

**3.4 Proposition 5: correct** (items 46-48). The tangent disc is invariant for the abstract scalar recursion; negative real couplings leave every small disc. Its use for UB″ is open (G8).

**3.5 Lemma 6: correct** (items 50-52), for every `v>0`, every continuous, positive, positively 1-homogeneous `𝒩`, and every measurable `ψ` with `∫_0^∞|ψ|dt/t<∞`. It is a continuum statement. It covers per-step totals of multiplicative one-norm splits, mixed scales included (G10). It does not cover lattice propagators or seagulls. `[check]` parts b, c: the trace identity holds to `3·10^{−13}` at 200 random points; Monte Carlo sphere averages at `v∈{0.5,1,2}` are `0.004, 0.005, 0.006` with standard error `0.0045` each.

**3.6 The three failed attacks on UB″.** `CN1_REFEREE.md` line 250 (item 59) rules that attacks "distinct in method" which "fail at different named steps" meet the stopping rule "a lemma on which three distinct attacks failed", and that "failed attacks as recorded, not impossibility theorems" is the right strength. CN1MOD's attacks meet that standard and go past it: A's failing step is a theorem, and B and C record written partial results.
- **A fails at Corollary 4″, a proved step,** for every version that delivers a bounded holomorphic `Δ_N/Δ_0` (or normalised `G_N`) on a fixed bare-coupling disc. Its new step relative to attack 2 on file is the domain of analyticity, not kernel summability. Broader claims (every bare-coupling expansion fails; attack 2 settled in the massive case) are not proved (G5).
- **B fails at B1, an unpassed step,** with a recorded partial attempt (one-block axial gauge and Neumann series). B also carries G6: M″'s Gaussian weight is not gauge invariant, so a covariant block flow needs a Stueckelberg field or a nonlocal invariant photon action first.
- **C fails at C1, an unpassed step,** with recorded partial results (the list of marginal coordinates, Lemma 6). Its claimed necessity of a positive quartic is not proved (G9).

The three attacks are distinct from one another (different first moves, different stops) and from attacks 1-4. So UB″ is a lemma on which three named attacks failed. B1 and C1 are not impossibility results, and A refutes a strategy, not UB″ or R1″-MOD[d].

**3.7 The five items between M″ and a framework law: incomplete** (item 60). Each item is real and open. The list should also carry the inputs `CN1.md` line 54 names for R2 (R-CS, ZM1-I1[INV], Y2-W, VC1, a specified plaquette class; R2-b, R2-c), and a matter item. Item 4 should separate R2-a/H-TICK (tick-loop coefficients) from the reflection-positive transfer identification (ST1 route B).

---

## 4. Required edits

Required for freeze:

- **E1 (item 57, ERROR).** Line 163: replace "exp(−V) grows quartically there" by "`|exp(−V)|` grows like `exp(a|A|⁴)` there".
- **E2 (items 3, 38; G7).** Line 9: delete "The last-scale prefactor in the draft's proof of Theorem 3 needs the correction given below." Line 106: replace "This also repairs the draft's unsupported assertion ..." by a statement that Theorem 1's constant with `K_1` works at every `k≤N`, with the closure of G7. Keeping `C_*` as a valid larger constant is optional.
- **E4 (item 34).** Theorem 3: add `(1+b_+G_0k)^{−γ}≤max(1,b_+^{−γ})(1+G_0k)^{−γ}`, so the bound has R1″-MOD[d]'s form.
- **E5 (item 44).** Corollary 4″: replace "at fixed `x>0`" by "at a fixed `x∈(0,r/(4B)]`" (and `x∈(0,r²/(8B)]` for the coupling half). Optionally drop "real on the real axis"; it is not used.
- **E7 (item 60).** Line 169: add the R2 inputs of `CN1.md` line 54 (R-CS, ZM1-I1[INV], Y2-W, VC1, a specified plaquette class; R2-b, R2-c) and a matter item (the law's light charged modes realise M″'s species: Dirac content, charges, multiplicities, node and tensor structure). Split item 4 into R2-a/H-TICK and the transfer identification of ST1 route B. Keep "at least".

Recommended:

- **E3 (items 17, 40, 44).** One meaning per symbol. Rename the contraction constant `c` of R1″-MOD[d] (it clashes with the photon speed), the `F`, `B`, `β` of Proposition 4 and the `F_N` of Corollary 4″ (they clash with the drag `F`, the speed set `B` and the rate `β`), the `B′` of Lemma 3a (it clashes with UB″'s `B′`), and the `K` of Proposition 5.
- **E6 (item 54).** Line 155: "Cubic symmetry" becomes "Spatial cubic symmetry, time reflection".
- **E8 (item 56; G6).** Line 161: write "at each scale of the chosen RG". Optionally add G6's partial closure: exact Ward identities hold for the fermion integral at fixed `A`, and the exact part of `A` decouples from gauge-invariant observables.
- **E9 (item 53; G10).** Line 153 and Definition 7: narrow the GAP. Per-step totals of multiplicative one-norm splits, mixed scales included, are covered. What remains is lattice propagators, Peierls seagulls and other splittings.
- **E10 (item 8; G2).** Line 23: fix a boundary condition, for example antiperiodic in `x_0`. The free massless kernel is then invertible for every `T`.
- **E11 (G5).** Line 159: optionally record that a scale-split massive kernel carries a marginal current-current coupling at each scale, so an "integrate the photon" plan can run a coupling.
- **E12 (item 5).** Line 13: at freeze, replace "No independent referee has checked this file" by a pointer to this report.

---

## 5. Open statements to carry by name

From this part:
- **UB″.** Three named attacks failed: A at Corollary 4″ (proved, for fixed-disc versions), B at B1, C at C1.
- **R1″-MOD[d]** for M″. Implied by UB″ (Theorem 3); not shown equivalent.
- **R1″-MOD** in `CN1.md`'s interpolated form. It needs (R-i) on every speed line, the photon line included, which UB″ does not contain (G4).
- **B1**, **B2**, **C1** with the lattice sign of the generated quartic photon coupling.
- **TD-UB″**: whether UB″ can be posed and proved on the tangent disc (G8).
- **M″-T**: uniformity in `T` and zero modes of the interacting measure (G2; the free zero mode is closed there).
- The discrete spread theorem for `n` species with unequal charges.

Inherited, unchanged: R1-MOD, R1′, R1-OBS, CN1-T, CN1-T(r), R2 with R2-a/H-TICK, R2-b/H-TRANSFER and R2-c, R3, R-P, H-PHOTON, H-THR, H-FIN, GB1-U1, GA1-5-Φ as a cone, VC1, ZM1-I1[INV]. Add, from `CN1.md` line 54: R-CS, Y2-W and the plaquette class.

---

## 6. Freeze recommendation

**Freeze `CN1MOD.md` after edits E1, E2, E4, E5 and E7.** E3, E6 and E8-E12 are recommended and do not block. No edit changes the content of a theorem. The two ERROR items are a wording slip (E1) and a GAP that is not a defect (E2). The one INCOMPLETE item is the bridge list (E7), which already says "at least". Every proof in the file was re-derived and holds under its displayed hypotheses. The file's status stays as it states it: conditional mathematics, not a construction of the RG, not a law, not a prediction. The proposed CN1 amendment remains not adopted. The supported line, for the lead and the owner to judge, is: "UB″ plus the displayed smallness implies R1″-MOD[d] (`CN1MOD` Theorem 3). Attacks A, B, C on UB″ failed at Corollary 4″ (proved, for fixed-disc versions), B1 and C1."

---

## Prior work used

All paths are in this folder at commit `37bc873ee`, unless `origin/main` is named. `origin/main` was read with `git show` after `git fetch -q origin main`, at `f5af11cd0` (the commit the draft records). No other branch was read.

| Prior result | Path and lines | Use here |
|---|---|---|
| The digest | `prior/CN1MOD.md`, all 79 lines; SHA-256 `6df25381...85c2`, as `CN1MOD.md` line 13 records | Map of prior work |
| One-loop flow (OL), with `P,R,S` | `CN1.md` lines 65-72 (the formula at line 69) | Items 20, 29; section 3.2 |
| `F=P(c−v)` and `Λ=−∫∂_vF` in the proof of Theorem 2 | `CN1.md` line 101 | Item 29 |
| Class `𝓡` and Theorem 3 (R1-C) with its box step | `CN1.md` lines 109-127 | Items 33, G4 |
| R1, R1-MOD, R1-OBS; R2 and its required inputs; R3, R-P; R1″-MOD, H-PHOTON, H-TICK | `CN1.md` lines 52, 54, 56, 58 | Items 60, G4; sections 3.7, 5 |
| Item 36: exchange symmetry plus a Lipschitz bound gives the pair bound | `CN1_REFEREE.md` line 204 (table row line 72) | Item 30 |
| Item 59: the standard for three failed attacks | `CN1_REFEREE.md` line 250 | Section 3.6 |
| Attacks 1-4 and the massive-kernel sentence | `CN1_OUTLINE.md` lines 295-300 | Items 58, G5 |
| Theorems 11-12 (integrated drag; marginal rate is not a power) | `LZ1I.md` lines 180-190 | Item 39 |
| R-CS^str as a named, unadopted working candidate | `TOE_ASSEMBLY.md` line 225 | Item 60 |
| ZM1-INV | `TOE_ASSEMBLY.md` lines 248-252 | Item 60 |
| ST1 route B, "reflection positivity of its Euclidean form" | `TOE_ASSEMBLY.md` line 351 | Item 60 |
| GB1-U1 as an open input | `TOE_ASSEMBLY.md` line 453 | Item 60 |
| Peierls note: status line, remainder line, higher loops open | `origin/main:docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 7, 269, 503 | Item 59 (spot check) |
| K note: "does not prove an invariant RG neighborhood" | `origin/main:docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` line 86 | Item 59 (spot check) |
| Referee format | `LW1_REFEREE.md` lines 1-80; head format `Y2W_DRAFT.md` lines 1-25 | Format only |

**Prior work the digest missed.** (a) `CN1.md` line 54 lists the inputs R2 requires: "a Clifford photon GA1-5-Φ, R-CS, ZM1-I1[INV], Y2-W, VC1 and a specified plaquette class". The digest quotes line 54 only for tick loops, threshold transfer and forcing. This list bears on CN1MOD's bridge (E7). (b) `CN1_OUTLINE.md` line 300: the massive kernel "removes the long-range tail but keeps the marginal coupling across `N` scales". This bears on attack A (G5). (c) `TOE_ASSEMBLY.md` line 351, ST1 route B, is where a reflection-positive Euclidean form of the update is already asked for. This bears on bridge item 4. The draft already added `CN1_REFEREE.md` item 36.

**Not read.** The quartet note, the Weyl note, the exchange-matrix note and the Hall note; the consolidation branches; the literature. CN1MOD uses none of them as a proof step. No citation is load-bearing here.

---

## 7. Four-test check of this report's own proposals

This report proposes one specification and no reading. Nothing is adopted.

| Proposal | 1 | 2 | 3 | 4 | Reason |
|---|---|---|---|---|---|
| E10: antiperiodic boundary condition in `x_0` for M″ | P | P | P | P | (1) M″ is a supplied test model; the condition fixes no part's target. (2) One stated condition; nothing can be added to it. (3) It removes only the free zero mode at `p=0`; it settles no physics question, and the bounds asked for are uniform in `T` anyway. (4) It replaces one boundary condition by another and adds no constant. |

The other edits (E1-E9, E11, E12) correct wording, notation, constants or cross-references. The repaired TD sentence of G8 is a statement of what Proposition 5(i) proves, not a reading.

---

## FINISH

**Proved here (referee closures; author-side, unrefereed).**
- Every theorem, lemma, proposition and corollary of `CN1MOD.md` holds under its displayed hypotheses. 66 items: 63 CORRECT, 2 ERROR, 1 INCOMPLETE.
- G7: under UB″, Theorem 1's constant `C` (with `K_1`) bounds `|Δ_k|` at every `k≤N`. The draft's Theorem 3 constant needed no correction.
- Corollary 4″ holds without its realness hypotheses (item 44). Its pair half uses no coefficient (section 3.3).
- G2: with antiperiodic boundary conditions in `x_0`, the free massless Wilson kernel is invertible on every torus, since `D^†D=m(p)²+Σ_μw_μ²sin²p_μ>0` for `p≠0`.
- G6, partial: the fermion integral at fixed `A` obeys exact lattice Ward identities; the exact part of `A` is an independent Gaussian and decouples from every gauge-invariant fermionic observable; the remaining weight has the nonlocal mass term `m²⟨F,Δ_2^{−1}F⟩`.
- G9: for real `A`, `|det D_a(A)|≤(|μ_a|+3Σ_μw_{aμ})^{4T^4}`. M″'s fermion-induced weight never grows like `exp(a|A|⁴)` along a real direction.
- G10: Lemma 6 covers per-step totals of multiplicative one-norm splits, mixed scales included.

**Counterexamples.**
- The draft's gauge map (draft line 107) leaves the phase `exp(2ieq[χ(x+μ̂)−χ(x)])` on each hop (G1; `CN1MOD.md` already repairs it).
- The draft's reason that an "integrate the photon" expansion cannot run a coupling (draft line 289) fails: a scale-split massive kernel carries a marginal current-current coupling at every scale (G5).
- `CN1MOD.md` line 9's claim that the draft's Theorem 3 prefactor needed correction is false (G7).
- The TD equivalence "tangent disc in the bare coupling, equivalently fixed disc in the running couplings" is false: a negative real orbit leaves every fixed running disc (Proposition 5(ii); G8).

**Open by name.** UB″ (attacks A, B, C failed at Corollary 4″, proved for fixed-disc versions, at B1 and at C1); R1″-MOD[d]; R1″-MOD in CN1's interpolated form; B1; B2; C1 with the lattice quartic sign; TD-UB″; M″-T; the discrete unequal-charge `n`-species spread theorem. Inherited: R1-MOD, R1′, R1-OBS, CN1-T, CN1-T(r), R2 with R2-a/H-TICK, R2-b/H-TRANSFER, R2-c, R3, R-P, H-PHOTON, H-THR, H-FIN, GB1-U1, GA1-5-Φ as a cone, VC1, ZM1-I1[INV], R-CS, Y2-W, the plaquette class.

**What changes downstream.**
- `CN1MOD.md`: apply E1, E2, E4, E5 and E7, then freeze (section 6).
- CN1: nothing is adopted. Supported line for the lead and the owner to judge: "UB″ plus the displayed smallness implies R1″-MOD[d] (`CN1MOD` Theorem 3); attacks A, B, C on UB″ failed at Corollary 4″ (proved, for fixed-disc versions), B1 and C1."
- Rung 2 bridge: the list gains the `CN1.md` line 54 inputs and a matter item (E7).
- LZ1: nothing new. The rate is a power of `N`, as `LZ1I.md` Theorem 12 says a marginal drag gives.
- Owner: nothing adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
