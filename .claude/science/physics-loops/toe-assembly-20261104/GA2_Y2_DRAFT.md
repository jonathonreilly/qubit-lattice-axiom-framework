# GA2 bridge Y2: finite quantum links and T0, pass 1

Written 2026-11-05 by a Claude Opus 5.5 subagent, as a pass-1 lane of the TOE assembly (part GA2, bridge Y2). Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (`check_ga2.py`, output `out.txt`, in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/ga2/`; under 1 s, a few MB, floating point). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (the commit the lane brief names for `claude/toe-assembly`) | `a42c3929cd` |
| `origin/claude/ym4d-hard-route` (read with `git show` only, after `git fetch -q origin`) | `2acf734661` |

Files read at those commits, by line. This folder: `TOE_ASSEMBLY.md` lines 13-23 (axioms), 132-140 (PS-6 with its 2026-11-05 correction), 183 (PS-6r), 369-395 (GA1, GA2), 538-560 (section 6: T0, the lowest rung, the correction, Y1-Y5); `LW1.md` lines 20 and 36-46 (free data, spin-`S` links, Gauss law); `LW1_5_DRAFT.md` lines 152-200 (Lemma Q, Lemma Q4, the hop, Theorem G), 252-262 (Theorem U), 280-320 (section 7, section 8.1), 422-445 (section 10), 510 (inputs); `LW1_5U_DRAFT.md` lines 34 and 230-245 (Proposition T); `LW1_5O_DRAFT.md` lines 39 and 247-262 (Proposition T); `CH1_DRAFT.md` lines 60, 99-104, 328, 379, 403-409 (section 10, rejected candidate 3); `CH1_5_DRAFT.md` lines 1-40 (format). YM branch, folder `.claude/science/physics-loops/ym4d-hard-route-20261030/`: `GOAL.md` lines 8-36 and 60-79 (last changed `2acf734661`); `FINISH.md` lines 1-30 (last changed `2acf734661`); `parts/upper-chain.md` lines 222 and 550, found by grep (last changed `4d58aa4f7f`).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". PS-6r and the axioms are read plainly. Where a word allows two readings, both are named (section 5.3). Nothing is adopted.

**Working set used, by name.** PS-6 and PS-6r (the link registers). PS-5 only through the two five-mode laws of `LW1_5_DRAFT.md` section 8.1. The axioms Lattice and Qubit only in the check of option (b). Results used, cited by name: `LW1.md`'s spin-`S` link (line 37); from `LW1_5_DRAFT.md`, Lemma Q, Lemma Q4, Theorem G, Theorem U, Corollary R.1 (through section 7's table); from `LW1_5U_DRAFT.md` and `LW1_5O_DRAFT.md`, Proposition T; `B5B_DRAFT.md` (through `TOE_ASSEMBLY.md` line 552: the exact frames of `L_cube` are `U(1)`).

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: spectra of similar operators, spectra of `1 ⊗ L − τ ⊗ 1` for commuting self-adjoint parts, the norm bound `‖π(a)‖ ≤ ‖a‖` for representations of C*-algebras, the regular representation of a finite group. Standard mathematics cited, not rebuilt: a closed subgroup of `U(n)` is a Lie group, and a compact Lie group of dimension zero is finite (Corollary N3 only); a continuous one-parameter unitary group on a finite-dimensional space has a Hermitian generator (Corollary N3 only). Literature context, credited from memory and never load-bearing: Kogut-Susskind Hamiltonian lattice gauge theory; quantum link models (Horn; Orland-Rohrlich; Chandrasekharan-Wiese, Nucl. Phys. B 492 (1997)); their `SU(N)`, `SO(N)` and `Sp(N)` forms with embedding algebras `u(2N)`, `so(2N)`, `sp(2N)` and the D-theory construction by dimensional reduction (Brower-Chandrasekharan-Wiese, Phys. Rev. D 60 (1999); Brower-Chandrasekharan-Riederer-Wiese, Nucl. Phys. B 693 (2004)); lattice gauge theories with finite subgroups of `SU(2)` (Petcher-Weingarten; Bhanot-Rebbi). None of these is used as a proof step.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 552: "Their link registers are finite quantum links (PS-6r), not group-valued Wilson links. Whether that sector is in T0's class is bridge Y2."

Line 556: "**Y2, the RG domain.** `S_fw` lies in the domain of the hard-core block RG (Balaban's class as rebuilt on the branch), or the hard core's bounds extend to `S_fw`. T0 is stated for the Wilson action."

PS-6r, line 183: "Each link register is a finite quantum link: a finite-dimensional register on which the frame group of the site content acts, with the raising and lowering structure the Gauss law needs. Link registers carry odds but no actual configuration and no records."

**T0's hypotheses, quoted exactly.** `GOAL.md` line 22: T0 is "the existence clause of the Clay problem without the mass gap, for SU(2) first: a non-trivial quantum Yang-Mills theory on R^4 whose Euclidean correlations satisfy the Osterwalder-Schrader axioms strongly enough to reconstruct a Wightman theory". The same line fixes the lattice theory: "The outline's Theorem 0 (SA lines 66-130) states this for the tr(F^2) sector of Wilson SU(2)." It is provisional: "When the write-up appears, pin T0 to its statement (gauge group, observables, axioms) and record any difference here." Line 26, the milestone T1: "SU(2) lattice Yang-Mills with the Wilson action has a non-trivial, reflection-positive, hypercubic-invariant limit on R^4 as the spacing goes to zero ... along a coupling trajectory the proof chooses." Line 24, the extension: "more observables, and SU(N)."

**Which lattice action and which link space.** `GOAL.md` names "Wilson SU(2)" but does not write out the action or the link space. `parts/upper-chain.md` line 222 does: "Dyadic lattices. a = 2^-n, L = 2^M, Lambda = (aZ/LZ)^4 ... Links carry U_b in SU(2), Haar probability measure. For a plaquette p, s_p = 1 - (1/2) Tr U_p ... W = sum over the 6|Lambda| plaquettes of s_p. The law is d mu_beta = Z(beta)^-1 exp(-beta W) prod dU_b." So the Euclidean link variables are elements of `SU(2)` with Haar measure, and the action is Wilson's. The Hilbert space of the transfer is fixed by line 550: "Let Y be the links of one time slice with Haar measure, and T_1 the one-step kernel". So the transfer acts on `L^2` of the slice links with Haar measure, that is `⊗_b L^2(SU(2))`, and the link variable `U_b` acts there as a multiplication operator. These are the hypotheses item 1 tests.

**The interface.** `GOAL.md` line 70-71, UV-CT: "**CT1-CT3, sources.** A bound with an analytic local counterterm E(w) at reflection-periodic complex plaquette sources ... **CT4, volume.** log Z_L(beta) >= (L/P)^4 log Z_Tor(beta) - c_F (L/a_*)^4", and line 73: "All constants are independent of a and L." `FINISH.md` line 11: "**Existence is not proved.**" A grep of `GOAL.md` and `FINISH.md` at `2acf734661` for "universal", "quantum link" and "initial action" finds nothing: the YM branch states no result for other lattice actions or for quantum links.

## 0.1 Outcome in one paragraph

**Item 1 is proved, in a stronger form than asked.** Take any Hilbert space, a bounded self-adjoint generator `L`, a Hermitian matrix `τ ≠ 0`, and an `n × n` matrix `𝐔` of bounded operators that is covariant: `[1 ⊗ L, 𝐔] = (τ ⊗ 1)𝐔` (or `𝐔(τ ⊗ 1)`). Then `𝐔` is not invertible (Theorem N). The proof compares the top and bottom of two spectra. Entries need not commute. Unitarity is not needed: invertibility is already excluded. Every finite register has bounded generators. So no finite register carries a group-valued link for any group with infinite image `ρ(G)`, non-abelian or `U(1)` (Corollaries N1-N3). For finite `ρ(G)` such links exist (Proposition N4). Even for large registers, `‖𝐔^†𝐔/c − 1‖ ≥ 1` for every `c > 0`. So a finite register never comes close to a unitary link in operator norm. **The result holds at every scale of the framework.** The law's site Gauss generators are bounded in every representation of its quasi-local algebra. So no link variable at any scale (fine link, block link, quasi-local or weak-closure operator) is both invertible and exactly covariant under the law's own gauge transformations at a site (Corollary N5). Quantum links satisfy covariance with non-commuting entries whose brackets are gauge generators (Lemma Q (Q2)-(Q3)). Their matrix `𝐔` is singular; on rishon registers it factors through one register, so its rank is at most `1/n` of full (Proposition R). **Y2.** T0 as stated applies to no PS-6r law at any register size (Corollary Y2-0). Y2's first clause cannot hold with link operators. Y2 can hold only as a universality statement about gauge-invariant correlators. **Options.** (a1) A large-register limit exists inside the free data of `L5-O` and `L_cube`, not of `L5-U`. It never converges in norm, and one law has one register. (a2) D-theory needs a fifth direction with gauge frames at every layer point, which the Lattice axiom does not supply as read plainly. (b) `L^2(G)` links conflict with PS-6r. They conflict with Qubit under one reading, not the other, and fail tests 1 and 3. (c) Emergence under ZM1 needs no change of spec. By Corollary N5 it can only work at the level of correlators or Euclidean integration variables. **Statement handed to the YM programme:** T0-start (with T0-rate): the hard core's bounds and T0's conclusions hold from any initial action in the hard core's own inductive class at small coupling, with constants independent of that action. This is not claimed. **Per law.** `L_cube`: `U(1)` spin-`S` quantum links; no T0 needed (GA2's abelian clause). `L5-U`: `U(5)` quantum links with embedding algebra `u(10)`, fixed register of dimension `C(10, m) ≤ 252`; needs T0-start for `SU(5)`. Its first open item is Y2-W (whether the free constants reach small coupling at all). `L5-O`: `Spin(10)` quantum links with embedding algebra `so(20)`, any finite register; needs T0-start for `SO(10)`, a group outside the branch's "SU(N)" extension.

---

## 1. Conventions

**Link matrices.** An `n × n` matrix of bounded operators `U^{ab}` on a Hilbert space `H` is the same thing as one bounded operator `𝐔 = Σ_{ab} E_{ab} ⊗ U^{ab}` on `C^n ⊗ H`. "Unitary" for a link means `𝐔^*𝐔 = 𝐔𝐔^* = 1` in this sense, that is `Σ_c U^{ca*}U^{cb} = δ_{ab}` and `Σ_c U^{ac}U^{bc*} = δ_{ab}`. "Entrywise commuting" means that all `U^{ab}` and `U^{cd*}` commute.

**Covariance.** Let `ρ` be a unitary representation of a group `G` on `C^n` and `V` a unitary representation of `G` (one end of the link) on `H`. Left covariance: `(1 ⊗ V(g)) 𝐔 (1 ⊗ V(g))^* = (ρ(g) ⊗ 1) 𝐔`. Right covariance: `(1 ⊗ V(g)) 𝐔 (1 ⊗ V(g))^* = 𝐔 (ρ(g)^{-1} ⊗ 1)`. A Wilson link has both, one for each end, with `U → g_x U g_y^{-1}`. At the Lie algebra level, with `V(e^{tX}) = e^{itL}` and `ρ(e^{tX}) = e^{itτ}` (`L`, `τ` Hermitian):

\[
\text{(left)}\quad [1\otimes L,\ \mathbf U]=(\tau\otimes 1)\,\mathbf U,\qquad
\text{(right)}\quad [1\otimes L,\ \mathbf U]=-\,\mathbf U\,(\tau\otimes 1). \tag{1.1}
\]

Signs and the choice of `g` or `g^{-1}` do not matter below, because `τ` ranges over a real vector space closed under `τ → −τ`.

**The Wilson link realizes both relations.** On `L^2(G)` with `V_L(g)f(u) = f(g^{-1}u)` and `(U^{ab}f)(u) = ρ(u)_{ab}f(u)`: `V_L(g)U^{ab}V_L(g)^{-1}` multiplies by `ρ(g^{-1}u)_{ab}`, so left covariance holds with `ρ(g)^{-1}`. The entries commute, and `𝐔` is unitary pointwise. The generators `L` are first-order differential operators. For `G` with `dρ ≠ 0` they are unbounded on `L^2(G)`. Theorem N shows that this unboundedness is necessary.

## 2. Item 1: no finite register carries a group-valued link

**Theorem N (spectral obstruction).** Let `H ≠ 0` be a Hilbert space, `L` a bounded self-adjoint operator on `H`, `τ` a Hermitian `n × n` matrix, and `𝐔` a bounded operator on `C^n ⊗ H` that satisfies the left or the right relation (1.1). If `𝐔` has a bounded inverse, then `τ = 0`.

*Proof.* Left case. The relation reads `(1 ⊗ L − τ ⊗ 1)𝐔 = 𝐔(1 ⊗ L)`. Put `A = 1 ⊗ L − τ ⊗ 1` and `B = 1 ⊗ L`. Then `A = 𝐔 B 𝐔^{-1}`, so `λ − A = 𝐔(λ − B)𝐔^{-1}` for every `λ ∈ C`. So `A` and `B` have the same spectrum. Diagonalize `τ = W diag(λ_1, …, λ_n) W^*` with `W` unitary. Then `(W^* ⊗ 1) A (W ⊗ 1) = ⊕_{a=1}^n (L − λ_a)` and `(W^* ⊗ 1) B (W ⊗ 1) = ⊕_{a=1}^n L`. So `spec A = ∪_a (spec L − λ_a)` and `spec B = spec L`. Both are compact subsets of `R`, non-empty because `H ≠ 0`. Their maxima: `max spec L − min_a λ_a = max spec L`, so `min_a λ_a = 0`. Their minima: `min spec L − max_a λ_a = min spec L`, so `max_a λ_a = 0`. A Hermitian matrix whose eigenvalues all vanish is zero. Right case: the relation reads `(1 ⊗ L)𝐔 = 𝐔(1 ⊗ L − τ ⊗ 1)`, so `1 ⊗ L − τ ⊗ 1 = 𝐔^{-1}(1 ⊗ L)𝐔`, and the same comparison applies. ∎

Every step is finite linear algebra when `dim H < ∞`: similarity preserves eigenvalues, and the eigenvalues of `L − λ_a` are those of `L` shifted. That is the case the framework needs first.

**Corollary N1 (finite registers, non-abelian or not).** Let `R ≠ 0` be finite-dimensional, with a representation of a Lie algebra `𝔤` by Hermitian operators `L^X` and a representation `X ↦ τ^X` of `𝔤` by Hermitian `n × n` matrices, not identically zero. No `n × n` matrix of operators on `R` that satisfies (1.1) for all `X` is invertible. In particular none is unitary, and none is an entrywise-commuting unitary. On a finite-dimensional space, `𝐔^*𝐔 = 1` alone already forces invertibility, so `U^†U = 1` alone is excluded.

*Proof.* Choose `X` with `τ^X ≠ 0`. Every operator on `R` is bounded. Apply Theorem N. ∎

**Corollary N2 (`U(1)`).** No nonzero finite register carries an invertible operator `U` with `[E, U] = qU`, `E` Hermitian, `q ≠ 0`. In particular none carries a unitary that `E` shifts by one.

*Proof.* `n = 1`, `τ = q`. Directly: `U^{-1}EU = E − q`, and the largest eigenvalue of the right side is smaller than that of the left. ∎

LW1's spin-`S` link fits this. `LW1.md` line 37: "`J_ℓ|m⟩=\sqrt{S(S+1)-m(m+1)}|m+1⟩`, with the last expression zero at `m=S` ... Thus `[E_ℓ,J_ℓ]=J_ℓ`." So `J_ℓ` kills `|S⟩` and is not invertible, as Corollary N2 requires. [check] (3): rank `J = 2S` of `2S + 1` for `S = 1/2, 1, 3/2, 5`.

**Corollary N3 (group form).** Let `G` be a compact Lie group, `ρ` a continuous unitary representation on `C^n` with `ρ(G)` infinite, and `V` a continuous unitary representation on a finite-dimensional `R ≠ 0`. No `𝐔` on `C^n ⊗ R` that is left or right covariant for all `g ∈ G` is invertible.

*Proof.* `ρ(G)` is a closed subgroup of `U(n)`, hence a compact Lie group (cited). It is infinite, so its dimension is positive (cited), so `dρ(X) ≠ 0` for some `X ∈ 𝔤`. Write `V(e^{tX}) = e^{itL}` and `ρ(e^{tX}) = e^{itτ}` (cited, finite dimension). Differentiate covariance at `t = 0`: `i[1 ⊗ L, 𝐔] = i(τ ⊗ 1)𝐔` (left case). Theorem N gives `τ = 0`, a contradiction. ∎

This covers `SU(2)`, `SU(N)`, `SO(N)`, `Spin(N)`, `U(N)` and `U(1)` in every representation with `dρ ≠ 0`.

**Proposition N4 (the converse: finite image).** If `K = ρ(G)` is finite, the register `R = L^2(K) = C^{|K|}` carries an entrywise-commuting unitary link, covariant at both ends.

*Proof.* Let `G × G` act by `(V(g, h)f)(k) = f(ρ(g)^{-1} k ρ(h))` and let `(U^{ab}f)(k) = k_{ab} f(k)`. The `U^{ab}` are multiplication operators, so they commute with each other and with their adjoints. At each `k` the matrix `(k_{ab})` is unitary, so `𝐔` is unitary. `(V(g,h)U^{ab}V(g,h)^{-1}f)(k) = (ρ(g)^{-1}kρ(h))_{ab} f(k)`, which is covariance at both ends. ∎

So the obstruction is exactly continuity of the gauge group's image. Section 5.5 records what Proposition N4 offers and why it does not reach T0.

**Corollary N3' (no approach in operator norm).** On a finite register, for every `c > 0`, every `𝐔` as in Corollary N1 satisfies `‖𝐔^*𝐔 − c‖ ≥ c`, that is `‖𝐔^*𝐔/c − 1‖ ≥ 1`.

*Proof.* `𝐔` is not invertible, and the space is finite-dimensional, so `𝐔^*𝐔 ≥ 0` has eigenvalue `0`. Then `𝐔^*𝐔 − c` has eigenvalue `−c`. ∎

So no sequence of finite registers, of any size, converges to a unitary link in operator norm. A large-register limit can only converge on a restricted class of states (for spin `S`, on states of bounded `|E|`), never uniformly.

**Corollary N5 (the framework, at every scale and in every representation).** Let a PS-6r law have exact gauge group `G` with Gauss generators `𝒢_x^T`, `T ∈ 𝔤` (`LW1.md` line 45 for `L_cube`, Theorem G for `L5-O`, Theorem U for `L5-U`). Each `𝒢_x^T` is a self-adjoint element of the quasi-local algebra `𝔄`, supported on site `x` and its six link ends. Let `π` be any representation of `𝔄` on a Hilbert space `K` (a finite box, the GNS space of any state, any volume). Let `𝔥 ⊂ 𝔤` be a subalgebra (for example `su(2)`) and `T ↦ τ^T` a representation of `𝔥` by Hermitian `n × n` matrices, not identically zero. Then no bounded operator `𝐔` on `C^n ⊗ K` with `[1 ⊗ π(𝒢_x^T), 𝐔] = (τ^T ⊗ 1)𝐔` for all `T ∈ 𝔥` (or the right form) is invertible.

*Proof.* `‖π(𝒢_x^T)‖ ≤ ‖𝒢_x^T‖ < ∞`, because `𝒢_x^T` lies in a finite-dimensional matrix algebra and representations of C*-algebras do not increase norms. Choose `T` with `τ^T ≠ 0` and apply Theorem N. ∎

A block link of a block-spin RG, in Balaban's sense, is covariant under the gauge transformations at the block's end sites. Those are gauge transformations of the law at fine sites. So Corollary N5 covers block links at every scale. What it does not exclude: (i) gauge-invariant observables, such as traces of products of link matrices around loops, and equality of their correlators with Wilson's; (ii) group-valued variables of integration in a Euclidean representation of the law (section 4.2); (iii) approximate unitarity in a state, `‖(𝐔^*𝐔 − c)ψ‖` small for the relevant `ψ`. Each of these is a statement about states or correlators, not about operators.

**Remark (the gauge actions themselves are inequivalent).** In T0's transfer space `⊗_b L^2(SU(2))`, the Gauss generator at a site is a sum of left and right generators on six links. It is unbounded: its spectrum contains the weights of every spin. The framework's `π(𝒢_x^T)` is bounded. A unitary equivalence preserves boundedness. So no unitary map intertwines the two gauge actions at a site, at any register size. Theorem N says more: it excludes the link variable, whatever the identification of generators.

## 3. What quantum links satisfy instead

**Lemma Q's relations, quoted.** `LW1_5_DRAFT.md` (Q2): "`[L_x^{cd},U^{ab}]=i(\delta_{db}U^{ac}-\delta_{cb}U^{ad})`, `[L_y^{cd},U^{ab}]=i(\delta_{da}U^{cb}-\delta_{ca}U^{db})`, `[L_x^{cd},L_y^{ef}]=0`". (Q3): "The `U^{ab}` generate `𝔨` as a Lie algebra: `[U^{ab}, U^{cb}] = −4iL_y^{ac}` for `a ≠ c`, and `[U^{ab}, U^{ad}] = −4iL_x^{bd}` for `b ≠ d`." A register is "a finite-dimensional unitary representation `ρ` of `𝔨`".

So a quantum link has three properties. (Q-cov) It is covariant at both ends: (Q2) is the right relation (1.1) at `x` with `(τ^{cd})_{eb} = i(δ_{db}δ_{ec} − δ_{cb}δ_{ed})`, a nonzero Hermitian matrix with eigenvalues `±1, 0`, and the left relation at `y`. (Q-nc) Its entries do not commute; their brackets are the end generators (Q3). (Q-sing) Its matrix `𝐔` is singular on every register (Corollary N1). The same holds for `L5-U`'s rishon links (`LW1_5_DRAFT.md` Theorem U: "`U_ℓ^{jk} = r^{ℓ,y}_j r^{ℓ,x†}_k`", covariant under the `u(5)` end generators `Σ r^†Tr`) and for `L_cube`'s spin-`S` link (`[E, J] = J`).

**The failure of unitarity has a fixed form.** For the `so(2N)` rishon register (`η` Hermitian, `U^{ab} = iη^y_aη^x_b`, so `U^{ab*} = U^{ab}`):

\[
(\mathbf U^*\mathbf U)^{ab}=\sum_c U^{ca}U^{cb}=N\,\delta_{ab}+(1-\delta_{ab})\,N\,\eta^x_a\eta^x_b
= N\big(\delta_{ab}-2i(1-\delta_{ab})L_x^{ab}\big). \tag{3.1}
\]

*Proof.* `(iη^y_cη^x_a)(iη^y_cη^x_b) = −η^y_cη^x_aη^y_cη^x_b = η^y_cη^y_cη^x_aη^x_b = η^x_aη^x_b`; sum over `c`; `η^x_aη^x_a = 1`; `η^x_aη^x_b = −2iT_{10+a,10+b}` for `a ≠ b`. ∎ So `𝐔^*𝐔` is `N` times one plus an `x`-end generator term, not `N` times one. For rishons of `U(N)`, `(𝐔^*𝐔)^{kl} = Σ_j r^x_k r^{y†}_j r^y_j r^{x†}_l = r^x_k N^y r^{x†}_l`, with `N^y` the `y`-end rishon number. For spin `S`, `J^†J = S(S+1) − E(E+1)`. In each case `𝐔^*𝐔` is a function of the end generators. [check] (1): (3.1) holds for `N = 2, …, 5`.

**Proposition R (rishon links factor through one register).** On the rishon register of `so(2N)` (`R = C^{2^N}`), `𝐔 = iAB` with `A: R → C^N ⊗ R`, `Av = Σ_a e_a ⊗ η^y_a v`, and `B: C^N ⊗ R → R`, `B(e_b ⊗ v) = η^x_b v`. So `rank 𝐔 ≤ dim R`, which is `1/N` of `dim(C^N ⊗ R)`. On the half-spinor register `S_+`, `𝐔` factors through `S_−` (each `η` exchanges `S_+` and `S_−`), so again `rank 𝐔 ≤ dim S_+`. For `U(N)` rishons in the sector of `m` rishons, `𝐔 = AB` with `B = Σ_k e_k^* ⊗ r^{x†}_k` (sector `m` to `m + 1`) and `A = Σ_j e_j ⊗ r^y_j` (back to `m`), so `rank 𝐔 ≤ C(2N, m+1)`.

*Proof.* Multiply out: `(AB)(e_b ⊗ v) = Σ_a e_a ⊗ η^y_aη^x_b v`, whose `(a, b)` entry is `η^y_aη^x_b`. The rank of a product is at most the dimension of the space it passes through. ∎

[check] (1), (2): for `so(2N)`, `N = 2, …, 5`, the rank is exactly `dim R` on `C^{2^N}` (kernel `128/160` at `N = 5`) and exactly `dim S_+` on `S_+`; for `U(2)`, `U(3)` rishons in every sector, the rank is at most `C(2N, m+1)`. So on rishon registers the defect is not a small corner (as for spin `S`, one state of `2S + 1`). It is most of the space. On `L5-O[S_+]`, `𝐔` is `5120 × 5120` with rank at most `512`.

**Answer to item 1.** Proved. No finite register, and no representation of the framework's quasi-local algebra in which the gauge action at a site comes from the law's own Gauss generators, carries an invertible link matrix that is covariant for a gauge group with infinite image. This holds for non-abelian `G` and for `U(1)`, with or without commuting entries. What quantum links satisfy instead is covariance (Q2) with non-commuting entries (Q3), and a singular `𝐔` whose `𝐔^*𝐔` is a function of the end generators ((3.1), Proposition R).

## 4. Consequence for Y2

### 4.1 T0 as stated applies to no PS-6r law

**Corollary Y2-0.** For no PS-6r law, at any finite register size, is the gauge sector Wilson's lattice gauge theory. That holds for the full gauge group and for every closed subgroup of positive dimension, `SU(2)` included.

*Proof.* T0's lattice theory, as quoted in section 0, has link variables `U_b ∈ SU(2)` with Haar measure. Its transfer acts on `⊗_b L^2(SU(2))`, where `U_b` is an invertible, covariant multiplication operator. By Corollary N5, the law's algebra, in any representation, contains no invertible operator matrix that is covariant under the law's Gauss generators for `SU(2)` (or any subalgebra with `τ ≠ 0`). An identification of the two lattice theories would carry `U_b` to such an operator. ∎

So the section 6 sentence (line 550) "That is T0's theory up to bridges Y1-Y3 below" holds on no PS-6r law, even after the 2026-11-05 correction. Y2's first clause, "`S_fw` lies in the domain of the hard-core block RG", cannot hold with the law's link operators as the RG's variables. It can hold only with variables of a Euclidean representation (section 4.2) or emergent ones. Y2's second clause, "or the hard core's bounds extend to `S_fw`", has to be read as a statement about gauge-invariant correlators: a **universality** statement. Suggested wording for the lead, not made here: "Y2, universality. The framework's gauge-invariant correlators at scales `≥ a_k` equal those of a theory in the hard core's domain, up to errors the hard core's bounds absorb."

### 4.2 Group-valued variables are still available in a Euclidean form

Corollary N5 excludes operators, not integration variables. Suppose a register `R`, as a representation of `G × G` (the two ends), is a direct sum `⊕_{j ∈ J} V_j ⊗ V_j^*` with each type at most once. By Peter-Weyl, `R` is then a `G × G`-invariant subspace of `L^2(G)` (cited). With `P` the projection onto `R`, a transfer `T` on registers becomes `P T P` on `L^2`, with a kernel `K(g, g')` in group variables. For `L_cube` with integer `S`, the spin-`S` register is the band `{e^{ikθ}: |k| ≤ S}` of `L^2(U(1))`. The kernel is band-limited (finite `J`) and is not Wilson's `exp(−β W)`. It need not be positive. Whether such a kernel lies in the hard core's domain is part of Y1 and Y2 together. This draft does not attack it. It records that the identification of variables is possible and the identification of operators is not.

### 4.3 The options

The four tests (`LW1_5_DRAFT.md` line 328): "(1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need." Nothing below is proposed. Each row records what a choice would do.

**(a1) A large-register limit.** A family of laws `L[R_k]` with registers whose size grows, and a joint limit in `k`, `a` and the constants. Inside the free data: `L_cube` has "The link spin is `S ∈ {1/2, 1, 3/2, …}`" (`LW1.md` line 20), and `L5-O` has "`R_ℓ = R`, a finite-dimensional unitary representation of `𝔨 = so(20)` ... Free datum" (`LW1_5_DRAFT.md` section 8.1 item 2). `L5-U` has no such datum: its register is ten rishon modes in a sector `1 ≤ m ≤ 9`, of dimension `C(10, m) ≤ 252`. Two facts limit (a1). By Corollary N3', the approach to Wilson links is never in operator norm, only on states of bounded flux. And one law has one register (AS0: "every part must hold for the same law"), so GA2 would hold with an error that depends on `R`, never exactly. What the YM programme would need: **T0-QLR[G]**, T0's clauses for the limit of quantum-link transfers along a trajectory `(a_i, R_{k_i}, constants_i)` chosen by the proof, with the limit equal to T0's theory. For GA2 it would also need the rate form with an `R`-dependent error. The hard core works with Haar measure and a split into large and small fields of group-valued links, so T0-QLR is not in its current domain. That is the reason (c) is preferred below.

**(a2) D-theory (Chandrasekharan-Wiese; Brower-Chandrasekharan-Wiese; credited from memory, unchecked, not load-bearing).** As recalled: a quantum link model with fixed finite registers in one more dimension, in a massless phase there, reduces to four-dimensional Yang-Mills as the extent `L_5` of the extra direction grows, with the 4D coupling set by `L_5`. Nothing of it is rebuilt here. What the YM programme would need: **T0-D[G]**, for the `(4+1)`-dimensional quantum link model of `G` with fixed registers on `aZ^4 × {1, …, L_5}`: along a trajectory with `L_5 → ∞` and `a → 0`, the gauge-invariant correlators at separated points of `R^4` converge, the limit meets T0's clauses, and it is T0's theory. The TOE side would need a fifth direction. The construction needs gauge frames at every layer point (the extra-direction links carry quantum links with their own Gauss laws). So layer points are sites in PS-6's sense. The Lattice axiom reads: "Physical sites are the points of the cubic lattice `Z^3`". Read plainly, it gives no layer index. A layer index inside each site changes the site content (Qubit, PS-5). A layer index inside the link registers alone gives no frames at layer points. Also, the four Euclidean directions of D-theory are spatial directions of its Hamiltonian; the framework's four are three of space and the tick. So (a2) is axiom-level. Tests: (1) fails (the layers are chosen because they yield T0's class); (2) passes if `L_5` is fixed, fails if "large"; (3) passes; (4) fails (a direction whose only reason is the plug-in). Recorded, not proposed. One remark, not used: in Brower-Chandrasekharan-Wiese the quarks of D-theory are domain-wall fermions on the boundary of the extra direction, so (a2) would also touch CH1.

**(b) Relax PS-6r's finiteness.** Make each link register `L^2(G)` (Kogut-Susskind links), with `G` the law's frame group. By Theorem N, this is the smallest change that admits exact group-valued link operators: the Gauss generators must be unbounded. Axiom check, two readings, both named:
- *Reading R-S (link registers are made of site content, for example cells of qubits).* Then every register is finite-dimensional, and (b) conflicts with Qubit ("The full one-site possibility domain has algebraic presentation `M_2(C)`"). `CH1_DRAFT.md` line 379 argues the same way for rotors: "A cell of qubits cannot host them either".
- *Reading R-X (link registers are PS-6's own structure, not site possibilities).* Qubit speaks of sites ("Each site has a domain of local possibilities"), and PS-6 adds "a register that transports frames between its two sites". Under R-X, Qubit is silent on links, and (b) conflicts only with PS-6r's words "a finite-dimensional register".
Lattice: no conflict under either reading (links are not sites). Record ("Link registers carry ... no records"): no conflict. Tests: (1) fails if its reason is T0 alone. It has a second reason: `CH1_DRAFT.md` Attack 3 needs "infinite-dimensional rotor degrees of freedom", with "a winding integer per link". Section 10's rejected candidate 3 rejects exactly this: "Admit rotor (infinite-dimensional) site or link content ... It conflicts with Qubit and PS-6r ... and its reason would be one construction (test 4)". With two reasons, test 1 is conditional. (2) passes (`L^2(G)` for the named `G`). (3) fails in part: it settles by premise the link-space half of Y2, a GA2 question. (4) passes (its reason needs exactly that). Even under (b), Y2 is not met: the update's Euclidean action is not Wilson's isotropic action (Y1, Y3). So (b) would still need T0-start below. Owner decision; recorded, not proposed.

**(c) Emergence under ZM1.** No change of spec: the law stays as it is, and the zoom (ZM1) must produce, at some scale `a_{k_0} = L^{k_0} a`, an effective theory in the hard core's domain. Tests: not a spec, so all four pass trivially. Corollary N5 fixes the form. The effective group-valued links cannot be operators covariant under the law's Gauss generators. They must be Euclidean variables (section 4.2) or emergent variables of a limit, and the agreement must be about gauge-invariant correlators. The split:
- *TOE side, ZM1-G (the TOE's own item, not handed):* at scale `a_{k_0}`, the framework's gauge-invariant correlators (loop traces of the quantum-link matrices, and the `tr F^2`-type composites built from them) equal those of a gauge-invariant, reflection-positive measure `μ` on `G`-valued links of `a_{k_0}Z^4`, up to an error `ε_{k_0}` small in the hard core's norms, with `μ`'s density in the hard core's class at step `k_0`. This contains Y1, Y3 and Y4 for the gauge sector.
- *YM side:* **T0-start** and **T0-rate**, stated in the FINISH block. This is what Y2's second clause already asks, in the form T0 uses.

The hard core is an induction over scales. Its inductive hypothesis at step `k` is a class of effective actions. T0-start asks that the induction may begin at any member of that class at small coupling, with constants independent of the member. Whether the branch's proof gives this is for that programme to say; nothing here claims it.

**(d) Finite-subgroup links (Proposition N4).** For a finite `K ⊂ SU(2)`, for example the binary icosahedral group of order 120, `L^2(K)` is a finite register with exact `K`-valued Wilson links. PS-6r asks that "the frame group of the site content acts" on the register. With `K`-valued links only `K` stays exact, so the law's exact group would be `K`, not the continuous frame group. Tests: (1) fails; (3) fails (it settles GA1's group by premise). T0 is not stated for finite groups. Recorded, not proposed.

**Answer to item 2.** T0 applies to no PS-6r law at any finite register size (Corollary Y2-0). (a1) exists inside `L_cube` and `L5-O`, never converges in norm, and gives GA2 only with a register-dependent error. (a2) is axiom-level (Lattice, read plainly). (b) is axiom-level: it conflicts with PS-6r, and with Qubit under R-S only. (c) needs no change of spec, and Corollary N5 fixes its form. The statement the TOE would hand to the YM programme is T0-start with T0-rate. None of them is claimed to hold.

## 5. Item 3: the three laws as quantum-link models

### 5.1 `L_cube`

Gauge group: `U(1)` per site (`TOE_ASSEMBLY.md` line 552: "There a site is one fermion mode, and its exact frames are `U(1)`"). Links: spin-`S` `U(1)` quantum links (`LW1.md` line 37), embedding algebra `u(2) ⊃ u(1) ⊕ u(1)` (`LW1_5_DRAFT.md` Lemma Q, examples: "`LW1`'s spin-`S` link is the one-mode case of the `U(N)` family of the same construction"). At `S = 1/2` it is the rishon link of `L5-U` at one mode. By Corollary N2, `J` is never invertible. As `S` grows it approaches Kogut-Susskind's `U(1)` on states of bounded `|E|` (Corollary N3'). **Yang-Mills plug-in:** none. `L_cube` has no non-abelian gauge group, and GA2(a) treats the abelian factor apart: "For the abelian factor, the corresponding statement holds as an effective lattice theory at scales above `a`, with no `a -> 0` limit required". The statement it needs is GA2's abelian clause for the spin-`S` `U(1)` quantum link in 3+1D (a Coulomb phase with a massless photon), not T0.

### 5.2 `L5-U`

Gauge group `U(5)` (`LW1_5_DRAFT.md` Theorem U). Links: ten rishon modes per link (five at each end), in the sector of `m` rishons, `1 ≤ m ≤ 9`: register `Λ^m(C^{10})`, of dimension `C(10, m) ≤ 252`. As a quantum-link model, it is the `U(5)` quantum link with embedding algebra `u(10)` (the `U(N)` form, credited above): `U^{jk} = r^y_j r^{x†}_k` are the off-diagonal block of `u(10)`, and the end generators `Σ r^†Tr` the diagonal blocks. The exact `SU(2)`: `LW1_5U_DRAFT.md` Proposition T, "every closed `H ⊂ U(5)`, in particular `SU(2)`, has an exact Gauss law at every angle", with (iii): "the link variables `U^{jk}_ℓ` split into a `(2, 2)` block (`j, k ∈ {4, 5}`), two doublet blocks (one index in `{4, 5}`), and an `SU(2)`-singlet block". The `(2,2)` block alone would be an `SU(2)` quantum link with embedding `u(4)`, but the hop contains every block. So the exact `SU(2)` is a subgroup of a `U(5)` quantum-link model, not an `SU(2)` model. By Corollary N5 with `𝔥 = su(2)`, even the `(2,2)` block is singular. **Named statement for the plug-in:** T0-start for `SU(5)` (on the branch's path: `GOAL.md` line 24, "and SU(N)"), with matter (Y4), and ZM1-G for `SU(5)`. Or, after `U(5)` breaks (EW1/VC1), T0-start for the `SU(2)` and `SU(3)` factors. **First open item, Y2-W:** the register has fixed dimension, so the law has no register-size knob. GA2(a) needs the window `a << r << Λ_i^{-1}`, that is a small coupling at some scale. Whether any value of `L5-U`'s free constants (angles, `τ_E`, the open plaquette class) gives such a window is not known. The D-theory literature, as recalled and not load-bearing, gets its small 4D coupling from the extent of the extra direction, not from a fixed 4D register. Not attacked in this pass.

### 5.3 `L5-O`

Gauge group `Spin(10)` on states, `SO(10)` on the algebra (`L5-O[S_+]`, `LW1_5_DRAFT.md` section 7). Links: any finite-dimensional unitary representation `R` of `so(20)`, proposed `S_+` (dimension 512). As a quantum-link model, it is the `SO(10)` quantum link with embedding algebra `so(20)` (Lemma Q, "the embedding algebra is `so(2N) = so(20)`"). `U^{ab}` is Hermitian and transforms as `(10, 10)`, so the Wilson analogue is an `SO(10)`-valued link (real orthogonal matrices), on which `−1 ∈ Spin(10)` acts trivially. On `S_+`, `𝐔` is `5120 × 5120` with rank at most 512 (Proposition R). The exact `SU(2)`: `LW1_5O_DRAFT.md` Proposition T(iii)-(iv), `SU(2)_W` "is an exact gauge subgroup ... with its own Gauss law" and "`L5-O` does not contain T0's pure `SU(2)` Yang-Mills as a sector", since "the hop (4.1) also contains the other blocks, which mix the two sets of indices". **Named statement for the plug-in:** T0-start for `SO(10)` (or its `Spin(10)` form), with matter, and ZM1-G for `SO(10)`. `LW1_5O_DRAFT.md` Proposition T: "`Spin(10)` is a simple group outside the `SU(N)` family, so that path does not reach it as stated." Unlike `L5-U`, `L5-O` has a register-size knob (the highest weight of `R`), so (a1) is available inside the law's free data, with Corollary N3' as its limit.

**Answer to item 3.** `L_cube`: `U(1)` spin-`S` quantum links; no T0 needed. `L5-U`: `U(5)` quantum links with `u(10)` embedding and a fixed register; T0-start for `SU(5)`; first open item Y2-W. `L5-O`: `SO(10)` quantum links with `so(20)` embedding and any register; T0-start for `SO(10)`, outside the branch's planned path. On both five-mode laws the exact `SU(2)` is a subgroup inside a larger quantum-link model, never a separate `SU(2)` model.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Theorem N: an invertible bounded link matrix covariant under a bounded generator has `τ = 0`.
- Corollaries N1, N2, N3: no finite register carries an invertible (hence no unitary, no entrywise-commuting unitary) covariant link, for any group with infinite image, non-abelian or `U(1)`; `[E, U] = U` has no invertible solution on a finite register.
- Corollary N3': `‖𝐔^*𝐔/c − 1‖ ≥ 1` for every `c > 0` on every finite register.
- Proposition N4: for a finite image `ρ(G)`, `L^2(ρ(G))` carries exact Wilson links.
- Corollary N5: in every representation of a PS-6r law's quasi-local algebra, no link variable at any scale is invertible and exactly covariant under the law's own Gauss generators, for the full group or any subgroup with `τ ≠ 0`.
- (3.1) and Proposition R: on rishon registers, `𝐔^*𝐔` is a function of end generators and `rank 𝐔 ≤ dim R`.
- Corollary Y2-0: T0 as stated applies to no PS-6r law at any register size. Y2 can hold only as universality of gauge-invariant correlators.

**Counterexamples.** Section 6's sentence (line 550) "That is T0's theory up to bridges Y1-Y3 below" is false for every PS-6r law (Corollary Y2-0).

**Open, by name.**
- **Y2-W** (`L5-U` first): whether the law's free constants give a small coupling at some scale, so that GA2(a)'s window `a << r << Λ^{-1}` is non-empty, with a register of fixed dimension `C(10, m)`. Not attacked here.
- **ZM1-G**: the TOE side of option (c), stated in section 4.3.
- The kernel question of section 4.2 (whether a band-limited Euclidean kernel lies in the hard core's domain), as part of Y1-Y2.

**Options, with check results.** Nothing is adopted; the owner decides.

| Option | Axiom check | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|---|
| (a1) large-register limit | none: inside free data of `L_cube` (`S`) and `L5-O` (`R`); not available on `L5-U` | conditional | fails for "large", passes for a named `R` | pass | pass | no norm convergence (N3'); one law, one register; GA2 only up to an `R`-dependent error |
| (a2) D-theory, fifth direction | Lattice read plainly gives no layer index; inside sites it changes Qubit/PS-5 content | fails | passes only with `L_5` fixed | pass | fails | axiom-level; recorded |
| (b) `L^2(G)` links | conflicts with PS-6r; with Qubit under R-S only; none under R-X; Lattice and Record no conflict | conditional (T0 and CH1 Attack 3) | pass | fails in part (Y2's link space) | pass | axiom-level; still needs T0-start (Y1, Y3) |
| (c) emergence under ZM1 | none (no spec) | pass | pass | pass | pass | form fixed by N5: correlators or Euclidean variables only |
| (d) finite-subgroup links | PS-6r's "frame group ... acts" not met | fails | pass | fails (GA1's group) | pass | T0 not stated for finite groups; recorded |

**The statement handed to the YM programme (a request in T0's form; not claimed).**

> **T0-start[G].** Let `G` be `SU(2)` (then `SU(5)` for `L5-U`, `SO(10)` for `L5-O`). Let `𝒜_k(g)` be the class of effective actions that the hard core's block RG carries at step `k` at coupling `g` (its inductive hypothesis at scale `a_k = L^k a`, Balaban's class as rebuilt on the branch). There is `g_* > 0` such that for every `a`, every torus side, every `k_0`, and every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4`, with Haar reference measure and density in `𝒜_{k_0}(g)` for some `g ≤ g_*`: (i) UV-CT (CT1-CT4) holds for `μ` at every coarser scale, with all constants independent of `a`, `L` and of `μ` within the class; (ii) along the hard core's trajectory, the Euclidean correlations of the `tr(F^2)` sector of `μ` converge to a non-trivial theory (NT1, NT2) on `R^4` that satisfies the Osterwalder-Schrader axioms with O(4) invariance, the factorial growth bound, and clustering (or a decomposition into clustering components), and reconstructs a Wightman theory; and that theory is T0's, up to a change of scale.
>
> **T0-rate (Y5, from the same start).** At fixed `a_{k_0}`, the correlators of `μ` at separation `r` equal those of the limit in (ii), at the running coupling `g(r)`, up to `O((a_{k_0}/r)^p) + O(g(r)^4)`, with `p > 0` and constants as in (i).

GA2 consumes (i) and T0-rate more than (ii), because the framework's lattice spacing is physical (`TOE_ASSEMBLY.md` section 6, item 4). Alternatives, if the owner chooses (a1) or (a2): T0-QLR[G] or T0-D[G], stated in section 4.3. Item 1 shows that every one of these is a universality statement: none can be met by identifying the law's link operators with Wilson's.
