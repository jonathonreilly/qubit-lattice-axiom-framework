# Beyond Lattice Gauge Theory: Two Concrete Results

**Status:** bounded runner diagnostics / interpretive contrast; effective
status is set only by the independent audit lane.
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Script:** `scripts/frontier_beyond_lattice_qcd.py`

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The runner verifies finite algebraic/numerical behavior of the chosen model, but it computes detector probabilities as np.abs(psi)**2 and therefore assumes the Born readout it claims to derive. No one-hop authority or theorem closes the gra"*

with repair: *"missing_bridge_theorem — derive the probability/readout map and graph-gravity/lattice-QCD comparison from retained inputs, then rerun an audit on the reduced or repaired claim."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The runner-computed finite numerical results are exactly produced: the gravity-QM coupling produces measurable changes in Y-centroid, RMS spread, fringe visibility, and profile shape on a `32^3` lattice, and the Sorkin `I_3` parameter is `0` to machine precision (`~10^-16`) across tested wavenumbers and slit spacings, confirming that linear path-sum superposition enforces pairwise-only interference numerically.
- **NON-load-bearing (split off / admitted):** The interpretation that `I_3 = 0` constitutes a derivation of the Born rule from graph structure — rather than a consequence of the `np.abs(psi)**2` readout assumed in the runner — depends on a readout-map bridge (connecting graph-path amplitudes to probabilities without pre-assuming Born) that is not supplied; that identification of the Sorkin test result with a derived Born rule is admitted as a not-derived relabeling of the numerical output.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## The honest overlap

Both lattice gauge theory and this graph-first framework use graphs,
Laplacians, path integrals, and gauge phases. This overlap is real and
must be acknowledged. The distinction is NOT merely "derivation direction"
(a framing argument that a reviewer would rightly dismiss). The distinction
is two concrete, testable results.

## Result 1: Gravity-QM inseparability

**Runner diagnostic:** The gravitational field proxy (Poisson potential sourced by
|psi|^2) modifies the propagator's quantum structure in ways that go
beyond simple deflection. Specifically, on a 32^3 lattice:

| Measure | Free (f=0) | With gravity | Change |
|---------|-----------|-------------|--------|
| Y-centroid at detector | 15.99 | 19.95 | +3.96 (deflection) |
| Profile shape diff (L2, centroid-aligned) | -- | 0.352 | Nonzero |
| RMS spread | 4.52 | 2.85 | -1.67 (focusing) |
| Fringe visibility | 0.29 | 0.98 | +0.69 (coherence change) |

The shape difference after centroid alignment is 0.35 -- gravity does not
merely shift the propagator, it changes its coherence structure.

**Why lattice QCD cannot do this:** In lattice QCD, the lattice is a fixed
computational scaffold. The lattice spacing `a` is a UV regulator that gets
sent to zero in the continuum limit. The lattice itself has no gravitational
content -- it cannot lens, focus, or modify quantum coherence. Quantum fields
live ON the lattice, but the lattice is inert.

In this runner surface, the action S = L(1-f) couples the quantum phase
directly to the Poisson potential. Treating that as a physical graph-gravity
identification requires a separate bridge and is not claimed here.

**Bounded claim:** The runner exhibits a gravity-coupled propagator diagnostic
on the graph-first surface. It does not prove a framework-vs-lattice-QCD
physical comparison theorem.

## Result 2: Structural Born rule (Sorkin I_3 = 0)

**Runner diagnostic:** The path-sum propagator on the graph produces Sorkin
parameter I_3 = 0 to machine precision (~10^-16) across all tested
wavenumbers (k = 2 to 20) and slit spacings (2 to 5).

The Sorkin parameter measures third-order interference:
I_3 = P_ABC - P_AB - P_AC - P_BC + P_A + P_B + P_C

I_3 = 0 means all tested interference is pairwise. On a supplied quadratic
probability readout this is the Born-rule interference signature; the readout
bridge itself is not derived by this runner.

A nonlinear (cubic) propagator gives I_3/P = 0.16, confirming the test
has discriminating power -- it can detect violations of the Born rule
when they are present.

**Why this differs from lattice QCD:** In lattice QCD (and all standard QFT),
the Born rule is an axiom of quantum mechanics. The path integral computes
amplitudes; the postulate that probabilities = |amplitudes|^2 is separate.
Lattice QCD does not derive the Born rule -- it assumes it.

In this runner, the path-sum propagator is a linear superposition of complex
amplitudes over graph paths. The linearity of this sum forces the tested
Sorkin `I_3 = 0` diagnostic. A full Born-rule theorem still requires the
separate probability/readout bridge.

**Bounded claim:** The runner confirms the linear path-sum pairwise
interference diagnostic. It does not by itself derive the probability rule.

## What this does NOT claim

- We do not claim lattice QCD is wrong or that its results are invalid.
- We do not claim this framework can reproduce lattice QCD's precision
  predictions for hadron spectra, quark confinement, etc.
- We do not claim the dimension emergence result (d_s = 3 special) is
  unique to this framework -- that result depends on lattice topology
  and could be obtained in other graph-based approaches.

## Reviewer FAQ

**Q: Isn't the gravity-QM coupling just a semiclassical approximation?**
A: The coupling S = L(1-f) with f sourced by |psi|^2 is indeed
semiclassical. But the point is that this coupling is built into the
graph structure -- it is not an add-on. Lattice QCD has no analogous
coupling at any level of approximation.

**Q: Isn't the Born rule result just Feynman's path integral argument?**
A: Partially. Feynman showed that linear superposition of amplitudes controls
interference structure. This row shows the Sorkin diagnostic concretely on a
graph propagator; it does not close the full probability/readout theorem or a
framework-vs-lattice-QCD comparison.

**Q: Can't you just add gravity to a lattice?**
A: Not in the same way. Lattice quantum gravity is a separate research
program (e.g., causal dynamical triangulations, Regge calculus). It uses
different lattices with different purposes than lattice QCD. The point is
that this framework gets both from the SAME structure.
