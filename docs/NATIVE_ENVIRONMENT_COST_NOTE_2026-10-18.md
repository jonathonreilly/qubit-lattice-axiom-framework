# Native energy bounds the size of a relaxed feature's environment

Status: bounded-support. No empirical scalar identification.

The one-qubit Hamiltonian already assigns an area cost to an almost-flat environment around a heavy feature. For an m by m patch in the derived four-layer coefficient model, the exact flat-sector cost is at least 6m²-74m-4 above the global ground, with an explicit correction for imperfect flatness. The proof uses internal interactions, boundary norms and a native product trial; it adds no surface tension or chosen environmental potential.

The stronger local version of the cost bound balances native kinetic and environment energies. Along the stated growing-box weak-coupling limit, the actual odd-heavy gap is 4J-4Jlambda+Theta(Jlambda^(5/2)); the dressing correction is positive and has matching upper and lower scaling bounds. The kinetic defect <T+4> is Theta(lambda^(3/2)), giving a defined transport scale Theta(lambda^(-3/4)). No environmental potential or radius is selected by hand. This is not a proof of a sharp domain radius.

Combined with the previously derived actual heavy-band energy bound, an almost-surely flat particle-relative patch cannot grow faster than O(lambda^(-3/4)). This applies to the matched dressed state in the odd, isolated two-wall cluster and R comparable to lambda^(-1). The earlier guaranteed flat-patch scale q<3/8 and this upper bound leave a genuine unresolved interval. Neither selects a radius or derives a cosmological profile.

See the [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/ENVIRONMENT_COST_PROOF.md), [independent check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ENVIRONMENT_COST_CHECK.md), and [runner](../scripts/native_environment_cost.py). These are exposed model-development calculations; Hamiltonian, anisotropy, geometry and measurement identification remain premises.
