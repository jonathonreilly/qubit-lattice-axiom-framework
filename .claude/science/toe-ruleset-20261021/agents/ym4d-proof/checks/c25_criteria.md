# c25 criteria (written 2026-10-27 BEFORE checks/c25_polymer_size.py; RTARGET §18)

For a connected finite union τ of segments in R^d with total length ℓ, N(τ) := #{k ∈ Z^d : dist_∞(k, τ) ≤ ½} (the closed
unit cubes centred at lattice points that τ meets). Bound to test: N ≤ 2^d + 2^{d-1}√d·ℓ (implies Dimock's
3^d(1 + ℓ)).
Instances, d = 2, 3, 4: 2000 random trees per d (up to 6 segments, random lengths in [0, 3], random directions,
attachment at random points of earlier segments) and adversarial cases (a point at a lattice-cube corner; axis segments
with integer and half-integer endpoints; diagonal segments; stars of near-axis arms; staircases).
Counting: exact segment-vs-closed-box intersection (slab method) over all candidate k.
- **Q1.** No instance violates N ≤ 2^d + 2^{d-1}√d·ℓ (tolerance 1e-9 on ℓ).
- **I1 (informational).** The largest ratio N/(2^d + 2^{d-1}√d·ℓ), and the largest N/(3^d(1 + ℓ)).
