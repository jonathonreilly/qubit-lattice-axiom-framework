# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|:---:|:---:|---|---|
| `h=0.5`, `W=12`, `L=20`, `max_d_phys=5`, probe `y=5`, and field strength `5e-5` | Defines the finite tested family | admitted normalization | primary runner and two-stage helper | yes | yes | explicit in note, runner, and stdout | bounded protocol choice |
| `BETA=0.8`, `K=5`, softening `0.1`, barrier/source/detector layers, and slit `|y|>=3` | Defines propagation and source geometry | admitted normalization | two helper sources included by citation graph | yes | yes | explicit in note and helper sources | bounded protocol boundary |
| Listed 19-value `topN` schedule | Defines the exhausted finite set, including saturated duplicates at 64 and 81 | admitted normalization | primary runner | yes | yes | exact list assertion | finite scan schedule; closed for listed set |
| `ratio_rel_err <= 0.01` and `carry >= 0.99` | Defines row stability | admitted normalization | source note and runner | yes | yes | explicit bounded protocol; no universality claim | evaluation convention accepted for scoped claim |
| One-hot probe amplitude; unit-normalized detector and compressed profiles; zero-profile centroid fallback; response-ratio and relative-error denominator safeguards `1e-30`; Bhattacharyya carry on normalized profiles | Defines numerical normalization and zero-denominator behavior | admitted normalization | primary runner and two-stage helper | yes | yes | explicit helper implementation and source-note equations | bounded setup |
| Stage propagation, compression, lattice-projected centroid control, and overlap functions | Computes each row | computed lattice input | helper runners included by citation graph | yes | yes | helper source plus primary-runner-SHA cache | closed |

No observed value, fitted selector, literature value, or external comparator is
used in the load-bearing finite-sweep conclusion.
