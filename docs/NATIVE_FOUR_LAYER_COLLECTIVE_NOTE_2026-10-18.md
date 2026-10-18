# Native four-layer collective response

Status: bounded-support. A fixed four-layer slab of the existing one-qubit
Hamiltonian has a positive low-energy neutral response to the original bond
diagnostic. Both the collective dynamics and its readout vertex are derived
at order lambda^4; no extra interaction or independently chosen coupling is
added. The thin geometry and weak-anisotropy regime remain supplied premises.

The proof is [FOUR_LAYER_COLLECTIVE_PROOF.md](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOUR_LAYER_COLLECTIVE_PROOF.md).
The reproducible coefficient control is [native_four_layer_collective.py](../scripts/native_four_layer_collective.py).

For periodic height four, in units J lambda^4/128, the derived Hamiltonian is
K=-4 sum P-5 sum E, while the original readout in units lambda^4/(128 sqrt(V))
is O=-12 sum P-18 sum E. Thus its centered ground-state source is
-3(E-<E>)g. Perron-Frobenius positivity proves its variance is strictly positive
at every fixed R>=3. Finite-box analytic perturbation transfers this response
to the original microscopic model with scaled error O_R(lambda). This is a
positive spectral window theorem, not an assertion of a bulk particle pole.

Opening the longitudinal boundary changes the native coefficients to
K=-18P-16E and O=-51P-48E. The same mechanism remains nonzero; its numerical
strength depends on geometry. Open transverse calculations show a low mode
whose edge participation remains about sixteen bonds between R5 and R6,
consistent with a corner contribution. It is not used as evidence for a bulk
mode. Removing transverse edges gives a visible periodic R6 coefficient gap
75.44675718 (physical energy 0.58942779 J lambda^4), with coefficient source
weight 196.2931143. The microscopic weight carries lambda^8/(128^2 V).
A much smaller gap 0.00004618 is dark in this diagnostic, illustrating why
the smallest eigenvalue alone does not identify the relevant mode.

Periodic R5 momentum controls show visible coefficient gaps 74.26777331 at
(0,0), 77.03850323 at (1,0), and 79.20412825 at (1,1), where momentum units
are 2pi/5. These finite results are neither a thermodynamic dispersion fit nor
a Lorentz-invariance test. High Lanczos nodes failing direct residual checks
are retained as rejected diagnostics in the development JSON. All numerical
inputs are exposed development calculations, not calibration or independent
observational tests. Native microscopic action, state, scales, three-dimensional
continuation, stable particle interpretation, matter coupling and measured
source/detector identification remain open.

The [frozen development results](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_layer_development_results.json) retain the larger R5/R6 and momentum diagnostics, including rejected nodes. Their [periodic solve recipe](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_periodic_development.py) and [momentum recipe](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_momentum_development.py) are preserved development scripts with original scratch-path dependencies; they are not the short replay entrypoints. The short runner independently replays exact winding marks and dense R3/R4 controls, not the larger solves.
