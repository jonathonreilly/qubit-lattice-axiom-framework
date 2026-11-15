# BK1-UQ. Strict-path charge capacity on the U(5) register

## 0. Status

**Pass 2; not refereed or frozen.** The results are conditional on the specified `L5-U[m]` law and EW1 definitions. They do not establish a vacuum, an FMS phase, or a physical symmetry breaking.

**Proved here.** For `1 ≤ m ≤ 9`, a bosonic `H`-fixed charged component has charge in `10Z \ {0}`. Its EW1 single-link matrix vanishes. Every strict transporter between distinct sites has both Hilbert–Schmidt transport defects at least `dim W_cap ≥ 1`, in every state. The named attacks do not evade this argument. Endpoint capacity also gives the stated bounds and the explicit nonzero split and matter-dressed examples below. These are mathematical statements under the stated conventions, pending the independent referee.

**GAPs and corrections.** The draft's CAR proof of its full single-link theorem only covers `|q| > 5`, not all `|q| > d_m`; the spectral proof covers the full statement. Its matter-necessity statement needs endpoint covariance at *both* endpoints, and the matter-number change at the second endpoint has the opposite sign. The link-count bound does not prove that the proposed endpoint-join construction is the unique or structurally smallest network extension. The word-count lemma for total charge also needs a nonzero operator to conclude that unused-site charges vanish. Exact corrections appear below.

**Open by name.** **T1-SPLIT** asks for arbitrarily small two-sided defects for `det^{±2}` with a fixed palette: link-only on `m ∈ {4,5,6}`, or with endpoint matter on `m ∈ {3,4,5,6,7}`. No such state or palette is constructed here. UQ's strict-path mathematical target has no remaining named step in this pass; the future referee must check it. The general FMS, BK1 vacuum and phase questions remain open. C-SPLIT and C-SPLIT-M are proposed, not adopted.

**Provenance.** Pass 1: Claude Opus 5.5, `BK1UQ_DRAFT.md`. Pass 2: Codex `gpt-6.1-terra`; effort and session id: see run log. Source context: `TOE_ASSEMBLY.md` §§3.4–3.6 and BK1 target, `prior/BK1UQ.md`, `BK1_TREE.md`, `EW1.md`, and the earlier results cited below. This is an author-side distillation, not independent review or an audit. The pass-1 source records its own revisions and literature search; those revision identifiers were not independently refreshed in this pass.

## 1. Definitions inferred by the distiller

These conventions make the draft's implicit domains explicit; they are not new physical axioms.

1. `L5-U[m]` has matter Fock space on five modes per site, and independent link algebras `End(Λ^m C^10)` with five rishon modes at each end, `1 ≤ m ≤ 9`. The graph is the cubic lattice, with six incident links per site. Matter and link factors commute; distinct link factors commute. The central gauge action at `z` is `Ad exp(iθ Q_z)`, where `Q_z=N_z+Σ_{ℓ∋z}p_{ℓ,z}`. On a link alone use its end number.
2. `I_m=[max(0,m−5), min(5,m)] ∩ Z` and `d_m=min(m,10−m)`. The matrix `U_ℓ^{jk}=r^y_j r^{x†}_k` raises the source end number and lowers the target end number. `V` is the dual of the creator representation; its central charge is `−1`. An irreducible in `V^{⊗p}⊗V̄^{⊗p′}` has charge `q=p′−p`.
3. EW1's fixed decomposition `W=⊕_r W_r` is read as orthogonal, with an adapted orthonormal basis. This is a **proposed reading**, not an owner decision. Distinct central-charge eigenspaces are orthogonal independently of this choice. Put `W^(q)={w:σ(e^{iθ}I)w=e^{iqθ}w for all θ}` and `W_cap=⊕_{|q|>d_m}W^(q)`. The cap and the main floor are canonical under changes of decomposition within a charge space.
4. A **strict transporter** is exactly EW1 Definition 2.3: on each irreducible summand form its projected tensor-product matrix on each link, multiply along a nonempty path, use its matrix adjoint on reversed links, and take a finite convex combination of paths. Endpoints are distinct. The same fixed summand decomposition is used on every link. Define `‖M‖²_HS=Σ_ij M_ij† M_ij`; `D_+=ω(‖T†T−I‖²_HS)` and `D_−=ω(‖TT†−I‖²_HS)`.
5. `H=S(U(3)×U(2))` is the standard-ratio subgroup in EW1; `K_G=H{±I_5}`. An EW1 bosonic composite is a local, fermion-even, linearly independent covariant tuple carried at a single site. R-FMS clauses (O), (C), (A), (T), block sites and quantifiers are exactly those of `EW1.md` Definition 2.5. In particular the fixed triple `(W,σ,v)` does not depend on tolerance in the BK1 root.
6. A local matrix `T` is **charge-diagonal** if its entries between different `W^(q)` vanish. Covariance at `z` means `a_{z,g}(T)=σ(g)^T T`; covariance at `z′` means `a_{z′,g}(T)=T(σ(g)^T)^{-1}`. Endpoint-charge statements below assume the relevant covariance explicitly. Paths used in the constructive examples are finite, do not repeat links, and are pairwise link-disjoint.

**Reading check.** The orthogonal-decomposition reading passes the draft's tests 1–4: it fixes no target, is closed, assumes no downstream conclusion, and adds no structure needed for the canonical charge-space floor. A nonorthogonal choice of irreducible complements does not change the orthogonal central-charge spaces; the proof uses their orthogonal projections. This check is an assessment, not adoption.

## 2. Prior results and the finite-register setting

`LW1_5.md` Z-U already proves total local central charge equals matter-number change, and parity is `(-1)^{Σq_z}`. `EW1.md` Theorem 4.1(1) already proves even charge for bosonic composites; its Proposition 6.5 proves the fifth-root central element lies in `H`. `EW1.md` §2.3 fixes charges, projection and reversed factors. `EW1.md` line 274 and `GA2_Y2.md` Theorem 3.2 already give the end-number interval. `CH1_5UQ.md` Theorem 5.1 already proves the charge-three hop is nonzero exactly for `3 ≤ m ≤ 7`. `GA2_Y2.md` Corollary 2.2 proves the related noninvertibility result; `EW1.md` Lemma 6.3a and Theorem 6.3′ give related grading and alignment floors. The charge-capacity argument below strengthens these only in its stated range. The word count in `EW1.md` Theorem 6.3′ already supplies the relevant central grading; the present conclusion that a whole single-link factor is zero is the explicit application here. `LW1_5.md` lines 240 and 250 already contain the singlet criterion and exterior-power embeddings used below.

The pass-1 literature search is recorded in `BK1UQ_DRAFT.md` §2. In particular Brower, Chandrasekharan and Wiese, *QCD as a Quantum Link Model* (hep-th/9704106), give the determinant special case; Chandrasekharan and Wiese (hep-lat/9609042) give the spin raising-operator link. These are context and credit, not independent checks of this file. The draft marks inaccessible literature as unverified. The digest `prior/BK1UQ.md` also records the failed same-order reversal, the missing-classicality alignment argument, and the limits of earlier cut bounds. We use adjoint reversal and retain (C).

**Lemma 2.1 (end-number spectrum).** Both end numbers on one link have spectrum `I_m` and diameter `d_m ≤ 5`; their sum is `mI`.

*Proof.* An occupation basis vector has `a` occupied source and `m−a` occupied target modes. It exists exactly when `0≤a≤5` and `0≤m−a≤5`. The resulting interval has the stated endpoints and diameter. □

**Lemma 2.2 (charge grading and parity).** For a nonzero local operator `B` of definite central charges `q_z`, only finitely many `q_z` are nonzero, its total matter-number change is `Σ_z q_z`, and its matter parity is `(-1)^{Σ_z q_z}`. Consequently every irreducible summand of an EW1 bosonic composite has even central charge.

*Proof.* Enclose the support in a finite set of sites together with both ends of its supported links. Summing the Gauss charges over those sites gives the total matter number plus scalar link totals and terms commuting with `B`. Outside that set the gauge action fixes `B`; its nonzeroness forces the corresponding `q_z` to vanish. At angle `π`, total matter-number conjugation is fermion parity. Each composite component in an adapted irreducible basis is nonzero by linear independence and has its summand's charge at its carrier and zero charge elsewhere. Evenness forces that charge to be even. This reproduces the already proved Z-U and EW1 results cited above. □

**GAP in draft Lemma 4.1.** It omits `B≠0` when concluding unused-site charges are zero. For `B=0`, any assigned `q_z` satisfies the covariance equation. Lemma 2.2 supplies the needed hypothesis; its use for composite components is unaffected.

**Lemma 2.3 (weights and basis).** Distinct `W^(q)` are orthogonal and their sum is `W`. If an `H`-fixed vector in `V^{⊗p}⊗V̄^{⊗p′}` has a nonzero weight component, that weight is `(n,n,n,n,n)` and the central charge is `5n`. The operator `‖M‖²_HS` is invariant under scalar unitary changes of basis in `W`.

*Proof.* Unitarity separates distinct central characters. The diagonal matrix with entries `s,s^{-1}` at any two positions and `1` elsewhere belongs to `H`; invariance forces the two corresponding weight coordinates to agree. The sum of the five weights is `p′−p`. For basis independence expand `(uMu†)_ij` and use the two unitary orthogonality identities; all coefficients are scalars. □

## 3. The charge-ten statement

**Theorem 3.1 (central charge).** Let `Φ` be an EW1 bosonic composite in `W=⊕_r W_r`, and let `H⊆Stab(v)`. Every summand has even charge, and every `r` with `v_r≠0` has `q_r∈10Z`. If the central `U(1)` does not fix `v`, some such `q_r` is nonzero. The same hypotheses hold if `Stab(v)=K_G`.

*Proof.* Evenness is Lemma 2.2. Each irreducible projection of an `H`-fixed vector is `H`-fixed. The scalar `ζI`, `ζ=e^{2πi/5}`, lies in `H`, since `ζ^5=1`. Thus `ζ^{q_r}v_r=v_r`, so `5|q_r` when `v_r≠0`. With evenness, `10|q_r`. If all nonzero-charge projections vanished, every central element would fix `v`. Finally `λI∈H` iff `λ^5=1`, and `λI∈K_G` iff `λ^{10}=1`; thus `H⊆K_G` but the full central circle is not in `K_G`. □

*Second proof of divisibility.* Lemma 2.3 gives `q_r=5n`; evenness forces `n` even. □

The charge magnitude `10` is attained by `det^{±2}`, whose restriction to `H` is trivial. At `m=5` a nonzero bosonic determinant-square carrier is described in Theorem 4.3 below.

## 4. One-link capacity and exact exterior powers

**Lemma 4.1 (spectral blocks).** If a finite-dimensional self-adjoint `E` has spectrum in an interval of diameter `d` and `[E,B]=qB` with `|q|>d`, then `B=0`.

*Proof.* For spectral projections `P_a,P_b`, `(a−b−q)P_aBP_b=0`; `|a−b|≤d`, so every block vanishes. The equivalent circle-covariance statement follows by differentiating. □

**Theorem 4.2 (single-link vanishing).** On `L5-U[m]`, a single-link operator of central charge `q` at either end vanishes if `|q|>d_m`. For every irreducible `σ_r` of charge `|q_r|>d_m`, every EW1 projected link matrix and its adjoint vanish, for every realization, copy, order and `c>0`. Hence all charged `H`-fixed components of Theorem 3.1 have zero single-link matrices on every register.

*Proof.* Apply Lemmas 2.1 and 4.1 to the relevant end number. Each `U` raises the source number by one and each entrywise adjoint lowers it by one. Every unprojected tensor entry with `p` and `p′` letters therefore has charge `p−p′=−q_r`, independent of order. Each projected entry, including a cross-copy projection, is a scalar linear combination of these zero words. Adjoint and scalar normalization preserve zero. Theorem 3.1 gives `|q_r|≥10>5≥d_m`. □

*CAR check, restricted range.* CAR normal ordering preserves net creation number. A normal-ordered word in five end modes with net creation number greater than five has repeated creators and vanishes; the negative case has repeated annihilators. Thus every link word of `|q|>5` vanishes even on the full ten-mode Fock space. This independently covers the charge-ten application. □

**GAP in draft's second proof of Theorem B(b).** It asserts the full range `|q|>d_m` but uses `|q|≥10>5`. For example `m=1`, `d_m=1`, `|q|=2` satisfies the theorem's hypothesis but not the CAR count used there. The corrected CAR statement is `|q|>5`; the spectral proof above covers all `|q|>d_m`.

**Corollary 4.2a (Abelian rung).** On a spin-`S` link, `[S³,B]=qB` and `|q|>2S` imply `B=0`; in particular `(S⁺)²=0` at `S=1/2`.

*Proof.* `S³` has spectral diameter `2S`. Apply Lemma 4.1. □

**Theorem 4.3 (exterior powers).** For ordered `a`-subsets `I,J`, `1≤a≤5`, in the normalized antisymmetric tensor basis,
\[
\sigma_{\Lambda^a V}(\mathbf U)_{IJ}=a!(-1)^{a(a-1)/2}\,r^y_I r^{x\dagger}_J.
\]
This matrix is nonzero exactly when `a≤d_m`. In particular `D_ℓ=5! r^y_{12345}r^{x†}_{12345}` is nonzero exactly at `m=5`, where it is `5!` times a rank-one partial isometry. The tree's determinant carrier `B_xD_{xy}B_y` and its product of determinant paths vanish for `m≠5`; the carrier is nonzero at `m=5`.

*Proof.* Expand the antisymmetrizers. Moving all `y` annihilators left past `x` creators gives `(-1)^{a(a−1)/2}`; sorting both index lists cancels the permutation signs and the `(a!)²` terms produce the factor `a!`. If `a>d_m`, Theorem 4.2 gives zero. Otherwise choose `a` occupied modes `I` at `y`, leave `J` empty at `x`, and place the remaining `m−a` particles among the `10−2a` available modes. This is possible exactly when `a≤min(m,10−m)`. The displayed monomial moves the chosen vector to a nonzero occupation vector. For `a=5` the only source and target configurations have all five particles at opposite ends. The nonzero matter factors in the carrier act on separate matter factors from the nonzero link operator. □

The `a=3` window is already proved in `CH1_5UQ.md` Theorem 5.1. The draft reports a sampled sparse-matrix check of this formula; this pass did not rerun or independently inspect that scratch script, and does not use it as proof.

## 5. Strict transport, floors and the three attacks

**Theorem 5.1 (strict floors).** For any strict `T` between distinct sites, `T=0⊕T′` on `W_cap⊕W_cap^⊥`, and
\[
\|T^\dagger T-I\|^2_{\rm HS}\ge (\dim W_{\rm cap})I,\qquad
\|TT^\dagger-I\|^2_{\rm HS}\ge (\dim W_{\rm cap})I.
\]
The inequalities hold in every state. Under Theorem 3.1's noncentral stabilizer hypothesis, both floors are at least one. For `W=det^{±2}` both defects equal one.

*Proof.* Each nonempty path factor is block diagonal in the fixed decomposition. Every block in `W_cap`, in either direction, is zero by Theorem 4.2; path products and convex sums preserve this block form. In an orthonormal basis adapted to `W_cap`, both defect matrices restrict to `−I` there. Summing `M_ij†M_ij` over just those entries gives the inequalities. Theorem 3.1 supplies a nonzero cap component. For a one-dimensional determinant-square representation the whole transporter is zero, so equality holds. □

**Corollary 5.2 (R-FMS and alignment).** Clause (T) cannot hold at `δ<dim W_cap`; for `Stab(v)=K_G` it fails at every `δ<1`, on all nine U registers. If (O), (C), (A) hold for one ordered pair, let `R_cap={r:W_r⊆W_cap}`, `s=|R_cap|`, `V_cap=Σ_{r∈R_cap}|v_r|²`. Then
\[
V_{\rm cap}\le \delta|v|^2+\left(s+\tfrac12\sqrt{\dim W}\right)\sqrt\delta,
\quad
\delta\ge\min\!\left\{1,\left(\frac{V_{\rm cap}}{|v|^2+s+\frac12\sqrt{\dim W}}\right)^2\right\}
\quad(V_{\rm cap}>0).
\]
For `Λ^4 C^5`, both strict defects are at least five when `m∈{1,2,3,7,8,9}`.

*Proof.* (T) conflicts with Theorem 5.1. For the alignment bound, the cap rows of `T` vanish, so (A) gives `Σ_{r∈R_cap}ω(|Φ_r|²)≤δ|v|²`. For each `r`, (O) bounds the expectation of the symmetrized invariant `|w_r|²` below by `|v_r|²−√δ`. Its difference from `|Φ_r|²` is half the sum of `[Φ^i,Φ^{i†}]`. Cauchy–Schwarz and (C) bound the sum of their expectation magnitudes by `√(dim W)√δ`. Sum over `r`; for `δ≤1`, use `δ≤√δ`. The charge-four example has dimension five and `d_m≤3` on the listed registers. □

The bound excludes only the strict U-law branch with the stated stabilizer and EW1 reading. It says nothing by itself about `L5-O`, a different transporter reading, or neutral electroweak data.

**Theorem 5.3 (attack checks).** The following do not evade Theorem 5.1: reducible carriers and multiplicities; reversed, repeated, or backtracking paths; and a cross-copy projection of a single-link tensor product. Even the different construction that projects only after forming a path holonomy vanishes for `|q|>d_m` between distinct sites.

*Proof.* Charge spaces are canonical and orthogonal. If a single-link entry has endpoint charges `q_r` and `−q_s`, the sum of end numbers is scalar, so it is zero when `q_r≠q_s`; when the charges agree and exceed `d_m`, Lemma 4.1 kills it. This also handles mixing across copies. Every reverse strict factor is the adjoint of zero; repeated products retain a zero factor. Multiplicity projections are linear combinations of the already zero tensor entries.

For the post-holonomy variant, let `n_ℓ` be the signed number of traversals of each oriented link. Telescoping gives `z′−z=Σ_ℓ n_ℓ(tgt ℓ−src ℓ)`, hence some `n_ℓ≠0`. Each word of the unprojected holonomy tensor has end-number change `±q n_ℓ` on that link. Operators on distinct links commute, so group the word by link without changing the order within any link. The chosen link subword vanishes by Lemma 4.1. Projection cannot restore it. □

The draft's diagnostic examples relax a hypothesis: odd `det^{-1}` permits a nonzero determinant link at `m=5`; `Λ²V` with `v=e_{45}` is not `H`-fixed and has nonzero links for `2≤m≤8`; split paths relax strictness; enlarging the end register changes the law. None is an admissible counterexample to the strict theorem. The rejected same-order reverse convention is also zero in the charge-capacity range, but is not EW1's definition.

## 6. Endpoint networks: construction and limits

**Lemma 6.1 (endpoint capacity).** For `k` distinct links incident at `z`, `E_z=Σ p_{ℓ,z}` has consecutive spectrum of diameter `kd_m`. A nonzero link-only operator of central charge `q` at `z` must act on at least `ceil(|q|/d_m)` incident links. If `|q|>6d_m`, it is zero.

*Proof.* Independent end numbers each take every value in `I_m`, so their sums fill the sum interval. Apply Lemma 4.1. There are six incident links. □

For `|q|=10` the minimum counts at an endpoint are 2 for `m=5`, 3 for `m=4,6`, 4 for `m=3,7`, 5 for `m=2,8`; no link-only operator exists for `m=1,9` because `6d_m=6`. This is a necessary count, not a classification of all networks.

**Proposed C-SPLIT, not adopted.** For each fixed irreducible `W_r`, pin a finite palette of strand representations and isometric intertwiners `J:W_r→⊗_t W_{s_t}`. For a finite translation-covariant path list, define
\[
\mathcal T^J_{\pi_1\cdots\pi_k}=J^T\bigotimes_{t=1}^k\mathcal T^{s_t}_{\pi_t}\,\bar J,
\]
with operator entries multiplied in a fixed order. Form block-diagonal finite convex combinations with strict transports. Reverse by matrix adjoint. Fix the palette independently of `Φ`; allow no interior join or matter factor in this candidate. The path list may vary with block size as specified in `BK1_TREE.md`.

**Lemma 6.2 (split covariance).** C-SPLIT is covariant at its endpoints, invariant elsewhere, and sends identity strand matrices to the identity on `W_r`.

*Proof.* At the first endpoint the strand tensor transforms by `⊗σ_{s_t}(g)^T`. The transpose of `Jσ_r(g)=(⊗σ_{s_t}(g))J` moves this through `J^T`. At the other endpoint use the conjugate intertwining relation and unitarity. Interior factors cancel within each strand. Finally `J^T\bar J=\overline{J†J}=I`. □

**Lemma 6.3 (determinant-square join).** If `1≤a_t≤5` and `Σ_t a_t=10`, there is an isometric intertwiner `J:det_V²→⊗_t Λ^{a_t}V`; likewise for `V̄`.

*Proof.* Use the exterior coproduct `Λ^{a+b}V→Λ^aV⊗Λ^bV` for `a+b≤5`. For `a+b≥5`, with `c=a+b−5`, use `Λ^cV⊗Λ^5V→Λ^aV⊗Λ^bV`, `w⊗vol↦(id⊗∧)(Δ_{a,5−a}vol⊗w)`. Both are equivariant and nonzero, and are injective because their source is irreducible. Iterating them embeds `Λ^{(Σa_t) mod 5}V⊗(Λ^5V)^{⊗floor(Σa_t/5)}` into the tensor product. At total ten this is `det_V²`. Normalize the embedding; Schur's lemma makes its adjoint times itself a positive scalar. These embeddings and the singlet criterion already appear in `LW1_5.md` lines 240 and 250. □

**Theorem 6.4 (nonzero split transport).** For `2≤m≤8`, let `k=ceil(10/d_m)` and choose positive `a_t≤d_m` with `Σa_t=10`: `(5,5)`, `(4,3,3)`, `(3,3,2,2)`, or `(2,2,2,2,2)` for `d_m=5,4,3,2`, respectively. With the join of Lemma 6.3, any `k` pairwise link-disjoint paths without repeated links yield a nonzero split `det_V²` transporter. The conjugate construction works for `det²`. The count `k` meets the endpoint lower bound.

*Proof.* Choose a tensor-basis coefficient `J_A≠0`, with `A=(A_t)`. On each link of strand `t`, put `A_t` at the departing end, choose the remaining `m−a_t` particles outside `A_t` on the two ends, and leave `A_t` empty at the arriving end. This is possible because `a_t≤d_m`. Let the output remove `A_t` at departure and add it at arrival. Theorem 4.3 and adjoint reversal show each strand factor has a nonzero matrix element between these link configurations. Distinct links are independent. The input and output configurations force every internal and external subset index on strand `t` to equal `A_t`; exactly one term survives, with coefficient a nonzero constant times `|J_A|²`. For neighbouring block sites `z′=z+Le_i`, five link-disjoint paths exist: the straight path and the four detours by `±e_j`, `j≠i`. □

**GAP: structural minimality.** Lemma 6.1 proves a lower bound on incident links and Theorem 6.4 attains it with endpoint joins for charge ten on `2≤m≤8`. It does not prove that all minimal networks factor into these strands or that endpoint intertwiners are the unique smallest addition. The draft's test-4 claim that covariance *forces* this join is stronger than its proof. C-SPLIT is a sufficient minimal-count construction, not a proved unique or universally smallest extension.

**Theorem 6.5 (two-sided endpoint capacity).** Let `T` be charge-diagonal and covariant at `z`. Put `Δ=6d_m` for link-only entries, or `Δ=5+6d_m` for general local entries. If `R={r:2|q_r|>Δ}`, then
\[
\|T^\dagger T-I\|^2_{\rm HS}+\|TT^\dagger-I\|^2_{\rm HS}
\ge\left(\sum_{r\in R}\dim W_r\right)I.
\]
The same inequality holds in every state. Link-only matrices covariant at both endpoints and invariant elsewhere are automatically charge-diagonal.

*Proof.* The spectrum of the central generator `E_z` on the six links, or `Q_z=N_z+E_z` with matter, lies in an interval `[e_−,e_+]` of diameter `Δ`. For `q>0`, a charge-`q` entry has `B=P_hi B P_lo`, where `P_lo` projects onto levels `e≤e_+−q` and `P_hi` onto levels `e≥e_−+q`. These projections are orthogonal if `2q>Δ`. Charge diagonality gives `(T†T)_ii=P_lo(T†T)_iiP_lo` for charge-`q` index `i`; row covariance gives `(TT†)_ii=P_hi(TT†)_iiP_hi`. For self-adjoint `X=PXP`, `(X−I)²≥I−P`. Summing the diagonal defect contributions gives at least `2I−P_lo−P_hi≥I` per index. For negative charge exchange the projections. For the final assertion, a link-only entry has zero total central charge because each link's end numbers sum to the fixed scalar `m`; covariance at both endpoints and invariance elsewhere therefore force its row and column charges to agree. □

**Corollary 6.6 (charge ten).** With a charge-`|q|≥10` summand, the two defects sum to at least one for all charge-diagonal covariant transporters on `m∈{1,2,8,9}`, and for link-only endpoint-covariant transporters on `m∈{3,7}`. Thus (T) fails for `δ<1/2`. This count proves no such floor for charge exactly ten on `m∈{4,5,6}`; it also proves no floor for dressed charge-ten operators on `m∈{3,7}`.

*Proof.* Apply Theorem 6.5: `5+6d_m≤17<20` on the first set and `6d_m=18<20` on the second. If both defects are at most `δ`, their sum is at most `2δ`. For `m=4,5,6`, the link-only diameter is at least 24; for dressed `m=3,7` it is 23. These comparisons do not cover `2|q|=20`. □

**Qualification.** For charges larger than ten, Theorem 6.5 can still apply on these registers. The draft's unqualified statement that the theorem gives no floor on `m=4,5,6` must be read for charge exactly ten.

**Theorem 6.7 (saturated first link).** If a block-diagonal transporter's entries on `W_r` all change one endpoint end number by the same `+d_m` or all by `−d_m`, then the sum of defects is at least `dim W_r` and `max(D_+,D_−)≥dim W_r/2`. This includes each charge-ten split of Theorem 6.4 with its minimal strand count and convex combinations whose saturated strands use the same first link with the same sign.

*Proof.* Such entries map one extreme end-number eigenspace to the other and kill all other levels. The two extreme projections are orthogonal. Apply the diagonal-entry argument of Theorem 6.5 to this link. For `d_m=5,4,3,2`, if all `k=ceil(10/d_m)` strand charges were at most `d_m−1`, their sum would be at most `8,9,8,5`, respectively. Thus a strand saturates. Link-disjointness makes its first link carry exactly that change; a convex combination retains it if the link and sign are common. □

At `m=5`, the tree's two determinant paths on one link-disjoint pair satisfy this bound. With `N` links per path and normalization `(5!/c^5)^{2N}=1`, the product is a rank-one partial isometry between the configurations with all path-link particles at their departing ends and all at their arriving ends. A mixture assigning each configuration weight `1/2` gives `D_+=D_−=1/2`. The claim does not bound combinations with different saturated first links or nonsaturated splits.

## 7. Endpoint matter for m=1,9

**Theorem 7.1 (matter necessity and witness).** Let `m=1` or `9`. Suppose an entry `B` of a charge-`q` block is covariant at `z`, `|q|≥10`, and is nonzero. At least one nonzero matter-number-change component at `z` has change `n` satisfying `|q−n|≤6`; hence `n` has the sign of `q` and `|n|≥4`. If the transporter is also covariant with the inverse at `z′` and block-diagonal in that charge, the same conclusion holds there with `q` replaced by `−q`; matter is needed at both endpoints.

For charge `−10` such a nonzero even block exists: define `ψ_u=c_{u,5}c_{u,4}c_{u,3}c_{u,2}c_{u,1}` and `𝒟=J_0^T(⊗_{t=1}^5 𝒯^V_{π_t})\bar J_0`, where `J_0` embeds `Λ^5V` into `V^{⊗5}` and the five paths are link-disjoint as in Theorem 6.4. Then `T_M=ψ_z ψ_{z′}† 𝒟` is nonzero, even, has the required determinant-square endpoint covariance, and is invariant elsewhere. Its adjoint/conjugate gives the opposite charge.

*Proof.* Decompose `B=Σ_n B_n` into spectral blocks of `N_z`. These components retain their total central charge and have link-end charge `q−n`. The link-end generator has diameter `6d_m=6`; Lemma 4.1 forces `B_n=0` unless `|q−n|≤6`. Since `|q|≥10`, every surviving `n` has the stated sign and magnitude. At `z′`, inverse covariance supplies charge `−q`, giving the corresponding opposite-sign conclusion. For the witness, `ψ_z` and `𝒟` each have charge `−5` at `z`; the adjoint matter factor and `𝒟` have charge `+5` at `z′`. The two matter factors contain ten fermion letters and are even together. The single-surviving-term proof of Theorem 6.4 applies to five `a_t=1` strands, also at `m=1,9`, so `𝒟≠0`. The matter product maps the state full at `z` and empty at `z′` to a nonzero state. Matter and links act on independent factors, so the product is nonzero. □

**GAP in draft Proposition G(i).** Covariance at `z` alone cannot imply a conclusion at `z′`: for example an operator supported only near `z` can have the required local charge and have no matter factor at a remote `z′`. Theorem 7.1 adds covariance with the inverse at `z′`; its required matter-number change there has the opposite sign. It also states existence of a surviving component, rather than claiming that every component has one predetermined change.

**Proposed C-SPLIT-M, not adopted.** For `m=1,9`, add to a pinned C-SPLIT palette a fixed site matter multiplet `ψ`, insert `ψ_z^a(ψ_{z′}^b)†` at the endpoints, and use an intertwiner `J:W_r→M⊗⊗_tW_{s_t}`. The witness above proves nonzero charge-ten blocks for one choice. Theorem 6.5 still gives the two-sided floor for charge ten, so this construction does not establish (T).

## 8. Proposed-reading checks and remaining scope

The four tests are the tests in `TOE_ASSEMBLY.md` §3.2. These assessments are proposed; none adopts a reading.

| Reading or candidate | Test 1: target | Test 2: closed | Test 3: downstream premise | Test 4: needed structure |
|---|---|---|---|---|
| C-SPLIT | Pass: asserts no (O), (C), (A), (T), orbit or channel. | Pass if palette, ordering, normalization and finite path lists are pinned independently of `Φ`; fails if chosen after the composite or state. | Pass: no FMS clause is assumed; Theorems 6.5–6.7 show (T) is not automatic. | **Conditional:** the endpoint count proves the number of incident links is necessary and this construction attains it on `2≤m≤8`; it does not prove endpoint-only joins are uniquely necessary. On `m=1,9` this link-only construction has no charge-ten block. |
| C-SPLIT-M at `m=1,9` | Pass. | Pass if the matter multiplet and palette are pinned. | Pass: the two-sided floor remains. | Conditional: endpoint matter is necessary under both-end covariance and yields nonzero blocks, but no near-unitarity follows. |
| Orthogonal irreducible decomposition | Pass. | Pass. | Pass: `W_cap` is canonical and the floor uses orthogonal charge spaces. | Pass: no extra physical structure is needed. |
| H-strict | Description of EW1 Definition 2.3, not a new proposed specification. | — | — | — |

The draft's register summary follows: for charge ten, strict paths vanish for all `m`; C-SPLIT is nonzero on `2≤m≤8`; no link-only charged block exists on `1,9`; the two-sided floor applies to every charge-diagonal transporter on `1,2,8,9`, and every link-only transporter on `3,7`. On `4,5,6`, Theorem 6.7 still bounds the named saturated single splits. These are operator-capacity results, not existence of an FMS state.

**T1-SPLIT remains open.** For fixed `det^{±2}` and a fixed transporter palette, determine whether, for every `δ>0`, some state gives both defects at most `δ`: on `m=4,5,6` for link-only transport; on `m=3,4,5,6,7` when endpoint matter is allowed. Different first links and nonsaturated splits remain available to examine. No owner adoption or downstream phase conclusion follows from the proposed candidates.

The draft also observes that the spin-1 charge-two version of Theorem 6.5 has `D_++D_−≥1`, since its spectral diameter is two and `2|q|=4`; at spin 2 the strict inequality fails. This supplies the elementary bounded rung requested in `BK1_TREE.md` node A1, under the stated covariance. It does not decide that node's larger construction.
