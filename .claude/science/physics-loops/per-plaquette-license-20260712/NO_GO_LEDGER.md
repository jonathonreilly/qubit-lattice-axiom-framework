# No-Go / Pruned-Route Ledger

## R1: minimal-nonempty-covariant-lift selector — PRUNED (pre-execution,
supervisor computation 2026-07-12)

Route: derive the license as the unique MINIMAL covariant lift whose
fundamental loop family is nonempty.

Pruning witness (computed by hand, to be re-verified in the block-01 runner):
covariant subdomains of C_1({0,e1}) containing the endpoints decompose into
link-stabilizer orbits {endpoints} ∪ {axial: -e1, 2e1} ∪ {transverse: ±e2,
±e3, e1±e2, e1±e3}. The TRANSVERSE-ONLY domain {endpoints ∪ transverse} is
strictly smaller than C_1 yet still passes all plaquettes under mutual
containment (checked on plaquette (0,e1,e1+e2,e2): every vertex is endpoint-
or transverse-relative to every edge). Hence minimality does NOT select the
unit neighborhood; the naive selector theorem is FALSE as stated.

Consequence: the derivation must go through the permissive-bound reading
(license = one-tick reachability upper bound C_1, unique by R-definition),
not through minimality. The transverse-only witness becomes a REQUIRED
robustness check in the block-01 runner (it discriminates the two theorem
shapes).

## Prior audit no-gos touching this lane
- Target note's own boundary: does NOT prove the fundamental action is
  per-plaquette; lengths 4/6 only; theta_bare untouched. Campaign inherits
  those boundaries.
