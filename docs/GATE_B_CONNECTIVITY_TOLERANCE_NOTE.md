# Gate B Connectivity Tolerance Note

**Date:** 2026-04-04  
**Claim type:** bounded_theorem
**Status:** finite-harness claim awaiting independent audit
**Primary runner:** [`scripts/gate_b_connectivity_tolerance.py`](../scripts/gate_b_connectivity_tolerance.py)
**Cached output:** [`logs/runner-cache/gate_b_connectivity_tolerance.txt`](../logs/runner-cache/gate_b_connectivity_tolerance.txt)

## Claim

The runner checks a finite statement about its declared algorithms and no
more:

1. In the fixed-adjacency jitter sweep, every jittered graph keeps exactly the
   same forward stencil while only the embedded transverse coordinates change.
   The frozen readouts remain finite through jitter `0.5`, and the `TOWARD`
   series is not monotonically decreasing.
2. For each seed, the templated-growth and K-NN rows have exactly the same
   unsnapped node coordinates and layers. They differ in adjacency: one uses
   the fixed label/offset stencil and the other recomputes the nine nearest
   targets in the next layer. Their aggregate finite readouts differ.

Thus the output depends on connectivity even when the coordinate sample is
held fixed, and the fixed-stencil `TOWARD` series is not monotonically
decreasing on the tested finite sweep. This is not a theorem that connectivity
is intrinsically the physical Gate B bottleneck.

## Declared finite harness

The finite object checked by the theorem is given by the following explicit
algorithmic definitions. They are not presented as physical laws.

- The slab has `13` layers and transverse labels `-5,...,5` in each direction.
- The six seeds are `{5,18,31,44,57,70}`. Fixed-stencil jitter adds independent
  seeded Gaussian displacements of standard deviation `jitter` to each
  transverse coordinate and leaves the layer coordinate unchanged.
- Templated and K-NN growth use the same seeded transverse Gaussian random
  walk with step standard deviation `0.22`. The templated row keeps the fixed
  label/offset edges; the K-NN row instead selects the `k=9` nearest targets in
  the next layer.
- The architecture row named `jittered lattice` is the fixed-stencil
  `jitter=0.5` ensemble. The snapped/grid-like row uses the templated random
  walk and applies Python's `round` to both transverse coordinates after every
  step while retaining the fixed label/offset edges.
- The fixed adjacency advances one layer with transverse offsets
  `(dy,dz) in {-1,0,1}^2`, clipped at the slab boundary. Its exact finite
  stencil properties are supplied by
  [Gate B Local Stencil Connectivity Bridge](GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md).
- The supplied runner scalar is
  `f_i = strength/(r(i,mass)+0.1)` and the supplied edge action is
  `S_ij = L_ij(1-(f_i+f_j)/2)`.
- The supplied edge weight is
  `exp(i K S_ij) exp(-BETA theta_ij^2)/L_ij`, with `K=5` and `BETA=0.8`.
  Here `L_ij` is the Euclidean edge length and
  `theta_ij=atan2(sqrt(dy^2+dz^2),max(dx,1e-10))`. The finite layered
  recursion is evaluated directly by the runner.
- Central barrier nodes in layer `13//3=4` satisfy `-1 < y < 1`. The source is
  the stable `(y_label,z_label)=(0,0)` node of the first layer. The detector
  set is the final layer. Its source amplitude is `1`; propagation drops an
  amplitude when `|a_i|<1e-30` and skips an edge when `L_ij<1e-10`.
- At layer `2*13//3=8`, the mass site is selected by its stable grid label
  `(y_label,z_label)=(y_m,0)` for `y_m in {2,3,4}`, not by rounded drifted
  coordinates. Hence every seed keeps the same three mass labels and the same
  nine strength/label trials. The scalar strength is `q*5e-5` for
  `q in {0.75,1,1.25}`.

No physical Poisson/source law, boundary condition, regulator selection,
absolute normalization, detector interpretation, or physical growth selector
is imported into the bounded claim.

## Exact readout definitions

For detector node `d`, the runner defines the normalized terminal weight

```text
P_d = |a_d|^2 / sum_e |a_e|^2.
```

For a mass label `y_m`, its detector window is
`W(y_m)={d: |y_d-y_m|<=1.5}` and its mass-window gain is

```text
delta(y_m,q) = sum_{d in W(y_m)} [P_d(mass strength q)-P_d(free)].
```

The three displayed summaries are definitions:

- `mean delta` is the arithmetic mean of `delta(y_m,1)` over the three mass
  labels and six seeds;
- `TOWARD` is the fraction of the `3 x 3 x 6 = 54` finite trials for which
  `delta(y_m,q)>0`;
- local `F~M` is the arithmetic mean of the three-point log-log slopes of
  `max(delta,1e-30)` against `q in {0.75,1,1.25}`, first over mass labels and
  then over seeds.

`TOWARD` and `F~M` are labels for these finite functionals. They are not a
physical force-direction observable or a universal mass law.

## Frozen replay result

| architecture | `TOWARD` | mean delta | local `F~M` |
|---|---:|---:|---:|
| ordered lattice | `66.7%` | `+0.000012` | `0.66` |
| jittered lattice | `72.2%` | `+0.000007` | `0.72` |
| templated growth | `50.0%` | `+0.000013` | `0.50` |
| K-NN grown | `61.1%` | `+0.000013` | `0.61` |
| snapped/grid-like | `50.0%` | `+0.000003` | `0.50` |

The paired templated-growth and K-NN rows use identical unsnapped coordinates
seed by seed. Their different `TOWARD` and local `F~M` summaries therefore
witness adjacency dependence inside this harness; they do not select either
adjacency as physical.

| fixed-stencil jitter | `TOWARD` | mean delta | local `F~M` |
|---|---:|---:|---:|
| `0.00` | `66.7%` | `+0.000012` | `0.66` |
| `0.10` | `55.6%` | `+0.000003` | `0.55` |
| `0.20` | `61.1%` | `+0.000010` | `0.61` |
| `0.30` | `55.6%` | `+0.000014` | `0.56` |
| `0.40` | `55.6%` | `+0.000008` | `0.55` |
| `0.50` | `72.2%` | `+0.000007` | `0.72` |

The fixed-stencil `TOWARD` column is not monotonically decreasing. The safe
statement is the table and that exact finite ordering, not a general
noise-tolerance law.

## Dependency and claim boundary

The load-bearing dependency is the finite local-stencil authority cited above.
All other load-bearing content is defined and recomputed inside the registered
runner. In particular, this note does not claim:

- a Gate B dynamics closure or physical gravity theorem;
- a derivation of the scalar source, regulator, boundary, or normalization;
- physical detector-window, `TOWARD`, or `F~M` semantics;
- dynamical generation or physical selection of the fixed stencil or K-NN
  rule;
- an architecture-independent theorem that connectivity is the bottleneck;
- universal constants or a prediction outside the displayed finite harness.

The open physical source, readout, and growth-selector problems are outside
this theorem rather than hidden premises used to promote it.

## Verification

Run:

```bash
python3 scripts/gate_b_connectivity_tolerance.py
```

The runner recomputes both tables, verifies the same-coordinate
templated/K-NN pairing, checks that jitter never changes the fixed adjacency,
checks the 54-trial panel and terminal normalization for every displayed row,
and validates this note's bounded source boundary.
