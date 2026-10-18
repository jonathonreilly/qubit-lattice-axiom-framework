"""Signed period of the four range-2 axis/full solutions: alpha^2 on X_0, Z_0 with phases."""
from rv_common import mul, translate
from rv_classify import classify
from rv_linear import decode
PASS = FAIL = 0
sites, vecs, d = classify(2, 'full')
for k, v in enumerate(vecs):
    PX, PZ = decode(v, sites)
    img = {'X': (0, PX), 'Z': (0, PZ)}
    img['Y'] = mul(mul((1, {}), img['X']), img['Z'])
    def alpha(P):
        out = (P[0], {})
        for r, a in P[1].items():
            out = mul(out, translate(img[a], r))
        return out
    a2 = [alpha(img[a]) for a in ('X', 'Z')]
    ok = a2[0] == (0, {(0,0,0): 'X'}) and a2[1] == (0, {(0,0,0): 'Z'})
    print(('PASS' if ok else 'FAIL'), f'solution {k} (|supp X-image|={len(PX)}): alpha^2 = id with phases', flush=True)
    PASS += ok; FAIL += (not ok)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
