# Koide Q = 2/3 — Block-Weight Hardening (bounded note)

**Date:** 2026-05-28
**Claim type:** bounded_theorem (exact structural core + one named
residual admission)
**Status authority:** none asserted. Imports no axiom, no comparator, no
convention; promotes no row. Sets no retained status. Local-branch
working source note for audit triage.
**Scope:** harden the F1-vs-F3 selection crux identified in the sister
notes `KOIDE_Q23_EXTREMAL_BRIDGE_PANEL_FINDINGS_2026-05-28.md` and
`KOIDE_Q_TWO_THIRDS_EXTREMAL_PRINCIPLE_ASSUMPTIONS_AUDIT_NOTE_2026-05-28.md`.
Runner: `scripts/koide_q23_central_trace_hardening_2026_05_28.py`;
cache `logs/runner-cache/koide_q23_central_trace_hardening_2026_05_28.txt`.
Companion derivations (working, `.claude/science/derivations/`):
`koide-q23-extremal-from-a1a2-2026-05-28.md`,
`koide-q23-assumptions-audit-2026-05-28.md`.

---

## 0. Object

For charged leptons, `Q = (sum m_i)/(sum sqrt(m_i))^2 = 2/3` empirically.
With `s_k = sqrt(m_k)` and the `C_3` circulant surface, the algebraic
reduction (sister notes) is `Q = 1/3 + (2/3)(|b|^2/a^2)`, so
`Q = 2/3  <=>  |b|^2/a^2 = 1/2  <=>  E_+ = E_perp`, where
`E_+ = 3a^2` (trivial isotype, 1 real dim) and `E_perp = 6|b|^2`
(doublet isotype, 2 real dim). The whole bridge is the isotype-weight
choice; F1 = `(1,1)` (per-block) selects `Q=2/3`, F3 = `(1,2)`
(per-real-dimension) selects `Q=1`.

## 1. Exact structural results (no admission)

All verified in the runner.

1. **Q is the purity of the sqrt-mass distribution.** `Q = sum_k p_k^2`,
   `p_k = s_k/sum_j s_j`; `Q in [1/d, 1]`, `n_eff = 1/Q`. (Identity.)
2. **The democratic direction is FORCED, not chosen.** The generation
   space is `Cl(3)` grade-1; the color-`Z_3` automorphism permutes
   `(sigma_1,sigma_2,sigma_3)` as the regular representation, whose
   unique `Z_3`-fixed axis is the body diagonal `(1,1,1)`. The trivial
   isotype `E_+` is therefore canonical.
3. **Kähler (1,1) structure is `Cl(3)`-native.** Frobenius–Schur:
   `R[Z_3] = R (+) C`. The doublet isotype is ONE complex line; its
   complex structure `J` (`J^2 = -I`) is the `Cl(3)` grade-2 bivector
   dual to the body-diagonal axis (rotation generator about `(1,1,1)`).
4. **Three canonical isotype weightings = three special Koide values.**
   `(p_+,p_perp) = (1,0)/(1/2,1/2)/(1/3,2/3)` give
   `Q = 1/3 / 2/3 / 1 = (Q_min, midpoint, Q_max)` exactly.
5. **Block count.** `R[Z_d]` has `B=2` real-irreducible blocks only for
   `d in {2,3}`; `d=2` gives the degenerate `Q=2/d=1`, so `d=3` is the
   unique nontrivial `B=2` case.
6. **d=3 double-characterization is transversal.** Equipartition value
   `2/d` equals range-midpoint value `(1+d)/(2d)` iff `d=3`;
   `Delta(d) = (d-3)/(2d)` is a simple zero, slope `1/6`.

## 2. Killed routes (negative results)

- **Canonical / Plancherel central tracial state does NOT select F1.**
  It weights blocks by `dim^2/|G| = (1/3,2/3)` → `Q = 1` (= F3, `Q_max`).
  So "equipartition = canonical central trace" is false; the literature
  lead naming the Frobenius–Schur central trace, read as the canonical
  trace, lands on `Q_max`, not `2/3`. Confirms the panel's lattice-QFT
  escape failure from the algebra side.
- **Pure-state purity does NOT force F1.** In the Bloch-trine embedding,
  `|n|=1` fixes `a^2+b^2=1` but leaves `|b|^2/a^2` free.
- **`rho_ref = (x) I/2` restricted to generations is uniform** → `Q=1/3`
  (`Q_min`), the opposite extreme.

## 3. Residual admission (the bounded boundary)

**A-block.** The physical packet sits at **equal-block weight**
`(1/2,1/2)` = maximum entropy over the `B=2` Frobenius–Schur block label.
This is the F1 selection. It is **named, not derived**. It is tied to A1
(the qubit is a 1-bit / 2-valued primitive; `B=2` holds exactly for
`d in {2,3}`), but a first-principles law forcing max-entropy over the
*block* label (→ `2/3`) rather than the *state* label (→ `1/3`) or the
dimension-weighted trace (→ `1`) is not established here. The two
independent exact anchors (equipartition `2/d`, range-midpoint
`(1+d)/(2d)`) coincide only and transversally at `d=3`.

## 4. Falsifiable prediction

Exactly three Koide-coherent charged-fermion generations: a `d=4`
democratic packet would need `Q_equi=1/2` but `Q_mid=5/8` (inconsistent),
so no 4th charged lepton can extend `(e,mu,tau)` into a `Q=2/3` quadruplet.

## 5. Honest status

Bounded. The structural core (§1) and negative results (§2) are exact;
the single residual admission (§3, F1 selection) is the open frontier,
sharply localized. No closure claimed.
