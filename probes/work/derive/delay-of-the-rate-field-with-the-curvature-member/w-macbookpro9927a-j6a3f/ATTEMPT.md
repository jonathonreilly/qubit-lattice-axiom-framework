# Delay of the rate field with the curvature member: the clock law has no retarded part, and a formation event that keeps the ledger still moves every distant packet at once and leaves a 1/r memory

Attempt 2 of 2. Worker `w-macbookpro9927a-j6a3f` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory; they run in a few seconds.
- The exact parts are the full `7 × 7` pencil solved over `Q(s)`, rotation invariance and the continuum kernel identities.
- One control on a periodic box is floating point and is labelled as such.

## Sources, provenance and route

**Sources.** Definitions come from the PR heads.

| Block | PR, head | What is used |
|---|---|---|
| 62 | #8592, `aada579459` | `R₁`, `R₂`, `F₂ = −K w̄ (uR₁ + R₂)`; the kinetic term `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]` |
| 60 | #8590 | the ledger per tick and the curvature member |
| 67 | #8598, `3bea45f6d8` | with the ledger kept, the monopole is unchanged and the dipole jumps by `Q′(y − X̄)`; by block 60 T5 the rates follow the content at the same label time |
| 54 | #8570 | the fall law `dk/dt = −E ∇u`, which the task restates |

Check family Q confirms 6 quoted lines verbatim.

**Attempt 1.** Worker `w-jonathonsmac4f50-j03c0`, another machine, not refereed.
- It derived `u(k,t) = −e/(4K w̄ p²) + α(α+3β) ë/(K² w̄³ (α+β) p⁴)` by splitting the modes.
- It treated a body whose total energy changes. Its ë term then pushes packets by an amount independent of distance.
- It found that `α + β = 0` forbids such events.

**My route.** I formed my plan before reading attempt 1 and do not rely on it.
- I re-derive the clock law without any mode split: the full pencil `s²M + V` in all seven variables, solved exactly.
- I then treat the formation events the framework actually uses, those that keep the ledger (blocks 58 and 67). For these the monopole is fixed and the dipole jumps.
- For those events I give the far fields, and a displacement memory of distant packets that attempt 1 does not state.

**Overlap disclosed.**
- My unit #8880 gave the rate field a kinetic term of its own, a different mechanism.
- My unit #8734 studied block 62's kinetic numbers under the blindness demands.

Neither result is used here.

## (1) Statement

**Setting.** Block 62's second-order member with its rotation-invariant kinetic term and no rate of change of a rate. The Lagrangian is `T − F₂ − e u`. The content is at rest: a source `e` only, no stress.

- **T1 (no retarded part).** For every wave vector `p ≠ 0` and all `α, β, K, w̄` (with `α ≠ 0` and `α + β ≠ 0`), the clock's response to the content is

  `u(k, s)/e(k, s) = −1/(4K w̄ p²) + C s²/p⁴`, with `C = α(α + 3β)/(K² w̄³ (α + β))`.

  This is a polynomial in `s`, with no pole. So `u(t) = −e(t)/(4K w̄ p²) + C ë(t)/p⁴` at the same label time: the clock is not retarded.

- **T2 (a formation event that keeps the ledger).** Take block 67's event: the monopole of the content is unchanged and the dipole jumps by `D = Q′(y − X̄)`. At a distance `r` large compared with the body:
  - **At once.** The clock's Poisson part changes by `Δu ≈ −(D·r̂)/(16π K w̄ r²)`. A slow packet's force therefore changes by a dipole force of order `r⁻³`.
  - **While the content is being rearranged.** The `C` term contributes `u_B ≈ C (D̈·r̂)/(8π)`, which does not decay. It exerts the force `−E C (D̈ − (D̈·r̂) r̂)/(8π r)`, which decays only as `1/r`.
  - **Afterwards.** Every slow packet of energy `E` and effective mass `m*` is left permanently displaced by

    `Δx = −(E C/m*)(ΔD − (ΔD·r̂) r̂)/(8π r)`.

    This is a memory transverse to `r̂` that falls off only as `1/r`.

- **T3 (the task's HIT condition).** All of this happens before any transverse traceless wave arrives; a body at rest does not source those waves. It depends on the body's energy through `D ∝ Q′`, so it is not the unobservable, instantaneous part of a constraint alone. **The task's HIT condition holds even for ledger-kept events.**

## (2) Steps

**S0 — ASSUMED.**
- Block 62's member, its kinetic term and the coupling `−eu`, as supplied. Nothing is adopted.
- The linear order around the uniform state.
- Block 54's fall law for a slow packet near a band minimum: `dk/dt = −E ∇u` and `dx/dt = k/m*`. The task restates it.
- The large-`r` limits of the lattice kernels `1/p²` and `1/p⁴` are their continuum kernels. This is classical for `1/p²`; for `1/p⁴` there is the floating-point control F.
- At first order, keeping the ledger keeps the zero-wave-vector part of `e`.

**S1 — T1 — PROVED, CHECKED (A, O).**
- Write `x = (h₁₁, h₂₂, h₃₃, h₁₂, h₁₃, h₂₃, u)`, `T = ½ ẋᵀMẋ` and `F₂ = ½ xᵀVx`.
  - `M` has no `u` row, so there is no `u̇`.
  - The Euler–Lagrange equations are `Mẍ + Vx + e·ê_u = 0`.
  - With zero initial data, `(s²M + V)x = −e ê_u`.
- CHECKED (A):
  - the `u` component of the solution, computed over `Q(s)` with every parameter symbolic at `p = P ẑ`, equals the stated `H(s)`;
  - the same at 12 exact rational points, over four wave vectors including three off the axes and three parameter sets.
- CHECKED (O): `R₁`, `R₂` and both kinetic invariants are unchanged under `p → Qp`, `h → QhQᵀ` for a rational rotation `Q`. So `H` depends on `p` only through `p²`, and the axis computation covers every `p`.
- The denominator of `H` contains no `s`. So `u(t)` is a combination of `e(t)` and `ë(t)` at the same `t`, and has no retarded or advanced part.

**S2 — T2, the far fields — PROVED, CHECKED (K).**
- In position space, `u = −(1/(4K w̄)) G * e + C B * ë`, with `G = 1/(4πr)` (the kernel of `1/p²`) and `B = −r/(8π)` (the kernel of `1/p⁴`, since `ΔB = −G`).
- For a change `Δe` with zero total and dipole `D`, `(kernel * Δe)(x) = −D·∇kernel(x) + O(r⁻²·∇kernel)`.
- This gives `G * Δe ≈ (D·r̂)/(4πr²)` and `B * Δe ≈ (D·r̂)/(8π)`.
- `∇∇B = −(I − r̂r̂)/(8πr)`, so `∇(B * Δe) ≈ (D − (D·r̂)r̂)/(8πr)`.
- All identities are symbolic in `D`.

**S3 — T2, the memory — PROVED from S1 and S0.**
- The `C` part of `u` changes the packet's wave vector by `Δk_B(t) = −E C ∇(B * ė(t))`.
- This vanishes before and after the event.
- Its time integral divided by `m*` is the displacement `Δx_B = −(E C/m*) ∇(B * Δe)`, where `Δe = e(after) − e(before)`.
- S2 gives the stated `1/r` form.
- The Poisson part adds the changed static fall, which continues after the event.

**S4 — F: the lattice kernel on a box — floating point.**
- On a periodic `96³` box with `p² = Σ 4 sin²(k_j/2)` and the source `±½` at `(±1, 0, 0)` (dipole 1), the transverse gradient of `B * src` times `8πd` is:

  | d | value |
  |---|---|
  | 8 | 0.840 |
  | 12 | 0.768 |
  | 16 | 0.698 |

- The long-range kernel's images shift these linearly in `d/L`.
- The line through the three points meets `d/L = 0` at `0.981`, against the continuum value 1.

**S5 — T3 — PROVED from S1 and S2.**
- A body at rest has no stress. So by block 62 T4(b) the transverse traceless strains are not sourced: they have `u = 0` and do not enter `H`.
- Everything in T2 is carried by `u`, at the same label time.
- It is linear in `D = Q′(y − X̄)`, which is proportional to the energy carried.

## (3) Where the route stops

- **First order only.** Block 67's clock monopole jumps at second order, by `−(m′ − m)/(4K)`. With it, the `C` term acquires attempt 1's push that is independent of distance, at second order. That is not computed here.
- **A packet as a point with effective mass.** The fall law is block 54's, as restated by the task. Block 106's caveat on local momenta is not addressed.
- **Moving bodies** (stress sources and transverse traceless waves) are not treated.
- **The branch `α + β = 0`** (attempt 1's (c)) is not redone. `C` diverges there, consistent with events being forbidden.

## (4) What would finish it

1. **Second order.** Include block 67's monopole jump to get the full far field of a ledger-kept event, including its distance-independent part.
2. **Whether the memory is observable in the framework.** The records' positions near a formation event, with block 95's clocked record motion as the test body instead of an amplitude packet.
3. **A clause for formation events that suppresses the `C` term.** For example `α + 3β = 0`, where the clock law has no `ë` part; attempt 1 notes this ratio. Or local conservation, as in the comparator.
