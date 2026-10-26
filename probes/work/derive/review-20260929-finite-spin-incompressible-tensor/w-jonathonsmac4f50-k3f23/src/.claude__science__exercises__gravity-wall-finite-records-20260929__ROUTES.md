# Steps 4, 6 and 7 — routes, kill verdicts, ranking

**Step 4: independent routes.** Four agents (Claude Fable 5.1; same vendor
family as the supervisor, so not independent referees) worked from the same
neutral brief (`agents/neutral_brief.md`, the precise wall and the premise
ledger, with the supervisor's route clusters withheld). Each had a
different lens:
1. condensed matter;
2. quantum-gravity programmes;
3. the axioms' own structure and the exact price;
4. arguing that the wall is misframed.

Their texts are in `agents/agent1…agent4`. Every agent did the refresher
read and said which surfaces it read.

**Step 6: kill round.** Four fresh agents, same family, were each given
routes proposed by others and told to break them. Their texts are in
`agents/kill1…kill4`, with scripts in `scripts/agents/`.

## Portfolio with kill verdicts

| ID | Route | Proposed by | Premise dropped or changed | Kill verdict | The decisive reason |
| --- | --- | --- | --- | --- | --- |
| F1 | **Price lemma.** An exact additive rule on finite slots puts every sector-preserving local Hamiltonian in the "character class", so the TT sum rule is O(q⁴) in every state | agents 1 and 3 | none; it names the price | **wounded** | Correct for spin-type slots. The "every term preserves the sector" step was already known (probe 15's Fable remark). It is not the whole price: an in-domain exit remains, the incompressible channel (F2). "Wall ⇔ one premise" is blocked-equivalent; the price is three premises |
| F2 | **Strong coupling or incompressible channel** | agents 1 and 3 | harmonic level (S4) | **wounded** | The killer derived a state-independent corollary. The TT electric density conserves its dipole and has no local conjugate. So with the exact rule and a local metric, a light-like graviton must be a composite (the stored field a derivative of its momentum), and its partners would have to be gapped non-perturbatively. No mechanism is known; Gu–Wen's "N-type" candidate is self-declared unreliable |
| F3 | **A non-ground (population-inverted) state** supplying Einstein's negative compression weight | agent 2 | the ground-state premise | **dead** | Test T1 (below) plus the kill round: the cancellation needs an exact knife edge; the inverted channel is a tachyon, or a frozen ghost under Fierz–Pauli; the ±1 modes become a flat zero-frequency band, which is still gapless; interactions make a negative-energy channel decay. The registry argument was a category error |
| F4 | **Gravity as an equation of state of entanglement** (Jacobson; first law; area law) | agents 1, 2 and 3 | the lattice tensor carrier (S1) | **dead as an escape** | It needs a metric to define areas, boosts (Lorentz invariance) and a universal area coefficient. The kill check found the cubic lattice Dirac sea's area-law coefficient differs by 16–18 % between (110) and (100) cuts: not universal. Lemma MI (records as a Markov field) is correct but irrelevant, and the Markov-field reading is itself an added premise |
| F5 | **Induced (Sakharov) graviton** from the walker sea | agent 4 | finite slots (S2, S11) | **dead as a route** | It needs a posited metric field, which is option A relabelled; induced gravity supplies the action, not the field. Its leftover computation, the helicity ±1 block of the induced action, survives as a one-day check with FAIL expected. The same check finds TT birefringence of 3.9 from the cubic lattice unless tuned |
| F6 | **Observational purity.** Radiating sources couple to helicity ±1 modes as strongly as to TT on direction average | agent 4 | the target (S8) | **wounded, survives narrowed** | Verified exactly: the ratio is 1 by representation theory. With the probe 20 floor, the double pulsar excludes partners slower than about 12 × the TT speed. Faster partners are unnatural but not excluded by the quoted data. Static decoupling needs a local conserved momentum density, which lattice matter may lack (probe 6 T9) |
| F7 | **Statics first** (PPN γ and β) | agent 4 | the order of work | **dead** | Already landed: blocks 59, 60, 144 and 145 give GR's perihelion, conditional and unaudited. The 0.834 × GR figure was a coordinate artefact |
| F8 | **Prediction: test A1 fails at bounded range** (Hojman–Kuchař–Teitelboim, Bahr–Dittrich) | agent 2 | locality at the effective level (S5) | **wounded** | It is consistent with block 112, but the cited theorems assume the continuum Dirac algebra (Leibniz, Jacobi) or Regge calculus. It restates the pre-registered FAIL. The predicted lapse-fixing residual already appears on the matter side (block 150), before A1's second order |

## Step 7: ranking

Ranked by what a route would change if it worked, divided by its cost.

| Rank | Route | Family | What you would have to believe | Terminal obligation | Strength vs target | Cost | First artifact | What it changes | Stop/reopen condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Consolidate the price (F1 + F2's corollary) | character class plus the dipole-conservation corollary | nothing new | a note stating the three-exit price, checked | weaker than the target (it is a price) | a note and one referee cycle (1–2 days) | the corollary proof, with its numeric check (`scripts/agents/`) | It turns probes 10–21 into one statement the owner can act on. The owner's options are complete for the fixed grid only if exit (b) or (c) is also judged | reopen if a mechanism for exit (b) or (c) is named |
| 2 | The helicity ±1 block of the induced action (F5's leftover) | a one-loop zone integral in probe 6's runner | option A is chosen | the E-irrep O(q²) block | not target-equivalent | one day | one projector in probe 6's runner | It prices option A: whether a posited metric plus the lattice matter brings partners or birefringence without extra tunings | stop if FAIL with no symmetry reason |
| 3 | Exit (c): non-perturbative gapping of a composite graviton's partners | beyond harmonic order | a strong-coupling mechanism exists | a model where the composite's ±1 partners are gapped and TT stays linear | target-equivalent in the exact-rule domain | unbounded | none known | everything, if it worked | reopen only with a named mechanism |

Not ranked, because dead or answered: F3, F4, F5 as routes, F7 and F8.

## Approach families

See `APPROACH_REGISTRY.md`.
