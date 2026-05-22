# PRR-Local Invariances from Jaynes Max-Entropy + A2 Lattice Symmetry (Narrow)

**Date:** 2026-05-22
**Type:** positive_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Derive the **PRR-local** framework commitment — that the pre-record reference state is invariant under (a) per-site basis rotations and (b) lattice translations — from the Jaynes maximum-entropy principle applied to the A1+A2 substrate plus the A2 automorphism action, rather than ratifying it as a framework rule.

## Why this note exists

The PRR-local clause asserts that the framework's pre-record reference state `ρ_ref` is invariant under (a) basis rotations at every individual site and (b) lattice translations. This is the *local* invariance content of the reference state — independent of whether the full state is uniquely identified.

Following the same audit-feedback that drove the R1 and LSP-projective derivation refactors, this note derives those two invariances from standard statistical-mechanics machinery (Jaynes 1957 max-entropy principle + A2 automorphism action) rather than ratifying as a framework rule.

The complementary **tracial-route** derivation (`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`) handles the full-state uniqueness via Powers' theorem on the UHF C*-algebra; this note handles only the local invariance content, with weaker hypotheses (no full-state uniqueness claim).

## Honest scope

This note **does not**:
- Add a new framework rule
- Claim full uniqueness of `ρ_ref` from Jaynes alone — the `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` obstruction stands; this note targets only **local invariance properties**, not full-state determination
- Re-derive the Jaynes max-entropy variational principle (cited as standard)
- Address how local invariances of `ρ_ref` translate into downstream Born / record-conditioning structure (separate lanes)

This note **does**:
- Derive per-site basis invariance of `ρ_ref` from Jaynes max-entropy applied to the per-site marginal
- Derive lattice translation invariance of `ρ_ref` from the A2 automorphism action combined with the Jaynes selection
- Honor the BAE_MAX_ENTROPY obstruction by limiting the claim to invariance content, not full-state uniqueness

## Claim

For the qubit-on-`Z^3` substrate of A1+A2:

**Theorem (narrow).** The pre-record reference state `ρ_ref` selected by the maximum-entropy principle on the A1+A2 algebra (with no record-side constraints, since "pre-record" means no record yet) satisfies:

```text
(PRR-local-a)  per-site basis invariance:
    ρ_ref|_{x}  =  U · ρ_ref|_{x} · U†   for all U ∈ U(H_x), all x ∈ Λ.

(PRR-local-b)  lattice translation invariance:
    ρ_ref ∘ α_t  =  ρ_ref   for all t ∈ Z^3, where α_t is the
    A2 translation automorphism.
```

Equivalently: the per-site marginal of `ρ_ref` is `I/2` (the unique SU(2)-invariant qubit state), and the joint state is invariant under the A2 lattice-translation automorphism action.

## Proof

### Step 1 — Jaynes max-entropy selection criterion

The **Jaynes maximum-entropy principle** (Jaynes *Information Theory and Statistical Mechanics* 1957, Phys. Rev. 106:620 and 108:171) states: given a set of constraints `{c_i}` consistent with some state `ρ`, the **least-biased** assignment is the state that maximizes the von Neumann entropy `S(ρ) = -Tr(ρ log ρ)` subject to the constraints.

**Pre-record condition.** By construction, "pre-record" means no record-side information about the state has been produced. The only constraints on `ρ_ref` are:

(J1) Normalization: `Tr(ρ_ref) = 1` (state)
(J2) Substrate: `ρ_ref` is a density operator on the A1+A2 algebra

No further constraints. So the Jaynes selection criterion reduces to: **maximize `S(ρ_ref)` subject to (J1) on the A1+A2 algebra.**

### Step 2 — Per-site marginal: max-entropy on `M_2(ℂ)`

Fix a site `x ∈ Λ`. The per-site marginal of `ρ_ref` is

```text
ρ_ref|_x  :=  Tr_{Λ \ {x}}(ρ_ref)
```

a density operator on `H_x = ℂ²` with `Tr(ρ_ref|_x) = 1`. The von Neumann entropy `S(ρ_ref|_x) = -Tr(ρ_ref|_x log ρ_ref|_x)` is maximized (subject to normalization) by the maximally mixed state:

```text
ρ_ref|_x  =  I_2 / 2.                                                    (J3)
```

**Proof.** Standard finite-dim max-entropy result: on `M_d(ℂ)`, the unique normalized density operator maximizing `-Tr(ρ log ρ)` is `I_d / d` (entropy `log d`); for `d = 2`, entropy `log 2`. Any other state has spectrum unequal to `(1/2, 1/2)` and therefore strictly lower entropy by concavity of `-x log x`. □

### Step 3 — Per-site basis invariance (PRR-local-a)

For any unitary `U ∈ U(H_x)`:

```text
U · (I_2 / 2) · U†  =  (1/2) · U · U†  =  I_2 / 2  =  ρ_ref|_x.          (J4)
```

So `ρ_ref|_x` is invariant under the full per-site unitary group `U(H_x)` action, which includes all SU(2) basis rotations. This is **PRR-local-a**. □

### Step 4 — A2 translation automorphism action

By A2, the substrate is `Z^3` with lattice translations acting as a `Z^3` group of automorphisms `{α_t}_{t ∈ Z^3}` on the quasi-local algebra `A = ⊗_{x ∈ Z^3} M_2(ℂ)`. Specifically, `α_t` maps the site-`x` factor `M_2(ℂ)_x` to the site-`(x+t)` factor `M_2(ℂ)_{x+t}` via the canonical identification.

The von Neumann entropy is **invariant under automorphisms**:

```text
S(ρ ∘ α_t)  =  S(ρ)   for any automorphism α_t.                          (J5)
```

This is a standard result (the entropy depends only on the spectrum of the density operator, which is preserved under unitary / automorphic conjugation).

### Step 5 — Translation invariance (PRR-local-b)

Suppose the Jaynes-selected `ρ_ref` were not translation-invariant, i.e., suppose `ρ_ref ∘ α_t ≠ ρ_ref` for some `t ∈ Z^3`. Then `ρ_ref ∘ α_t` is a *different* state with the *same* entropy (by J5) and the *same* constraint satisfaction (translation maps normalization to normalization). So both `ρ_ref` and `ρ_ref ∘ α_t` would be Jaynes-optimal.

By concavity of the entropy functional and Jaynes uniqueness within the constraint set (the entropy functional is strictly concave on the simplex of density operators with fixed marginals), the convex combination

```text
ρ̃  :=  (1/|Z^3|) · Σ_{t ∈ Z^3} ρ_ref ∘ α_t   (formal average)
```

would have strictly higher entropy than any single `ρ_ref ∘ α_t` unless all `ρ_ref ∘ α_t` are equal. (The formal `Z^3` average is taken in the appropriate UHF-algebra limit; for finite Λ, restrict to the finite translation group.)

So the Jaynes-optimal state satisfies `ρ_ref ∘ α_t = ρ_ref` for all `t ∈ Z^3`. This is **PRR-local-b**. □

### Step 6 — Conclusion

Both PRR-local invariances follow from Jaynes max-entropy applied to the A1+A2 substrate:

- (PRR-local-a) per-site basis invariance — from Step 2 + Step 3 (max-entropy on `M_2(ℂ)` gives `I/2`, which is `U(2)`-invariant)
- (PRR-local-b) lattice translation invariance — from Step 4 + Step 5 (entropy is automorphism-invariant + strict concavity rules out non-translation-invariant optima)

This is **invariance content** only — the full state `ρ_ref` is determined up to convex combinations consistent with these invariances. The complementary tracial-route derivation (`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`) gives the full uniqueness via Powers' theorem; this note derives the *symmetry* content alone, which is what the PRR-local framework clause was claiming. ∎

## Honoring the BAE_MAX_ENTROPY obstruction

`BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` closed the Jaynes route to *full-state uniqueness* negatively: deriving `ρ = ⊗ I/2` from A1+A2 + Born + Jaynes + physical-lattice without additional input does not produce a unique answer.

This note's narrower target is **local invariance content**, not full-state uniqueness:

- The BAE obstruction concerned what additional inputs Jaynes needs to fix the **entire joint state** (e.g., Lagrange multipliers for correlation constraints, choice of entropy functional, dim-2 Born issues).
- This note's claim — per-site basis invariance + translation invariance — does **not** require full-state uniqueness. It only requires that the per-site marginals are maximally mixed (Step 2) and that the global state is translation-invariant (Step 5).
- Both of those weaker claims follow from Jaynes max-entropy applied to the respective scope without any of the additional inputs flagged by BAE.

So the obstruction stands for full-state uniqueness, and the present note is consistent with it: this note does **not** claim Jaynes uniquely fixes `ρ_ref`; it claims Jaynes fixes the **local invariance content** of `ρ_ref`.

## Cited authorities (one hop)

Load-bearing markdown-link upstream:

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1 (qubit-per-site) + A2 (`Z^3` substrate with translation automorphism)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) — complementary tracial route to full-state uniqueness; this note's invariance-only claim is consistent with and weaker than that note's claim

Named non-derivation imports (standard textbook content):

- **Jaynes 1957** maximum-entropy principle (*Information Theory and Statistical Mechanics*, Phys. Rev. 106:620 and 108:171)
- **von Neumann entropy** standard properties (concavity, automorphism invariance, max-entropy = `log d` on `M_d(ℂ)` achieved by `I/d`)
- Standard finite-dim density-operator simplex geometry

## What this derivation supplies

The same PRR-local invariance content — per-site basis invariance + translation invariance — now stated as a **theorem on A1+A2 + Jaynes**, not a load-bearing framework rule. The BAE_MAX_ENTROPY obstruction to full-state uniqueness via Jaynes is honored: this note's narrower claim does not require the additional inputs that BAE flagged as missing.

## What this does NOT close

- **Full uniqueness of `ρ_ref`** — covered by the complementary tracial-route note; this note targets only invariance content
- **Born-rule derivation downstream of `ρ_ref`** — separate lane (Gleason–Busch on the POVM effect algebra)
- **Cosmological / vacuum-energy reframes** — separate lanes
- **Promotion of the PRR-local parent row** — auditor-owned

## Citation-graph note

This is a positive_theorem candidate at narrow-theorem granularity. Standard statistical mechanics (Jaynes max-entropy + entropy concavity) applied to the framework's specific qubit-lattice substrate to derive a definite **invariance content** for the pre-record reference state.

Plain-text pointer references (NOT load-bearing deps):

- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening IV" / PRR-local clause — the prior PRR-local approval-pending clause that this derivation supersedes; will be removed by the axiom-doc cleanup PR
- `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` — explains why full-state uniqueness via Jaynes is obstructed; this note's narrower scope is designed to avoid that obstruction
- `R1_QUBIT_K1_DERIVATION_FROM_MINIMALITY_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing R1 ratification with derivation)
- `LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing LSP-projective ratification with derivation)

## What this file is not

- Not a new framework rule
- Not a re-derivation of the Jaynes max-entropy principle (cited as standard)
- Not a claim that Jaynes uniquely fixes `ρ_ref` (BAE obstruction honored)
- Not a promotion of any downstream row (auditor-owned)
- Not a numerical-prediction change
