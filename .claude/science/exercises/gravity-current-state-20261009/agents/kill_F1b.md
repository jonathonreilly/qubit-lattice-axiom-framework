# Kill agent: F1b, the flowing (liquid) vacuum

**Agent:** Claude Opus 5.5, extra-high (xhigh).
**Refresher read (stated):** the full axioms, the primitive registry check (kinetic isotropy at :63-71), the packet files, and TEST_LOG sections K7a, K3a, K3a″ and W1.
**Scripts:** `scripts/KF1b_K1_medium_mass_matrix.py` and `scripts/KF1b_K2_collins_speed_split.py`, with their outputs.

## Verdict: DEAD as an untuned escape

R3's lemma survives only as a statement of the price: a liquid has zero shear stiffness (EXACT).

**Other-vendor referee: codex gpt-5.6-sol xhigh, CONFIRMED WITH CORRECTIONS** (`agents/kill_F1b_referee.md`).

- **What stands:** a three-label liquid governed by √−g F(b) exactly removes the TT mass for a supplied metric. With only a CC counterterm, an exactly Minkowski background forces ρ + p = 0, which removes the phonon kinetic term, so the leading fluid EFT is degenerate. Its preferred frame transmits dimension-4 Lorentz violation to interacting matter. Its displacement supplies no helicity-2 mediator, and exact mobile positions exceed a finite local qubit. **"Merely replacing the cubic grid by a conventional continuous-time liquid is dead as a complete untuned escape."**
- **Corrections:**
  - The ρ + p ~ M_P⁴ estimate is naturalness only.
  - The strong-coupling statement is conditional ("the two-derivative F(b) realization is degenerate unless other operators or degrees of freedom supply the leading dynamics"; not a theorem against every quantum liquid).
  - In K2 the fermion's +1/3 is an order-of-limits artifact, and the sign label is flipped. The Ξ identity and the minimum 3.872e-4 are confirmed.
  - **"Supersymmetry is the only exception" is false.** Belenchia–Gambassi–Liberati list other mechanisms: Lorentz-covariant UV structure, scale separation, gravitational confinement, special cancellations and strong RG attraction.
- **Untested architectures, which are changes of route rather than counterexamples:**
  - Lorentz-covariant **spacetime-event substrates**, such as a Lorentzian Poisson sprinkling;
  - **number-changing media, i.e. created sites**;
  - extra dynamical sectors;
  - SUSY.

## (2) The full mass matrix (K1, CHECKED, sympy)

**Setup.** L = √−g[F(B) − Λ], with spatial labels only, about flat space.
- **No tadpole:** F′(b₀) = 0, i.e. **enthalpy w = ρ + p = 0**.
- **The masses:**
  - m₀ = m₁ = m₄ = 0 (EXACT, from the residual time reparametrization);
  - m₂ = 0 for the fluid, against (S₁ + 4S₂)/2 for a solid;
  - only m₃² ∝ F″ survives.
- **The π̇² coefficient is exactly w/2.** So on flat space the liquid has **no kinetic term**: the whole quadratic action is (F″/2)(∇·π)². There are no vortex modes at this order and no sound dynamics, and the medium is infinitely strongly coupled (COMPARATOR: Endlich–Nicolis–Rattazzi–Wang).
- **With w ≠ 0,** space is not flat. A CC counterterm cannot cancel w, because it shifts ρ and p oppositely. Flatness needs w ≲ 1e-123 M_Pl⁴, while a quantum liquid of Planck-spaced sites has w ≳ M_P⁴ from zero-point motion (ARGUED).
- **What is new.** In F1b, w is also the liquid's inertia, so the tuning that flatness needs **switches the liquid off**.

## (3) Can a quantum liquid of sites exist?

- **Supplied parameters.** It needs a mass per site, a pair potential, and a quantum parameter in a narrow window (helium-4 stays liquid, H₂ freezes; COMPARATOR). None are in the axioms.
- **The Qubit axiom changes too.** Position and momentum form a canonical algebra with no finite-dimensional representation (the landed 05-02 no-go). So F1b changes Qubit as well as Lattice; ROUTES.md listed only Lattice.
- **Low-energy phase (COMPARATOR).** Bosonic sites give a superfluid with an extra phonon, which needs nμ = 0 on flat space. Fermionic sites give a Planck-scale Fermi surface.
- **Records (ARGUED).** If a record locks its site's position, accumulating records pin sites permanently, and R3's frozen-set stiffness returns. If records cannot lock positions, geometry cannot be read.

## (1) One light cone (K2, CHECKED)

- **The model.** A Yukawa theory with a spatial-only regulator f(\|k\|/Λ) and continuous time, standing in for matter on the liquid in its rest frame.
- **The result:** δc_φ − δc_ψ = (2/3)·ξ·g²/16π², with **ξ = 1 + 2∫₀^∞ x f′(x)² dx ≥ 1**, independent of Λ.
  - Four regulator shapes give ξ = 2, 3, 7/3 and 2, reproducing Collins et al.
  - **No regulator shape removes it.** At electromagnetic strength the split is at least 3.9e-4, against bounds of about 1e-15.
- **Repo prior art.** It agrees with the Z³ continuous-time value of +0.0263 g² (the viability-branch one-light-cone note), and with main's `docs/LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`.
- **No time–space symmetry.** The repo's one known protection is the hypercubic tick (Z³ × Z_τ, the kinetic-isotropy primitive), and F1b deletes exactly that.
- **Graviton speed (ARGUED).** With a supplied Einstein–Hilbert term, loops shift c_g by about NΛ²/(16π²M_P²) ~ 1e-2, against 1e-15.
- **The one exception** is supersymmetry (COMPARATOR: Groot Nibbelink–Pospelov), which no one has built here.

## (4) Assumes the target? Partly

- The intertwiner needs couplings from proper distances in a **supplied** metric.
- The liquid's displacement is a **vector** (only ∇·π appears), not the helicity-2 carrier.
- So F1b fixes m₂ naturalness for a supplied metric and leaves the mediator problem untouched.

## (5) Tried? Not in the repo

The light-cone obstacle is prior art (main 06-06 note; the 09-27 viability note). Option B of 09-29 had no bounded test.

## (6) Target-equivalent? Yes, or harder

- "One light cone on a fluid" is the open Collins problem, with the repo's one fix removed.
- "A flat vacuum with a dynamical liquid" contradicts itself.
- **One gain (SUGGESTED):** continuous translations give an exactly conserved momentum, so K3a's lattice-scale (umklapp) obstruction should go away.

## Reopen conditions

1. Sites that are not conserved (μ = 0 by equilibrium). There are then no lasting labels, so m₂ = 0 must come from elsewhere.
2. A site law invariant under 4D rotations in Euclidean spacetime, such as the Christ–Friedberg–Lee random lattice. That is F1a in 4D, which inherits R3's per-configuration noise.
3. Site energy that does not gravitate, which breaks universality for composites bound through the liquid.
