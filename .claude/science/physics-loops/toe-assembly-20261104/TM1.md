# TM1-i: where and why records form

**FINISH: FROZEN 2026-11-05 after pass 3 (TM1_REFEREE.md); the referee's edits are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment.

**Amendment 1, 2026-11-06 (prior work in the repository; digest `prior/TM1.md`).** No proved result of this file changes. TM1 was drafted before the prior-work gate (SCIENCE_WORKFLOW rule 9, PR #10138). The digest (Codex `gpt-6.1-sol`, read-only) records:
- Duplicates, credited here: Theorem 1's deterministic formation and copy-neighbour content repeat E3/B9 in `LW1.md`; Theorem 6's free-sea nonformation repeats B8a in `LW1.md`, and its dark/trace conclusions repeat conditional record corollaries in `VC1_5.md`.
- Theorems 2–5, 12–13, 16 and Corollary 17 give new statements; R2, Theorem 1, Lemmas 7–10, Theorem 11 and Lemma 15 extend earlier work.
- Contradicted: nothing; R1 corrects the draft's unrestricted saturation claim.
- Inputs that the open statements should use: `LW1U_SEA.md`, for frozen free-sea histories and the segment exception; `docs/PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md` and `docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`, for non-emptiness and pointer formation; `docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md`, for capacity balance; `docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md` and `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`, for the time-axis bridge and kinetic ratio.
- Open statements are unchanged.

Under PS-3c, PS-4, the joint Born identification and the definitions below, the formation set is deterministic. A stationary, site-transitively symmetric state forms records everywhere at tick 1 or nowhere. The proofs below are conditional on the stated laws, observables and imported results. They do not select the physical vacuum. The examples show partial and later formation when the relevant hypotheses are dropped.

**GAP.** PS-3 does not select a transport for every non-factor state. This is not load-bearing for the statements here; see Definition 7 and Lemma R2. The draft’s Corollary 2.9 already states full occupancy as its reading of saturation; the overstatement was its claim of a counterexample under “any reading”. Proposition R1 makes the distinction exact.

**Open.** **TM1-i, remaining parts:** which state VC1 selects and whether its vacuum is in case (E) or (N); the formation rate outside the stated cases; PS-4 stays a premise. **The domain or form of TM1(a)(2):** LW1-R, moved into TM1-i by LW1 Amendment 1; a choice for the owner and lead. **The free-sea excitation question:** whether some local excitation of the free sea forms records at infinitely many ticks. **Inherited, not TM1's own:** VC1 (the gauged vacuum), LW1-U_f with LW1-U_hop, LW1-N and GA1-P. No reading of the Record axiom is proposed or adopted here.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1aea0-1f36-78b0-ab6c-1a5894599987`. Pass 2 distillation of `TM1_DRAFT.md`, Claude Opus 5.5 pass 1, for PR #10138's method. The distiller could not see its own effort or session id; the values above come from the run log. Checkout HEAD `5ff19240cf33824df71619ddac9ce2f943db6247`; local `origin/main` `f5af11cd0102cfd0b51aef0911f600130bf5beb1`. The draft reports earlier HEAD `2d0adc0c02` and the same main revision. This is an author check, not the fresh referee or an audit. `LW1.md` is frozen; `VC1_5_DRAFT.md` and `LW1U_SEA_DRAFT.md` are provisional. The five-mode source `LW1_5_DRAFT.md` is used through the pass-1 citations; its results are conditional imports, not independently checked here. No source grants retained status.

**Editing session provenance.** Codex `gpt-6.1-terra`, effort high, codex-cli 0.165.0, session `01a1aebf-dd05-7e43-a755-d9d39a1c0fb8`.

## 1. Definitions inferred by the distiller

These definitions formalize the draft; they do not add axioms.

1. Sites are `Z^3`, `N(x)={x±e_i}`. The even and odd tilings `T_e,T_o` consist of cubes `2b+{0,1}^3` and `2b+1+{0,1}^3`. A link belongs to the tiling of its unique cube. `G=2Z^3 ⋊ O_{c_0}` preserves both tilings and acts transitively on sites (LW1 A1–A2).
2. `α(A)=U_0^*AU_0` is the tick automorphism, and `ρ_n=ω_0∘α^n`. For the base tick, `U_0=W_E M_o M_e`, `M_e=∏_{C∈T_e} exp(-ia_e H_C)`, `M_o=∏_{C∈T_o} exp(ia_o H_C)`, `a_e=ε-μ/2`, `a_o=ε+μ/2`, `0≤μ<2ε<π`. Infinite products mean the local automorphisms of LW1 E1. `S` or `m` and `τ_E` are law data. `L5-O` means `L5-O[S_+]`, the proposed register; it contains the rishon vacuum.
3. A site-covariant actual value is a finite-spectrum self-adjoint even site observable `a_x`, with `β_g(a_x)=a_{gx}`. Here `β_g` is an automorphism that commutes with `α` and maps neighbours to neighbours. A state is symmetric under a subgroup when it is invariant under one such lift for every group element. Existence of these lifts is imported: for `L_cube` from LW1 A2 and its gauged-covariance proof (`LW1.md` lines 209 and 243), for the five-mode laws from VC1 Lemma C; the covariance of `P_x` and `N_x` is shown in Definition 4.
4. For `L_cube`, `a_x=n_x`. For `L5-O`, `a_x=P_x=∏_{j=1}^5(1-2n_{xj})`. For `L5-U`, `a_x=N_x=Σ_j n_{xj}`. The five-mode identifications are **PS-3h5, proposed only**, not working-set entries. Their source's check results are not adoption of a reading of the Record axiom. Covariance follows from the lifts' common site sign on Majoranas for `P_x`, and number covariance for `N_x`.
5. Write `Π_x(v)` for the spectral projections and `D_xy=1-Σ_v Π_x(v)Π_y(v)` for the disagreement projection, with the union of the two spectra understood. Even observables at distinct sites commute. The joint Born identification supplies `P(ξ_x≠ξ_y)=ρ(D_xy)`; it is an external premise, not derived from PS-3c.
6. Set `F_n={x: ρ_n(D_xy+D_xz)=0 for some distinct y,z∈N(x)}`, `R_0=∅`, `R_n=R_{n-1}∪F_n`, `t_x=inf{n≥1:x∈F_n}`. A first record forms at `t_x` and has content `r_x=ξ_{2t_x}(x)`. Thus `F_n` includes sites that have already recorded; new records at tick `n` are `F_n\R_{n-1}`. This implements PS-3c's probability-one test and LW1's one-record-per-site convention, with PS-4 as the empty start.
7. A history assertion means any measure whose tick marginals are the stated Born laws. Such measures exist for every initial state: the product of the one-time Born laws is one (R2), and LW1 E5 gives supported Markov ones under its hypotheses. The non-factor selection issue remains open. No statement below needs a particular transport to decide `F_n`.
8. For `B⊆Z^3`, `B^{+r}={x:dist_∞(x,B)≤r}`. `A(Λ)` is generated by sites in `Λ` and links with both ends in `Λ`. Full saturation of a finite box means a record at every site of that box.

**Lemma R2 (history measures with prescribed marginals).** (referee closure, TM1_REFEREE.md) Take a live law and an initial state `ω_0`. For each half-tick `h`, let `ν_h` be the Born law of `ω_h` on `Ω=∏_x V_x` (for `h=2n`, `ω_h=ρ_n`). There is a probability measure `Q` on `Ω^{N_0}` whose time-`h` marginal is `ν_h` for every `h`. Every statement below about record contents holds under every measure with these marginals.

*Proof.* `Ω` is a countable product of finite sets, hence compact metrizable. The finite products `⊗_{h∈H}ν_h`, for finite `H⊂N_0`, are consistent. Kolmogorov’s extension theorem gives `Q=⊗_hν_h`. The content law uses only `Q(ξ_{2n}(x)≠ξ_{2n}(y))=ρ_n(D_xy)` and `Q(ξ_{2n}(y)=v)=ρ_n(Π_y(v))`. Theorem 5’s content clause and the dark-state mixture use the joint law at tick 1. These are one-time quantities. `Q` need not respect transport support. `□`

## 2. Formation and symmetry

**Theorem 1 (formation and mixtures).** `F_n,R_n,t_x` depend only on the state sequence. In any history with the prescribed marginals, formation at a fixed site and tick has probability zero or one. If `t_x<∞`, a copy neighbour `y` at `t_x` obeys `P(r_x=v)=ρ_{t_x}(Π_y(v))`. If `ω=λω'+(1-λ)ω''`, `0<λ<1`, then `x∈F_n(ω)` exactly when the same pair of neighbours witnesses formation in both components. In particular `F_n(ω)⊆F_n(ω')∩F_n(ω'')`.

*Proof.* The tests are finitely many fixed nonnegative expectations. The recursion fixes the times independently of the realized configuration. At `t_x`, `ρ(D_xy)=0`, so `ξ_x=ξ_y` almost surely and the marginal gives the content law. Linearity of the tick and positivity show that a positive mixture of the two expectations vanishes exactly when both vanish, for the same pair. `□`

Thus mixing a dark state with the trace does not make formation a random event: the trace has positive disagreement on every link. Content can nevertheless be random.

**Theorem 2 (stationarity).** If `ω_0∘α=ω_0`, then `F_n=F_1`, `R_n=F_1` for all `n≥1`, and `t_x∈{1,∞}`. If `ω_0∘α^p=ω_0`, every first record forms by tick `p`.

*Proof.* Stationarity makes all `ρ_n` equal. More generally `ρ_n` is periodic with period `p`. Apply the definition of `F_n` and the recursion for `R_n`. `□`

**Theorem 3 (transitive symmetry).** If a site-transitive subgroup `H⊆G` has lifts commuting with the tick and fixing `ω_0`, then each `F_n` is empty or all of `Z^3`. Consequently all records first form at one common tick, or none form.

*Proof.* `ρ_n∘β_h=ρ_n`, and spectral calculus gives `β_h(D_xy)=D_{hx,hy}`. A witnessing pair at `x` maps to one at `hx`. Transitivity gives the two possibilities. Apply the recursion for `R_n`. `□`

**Theorem 4 (TM1-D).** Under the hypotheses of Theorems 2 and 3, either every site records at tick 1 and `R_n=Z^3` for `n≥1`, or no site ever records. The first case holds exactly when, at one site `x_0`, two neighbours `y ≠ z` have `ω_0(D_{x_0y}) = ω_0(D_{x_0z}) = 0`. Gauge invariance and purity are not needed.

*Proof.* Combine Theorems 2 and 3. Stationarity identifies the tick-1 tests with those in `ω_0`; transitivity propagates a witness. `□`

**Theorem 5 (which case under `G`).** At a tick of a `G`-symmetric state let `d_e,d_o` be the disagreement expectations on even and odd links. They are well defined. `F_n=Z^3` exactly when `d_e=0` or `d_o=0`. Equivalently the configuration is almost surely constant on every cube of at least one tiling. If both vanish it is almost surely constant on the lattice. In case (E) of Theorem 4, record content is at most one value per cube of such a tiling.

*Proof.* The site stabilizer cyclically permutes the three even incident links and the three odd incident links; site transitivity gives one orbit per tiling. Each site has three links of each type. Zero on one type provides two witnesses; any witness forces one of the two orbit values to vanish. Each cube's edge graph is connected. A countable union of null disagreement events is null. In case (E), the contents are the tick-1 configuration. `□`

The mixture of empty and full dark `L_cube` states with equal weights records everywhere, with all contents zero or all one, each with probability one half.

**Theorem 6 (states on file, conditional on the cited results).** For the actual values in Definition 4, the following stationary symmetric states are in case (E): the two `L5-O` dark witnesses of VC1 O2 and Remark O2.1, the even-`m` `L5-U` dark witnesses and their full partners of VC1 U3, and empty- or full-matter `L_cube` with tracial links. In case (N) are the free seas of the free ticks, each law's tracial state, and the `L5-U` states `ω_t` for finite `t` (VC1 U1). The gauged examples are gauge invariant.

*Proof.* The dark witnesses have respectively sharp uniform `P=±1`, `N=0` or `5`, or `n=0` or `1`. Every disagreement vanishes. For `L_cube`, every hop kills empty and full matter; electric gates preserve the link trace. Lifts and gauge transformations preserve these states. The other stationarity and invariance claims are the cited VC1 results. LW1 B8a and the imported five-mode B8a-5 give the free-sea result; stationarity and symmetry are from `LW1.md` B10(3) and `LW1_5_DRAFT.md` A2-5. In the trace, independent site values give disagreement `1/2` for `n` or parity and `1-Σ_k [C(5,k)/32]^2=772/1024` for `N`. For finite `t`, the independent number probabilities `p_k∝C(5,k)e^{-tk}` are all positive, hence `1-Σ_k p_k²>0`. Theorem 4 applies. `□`

As `t→+∞`, `ω_t` converges locally to the matter-vacuum, tracial-register state, which is case (E). Thus formation is discontinuous in the state. For the free sea, `LW1U_SEA_DRAFT.md` Corollary 3.3 additionally gives a frozen actual configuration off `Σ_π`, conditional on its stated transport and its provisional proof. It does not establish the gauged vacuum.

## 3. Constructions that remove hypotheses

The next four lemmas use the base tick. A configuration state has sharp matter occupations and link labels. A blocked link is one whose hopping operator kills the configuration. The five-mode gauge average `E` of VC1 Lemma 1.1 preserves gauge-invariant `D_xy`, commutes with the base tick and lifts, and produces a gauge-invariant state. These are conditional imports.

**Lemma 7 (blocked `L_cube` links).** For an oriented link `(x,y=x+e_i)` with electric eigenvalue `e`, `T=c_y†Jc_x+c_x†J†c_y` kills a configuration exactly if the endpoint occupations coincide, or `(n_x,n_y,e)=(1,0,S)`, or `(0,1,-S)`. Otherwise the one allowed hop has coefficient `±j(e)` or `±j(e-1)`, where `j(e)=√[S(S+1)-e(e+1)]`.

*Proof.* The forward term needs `(n_x,n_y)=(1,0)` and `e<S`; the reverse needs `(0,1)` and `e>-S`. The conditions exclude each other. `□`

**Lemma 8 (frozen `L_cube` configurations).** If every link is blocked, its configuration state is stationary and locally gauge invariant, and its occupation law is the point mass at that configuration.

*Proof.* Every cube Hamiltonian kills the vector and each electric gate gives a phase. Finite gate support proves stationarity on local observables. Each Gauss generator is diagonal in the labels, so gauge transformations also give phases. `□`

**Lemma 9 (blocked `L5-U` links).** A sector product vector has definite site numbers and definite end numbers. A link hop kills such a vector if both endpoint numbers are zero, both are five, or the endpoints have numbers `5,0` and the full-matter end holds `min(m,5)` rishons.

*Proof.* For equal empty or full numbers, matter annihilation or creation kills both terms. Otherwise the term moving away from the full site is killed because its rishon creation end is full when `m≥5`, or its annihilation end is empty when `m≤5`. Matter kills the reverse term. `□`

**Lemma 10 (blocked `L5-O` links).** With the rishon vacuum on a link and definite matter occupations, the hop kills the vector if either end is empty.

*Proof.* In the four matter creation/annihilation sectors, the register coefficients are proportional to `d_y d_x`, `d_y d_x†`, `d_y† d_x`, and `d_y† d_x†`, respectively. The first three kill the rishon vacuum. The last multiplies `c_y c_x`, which kills an empty endpoint. The electric layer gives a phase because the rishon vacuum has `Γ^x=-1` (VC1 O2). `□`

**Theorem 11 (stationary partial formation).** On each of the three base laws there is a gauge-invariant, `2Z^3`-translation-invariant stationary state in which precisely the sites outside `2Z^3` first record at tick 1, and no site of `2Z^3` ever records. For five modes use proposed PS-3h5.

*Proof.* Mark `2Z^3`; no two marked sites are neighbours. For `L_cube` put one particle at each marked site, none elsewhere, and set each mixed link to its blocking endpoint value from Lemma 7; set the other link values to `S`. For `L5-U`, put full matter at marked sites, empty matter elsewhere, and put rishons of flavours `1, …, min(m,5)` at the marked end of each mixed link and flavours `1, …, max(m−5,0)` at the other end; on each link with no marked end put `min(m,5)` rishons at the source end and the rest at the target end, in the same definite configuration on every link of its kind. For `L5-O`, put one mode-1 particle at each marked site, empty matter elsewhere and rishon vacuum on every link. Lemmas 8–10 block the hops. On `L5-U`, `W_E` is a function of the end numbers, so it multiplies each vector with definite end numbers by a phase; on `L5-O`, Lemma 10 gives the phase. On each finite region containing the gates in `α(A)`, `U_0` therefore multiplies the product vector by a phase. The argument of Lemma 8 then gives stationarity on both five-mode laws (referee closure, TM1_REFEREE.md). Gauge-average the five-mode states. Even translations preserve the construction. Actual values are sharp and unequal on mixed links, including after the gauge average. Each marked site differs from all six neighbours. Each unmarked site has at most two marked neighbours and hence at least four agreeing neighbours. Theorem 2 completes the proof. `□`

**Theorem 12 (symmetric later formation).** On `L_cube`, suppose `sin(a_o j(m)/√3)≠0` for some `m∈{-S,…,S-1}`. There is a symmetric gauge-invariant nonstationary state with no records at tick 1 and records everywhere at tick 2. The hypothesis holds throughout the window for `S≤3/2`, and for each fixed `S` outside finitely many values of `a_o`.

*Proof.* Let `ψ` be the product over even cubes of the equal mixture of empty and full matter, with tracial links, and let `ω_0=ψ∘α^{-2}`. Cube preservation and link trace give symmetry and gauge invariance, which `α^{-2}` preserves. At tick 2 the state is `ψ`, and all three even neighbours agree.

At tick 1 the state is `ψ∘α^{-1}`. It suffices by symmetry to show positive disagreement with all six neighbours of `x=(1,1,1)`. In a finite support expansion of `ψ`, every configuration with constant occupation per even cube has positive weight. Choose one with the even cube of `x` full, all other even cubes empty, every mixed link at its blocking value and every other link at `S`. It remains fixed and disagrees with each odd neighbour.

For even neighbours, change the odd link `(x,x+e_1)` to `m<S`, and set the two even links entering `x+e_1` in directions 2 and 3 to `-S`. Only this odd link can hop. After the hop all other links at the two endpoints are blocked; all other links are unchanged and blocked. The odd-cube Hamiltonian acts as `(j(m)/√3)σ_x` on the two configurations, and all even-cube generators kill both. The inverse tick therefore produces the moved configuration with squared amplitude `sin²(a_o j(m)/√3)>0`. It disagrees with all three even neighbours of `x`. Positivity of the mixture makes each disagreement positive, so `F_1=∅` and `F_2=Z^3`. The two states differ, so the initial state is not stationary. For `S≤3/2`, use `m=-S`: `0<a_o j(m)/√3≤a_o<π`. For fixed `S`, the zeros for that `m` are finite in `(0,π)`. `□`

**Theorem 13 (prescribed first-record time).** On `L_cube`, choose `m∈{-S,…,S-1}`, `θ=a_e j(m)/√3`, `φ=τ_E(2m+1)` and

`U=diag(e^{iφ/2},e^{-iφ/2})(cos θ I-i sin θ σ_x)`.

Let `q` be the least positive integer with `U^q` scalar, or `∞`. If `sin θ≠0`, then for every integer `1≤k≤q` there is a gauge-invariant state in which `x=0` first records at tick `k`, and every site other than `x,y=e_1` records at tick 1. If `q≥3`, choosing `k=3` gives no new record at tick 2 and a new record at `x` at tick 3. For `S=1/2`, throughout the window `q≥4`; `q=∞` exactly when `a_e/(√3π)` is irrational.

*Proof.* Let `|x⟩` have one particle at `x`, electric value `m` on `(x,y)`, and the remaining links at `x` or `y` set to block a particle at that endpoint; all other sites are empty and all other link values are `S`. Let `|y⟩` move the particle to `y` and raise that link to `m+1`. All links other than `(x,y)` are blocked on both vectors. The even cube containing that link acts as `j(m)σ_x/√3`, the odd cubes act trivially, and the electric layer supplies the displayed diagonal phases up to a common phase. Thus the tick acts as `U` up to phase. The two vectors have identical Gauss eigenvalues: the particle and outgoing electric changes cancel at `x`, as do the particle and incoming changes at `y`. The initial vector `U^{-k}|y⟩` therefore defines a gauge-invariant state.

At tick `n` its vector is `U^{n-k}|y⟩`. Let `p_n` be the probability that the particle is at `x`. All sites outside `{x,y}` are certainly empty and have at least four certainly empty neighbours, hence record at tick 1. Site `x` has five certainly empty neighbours and disagrees with `y` with probability one, so `x∈F_n` exactly if `p_n=0`. Write `U=e^{iχ}(cos β I+i sin β u·σ)`. Its off-diagonal entries are nonzero, so `u` has a nonzero transverse component. Therefore `U^r|y⟩` is proportional to `|y⟩` exactly when `sin(rβ)=0`, equivalently `U^r` is scalar. For `n<k≤q`, this does not occur; it occurs at `n=k`.

For `k=3`, at tick 2 `p_2>0`. A first record at `y` would need `p_2=1`, making `U^{-1}` anti-diagonal and `U²` scalar, contrary to `q≥3`. The other sites have already recorded. For `S=1/2`, `m=-1/2`, `φ=0`, `θ=a_e/√3∈(0,π/(2√3))`, and `U^r` is scalar exactly when `rθ∈πZ`. The stated bounds follow. `□`

For finite `q`, `y` may record; for example `S = 1/2`, `a_e = √3π/4`, `k = 3` gives `p_1 = 1`. Nothing below uses `y`.

**Corollary 14 (new records at every tick).** If the data in Theorem 13 have `sin θ ≠ 0` and `q = ∞`, there is a gauge-invariant state forming at least one new record at every tick. For example take `S=1/2` and irrational `a_e/(√3π)`.

*Proof.* Place the two-site construction at `x_k=(8k,0,0)`, `y_k=x_k+e_1`, using `U^{-k}|y_k⟩`, for every `k≥1`. Their relevant cubes, links and copy neighbourhoods are disjoint. Each evolves as in Theorem 13. The local vector states are even, so their infinite product is a state. The Gauss argument applies to each copy. Thus `x_k` first records at tick `k`. `□`

For a finite box containing the first `K` copies and no later copies, the count rises at ticks 1 through `K` and then stays fixed. No `y_k` records: an anti-diagonal power would have a scalar square, contradicting `q=∞`. Each `x_k` record has value zero. These are constructed initial states, not vacuum selection results.

**Check record.** The pass-1 draft reports that `/tmp/toe-tm1/check_blocked.py` tested the link support bookkeeping on a `4³` torus for `S=1/2,1,3/2,2`, all allowed `m`, with four reported PASS classes: the marked configuration, the two-state construction, and the configuration `v_1` and the pair `v_2, b_2` in Theorem 12. The script used the same definitions as the proof. It is not present in this environment, so this pass did not inspect or rerun it. The reported check is neither independent evidence nor a proof.

## 4. Local excitations

**Lemma 15 (base-tick cone).** `α^n(A(Λ))⊆A(Λ^{+2n})`, and `α` preserves even parity.

*Proof.* An electric gate acts on one link. Odd-cube gates expand support by at most one in sup distance; even-cube gates expand it by at most one more. Disjoint even gates commute with local observables, including odd observables. All gates are even. Iterate. `□`

**Theorem 16 (formation outside the cone).** Suppose `ω_0(A)=ω_v(A)` for every even `A∈A(Z^3\B)`. If `dist_∞(x,B)>2n+1`, then `x` has the same membership in `F_n` and in `R_n` for the two states.

*Proof.* Each even test `D_xy+D_xz` is supported within distance 1 of `x`. Lemma 15 puts its `n`-tick evolution within distance `2n+1`, disjoint from `B`. The expectations, hence all witnesses, agree. The same holds at each earlier tick, giving the assertion for `R_n`. `□`

**Corollary 17 (two backgrounds).** If `F_1(ω_v)=Z^3`, every site at distance at least 4 from `B` records at tick 1 under `ω_0`. In that case, if `B` is finite, at most `|B^{+3}|` records form after tick 1. If `R_n(ω_v)=∅` for every `n`, then `R_n(ω_0)⊆B^{+(2n+1)}`.

*Proof.* Use Theorem 16. A site records at most once. `□`

A local even or odd unitary `W∈A(B)` gives an example: for any even observable outside `B`, graded locality gives `[W,A]=0`, so `ω_v(W*AW)=ω_v(A)`. This includes `W=c_x+c_x†`. Product states differing only at sites of `B` and links meeting `B` also agree outside `B`; the local gauge average preserves the outside algebra and this agreement. For the tracial state, `τ(W*AW)=τ(A)` for every unitary, so a unitary excitation is the same state and forms no records.

## 5. Consequences for TM1

For a nonempty finite box, Theorem 4 makes its deterministic count either `0, |Λ|, |Λ|, …` or `0, 0, 0, …`. Under the explicitly inferred full-occupancy definition of saturation, TM1(a)(2) holds for a stationary symmetric state exactly in case (E): it has one increase, at tick 1. In case (N) it fails. This conditional result does not fix how saturation should be read in the assembly.

TM1(a)(2) cannot hold for every initial state with full-occupancy saturation: the trace never records, and Theorem 11 leaves the marked sites unrecorded. More decisively, choose Theorem 13 with `S=1/2`, `k=3`, and a finite box containing `x` and at least one site outside `{x,y}`. Its count increases at tick 1, is flat at tick 2, and increases at tick 3. Under every reading of saturation under which a saturated box never gains a record later (full occupancy is one), this box is not saturated at ticks 0, 1 or 2, because it gains a record at tick 3; its count does not rise from tick 1 to tick 2; so TM1(a)(2) fails for it (referee closure, TM1_REFEREE.md). These are statements about the specified state and its allowed history marginals; they do not assert a selected PS-3 transport for a non-factor state.

**Proposition R1.** (referee closure, TM1_REFEREE.md) For the box just described, TM1(a)(2) fails under every monotone reading of saturation: one under which a saturated box never gains a record later. Full occupancy is monotone. Under the reading “a box is saturated at tick `s` when `c_{s+1}=c_s`”, where `c_n=|R_n∩Λ|`, TM1(a)(2) holds at every finite box for every state of the three laws.

*Proof.* For the first assertion the preceding paragraph gives `c_0<c_1=c_2<c_3`, so saturation cannot occur by tick 2 and the required strict increase fails at tick 2. For the second, let `s*` be the first tick with `c_{s+1}=c_s`, or infinity if none. For `n<s*`, the counts differ, and `R_n⊆R_{n+1}` makes them nondecreasing; hence `c_{n+1}>c_n`. `□`

A record set that grows on more than one tick requires both nonstationarity and absence of site-transitive lifted symmetry. Theorem 13 and Corollary 14 exhibit such behaviour. A finite local excitation of an everywhere-recording background has only finitely many possible later first records, all in `B^{+3}`. Above a never-recording background, records at tick `n` are confined to `B^{+(2n+1)}`. These results do not establish an arrow in the selected physical vacuum or a formation rate for general initial states.

For VC1, the `L5-O` half-filled dark witness records everywhere under proposed PS-3h5, while its tracial witness does not. The `L5-U` tracial state is half filled and does not record; its even-`m` dark witnesses record under proposed PS-3h5. VC1's provisional U2 and U2′ exclude half filling under their stated symmetry and gauge-invariant purity hypotheses; they do not select the vacuum. The record pattern in a dark witness with uniform sharp content contains no spatial information. In a general case-(E) state it can carry one value per cube of a zero-disagreement tiling.

**Readings and checks.** PS-3c and PS-3h are owner-selected refinements; the four-test results and revisions are recorded in `TOE_ASSEMBLY.md` §3.2. PS-3g and PS-3h5 remain proposed only. The source four-test check gives both passes on tests 1, 2 and 4, and a conditional result on test 3: together with PS-6r, PS-3g excludes register classes with no frame-invariant site value and so affects the component group in GA1-i. PS-3h5 inherits that condition. No adoption or new check is asserted here. The `LW1U_SEA_DRAFT.md` result has its own stated domain and provisional status. No new Record-axiom reading is proposed. The restriction of admissible states or any restatement of TM1(a)(2) remains an owner/lead decision.
