# L5-U, pass 1: structure of the number-conserving five-mode law

Written 2026-11-05 by a Claude Opus 5.5 subagent, as a pass-1 lane of the open item LW1-5-RQ of the TOE assembly (method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen). A parallel lane writes `LW1_5O_DRAFT.md`; this file does not use it.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (scripts outside the repo, in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/lw15u/`, `check_u.py` and `check_x.py`, outputs `out.txt` and `out_x.txt`; under 100 MB and a few seconds each). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (same commit as `origin/claude/toe-assembly`) | `e648fa3e0f` |
| `origin/claude/toe-why-five-modes-20261021` (#10014, closed) | `3d00c61f05` |

Files read at those commits, by line: `LW1_5_DRAFT.md` lines 1-511 (all); `TOE_ASSEMBLY.md` lines 125-145 (PS-5, PS-6, PS-7), 199-209 (section 3.4, D1), 342-417 (MT1, GA1, GA2, CH1, CG1), 464-476 (VC1), 530 (T0); `LW1.md` lines 40-50 (link algebra and the reading of gauge invariance), 114, 168, 176 (Lemma A1), 231-233 (B4), 411-424 (E2b), 502 (VC1); the #10014 note `docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md` (all 201 lines, by `git show`).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The working set is read plainly. Where a statement depends on a reading, the reading is named. Every recorded option carries the four-test check (section 8). Nothing is adopted.

**Working set used, by name.** PS-5 (fallback text, D1); PS-6 and PS-6r (frames and registers); PS-7 and PS-7r (section 4 only); LW1's reading of local gauge invariance (`LW1.md` lines 47, 114). From `LW1_5_DRAFT.md`: Theorem C, Theorem M, Corollary M.1, Theorem U, section 8.1's variant `L5-U`, and the four-test table of section 8.3. PS-1c, PS-2, PS-3, PS-4 are not used.

---

## 0. The open item, quoted

`LW1_5_DRAFT.md` line 345: "**The owner decision these leave.** Which reading of "the frame group of the site content" (PS-6r) the law should keep exact: `G_full` (PS-6's "possibilities", law `L_full`), `O(10)`/`SO(10)` (PS-5's "`Cl(10)`", law `L5-O`), or `U(5)` (PS-5's "fermion modes" as complex modes, law `L5-U`)."

The two facts that count against `L5-O` today. Line 231 (Proposition Σ): "Then at every site, `−1 ∈ Spin(10)` acts on the space of the site and its six link ends as the scalar `−1`. So no vector there is invariant under the local `Spin(10)`". Line 240 (Lemma Z(iii)): "if it is fermion odd, `−1_{10}` acts on it as `−1`: it is in the vector class (`10`, `120`, `126`, …). No local operator transforms as a spinor `16`."

The law studied here. Line 254 (Theorem U): "On each link `ℓ = (x, y)` put ten complex rishon modes `r^{ℓ,y}_j`, `r^{ℓ,x}_k` (`j, k = 1, …, 5`), fermionic among themselves, in an ordinary tensor factor that commutes with matter, restricted to a sector of fixed total rishon number `m`, `1 ≤ m ≤ 9`." Line 258: "For Hermitian `T ∈ u(5)` put `𝒢^T_x = Σ_{jk}c_{x,j}^†T_{jk}c_{x,k} + Σ_{ℓ∋x}Σ_{jk}r^{ℓ,x†}_jT_{jk}r^{ℓ,x}_k`. Then every `h^U_ℓ` commutes with every `𝒢^T_z`, and the compatible frames of any cube generator built from the `h^U_ℓ` are exactly `Ad Γ(u)`, `u ∈ U(5)` (generator level; gates at angles outside `𝔈`)." Line 318 defines the full law `L5-U` from `L5-O` by replacing the register, the hop, the electric class and the Gauss law.

D1's reason. `TOE_ASSEMBLY.md` line 207: "Test 4: passes conditionally. The constant 5 comes from #10014 under its conditions (a)-(c)." #10014 line 163: "(a) the frame group is the full Spin(2N);".

## 0.1 Outcome in one paragraph

**Gauss singlets (item 1).** Under the representation that Theorem U writes, a vector at a site is invariant only if that site's matter and all six of its link ends are empty. So no state is a singlet at every site, for any `m` (Proposition Σ-U(i)). Under LW1's own reading (a state is gauge invariant when conjugation leaves it unchanged), a pure state is gauge invariant at `x` exactly when it is `SU(5)_x`-invariant and has a sharp `U(1)` Gauss charge `Q_x`. Such states exist at every site, for **every** `m` from 1 to 9, and can be chosen translation invariant (Proposition Σ-U(ii)-(iii)). So the obstruction of Proposition Σ does not arise. **Local operators (item 2).** A fermion-odd gauge-covariant local operator has odd total `U(1)` charge, so none is `U(5)`-invariant. At one site, `c`, `c c c` and `c^5` carry the `SU(5)` types `5bar`, `10` and `1`, with `U(1)_N` charges `−1`, `−3`, `−5` (Lemma Z-U). This is the `SU(5)` content of one family, as representation types of local operators. It says nothing about the light spectrum, chirality or hypercharge. **Filling (item 3).** Local `U(5)` invariance fixes the site marginal to `Σ_k p_k Π_k / C(5,k)` with free weights `p_k`. So all five modes are filled equally and carry no coherence between them, but the filling itself is free (Lemma H-U). If a state is pure, gauge invariant, and invariant under a symmetry group that acts transitively on sites, then its filling is the integer `5k − 3m` on every periodic box. That is never `5/2` (Theorem F-U). So PS-7's "half-filled" vacuum cannot be pure, gauge invariant and site-transitive under `L5-U` with one value of `m`. The same proof gives the same conclusion for `L_cube` (Remark F.1). **LW1-5-X (item 4).** The frame bound `U(5)` holds at every parameter point `(ε, μ)` of the window, except possibly at finitely many (Proposition X2). At those points it is open. Three attacks are recorded. A [check] on a single link with two modes per site shows that an exceptional angle can admit a frame outside `U(2)`, and that this frame keeps `N_x`. **D1's reason (item 5).** #10014's criteria, rerun with `SU(5)` or `U(5)` in place of `Spin(10)`, do not select `N = 5`. Under `SU(N)`, the singlet `Λ^0` in `S+` always has an invariant Majorana mass, so protection fails at every `N`. Under `U(5)` with integer charge shifts, the `U(1)`-gravitational anomaly of `S+` is `40 − 16c ≠ 0` (Proposition D). Only the half-integer shift `c = 5/2`, which is the action of `Spin(10)`'s spinor, restores the selection. **SU(2) (item 6).** Every `SU(2) ⊂ U(5)` is an exact gauge subgroup with its own Gauss law of three generators per site, at every angle (Proposition T). The lattice theory is not `SU(2)` Yang-Mills: from `SU(2)`'s point of view the `U(5)` link register carries extra charged link fields, and GA2's simple factor is `SU(5)`. **For LW1-5-RQ:** `L5-U` removes both facts that count against `L5-O`. It brings two new costs: D1's reason for five modes does not carry over, and a pure, site-transitive, gauge-invariant vacuum cannot be half filled.

---

## 1. Setting

### 1.1 The law

The law is `L5-U` of `LW1_5_DRAFT.md` section 8.1 (line 318). Sites `x ∈ Z^3` carry five modes `c_{x,j}`. `N_x = Σ_j c^†_{x,j}c_{x,j}`. Each link `ℓ` carries rishons `r^{ℓ,x}_j`, `r^{ℓ,y}_j` in the sector of total rishon number `m`. Write `p_{ℓ,x} = Σ_j r^{ℓ,x†}_jr^{ℓ,x}_j` for the number at the `x`-end. Then `p_{ℓ,x} + p_{ℓ,y} = m` on the register. The register is `Λ^m(C^{10}) = ⊕_p Λ^p(C^5_x) ⊗ Λ^{m−p}(C^5_y)`, with `max(0, m−5) ≤ p ≤ min(5, m)`. Every link operator is in `End(Λ^m(C^{10}))`, so it keeps the link's total rishon number.

For `u ∈ U(5)` write `Γ(u)` for its action on the site Fock space `Λ(C^5)`, with `Γ(u)c^†_jΓ(u)^* = Σ_k u_{kj}c^†_k`. Put
\[
Q_x:=\mathcal G^{\mathbf 1}_x=N_x+\sum_{\ell\ni x}p_{\ell,x}.
\]
`e^{i𝒢^T_x}` acts as `Γ(e^{iT})` on the matter at `x` and as the same `Γ(e^{iT})` on each of the six `x`-ends. Matter creators and `x`-end rishon creators both transform as `5`. Write `U(5)_x` for this local group and `SU(5)_x` for its subgroup with `det = 1`. The centre element `e^{iθ}·1` acts as `e^{iθQ_x}`. The `SU(5)` centre element `ζ = e^{2πi/5}·1` acts as `ζ^{Q_x}`.

**Periodic box.** `Λ_L = (Z/LZ)^3`, `L` even, so both tilings fit. It has `V = L^3` sites and `3V` links. Every link has both ends in the box. Summing `Q_x` over sites counts each link's two ends once:
\[
\sum_{x\in\Lambda_L}Q_x=N_{\rm tot}+3mV\qquad\text{on the box Hilbert space.} \tag{1.1}
\]
Each site lies in one cube of each tiling, so it has three links of each tiling (`LW1_5_DRAFT.md` line 235, from Lemma A1).

### 1.2 Gauge invariance of a state

`LW1.md` line 47: "Gauge invariance of a state means invariance under these conjugations, not support in the sector \(\mathcal G_x=0\)." This file uses that reading. It also states the stricter sector reading where it matters, and names it.

**Lemma P (pure gauge-invariant states).** Let `ψ` be a unit vector of the box Hilbert space and `ω_ψ` its vector state. Then `ω_ψ` is invariant under conjugation by `U(5)_x` exactly when `ψ` is `SU(5)_x`-invariant and an eigenvector of `Q_x`. Its eigenvalue then lies in `5Z`.

*Proof.* The box algebra is a full matrix algebra (finitely many modes, finite registers), so `ω_{gψ} = ω_ψ` gives `gψ = χ(g)ψ` with `|χ(g)| = 1`. So `χ` is a continuous character of `U(5)_x`. Differentiating, `𝒢^T_xψ = dχ(T)ψ` with `dχ` a real Lie algebra map `u(5) → R`. It vanishes on commutators, and every traceless Hermitian `T` is a real combination of the `i[S, S']`, so `dχ` vanishes on `su(5)`. Hence `ψ` is `SU(5)_x`-invariant. For `T = 1`, `ψ` is a `Q_x`-eigenvector. Then `ζ^{Q_x}ψ = ψ` gives `Q_x ∈ 5Z` on `ψ`. The converse is direct: `e^{i𝒢^T}` multiplies `ψ` by a phase. ∎

The spanning fact: for `j ≠ k`, `E_{jk} = [E_{jj}, E_{jk}]` and `E_{jj} − E_{kk} = [E_{jk}, E_{kj}]`. So the complex span of commutators is all of `sl(5)`. Taking Hermitian parts gives the real statement.

### 1.3 Exterior powers

**Lemma E.** Let `V = C^5`.
(E1) Each `Λ^k(V)` is irreducible under `SU(5)` (and under `U(5)`).
(E2) For `a + b ≤ 5`, there is an injective `U(5)`-equivariant map `Λ^{a+b}(V) → Λ^a(V) ⊗ Λ^b(V)`.
(E3) For `a + b ≥ 5`, there is an injective `SU(5)`-equivariant map `Λ^{a+b−5}(V) → Λ^a(V) ⊗ Λ^b(V)`.

*Proof.* (E1) Let `X` commute with `Γ(u)` on `Λ^k` for all `u ∈ SU(5)`. Differentiating, `X` commutes with every `c^†_ic_j` (`i ≠ j`) and every `n_i − n_j`; on `Λ^k`, `N = k`, so `X` commutes with every `n_i`. The joint eigenvalues of `(n_1, …, n_5)` separate the basis vectors `e_S`, `|S| = k`. So `X e_S = x_S e_S`. For `j ∈ S`, `i ∉ S`, `c^†_ic_je_S = ±e_{S∖{j}∪{i}}`. Commuting gives `x_{S∖{j}∪{i}} = x_S`. Any two `k`-subsets are joined by such moves, so `X` is a scalar. A unitary representation with scalar commutant is irreducible: the projection onto an invariant subspace commutes.
(E2) Let `Δ` be the algebra map `Λ(V) → Λ(V) ⊗̂ Λ(V)`, `v ↦ v ⊗ 1 + 1 ⊗ v`. It commutes with `Γ(u) ⊗ Γ(u)`. Its `(a, b)` component sends `e_S` to `Σ_{A ⊂ S, |A| = a} ±e_A ⊗ e_{S∖A} ≠ 0`. A nonzero equivariant map from an irreducible representation is injective (its kernel is invariant).
(E3) Put `c = a + b − 5`, `vol = e_{12345}`. `Λ^5(V)` is trivial under `SU(5)`. Map `w ∈ Λ^c` to `(id ⊗ ∧)(Δ_{a,5−a}(vol) ⊗ w) ∈ Λ^a ⊗ Λ^b`. It is `SU(5)`-equivariant. On `w = e_T` it gives `Σ_{|A|=a} ±e_A ⊗ (e_{A^c} ∧ e_T)`. A term is nonzero exactly when `T ⊂ A`. Such `A` exist because `|T| = a + b − 5 ≤ a`. Distinct `A` give independent basis tensors. So the map is nonzero, hence injective by (E1). ∎

---

## 2. Gauss singlets (item 1)

**Lemma S (singlets in products of exterior powers).** Let `a_0, …, a_6 ∈ {0, …, 5}`. The space `Λ^{a_0}(V) ⊗ ⋯ ⊗ Λ^{a_6}(V)`, with `U(5)` acting diagonally, contains a nonzero `SU(5)`-invariant vector exactly when `Σ_i a_i ≡ 0 mod 5`.

*Proof.* Only if: `ζ` acts as `ζ^{Σa_i}`. If: merge factors from the left. Suppose `Λ^s ↪ Λ^{a_0} ⊗ ⋯ ⊗ Λ^{a_{i−1}}` equivariantly and injectively, with `s ≡ a_0 + ⋯ + a_{i−1} mod 5` and `0 ≤ s ≤ 5`. If `s + a_i ≤ 5`, (E2) gives `Λ^{s+a_i} ↪ Λ^s ⊗ Λ^{a_i}`. Otherwise (E3) gives `Λ^{s+a_i−5} ↪ Λ^s ⊗ Λ^{a_i}`. Tensoring the induction map with the identity keeps it injective, and composites of injective maps are injective. At the end, `Λ^r ↪ ⊗_iΛ^{a_i}` with `r ≡ Σa_i mod 5`. If `Σa_i ≡ 0`, then `r ∈ {0, 5}`, and `Λ^0`, `Λ^5` are trivial under `SU(5)`. The image of a nonzero vector is a nonzero invariant. ∎

[check] `check_u.py` part (1), by Weyl integration on a grid: the invariant spaces for counts `(4;1,1,1,1,1,1)`, `(2;1,1,1,0,0,0)`, `(1;1,1,1,2,2,2)`, `(3;3,3,3,3)`, `(3;2,2,2,2,2,2)`, `(5;5,5,5)` have dimensions 5, 1, 13, 6, 60, 1. The counts `(2;1,1,1,1,1,1)` and `(0;1,1,1,1,1,1)` give 0. The count `(3,3,3,3,3)` cannot be split into groups that each sum to 5, so a pairing argument alone would miss it. The merging proof covers it.

**Proposition Σ-U (Gauss singlets of `L5-U`).**
(i) *Sector reading.* A vector `ψ` satisfies `𝒢^T_xψ = 0` for all `T` exactly when `N_x = 0` and `p_{ℓ,x} = 0` on `ψ` for all six links at `x`. Such vectors exist at one site exactly when `m ≤ 5`. No vector of a periodic box satisfies this at every site, for any `m ∈ {1, …, 9}`.
(ii) *LW1's reading, pure states, one site.* For every `m ∈ {1, …, 9}` there are pure states invariant under conjugation by `U(5)_x`.
(iii) *Every site.* For every `m ∈ {1, …, 9}`, every even `L`, and each `n_m` in the table below, there is a pure state of the box that is invariant under conjugation by every `U(5)_x`, is translation invariant, and has `N_x = n_m` sharp at every site:

| `m` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| `n_m` | 2 | 4 | 1 | 3 | 0 or 5 | 2 | 4 | 1 | 3 |
| `Q_x = n_m + 3m` | 5 | 10 | 10 | 15 | 15 or 20 | 20 | 25 | 25 | 30 |

*Proof.* (i) `T = 1` gives `Q_xψ = 0`. All terms of `Q_x` are nonnegative, so `N_x = 0` and every `p_{ℓ,x} = 0` on `ψ`. Conversely, on such a vector every `𝒢^T_x` is zero, because each term contains an annihilator of an empty mode on the right. At one site, `p_{ℓ,x} = 0` needs `m − 0 ≤ 5` at the other end. On a box, (1.1) applied to `ψ` gives `0 = ⟨N_{tot}⟩ + 3mV > 0`.
(ii) Fix any admissible end numbers `p_1, …, p_6`. Choose `N ∈ {0, …, 4}` with `N + Σp_i ≡ 0 mod 5`. Lemma S gives a nonzero `SU(5)`-invariant `v` in `Λ^N ⊗ ⊗_iΛ^{p_i}`. It is a `Q_x`-eigenvector, with eigenvalue `N + Σp_i`. Lemma P finishes.
(iii) Take the configuration `N_x = n_m` and, on each link `(x, x+e_i)`, source end `α`, target end `m − α`, with one fixed admissible `α`. Every site then has end numbers `(α, α, α, m−α, m−α, m−α)` and `Q_x = n_m + 3m`, a multiple of 5 by the table. For this configuration, the box Hilbert space is the tensor product over sites of `Λ^{n_m}(C^5_x) ⊗ (its six end spaces)`. On each link the summand is `Λ^α ⊗ Λ^{m−α} ⊂ Λ^m(C^{10})`. Choose one `SU(5)`-invariant `v` by Lemma S and put the same `v` at every site. The product vector is invariant under every `SU(5)_x`. The generators at different sites are even and act on disjoint modes, so they commute. It is a `Q_x`-eigenvector at every site. Lemma P gives invariance. Translation maps the configuration and `v` to themselves. ∎

**What this does not show.** (a) Invariance of a pure all-site singlet under the point group `O_{c_0}`. For odd `m` the configuration above depends on link orientation. For even `m` with `α = m/2` the configuration is symmetric, but the action of the site stabilizer on the invariant space is not computed. Open as **LW1-5U-Σc**. (b) Stationarity.

*Remark Σ.1 (the centre).* On `L5-O`, the centre `−1 ∈ Spin(10)` acts on a site and its ends as a fixed scalar `−1` (Proposition Σ). On `L5-U`, `ζ` acts as `ζ^{Q_x}`, and `Q_x` takes every residue mod 5 as `N_x` varies. So the centre gives no obstruction. That is the structural reason Proposition Σ does not carry over.

*Remark Σ.2 (LW1's normalisation).* At one mode with `m = 1`, `LW1_5_DRAFT.md` line 318 identifies `E_ℓ = n^ℓ_{x-end} − 1/2`. With that, LW1's `𝒢_x = n_x + Σ_{out}E − Σ_{in}E` (`LW1.md` line 45) equals `Q_x − 3`. The five-mode analogue `𝒢^T_x − (3m/5)tr T` is a representation of `U(5)` only when `5 | 3m`, that is `m = 5`. In every normalisation, the zero sector at every site fixes `N_{tot}` by (1.1). This is why LW1 reads gauge invariance by conjugation and not by a sector.

**Answer to item 1.** In the sector reading, no `m` gives a state that is a singlet at every site. In LW1's reading, every `m` gives pure gauge-invariant states at every site, and they can be chosen translation invariant. With one value of `m` on all links, which is a covariant law datum, the Gauss-singlet obstruction of `L5-O` is absent. Point-group invariance of such a state is open (LW1-5U-Σc).

---

## 3. Local operator classes (item 2)

A *local operator* is an element of the algebra of finitely many sites and links. It is *gauge covariant of charges `(q_x)`* if `e^{iθQ_x}Oe^{−iθQ_x} = e^{iθq_x}O` for all `x`. Every local operator is a finite sum of such homogeneous ones, because the `Q_x` commute and act on a finite-dimensional space. Fermion parity means matter parity `Ad ∏_xP_x`. Link operators are rishon-number conserving, hence rishon even, so they are bosonic.

**Lemma Z-U.**
(i) A homogeneous local operator `O` has fermion parity `(−1)^{Σ_xq_x(O)}`. Also `Σ_xq_x(O)` is the change of total matter number that `O` makes.
(ii) The gauge transformation `−1_5 ∈ U(5)` at every site of a finite set `Λ` containing the sites and link ends of `O` acts on `O` as its fermion parity. So no fermion-odd local operator is invariant under every `U(5)_x`.
(iii) At one site, with no links, the odd elements of `𝒜_x` carry the `U(5)` representation `⊕_{a−b\ odd} Λ^a(V) ⊗ Λ^b(V)^*`, with `U(1)` charge `a − b`.
(iv) The annihilator monomials of odd degree at `x` span three irreducible `U(5)` multiplets. Under `SU(5)` and `U(1)_N` they are `c_{x,j}`: `5bar`, charge `−1`; `c c c`: `10`, charge `−3`; `c_{x,1}⋯c_{x,5}`: `1`, charge `−5`. Their adjoints are `5_{+1}`, `10bar_{+3}`, `1_{+5}`.
(v) Under `SU(5)` alone, `ζ` at every site of `Λ` acts on `O` as `ζ^{ΔN}`. The operator `c_{x,1}⋯c_{x,5}` is fermion odd and invariant under every `SU(5)_z`.

*Proof.* (i) Choose `Λ` to contain every site in `O`'s matter support and both ends of every link in its support. Sum `Q_x` over `Λ`: `Σ_{x∈Λ}Q_x = N_Λ + R`, where `R` collects the end numbers. For a link in `O`'s support, both ends appear in `R`, and their sum is `m`, which commutes with `O`. For a link outside the support, `O` commutes with its end numbers. So `[Σ_{x∈Λ}Q_x, O] = [N_Λ, O]`, and the left side is `(Σq_x)O`. So `O` changes the matter number by `Δ = Σq_x`. A matter polynomial with definite number change `Δ` has `#c^† − #c = Δ` in every monomial, so its degree is `≡ Δ mod 2`. (ii) `Ad ∏_{x∈Λ}e^{iπQ_x}` multiplies `O` by `(−1)^{Σq_x}`, which is its parity by (i). An invariant operator has all `q_x = 0`, so it is even. (iii) `𝒜_x = End(Λ(V)) = ⊕_{a,b}Hom(Λ^b, Λ^a)`, and `Hom(Λ^b, Λ^a) ≅ Λ^a ⊗ (Λ^b)^*` as `U(5)` representations. Odd elements are the blocks with `a − b` odd. `e^{iθ}·1` acts on the block by `e^{iθ(a−b)}`. (iv) `Γ(u)c_jΓ(u)^* = Σ_k\bar u_{kj}c_k`, so the `c_j` span `V^* = 5bar`. Products of `k` annihilators span `Λ^k(V^*)`, irreducible by (E1) applied to `V^*`. `Λ^3(V^*) = (Λ^3V)^*`. The wedge pairing `Λ^2V ⊗ Λ^3V → Λ^5V` is nondegenerate and equivariant, so `Λ^3V ≅ (Λ^2V)^* ⊗ det`. Hence `Λ^3(V^*) ≅ Λ^2V ⊗ det^{−1}`, which is `10` under `SU(5)`. `Λ^5(V^*) = det^{−1}`, trivial under `SU(5)`. (v) `Γ(u)c_1⋯c_5Γ(u)^* = det(\bar u)c_1⋯c_5`, by antisymmetry of the product. ∎

Rishon dressing moves charge between sites and shifts it at one site by multiples of 5. For example, `Σ_kc_{x,k}r^{ℓ,x†}_k r^{ℓ,y}_j` is `U(5)_x`-invariant and is a `5bar` of charge `−1` at `y`: the fermion transported to `y`. The total `Σq_x` is fixed by (i).

**What is shown and what is not.**
- Shown: the `SU(5)` types `5bar`, `10`, `1` of one family (Georgi–Glashow's assignment, credited from memory, not load-bearing) are the types of gauge-covariant fermion-odd local operators. One site suffices. With their adjoints they are the 32 odd monomials built from annihilators alone or from creators alone.
- Shown: under the exact group `U(5)` the three types are three separate multiplets, with `U(1)_N` charges in ratio `1 : 3 : 5`. `LW1_5_DRAFT.md` line 428 already places hypercharge in `su(5)` and states that `U(1)_N` is not hypercharge (CH1, S2).
- Shown: no fermion-odd operator is `U(5)`-gauge invariant. Under `SU(5)` alone, the family singlet `c^5` is one.
- Not shown: anything about the light spectrum, chirality, doublers, mirrors, or which multiplets are excitations of a vacuum. This is representation content, not CH1, CG1 or MT1-ii.

*Contrast with `L5-O`.* `LW1_5_DRAFT.md` line 430 notes that on `L5-O` the `SU(5)` pieces occur inside vector-class `Spin(10)` multiplets. In both laws, then, the `SU(5)` types occur among local operators. The two laws differ in the exact multiplets. On `L5-U`, each type is its own multiplet of the exact group. On `L5-O`, the multiplets are `10`, `120`, `126`, …, never the `16`.

**Answer to item 2.** Fermion-odd gauge-covariant local operators carry `U(5)` representations with odd total `U(1)` charge (Lemma Z-U(i)). At a single site they are the blocks `Λ^a ⊗ (Λ^b)^*` with `a − b` odd. The one-family `SU(5)` content `5bar + 10 + 1` is realized by `c`, `c c c`, `c^5`. No fermion-odd operator is `U(5)`-invariant.

---

## 4. Filling (item 3)

**Lemma H-U (what local `U(5)` invariance fixes).** Let `ω` be invariant under conjugation by `U(5)_x`. Then its restriction to `𝒜_x` has density
\[
\rho_x=\sum_{k=0}^5 p_k\,\frac{\Pi_k}{\binom5k},\qquad p_k\ge0,\ \sum_kp_k=1,
\]
with `Π_k` the projection onto `N_x = k`. In particular `ω(c^†_{x,j}c_{x,k}) = δ_{jk}ω(N_x)/5`. Every value of `ω(N_x)` in `[0, 5]` occurs for some gauge-invariant state.

*Proof.* For `X ∈ 𝒜_x`, conjugation by `e^{i𝒢^T_x}` acts as `Ad Γ(e^{iT})`, because the end factors commute with `𝒜_x`. So `tr(ρ_xΓXΓ^*) = tr(ρ_xX)` for all `X`, and `ρ_x` commutes with every `Γ(u)`. It preserves each `Λ^k`, since it commutes with `N_x`. By (E1) it is a scalar on each `Λ^k`. The two-point formula follows: `tr(Π_kc^†_jc_l) = δ_{jl}binom(4,k−1)`. Examples: the product of `e^{−tN_x}/Z_x` over sites with the normalized trace on each register is invariant, since `N_x` commutes with `Γ(u)` and traces are invariant under unitaries. It has `ω(N_x) = 5/(e^t+1)`, which takes every value in `(0, 5)`. Empty or full matter with traced registers gives `0` and `5`. ∎

So local `U(5)` invariance fixes equal filling across the five modes and no coherence between modes. It does not fix the filling. This differs from `L5-O`, where Lemma H forces `ω(N_x) = 5/2`.

**Theorem F-U (filling of pure, gauge-invariant, site-transitive states).** On a periodic box `Λ_L`, let `ω` satisfy:
(a) for every `x`, `ω` is sharp in `Q_x`, that is `ω((Q_x − q_x)^2) = 0` for some `q_x`;
(b) a group of automorphisms `α_g` with `ω∘α_g = ω`, `α_g(Q_x) = Q_{gx}` and `α_g(N_x) = N_{gx}` acts transitively on sites.
Then `ω(N_x) = q − 3m` for every `x`, with `q` the common value of `q_x`, an integer. If `ω` is pure and invariant under conjugation by every `U(5)_x`, then (a) holds with `q ∈ 5Z`, so `ω(N_x) = n_m`, the value in the table of Proposition Σ-U (for `m = 5`, `0` or `5`). In no case is `ω(N_x) = 5/2`.

*Proof.* `ω((Q_{gx} − q_x)^2) = ω(α_g((Q_x − q_x)^2)) = 0`, so `q_{gx} = q_x`. Transitivity makes `q_x = q` and `ω(N_x) = n̄` constant. Apply `ω` to (1.1): `qV = n̄V + 3mV`. `Q_x` has integer spectrum, so `q ∈ Z`. If `ω` is pure and gauge invariant, Lemma P gives sharpness with `q ∈ 5Z`. Then `n̄ = q − 3m ∈ [0, 5]` picks `q` uniquely for `m ≠ 5`, and gives two options for `m = 5`. ∎

The hypothesis (b) holds for any symmetry that permutes sites and links, swaps link ends on reversed links, and acts on modes by number-preserving maps. The covariance of `L5-U` under `𝒢 = 2Z^3 ⋊ O_{c_0}` (the analogue of B1-5) is not proved in `LW1_5_DRAFT.md` for `L5-U`. Theorem F-U uses only (b), so it does not need that proof.

*Remark F.1 (the same holds for `L_cube`).* `LW1.md` line 45: "\(\mathcal G_x=n_x+\sum_{\ell\text{ out of }x}E_\ell-\sum_{\ell\text{ into }x}E_\ell\)." On a periodic box the `E_ℓ` terms cancel in `Σ_x𝒢_x`, so `Σ_x𝒢_x = N_{tot}`. The spectrum of `𝒢_x` is integral for every `S`, since six values of `E` sum to an integer. The proof above then gives: a state of `L_cube` that is sharp in every `𝒢_x` and invariant under a site-transitive group mapping `𝒢_x` to `𝒢_{gx}` has `ω(n_x) ∈ {0, 1}`. A pure, locally gauge-invariant state is sharp. So on every periodic box, no pure, locally gauge-invariant, site-transitive state of `L_cube` is half filled. `LW1.md` line 502 lists purity among what E2b does not prove ("not their uniqueness, a sea-continuation property, purity, or a vacuum selection"). This remark settles purity negatively for site-transitive states on periodic boxes. Infinite volume needs the irreducibility of the GNS representation and is not done here.

*Remark F.2 (what can give half filling).* Formula (1.1) shows what is needed. (α) A mixed vacuum, as in E2b (the tracial state). (β) A pure vacuum that is not site transitive. With only `2Z^3` cell translations, the cell average of `q_x ∈ 5Z` lies in `(5/8)Z`. Half filling then needs `3m + 5/2 ∈ (5/8)Z`, that is `24m + 20 ≡ 0 mod 5`, so `m = 5`. So `m = 5`, the half-filled register, is the only sector where a pure, gauge-invariant, cell-invariant state can be half filled, and then only with a sublattice pattern of Gauss charges. Existence is not shown. (γ) Two register classes, `m` on even-tiling links and `m'` on odd-tiling links. Then `n̄ = q − (3/2)(m + m')`, and `n̄ = 5/2` with `q ∈ 5Z` needs `m + m' ∈ {5, 15}`. Existence is not shown. (δ) Gauss constraints only for `SU(5)`, with `U(1)_N` acting as a global symmetry on states. Then a pure state need not be sharp in `Q_x`, and (1.1) fixes nothing. Each option is recorded in section 8, none is proposed.

**Answer to item 3.** No. Local `U(5)` invariance does not force a filling: it forces equal filling of the modes (Lemma H-U). For pure, gauge-invariant, site-transitive states, `m` alone fixes the filling at the integer `n_m` (Theorem F-U). **What PS-7 then needs.** PS-7 says "The vacuum is the half-filled state of the update's fermion modes" (`TOE_ASSEMBLY.md` line 140). VC1 asks for "a translation- and rotation-invariant stationary state" (line 466). Under `L5-U` with one `m`, these cannot both hold for a pure, locally gauge-invariant state. PS-7 then needs one of (α)-(δ), or it needs "half-filled" to describe the free sea of PS-7r only, with VC1's gauged vacuum allowed a different filling. This is an owner-level reading. It is named **LW1-5U-PS7** and not decided here. The same tension holds for `L_cube` (Remark F.1). On `L5-O` with one register class, the pure case is already empty (Proposition Σ).

---

## 5. LW1-5-X for `L5-U` (item 4)

`LW1_5_DRAFT.md` line 448: "For `L5-O[R]` (and `L5-U`), at angles `a ∈ 𝔈(H_C)` in the window, is every frame compatible with the cube gate `e^{iaH_C}` still Bogoliubov (resp. in `U(5)`)?"

Fix a site `x`. Let `C_e` and `C_o` be its even and odd cubes, `H_e` and `H_o` their `L5-U` cube generators, and `W_e = e^{−ia_eH_e}`, `W_o = e^{ia_oH_o}`. Each acts on a finite-dimensional space: eight five-mode sites and twelve registers of dimension `binom(10, m)`. Gate-wise compatibility asks, for each gate separately, for some register change `Ad L` with `(φ∘Ad L)(W) = W`.

**Proposition X2 (the bad parameters are finite).** Outside a finite set of points `(ε, μ)` with `0 ≤ μ < 2ε < π`, every frame at `x` that is gate-wise compatible with `W_e` and `W_o` is `Ad Γ(u)` with `u ∈ U(5)`. The finite set is contained in `{(ε, μ) : ε − μ/2 ∈ 𝔈(H_e),\ ε + μ/2 ∈ 𝔈(H_o)}`.

*Proof.* If `a_e ∉ 𝔈(H_e)`, Corollary M.1 makes the frame compatible with `H_e`, and Theorem U (by Theorem M(ii)) puts it in `U(5)`. The same holds for the odd gate. So a frame outside `U(5)` needs both angles exceptional. `𝔈(H) ∩ (−π, π)` is finite: `H` has finitely many eigenvalue differences `d ≠ 0`, and `|a| < π` allows only `|k| < |d|/2` in `ad = 2πk`. The angles satisfy `a_e ∈ (0, π/2)` and `a_o ∈ (0, π)`. The map `(ε, μ) ↦ (a_e, a_o)` is injective. ∎

`LW1_5_DRAFT.md` line 448 says "a countable set". Here the set is finite. The same proof works for `L5-O[R]`, with Theorem M(i) and Corollary R.1 in place of Theorem U. At the finitely many remaining points, LW1-5-X is open for `L5-U`. Three attacks follow.

**Lemma X1 (charge commutant, every angle).** Let `ψ = φ∘Ad L` fix a gate `W` of a cube `O ∋ x`. Put `𝔐 = O∖{x}`. Then `D = φ(N_x) − N_x` is an even element of `𝒜_x` that commutes with `W`. If the only even elements of `𝒜_x` commuting with `W` are scalars, then `φ` preserves `N_x`.

*Proof.* `W` commutes with `N_x + N_𝔐`. `ψ` fixes `N_𝔐`: `φ` fixes `𝒪_x`, and `Ad L` fixes matter. So `ψ(N_x + N_𝔐) = φ(N_x) + N_𝔐`, and it commutes with `ψ(W) = W`. Subtract. `D` is even because `φ` keeps parity (Theorem C). If `D = λ`, then `φ(N_x) = N_x + λ`, and equal spectra force `λ = 0`. ∎

For the generator `H` the even commutant in `𝒜_x` is `C1`. `[D, H] = Σ_k[D, c^†_{x,k}]X_k + Σ_k[D, c_{x,k}]X^♯_k`, the `X_k`, `X^♯_k` are independent (Theorem U's proof), so `D` commutes with every generator of `𝒜_x`.

- **Attack 1 (charge commutant).** Lemma X1 gives at most "φ preserves `N_x`", a group of dimension 251 (`LW1_5_DRAFT.md` line 450). That is not `U(5)`. Its hypothesis, a trivial even commutant of `W` in `𝒜_x`, is itself a spectral condition at the exceptional angle, and it is not verified.
- **Attack 2 (probe products).** `ψ` fixes the matter algebra of `𝔐` pointwise, so it fixes the algebra generated by `W` and that matter. Let `P_0` be the projection onto empty `𝔐`. Then `Z_{y,j} = P_0Wc^†_{y,j}P_0` is fixed and raises `N_x` by one. A product of five such operators has `x`-slices in `Hom(Λ^0, Λ^5)` only. If its link part `B` is nonzero, `φ` fixes the lines of `|0⟩` and `|5⟩`. Then `Z_{y,j}(|0⟩⟨0| ⊗ B^*B)` has slices `|e_k⟩⟨0|`, and `φ` preserves `Λ^1`. After composing with an exact `Γ(u)^{-1}`, `φ` is the identity on `Λ^0 ⊕ Λ^1`. The attack stops here, for three reasons. (i) `B ≠ 0` and the independence of the one-particle link amplitudes are themselves conditions on `a`, with their own zero sets. (ii) On `Λ^k` with `k ≥ 2`, the slices of `Z` come from the `k`-particle sector of the cube. At an exceptional angle these slices are not fixed by the one-particle ones. (iii) The [check] below shows that a frame acting as the identity on `Λ^0 ⊕ Λ^1` and as a phase on `Λ^2` can be compatible with a single-link gate.
- **Attack 3 (spectral).** A direct proof needs the eigenvalue differences of `H_C` and, at each coincidence, the commutant of the gate. The cube has 40 matter modes and twelve registers of dimension `binom(10, m)`. The Gauss laws block-diagonalize `H_C`, but no closed form for the blocks is found here. A computation is far outside the allowed size, and it could only guide.

[check] `check_x.py`: one link, `n` modes per site, number-conserving rishon hop in sector `m`, every exceptional angle in `(0, π)` with multiplier up to 11. The site part of the Lie algebra of compatible frames has rank `1 + n^2 = 5` at the generator. For `(n, m) = (2, 1)` and `(2, 3)` it stays 5 at every exceptional angle tested. For `(2, 2)`, at `a = π/√2 ≈ 2.2214`, the rank is 6. The extra frame commutes with `N_x`, so it lies in the `N_x`-preserving group of Attack 1 and outside `U(2)`. `check_u.py` part (3), for `(n, m) = (3, 1)`, finds rank 10 at the first six exceptional angles. So the gate-level bound can fail at an exceptional angle of a single-link number-conserving gate. Whether it fails for the cube gate is LW1-5-X.

**Answer to item 4.** Partly closed. The bound `U(5)` holds at all but finitely many parameter points (Proposition X2). At those points it is open, after three attacks: charge commutant, probe products, spectral. A small single-link analogue has a counterexample at one exceptional angle.

---

## 6. D1's reason under `L5-U` (item 5)

Lines of #10014 used, quoted.
- Lines 4-8 (claim_scope): "Suppose N identical complex fermion modes are carried per frame cell, the frame group is the full Bogoliubov group Spin(2N) of those modes, and the light content is one fermion-parity half S+ (dimension 2^(N-1)), read as 2^(N-1) Weyl species in 3+1 dimensions. Then the smallest N for which S+ has no perturbative anomaly, no old SU(2) (Witten) anomaly, no Spin-Z4 (mod-16) anomaly of the centre, and no Spin(2N)-invariant mass is N = 5".
- Line 66: "A Majorana mass for a Weyl multiplet needs a *symmetric* invariant bilinear on S+."
- Line 78: "For N odd, z = exp(i pi (n - N/2)) lies in Spin(2N), acts on S+ as a uniform +-i, and z^2 = -1."
- Lines 103-104: "The theorem uses the full Spin(2N). If M3's "as large as M4 permits" lets a proper subgroup serve for small N, the following hold."
- Line 163: "(a) the frame group is the full Spin(2N);"

So #10014 tests proper subgroups only for `N ≤ 4` (lines 102-113). It does not test `U(N)` or `SU(N)` at `N = 5`. Under `L5-U`, the exact group is `U(5)` (Theorem U), so condition (a) fails. The question is whether the same four criteria, with the exact group in place of `Spin(2N)`, still pick `N = 5`. Reading (b) is kept: `S+ = ⊕_{k\ even}Λ^k(C^N)`, each state read as one Weyl species. A `U(N)` action on the site is `Γ(u)` times a character. On `Λ^k` the central `U(1)` then has charge `k − c`. For `U(5)` representations, `c ∈ 5Z` (characters `det^j`). The statements below hold for every `c ∈ Z`.

**Proposition D (the selection under `SU(5)` and `U(5)`).**
(i) Under `SU(5)`, `S+ = 1 ⊕ 10 ⊕ 5bar`. Its cubic anomaly vanishes. Its only invariant bilinear is on `1 ⊗ 1`, and that bilinear is symmetric. So `S+` has an `SU(5)`-invariant Majorana mass, and the "no invariant mass" criterion fails at `N = 5`.
(ii) Under `SU(N)`, for every `N ≥ 1`, `S+` has a symmetric invariant bilinear. So the criterion selects no `N`.
(iii) Under `U(5)` with charges `k − c`, `c ∈ Z`, the `U(1)`-gravitational anomaly of `S+` is `40 − 16c ≠ 0`. All three `U(1)` anomalies (gravitational, cubic, mixed with `SU(5)^2`) vanish exactly at `c = 5/2`.
(iv) Under `U(N)` with `c ∈ Z`, no `N ≥ 1` meets both `U(1)`-gravitational anomaly freedom and protection.

*Proof.* (i) Cubic anomaly, from `Tr X^3` on a diagonal traceless `X = diag(x_i)`, `p_3 = Σx_i^3`. On `Λ^2`: `Σ_{i<j}(x_i + x_j)^3 = (N−1)p_3 + 3Σ_{i≠j}x_i^2x_j = (N−4)p_3`, using `Σ_{i≠j}x_i^2x_j = p_2p_1 − p_3 = −p_3`. At `N = 5` this is `p_3`. On `Λ^4`: the four-subsets are complements of one index, with sum `−x_j`, so the trace is `−p_3`. `Λ^0` gives 0. Total 0. Bilinears: `ζ` acts on `Λ^a ⊗ Λ^b` as `ζ^{a+b}`. For `a, b ∈ {0, 2, 4}`, `a + b ≡ 0 mod 5` only for `a = b = 0`. `Λ^0 ⊗ Λ^0` is one-dimensional and trivial, and its bilinear is symmetric. (ii) `Λ^0 ⊂ S+` is trivial under `SU(N)`. (iii) The `SU(5)` multiplets have dimensions `1, 10, 5` and charges `−c, 2 − c, 4 − c`. Gravitational: `−c + 10(2 − c) + 5(4 − c) = 40 − 16c`. Mixed, with indices `T(10) = 3/2`, `T(5bar) = 1/2`: `(3/2)(2 − c) + (1/2)(4 − c) = 5 − 2c`. Both vanish only at `c = 5/2`. Cubic: `−c^3 + 10(2 − c)^3 + 5(4 − c)^3`, which is 0 at `c = 5/2`. (iv) For `N = 1`, `S+ = Λ^0` has charge `−c`. Its gravitational anomaly vanishes only at `c = 0`, and then it is neutral and massable. For `N ≥ 2`, `Σ_{k\ even}binom(N,k) = 2^{N−1}` and `Σ_{k\ even}k·binom(N,k) = N2^{N−2}`, so the gravitational anomaly is `2^{N−1}(N/2 − c)`. For odd `N` no integer `c` makes it zero. For even `N` it is zero only at `c = N/2`. Then `Λ^0` and `Λ^N` are both in `S+`, both trivial under `SU(N)`, with total charge `N − 2c = 0`, so the pairing `Λ^0 ⊗ Λ^N → C` is `U(N)`-invariant. That gives an invariant pairing between two multiplets, which extends to a symmetric bilinear on their sum: a Dirac mass. ∎

[check] `check_u.py` part (2): the three `U(1)` anomalies at `c = 0, 1, 2, 5/2, 3` are `(40, 400, 5)`, `(24, 144, 3)`, `(8, 32, 1)`, `(0, 0, 0)`, `(−8, −32, −1)`. The `SU(N)` cubic anomaly of `S+` is `−1` at `N = 3` and `0` for `N = 4, …, 7`.

*Remark D.1 (what restores the selection).* The shift `c = 5/2` is the action of `Spin(10)`'s spinor restricted to the double cover of `U(5)`. It uses the Cartan generators `n_j − 1/2` (#10014 lines 35-36: "The Cartan generators are M_{2j,2j+1} = n_j - 1/2."). It acts through `det^{−1/2}`, which is not a representation of `U(5)`. With that shift and `N` odd, the singlet has charge `−N/2 ≠ 0`, and `Λ^a ⊗ Λ^b` with `a, b` even has an `SU(N)` invariant only if `a + b ∈ {0, N, 2N}`. That allows only `a = b = 0`, so `S+` is protected. As a guide (not rebuilt here), #10014's section 2 makes the cubic forms vanish for `N ≥ 4`, so the smallest passing `N` would again be 5. This brings back condition (a) through `Spin(10)`'s normalisation. It is recorded, not proposed (section 8, u6).

*Remark D.2 (a content change, not proposed).* If the `SU(N)` singlets are removed from `S+`, then under `SU(5)` the content `10 ⊕ 5bar` is anomaly free and protected (by the centre argument of (i)). `N = 3` (`3bar`, anomalous) and `N = 4` (`6`, real) fail. So `N = 5` would again be the smallest. But this changes reading (b) and fails test 4 (section 8, u7). #10014 line 84 says the singlet is needed under `Spin(10)`'s `Z_4`: "Removing the SU(5)-singlet state (nu^c) leaves nu = 15."

*The mod-16 criterion.* Line 78's `z` acts on `S+` as a uniform `±i`. Under genuine `U(5)`, the nearest element `Γ(i·1)` acts on `Λ^k` as `i^k`, which is `1, −1, 1` on `S+`. It is not uniform, so the criterion as written does not apply. This is not pursued.

**Answer to item 5.** No. Under `L5-U`, #10014's selection of `N = 5` does not survive with the exact group in place of `Spin(10)`. Under `SU(5)`, perturbative anomaly freedom holds (as for `N = 4, 6, 7`), but the singlet takes an invariant Majorana mass at every `N`. Under `U(5)`, the `U(1)`-gravitational anomaly is `40 − 16c`, nonzero for every integer shift. So D1's test-4 line, "The constant 5 comes from #10014 under its conditions (a)-(c)", holds for `L5-O[S_+]` (`LW1_5_DRAFT.md` line 442: "Its condition (a) ... is met exactly by `L5-O[S_+]`"). It does not hold for `L5-U`. Under `L5-U`, the constant 5 needs another reason, or it is a free datum of PS-5.

---

## 7. `SU(2)` and T0 (item 6)

`TOE_ASSEMBLY.md` line 530: T0 is "the existence clause of the Clay problem without the mass gap, for SU(2) first". Line 377 (GA2): "For each simple factor `G_i` with negative one-loop beta coefficient, the framework's gauge sector ... agrees with continuum `G_i` Yang-Mills".

**Proposition T (exact `SU(2)` Gauss law).** Let `𝔥 ⊂ u(5)` be the Lie algebra of a closed subgroup `H ⊂ U(5)`, for example `su(2)` on modes 4 and 5. Then:
(i) for `T ∈ 𝔥`, the `𝒢^T_x` commute with every gate of `L5-U`, at every angle and for every `m`; they satisfy the `𝔥` relations, and `T ↦ e^{i𝒢^T_x}` is a representation of `H` at each site, given by the representation of `U(5)` restricted to `H`;
(ii) for `H = SU(2)` this is a Gauss law of three generators per site, each a sum of commuting site and link-end parts;
(iii) under `SU(2)_x × SU(2)_y`, with `SU(2)` on modes 4, 5, the link variables `U^{jk}_ℓ = r^{ℓ,y}_j r^{ℓ,x†}_k` split into a `(2, 2)` block (`j, k ∈ {4, 5}`), two doublet blocks (one index in `{4, 5}`), and an `SU(2)`-singlet block (`j, k ∈ {1, 2, 3}`).

*Proof.* (i) Theorem U: every `h^U_ℓ` commutes with every `𝒢^T_z`, so every cube gate does at every angle. Electric gates are functions of end numbers, which commute with `𝒢^T`. `T ↦ 𝒢^T_x` is a Lie algebra map, because each summand `Σc^†Tc` and `Σr^†Tr` is, and the summands commute. It is the derivative of the `U(5)` representation `u ↦ Γ(u) ⊗ (end actions)`, restricted to `H`. (ii) `dim su(2) = 3`. (iii) `U^{jk}` transforms by `u_y` on `j` and `\bar u_x` on `k`. ∎

So `SU(2)` is an exact gauge subgroup with its own Gauss law. Seen from `SU(2)`, though, `L5-U` is an `SU(2)` lattice gauge theory coupled to extra fields: the doublet and singlet link blocks, plus modes 1-3. Its full Gauss law is the stronger `U(5)` law. GA2's simple factor under `L5-U` is `SU(5)`. T0 then enters in one of two ways. Either `U(5)` is broken at long distance to a group with `SU(2)` as a simple factor and the extra fields gapped (EW1/VC1), or T0 is extended to `SU(5)`. `LW1_5_DRAFT.md` line 438 records the same alternatives: "A pure `SU(2)` Yang–Mills sector of T0's kind arises only after breaking (EW1/VC1), or GA2 needs T0's extension to `Spin(10)` or `SU(5)`". Restricting the hop or the registers to modes 4 and 5 would be a choice made because it yields T0's group: test 1 fails. T0 is pure gauge (`TOE_ASSEMBLY.md` line 385: "matter in the RG (T0 is pure gauge)").

**Answer to item 6.** Yes, `SU(2) ⊂ U(5)` is an exact gauge subgroup with its own exact Gauss law, at every angle and every `m`. It is not the gauge group of the lattice theory. The plug-in into T0 needs breaking or T0's extension, as on `L5-O`.

---

## 8. Four-test check of recorded options

Tests: (1) states or fixes a part's target; (2) open-ended; (3) settles a downstream question by premise; (4) adds structure its reasons do not need. Nothing below is proposed. Each row records what a choice would do.

| Option | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| u1. LW1's conjugation reading of gauge invariance, applied to pure states (Lemma P) | pass | pass | pass | pass: no new structure | not a new choice; used |
| u2. A fixed Gauss constraint `𝒢^{\mathbf 1}_x = 5k` as a law premise | pass | pass (integer) | fails: by Theorem F-U it fixes the filling `5k − 3m` of every pure site-transitive gauge-invariant state, which is PS-7/VC1's question | conditional | recorded, not proposed |
| u3. The value of `m` | pass | pass (named range) | conditional: by Theorem F-U, `m` fixes the filling `n_m` of pure, site-transitive, gauge-invariant states. Choosing `m` *because* of a filling fails test 1 | pass | free datum, as in `LW1_5_DRAFT.md` line 318; disclosed |
| u4. Two rishon classes, `m + m' ∈ {5, 15}` (Remark F.2 γ) | conditional: chosen to meet PS-7 | pass | conditional: it decides VC1's half-filled pure-vacuum question | fails unless a part needs a pure, half-filled, site-transitive vacuum; none does today | recorded, not proposed |
| u5. `m = 5` with a sublattice pattern of Gauss charges (Remark F.2 β) | pass | pass | — | — | not a law choice: a property of a state that breaks site transitivity; existence open |
| u6. Charge shift `c = 5/2` in the anomaly reading (Remark D.1) | fails unless derived: it is chosen because it makes #10014 pass at `N = 5` | pass | conditional | conditional: it imports `Spin(10)`'s normalisation into a `U(5)` law | recorded, not proposed |
| u7. Removing `SU(N)` singlets from `S+` (Remark D.2) | fails: it changes the content to get the selection | pass | conditional | fails | recorded, not proposed |
| u8. Gauss constraints for `SU(5)` only, `U(1)_N` global on states (Remark F.2 δ) | pass | pass | conditional: it decides PS-7's compatibility and CH1's `U(1)_N` question | conditional: the frames of `U(1)_N` stay exact anyway; only the reading of states changes | recorded, not proposed |

---

## 9. `L5-U` beside `L5-O`, for LW1-5-RQ

| Fact | `L5-O[S_+]` (from `LW1_5_DRAFT.md`) | `L5-U` (this file) |
|---|---|---|
| Exact group at a site | `Spin(10)` on states | `U(5)` |
| Pure Gauss singlets at every site, one register class | none (Proposition Σ) | exist for every `m`, translation invariant (Proposition Σ-U); point group open |
| Fermion-odd gauge-covariant local operators | vector class only, never the `16` (Lemma Z) | odd total `U(1)` charge; `SU(5)` types `5bar_{−1}`, `10_{−3}`, `1_{−5}` at one site (Lemma Z-U) |
| Filling of gauge-invariant states | `5/2`, forced (Lemma H) | free (Lemma H-U); pure and site transitive: integer `n_m`, never `5/2` (Theorem F-U) |
| PS-7 with a pure, site-transitive, gauge-invariant vacuum | impossible: no pure invariant state (Σ) | impossible: not half filled (F-U) |
| #10014's reason for `N = 5` (D1, test 4) | holds: condition (a) met | fails: no `N` selected under `SU(5)` or genuine `U(5)` (Proposition D) |
| Frame bound at exceptional angles | open at finitely many `(ε, μ)` (Proposition X2's proof) | open at finitely many `(ε, μ)` (Proposition X2) |
| `SU(2)` for T0 | exact subgroup; needs breaking or extension | exact subgroup (Proposition T); needs breaking or extension |
| Register, hop terms per link | 512, 100 | `binom(10, m)`, 25 |
| Extra gauge `U(1)` | none | `U(1)_N`, not hypercharge (CH1 S2) |

Neither law dominates. `L5-U` removes both facts that count against `L5-O`, and it is smaller. It gives up D1's own reason for five modes. It also makes PS-7's half filling incompatible with a pure, site-transitive, gauge-invariant vacuum, though `L5-O` with one register class has no pure invariant vacuum at all. With a second register class, each law reaches a pure half-filled option. For `L5-O` that is `S_+`/`C^{20}`, choice c10. For `L5-U` it is `m + m' ∈ {5, 15}`, existence not shown. Each such option fails test 4 today.

---

## FINISH

**Proved here (pass 1, not refereed).**
- Lemma P: a pure state is invariant under conjugation by `U(5)_x` exactly when it is `SU(5)_x`-invariant and sharp in `Q_x`; then `Q_x ∈ 5Z`.
- Lemma E: `Λ^k(C^5)` is irreducible under `SU(5)`; the comultiplication and the volume-split maps are injective and equivariant.
- Lemma S: `⊗_iΛ^{a_i}(C^5)` has an `SU(5)` invariant exactly when `Σa_i ≡ 0 mod 5`.
- Proposition Σ-U: in the sector reading, there are no all-site singlets for any `m`. In LW1's reading, pure all-site singlets exist for every `m ∈ {1, …, 9}`, translation invariant, with `N_x = n_m` sharp.
- Lemma Z-U: fermion parity of a local operator is `(−1)^{total U(1) charge}`, and it is a gauge transformation. No fermion-odd operator is `U(5)`-invariant. One-site odd operators carry `Λ^a ⊗ (Λ^b)^*`, `a − b` odd. `c`, `c c c`, `c^5` carry `5bar_{−1}`, `10_{−3}`, `1_{−5}`. `c^5` is `SU(5)`-invariant and fermion odd.
- Lemma H-U: local `U(5)` invariance fixes the site marginal to `Σ_kp_kΠ_k/binom(5,k)`; the filling is free.
- Theorem F-U: a Gauss-sharp, site-transitive state has integer filling `q − 3m`. A pure, gauge-invariant, site-transitive state has filling `n_m`, never `5/2`. Remark F.1: the same for `L_cube`, `ω(n_x) ∈ {0, 1}`.
- Lemma X1 and Proposition X2: the frame bound `U(5)` holds outside a finite set of `(ε, μ)`; the same argument applies to `L5-O`.
- Proposition D: under `SU(N)`, `S+` is never protected. Under `U(N)` with integer shifts, gravitational anomaly freedom and protection never hold together. At `N = 5`, the three `U(1)` anomalies vanish only at `c = 5/2`.
- Proposition T: every closed `H ⊂ U(5)`, in particular `SU(2)`, has an exact Gauss law at every angle. The `U(5)` link variables split under `SU(2)` into gauge, doublet and singlet blocks.

**Counterexamples.**
- To "local `U(5)` invariance forces a filling" (the analogue of Lemma H): the Gibbs product states of Lemma H-U have every filling in `[0, 5]`.
- To "a pure, gauge-invariant, site-transitive half-filled vacuum exists" for `L5-U` with one `m`, and for `L_cube`, on periodic boxes: Theorem F-U and Remark F.1.
- To "#10014's criteria select `N = 5` under the exact group of `L5-U`": Proposition D.
- To the gate-level frame bound for a single-link number-conserving gate (two modes per site, `m = 2`, `a = π/√2`): [check] only, a guide, not a proof.

**Open, by name.**
- LW1-5-X for `L5-U` at the finitely many points of Proposition X2. Three attacks recorded: charge commutant, probe products, spectral.
- LW1-5U-Σc: invariance of a pure all-site singlet under the point group `O_{c_0}`.
- LW1-5U-PS7 (owner-level reading): how PS-7's "half-filled" reads under `L5-U`. Options (α)-(δ) of Remark F.2, with existence open for (β) and (γ).
- Covariance of `L5-U` under `𝒢` (the analogue of B1-5), not proved here and not used.
- The infinite-volume form of Theorem F-U and Remark F.1.
- LW1-5-RQ (owner).

**What this means for LW1-5-RQ.** Both facts that count against `L5-O` are absent on `L5-U`. Pure Gauss singlets exist for every `m`. The `SU(5)` types of one family are local operator types. Against `L5-U`, two facts are new. First, D1's stated reason for five modes, #10014's condition (a), fails there, and the same criteria with `U(5)` or `SU(5)` select no `N`. Choosing `L5-U` therefore leaves PS-5's constant 5 without its recorded reason. Second, under one value of `m`, PS-7's half filling cannot hold for a pure, site-transitive, gauge-invariant vacuum. That tension also holds for `L_cube`, and `L5-O` with one class has no pure invariant vacuum at all. Both laws leave LW1-5-X open at finitely many parameter points. Both have `SU(2)` only as an exact subgroup. The choice trades the singlet and family-content gains of `L5-U` against D1's reason, which only `L5-O` keeps. This draft does not choose.

**Inputs from outside the working set.** The CAR reading of five site modes and of the rishons, with links as ordinary tensor factors (`LW1.md` line 42). `LW1_5_DRAFT.md`'s Theorems C, M, U and Corollary M.1. LW1's Lemma A1 (three links of each tiling per site). Standard mathematics, rebuilt in the text: commutators span `sl(5)`, irreducibility of `Λ^k` by elementary moves, comultiplication on the exterior algebra, the wedge pairing, Schur's lemma for unitary representations, the anomaly sums by direct expansion, binomial sums over even `k`, Lagrange interpolation (through Corollary M.1). Standard facts cited, not rebuilt, and not load-bearing: the `SU(5)` content of one Standard Model family and its branching (Georgi–Glashow); `T(10) = 3/2` and `T(5bar) = 1/2` (rebuilt only through the `U(1)` mixed sum, which uses them); the vanishing of `so(2N)` cubic forms for `N ≥ 4` (Remark D.1, guide only, from #10014 section 2). Literature context, credited from memory and not load-bearing: quantum link models with rishons (Brower–Chandrasekharan–Wiese); Kogut–Susskind background charges for staggered fermions.
