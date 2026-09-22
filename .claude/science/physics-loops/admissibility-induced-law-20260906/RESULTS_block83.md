# Block 83 — results (2026-09-22)

- Runner `scripts/admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_rest_energy_needs_the_bonds_own_amplitude_2026_09_22.py`: `TOTAL: PASS=14 FAIL=0`; 8 mutations, each in its own family (1 s).
- T1 (exact, `4³`, `δ = 3/10`): frame-coupled alternation `=` free walk; block 64's strain-coupled alternation `= 0` operator; `B_a^a = d_aξ_a`, `ξ_a = −(δ/2)(−1)^{x_a}`; all curls `0`; volume sum `= N`.
- T2 (exact): `½{X, S_j}` and `½{C_a[v], S_a}` have zero corner matrix elements for generic rational `X`, `v`; the bond-amplitude corner block is nonzero and squares to `3δ²`.
- T3 (exact): ring of four, bond-amplitude alternation: energies `±|δ|` ×2, `±1` ×2; `E_sea = −2 − 2|δ|`; translation by `(1,1,1)` conjugates `+δ` to `−δ` on `4³`.
- Control (`specs/supervisor_control_block83_relabelling.py`): `6³`: frame/strain couplings identical to free (max difference `0`), bond amplitude gaps at `√3δ = 0.5196`; smooth strain: corner elements `~10⁻¹⁸`, zero modes move to within `4·10⁻⁵` of zero (no gap); sea on `8³`: bond amplitude `−1.190 → −1.732` (`δ: 0 → 1`), frame-coupled constant `−1.190`.
