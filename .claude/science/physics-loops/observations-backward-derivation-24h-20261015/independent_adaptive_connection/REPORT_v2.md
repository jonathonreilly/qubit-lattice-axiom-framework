# Same-session v2 correction confirmation

PASS for the amended conditional adaptive-connection result. Complete v1→v2 note/code diffs were read and preserved. The source now requires omega>0 for separate harmonic coefficients, retains resonance exclusion, and identifies B3(0) only as rational continuation. The static cubic force is separately given as 4lambda4-g²/(2C). Direct relaxed substitution w=-gA²/(2C) yields that coefficient; the fundamental and third-harmonic continuations sum to it. The v1 counterexample is therefore addressed without changing the nonzero-frequency mathematics.

Other changes are spacing, an explicit preserved-finding paragraph, the renamed continuation control, a new static harmonic-merger control and runner binding to note v2. No physical assumption is newly promoted. The fixed-v1 derivation, independent computations and qualifications continue to apply; original v1 sources/evidence remain unchanged.

Full v2 runner reproduced the published JSON exactly: 13 passing families, zero failures. Execution was bounded by 120 seconds, completed successfully and is recorded in reproduction_v2_receipt.json with preserved stdout/stderr. Both v1 and v2 hash manifests were verified after execution. No actual execution failure or timeout occurred. Exact v2 binding:

- NETWORK_EVOLUTION_BLOCK15_v2.md: 938fd7cea467e0fbdd1ac48b0aa1a841a0584a45ccbf9aae09417851c987a6ee
- probe_adaptive_connection_v2.py: fc64827e070bd9aa550e6aec0d89521172a845a8ca77255c5df196013b107b99
- ADAPTIVE_CONNECTION_CONTROLS_v2.json: 2e221ef0d83694b82df3b0442f7edcf1823c9804a961c5d831ecce65441cf23c

This is focused source checking, not an audit verdict or empirical validation. All writes remain in independent_adaptive_connection/.
