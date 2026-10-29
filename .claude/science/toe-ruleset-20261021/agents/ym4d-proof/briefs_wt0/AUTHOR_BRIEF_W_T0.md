# Author brief W-T0: put the non-freeness witness on the OS algebra

Lead: Claude Opus 5.5, 2026-10-29. One Codex author context on the MacBook, followed by a fresh reviewer.
Process: follow PROCESS_LIGHT.md. Edit in place; pre-register numerics only; independent review; rebuild rather than cite.

## The gap
ASSEMBLY55 **F1** (around l.390-401) says: "H_int ↛ T_OS: the witness is not on the OS algebra".
- HINT2_55's witness uses the 4D-flowed bare density 𝓔.
- Its one-point function is not an OS invariant (HINT2_55 R1.10 (ii), Codex CONFIRMED).
- The e-field algebra of N2-N4 does not contain 𝓔.
- No file proves that non-freeness on the joint Euclidean state implies non-freeness of the reconstructed theory.

Repair (a), **(W-T0)**, is the one you implement. It uses HINT2_55 **R1.9 Proposition T0** (around l.280-300), the time-zero 3D-flowed magnetic witness 𝓑. For site reflection 𝓑 lies in 𝔄₊, its comparator value f_B is a reconstructed-theory number, and it is monotone. CODEX_REVIEW_HINT2 (around l.134-140) records what T0 does **not** do:
- it gives no continuum sharp-time YM observable, Hilbert-space domain or moment bounds;
- a first-moment bound does not give a vector [𝓑], because the vector's norm needs a second moment;
- it does not prove absolute non-freeness;
- the word "only" at HINT2_55 :312 and :555 claims too much;
- there is a 2N normalisation error in one coefficient.

## Deliverables (in W_T0.md)
1. **Theorem T0-OS, the reduction.** State it precisely on the common algebra and the common sequence used by N1F/N1S. It has the form: if (MOM2-B), (TS-up)^B, (TS-low)^B and (SHARP-B) hold, then the reconstructed theory satisfies |f_B^{YM}(t₀) − f_B(μ)| ≥ c > 0 for every μ in the named free comparator class. Hence it is not in that class. The input names are yours to fix exactly.
   - Prove the implication completely.
   - Include the step from Euclidean data to the reconstructed-theory number: the Hilbert vector [𝓑], its norm from the second moment, and ⟨Ω,[𝓑]⟩.
2. **(ALG) extension.** Add 𝓑, its translates and its rotated versions (other time directions) to the OS algebra.
   - Show compatibility with OS0-OS3 as N1F consumes them.
   - Say which E(4) elements act and which act only through rotated copies.
   - Check consistency with OSLEAF55's test algebra and the ordered positive-half cone.
   - If 𝓑 cannot be put on the same algebra as the e-field family, give the exact obstruction.
3. **What is provable now.** Prove every piece that does not need new Yang–Mills estimates. Examples:
   - at fixed lattice cutoff, 𝓑 is bounded and depends on one time slice, so its site-reflection pairing is exact (CODEX_REVIEW_HINT2);
   - T0's comparator formula for generalised free fields, with the 2N normalisation fix;
   - narrowing the "only" claim;
   - limit passage of f_B along the common subsequence, given the moment inputs.
4. **The YM-side inputs, named exactly.** These are open leaves:
   - (MOM2-B): uniform second moment;
   - (TS-up)^B and (TS-low)^B;
   - (SHARP-B): sharp-time finiteness in the continuum.

   For each one, give the exact statement and the existing lane result or obligation that would supply it. Quote the source: SRC-κ, (LF-inst), H-Bal-1, H-loc-LF, and ASSEMBLY55 N15/F17.
   - Say plainly whether each one is easier or harder than the corresponding 𝓔 input.
   - Do not prove these inputs.
5. **Consumers table.** List ASSEMBLY55 N5 and F1, PANEL_P1 item 4, and CODEX_REVIEW_P4 §4.3, with exact quotes, and say what is discharged.

## Rules
- Literature is for method only and must not be load-bearing. Mark anything recalled from memory as [m].
- Numerics: none expected. If you run any, pre-register the criteria in checks/wt0_criteria.md first and follow the laptop resource rules (nice, BLAS=1, under 1 GB, load < 8, at least 30% memory free).
- Write W_T0.md and W_T0_LOG.md only. No other edits, no commits, no audit or ledger files, no axiom edits.
- Final message under 300 words.
