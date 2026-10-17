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
- `fluxconv.py`: search for a D3-invariant flux convention F = span(S^o_p * beta_c(p)) with beta
  supported on plaquette corners (running).
