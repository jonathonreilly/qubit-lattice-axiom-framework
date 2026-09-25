# Mixed-pair chase with a staggered rest term — run 1

Worker `w-jonathonsmac4f50-jd223`, model `claude-opus-5-5`. Blocks 55, 71 and 77 were written by the same model family (Claude). The log is `logs/probes/C:the-mixed-pair-chase-with-a-staggered-mass:a1/w-jonathonsmac4f50-jd223__53d7f9ce__20260925T075433Z.*`.

**HIT:** in all three variants the mixed pair still chases. At m = 0.3 the pulls cancel to 1e-8 to 3e-6 of the larger. At m = 0.6 they cancel only to 2.5e-4 to 3.1e-4 of the larger, which exceeds the task's 1e-4. The residual is converged in both step size and field self-consistency.

## As landed on main

- **Block 71 (#8603).**
  - T1: twins source oppositely.
  - T2, in the weak pair ansatz: pulls are antisymmetric for any signs, and a ray from rest falls by −w∇w whatever the sign of its energy.
  - Its own narrowing: the pair formula "does not supply an exact coupled dynamical conservation theorem".
- **Block 77 (#8612).**
  - The supplied family is `a0 I + 2a Σ C_j + Σ σ_j S_j` plus a supplied staggered `m ε`.
  - T3: odd-displacement terms anticommute with ε, and `φ(K + mε)φ = φKφ + m w ε`.
  - T4: the paired energies are `a0 ± sqrt((2a c + λ)² + m²)`.

## Model (block 55's ring control)

- **Walk.** `H = a0 + 2a C + σ_z S + m ε` on a ring of 1500, clocked as `H_w = φ H φ`.
- **Field.** The static weak-field law is `2u_z − u_{z+1} − u_{z−1} = −Γ(s_z − mean s)`, with `s = e^A + e^B` and `e_z = Re χ_z†(H_w χ)_z`.
  - It is solved to self-consistency at every step, and walkers are advanced by expm_multiply at the midpoint field.
- **Settings.** Γ = 0.002, dt = 1, t = 300. Bodies sit at sites 500 and 1000, coin up, width 30.
- **Initial states.** Bodies start at rest on one branch. They are built exactly per momentum pair `{k, k+π}` from the 2×2 block.
- **What is measured.** Each quantity is taken against a free (Γ = 0) control of the same packet.
  - Wave-vector change: the phase of `⟨T²⟩/2`. `T²` commutes with ε, and its drift in the free control is ≤ 3e−16.
  - Displacement: the circular mean position.
- **Ledger.** `Σ⟨H_w⟩ + (1/2Γ) Σ u(2u − u₊ − u₋)`. It is stationary in u at the slaved field, so its drift only measures the integrator. The drift is ≤ 2e−10.

## Exact (sympy)

- On a ring of 8, ε anticommutes with S and C and commutes with `T²`.
- The pair block `[[b, m], [m, −b]]` has energies `±sqrt(b² + m²)`.
- `sin k + 2a cos k = sqrt(1 + 4a²) sin(k + arctan 2a)`.
- So **on one axis the scalar hop only moves the coin-up rest momentum to k\* = −arctan(2a)** (and rescales the speed). The rest energies stay ±m.
- Block 77's four levels are a three-axis corner effect. On the ring, the hop does not put the two walkers at different levels.
- I therefore ran both readings:
  - the literal hop a = 0.1;
  - the offset a0 = 0.1, which does give the walkers different levels (a0 ± m).

## Results at t = 300 (floating point)

| variant | m | energies A, B | Δk_A, Δk_B | sum / larger | displacements A, B | chase |
|---|---|---|---|---|---|---|
| no scalar term | 0.3 | +0.275, −0.330 | −9.099e−3, +9.099e−3 | 1.0e−8 | −4.15, −4.89 | yes |
| no scalar term | 0.6 | +0.506, −0.734 | −3.7207e−2, +3.7218e−2 | **3.1e−4** | −7.81, −10.76 | yes |
| hop a = 0.1 | 0.3 | +0.275, −0.330 | −9.101e−3, +9.100e−3 | 3.0e−7 | −4.32, −5.08 | yes |
| hop a = 0.1 | 0.6 | +0.506, −0.734 | −3.7210e−2, +3.7221e−2 | **3.0e−4** | −8.12, −11.17 | yes |
| offset a0 = 0.1 | 0.3 | +0.364, −0.217 | −7.872e−3, +7.872e−3 | 2.8e−6 | −3.55, −4.18 | yes |
| offset a0 = 0.1 | 0.6 | +0.587, −0.598 | −3.5145e−2, +3.5154e−2 | **2.5e−4** | −7.29, −10.14 | yes |

- **Energies.** They include each body's own field. The positive body sits in its own well and the negative one on its own hill, so |E_B| > |E_A| without the offset.
- **The chase.** Both accelerations point the same way in every variant and mass: B (negative) moves toward A (positive), and A moves away from B.
  - B accelerates harder than A. The separation shrinks by 0.7 sites (m = 0.3) to 3 sites (m = 0.6) by t = 300.
  - The initial rates match block 71's weak-ansatz formula `dk/dt = −E ⟨∂u_other⟩` to 2–10 %.
- **Same-sign controls.** Pairs of two positive or two negative bodies cancel to ≤ 5e−14. This is enforced by the mirror symmetry of the set-up (sites 500 and 1000), so it says nothing about momentum conservation.
  - Two positives attract and two negatives repel.
- **The a-term.** The hop leaves the wave-vector changes within 0.05 % and the m = 0.6 residual unchanged. Displacements are about 4 % larger, which fits the speed rescale sqrt(1 + 4a²).
  The offset changes the levels, and with them the magnitudes of the pulls; at m = 0.3 the pulls still match to 2.8e−6.

## The residual is not numerical

- **Step size.** dt = 0.5 gives sum 1.121e−5, against 1.116e−5 at dt = 1 (hop, m = 0.6).
- **Field self-consistency.** 20 iterations per solve give 1.1365e−5, identical to 5 iterations (no scalar term, m = 0.6).
- **Coupling.** At Γ = 0.001 the sum is 5.5e−7, or 3.0e−5 of the larger. The absolute residual falls by ~20× when Γ halves, while the pulls fall by 2×.
- **Time.** At m = 0.6 the residual grows as roughly t³: 4e−7, 3.9e−6 and 1.1e−5 at t = 100, 200 and 300. The pulls grow as t.

So the total wave vector of the coupled mixed pair is not kept exactly. The loss is higher order in the coupling and grows with the acquired motion. Block 71's own narrowing already allows this: the pair formula makes no claim about the coupled dynamics.

I did not establish the mechanism. One candidate is a mismatch between the site energy density that sources the field and the bond-level force density the walker feels. The kinetic part of that mismatch would grow as the bodies speed up, and same-sign pairs would cancel it by symmetry. This is not checked.

## Answer

- **Do the accelerations still point the same way?** Yes, in every variant and mass: the mixed pair still chases.
- **Are the pulls still matched?**
  - At m = 0.3: yes, to 1e−8 to 3e−6.
  - At m = 0.6: no, not to 1e−4. They match to 2.5e−4 to 3.1e−4 of the larger after t = 300 at Γ = 0.002, and the residual is growing.
- **Does the a-term matter?**
  - The literal hop a = 0.1 changes nothing material on one axis.
  - The offset a0 = 0.1, which does put the walkers at different levels, keeps the chase and the same order of residual.
