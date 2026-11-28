"""GUIDE only (row 836): more flat shapes with the heuristic F of blockwalk3."""
import itertools, sys
from blockwalk3 import threshold
def box(s):
    return [tuple(c) for c in itertools.product(*[range(k) for k in s])]
shapes = {"sq4": box((4,4,1,1)), "box332": box((3,3,2,1)), "rect4x2": box((4,2,1,1))}
for name in sys.argv[1:]:
    print(name, *threshold(shapes[name]), flush=True)
