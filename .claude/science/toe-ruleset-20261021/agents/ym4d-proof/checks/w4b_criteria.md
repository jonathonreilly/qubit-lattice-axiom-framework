# w4b criteria (lane H, session 4), written 2026-10-28 after w4 run 2 (OVERALL FAIL by design flaw), before w4b_footprint.py

w4 run 2 failed C and D because its random histories relaxed almost every cube. w4b keeps the model, the reading rules and
criteria A-D of w4_criteria.md verbatim, and changes ONLY the history generator and the link sampler:
- histories: at each level j, n_U = 2 cubes of 𝒰_j drawn uniformly from the cubes outside Σ(Ω^c_{j-1}) (A2), so the relaxed
  sets are sparse;
- links: per (history, k), half the sampled level-k links are drawn among links whose two endpoint cubes project into
  A_{k+1} (relaxed column; feeds B and D), half uniformly (feeds A and C).
Disclosure: this is a post-hoc redesign after seeing w4 fail; the pass criteria are unchanged. OVERALL PASS needs A, B, C, D
in both dimensions, with B, C, D each tested at least 10 times per dimension.
