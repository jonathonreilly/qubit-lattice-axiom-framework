# Koide Q=2/3 — last mile: derived modulo chirality (Dirac-mass signature)

**Date:** 2026-05-28
**Claim type:** bounded_theorem / status synthesis. `derived-modulo-chirality`.
Imports nothing; promotes nothing; sets no retained status (audit lane decides).
Local-branch working note (campaign last mile).
**Runner:** `scripts/koide_last_mile_chirality_2026_05_28.py`;
cache `logs/runner-cache/koide_last_mile_chirality_2026_05_28.txt`.
**Builds on (retained):** `koide_anticommuting_operator_derivation_theorem`,
`koide_q_two_thirds_z3_character_norm_split_recasting_theorem`,
`koide_z3_equivariant_anticommuting_no_go`. **Resolves** the open question
left by `KOIDE_TWO_QUESTIONS_RESOLUTION_NOTE_2026-05-28.md` (trace vs block /
thermal vs structural) at the operator level.

## The result
Charged-lepton `Q=2/3` is **derived modulo chirality**: it follows
**non-circularly**, via the retained anticommuting-operator theorem, from the
charged-lepton mass operator being **chiral** — anticommuting with the Z₃
singlet/doublet grading `Γ_χ = (2/3)J − I`. The framework's **non-chiral
default** (the Z₃-equivariant circulant) gives **Q=1**. So:

> **Q=2/3 is the signature of chiral (Dirac) mass generation; Q=1 is the
> non-chiral/thermal signature.**

This resolves "trace (Q=1) vs block (Q=2/3)" at the operator level: the
block/structural weighting *is* the chiral (off-diagonal, λ↔−λ-paired)
operator; the trace/thermal weighting *is* the non-chiral (diagonal,
commuting) operator.

## Why it is non-circular
- **Forward mechanism (retained):** `{H,Γ_χ}=0`, `Hv=λv`, `λ≠0` ⟹
  `H(Γ_χ v) = −λ(Γ_χ v)` ⟹ `Γ_χ v ⊥ v` ⟹ `⟨v|Γ_χ|v⟩=0` ⟹ Q=2/3. The proof
  never names v, Q, or 2/3 (verified: max `|⟨v|Γ_χ|v⟩|` = 1e-15 over 20000
  chiral H). It is a genuine **chiral symmetry** (spectral λ↔−λ pairing),
  strictly more general than per-vector Q=2/3.
- **`Γ_χ`'s "2/3" is forced, not tuned:** `(tJ−I)²=I` ⟹ `3t²−2t=0` ⟹
  `t∈{0, 2/3}`; `t=0` trivial, so `t=2/3 = 2/dim` is the *unique* nontrivial
  Z₃-equivariant involution. It is not the Koide ratio inserted by hand.
- **Faithful relabeling:** the converse holds (every Q=2/3 vector is a
  nonzero eigenvector of some anticommuting H, verified 5000/5000), so the
  *existential* "∃ chiral H with v as eigenvector" ⟺ "Q(v)=2/3" — equal
  information. The non-circular content is the *forward* implication; the
  open piece is whether the **physical** mass operator is chiral.

## Why chirality is the open gate (and is not supplied by A1+A2)
- A1+A2 canonically supply only the **Z₃-equivariant circulant algebra**
  `{I,S,S²}`. `Γ_χ` is itself a circulant (`[Γ_χ,S]=0`), so **every
  equivariant operator commutes with `Γ_χ`** → non-chiral → **Q=1 default**.
- Retained no-go (`koide_z3_equivariant_anticommuting_no_go`):
  `comm(S) ∩ anticomm(Γ_χ) = {0}` — no nonzero circulant anticommutes with
  `Γ_χ`. A1's Clifford bivector `S−Sᵀ` **commutes** with `Γ_χ` (no
  singlet↔doublet mixing). A1's Clifford anticommutation lives on the **2×2
  qubit/spinor factor**, not the generation R³.
- So the chiral operator necessarily **breaks Z₃-equivariance** (off-diagonal
  singlet↔doublet, Dirac-type) and is **absent without an import**.

## Honest caveat: the gate is MIS-LOCATED
The framework's existing chirality machinery (`anomaly_forces_time` → γ₅)
acts on the **spacetime** Clifford factor; `Γ_χ` grades the **generation**
factor. These are *different tensor factors*. So Q=2/3 does **not** reduce
cleanly to the existing (unaudited) chirality gate — it needs a separate,
**unbuilt spacetime-γ₅ → generation-`Γ_χ` bridge**, and staggered Dirac on
Z³ has no Ginsparg-Wilson relation. Claiming "Koide reduces to
`anomaly_forces_time`" without that bridge would be a category error.

## Falsifiable content
Q=2/3 = chiral (Dirac) mass; Q=1 (or off-cone) = non-chiral (Majorana /
thermal). Charged leptons are Dirac → Q=2/3 (postdiction to 6e-6, 3 masses /
1 relation). Majorana neutrinos need not sit at 2/3 — real-in-principle but
untestable today (neutrino absolute scale unknown).

## Status and next step
**`derived-modulo-chirality`** — not closed (the physical chiral H is not
established from A1+A2+retained), not circular (forward proof + forced 2/3
are clean). This is **genuine progress**: "why 2/3" is exactly relocated to
"why is charged-lepton mass-generation chiral on the generation sector" — a
single, physical, well-posed gate, making Koide a *corollary of chiral mass
generation* rather than a coincidence. **Next:** build/audit the
spacetime-γ₅ → generation-`Γ_χ` factor bridge (attack
`koide_z3_equivariant_anticommuting_no_go §4`). If it exists → Koide closes
to `derived`; if a no-go → it formally pins the chirality import.
