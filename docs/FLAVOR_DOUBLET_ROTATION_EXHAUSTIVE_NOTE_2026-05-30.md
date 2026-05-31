# Flavor — exhaustive enumeration of doublet rotations in the lattice: no new rotation, J_cs is FORCED (Schur), the free bit is now purely a measure choice

**Date:** 2026-05-30
**Claim type:** bounded completeness result (exhausts the symmetry classes, with cohomology backstop) + one upgrade (J_cs forced) + relocation of the open bit.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_doublet_rotation_exhaustive_2026_05_30.py` (SCORECARD PASS=4).
**Source:** 7-agent build `wf_5fb30a2e` (enumerate 4 classes → completeness auditor + adversary → adjudication).

## Question
"Have we explored ALL the ways the generation doublet can rotate in the lattice — not just convention,
but all ways?" Enumerated exhaustively: ordinary point group, full O_h, projective/magnetic-translation
reps, algebra automorphisms, complex structures, anti-unitary/time-reversal, coin factor, induced reps.

## Answer — yes at the symmetry/operator level (complete), and no new rotation
| class | doublet action | continuous? |
|---|---|---|
| point group S₃ on hw=1 | dihedral D₃: rotations {0,±120°} + 3 reflections | discrete |
| full O_h (48) | hw=1 stabilizer = S₃ (same D₃); **0 of the 12 order-4 (90°) elements preserve hw=1** | discrete |
| charge conjugation `(1,1,1)−v` | real Z₂ swap hw1↔hw2 (to the *separate* doublet) | discrete |
| projective / magnetic translations | **vanish on the doublet** (a bit-flip leaves hw=1); qubit cocycle descends as the **central scalar `i·I₃`** (generation-blind), not `J_cs` | finite |
| algebra automorphisms `Aut(ℝ[Z₃])` | `Gal(ℂ/ℝ)=Z₂` = conjugation = reflection; no continuous auto | discrete |
| anti-unitary / coin / induced reps | all collapse onto the same D₃ | discrete |

**Cohomology backstop:** `H²(C₃,U(1))=0` and the Schur multiplier `M(S₃)=0`, so every projective rep within
a doublet linearizes — there is **no nontrivial-cocycle escape**, and H² is the only classifying degree.
**The enumeration is complete at the operator level: no lattice symmetry rotates the doublet beyond discrete
D₃ + a real charge-conjugation Z₂.** The most-touted unexplored class (projective/magnetic, the qubit's own
Heisenberg structure) does **not** complexify the generation doublet — it descends as the generation-blind
central `i·I₃`, provably distinct from the non-central `J_cs`.

## The genuine upgrade (Schur)
The C₃ doublet is of **complex type** (eigenvalues `ω, ω²`), so by Schur its C₃-equivariant endomorphism
algebra is canonically `ℂ`. Hence **`J_cs` EXISTS and is UNIQUE up to sign** (exactly two `J` with `J²=−I`,
`[J,C]=0`: `J=±J_cs`). The doublet's complex structure is therefore a **FORCED native structure, not a
posited object** — stronger than the prior "native but a choice" framing.

## What stays open — and it is now purely a *measure* question
Possessing the canonical `J_cs` is **not** the same as the fluctuation measure being its holomorphic
(Kähler, `det_C`) measure:
- **Existence:** discharged — `J_cs` forced.
- **Orientation:** not fixed — the dihedral reflections swap `J_cs ↔ −J_cs`; no lattice symmetry orients it.
- **Measure:** **open and free** — `det_C` (holomorphic w.r.t. `J_cs` → r=1/2 → Q=2/3) vs `det_R` (flat real
  → r=1 → Q=1) is a measure choice, not forced by symmetry. The lattice realizes only the discrete
  `{I,C,C²}` of `exp(θJ_cs)`, never the continuous `U(1)` (consistent with the retained `C³=I` obstruction).

So `r=1/2` is **neither derived nor forbidden** by the lattice symmetry structure. The free bit is now
sharper than before:
- **Old (closed):** "find a continuous `U(1)_b` lattice symmetry rotating the doublet" — forbidden by `C³=I`.
- **New (open):** "find a measure/positivity/holomorphicity *principle* selecting the Kähler measure of the
  now-forced `J_cs`." The import shrinks from "posit a complex structure **and** its use" to *only* "posit the
  measure is holomorphic w.r.t. the unique native `J_cs`" — a single, sharply-characterized, natural primitive.

## Next step (sharpens, not closes)
Attack whether a **measure/positivity** argument (not a symmetry) selects the orientation+use of `J_cs` — e.g.
whether reflection-positivity or a holomorphicity requirement on the path-integral measure forces `det_C`.
Per repo policy, a measure-selection primitive is an import requiring user approval + independent audit, even
though it is now the *unique* natural one. Cross-check against the `√m`-signed-vs-singular-value readout lever.

## Stale-citation flags
- Confirms (from 4 fresh angles, no escape) the existing `generation-doublet-measure-detC-vs-detR-2026-05-29`
  derivation. Anchors: `koide_real_rep_block_count_permitted_not_forced` (unaudited), `koide_c3_generator_rephasing_obstruction` (retained, the `C³=I` symmetry obstruction).
