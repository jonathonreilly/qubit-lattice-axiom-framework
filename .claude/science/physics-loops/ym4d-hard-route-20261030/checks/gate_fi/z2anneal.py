#!/usr/bin/env python3
"""Discrete search, registered as an addition before its first run. Gradients cannot move a sign, and majority flips of the two normalised means are exactly the mechanism by which a vortex of area below L^2 could flip W.
Field: links in {+1, -1} on the box, times fixed noise of size 1e-7 that breaks exact ties in the means (those fields are legitimate, f ~ 1e-7 is not rough). Score: Ratio_C, rule map, regime R1. Ratio_C > 1 needs W far from 1 with fewer than L^2 vortex plaquettes.
Metropolis on log Ratio_C at low temperature. Moves: flip one link; flip all links of a 2 x 2 x 2 patch of a random axis hyperplane; flip a line of links. Starts: centre sheet, interior sheet, half-cut.
PASS-Z2: best Ratio_C <= 1.05 is NULL for this family. Above 1.05: ABOVE-ONE, verified by the old map at L = 3, 5."""
import json, math, pathlib, sys, time
import numpy as np, torch
import fi_map as fm
HERE = pathlib.Path(__file__).resolve().parent
L = int(sys.argv[1]); steps = int(sys.argv[2]); eps = 0.02 / L ** 2; srule = 0.02
rng = np.random.default_rng(100 + L)

def signs(name):
    S = [np.ones(u.shape[:-1]) for u in fm.flat_links(L)]; o = (L - 1) // 2
    if name == "sheet":
        S[0][L - 1, L:] = -1
    elif name == "sheet_int":
        S[0][o, o:] = -1
    elif name == "sheet_off":                    # vortex off centre, where the linear weight is below 1 and only the majority helps
        S[0][o + 1, o + 1:] = -1
    return S

g = torch.Generator().manual_seed(L)
NZ = []
for u in fm.flat_links(L):
    v = torch.randn(*u.shape[:-1], 3, generator=g) * 1e-7
    NZ.append(torch.cat((torch.ones(*u.shape[:-1], 1), v), -1))

def score(S):
    U = [torch.from_numpy(s)[..., None] * n for s, n in zip(S, NZ)]
    U = [u / u.norm(dim=-1, keepdim=True) for u in U]
    return fm.evaluate(U, L, eps, srule)

for name in ("sheet", "sheet_int", "sheet_off"):
    S = signs(name); e = score(S); cur = e["ratio_c"]; best = cur; bestA = e["nrough"]; t0 = time.time(); acc = 0
    print(name, "start", round(cur, 4), "w1", round(e["w1"], 3), "A", e["nrough"], flush=True)
    for it in range(steps):
        mu = int(rng.integers(4)); sh = S[mu].shape; T = 0.03
        kind = rng.random()
        if kind < 0.5:
            sl = tuple(int(rng.integers(n)) for n in sh)
        elif kind < 0.8:
            lo = [int(rng.integers(n)) for n in sh]
            sl = tuple(slice(l, l + 2) if i != mu else l for i, l in enumerate(lo))
        else:
            lo = [int(rng.integers(n)) for n in sh]; ax = int(rng.integers(4))
            sl = list(lo); sl[ax] = slice(None); sl[mu] = lo[mu]; sl = tuple(sl)
        S[mu][sl] *= -1
        e = score(S); new = e["ratio_c"]
        if new > 0 and (new >= cur or rng.random() < math.exp((math.log(new) - math.log(max(cur, 1e-9))) / T)):
            cur = new; acc += 1
            if new > best:
                best = new; bestA = e["nrough"]
                np.savez_compressed(HERE / f"z2best_L{L}.npz", **{f"S{i}": s.astype(np.int8) for i, s in enumerate(S)})
        else:
            S[mu][sl] *= -1
    rec = dict(L=L, start=name, steps=steps, best=best, A=bestA, final=cur, acc=acc, secs=round(time.time() - t0, 1))
    print(json.dumps(rec), flush=True)
    with open(HERE / "z2anneal.jsonl", "a") as fh:
        fh.write(json.dumps(rec) + "\n")
