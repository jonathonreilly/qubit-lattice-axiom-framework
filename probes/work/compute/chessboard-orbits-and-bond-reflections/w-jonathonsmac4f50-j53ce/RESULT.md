chessboard-orbits-and-bond-reflections, independent run 2 of 2
worker w-jonathonsmac4f50-j53ce (claude-opus-5), unit C-chessboard-orbits-and-bond-reflections-a2

Six-axis rule: six axis values (antipodal pairs), bond weight K = p (equal), q (antipodal), r (orthogonal).
Static law on the torus: product of the bond weights, normalised.

(1) ORBITS OF ONE DIRECTION-1 BOND (exact, breadth-first search)
  A direction-1 bond is {x, x + e1}; there are L^d of them on (Z/L)^d. Reflections act on the base x as
    site plane, direction 1:   x_1 -> 2k - x_1 - 1      (parity of x_1 FLIPS)
    site plane, direction i>1: x_i -> 2k - x_i          (parity preserved)
    bond plane, direction 1:   x_1 -> 2k - x_1          (parity PRESERVED)
    bond plane, direction i>1: x_i -> 2k + 1 - x_i      (parity flips)

  torus      bonds   site planes    bond planes    both
  (Z/4)^2      16      8  (1/2)       8  (1/2)      16  (all)
  (Z/6)^2      36     18  (1/2)      18  (1/2)      36  (all)
  (Z/8)^2      64     32  (1/2)      32  (1/2)      64  (all)
  (Z/4)^3      64     16  (1/4)      32  (1/2)      64  (all)
  (Z/6)^3     216     54  (1/4)     108  (1/2)     216  (all)

  Site planes reach a half in 2D and a quarter in 3D, as the task expects.
  Bond planes reach a HALF in both dimensions, not all of them: the reflection in the bond's own direction preserves the
  parity of the base coordinate, so the orbit is {y : y_1 = x_1 mod 2}. Only the two families together are transitive.
  (This is the HIT: the task's expectation for bond planes is wrong.)

(2) THE WEIGHT MATRIX (exact)
  W = (p - r) I + (q - r) P + r J, P the antipodal pairing, J all ones. Eigenvalues:
    p + q + 4r  (once, the all-ones vector)
    p - q       (three times, antisymmetric under P)
    p + q - 2r  (twice, symmetric under P and orthogonal to all ones)
  With positive weights the first is automatic, so
    W is positive semidefinite  iff  p >= q  and  p + q >= 2r.
  On the line (p, 1, 2): p >= 1 and p >= 3, i.e. p >= 3. At (3,1,2) the eigenvalue p + q - 2r is exactly 0: the boundary.

(3) REFLECTION POSITIVITY THROUGH A BOND PLANE, NUMERICALLY
  4 x 2 torus, the FULL Gram matrix of <F theta(G)> over all 1296 indicators of the half-torus configurations
  (theta(i, j) = (3 - i, j), crossing bonds (1,j)-(2,j) and (3,j)-(0,j)):
    (3,1,2) inside : smallest eigenvalue -3.2e-19, largest 1.124e-03   (semidefinite, with the expected zero mode)
    (5,1,2) inside : smallest +2.1e-09,  largest 6.071e-03
    (4,1,1) inside : smallest +2.1e-07,  largest 4.396e-02
    (2,1,2) OUTSIDE: smallest -1.098e-04, largest 9.105e-04            (indefinite)
  4 x 4 torus, the Gram matrix over the 1296 indicators of the column next to the plane (transfer matrices):
    (3,1,2) inside : smallest +1.9e-15, largest 1.158e-03
    (5,1,2) inside : smallest +1.0e-09, largest 1.914e-02
    (4,1,1) inside : smallest +4.7e-09, largest 1.321e-01
    (2,1,2) OUTSIDE: smallest -1.111e-04, largest 9.121e-04
  So reflection positivity through a bond plane holds exactly on the region of (2), on both tori.

READING
  For the block 17 repair: bond-plane reflection positivity is available on p >= q, p + q >= 2r, which on (p, 1, 2) means
  p >= 3 - the chessboard estimate can use it there. But a bond-plane reflection alone does not move a bond onto every other
  bond: it reaches half of them, in 2D and in 3D alike. A chessboard argument that needs transitivity on bonds has to use
  both reflection families, and the site-plane family reaches only a half (2D) or a quarter (3D) by itself.
