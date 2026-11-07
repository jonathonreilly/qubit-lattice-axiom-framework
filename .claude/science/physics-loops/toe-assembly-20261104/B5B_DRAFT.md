# B5(b), pass 1 (long draft): frames on cells of L_cube

Written 2026-11-05 by a Claude Opus 5.5 subagent, as pass 1 of the open item B5(b) of part LW1 of the TOE assembly (method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

Section 7 was added 2026-11-05 by a Claude Opus 5.5 subagent: it proves B5b-T (whole-update invariance gives the same mode image `U(1)^8`) and answers B5b-E with a counterexample and a classification.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (scripts outside the repo, in `/private/tmp/claude-501/`, under 100 MB, under a minute); a check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (same commit as `origin/claude/toe-assembly`) | `da0ec19348` |

Files read at that commit, by line: `LW1.md` lines 1-260 (section 0 status, section 1 definitions, section 2, section 3.1, section 3.2 with B2-B5) and lines 480-503 (the GAP list, GAP B5(b) at line 492); `LW1_REFEREE.md` lines 45-46, 77, 165-178 (the check of the `U(1)^8` counterexample at line 171); `CH1_DRAFT.md` lines 1-40 (head and the lead note at line 23) and lines 240-275 (Theorem S2, Theorem S3 at line 256, the PS-5 paragraph at line 263); `LW1_DRAFT.md` lines 46-50, 109, 244-271 (the draft's B3, B5 and scope note); `TOE_ASSEMBLY.md` lines 83-90, 120-140 (PS-5, PS-6) and 182 (PS-6r).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". PS-6 and PS-6r are read plainly. Where a reading has to be chosen, the choice is named, each reading is treated, and nothing is adopted.

**Working set used, by name.** PS-6 (what a frame is), PS-6r (link registers are finite quantum links on which the frame group acts), PS-1c (only through the law `L_cube`: the two tilings and the cell lattice), PS-5 (only in section 6, downstream). The law `L_cube` and its definitions are LW1 section 1 and section 2. LW1 results used: Lemma A1 (each edge lies in exactly one cube of exactly one tiling), Theorem B3 (one-site CAR automorphisms), Theorem B4 (Gauss conservation). No other working-set entry is used. PS-2, PS-3 (all forms), PS-7 and PS-11 are not used: no step reads states, odds, records or actual configurations.

---

## 0. The open item, quoted

`LW1.md` line 243:

> "**B5(b), retained as an unproved draft statement.** If a compact group acts on the eight modes of each even cell and each dressed half-tick gate is invariant after changing the registers on its own cube, the draft claims that the mode image is scalar \(U(1)\) per cell."

`LW1.md` line 245 (GAP B5(b), in part): "the eight independent site phases, grouped as \(U(1)^8\) on a cell and compensated on their incident links as in B4, satisfy the stated gate invariance and are not scalar on the cell. Thus the scalar conclusion is false under the stated hypotheses. The draft's weaker exclusion of non-abelian cell-mixing actions still needs a proof."

`LW1.md` line 492: "Determine the image of compact mode-linear frame groups on an even cell under the stated invariance of every dressed cube gate. ... Whether the remaining hypotheses exclude every non-abelian mode image is unproved."

`LW1_REFEREE.md` line 171 checks the counterexample: "for `g=diag(e^{iθ_x})_{x∈A}`, combine with `e^{i(θ_{\rm source}−θ_{\rm target})E_ℓ}` on each link of the gate's own cube ... This works for the even gate of `A` and for each odd gate (one corner of `A`, compensated on its three links in the odd cube)."

`CH1_DRAFT.md` line 23 (lead note): "S3 holds under PS-6 read per site ... For cell frames it waits on B5(b). D1 is not put to the owner until B5(b) is settled." Theorem S3 (i), line 257: "`G = U(1)` for one-body frame actions (LW1 Theorem B5)".

## 0.1 Outcome in one paragraph

Under B5(b)'s own hypothesis (each dressed gate invariant, with register changes on links only), **the abelian conclusion is proved, for every frame and not only mode-linear ones**. Every local frame on an even cell `A` acts on the eight modes by independent site phases, times a unitary on A's twelve internal links (a register change). The mode image of the set of such frames is exactly the site-phase torus `U(1)^8`. The proof uses only the eight odd gates, one per corner. It holds for the gate at every nonzero angle and every spin `S`, so the gate-versus-generator question does not arise: no exceptional angle enlarges the mode image. The lead's sketch is right; this file closes it, with a different key step at gate level (Lemma T: each gate moves a particle across each edge). PS-6's plain wording gives the same answer. If only the *whole update* `U_0` must be unchanged, by one frame and one register change split at `A`, the mode image is again exactly `U(1)^8` (section 7, Theorem B5b-T). The key step cuts the tick at the odd layer: the even and electric layers respect the cut between the cell and its outside. Invariance of the odd half-step `W_EM_o` alone also suffices (Proposition 7.2). Two wider readings change the answer. (i) If a gate's compensation may also change the *matter* of neighbouring cells, a sign-twisted charge conjugation survives: the image is `U(1)^8 ⋊ Z_2`. It is non-abelian but mixes no modes, and its compensations are not register changes, so it lies outside PS-6. (ii) If register changes may entangle A's internal registers with outside registers (reading R-E), the odd gates allow operator-valued phases `c_x ↦ c_x u_x`, with commuting unitaries `u_x` on internal registers (Theorem 7.3). These mix no modes and fix every occupation number, but they have no mode image. R-E with the even gate or with the whole update is open (B5b-E′).

---

## 1. The hypothesis class

### 1.1 What PS-6 and PS-6r say, read plainly

PS-6 (`TOE_ASSEMBLY.md` line 133): "The internal frame of each site's possibilities is local. Each nearest-neighbour link carries a register that transports frames between its two sites. The update is unchanged when the frame at one site and the registers on its links are changed together."

PS-6r (line 182): "Each link register is a finite quantum link: a finite-dimensional register on which the frame group of the site content acts, with the raising and lowering structure the Gauss law needs."

Plain content: (a) a frame change acts on one site's possibilities; (b) the compensation acts on registers, that is, on links; (c) the object that must be unchanged is the update. The cell question (CH1 D1, PS-5 "Build site content on cells of qubits") replaces "site" in (a) by an even cell. B5(b) as written in LW1 strengthens (c) to: each dressed gate is unchanged, with registers changed on the gate's own cube.

### 1.2 Definitions

Fix an even cell `A = b + {0,1}^3`, `b ∈ 2Z^3`. Write:
- `𝔄^m_A` for the algebra generated by `c_x`, `x ∈ A` (isomorphic to `M_{256}(C)` by a Jordan–Wigner map inside `A`);
- `𝔏_A` for the algebra of A's twelve internal links (by Lemma A1 these are the edges of `A`; they all belong to the even tiling);
- `𝒜_A = 𝔄^m_A ⊗ 𝔏_A`, the cell's content with its internal registers. Links are ordinary tensor factors that commute with matter (`LW1.md` line 42), so this is an ordinary tensor product;
- `𝒪_A` for the algebra generated by all `c_y`, `y ∉ A`, and all links not internal to `A`.

The quasi-local algebra `𝔄` is generated by `𝒜_A` and `𝒪_A`.

**Definition F (frame on `A`).** A frame on `A` is an automorphism `φ` of `𝔄` with `φ(𝒜_A) = 𝒜_A` and `φ(z) = z` for every `z ∈ 𝒪_A`.

This is the widest local class. It includes mode-linear frames `Γ(g)`, `g ∈ U(8)`; many-body unitaries on A's Fock space; unitaries that entangle A's modes with A's internal links; and odd unitaries (Lemma G1 shows these are the only extra case). It answers the lead's points (3) and (4) by definition: parity is not assumed, and mixing with internal links is allowed.

**Definition R (register change).** A register change is `Ad L` for a unitary `L` on finitely many links. It is *split at A* if `L = L^{in} ⊗ L^{out}` with `L^{in}` on A's internal links and `L^{out}` on links not internal to `A`. Every change made link by link (`L = ⊗_ℓ L_ℓ`) is split at `A`. LW1's "registers on its own cube" is split at `A` for every gate: the own links of an odd cube are not internal to `A` (Lemma 2.1).

**Gate-wise invariance (B5(b)'s hypothesis).** For each corner `x ∈ A` let `O_x` be its odd cube (Lemma 2.1). The frame `φ` is *gate-compatible* if for each corner `x` there are a split register change `Ad L_x` and a real `a_x ≠ 0` with
\[
(\varphi\circ\operatorname{Ad}L_x)\big(e^{ia_xH_{O_x}}\big)=e^{ia_xH_{O_x}} .
\]
The law's case is `a_x = a_o = ε + μ/2`; the window `0 ≤ μ < 2ε < π` gives `0 < a_o < π`. The theorem needs only `a_x ≠ 0`. It does not need the even gate, the electric layer or a plaquette layer.

**Readings outside B5(b)'s hypothesis, treated in section 5.**
- R-M: the compensation for a gate may act on anything outside `A`, matter included.
- R-E: the register change need not be split at `A` (it may entangle A's internal registers with outside registers).
- R-T: only the whole update `U_0` must be unchanged, by one frame and one register change.

### 1.3 Four-test check of the readings proposed here

The owner adopts readings; this file only proposes them. Definition F with gate-wise invariance (the class of the main theorem):
1. *Does it state or fix a part's target?* No. It names no group; the group is derived.
2. *Is it open-ended?* No. It is a closed definition: one automorphism class, one compensation class, one invariance condition.
3. *Does it settle a downstream physics question by premise?* Not by its text. But choosing gate-wise invariance over whole-update invariance (R-T) could exclude by fiat a frame that R-T allows. So test 3 passes only conditionally: it passes if B5b-T has the same answer, and it is unsettled until then. This is reported, not hidden.
4. *Does it add structure or constants its own reasons do not need?* No constants. The split condition on registers follows from "registers ... changed" read link by link.

Result: passes tests 1, 2 and 4; passes test 3 conditionally on B5b-T. (Update, section 7.8: Theorem B5b-T gives the same mode image, so test 3 passes for register changes split at `A`.) Reading R-M fails PS-6's own wording (it changes site content outside the frame's site, not registers); it is treated only to show what it would add.

---

## 2. Lemmas

**Lemma 2.1 (corners and odd cubes).** Each corner `x` of `A` lies in exactly one odd cube `O_x`. `O_x ∩ A = {x}`. Distinct corners lie in distinct odd cubes. No link of `O_x` is internal to `A`.

*Proof.* The odd tiling partitions the sites, so `O_x` exists and is unique. Along axis `j` an odd cube covers `{b'_j+1, b'_j+2}` with `b'_j` even, and `A` covers `{b_j, b_j+1}` with `b_j` even. These sets share at most one integer: `b'_j+1 = b_j+1` and `b'_j+2 = b_j` cannot both hold. So an odd cube meets `A` in at most one site. If `O_x = O_{x'}`, both corners lie in `O_x ∩ A`, so `x = x'`. Links of `O_x` belong to the odd tiling and links internal to `A` belong to the even tiling; by Lemma A1 no edge belongs to both. ∎

**Lemma G1 (locality fixes parity).** Let `φ` be a frame on `A`. Then `φ` maps even elements of `𝒜_A` to even ones and odd to odd. There is a unitary `V ∈ 𝒜_A`, unique up to a phase, with `φ|_{𝒜_A} = Ad V`, and `V` is even or odd.

*Proof.* Let `b ∈ 𝒜_A` with parts `b_±`, and fix `y ∉ A`. Then `b c_y = c_y(b_+ − b_-)` and the same with `c_y^†`. If `a ∈ 𝒜_A` is odd, `a c_y = −c_y a`, so `φ(a) c_y = −c_y φ(a)`, because `φ` fixes `c_y`. With `b = φ(a)` this gives `c_y b_+ = 0` and, in the same way, `c_y^† b_+ = 0`. Then `b_+ = (c_y^†c_y + c_yc_y^†) b_+ = 0`. Even elements are treated the same way with commutation, giving `φ(a)_- = 0`. Next, `𝒜_A ≅ M_n(C)`, so `φ|_{𝒜_A} = Ad V` by Lemma G3. Let `P_A = (−1)^{N_A}`. The grading on `𝒜_A` is `Ad P_A`, and `φ` commutes with it. So `Ad(P_A V P_A V^*)` is the identity, and `P_A V P_A = ζ V` for a scalar `ζ`. Since `P_A^2 = 1`, `ζ = ±1`: `V` is even or odd. ∎

*Remark.* Conversely each homogeneous `V ∈ 𝒜_A` gives a frame: the graded tensor product of `Ad V` on `𝒜_A` with the identity on `𝒪_A`. A non-homogeneous `V` gives none. As a plain operator `V ⊗ 1` in a Jordan–Wigner order that lists `A` first, it fixes every `c_y` only when `V` is even; an odd `V` flips the sign of every later `c_y`. Below, the main theorem shows `V` is even in any case.

**Lemma G2 (splitting across disjoint supports).** Let `𝒞_1` be generated by the modes of a finite set `F_1` and the links of a finite set `Λ_1`, and let `𝒞_2` be generated by modes of `F_2` and links of `Λ_2`, with `F_1 ∩ F_2 = ∅` and `Λ_1 ∩ Λ_2 = ∅`.
(a) If `z_j ∈ 𝒞_1` and `m_j ∈ 𝒞_2` are linearly independent and all of one parity, then `Σ_j z_j m_j = 0` (or `Σ_j m_j z_j = 0`) forces every `z_j = 0`.
(b) If `a, a' ∈ 𝒞_1`, `b, b' ∈ 𝒞_2` are nonzero, `b, b'` of one parity, and `ab = a'b'`, then `a' = κa` and `b' = κ^{-1}b` for a scalar `κ ≠ 0`.

*Proof.* Order the modes of `F_1` first in a Jordan–Wigner map. Then `c_u = ĉ_u ⊗ 1` for `u ∈ F_1`, and `c_v = P_1 ⊗ ĉ_v` for `v ∈ F_2`, where `P_1` is the parity of `F_1`. Links sit in their own factors. A product of generators shows that each `m ∈ 𝒞_2` of parity `p` equals `P_1^p ⊗ m̂`, and `m ↦ m̂` is linear and injective. Hence `z m = (z P_1^p) ⊗ m̂` and `m z = (P_1^p z) ⊗ m̂`. In (a), independence of the `m̂_j` in an ordinary tensor product gives `z_j P_1^p = 0`, so `z_j = 0`. In (b), `(aP_1^p) ⊗ b̂ = (a'P_1^p) ⊗ b̂'` with both sides nonzero. Choose a functional `f` with `f(b̂) = 1`. Then `aP_1^p = f(b̂') a'P_1^p`, so `f(b̂') ≠ 0`; put `κ = 1/f(b̂')`. Then `(aP_1^p) ⊗ (b̂ − κ b̂') = 0`, so `b̂ = κ b̂'`. Cancel the invertible `P_1^p`. ∎

**Lemma G3 (automorphisms of a full matrix algebra are inner).** Every `*`-automorphism `ψ` of `M_n(C)` is `Ad V` for a unitary `V`, unique up to a phase. The commutant of `M_n ⊗ 1` in `M_n ⊗ M_k` is `1 ⊗ M_k`.

*Proof.* Put `f_{ij} = ψ(e_{ij})`. Then `f_{11}` is a projection with `f_{11} M_n f_{11} = ψ(e_{11}M_ne_{11}) = C f_{11}`, so it has rank one. Take a unit vector `w` in its range and set `V e_i = f_{i1}w`. From `f_{i1}^*f_{j1} = f_{1i}f_{j1} = δ_{ij}f_{11}` the vectors `V e_i` are orthonormal, so `V` is unitary. Also `V e_{ij} V^* (V e_k) = δ_{jk} f_{i1}w = f_{ij} f_{k1} w`, so `V e_{ij} V^* = f_{ij}`. Uniqueness: `V'^*V` commutes with `M_n`, hence is a scalar. For the commutant, write `z = Σ e_{ij} ⊗ z_{ij}`; commuting with every `e_{kl} ⊗ 1` gives `z_{ij} = δ_{ij} z_{11}`. ∎

**Lemma T (each gate moves a particle across each edge).** Let `C` be a cube of either tiling, `{x, y}` an edge of `C`, `S` any spin, and `a ∈ R`, `a ≠ 0`. There are one-particle states `|x; m⟩`, `|y; m'⟩` (one particle in `C` at the named site, all other modes empty, links in fixed basis states) with
\[
\langle y;m'|\,e^{iaH_C}\,|x;m\rangle\neq0 .
\]
Hence `(1−n_x) e^{iaH_C} n_x ≠ 0` and `n_x e^{iaH_C}(1−n_x) ≠ 0`, and `e^{iaH_C}` does not commute with `n_x`.

*Proof.* A hop term at link `ℓ = (u, u+e_i)` moves a particle from `u` to `u+e_i` by `J_ℓ` and back by `J_ℓ^†`. Call a link state *blocking at* `u` if it kills the hop away from `u`: `m = S` when `u` is the source, `m = −S` when `u` is the target. Call it *open at* `u` if the hop away from `u` has the extreme amplitude `√(2S)`: `m = S−1` when `u` is the source (`J|S−1⟩ = √(2S)|S⟩`), `m = −S+1` when `u` is the target (`J^†|−S+1⟩ = √(2S)|−S⟩`). For a one-particle state there are no fermion signs: `c_v^† c_u c_u^†|0⟩ = c_v^†|0⟩`.

*Two-site block.* Put `ℓ_1 = {x,y}` open at `x`. Put each other link at `x` blocking at `x`, and each other link at `y` blocking at `y`. The cube graph has no triangles, so each of these links has exactly one end in `{x,y}`. Other links are arbitrary. Let `|x⟩` be the resulting state and `|y⟩` the state after the hop. Only terms whose annihilated site carries the particle act. So `H_C` maps `span{|x⟩,|y⟩}` into itself and acts there as `σβ σ^x` with `σ = ±1` (the sign `η_i`) and `β = √(2S/3)`. Hence `⟨y|e^{iaH_C}|x⟩ = iσ sin(aβ)`.

*Three-site block.* Pick a third site `z ∈ C`, a neighbour of `y` with `z ≠ x`. Put `ℓ_1` open at `x` and `ℓ_2 = {y,z}` open at `y` (its value is untouched until the particle reaches `y`). Put each other link at `x`, `y`, `z` blocking at that end. `x` and `z` are at distance two, so again each blocking link has exactly one end on the path. The span of the three states along the path is invariant. In it `H_C` is the real symmetric tridiagonal matrix with off-diagonal entries `σ_1β`, `σ_2β`. Then `H^3 = ω^2 H` with `ω = √(2β^2) = √(4S/3)`, so
\[
e^{iaH}=1+i\frac{\sin a\omega}{\omega}H+\frac{\cos a\omega-1}{\omega^2}H^2 .
\]
`H^2` connects `x` only to `x` and `z` (the graph is bipartite), so `⟨y|e^{iaH}|x⟩ = iσ_1β sin(aω)/ω`.

If both amplitudes vanish, then `aβ = kπ` and `aω = k'π` with integers `k, k' ≠ 0`, since `a ≠ 0` and `β, ω > 0`. Then `k'/k = ω/β = √2`, which is irrational. So one amplitude is nonzero. The block states lie in the ranges of `n_x` and `1−n_x` as named. `e^{iaH}` restricted to a real symmetric block is symmetric, so the reverse amplitude `⟨x|e^{iaH}|y⟩` is the same number. ∎

[check] `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/b5b/blocks.py` builds every two-site and three-site block (all 8 corners, all 3 edges, both third sites) of the odd cube `{1,2}^3` with LW1's `η_i` signs, for `S = 1/2, 1, 3/2, 2, 3`. Each orbit closes in dimension 2 or 3, with `|eigenvalues|` `{β, β}` and `{0, ω, ω}`, `β = √(2S/3)`, `ω = √(4S/3)`, as stated.

*Note.* Lemma T needs no window: it holds for every `a ≠ 0` and every `S`. So it holds at `a_o` and at `a_e = ε − μ/2 > 0` throughout `0 ≤ μ < 2ε < π`.

---

## 3. The main theorem

**Theorem B5b (cell frames under gate-wise invariance).** Let `φ` be a frame on the even cell `A` (Definition F) that is gate-compatible (section 1.2). Then there are phases `λ ∈ U(1)^8` and a unitary `W` on A's internal links with
\[
\varphi(c_x)=\lambda_x c_x\quad(x\in A),\qquad
\varphi|_{\mathcal A_A}=\operatorname{Ad}(D_\lambda W),\quad D_\lambda=\textstyle\prod_{x\in A}e^{-i\theta_x n_x},\ \lambda_x=e^{i\theta_x}.
\]
In particular `φ` is even, preserves every `n_x`, mixes no two modes, mixes no mode with a link, and is not a particle-hole map at any site. Conversely, every `λ ∈ U(1)^8` occurs: the frame `Ad(D_λ ∏_{ℓ=(s,t)⊂A} e^{-i(θ_s−θ_t)E_ℓ})`, with the register change `e^{∓iθ_xE_ℓ}` on the three links of `O_x` at `x` (minus sign when `x` is the source), leaves every gate of `U_0` unchanged, and every plaquette monomial too.

So the mode image of the set of gate-compatible frames is exactly the site-phase torus `U(1)^8`. It is abelian. For a group acting by gate-compatible frames, the image is a subgroup of `U(1)^8`; for a compact group acting continuously, a closed subgroup. B5(b)'s mode-linear case: `Γ(g)`, `g ∈ U(8)`, is gate-compatible only if `g` is diagonal.

*Proof.* Fix a corner `x`. Write `O = O_x`, `G = e^{iaH_O}` with `a = a_x`, `L = L_x = L^{in} ⊗ L^{out}`, and `ψ = φ ∘ Ad L`. By hypothesis `ψ(G) = G`.

*Step 1 (isolate the inflow at `x`).* Let `𝔐` be the seven modes of `O ∖ {x}` and `Π_k` the spectral projections of their number `N_𝔐`. The `Π_k` lie in the matter algebra outside `A`, so `φ` fixes them, and `Ad L` fixes all matter. Hence `ψ(Π_k) = Π_k`, and
\[
G^{(-1)}:=\sum_k\Pi_{k-1}G\Pi_k\quad\text{satisfies}\quad\psi(G^{(-1)})=G^{(-1)}.
\]
Each hop term conserves `n_x + N_𝔐`, so `G` does. A block `Π_{k−1}GΠ_k` lowers `N_𝔐` by one, so it raises `n_x` from 0 to 1. Conversely `n_x G (1−n_x)` lowers `N_𝔐` by one. Hence `G^{(−1)} = n_x G (1−n_x)`, which is nonzero by Lemma T.

*Step 2 (write it as an inflow operator).* Let `𝒞_2` be the algebra of the modes `𝔐` and all links not internal to `A`. In a Jordan–Wigner order with `x` first, `n_x G(1−n_x) = |1⟩⟨0|_x ⊗ Y` for a unique `Y`; `Y` is odd because `G` is even. Let `X ∈ 𝒞_2` be the odd element with `X̂ = Y` (Lemma G2's map). Then `c_x^† X = |1⟩⟨0|_x ⊗ Y`, so
\[
n_xG(1-n_x)=c_x^\dagger X,\qquad X\in\mathcal C_2\ \text{odd},\ X\neq0 .
\]

*Step 3 (apply the frame).* `L` acts on links only, so `Ad L(c_x^†) = c_x^†` and `ψ(c_x^†) = φ(c_x^†) =: d^† ∈ 𝒜_A`. `L^{in}` commutes with `X`, so `Ad L(X) = Ad L^{out}(X) =: X'`, an odd nonzero element of `𝒞_2`. `φ` fixes `𝒞_2 ⊂ 𝒪_A`. Hence `ψ(X) = X'`, and Step 1 gives
\[
d^\dagger X'=c_x^\dagger X .
\]

*Step 4 (split).* Apply Lemma G2(b) with `𝒞_1 = 𝒜_A` and `𝒞_2` as above; the supports are disjoint (Lemma 2.1 for the links). So `d^† = κ c_x^†`. Since `φ` is an automorphism, `1 = d d^† + d^† d = |κ|^2`. So `φ(c_x) = λ_x c_x` with `λ_x = \bar κ`, `|λ_x| = 1`.

*Step 5 (all corners).* Steps 1-4 hold for each of the eight corners, with its own `O_x`, `L_x`, `a_x`. So `φ` and `Ad D_λ` agree on the generators of `𝔄^m_A` (`Ad e^{−iθn}(c) = e^{iθ}c` because `n c = 0` and `c n = c`), hence on `𝔄^m_A`. The automorphism `χ = Ad D_λ^{-1} ∘ φ` of `𝒜_A = 𝔄^m_A ⊗ 𝔏_A` fixes `𝔄^m_A` pointwise. So it maps the commutant `1 ⊗ 𝔏_A` (Lemma G3) onto itself, and there it is `Ad W` (Lemma G3). An automorphism of a tensor product is fixed by its values on the two factors, so `χ = Ad(1 ⊗ W)` and `φ|_{𝒜_A} = Ad(D_λ W)`. `D_λ W` is even.

*Converse.* Put `θ_y = 0` for `y ∉ A`. The unitary `∏_{x∈A} e^{−iθ_x𝒢_x}` equals `D_λ ∏_{ℓ⊂A} e^{−i(θ_s−θ_t)E_ℓ} ∏_{x} ∏_{ℓ∈O_x, ℓ∋x} e^{∓iθ_xE_ℓ}`. The first two factors lie in `𝒜_A`; the last acts on links of the odd cubes `O_x` only. By B4 every dressed gate, every electric gate and every plaquette monomial commutes with every `𝒢_x`. Per gate, the factors outside the gate's cube commute with it. So the even gate of `A` is unchanged by the frame alone; the odd gate of `O_x` is unchanged by the frame with the change `e^{∓iθ_xE}` on O_x's three links at `x`, which are its own links; `e^{iφE_ℓ}` commutes with `e^{−iτ_EE_ℓ^2}`; all other gates have disjoint support. This is the referee's check at `LW1_REFEREE.md` line 171. ∎

**Corollary B5b.1 (one-site frames).** Take a frame that acts on one site `x` only (so `𝒜` is the algebra of `x`). Under gate-wise invariance with split register changes, it is `c_x ↦ λc_x`. The particle-hole branch `c_x ↦ v c_x^†` of Lemma B3 is excluded. B5(a) assumed number preservation to remove it; here gate compatibility removes it.

*Proof.* Steps 1-4 with `A` replaced by `{x}` and `𝒜_A` by the algebra of `x`. ∎

### 3.1 The lead's sketch, point by point

The sketch: odd gates force `d_x = λ_x c_x`, so the mode image lies in `U(1)^8`, even for many-body `V`. It is right. Its five weak points:

1. **Gate versus generator.** Settled in section 4: the proof never compares `H_O` with its conjugate. It uses one property of the gate, Lemma T, which holds at every `a ≠ 0`. No angle enlarges the mode image.
2. **Graded tensor structure.** Lemma G2, by a Jordan–Wigner order with the cell first. The splitting `d^† X' = c_x^† X` is an elementary-tensor identity after a right factor `P_A`, which cancels.
3. **Parity and locality.** Lemma G1: locality forces a homogeneous implementer. The theorem then forces an even one. Odd frames do not occur.
4. **Mixing modes with internal links.** Allowed by Definition F and excluded by the theorem: `φ(c_x) = λ_x c_x` carries no link factor. The internal-link part `W` acts only on registers; the even gate and the electric gates constrain only `W`, never the mode image.
5. **Compensation beyond the odd cube's own links.** Any split register change on any links gives the same answer (Step 3 uses only that `L` acts on links and is split at `A`). Compensation on matter outside `A` changes the answer (Theorem 5.1). Compensation that entangles A's internal registers with outside registers gives a weaker conclusion (Proposition 5.2).

---

## 4. Gate versus generator

Invariance of the generator, `Ad(VL)(H_O) = H_O`, implies invariance of every gate `e^{iaH_O}`. The converse holds whenever the map `t ↦ e^{iat}` is injective on the spectrum of `H_O`: then `H_O = f(e^{iaH_O})` for a polynomial `f`, and the conjugate has the same spectrum and the same `f`. It can fail only when two eigenvalues of `H_O` differ by a nonzero multiple of `2π/a`.

The proof of Theorem B5b does not use the converse. Step 1 uses only that `G` conserves `n_x + N_𝔐` and that `n_x G (1−n_x) ≠ 0`. Lemma T proves the second for every `a ≠ 0` and every `S`. So:

**Gate-level outcome.** The mode image is `U(1)^8` at the gate level, for every angle `a_o ≠ 0`, for every spin, inside and outside the window `0 ≤ μ < 2ε < π`. Exceptional angles, if `H_O` has any, admit no extra mode image, abelian or not.

**Not settled, and not needed.** At an exceptional angle the set of register changes `L` that compensate a given `λ` may be larger than at generic angles. This file does not decide whether exceptional angles of `H_O` occur in the window. The mode image does not depend on it.

---

## 5. Wider readings

### 5.1 Reading R-M: compensation may change matter outside `A`

**Theorem 5.1.** Let `φ` be a frame on `A`. Suppose for each corner `x` there is an automorphism `κ_x` of `𝒪_A` (matter and links outside `A`) with `(φ∘κ_x)(e^{ia_xH_{O_x}}) = e^{ia_xH_{O_x}}`, `a_x ≠ 0`. Suppose also that the even gate of `A` is unchanged by `φ` followed by a register change on A's internal links, at some angle `a ≠ 0`. Then either `φ(c_x) = λ_x c_x` for all `x ∈ A`, or `φ(c_x) = λ_x s_x c_x^†` for all `x ∈ A`, with `s_x = (−1)^{x_1+x_2+x_3}`. Both branches occur. The mode image is `U(1)^8 ⋊ Z_2`, where `Z_2` is generated by the sign-twisted charge conjugation `C_A : c_x ↦ s_x c_x^†`, and `C_A Γ C_A^{-1}` inverts every site phase. It is non-abelian. It mixes no two modes.

*Proof.* Fix `x`, `O`, `G` as before and write `G = (1−n_x)P + n_xQ + c_x^†X + X^♯c_x` with `P, Q, X, X^♯` in the algebra of `𝔐` and O's links (Jordan–Wigner with `x` first, as in Step 2). By number conservation, `P, Q` have `𝔐`-charge 0, `X` has charge −1 and `X^♯` charge +1. `X ≠ 0` and `X^♯ ≠ 0` by Lemma T. Lemma G1 applies to `κ_x` on `𝒪_A` as well (same proof with the roles of `A` and its complement exchanged on a finite region), so `κ_x` preserves parity. With `d = φ(c_x)` (odd),
\[
(1-d^\dagger d)\kappa(P)+d^\dagger d\,\kappa(Q)+d^\dagger\kappa(X)+\kappa(X^\sharp)d=(1-n_x)P+n_xQ+c_x^\dagger X+X^\sharp c_x .
\]
Split by Lemma G2 (cell first, right factor `P_A`). The `𝒪_A`-components `X̂` and `X̂^♯` lie in different charge spaces from each other and from `P̂, Q̂`, and they are nonzero. Choose a functional `f` with `f(X̂) = 1` and `f` zero on `X̂^♯, P̂, Q̂`; take the odd part in `𝒜_A`. This gives `c_x^† ∈ span{d, d^†}`; the same with `X̂^♯` gives `c_x ∈ span{d, d^†}`. `d` and `d^†` are independent (if `d^† = μd` then `d^†d = μd^2 = 0` and `dd^† = 0`, contradicting `dd^† + d^†d = 1`). So `span{d, d^†} = span{c_x, c_x^†}`. Write `d = uc_x + vc_x^†`; `d^2 = uv = 0`, so `d = uc_x` or `d = vc_x^†`.

Let `F` be the set of corners in the second branch. The register change on A's internal links fixes all matter, so the composite map `ψ_A` sends `n_z` to `n_z` for `z ∉ F` and to `1 − n_z` for `z ∈ F`. The even gate `G_A` commutes with `N_A`; then `G_A = ψ_A(G_A)` commutes with `ψ_A(N_A) = N_{A∖F} + |F| − N_F`, hence with `N_F`. If `∅ ≠ F ≠ A`, the cube graph of `A` is connected, so some edge `{x,y}` has `x ∈ F`, `y ∉ F`. Lemma T for the even cube gives one-particle states with `⟨y|G_A|x⟩ ≠ 0`, so `⟨y|[G_A, N_F]|x⟩ = ⟨y|G_A|x⟩ ≠ 0`. So `F = ∅` or `F = A`. When `F = A`, absorb `s_x` into the phases.

*Realization of `C_A`.* Let `R = e^{−iπS^x}` on a link; it sends `J ↦ J^†` and `E ↦ −E`. For neighbours `s_xs_y = −1`. Then `c_y^†J c_x ↦ s_ys_x c_y J^† c_x^† = c_x^† J^† c_y`, the partner term with the same coefficient. So `C_A` with `R` on A's internal links fixes `H_A` exactly; `R` fixes `E_ℓ^2`. For the odd gate of `O_x`, take `κ_x` = the same conjugation on the seven modes `O_x∖{x}` and `R` on O_x's twelve links; then `φ ∘ κ_x` is the charge conjugation of the whole cube `O_x`, which fixes `H_{O_x}`. [check] `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/b5b/cconj.py` confirms `RJR^† = J^†` and that one dressed edge term is fixed, for `S = 1/2, 1, 3/2`. ∎

*What R-M means.* The compensations `κ_x` change the content of 56 sites in neighbouring cells. Those are site possibilities, not registers, so R-M is outside PS-6 ("the registers on its links") and PS-6r. In addition, the compensations for different gates disagree on the neighbouring cells, so no single transformation realizes `C_A` locally; globally it is the charge conjugation of the whole lattice. If frames must preserve number (B3's subgroup), `C_A` is excluded. Either way the Lie algebra of the image is `u(1)^8`, and no frame mixes modes.

### 5.2 Reading R-E: register changes not split at `A`

**Proposition 5.2.** In Theorem B5b, drop "split at `A`": let each `L_x` be any unitary on finitely many links (A's internal links allowed, entangled with outside links). Then for each corner, `φ^{-1}(c_x) = c_x u_x` for a unitary `u_x` on A's internal links.

*Proof.* Steps 1-2 are unchanged. Write `X = Σ_j m_j k_j` with `m_j` independent odd elements of the `𝔐` algebra and `k_j` on O's links. `ψ` fixes `m_j`, so `ψ(c_x^†X) = c_x^†X` and Lemma G2(a) (with `𝒞_1` = A's modes and all links) give `ψ(c_x^† k_j) = c_x^† k_j` for each `j`. Fix `k = k_j ≠ 0` and write `Ad L(k) = Σ_r ι_r ⊗ e_r` with `ι_r ∈ 𝔏_A` and independent `e_r` on outside links. `φ` fixes `e_r`, so `Σ_r φ(c_x^†ι_r) ⊗ e_r = c_x^† ⊗ k`. Comparing coefficients, `k = Σ_r κ_re_r` and `φ(c_x^†ι_r) = κ_r c_x^†`. Take `κ_r ≠ 0`; then `φ^{-1}(c_x^†) = c_x^†ι` with `ι = ι_r/κ_r`. The CAR give `(1−n_x)ι^†ι + n_xιι^† = 1`, so `ι` is unitary. Put `u_x = ι^†`. ∎

So under R-E no frame mixes corners or flips a site, but a corner may pick up an operator-valued phase on A's internal links. Such a frame does not map A's mode algebra into itself unless every `u_x` is scalar, so its "mode image" is not defined. Whether any gate-compatible frame with a non-scalar `u_x` exists was named **B5b-E**. It exists: section 7.6 classifies these frames (Theorem 7.3) and gives a counterexample. A split register change (in particular any change made link by link) gives `ι` scalar, which is Theorem B5b.

### 5.3 Reading R-T: only the whole update must be unchanged

PS-6's plain words ask that "the update is unchanged". Gate-wise invariance implies this, but not conversely. **B5b-T (proved in section 7, Theorem B5b-T: the mode image is exactly `U(1)^8`):** classify frames `φ` on `A` (Definition F) for which some split register change `Ad L` gives `(φ∘Ad L)(U_0) = cU_0`, `|c| = 1`. The image contains `U(1)^8` (Theorem B5b, converse). Three attacks were made and each stopped at one point:
1. *Light cone.* `φ` commutes with the tick automorphism `τ`, so it fixes `τ(z)` for each `z ∈ 𝒪_A` away from `supp L`. But `τ(c_y)` for `y` next to `A` mixes A's modes with compensated links in a way that is not an elementary tensor across A's boundary, so Lemma G2 does not apply.
2. *Charge components of the tick.* Inflow into `A` comes only from `M_o`, so the `N_{out}`-charge −1 component is `W_E M_o^{(−1)} M_e`. It contains `G_A` and the charge-zero parts of the other seven odd gates. These involve A's occupations, on which `φ` acts in an unknown way.
3. *Finite reduction.* With `L` on A's 24 outside links, the identity reduces to `φ(W^{36} ∏_xG_{O_x}G_A) = c W^{36}∏_xG_{O_x}G_A` on `A ∪ ⋃O_x` (all other gates cancel). Projecting the outside modes onto fixed patterns removes `𝔐_x` but leaves factors `(1−n_{x'}) + n_{x'}K_{x'}` with link-valued `K_{x'}`; the products do not separate.

All three stop at the same missing step: that `φ` preserves A's occupation numbers. Section 7 supplies it without a conserved-quantity argument. It cuts the tick at the odd layer, `γ_e^{-1}ψγ_e = γ_o(γ_Eψγ_E^{-1})γ_o^{-1}`; both sides are still products across the cut, and the two sides of the odd layer give (7.2) and then Step 2 of section 7.4. The half-step case (invariance of `M_e` and of `W_EM_o` separately) is Proposition 7.2: the odd half-step alone gives `U(1)^8`.

---

## 6. What changes downstream

**CH1 Theorem S3 (i).** S3 (i) cites "`G = U(1)` for one-body frame actions (LW1 Theorem B5)". Under gate-wise invariance with register-only compensation (B5(b)'s own hypothesis), Theorem B5b upgrades this: *every* local frame on a cell of one-mode sites, many-body, of either parity, entangled with internal links, acts on modes by site phases. The cell frame group's mode image is `U(1)^8` per cell, that is `U(1)` per site. This is the same exact gauge group as the site-local reading. S3 (ii) and (iii) and Theorem S2 then hold for cell frames under that reading, unchanged. Under R-M the image gains a `Z_2` charge conjugation, which carries no non-abelian charge (its Lie algebra is still abelian); S3 (ii) is unaffected. Under R-T (PS-6's plain wording), with register changes split at the cell, Theorem B5b-T gives the same mode image `U(1)^8`, so S3 (i) holds for cell frames there too (section 7). Under R-E the odd gates allow operator-valued phases (Theorem 7.3). These mix no modes, but they have no mode image, so S3 (i)'s "`G = U(1)`" has no direct meaning there; R-E with the even gate or the whole update is open (B5b-E′).

**Owner decision D1 (PS-5).** The named step D1 asked for is now proved in this form: "On `L_cube`, with each dressed gate unchanged after register changes, the frames of a cell of one-mode sites act on its modes by site phases only; no non-abelian frame group arises, many-body frames included (Theorem B5b)." Section 7 proves the same step under PS-6's plain wording: "On `L_cube`, with the whole tick `U_0` unchanged after a register change split at the cell (in particular any change made link by link), the frames of a cell of one-mode sites act on its modes by site phases only, many-body frames included (Theorem B5b-T)." Invariance of the odd half-step alone gives the same (Proposition 7.2). So B5b-T no longer holds D1 back, and section 1.3's test 3 passes for split register changes. Whether this step counts as the cell route failing under PS-5 is the owner's call. One reading question still bears on the call: whether a register change may entangle the cell's internal registers with outside registers (R-E). Under R-E the odd gates admit operator-valued phases that mix no modes (Theorem 7.3); the full-update R-E case is open (B5b-E′). PS-6r's words ("a finite-dimensional register on which the frame group of the site content acts") speak of each link register; this file does not adopt a link-by-link reading. Reading R-M remains outside PS-6. The owner may also specify the gate-wise or the whole-update reading; that is a specification, and this file does not adopt it.

**GA1.** GA1-i asks for "the group that the chosen content gives". For one-mode cells of `L_cube` under gate-wise invariance, or under whole-update invariance (section 7), with split register changes, the answer is `U(1)` per site, with Gauss laws from B4. The SU(2) rung of the skeleton's section 6 ("With one qubit per site and PS-6, the frame group of `M_2(C)` is `U(2)`") is not reached from one-mode cells of `L_cube` in this reading. It needs the qubit reading of a site, more modes per site (PS-5's fallback), or non-abelian structure that emerges at long distance. #9882's "U(m) commutants with m >= 3" on n-particle states (quoted in `LW1_DRAFT.md` line 266) are not gate-compatible frames: Theorem B5b excludes every frame that is not a site phase.

---

## 7. B5b-T: whole-update invariance

*Added 2026-11-05 by a Claude Opus 5.5 subagent (pass 1, not refereed). Read at commit `1cadeac0dc`: this file in full; `LW1.md` lines 26-64 (definitions), 231 (B4) and 390-399 (E1).*

### 7.1 Statement

`LW1.md` line 62: "The matter layers are \(M_e=\prod_{C\in\mathcal T_e}e^{-ia_eH_C}\) and \(M_o=\prod_{C\in\mathcal T_o}e^{ia_oH_C}\). The electric layer is \(W_E=\prod_\ell e^{-i\tau_E E_\ell^2}\). Products at infinite volume mean the local automorphisms of E1. The specified base tick is \(U_0=W_EM_oM_e\)." Line 64: "the tick automorphism \(\alpha(A)=U_0^*AU_0\)". Line 390 (E1): "Each base layer and their tick composition define automorphisms of \(\mathfrak A\)."

So each layer gives an automorphism, by E1's finite gate lists:
\[
\gamma_E(z)=W_E^*zW_E,\qquad \gamma_o(z)=M_o^*zM_o,\qquad \gamma_e(z)=M_e^*zM_e,\qquad \alpha=\gamma_e\circ\gamma_o\circ\gamma_E ,
\]
since `U_0^* z U_0 = M_e^* M_o^* W_E^* z W_E M_o M_e`. For `x ∈ A` write `G_x = e^{ia_oH_{O_x}}`, `𝔐_x = O_x ∖ {x}`, and `G_A = e^{−ia_eH_A}`.

**Hypothesis T.** `φ` is a frame on `A` (Definition F). `L = L^{in} ⊗ L^{out}` is a register change split at `A` (Definition R). `ψ = φ ∘ Ad L` satisfies `ψ ∘ α = α ∘ ψ`.

On a finite torus (even side at least 4, so Lemma 2.1 holds), Hypothesis T is equivalent to B5b-T's identity `ψ(U_0) = cU_0`, `|c| = 1`. If `ψ(U_0) = cU_0`, then `ψ(U_0^*zU_0) = ψ(U_0)^*ψ(z)ψ(U_0) = U_0^*ψ(z)U_0`. Conversely, `ψ∘Ad U_0^* = Ad ψ(U_0)^* ∘ ψ`, so commutation gives `Ad(U_0ψ(U_0)^*) = id`, and `U_0ψ(U_0)^*` is a scalar in a full matrix algebra. At infinite volume `U_0` is not an element of `𝔄`, and Hypothesis T is the meaning of the identity (four-test in section 7.8). The phase `c` drops out.

**Theorem B5b-T.** Under Hypothesis T there are `λ ∈ U(1)^8` and a unitary `W` on A's internal links with `φ|_{𝒜_A} = Ad(D_λ W)` (notation of Theorem B5b). The mode image of the set of such frames is exactly `U(1)^8`. The proof uses only `a_o ≠ 0`. It holds for every `a_e` (zero included), every `τ_E` and every spin `S`.

### 7.2 Three facts about the layers

**(H1)** `γ_e` and `γ_E` map `𝒜_A` onto `𝒜_A` and `𝒪_A` onto `𝒪_A`.

*Proof.* For `z ∈ 𝒜_A` the only even gate whose support meets `supp z` is `G_A ∈ 𝒜_A`, so `γ_e(z) = G_A^* z G_A ∈ 𝒜_A`. For `z ∈ 𝒪_A`: `G_A` is an even element of `𝒜_A`, so it commutes with `z`; every other even gate `G_B` is an even element of `𝒜_B ⊂ 𝒪_A` (B's modes lie outside `A`, and B's links are not internal to `A`). So `γ_e(z) ∈ 𝒪_A`. The same holds for `γ_e^{-1}`. `W_E` is a product of even one-link gates; those on A's internal links lie in `𝒜_A`, the rest in `𝒪_A`. ∎

**(H2)** For `y ∈ 𝔐_x`, `γ_o(c_y) = G_x^* c_y G_x`. Also `γ_o^{-1}(n_x) = G_x n_x G_x^*`.

*Proof.* By E1's gate list. The odd tiling partitions the sites, so `G_x` is the only odd gate whose support contains `y` or `x`. ∎

**(H3)** If `L'` is a unitary on finitely many links, `Ad L'` fixes every matter element. So `Ad L'` commutes with `Ad e^{iθN_F}` for every finite set `F` of sites.

Say `z` has *`F`-charge `k`* if `Ad e^{iθN_F}(z) = e^{ikθ}z` for all `θ`. Then `c_y` has `{y}`-charge `−1`.

### 7.3 Two lemmas

**Lemma D (decomposition along one mode).** Let `𝒞` be generated by finitely many modes other than `x` and finitely many links. Each `z` in the algebra generated by `c_x` and `𝒞` has a unique form
\[
z=(1-n_x)P+n_xQ+c_x^\dagger X+c_xY,\qquad P,Q,X,Y\in\mathcal C .
\]
Then `(1−n_x) z n_x = c_xY` and `n_x z (1−n_x) = c_x^†X`. If `z` has parity `p`, then `P, Q` have parity `p` and `X, Y` parity `p+1`. If `F ∌ x` and `z` has `(F∪{x})`-charge `k`, then `P, Q` have `F`-charge `k`, `X` has `k−1` and `Y` has `k+1`.

*Proof.* Use a Jordan–Wigner order with `x` first, as in the proof of Lemma G2. Then `c_x = e_{01} ⊗ 1` with `e_{01} = |0⟩⟨1|`, and each `b ∈ 𝒞` of parity `q` is `P_x^q ⊗ b̂`, with `b ↦ b̂` linear and injective. Since `P_x e_{00} = e_{00}`, `P_x e_{11} = −e_{11}`, `e_{10}P_x = e_{10}` and `e_{01}P_x = −e_{01}`, the four maps `P ↦ (1−n_x)P`, `Q ↦ n_xQ`, `X ↦ c_x^†X`, `Y ↦ c_xY` send `𝒞` bijectively onto `e_{00}⊗𝒞̂`, `e_{11}⊗𝒞̂`, `e_{10}⊗𝒞̂` and `e_{01}⊗𝒞̂`. These four spaces form a direct sum equal to the whole algebra. This gives existence and uniqueness. `n_x` commutes with `𝒞`, so `(1−n_x)zn_x` keeps only the term `c_xY`, and `n_xz(1−n_x)` keeps only `c_x^†X`. Parity and `Ad e^{iθN_F}` map each of the four spaces into itself, so by uniqueness they act term by term. `Ad e^{iθn_x}` multiplies the four terms by `1, 1, e^{iθ}, e^{−iθ}`. ∎

**Lemma T′ (two amplitudes).** Let `x ∈ A`, `G = G_x`, and `y ∈ 𝔐_x` a neighbour of `x`. Then
(a) `(1−n_x) G^* c_y G n_x ≠ 0`;
(b) `n_x G n_x G^* (1−n_x) ≠ 0`.

*Proof.* Use the two blocks of Lemma T for the edge `{x,y}` of `O_x`, at angle `a = a_o`. In a block, `|x⟩` has `n_x = 1`, and `|y⟩`, `|z⟩` have `n_x = 0`; `G` and `G^*` map the block to itself. Write `g_{vx} = ⟨v|G|x⟩`.

(a) `G|x⟩ = Σ_v g_{vx}|v⟩`. `c_y` kills `|x⟩` and `|z⟩` (no particle at `y`) and maps `|y⟩` to the matter-empty state `|∅; m_y⟩` with the link values of `|y⟩`. Every term of `H_O` contains an annihilator, so `G^*` fixes matter-empty states. Hence `(1−n_x)G^*c_yGn_x|x⟩ = g_{yx}|∅; m_y⟩`. Lemma T gives `g_{yx} ≠ 0` in one of the blocks.

(b) In a block `n_x` acts as `|x⟩⟨x|`, so `⟨y|Gn_xG^*|x⟩ = g_{yx}\overline{g_{xx}}`. In the two-site block, `g_{xx} = cos(aβ)` and `g_{yx} = iσ sin(aβ)`; the product vanishes only if `sin(2aβ) = 0`. In the three-site block, Lemma T's formula gives `g_{xx} = 1 + (cos aω − 1)β^2/ω^2 = (1 + cos aω)/2` and `g_{yx} = iσ_1β sin(aω)/ω`; the product vanishes only if `sin(aω) = 0` (`cos aω = −1` forces `sin aω = 0`). If both vanish, then `2aβ = kπ` and `aω = k'π` with nonzero integers `k, k'`, since `a ≠ 0`. Then `k'/k = ω/(2β) = 1/√2`, which is irrational. So `(1−n_x)(Gn_xG^*)n_x ≠ 0` in one block. `Gn_xG^*` is self-adjoint, so the adjoint `n_x(Gn_xG^*)(1−n_x)` is nonzero too. ∎

[check] `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/b5b/outflow.py` rebuilds every block of `blocks.py` (odd cube `{1,2}^3`, all corners and edges) for `S = 1/2, 1, 3/2, 2`. It compares `|g_{yx}g_{xx}|` from `expm` with the closed forms above at 45 angles, including `aβ = π/4, π/2, π` and `aω = π, 2π`. All 4320 cases match. The larger of the two block values never vanished; `g_{yx} ≠ 0` held in some block in every case.

### 7.4 Proof of Theorem B5b-T

*Step 0 (reduction and the key identity).* `φ ∘ Ad L^{in}` is a frame on `A`, and `ψ = (φ∘Ad L^{in}) ∘ Ad L^{out}`. Rename `φ∘Ad L^{in}` as `φ` and `L^{out}` as `L`. A conclusion `Ad(D_λW)` for the new `φ` gives `Ad(D_λ W L^{in*})` for the old one. So assume `L` acts on links not internal to `A`.

Put `ψ' = γ_E ψ γ_E^{-1}` and `χ = γ_e^{-1} ψ γ_e`. From `ψ γ_eγ_oγ_E = γ_eγ_oγ_E ψ`,
\[
\chi=\gamma_o\,\psi'\,\gamma_o^{-1}. \tag{7.1}
\]
By (H1), `φ' = γ_Eφγ_E^{-1}` and `φ_1 = γ_e^{-1}φγ_e` are frames on `A`. Also `γ_E Ad L γ_E^{-1} = Ad L'` with `L' = W_E^*LW_E`, a unitary on the links of `supp L`. And `γ_e^{-1} Ad L γ_e = Ad R` with `R = M_eLM_e^*`. By E1, `R` uses only the gates `G_B` of even cubes `B` that have a link of `supp L` inside; `B ≠ A`, because no link of `supp L` is internal to `A`. So `R` is an even unitary in `𝒪_A`. Thus
\[
\psi'=\varphi'\circ\operatorname{Ad}L',\qquad \chi=\varphi_1\circ\operatorname{Ad}R ,
\]
and for `a ∈ 𝒜_A`, `b ∈ 𝒪_A`: `ψ'(ab) = φ'(a)·L'bL'^*` and `χ(ab) = φ_1(a)·RbR^*`. Here `Ad L'` changes links only. `Ad R` may also change matter outside `A`.

*Step 1 (one side of the odd layer: each mode goes to itself or its conjugate).* Fix `x ∈ A`, `G = G_x`, and a neighbour `y ∈ 𝔐_x` of `x`. `ψ'(c_y) = c_y`, since `φ'` fixes `𝒪_A` and `Ad L'` fixes matter. By (7.1) and (H2), `χ` fixes `Z = γ_o(c_y) = G^*c_yG`. Expand `Z` by Lemma D with `𝒞` generated by the modes of `𝔐_x` and the links of `O_x`. Each hop term of `H_O` moves one particle inside `O_x`, so `G` commutes with `n_x + N_{𝔐_x}`, and `Z` has `O_x`-charge `−1`. So `P, Q` have `𝔐_x`-charge `−1`, `X` has `−2` and `Y` has `0`. `Z` is odd, so `X, Y` are even. `Y ≠ 0`, since `c_xY = (1−n_x)Zn_x ≠ 0` by Lemma T′(a). With `d = φ_1(c_x)`, `χ(Z) = Z` reads
\[
\varphi_1(1-n_x)\,RPR^*+\varphi_1(n_x)\,RQR^*+d^\dagger\,RXR^*+d\,RYR^*=(1-n_x)P+n_xQ+c_x^\dagger X+c_xY .
\]
Use the representation in the proof of Lemma G2, with the modes of `A` first: each `b ∈ 𝒪_A` of parity `q` (in a finite region holding every term) is `P_A^q ⊗ b̂`, and `ab = (aP_A^q) ⊗ b̂` for `a ∈ 𝒜_A`. The hat map commutes with `Ad e^{iθN_{𝔐_x}}`, because `N_{𝔐_x}` is even and lies outside `A`. Choose a linear functional `f` on the outside factor with `f(Ŷ) = 1` and `f = 0` on the `𝔐_x`-charge `−1` and `−2` subspaces. This is possible because `Ŷ ≠ 0` lies in the charge-0 subspace. Apply `id ⊗ f` and keep the odd part in `𝒜_A`. The right side gives `c_x`. On the left, `φ_1(1−n_x)P_A` and `φ_1(n_x)P_A` are even (Lemma G1: `φ_1` preserves parity). So `c_x = t d^† + s d` for scalars `t, s`. Taking adjoints, `c_x^† ∈ span{d, d^†}`. So `span{c_x, c_x^†} = span{d, d^†}`, both of dimension 2. Write `d = uc_x + vc_x^†`. Then `d^2 = 0` gives `uv = 0`, and `dd^† + d^†d = 1` gives `|u| = 1` or `|v| = 1`. Hence
\[
\varphi_1(n_x)=d^\dagger d\in\{\,n_x,\ 1-n_x\,\}. \tag{7.2}
\]
Step 1 alone allows the flip `c_x ↦ vc_x^†`, because `Ad R` may change outside matter (compare Theorem 5.1).

*Step 2 (the other side: no flip).* By (7.1), `ψ' = γ_o^{-1} χ γ_o`. Put `Z' = γ_o^{-1}(n_x) = Gn_xG^*` (H2). `χ` acts on `n_x ∈ 𝒜_A` as `φ_1`, so by (7.2), `ψ'(Z') = γ_o^{-1}(φ_1(n_x))` equals `Z'` or `1 − Z'`. Expand `Z' = (1−n_x)P' + n_xQ' + c_x^†X' + c_xY'` by Lemma D. `Z'` is even and has `O_x`-charge 0, so `X'` is odd with `𝔐_x`-charge `−1`. `X' ≠ 0`, since `c_x^†X' = n_xZ'(1−n_x) ≠ 0` by Lemma T′(b). Let `E_{−1}(z) = (2π)^{-1}∫_0^{2π} e^{iθ} Ad e^{iθN_{𝔐_x}}(z) dθ`, the charge `−1` part. It fixes `𝒜_A` pointwise, satisfies `E_{−1}(ab) = aE_{−1}(b)`, and commutes with `Ad L'` by (H3). Apply `E_{−1}` to `ψ'(Z') = ±Z' + (0` or `1)`:
\[
\varphi'(c_x^\dagger)\;L'X'L'^*=\pm\,c_x^\dagger X' .
\]
Lemma G2(b), with `𝒞_1 = 𝒜_A` and the odd nonzero elements `L'X'L'^*` and `X'`, gives `φ'(c_x^†) = κc_x^†`. The CAR give `|κ| = 1`. So `φ'(c_x) = λ_xc_x` with `λ_x = \bar κ`.

*Step 3 (all corners).* Steps 1-2 hold for each `x ∈ A`. Step 5 of the proof of Theorem B5b, applied to `φ'`, gives `φ'|_{𝒜_A} = Ad(D_λW')` with `W'` on A's internal links. On `𝒜_A`, `γ_E = Ad W_A^*` with `W_A = ∏_{ℓ⊂A} e^{−iτ_EE_ℓ^2}`. So `φ = γ_E^{-1}φ'γ_E = Ad(W_AD_λW'W_A^*) = Ad(D_λW)` with `W = W_AW'W_A^*`, because `W_A` commutes with `D_λ`. Undo Step 0. *Converse:* the converse of Theorem B5b gives every `λ` with a link-by-link `L` and every gate unchanged; then `ψ` commutes with each layer, hence with `α`, with `c = 1`. ∎

**The key step.** The attacks in section 5.3 expanded `α(c_y)` across both layers. This proof cuts the tick at the odd layer, (7.1). The even layer and the electric layer respect the cut between `𝒜_A` and `𝒪_A` (H1). So both `χ` and `ψ'` are still products across the cut. `χ`'s outside factor may change outside matter; Step 1 treats it as reading R-M does and gets at most a flip. `ψ'`'s outside factor changes registers only; Step 2 removes the flip. The missing step of section 5.3 (occupations preserved) is (7.2) plus Step 2.

### 7.5 Half-step variant

`LW1.md` line 64: "the Schrödinger half-step operators are \(W_{2n}=M_e\) and \(W_{2n+1}=W_EM_o\)."

**Proposition 7.2.** Let `φ` be a frame on `A` and `L_o` a split register change with `ψ_o = φ∘Ad L_o` commuting with `γ_o∘γ_E` (invariance of the half-step `W_EM_o`, up to a phase). Then `φ|_{𝒜_A} = Ad(D_λW)`. Invariance of `M_e` alone does not restrict the mode image: `Ad G_A` is a frame on `A` that commutes with `γ_e`, and by Lemma T for the even cube it does not map `c_x` to a multiple of `c_x` (that would make `G_A` commute with `n_x`).

*Proof.* Absorb `L_o^{in}` as in Step 0. `ψ_o` fixes `c_y`, so it fixes `γ_oγ_E(c_y) = G^*c_yG = Z`. Expand `Z` as in Step 1. Now `ψ_o(ab) = φ(a)·L_obL_o^*`, and `Ad L_o` commutes with `Ad e^{iθN_{𝔐_x}}` (H3). Take the `𝔐_x`-charge-0 part of `ψ_o(Z) = Z`: `φ(c_x)·L_oYL_o^* = c_xY`. Both outside factors are even and nonzero (Lemma T′(a)). Lemma G2(b) gives `φ(c_x) = λ_xc_x`. Finish with Step 5 of Theorem B5b. ∎

So under "invariance of `M_e` and of `W_EM_o` separately", the odd half-step alone gives the mode image `U(1)^8`; the even one adds nothing on modes.

### 7.6 B5b-E: register changes not split at `A`

Section 5.2 asked whether a gate-compatible frame with a non-scalar operator-valued phase `u_x` exists when register changes may entangle A's internal and outside registers. It exists. The answer is a full classification.

**Theorem 7.3 (reading R-E, odd gates).** For a frame `φ` on `A` the following are equivalent.
(i) For each corner `x` there are a unitary `L_x` on finitely many links (split or not) and a real `a_x ≠ 0` with `(φ∘Ad L_x)(e^{ia_xH_{O_x}}) = e^{ia_xH_{O_x}}`.
(ii) `φ|_{𝒜_A} = Ad(W_0 ∏_{x∈A} e^{−in_xh_x})` for a unitary `W_0` and pairwise commuting Hermitian `h_x`, all on A's internal links.
In case (ii), `φ(n_x) = n_x` for every `x`, and `φ(c_x) = c_x·W_0e^{ih_x}W_0^*`.

*Proof.* (i) ⇒ (ii). Proposition 5.2 gives `φ^{-1}(c_x) = c_xu_x` with `u_x` a unitary on A's internal links. The `u_x` commute with matter. For `x ≠ x'` the CAR give `0 = {φ^{-1}(c_x), φ^{-1}(c_{x'})^†} = c_xc_{x'}^†(u_xu_{x'}^* − u_{x'}^*u_x)`. In `𝔄^m_A ⊗ 𝔏_A` with `c_xc_{x'}^† ≠ 0`, this gives `u_xu_{x'}^* = u_{x'}^*u_x`, so `u_x` and `u_{x'}` commute. Let `φ^{-1}|_{𝒜_A} = Ad V` (Lemma G1). `φ^{-1}(n_x) = u_x^*n_xu_x = n_x`, so `V` commutes with every `n_x`. With `P_σ` the occupation projectors of A (`LW1.md` line 69) and `P_σ𝒜_AP_σ = P_σ ⊗ 𝔏_A`, this gives `V = Σ_σ P_σ ⊗ V_σ`. For `σ_x = 1`, compare the `P_{σ−e_x}(·)P_σ` parts of `Vc_xV^* = c_xu_x`; since `P_{σ−e_x}c_xP_σ ≠ 0`, `V_{σ−e_x}V_σ^* = u_x`. So `V_σ = (∏_{x:σ_x=1}u_x^*)V_0`, that is, `V = ∏_x(1−n_x+n_xu_x^*)·V_0`. Diagonalize the commuting `u_x` together and write `u_x = e^{−ih_x}` with commuting Hermitian `h_x`. Then `1−n_x+n_xu_x^* = e^{in_xh_x}`, and `φ = Ad V^* = Ad(V_0^*∏_xe^{−in_xh_x})`. Put `W_0 = V_0^*`.

(ii) ⇒ (i). `LW1.md` line 45: "\(\mathcal G_x=n_x+\sum_{\ell\text{ out of }x}E_\ell-\sum_{\ell\text{ into }x}E_\ell\)". Split `𝒢_x = n_x + E^A_x + E^o_x`, with `E^A_x` the part on A's internal links and `E^o_x` the part on the three links of `O_x` at `x`. Take `L_x = e^{−ih_xE^o_x}`, a unitary on A's internal links and those three links. It is not split when `h_x` is not a scalar. All factors below commute, since `h_x` sits on A's internal links:
\[
W_0\prod_{x'}e^{-in_{x'}h_{x'}}\cdot L_x=W_0\prod_{x'\ne x}e^{-in_{x'}h_{x'}}\cdot e^{-ih_x(n_x+E^o_x)} .
\]
`LW1.md` line 231 (B4): "Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\)." `G_x` commutes with `𝒢_x` (B4) and with `E^A_x` (disjoint links, Lemma 2.1), so with `n_x + E^o_x`. `G_x` commutes with `h_x`, `W_0` and `n_{x'}`, `x' ≠ x` (disjoint supports). So `G_x` commutes with the right side. That is (i), with `a_x = a_o`. ∎

**Counterexample to "u_x scalar".** Take `W_0 = 1`, `h_x = θE_m` for one internal link `m` with `θ ∉ 2πZ`, and `h_{x'} = 0` otherwise. Then `φ(c_x) = c_xe^{iθE_m}`: an operator-valued phase on a register. `φ` satisfies (i) for every `S`, every angle and every `τ_E`.

*What R-E means.* Under R-E the frames of (ii) mix no two modes and fix every `n_x`. They do not map A's mode algebra to itself, so they have no mode image. The set (ii) is not closed under composition in general: an entangling `L_x` does not commute with a second frame. So "the frame group" is not defined in this reading without more structure.

**Lemma 7.4.** If an operator `O` on A's internal links commutes with `H_A`, then `O` is a scalar.

*Proof.* `[O, H_A] = 3^{−1/2}Σ_{ℓ=(x,y)}η(c_y^†c_x ⊗ [O,J_ℓ] + c_x^†c_y ⊗ [O,J_ℓ^†])`. The operators `c_y^†c_x` for distinct ordered pairs are linearly independent: `c_y^†c_x|x'⟩ = δ_{xx'}|y⟩` on one-particle states. So `[O,J_ℓ] = [O,J_ℓ^†] = 0` for every internal link. `[J_ℓ,J_ℓ^†] = 2E_ℓ`, and `E_ℓ` has simple spectrum, so the algebra generated by `J_ℓ, J_ℓ^†` contains each `|m⟩⟨m|` and each `J_ℓ|m⟩⟨m| ∝ |m+1⟩⟨m|`: it is the whole matrix algebra of link `ℓ`. So `O` commutes with all of `𝔏_A` and is a scalar (Lemma G3). ∎

The construction (ii) ⇒ (i) works because `h_x` commutes with every odd gate. By Lemma 7.4 a non-scalar `h_x` does not commute with `H_A`. So the construction does not carry over to the even gate as it stands. **B5b-E′ (open):** which frames of (ii) also leave the even gate unchanged after some entangling register change, and the whole-update case R-T with entangling register changes. In the latter, Step 0 fails: `M_eLM_e^*` is not in `𝒪_A` when `L` entangles A's internal links with outside links.

### 7.7 What section 7 does not settle

- The register factors: which `W` and `L` go with a given `λ` under Hypothesis T. The mode image does not depend on it.
- A plaquette layer `W_B`. If its gates join A's internal links to outside links, `γ_Eγ_B` does not respect the cut, and Step 2 fails as written. `W_B` is unspecified (GA1-P).
- B5b-E′ (section 7.6).

### 7.8 Four-test check of the readings used in section 7

*Hypothesis T* (B5b-T's identity at infinite volume read as `ψ∘α = α∘ψ`).
1. It names no group; the group is derived. Pass.
2. It is closed: one automorphism identity. Pass.
3. It settles no downstream question by premise: on every finite torus it is equivalent to `ψ(U_0) = cU_0` (section 7.1), so it adds and removes no frames relative to R-T's text. Pass.
4. It adds no structure or constants. Pass.

*Half-step reading* (each half-step unchanged under its own split register change).
1. Pass. 2. Pass. 4. Pass.
3. It is stronger than R-T. Proposition 7.2 shows that its odd half alone gives the same mode image as R-T, so on modes it excludes nothing that R-T allows. Pass on modes; the register factors may differ.

Section 1.3's test 3 for gate-wise invariance was conditional on B5b-T. Theorem B5b-T gives the same mode image, so test 3 now passes for register changes split at `A`. The gate-wise reading (odd gates only) allows every `W`; R-T may allow fewer. That difference lies in the registers, not the modes. Under R-E the two readings are not yet compared (B5b-E′).

---

## FINISH

**Proved here (pass 1, not refereed).**
- Lemma 2.1 (each corner of an even cell in its own odd cube; no shared links).
- Lemma G1 (a local frame has a homogeneous implementer), Lemma G2 (splitting across disjoint supports, graded), Lemma G3 (inner automorphisms of `M_n`; the commutant of `M_n ⊗ 1`).
- Lemma T (every dressed cube gate `e^{iaH_C}`, `a ≠ 0`, any `S`, moves one particle across each edge with nonzero amplitude; by `√2` irrational).
- **Theorem B5b**: under B5(b)'s gate-wise hypothesis with split register changes, every frame on an even cell is `Ad(D_λW)`: site phases times an internal-link unitary. The mode image is exactly `U(1)^8`, abelian, at every nonzero angle and spin. Only the eight odd gates are used.
- Corollary B5b.1 (one-site frames are phases; the particle-hole branch of B3 is excluded without assuming number preservation).
- Theorem 5.1 (reading R-M: image `U(1)^8 ⋊ Z_2`, all-or-none charge conjugation).
- Proposition 5.2 (reading R-E: `φ^{-1}(c_x) = c_xu_x` with `u_x` a unitary on internal links).
- Section 7 (added 2026-11-05): Lemma D (decomposition along one mode); Lemma T′ (each odd gate has nonzero outflow `(1−n_x)G^*c_yGn_x` and nonzero `n_xGn_xG^*(1−n_x)`, at every `a_o ≠ 0` and `S`; by `√2` irrational).
- **Theorem B5b-T**: under invariance of the whole tick `U_0` up to a phase, by one frame and one register change split at `A`, every frame on an even cell is `Ad(D_λW)`. The mode image is exactly `U(1)^8`. It uses only `a_o ≠ 0`; any `a_e`, `τ_E`, `S`; `c` plays no role. Key step: cut the tick at the odd layer; the even and electric layers respect the cut.
- Proposition 7.2 (half-step variant: invariance of `W_EM_o` alone gives `Ad(D_λW)`; `M_e` alone restricts nothing on modes).
- Theorem 7.3 (reading R-E, odd gates: the gate-compatible frames are exactly `Ad(W_0∏_xe^{−in_xh_x})` with commuting internal-register `h_x`). Lemma 7.4 (no non-scalar internal-register operator commutes with `H_A`).

**Counterexamples.**
- To the draft's scalar claim: `U(1)^8` (as in `LW1.md` line 245, rechecked in the converse of Theorem B5b).
- To "abelian" under reading R-M: the sign-twisted charge conjugation `C_A` (Theorem 5.1), with compensations that change matter of neighbouring cells. It mixes no modes, reverses number, and is outside PS-6's register wording.
- To "`u_x` scalar" under reading R-E with the odd gates (B5b-E): `φ(c_x) = c_xe^{iθE_m}`, `m` an internal link, `θ ∉ 2πZ`, compensated by `L_x = e^{−iθE_mE^o_x}` (section 7.6). It holds for every angle, `S` and `τ_E`.

**Open, by name.**
- **B5b-E′**: reading R-E (register changes that entangle A's internal and outside registers) with the even gate added, or with only the whole update unchanged. No attack is recorded yet; section 7.6 notes why the odd-gate construction does not carry over as it stands (Lemma 7.4), and why Step 0 of section 7.4 fails.
- The register factors `W`, `L` that go with a given `λ` under whole-update invariance (not needed for the mode image).
- A plaquette layer `W_B` whose gates join A's internal links to outside links (section 7.7; `W_B` is unspecified).
- Not needed and not settled: whether `H_O` has exceptional angles in the window, and the full compensation group at such angles.

**What changes downstream.**
- CH1 S3 (i) holds for cell frames under gate-wise invariance and under PS-6's whole-update wording, with register changes split at the cell, including many-body frames (Theorems B5b and B5b-T).
- D1: the named step is proved in both the gate-wise and the whole-update readings (sections 6 and 7); B5b-T no longer holds D1 back. The owner decides whether it triggers PS-5's fallback. The reading question left is R-E (B5b-E′).
- GA1-i: `U(1)` per site for one-mode cells of `L_cube` in the gate-wise and whole-update readings with split register changes; the SU(2) rung needs content beyond one mode per site or emergence.

**Inputs from outside the working set.** The CAR reading of one site mode and parity superselection, as in LW1's premises (`LW1.md` line 18). The law `L_cube` with its definitions (LW1 sections 1-2) and LW1's Lemma A1 and Theorems B3-B4. Standard mathematics, rebuilt in the text: Jordan–Wigner representation, elementary-tensor uniqueness, inner automorphisms of `M_n(C)` (Skolem–Noether in this case), irrationality of `√2`. Section 7 adds LW1's Theorem E1 (layers as automorphisms) and, from standard mathematics, joint diagonalization of commuting unitaries and the fact that `J, J^†` generate the full matrix algebra of one link (rebuilt in Lemma 7.4). Literature context from memory, not load-bearing: local gauge invariance with link registers in Hamiltonian lattice gauge theory (Kogut–Susskind) and quantum link models (Horn; Orland–Rohrlich; Chandrasekharan–Wiese), where site phases compensated by `e^{iθE}` on links are the standard `U(1)` gauge transformations.
