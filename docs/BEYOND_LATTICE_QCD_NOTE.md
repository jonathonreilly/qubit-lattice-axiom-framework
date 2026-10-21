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

- **Load-bearing (in scope):** The supplied field changes finite detector-density diagnostics on a `32^3` lattice. In the separate slit model, a common linear transfer with one additive slit mask and the supplied quadratic readout gives vanishing Sorkin `I_3` up to floating-point error. These are conditional model calculations.
- **NON-load-bearing (split off / admitted):** The interpretation that `I_3 = 0` constitutes a derivation of the Born rule from graph structure — rather than a consequence of the `np.abs(psi)**2` readout assumed in the runner — depends on a readout-map bridge (connecting graph-path amplitudes to probabilities without pre-assuming Born) that is not supplied; that identification of the Sorkin test result with a derived Born rule is admitted as a not-derived relabeling of the numerical output.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Supplied field and density diagnostic

The runner solves a finite Dirichlet Poisson equation and propagates complex
amplitudes with the supplied edge phase `exp(i k L(1-f))/L`. Its density is
`abs(psi)**2`, normalized in the implementation. Neither the action nor the
quadratic readout is derived here. A point-source field and one additional
feedback step sourced by the first propagated density are compared with the
zero-field case. The feedback calculation is not a converged self-consistent
solution.

The inputs are `N=32`, source `(1,16,16)`, point mass `(16,20,16)` of strength
8 in the runner's Poisson convention, `k=6`, transverse Gaussian width 2.5,
and detector plane `x=30`. The feedback source coefficient is 2. The field
changes detector centroid and RMS spread. A finite-window profile is shifted
by **free centroid minus field centroid** before its L2 difference is measured;
interpolation, boundary cropping and renormalization mean this is only an
approximate translation alignment. The previous sign moved the profile away
from the reference and its reported 0.352 value is withdrawn.

The central-window `(max-min)/(max+min)` is a density contrast. An envelope
change can change it; it is not a measurement of quantum coherence or a
fringe-specific visibility. The runner's diagnostic predicate is a disjunction
of centroid, shifted-profile and spread thresholds, not a proof that each
observable changes in every parameter regime.

Standard lattice methods can also be supplied with external fields. This
finite calculation establishes no impossibility or superiority theorem about
lattice QCD and no physical graph-gravity identification.

## Pairwise interference under explicit readout premises

In a separate `20 x 21` forward-transfer graph, one barrier mask selects
slits. The transfer before and after the barrier is fixed across all slit
subsets. Hence `psi_ABC = psi_A + psi_B + psi_C` and likewise for pairs.
With the supplied `P_S = abs(psi_S)**2`, expanding the squares gives exactly

`I3 = P_ABC - P_AB - P_AC - P_BC + P_A + P_B + P_C = 0`.

This algebra holds pointwise; the runner checks finite floating-point
instances at `k=2,4,6,8,10,15,20` and spacings `2,3,4,5`, with relative
threshold `1e-12`. Both additive amplitudes and quadratic readout are needed.
Linearity alone does not derive the readout; nor does it ensure the identity
when the transfer itself changes between slit configurations.

The comparison control uses slit-dependent layer normalization and a cubic
amplitude update. Both can break amplitude additivity. A nonzero `I3` in that
control is not an isolated test of the cubic term and is not a violation of
the quadratic readout, which the control still uses. It demonstrates that the
diagnostic can detect the resulting failure of the additive-amplitude model.

Physical gravity, a derived probability map, and comparison with other
frameworks remain separate open bridges. The script is a diagnostic reporting
program; its process exit code alone is not a fail-closed theorem gate.
