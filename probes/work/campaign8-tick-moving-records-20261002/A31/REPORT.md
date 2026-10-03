*(Saved by the coordinator from the agent's final message; the agent's sandbox blocked it from writing REPORT.md.)*

# A31 report: assembly v2 of the Option R package, and where it breaks

**Paths.** SP = `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`. No git, no repo edits, no review or audit lanes.

**A29.** A29 landed during this lane. Its corrections C27–C55 are folded in and cited where used: C27, C29, C30, C31, C33, C35, C38, C39, C40, C53 and C54.

**Grades.**
- **EXACT**: a proof, or exact arithmetic.
- **CHECKED**: numerics in a stated toy, with a tolerance.
- **ARGUED**: reasoning without proof.
- **SUPPLIED**: a premise put in by hand.
- **COMPARATOR**: literature quoted from memory, never adopted.

All models are supplied toys, and every rule is a named conditional. I1–I6 are the owner's instincts, not positions.

---

## 1. Question

Put Option R together as one model:
- records that form and step on ticks (the swap step SW and the claim rule CL);
- possibilities that change smoothly between ticks, holding records fixed;
- matter, the gravity field, their coupling, and formation (gated, catch first).

Then answer six things:
1. State the model in one place, with the status of each ingredient.
2. Is the Kogut–Susskind (KS) sign pattern forced for light-cone matter? Is it supplied, or covariant up to a relabelling? Can records show it?
3. Can matter's 2×2×2 cell and the field's 2×2×2 role layout be one shared choice?
4. Sweep pairs of ingredients for conflicts.
5. List the supplied items, ranked, with the owner decisions.
6. Name the top open problem and the smallest next calculation.

## 2. The assembled model

**Status codes.**
- **AX**: axiom text.
- **Q**: owner-decided reading.
- **C7-Sn**: unadopted Campaign 7 sentence n.
- **I-n**: owner instinct.
- **NC**: named conditional.
- **SP**: supplied pattern.
- **PREP**: supplied initial condition.
- **PROP**: proposed text, not approved.

| # | Ingredient | In the model | Status | Source |
|---|---|---|---|---|
| **Arena** | | | | |
| 1 | Sites | Z³, nearest-neighbour adjacency, translations, proper rotations about each site; no edge | AX (I6 is axiom text) | axioms |
| 2 | One site | One qubit, M₂(C); no possibility privileged | AX | axioms |
| 3 | Shared possibilities | One joint description on the ordinary (ungraded) tensor product. When a record forms, the possibilities change at once to agree (Lüders cut). | Q1 for sharing and "at once"; C7-S1/S3 for the form (C43) | BRIEF |
| **Records** | | | | |
| 4 | Records | They form. Each locks one admissible possibility, at most one per site. Only records are readable, by content. | AX | axioms |
| 5 | Permanence | Never destroyed. A record may move next door by trading places, keeping its content. A swap is not re-forming (C40). | NC "move-permanence"; decision 7 | A13 M4, A27 |
| 6 | Ticks | In this option, records form and step only on ticks, at most one site per tick. In the continuum reading (D13) these become rates. | I1, I2 via NC R-a; decision 18 | A27 |
| 7 | Step rule SW | Kraus √(c/z)·SWAP·√W, plus a stay outcome. The blind weight W = 1 is preferred: no back-action, and no energy change in calm surroundings (D11). | NC SW. C40 gaps: is the moved content admissible at its new spot? Blind odds ignore unrecorded neighbours. | A27 |
| 8 | Claim rule CL | A contested site takes one record, with relative odds | NC. Range 2 (C40). Drops out in the continuum reading (ARGUED). | A27 |
| **Change** | | | | |
| 9 | Between record events | e^{−iH_R t}, with H_R = Q_R H Q_R. Records act as walls and fixed fields. | C7-S2, read as compression. Q2 holds between record events (C53). | A27 |
| 10 | Form of H | Homogeneous, glued, a sum of nearest-neighbour pair terms. The only allowed terms are J σ·σ + K σ^aσ^a + D(σ_x × σ_{x+a})_a (EXACT). | C7-S2 + Q3 | D1 |
| 11 | Calm forces Heisenberg | Calm forces K = 0. Once any record holds the content −n, it also forces D = 0, so H = J Σσ·σ (EXACT). | consequence | D2 |
| 12 | Theorem N | Possibilities take A20's quasi-locality exit and records take the irreversible exit. The two fit together, so records still move at most one site per tick (EXACT by construction). There is no strict cone for unrecorded influence. | C27, C38, C52 | A20, A27 |
| **Formation** | | | | |
| 13 | Instruments | Chance tr(Fρ); lock odds taken after the update; no-record update √(1−F) | C7-S3, S4 ("if those hold") | A9 |
| 14 | Gate | F^(∅) = 0, gated on the records present before the event | NC G, plus NC start-of-tick (drops out in the continuum reading) | A28 |
| 15 | Enclosure | What a fully surrounded spot does | NC | A28 |
| 16 | Settled formation | The weight sits on caught configurations and acts slowly; cost ≈ κħΓ_f per record | NC; one supplied toy (C35); decision 14 | A24 |
| 17 | Menus | Records cut to agree set the frames; unrecorded possibilities shape the odds only linearly | Q7 + PROP menu text | A16 C4 |
| 18 | Preparation | Initial records, with every content on the calm axis | PREP | A28 |
| 19 | Q4 | Read as "given that a record forms" | reading (C51) | A28 |
| **Calm emptiness** | | | | |
| 20 | Calm class | \|n⟩^⊗ everywhere; every record content ±n; the axis is law-fixed or inherited | NC; decision 16 (C30) | A13, A28 |
| 21 | Its ripples | One analytic band (z = 2); no cone without a supplied pattern | EXACT | D3 |
| **Matter** | | | | |
| 22 | Light-cone matter | A supplied π-flux sign pattern (KS, up to gauge). Glued form η_b Jσ·σ, or hop-only form η_b(XX+YY)+ZZ. | SP "M-KS"; decision 17 | D4–D6 |
| 23 | Mass | Hop-only form: on-site μεZ. Glued form: no clean nearest-neighbour mass found. | SP; ARGUED | D7 |
| 24 | Cone energy | In the glued form, a site-sum-0 gauge puts the cone exactly at the calm vacuum's energy (E_c = 0) | part of SP; CHECKED | D7 |
| 25 | Coupling | Lapse on every term, frame on every hop (F2, G1). The ST classing applies only to two-site masses. Shear needs a taste-singlet operator beyond nearest neighbours; it is neither a nearest-neighbour term (C31) nor shareable with the roles (D9). | NC; SP sandwich and cells | A26 |
| 26 | Lapse-weighted record odds | F = N̂⊗F_m; SW odds multiplied by N̂ | NC | C17, A23 |
| **Gravity field** | | | | |
| 27 | Field conditionals | F1 never locked; F3 energy–momentum source; F4 at state level only (D15); F5 | NC (C33) | A23 |
| 28 | Role layout | F6, 1 of 8; needed in continuous time too | SP (C29) | A25 |
| 29 | Payload | More than one qubit per site, or a compilation (OPEN) | Qubit-level (C54); decision 13 | A25 |
| 30 | Lapse | D16 makes the lapse a dynamical field component (harmonic form), which adds payload | NC; ARGUED | K4 |
| 31 | Field places | Field places never hold records | NC, new (EXACT consequence) | D10 |
| 32 | Field numbers | Speed relative to light; G; β | SP numbers; β OPEN | C33, C55 |

## 3. Answers to tasks 2–6

### Task 2: is KS forced, supplied, or shown by records?

**Answer: inside the model's own class, yes, and more strongly than "seems to need" (EXACT).** The class is a calm product vacuum, left exactly unchanged by a homogeneous, glued, nearest-neighbour pair generator.
- **(i) The generator must be plain Heisenberg.** Once any record holds the content −n, H = J Σσ·σ (D2).
- **(ii) Single excitations form one analytic band.** So there is no cone anywhere (D3). This is exact at harmonic order for any change that keeps a product vacuum exact.
- **(iii) A cone needs π flux, and only signs are available.** A Dirac-like cone needs at least two bands, so translations must act projectively, with π flux through every face. Glued pair terms give real hops, so only signs can do this. The π-flux sign pattern is unique up to gauge: that is KS (D4, given A10 S8).
- **So KS is the minimal supplied ingredient,** not something the axioms produce.

**KS is SUPPLIED in both available forms (EXACT, D5).**
- **Glued form (signs on the whole exchange).** No on-site relabelling maps σ·σ to −σ·σ: their spectra are {1,1,1,−3} and {3,−1,−1,−1}. So the gauge is physical, and the law is not covariant even up to relabelling.
- **Hop-only form (A10's Z·G·Z).** A site-dependent Z relabelling realizes all 24 turns of space alone. But the change then privileges the possibility axis z, and only 8 of the 24 glued turns survive. That is against Q3 and against the Qubit axiom. Q3 as decided does not provide site-dependent relabellings either; using them would be a further owner decision.

**Do records show the pattern under smooth change? (CHECKED: c3, c3b; D6.)**

| Form | Setting | Shows in records? | Largest TV over placements |
|---|---|---|---|
| Hop-only | Z menus and contents, starts that are record configurations, a step that carries the bond sign | No (EXACT) | ≤ 8e-15 |
| Hop-only | Option R's pattern-blind swap step | Yes | 0.37 (2D), 0.10 (3D) |
| Hop-only | X-type records on two sites | Yes | 0.29 |
| Hop-only | Coherent (non-record) starts without re-phasing (cf. A10 S13c) | Yes | 0.05–0.58 |
| Glued | One excitation, site sums not uniform | Yes | 0.54 (3×3 patch), 0.19 (3D box) |
| Glued | Uniform site sums, one excitation | No (EXACT: covariant in that sector) | ≤ 1e-14 |
| Glued | Uniform site sums, two interacting excitations | Yes | 0.081 |
| Glued | Uniform site sums, a record with content −n nearby | Yes | 0.45 |

- **Two zeros on the 4×2 torus are accidents.** One is the glued KS gauge with one excitation; the other is hop-only with a content-0 swap. Both come from a chiral symmetry of potential-free bipartite hopping (D6).

**Spatial doubling.** As A27 noted, smooth change moves the doubler from time into space.
- One qubit per site cannot host a two-component naive Dirac generator: each site offers one excitation state (EXACT counting).
- KS absorbs the spatial partners into the 2³ cell. In 3D that leaves 2 tastes and net chirality 0 (A10; A27 Step 7).

**Outside the class (OPEN).** Possible escapes are an entangled calm vacuum with emergent π flux, composite excitations, a graded product, or more room per site.
- A20's two covariant calm stabilizer vacua, the star and face states, do not work as hosts: their single defects are immobile.
- No Pauli operator moves a lone defect by any of the 215 displacements on a 6³ torus.
- Their degeneracy grows linearly with L, a fracton-like signature (CHECKED c5; COMPARATOR X-cube).

### Task 3: one shared cell?

**Answer: no for the glued form (EXACT). Yes only in the hop-only form, at the cost of the gluing, and only if a cell-free shear coupling exists (OPEN).**

**Theorem S (EXACT).** For any sign pattern with π flux through every plaquette:
- **Statement.** The rotations about a site that preserve the pattern exactly lie in the tetrahedral group T or in a 4-element C4. They never include a face-diagonal half turn.
- **Proof.** The half turn about the face diagonal through x maps the plaquette (x, x+e_a, x+e_a+e_b, x+e_b) onto itself and swaps its bonds in pairs. That forces the plaquette product to be +1, contradicting π flux.

**Consequence.**
- **The field's layout keeps every turn.** A25's layout is kept by all 24 turns about every vertex-role and cube-role site, and every plaquette touches such a site. So no π-flux pattern shares the layout's symmetry.
- **Checks (c2, c2c).** 0 of 2¹² patterns invariant under all 24 turns about a site have π flux; 2048 T-invariant ones do. Every pattern invariant under the layout's symmetry group G_s has flux +1.

**Matter's own best pattern is also 1 of 8, but of a different kind (c2b).**
- Among all 128 period-2 π-flux patterns, the largest symmetry group has 24 of 192 cosets: T with no shift, plus the quarter turns and face-diagonal half turns only combined with a (1,1,1) shift.
- This group is not conjugate to the layout's group (EXACT, by hand). It echoes A16's (1,1,1) shift.
- Tied to the layout, the joint symmetry is T: 12 of the 24 turns survive, and the joint structure is 1 of 16.

**Partly shareable.**
- **Yes:** the one-site staggered mass sign (−1)^{Σ(x−s)}.
- **No (EXACT, c2):**
  - any dimerization mass, and the ST classing it needs: a role-invariant bond modulation has no momentum-π part along its own bond;
  - 2×2×2 blocks, which keep only 3 of the 24 turns;
  - A26's in-cell sandwich: a site-centred half turn moves all 16 in-cell diagonal pairs out of cell.

**Hop-only form.** The signs carry no layout label (the gauge is a Z relabelling), and the mass sign can be tied to the layout. So one label s suffices, provided three things:
1. The change accepts a privileged possibility axis. Gluing is then lost for 16 of the 24 turns.
2. Masses are one-site, so the ST classing is unneeded (A26 D6: one-site masses fall alike).
3. A cell-free, taste-singlet shear operator centred on face-role sites exists. This is OPEN (COMPARATOR: staggered shift symmetry, Kluberg-Stern et al. 1983).

### Task 4: consistency sweep

| # | Pair | Conflicts | Grade |
|---|---|---|---|
| K1 | SW/CL vs smooth change | **(a)** No logical conflict: linear, complete, no signalling, records stay pure (A27/A28). **(b)** A swap changes ⟨H⟩ next to unrecorded excitations (a jumping mirror), but not in calm surroundings with contents ±n. In a full-rank sea, a sudden wall jump excites the sea, so moving records need calm surroundings. **(c)** A pattern-blind swap exposes hop-only KS (up to 0.37). A signed swap does not, but then the step must know the matter pattern. **(d)** C40: in the calm class every frame is the n-frame, so a moved ±n content fits it. Whether it has nonzero odds against what the spot held before is decision 15. **(e)** Claim contests drop out in the continuum reading. | (a) A27/A28; (b) EXACT that ΔE = 0 when calm and ΔE ≠ 0 generically; magnitude ARGUED; (c) CHECKED; (d, e) ARGUED |
| K2 | Gate vs catch first | **(a)** Compatible: traps sit beside records. **(b)** No linear weight fires only on settled possibilities (A24 V5), so weights must sit on caught configurations, at a cost ≈ κħΓ_f. **(c)** Edge floor (A28) × unsettled cost (A24): next to a full-rank sea every nonzero weight forms unsettled records with Planck-scale ghosts. So the calm emptiness is forced at matter's edges. **(d)** Trap records must step much more slowly than Γ_f, which is itself small: in effect they are still. **(e)** Catch-and-emit is not in the model's own change yet (C35): J Σσ·σ conserves number, so emission needs a second excitation or a field sector. | (b) EXACT; (c) EXACT (combination); (a, d, e) ARGUED |
| K3 | Catch first vs field source F3 | **(a)** Settled means zero ghost on average (A24 V2). **(b)** F4 cannot hold as an operator identity on all states if records register anything: an operator-commuting lock is sterile (A23(f) + A24 V1). So F4 holds at state level only. **(c)** Swaps near excitations, and claims with content or activity weights, also inject energy. Blind swaps in calm surroundings do not. **(d)** Lapse-weighted odds slightly cut the field's lapse possibility at every event, about (c/12)(√N₁ − √N₂)² per event. | (a, b) EXACT; (c) mixed (EXACT for blind/calm, ARGUED otherwise); (d) ARGUED |
| K4 | Lapse pacing the field (D16) vs tick-free possibilities | **(a)** "Change per tick" pacing is unavailable for possibilities. Pacing must be an operator inside H (F2), which is linear and does not signal. **(b)** With a fixed lattice time the lapse cannot be a free gauge multiplier. It must be a dynamical component (harmonic form, A23 D19) whose static value is −U, which adds payload (C54). **(c)** Record odds must carry N̂ too, so record clocks redshift with the rest. **(d)** No seam mirrors arise, since possibilities do not tick (C38). | (a) EXACT; (b) ARGUED; (c) EXACT (linearity); (d) ARGUED |
| K5 | Records as walls vs light and gravity through matter | **(a)** A record locks the whole M₂ domain and compression holds it, so F1 + Record + one qubit per site force field places never to record. **(b)** Otherwise, one record per nucleon walls the field: gravitational waves in the Earth would get a mass ≈ 2.9e-9 eV, far above ħω ≈ 4e-13 eV at 100 Hz, and would die within about 70 m. Waves that crossed the Earth have been detected (COMPARATOR). **(c)** Light. Gauge-type light: point walls scatter as Rayleigh dipoles, negligibly. Scalar-type light: s-wave scattering with mean free path a/(Cap₁u), also negligible for sparse points. But nucleon-sized recorded balls would fail water and fibre transparency. | (a) EXACT; (b) EXACT arithmetic + ARGUED + COMPARATOR; (c) ARGUED |
| K6 | A14's photon-mass bound vs walls | **(a)** Δω² = Cap₁·u with Cap₁ = 3.957. The bound m_γ ≲ 1e-18 eV then needs u ≲ 1.7e-93 per Planck site where light crosses. **(b)** Under the gate, no records form in voids, and they diffuse only about 1e-5 m in the universe's age, so voids pass. **(c)** In water, one record per nucleon gives ≈ 1.2e-9 eV, below ordinary dispersion. **(d)** For gauge light, isolated walls give an index shift ∝ u, not a mass (COMPARATOR: Maxwell-Garnett). | (a) EXACT arithmetic; (b–d) ARGUED |
| K7 | Calm vacuum vs light-cone matter | No cone without a supplied pattern. This sharpens C30 from "not built" to "impossible in the class". | EXACT |
| K8 | KS vs the field's roles | Not shareable in the glued form; the hop-only form breaks the gluing | EXACT |
| K9 | Calm stabilizer vacua vs mobile matter | Single defects are immobile | CHECKED |
| K10 | Strict record cone vs Option R's tails | Record places obey the gate's cone; record statistics leak faint tails (A27 Step 9) | EXACT |

### Task 5: supplied-items ledger and owner decisions

**Ledger, ranked by cost to the axioms (1 = costliest).**

| Rank | Item | Cost |
|---|---|---|
| 1 | More than one qubit per site for the field, or a compilation (OPEN) | Changes Qubit's one-site domain |
| 2 | A privileged possibility axis: the calm direction if law-fixed (decision 16). In the hop-only form, the same axis also sits inside the change. | Against "No possibility is privileged". The hop-only form also breaks Q3 for 16 of 24 turns. |
| 3 | Matter's π-flux sign pattern (glued form) | A law-level pattern that records show; against "No site is privileged"; not shareable with rank 4 |
| 4 | Field layout F6, 1 of 8 | A state-level, superselected pattern under a covariant law: milder |
| 5 | Field places never record (new) | A rule tying where records form to the roles |
| 6 | F1, F3, F4 (state level), F5, a dynamical lapse (D16), F2/G1 couplings, field speed relative to light, G | New dynamics clauses |
| 7 | A shear operator beyond nearest neighbours (cell-free version OPEN); a Dirac mass; the ST classing only for two-site masses | Terms beyond "a sum of nearest-neighbour terms" |
| 8 | Move-permanence (swap) and "admissible" for a moved record | Record's "permanent" and "locks" wording |
| 9 | Campaign 7's S1–S4, with S2 read as compression and S4 as "no nonlinear signalling" | The unadopted one clause |
| 10 | Blind swap weight; lapse-weighted odds | Small new rules |
| 11 | Gate, preparation, enclosure rule | Within reading note 2's freedom. An absorbing empty state touches "A law privileges no states". |
| 12 | Settled (catch-first) formation | Within the formation freedom |
| 13 | Ticks (I1/I2), or the continuum reading | Wording |
| 14 | Q4 read as "given formation"; the menu text | Wording |

**Dissolved here.**
- A26's dose form and block order: stepping artifacts, gone in the smooth limit (C31(v), ARGUED).
- The cone offset: fixed by the choice of gauge (CHECKED).
- The ST split: needed only for two-site masses.
- In the continuum reading: the claim rule, start-of-tick gating, the ordering rule and the dose per tick.

**Owner decisions, de-duplicated against the draft's 0–18 (plain language; nothing here is adopted).**
1. **Decision 17, sharpened.** Light-like matter needs a fixed sign pattern, in one of two versions:
   - **The version that keeps your gluing.** Records can tell sub-grids apart, and the pattern can never share the field's 8 layouts. It lacks the quarter turns the field's layout has (proved). That means two patterns.
   - **The signs-on-hopping-only version.** It can be hidden from records along the calm direction, provided record steps carry the signs. It can share the field's layout. But the change itself then favours one direction, and 16 of the 24 turns are no longer treated alike.
   - Which version, if either?
2. **New: records only at matter places.** A never-locked field on one qubit per place means field places must never hold records. Accept that rule?
3. **Decision 13, sharpened.**
   - The "time-stretch" that paces the field becomes a moving part of the field, so each place needs more settings.
   - The field's bookkeeping can hold only on average over records, never exactly for every state, if records are to register anything (exact).
4. **Decision 18, sharpened.**
   - The chance per tick of forming a record must shrink with the tick, or regions freeze.
   - The chance per tick of stepping must shrink too, or records outrun light.
   - Ticks then become bookkeeping, and four choices disappear: the claim rule, start-of-tick gating, the formation order, and the change per tick.
5. **Decisions 15 and 16 are linked.** In the calm picture a moved record always fits its new spot's frame. What remains: does "admissible" mean "in the frame", or "possible for what the spot held before"?
6. **Decisions 4 and 14 together.** If records form only next to records and only on caught things, empty space next to matter must be the tidy kind (exact). Records that form a trap must also stay still.

### Task 6: the single most important open problem

**The problem.** Can a homogeneous, glued, star-local change on one qubit per site give light-cone excitations over a calm vacuum, with every pattern at the state level?

**Why it matters most.**
- **Calm product vacua: no.** This lane proves it for every one of them (EXACT).
- **Known stabilizer vacua: no.** The two known covariant calm stabilizer vacua also fail, because their single defects are immobile (CHECKED).
- **That forces both patterns.** It is why the package needs both KS and F6, and those cannot be one choice (Theorem S).
- **Payload is the same obstruction.** The field's payload problem (C54) is the field-side face of it.
- **A yes would change the picture.** If the vacuum itself supplied the flux, KS would become a superselected state label like F6, and might be shared.

**The smallest next calculation.** An exact Clifford search over F₂, taking seconds per candidate, over A20's equivariant module (O-covariant, translation-invariant stabilizer states of low degree; A20 C3). For each candidate:
- **(a) Calm?** Test calmness: frustration-free, with an annihilating projector weight.
- **(b) Mobile?** Test single-defect mobility with c5's F₂ rank test.
- **(c) Emergent flux?** If a defect is mobile, compute the commutation phase of the x- and y-movers around a plaquette. A phase of −1 means emergent π flux supplied by the vacuum itself.

## 4. Derivations

**D1. Covariant pair terms (EXACT; CHECKED c1).**
- **Bond stabilizer.** It is generated by the C4 about the bond axis and the C2 about x through the bond midpoint (which swaps the two sites).
- **Under C4.** {1, σ^z} span A and {σ^x, σ^y} span E. The invariants are four from A⊗A and two from E⊗E (δ and ε).
- **Under the C2 with swap.** It keeps σ^z₁ − σ^z₂ (which telescopes), σ^zσ^z, σ^xσ^x + σ^yσ^y and σ^xσ^y − σ^yσ^x.
- **CHECKED.** The invariant space is 5-dimensional (residuals ≤ 2.7e-15; non-covariant controls give 1.41).

**D2. Calm forces Heisenberg (EXACT; CHECKED c1b).** Write m = ⟨n̄|σ|n⟩, with m ⊥ n, m·m = 0 and m×m = 0.
- **Double flips.** They are bond-local and independent across bonds, with amplitude K(m^a)². So K = 0.
- **Single flips from D.** At x they come from the two a-bonds, with amplitudes ∓D(n×m)_a, and cancel by translation invariance.
- **Next to a −n record.** The compressed term is −(n×σ_y)_a, the cancellation fails, so D = 0.
- **J alone.** The double-flip amplitude is m_x·m_y, zero only when n_x = n_y. So the only product eigenstates are uniformly aligned.
- **CHECKED on a 3×3 torus.**
  - DM residual: ≤ 7e-16 with no records, 3.3–4.0 next to a −n record.
  - Heisenberg residual: ≤ 1.7e-14.
  - Compass residual: 2.6–4.2.
- **Superseded run.** `c1`'s open-cube DM line was a boundary artifact.

**D3. No cone over a calm product vacuum (EXACT at harmonic order).**
- **The band is analytic.** An exact product eigenstate gives ⟨2 flips|H|Ω⟩ = 0, so B(k) = 0 and the energy is A(k) = Σ t_d e^{ik·d}, a single analytic band.
- **A cone is excluded.** A cone |k − k₀| is non-differentiable at k₀.
- **When it is exact.** It is exact for J alone.
- **With D.** The one-flip block has uniform Peierls phases (zero flux). D also couples one flip to two (weight 9.96).
- **Bogoliubov cones need a non-calm vacuum.** A Bogoliubov cone √(A² − |B|²) needs B ≠ 0, i.e. a vacuum that is not exactly stationary.
- **CHECKED.** The plain band is −4JΣ(1 − cos k), to 6.8e-14 on 8³.

**D4. What a cone needs (EXACT, given A10 S8/S13b).**
- Two or more bands need an enlarged cell or flux; an isotropic linear cone needs anticommuting velocity matrices, i.e. π through every face.
- J gives real hops and D zero flux.
- Equal fluxes on Z³ imply gauge equivalence, so the pattern is KS up to gauge.

**D5. The two forms (EXACT).**
- **Glued form.** A relabelling would need V(σ_x·σ_y)V† = −σ_x·σ_y, which the spectra forbid.
- **Hop-only form.** G = ΠZ^{g} gives G H_η G = H_{η^g}. Glued symmetry survives only for the 8 turns that fix z up to sign.
- **DM signs.** Sign patterns on DM terms are not relabelling-equivalent either: no single on-site turn flips all three axes' DM terms (ARGUED).

**D6. Readability (EXACT arguments; CHECKED c3, c3b).**
- **Hop-only form.** G commutes with Z projectors, with compression onto Z contents, and with Z-product starts.
- **Pattern-blind swap.** G·SWAP_xy·G = SWAP·Z_xZ_y when g_x ≠ g_y, so the moved possibility gets an extra Z the law never applies.
- **Signed swap.** SWAP·Z_y^{[η=−1]} restores covariance.
- **X-type records.** They flip under G.
- **Glued form.** On-site energies −2J s_x are not gauge-covariant unless the site sums s are uniform. Interactions and the field of a −n record depend on the individual signs.
- **Accidental zeros.** A chiral symmetry of real, potential-free, bipartite hopping puts the moved component π/2 out of phase, so the extra Z cancels.

**D7. Masses and cone energy.**
- **No staggered one-site potential from pair terms (EXACT).** Σε_x s_x = Σ_b w_b(ε_i + ε_j) = 0, and DM has no diagonal part on one flip.
- **Clean dimerization needs a special pattern (EXACT; enumeration of 128).** Dimerization is clean only if each axis sign is independent of its own coordinate. All such π-flux patterns are period 2, and none has uniform site sums.
- **On the site-sum-0 pattern (CHECKED c4).**
  - The cone sits exactly at E = 0, with levels ±4J√(Σcos²k) to 6.8e-14.
  - 10% dimerization leaves zero modes.
  - The role-symmetric modulations and a staggered next-nearest exchange do not gap it.
  - The hop-only μεZ gaps all bands at 2μ = 0.6.
- **Grade.** "No clean nearest-neighbour glued mass" is ARGUED beyond the tested terms.

**D8. Theorem S.** As stated in Task 3. The maximal subgroups of O that avoid the six face-diagonal half turns are T (order 12) and C4 (order 4).

**D9. Bond- and block-classed structures (EXACT; CHECKED c2).**
- A site-centred half turn reverses the bond axis, so a G_s-invariant modulation has no longitudinal-π part.
- Blocks keep 3 of the 24 turns at all 8 offsets.
- A site-centred half turn moves 16 of 16 in-cell diagonal pairs out of cell.

**D10. Field places never record (EXACT).** Record plus Qubit means a record locks the whole M₂ domain of its site, and compression holds it. So F1 forbids hosting the field on any site that ever records.

**D11. Swap energy.** ΔE = Σ(c/z)(⟨SWAP H′ SWAP⟩ − ⟨H⟩).
- It is 0 for content n in calm surroundings (EXACT).
- It is 0 for content −n in calm surroundings, by translation invariance (EXACT).
- It is generically nonzero next to excitations.

**D12. Wall mass.** m_eff = √(Cap₁u)·m_P. EXACT arithmetic: the Earth gives 2.86e-9 eV with a range of 69 m; water gives 1.22e-9 eV.

**D13. Continuum reading (ARGUED; COMPARATOR: piecewise-deterministic processes, Blanchard–Jadczyk).**
- Formation chances must scale as c = γτ to avoid Zeno freezing (A27 Step 8).
- Step chances must also scale, or records outrun the Lieb–Robinson speed: with 6Jτ < 1, one site per tick is faster than the change.
- Same-tick coincidences then cost O(τ²) per pair and drop out.

**D14. Calm stabilizer vacua (CHECKED c5).**
- A single Pauli flips 4 star defects or 8 face defects.
- No pattern {x, x+v} lies in the F₂ span on 6³, so a single defect cannot move.
- The rank deficit is 4L (star) or 16L − 24 (face), for L = 4, 6, 8.

**D15. F4 at state level only (EXACT).** An operator-level constraint needs [P_k, ρ̂(y)] = 0 for every y, which gives [P_k, H] = 0. By A24 V1 the record is then sterile.

## 5. Checks

All runs went through `run.sh`: `nice -n 10`, all four thread caps at 1, a 55 s alarm, and a load gate at 6. One run was skipped at load 6.12 and rerun at 3.21. Loads at run time were 1.9–4.0.

| Script | Key results | Time, memory |
|---|---|---|
| `c1_pairterms` | Covariant pair space has dim 5; chirality annihilates aligned states (2.4e-16). The DM stationarity line is superseded by `c1b`. | 0.15 s, 63 MB |
| `c1b_periodic` | DM ≤ 7e-16 (calm) and 3.3–4.0 (−n record); compass 2.6–4.2; one flip → two flips 9.96 | 0.55 s, 167 MB |
| `c2_patterns` | 3 orbits, flux +1; KS site sums {−2, 2, 6}; uniform-sum gauges (2 and 0) exist on 4³; best symmetry 24/192; blocks 3/24; 16/16 pairs moved out of cell | 0.83 s, 35 MB |
| `c2b_stab` | The stabilizer is T at shift 0, plus 12 elements at shift (1,1,1) | 0.66 s, 28 MB |
| `c2c_pointstab` | π-flux patterns: 0 of 2¹² (O); 2048 (T) | 17.7 s, 27 MB |
| `c3_readability`, `c3b_scan` | The tables in Task 2; the Heisenberg control is 0 throughout | ≤ 0.6 s, 35 MB |
| `c4_cone` | Plain band 6.8e-14; site-sum-0 cone at E = 0 (6.8e-14); masses as in D7 | 0.24 s, 42 MB |
| `c4b_mass`, `c4c_mass_enum` | Annealing (inconclusive) was superseded by exhaustive enumeration: 0 of 128 | 4.1 s, 0.1 s |
| `c5_defects` | 0 of 215 displacements (star and face); rank deficits as in D14 | 0.16 s, 28 MB |

- **Tolerance.** "Zero" means ≤ 1e-14.
- **Not run.** The Task 6 Clifford search.

## 6. Real-physics match (comparators flagged)

- **Matter.** The KS count gives two tastes and net chirality 0, and doubling persists (COMPARATOR: Kogut–Susskind 1975; Susskind 1977; Nielsen–Ninomiya 1981).
- **Emergent route.** Emergent π flux would mirror Affleck–Marston and Wen's projective symmetry groups (COMPARATOR).
- **What the calm class allows.** Only z = 2 magnons (COMPARATOR: Holstein–Primakoff).
- **Gravitational waves.** They crossed the Earth (COMPARATOR: LIGO/Virgo sky coverage), so the field must not be walled by records (D10).
- **Light.** The photon-mass bound of ~1e-18 eV (COMPARATOR: PDG) is met in gated voids.
- **Vacua.** The star and face vacua are fracton-like (COMPARATOR: X-cube, Haah).
- **Falsifiers.**
  - Gravitational waves screened by matter.
  - Quadratic dispersion in anything meant as light.
  - Period-2 effects at Planck scale; these are invisible at long wavelength.

## 7. Open edges

1. The Task 6 Clifford search, then non-Clifford calm entangled vacua.
2. A cell-free, taste-singlet shear operator on face roles, and whether it is truly taste-blind.
3. A clean nearest-neighbour glued Dirac mass, or a proof that none exists.
4. Tails of record statistics in the continuum reading (COMPARATOR: dissipative Lieb–Robinson bounds, Poulin 2010).
5. Patterned calm product vacua when compass terms are allowed.
6. Catch-and-emit inside J Σσ·σ.

## 8. Plain-language summary

Put together, tonight's best shape works for records. They sit still or swap with an empty neighbour, they never pile onto one spot, faraway choices cannot steer them, and empty space far from records stays exactly quiet. But this lane found a sharp limit on everything else. If empty space is the tidy, lined-up kind that the shape needs, a rule that treats every spot and every turn alike can only make slow, heavy ripples over it, never anything that moves like light. To get light-like matter, a fixed pattern of plus and minus signs must be painted onto the rule. That pattern either lets records tell neighbouring sub-grids apart, or makes the rule favour one direction of the possibilities. It also can never be the same pattern the gravity field needs, because the field's pattern keeps the grid's quarter turns and this one cannot (proved). A field that is never recorded also needs its own places where records never form. So the record side holds up, but light, matter and gravity each still need something put in by hand. The most useful next step is a quick exact search for an empty background whose own structure supplies that pattern.