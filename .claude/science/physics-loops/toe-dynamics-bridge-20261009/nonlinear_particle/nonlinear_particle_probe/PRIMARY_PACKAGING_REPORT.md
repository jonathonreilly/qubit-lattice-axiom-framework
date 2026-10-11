# Primary particle runner packaging record — 2026-10-11

This is an author evidence record, not an independent review or formal audit verdict.
The self-contained candidate is `../root_nonlinear_particle_primary.py`, for planned
`docs/SPATIAL_PARTICLE_TO_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md`
and `scripts/spatial_particle_to_nonlinear_fluid_limit_2026_10_11.py`.
The analytic construction remains in `../NONLINEAR_PARTICLE_PROBE.md`.
No repository source or prompt file was edited by this packaging task.

## Executed evidence and source identity

The final baseline exited 0 under Python 3.13.5 in 1.804423 seconds. It uses only
the Python standard library and exact rational arithmetic, including Q(omega)
with omega squared plus omega plus one equal to zero. Its only runtime file
read is its own source bytes, to print and freeze its SHA256. The declared
`AUDIT_TIMEOUT_SEC = 180` is a harness budget, not an in-process alarm.
`AUDIT_INPUT_PATHS` conservatively names the proposed note and four mathematical
source notes as provenance/cache inputs; it does not pretend to read them at
runtime. The proposed note is not yet present in the read-only worktree.

| Artifact relative to resume_20261011 | SHA256 |
|---|---|
| root_nonlinear_particle_primary.py | `b23fbf74766b94b3cf9c0882392eee660fe917878c5f9b951c1f701dd131cf64` |
| nonlinear_particle_probe/primary.log | `1a898746c0098a13aa06ba79aed84be8dbdf5c0b246ddbba09bd73d5b1548be1` |
| nonlinear_particle_probe/run_primary_mutations.py | `d3342d48daa65d9ab5ccccf4439f1709dbc8f74eb503a196a11a364306f82a8c` |
| nonlinear_particle_probe/primary_mutations.log | `56f87de566230d7448f5404dbd3372d5275cad0c189c845f43ce46be22c4280d` |
| nonlinear_particle_probe/primary_mutation_manifest.json | `954870b2fe629d1e75254510837a898772baf0c1a91c7cda5b6a0de455900110` |
| NONLINEAR_PARTICLE_PROBE.md | `a860a3d0a914148746d0c2baee42375ebcc36a41b6722d0a20b5946b27ed62bb` |

The dependency identities were rechecked at repository HEAD
`73a76d2141d30d75c6aebfb2f2f9baa6e0a025bf`. The three directly used particle,
nonlinear-fluid and hydrodynamic source bodies retain the hashes from their
previous complete reads. The collision supplier is recorded for model provenance.
The nonlinear-fluid note remains a provisional dependency of this new construction.

| Dependency in worktree/docs | SHA256 |
|---|---|
| SPATIAL_PARTICLE_TO_LINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-09.md | `622e9c4e86ba8c181339dae82b293965726c94a717ef947120d1f5516828734b` |
| D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md | `c81c0029fb70d1cea0ecf41ee893caf357747bcda138af5d1bef5ed5848a114a` |
| D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md | `038e1ed6942d79720aa1dd7360d90f9fa1067016940ceb3554efeb99c21ed0c1` |
| SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md | `888ede1aba130d9bf4df5ffecfbadf9c4e45dd94a49ca3a350894a052e0677c0` |

## What the executable checks

- It reconstructs the 27 velocities, product weights, 288 conservative binary
  reactions and nine axial reactions. Exact sums recover the axial and nonaxial
  coefficients of C_R and S.
- At a realizable integer equilibrium count state with 5832 particles, it sums
  actual count rates times squared jumps. This yields hop coefficient 108 and
  collision coefficient 2 C_R. The corresponding pointwise F <= 2M envelope
  factors are 216 and 8 C_R, respectively. Hop calculations factor out the same
  positive physical spacing factor 1/ell on both sides.
- At a separate nonuniform admissible integer count state it checks the complete
  conditional collision and hop drifts at every cell and species. No expectation
  factorization or replacement of local transport by mixing is used.
- A direct cyclotomic DFT computes each of 288 collision and 54 directed-hop
  squared jump norms in H0, H3 and H4 on a genuine three-by-three-by-three grid.
- An admissible first collision explicitly overshoots the stopping radius. The
  checked generator increment retains the full jump energy. A separate exact
  projected-energy complete square checks the coefficient A_p squared / lambda
  and the absence of a singular delta factor in that coefficient.
- A positive, nonuniform, exactly mass-normalized iid preparation yields the
  full spatial multinomial covariance trace. An independent Fourier calculation
  agrees exactly in H0, H3 and H4 and satisfies the 27 K/(N delta squared) bound.
- An actual quadratic product has frequencies outside the principal grid box;
  direct DFT samples agree with the folded coefficients and differ from a Fourier
  cutoff. All five invariant contractions of its collision output vanish before
  and after folding. Full principal-map geometry is checked at m = 3, 5, 7, 9.
  Every upwind symbol on the exact m = 3 grid has nonpositive real part.
- Separate exponent bookkeeping checks the ell ~ delta squared, N ~ delta to
  minus 19 L2 route and the larger Sobolev schedules. It distinguishes initial,
  hop, collision, threshold, streaming, alias, cutoff, interpolation and fluid
  powers. A coarse mesh is rejected directly because ell/delta is too large.

The collision drift and rate controls use the transparent positive unit-rate
member of the family; axial dependence of C_R and S is checked coefficient by
coefficient. The displayed rational lambda is a positive control for the scalar
complete square. This runner does not re-prove its spectral-gap interpretation,
the tuned alpha value, the correctors, or the fluid Poisson responses.

## Actual scratch-source mutants

`run_primary_mutations.py` changes a single exact source fragment in each fresh
scratch copy, parses the result, and executes it in a subprocess. All 13 detected
mutants exited 1 with a mathematical AssertionError; none was credited for a
syntax/import/type error or timeout. The final mutation batch took 4.610487 seconds.
Every source and full stdout/stderr log is retained under `primary_mutants/`.
The manifest records old/new fragments, source/log hashes, runtimes and failure
sites. The baseline and final manifest were fully read, and each final failure
site and each source/log hash was checked. The primary source was unchanged by
the mutation run.

| Mutant | Load-bearing finite family | Outcome |
|---|---|---|
| cell_volume_jump | point-jump normalization | AssertionError, exit 1 |
| missing_hop_endpoint | two-cell hop energy | AssertionError, exit 1 |
| double_collision_rate | binary direction and rate count | AssertionError, exit 1 |
| collision_volume_drift | exact conditional collision drift | AssertionError, exit 1 |
| hop_clock_drift | exact conditional transport drift | AssertionError, exit 1 |
| clip_exit_energy | stopping overshoot accounting | AssertionError, exit 1 |
| halve_drift_coefficient | projected energy complete square | AssertionError, exit 1 |
| preparation_volume | initial probability normalization | AssertionError, exit 1 |
| drop_multinomial_covariance | multinomial covariance trace | AssertionError, exit 1 |
| lose_microscopic_output | conservation through collision aliasing | AssertionError, exit 1 |
| discard_alias_folding | quadratic Fourier alias map | AssertionError, exit 1 |
| mesh_too_coarse | deterministic spatial scale | AssertionError, exit 1 |
| particle_count_too_small | stopped failure scale | AssertionError, exit 1 |

## Coverage limits and integration obligations

Finite exact controls support the analytic proof; they do not establish the
all-m alias estimate, stopped Dynkin argument, uniform smooth-lifetime PDE
comparison, global Navier–Stokes existence, or a native M2 derivation. The supplied
model, smooth fluid lifetime and provisional nonlinear-fluid theorem stay
explicit premises. The preserved overshoot witness is a finite control, not the
asymptotic scale schedule. The scale table checks powers once the analytic
inequalities are established; it is not a stochastic simulation or convergence
experiment. The four finite principal-map inventories do not replace the proof
for arbitrary odd m.

No one-time quantum composition or repeated quantum history claim is added.
Independent review of the new note and final packaged source remains separate.
If integration changes the mathematics or runner, source-bound baseline and
mutation evidence must be refreshed. Copying the primary unchanged to its planned
repository filename preserves its content hash; the external mutation driver's
`PRIMARY` path must be adjusted only if it is relocated or aimed at the repository
copy. The JSON packaging hash record retains machine-readable identities.
