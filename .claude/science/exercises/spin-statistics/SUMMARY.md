# Exercise packet — spin-statistics / FS wall (2026-06-06)

Repo `/exercise` skill, 5-subagent fan-out (max-reasoning, each with framework-refresher).

## Wall (Exercise Zero)
Per-site Z₂ fermion-parity grading + Pauli exclusion + Berezin det are RETAINED;
the **cross-site fermion exchange sign** (CAR / −1, vs hard-core-boson CCR) is NOT
forced from {Lattice, Quantum, Record}. `axiom_first_spin_statistics_theorem`
unaudited. The standard spin-statistics theorem needs Lorentz+microcausality+
positivity — the lattice lacks manifest Lorentz.

## Verdict (all 5 slices converge): FS is a genuine admission, precisely located
1. **Cl(3) doesn't supply the CAR grading** (Ex4, verified): ω=σ₁σ₂σ₃=iI, ω²=−I
   (not an involution); only G=0 anticommutes all three Paulis (the d_s=3 fact).
   So the CAR grading = Fock parity σ₃ = a basis choice, not the Cl(3) vector grade.
2. **Topology → dichotomy only** (Ex2/Ex3/Ex4): the 2-particle exchange class is
   order-2 (anyons excluded) but Hom(Z₂,U(1))={±1} admits both; the config-space
   route is sign-blind (Koszul vs ungraded → identical Z₂ torsion). Sharper Z³
   witness (Ex2): the **3×3×2 box has H₁(UD₂)=Z¹⁶⊕Z₂** — smallest concrete Z³
   graph with the exchange Z₂ (to re-verify; dichotomy is retained_bounded).
3. **Precise location** (Ex5, sharpest): the Z₂ fermion-parity grading F=(−1)^Q is
   the **central-sector** (K/CPT-orbit) structure Record DELIVERS (retained);
   the exchange **sign** is **within-sector** data, which Record "supplies none
   of." Record forces the grading and is constitutively silent on the sign → FS is
   a genuine admission of the same class as Lorentz-route spin-statistics, NOT a
   missing lemma.
4. **Literature no-go** (Ex3): Allen–Mondragon (quant-ph/0304088) "no
   spin-statistics in NRQM"; DHR classifies but doesn't select the sign;
   Berry–Robbins non-unique. Every lattice-native route leaves the dichotomy.

## Route portfolio
| Rank | Route | Class | First artifact |
|---|---|---|---|
| 1 | multi-loop graded-net cocycle consistency (Ex5×6) | possible forcing lemma | 2 linked JW-string loops on a Z³ patch: does HCB framing survive joint single-valuedness? |
| 2 | continuum migration (emergent Lorentz → standard theorem) | migrate to continuum | complete the OS→Wightman reconstruction (rungs A–C) |
| 3 | 3×3×2 Z³ box H₁(UD₂) witness | sharpen dichotomy | SNF on the actual Z³ box (vs abstract K₅/K₃,₃) |
| — | graded-tensor/SSR from {L,Q,R} | infeasible w/o new principle | (re-derives the admission) |

No route closes FS on the static {Lattice,Quantum,Record} baseline without a new
principle — consistent with the four repo no-gos (car_from_positivity,
statistics_agnostic, ring_monodromy, FS_rotation_exchange). No new axiom.

Files: this SUMMARY.md. Full slice outputs in the exercise note + commit.
