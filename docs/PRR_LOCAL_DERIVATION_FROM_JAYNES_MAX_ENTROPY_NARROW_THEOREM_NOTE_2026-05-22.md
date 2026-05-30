# PRR-Local Invariances from Jaynes Max-Entropy + Z^3 Lattice Symmetry (Narrow)

**Date:** 2026-05-22
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Derive the **PRR-local** invariance content — maximally mixed one-site marginals and lattice-translation invariance on finite translation-covariant windows — from the Jaynes maximum-entropy principle applied to the one-qubit operator algebra on the `Z^3` spatial substrate plus its translation automorphism action, rather than ratifying it as a framework rule.

## Why this note exists

The PRR-local clause asserts that the framework's pre-record reference state `ρ_ref` is invariant under (a) basis rotations at every individual site and (b) lattice translations. This is the *local* invariance content of the reference state — independent of whether the full state is uniquely identified.

Following the same audit-feedback that drove the k=1 and LSP-projective derivation refactors, this note derives those two invariances from standard statistical-mechanics machinery (Jaynes 1957 max-entropy principle + `Z^3` translation automorphism action) rather than ratifying as a framework rule.

The complementary **tracial-route** derivation, `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`, handles the full-state uniqueness via Powers' theorem on the UHF C*-algebra; this note handles only the local invariance content, with weaker hypotheses (no full-state uniqueness claim).

## Honest scope

This note **does not**:
- Add a new framework rule
- Claim full uniqueness of `ρ_ref` from Jaynes alone — the `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` obstruction stands; this note targets only **local invariance properties**, not full-state determination
- Re-derive the Jaynes max-entropy variational principle (cited as standard)
- Address how local invariances of `ρ_ref` translate into downstream Born / record-conditioning structure (separate lanes)

This note **does**:
- Derive per-site basis invariance of `ρ_ref` from Jaynes max-entropy applied to the per-site marginal
- Derive lattice translation invariance of `ρ_ref` from the `Z^3` translation automorphism action combined with the Jaynes selection
- Honor the BAE_MAX_ENTROPY obstruction by limiting the claim to invariance content, not full-state uniqueness

## Claim

For the one-qubit operator algebra on the `Z^3` spatial substrate:

**Theorem (narrow finite-volume form).** On every finite translation-covariant qubit-lattice window `Λ` with no record-side constraints, the Jaynes maximum-entropy state `ρ_ref,Λ` on `A_Λ` satisfies:

```text
(PRR-local-a)  per-site basis invariance:
    ρ_ref,Λ|_{x}  =  U · ρ_ref,Λ|_{x} · U†   for all U ∈ U(H_x), all x ∈ Λ.

(PRR-local-b)  lattice translation invariance:
    ρ_ref,Λ ∘ α_t  =  ρ_ref,Λ
    for translations t that preserve the finite window/boundary convention.
```

Equivalently: the per-site marginal is `I/2` (the unique SU(2)-invariant qubit state), and the finite-window joint state is invariant under the available `Z^3` lattice-translation automorphism action. Infinite-volume uniqueness is not claimed here; it belongs to the tracial-route note.

## Proof

### Step 1 — Jaynes max-entropy selection criterion

The **Jaynes maximum-entropy principle** (Jaynes *Information Theory and Statistical Mechanics* 1957, Phys. Rev. 106:620 and 108:171) states: given a set of constraints `{c_i}` consistent with some state `ρ`, the **least-biased** assignment is the state that maximizes the von Neumann entropy `S(ρ) = -Tr(ρ log ρ)` subject to the constraints.

**Pre-record condition.** By construction, "pre-record" means no record-side information about the state has been produced. The only constraints on `ρ_ref` are:

(J1) Normalization: `Tr(ρ_ref) = 1` (state)
(J2) Substrate: `ρ_ref` is a density operator on the one-qubit operator algebra over the `Z^3` spatial substrate

No further constraints. On a finite window `Λ`, the Jaynes selection criterion reduces to: **maximize `S(ρ_ref,Λ)` subject to (J1) on `A_Λ`.**

### Step 2 — Per-site marginal: max-entropy on `M_2(ℂ)`

Fix a site `x ∈ Λ`. The per-site marginal of `ρ_ref,Λ` is

```text
ρ_ref,Λ|_x  :=  Tr_{Λ \ {x}}(ρ_ref,Λ)
```

a density operator on `H_x = ℂ²` with `Tr(ρ_ref|_x) = 1`. The von Neumann entropy `S(ρ_ref|_x) = -Tr(ρ_ref|_x log ρ_ref|_x)` is maximized (subject to normalization) by the maximally mixed state:

```text
ρ_ref,Λ|_x  =  I_2 / 2.                                                  (J3)
```

**Proof.** Standard finite-dim max-entropy result: on `M_d(ℂ)`, the unique normalized density operator maximizing `-Tr(ρ log ρ)` is `I_d / d` (entropy `log d`); for `d = 2`, entropy `log 2`. Since the finite-window unconstrained maximizer on `A_Λ` is the normalized trace state `I_{2^{|Λ|}} / 2^{|Λ|}`, its one-site marginal is `I_2 / 2`. Equivalently, any nonmaximally mixed one-site marginal would be lower entropy than `I_2/2` on that factor. □

### Step 3 — Per-site basis invariance (PRR-local-a)

For any unitary `U ∈ U(H_x)`:

```text
U · (I_2 / 2) · U†  =  (1/2) · U · U†  =  I_2 / 2  =  ρ_ref,Λ|_x.        (J4)
```

So `ρ_ref|_x` is invariant under the full per-site unitary group `U(H_x)` action, which includes all SU(2) basis rotations. This is **PRR-local-a**. □

### Step 4 — Z^3 translation automorphism action

By the `Z^3` spatial substrate axiom, lattice translations act as a `Z^3` group of automorphisms `{α_t}_{t ∈ Z^3}` on the quasi-local algebra `A = ⊗_{x ∈ Z^3} M_2(ℂ)`. Specifically, `α_t` maps the site-`x` factor `M_2(ℂ)_x` to the site-`(x+t)` factor `M_2(ℂ)_{x+t}` via the canonical identification. On a finite periodic window, use the induced finite translation action; on a finite nonperiodic window, restrict to translations preserving the chosen window/boundary convention.

The von Neumann entropy is **invariant under automorphisms**:

```text
S(ρ ∘ α_t)  =  S(ρ)   for any automorphism α_t.                          (J5)
```

This is a standard result (the entropy depends only on the spectrum of the density operator, which is preserved under unitary / automorphic conjugation).

### Step 5 — Translation invariance (PRR-local-b)

On a finite translation-covariant window, the unconstrained Jaynes maximizer is the normalized trace state:

```text
ρ_ref,Λ = I_{2^{|Λ|}} / 2^{|Λ|}.                                        (J6)
```

For every translation automorphism `α_t` that preserves the window/boundary convention,

```text
ρ_ref,Λ ∘ α_t = ρ_ref,Λ                                                   (J7)
```

because the trace state is invariant under algebra automorphisms. Equivalently, if one starts from an arbitrary finite-window optimum, strict concavity gives uniqueness of the maximizer, and automorphism invariance of entropy forces its translate to be the same maximizer. This is **PRR-local-b** on the finite-window scope. □

### Step 6 — Conclusion

Both finite-window PRR-local invariances follow from Jaynes max-entropy applied to the one-qubit operator algebra over the `Z^3` spatial substrate:

- (PRR-local-a) per-site basis invariance — from Step 2 + Step 3 (max-entropy on `M_2(ℂ)` gives `I/2`, which is `U(2)`-invariant)
- (PRR-local-b) lattice translation invariance — from Step 4 + Step 5 (finite-window trace state and entropy uniqueness are automorphism-invariant)

This is **finite-window invariance content** only. The complementary tracial-route derivation, `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`, gives the infinite quasi-local full-state route via Powers' theorem; this note derives the local finite-window symmetry content that the PRR-local clause needs. ∎

## Honoring the BAE_MAX_ENTROPY obstruction

`BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` closed the Jaynes route to *full-state uniqueness* negatively: deriving `ρ = ⊗ I/2` from the one-qubit operator algebra on the `Z^3` spatial substrate + Born + Jaynes + physical-lattice without additional input does not produce a unique answer.

This note's narrower target is **local invariance content**, not full-state uniqueness:

- The BAE obstruction concerned what additional inputs Jaynes needs to fix the **entire joint state** (e.g., Lagrange multipliers for correlation constraints, choice of entropy functional, dim-2 Born issues).
- This note's claim — per-site basis invariance + finite-window translation invariance — does **not** require asserting a separate infinite-volume full-state uniqueness theorem. It only requires the finite-window trace maximizer and its one-site marginals (Steps 2 and 5).
- Both of those weaker claims follow from Jaynes max-entropy applied to the respective scope without any of the additional inputs flagged by BAE.

So the obstruction stands for full-state uniqueness, and the present note is consistent with it: this note does **not** claim Jaynes uniquely fixes `ρ_ref`; it claims Jaynes fixes the **local invariance content** of `ρ_ref`.

## Cited authorities (one hop)

Load-bearing markdown-link upstream:

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies the qubit-per-site axiom and `Z^3` spatial substrate with translation automorphism; canonical axiom-premise node
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md) — retained narrow theorem supplying the per-site `M_2(ℂ)` operator algebra used in Step 2
- [`CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md) — retained narrow theorem supplying `H_x = ℂ²` (the one-site factor on which `I/2` is the max-entropy state)

Named non-derivation imports (standard textbook content):

- **Jaynes 1957** maximum-entropy principle (*Information Theory and Statistical Mechanics*, Phys. Rev. 106:620 and 108:171)
- **von Neumann entropy** standard properties (concavity, automorphism invariance, max-entropy = `log d` on `M_d(ℂ)` achieved by `I/d`)
- Standard finite-dim density-operator simplex geometry

Plain-text contextual pointer (not load-bearing dep):

- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — complementary tracial route to full-state uniqueness; this note's invariance-only claim is consistent with and weaker than that note's claim

## What this derivation supplies

The same PRR-local invariance content — per-site basis invariance + finite-window translation invariance — now stated as a **bounded theorem on the one-qubit operator algebra over the `Z^3` spatial substrate + Jaynes**, not a load-bearing framework rule. The BAE_MAX_ENTROPY obstruction to full-state uniqueness via Jaynes is honored: this note's narrower claim does not require the additional inputs that BAE flagged as missing.

## What this does NOT close

- **Full uniqueness of `ρ_ref`** — covered by the complementary tracial-route note; this note targets only invariance content
- **Born-rule derivation downstream of `ρ_ref`** — separate lane (Gleason–Busch on the POVM effect algebra)
- **Cosmological / vacuum-energy reframes** — separate lanes
- **Promotion of the PRR-local parent row** — auditor-owned

## Citation-graph note

This is a bounded_theorem candidate at narrow-theorem granularity. Standard statistical mechanics (Jaynes max-entropy + entropy concavity) applied to finite qubit-lattice windows to derive definite **local invariance content** for the pre-record reference state.

Plain-text pointer references (NOT load-bearing deps):

- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening IV" / PRR-local clause — the prior PRR-local approval-pending clause that this derivation supersedes; will be removed by the axiom-doc cleanup PR
- `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` — explains why full-state uniqueness via Jaynes is obstructed; this note's narrower scope is designed to avoid that obstruction
- `QUBIT_K1_DERIVATION_FROM_MINIMALITY_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing the prior k=1 ratification with derivation)
- `LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing LSP-projective ratification with derivation)

## What this file is not

- Not a new framework rule
- Not a re-derivation of the Jaynes max-entropy principle (cited as standard)
- Not a claim that Jaynes uniquely fixes `ρ_ref` (BAE obstruction honored)
- Not a promotion of any downstream row (auditor-owned)
- Not a numerical-prediction change
