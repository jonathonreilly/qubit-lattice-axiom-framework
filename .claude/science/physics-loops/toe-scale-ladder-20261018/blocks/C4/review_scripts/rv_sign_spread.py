"""How many of the 84 nonconstant-tau matrices admit a covariant phase choice under the sign action."""
from rv_classify import classify, signed_ok
from rv_linear import decode
sites, vecs, d = classify(1, 'sign')
n = nv = 0
for v in vecs:
    PX, PZ = decode(v, sites)
    tX = {r for r, a in PX.items() if a in 'XY'}; tZ = {r for r, a in PZ.items() if a in 'ZY'}
    tau = tX ^ tZ
    if tau <= {(0, 0, 0)}: continue
    n += 1
    nv += any(signed_ok(PX, PZ, sx, sz, 'sign') for sx in (1, -1) for sz in (1, -1))
print(f'sign action: nonconstant-tau unsigned={n}, with a valid phase choice={nv}')
ok = n == 84
print(f'TOTAL: PASS={int(ok)} FAIL={int(not ok)}')
