# C2b review: candidate kinetic-isotropy extension KI+

**Reviewer:** a Claude subagent, same model as the author. Not independent in the model sense; independent only in method and code. Reasoning setting is the one the session supplied.
**Object:** `blocks/C2b/NOTE.md` at commit 40e20dfd3, with its scripts and logs, plus the evidence-restore commit a80252e33. Context read: `blocks/C2/NOTE.md`, `blocks/C2/REVIEW.md`, `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`, the `kinetic_isotropy_primitive` registry node in `docs/audit/data/axiom_premise_nodes.json`, and `docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md` (Theorems 2, 4 and 5).
**Writes:** only this file and `review_scripts/`. No commits made. Every job ran on one core under `nice 10` and took under 6 minutes.

## Evidence (reviewer code, written separately from the author's)

| script | method (how it differs from the author's) | log | result |
|---|---|---|---|
| `review_scripts/rv_group.py` | Finds the subgroups O ⊆ H ⊆ B4 by testing all 2^15 unions of the 16 right cosets of O for closure. Counts invariants from SVD null spaces of (ρ(g) − 1), not from characters. Checks F² and FF̃ as explicit tensors. | `review_scripts/rv_group.log` | `TOTAL: PASS=11 FAIL=0` |
| `review_scripts/rv_select.py` | Works from the parent note's definitions: the identity vᵀGv = 1 − s², then a lex Gröbner basis of G v = 0. Spectra come from the scalar dispersion cos ω = φ0ᵀGφ(k); no 4×4 walk matrix is built. | `review_scripts/rv_select.log` | `TOTAL: PASS=11 FAIL=0` |
| `review_scripts/rv_collins.py` | Same toy model, new integrator. The second p-derivative is taken analytically, with no finite-difference stencil. Quadrature uses the even symmetry to reduce to [0,π]⁴ × 16, on a geometrically graded composite Gauss–Legendre mesh, not the author's sinh map. Two mesh densities are compared. | `review_scripts/rv_collins.log` | `TOTAL: PASS=9 FAIL=2` (kept failed run, see below) |
| `review_scripts/rv_collins_run2_rt_range.py` | Same integrator, with the RT range extended down to m a = 1.95e-4. Limits come from both a geometric tail and a least-squares fit A∞ + c₁m + c₂m ln m. | `review_scripts/rv_collins_run2_rt_range.log` | `TOTAL: PASS=5 FAIL=0` |

**Kept failed run.** `rv_collins.log` fails 2 checks, both on RT, for the reason the author's run 2 failed. With m a ≥ 0.00625 the dimension-5 (RT) anisotropy has only just passed its extremum, so the geometric-tail estimate diverges (step ratio 13.4). No threshold was changed. Run 2 extends the mass range and passes. The T3 and SYM checks in run 1 pass as they stand.

## Per-claim verdicts

### (1) Subgroup claim: B4⁺ is the unique smallest sufficient group. **Correct with a wording fix.** Severity: low.

- **Independently confirmed:**
  - Exactly 7 subgroups of B4 contain O, of orders 24, 48, 48, 48, 96, 192 and 384.
  - The invariant counts (n_S, n_A, n_F) match the NOTE table row by row:
    - order 24: (2, 0, 3);
    - the three order-48 groups: (2, 0, 2), (2, 0, 2) and (2, 0, 3);
    - order 96: (2, 0, 2);
    - order 192: (1, 0, 2);
    - order 384: (1, 0, 1).
  - Only the groups of order 192 and 384 are sufficient.
  - The order-192 group is exactly the det = +1 subgroup of B4, and it equals ⟨O, R_tx⟩.
  - Under B4⁺ the two F-invariants are exactly F² and FF̃.
  - Every group of order below 192 leaves n_S = 2.
- **Fix: the time-reflection wording.**
  - The NOTE says "the minimal symmetric form needs no time reflection" (§0.1) and "time reflection does not need to be imported" (§1).
  - It is true that B4⁺ contains no improper element and no pure T = diag(−1,1,1,1).
  - But it does contain t → −t composed with a spatial flip: R_tx² = diag(−1,−1,1,1), a π-rotation in the (t, x) plane.
  - The author's own log prints `contains t->-t=True` for B4⁺.
  - Suggested wording: "needs no improper element and no separate time-reflection generator; t → −t enters only as R_tx², combined with x → −x".

### (2) Tree level: c_γ = c_ψ under KI+_G; "KI+_w restates the target". **Correct.** Severity: none.

- **KI+_G.** The steps are:
  - n_S = 1 and n_A = 0 make the matter tensor T_{μν} in ψ̄γ_μT_{μν}∂_νψ, and the scalar form, proportional to δ_{μν};
  - n_F = 2 with {F², FF̃};
  - FF̃ is a total derivative and carries no velocity;
  - hence c_γ = c_ψ = a/a_τ = 1.
  This holds given H1 (γ_μ a vector under the spin lift of B4⁺) and H2.
- **KI+_w.** With two sectors, KI+_w is exactly c_γ = c_ψ. With more sectors it extends to all of them. Calling it "the target restated" is fair, and the NOTE does not over-claim it.

### (3) One-loop Collins-type toy. **Correct.** Severity: none (minor presentation fix).

- **Model and agreement.** My integrator implements the stated model with an exact p-derivative and a different mesh. At m a = 0.00625 it reproduces the author's Z_0 − Z_s to all 7 printed digits: T3(0.5) −2.192132e-3, T3(0.25) −1.125564e-3, RT −1.198112e-2. Changing the mesh changes the values by at most 1.4e-8.
- **SYM.** |Z_0 − Z_s| ≤ 7e-17 with analytic derivatives, so the author's 6e-10 is finite-difference rounding. The log slope runs 0.0283 → 0.0268 toward 1/(4π²) = 0.02533.
  - I re-derived that continuum value by Feynman parameters. The coefficient of p² ln Λ is (4/16π²)·3∫x(1−x)dx·2 → 1/(4π²) per ln(1/m).
- **Nonzero a-independent limit.**
  - T3(0.5): |Z_0 − Z_s| grows from 2.03e-3 at m a = 0.025 to 2.239e-3 at 7.8e-4. The step ratio is about 0.5 (O(m a) approach). The fitted limit is −2.245e-3.
  - RT: the anisotropy converges with step ratio 0.59 (an m ln m approach) to −1.1775e-2 (geometric tail) or −1.1734e-2 (fit).
  - The anisotropy is not suppressed by any power of a. This is the Collins mechanism as stated.
- **C coefficients.** C = 8π²(Z_s − Z_0)/mismatch:
  - T3: 0.355 (ε = 0.5) and 0.364 (ε = 0.25). The response is linear, with ratio 1.949.
  - RT: 0.930 (geometric) and 0.926 (fit).
  - These agree with the NOTE's 0.36 and 0.93, not just in order of magnitude.
- **Labelling of the KI+_G stability claim.** It is correctly labelled. §3(b) says "standard symmetry argument; not re-proved here", and the §8 table says "standard symmetry argument, conditional on H1–H4; not re-proved".
- **Fix (presentation).**
  - The RT value C ≈ 0.93 is normalised per unit of the label "r_t = 0.5, r_s = 1", not per unit (r_s − r_t). Per unit Δr it is 1.85.
  - §3(b) quotes "C ≈ 0.36 (T3, per unit ε) to 0.93 (RT)" as if both had one normalisation. State the RT normalisation explicitly.

### (4) Parameter selection on the supplied carriers. **Correct with a wording fix.** Severity: low.

- **Walk.** Re-derived from the parent's G(b) and s = b0 + 2b1 + b2:
  - vᵀGv = 1 − s², wᵀGw = s² and vᵀGw = 0 (exact).
  - So s² = 1 together with G ⪰ 0 forces G v = 0. The NOTE's vector φ0 + φ(X) equals 2v, so it is the same equation.
  - The lex Gröbner basis is zero-dimensional, with b0 eliminant (19b0² − 5b0 − 5)(19b0² + 5b0 − 5). That gives 4 real solutions.
  - Exactly two are PSD, namely ±b_gold. The other pair has eigenvalues −14.38 and −4.51.
  - At b_gold the cone speed is 1 on the axis and on the diagonal.
- **Comparator.** β_t = 1/(Uρ) and β_s = Kρ, so β_t = β_s ⇔ ρ = 1/√(UK), with speed √(UK)ρ. The value 1/1.025 = 0.9756 uses the cited landed reading.
- **Two-tick caveat (spot-checked).** At b_gold, cos ω(X) = −1. The X cone has v_par = 1 and v_perp = 0.2360680 = √5 − 2. Under U² these modes sit at quasienergy 0 with transverse speed 0.236068 per tick, so the caveat is correct.
- **Fixes.**
  - (a) "s(b) = 1 has exactly the solutions ±b_gold" should read **|s| = 1** (s² = 1): s = −1 at −b_gold. Also, the indefinite pair has s = ∓1, so the PSD test is what does the selecting.
  - (b) "Under a single-tick clock these modes sit at energy π/a and decouple" is cited from C7 and not established here. Label it as cited.

### (5) Classification and labelling. **Correct with a fix.** Severity: low–medium.

- **Not derivable.**
  - C2's W2 models A and B share every registered premise under reading K_m, applied to the bare matter action. They have c_γ/c_ψ = 1 and 6/5.
  - So KI+_w, KI+_G and KI+_tick are each underivable from the registered surface under K_m. The NOTE correctly restricts this to the bare action, since model B develops O(α) matter anisotropy once the interaction is on (C2 §3).
- **Fix: "strictly implies the registered primitive" is too broad.**
  - §0.5 says "KI+ strictly implies the registered `kinetic_isotropy_primitive`", and §6 repeats it. This holds for KI+_G and KI+_tick.
  - It fails for KI+_w alone. KI+_w with a universal q_s/q_t ≠ 1 violates c_t = c_s, and K_m does not imply KI+_w (W2). So KI+_w and the registered primitive are independent, which §1 implicitly concedes ("the registered primitive then fixes that number to 1").
  - "Strictly stronger" also holds only relative to reading K_m. The registered text's "equivalently the Euclidean regulator block ... is hypercubic-symmetric" read as K_full, with irrelevant terms included and the full group B4, would imply KI+_G, since B4 ⊃ B4⁺.
  - §1 does say KI+_G is "the content of reading K_full" for velocities. §0.5 and §6 should say "under reading K_m".
- **Labelling: correct.**
  - The header reads "CANDIDATE PRIMITIVE EXTENSION — owner-authorized study, not adopted".
  - The Status line says "not adopted", says it is not entered in `axiom_premise_nodes.json`, and says adoption needs an owner act under AXIOM_MINIMALITY_POLICY §6.
  - Commit 40e20dfd3 touches only files under `blocks/C2b/`.
  - KI+-dependent statements are flagged as conditional.
  - No fix needed beyond the one above.

### (6) Evidence preservation: deleted committed log. **Finding: confirmed.** Severity: medium (process). Restoration: done, with one documentation step remaining.

- **What happened.**
  - WIP checkpoint 7b6117b76 committed `logs/kip_collins_toy.log`: 48 lines, 4658 bytes, sha256 `c6399515…b7b0`.
  - Commit 40e20dfd3 deleted it. Rename detection pairs it with the new `kip_collins_toy_run2_rt_needs_smaller_mass.log`.
- **What it is.**
  - It is an in-progress snapshot of the run that became "run 2", captured mid-run at 295 s. It stops at `T3 par=0.25 m=0.003125 N=72`, before any PASS/FAIL line or TOTAL.
  - It was produced by the script version at 7b6117b76, before the RT range was extended.
  - It is byte-identical to the first 48 lines (4658 bytes) of the run-2 log. So it "differs" from the run-2 log only by being a strict truncated prefix. No numbers were lost or altered.
- **Restoration status.**
  - Commit a80252e33 adds `logs/kip_collins_toy_committed_snapshot_RESTORED.log`. I checked that it is byte-identical to the blob at 7b6117b76 (same sha256). That restores the content.
- **Still needed.**
  - (i) NOTE §8 "Kept failed runs" should list the restored file. It should say that it is a truncated WIP-checkpoint snapshot of run 2, written by the pre-extension script at 7b6117b76, and a prefix of `kip_collins_toy_run2_rt_needs_smaller_mass.log`.
  - (ii) The stale reference in `scripts/kip_flow.py:53` ("see kip_collins_toy.log") should point to `kip_collins_toy.runall.log`.
  - (iii) Process: the WIP-checkpoint mechanism snapshots logs that are still being written. It did so again during this review: checkpoint 2d37ee179 committed a partial `review_scripts/rv_collins_run2_rt_range.log`, and the working-tree file is now the complete run. The final commit of this review should carry the complete log. Checkpoints should not later delete or rename such snapshots; they should keep them under a `_snapshot` name.

## Summary table

| claim | verdict | severity | fix |
|---|---|---|---|
| (1) B4⁺ unique minimal sufficient | correct with fix | low | "no improper element"; t → −t appears only as R_tx² |
| (2) tree-level c_γ = c_ψ; KI+_w is the target restated | correct | none | none |
| (3) Collins toy, C ≈ 0.36 / 0.93, a-independent; KI+_G stability labelled standard | correct | none (presentation) | state the RT normalisation (per Δr it is 1.85) |
| (4) ±b_gold, ρ = 0.9756, two-tick caveat | correct with fix | low | |s| = 1; label single-tick π-mode decoupling as cited from C7 |
| (5) not derivable; candidate labelling | correct with fix | low–medium | "strictly implies" holds for KI+_G and KI+_tick and only under K_m; KI+_w is independent of the registered primitive |
| (6) deleted committed log | finding confirmed; restored byte-identical in a80252e33 | medium (process) | list it in §8 as a run-2 prefix snapshot; fix the `kip_flow.py` reference; stop checkpoints from deleting snapshots |

No claim is incorrect. The load-bearing numerical step was re-derived with different code and agrees to 7 digits: B4-breaking irrelevant terms give an anisotropy that tends to a nonzero, a-independent constant, and the symmetric action gives exactly zero.

## Correction confirmation

I read the whole corrected `NOTE.md` (§0–§9) and checked the `scripts/kip_flow.py` diff since 40e20dfd3. It changes only the comment on line 53, so the logs still stand.

| item | status |
|---|---|
| (1) time-reflection wording | Resolved (§0.1, §1). "No improper element, no separate time-reflection generator; t → −t only as R_tx² = diag(−1,−1,1,1)." |
| (3) RT normalisation | Resolved (§3(b), §4). 1.85 per unit Δr, which is 0.93 at Δr = 0.5. This is consistent with C = 8π²·0.01175/0.5 = 1.86. |
| (4) \|s\| = 1; π-mode decoupling | Resolved (§0.4, §5). s = −1 at −b_gold. Single-tick decoupling is marked as cited from C7 §5. |
| (5) "strictly implies" | Resolved (§0.5, §1, §6). It is restricted to KI+_G and KI+_tick under K_m, and KI+_w is stated to be independent. |
| (6) restored snapshot; stale reference | Resolved (§8). The snapshot is listed as a WIP-checkpoint artifact with no data lost, and the kip_flow.py comment is fixed. |

**Two nits (optional, not blocking):**
- In §8 the closing bullet "In neither case was any expected constant changed" now sits after three items. It should read "In none of these cases".
- The snapshot entry could also say that it is a byte-identical 48-line prefix of the run-2 log, written by the script version at 7b6117b76.

**No new defect found.** The Status line reports review provenance without model identifiers. The candidate and not-adopted labelling is unchanged. No headline claim was altered beyond the requested wording.

**Final verdict: ready.** It is ready as a reviewed **candidate** (not adopted). Adoption still needs an owner act under AXIOM_MINIMALITY_POLICY §6.
