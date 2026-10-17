# C9 (in progress): symmetric hop systems and O-covariant condensation of the 4-copy BKSF stack

Findings so far (L = 4 unless stated; exploratory scripts in this folder):
- `stack.py`: the O-covariant stack of the four D3 codes (log2 dim 12). Stabilizer condensation of the
  quad boson f0f1f2f3 with each copy's own ordering gives log2 dim 9, but (`quad.py`) the result is
  invariant only under a D4 subgroup of O.
- `hoptypes.py`: in a D3 code the 12 orderings give, per edge direction, 6 inequivalent hop types
  (hops differing by local flux-creating factors). D3 acts on the 6^3 assignments; exactly 2 are fixed.
- `equiv.py`: with an O-equivariant hop-type assignment the quad-condensed group (full commutant on
  the torus) is O-invariant, log2 dim 9 at L = 4. BUT the locally generated part of the kept group
  gives log2 dim 71 (L = 4) and 126 (L = 6): the commutant needs nonlocal generators, so this is not
  a local topological code. `hopcomm.py`: equivariant (mixed-type) hops at a vertex anticommute
  across a body-diagonal bipartition of the six directions instead of pairwise.
- `splaq.py`: for every ordering of a D3 code, span(S^o) (the flux-free convention defining clean
  hops) is preserved by only 2 of the 6 stabilizing rotations (E and one edge C2). Orbit-6 codes:
  1 or 2 of 4; orbit-12 codes: 1 or 2 of 2.
- `fluxconv.py`: 8 of 4096 corner-supported dressings beta give a D3-invariant flux convention
  F = span(S^o_p * beta_c(p)) (L = 4; confirmed D3-invariant at L = 6).
- `cleanhop.py` (run with LL=6 via the *L.py variants): for 2 of the 8 (beta = ([0,1],[0,3],[1,3]) and
  ([1,3],[0,1,2,3],[0,1])), rank F = 430 = reference and local clean hops exist in all three
  directions (L = 6 window, no wrapping). So a D3-symmetric clean hop system exists for the D3 code
  (`symhopL.py`: rotations map hops to hops times F*B elements, as required).
  (At L = 4 the window covered the whole torus; those runs are not meaningful.)
- `symstack2.py`, `cquad.py`: building the O-covariant 4-copy stack from these symmetric hops, the quad
  operators do NOT commute: at a vertex they anticommute in the complete bipartite pattern
  {+-z} vs {+-x, +-y} (all triangles even, so a switching by odd vertex terms would fix it, but the
  switching class singles out z and is not O-invariant), and some non-adjacent quads also anticommute.
- Status: O-covariant local Pauli condensation of the quad boson is not achieved by either route
  (mixed-type hops: nonlocal commutant; symmetric hops: noncommuting quads). Open.
