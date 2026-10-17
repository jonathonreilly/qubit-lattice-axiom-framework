# C11: site-local realization of the BKSF codes

- `siteaction.py`: read naively as three axis qubits per site (site v owns its edges (v,+a)), the BKSF codes
  are almost never symmetric under the framework's site rotation: 57 codes have a trivial stabilizer and 3
  have a C3. The reason is that the site rotation maps reversed edges to the wrong site.
- `halfedge.py`: use six direction-labelled qubits per site (half-edges) with a Z Z repetition stabilizer
  on each edge. The site action then maps the edge operators exactly, the stabilizers equal the edge-action
  stabilizers, and the orbit sizes are 4/6/12 (now in the runner).
