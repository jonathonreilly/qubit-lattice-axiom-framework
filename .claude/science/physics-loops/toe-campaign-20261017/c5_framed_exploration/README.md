# C5 exploration: framed edge codes and the statistics method (not a note)

The question was whether a 3D toric code with "framed" hopping operators
U_e = Z_e X_{S(e)} (edge qubits, labels fixed) can carry a fermionic vertex
charge with a large rotation symmetry. If so, an O-covariant stack would carry
fermion multiplets of size 24/|H|.

- **First pass (`framed.py`, `symframed.py`).** The unconfined box-solver
  T-junction reported "fermions": single-edge framings with trivial symmetry
  (`framed.log`), and two-edge framings with T, D3 and C3 symmetry. The
  T-framed code has symmetry exactly T, and constant torus code dimension
  (log2 = 3 at L = 4, 5, 6).
- **Artifact.** Its T-junction sign depended on the leg choice
  (`tcheck.py`): -1 for (e_x, e_y, e_z) but +1 for the reversed or doubled
  legs. That is impossible for a genuine exchange statistic.
- **Straight legs (`straight.py`, `symstraight.py`).** For these codes U_e
  is a pure hopping operator. The legs, built as products of U_e along
  axes, give +1 for all 20 direction triples, for the plain, T-framed and
  earlier "fermionic" framings. Every symmetric framing with up to two
  edges, for O, T, D3, C3, D4, C4 and D2, is bosonic (`ss2.log`).
- **Tube-confined solver (`tubestats.py`, `tube3d.py`).** It reproduces the
  2D toric code e, m = +1 and e x m = -1 for several leg geometries, and
  gives +1 for the 3D framed codes. The C4 runner now uses it;
  `c4tube.py` re-checked the 36 unsoldered rules (bosons).
- **Conclusion.** This ansatz produced no genuine fermion. That does not
  show that 3D fermionic stabilizer codes need more structure in general:
  they exist (Levin–Wen 2003; Chen–Kapustin 2019). The framing-multiplet
  question stays open.
