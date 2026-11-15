# LW1-5, pass 1 (long draft): the law on five-mode sites

Written 2026-11-05 by a Claude Opus 5.5 subagent, as pass 1 of the open item LW1-5 of the TOE assembly (method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (scripts outside the repo, in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/lw15/`, under 100 MB, under a minute); a check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (same commit as `origin/claude/toe-assembly`) | `b913d2d2e1` |
| `origin/claude/toe-why-five-modes-20261021` (#10014, closed) | `3d00c61f05` |
| `origin/claude/toe-composite-sixteen-20261021` (#10027, closed) | `fc76a41135` |

Files read at those commits, by line: `TOE_ASSEMBLY.md` lines 71-210 (section 3 in full, with 3.4), 225-254 (LW1), 342-421 (MT1, GA1, GA2, CH1, CG1); `LW1.md` lines 1-503 (all); `B5B_DRAFT.md` lines 1-428 (all); `CH1_DRAFT.md` lines 224-283 (Lemma S1, Theorems S2 and S3, section 5.1); the #10014 note `docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md` (all 201 lines, by `git show`); the #10027 note `docs/SPIN10_MOTT_SITES_CARRY_NO_COMPOSITE_SIXTEEN_THE_CENTRE_FIXES_EVERY_FERMION_TO_THE_VECTOR_CLASS_BOUNDED_THEOREM_NOTE_2026-10-22.md` (frontmatter and sections A-B, by `git show`); PR #10027's body (`gh pr view 10027`).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". PS-5, PS-6 and PS-6r are read plainly. Where the plain words allow more than one reading, each reading is named and treated, and nothing is adopted. Proposed specifications carry the four-test check.

**Working set used, by name.** PS-5 (fallback text, D1), PS-6 and PS-6r (frames and registers), PS-1 read by PS-1c (the update and its covariance), PS-3 read by PS-3h and PS-3c (only in sections 9-10, for carry-over), PS-7 read by PS-7r (only in section 9), PS-11 read by PS-11c (section 9), PS-Ar (section 9). LW1 results used are named where they are used. PS-2 and PS-4 are not used.

---

## 0. The open item, quoted

`TOE_ASSEMBLY.md` line 205 (PS-5, in the working set since D1): "Each site has the possibilities of five fermion modes; its full algebra is `Cl(10)`, presented as `M_32(C)`."

Line 208: "The law on five-mode sites is a new open item, **LW1-5**. It needs a covariant local update, with link registers on which the site frame group acts, that keeps that group exact. #10014 records that "no nearest-neighbour inter-cluster coupling keeps Spin(2N>2) exact" for clusters of one-mode sites. Whether a number-conserving hop on five-mode sites keeps more than `U(5)` is LW1-5's first question."

Line 133 (PS-6): "The internal frame of each site's possibilities is local. Each nearest-neighbour link carries a register that transports frames between its two sites. The update is unchanged when the frame at one site and the registers on its links are changed together."

Line 183 (PS-6r): "Each link register is a finite quantum link: a finite-dimensional register on which the frame group of the site content acts, with the raising and lowering structure the Gauss law needs. Link registers carry odds but no actual configuration and no records."

Line 136 (PS-6, "What it lets us derive"): "With five modes it is `Spin(10)`, which contains the Standard Model group".

#10014 claim_scope (in part): "Suppose N identical complex fermion modes are carried per frame cell, the frame group is the full Bogoliubov group Spin(2N) of those modes, and the light content is one fermion-parity half S+ ... With one mode per site, no 5-site cluster tiles Z^3 covariantly, and no nearest-neighbour inter-cluster coupling keeps Spin(2N>2) exact." Its section (3) gives the reason: "By Schur, the only Spin(2N)-invariant coupling between two clusters' Majorana vectors is the identity (W5)." That is a statement about c-number couplings under one global group, on clusters of one-mode sites.

#10027 claim_scope (in part): "(B, exact, any Spin(10)-invariant H at any coupling and range) The element -1 of Spin(10) is the c-number (-1)^n_sites ... every fermion-parity-odd excitation is in the vector class (10, 120, 126, ...), never a spinor 16."

## 0.1 Outcome in one paragraph

**The frame group is fixed by the update, not by the site content.** PS-6 read plainly, with B5B's Lemma G1, makes the local frames of a five-mode site the group `G_full` of all parity-respecting automorphisms of `M_32(C)`, of dimension 511 (Theorem C). The Bogoliubov group `O(10)` and `U(5)` are subgroups of it. For one mode the three coincide, which is why `L_cube` never had to choose. **(a) is proved:** if a gate's generator moves one site mode at each end of a link (each term has one site Majorana at each end) and every mode takes part, every compatible frame is Bogoliubov, `O(10)`; if the hop also conserves matter number, every compatible frame lies in `U(5)`, so the Bogoliubov part of `Spin(10)` is broken (Theorem M). The proof is at the generator level and, for gates, at every angle outside a discrete exceptional set. **(b) is proved:** a Majorana hop `(i/2) Σ γ_{y,a} U_ℓ^{ab} γ_{x,b}`, with `U_ℓ^{ab}` the mixed generators of a finite-dimensional representation `R` of `so(20)` on each link (the quantum-link construction of Brower, Chandrasekharan and Wiese, rebuilt in Lemma Q), keeps `Spin(10)` exact at every angle. Its Gauss law `𝒢_x^{cd} = M_x^{cd} + Σ_{ℓ∋x} L^{cd}_{ℓ,x}` commutes with every gate (Theorem G). Reflections are exact exactly when `R` is isomorphic to its reflected twist; the half-spinor register `S_+` (dimension 512) breaks them, so its exact group is `SO(10)` on the algebra and `Spin(10)` on states (Theorem R). The full `G_full` is also reachable, by a law whose hop moves arbitrary odd site operators (Proposition A). **(c):** none of `Spin(10)`, `Pin(10)`, `U(5)` is the plain PS-6 group; each is the exact group of a named law. Three structural facts follow for the `Spin(10)` law. With one register class on all links, no state of a site and its link ends is a Gauss singlet, because the centre element `−1` acts there as the scalar `−1` (Proposition Σ). Every fermion-odd gauge-covariant operator is in the vector class, never the 16: #10027's centre theorem holds on the gauged law (Lemma Z). Every locally gauge-invariant state is half filled in every mode (Lemma H), so PS-7's filling is automatic there. The candidate laws are `L5-O[R]` (Majorana hop, `so(20)` registers) and `L5-U` (number-conserving hop, `u(10)` rishon registers). At one mode `L5-U` with one rishon per link is `L_cube` with `S = 1/2`; `L5-O` has the same gauge group there (`SO(2) = U(1)`) but also pairing hops. Geometry, free-tick results, factorization, infinite-volume dynamics and the transport existence results carry over. PS-3h's "site occupations" are not frame invariant on five-mode sites; restated, the actual value of a site is its parity under `L5-O[S_+]` and its number under `L5-U`. B8, B8a, B8b, B11 and E2b need restatements, proved in section 9. The first open item is **LW1-5-X**: the frame bound at the exceptional angles of the cube gate. A [check] shows that for a single-link gate an exceptional angle does enlarge the frame algebra.

---

## 1. Setting and definitions

### 1.1 One five-mode site

At a site `x` take ten Hermitian Majorana generators `γ_{x,1}, …, γ_{x,10}` with `{γ_{x,a}, γ_{y,b}} = 2δ_{xy}δ_{ab}`. The five modes are `c_{x,j} = (γ_{x,2j−1} + iγ_{x,2j})/2`, `j = 1, …, 5`. So `γ_{x,2j−1} = c_{x,j} + c_{x,j}^†` and `γ_{x,2j} = i(c_{x,j}^† − c_{x,j})`. Put `n_{x,j} = c_{x,j}^†c_{x,j}` and `N_x = Σ_j n_{x,j}`. Then
\[
n_{x,j}-\tfrac12=\tfrac i2\,\gamma_{x,2j-1}\gamma_{x,2j},\qquad
P_x:=(-1)^{N_x}=(-i)^5\,\gamma_{x,1}\gamma_{x,2}\cdots\gamma_{x,10}.
\]
Write `M_x^{ab} = (i/2)γ_{x,a}γ_{x,b}` for `a ≠ b`. A direct computation gives
\[
[M_x^{ab},\gamma_{x,c}]=i(\delta_{bc}\gamma_{x,a}-\delta_{ac}\gamma_{x,b}). \tag{1.1}
\]
`𝒜_x` is the algebra generated by the `γ_{x,a}`. A Jordan–Wigner map inside `x` makes it `M_32(C)` on `H_x = Λ(C^5) = H_+ ⊕ H_−`, the even and odd Fock subspaces, each of dimension 16. Parity of elements of `𝒜_x` is the grading `Ad P_x`. This is PS-5's text: five fermion modes, the algebra `Cl(10)`, presented as `M_32(C)`.

The matter algebra of all sites is the CAR algebra of all the `c_{x,j}` (as in `LW1.md` line 35, now with five modes per site). Links are as in `LW1.md` line 42: "Link algebras are ordinary tensor factors and commute with matter."

### 1.2 Frames, register changes, compatibility

Let `𝒪_x` be the algebra generated by all matter modes of other sites and all links.

**Definition F1 (frame at `x`).** A frame at `x` is an automorphism `φ` of the quasi-local algebra with `φ(𝒜_x) = 𝒜_x` and `φ(z) = z` for `z ∈ 𝒪_x`. This is B5B's Definition F with `A = {x}`; a site has no internal links.

**Definition R1 (register change).** A register change is `Ad L` with `L` a unitary on finitely many links. Since `x` has no internal links, every register change is split at `{x}` in B5B's sense, so B5B's reading R-E (entangling register changes) adds nothing for site frames.

**Compatibility.** For a Hermitian `H` in the algebra of one cube and its links, `φ` is *compatible with `H`* if there is a register change `Ad L` with `(φ∘Ad L)(H) = H`. It is *compatible with the gate `e^{iaH}`* if `(φ∘Ad L)(e^{iaH}) = e^{iaH}` for some such `L`. Gate-wise invariance (B5(b)'s hypothesis, B5B section 1.2) asks this for every gate of the update.

**Exceptional angles.** For `H` as above with distinct eigenvalues `λ_1, …, λ_m`, put `𝔈(H) = {a ∈ R : a(λ_k − λ_l) ∈ 2πZ∖{0} for some k ≠ l}`. It is a discrete subset of `R`.

**Hop classes.** Let `O` be a cube containing `x`, and `𝔐 = O ∖ {x}`. Let `𝒞_O ⊂ 𝒪_x` be generated by the matter of `𝔐` and the links of `O`.
- `H` has *one-mode inflow at `x`* if `H = Σ_{b=1}^{10} γ_{x,b}B_b + H'` with `B_b ∈ 𝒞_O` odd and `H' ∈ 𝒞_O` even. It is *faithful* if `B_1, …, B_{10}` are linearly independent (every mode at `x` takes part).
- `H` is *number conserving* if it commutes with `N_x + N_𝔐`. Then (Lemma M0 below) `H = Σ_j (c_{x,j}^†X_j + X_j^♯c_{x,j}) + H'`, and it is *faithful* if `X_1, …, X_5` are linearly independent.

### 1.3 Four-test check of the readings used here

Definition F1, the register changes and gate-wise invariance are B5B's, already checked there (B5B sections 1.3 and 7.8). Compatibility with a generator is stronger than with a gate; it is used only through Corollary M.1, which states the angles at which the two agree. The exceptional set is a definition, not a reading. No reading in this section names a group.

---

## 2. The frame group of a five-mode site (item 1(c))

**Theorem C (local frames of a five-mode site).**
(i) The frames at `x` are exactly the maps that act on `𝒜_x` as `Ad V`, with `V ∈ U(32)` homogeneous (`P_xVP_x = ±V`), and as the identity on `𝒪_x`.
(ii) They form the compact Lie group `G_full ≅ ((U(16) × U(16))/U(1)) ⋊ Z_2`, of dimension 511. The identity component consists of the even `V`.
(iii) The Bogoliubov frames, those with `φ(span_R{γ_{x,a}}) = span_R{γ_{x,a}}`, form a closed subgroup isomorphic to `O(10)` (Lemma C1). A Bogoliubov frame has an even implementer exactly when its matrix has determinant one.
(iv) The number-preserving Bogoliubov frames are the `Ad Γ(u)`, `u ∈ U(5)`; they form `U(5)`.
(v) For one mode per site the three groups coincide: `G_full = O(2) = U(1) ⋊ Z_2`, and the number-preserving subgroup is `U(1)`. This is LW1's Lemma B3.

*Proof.* (i) B5B line 98 (Lemma G1): "Let `φ` be a frame on `A`. Then `φ` maps even elements of `𝒜_A` to even ones and odd to odd. There is a unitary `V ∈ 𝒜_A`, unique up to a phase, with `φ|_{𝒜_A} = Ad V`, and `V` is even or odd." Its proof uses only one mode outside `A` and Lemma G3, so it holds for `A = {x}` with `𝒜_A = 𝒜_x ≅ M_32(C)`. B5B line 102 gives the converse: "each homogeneous `V ∈ 𝒜_A` gives a frame: the graded tensor product of `Ad V` on `𝒜_A` with the identity on `𝒪_A`."
(ii) Homogeneous unitaries are block diagonal (even) or block off-diagonal (odd) for `H_+ ⊕ H_−`. The even ones form `U(16) × U(16)`. The odd ones are the even ones times `γ_{x,1}`, which is odd, unitary and squares to one. `Ad V = Ad V'` exactly when `V' = λV` (Lemma G3 uniqueness). So the group is the quotient of `(U(16) × U(16)) ⋊ Z_2` by the central scalars. Its dimension is `256 + 256 − 1`.
(iii) Lemma C1.
(iv) A Bogoliubov frame with matrix `R` preserves `span{c_{x,j}^†}` exactly when `R` commutes with the complex structure `J` that pairs `(2j−1, 2j)`. Then `φ(c_{x,j}^†) = Σ_k u_{kj}c_{x,k}^†`. The CAR force `u` unitary, and `Γ(u)` implements it. The converse is direct.
(v) With one mode, `H_±` are one-dimensional, so `G_full = (U(1) × U(1))/U(1) ⋊ Z_2`; the odd frame is `c ↦ c^†` up to phase. `LW1.md` line 227 (B3): "These transformations form \(U(1)\rtimes\mathbb Z_2\). The number-preserving subgroup is \(U(1)\)." ∎

**Lemma C1 (Bogoliubov automorphisms).** For every `R ∈ O(10)` there is exactly one automorphism `φ_R` of `𝒜_x` with `φ_R(γ_{x,c}) = Σ_b R_{bc}γ_{x,b}`. It is a frame at `x`. It satisfies `φ_R(P_x) = det(R) P_x`, so its implementer is even if `det R = 1` and odd if `det R = −1`.

*Proof.* Put `γ'_c = Σ_b R_{bc}γ_b`. Orthogonality of `R` gives `{γ'_c, γ'_d} = 2δ_{cd}`, and the `γ'_c` are Hermitian. For a subset `S` of `{1, …, 10}` let `γ'_S` be the ordered product. If `S ≠ ∅`, `γ'_S` is traceless on `C^32`: if `|S|` is odd and `S ≠` everything, a `γ'_b` with `b ∉ S` anticommutes with it; if `|S|` is even, any `γ'_a` with `a ∈ S` anticommutes with it; in both cases `tr γ'_S = tr(γ'_bγ'_Sγ'_b) = −tr γ'_S`. So the `2^{10}` products are orthogonal in the trace inner product (`(γ'_S)^*γ'_T = ±γ'_{SΔT}`), hence a basis of `M_32(C)`. The same holds for the `γ_S`. The linear map `γ_S ↦ γ'_S` is multiplicative, because both families obey the same Clifford multiplication table. So it is an automorphism; it is unique because the `γ_c` generate. It is a `*`-map because `(γ'_S)^*` is computed by the same rule. The `γ'_c` pairwise anticommute, so `γ'_1 ⋯ γ'_{10}` equals its own antisymmetrization, which is `det(R) γ_1 ⋯ γ_{10}`. Hence `φ_R(P_x) = det(R)P_x`. `φ_R` preserves parity, so by Lemma G3 and the last step of Lemma G1's proof its implementer `V` is homogeneous, and `VP_xV^* = ±P_x` as `V` is even or odd. So `φ_R` is a frame (Theorem C(i)), even exactly when `det R = 1`. ∎

**Lemma C2 (frame-invariant site observables).** Let `𝒱(K)` be the elements of `𝒜_x` fixed by every frame in a set `K`.
(i) `𝒱(SO(10)) = span{1, P_x}`. (ii) `𝒱(O(10)) = C1`. (iii) `𝒱(G_full) = C1`, and the identity component of `G_full` fixes exactly `span{1, P_x}`. (iv) `𝒱(U(5))` contains the spectral projections of `N_x`.

*Proof.* (i) The frames `Ad e^{iθM^{ab}}` (Lemma C1, `det = 1`) fix `z` for all `θ` exactly when `z` commutes with every `M^{ab}`. The `M^{ab}` generate the even part of `𝒜_x`, since every even monomial is a product of quadratic ones. The even part lies in `End(H_+) ⊕ End(H_−)` and has dimension `2^9 = 16^2 + 16^2`, so it is all of it. An operator commuting with `End(H_+) ⊕ End(H_−)` commutes with the projections onto `H_±`, so it is block diagonal, and each block is a scalar (Lemma G3's commutant step). That is `span{1, P_x}`. Conversely `P_x` is even, so it commutes with the even part. (ii) `O(10)` adds `φ_R` with `det R = −1`, which sends `P_x` to `−P_x` (Lemma C1). (iii) Odd frames send `P_x` to `−P_x`; the even ones contain `Ad(U(16) × U(16))`, whose fixed algebra is the same block-scalar algebra. (iv) `Γ(u)` commutes with `N_x`. ∎

*Remark.* Equality in (iv), `𝒱(U(5)) = span{Π_0, …, Π_5}` with `Π_k` the projection onto `N_x = k`, follows from the standard irreducibility of `Λ^k C^5` under `U(5)`. It is not used below.

**Answer to item 1(c).** PS-6's words name "the internal frame of each site's possibilities". Read plainly, with Lemma G1, these frames are `G_full`. That is neither `Spin(10)` nor `Pin(10)` nor `U(5)`. PS-5's other words, "five fermion modes" and "`Cl(10)`", single out two subgroups: the frames that keep the ten Majorana generators as generators (`O(10)`, Lemma C1), and the frames that keep the five modes as modes (`U(5)`). Which of these is *exact* is decided by the update (sections 3-6). `TOE_ASSEMBLY.md` line 136 ("With five modes it is `Spin(10)`") holds for one named law, `L5-O[S_+]` (Corollary R.1), not for PS-6 by itself.

---

## 3. What the hop allows (item 1(a))

**Lemma M0 (decomposition at `x`).** Every `z` in the algebra generated by `𝒜_x` and `𝒞_O` has a unique form `z = Σ_S γ_{x,S} z_S` with `z_S ∈ 𝒞_O` (sum over the `2^{10}` subsets). In the Jordan–Wigner map that lists `x` first, `a b = (aP_x^q) ⊗ b̂` for `a ∈ 𝒜_x` and `b ∈ 𝒞_O` of parity `q`, with `b ↦ b̂` linear and injective.

*Proof.* B5B line 108 (proof of Lemma G2): "Order the modes of `F_1` first in a Jordan–Wigner map. Then `c_u = ĉ_u ⊗ 1` for `u ∈ F_1`, and `c_v = P_1 ⊗ ĉ_v` for `v ∈ F_2` ... each `m ∈ 𝒞_2` of parity `p` equals `P_1^p ⊗ m̂`, and `m ↦ m̂` is linear and injective." Take `F_1 = {x}` (five modes). Links sit in their own ordinary tensor factors. Uniqueness follows because the `γ_{x,S}P_x^q` are a basis of `M_32(C)` (Lemma C1's proof) and the map to the ordinary tensor product is injective. For a number-conserving `H`, the part with `|S| = 1` has the stated form after the change of basis `γ ↔ c, c^†`; terms with `|S| ≥ 2` are absent from a hop by definition of the class. ∎

**Theorem M (the hop bounds the frame group).** Let `φ` be a frame at `x`, `Ad L` a register change, `ψ = φ∘Ad L`, and `H` a Hermitian generator with faithful one-mode inflow at `x`, with `ψ(H) = H`.
(i) `φ` is a Bogoliubov frame: `φ(γ_{x,c}) = Σ_b R_{bc}γ_{x,b}` with `R ∈ O(10)`.
(ii) If `H` is also number conserving with faithful inflow, then `φ = Ad Γ(u)` on `𝒜_x` with `u ∈ U(5)`.

*Proof.* (i) In the representation of Lemma M0, `H` becomes `Σ_b (γ_bP_x) ⊗ B̂_b + 1 ⊗ Ĥ'` (write `γ_b` for `γ_{x,b}`). `L` acts on links only, so `L = 1 ⊗ L̂` and `(LbL^*)^ = L̂b̂L̂^*`. `φ` fixes `𝒞_O ⊂ 𝒪_x` and maps `γ_b` to an odd element of `𝒜_x` (Lemma G1). So
\[
\psi(H)\;\mapsto\;\sum_b(\varphi(\gamma_b)P_x)\otimes\hat L\hat B_b\hat L^*+1\otimes\hat L\hat H'\hat L^* .
\]
Apply the projection onto the odd part of the first factor to both sides of `ψ(H) = H`:
\[
\sum_b(\varphi(\gamma_b)P_x)\otimes\hat L\hat B_b\hat L^*=\sum_b(\gamma_bP_x)\otimes\hat B_b .
\]
The `L̂B̂_bL̂^*` are linearly independent, because the `B_b` are and both maps are injective. Take linear functionals `f_c` on the second factor with `f_c(L̂B̂_bL̂^*) = δ_{bc}`. Then `φ(γ_c)P_x = Σ_b f_c(B̂_b) γ_bP_x`, so `φ(γ_c) = Σ_b R_{bc}γ_b` with `R_{bc} = f_c(B̂_b)`. `φ(γ_c)` is Hermitian, so `R` is real. `{φ(γ_c), φ(γ_d)} = 2δ_{cd}` gives `R^TR = 1`.

(ii) Write `E_{−1}(z) = (2π)^{-1}∫_0^{2π} e^{iθ} Ad e^{iθN_𝔐}(z)dθ`, as in B5B line 328. `N_𝔐 ∈ 𝒞_O` is fixed by `φ`, and `Ad L` fixes all matter, so `ψ` commutes with every `Ad e^{iθN_𝔐}` and with `E_{−1}`. `H` commutes with `N_x + N_𝔐`, so by uniqueness in Lemma M0 each `X_j` has `N_𝔐`-charge `−1`, each `X_j^♯` charge `+1`, and `H'` (which commutes with `N_x`) charge `0`. Hence `E_{−1}(H) = Σ_j c_{x,j}^†X_j`, and `ψ(E_{−1}(H)) = E_{−1}(H)`. The argument of (i), with the odd elements `c_{x,j}^†` and the independent `X̂_j`, gives `φ(c_{x,j}^†) ∈ span{c_{x,k}^†}`. So `φ(c_{x,j}^†) = Σ_k u_{kj}c_{x,k}^†`. The CAR force `u` unitary, and `φ = Ad Γ(u)` on the generators, hence on `𝒜_x`. ∎

**Corollary M.1 (gates).** If `a ∉ 𝔈(H)`, a frame compatible with the gate `e^{iaH}` is compatible with `H`. So Theorem M holds for every gate-compatible frame at every angle outside the discrete set `𝔈(H)`.

*Proof.* The map `t ↦ e^{iat}` is injective on the spectrum of `H`. Lagrange interpolation gives a polynomial `f` with `f(e^{iaλ_k}) = λ_k` for every eigenvalue, so `f(e^{iaH}) = H`. `ψ` is a `*`-homomorphism, so `ψ(H) = f(ψ(e^{iaH})) = f(e^{iaH}) = H`. ∎

**Answer to item 1(a).** Yes. A number-conserving hop `Σ_{ab} c_{y,a}^†(U_ℓ)_{ab}c_{x,b} + h.c.`, with any operator-valued `U_ℓ` on any finite registers, and with every mode taking part, keeps at most `U(5)`. Every element of `SO(10)` outside `U(5)` (every Bogoliubov rotation that mixes `c` with `c^†`) is broken. This holds at the generator level, and at the gate level for every angle outside `𝔈(H)`. The bound uses one gate containing `x`; further gates can only shrink the group. Theorem U (section 5) shows `U(5)` is reached.

[check] `check1.py`, `run_u(2)`: the two-mode analogue (two modes per site, complex rishons in the one-rishon sector of the link, one number-conserving hop). The Lie algebra of compatible frames, projected on the site, has rank 5 = `dim u(2) + 1` (the `+1` is the identity), against rank 7 = `dim so(4) + 1` for the Majorana hop below.

**On the exceptional angles.** At `a ∈ 𝔈(H)` the gate generates a smaller algebra than `H`, and the frame group may grow. [check] `check1.py`, `run(4)`: for the four-Majorana analogue of the Majorana hop on one link with the half-spinor register (total dimension 128), the hop has spectrum `{0, ±2, ±4, ±8}`. At `a = 0.7` and `a = 1.3` the compatible frames have site rank 7, as at the generator level. At `a = π/2` the rank is 8: every even site operator is compatible, so the whole identity component of `G_full` is allowed at that angle. At `a = π` the gate is the identity. So the gate-level bound fails at exceptional angles for a single-link gate. The law's gates are cube gates (twelve links, factor `3^{-1/2}`). Whether their exceptional angles in the window enlarge the frame group is open (**LW1-5-X**, section 11).

---

## 4. Quantum links that keep `Spin(10)` exact (item 1(b))

### 4.1 The register algebra, rebuilt

**Lemma Q (the `so(20)` link algebra).** Let `η_1, …, η_{20}` generate `Cl(20)` (`{η_i, η_j} = 2δ_{ij}`, Hermitian). Write `η^y_a = η_a` and `η^x_b = η_{10+b}` for `a, b = 1, …, 10`. Let `𝔨` be the real span of the Hermitian elements `T_{ij} = (i/2)η_iη_j`, `i ≠ j`. Then:
(Q1) `𝔨` is closed under `i^{-1}[·,·]`; it is a real Lie algebra of dimension 190 (the Lie algebra `so(20)`).
(Q2) Put `L_y^{cd} = T_{cd}`, `L_x^{cd} = T_{10+c,10+d}`, and `U^{ab} = 2T_{a,10+b} = iη^y_aη^x_b`. Then
\[
[L_x^{cd},U^{ab}]=i(\delta_{db}U^{ac}-\delta_{cb}U^{ad}),\qquad
[L_y^{cd},U^{ab}]=i(\delta_{da}U^{cb}-\delta_{ca}U^{db}),\qquad
[L_x^{cd},L_y^{ef}]=0 .
\]
(Q3) The `U^{ab}` generate `𝔨` as a Lie algebra: `[U^{ab}, U^{cb}] = −4iL_y^{ac}` for `a ≠ c`, and `[U^{ab}, U^{ad}] = −4iL_x^{bd}` for `b ≠ d`.

A *register* is a finite-dimensional unitary representation `ρ` of `𝔨` (equivalently of the simply connected group `Spin(20)`) on a space `R`, with `ρ(T)` Hermitian. On a register put `L^{cd}_{ℓ,x} = ρ(L_x^{cd})`, `L^{cd}_{ℓ,y} = ρ(L_y^{cd})` and `U^{ab}_ℓ = ρ(U^{ab})`. Every identity in (Q2)-(Q3) holds there, because `ρ` is a Lie algebra map.

*Proof.* (Q1) The bracket of two quadratic monomials is a quadratic monomial or zero; this is (1.1) one level up. (Q2) `η^y_a` commutes with the even element `η^x_cη^x_d`, so `[L_x^{cd}, iη^y_aη^x_b] = iη^y_a[L_x^{cd}, η^x_b]`, and (1.1) for the `η^x` gives the first identity. The second is the same at the other end. `L_x` and `L_y` are even products of disjoint generators, so they commute. (Q3) For `a ≠ c`: `η^y_aη^x_bη^y_cη^x_b = −η^y_aη^y_c` and `η^y_cη^x_bη^y_aη^x_b = η^y_aη^y_c`, so `[iη^y_aη^x_b, iη^y_cη^x_b] = 2η^y_aη^y_c = −4iL_y^{ac}`. The other identity is the same with the ends exchanged. Brackets of the `U`, `L_x`, `L_y` span `𝔨`. ∎

*Examples of registers.* The rishon register: `R = C^{1024}`, the Fock space of `Cl(20)` with `ρ` the identity map. Its chirality `Γ = i^{10}η_1 ⋯ η_{20}` commutes with `𝔨`. Its eigenspaces `S_±` (dimension 512 each) are the half-spinor registers. The vector register: `R = C^{20}` with `ρ(T_{ij}) = −i(E_{ij} − E_{ji})`. In the language of Brower, Chandrasekharan and Wiese (quantum link models of `SO(N)`, credited from memory, not load-bearing), `U^{ab}` is the quantum link variable, `L_x`, `L_y` are its left and right generators, and the embedding algebra is `so(2N) = so(20)`. `LW1`'s spin-`S` link is the one-mode case of the `U(N)` family of the same construction: embedding algebra `u(2) ⊃ u(1) ⊕ u(1)`, with `J` the raising generator.

**Lemma Q4 (the link operators are independent).** On every register with `ρ ≠ 0`, the 100 operators `U^{ab}_ℓ` are linearly independent.

*Proof.* `𝔨 ≅ so(20)` is simple, so `ker ρ` is `0` or `𝔨`, and `ρ ≠ 0` makes it injective. The `U^{ab}` are independent in `𝔨`. For `S_+` directly: `tr_{S_+}(U^{ab}U^{cd}) = 512δ_{ac}δ_{bd}`, since the trace over `C^{1024}` of a product of four distinct Majoranas, or of one with `Γ`, vanishes. ∎

### 4.2 The hop and its Gauss law

For a link `ℓ = (x, y)`, `y = x + e_i`, with register `R_ℓ`, put
\[
h_\ell=\tfrac i2\sum_{a,b=1}^{10}\gamma_{y,a}\,U_\ell^{ab}\,\gamma_{x,b}. \tag{4.1}
\]
`h_ℓ` is Hermitian: `U_ℓ^{ab}` is Hermitian and commutes with matter, and `γ_{x,b}γ_{y,a} = −γ_{y,a}γ_{x,b}`. It is even. It has faithful one-mode inflow at `x` and at `y`: in `H = Σ_b γ_{x,b}B_b + …`, `B_b = −(i/2)Σ_a γ_{y,a}U_ℓ^{ab}`, and `Σ_bλ_bB_b = 0` forces `Σ_bλ_bU_ℓ^{ab} = 0` for every `a` (the `γ_{y,a}` are independent matter elements and the link is an ordinary tensor factor), hence `λ = 0` (Lemma Q4). The same holds for a cube generator `H_C = 3^{-1/2}Σ_{ℓ⊂C}η_i(x)h_ℓ`: the coefficient of `γ_{y,a}` for one link already forces `λ = 0`.

At each site put, for `c < d`,
\[
\mathcal G_x^{cd}=M_x^{cd}+\sum_{\ell\ni x}L^{cd}_{\ell,x},
\]
with `L^{cd}_{ℓ,x}` the generator of the end of `ℓ` at `x` (`L_x` if `x` is the source of `ℓ`, `L_y` if it is the target).

**Theorem G (Gauss law of the Majorana quantum-link hop).** For every register:
(i) every `h_ℓ` commutes with every `𝒢_z^{cd}`; hence so does every cube gate `e^{iaH_C}`, at every angle;
(ii) for every `g` in the group generated by the `e^{iθ𝒢_x^{cd}}`, `Ad g` is a frame at `x` composed with a register change on the six links at `x`, made link by link; it leaves every gate of the update unchanged; its action on `𝒜_x` is the Bogoliubov frame of an element of `SO(10)`, and every element of `SO(10)` occurs;
(iii) the `e^{iθ𝒢_x^{cd}}` give a representation of `Spin(10)` on the space of site `x` and its six link ends.

*Proof.* (i) Take `ℓ = (x, y)` and `z = x`. `M_x^{cd}` is even and supported on `x`, so it commutes with `γ_{y,a}` and with links. `L^{cd}_{ℓ,x} = ρ(L_x^{cd})` commutes with matter and with `ρ(L_y)`. By (1.1) and (Q2),
\[
\Big[\mathcal G_x^{cd},\sum_bU^{ab}\gamma_{x,b}\Big]
=\sum_b i(\delta_{db}U^{ac}-\delta_{cb}U^{ad})\gamma_{x,b}+U^{ab}\,i(\delta_{db}\gamma_{x,c}-\delta_{cb}\gamma_{x,d})=0 .
\]
`𝒢_x^{cd}` also commutes with `γ_{y,a}`, so it commutes with `h_ℓ`. The generators of the other five links at `x` act on other links. For `z = y` the same computation runs on the first index of `U`. For other `z` the supports are disjoint. Linear combinations and exponentials keep commutation.
(ii) `e^{iθ𝒢_x^{cd}} = e^{iθM_x^{cd}} ∏_{ℓ∋x} e^{iθL_{ℓ,x}^{cd}}`, a product of commuting factors. The first factor is an even element of `𝒜_x`, so its conjugation is a frame at `x` (Theorem C(i)). The others are unitaries on single links. By (1.1), `Ad e^{iθM^{cd}}` rotates the `γ_{x,a}` by a rotation in the `(c, d)` plane. These rotations generate `SO(10)`. By (i), the product leaves every gate unchanged. The electric gates of section 8 are built from the commutant of the end generators, so they are unchanged too.
(iii) The `𝒢_x^{cd}` satisfy the `so(10)` relations (each summand does, and the summands commute), so they exponentiate to a representation of the simply connected `Spin(10)`. ∎

### 4.3 Reflections

Let `σ` be the automorphism of `𝔨` induced by reflecting the last coordinate of the `x`-end: `σ(T_{ij}) = s_is_jT_{ij}` with `s_{20} = −1` and `s_i = 1` otherwise. Write `R^σ` for the register `ρ∘σ`.

**Theorem R (which reflections are exact).** Let every link carry the register `R`, and let `x` be a site.
(i) If `R ≅ R^σ` (a unitary `Q` on `R` with `Qρ(X)Q^* = ρ(σ(X))` for all `X`), then every Bogoliubov frame at `x` with `det = −1` is exact: it leaves every gate unchanged at every angle, with a register change made link by link. Examples: `R = C^{20}` and `R = S_+ ⊕ S_−`.
(ii) If `R = S_+`, no Bogoliubov frame with `det = −1` is compatible with any cube generator containing `x`, for any register change.
(iii) If `R` is irreducible and `R ≇ R^σ`, the same conclusion as in (ii) holds.

*Proof.* Every `det = −1` frame is `φ_r` composed with an `SO(10)` frame, with `r = diag(1, …, 1, −1)`. `SO(10)` frames are exact (Theorem G(ii)). So it suffices to treat `φ_r`.
(i) Use `φ_r` at `x` and `Q` on each link where `x` is the source. For a link where `x` is the target, the needed automorphism is the reflection `σ'` of the `y`-end; `σ' = sσs^{-1}` with `s` the end swap of B1-5, which lifts to `Spin(20)`, so `R^{σ'} ≅ R^σ ≅ R` and an intertwiner exists there too. In (4.1), `φ_r` changes the sign of `γ_{x,10}` and `Ad Q` changes the sign of `U^{a,10}` only. So `h_ℓ` is unchanged. For `C^{20}`, `Q = diag(1, …, 1, −1)`. For `S_+ ⊕ S_−`, `Q = η_1 ⋯ η_{19}`, an odd product of the other nineteen generators: it commutes with `η_i` for `i ≤ 19` and anticommutes with `η_{20}`.
(ii) Suppose `(φ_r∘Ad L)(H_O) = H_O` for a cube `O ∋ x`. The proof of Theorem M(i) gives `Σ_c r_{bc} LB_cL^* = B_b`, so `LB_cL^* = Σ_b r_{bc}B_b`. With `B_c = −(i/2)Σ_{ℓ∋x, ℓ⊂O} η_ℓ Σ_aγ_{y_ℓ,a}U_ℓ^{ac}` (for links where `x` is the source; the other case has the first index) and `L` fixing matter, comparison of the independent coefficients `γ_{y_ℓ,a}` gives, for each such link,
\[
LU_\ell^{ac}L^*=\sum_br_{bc}U_\ell^{ab}=\rho_\ell(\sigma(U^{ac})) . \tag{4.2}
\]
`Ad L` preserves brackets, and by (Q3) the `U^{ab}` generate `𝔨`. So `Ad L(ρ_ℓ(X)) = ρ_ℓ(σ(X))` for every `X ∈ 𝔨`. Put `Π = ∏_{k=1}^{10} 2ρ_ℓ(T_{2k−1,2k})`. `σ` fixes `T_{2k−1,2k}` for `k ≤ 9` and negates `T_{19,20}`. So `Ad L(Π) = −Π`. On `S_+`, `2T_{2k−1,2k} = iη_{2k−1}η_{2k}`, so `Π = Γ = 1`. Then `1 = Ad L(1) = −1`, a contradiction.
(iii) As in (ii), `Ad L` maps the algebra generated by `ρ_ℓ(𝔨)`, which is `End(R_ℓ)` by Burnside's theorem, onto itself. By Lemma G3 it is `Ad Q_ℓ` there, and `Q_ℓ` intertwines `ρ` and `ρ∘σ`. ∎

**Corollary R.1 (exact frame group of the Majorana law).** For the law `L5-O[R]` of section 8, at the generator level and for gates at every angle outside `𝔈(H_C)`, the frames at a site that are compatible with the cube gates are:
- the Bogoliubov frames of `SO(10)`, if `R = S_+` or `R` is irreducible with `R ≇ R^σ`; on the site Hilbert space they are implemented by `Spin(10)`, acting as `16 ⊕ 16bar`;
- the Bogoliubov frames of `O(10)`, if `R ≅ R^σ`.
All of these are exact at every angle (Theorem G, Theorem R(i)).

*Proof.* Theorem M(i) with the faithful inflow of section 4.2, Corollary M.1, Theorem R and Theorem G. ∎

[check] `check1.py`, `run(4)` and `run(6)`: four- and six-Majorana analogues (two sites, one link, half-spinor register `S_+` of `Cl(8)` and `Cl(12)`; total dimensions 128 and 2048). `max |[𝒢_x^{cd}, h]| = 0` to machine precision. `exp(2πiM^{12}) = −1` on the site and `exp(2πiL^{12}) = −1` on `S_+`. Reflection intertwiners: none on `S_+`; two independent ones on `S_+ ⊕ S_−` (for four Majoranas). For four Majoranas, the compatible frames of the generator have site rank 7 = `dim so(4) + 1`.

**Answer to item 1(b).** Yes. Finite registers carry the needed raising and lowering structure: the mixed generators `U^{ab}` of any finite-dimensional representation of `so(20)`, as in quantum link models of `SO(N)`. The hop (4.1) keeps `Spin(10)` exact. The Gauss law is `𝒢_x^{cd} = M_x^{cd} + Σ_{ℓ∋x}L^{cd}_{ℓ,x}`, 45 generators per site, and it commutes with every gate of the update. With `R = S_+`, the reflections are broken and the exact group is `SO(10)` on the algebra, `Spin(10)` on states.

### 4.4 Three structural facts of the `Spin(10)` law

**Proposition Σ (no Gauss singlet with one register class).** Suppose every link register is a representation on which `−1 ∈ Spin(20)` acts as one scalar `ε = ±1` (this holds for every irreducible register: `ε = −1` for `S_±`, `ε = +1` for `C^{20}`). Then at every site, `−1 ∈ Spin(10)` acts on the space of the site and its six link ends as the scalar `−1`. So no vector there is invariant under the local `Spin(10)`: the Gauss singlet sector is empty at every site.

*Proof.* `−1 ∈ Spin(10)` is `exp(2πi𝒢^{12}_x) = exp(2πiM_x^{12})∏_{ℓ∋x}exp(2πiL^{12}_{ℓ,x})`. `M_x^{12} = n_{x,1} − 1/2` has eigenvalues `±1/2`, so the first factor is `−1`. Each end factor is `ρ` of `exp(2πiT_{ij})`, which is `−1 ∈ Spin(20)` (the same element: a full turn in one coordinate plane), so it is `ε`. The product is `−ε^6 = −1`. ∎

So pure locally gauge-invariant states do not exist for these registers. LW1 reads gauge invariance of a state as "invariance under these conjugations, not support in the sector \(\mathcal G_x=0\)" (`LW1.md` line 47), and under that reading gauge-invariant states exist (the tracial state, for example); they are mixed at every site. If VC1 needs a pure Gauss-singlet vacuum, the register classes must differ between links. A covariant way exists: put `S_+` on even-tiling links and `C^{20}` on odd-tiling links. Each site has three links of each tiling (Lemma A1), so the product above becomes `−(−1)^3(+1)^3 = +1`, and singlets can occur. This two-register option is recorded, not proposed (section 8.3, choice c10).

**Lemma Z (centre: the vector class, never the 16).** Under the hypothesis of Proposition Σ:
(i) for every site `x`, conjugation by the local `−1 ∈ Spin(10)_x` is the identity on the whole quasi-local algebra;
(ii) the element `−1_{10} ∈ SO(10)` applied at every site of a finite region `Λ` (with its link changes) acts as the fermion parity automorphism on every operator supported, with all its links, inside `Λ`;
(iii) hence every gauge-covariant local operator transforms under the gauge group by a true `SO(10)` representation, and if it is fermion odd, `−1_{10}` acts on it as `−1`: it is in the vector class (`10`, `120`, `126`, …). No local operator transforms as a spinor `16`.

*Proof.* (i) Proposition Σ: the implementer is a scalar. (ii) On matter, `−1_{10}` sends every `γ_{z,a}` to `−γ_{z,a}`, which is `Ad ∏_z P_z`. On each link inside `Λ` both ends are rotated by `−1_{10}`, which is `−1_{20} ∈ SO(20)`. Its lifts to `Spin(20)` are central (in `Cl(20)` they are `±` the volume element, which commutes with every even element), so on an irreducible register they act as scalars (`±Γ = ±1` on `S_+`; `−1` on `C^{20}`). Their conjugation is the identity on `End(R)`. (iii) Follows from (i) and (ii). ∎

This is #10027's centre theorem (its section B) carried to the gauged law with finite registers. Mixed-class registers (both classes in one register) admit operators that change a link's class; such operators can carry the spinor class. The law's gates preserve the class of each link (`ρ(−1)` commutes with `ρ(𝔨)`), so these operators connect different superselection sectors. Whether that is a usable escape is open (**LW1-5-16**).

**Lemma H (gauge invariance fixes the filling).** Let `ω` be a state invariant under conjugation by every `e^{iθ𝒢_x^{cd}}` at a site `x`. Then `ω(X) = 0` for every `X ∈ span{M_x^{cd}}`. In particular `ω(n_{x,j}) = 1/2` for every mode, in every frame, and `ω(N_x) = 5/2`.

*Proof.* The link-end parts of `𝒢_x` commute with `𝒜_x`, so conjugation by `g ∈ Spin(10)_x` acts on `span{M_x^{cd}}` by the adjoint representation of `so(10)`. Average over the Haar measure of the compact group `Spin(10)`: `ω(X) = ω(∫Ad g(X)dg)`, and `∫Ad g(X)dg` is fixed by every `Ad g`. Differentiating, it commutes with every `M^{ef}`, so it lies in the centre of `so(10)`. That centre is zero: identify `so(10)` with real antisymmetric `10 × 10` matrices; a matrix commuting with every `E_{ef} − E_{fe}` commutes with the algebra they generate, which is all of `M_{10}(R)` for `n ≥ 3`, so it is a scalar, and an antisymmetric scalar is zero. Finally `n_{x,j} − 1/2 = M_x^{2j−1,2j}`. ∎

---

## 5. The number-conserving law reaches `U(5)`

**Theorem U.** On each link `ℓ = (x, y)` put ten complex rishon modes `r^{ℓ,y}_j`, `r^{ℓ,x}_k` (`j, k = 1, …, 5`), fermionic among themselves, in an ordinary tensor factor that commutes with matter, restricted to a sector of fixed total rishon number `m`, `1 ≤ m ≤ 9`. Put `U_ℓ^{jk} = r^{ℓ,y}_j r^{ℓ,x†}_k` and
\[
h^{U}_\ell=\sum_{j,k}c_{y,j}^\dagger U_\ell^{jk}c_{x,k}+\text{h.c.}
\]
For Hermitian `T ∈ u(5)` put `𝒢^T_x = Σ_{jk}c_{x,j}^†T_{jk}c_{x,k} + Σ_{ℓ∋x}Σ_{jk}r^{ℓ,x†}_jT_{jk}r^{ℓ,x}_k`. Then every `h^U_ℓ` commutes with every `𝒢^T_z`, and the compatible frames of any cube generator built from the `h^U_ℓ` are exactly `Ad Γ(u)`, `u ∈ U(5)` (generator level; gates at angles outside `𝔈`).

*Proof.* `[Σc^†Tc, c_k] = −Σ_jT_{kj}c_j` and `[Σr^†Tr, r^†_k] = Σ_jT_{jk}r^†_j`, so `Σ_k r^{x†}_kc_{x,k}` commutes with `𝒢^T_x`. The same holds for `Σ_j c^†_{y,j}r^y_j` at `y`. So `h^U_ℓ` commutes with the Gauss generators of both ends; other sites are disjoint. Each `e^{i𝒢^T_x}` is `Γ(e^{iT})` at `x` times rishon unitaries on the six links, so all of `U(5)` is exact. The hop is number conserving. Its inflow at `x` from `ℓ` is `c_{x,k}^† X_k` with `X_k = r^{ℓ,x}_k Σ_j r^{ℓ,y†}_j c_{y,j}` (from the adjoint term). In the sector `1 ≤ m ≤ 9` the operators `r^x_kr^{y†}_j` are nonzero and independent, so the `X_k` are independent. Theorem M(ii) gives the upper bound. ∎

With `m = 1` the register is 10-dimensional. The `U(1)` part of the Gauss law is `N_x + Σ_{ℓ∋x} n^{ℓ}_{x\text{-end}}`; with one rishon per link this is the five-flavour form of LW1's spin-1/2 link. At one mode, `L5-U` is `L_cube` with `S = 1/2`.

---

## 6. The plain PS-6 group is reachable

**Proposition A.** There is a law of the PS-1c form, with finite registers, whose exact frame group at every site is all of `G_full`.

*Proof.* Identify all site algebras with one copy of `M_32(C)`. Fix a Hilbert–Schmidt orthonormal basis `O_1, …, O_{512}` of its odd part. Each frame `Ad V` acts on the odd part unitarily: `Ad V(O_i) = Σ_k π(V)_{ki}O_k`. On a link `ℓ = (x, y)` take the register `R_ℓ = C^{512}_{x} ⊕ C^{512}_{y}` with orthonormal bases `|i, x⟩`, `|j, y⟩`. Put `Θ_{ℓ,x} = Σ_i O_{x,i} ⊗ |i, x⟩` and
\[
h^{\rm full}_\ell=\sum_{i,j}O_{x,i}O_{y,j}^*\otimes|i,x\rangle\langle j,y|+\text{h.c.}
\]
It is even and Hermitian. A frame `Ad V` at `x`, with the unitary `π(V)^-` (complex conjugate matrix) on the `x`-slot of each of the six links at `x`, fixes `Θ_{ℓ,x}`: `Σ_{i,k,l}π_{ki}\bar π_{li}O_k ⊗ |l⟩ = Σ_kO_k ⊗ |k⟩` since `ππ^* = 1`. So it fixes every `h^{full}_ℓ`. Build cube gates and the two tilings as in section 8; the structure is the same on every link, and a reversal of orientation swaps the two slots and the two terms. So every frame in `G_full` is exact. ∎

Under this law the hop moves an arbitrary odd site operator, not one mode. Lemma C2(iii) shows that `G_full` fixes no site observable but the scalars, and its identity component fixes only `span{1, P_x}`. So this law meets section 8.2's reading PS-3g only if its odd frames are broken.

---

## 7. Item 1 collected

| Law (hop, register) | Exact frame group at a site | Proof | Frame-invariant site values (Lemma C2) |
|---|---|---|---|
| any law | `⊂ G_full` (dim 511) | Theorem C | — |
| one-mode hop, faithful | `⊂ O(10)` | Theorem M(i), Cor. M.1 | — |
| number-conserving one-mode hop, faithful | `⊂ U(5)` | Theorem M(ii), Cor. M.1 | — |
| `L5-O[R]`, `R ≅ R^σ` (e.g. `C^{20}`, `C^{1024}`) | `O(10)` (implementers `Pin(10)`) | Theorems G, R(i), Cor. R.1 | scalars only |
| `L5-O[S_+]` | `SO(10)` on the algebra, `Spin(10)` on states | Theorems G, R(ii), Cor. R.1 | parity `P_x` |
| `L5-U` (rishons, sector `m`) | `U(5)` | Theorem U | contains `N_x` |
| `L_full` | `G_full` | Proposition A | scalars only |

All "`⊂`" rows and the upper bounds in the other rows hold at the generator level and, for gates, at every angle outside `𝔈(H_C)`. All lower bounds hold at every angle. The exceptional angles are LW1-5-X. The whole-update reading (B5B's R-T) is LW1-5-T.

**Run-to-closure record for item 1.** (a), (b) and (c) are each closed by a proof above. Two refinements are open, each with three attacks recorded in section 11: LW1-5-X and LW1-5-T. The [check] in section 3 is a counterexample to the all-angle form of Theorem M for single-link gates.

---

## 8. The law

### 8.1 Statement of `L5-O`

Notation of `LW1.md` section 1 (sites `Z^3`, tilings `𝒯_e`, `𝒯_o`, signs `η_i(x)`, angles `a_e = ε − μ/2`, `a_o = ε + μ/2`, the group `𝒢 = 2Z^3 ⋊ O_{c_0}`), with these changes.

1. **Sites.** Each site carries five fermion modes, `γ_{x,1..10}` as in section 1.1 (PS-5).
2. **Links.** Each positively oriented link `ℓ = (x, x + e_i)` carries a register `R_ℓ = R`, a finite-dimensional unitary representation of `𝔨 = so(20)` (Lemma Q). Free datum. Proposed value: `R = S_+` (dimension 512). Link algebras are ordinary tensor factors and commute with matter.
3. **Hop.** `h_ℓ` as in (4.1).
4. **Cube generator.** `H_C = 3^{-1/2}Σ_{ℓ=(x,x+e_i)⊂C}η_i(x)h_ℓ`, the same form as `LW1.md` line 59 with `c_y^†J_ℓc_x + h.c.` replaced by `h_ℓ`.
5. **Layers.** `M_e = ∏_{C∈𝒯_e}e^{−ia_eH_C}`, `M_o = ∏_{C∈𝒯_o}e^{ia_oH_C}`. Gates in one layer have disjoint sites and disjoint links (Lemma A1), so they commute.
6. **Electric class (optional).** `W_E = ∏_ℓ e^{−iτ_E Γ^x_ℓ}`, with `Γ^x_ℓ = i^5η^x_1 ⋯ η^x_{10}` the chirality of the `x`-end. On `S_+`, `Γ^x_ℓ = Γ^y_ℓ`, and `Γ^x_ℓ` commutes with both ends' generators. With `1` it spans their commutant on `S_+ = (16,16) ⊕ (16bar,16bar)`, by the standard fact that `16` and `16bar` are irreducible and inequivalent (not used elsewhere). Free constant `τ_E ∈ R`, zero allowed.
7. **Plaquette class.** OPEN as law data, as in `LW1.md` line 162 (GA1-P).
8. **Tick.** `U = W_EM_oM_e`. Half-steps `W_{2n} = M_e`, `W_{2n+1} = W_EM_o`, as `LW1.md` line 64.
9. **Gauss law.** `𝒢_x^{cd}` of section 4.2; it commutes with the tick (Theorem G).
10. **Free tick.** Replace every `U_ℓ^{ab}` by `δ^{ab}`. Then `h_ℓ^{free} = (i/2)Σ_aγ_{y,a}γ_{x,a} = iΣ_j(c_{y,j}^†c_{x,j} − c_{x,j}^†c_{y,j})`. Its one-body tick is `(W V W^*) ⊗ 1_5`, with `V` LW1's free tick and `W = diag(i^{x_1+x_2+x_3})` (section 9, A2-5).
11. **Initial state and actuality.** `ω_0` supplied; no records initially; odds never depend on records; actuality and records as in `LW1.md` line 166, with the actual configuration read by PS-3h5 (section 8.2): a configuration of site parities.

**Free data.** `ε, μ` with `0 ≤ μ < 2ε < π`; the register `R`; `τ_E` (zero allowed); the plaquette class (open); `ω_0`. Readers: LZ1 uses `ε`; MT1/VC1 use `μ`; GA1/GA2 use `R`, `τ_E` and any plaquette data; TM1 uses `ω_0`.

**The variant `L5-U`.** Items 1, 4, 5, 8, 10, 11 unchanged; items 2-3 replaced by the rishon register of Theorem U (free datum `m`, `1 ≤ m ≤ 9`) and the hop `h^U_ℓ`; item 6 by `W_E = ∏_ℓ e^{−iτ_E(n^ℓ_{x\text{-end}} − m/2)^2}`; item 9 by the `u(5)` Gauss law. Its actual configuration is the site numbers `N_x` (PS-3h5). Its free tick is the same as `L5-O`'s. At one mode per site, `L5-U` with `m = 1` is `L_cube` with `S = 1/2` (identify `E_ℓ = n^ℓ_{x\text{-end}} − 1/2`). `L5-O` at one mode has the same gauge group, `SO(2) = U(1)`, but its hop also contains pairing terms `c_y c_x` times link operators, so it is not `L_cube`.

### 8.2 Proposed readings needed by the law (adopt nothing)

**PS-3g (frame-invariant actuality; proposed reading of PS-3 with PS-6).** "The actual value of a site is a joint value of the site observables that every exact frame at that site leaves unchanged." Reason: PS-6 makes the local frame a choice of description, and PS-3's actual configuration names what is actual; read plainly, what is actual does not depend on a choice of description. For one-mode sites of `L_cube` this changes nothing: the exact frames are phases, and `n_x` is invariant.

**PS-3h5 (restatement of PS-3h on five-mode sites).** "The actual configuration is a configuration of the frame-invariant site values: under `L5-O[S_+]` the site parities `P_x = ±1`; under `L5-U` the site numbers `N_x ∈ {0, …, 5}`." It follows from PS-3g and Lemma C2. The rest of PS-3h is unchanged ("It exists at every half-tick and moves once per half-tick, using only the nonzero matrix elements of that half-tick between" these configurations).

### 8.3 Four-test check of every choice

Tests: (1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need.

| Choice | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| c1. Five modes per site | — | — | — | — | PS-5, in the working set (D1); not re-checked |
| c2. One-mode hops (each hop term has one site Majorana at each end) | pass: names no group; the bound `O(10)` is derived (Theorem M) | pass: closed (degree one at each end) | conditional: the degree bounds GA1-i's group; higher-degree hops reach larger groups up to `G_full` (Proposition A). Reason given: the smallest odd site operators, and the degree of `L_cube`'s hop | pass | passes 1, 2, 4; 3 conditional, disclosed |
| c3a. General bilinear hop (`L5-O`) | conditional: it is the law the target names. Choosing it *because* it gives `Spin(10)` fails. Reason given: it is the one-mode hop with no further constraint | pass | conditional, as c2 | pass: no constraint beyond c2 | conditional on the stated reason |
| c3b. Number-conserving hop (`L5-U`) | pass | pass | conditional, as c2 | conditional: it adds global number conservation, a complex structure `J` at every site and link end. PS-5's word "modes" supplies `J` if "fermion modes" is read as complex modes | conditional on that reading of PS-5 |
| c4. Register `R` (free datum; `S_+` proposed) | pass | pass: a free datum with a named range, like LW1's `S` | conditional: `R`'s class decides `O(10)` versus `SO(10)` (Theorem R) and the singlet question (Proposition Σ). `S_+` is proposed only because PS-3g needs `R ≇ R^σ` | pass | passes 1, 2, 4; 3 conditional, disclosed |
| c5. Tilings, `η_i(x)`, `3^{-1/2}`, angle window | pass | pass | pass | pass: carried from `L_cube`. In the gauged law the signs can be absorbed into the registers (each `−1` on `U_ℓ` is the lift of `−1_{10}` at one end, a register unitary); they matter only for the free tick, which they make five copies of LW1's | pass |
| c6. Electric class, `τ_E`, zero allowed | pass | pass | pass | pass: optional class with a named constant, as PS-6r's correction asks | pass |
| c7. Plaquette class | not chosen (GA1-P) | | | | open |
| c8. PS-3g | pass | pass | conditional: with PS-6r's "no actual configuration" on links, it excludes registers with `R ≅ R^σ` (no frame-invariant site value), so it decides the component group in GA1-i's answer | pass | passes 1, 2, 4; 3 conditional |
| c9. PS-3h5 | pass | pass | as c8 | pass: it removes structure | as c8 |
| c10. Two register classes (`S_+` even links, `C^{20}` odd links) | pass | pass | pass | fails unless a part needs a pure Gauss-singlet vacuum; no working-set reason does | recorded, not proposed |
| c11. `L_full` (Proposition A) | pass | pass | pass | conditional: its hop moves every odd site operator; needed only if the frame group is read as `G_full` | recorded as the plain-PS-6 alternative |

**The owner decision these leave.** Which reading of "the frame group of the site content" (PS-6r) the law should keep exact: `G_full` (PS-6's "possibilities", law `L_full`), `O(10)`/`SO(10)` (PS-5's "`Cl(10)`", law `L5-O`), or `U(5)` (PS-5's "fermion modes" as complex modes, law `L5-U`). The four tests do not decide it. On register size and hop terms, `L5-U` (register 10, 25 hop terms) is smaller than `L5-O[S_+]` (512, 100) and `L_full` (1024, 512^2). On constraints added to the one-mode hop, `L5-O` adds none and `L5-U` adds `J`. This draft does not choose.

---

## 9. Carry-over of LW1

"Unchanged" means the LW1 statement and proof hold as written, with five modes per site. "Restated" means a new statement is given and proved here. Statements are for `L5-O[S_+]` unless marked; for `L5-U` the number-conserving proofs of LW1 apply as written, with `N_x` in place of `n_x` where noted.

| LW1 result | Status | Note |
|---|---|---|
| A1 ownership, flux, involutions | unchanged | geometry |
| A1a free factorization | unchanged | the free tick is `Γ((WVW^*) ⊗ 1_5)`; Givens per flavour; `W` diagonal |
| Dressed factorization (LW1-edge) | unchanged | `LW1.md` line 188's Lie-group argument uses only finite dimension; each edge-triple factor commutes with the Gauss law by Theorem G |
| GAP UALL | unchanged | same parity-trace obstruction |
| A2 free covariance | restated, A2-5 | proof below |
| A3, B12 | unchanged | geometry |
| B2 scalar walks | restated, B2-5 | proof below |
| B3 one-site frames | replaced | Theorem C |
| B4 Gauss conservation | replaced | Theorem G (`L5-O`), Theorem U (`L5-U`) |
| B5(a), B5(b), B5b, B5b-T | replaced for sites | Theorem M, Corollary R.1. Cell frames of five-mode sites are not needed. The whole-update form is LW1-5-T |
| Gauged covariance B1/B1q | restated, B1-5 | proof below |
| B6, B7, support factorization | unchanged | with parity projectors; B6 allows projectors of rank above one (`LW1.md` line 249) |
| B8 copy criterion | restated, B8-5 | proof below |
| B8a | restated, B8a-5 | proof below |
| B8b(i) | fails as stated; restated, B8b-5 | the dressed Majorana hop creates pairs from empty matter, so "Its dressed hops annihilate that matter subspace, independently of its links" (`LW1.md` line 291) is false. `L5-U`: unchanged |
| B8b(ii) | unchanged | with the parity vector `2^{-1/2}(|odd_x odd_y odd_z⟩|even_{abc}⟩ + |even⟩|odd⟩)`, one particle in mode 1 at each odd site |
| B9 established clauses | unchanged | with values `P_y = ±1` and projectors `(1 ± P_y)/2` |
| B10, C1, E2a | unchanged | five flavours, covariance `WPW^*`, `|(WPW^*)_{xy}| = |P_{xy}|` |
| B11 | restated, B11-5 | proof below; the countable-list part is unchanged |
| E1 | unchanged | gates commute with every `e^{it𝒢_x^{cd}}` by Theorem G |
| E2b | restated, E2b-5 | its half-filling step (cube-number conservation) fails for Majorana hops; the conclusion holds by Lemma H. `L5-U`: unchanged |
| E3-E6 | unchanged | finite alphabets `{±1}` per site; the pair alphabet per cell is `{±1}^{16}` |
| LW1-U_f, LW1-U_sea, LW1-N | open | restated on parity configurations; the free sea is five copies, but its parity marginals are not determinantal, so LW1U_DRAFT's Theorem 10.2 does not transfer as written |
| GA1-P | open | for `so(20)` quantum links |
| VC1 | open | add Proposition Σ: with one register class there is no pure Gauss-singlet state |
| PS-1c, PS-7r, PS-11c, PS-Ar | unchanged | PS-Ar's neighbourhood of influence has the same geometry |

**A2-5 (free covariance).** The free tick of `L5-O` and `L5-U` is `(WVW^*) ⊗ 1_5` with `W = diag(i^{x_1+x_2+x_3})`. Its symmetries are those of A2, with lifts multiplied by diagonal phases.

*Proof.* Per flavour, `h^{free}_ℓ` has one-body matrix `⟨y|h|x⟩ = i`, `⟨x|h|y⟩ = −i` for `y = x + e_i`. `(WR_TW^*)_{yx} = i^{Σy}η_i(x)i^{−Σx} = iη_i(x)`, and the reverse entry is `−iη_i(x)`. So the free cube generators are `WR_TW^* ⊗ 1_5` for both tilings. A lift `D_gP_g` preserving `V` gives `W D_gP_g W^* = (W D_g (P_gW^*P_g^*)) P_g`, a diagonal unitary times `P_g`, preserving `WVW^*`. A2's exclusion of odd translations uses moduli of entries, which `W` does not change. ∎

**B2-5 (scalar walks on five-mode sites).** A finite-range unitary on `ℓ^2(Z^d) ⊗ C^5` that commutes with all translations and with `1 ⊗ u` for every `u ∈ U(5)` is `w ⊗ 1_5` with `w` a phase times a translation. The same holds for a real orthogonal operator on `ℓ^2(Z^d; R^{10})` commuting with `SO(10)`.

*Proof.* The commutant of `U(5)` on `C^5` is `C1` (an operator commuting with all unitaries commutes with all matrices). So the walk is `w ⊗ 1_5`, and `w` is a scalar walk; apply B2. For `SO(10)` on `R^{10}`: the commutant over `R` is `R1` (an operator commuting with all rotations commutes with the matrices `E_{ab} − E_{ba}`, which generate `M_{10}(R)`), and B2's proof runs with real coefficients. ∎

So the reason for PS-1c, the scalar-walk obstruction, carries over: a law whose free tick has the global frame symmetry cannot use unit translations.

**B1-5 (gauged covariance of `L5-O[R]`).** Under PS-1c the tick `U` is cell covariant and acts transitively on sites.

*Proof.* A symmetry `g ∈ 𝒢` permutes sites and links. If it reverses a link, use on that register the lift of the swap `s: η_a ↔ η_{10+a}`. `s` is a product of ten transpositions, so `det s = +1`, and it lifts to `Spin(20)`; it acts on every register. `s(U^{ab}) = iη^x_aη^y_b = −U^{ba}`. Then (4.1) for `ℓ` maps to `−(i/2)Σγ_{gy,a}U'^{ba}γ_{gx,b} = (i/2)ΣU'^{ba}γ_{gx,b}γ_{gy,a}`, which is (4.1) for `gℓ` with its own orientation. A2's sign correction `d(x)` is implemented on matter by `Ad P_x` (`P_xγ_{x,a}P_x = −γ_{x,a}`). The angle of each tiling is preserved. `s` exchanges `Γ^x_ℓ` and `Γ^y_ℓ`, which are equal on `S_+`. A2 supplies transitivity. ∎

**B8-5 and B8a-5 (no parity copy in the free sea).** Let `ω` be a number-invariant quasi-free state of the five-flavour matter with covariance `G ⊗ 1_5` in some flavour basis. Then
\[
\omega(P_xP_y)=\big[(1-2G_{xx})(1-2G_{yy})-4|G_{xy}|^2\big]^5 .
\]
If `G_{xx} = G_{yy} = 1/2`, then `ω(P_xP_y) = −4^5|G_{xy}|^{10} ≤ 0`, so the parity-disagreement projector `D^P_{xy} = (1 − P_xP_y)/2` has `ω(D^P_{xy}) ≥ 1/2`. Under the free tick and PS-3c read with PS-3h5, from the free sea, no record forms. For `L5-U` (actual values `N_x`): `ω((N_x − N_y)^2) = 5[G_{xx}(1−G_{yy}) + G_{yy}(1−G_{xx}) + 2|G_{xy}|^2] ≥ 5/2` at half filling, so again no record forms.

*Proof.* Block-diagonal covariance makes the quasi-free state a product over flavours: Wick's determinant rule factorizes every moment. `P_x = ∏_j(1 − 2n_{x,j})`, so `ω(P_xP_y) = ∏_jω((1−2n_{x,j})(1−2n_{y,j}))`. For one flavour, `LW1.md` line 279: "Wick's determinant rule gives \(\omega_G(n_xn_y)=G_{xx}G_{yy}-|G_{xy}|^2\)", so `ω((1−2n_x)(1−2n_y)) = (1−2G_{xx})(1−2G_{yy}) − 4|G_{xy}|^2`. The free sea of A2-5 has covariance `(WPW^*) ⊗ 1_5`, and B10(2) gives `P_{xx} = 1/2`. The free sea is stationary (B10(3)), so every full tick fails the copy test. For `L5-U`, sum B8's formula over the five independent flavours. ∎

**B8b-5 (record witnesses for `L5-O`).** Fix a complex structure, rishon annihilators `d^y_k = (η^y_{2k−1} + iη^y_{2k})/2` and `d^x_j` likewise, and the 25 operators `𝒰^{++}_{kj} = ρ(4i d^y_kd^x_j) = U^{2k−1,2j−1} + iU^{2k−1,2j} + iU^{2k,2j−1} − U^{2k,2j}` on each register. Let `K_ℓ` be their joint kernel. (i) `K_ℓ ≠ 0` for every register. (ii) `h_ℓ` annihilates every vector with matter empty at both ends of `ℓ` and register in `K_ℓ`. (iii) If an even product initial state has empty matter on the side-seven cube centred at `x`, and every link register there lies in `K_ℓ`, then tick one has perfect parity copies at `x` and its six neighbours.

*Proof.* (i) The elements `d^y_kd^x_j` of `𝔨_C` pairwise commute (even products of anticommuting annihilators). Put `Q = Σ_{k=1}^5(T_{2k−1,2k} + T_{10+2k−1,10+2k}) ∈ 𝔨`; in `Cl(20)`, `T_{2k−1,2k} = d^†_kd_k − 1/2` by the identity of section 1.1, so `Q` is the rishon number minus 5. Then `[Q, d^y_kd^x_j] = −2d^y_kd^x_j`. These are Lie algebra identities, so they hold in every register: each `𝒰^{++}_{kj}` lowers the eigenvalue of `ρ(Q)` by 2. A `ρ(Q)`-eigenvector with the lowest eigenvalue is killed by all of them. (ii) `γ_{x,2j−1}|∅⟩ = c_{x,j}^†|∅⟩` and `γ_{x,2j}|∅⟩ = ic_{x,j}^†|∅⟩`. So
\[
h_\ell|\varnothing\rangle|r\rangle=-\tfrac i2\sum_{j,k}c_{x,j}^\dagger c_{y,k}^\dagger|\varnothing\rangle\otimes\mathcal U^{++}_{kj}|r\rangle ,
\]
which is zero for `r ∈ K_ℓ`. (iii) For a cube `C` with empty matter and all registers in `K_ℓ`, `H_C` kills the state, so `e^{iaH_C}` fixes it. Follow `LW1.md` line 291's backward cone: the even-layer ancestor cubes of the seven outputs lie in the side-seven cube, so they fix the state there; the odd cubes' links are untouched by the even layer (Lemma A1) and their matter is still empty, so they fix it too. The electric layer commutes with parities. So the seven output parities are `+1` with probability one. ∎

**B11-5 (atomless parity measure).** For the free sea and every finite set `F` of sites and every parity pattern `s`, `ν(P_z = s_z, z ∈ F) ≤ 2^{−|F|/2}`. So the parity measure is atomless, and so is the history measure.

*Proof.* The flavours are independent (B8-5's proof). Condition on flavours 2-5; the event becomes `{n^{(1)}_F = t}` for a pattern `t` fixed by them. So the probability is at most `sup_t ν^{(1)}(n_F = t)`. With `A = {z : t_z = 1}`, `ν^{(1)}(n_F = t) ≤ min(ν(n_A ≡ 1), ν(n_{F∖A} ≡ 0)) = min(det P'_A, det(I − P')_{F∖A})`, and Hadamard's inequality with `P'_{zz} = 1/2` bounds this by `min(2^{−|A|}, 2^{−|F∖A|}) ≤ 2^{−|F|/2}`, as in `LW1.md` line 352. The tracial state's parities are independent fair bits. The rest of B11's proof is unchanged. ∎

**E2b-5 (stationary gauge-invariant states of `L5-O`).** If `ω` is cell-translation invariant and locally gauge invariant, every weak-* limit point of its Cesàro means is stationary, cell-translation invariant and locally gauge invariant; such states exist (the tracial state); and every locally gauge-invariant state is half filled in every mode at every site.

*Proof.* `LW1.md` line 417's compactness and averaging argument, with Theorem G for gauge invariance. Half filling is Lemma H; it needs no conservation law. ∎

---

## 10. What the result means downstream

**GA1-i.** GA1(a)(2) asks for "the group that the chosen content gives". On five-mode sites the content alone gives `G_full` (Theorem C); the law decides. `L5-O[S_+]`: `Spin(10)` (`SO(10)` on the algebra), with exact Gauss laws from finite registers (Theorem G). It contains `SU(5)`, and so the group `SU(3) × SU(2) × U(1)/Z_6` by the standard embedding. `L5-U`: `U(5)`, which contains it too. `TOE_ASSEMBLY.md` line 136 should read: with five modes and the Majorana quantum-link law it is `Spin(10)`; with the number-conserving law it is `U(5)`; PS-6 alone gives `G_full`. GA1(a)(1) is met by both laws. GA1(a)(3)-(4) wait on GA1-P. Literature context, from memory and not load-bearing: in Brower–Chandrasekharan–Wiese the continuum Yang–Mills limit of quantum link models comes from dimensional reduction of an extra dimension; whether finite registers on `Z^3` reach GA1(a)(4) is GA1's question.

**CH1, Lemma S1 (charge parity).** S1 is a statement about one-mode sites. On `L5-O` its role passes to Lemma Z: `−1_{10}` acts on every gauge-covariant local operator as its fermion parity. On `L5-U`, S1 holds for the `U(1)` factor of `U(5)` unchanged in form: every local operator of `N`-charge `k` has fermion parity `(−1)^k`.

**CH1, Theorem S2.** S2 assumes that the candidate charge "acts as the gauge `U(1)` of Lemma S1". On `L5-O` there is no abelian factor, and hypercharge is a generator of `so(10)`, so S2's obstruction does not arise. On `L5-U`, S2 applies to `U(1)_N` and says it is not hypercharge; hypercharge lies in `su(5)`, where S2 says nothing.

**CH1, Theorem S3.** (i) becomes: `G = Spin(10)` (`L5-O[S_+]`) or `U(5)` (`L5-U`), non-abelian. (ii) becomes: the non-abelian charges and the hypercharge of CG1 are carried by `G`. But on `L5-O` with one register class, no fermion excitation created by a gauge-covariant local operator is a spinor of `Spin(10)` (Lemma Z), so CH1(a) read with "one Weyl 16" fails there as stated. Pieces of the Standard Model multiplet occur inside vector-class representations (for example the `120` contains a `10` of `SU(5)`), so the "Standard Model multiplet" reading is not excluded by Lemma Z; it needs breaking (EW1/VC1). On `L5-U`, fermion-odd site operators lie in `Λ^{odd}`: the `SU(5)` types `5` (`c^†`, `N = 1`), `10bar` (`c^†c^†c^†`, `N = 3`) and `1` (`N = 5`), with their adjoints. These are the `SU(5)` types of one family, with `U(1)_N` charges proportional to `(1, 3, 5)`. Whether a light chiral family arises is CH1's open input CH1-i. (iii): CH1(a) is no longer blocked by the size of `G`; on `L5-O` it is blocked by the centre for the 16.

**CH1, Theorems F1-F4.** Unchanged: they are one-body statements for any number of components per cell, and the free tick of both laws is number conserving.

**MT1.** (1): PS-5 supplies the CAR modes, so MT1-i ("no added site content") is moot under PS-5. (2): open as before; the free tick is five copies of LW1's, so #10016's per-flavour cell structure carries over. (3), MT1-ii: on `L5-O` with one register class the 16 is the Fock content of a site, not an excitation (Lemma Z; #10027 section A3: "The even level ... is one degenerate 16"). On `L5-U` it is open.

**CG1.** CG1(e)'s escape list ("a site-count change, deconfined spinons outside the finite-site theorem, or a Spin(10) not generated by site bilinears") gains one precise case on `L5-O`: mixed-class registers (LW1-5-16). On `L5-U` the `SU(5)` types of a family occur as site operators; their charges and chirality are CH1/CG1 questions.

**T0's SU(2).** Every closed subgroup of an exact gauge group is an exact gauge subgroup. `SU(2) ⊂ Spin(4) ⊂ Spin(10)` and `SU(2) ⊂ SU(5) ⊂ U(5)` are exact gauge subgroups of `L5-O[S_+]` and `L5-U`. The lattice gauge theory is `Spin(10)` (or `U(5)`), not `SU(2)`. A pure `SU(2)` Yang–Mills sector of T0's kind arises only after breaking (EW1/VC1), or GA2 needs T0's extension to `Spin(10)` or `SU(5)` (the Sussman-Alpoge extension the target names). Restricting the registers to `SU(2)` would be a choice made because it yields T0's group: test 1.

**PS-7.** On `L5-O`, every locally gauge-invariant state is half filled in every mode (Lemma H). So PS-7's "half-filled" is a consequence of gauge invariance there, not a choice; PS-7r's content reduces to which free sea. On `L5-U`, `N_x` is gauge invariant and the filling stays a choice.

**#10014.** Its condition (a), "the frame group is the full Spin(2N)", is met exactly by `L5-O[S_+]` (Corollary R.1). Its "no nearest-neighbour inter-cluster coupling keeps Spin(2N>2) exact" is about c-number couplings of clusters of one-mode sites; with five modes per site and operator-valued couplings, the local `Spin(10)` is exact. No contradiction. Its condition (b), the Weyl-species reading of `S+`, meets Lemma Z on `L5-O`: the species would have to be spinor-class excitations, and there are none.

---

## 11. Open statements and attacks

**LW1-5-X (OPEN, first).** For `L5-O[R]` (and `L5-U`), at angles `a ∈ 𝔈(H_C)` in the window, is every frame compatible with the cube gate `e^{iaH_C}` still Bogoliubov (resp. in `U(5)`)? The gate-wise bound fails only where both `a_e` and `a_o` are exceptional, a countable set of `(ε, μ)`. The [check] in section 3 shows that the analogous statement is false for a single-link gate at `a = π/2`.
- *Attack 1 (B5B's Lemma T route).* One-particle blocks show that each mode at `x` receives inflow at every angle, by an irrationality argument as in B5B line 130. But the frame must preserve the whole `x`-slice space of the gate, and at finite angle that space contains degree-3 Majorana products, which Lemma T does not control.
- *Attack 2 (charge projection, B5B line 153).* For `L5-U`, the `N_𝔐`-charge `−1` part of the gate has `x`-slices of `N_x`-charge `+1`, which include `c^†c^†c` terms. Preserving that space forces at best that `φ` commutes with `N_x` (when the slice space is all charge-`+1` operators), a group of dimension 251, not `φ ∈ U(5)`. For `L5-O` only the parity of `𝔐` is available.
- *Attack 3 (commutant of the gate).* A compatible frame need only preserve the algebra generated by the gate. At exceptional angles it is smaller than the algebra generated by `H_C`, and the single-link [check] shows that it can admit every even site operator. A proof must use the spectrum of the twelve-link cube generator, which is not computed here.

**LW1-5-T (OPEN).** The whole-update reading (B5B's R-T): classify frames `φ` at `x` with `(φ∘Ad L)∘α = α∘(φ∘Ad L)`.
- *Attack 1 (B5B section 7's cut).* (H1) and (7.1) carry over: the even and electric layers respect the cut between an even cell and its outside. Step 1 then shows that `φ_1` preserves the `x`-slice space of `G_x^*γ_{y,a}G_x`, which again contains degree-3 elements.
- *Attack 2 (charges).* B5B's Step 2 removes a flip by a charge `−1` projection; for five modes the same projection keeps all charge-`+1` many-body slices.
- *Attack 3 (functional calculus).* Corollary M.1 needs one fixed gate. (7.1) relates two different automorphisms, so no fixed gate is available.

**LW1-5-Σ (OPEN, owner/VC1).** Whether VC1 needs a pure Gauss-singlet vacuum. If yes, `L5-O` needs two register classes (choice c10), which fails test 4 today.

**LW1-5-16 (OPEN).** Whether mixed-class registers give a usable spinor-class excitation on `L5-O`.

**LW1-5-RQ (owner decision).** The reading of "the frame group of the site content" (section 8.3).

**GA1-P-5 (OPEN).** A plaquette class for `so(20)` (resp. `u(10)`) quantum links, as `LW1.md` line 476.

**LW1-U_f and LW1-U_sea on parity configurations (OPEN).** As LW1, with the parity alphabet.

---

## FINISH

**Proved here (pass 1, not refereed).**
- Theorem C: the local frames of a five-mode site form `G_full ≅ ((U(16)×U(16))/U(1)) ⋊ Z_2` (dimension 511); Bogoliubov `O(10)` and `U(5)` are subgroups; at one mode they coincide with B3's `U(1) ⋊ Z_2`. Lemma C1 (Bogoliubov automorphisms; `det R` decides the parity of the implementer). Lemma C2 (frame-invariant site observables: `span{1, P_x}` for `SO(10)`, scalars for `O(10)` and `G_full`).
- Theorem M: a generator with faithful one-mode inflow allows only Bogoliubov frames (`O(10)`); if number conserving, only `U(5)`. Corollary M.1: the same for gates at every angle outside the discrete set `𝔈(H)`.
- Lemma Q and Lemma Q4: the `so(20)` quantum-link register algebra, rebuilt; the link variables are independent on every register.
- Theorem G: the Majorana quantum-link hop commutes with the `so(10)` Gauss law at every angle; `SO(10)` frames are exact with link-by-link register changes; `Spin(10)` acts on states.
- Theorem R: a reflection is exact exactly when the register is isomorphic to its reflected twist (both directions for irreducible registers; the half-spinor `S_+` breaks reflections by the chirality argument). Corollary R.1: the exact frame group of `L5-O[S_+]` is `SO(10)`.
- Proposition Σ: with one register class on all links, no site has a Gauss singlet.
- Lemma Z: on `L5-O` with one register class, every gauge-covariant local operator is in a true `SO(10)` representation; fermion-odd ones are vector class; none is a spinor.
- Lemma H: every locally gauge-invariant state of `L5-O` is half filled in every mode.
- Theorem U: the number-conserving rishon law keeps exactly `U(5)`.
- Proposition A: `G_full` is exact for a law whose hop moves every odd site operator.
- Restatements A2-5, B2-5, B1-5, B8-5, B8a-5, B8b-5, B11-5, E2b-5.

**Counterexamples.**
- To "PS-6 gives `Spin(10)` on five-mode sites" (`TOE_ASSEMBLY.md` line 136): PS-6 with Lemma G1 gives `G_full`; `L5-U` keeps only `U(5)`; `L5-O[C^{20}]` keeps `O(10)`.
- To the all-angle form of Theorem M for single-link gates: the four-Majorana single-link gate at `a = π/2` admits every even site operator ([check], section 3).
- To "dressed hops annihilate empty matter independently of the links" (B8b's proof step) on `L5-O`: `h_ℓ|∅⟩|r⟩ ≠ 0` unless `r ∈ K_ℓ` (B8b-5(ii)).
- To E2b's half-filling proof step on `L5-O`: the Majorana hop does not conserve cube number (the conclusion still holds, by Lemma H).

**Open, by name.** LW1-5-X (first; three attacks recorded); LW1-5-T (three attacks recorded); LW1-5-Σ; LW1-5-16; LW1-5-RQ (owner); GA1-P-5; LW1-U_f and LW1-U_sea on parity configurations; LW1-N as before.

**Proposed specifications, with check results.**
- PS-3g (frame-invariant actuality): passes tests 1, 2, 4; test 3 conditional (it decides the component group in GA1-i's answer by excluding `R ≅ R^σ`).
- PS-3h5 (actual configuration = site parities under `L5-O[S_+]`, site numbers under `L5-U`): as PS-3g.
- The law `L5-O[R]` with `R = S_+` proposed: choices c2-c6 in section 8.3; c2, c3a and c4 pass with test 3 (and for c3a test 1) conditional on stated reasons; c5 and c6 pass; c7 open.
- The variant `L5-U`: as `L5-O`, with test 4 conditional on reading PS-5's "fermion modes" as complex modes.
- Recorded, not proposed: two register classes (c10, fails test 4 today); `L_full` (c11).
- Owner decision named: LW1-5-RQ, which frame group the law keeps exact.

**What changes downstream.**
- GA1-i: `Spin(10)` (`L5-O[S_+]`) or `U(5)` (`L5-U`), each with exact Gauss laws from finite registers; both contain the Standard Model group. `TOE_ASSEMBLY.md` line 136 needs the law named.
- CH1: S1's role passes to Lemma Z (`L5-O`) or to `U(1)_N` (`L5-U`); S2's obstruction does not arise for hypercharge in a non-abelian `G`; S3(iii) is no longer blocked by `G`, but on `L5-O` the 16 is blocked by the centre.
- MT1-ii and CG1: on `L5-O` the 16 is site content, not an excitation; on `L5-U` the `SU(5)` types of a family are site operators.
- T0: `SU(2)` is an exact gauge subgroup of both laws; the plug-in needs breaking or T0's extension to `Spin(10)`/`SU(5)`.
- PS-7: automatic for gauge-invariant states on `L5-O`.
- VC1: Proposition Σ (no pure Gauss-singlet state with one register class).
- PS-3h: needs PS-3h5 on five-mode sites.

**Inputs from outside the working set.** The CAR reading of five site modes with parity superselection (as `LW1.md` line 18 for one mode). Links as ordinary tensor factors commuting with matter (`LW1.md` line 42). LW1's Lemma A1, Theorems A2, B2, B6-B11, E1-E6 and its definitions; B5B's Lemmas G1-G3 and its `E_{−1}` projection. Standard mathematics, rebuilt in the text: Clifford monomial bases and the determinant of the top product, Jordan–Wigner, elementary-tensor uniqueness, Lagrange interpolation, Burnside's theorem (used only in Theorem R(iii)), the zero centre of `so(10)`, lowest-weight vectors for a grading element. Standard mathematics cited, not rebuilt: existence of Haar measure on compact groups (Lemma H), simplicity of `so(20)` (Lemma Q4; the `S_+` case is proved directly), integration of `so(n)` representations to `Spin(n)`, irreducibility of `Λ^k C^5` (a remark only). Literature context, credited from memory and never load-bearing: Hamiltonian lattice gauge theory (Kogut–Susskind); quantum link models (Horn; Orland–Rohrlich; Chandrasekharan–Wiese) and their `SO(N)`, `U(N)` and `Sp(N)` forms with embedding algebras `so(2N)`, `u(2N)` (Brower–Chandrasekharan–Wiese), including rishon realizations; the `SO(10)` and `SU(5)` embeddings of the Standard Model group (Georgi–Glashow; Georgi; Fritzsch–Minkowski).
