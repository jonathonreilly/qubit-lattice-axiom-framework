# No-Go Ledger — BAE F1-vs-F3 + u_0(SU(2)) campaign

## Target 1 (BAE F1-vs-F3)

### Routes already shown to FAIL (do not re-explore)

| Route | Result | Source |
|---|---|---|
| Plancherel measure on Z/3Z | Selects F3 (rank-weighted), not F1 | 30-probe BAE campaign + PR #1174 |
| Born-rule operationalism | Selects F3, not F1 | 30-probe BAE campaign + PR #1174 |
| Jaynes max-entropy (over circulant Hermitian) | Selects F3, not F1 | 30-probe BAE campaign + PR #1174 |
| Probe 25/27/28 7-AV convergence | Mutual deviation <1e-9 on F3, conclusive | PR #1174 + BAE campaign |
| `koide_kappa_block_total_frobenius` retention (already retained) | Ratifies F1-extremum algebra but does NOT supply F1-vs-F3 selection mechanism | PR #1174 |

### Open routes worth attempting (per pre-closure analysis)

| Route | Expected probability | Reason |
|---|---|---|
| SUSY-style oscillator decomposition | Low-medium (~15%) | Untested route; gives multiplicity-weighted norm naturally if works |
| Cl(3) bivector irrep on dim-2 spinors | Medium (~25%) | Cl(3) faithful irrep retained; need to check if it picks F1 |
| Plancherel on SU(2) (different group than Z/3Z) | Low (~10%) | Different group; needs to embed circulant structure |
| Literature: canonical extremal principles | Variable | Worth a survey |

## Target 2 (u_0(SU(2)) numerical)

### Known difficulties

| Difficulty | Reason |
|---|---|
| No framework-native non-perturbative SU(2) plaquette evaluation | Existing repo lacks this — would need new lattice code or analytic strong-coupling expansion |
| Lüscher mean-field is a literature import, not framework-derived | Would land as bounded with explicit Lüscher admission |
| `alpha_s_tadpole_improvement_vertex_power_narrow_theorem` is retained but for SU(3) not SU(2) | Template exists; needs SU(2) analog |

### Routes worth attempting

| Route | Expected probability |
|---|---|
| Analytic Lüscher-style tadpole derivation from Cl(3) bivector + b_2 = 19/6 | Medium (~30%) — likely Path B bounded |
| Framework-native strong-coupling series at SU(2) Wilson plaquette | Low (~15%) — needs new machinery |
| Match-to-literature + prove framework-internal route gives same | Medium-high (~40%) — but lands as bounded with literature import |
