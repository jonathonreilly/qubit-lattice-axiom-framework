# Author brief LGF-LIB: rebuild the lattice Green's function estimates that H_int needs

Lead: Claude Opus 5.5, 2026-10-29. One Codex author context runs on the laptop, and a fresh reviewer follows it.
Process: PROCESS_LIGHT.md. Edit in place. Pre-register numerical checks only. Independent review. Rebuild the result; do not cite it.

## Why
The non-freeness witness (H_int, one of the four top-level T_OS inputs) rests on Lemma FREE in TSE55.md (around l.194-208). FREE is PROVEN given **(LGF)**, but (LGF) is "[m], IMPORTED-standard, not re-derived here".

CODEX_REVIEW_TSE.md R11 (around l.158-170) records two things:
- the import is NOT-VERIFIED;
- the torus wording is false at order 0. A counterexample by summation by parts shows that a T^{-2} correction is needed at |α| = 0, and the natural correction at |α| = 1 is T^{-3}.

Only the **order-2 torus estimate with a T^{-4} correction** is consumed by FREE and R9. This is a self-contained piece of mathematics with a known proof route, so it is a library rebuild.

## Target: Theorem LGF, statement fixed first, with all conventions explicit
Fix these conventions:
- **The operator.** Use the one FREE actually uses: Δ = d*d + dd* on functions, which equals 8(I − P) in d = 4. Check this against TSE55 and the lane's Feynman-gauge propagator 𝔊^F = dΔ^{-1}d*.
- **The normalisation of G.**
- **The torus.** Side T, with the zero mode removed: ΔG_T = δ_0 − T^{-4}.
- **The lattice differences ∇^α.**

Then prove:
- **(i) Z⁴.** For |α| ≤ 2 and |x| ≥ 1,
  |∇^α G(x) − ∂^α c_4|x|^{-2}| ≤ C_α |x|^{-3-|α|}.
  Determine c_4 for this normalisation; 1/(4π²) belongs to the unit-normalised Laplacian. Give explicit numerical constants C_α. Sharper rates, such as |x|^{-4-|α|}, are welcome if proven.
- **(ii) Torus, order 2 (the consumed form).** For 1 ≤ |x| ≤ T/4,
  |∇^α G_T(x) − ∂^α c_4|x|^{-2}| ≤ C_α|x|^{-5} + C'_α T^{-4} for |α| = 2,
  uniformly in T. Make the image sum, the orbit cancellation and the zero-mode quadratic polynomial fully rigorous.
- **(iii) Torus, orders 0 and 1 (correct forms).** State and prove these with the T^{-2} and T^{-3} corrections. Show that the uncorrected order-0 version is false, either by giving R11's counterexample in full or by improving it.
- **(iv) Consumer form.** Restate exactly what Lemma FREE uses, namely
  𝔊^F(p,q) = D_{μν,ρσ}(x_p − x_q) + O(r^{-5}) + O(T^{-4}),
  and prove it from (i)-(ii). Include the Weitzenböck/Feynman-gauge step, which reduces the operator to the componentwise scalar Laplacian.

## Proof method
- Use Fourier analysis on the Brillouin zone.
- Expand 1/Δ̂(p) around p = 0. Use the cubic symmetry of the quartic correction.
- Control the remainder by smooth cutoffs and repeated summation by parts, or by Littlewood–Paley. Every constant must be explicit.
- Literature, for method only: Spitzer; Lawler–Limic §4.3; Uchiyama; Fukai–Uchiyama. Credit them by name. Nothing from the literature may be load-bearing, and anything taken from memory is marked [m] and counts as residue.

## Numerical check (optional; pre-register it)
- Write checks/lgf_criteria.md before writing any script.
- Compute G on Z⁴ and on tori (T = 8, 16, 32) at small |x|. Use exact or high-precision quadrature, and use interval arithmetic (mpmath.iv) for any value that the proof relies on.
- Compare against the proven constants. Floating-point output is a diagnostic and must never be labelled "certified".
- Run one process, under `nice -n 10`, with BLAS threads = 1. Keep RSS under 1 GB, with the script checking it itself, and keep each job under 20 minutes. Start only if load < 8 and free memory is ≥ 30%. No pools.
- Numeric lock: `until mkdir /Users/jonreilly/Projects/Physics/.claude/worktrees/ym4d-lgf/.locks_numeric 2>/dev/null; do sleep 20; done`, run, then `rmdir` exactly once.
- Note: the Codex sandbox forbids raising nice. If the run is blocked, report that and do not weaken the guard. The lead reruns it outside the sandbox.

## Write
- **LGF.md**, containing:
  - the theorem and its proofs, each marked PROVEN, ARGUED or OPEN;
  - a "Consumers" table covering TSE55 Lemma FREE, R9 and CODEX_REVIEW_TSE R11, with exact quotes;
  - the open residue;
  - the binding fixes this implies for TSE55's (LGF) wording.
- **LGF_LOG.md**, and **checks/lgf_\***.

## Rules
- Edit nothing else.
- No commits or PRs.
- Do not touch audit or ledger files, and do not edit the axioms.
- Final message: under 300 words.
