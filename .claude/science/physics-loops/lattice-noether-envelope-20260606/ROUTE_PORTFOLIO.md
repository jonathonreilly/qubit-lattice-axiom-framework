# Route Portfolio

## Considered

1. Narrow P1 to nearest-neighbour only.
   - Valid but unnecessarily loses the arbitrary-bilinear continuity result.

2. Prove support envelope for arbitrary `c_xy`.
   - Chosen. The pair current on `{p,q}` uses only `c_pq` and `c_qp`, so finite
     support stays finite and all-to-all support stays all-to-all.

3. Treat site-mixing generators as local.
   - Rejected. The row keeps site-mixing generators out of scope and records the
     two-site shift branch as a named open item.
