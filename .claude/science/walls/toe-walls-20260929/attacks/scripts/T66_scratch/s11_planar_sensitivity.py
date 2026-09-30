# Sensitivity control: matched planar system must FAIL if a continuum target is deliberately wrong.
import copy
from fractions import Fraction as F
import refs, solve2
base = copy.deepcopy(refs.REF)
def run(tag):
    r, _ = solve2.run(1, verbose=False)
    print(tag, "float_resid=%.2e" % r['float_resid'], "mod_consistent", r['mod'][2])
run("correct targets      ")
# wrong G2 transport (P_yy h_yy' coefficient doubled)
refs.REF['G2'] = [(c * 2 if (len(sl) == 3 and (('P', 1), 0) in sl and (('h', 1), 1) in sl) else c, sl) for c, sl in base['G2']]
solve2.REF = refs.REF
run("G2 transport doubled ")
refs.REF['G2'] = base['G2']
# wrong xi1 sign
refs.REF['xi1'] = [(-c, sl) for c, sl in base['xi1']]
solve2.REF = refs.REF
run("xi1 sign flipped     ")
refs.REF['xi1'] = base['xi1']
# wrong T3 (scaled 3/2)
refs.REF['T3'] = [(c * F(3, 2), sl) for c, sl in base['T3']]
solve2.REF = refs.REF
run("T3 x 3/2             ")
