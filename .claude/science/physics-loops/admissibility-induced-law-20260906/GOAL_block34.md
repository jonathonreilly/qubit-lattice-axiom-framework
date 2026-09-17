# GOAL — block 34: the torus memory time of the sphere formation law — the linearized field exactly, the nonlinear law measured against it (2026-09-17)

**Directive.** Owner 2026-09-17: "pick up the next in the queue and get going." With the six-axis threshold lane capped at the count (blocks 32–33), the sphere lane's queue item "the torus memory time" (block 26, PR #8170: "of order βL²" by the gain-one reading; finite planes forget by a minorization whose rate is useless for the scale) is the tractable exact target.

**Exact target (claim type `bounded_theorem`).**
- T1: on the periodic `L × L` level plane the linearized transverse field splits into modes with multiplier `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`; the identity `1 − |φ|² = (4/9)[sin²(k₁/2) + sin²(k₂/2) + sin²((k₁ − k₂)/2)]`; the zero mode random-walks (plane-average variance `σ²t/L²` per component, `σ² = A(3β)/(3β)`), the nonzero modes are stationary.
- T2: the mode formula against the exact rational covariance recursion on tiny tori.
- T3: the memory time `τ_L = 3βL²/A(3β)` and the decay rate `A(3β)/(3βL²)` enclosed exactly; the stationary transverse variance `V_L` bracketed by exact lattice sums; its asymptotic `2γ log L + O(1)`.
- Executed: the nonlinear law's angular diffusion of the plane-average direction against the zero-mode rate at `β = 6, 12, 24, 48`, `L = 16, 32`.

**Seat plan (supervisor-run, no subagents).** Controls: block 26's sampler restated (`supervisor_control_block34_torus_sim.py`, `..._torus_msd.py`); the exact runner; refuting pass (`..._refuter.py`: a floating-point covariance recursion on `L = 8`, an independent rotated-pole sampler, the memory times in floating point, `V_L` by direct summation against the bracket and `2γ log L`). Contract with a lens pass; primary; fold; census; gates; independent PR against `main`.

**Stop conditions.** The exact statements proved and executed; the nonlinear comparison recorded as executed, not claimed. Never merge; layman update at the milestone.
