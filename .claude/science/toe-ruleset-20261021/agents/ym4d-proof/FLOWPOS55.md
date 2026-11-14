Reviewer model: claude-opus-5-5

# FLOWPOS55 — the coupling flow with plane-dependent couplings (Flow-pos)

Worker: Opus 5.5 (claude-opus-5-5), max reasoning. Task brief: scratchpad/queue/flowpos.md. Shared rules:
scratchpad/REVIEW_BRIEF_55.md. Status of everything below: worker draft, NOT banked; a Codex reviewer checks
before anything is banked.

## PRE-STATED (written 2026-10-29T06:28:53Z UTC, before any derivation)

Targets.
- T1. State (Flow-pos) for plane-dependent coupling fields: the coupling is a field g_k(P) (or an
  equivalent per-plane-orientation field) on the level-k lattice; state the relative polydisc around the
  constant-coupling trajectory, its radius, the Hölder (Wilson-Hölder) class in which the field is
  controlled, and the uniformity in the RG level k, the time extent T and the lattice spacing a.
- T2. Prove (Flow-pos) from named structural flow hypotheses (the plane-dependent generalisation of
  SRC2_55 Proposition FP's three hypotheses), each tied to the open items of the constant-coupling flow
  ((UIR^♮)/(ρ-null) or the weaker two-sided slope bracket), handling explicitly (i) the harmonic-versus-
  arithmetic averaging of Proposition HOM and (ii) the O(1)-relative anisotropic remainder −(u/4)ε²;
  OR exhibit an obstruction (an anisotropy or inhomogeneity mode that grows along the flow).
- T3. State, as implications only, what the result gives to SRC2_55 Theorem II and to the sphere route's
  W0 / LCS-a (SEAM55, ASSEMBLY55 ML4).

What counts as a refutation of a positive (Flow-pos) claim (any one suffices).
- R1. A mode of the linearised plane-dependent flow (anisotropy between plane orientations, or spatial
  inhomogeneity at some scale) whose relative size is multiplied per step by a factor ≥ 1 + c·g_k^2 with
  c > 0 not summable along the flow, i.e. growth of the relative deviation by a power of log(1/a) or of
  1/g_k^2 — this would refute uniformity in k and a.
- R2. A per-step relative-polydisc map that fails to send the polydisc into itself at the stated radius
  for some admissible plane-dependent initial field (e.g. because the HOM remainder is O(1) relative to
  the polydisc radius and is not compensated by contraction).
- R3. A dependence of the radius r_F on T or a (beyond what the hypotheses permit), or a Hölder class
  that the flow does not preserve (Hölder seminorm grows per step by a non-summable factor).
- R4. A derivation step that uses the constant-coupling flow's open items ((UIR^♮)/(ρ-null)) in a
  stronger form than they are stated, or uses a symbol (ε, r_F, c_1, θ, κ, …) for a different object than
  the file it is cited from defines.

What I will NOT claim. Nothing is banked by this file; every result is CONDITIONAL on the named inputs;
the scalar-model Proposition FP of SRC2_55 is an input whose proof I re-derive rather than quote.
