Reviewer model: claude-opus-5-5

# ALIGN55 — (ALIGN-ℓ): a level-local alignment with regularity across levels, for the background transfer (R2) on 𝒞_glob

## PRE-STATED (written 2026-10-29T01:33:54Z, before any derivation in this file; only BGT55.md and REVIEW_BRIEF_55.md read so far)

Role: worker (Opus 5.5), scope given by the lead. Write-set: this file and `checks/al55_*` only. No git.
The Balaban paper directory /Users/jonBridger/Documents/balaban-cmp/ was EMPTY when checked (2026-10-29T01:33Z); CMP 99:75 is not
available to me locally. Anything I say about it below is from the lane's own extracts (BALABAN_EXTRACT.md), labelled as such.

### Targets
- T1. State (ALIGN-ℓ) precisely: every quantifier (k, T, background, ε), every norm, and exactly which inequality each of Theorem GA's
  inputs (A1) [t_+, t_*, invertibility] and (A2) [δ_Υ] consumes from it, in the transport-weighted pair (|||·|||_♯ → N).
- T2. Construct a candidate alignment: starting from the per-level slice functional Γ_PL (GSHARP55 Lemma PL-adm), and/or an
  axial-in-blocks construction adapted to the soft scheme; explain how it avoids (or fails) the two recorded axial failures
  (global axial: factor T, Dirac string; within-cell axial: sup budget fails by L^k — NLOC.md).
- T3. Prove regularity across levels uniformly in k and T in the transport-weighted norm — or isolate the exact obstruction,
  as a precise statement with a witness or a power count, and say which.
- T4. Assemble: Theorem GA + (ALIGN-ℓ) ⇒ (R2) on 𝒞_glob, as an implication, every input named with its status.

### What would count as a refutation of my own construction (stated in advance)
- R-a. The candidate Λ_W fails to be a left inverse (Λ_WΞ_1 ≠ −1 on Λ_0), or Υ_W fails exact alignment Υ_WΞ_1 = Ξ_ZA —
  tested in exact rational arithmetic on a small multi-level model.
- R-b. A level-l unit datum (charge, or level-l link field) whose image under the candidate's completion map (Λ_W^T on sources,
  or Λ_W on fields) has a coarse size that grows with k (e.g. ≍ L^{3l} spikes, the S_E failure) or with T (Dirac string).
- R-c. An explicit chain x with |||(Ξ_z − Ξ_1)Λ_W x|||_♯ ≥ c·η·f(k,T)·|||x|||_♯ with f unbounded — i.e. the cross-level regularity
  fails in the transport-weighted norm.
- R-d. Any step where a level-l gauge value depends on data at level l′ ≠ l in a way not dominated by a geometric factor in |l − l′|
  (in the transport weight), when level-locality is claimed.
- R-e. Any constant that depends on k, T or volume where uniformity is claimed.
- R-f. Silent use of S_E's completion (BGT55 §6.4 refuted it as an alignment at levels ≥ 1 by power count) or of a refuted input
  (relative-Hessian series, (GAP-Z) as input, TRANSP slot transport).

### Gate discipline
Any numeric check: `checks/al55_<id>_criteria.md` with pre-registered PASS/FAIL written before the script; exact rational
arithmetic only (python fractions), no floats for verdicts.

---
