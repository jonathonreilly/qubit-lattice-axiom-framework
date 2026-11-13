# Assumptions and Imports

## Mathematical Definitions Used

All definitions in [`docs/U5_THREE_PLUS_TWO_FMS_PROJECTOR_CARRIER_BOUNDED_THEOREM_NOTE_2026-11-09.md`](../../../../docs/U5_THREE_PLUS_TWO_FMS_PROJECTOR_CARRIER_BOUNDED_THEOREM_NOTE_2026-11-09.md) are stated explicitly in the note from first principles:

- Standard Pauli matrices $\sigma_1, \sigma_2, \sigma_3 \in M_2(\mathbb{C})$ and internal Hilbert-Schmidt square $|M|_{\mathrm{HS}}^2 = \operatorname{Tr}_{M_d}(M^* M)$ on $\mathcal{A} \otimes M_d(\mathbb{C})$.
- Canonical anticommutation relations (CAR) $\{f_\alpha, f_\beta\} = 0$, $\{f_\alpha, f_\beta^\dagger\} = \delta_{\alpha\beta} I$ on the five-mode site Fock spaces $\Lambda(\mathbb{C}^5)$ and the ten-mode link Fock space $\Lambda(\mathbb{C}^{10})$ restricted to the half-filled five-rishon register $\Lambda^5 \mathbb{C}^{10}$ ($\dim = \binom{10}{5} = 252$).
- Standard real embedding $\iota: M_5(\mathbb{C}) \to M_{10}(\mathbb{R})$ mapping $x + i y \mapsto x I_2 + y J_2$ and the Lie algebra $\mathfrak{so}(10) = \{X \in M_{10}(\mathbb{R}) : X^T = -X\}$.

## External / Unlanded Dependencies

- **None.** Zero unlanded branches, external datasets, or fitted parameters are imported.

## Scope Boundary (What Is Not Claimed)

- Does not construct a dynamical stationary state $\omega$ of a coupled lattice tick or prove that such a state concentrates on the $3+2$ orbit.
- Does not establish two-sided near-unitarity ($\omega(\|T^\dagger T - I\|_{\mathrm{HS}}^2) \le \delta$) for long-distance determinant-square transport or an infrared mass gap.
