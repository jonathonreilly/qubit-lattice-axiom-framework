"""Validate k7_GC's columns against torch autograd on a ring, then diagnose which {G,C} sector is inconsistent."""
import random, sys
import torch
import numpy as np
from fractions import Fraction as F
import k7_GC as K7
from k7_GC import *
import solve

torch.set_default_dtype(torch.float64)
Lr = 11
random.seed(1); torch.manual_seed(1)

def make_cfg():
    cfg = {}
    for kind in ('h', 'P'):
        for c in COMPS:
            cfg[(kind, c)] = torch.randn(Lr, requires_grad=True)
    for kind in ('N', 'X'):
        cfg[(kind, 0)] = torch.randn(Lr)
    return cfg

def eval_dict(d, cfg):
    tot = 0.0
    for mono, coef in d.items():
        term = None
        for (k, c, p) in mono:
            v = torch.roll(cfg[(k, c)], -p)
            term = v if term is None else term * v
        tot = tot + float(coef) * (term.sum() if term is not None else torch.tensor(float(Lr)))
    return tot

def ag(A, B, cfg):
    tot = 0.0
    for c in COMPS:
        h, P = cfg[('h', c)], cfg[('P', c)]
        gAh, gAP = torch.autograd.grad(A, [h, P], retain_graph=True, allow_unused=True, create_graph=True)
        gBh, gBP = torch.autograd.grad(B, [h, P], retain_graph=True, allow_unused=True, create_graph=True)
        z = lambda g: torch.zeros(Lr) if g is None else g
        tot = tot + (z(gAh) * z(gBP)).sum() - (z(gAP) * z(gBh)).sum()
    return tot

R = 2
worst = 0
def rel(e, a): return abs(float(e.detach() if hasattr(e,'detach') else e) - float(a.detach() if hasattr(a,'detach') else a)) / (1 + abs(float(a.detach() if hasattr(a,'detach') else a)))
cfg = make_cfg()
# G1X against direct formula
G1v = eval_dict(G1X(), cfg); Px = cfg[('P', XX)]; X_ = cfg[('X', 0)]
print("G1X vs direct:", rel(G1v, (2 * Px * (X_ - torch.roll(X_, 1))).sum()))
for u in random.sample(solve.enum_G2(R), 5):
    cfg = make_cfg()
    g2 = G2X(u)
    e = eval_dict(fadd(bracket(g2, C1('N')), bracket(g2, T2('N'))), cfg)
    a = ag(eval_dict(g2, cfg), eval_dict(C1('N'), cfg), cfg) + ag(eval_dict(g2, cfg), eval_dict(T2('N'), cfg), cfg)
    worst = max(worst, rel(e, a))
for v in random.sample(enum_V2(R), 5):
    cfg = make_cfg()
    e = eval_dict(bracket(G1X(), V2_of(v, 'N')), cfg)
    a = ag(eval_dict(G1X(), cfg), eval_dict(V2_of(v, 'N'), cfg), cfg)
    worst = max(worst, rel(e, a))
for t in random.sample(enum_T3(R), 5):
    cfg = make_cfg()
    e = eval_dict(bracket(G1X(), T3_of(t, 'N')), cfg)
    a = ag(eval_dict(G1X(), cfg), eval_dict(T3_of(t, 'N'), cfg), cfg)
    worst = max(worst, rel(e, a))
for (a_, b_) in [(-1, 0), (0, 1), (1, -1), (2, 1)]:
    cfg = make_cfg()
    Y = torch.roll(cfg[('X', 0)], -a_) * torch.roll(cfg[('N', 0)], -b_)
    hyz = cfg[('h', YY)] + cfg[('h', ZZ)]
    C1Y = ((2 * Y - torch.roll(Y, -1) - torch.roll(Y, 1)) * hyz).sum()
    e = eval_dict(C1_of_Y(a_, b_), cfg)
    worst = max(worst, rel(e, C1Y))
    pp = sum(cfg[('P', c)]**2 for c in COMPS)*(1-0.5) - 2*0.5*(cfg[('P',0)]*cfg[('P',1)]+cfg[('P',0)]*cfg[('P',2)]+cfg[('P',1)]*cfg[('P',2)])
    T2Y = (Y * pp).sum() / 4
    e2 = eval_dict(T2_of_Y(a_, b_), cfg)
    worst = max(worst, rel(e2, T2Y))
print("worst rel err of k7 columns vs autograd/direct:", worst)
