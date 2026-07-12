# Route Portfolio And Stuck Fan-Out

Scores are 0-3 for claim movement, trace reachability, import retirement,
review value, artifactability, hard-residual pressure, and overclaim risk
(negative).

| Route | Attack | Movement | Trace | Import | Review | Artifact | Hard pressure | Risk | Disposition |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Direct heavy-kernel reconstruction | derive `A,b,c,d` from the weak source carrier and compute `K00` | 3 | 3 | 3 | 3 | 1 | 3 | -1 | attempted; no typed source-to-`H_core` map exists in packet |
| All-baseline determinant equation | insert actual coefficients before comparing responses and solve symbolically | 3 | 3 | 2 | 3 | 3 | 3 | 0 | selected subroute; gives `K00 = c tau_+` |
| Equivariant partial isometry | map the normalized `S2` and `S3` invariant rays | 2 | 2 | 2 | 3 | 3 | 3 | -1 | attempted; fixes ray transport but leaves scalar intertwiner/physical identification |
| Sharp-projector normalization | use nonzero idempotency to choose the source object | 2 | 2 | 2 | 3 | 3 | 3 | -1 | attempted; selects `P+`, yielding `c=1`, not the asserted `c=2` |
| Record/log-det route | derive the physical coefficient map from additive readout | 2 | 2 | 2 | 3 | 2 | 3 | -2 | attempted; minimal axioms explicitly omit source/action and observable identification |
| Restricted-packet no-go | construct countermodels varying embedding scale and source magnitude independently | 3 | 3 | 3 | 3 | 3 | 3 | 0 | selected synthesis |

## Fan-out synthesis

The direct-kernel, determinant, representation-theoretic, projector, and
Record-facing frames agree on the same residual. The packet fixes two bright
rays but contains no typed physical map between them and no source-magnitude
selection. The determinant route is decisive because it does not merely say a
map is absent: it classifies every bright-ray embedding by `c` and constructs
response-matched countermodels. The sharp-projector route supplies the most
important falsifier to the old argument: using the projector actually gives
`c = 1`; obtaining `c = 2` requires choosing the unnormalized row-sum
generator.
