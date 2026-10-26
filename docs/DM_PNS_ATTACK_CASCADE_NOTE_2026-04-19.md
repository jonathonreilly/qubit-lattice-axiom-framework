# PNS finite-search and specified-path diagnostics

**Type:** open_gate
**Status:** supplied-model conditional result; physical path/selection open
**Primary runner:** `scripts/frontier_dm_pns_attack_cascade.py`

PNS means det(H(t))!=0 throughout a specified continuous path. It is an additional path premise, not a consequence of mixing measurements alone.

## Retained conditional logic

For any continuous Hermitian path with det(H(0))>0, PNS implies det(H(t))>0 throughout by continuity. Conversely a positive endpoint does not ensure PNS along a chosen path: intermediate paired crossings are possible. A separate exact polynomial or certified bound can prove PNS for a particular supplied path, without selecting that path physically.

## Actual numerical evidence

The runner supplies Hbase, three affine generators, fixed candidate coordinates, a chamber q+delta>=sqrt(8/3), pairing (2,1,0), angle targets, and a sign cut. The chamber sign branch and all target values are inputs. Its 2000-seed local search can report only candidates found, not completeness or uniqueness over the whole chart. Uniqueness after filtering means uniqueness among the found candidates; no physical Basin-1 selection is inferred.

The runner samples determinant and eigenvalue tracks on the Basin-1 line and other specified lines. A sampled positive minimum is numerical evidence, not itself an all-t certificate. The historical 0.878 readout belongs to that chosen line. Other supplied endpoints yield sign changes, showing that these particular chart inputs alone do not enforce PNS on every path in the supplied collection. This does not exclude additional framework constraints or prove observational input is necessary.

Nonmonotone sampled eigenvalue tracks invalidate that particular monotonicity argument. Mixed-spectrum generators invalidate an unqualified positive-semidefinite-generator argument, not every possible lower-bound proof. The HF diagnostic compares signs across modes at sampled times; it does not by itself prove a sign change along one mode. No lattice spectral embedding is provided.

Distinct endpoint eigenvalues need not be nonzero: diag(0,1,2) is a counterexample. Nonzero measured mass-squared differences likewise do not establish nonzero lightest mass, and no endpoint measurement constrains every interpolation coupling. Neither observation establishes PNS.

The existing search, thresholds and numerical checks are retained as diagnostics. Physical admissible-domain selection, completeness, experimental interpretation of the supplied cuts and a certified path bound remain separate obligations. No DM flagship closure or universal algebraic impossibility is claimed.

## Recovery and context

Original source is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. Related notes are context/definitions, not blanket retained authority:

- [SIGMA_HIER_UNIQUENESS_THEOREM_NOTE_2026-04-19.md](SIGMA_HIER_UNIQUENESS_THEOREM_NOTE_2026-04-19.md)
- [ABCC_CP_PHASE_NO_GO_THEOREM_NOTE_2026-04-19.md](ABCC_CP_PHASE_NO_GO_THEOREM_NOTE_2026-04-19.md)
- [DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md](DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md)
