# Continuous Hermitian paths: conditional inertia and determinant boundaries

**Type:** bounded_theorem
**Status:** supplied-model conditional result; physical path/selection open
**Primary runner:** `scripts/frontier_dm_abcc_signature_forcing_theorem.py`

## Theorem

Let A(t) be a continuous finite Hermitian matrix path with nonsingular endpoints. If endpoint inertias differ, some interior matrix is singular: ordered eigenvalues vary continuously, and a change in positive/negative counts requires a zero. In particular opposite endpoint determinant signs force a crossing by the intermediate value theorem. This does not require a global chart classification.

For the supplied Hbase and listed Basin 2/X endpoints, the numerical inertias (n+,n0,n-) are (1,0,2) and (2,0,1). Therefore admitting those endpoints forces a singularity on every continuous path between them. Under an independently imposed PNS premise such endpoints are excluded. PNS itself is not derived.

For a path with regular isolated crossings, net signed spectral flow is n_-(start)-n_-(end)=1 here. This is not the total number of crossings: additional opposite-direction crossings may cancel. For merely continuous paths the existence result holds, while counting individual crossings requires additional regularity.

An explicit control is diag(f(t),-1,1), with f(t)=(t-1/4)(t-1/2)(t-3/4). Its endpoint negative count falls by one but it has three simple zero crossings. This refutes any inference of exactly one crossing from endpoint inertia alone.

## Numerical scope

The runner retains listed endpoint eigenspectra, six monotone reparameterizations of each straight segment, finite region scans and sampled crossing counts. Those six parameterizations traverse the same segment; they are not six geometrically distinct curved paths. Their sampled Basin-1 positivity does not certify every path to that endpoint. Region samples do not prove that determinant sign determines a unique inertia throughout the chart; in all Hermitian 3x3 matrices each determinant sign contains two inertia classes.

Nonzero neutrino mass-squared differences allow a zero lightest mass. Even knowledge of nonzero physical endpoint masses would not exclude zero crossings at intermediate couplings. Physical interpretation of eigenvalues and PNS require their own bridge. No observation-derived PNS, unique physical source, whole-domain chamber classification or retained status is asserted here.

## Recovery and context

Original source is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. Related notes are context/definitions, not blanket retained authority:

- [dm_abcc_pmns_nonsingularity_theorem_note_2026-04-19](DM_ABCC_PMNS_NONSINGULARITY_THEOREM_NOTE_2026-04-19.md)
