"""Cycle 729 of the emergent-geometry lane: the block's adjacency cost is exactly [216, 320].

The lane's object is a 2 by 1 by 1 spatial block of the Z^3 lattice carried through one
tick, so a 3 by 2 by 2 by 2 array of 24 corners.  Its four-volume is 2, a minimal piece has
volume 1/24, so every minimal-volume dissection uses exactly 48 pieces.  The adjacency
charge of a piece counts the corner pairs whose spatial separation exceeds one lattice
step, and the cost of a dissection is the total over its pieces.

Charging every piece its least or its greatest adjacency gives only the interval 144 to
432.  This cycle replaces both ends by exact values, with an integer certificate and an
exhibited dissection at each end, and no solver anywhere in the artifact.

  FLOOR  216, certificate at denominator 512, attained by the stacked monotone stencil.
  CEILING 320, certificate at denominator 49, attained by a 48-piece dissection built here.

The certificate inequality is one line.  Fix an integer weight u_o for every orbit of
sample points and one integer Z.  If

    sum_o M[p][o] u_o + Z  <=  D * adjacency(p)

holds for every minimal piece p, then summing over the 48 pieces of any dissection gives
16 * sum(u) + 48 * Z <= D * cost, because the sample points are group-closed with 16 per
orbit and no sample point lies on a piece boundary, so each point is interior to exactly
one piece of any dissection.  The same statement with the inequality reversed bounds the
cost above.  Nothing in the argument assumes the dissection is symmetric; the symmetry is
used only to compress the program from 17280 rows to 1080.

Two readings from cycle 728 are corrected here, both in the direction of a sharper result.

  Its best dissection cost 318 and its certified ceiling was 324.  The window shuts at 320:
  a dissection of cost 320 is exhibited, and a certificate rules out 321.

  Its boundary paragraph said sharpening the ceiling would need a certificate of a
  different shape rather than a larger denominator.  That is wrong for denominators from 49
  upward, and the certificate embedded here is the constructive demonstration.  The
  arithmetic slipped: the bound is the integer part of value over D, so a fixed gap of 48
  between the value and 320 D stops mattering as soon as D exceeds 48.

The last section explains why cycle 728's search stopped where it did.  A dissection that
is the set of lower faces of a lifted polytope is face-to-face, because lower faces of a
polytope meet in common faces.  The stencil and cycle 728's own best dissection both carry
an explicit integer height, so both are lower hulls.  The cost-320 dissection has facets
carried by exactly one piece and away from the boundary of the box, so it is not
face-to-face and no lift produces it.  Cycle 728 generated candidates as lower hulls, so
the dearest dissection was outside its search space by construction, not by bad luck.

Not being face-to-face is ordinary here and carries no soundness cost: the exact-cover
proof uses volume, pairwise disjointness by exhibited integer normals, and containment of
every sample point, and never uses a face-to-face hypothesis.
"""
import itertools
from collections import Counter

import numpy as np

PAIRS = list(itertools.combinations(range(5), 2))
OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
NP = [0, 0]

FLOOR_U = [-1081, 2, 1, -373, 0, 0, 503, 1, 0, 648, 0, 1055, 0, -522, -20, 0, -416, 386, 0,
           -687, 0, 1, 0, 169, 0, 0, 0, 0, 0, 0, 0, 0, -415, -500, -292, 4, 2548, 2, 0, 7,
           0, 0, 0, 417, 0, 0, 0, 0, 0, 0, 0, 0, 151, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -537, 0, 865, -1074, 0, 0, 0,
           679, 0, 0, 0, -179, 0, 0, 0, 2, 0, 0, -1183, 73, 0, 0, -63, 0, 0, 1397, 0, 0, 0,
           0, 140, 0, 1743, 0, 0, 0, 0, 0, 0, 0, -260, 0, 0, 427, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 2823, 0, 0, 0, 0, 0, 0, 0, 1745, 0, 0, 0, 0, 0, 0, -2661, 0, 0, 0, 0,
           0, 0, 0, 681, 0, 0, 0, 0, 0, 0, -747, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           -2050, 0, 0, -278, 4, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, -1480, 0, 0, -1158, 0, 0,
           0, 0, 818, 0, 0, 1937, 0, 0, 0, 3, 0, 0, 0, 1, 0, 1726, 0, 0, 0, 0, 0, 0, 145, 0,
           0, 0, 0, 0, 0, 0, 0, -966, 0, 0, 236, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -234, 0, 0, 0, 0,
           -459, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -448, 0, 672, 136, 0, 235, 0, 342, 0,
           0, 0, 0, 0, 0, 783, 731, 18, 29, 0, 0, 0, 0, 0, 334, 1565, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, -334, 0, 0, 0, 0, -664, 0, -1407, 0, -1627, 1983, 0, 0, 0, 0, 0, 0, 0,
           0, -594, -760, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1213, -1277,
           0, -420, 323, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -329, -489, 0, 0, 0,
           0, 0, 0, 1031, 0, 0, 0, 0, 987, 0, 0, 0, 0, 0, -1463, 0, 308, 0, -41, -321, 0,
           -41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -359, -38, 0, 65, 0, 581, 398, -1086,
           0, 243, 1366, 0, 0, 0, 0, 0, -1211, 0, 0, 0, 0, 0, -1191, 0, 0, 0, 0, 0, 0, 0,
           -300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3138, 0,
           0, 0, 0, 2733, 0, 0, -144, 0, 0, 687, 0, 0, 0, -2049, 1241, 0, 0, 0, 0, 0, -3118,
           0, 0, 0, 0, 0, 0, 0, 0, -65, -1569, 0, 0, 0, 0, 1048, 0, 0, 0, 0, 0, 0, -493, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 526, 0, -1006, 0, 0, 0, 0, 0, 0, -179, 0, 0, -1196, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -346, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -886, 0, 1, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -97, 0, 0, 0, 0, 0, 0, -588, 0, -558, 0, 0, 689, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 257, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -258, 639, 0,
           -1067, 0, 0, 0, 847, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 278, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -347, 0, 0, 1830, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -654, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 1126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 602, 0, 0, 0, 0, 0, 0, 0,
           -875, 0, 0, 0, 0, 0, 0, 1172, 0, 0, 1096, 0, 0, 0, 0, -367, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1841, 0, 0, 0, 0, 0, 791, 0, 0, 0, 0, 0, 0, 0, 0,
           -2543, 0, 0, 0, 0, 0, 0, -645, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -662, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1748,
           -962, 0, 0, 1038, 0, -983, 0, 0, 0, 0, -1857, 0, -2560, 0, 0, 0, -103, -703, 0,
           136, 0, 0, 0, 0, 0, 1740, 0, 0, -365, 0, 0, -390, 0, 0, 0, 746, 0, 0, 741, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 2038, 0, 0, 0, 0, 1018, -877, 0, 0, 0, 1294, -2357, 0, 0, 0,
           0, 0, 0, 0, 0, 0, -768, 0, -1519, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, -1393, 0, 0, 0, 0, -742, 0, -34, 0, 0, 0, 0, 0, 0, 0, 0, -346, 0, 0, 0, 0, 0,
           0, -624, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 926, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 1889, 0, -1008, 0, 2370, 0, 0, 0, 0, 0, 0, 0]
FLOOR_VAL = 110144
FLOOR_Z = 1752
FLOOR_D = 512
CEIL_U = [90, 0, 0, 64, 0, 0, 6, 0, 0, 0, 0, 26, 0, 23, -35, 0, 151, -153, 0, -194, 0, 0, 0,
          62, 0, 0, 0, 0, 0, 0, 0, 0, -272, 213, 62, 0, -126, 0, 0, 0, 0, 0, 0, 63, 0, 0, 0,
          0, 0, 0, 0, 0, 282, 0, 0, 0, 0, -205, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 113, 0, -132, -41, 0, 0, 0, 90, 0, 0, 0, 152, 0, 0, 0,
          0, 0, 0, 69, 286, 0, 0, -33, 0, 0, -166, 0, 0, 0, 0, 205, 0, -113, 0, 0, 0, 0, 0,
          0, 0, 97, 0, 0, 168, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -175, 0, 0, 0, 0, 0,
          0, 0, -90, 0, 0, 0, 0, 0, 0, 122, 0, 0, 0, 0, 0, 0, 0, 82, 0, 0, 0, 0, 0, 0, 42,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 88, 0, 0, -19, 0, 0, 0, 0, -75, 0, 0, 84, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          -139, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 105, 0, 0, -111, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 206, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -246, 0, 106,
          96, 0, -79, 0, -22, 0, 0, 0, 0, 0, 0, 82, -144, 31, -321, 0, 0, 0, 0, 0, 37, 5, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 126, 0, 0, 0, 0, -28, 0, 110, 0, 189, -74, 0, 0, 0, 0,
          0, 0, 0, 0, -43, -17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51,
          -145, 0, 74, -18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 22, 0, 0, 0, 0,
          0, 0, -94, 0, 0, 0, 0, -6, 0, 0, 0, 0, 0, -16, 0, 111, 0, -241, -41, 0, -51, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -27, 129, 0, 13, 0, -201, -103, -34, 0, -50,
          -115, 0, 0, 0, 0, 0, -155, 0, 0, 0, 0, 0, -29, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -90, 0, 0, 0, 0, -88, 0, 0,
          204, 0, 0, 32, 0, 0, 0, 89, -200, 0, 0, 0, 0, 0, -46, 0, 0, 0, 0, 0, 0, 0, 0, -61,
          105, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 69, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 211,
          0, 0, 0, 0, 0, 0, -260, 0, 0, 79, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, -53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, -124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -96, 0, 0, 0, 0,
          0, 0, -24, 0, -92, 0, 0, 194, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -75, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, -212, 15, 0, 23, 0, 0, 0, -41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 169, 0, 0, -74, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 89, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, -40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0,
          0, 0, 7, 0, 0, 0, 0, 0, 0, 213, 0, 0, 59, 0, 0, 0, 0, -101, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -150, 0, 0, 0, 0, 0, -9, 0, 0, 0, 0, 0, 0, 0, 0, 13,
          0, 0, 0, 0, 0, 0, -40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -155, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 166, -67, 0, 0,
          -6, 0, 29, 0, 0, 0, 0, -17, 0, 104, 0, 0, 0, 175, 64, 0, -30, 0, 0, 0, 0, 0, 65,
          0, 0, 91, 0, 0, 40, 0, 0, 0, 62, 0, 0, -63, 0, 0, 0, 0, 0, 0, 0, 0, 0, -50, 0, 0,
          0, 0, -23, 40, 0, 0, 0, 3, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, -20, 0, 15, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 130, 0, 0, 0, 0, 137, 0, 272, 0, 0, 0, 0,
          0, 0, 0, 0, -74, 0, 0, 0, 0, 0, 0, -92, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -188, 0, -130, 0, -127, 0, 0, 0, 0, 0,
          0, 0]
CEIL_VAL = 15728
CEIL_Z = 189
CEIL_D = 49
DEAR = [[11, 17, 18, 19, 23], [12, 16, 20, 21, 22], [0, 1, 2, 5, 9], [2, 5, 6, 7, 14], [0,
        2, 4, 5, 14], [2, 3, 5, 7, 9], [10, 16, 17, 21, 22], [13, 17, 18, 22, 23], [0, 4, 5,
        8, 14], [2, 3, 7, 9, 15], [10, 13, 16, 17, 21], [10, 13, 18, 22, 23], [1, 2, 3, 5,
        9], [2, 4, 5, 6, 14], [10, 16, 17, 18, 22], [13, 17, 21, 22, 23], [2, 3, 11, 17,
        23], [4, 5, 12, 16, 22], [2, 5, 9, 16, 17], [2, 5, 14, 22, 23], [2, 3, 9, 15, 17],
        [4, 5, 8, 14, 22], [2, 10, 13, 16, 17], [5, 10, 13, 22, 23], [2, 3, 15, 17, 23], [4,
        5, 8, 16, 22], [2, 5, 10, 22, 23], [2, 5, 13, 16, 17], [0, 2, 5, 8, 9], [2, 5, 7,
        14, 15], [0, 2, 5, 8, 14], [2, 5, 7, 9, 15], [10, 11, 17, 18, 23], [12, 13, 16, 21,
        22], [10, 13, 16, 21, 22], [10, 13, 17, 18, 23], [2, 5, 8, 16, 22], [2, 5, 15, 17,
        23], [2, 10, 11, 17, 23], [5, 12, 13, 16, 22], [2, 10, 13, 16, 22], [5, 10, 13, 17,
        23], [2, 5, 10, 17, 23], [2, 5, 13, 16, 22], [2, 5, 8, 9, 16], [2, 5, 14, 15, 23],
        [2, 5, 8, 14, 22], [2, 5, 9, 15, 17]]
PRIOR = [[0, 1, 3, 7, 10], [0, 1, 4, 7, 12], [0, 1, 7, 8, 18], [0, 1, 7, 8, 20], [0, 1, 7,
         10, 18], [0, 1, 7, 12, 20], [0, 2, 3, 7, 10], [0, 2, 6, 7, 10], [0, 4, 6, 7, 10],
         [0, 4, 7, 10, 12], [0, 7, 8, 18, 20], [0, 7, 10, 12, 20], [0, 7, 10, 18, 20], [1,
         3, 7, 10, 18], [1, 3, 7, 11, 18], [1, 4, 5, 7, 12], [1, 5, 7, 12, 20], [1, 5, 7,
         13, 20], [1, 7, 8, 16, 18], [1, 7, 8, 16, 20], [1, 7, 11, 16, 18], [1, 7, 11, 16,
         20], [1, 7, 11, 19, 20], [1, 7, 13, 20, 21], [1, 7, 15, 19, 20], [1, 7, 15, 20,
         21], [1, 9, 15, 19, 20], [1, 9, 15, 20, 21], [1, 9, 16, 19, 20], [1, 11, 16, 19,
         20], [4, 6, 7, 10, 12], [6, 7, 10, 12, 20], [6, 7, 10, 18, 20], [6, 7, 14, 18, 20],
         [7, 8, 16, 18, 20], [7, 11, 16, 18, 20], [7, 11, 18, 19, 20], [7, 14, 15, 18, 20],
         [7, 15, 18, 19, 20], [9, 15, 17, 19, 20], [9, 15, 17, 20, 21], [9, 16, 17, 19, 20],
         [11, 16, 18, 19, 20], [14, 15, 18, 20, 22], [15, 17, 19, 20, 21], [15, 18, 19, 20,
         23], [15, 18, 20, 22, 23], [15, 19, 20, 21, 23]]
HGT_LO = [80, 96, 96, 96, 96, 96, 96, 80, 56, 56, 56, 40, 56, 40, 40, 8, 96, 80, 80, 48, 80,
          48, 48, 0]
HGT_PR = [704, 448, 704, 352, 704, 704, 672, 0, 560, 560, 400, 208, 464, 688, 528, 80, 448,
          704, 224, 256, 256, 704, 704, 288]


def gate(ok, name, detail):
    NP[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail)


def sec(text):
    print(text)


def det4(A):
    """exact integer determinants of a batch of 4 by 4 integer matrices"""
    def minors(r0, r1):
        out = {}
        for i in range(4):
            for j in range(i + 1, 4):
                out[(i, j)] = (A[:, r0, i] * A[:, r1, j]
                               - A[:, r0, j] * A[:, r1, i])
        return out
    m = minors(0, 1)
    c = minors(2, 3)
    return (m[(0, 1)] * c[(2, 3)] - m[(0, 2)] * c[(1, 3)] + m[(0, 3)] * c[(1, 2)]
            + m[(1, 2)] * c[(0, 3)] - m[(1, 3)] * c[(0, 2)] + m[(2, 3)] * c[(0, 1)])


def volumes(V, P):
    A = V[P[:, 1:]] - V[P[:, 0]][:, None, :]
    return np.abs(det4(A))


def census(V):
    subs = np.array(list(itertools.combinations(range(len(V)), 5)), dtype=np.int64)
    return subs, volumes(V, subs)


def charge(V, P, cols):
    tot = np.zeros(len(P), dtype=np.int64)
    for a, b in PAIRS:
        d = np.abs(V[P[:, a]][:, cols] - V[P[:, b]][:, cols]).sum(axis=1)
        tot = tot + (d > 1).astype(np.int64)
    return tot


def inverses(V, P):
    MM = np.stack([(V[p[1:]] - V[p[0]]).T for p in P])
    IV = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)
    eye = np.eye(4, dtype=np.int64)
    exact = bool((np.einsum("nij,njk->nik", IV, MM) == eye).all())
    return IV, exact


def bary_bound(V, P, IV):
    L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[P[:, 0]][:, None, :])
    return max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))


def weights(cmax):
    base = cmax * int(OFF.sum()) + 1
    w = 2 * (base + OFF)
    return w, int(w.sum())


ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if int(round(np.linalg.det(R.astype(float)))) == 1:
            ROT.append(R)


def group(corners, pos, cen2):
    keep = []
    out = []
    for R in ROT:
        good = False
        for tf in (0, 1):
            img = []
            for (x, y, z, t) in corners:
                w = R @ (2 * np.array([x, y, z], dtype=np.int64) - cen2) + cen2
                if bool((w & 1).any()):
                    img = None
                    break
                key = (int(w[0]) // 2, int(w[1]) // 2, int(w[2]) // 2,
                       (1 - t) if tf else t)
                if key not in pos:
                    img = None
                    break
                img.append(pos[key])
            if img is not None:
                out.append((R, tf, np.array(img, dtype=np.int64)))
                good = True
        if good:
            keep.append(R)
    return keep, out


def orbits(P, G):
    posp = dict((tuple(int(c) for c in s), i) for i, s in enumerate(P))
    lab = -np.ones(len(P), dtype=np.int64)
    reps = []
    for i in range(len(P)):
        if lab[i] >= 0:
            continue
        o = len(reps)
        reps.append(i)
        for (_, _, g) in G:
            lab[posp[tuple(sorted(int(g[c]) for c in P[i]))]] = o
    return lab, np.array(reps, dtype=np.int64)


def constant_on_orbits(lab, n_orb, vals):
    order = np.argsort(lab, kind="stable")
    bnd = np.searchsorted(lab[order], np.arange(n_orb + 1))
    for o in range(n_orb):
        blk = vals[order[bnd[o]:bnd[o + 1]]]
        if int(blk.max()) != int(blk.min()):
            return False
    return True


def points(V, P, G, reps, w, s, sc):
    lab = {}
    for o, i in enumerate(reps):
        q = (w[:, None] * V[P[i]]).sum(axis=0)
        for (R, tf, _) in G:
            u = R @ (q[:3] - sc) + sc
            key = (int(u[0]), int(u[1]), int(u[2]),
                   (s - int(q[3])) if tf else int(q[3]))
            if lab.setdefault(key, o) != o:
                return None, None
    keys = sorted(lab)
    return (np.array(keys, dtype=np.int64),
            np.array([lab[k] for k in keys], dtype=np.int64))


def membership(V, P, IV, Q, porb, n_orb, s):
    M = np.zeros((len(P), n_orb), dtype=np.int16)
    QT = Q.T
    bad = 0
    for i in range(len(P)):
        lam = IV[i] @ (QT - (s * V[P[i, 0]])[:, None])
        tot = lam.sum(axis=0)
        bad += int(((lam == 0).any(axis=0) | (tot == s)).sum())
        ins = (lam > 0).all(axis=0) & (tot < s)
        M[i] = np.bincount(porb[ins], minlength=n_orb)
    return M, bad


NEG = [np.array(t, dtype=np.int64)
       for t in itertools.product((-1, 0, 1), repeat=4) if any(t)]


def separated(V, P):
    pts = [V[p] for p in P]
    fac = []
    for p in P:
        MM = (V[p[1:]] - V[p[0]]).T
        Iv = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)
        fac.append([Iv[k] for k in range(4)] + [-Iv.sum(axis=0)])
    good = 0
    total = 0
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            total += 1
            for nv in NEG + fac[i] + fac[j]:
                a = pts[i] @ nv
                b = pts[j] @ nv
                if int(a.max()) <= int(b.min()) or int(b.max()) <= int(a.min()):
                    good += 1
                    break
    return good, total


def kuhn(base, pos):
    out = []
    for perm in itertools.permutations(range(4)):
        v = list(base)
        path = [tuple(v)]
        for c in perm:
            v[c] += 1
            path.append(tuple(v))
        out.append(tuple(sorted(pos[p] for p in path)))
    return sorted(out)


def verify(M, ch, u, Z, D, upper):
    """the certificate check, in integers, over every row of M"""
    worst = None
    tight = 0
    lo = 0
    while lo < len(M):
        hi = min(lo + 4096, len(M))
        s = (M[lo:hi].astype(np.int64) @ u + Z) - D * ch[lo:hi]
        if not upper:
            s = -s
        w = int(s.min())
        worst = w if worst is None else min(worst, w)
        tight += int((s == 0).sum())
        lo = hi
    return worst, tight


def bump(M, ch, u, Z, D, upper):
    """move one weight the wrong way against a row the certificate holds tight"""
    s = (M @ u + Z) - D * ch
    if not upper:
        s = -s
    r = int(np.argmin(s))
    o = int(np.nonzero(M[r] > 0)[0][0])
    v = u.copy()
    v[o] = v[o] + (-1 if upper else 1)
    return v, o


def facets(V, P, face):
    """facets carried by exactly one piece and not lying on the boundary of the box"""
    fac = Counter()
    for p in P:
        for f in itertools.combinations(sorted(int(c) for c in p), 4):
            fac[f] += 1
    once = [f for f, m in fac.items() if m == 1]
    odd = [f for f in once
           if not any((V[list(f)][:, a] == v).all() for a, v in face)]
    return len(fac), len(once), len(odd)


def lower_rows(V, P):
    """every corner outside a piece must lift strictly above that piece's plane"""
    out = []
    nv = len(V)
    for p in P:
        pv = V[p]
        Iv = np.rint(np.linalg.inv((pv[1:] - pv[0]).T.astype(float))).astype(np.int64)
        ins = set(int(c) for c in p)
        for w in range(nv):
            if w in ins:
                continue
            lam = Iv @ (V[w] - pv[0])
            b = np.zeros(nv, dtype=np.int64)
            b[p[0]] += 1 - int(lam.sum())
            for k in range(4):
                b[p[k + 1]] += int(lam[k])
            b[w] -= 1
            out.append(b)
    return np.array(out, dtype=np.int64)


# ------------------------------------------------- the block and its minimal pieces
CORNB = [(x, y, z, t) for x in range(3) for y in range(2)
         for z in range(2) for t in range(2)]
VB = np.array(CORNB, dtype=np.int64)
POSB = dict((c, i) for i, c in enumerate(CORNB))
FACE = [(0, 0), (0, 2), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]

SUBB, DB = census(VB)
MINB = SUBB[DB == 1]
BX = charge(VB, MINB, [0, 1, 2])
IB, EXB = inverses(VB, MINB)

sec("the block: two lattice cells side by side, carried through one tick")
gate(len(VB) == 24 and int(VB[:, 0].max()) == 2 and int(VB[:, 3].max()) == 1,
     "block corners", "3 by 2 by 2 spatial corners times 2 tick corners is 24")
gate(len(SUBB) == 42504 and int(DB.max()) == 6, "five-subset census",
     "{0} subsets, volume spectrum {1}".format(
         len(SUBB), sorted(Counter(DB.tolist()).items())))
gate(len(MINB) == 17280, "minimal pieces",
     "{0} five-subsets of volume one twenty-fourth".format(len(MINB)))
gate(EXB, "piece inverses are exact integer matrices",
     "all {0} inverse matrices give back the identity".format(len(MINB)))
gate((int(BX.min()), int(BX.max())) == (3, 9), "adjacency charge spectrum",
     str(sorted(Counter(BX.tolist()).items())))
gate(48 * int(BX.min()) == 144 and 48 * int(BX.max()) == 432, "counting bounds",
     "charging all 48 pieces the least or the most gives only 144 to 432")

# ------------------------------------------------- sample points and the inequality
CEN2 = np.array([2, 1, 1], dtype=np.int64)
KEEPB, GB = group(CORNB, POSB, CEN2)
LABB, REPB = orbits(MINB, GB)
NORB = len(REPB)
SZB = np.bincount(LABB, minlength=NORB)
CB = bary_bound(VB, MINB, IB)
WT, SBT = weights(CB)
SC = np.array([SBT, SBT // 2, SBT // 2], dtype=np.int64)
QB, PORBB = points(VB, MINB, GB, REPB, WT, SBT, SC)
MB, BADB = membership(VB, MINB, IB, QB, PORBB, NORB, SBT)
PTSZ = np.bincount(PORBB, minlength=NORB)
BO = MB[REPB].astype(np.int64)
BXO = BX[REPB]
ROWS = len(set(MB[i].tobytes() for i in range(len(MINB))))

sec("sample points, and the certificate inequality they carry")
gate(len(KEEPB) == 8 and len(GB) == 16, "block symmetry",
     "8 proper rotations preserve the block, 16 corner permutations with the tick flip")
gate(NORB == 1080 and int(SZB.min()) == 16 and int(SZB.max()) == 16, "piece orbits",
     "{0} orbits, every one of size 16".format(NORB))
gate(constant_on_orbits(LABB, NORB, BX), "adjacency is constant on every orbit",
     "one charge per orbit, so the program has {0} rows".format(NORB))
gate(CB == 6 and float(WT.max()) / float(WT.min()) < 1.15, "generic weights",
     "barycentric integers bounded by {0}, weight spread under 1.15".format(CB))
gate(QB is not None and len(QB) == 17280 and int(PTSZ.min()) == 16
     and int(PTSZ.max()) == 16, "sample points",
     "{0} distinct points, exactly 16 in every orbit".format(len(QB)))
gate(BADB == 0, "no sample point lands on a piece boundary",
     "boundary incidences {0} over all {1} pieces".format(BADB, len(MINB)))
gate(MB.shape == (len(MINB), NORB) and int(MB.sum(axis=1).min()) > 0
     and ROWS == 1060, "membership matrix",
     "{0} by {1}, {2} distinct rows, none empty".format(
         MB.shape[0], MB.shape[1], ROWS))
gate(bool((BO[LABB] == MB).all()), "membership is constant on every orbit",
     "the {0} orbit rows reproduce all {1} piece rows".format(NORB, len(MINB)))

# ------------------------------------------------- the floor
UFL = np.array(FLOOR_U, dtype=np.int64)
wf, tf = verify(BO, BXO, UFL, FLOOR_Z, FLOOR_D, False)
wfa, _ = verify(MB, BX, UFL, FLOOR_Z, FLOOR_D, False)
vfl = 16 * int(UFL.sum()) + 48 * FLOOR_Z
bfl = -((-vfl) // FLOOR_D)
STEN = np.array(kuhn((0, 0, 0, 0), POSB) + kuhn((1, 0, 0, 0), POSB), dtype=np.int64)
gs, ts = separated(VB, STEN)
CS = int(charge(VB, STEN, [0, 1, 2]).sum())

sec("the floor: 216, certified and attained")
gate(len(UFL) == NORB and wf >= 0, "floor certificate is valid",
     "least slack {0} over all {1} orbit rows, tight on {2}".format(wf, NORB, tf))
gate(wfa == wf, "floor certificate checked on every piece",
     "least slack {0} over all {1} pieces matches the orbit program".format(
         wfa, len(MINB)))
gate(vfl == FLOOR_VAL and bfl == 216, "floor bound",
     "value {0} over denominator {1} rounds up to {2}".format(vfl, FLOOR_D, bfl))
gate(len(STEN) == 48 and int(volumes(VB, STEN).sum()) == 48 and gs == ts,
     "the stacked stencil is a dissection",
     "48 pieces, volumes sum to the box volume, all {0} pairs separated".format(ts))
gate(CS == 216, "the stacked stencil attains the floor",
     "its adjacency cost is {0}".format(CS))

# ------------------------------------------------- the ceiling
UCL = np.array(CEIL_U, dtype=np.int64)
wc, tc = verify(BO, BXO, UCL, CEIL_Z, CEIL_D, True)
wca, _ = verify(MB, BX, UCL, CEIL_Z, CEIL_D, True)
vcl = 16 * int(UCL.sum()) + 48 * CEIL_Z
bcl = vcl // CEIL_D
DEARP = np.array(DEAR, dtype=np.int64)
PRIORP = np.array(PRIOR, dtype=np.int64)
gd, td = separated(VB, DEARP)
CD = int(charge(VB, DEARP, [0, 1, 2]).sum())
gp, tp = separated(VB, PRIORP)
CP = int(charge(VB, PRIORP, [0, 1, 2]).sum())

sec("the ceiling: 320, certified and attained")
gate(len(UCL) == NORB and wc >= 0, "ceiling certificate is valid",
     "least slack {0} over all {1} orbit rows, tight on {2}".format(wc, NORB, tc))
gate(wca == wc, "ceiling certificate checked on every piece",
     "least slack {0} over all {1} pieces matches the orbit program".format(
         wca, len(MINB)))
gate(vcl == CEIL_VAL and bcl == 320, "ceiling bound",
     "value {0} over denominator {1} rounds down to {2}".format(vcl, CEIL_D, bcl))
gate(len(DEARP) == 48 and int(volumes(VB, DEARP).sum()) == 48 and gd == td,
     "the dearest dissection is a dissection",
     "48 pieces, volumes sum to the box volume, all {0} pairs separated".format(td))
gate(CD == 320, "it attains the ceiling", "its adjacency cost is {0}".format(CD))
gate(bfl == CS and bcl == CD, "the interval is pinned at both ends",
     "cost lies in 216 to 320 and both ends are reached")
gate(len(PRIORP) == 48 and gp == tp and CP == 318 and CP < CD,
     "the previously dearest dissection is passed",
     "the earlier witness is a dissection of cost {0}".format(CP))

# ------------------------------------------------- lower hulls
RS, RD, RP = lower_rows(VB, STEN), lower_rows(VB, DEARP), lower_rows(VB, PRIORP)
HS = np.array(HGT_LO, dtype=np.int64)
HP = np.array(HGT_PR, dtype=np.int64)
_, _, ODD_D = facets(VB, DEARP, FACE)
_, _, ODD_S = facets(VB, STEN, FACE)
_, _, ODD_P = facets(VB, PRIORP, FACE)

sec("the dearest dissection is not the lower hull of any lift")
gate(ODD_D > 0, "it is not face-to-face",
     "{0} facets are carried by one piece and lie away from the boundary".format(ODD_D))
gate(int((RS @ HS).max()) <= -1, "the stacked stencil is a lower hull",
     "an integer height clears all {0} lower-face inequalities, worst {1}".format(
         len(RS), int((RS @ HS).max())))
gate(int((RP @ HP).max()) <= -1, "the earlier witness is a lower hull",
     "an integer height clears all {0} lower-face inequalities, worst {1}".format(
         len(RP), int((RP @ HP).max())))
gate(ODD_S == 0 and ODD_P == 0 and CS < CP < CD, "why a lift-based search stops at 318",
     "lifts reach 216 and {0}; the dissection costing {1} is not reachable that way"
     .format(CP, CD))

# ------------------------------------------------- controls
UF2, of2 = bump(BO, BXO, UFL, FLOOR_Z, FLOOR_D, False)
UC2, oc2 = bump(BO, BXO, UCL, CEIL_Z, CEIL_D, True)
wf2, _ = verify(BO, BXO, UF2, FLOOR_Z, FLOOR_D, False)
wc2, _ = verify(BO, BXO, UC2, CEIL_Z, CEIL_D, True)
SSET = set(tuple(int(c) for c in p) for p in DEARP)
ALT = [p for p in STEN if tuple(int(c) for c in p) not in SSET][0]
BADP = DEARP.copy()
BADP[0] = ALT
gb, tb = separated(VB, BADP)
HD = int((RD @ HS).max())

sec("controls: every gate above is made to fail on purpose")
gate(wf2 < 0, "the floor certificate has no slack to give",
     "raising weight {0} by one breaks it, least slack {1}".format(of2, wf2))
gate(wc2 < 0, "the ceiling certificate has no slack to give",
     "lowering weight {0} by one breaks it, least slack {1}".format(oc2, wc2))
gate(gb < tb, "the separation test is not automatic",
     "swapping one piece leaves {0} of {1} pairs separated".format(gb, tb))
gate(HD > -1, "a height is specific to its own dissection",
     "the stencil height fails the dearest dissection's rows, worst {0}".format(HD))
gate(ODD_D > 0 and ODD_S == 0, "the facet count separates the objects",
     "{0} for the dearest dissection against {1} for the stencil".format(ODD_D, ODD_S))

# ------------------------------------------------- computational identities
sec("computational identities")
for k in (2, 3, 5):
    wk, _ = verify(BO, BXO, k * UFL, k * FLOOR_Z, k * FLOOR_D, False)
    vk = 16 * int((k * UFL).sum()) + 48 * k * FLOOR_Z
    gate(wk >= 0 and -((-vk) // (k * FLOOR_D)) == 216, "floor certificate scales by " + str(k),
         "denominator {0} gives the same bound".format(k * FLOOR_D))
for k in (2, 3, 5):
    wk, _ = verify(BO, BXO, k * UCL, k * CEIL_Z, k * CEIL_D, True)
    vk = 16 * int((k * UCL).sum()) + 48 * k * CEIL_Z
    gate(wk >= 0 and vk // (k * CEIL_D) == 320, "ceiling certificate scales by " + str(k),
         "denominator {0} gives the same bound".format(k * CEIL_D))
gate(int(charge(VB, STEN, [3, 1, 2]).sum()) == 216, "the transposed charge agrees at the floor",
     "swapping the long spatial axis for the tick axis leaves the stencil at 216")
RW = int(np.argmin(FLOOR_D * BXO - (BO @ UFL + FLOOR_Z)))
EXACT = FLOOR_D * int(BXO[RW]) - (sum(int(BO[RW, o]) * int(UFL[o])
                                      for o in range(NORB)) + FLOOR_Z)
gate(EXACT == wf, "the arithmetic does not overflow",
     "recomputing the tightest row in unbounded integers gives {0}".format(EXACT))

print("TOTAL: PASS={0} FAIL={1}".format(NP[0], NP[1]))
