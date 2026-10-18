# HIER-2 PREREG follow-ups (dated; PREREG.md itself is unchanged)

## 12:16Z — deviations after the first runs

1. **A4 replaced by a stronger, model-independent version.** The PREREG planned a lattice illustration in the two-band naive Weyl model. Doing the algebra first showed a limitation: at the eight nodes that model's folded Bloch Hamiltonian is exactly ε·V, with no remote bands, so every Dirac mass is exactly linear in ε or exactly zero. It cannot show an order-raising effect. So I dropped the lattice run. In its place A3/A4 use a **generic equivariant effective Hamiltonian** on the 16-dimensional node space: H(ε) = Σ_n ε^n f_n(φ), with each f_n the group average of a random degree-n polynomial map, normalised to unit norm. This is the generic member of the symmetry class. The two-band statement ("orders 1 or ∞") follows by inspection and is not run.
2. **Extra checks added after the first A3 run (11:49Z).** That run used unnormalised f_n, and higher orders contaminated the slopes (one non-integer slope, 0.49). Its result is superseded; it showed orders {1, 3} only. The additions:
   - **Nested span check (A3).** V_1 ⊆ V_3 ⊆ V_5 ⊆ Fix(Stab φ) on the chirality-odd operators. If V_1 + V_3 already equals Fix, no new structure can appear at order ≥ 5.
   - **Node-representation variants.** I added eight of them: a character of O on the {k*, −k*} orbit (A1 or A2), times a character of D4 on the six doubler nodes (A1, A2, B1 or B2). They cover the PSG twist freedom between orbits that a corner-model node representation may carry.
   - **Independent code path for the charge-111 cases** (`check_saturation.py`). It solves the equivariance constraints directly by a Kronecker null space, and shares no code with `orders_group.py`.
3. **Fit control (A1/A2).** It ran as planned, with one addition: a random-spectrum control. The ε grid in the sector-blind fit went up to 0.9. Fits with ε above about 0.5 need very large exponents (up to 40), which in practice turns ε into a continuous dial. They are reported but given no weight.
4. **Sector-blind fit.** Also as planned. An observation from it: a ×10 sector-blind fit exists (×9.9 at ε = 0.2165, n = (7, 4, 1), set M_Z).

None of these changes alters a reading criterion.

## 13:02Z — runs completed; files superseded

- `scripts/orders_naive.out` and `scripts/orders_twist.out` come from earlier versions of `orders_group.py`. They are superseded by `orders_A1-A1.out` (the per-line results are identical) and `orders_A2-A1.out` (a coset-induced twist, which replaces the ad-hoc twist).
- Also run, after A3:
  - `fit_twolevel.py`, the best fits allowed when only the orders {1, 3} occur. It uses only the A3 result and no new criterion.
  - `parse_variants.py`, a summary of the eight variants.
- `check_saturation.py` reached a peak RSS of 322 MB, under the 400 MB cap.
- No processes are left running.
