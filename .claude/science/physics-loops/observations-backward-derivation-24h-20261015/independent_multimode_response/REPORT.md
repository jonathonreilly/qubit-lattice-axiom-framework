# Focused finite-multimode check

PASS within the stated finite positive-residue, below-pole and real common-readout domain. No material mathematical or implementation defect found. Complete note was read and the independent proof recorded before author code inspection; complete code and output then read. Exact binding:

- NETWORK_EVOLUTION_BLOCK17_v1.md: 540bd73f34f9c43470f4ce0b8a2d96ef48f8ce10d9cade400eea83922f176a60
- probe_multimode_response_v1.py: 9a902ab84b950ef05ad31b6f9b4508d4bfc257878302e3da573176e61d806802
- MULTIMODE_RESPONSE_CONTROLS_v1.json: 1fc99fe20682d365dd717b0cfe4031be639f7af476c04eaa5328e541423aa84c

The action's boundedness/coercivity condition follows by independent square completion, including its equality case. The harmonic formula correctly uses x=4omega² and positive residues g_j²/(8tau_j). Positive frequency, exclusion of resonances and a periodic particular branch or justified transient treatment remain indispensable; arbitrary homogeneous preparation is not removed by this frequency test.

Both two-column Cauchy determinants have negative sign with increasing settings/poles. Their product is positive, giving the pair expansion and strict positivity exactly when at least two distinct poles have positive residue. Repeated poles combine, zero residues disappear, and the empty response is constant. Ordered row and column pairs may interleave; only their own order and all four settings' distinctness matter. The below-all-poles condition is explicit and cannot be inferred from four-point success.

A common nonzero real affine gain preserves determinant sign and exact zero, including negative gain. Zero gain loses identification; complex or frequency-dependent gains are outside this guarantee. The entry and determinant error bounds include quadratic error terms and permit correlated measurement errors. Their rejection conclusions are correct within the frozen measurement model, with frequency uncertainty and harmonic extraction separately bounded. The moment condition equals a nonnegative weighted pair variance with the same distinct-pole equality cases. Static stability bounds lambda4-M0 below by zero but does not select it or a spectral shape.

Independent check.py uses exact rational interleaved settings, duplicate/zero poles, negative and zero readout gain, direct moment pair sums and all 16 corners of a rational point-error box. Forty-nine assertions passed. Full author JSON reproduced exactly: 13 passing families. The exact general derivation, rather than the finite controls alone, supports the quantified statements. Synthetic evidence supplies no empirical validation, unique hidden-mode reconstruction or universal no-go.

Actual commands, 120-second execution bounds, successful return codes, timings and stdout/stderr are preserved beside results.json. No failures or timeouts occurred; all frozen source hashes were rechecked unchanged. No canonical or author source was modified and no audit verdict was applied.
