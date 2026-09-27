# Permanent record contents and symmetric field dynamics: an independent check (result (c))

- **Task:** `J:derive:deferred-20260926-author-only-field-results:a1`
- **Worker:** `w-jonathonsmac4f50-j8d87`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Provenance.** The source is a Codex author-only note, so this is a cross-family check. The author's runners (`record_content_permutation_check.py`, `local_record_content_symmetrization_check.py`) were not used.
- **Obligation chosen.** The task asks for one of three results. This attempt takes (c): distinct permanent contents through the exact permutation-fibre intertwiner.
- **Prior attempts.** None existed on `ai/probes` for this problem at claim time.

**Sources.**
- `PERMANENT_RECORD_CONTENTS_AND_SYMMETRIC_FIELD_DYNAMICS.md` (SHA256 `5b4aeab2…c284`), read in full.
- `APPROACH_REGISTRY.md` (`3a6536bc…83ec`).
- The other two results' notes were read for scope; their hashes are in `RECOVERY_STATUS.json`.
- No `correction_ack` exists for this note.

## (1) Statement

This concerns the note's supplied coloured extension of the hard-core bosonic gauge model: `k` orthogonal contents per record, transported unchanged. The following hold.

- **(I) Intertwiner.** Suppose every hop of the base configuration graph multiplies its scalar amplitude by a slot permutation, and all diagonal terms are content independent. Then for every symmetric content vector `v`, `H_col R_v = R_v H_base`, with `R_v|c⟩ = |c⟩ ⊗ v`. This holds exactly, at finite hopping, with no perturbation theory.
- **(II) Ground energy.** With nonpositive hops, every fixed-content-count fibre has ground energy `E₀(H_base)`.
- **(III) One loop.** For `H = −J X ⊗ P`, starting from field `|0⟩`:
  - `ρ_F(τ) = [[cos²θ, −iη cosθ sinθ], [iη cosθ sinθ, sin²θ]]`, with `η = Tr(Pρ)` and `θ = Jτ`;
  - the purity is `1 − ½ sin²2θ (1 − η²)`.
- **(IV) Local symmetrising reservoir.** `Σ γ D[L_ab^{αβ}]`, with `L = (|αβ⟩ + |βα⟩)(⟨αβ| − ⟨βα|)/2` on the edges of a connected graph, has the Dicke projector as its unique stationary state in each fixed-count sector.

## (2) Steps

1. **(I) PROVED and CHECKED (P1).**
   - *Proof.* Each hop block is `−a_{cc′} P_π`, and `P_π v = v` for symmetric `v`. So `(H_col R_v)_{c′} = Σ_c H_base(c′, c)·v`, which is `(R_v H_base)_{c′}`. Diagonal blocks are scalar.
   - *Check.* A five-configuration graph with six hops carries the non-commuting `S₃` labels `(1,0,2)`, `(2,0,1)`, `(2,1,0)` and `(0,2,1)`, with random rational amplitudes and diagonal. The identity holds exactly for the Dicke vectors of counts `(3,0)`, `(2,1)` and `(1,2)`, and fails for a non-symmetric vector.
2. **(II) PROVED (Cauchy–Schwarz); CHECKED P2 (float plus exact samples).**
   - `⟨Ψ, H_col Ψ⟩ ≥ ⟨r, H_base r⟩` with `r_c = ‖Ψ_c‖`, because `|⟨Ψ_c, P Ψ_{c′}⟩| ≤ r_c r_{c′}` and the hops are nonpositive. This is `≥ E₀‖Ψ‖²`, and (I) attains it.
   - The minimum eigenvalue of every count fibre equals the base `E₀` to 10⁻¹⁰.
   - The inequality holds on 20 random rational vectors.
3. **(III) CHECKED symbolically (P3).**
   - The general block content density, restricted to the swap-invariant structure the note uses, reproduces the note's `ρ_F` and purity exactly.
   - For i.i.d. contents `τ = diag(7/10, 3/10)`: `η = 29/50`, and the purity at `θ = π/4` is `3341/5000 = 0.6682`, as the note states.
4. **(IV) PROVED (the note's §5 argument re-read) and CHECKED (P4).**
   - Every jump has the fixed one-hot displacement (8). Exchange graphs on a connected graph generate every permutation.
   - The degree-lowering lemma (9) excludes invariant subspaces orthogonal to the target. P5 checks the lemma symbolically on a cubic polynomial.
   - The exact rational rank of the real Lindbladian is `D² − 1` on path graphs with counts `(2,1)`, `(2,2)`, `(1,1,1)`, `(2,1,1)` and `(3,2)` (`D = 3, 6, 6, 12, 10`). The Dicke projector is annihilated.
   - The author certified this rank modulo 65521. This check computes it over ℚ.
5. **The fuel dilation (10) (CHECKED P5).** `C³ = C`, `A₀ = I + (cos θ − 1)P₋` and `A₁ = −i sin θ L`, exactly.

## (3) Where it stops

- **No defect found.** Result (c)'s exact statements hold as written.
- **Not reproduced:** the single-plaquette perturbative control (2) (`H₂ = −2I₈`, `H₄ = 2I₈ − 2X ⊗ P₁₂`). It requires the base microscopic model, and its content-swap factor rests on the four-hop exchange argument of §1, which was only read.
- **Not addressed:** the slow-birth extension (§6) and results (a) and (b).
- **What matching to created mobile matter would still require** (the task's question):
  - a birth law whose new contents keep the joint state in the symmetric sector; appending a definite content does not map `Sym^N` into `Sym^{N+2}`;
  - a local, autonomous realisation of the symmetrising reservoir from the record-motion rule, including fuel, routing and export;
  - a content readout that does not decohere the Dicke superposition.

  Until these are supplied, (I)–(IV) are statements about a prepared, fixed-number sector.

## (4) What would finish it

- **(i)** Reproduce the plaquette control from the microscopic hard-core model.
- **(ii)** Prove or refute that some local birth channel preserves `Sym`, or bound its leakage uniformly.
- **(iii)** Check result (a), the static-source Coulomb energy, or result (b), the formation energy and number offset, in a further attempt.

## ASSUMED

The supplied coloured model: its contents, hops, penalties and reservoir. No outside theorem is used.

## Reproduce

```bash
python3 probes/work/derive/deferred-20260926-author-only-field-results/w-jonathonsmac4f50-j8d87/check.py
```

The run takes about 2 s.
