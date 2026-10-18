# Native assisted coupling across fixed feature heights

Status: conditional-support. Trace: upstream_support. No empirical scalar identification.

The existing one-qubit/site Hamiltonian generates a nearest-hop vertex that reverses two whole column backgrounds. At fixed even height L its exact leading coefficient is -J lambda^(L-1)/2^(L-2) in the x direction. No interaction or coupling constant is added. For L>=6 the prepared vacuum-background channel has squared weight J² lambda^(2L-2)/2^(2L-4) in its derived four-plaquette window near JL lambda^4/16.

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/ALL_HEIGHT_ASSISTED_HOP_PROOF.md) evaluates all virtual paths and separates diagonal contamination, dressing and background-channel interpretation. The [runner](../scripts/native_all_height_assisted_hop.py) checks exact finite path sums and the height-six third-order cancellation. These are model-development checks, not independent observational tests.

The connection is a prepared vertex, not a full heavy-particle scattering channel or cosmological scalar. Feature height, weak anisotropy, geometry, preparation and units remain supplied. A small coupling obtained by choosing a large height does not derive a physical hierarchy. Independent coefficient and window checks are recorded in the campaign native directory.
