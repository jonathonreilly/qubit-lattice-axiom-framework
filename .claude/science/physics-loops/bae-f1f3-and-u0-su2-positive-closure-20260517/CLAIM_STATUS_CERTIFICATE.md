# Claim Status Certificate — Cycle 1 / Agent A
# Physics Loop: bae-f1f3-and-u0-su2-positive-closure-20260517
# Date: 2026-05-17

## Cycle summary

- **Agent:** A
- **Target:** F1 vs F3 weighting selection on `Herm_circ(3)` (BAE
  campaign-residue Open derivation gap)
- **Route:** NCG / KO-dim real-structure spectral triple
- **Pre-closure probability (subjective):** ~18%
- **Outcome:** Honest gap. Partial-narrowing shipped.
- **Branch:** `physics-loop/bae-ncg-kodim-block01-20260517`

## Shipped artifacts

- Source note: `docs/BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17.md`
- Runner: `scripts/audit_companion_bae_ncg_kodim_real_structure_partial_narrowing_2026_05_17.py`
- Runner result: **PASS=45, FAIL=0** (exact sympy verification)

## Mathematical content (verified)

**Positive:**

1. (T1) `J = U_swap * K` is well-defined anti-unitary involution with
   `J^2 = +I` on `C^3` (KO-dim 0 mod 8 family).
2. (T2) `J C J^{-1} = C^{-1} = C^2`. Orbit-orientation reversal.
3. (T3) `[D, J] = 0` for every circulant Hermitian `D = a I + b C + b̄ C^2`
   with `b` complex (the `U_swap`-twist is essential — `K` alone fails
   for complex `b`).
4. (T4) `H_R = +1` eigenspace of `J` is 3-real-dim with explicit
   orthonormal basis `(e_1, e_2, e_3)`. `D` restricted to `H_R` is a
   real symmetric `3 x 3` matrix `D_R` with eigenvalues
   `(lambda_0, lambda_om, lambda_omb) = (a + 2 b_re,
   a - b_re - sqrt(3) b_im, a - b_re + sqrt(3) b_im)`. Same eigenvalues
   as `D` on `C^3`.

**Negative (core finding):**

5. (T5) Spectral-action functional `Tr_{H_R} f(D / Lambda)` on `H_R`
   equals `Tr_{C^3} f(D / Lambda)` on `C^3`. As a symmetric function
   of three eigenvalues, the spectral action weights the doublet pair
   `(lambda_om, lambda_omb)` as two distinct eigenvalues — this is
   F3-style real-dim weighting `(mu, nu) = (1, 2)` at the eigenvalue
   level. F1 multiplicity weighting `(1, 1)` is NOT supplied by
   `J`-projection.

**Counterfactual:**

6. (T6) Pointwise `K` alone does not commute with complex-`b` `D`:
   `K H K^{-1} - H = -2 i b_im (C - C^2)`, vanishes only for `b_im = 0`.
   So `K` is restricted to the 1-real-dim slice of the doublet;
   `J = U_swap * K` is the strict generalization that fixes the full
   2-real-dim doublet.

## V1-V5 Promotion Value Gate

| Item | Question | Answer |
|---|---|---|
| V1 | What SPECIFIC verdict-identified obstruction does this PR close? | The Probe U residual question of whether a canonical `J` exists on `hw = 1` and whether it forces F1. Quoting Probe U: "the repo baseline does not supply a canonical J on the hw=1 lepton sector; this is an extra imported choice." This PR supplies the canonical `J = U_swap * K`, shrinking Probe U's 4-primitive admission count to 3. It also closes the negative direction: even with canonical `J`, F1 is not selected. |
| V2 | What NEW derivation does this PR contain that the audit lane doesn't already have? | The explicit construction of `J = U_swap * K` and the proof that `[D, J] = 0` for complex `b` (unlike `K` alone), together with the explicit `H_R` 3-real-dim basis and the negative-core observation that spectral action on `H_R` equals spectral action on `C^3`. Probe 13 only tested `K, T_alg, *, Theta_H, CPT` (all discrete with K-orbit weighting `(1, 2)`) and Probe U did not supply a canonical `J`. |
| V3 | Could the audit lane already complete this derivation from existing retained primitives + standard math machinery? | No. The `U_swap`-twist is non-obvious: it is the specific modification (a real involution composed with `K`) that allows the real structure to commute with the full complex-`b` doublet rather than restricting to the real-`b` slice. The negative-core observation (T5) requires the explicit basis (`e_1, e_2, e_3`) of `H_R` to make the eigenvalue match exact. |
| V4 | Is the marginal content non-trivial? | Yes. The `J = U_swap * K` construction is new (not in Probe 13's tested set). The fact that `[D, J] = 0` for complex `b` while `[D, K] != 0` is a sharp distinction. The negative-core observation (T5) is a new structural claim narrower than Probe U's: "even with canonical `J` in hand, F1 is not selected" reduces Probe U's 4-primitive count by exactly one. |
| V5 | Is this a one-step variant of an already-landed cycle in this campaign? | No. Closest priors: Probe U (PR #769) used spectral action with unspecified `J`; Probe 13 (campaign synthesis 2026-05-09) tested `K, T_alg, *, Theta_H, CPT` discrete antilinear involutions. None tested the `U_swap`-twisted `J = U_swap * K`. The structural distinction is that this `J` commutes with complex-`b` `D` (extending Probe 13's `K`) while satisfying KO-dim `J^2 = +I` requirements. |

## Forbidden import check

- No PDG observed values consumed.
- No literature numerical comparators consumed.
- No fitted selectors consumed.
- No admitted unit conventions load-bearing.
- No new axiom introduced.
- No new repo vocabulary introduced.
- `A_min` fixed.

## Ledger verification (2026-05-17)

Per `docs/audit/data/audit_ledger.json` `effective_status` values cited
in the note:

- `koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10`:
  retained / positive_theorem ✓
- `cl3_complexification_split_narrow_theorem_note_2026-05-10`: retained
  / positive_theorem ✓
- `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10`:
  retained_bounded / bounded_theorem ✓
- `primitive_p_bae_m1_m2_duality_note_2026-05-10_ppbae_duality`:
  retained_bounded / bounded_theorem ✓
- `bae_block_total_frobenius_derivation_narrow_theorem_note_2026-05-16`:
  unaudited / bounded_theorem (sister narrow theorem, context only)

## Cycle outcome

**Honest gap.** The route was tested constructively and the
mathematical content shipped is a strict improvement over Probe 13
(canonical `J` for complex `b`) plus the negative-core structural
observation that the route does not close F1. This is a legitimate
partial-narrowing of Probe U's residue: one admission primitive
(`J`) is now canonical rather than imported.

The brief's three honest fallbacks corresponded to:

1. **Positive closure** — not achieved. The eigenvalue-symmetric
   structure of the spectral-action functional persists under
   `J`-projection.
2. **Cutoff-sensitive bounded conditional** — not the failure mode.
   The failure is at the eigenvalue level (the doublet eigenvalues
   stay distinct after `J`-projection), independent of cutoff `f`.
3. **Honest gap (partial-narrowing)** — chosen outcome. The note
   ships positive content (T1)-(T4) + counterfactual (T6) and the
   structural negative-core (T5).

## What this cycle did NOT attack

- Multiplicity-counting principles outside the spectral-action class.
- The `U_0` SU(2) positive closure route (separate cycle target).
- Cycle 2 attempts on alternative real-structure routes.
