"""Kill check: validate the attack's planar bracket engine against an independent torch-autograd Poisson bracket on a periodic ring.
For random unknown monomials (V2, T3 families), compare col_V2 / col_T3 (engine) with the bracket computed by autograd from the functionals."""
import random, itertools
import torch
from fractions import Fraction as F
import engine, model
from model import *

torch.set_default_dtype(torch.float64)
Lr = 11
random.seed(3); torch.manual_seed(3)

def make_cfg():
    cfg = {}
    for kind in ('h', 'P'):
        for c in COMPS:
            cfg[(kind, c)] = torch.randn(Lr, requires_grad=True)
    for kind in ('N', 'M'):
        cfg[(kind, 0)] = torch.randn(Lr)
    return cfg

def eval_dict(d, cfg):
    """sum over translations s of coef * prod var(pos+s); works for engine dicts (canonical monos) with torch or float cfg."""
    tot = 0.0
    for mono, coef in d.items():
        term = None
        for (k, c, p) in mono:
            arr = cfg[(k, c)]
            v = torch.roll(arr, -p)      # v[s] = arr[(s+p) % L]
            term = v if term is None else term * v
        tot = tot + float(coef) * (term.sum() if term is not None else torch.tensor(float(Lr)))
    return tot

def ag_bracket(A, B, cfg):
    """{A,B} = sum dA/dh dB/dP - dA/dP dB/dh via autograd (A,B scalars depending on cfg)."""
    tot = 0.0
    for c in COMPS:
        h, P = cfg[('h', c)], cfg[('P', c)]
        gAh, gAP = torch.autograd.grad(A, [h, P], retain_graph=True, allow_unused=True, create_graph=True)
        gBh, gBP = torch.autograd.grad(B, [h, P], retain_graph=True, allow_unused=True, create_graph=True)
        z = lambda g: torch.zeros(Lr) if g is None else g
        tot = tot + (z(gAh) * z(gBP)).sum() - (z(gAP) * z(gBh)).sum()
    return tot

def check(R, nsamp=6):
    worst = 0.0
    V2m = random.sample(enum_V2(R), nsamp)
    T3m = random.sample(enum_T3(R), nsamp)
    for kind, monos in (('V2', V2m), ('T3', T3m)):
        for m in monos:
            cfg = make_cfg()
            # engine column
            col = col_V2(m) if kind == 'V2' else col_T3(m)
            e = eval_dict(col, cfg)
            # autograd
            if kind == 'V2':
                A1 = eval_dict(T2('N'), cfg); B1 = eval_dict(V2_of(m, 'M'), cfg)
                A2 = eval_dict(V2_of(m, 'N'), cfg); B2 = eval_dict(T2('M'), cfg)
            else:
                A1 = eval_dict(C1('N'), cfg); B1 = eval_dict(T3_of(m, 'M'), cfg)
                A2 = eval_dict(T3_of(m, 'N'), cfg); B2 = eval_dict(C1('M'), cfg)
            a = ag_bracket(A1, B1, cfg) + ag_bracket(A2, B2, cfg)
            err = abs(float(e) - float(a)) / (1 + abs(float(a)))
            worst = max(worst, err)
    return worst

for R in (1, 2, 3):
    print("R", R, "worst rel err engine-vs-autograd:", check(R))

# also degree-1 identity numerically: {C1[N],T2[M]}+{T2[N],C1[M]} = G1[xi0] with a direct ring formula
cfg = make_cfg()
A = eval_dict(C1('N'), cfg); B = eval_dict(T2('M'), cfg); A2 = eval_dict(T2('N'), cfg); B2 = eval_dict(C1('M'), cfg)
lhs = ag_bracket(A, B, cfg) + ag_bracket(A2, B2, cfg)
N_, M_, Px = cfg[('N', 0)], cfg[('M', 0)], cfg[('P', XX)]
xi = 0.25 * (torch.roll(N_, -1) * M_ - N_ * torch.roll(M_, -1))      # xi(n -> n+1), K/(4 alpha) = 1/4
G1 = (2 * Px * (xi - torch.roll(xi, 1))).sum()
print("degree-1 numeric: lhs", float(lhs), " G1[xi0]", float(G1))
