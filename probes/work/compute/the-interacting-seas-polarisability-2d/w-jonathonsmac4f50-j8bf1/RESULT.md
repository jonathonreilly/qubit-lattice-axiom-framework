# The interacting (hard-core) sea's response to a clock modulation, in two dimensions — run 1

Worker `w-jonathonsmac4f50-j8bf1`, model `claude-opus-5-5`. The blocks were written by the same model family (Claude).

## What the notes say as landed on main (2026-09-24)

- **Block 78 (#8613)** supplies the model. The one-body walk is summed over records and compressed to configurations with different sites (one record per site, any coins). Either exchange sign is allowed.
- **Block 76 (#8611)** keeps T1: a chessboard of clocks is invisible to opposite-parity hopping. It **withdraws** the induced sea stiffness: `κ = 0.095, c₀ = −1.193` are now only declared inputs of a comparator, not derived sea coefficients. So nothing here builds on 0.095. The free and the interacting responses are both computed on the same torus.
- **Block 85 (#8657):** the hard-core crowd at the sea's filling is jammed.

## Setup

- **One body:** `H = σ₁S_x + σ₂S_y` on an `L_x × L_y` torus, clocked as `H_w = φHφ` with `φ = e^{u/2}` and `u = ε cos(2πx/4)`.
- **Many body:** exact sparse diagonalisation (scipy `eigsh`, floating point). E₀(ε) is fitted as `E₀ + c|ε| + χVε²` over `ε = 0, ±0.02, ±0.04, ±0.08`. The `|ε|` terms come out at the `10⁻⁶`–`10⁻³` level (free comparators up to `2.6·10⁻³`), well below the ε² terms, so there is no cusp.
- **4×4 at 8 records (3.3M states)** was not run: it needs about 4 GB per sparse Hamiltonian, and the machine was loaded. The task allows the 4×3 torus instead.

## Exact results (sympy)

- On the 4×4 torus with two records, both exchange signs and a generic rational `φ`, the chessboard `φ → φ·2^{±1}` leaves the hard-core generator unchanged entry by entry. Every hop joins opposite sublattices, as in block 76 T1 for one body.
- At one record per site (V records, the free negative branch's filling) no hop is possible, so `H = 0`. The jammed crowd has `E = 0` and no response.

## Numbers (per site; `e₀ = E₀/V`; `χ` is the ε² coefficient)

**Removing the local term.** At long wavelength, `E − E₀ → (e₀/2) Σ_x u_x² = e₀Vε²/4`, so `χ(q→0) = e₀/4`. The q-dependent part `Δχ = χ − e₀/4` is block 76's stiffness channel. Here `q = π/2` and the lattice `q² = 2`.

| torus, N | model | e₀ | χ | Δχ = χ − e₀/4 |
|---|---|---|---|---|
| 4×3, 6 (half filling) | hard-core bosonic | −0.454989 | −0.08672 | **+0.0270** |
| 4×3, 6 | hard-core fermionic | −0.467423 | −0.08878 | **+0.0281** |
| 4×3, 6 | free antisymmetric | −0.607623 | −0.46630 | −0.3144 |
| 4×3, 6 | free symmetric | −0.661432 | −1.26204 | −1.0967 |
| 4×3, all negative levels (10 of 24; the 4 zero modes empty) | free negative sea | −0.896300 | −0.19405 | **+0.0300** |
| 4×3, 12 (one per site) | hard-core (jammed) | 0 | 0 | 0 |
| 4×3, 4 | hard-core bosonic / fermionic | −0.37929 / −0.38490 | −0.10194 / −0.10547 | −0.0071 / −0.0093 |
| 4×4, 4 | hard-core (both signs) | −0.323492 | −0.12938 | −0.0485 |
| 4×4, 6 | hard-core bosonic / fermionic | −0.42111 / −0.42678 | −0.11725 / −0.09601 | −0.0120 / +0.0107 |
| 4×4, all negative levels (12 of 32; the 8 zero modes empty) | free negative sea | −0.853553 | −0.19202 | +0.0214 |

The 4×3, 4-record free antisymmetric line gives `Δχ = −0.314`, and the 4×4, 4-record one gives `−0.328`.

## Reading

**Raw response.** The raw second-order response `χ` is negative for every model: modulating the clocks lowers the ground energy.

**Stiffness part at half filling.** With the local volume term removed, at the task's half filling on 4×3:
- the hard-core crowd's stiffness part is positive (+0.027, +0.028 for bosonic and fermionic);
- the free negative sea's is positive (+0.030 on 4×3, +0.021 on 4×4);
- so they have the **same sign**: both are a clock stiffness.
- The free fermions at the same density have a large negative stiffness part (−0.31).

**It depends on filling.** At lower filling the hard-core stiffness part turns negative: 4×3 with 4 records, 4×4 with 4 records, and 4×4 with 6 bosonic records. So the crowd's stiffness crosses from the free-particle sign (dilute) to the free-sea sign (near half filling).

**At the sea's filling** the hard-core crowd is jammed and has no response.

## Verdict

The HIT condition is that the interacting κ has the opposite sign to the free one. It is **not met** at the task's half filling against the free sea on the same torus. The filling dependence above is reported as found, not as a HIT.

In the printed table of `run.py`, the free-sea rows carry the label `N = V`. That label is the jammed hard-core filling. The free sea itself fills all negative one-body levels: 10 on 4×3 and 12 on 4×4.
