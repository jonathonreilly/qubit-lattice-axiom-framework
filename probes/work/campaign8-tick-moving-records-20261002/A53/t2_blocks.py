"""A53 t2_blocks: restricted-rule singlet ground-state energy per site of open blocks, for several A51 rules.
For tilings by translates of these blocks no star four-set splits 2+2 (enumerated in t2_prod: n_inter_terms = 0 for
211/221/222/223/224/233), so this IS the exact block-product energy per site.  Also the 2-block interface gain
dE = E(2x2x4) - 2 E(2x2x2) (total), used for a rough dressed-cube estimate (ARGUED, not a bound).
Usage: t2_blocks.py RULES(L:KEY,...) BLOCKS(222,...)"""
import sys, signal, time, numpy as np
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
from t2_prod import lowest_singlets
t0 = time.time()
rules = [(int(r.split(":")[0]), r.split(":")[1]) for r in sys.argv[1].split(",")]
blocks = [tuple(int(c) for c in b) for b in sys.argv[2].split(",")]
for L, key in rules:
    ks, J, c4 = load_rule(L, key); res = {}
    for B in blocks:
        loc = [np.array(o) for o in itertools.product(*[range(b) for b in B])]; n = len(loc); fo = open_index(loc)
        sing, S, _ = lowest_singlets(bilinear_pairs(loc, fo, ks, J), four_sets(loc, fo, c4), n)
        res[B] = sing[0][0]
        print(f"rule L{L} {key}: block {B} (n={n}, sector {S.D}): E/N {sing[0][0]/n:+.6f}  [{time.time()-t0:.0f}s]", flush=True)
    if (2, 2, 2) in res and (2, 2, 4) in res:
        dE = res[(2, 2, 4)] - 2 * res[(2, 2, 2)]
        print(f"   interface gain (2x2x4 - 2 cubes) {dE:+.4f}; dressed-cube estimate E(222)/8 + 3 dE/8 = {res[(2,2,2)]/8 + 3*dE/8:+.5f} (ARGUED)")
