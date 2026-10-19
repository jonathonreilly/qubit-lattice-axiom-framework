"""Phase C helper: run the AUTHOR's c4e_02 matching (source text executed in memory, file untouched)
with two in-memory patches: (1) record one witness image d for every orbit edge; (2) write the JSON
into review_scripts/logs instead of the author's logs directory. Then dump the matching
(source rep -> witness image) for the reviewer's independent global verifier (rv_matching_verify.py).
"""
import os, sys, json
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'scripts', 'c4e_02_k3_matching.py')
src = open(SRC).read()
a = "            E.add(tindex[kd])"
assert src.count(a) == 1
src = src.replace(a, a + "\n            WIT.setdefault((i, tindex[kd]), d); ALLC.append((i, tindex[kd], sorted(d)))")
b = "rows, cols = [], []"
assert src.count(b) == 1
src = src.replace(b, b + "\nWIT = {}\nALLC = []")
c = "open(os.path.join(os.path.dirname(__file__), '..', 'logs', 'c4e_02_k3_data_s%d.json' % s), 'w')"
assert src.count(c) == 1
src = src.replace(c, "open(os.path.join(%r, 'logs', 'author_c4e_02_rerun2_s%%d.json' %% s), 'w')" % HERE)
sys.argv = [SRC, '-1']
g = {'__file__': os.path.abspath(SRC), '__name__': '__main__'}
exec(compile(src, SRC, 'exec'), g)
match = g['match']; C3 = g['C3']; WIT = g['WIT']
json.dump({'C3': [sorted(c) for c in C3], 'tkeys_n': len(g['tkeys']), 'cands': g['ALLC']},
          open(os.path.join(HERE, 'logs', 'candidates_s-1.json'), 'w'))
print('dumped candidates', len(g['ALLC']))
out = []
for i, j in enumerate(match):
    j = int(j)
    out.append({'src': sorted(C3[i]), 'img': sorted(WIT[(i, j)])})
pass
print('dumped', len(out))
