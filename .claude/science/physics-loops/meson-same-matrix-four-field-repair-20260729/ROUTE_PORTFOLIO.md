# Route portfolio

The review used current `origin/main` and searched meson, Grassmann, Wick, minor,
same-matrix, determinant-weighted, operator-sector, and transfer-kernel variants.

| Route | Object and mechanism | Strength vs narrowed target | Status |
|---|---|---|---|
| Same-matrix covariance minor | one `M`, explicit Wick determinant, temporal intertwiners | target-equivalent | candidate-complete |
| Grassmann source derivative | second bilinear-source derivative of `det(M+J)` | target-equivalent | unexplored |
| Exterior-power covariance | second compound of `M^{-1}` | target-equivalent | unexplored |
| Analytic trace kernel | `Tr(V^dag G V G)` | weaker alone; comparator after same-M construction | completed comparator |
| Genuine operator sector | quark-antiquark or nonempty-vacuum Hilbert construction | stronger than narrowed target | open |

The same-matrix route directly implements the audit's artifact request. It does not
establish the stronger operator-sector interpretation, which is explicitly left open.
