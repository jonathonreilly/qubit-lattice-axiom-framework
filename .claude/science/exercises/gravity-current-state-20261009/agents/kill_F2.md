# Kill agent: F2, smooth proper-distance kernels on fixed Z³

**Agent:** Claude Opus 5.5, extra-high (xhigh).
**Refresher read (stated):** the full axioms memo, the primitive registry check, the kinetic-isotropy primitive note, WALL, ROUTES, R2 and both of R2's scripts, the pack TEST_LOG (K7a, K3a″, W1), and TESTS (including the T1 results).
**Scripts:** `scripts/KF2_K1 … K4b` with their outputs.

## Verdict: DEAD

This is a no-go claim, so the other-vendor referee is required (`agents/kill_F2_referee.md` once it returns).

**Plain summary.** F2 kills the grid's stiffness by making every coupling a smooth Gaussian in proper distance. Smoothness is the whole mechanism. Gauge fields, nearest-neighbour locality, and positivity plus the space–time lattice symmetry each remove it or make it costly.

## (1) Gauge transporters (CHECKED, 2D scalar QED at O(e²))

**Setup.** Photons live on nearest-neighbour links, with the kinetic metric from transporter flows. The free spectrum is exactly ω² = K(q).

| Transporters | O(e²) stiffness vs σ |
|---|---|
| all smooth (no lattice paths), the control | 1.7e-4, 1.5e-6, 2.9e-8 at σ = 1, 1.25, 1.5; falls like the free part |
| **uniform staircase (lattice paths)** | −3.4e-4 … −3.6e-5 at σ = 1 … 2: about **σ^−2.6** (E-like), σ^−1.8 (T-like) |
| L-shaped paths | also a power law (−4.9e-4 → −8.5e-5) |

- **Robustness.** L = 32 and 48 agree to about 1%. The result is stable as μ → 0.
- **Mechanism (ARGUED).** The exact lattice Ward identity forces each transporter to be a lattice flow. Such a flow cannot be smooth in displacement without power-law tails (COMPARATOR: SLAC derivative / Karsten–Smit).
- **Size (ARGUED).** About 3e-6·e² per cell at σ ≈ 5, roughly 1e96 above the bar.
- **Untested escape.** Gauge links on every pair out to about 22σ, which drops nearest-neighbour adjacency.

## (2) Fermions (CHECKED, K1)

- **Smooth massless Dirac:** the stiffness goes as e^(−π²σ²/2), half the exponent. It vanishes at all 8 zone corners (Nielsen–Ninomiya), and **54–94% of the zone becomes a near-zero flat band**. This is the band that T1(a1) finds splitting the light cone.
- **With a smooth Wilson term** the full e^(−π²σ²) returns, but chiral symmetry is broken, so each light fermion needs a mass tuning.

## (3) The trilemma at kernel level (Lemma N: EXACT plus CHECKED)

- **The setup.** Take a free field with a positive transfer matrix. Write the time kernel as D(z = cos q₀), with σ² := −4c₄/c₂.
  - −D is Nevanlinna: D = a − bz − ∫dν(t)/(t − z), with b, ν ≥ 0 and t > 1.
  - Jensen's inequality then gives **(zone-face curvature)/(origin curvature) ≥ 1/(σ² + 2/3)²**.
  - Equality holds only for a single pole, which is R2's rational kernel.
- **Checks.**
  - The minimum over 200,000 random measures is 0.9999996.
  - A Gaussian breaks the floor (2e-7 vs 4.6e-2 at σ = 2), which explains C4.
  - Kernels of this form pass the Hankel positivity test.
- **Transfer to space (EXACT).** Any signed-permutation group that leaves only one invariant quadratic form maps the time axis onto a spatial axis. The floor then holds along every spatial axis.
- **Not proved.**
  - "Face floor ⇒ stiffness floor" is ARGUED. It is CHECKED only for the extremal (rational) family, about σ^−3.5.
  - A tuned mixture can zero the two TT numbers, which is tuning.
- **The other corners.**
  - A smooth kernel in Euclidean time violates positivity (C4).
  - A smooth spatial kernel with continuous time breaks the kinetic-isotropy primitive. T1(a2) gives Δ = −0.69 independent of σ (Collins).

## (4) Locality (CHECKED, K2)

- Truncating the Gaussian at radius R leaves 10–70 × e^(−R²/2σ²). Reaching 1e-102 needs R ≈ 22σ ≈ **107 sites**, about 5e6 couplings per site.
- Kernels generated from finite-range rules give only σ^−6 to σ^−8.
- **So "S7 only; no axiom" (ROUTES) is wrong:** F2 conflicts with nearest-neighbour adjacency and with the kinetic-isotropy primitive.

## (5) Prior art

F2 first appears as R2 Route 3. The K3a″ referee found that every transporter path gives a nonzero response. The 09-29 exercise assumed finite range and analytic symbols.

## (6) Terminal obligation: target-equivalent or stronger

- With the kinetic-isotropy primitive and positivity, Lemma N makes the obligation unsatisfiable for free fields.
- Dropping the primitive means protecting one light cone without a lattice symmetry, which is the naturalness clause restated (blocked-equivalent).
- Gauge fields add the need for links beyond nearest neighbours.
