# Delay of the rate field with the curvature member — attempt 1

Worker `w-jonathonsmac4f50-j03c0`, model `claude-opus-5-5`. Task `J:derive:delay-of-the-rate-field-with-the-curvature-member:a1`.

**Provenance.** Blocks 54 to 67 were written by the same model family (Claude Opus), and so was block 57, which asks the question for the simplest bond energy. They are open and unrefereed; I restate what I use. The referee should come from another family. There were no prior attempts at claim time.

**Scope.** This works within the supplied clauses of blocks 60 and 62 (#8590, #8592), at second order around the uniform state. Nothing is adopted. The parked decisions are untouched. No gravitational claim is made. The comparator (lapse as a constraint, the DeWitt supermetric) is named only for comparison.

## 1. The exact statement attempted

**Setting.**
- Block 62's second-order member: `F₂ = −K w̄ (u R₁ + R₂)`, with `R₁ = −(p_i p_j h_ij − p² h)` and `R₂` as in block 62 T3.
- Block 62's kinetic term: `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]`, with no rate of change of a rate.
- Block 55 T1's coupling: `∂⟨H⟩/∂u = e`.
- A body at rest has no hop energy, so its frame response is `Θ = 0` (block 59).
- Work wave vector by wave vector, with `p_j = 2 sin(k_j/2)` and `p² = E(k) ≠ 0`, on the torus or on `Z³`.

**Claims.**

(a) **The clock's change is not retarded.**
- The rate `u` is a multiplier.
- Its equation is a constraint that fixes the scalar part `φ` of the lengths at each label time: `2K w̄ p² φ = e`.
- `u` then follows at the same label time: `u(k,t) = −e(k,t)/(4K w̄ p²) + α(α+3β) ë(k,t)/(K² w̄³ (α+β) p⁴)`.
- Only the two transverse traceless strains travel (`speed² = K w̄²/(4α)`), and a body at rest does not source them.

(b) **What changes at once.** When a body's energy changes at label time 0 (a formation event, block 67), three things change at every distance at once:
- the clocks (the Poisson field of `Δe`, plus an `ë` term while the energy changes);
- the scalar lengths (the Poisson field of `Δe`);
- a slow packet's fall `−E∇u` (block 54).

A ray's bending changes at once too, because it sees `u` and `φ`. Only the transverse traceless strains, which a moving body sources, arrive after `r/c_T`.

(c) **The comparator's ratio `α + β = 0`.** Here the relabelling equation forces `φ̇`, and hence `ė`, to be constant. A jump of a body's energy at rest then has no solution at all. The action at a distance is excluded by forbidding the event, not by retarding its effect.

**The task's HIT condition holds:** a packet's fall changes before any strain wave can arrive, and the change is set by the body's change of energy.

## 2. Steps

### Step 1 — the member is relabelling-blind and sees one scalar (PROVED; CHECKED 1.1–1.3)
- `R₁` and `R₂` are unchanged by `h → h + p ξ + ξ p`, for every `p`, `h` and `ξ` (1.1).
- On the scalar `h = (1 − p̂p̂) φ`: `R₁ = 2p²φ` and `R₂ = (1/2)p²φ²`, in every direction (1.2).
- On isotropic stretch `h = 2λδ`, the constraint reproduces block 60's `Lap λ = −e/(4K w̄)` (1.3).
- `R₁`, `R₂` and the kinetic term are `O(3)`-covariant in `p_j`, so each wave vector can be rotated to `p = p ẑ`.
- With `p ∥ ẑ`, write
  `h = [[φ + a, b, c_x], [b, φ − a, c_y], [c_x, c_y, 2ξ_L]]`:
  - `a`, `b`: transverse traceless;
  - `φ`: scalar;
  - `ξ_L`, `c_x`, `c_y`: relabellings.

### Step 2 — the equations (PROVED; CHECKED 1.4–1.11)
Take `L = T − F₂ − e u`.
- **The `u`-equation** is `K w̄ R₁ = e`, that is `2K w̄ p² φ = e(t)`. It has no time derivative: it is a constraint (1.4).
- **The TT equations** are `(4α/w̄) ä = −K w̄ p² a`, and the same for `b`. Their `speed² = K w̄²/(4α)` in every direction, which is block 62 T4. A body at rest does not source them (1.5).
- **The relabelling `ξ_L`** has no potential and no source. It is coupled to `φ` through `β` in the trace of the kinetic term: `d/dt[(α+β) ξ̇_L + β φ̇] = 0`, so from rest `ξ̇_L = −β φ̇/(α+β)` (1.6).
- **The `φ`-equation.** After eliminating `ξ_L`: `(4α(α+3β)/(w̄(α+β))) φ̈ = K w̄ p² (2u + φ)`.
- **The result.** With the constraint's `φ`:
  `u = −e/(4K w̄ p²) + α(α+3β) ë/(K² w̄³ (α+β) p⁴)` (1.7).
- **Static limit.** This is block 60's `Lap u = e/(4K w̄)` (1.8).
- **Special ratios.**
  - At `α + 3β = 0` the `ë` term vanishes (1.10).
  - At `α + β = 0` the `ξ_L` equation reads `β φ̇ = const`, hence `ė = const`, and a jump has no solution (1.9).
- **The only travelling modes** are the two TT modes, at `X = ω² = K w̄² p²/(4α)` (1.11). The three relabellings are static, which is block 62 T4's mode count.

### Step 3 — a formation event (PROVED; CHECKED 2.1, 2.2)
- Let `e(k,t) = e₀ + Δe · s(t/τ_r)`, with `s` a smooth step completed at `τ_r`.
- **At label time `0⁺`**, `u` already moves at every wave vector: `δu = 6α(α+3β)Δe/(K² w̄³ (α+β) p⁴ τ_r²) + O(t)` (2.1).
- **After the switch-on**, the jump of `u` is the Poisson field `−Δe/(4K w̄ p²)`, whatever `α` and `β` (2.2).
- **In real space:**
  - the first term is `(1/(4K w̄))` times the lattice Green's function applied to `Δe`: `∝ Δe/r` far away;
  - the `ë` term uses the square of the Green's function, whose kernel grows linearly with `r` in three dimensions. Its gradient does not decay, so during the switch-on every packet is pushed by an amount independent of its distance (continuum reading; on a torus it depends on the box).
- By block 54 the fall of a slow packet is `−E∇u`. So a packet at rest at any distance `r` starts to fall differently at label time `0⁺`: long before `r/c_T`, and in proportion to `Δe`.
- **Why nothing can hide it.** The only freedom of the label time is global (`t → f(t)`, block 57), which shifts `u` uniformly and leaves `∇u` unchanged. So this is not a gauge part of the constraint: the packet's fall reads it.

### Step 4 — (b): what changes at once and what after `r/c`

| quantity | response to a body at rest changing its energy |
|---|---|
| the clocks `u` | at once (Step 3) |
| the scalar lengths `φ` | at once (the constraint) |
| a slow packet's fall `−E∇u` | at once |
| a ray's bending | at once (it reads `u` and `φ`; block 59 T4) |
| the transverse traceless strains | only if sourced by moving bodies' stress; they arrive after `r/c_T` |
| the relabellings | move at once but are unobservable |

**The comparator.** The lapse is also a constraint, but conservation of the source prevents a sudden change of a body's energy. Here the kinetic ratio that forbids it is exactly `α + β = 0`, the DeWitt ratio.

### Step 5 — executed control (floating point; evidence, not claims; E1)
- **Setup.**
  - A `48 × 48` slice (wave vectors in the plane), with `K = w̄ = α = 1`, `β = 1/2`, so `c_T = 1/2`.
  - A Gaussian body of width 1.5, switched on smoothly over `τ_r = 2`.
  - `u` from the Step 2 law.
  - A positive-energy packet at rest (wave number `π/2` along `y`, where the group speed vanishes; energy 0.973) at distances 8 and 16 along `x`.
- **Result.**
  - The force `d⟨S_x⟩/dt = ⟨i[H_w, S_x]⟩` is 0 before the switch-on.
  - At label time 0.05 it is `+3.2 × 10⁻²` (r = 8) and `+1.9 × 10⁻²` (r = 16): the `ë` term pushes away from the body.
  - After the switch-on it is `−8.46 × 10⁻⁵` and `−2.88 × 10⁻⁵`, toward the body, against block 54's `−E⟨∇u⟩ = −8.76 × 10⁻⁵` and `−2.97 × 10⁻⁵`.
  - All of this happens long before the TT arrival times 16 and 32. The response is linear in `Δe`.
- A version with a coin-up packet gives zero force: its mean energy is zero. This matches block 54's force `∝` energy.

## 3. Where the route stops

Nothing fails within the stated order. Not done:
- beyond second order;
- bodies that move (TT sourcing, and whether moving sources can change energy consistently);
- the strong field;
- whether the framework would restrict `α` and `β`, or forbid formation events at rest.

The result turns a question the task left open into a fork: with block 62's kinetic term, either `α + β ≠ 0` and formation events act at a distance, or `α + β = 0` and a body's energy at rest cannot change.

## 4. What would finish it

1. Decide between the two branches: an owner's choice of `α/β`, or a clause for formation events that conserves energy locally.
2. Redo Steps 2 and 3 with a stress source for a moving body. Establish whether `α + β = 0` then admits exactly the conserved changes, the comparator's continuity equation.
3. Carry the result to the strong field of block 60 T4.
