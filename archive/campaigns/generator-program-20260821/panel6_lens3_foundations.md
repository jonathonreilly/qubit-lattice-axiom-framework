# Panel 6 — Lens 3: Foundations (Born-rule derivation landscape)
Read: DECISION_MEMO_20260821 §§1-5; RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05; analyses/born-rule-
derivation-2026-03-30; ADMISSIBILITY_..._INTERPRETATION_DISCRIMINATORS_..._2026-08-21 (N5 fence
per_site/per_scope, N6, N7). External strategies are REFERENCED as targets to re-prove, never borrowed.

## 1. Prior art (2026-03-30) and what postdates it
Its conclusion: Born *is* derived there, from three inputs put in — complex amplitudes, linear
propagation, reversibility. Content = p-norm uniqueness: p=2 survived 6/6 test transforms, every
other p in {0.5,1,1.5,2.5,3,4,5,6} broke under at least one. Three things postdate it:

1. **Its premise is now measured non-supplied.** p-norm uniqueness selects p=2 *by invariance
   under a unitary group*; the OS closure says this action class does not supply the Hilbert space
   that group acts on, and the memo calls imposing a unitary step "rate-from-ratelessness… measured
   OS-incompatible". Reversibility moves from assumed-but-plausible to assumed-and-measured-non-
   supplied here (CYCLE913: non-supply in this formalism, never necessity).
2. **The object changed.** Not |ψ|² over complex amplitudes but a real, diagonal, positive slice
   Gram `G = m·diag(D(c,·))` whose induced state `ω(A)=tr(GA)/tr(G)` is *already* a probability
   vector `p(x)=D(c,x)/Σ_y D(c,y)`. No squaring step; the exponent question does not arise.
3. **The question got harder.** 2026-03-30 asked *which functional of the state is the
   probability*; the live gate asks *why any normalized weight equals a limiting frequency*. p-norm
   uniqueness constrains a measure's form given a group and says nothing about frequencies — the
   note should not be cited as covering the bridge.

## 2. Objects the strategies must attach to
| foundations role | in-framework candidate | measured status |
|---|---|---|
| Hilbert space | `H_c = span(S)/ker P_c`, `dim H_c = L_x` (4/4/6) | built at pairing scope |
| state / density matrix | `G = m·diag(D(c,·))`, `ω(A)=tr(GA)/tr(G)` | classical; `[1/4]×4` on tested carrier |
| system / environment algebras | matter from `B = m·diag(D(c,·))`; record = span `∂P/∂b` on `H_c` | record **≡ 0** at `s_t=0`, acts as scalars |
| branch / history | record-compatible world; trail word `w` | grammar landed |
| interference / off-diagonal | inter-slice block `H_q[c+1,c]` | **= 0** identically, region, `s_t=0` |
| decoherence mechanism | the recording rule (pins link `c`) | = the disconnection rule |

Two facts constrain every row. **(i) The recording rule is the disconnection rule:** `H_q[c+1,c]`
is a form in the shear moduli of link `c` alone and the region pins exactly link `c` — recording
does not *cause* decoherence, recording *is* the pinning that removes the channel. **(ii) Pairing
scope ≠ theory scope:** the same free shears are LIVE in the full quotient action `Q` on the same
region at `s_t=0` (8x4, 12x4); N6 quotes and corrects the "no operator representative at all"
reading — the record is invisible only to the half-support reflected functional.

## 3. What zero collisions decides (stated once)
The census tests **injectivity / well-definedness** of the map between weight profiles and record-
frequency profiles. Zero collisions gives *uniqueness* — no frequency profile admits two weight
laws, so a bridge, if one exists, is the only one — and no *existence*: no dynamical reason why
realized frequencies track weights. Below, an assumption is **discharged** only if it is
underdetermination, **relocated** if it is existence/dynamics or kinematics.

### (a) Everett branch-counting + weight-proportional multiplicity
*Analog:* branches = record-compatible worlds; branch count = uniform counting on the history
index. Naive form already closed — RECORD_BORN_FREQUENCY_BOUNDARY prunes "finite record counts
derive Born probabilities" (at N=4 achievable frequencies are {0,1/4,1/2,3/4,1}; nothing forced).
*The repair* (one reading of the owner's intuition): posit worlds-per-record ∝ slice-Gram weight.
*Requires:* a multiplicity function defined from the action/quotient structure whose counts are
provably `∝ D(c,x)` as exact rationals, not merely non-uniform. *Smuggles:* a non-counting measure
on the history index — the bridge restated combinatorially. *Census:* **relocates** — at most one
multiplicity assignment is consistent, none is constructed; cheaply falsifiable on its own.

### (b) Deutsch–Wallace decision theory
*Analog:* nothing plays rational agent — the record algebra acts as scalars, the record factor is
one-dimensional, `I(record:matter)=0` exactly, so no preference-bearing subsystem exists.
*Requires:* a preference order on record-compatible worlds plus branching indifference, diachronic
consistency, measurement neutrality, all re-proven. *One real analog, cutting the wrong way:* the
region Gram carries **no shear symbol at all**, so `G(σ)=G(-σ)` is an identity and the pairing
cannot distinguish worlds differing only in a free shear — an exact, measured branching-
indifference analog. Indifference over an *invisible* label yields no ordering over weights: it
delivers the axiom and deletes what the axiom was to constrain (N7: the Z₂ is invisible rather
than superselected). *Smuggles:* an agent, and measurement neutrality. *Census:* **irrelevant.**

### (c) Zurek envariance
*Requires:* a system⊗environment factorization, a Schmidt pair with equal coefficients, and a system
swap undone by an environment counter-swap. *Blockage:* with matter = system and record =
environment, at `s_t=0` on the region the environment factor is **one-dimensional** (`∂P/∂b ≡ 0`) —
no Schmidt pair, no swap; envariance fails at its first ingredient exactly as Page–Wootters does
(N6). Structural cause is §2(i): **the recording rule is the disconnection rule**, so the act that
makes a record removes the correlation envariance needs. It blocks. *Where it could still live:* the
full quotient `Q`, where the shears are live — facing the anti-shim standard (a derived inter-record
channel must be shear-dependent or it is physics-empty). *Smuggles even if built:* (1) the choice of
factorization; (2) the fine-graining step — envariance derives *equal* probabilities for equal
coefficients, then recovers unequal ones by fine-graining into equiprobable branches and
**counting** them, precisely the step RECORD_BORN_FREQUENCY_BOUNDARY prunes here. *Census:*
**relocates**, and does not reach the blockage — the gap is kinematic.
### (d) Gleason-type theorems
*Correspondence:* Hilbert space → `H_c`; projection lattice → orthogonal resolutions of `H_c` by
record classes; frame function → record ↦ limiting relative frequency; density matrix → normalized
`G`. *Hypotheses scored:* **dim ≥ 3 is met** — `dim H_c = L_x` = 4, 4, 6 at the three measured
sizes; it would fail at `L_x = 2`, a fixture condition, not a framework limit. **Noncontextuality
is not established and carries the whole load** — here: the frequency of a record must not depend
on which family of alternatives / trail refinement contains it.
*Gap to the census.* The census tests injectivity of a map between profile spaces across fixtures;
Gleason gives uniqueness of an **additive extension** on one lattice. Injectivity is not
additivity, and a family statement is not a lattice statement — "the census is a discrete Gleason
question" is half right. A Gleason-shaped census varies the *resolution* of a fixed record
(refinement families), a different sweep. Also missing at pairing scope: a nontrivial lattice —
when the record algebra acts as scalars the lattice is {0,1} and Gleason has nothing to run on; it
must come from `Q`. *Smuggles:* noncontextuality and additivity. *Census as specified:*
**relocates.** *Extended to refinement families:* it would genuinely test noncontextuality — the
highest-value modification this lens names.

### (e) Bohmian quantum equilibrium / typicality
*Analog:* actual configuration = realized record trail; guidance equation = the sought generator
`P(next record | trail)`; typicality measure = a measure on the history index. The count-vs-weight
fork is Bohm's own: uniform counting measure (pruned) vs Gram-weight measure (the bridge). Bohm
does not escape it — the measure is justified by **equivariance** (preserved by the dynamics) plus
typicality, and the standing objection is that the choice remains an input. *The available
transplant:* re-proving equivariance converts the bridge from an axiom into a **fixed-point
condition** — it holds iff the normalized slice-Gram weight is a (ideally the unique) stationary
measure of the record-extension map. Computable on the same fixtures, distinct from the census,
attacking *existence* where the census attacks *uniqueness*. *Smuggles:* the typicality measure;
in the original, a deterministic trajectory. *Census:* **relocates**; equivariance is the decider.

### (f) Consistent histories / decoherence functionals
*Analog:* histories = record trails; `D(h,h')`; consistent when off-diagonals vanish, then the
diagonal is additive. *Measured:* the off-diagonal analog **already vanishes exactly** —
`H_q[c+1,c] = 0` identically on the region at `s_t=0`, 4 of 4 slices at 8x4 and 6 of 6 at 12x4,
empty symbol set (control: off the region, full rank `L_x`). Additive weights exist trivially.
*Why that is less than it looks:* the standard route's leverage comes from consistency being a
**constraint** only some sets satisfy, which is what selects the functional. Here the vanishing is
produced by the recording rule pinning link `c`, so every record set is consistent by construction
— a condition satisfied by fiat for all candidates constrains nothing, and the diagonal carries no
interference information to fix weights. *Smuggles:* that the diagonal of `D` is a probability —
Born, un-argued. Also `T_phys`-sensitive: the 8x4 corner `E` is a wrap accident, dead at
`T_phys ≥ 6` (T5b3 retraction), so any consistency argument resting on 8x4 corner behaviour
inherits that. *Census:* **relocates, and would not detect the vacuity** — trivially consistent
sets can be collision-free and still supply no derivation.

## 4. Cross-cutting
- **(d) and (f) share one missing ingredient: additivity/noncontextuality.** Gleason takes it as a
  hypothesis; consistent histories would supply it from a nonvacuous consistency condition, which
  this framework lacks. Neither closes without an independent argument that record frequencies are
  additive over refinements.
- **Fixture caution before reading a zero-collision result.** The measured induced state on the
  tested carrier is `p(x)=[1/4,1/4,1/4,1/4]` — uniform, and on a uniform weight profile the
  counting law and the bridge predict the *same* frequencies, so weight-vs-count discrimination is
  degenerate. The memo names the half-support scope as the trivially-colliding control; the
  analogous check at full-quotient scope is whether `D(c,·)` is non-uniform on the census fixtures.
  If it is not, zero collisions is a fixture artifact. (Census spec not read — a check, not a claim.)
- **Order without rate suffices for the frequency side and only that.** A limiting frequency needs
  an ordered index and a limit along it, which time-as-order-without-rate supplies; it supplies no
  rate, so no route needing a per-unit-time transition probability can close.
- **Scope discipline.** (b), (c), (d) all fail or trivialize *at pairing scope* and are untested at
  full-quotient scope where the record is live. Under N6 and CYCLE913 none of those failures is a
  statement about the framework, only about the half-support functional.

## 5. Checks this lens would want run
1. Is `D(c,·)` non-uniform on the census fixtures? Gates interpretability of the outcome.
2. A refinement-family sweep alongside the weight-profile sweep — the Gleason-shaped question.
3. Equivariance of the normalized slice-Gram weight under record-extension — the existence-side
   decider the census does not supply.
4. Does the record algebra on the full quotient `Q` give a projection lattice of rank ≥ 3? A
   precondition for any Gleason or envariance analog surviving out of pairing scope.
