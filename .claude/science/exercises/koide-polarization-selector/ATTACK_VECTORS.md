# Attack vectors — Koide r=1/2 polarization selector (ranked)

The fork is now precise: **first-order/holomorphic flavor kinetic term → r=1/2** vs **second-order real
modulus → r=1**. The selector is dynamical (static `J_cs` is measure-neutral). Ranked routes:

## Rank 1 — Inherit the qubit coherent-state first-order (Berry) dynamics  ← DECISIVE, do first
**Premise challenged:** "the flavor kinetic term is a second-order real modulus."
**Claim to derive:** the `b`-field (C₃-breaking coefficient) is a coordinate on a manifold built from the
qubit coherent state `CP¹`; its emergent kinetic term inherits the **first-order Berry/symplectic** term
(`∫A_z ḃ dt`, holomorphic) rather than a second-order `|ḃ|²`. First-order ⇒ the doublet is counted once ⇒ `r=1/2`.
**First artifact:** in the AC_φλ staggered/corner realization, write the generation-sector effective action for
the slow `b`-mode by adiabatically eliminating the fast on-site qubit DOF (Born-Oppenheimer / coherent-state
path integral), and read whether the leading `ḃ`-term is first-order (Berry, `i b̄ ḃ`-type) or second-order (`|ḃ|²`).
**Stop condition:** if first-order survives the elimination → `r=1/2` derived (close the lever, conditional on AC_φλ).
If the leading term is genuinely second-order real → `r=1` confirmed (upgrade the partial-falsification, this time
correctly oriented, with a no-go on the holomorphic route).
**Risk:** the b-field may not be a `CP¹` coordinate at all (the C₃/flavor structure could be independent of the
on-site Bloch sphere) — then the coherent-state metric does not transfer and this collapses to "AC_φλ undecided."

## Rank 2 — Readout-functional factorization through the complex-slot quotient
**Premise challenged:** "Record additivity fixes the per-orbit value to the trace/dimension count."
**Claim to derive:** the Record readout `I` necessarily factors through the K/CPT-orbit quotient (ω,ω̄ → one
record), forcing the count-once value — *as a readout fact*, not a real-structure fact (the route the
`KOIDE_REAL_REP_BLOCK_COUNT` note left explicitly open).
**First artifact:** test whether any additive `I` consistent with R3 ("no within-sector data") can resolve the
doublet's two modes; if R3 provably forbids resolving ω vs ω̄ (within-orbit data), the count-once is forced.
**Risk:** the landed result is that the *instantiated* `I = log|det|` does resolve modes → this route must show
R3 forbids that instantiation, i.e. argue the dimension-count `I` itself violates "no within-sector data." Hard;
this is close to the refuted *static* orbit-count — only legitimate if framed as a readout-admissibility theorem.

## Rank 3 — Frobenius-Schur faithfulness as an admissibility constraint
**Premise challenged:** "realifying the complex-type doublet is an admissible readout."
**Claim to derive:** reading a FS-complex (FS=0) irrep by its real dimension is *unfaithful* (it imposes a real
structure the irrep lacks); the faithful readout over the complex carrier counts the complex-type block once.
**First artifact:** a representation-theory argument that the complex carrier `M₂(ℂ)` (rebit-excluded, #2573)
admits only FS-faithful readouts of its modules → excludes the realified count for FS=0 blocks → `r=1/2`.
**Risk:** "faithful" may not be axiom-forced; needs the complex-carrier→complex-readout bridge (Rank 1's content).

## What NOT to do
- Do not re-walk the **static** orbit-count / min-info / max-entropy (refuted: native `I = log|det|` is the
  dimension count). Rank 2/3 are legitimate only as *readout-admissibility* arguments, not static re-assertions.
- Do not invert the FS-type mapping again (complex ↔ r=1/2, NOT Majorana ↔ r=1/2). #3138 died on that.
- Do not claim a closure without deriving Rank 1's first-order kinetic term from the realization.

## Literature / math-sector tools worth translating (comparators only)
- **Frobenius-Schur indicator** (Serre, *Lin. Reps. of Finite Groups*, ch. 4) — the FS=0 typing. [used]
- **Spin coherent-state path integral / Berry phase** (Perelomov; Stone) — the first-order symplectic term. [Rank 1]
- **Quillen determinant line / holomorphic vs real det** (Quillen 1985) — canonical determinant of a complex mode. [Rank 1/3]
- **Kähler-Dirac / staggered reality** (Adams 2002; Becher-Joos; Banks-Susskind) — whether the lattice mass term
  is complex (Dirac) — the AC_φλ realization. [Rank 1]
