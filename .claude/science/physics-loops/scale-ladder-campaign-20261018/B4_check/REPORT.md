# B4 independent check: claims hold, with corrections

Provenance: a fresh-context agent of the same model family, independent of the author only in code path. It used exact rational polynomial invariants. Saved by the supervisor from the hand-back.

## (a) Form counts: confirmed

- **Counts.**
  - S4: 38 forms, 2 gauge-invariant.
  - B4: 9 forms, 1 gauge-invariant.
  - B3×Z2: 26 forms, 2 gauge-invariant.
  - No symmetry: 10 gauge-invariant in 4D, and 1 in 3D.
- **Theorem (exact check).** The 4D gauge-invariant forms are L_M = εε M k k h h, with M symmetric.
  - L_I = −(flat Fierz–Pauli).
  - For non-degenerate M, L_M has the same ray as Einstein–Hilbert about g0 = M.
  - In temporal gauge, det = Q²·(−16w⁸) with Q = adj(M)(k,k), so there is one cone for every gauge-invariant form of any signature.
- **Wording.** "EH about I + c(J−I) up to scale and sign, c ∈ R ∪ {∞}, with degenerate limits at c = 1 and c = −1/3."
- **Not cited.** The repo already proved the 10-dimensional class equals background-metric EH, with Regge giving −½ EH, in `docs/CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md` and the 06-09 note. FINDINGS §1 re-derives this without citing it.
- **Supplied.** g3 = 0 exactly needs zero tilt, which holds because the edge lengths are supplied to realise δ. This is the Kostelecký–Mewes-type structure (recalled).

## (b) ε₃ = 0 for the curvature member: true, but supplied

From the rotation-invariant kinetic term, M1 = α+β, M2 = 2β and M3 = 2α, so ε₃ = 0 by construction. The TT speed Kp²/(4α) is confirmed analytically.

## (c) Closure forces ε₃ = 0: confirmed and robust, with caveats

- **Result.** In exact arithmetic, on 3³, 4³ and 5³ tori, for generic lapse pairs and both corner timings, the closing set is the single ray (2,−1,1): DeWitt with ε₃ = 0. The base ranks are 78, 189 and 372.
- **Caveats.**
  - It needs closure for all lapse pairs. Some pairs close for every kinetic form, or fix c only.
  - It depends on the supplied face-timing clause; with single-corner timing nothing closes.
  - **Label error.** The script's "ε₃ = +0.1" is actually −1/11, and "−0.2" is +1/4. The conclusion is unaffected.
  - This is the lattice form of Hojman–Kuchař–Teitelboim. Only R1 and the kinetic term enter. It holds at leading order.

## (d) Attribution

- **Supplied:** ε₃ = 0 of the kinetic term, c_t = c_s, zero tilt.
- **Derived, conditional on supplied clauses** (closure rule, face timing, R1 placement, ultralocal kinetic ansatz): closure forces ε₃ = 0.
