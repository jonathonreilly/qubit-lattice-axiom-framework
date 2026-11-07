lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# TM1-i on the current laws, pass 1: where and why records form

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. Lane: TM1-i of part TM1.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks one tiny scratch computation, `/tmp/toe-tm1/check_blocked.py` (section 3.5). It ran after `memory_pressure` showed 64 percent free. `scripts/lab_ops.py preflight` could not run, because the script is not in this sparse checkout. A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), HEAD | `2d0adc0c02` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `f5af11cd01` |

Files read at HEAD, by line, with the commit that last changed each. All are in `.claude/science/physics-loops/toe-assembly-20261104/`.
- `TOE_ASSEMBLY.md` (last changed `7d2b20d29`): lines 1-230 (head, axioms, section 3 in full), 279-297 (TM1), 476-486 (VC1), 567-585 (imports). Used by line: 20 (Record axiom), 144 (PS-7's tension), 181-182 (PS-3h, PS-3c), 198 ("Records form.": left to TM1), 281-283 (TM1(a)), 290-293 (sources), 297 (TM1(e)), 476 (VC1(a)(4)).
- `LW1U_SEA_DRAFT.md` (last changed `2d0adc0c0`): lines 1-404, all of it. Used by line: 145-151 (Theorem 2.3), 183 (Corollary 3.3), 371 (what it changes for TM1).
- `VC1_5_DRAFT.md` (last changed `2d0adc0c0`): lines 1-353, all of it. Used by line: 42 (the lane target there), 56-60 (the two laws), 64-76 (Lemma 1.1, the gauge average), 80-90 (Lemma C, the lifts), 92-97 (Lemma S2′), 156-160 (Theorem O1), 162-193 (Theorem O2; 174 for `𝒰^{++}`, 176 for `Γ^x_ℓ` on the vacuum, 178 for the lifts on `L5-O`), 195 (Remark O2.1), 197-201 (Corollary O3), 222-224 (Theorem U1), 240-254 (Theorem U3, Corollary U3′; 250 for the gauge invariance of `N_x`), 314 (TM1-i depends on the state VC1 selects).
- `LW1.md` (frozen; last changed `da0ec1934`): lines 1-502, all of it. Used by line: 11-16 (Amendment 1), 28-47 (sites, links, gauge invariance), 57-64 (dressed tick, time convention), 66-76 (odds, copy test, formation sets), 97 (quasi-free states), 117 and 132 (inferred definitions 11 and 26), 176-178 (A1), 199-205 (A2), 231-237 (B4, gauged covariance), 272-306 (B8, B8a, B8b, B9), 312-340 (B10), 391-399 (E1), 428-430 (E3), 440-446 (E5), 500 (LW1-R).
- `LW1_5_DRAFT.md` (last changed `e648fa3e0`): lines 296-425 (sections 8, 9 and the start of 10). Used by line: 305-318 (statement of `L5-O` and `L5-U`), 322-324 (PS-3g, PS-3h5, proposed only), 376 (E3-E6 carry over), 392-394 (B1-5), 396-402 (B8-5, B8a-5).
- `Y2W_DRAFT.md` (last changed `92e03055c`): lines 1-40 and 170-208, for the file format only.
- `LW1_5X_DRAFT.md` (untracked, another lane's file): lines 1-5, to see what it is. Not used.

On `origin/main`: `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md` (last changed `9b923469d`), lines 1-80, as context for section 5 only. No other branch was read. No existing file was edited.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The Record axiom, PS-3c, PS-4 and PS-3h5 are read plainly. This file proposes no reading, specification or definition, so no four-test smuggle check is run. The notions defined in sections 1.2, 1.4 and 3.1 (site-covariant actual values, lifts, blocked links) are notation for stating the theorems. The theorems quantify over every choice, so none of them is proposed for adoption. Section 5 states what the theorems imply for TM1. It proposes no rule.

**Working set used, by name.** PS-3 read by PS-3c (the copy rule) and PS-3h (the actual configuration), with LW1's formalization of them (`LW1.md` lines 66-76, E3). PS-4 (no record at tick 0). PS-1 read by PS-1c, only through the three laws and their lifts. PS-5 and PS-6r, only through `L5-O` and `L5-U` as stated in `LW1_5_DRAFT.md` section 8.1. On five-mode sites, the actual values are those of PS-3h5 (proposed only, not in the working set) wherever a five-mode example names them. The main theorems hold for every site-covariant choice of actual values, so they do not depend on PS-3h5. PS-2, PS-7, PS-11 are not used.

**Results of other files used.** `LW1.md`: A1 (tilings), A2 (the group `𝒢`, transitivity, three-element stabilizers), B4 and gauged covariance (lifts commute with the tick), B8 and B8a (no copy in a quasi-free state at half filling), E1 (infinite-volume tick), E3 (formation is a function of the state sequence; rebuilt here as Lemma 1.1), E5 (history measures). `VC1_5_DRAFT.md`: Lemma 1.1 (gauge average), Lemma C (lifts on `L5-O` and `L5-U`), Lemma S2′ (stabilizers and link reversals), Theorems O1, O2, U1, U3 and Corollaries O3, U3′ (the state classes in Corollary 2.7). `LW1_5_DRAFT.md`: B1-5, B8-5, B8a-5. `LW1U_SEA_DRAFT.md`: Corollary 3.3, as context in section 5. Each step used from these is quoted or rebuilt at the point of use.

**Inputs from outside the working set.** The joint Born identification, which `LW1.md` takes as a premise (inferred definition 26): the law's probability that two actual values agree is the state's expectation of the agreement projector. Standard mathematics, rebuilt where used: commuting spectral projections, positivity of states, the spectral form of a two-by-two unitary. Literature context, credited from memory and never load-bearing: the past hypothesis (Boltzmann; Penrose; Albert, *Time and Chance*, 2000) and redundant records (Zurek's quantum Darwinism, for example *Nature Physics* 5 (2009) 181). The main-branch arrow note quoted in section 5 is context, not a proof step.

**Literature and repo search.** Time-boxed. Repo: the TM1 sources that `TOE_ASSEMBLY.md` lines 290-293 name, and the arrow note on `origin/main`. Its closest statement: "from the **`I/d` equilibrium** (max-entropy) state, `R_red` is exactly **flat** (`[0,0,0,0,0,0]`); `I/d` is invariant — equilibrium has no arrow". That is a finite toy with a redundancy functional, not PS-3c. No web search was run. The dichotomy below is elementary. Its proof uses only stationarity, the lifts and the determinism of PS-3c's test, and it is rebuilt in full.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 283, TM1(a)(2):

> "2. under PS-4 (`R_0` empty) and the formation rule of PS-3, on every finite box the law-expected record count is strictly increasing in `n` until saturation [**open input TM1-i**: formation in the vacuum, see (e)], so the arrow is the direction of record growth;"

Line 297: "(e) **Open inputs.** TM1-i: whether records form in the PS-7 vacuum at all (#9876, #10018 say records on change are frozen there); the formation rate; PS-4."

Line 198, the owner decision of 2026-11-04: "**"Records form.": left to part TM1.** Under PS-3c no record forms in the free vacuum or in the tracial state. Where and why records form is TM1's open input TM1-i. No reading of the Record axiom is adopted."

Line 182, PS-3c: "The actual value of a site has been copied into a neighbouring site at a tick when the law gives probability one that their actual values agree at that tick. A record forms at the end of a tick at each site that carries no record and whose actual value has then been copied into at least two of its neighbours; it locks the site's actual value."

What is known at the two ends. `LW1U_SEA_DRAFT.md` line 183, Corollary 3.3: "Let `(eps, mu)` lie in the window and off `Σ_π`. Build a history measure from `ω_P` as in `LW1.md` E5, with each step selected from `O_h`. Then `ξ_h = ξ_0` for every `h`, almost surely". `LW1.md` line 285, Corollary B8a: "Under the free tick and PS-3c, starting from the free sea, no record forms." `VC1_5_DRAFT.md` line 197, Corollary O3: "If actual values are site parities (PS-3h5 ...), then under PS-3c every site's actual value is copied into all six neighbours at tick 1, and a record forms at every site at the end of tick 1, with value `+1`." Line 254, Corollary U3′, says the same for the dark witnesses of `L5-U`. Line 160: in the tracial state of `L5-O` "no record forms under PS-3c".

**The lane's question.** Take a live law: `L_cube`, `L5-O` or `L5-U`. Is there a state of it that is stationary, gauge-invariant and symmetric, in which records form at some sites and not at others, or form progressively over ticks, with probability strictly between 0 and 1? The brief asks for a dichotomy theorem, or for a state with partial or progressive formation. It also asks what TM1 then needs for an arrow of time.

## 0.1 Outcome

**The answer is no, by a theorem.**

**Theorem TM1-D (dichotomy; proved here, Theorem 2.3).** Take `L_cube`, `L5-O` or `L5-U`, at any value of the free constants, with PS-3c and any site-covariant choice of actual values. Let `ω_0` be stationary under the tick and invariant under the lifts of the group `𝒢` of PS-1c. Then either a record forms at every site at the end of tick 1, or no record ever forms. Gauge invariance is not needed.

The theorem has two halves, each proved alone.
- **Stationarity alone** (Theorem 2.1): in every stationary state, every record that ever forms, forms at the end of tick 1.
- **Symmetry alone** (Theorem 2.2): in every state invariant under a group of lifts that acts transitively on sites, at each tick records form at every unrecorded site or at none.

Both rest on one fact. Under PS-3c the record set is a function of the state sequence, not of the realized history (Lemma 1.1, rebuilt from `LW1.md` E3). So for every state, formation at a given site and tick has probability 0 or 1. Only the record content is random. The clause "with probability strictly between 0 and 1" has no instance for any state, stationary or not.

**Which case holds** (Proposition 2.5). In a `𝒢`-invariant state, records form at a tick exactly when the actual values agree with probability one across every link of one tiling. Equivalently, the actual configuration is almost surely constant on every cube of the even tiling, or on every cube of the odd tiling. The dark vacua of `L5-O` and of `L5-U` (even `m`) and the dark states of `L_cube` are in the first case. The free sea, the tracial state and the states `ω_t` of `L5-U` at finite `t` are in the second (Corollary 2.7).

**Each hypothesis is needed** (section 3). All three examples are gauge invariant.
- Without rotations: on each of the three laws, a stationary state invariant under the cell translations forms a record at tick 1 at every site outside `2Z^3`, and never at the sites of `2Z^3` (Proposition 3.5).
- Without stationarity: a `𝒢`-invariant state of `L_cube` forms no record at tick 1 and a record at every site at tick 2 (Proposition 3.6).
- Without both: a state of `L_cube` with one site whose first record forms at tick `k`, for every `k` up to the order `q` of a two-by-two unitary of the law, with `q ≥ 4` for `S = 1/2` (Proposition 3.7). Where `q` is infinite, a state forms new records at every tick (Corollary 3.8).

**Excitations above a stationary state** (Theorem 4.2). Let `ω_0` agree with a stationary state `ω_v` on the even observables outside a finite set `B`. If `ω_v` forms records everywhere, every site at sup-distance at least 4 from `B` records at tick 1, so at most `|B^{+3}|` records form after tick 1 in the whole history. If `ω_v` forms none, every record formed at tick `n` lies within sup-distance `2n + 1` of `B`.

**What TM1 needs** (section 5). In a stationary symmetric state, TM1(a)(2) holds exactly when records form everywhere at tick 1. The arrow is then a single step, from tick 0 to tick 1. As a statement about every history of the law, TM1(a)(2) is false: Proposition 3.7 gives a box whose count stays flat for one tick and then rises. A record arrow that grows at more than one tick needs an initial state that is neither stationary nor symmetric. Above a dark vacuum, local excitations add only finitely many records after tick 1. Under PS-3c as on file, the arrow is a property of the initial state.

---

## 1. Setting: the copy rule on the three laws

### 1.1 Laws and ticks

The notation is that of `LW1.md` section 1. Sites are `x ∈ Z^3`, the shell is `N(x) = {x ± e_i}`, and the tilings `𝒯_e`, `𝒯_o` are those of `LW1.md` line 31. A link `(x, x + e_i)` lies in an even cube when `x_i` is even and in an odd cube when `x_i` is odd (`LW1.md` A1). Call it an *even link* or an *odd link*. The group `𝒢 = 2Z^3 ⋊ O_{c_0}` is that of `LW1.md` line 33.

The three live laws are `L_cube` (`LW1.md` section 2, with link spin `S`), `L5-O[S_+]` and `L5-U[m]` (`LW1_5_DRAFT.md` section 8.1, restated in `VC1_5_DRAFT.md` section 1.1). Each has the base tick `U_0 = W_E M_o M_e`, with `M_e = ∏_{C ∈ 𝒯_e} e^{−i a_e H_C}`, `M_o = ∏_{C ∈ 𝒯_o} e^{i a_o H_C}` and a link-only electric layer `W_E`. The tick automorphism is `α(A) = U_0^* A U_0` (`LW1.md` E1), and the state at the end of tick `n` is `ϱ_n = ω_0 ∘ α^n` (`LW1.md` line 64). The free data are `0 ≤ μ < 2ε < π`, `τ_E ∈ R`, and `S` or `m`. The free tick of `L_cube` (one-body tick `V`, `LW1.md` line 55) is used only for the free sea. Sections 1 and 2 hold for every tick automorphism that commutes with the lifts of section 1.4, so they hold also with any cell-covariant plaquette layer. Sections 3 and 4 use the base tick.

### 1.2 Actual values and the copy test

**Actual values.** A *site-covariant choice of actual values* assigns to each site `x` a self-adjoint element `a_x` of the even part of the algebra of site `x`, with finite spectrum `V_x`. The lifts of section 1.4 must satisfy `β_g(a_x) = a_{gx}`. Elements of the even parts of different sites commute, so the `a_x` commute. Write `Π_x(v)` for the spectral projection of `a_x` at `v`. The choices on file are:
- `L_cube`, PS-3h: `a_x = n_x`, values `{0, 1}`.
- `L5-O[S_+]`, PS-3h5 (proposed only): `a_x = P_x = ∏_j (1 − 2 n_{x,j})`, values `{±1}`.
- `L5-U[m]`, PS-3h5 (proposed only): `a_x = N_x`, values `{0, …, 5}`.

**The copy test.** Put `D_xy = 1 − Σ_v Π_x(v) Π_y(v)`. It is the projection onto "the actual values at `x` and `y` differ". For `L_cube` it is `(n_x − n_y)^2`, the copy test of `LW1.md` line 71. For `L5-O` it is `(1 − P_x P_y)/2`, the projector of `LW1_5_DRAFT.md` line 400.

The Born law of a state `ω` on configurations `ξ ∈ ∏_x V_x` is `ν_ω(ξ_F = σ) = ω(∏_{x ∈ F} Π_x(σ_x))`, as in `LW1.md` line 69. Applying the state to joint projectors is the joint Born identification (`LW1.md` inferred definition 26). Then `ν_ω(ξ_x ≠ ξ_y) = ω(D_xy)`.

**Formation sets.** As in `LW1.md` lines 72-76, with this `D`:

`F_n = {x : there are y ≠ z in N(x) with ϱ_n(D_xy + D_xz) = 0}`,  `R_0 = ∅`,  `R_n = R_{n−1} ∪ F_n`,  `t_x = inf{n ≥ 1 : x ∈ F_n}`.

A record forms at `x` at the end of tick `n` exactly when `t_x = n`. If `t_x < ∞`, its content is `r_x = ξ_{2 t_x}(x)`, the actual value at that time. Both `D`'s are positive, so `ϱ_n(D_xy + D_xz) = 0` exactly when `ϱ_n(D_xy) = ϱ_n(D_xz) = 0`.

**Why this is PS-3c.** Let `Q` be any history measure whose one-time marginals are the Born laws `ν_h` of `ω_h` (`LW1.md` E5; `LW1_5_DRAFT.md` line 376 carries E3-E6 to five-mode sites). Then `Q(ξ_{2n}(x) = ξ_{2n}(y)) = ν_{2n}(ξ_x = ξ_y) = 1 − ϱ_n(D_xy)`. So "the law gives probability one that their actual values agree at that tick" holds exactly when `ϱ_n(D_xy) = 0`. This does not depend on which transport `Q` uses. `F_n` is the set of sites whose actual value has been copied into two neighbours at tick `n`. PS-4 is `R_0 = ∅`. The rule that each site carries at most one record, kept from its first formation, is `t_x` and `r_x` (`LW1.md` inferred definition 11).

### 1.3 Formation is a function of the state sequence

**Lemma 1.1 (rebuilt from `LW1.md` E3).** For every initial state `ω_0`, the sets `F_n`, `R_n` and the times `t_x` are functions of the sequence `(ϱ_n)_n`, hence of `ω_0` and the law. For every history measure `Q` and every site `x` and tick `n`, the event "a record forms at `x` at the end of tick `n`" is the whole history space or empty. So its probability is 1 or 0. The content `r_x` is a random variable, with `Q(r_x = v) = ϱ_{t_x}(Π_y(v))` for any copy neighbour `y`.

*Proof.* `ϱ_n(D_xy + D_xz)` is a number fixed by `ω_0`. `N(x)` is finite. So membership of `x` in `F_n` is decided by finitely many numbers, and `R_n`, `t_x` follow by the recursion. None of these depends on a configuration `ξ`. For the content: `Q(ξ_{2n}(x) ≠ ξ_{2n}(y)) = ϱ_n(D_xy) = 0` at `n = t_x`, so `r_x = ξ_{2n}(y)` almost surely, and `Q(ξ_{2n}(y) = v) = ν_{2n}(ξ_y = v) = ϱ_n(Π_y(v))`. This is `LW1.md` B9's first clause, with `Π_y(v)` in place of `n_y^v(1 − n_y)^{1−v}`. ∎

`LW1.md` B9's proof says the same: "Formation times, including prior non-formation, are deterministic functions of the state sequence, so conditioning on formation at such a site adds no random constraint on \(\xi\)."

**Lemma 1.2 (mixtures form fewer records).** Let `ω_0 = λ ω' + (1 − λ) ω''` with `0 < λ < 1`. Then `x ∈ F_n(ω_0)` exactly when some pair `y ≠ z` in `N(x)` has `ϱ'_n(D_xy + D_xz) = 0` and `ϱ''_n(D_xy + D_xz) = 0`. In particular `F_n(ω_0) ⊆ F_n(ω') ∩ F_n(ω'')`.

*Proof.* `ϱ_n = λ ϱ'_n + (1 − λ) ϱ''_n` because `α^n` is linear. A positive combination of two nonnegative numbers vanishes exactly when both vanish. ∎

So a state that is "a dark vacuum with probability `λ`" does not form records with probability `λ`. For example `λ ω_dark + (1 − λ) τ`, with `τ` the tracial state, forms no record at all, since `τ(D_xy) > 0` for every pair (Corollary 2.7). Under PS-3c a record needs agreement with probability one under the whole state.

### 1.4 Lifts

A *lift* of `g ∈ 𝒢` is an automorphism `β_g` of the quasi-local algebra `𝔄` with
- (L1) `β_g ∘ α = α ∘ β_g`, and
- (L2) `β_g(a_x) = a_{gx}` for every site `x`.

A state is *symmetric* if `ω ∘ β_g = ω` for one lift of each `g ∈ 𝒢`. This is condition (iii) of `VC1_5_DRAFT.md` line 42.

**Lemma 1.3 (lifts exist on all three laws).** On each of `L_cube`, `L5-O[S_+]` and `L5-U[m]`, every `g ∈ 𝒢` has a lift with (L1), and (L2) holds for the actual values listed in section 1.2. Each `g` maps `N(x)` onto `N(gx)`.

*Proof.* `L_cube`. `LW1.md` line 237 (gauged covariance): "A geometric symmetry permutes site factors and link factors. If it reverses an oriented link, conjugation by the spin rotation \(e^{-i\pi S^x}\) sends \(E\) to \(-E\) and \(J\) to \(J^\dagger\). A hopping monomial then becomes its correctly oriented monomial or its adjoint. Apply A2's site sign correction to restore the \(\eta_i\). Thus each cube Hamiltonian is sent to the Hamiltonian of the image cube. Its angle is unchanged because each tiling is preserved. The electric squares are preserved by link reversal. This proves covariance of \(U_0\)." So `β_g` maps each gate of each layer to a gate of the same layer, and (L1) holds at infinite volume through the local construction of E1. The sign correction acts on matter as `c_x ↦ d(gx) c_{gx}` with `d = ±1` (`LW1.md` line 203). Hence `β_g(n_x) = n_{gx}`, which is (L2). For the free tick, `LW1.md` line 340: "A2's lifted symmetries commute with \(V\)".

`L5-O` and `L5-U`. `VC1_5_DRAFT.md` Lemma C(i): "`β_g` maps the algebra of site `x` onto that of `gx` and the register of `ℓ` onto that of `gℓ`, and `β_g∘α = α∘β_g`". That is (L1). Lemma C(iii) gives `β_g(N_x) = N_{gx}` on `L5-U`. On `L5-O`, `VC1_5_DRAFT.md` line 178: "`β_g` maps each `γ_{x,a}` to `±γ_{gx,a}`". The sign is the same for all ten `a` at a site, because it comes from `Ad P_x`, and "`P_xγ_{x,a}P_x = −γ_{x,a}`" for every `a` (`LW1_5_DRAFT.md` line 394). From `c_j = (γ_{2j−1} + iγ_{2j})/2`, one has `1 − 2n_{x,j} = −i γ_{x,2j−1} γ_{x,2j}`. A common sign `s` gives `(−i s γ_{gx,2j−1})(s γ_{gx,2j}) = −i γ_{gx,2j−1} γ_{gx,2j}`. So `β_g(P_x) = P_{gx}`.

Every `g ∈ 𝒢` is a lattice isometry: a signed permutation about a cube centre followed by an even translation (`LW1.md` line 201). It maps nearest neighbours to nearest neighbours, so `g N(x) = N(gx)`. ∎

Lifts are fixed only up to sign automorphisms (`VC1_5_DRAFT.md` Lemma C(iv)). Signs do not change any `a_x`, so (L2) holds for every lift.

---

## 2. The dichotomy

### 2.1 Stationarity alone

**Theorem 2.1 (stationary states form all their records at tick 1; proved here).** Let `ω_0 ∘ α = ω_0`. Then `F_n = F_1` and `R_n = F_1` for every `n ≥ 1`, and `t_x ∈ {1, ∞}` for every site `x`.

*Proof.* By induction `ϱ_n = ω_0 ∘ α^n = ω_0` for every `n ≥ 0`. By Lemma 1.1, `F_n` depends only on `ϱ_n`, so `F_n = F_1` for `n ≥ 1`. Then `R_n = F_1 ∪ ⋯ ∪ F_n = F_1`. ∎

So in a stationary state no record forms after tick 1, symmetric or not. The same proof gives: if `ω_0 ∘ α^p = ω_0` for some `p ≥ 1`, every record forms by tick `p`. Stationarity is needed only at full ticks. At odd half-ticks the state may differ, as the free sea does (`LW1U_SEA_DRAFT.md` Theorem 2.3: covariance `\bar P` at odd half-ticks).

### 2.2 Symmetry alone

**Theorem 2.2 (symmetric states form records everywhere or nowhere at each tick; proved here).** Let `H ⊆ 𝒢` be a subgroup that acts transitively on sites, and let `ω_0 ∘ β_h = ω_0` for a lift `β_h` of each `h ∈ H`. Then for every `n ≥ 1`, `F_n = ∅` or `F_n = Z^3`. Hence there is `n* ∈ {1, 2, …} ∪ {∞}` such that `R_n = ∅` for `n < n*` and `R_n = Z^3` for `n ≥ n*`, and `t_x = n*` for every `x`.

*Proof.* Fix `h ∈ H`. By (L1), `ϱ_n ∘ β_h = ω_0 ∘ α^n ∘ β_h = ω_0 ∘ β_h ∘ α^n = ω_0 ∘ α^n = ϱ_n`. An automorphism maps the spectral projections of `a_x` to those of its image, so (L2) gives `β_h(Π_x(v)) = Π_{hx}(v)` and `β_h(D_xy) = D_{hx,hy}`. Let `x ∈ F_n` with witnesses `y ≠ z` in `N(x)`. Then `ϱ_n(D_{hx,hy} + D_{hx,hz}) = ϱ_n(β_h(D_xy + D_xz)) = ϱ_n(D_xy + D_xz) = 0`, and `hy ≠ hz` lie in `N(hx)` (Lemma 1.3). So `hx ∈ F_n`. Thus `F_n` is invariant under `H`, and `H` is transitive, so `F_n` is empty or everything. Let `n*` be the least `n ≥ 1` with `F_n = Z^3`, or `∞` if there is none. For `n < n*` every `F_j` with `j ≤ n` is empty, so `R_n = ∅`. For `n ≥ n*`, `R_n ⊇ F_{n*} = Z^3`. ∎

`𝒢` itself is transitive (`LW1.md` A2: "The action on sites is transitive"). So is `2Z^3 ⋊ K` for every `K ⊆ O_{c_0}` that acts transitively on the eight corners of `C_0 = {0,1}^3`, since even translations carry those corners to every site. The cell translations `2Z^3` alone have eight orbits, the residue classes mod 2. For them the proof gives only that each `F_n` is a union of residue classes. Proposition 3.5 shows that a proper union occurs.

### 2.3 The dichotomy

**Theorem 2.3 (TM1-D; proved here).** Take `L_cube`, `L5-O[S_+]` or `L5-U[m]`, any value of the free constants, a tick automorphism that commutes with the lifts, and any site-covariant choice of actual values. Let `ω_0` be stationary and invariant under a lift of each element of a site-transitive subgroup `H ⊆ 𝒢`, for example `H = 𝒢`. Then exactly one of the following holds:
- (E) a record forms at every site at the end of tick 1: `R_n = Z^3` for every `n ≥ 1`;
- (N) no record ever forms: `R_n = ∅` for every `n ≥ 0`.

Case (E) holds exactly when, at one site `x_0`, two neighbours `y ≠ z` have `ω_0(D_{x_0 y}) = ω_0(D_{x_0 z}) = 0`.

*Proof.* Theorem 2.1 gives `R_n = F_1` for `n ≥ 1`. Theorem 2.2 gives `F_1 ∈ {∅, Z^3}`. By transitivity, `F_1 = Z^3` exactly when `x_0 ∈ F_1` for one site `x_0`, and `ϱ_1 = ω_0`. ∎

Gauge invariance is not used. Neither is purity, a factor property, the PS-3 transport, or any property of the realized history. So no stationary symmetric state of a live law has records at some sites and not at others, and none has records that form progressively over ticks. This answers TM1-i's first question.

### 2.4 Which case: the links of one tiling

**Lemma 2.4 (link orbits; proved here).** `𝒢` maps even links to even links and odd links to odd links. It acts transitively on the set of even links and on the set of odd links (links taken unoriented). Each site lies on exactly three even links and three odd links.

*Proof.* `𝒢` preserves each tiling. `LW1.md` line 201: "It sends even cube centres to even cube centres. It sends an odd centre \(c_0+\mathbf1+b\) to \(c_0+Q\mathbf1+Qb\), again an odd centre since \(Q\mathbf1-\mathbf1\in2\mathbb Z^3\)." Even translations preserve both tilings. A link lies in exactly one cube (A1), so `g` maps it into a cube of the same tiling. Of the two links of `x` along `e_i`, `(x, x + e_i)` is even exactly when `x_i` is even and `(x − e_i, x)` is even exactly when `x_i` is odd, so exactly one is even. For transitivity, `VC1_5_DRAFT.md` Lemma S2′(b): "`𝒢` acts transitively on sites. The stabilizer of `x` is cyclic of order 3, generated by the turn `h_x` about the line through `x` and the centre of its even cube. `h_x` permutes the three even-cube links at `x` in one 3-cycle and the three odd-cube links at `x` in another." Given even links `ℓ ∋ x` and `ℓ' ∋ x'`, take `g` with `gx = x'`. Then `gℓ` is an even link at `x'`, and a power of `h_{x'}` maps it to `ℓ'`. The same argument works for odd links. ∎

**Proposition 2.5 (which case; proved here).** Let `ω_0` be symmetric and `n ≥ 1`. The number `ϱ_n(D_ℓ)` takes one value `d_e` on all even links and one value `d_o` on all odd links. Then `F_n = Z^3` exactly when `d_e = 0` or `d_o = 0`. Equivalently, `F_n = Z^3` exactly when, under the Born law `ν_{2n}`, the actual configuration is almost surely constant on every cube of `𝒯_e`, or almost surely constant on every cube of `𝒯_o`. If `d_e = d_o = 0`, it is almost surely constant on all of `Z^3`.

*Proof.* `ϱ_n ∘ β_g = ϱ_n` and `β_g(D_ℓ) = D_{gℓ}` (proof of Theorem 2.2), so `ϱ_n(D_ℓ)` is constant on each `𝒢`-orbit of links, and Lemma 2.4 names the two orbits. If `d_e = 0`, each site has three even links with `ϱ_n(D) = 0`, and two of them are witnesses, so `F_n = Z^3`. Likewise if `d_o = 0`. Conversely, if `x ∈ F_n` with witness `y`, the link `{x, y}` is even or odd and has `ϱ_n(D) = 0`, so `d_e = 0` or `d_o = 0`. For the second form: the twelve edges of a cube are links of its tiling, and `ν_{2n}(ξ_u ≠ ξ_v) = ϱ_n(D_uv)`. The edge graph of a cube is connected, so zero disagreement on every edge forces all eight corners to agree almost surely. The converse holds because each even link lies in an even cube. If both values vanish, every link has disagreement probability zero. `Z^3` is connected, and a countable union of null events is null. ∎

So excitations spread through a stationary symmetric state do not make formation partial. They remove it. If the actual values differ with positive probability across one even link and across one odd link, then `d_e > 0` and `d_o > 0`, and the state is in case (N). A uniform gas of excitations of positive density above a dark vacuum is an example of such a state, whenever its excitations change the actual values on links of both tilings.

**Corollary 2.6 (record content in case (E); proved here).** In a symmetric stationary state of case (E), the record content `r_x = ξ_2(x)` is almost surely constant on every cube of a tiling whose links have `d = 0`. So the record pattern carries at most one value per cube.

*Proof.* Every site has `t_x = 1`, so `r = ξ_2`, whose law is `ν_2`. Apply Proposition 2.5 with `n = 1`. ∎

The content can be random. The mixture `(ω_dark + ω_full)/2` of the two dark states of `L_cube` in Corollary 2.7 is stationary and symmetric. Both components have `n_x` sharp at every site, so `D_xy = 0` in both, and Lemma 1.2 puts the mixture in case (E). Its records are all `0` or all `1`, with probability `1/2` each.

### 2.5 The states on file

**Corollary 2.7 (proved here, from the sources named).** Each state below is stationary and symmetric. Each state of a gauged law below is also locally gauge invariant. (The free seas are states of the free ticks, which have no links.)
- (a) Case (E). The dark vacua of `L5-O[S_+]`, `ω_0` and `ω'_0` (`VC1_5_DRAFT.md` Theorem O2, Remark O2.1). The dark witnesses `ω_m` of `L5-U[m]` for even `m`, and their full-matter partners (Theorem U3). On `L_cube`, the state `ω_dark` (matter vacuum, tracial links) and the state `ω_full` (full matter, tracial links).
- (b) Case (N). The free sea of the free cube tick and of the five-mode free tick. The tracial state of each law. The product states `ω_t` of `L5-U` for every finite `t` (Theorem U1).

*Proof.* (a) In each of these states the actual value is one sharp number at every site. In `ω_0` every `P_x = +1`, and in `ω'_0` every `P_x = −1` (`VC1_5_DRAFT.md` line 195: "In `ω_0` every `P_x = +1`; in `ω'_0` every `P_x = −1`"). In `ω_m`, `N_x = 0`, and `N_x` is gauge invariant, so `ω_m(N_x^2) = Φ_m(N_x^2) = 0`. The full-matter partner has `N_x = 5`. So `ω(D_xy) = 0` for every pair, and Theorem 2.3 gives case (E). Their stationarity, symmetry and gauge invariance are Theorems O2 and U3.

For `ω_dark` and `ω_full` on `L_cube`: each edge term `c_y^† J_ℓ c_x + c_x^† J_ℓ^† c_y` annihilates every vector whose matter is empty at both `x` and `y`, since `c_x` and `c_y` act first. It also annihilates every vector whose matter is full at both, since `c_y^†` and `c_x^†` act last on an occupied site. So each `H_C` vanishes on the subspace (empty matter) ⊗ (all link states), and on (full matter) ⊗ (all link states). Each matter gate is the identity there. `W_E` acts on links only and preserves the normalized trace. On every finite region the density matrix `|vac⟩⟨vac| ⊗ 1/d` is therefore fixed by the gates, and `ω_dark ∘ α = ω_dark` through the local construction of E1. The same holds for `ω_full`. A lift maps `n_x` to `n_{gx}` and acts on links by unitaries, so it fixes both states. A gauge transformation `e^{it𝒢_x}` is `e^{itn_x}` times a link unitary. The matter part fixes a state diagonal in occupations, and the link part fixes the trace. Both states have `n_x` sharp, so they are in case (E).

(b) The free sea: `LW1.md` B8a ("starting from the free sea, no record forms") for `n_x`, and `LW1_5_DRAFT.md` B8a-5 for parities and numbers. Its stationarity and symmetry are B10(3). The tracial state `τ` is invariant under every automorphism that maps local algebras to local algebras (`VC1_5_DRAFT.md` Lemma 2.4(a)). Under `τ` the site modes are independent fair bits. So on `L_cube`, `τ(D_xy) = 1/2` (`LW1.md` line 500). On `L5-O`, `τ((1 − P_xP_y)/2) = 1/2` (`VC1_5_DRAFT.md` line 160). On `L5-U`, the `N_x` are independent with law `Binomial(5, 1/2)`, so `τ(D_xy) = 1 − Σ_k (C(5,k)/32)^2 = 1 − C(10,5)/1024 = 772/1024`. For `ω_t` with `t` finite, the `N_x` are independent with law `p_k ∝ C(5,k) e^{−tk}`. Every `p_k > 0`, so `ω_t(D_xy) = 1 − Σ_k p_k^2 > 0`. In each case `D_xy` has positive expectation for every pair, and the state is in case (N). ∎

**Remark 2.8 (formation is not continuous in the state).** As `t → +∞`, the states `ω_t` of `L5-U` converge on every local element to `ω_{+∞}` (matter vacuum, tracial registers), because each site density `e^{−tN_x}/Z_t` converges to the vacuum projection. Every `ω_t` with finite `t` is in case (N), and `ω_{+∞}` is in case (E) (Theorem U1 includes `t = ±∞`; its `N_x = 0` is sharp). So the record behaviour can jump at a limit of stationary symmetric states. This is the same exactness that Lemma 1.2 shows for mixtures: PS-3c asks for probability one.

### 2.6 What this says about TM1(a)(2)

**Corollary 2.9 (proved here).** Let `ω_0` be stationary and symmetric, and let `Λ` be a finite box. The record count `|R_n ∩ Λ|` is a number, not a random variable (Lemma 1.1), so it equals its law-expected value. It is `0` at `n = 0`. For every `n ≥ 1` it is `|Λ|` in case (E) and `0` in case (N). Read "saturation" as "every site of the box carries a record". Then TM1(a)(2) holds for `ω_0` exactly in case (E), with saturation at `n = 1`. In case (N) the count stays `0` and TM1(a)(2) fails.

*Proof.* Theorem 2.3. ∎

---

## 3. Each hypothesis is needed

The examples use frozen configurations: product states on which every hop term of the base tick vanishes. `VC1_5_DRAFT.md` calls such states dark. This section first proves when a hop term vanishes, on each law.

### 3.1 Blocked hops

On `L_cube`, a *configuration vector* `|ν, ε⟩` has occupation `ν_x ∈ {0, 1}` at each site and value `ε_ℓ ∈ {−S, …, S}` of `E_ℓ` at each link of a finite region. For `ℓ = (x, y)`, `y = x + e_i`, write the edge term of `H_C` (`LW1.md` line 59) as `T_ℓ = c_y^† J_ℓ c_x + c_x^† J_ℓ^† c_y`, so `H_C = 3^{−1/2} Σ_{ℓ ⊂ C} η_i(x) T_ℓ`. Put `j(m) = (S(S + 1) − m(m + 1))^{1/2}`, the coefficient in `J|m⟩ = j(m)|m + 1⟩` (`LW1.md` line 40).

**Lemma 3.1 (blocked hops on `L_cube`; proved here).** `T_ℓ |ν, ε⟩ = 0` exactly when one of these holds:
- (a) `ν_x = ν_y`;
- (b) `ν_x = 1`, `ν_y = 0` and `ε_ℓ = S`;
- (c) `ν_x = 0`, `ν_y = 1` and `ε_ℓ = −S`.

Otherwise `T_ℓ |ν, ε⟩ = ± j |ν', ε'⟩ ≠ 0`, where `(ν', ε')` moves the particle across `ℓ` and changes `ε_ℓ` by `+1` if it moved from `x` to `y` and by `−1` if it moved from `y` to `x`, and `j = j(ε_ℓ)` or `j(ε_ℓ − 1)` respectively.

*Proof.* `c_y^† J_ℓ c_x |ν, ε⟩` is nonzero only if `ν_x = 1`, `ν_y = 0` and `ε_ℓ < S`. `c_x^† J_ℓ^† c_y |ν, ε⟩` is nonzero only if `ν_y = 1`, `ν_x = 0` and `ε_ℓ > −S`. The two conditions exclude each other, so at most one term is nonzero, and a nonzero term is a sign times `j` times a configuration vector. So `T_ℓ |ν, ε⟩ = 0` exactly when [`ν_x = 0` or `ν_y = 1` or `ε_ℓ = S`] and [`ν_y = 0` or `ν_x = 1` or `ε_ℓ = −S`]. For `ν_x = ν_y` both brackets hold. For `(ν_x, ν_y) = (1, 0)` the first needs `ε_ℓ = S` and the second holds. For `(0, 1)` the first holds and the second needs `ε_ℓ = −S`. ∎

Call `ℓ` *blocked* at `|ν, ε⟩` when (a), (b) or (c) holds. In words: a link between a full site and an empty site is blocked when its value sits at the end of the range that the hop away from the full site would leave.

**Lemma 3.2 (frozen configurations on `L_cube`; proved here).** Let `(ν, ε)` be a configuration of all of `Z^3` at which every link is blocked. Let `Φ` be the state whose restriction to each finite region is the vector state of `|ν, ε⟩` there. (On matter it is the quasi-free state with diagonal covariance `diag(ν)`, `LW1.md` line 97.) Then `Φ` is stationary under the base tick, invariant under every gauge transformation `Ad e^{it𝒢_x}`, and its Born law is the point mass at `ν`.

*Proof.* Every `H_C` kills `|ν, ε⟩` (Lemma 3.1), so every matter gate `e^{±iaH_C}` fixes it. `W_E = ∏_ℓ e^{−iτ_E E_ℓ^2}` multiplies it by a phase, since `ε_ℓ` is an eigenvalue of `E_ℓ`. For a local `A`, `α(A) = U_F^* A U_F` with `U_F` a finite product of gates (`LW1.md` E1). On a finite region containing their supports, `U_F |ν, ε⟩` is a phase times `|ν, ε⟩`, so `Φ(α(A)) = Φ(A)`. Each `𝒢_x = n_x + Σ_out E_ℓ − Σ_in E_ℓ` is diagonal in configuration vectors, so `e^{it𝒢_x}` multiplies `|ν, ε⟩` by a phase, and `Φ` is gauge invariant. The occupations are sharp. ∎

**Lemma 3.3 (blocked hops on `L5-U[m]`; proved here).** Let `v` be a product vector with definite site numbers `N_x` and definite end numbers `p_{ℓ,z}` (any vectors in those sectors). For `ℓ = (x, y)`, `h^U_ℓ v = 0` if one of these holds:
- (a) `N_x = N_y = 0`, or `N_x = N_y = 5`;
- (b) `N_x = 5`, `N_y = 0` and `p_{ℓ,x} = min(m, 5)`;
- (c) `N_x = 0`, `N_y = 5` and `p_{ℓ,y} = min(m, 5)`.

*Proof.* `h^U_ℓ = Σ_{j,k} c^†_{y,j} U^{jk}_ℓ c_{x,k} + Σ_{j,k} c^†_{x,k} U^{jk†}_ℓ c_{y,j}`, with `U^{jk}_ℓ = r^{ℓ,y}_j r^{ℓ,x†}_k` and `U^{jk†}_ℓ = r^{ℓ,x}_k r^{ℓ,y†}_j` (`VC1_5_DRAFT.md` line 58). Rishons commute with matter. (a) If both sites are empty, `c_{x,k}` kills the first sum and `c_{y,j}` the second. If both are full, `c^†_{y,j}` kills the first sum and `c^†_{x,k}` the second, since the other factors do not change the occupation of that site. (b) `c_{y,j}` kills the second sum. In the first sum, `U^{jk}_ℓ` acts on the register. If `m ≥ 5`, the `x`-end is full and `r^{ℓ,x†}_k` kills it. If `m ≤ 5`, the `y`-end holds `m − min(m, 5) = 0` rishons, `r^{ℓ,x†}_k` does not change it, and `r^{ℓ,y}_j` kills it. (c) The same with the roles of the ends exchanged: `c_{x,k}` kills the first sum, and `U^{jk†}_ℓ = r^{ℓ,x}_k r^{ℓ,y†}_j` kills the register, since the `y`-end is full or the `x`-end is empty. ∎

**Lemma 3.4 (blocked hops on `L5-O[S_+]`; proved here).** Let `v` be a product vector with definite occupation of the five modes at `x` and of the five modes at `y`, and with the rishon vacuum `|0⟩_ℓ ∈ S_+` on `ℓ = (x, y)`. If `x` or `y` is empty, `h_ℓ v = 0`.

*Proof.* Write `γ_{z,2j−1} = c_{z,j} + c^†_{z,j}` and `γ_{z,2j} = −i(c_{z,j} − c^†_{z,j})`, from `c_{z,j} = (γ_{z,2j−1} + iγ_{z,2j})/2`. Registers commute with matter, so `h_ℓ = (i/2) Σ_{a,b} U^{ab}_ℓ γ_{y,a} γ_{x,b}`. Collect the terms by matter monomial. The coefficient of `c^†_{y,k} c^†_{x,j}` is `U^{2k−1,2j−1} + iU^{2k−1,2j} + iU^{2k,2j−1} − U^{2k,2j}`, which `VC1_5_DRAFT.md` line 174 calls `𝒰^{++}_{kj} = 4i d^y_k d^x_j`. With `U^{ab} = iη^y_a η^x_b` (line 56) and `d_k = (η_{2k−1} + iη_{2k})/2`, the other three coefficients factor in the same way:
- `c^†_{y,k} c_{x,j}`: `U^{2k−1,2j−1} − iU^{2k−1,2j} + iU^{2k,2j−1} + U^{2k,2j} = i(η^y_{2k−1} + iη^y_{2k})(η^x_{2j−1} − iη^x_{2j}) = 4i d^y_k d^{x†}_j`;
- `c_{y,k} c^†_{x,j}`: `U^{2k−1,2j−1} + iU^{2k−1,2j} − iU^{2k,2j−1} + U^{2k,2j} = 4i d^{y†}_k d^x_j`;
- `c_{y,k} c_{x,j}`: `U^{2k−1,2j−1} − iU^{2k−1,2j} − iU^{2k,2j−1} − U^{2k,2j} = 4i d^{y†}_k d^{x†}_j`.

The first three register operators kill `|0⟩_ℓ`, since each has a rishon annihilator that acts on the vacuum or anticommutes past a creator of another mode onto it. The fourth comes with `c_{y,k} c_{x,j}`, which kills the matter vector when `x` or `y` is empty. ∎

So with the rishon vacuum on every link, every product vector of definite occupations in which no link joins two non-empty sites is killed by every `h_ℓ`. `W_E` multiplies it by a phase, since `Γ^x_ℓ |0⟩ = −|0⟩` (`VC1_5_DRAFT.md` line 176). The dark vacuum `ω_0` of Theorem O2 is the case with all sites empty.

On the five-mode laws the product state `Φ` of such a vector need not be gauge invariant, because a vector of definite occupation of each mode picks a frame. Use the gauge average `E` of `VC1_5_DRAFT.md` Lemma 1.1 and put `ω = Φ ∘ E`. That file's Lemma 1.1(c) makes `ω` gauge invariant. Its Lemma 1.1(d), "`E∘α = α∘E`, and `E∘β_g = β_g∘E`", gives `ω ∘ α = Φ ∘ α ∘ E = ω` when `Φ` is stationary, and likewise for each lift that fixes `Φ`. The actual values are gauge invariant (`P_x ∈ 𝔄^G`, `VC1_5_DRAFT.md` line 195; "`N_x` and `Q_x` are gauge invariant", line 250), so `D_xy ∈ 𝔄^G` and `ω(D_xy) = Φ(D_xy)`. Stationarity of `Φ` follows as in Lemma 3.2 from Lemmas 3.3 and 3.4.

### 3.2 Without rotations: partial formation in a stationary state

**Proposition 3.5 (proved here).** Take `L_cube` (any `S`), `L5-U[m]` (any `m`) or `L5-O[S_+]`, at any value of `ε, μ, τ_E`. On the five-mode laws, take the actual values of PS-3h5. Then there is a state `ω` that is stationary under the base tick, locally gauge invariant and invariant under the cell translations `2Z^3`. In `ω` a record forms at the end of tick 1 at every site of `Z^3 ∖ 2Z^3`, and no record ever forms at a site of `2Z^3`.

*Construction.* Mark the sites of `2Z^3`. No link joins two marked sites, since two marked sites differ by a vector with even coordinates.
- `L_cube`: `ν_x = 1` at marked sites and `0` elsewhere. On a link whose source is marked put `ε_ℓ = S`; on a link whose target is marked put `ε_ℓ = −S`; on every other link put `ε_ℓ = S`. Every link is blocked: with no marked end, (a); with a marked source, (b); with a marked target, (c). Let `ω = Φ` of Lemma 3.2.
- `L5-U[m]`: `N_x = 5` (the full vector) at marked sites and `0` elsewhere. On a link with a marked end, that end holds `min(m, 5)` rishons, in flavours `1, …, min(m, 5)`, and the other end holds the rest, in flavours `1, …, max(m − 5, 0)`. On every other link the source end holds `min(m, 5)` rishons and the target end the rest, in the same flavours. Every link is blocked by Lemma 3.3. Let `ω = Φ ∘ E`.
- `L5-O[S_+]`: one particle in mode 1 at each marked site (parity `−1`), empty elsewhere (parity `+1`), and the rishon vacuum on every link. Every link has an empty end, so Lemma 3.4 applies. Let `ω = Φ ∘ E`.

*Proof.* Stationarity and gauge invariance: Lemma 3.2 on `L_cube`, and the paragraph after Lemma 3.4 on the five-mode laws. Each rule depends only on which ends are marked, and `2Z^3` maps marked sites to marked sites. Even translations act without sign corrections (`LW1.md` A2: "Even translations preserve its phases exactly"; on `L5-U`, `VC1_5_DRAFT.md` Lemma C's proof: "Even translations need `d = 1`"). So `Φ` is translation invariant, and so is `Φ ∘ E` by Lemma 1.1(d) of `VC1_5_DRAFT.md`. The actual values are sharp: `1`, `5` or `−1` at marked sites, and `0`, `0` or `+1` elsewhere. A marked site differs from all six neighbours, so `ω(D_xy) = 1` for every neighbour and the site is never in `F_1`. An unmarked site `x` has at most two marked neighbours: if exactly one coordinate `x_i` is odd, the marked neighbours are `x ± e_i`; if two or three coordinates are odd, it has none. So `x` agrees with at least four neighbours, and `x ∈ F_1`. Theorem 2.1 gives `R_n = F_1 = Z^3 ∖ 2Z^3` for every `n ≥ 1`. ∎

The recorded sites have density `7/8`. By Theorem 2.2 the state cannot be invariant under all of `𝒢`, and indeed a rotation about `c_0` moves `0` to the other corners of `{0,1}^3`.

### 3.3 Without stationarity: a later formation tick in a symmetric state

Let `ψ_cc` be the product over the even cubes `C` of the matter state `(|0^8⟩⟨0^8| + |1^8⟩⟨1^8|)/2` on `C` (all empty or all full, with probability `1/2` each), with the tracial state on every link. It is an even product state over disjoint regions, so it is a state of `𝔄`.

**Proposition 3.6 (proved here).** On `L_cube`, assume `sin(a_o j(m)/√3) ≠ 0` for some `m ∈ {−S, …, S − 1}`. This holds at every window point when `S ≤ 3/2`, and for each `S` at all but finitely many values of `a_o`. Put `ω_0 = ψ_cc ∘ α^{−2}`. Then `ω_0` is symmetric and locally gauge invariant, it is not stationary, no record forms at tick 1, and a record forms at every site at the end of tick 2: `R_1 = ∅` and `R_n = Z^3` for `n ≥ 2`.

*Proof.* *Symmetry and gauge invariance.* Each `g ∈ 𝒢` maps even cubes to even cubes (proof of Lemma 2.4). Its lift maps `n_x` to `n_{gx}`, so it maps the cube state of `C` to that of `gC`, and it acts on links by unitaries, which fix the trace. So `ψ_cc ∘ β_g = ψ_cc`. A gauge transformation `e^{it𝒢_x}` is `e^{itn_x}` times a link unitary, which fixes a state that is diagonal in occupations and tracial on links. The tick commutes with the lifts (L1) and with the gauge transformations (`LW1.md` E1: the base layers "fix every \(e^{it\mathcal G_x}\)"), so `ω_0 = ψ_cc ∘ α^{−2}` inherits both invariances.

*Tick 2.* `ϱ_2 = ψ_cc`. Under `ψ_cc` each site agrees almost surely with its three even neighbours, which lie in its even cube. So `F_2 = Z^3`.

*Tick 1.* By Theorem 2.2 it suffices to show `x_0 := (1,1,1) ∉ F_1`. Now `ϱ_1 = ψ_cc ∘ α^{−1}`, and `α^{−1}(A) = U_0 A U_0^*`. Take a finite union `Λ` of even cubes that contains the supports of the gates involved (E1). On `Λ`, `ψ_cc` has the density matrix `ρ = Σ_v p_v |v⟩⟨v|`. The sum runs over the configuration vectors `v = |ν, ε⟩` with `ν` constant on each even cube of `Λ`, and each weight `p_v` is positive. Since `D_{x_0 y}` is a projection,

`ϱ_1(D_{x_0 y}) = Σ_v p_v ‖D_{x_0 y} U_0^* v‖^2 ≥ p_v ‖D_{x_0 y} U_0^* v‖^2` for each such `v`.

Here `U_0^* = M_e^* M_o^* W_E^*` stands for the finite product of the gates involved, in that order: `W_E^*` acts first on `v`, then `M_o^*`, then `M_e^*`. Write `C_0 = {0,1}^3`, `C^o_0 = {1,2}^3` (the odd cube of `x_0`), `x_1 = x_0 + e_1 = (2,1,1)` and `C_1 = (2,0,0) + {0,1}^3` (the even cube of `x_1`). Each odd cube meets eight even cubes, in one corner each, because its corner `b + 1 + r` lies in the even cube with index `b/2 + r`.

*The odd neighbours of `x_0`.* Let `v_1` have `ν = 1` on `C_0` and `ν = 0` on the other even cubes of `Λ`. Set every odd link at a corner of `C_0` to its blocking value: `ε = S` where the corner is the source, `−S` where it is the target. Set every other link to `ε = S`. Every link is blocked at `v_1`. Even links inside `C_0` join two full sites, odd links at corners of `C_0` are blocked by choice, and all other links join two empty sites. So `U_0^* v_1` is a phase times `v_1` (Lemma 3.2). For each odd neighbour `y` of `x_0`, `ν_{x_0} = 1` and `ν_y = 0`, so `‖D_{x_0 y} U_0^* v_1‖ = 1`.

*The even neighbours of `x_0`.* Let `v_2` be `v_1` with new values on three links:
- `ℓ = (x_0, x_1)`, an odd link with source `x_0`, gets `ε_ℓ = m`, with `m < S` as in the hypothesis;
- the two even links `(x_1 − e_2, x_1)` and `(x_1 − e_3, x_1)` of `C_1`, with target `x_1`, get `ε = −S`.

The other links at `x_0` and `x_1` keep the values of `v_1`. These are `ε = S` on the three even links `(x_0 − e_i, x_0)` (target `x_0`), on the other two odd links of `x_0` (source `x_0`), on the other two odd links `(x_1, x_1 + e_2)`, `(x_1, x_1 + e_3)` of `x_1` (source `x_1`), and on the even link `(x_1, x_1 + e_1)` (source `x_1`).

At `v_2` every link except `ℓ` is blocked, and `ℓ` is not: `x_0` is full, `x_1` is empty and `ε_ℓ < S`. Let `b_2` be `v_2` with the particle moved from `x_0` to `x_1` and `ε_ℓ = m + 1`. At `b_2` every link except `ℓ` is blocked. The even links of `x_0` now join a full source to the empty target `x_0` with `ε = S`, which is (b). The other two odd links of `x_0` join two empty sites, which is (a). The five links of `x_1` other than `ℓ` join the full site `x_1` to empty sites: as source with `ε = S`, which is (b), or as target with `ε = −S`, which is (c). All other links are as at `v_1`. So by Lemma 3.1, every cube generator except `H_{C^o_0}` kills `v_2` and `b_2`, and `H_{C^o_0} v_2 = σh b_2`, `H_{C^o_0} b_2 = σh v_2`, with `h = j(m)/√3` and a sign `σ` (`η_1 = 1`; `T_ℓ` is Hermitian, so both entries carry the same sign). Hence

`U_0^* v_2 = ζ [cos(a_o h) v_2 − iσ sin(a_o h) b_2]`, with `|ζ| = 1`:

`W_E^*` gives the phase `ζ`, `M_o^*` acts on the span of `v_2, b_2` through its `C^o_0` factor `e^{−ia_o H_{C^o_0}}`, and `M_e^*` fixes both vectors. For an even neighbour `y` of `x_0`, `D_{x_0 y} v_2 = 0` (both full) and `D_{x_0 y} b_2 = b_2` (`x_0` empty, `y` full). So `‖D_{x_0 y} U_0^* v_2‖^2 = sin^2(a_o h) > 0`.

So `ϱ_1(D_{x_0 y}) > 0` for all six neighbours, `x_0 ∉ F_1`, and `F_1 = ∅`. Then `ϱ_1 ≠ ϱ_2`, so `ω_0` is not stationary. Finally, for `S ≤ 3/2` take `m = −S`: `j(−S) = (2S)^{1/2} ≤ √3`, so `0 < a_o h ≤ a_o < π`. For any `S`, `a_o h ∈ πZ` holds for at most finitely many `a_o ∈ (0, π)`. ∎

[check: section 3.5 confirms the support claims for `v_1`, `v_2`, `b_2` with the full generators on the `4^3` torus.]

### 3.4 Without both: progressive formation

On `L_cube`, fix `m ∈ {−S, …, S − 1}` and put `x = 0`, `y = e_1`, `ℓ = (x, y)`. `ℓ` is an even link of `C_0`. Let `|x⟩` be the configuration vector with one particle at `x` and `ε_ℓ = m`. Every other link at `x` or at `y` takes its blocking value for a particle at that site: `ε = S` where that site is the source, `−S` where it is the target. All other sites are empty and all other links have `ε = S`. Let `|y⟩` be the same with the particle at `y` and `ε_ℓ = m + 1`.

Put `θ = a_e j(m)/√3` and `φ = τ_E(2m + 1)`, and let

`U = diag(e^{iφ/2}, e^{−iφ/2}) · (cos θ − i sin θ σ_x)`

in the basis `(|x⟩, |y⟩)`. Let `q ∈ {1, 2, …} ∪ {∞}` be its order up to scalars: the least `q ≥ 1` with `U^q ∈ C·1`.

**Proposition 3.7 (proved here).** Assume `sin θ ≠ 0`, and let `1 ≤ k ≤ q`. Let `ω^{(k)}` be the vector state of `U^{−k}|y⟩`, extended outside a finite region by the configuration state of Lemma 3.2. Then `ω^{(k)}` is a locally gauge-invariant state of `L_cube`. In it every site other than `x` and `y` forms its record at tick 1, and `x` forms its record exactly at tick `k`. If `q ≥ 3`, then for `k = 3` no record forms anywhere at tick 2, and one forms at `x` at tick 3. For `S = 1/2`, at every window point, `φ = 0`, `θ = a_e/√3`, `q ≥ 4`, and `q = ∞` exactly when `a_e/(√3 π)` is irrational.

*Proof.* *The dynamics.* At `|x⟩` and at `|y⟩` every link except `ℓ` is blocked. At `x` and `y` the values were chosen for that purpose, and every other link joins two empty sites. By Lemma 3.1 the span of `|x⟩, |y⟩` is invariant, every cube generator except `H_{C_0}` kills it, and `H_{C_0}|x⟩ = h|y⟩`, `H_{C_0}|y⟩ = h|x⟩` with `h = j(m)/√3`. There is one particle, so no fermion sign enters, and `η_1(0) = 1`. Per tick, `U_0 = W_E M_o M_e` acts on the span as follows. `M_e` acts by `e^{−ia_e H_{C_0}} = cos θ − i sin θ σ_x`. `M_o` acts as the identity. `W_E` acts by `diag(e^{−iτ_E m^2}, e^{−iτ_E (m+1)^2})` times a common phase, which is a phase times `diag(e^{iφ/2}, e^{−iφ/2})`. So `U_0` acts as a phase times `U`, and the state at the end of tick `n` is the vector state of `U^{n−k}|y⟩`.

*Gauge invariance.* `|x⟩` and `|y⟩` have the same eigenvalue of every `𝒢_z`. At `x`: `1 + m + κ_x` against `0 + (m + 1) + κ_x`. At `y`: `0 − m + κ_y` against `1 − (m + 1) + κ_y`. Here `κ_x`, `κ_y` collect the other links, which are the same in both. At other sites nothing differs. So `U^{−k}|y⟩` is a joint eigenvector, and its vector state is gauge invariant.

*Records.* Let `p_n = |⟨x|U^{n−k}|y⟩|^2`, the probability that the particle is at `x` at tick `n`. A site other than `x, y` is empty almost surely at every tick, and at least four of its neighbours lie outside `{x, y}` and are empty too. So it records at tick 1. If `p_n = 0`, then `n_x = 0` almost surely, and the five neighbours of `x` other than `y` are empty, so `x ∈ F_n`. If `p_n > 0`, every neighbour `w ≠ y` has `P(n_x ≠ n_w) = p_n > 0`, and `P(n_x ≠ n_y) = 1`, so `x ∉ F_n`. So `t_x` is the least `n ≥ 1` with `U^{n−k}|y⟩ ∈ C|y⟩`.

*The order.* Write `U = e^{iχ} W` with `W ∈ SU(2)`, `W = cos β + i sin β (u·σ)`, `u` a unit vector. `U` is not diagonal, because its off-diagonal entries have modulus `|sin θ| ≠ 0`. So `sin β ≠ 0` and `(u_1, u_2) ≠ (0, 0)`. Then `W^r = cos(rβ) + i sin(rβ)(u·σ)` is diagonal exactly when `sin(rβ) = 0`, that is, when `W^r = ±1`. So `U^r|y⟩ ∈ C|y⟩` exactly when `U^r ∈ C·1`, exactly when `q` divides `r`. For `1 ≤ n < k`, `1 ≤ k − n ≤ k − 1 < q`, so `q` does not divide `n − k`. At `n = k` it does. Hence `t_x = k`.

*`k = 3`.* At tick 2, `p_2 > 0`, so `x ∉ F_2`. Also `y ∈ F_2` would need `p_2 = 1`, that is, `U^{−1}` anti-diagonal. But an anti-diagonal `U` has `U^2 ∈ C·1`, so `q ≤ 2`, which is excluded. Every other site recorded at tick 1. So no record forms at tick 2, and `x` records at tick 3.

*`S = 1/2`.* The only value is `m = −1/2`. Then `j(m) = 1` and `2m + 1 = 0`, so `θ = a_e/√3` and `φ = 0`. So `U = e^{−iθσ_x}`, and `U^r ∈ C·1` exactly when `rθ ∈ πZ`. Since `0 < θ < π/(2√3)`, this needs `r > 2√3`, so `q ≥ 4`, and `q = ∞` exactly when `θ/π` is irrational. ∎

**Corollary 3.8 (new records at every tick; proved here).** Take law data with `sin θ ≠ 0` and `q = ∞`, for example `S = 1/2` with `a_e/(√3 π)` irrational. For every `k ≥ 1`, place one copy of the construction at `x_k = (8k, 0, 0)`, `y_k = x_k + e_1`, with vector `U^{−k}|y_k⟩`. Take the product state. For every `n ≥ 1`, some site forms its first record at the end of tick `n`.

*Proof.* `ℓ_k = (x_k, y_k)` is an even link, since `8k` is even. The copies are at sup-distance at least 6 apart. No cube, no link and no copy-test neighbourhood meets two copies. The blocking values of different copies sit on disjoint links. So each copy evolves as in Proposition 3.7, and `t_{x_k} = k`. Each copy's vector has odd parity, but its vector state is parity invariant, so the infinite product of these even states on disjoint regions is a state of `𝔄`. ∎

**Remark 3.9.** On a box that contains the first `K` copies, the record count rises at every tick from 1 to `K` and then stays constant. It never reaches the size of the box, because no `y_k` ever records: that would need `U^{n−k}` anti-diagonal, which forces `q ≤ 2`. Every record at a site `x_k` reads `0`. These states are built for the purpose, through the choice of the initial vector `U^{−k}|y_k⟩`. Section 5 uses them only to show that progressive formation does not contradict PS-3c.

### 3.5 The [check]

`/tmp/toe-tm1/check_blocked.py` builds the dressed generators `H_C` of `L_cube` on the `4^3` torus with periodic tilings and signs, with all twelve edge terms, the `J` matrix elements and Jordan-Wigner signs. For `S = 1/2, 1, 3/2, 2` and every allowed `m` it reports PASS on four claims. (1) The configuration of Proposition 3.5 is killed by all sixteen cube generators. (2) In the construction of Proposition 3.7, only `H_{C_0}` acts, as `h σ_x` with `h = j(m)/√3`. (3) `v_1` of Proposition 3.6 is killed by every generator. (4) On `v_2` and `b_2`, only `H_{C^o_0}` acts, with modulus `h`, and every even cube generator kills both. The script ran in under a second and used 15 MB. It uses the same definitions as the proofs. It confirms the support bookkeeping and the orientation conventions, and it proves nothing.

---

## 4. Excitations above a stationary state

For a set `Λ` of sites, let `𝔄(Λ)` be the algebra generated by the sites of `Λ` and the links with both ends in `Λ`. Put `Λ^{+r} = {x : dist_∞(x, Λ) ≤ r}`.

**Lemma 4.1 (light cone of the base tick; proved here).** On each live law, `α^n(𝔄(Λ)) ⊆ 𝔄(Λ^{+2n})` for every `n ≥ 0`, and `α` maps even elements to even elements.

*Proof.* `α(A) = M_e^* M_o^* W_E^* A W_E M_o M_e`, built locally as in `LW1.md` E1. A gate whose support is disjoint from that of `A` commutes with `A`, since gates are even (E1: "A further gate disjoint from \(F\) commutes with \(A\), by evenness"). The factors of `W_E` act on single links, so `W_E^* A W_E ∈ 𝔄(Λ)`. The odd cubes that meet `Λ` lie in `Λ^{+1}`, since a cube has sup-diameter 1, and their links have both ends in the cube. So conjugation by `M_o` maps `𝔄(Λ)` into `𝔄(Λ^{+1})`. In the same way conjugation by `M_e` maps `𝔄(Λ^{+1})` into `𝔄(Λ^{+2})`. Conjugation by even unitaries keeps elements even. Induction on `n` finishes the proof. ∎

This is the backward cone that `LW1.md` B8b(i) uses for one tick: "the union lies within supremum distance three of \(x\)".

**Theorem 4.2 (excitations; proved here).** Let `ω_0` and `ω_v` be states of a live law with the base tick, and let `B` be a set of sites with `ω_0(A) = ω_v(A)` for every even `A ∈ 𝔄(Z^3 ∖ B)`. Let `n ≥ 1` and `dist_∞(x, B) > 2n + 1`. Then `x ∈ F_n(ω_0)` exactly when `x ∈ F_n(ω_v)`, and `x ∈ R_n(ω_0)` exactly when `x ∈ R_n(ω_v)`.

*Proof.* For `y, z ∈ N(x)`, `D_xy + D_xz` is even and lies in `𝔄(B_∞(x, 1))`. By Lemma 4.1, `α^n(D_xy + D_xz)` is even and lies in `𝔄(B_∞(x, 2n + 1))`. The ball avoids `B`, so this algebra lies in `𝔄(Z^3 ∖ B)`. Hence `ω_0(α^n(D_xy + D_xz)) = ω_v(α^n(D_xy + D_xz))` for every pair, and the two states have the same witnesses at `x`. For `R_n`, the condition `dist_∞(x, B) > 2n + 1 ≥ 2j + 1` holds for every `j ≤ n`, so membership in each `F_j` agrees. ∎

**Corollary 4.3 (above a case-(E) state; proved here).** If `F_1(ω_v) = Z^3`, every site at sup-distance at least 4 from `B` records at tick 1 in `ω_0`. If `B` is finite, every record of `ω_0` formed after tick 1 lies in `B^{+3}`, so at most `|B^{+3}|` records form after tick 1 in the whole history.

*Proof.* Theorem 4.2 with `n = 1`. A site carries at most one record. ∎

**Corollary 4.4 (above a case-(N) state; proved here).** If `R_n(ω_v) = ∅` for every `n`, then `R_n(ω_0) ⊆ B^{+(2n+1)}` for every `n`.

*Proof.* Theorem 4.2. ∎

**Remark 4.5 (which states agree outside `B`).**
- (i) Local unitary excitations. Let `W ∈ 𝔄(B)` be unitary and either even or odd, and put `ω_0(A) = ω_v(W^* A W)`. For even `A ∈ 𝔄(Z^3 ∖ B)`, `A` commutes with `W` (an even element commutes with every element of disjoint support), so `W^* A W = A` and `ω_0(A) = ω_v(A)`. This covers excitations that add one fermion, such as `W = c_x + c_x^†`.
- (ii) Product states. Let `ω_v` be a product over the sites and links, as the frozen states of section 3 and the dark states of Corollary 2.7 are. Then any product state that differs from it only on the sites of `B` and the links that meet `B` agrees with it outside `B`. On the five-mode laws this survives the gauge average. For `A ∈ 𝔄(Z^3 ∖ B)`, `E(A)` integrates the gauge unitaries of the sites of `A`, and their action on links outside `A`'s support cancels, so `E(A) ∈ 𝔄(Z^3 ∖ B)`.
- (iii) The tracial state. `τ` is a trace, so `τ(W^* A W) = τ(A)` for every unitary `W ∈ 𝔄`. Every unitary excitation of `τ` is `τ` itself, and it never forms a record (Corollary 2.7).

---

## 5. What TM1 needs for an arrow of time

### 5.1 TM1-i's first question

Under PS-3c, with the reading on file, record formation in a stationary symmetric state is one bit: case (E) or case (N) (Theorem 2.3). "Where" has the answer everywhere or nowhere. "Why" has the answer exact agreement: the actual values agree with probability one across every link of one tiling (Proposition 2.5). No partial and no progressive formation occurs in this class, and in no state is formation a random event (Lemma 1.1). So VC1(a)(4), "whether records form there; TM1-i", has a two-valued answer for every candidate vacuum that is stationary and symmetric. Which value holds is VC1's choice of state (`VC1_5_DRAFT.md` line 314). The free sea is in case (N), and `LW1U_SEA_DRAFT.md` line 371 adds: "in the free sea the actual configuration itself is frozen, not only the records".

The tension of `TOE_ASSEMBLY.md` line 144 reads differently on the two five-mode laws. On `L5-O` the dark vacuum `ω_0` is half filled ("so `ω_0(N_x) = 5/2`", Theorem O2) and in case (E). So a half-filled, stationary, symmetric, gauge-invariant vacuum there forms records, all of them at tick 1. On `L5-U` and `L_cube`, the half-filled stationary symmetric states on file are the tracial states (`ω_{t=0}` of Theorem U1 on `L5-U`), which are in case (N). Theorem U2 and Corollary U2′ exclude half filling for the symmetric states that are pure on the gauge-invariant algebra.

### 5.2 TM1(a)(2)

In case (E), TM1(a)(2) holds, with saturation at tick 1 (Corollary 2.9). The arrow it gives is a single step: `R_0 = ∅` and `R_n = Z^3` for every `n ≥ 1`. Records tell tick 0 apart from every later tick, and they tell no two later ticks apart. Their content is one value per cube at most (Corollary 2.6), and in the dark vacua it is the same value at every site. In case (N), TM1(a)(2) fails.

TM1(a) states its items "For every history of `L`". Item (2) is false for some states of the law. Read "saturation" as "every site of the box carries a record". Then on each live law the tracial state never forms a record, and the state of Proposition 3.5 stops at density `7/8`. The free sea of the free tick never forms one either. Under any reading of "saturation", the state of Proposition 3.7 on `L_cube` with `k = 3` is a counterexample: its count stays flat from tick 1 to tick 2 and then rises at tick 3. So TM1(a)(2) can hold only on a restricted class of initial states, or in a changed form. That class is the question LW1-R left (`LW1.md` line 500: "Specify the law-admissible initial-state domain on which the axiom that records form is required"), which Amendment 1 moved to TM1 as TM1-i.

### 5.3 An arrow beyond tick 1

If `R_n` is to grow at more than one tick, the initial state must be non-stationary (Theorem 2.1) and must not be invariant under any site-transitive group of lifts (Theorem 2.2). Such states exist (Proposition 3.7, Corollary 3.8). The theorems above say this about the natural candidates:
- A local excitation of a case-(E) vacuum adds at most `|B^{+3}|` records after tick 1, all near its support (Corollary 4.3). The excitation then moves through sites that already carry records, and "A site never carries more than one record". So in a dark vacuum, no later event leaves a record on a vacuum site outside `B^{+3}`.
- A local excitation of a case-(N) vacuum forms records only inside its cone `B^{+(2n+1)}` (Corollary 4.4). For the tracial state every unitary excitation is trivial (Remark 4.5(iii)). For the free sea, whether some local excitation forms records at infinitely many ticks is not decided here.

So under PS-3c as on file, a record arrow that grows over many ticks is a property of the initial state, not of any stationary symmetric vacuum. The main-branch arrow note says the same for its toy, with a redundancy functional in place of PS-3c: "The sign of the candidate arrow is therefore an **output** fixed entirely by the initial condition, with the dynamics held fixed", and "from the **`I/d` equilibrium** (max-entropy) state, `R_red` is exactly **flat**". That note is context here, not a proof step.

What TM1 then needs is stated here as a consequence, not as a proposal. TM1(a)(2) needs a class of initial states that lies outside the stationary symmetric states, apart from case (E) with its one-step arrow. Or it needs a restatement whose claim is the one-step arrow of a case-(E) vacuum. Either is a choice for the lead and the owner, and either would need the four-test check. This file proposes neither.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemma 1.1 (rebuilt from `LW1.md` E3 and B9): under PS-3c the formation sets, record sets and first-record times are functions of the state sequence. Formation at a given site and tick has probability 0 or 1 for every state, and only the record content is random.
- Lemma 1.2: a mixture forms a record only where every component does, with a common pair of witnesses.
- Lemma 1.3: on all three laws every `g ∈ 𝒢` has a lift that commutes with the tick and maps the actual value at `x` to the one at `gx`. On `L5-O`, `β_g(P_x) = P_{gx}`.
- Theorem 2.1: in a stationary state every record that ever forms, forms at tick 1.
- Theorem 2.2: in a state invariant under a site-transitive group of lifts, at each tick records form everywhere or nowhere, so all records form at one tick `n*`.
- **Theorem 2.3 (TM1-D):** take `L_cube`, `L5-O` or `L5-U`, any free constants and any site-covariant actual values. Every stationary symmetric state forms a record at every site at tick 1 (case (E)), or never forms one (case (N)). Gauge invariance is not used. The case is decided at one site.
- Lemma 2.4 and Proposition 2.5: `𝒢` is transitive on even links and on odd links. Case (E) holds exactly when the actual values agree with probability one across every link of one tiling, that is, when the configuration is almost surely constant on every cube of that tiling. Corollary 2.6: in case (E) the record content is one value per cube at most.
- Corollary 2.7: the dark vacua of `L5-O` and of `L5-U` (even `m`), and the dark states of `L_cube`, are in case (E). The free seas, the tracial states and the states `ω_t` of `L5-U` at finite `t` are in case (N). Remark 2.8: the case jumps at the limit `t → ∞`.
- Corollary 2.9: in a stationary symmetric state, TM1(a)(2) holds exactly in case (E), with saturation at tick 1.
- Lemmas 3.1-3.4: blocked hops on `L_cube`, `L5-U` and `L5-O`; frozen configurations are stationary and, after the gauge average, gauge invariant.
- Proposition 3.5: on all three laws, a stationary, gauge-invariant, cell-translation-invariant state records at tick 1 on `Z^3 ∖ 2Z^3` and never on `2Z^3`.
- Proposition 3.6: on `L_cube`, when `sin(a_o j(m)/√3) ≠ 0` for some `m` (every window point if `S ≤ 3/2`), the symmetric, gauge-invariant state `ψ_cc ∘ α^{−2}` forms no record at tick 1 and a record at every site at tick 2.
- Proposition 3.7 and Corollary 3.8: on `L_cube`, a gauge-invariant state whose site `x` first records at tick `k`, for every `k` up to the order `q` of a two-by-two unitary of the law. For `S = 1/2`, `q ≥ 4` at every window point, and `q = ∞` when `a_e/(√3π)` is irrational. With `q = ∞`, a product of copies forms new records at every tick.
- Lemma 4.1, Theorem 4.2 and Corollaries 4.3-4.4: a state that agrees with `ω_v` on the even observables outside `B` has the same formation as `ω_v` outside `B^{+(2n+1)}` at tick `n`. Above a case-(E) state, at most `|B^{+3}|` records form after tick 1. Above a case-(N) state, records stay in `B^{+(2n+1)}`. Remark 4.5: every unitary excitation of the tracial state is trivial.

**Counterexamples.**
- To "a stationary, gauge-invariant, cell-translation-invariant state forms records everywhere or nowhere": Proposition 3.5, on all three laws.
- To "a symmetric, gauge-invariant state forms its records at tick 1 or never": Proposition 3.6, on `L_cube` at the law data stated.
- To TM1(a)(2) as a statement about every history: Proposition 3.7 with `k = 3`, on `L_cube` (for example `S = 1/2` at every window point), under any reading of "saturation". With "saturation" read as "every site of the box carries a record", also the tracial state and Proposition 3.5 on each live law, and the free sea.
- To "record formation is continuous in the state": Remark 2.8.

**Open, by name.** None for this lane's target. Theorem 2.3 decides TM1-i's first question. Section 5.3 asks whether some local excitation of the free sea forms records at infinitely many ticks. This lane did not attack that question, so it names no open lemma for it.

**What changes downstream.**
- TM1: TM1-i's first question has the answer no. In a stationary symmetric state records form everywhere at tick 1 or never. TM1(a)(2) holds in case (E) with a one-step arrow and fails in case (N). As a statement about every history it is false (Proposition 3.7). TM1(a)(2) needs a stated class of initial states outside the stationary symmetric ones, or a restatement that claims the one-step arrow. That choice belongs to the lead and the owner (section 5.3).
- VC1: VC1(a)(4) is one bit for each stationary symmetric candidate, read off one link of each tiling (Proposition 2.5). On `L5-O` the half-filled dark vacuum is in case (E).
- BR1: in case (E) a record pattern carries at most one value per cube (Corollary 2.6), and in the dark vacua it carries none. After tick 1, a local excitation of a case-(E) vacuum can leave records only in `B^{+3}` (Corollary 4.3), so records of later events cannot form on vacuum sites outside `B^{+3}`.
- For the owner, one fact and no proposal: PS-3c asks for agreement with probability one under the whole state, so mixtures and limits of states can lose formation (Lemma 1.2, Remark 2.8).
