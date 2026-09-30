import itertools, math, json
import numpy as np
exec(open('test_T26.py').read().split("# ------------- TEST A")[0])
res = {}
for name, gens in {"Z_i only (translation as doubler phase)": Z,
                   "Z_2 only": [Z[1]], "Z_3 only": [Z[2]], "Z_1 only": [Z[0]],
                   "X_i and Z_i (Pauli group)": X + Z,
                   "Z_i + tau": Z + [tau]}.items():
    S = close(g8, gens)
    S3 = close(g_su3, gens)
    print(f"  {name}: closure(g8) = {S.dim}, closure(su(3)) = {S3.dim}")
    res[name] = (S.dim, S3.dim)
json.dump(res, open('test_T26c_results.json', 'w'), indent=1)
