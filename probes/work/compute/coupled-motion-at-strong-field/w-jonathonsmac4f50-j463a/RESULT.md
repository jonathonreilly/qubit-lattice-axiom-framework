# Coupled motion of two heavy walkers under the simplest clock law at strong field — run 1

Worker `w-jonathonsmac4f50-j463a`, model `claude-opus-5-5`. Blocks 55 and 56 were written by the same model family (Claude). `run.py` takes about 8 seconds.

## Setup

- **The walk.** Block 55's reduced walk `H(m) = mσ_x + σ_z D` on a line of `n` sites, with the hop `H_{z,z+1} = −(i/2)σ_z`.
- **Walls.** Held at `φ = 1` just outside both ends. This is not a ring, so no multiplier appears.
- **Clocked generator.** `H_w = φHφ`.
- **Ledger.** `⟨H_w⟩_A + ⟨H_w⟩_B + (6/Γ) Σ_{all bonds, walls included} (φ_z − φ_{z+1})²`. This is the line's normalisation of block 56's `(2/γ) Σ`.
- **Static law.** Stationarity in `φ` gives the task's linear law `((12/Γ)(1 − A) + K)φ = 0`, where `A` is the two-neighbour average and `K_xy = Re Σ_walkers ψ_x† H_xy ψ_y` (rate-free).
- **Time step.** Each step solves the tridiagonal system for `φ` and evolves both walkers with `H_w`. The midpoint step is as in block 55's two-walker control: a trial step, a re-solve, then the step at the mean `φ`.

## Exact (rationals, line of 11)

For bodies at rest (`K = diag(m)`):
- `0 < φ ≤ 1`;
- ledger `= Σ mφ = (6/Γ)(2 − φ₁ − φ_n)`, a term at the walls;
- one body: `φ₀ = 1/(1 + x)` with `x = (Γ/6) G_L(z₀,z₀) m`, where `G_L = L⁻¹` is the Dirichlet Green function `G_L(z,y) = min(z,y)(n+1−max(z,y))/(n+1)`;
- two bodies: `φ = 1 − (Γ/6) Σ_i (m_iφ_i) G_L(·, z_i)` exactly. The field is linear in the charges `q_i = m_iφ_i`.

## Numerical (floating point)

Line `n = 240`. Walker A (`m = 2`) at 90 and walker B (`m = 3`) at 150, width 6, both at rest. Here `x_A = (Γ/6) G_L(z_A,z_A) m_A`.

| x_A | Γ | ledger | drift over t = 20 | φ_A | φ_B | dk_A/dt | charge (point) | bare | smeared bilinear ratio A | ratio B |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 5.30e-3 | 4.1805 | −1.9e-12 | 0.843 | 0.829 | +3.391e-3 | +3.381e-3 | +4.82e-3 | 1.0000 | 1.0001 |
| 0.5 | 2.65e-2 | 2.5271 | −3.3e-12 | 0.524 | 0.487 | +6.318e-3 | +6.225e-3 | +2.41e-2 | 1.0001 | 1.0002 |
| 1 | 5.30e-2 | 1.6928 | −4.0e-13 | 0.359 | 0.316 | +5.766e-3 | +5.599e-3 | +4.82e-2 | 1.0002 | 1.0004 |
| 2 | 0.106 | 1.0210 | −1.5e-14 | 0.221 | 0.182 | +4.283e-3 | +4.039e-3 | +9.64e-2 | 1.0003 | 1.0006 |
| 5 | 0.265 | 0.4676 | −5.6e-17 | 0.103 | 0.076 | +2.304e-3 | +1.994e-3 | +0.241 | 1.0008 | 1.0012 |

**(i) Ledger.** The drift is at most `1.3×10⁻¹²` of the ledger, which is the integrator's level. In the long runs (t = 160) it is `3×10⁻¹⁰` and `1×10⁻¹²`.

**(ii) Pull.**
- *Measured.* The pull is the initial slope of `k = −arg⟨ψ|T|ψ⟩`.
- *Exact bilinear form.* For packets at rest, `K` has no bond entries, and the solved `φ` equals `1 − (Γ/6) G_L(q_A + q_B)` to `7×10⁻¹⁴`, with `q(z) = K_zz φ_z`. Block 54's law then gives each walker's pull as `(Γ/3) Σ_z q_self(z) ∂[G_L(q_A + q_B)](z)`, which is bilinear in the charge densities `mφ`.
- *Agreement.* Measured over this form is `1.000–1.001` at every `x`.
- *Point charges.* Placing the charges at the centroids is off by up to 16–18% at `x = 5`, because the field varies across the packet.
- *Bare energies.* Replacing the charges by the bare energies `m` gives ratios `0.70, 0.26, 0.12, 0.044, 0.010`. At strong field the pull is set by `mφ`, not by `m`.
- *Walls.* The walls take up momentum, so the pulls on A and B are not equal and opposite on this finite walled line.

**(iii) Positivity for moving packets at large energy.**
- **The mechanism.** `M = (12/Γ)(1 − A) + K` stays an M-matrix while every bond entry satisfies `K_{z,z+1} ≤ 6/Γ`.
  - A fast packet's bond entries are its hop energies, which are positive.
  - The scan below uses one packet with `m = 0.05`, `k₀ = 1.2`, bare energy `0.933`.
- **The result.** For each width, `φ` first goes negative at the `Γ` where the M-matrix property is lost, to scan accuracy. That is well before `M` stops being positive definite.

  | width | max bond entry | M-matrix lost at Γ | min φ < 0 from Γ ≈ | λ_min(M) < 0 from Γ ≈ |
  |---|---|---|---|---|
  | 1 | 0.1592 | 37.7 | 37.7 | 85.1 |
  | 2 | 0.1158 | 51.8 | 52.4 | 124.5 |
  | 4 | 0.0636 | 94.3 | 94.4 | 212.8 |

- **What the run does.** Two packets at `k = ±1.2`, width 1:
  - at `Γ = 13.2`, `φ` stays positive (min `+0.0063`);
  - at `Γ = 60`, min `φ = −0.0055`. The linear problem stays solvable (`λ_min(M) > 0`), the ledger stays conserved and the run continues. The field develops a node, so `w = φ²` vanishes between sites: a clock stops.
  - For bodies at rest this cannot happen (block 56). For moving packets it happens once a hop energy exceeds `6/Γ`.

**(iv) Clock rates as the walkers approach.** `w = ⟨φ²⟩` at each walker, against the static two-body law at the current centroids:
- At `x = 1`: the separation goes 60 → 56.3 over t = 160, and the rates at A go 0.1321 → 0.1186. The static law gives 0.1284 → 0.1234. The clocks slow as the walkers approach, at the few-per-cent level of the packet-size corrections.
- At `x = 5`: the walkers barely move. The separation goes 60 → 59.7, because the pull scales with the small charges `mφ ≈ 0.2`. The rates are 0.0124 → 0.0118, against a static 0.0113.

## Summary

Nothing contradicts the task's expectations, so there is no HIT.
- The ledger is conserved at the integrator's level.
- The pull is bilinear in the charges `mφ`, exactly in the smeared form (to 0.1%), and not in the bare energies.
- New: for moving packets, `φ` stays positive until a bond hop energy exceeds `6/Γ`. Beyond that the field has nodes and clocks stop, while the ledger is still kept.
