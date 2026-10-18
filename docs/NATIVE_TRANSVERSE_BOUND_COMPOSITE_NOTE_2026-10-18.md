# A native neutral bound composite at transverse band-edge momentum

**Status:** bounded-support.
**Primary runner:** [scripts/native_transverse_bound_composite.py](../scripts/native_transverse_bound_composite.py)

The same one-qubit Hamiltonian has an isolated neutral composite in its complete
compact four-wall first-order sector near momentum (0,pi,0). No binding potential
or collective interaction is added. At that momentum, the exact hopping graph
splits into chains and a three-lead junction. The latter has normalized root
amplitude1/2 and bound energy -3sqrt2, below the entire coefficient continuum
[-4,4]. Its physical leading energy is8Jz-3sqrt2 Jz lambda.

The original distance-two bond readout has zero leading dressed-source overlap
at the exact band-edge momentum.
A small momentum displacement activates it: with b=cos(Qy/2), its derived
leading bound-state amplitude is -3lambda b/2. The corresponding leading
positive weight is9lambda²b²/4. This source coefficient comes from the original
physical operator and ground dressing, rather than a supplied scalar coupling.

The branch persists in an explicit neighborhood, but its dispersion is a
saddle: positive curvature along x and z, negative curvature away from pi along
y. It is therefore not an isotropic relativistic scalar. The anchor state is
also compact; a controlled large-feature limit is a separate next calculation.

The [complete derivation](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/TRANSVERSE_BOUND_STATE_PROOF.md)
includes the exact wavefunction, native Bloch matrix elements, source overlap,
second-order momentum coefficient and independent checks. Physical controls
use640-qubit bit configurations, not640-qubit exact diagonalization. Numerical
coefficient graphs corroborate the proof. No full-H isolated band, experimental
line, fermion, gravitational scalar or cosmological identification is claimed.
