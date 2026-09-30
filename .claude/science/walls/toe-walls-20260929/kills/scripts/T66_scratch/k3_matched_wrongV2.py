"""Kill check: in the ADM-matched planar system, replace the potential (V2 target and V2[1] normalisation) by a wrong one
while keeping the ADM T3, G2, xi1 targets. If the system stays consistent, the matched test does not tie the potential to the rest."""
import sys, copy
from fractions import Fraction as F
import refs, solve, solve2, model
from model import V, XX, YY, ZZ

R = int(sys.argv[1]) if len(sys.argv) > 1 else 1
base_REF = copy.deepcopy(refs.REF)
R2_true = model.R2_S1()

def mass_norm(lam):
    def f():
        out = dict(R2_true)
        key = tuple(sorted([V('h', YY, 0), V('h', ZZ, 0)]))
        out[key] = out.get(key, F(0)) + lam
        return out
    return f

def run(tag, refV2, norm):
    refs.REF['V2'] = refV2
    solve.R2_S1 = norm
    solve2.REF = refs.REF
    r, _ = solve2.run(R, verbose=False)
    print(f"R={R} {tag:34s} float_resid={r['float_resid']:.2e} modOK={r['mod'][2]} (rows {r['rows_identity']}+{r['rows_match']}, cols {r['cols']})", flush=True)

run('correct', base_REF['V2'], lambda: R2_true)
# wrong potential: add lam * N h_yy h_zz (D=0 mass-like) to target
slots = [(('N', 0), 0), (('h', 1), 0), (('h', 2), 0)]
for lam in (F(1, 10), F(1)):
    run(f'V2 + {lam} N h_yy h_zz mass', base_REF['V2'] + [(lam, slots)], mass_norm(lam))
# wrong potential: sign of the cross term flipped
run('V2 sign flipped', [(-c, sl) for c, sl in base_REF['V2']], lambda: {k: -v for k, v in R2_true.items()})
# wrong potential scaled by 2 (T3,G2,xi1 fixed at ADM)
run('V2 x2', [(2*c, sl) for c, sl in base_REF['V2']], lambda: {k: 2*v for k, v in R2_true.items()})
