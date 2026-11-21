#!/usr/bin/env python3
"""z2anneal.py lost the sheet at L >= 5: Ratio has no gradient once W = 1, so the walk fell to Ratio 0 and wandered. Registered before its first run: same fields and moves, but a hard constraint |W - 1| >= 1.9 and energy A = number of rough plaquettes, Metropolis at T = 1.5. Ratio_C is about 2 L^2 / (2 A), so above-one means A < L^2 at W near -1.
Start: the centre sheet and the off-centre sheet. PASS: best A >= L^2, NULL for this family."""
import json, math, pathlib, sys, time
import numpy as np, torch
import fi_map as fm
HERE = pathlib.Path(__file__).resolve().parent
L = int(sys.argv[1]); steps = int(sys.argv[2]); eps = 0.02 / L ** 2; srule = 0.02; T = 1.5
rng = np.random.default_rng(200 + L)
g = torch.Generator().manual_seed(L)
NZ = []
for u in fm.flat_links(L):
    v = torch.randn(*u.shape[:-1], 3, generator=g) * 1e-7
    NZ.append(torch.cat((torch.ones(*u.shape[:-1], 1), v), -1))
def score(S):
    U = [torch.from_numpy(s)[..., None] * n for s, n in zip(S, NZ)]
    U = [u / u.norm(dim=-1, keepdim=True) for u in U]
    return fm.evaluate(U, L, eps, srule)
for name in ("sheet", "sheet_off"):
    o = (L - 1) // 2
    S = [np.ones(u.shape[:-1]) for u in fm.flat_links(L)]
    if name == "sheet":
        S[0][L - 1, L:] = -1
    else:
        S[0][o + 1, o + 1:] = -1
    e = score(S); A = e["nrough"]; best = A; bestr = e["ratio_c"]; acc = 0; t0 = time.time()
    for it in range(steps):
        mu = int(rng.integers(4)); sh = S[mu].shape; k = rng.random()
        lo = [int(rng.integers(n)) for n in sh]
        if k < 0.4:
            sl = tuple(lo)
        elif k < 0.8:
            sl = tuple(slice(l, l + 2) if i != mu else l for i, l in enumerate(lo))
        else:
            ax = int(rng.integers(4)); sl = list(lo); sl[ax] = slice(None); sl[mu] = lo[mu]; sl = tuple(sl)
        S[mu][sl] *= -1
        e = score(S); nA = e["nrough"]
        if e["w1"] >= 1.9 and (nA <= A or rng.random() < math.exp((A - nA) / T)):
            A = nA; acc += 1
            bestr = max(bestr, e["ratio_c"]); best = min(best, A)
        else:
            S[mu][sl] *= -1
    rec = dict(L=L, start=name, steps=steps, best_A=best, L2=L ** 2, best_ratio=bestr, final_A=A, acc=acc, secs=round(time.time() - t0, 1))
    print(json.dumps(rec), flush=True)
    with open(HERE / "z2anneal2.jsonl", "a") as fh:
        fh.write(json.dumps(rec) + "\n")
