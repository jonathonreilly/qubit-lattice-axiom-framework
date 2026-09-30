"""Kill check: validate the 2D bracket engine (doubled coordinates, xy faces) against torch autograd on a periodic torus,
and check the 2D degree-1 identity and the R2 (gauge invariance) numerically with an independent real-space implementation."""
import random
import torch
import engine2, model2, solve2d
from model2 import *
from solve2d import enum_V2, enum_T3, col_V2, col_T3, V2_of

torch.set_default_dtype(torch.float64)
Lr = 7
random.seed(5); torch.manual_seed(5)
COMP4 = (XX, YY, ZZ, XY)

def make_cfg():
    cfg = {}
    for kind in ('h', 'P'):
        for c in COMP4:
            cfg[(kind, c)] = torch.randn(Lr, Lr, requires_grad=True)
    for kind in ('N', 'M'):
        cfg[(kind, 0)] = torch.randn(Lr, Lr)
    return cfg

def val(cfg, v):
    k, c, (px, py) = v
    if k in ('N', 'M'):
        ox, oy = px // 2, py // 2
    elif c == XY:
        ox, oy = (px - 1) // 2, (py - 1) // 2
    else:
        ox, oy = px // 2, py // 2
    return torch.roll(cfg[(k, c)], shifts=(-ox, -oy), dims=(0, 1))

def eval_dict(d, cfg):
    tot = 0.0
    for mono, coef in d.items():
        term = None
        for v in mono:
            a = val(cfg, v)
            term = a if term is None else term * a
        tot = tot + float(coef) * (term.sum() if term is not None else torch.tensor(float(Lr * Lr)))
    return tot

def ag_bracket(A, B, cfg):
    tot = 0.0
    for c in COMP4:
        h, P = cfg[('h', c)], cfg[('P', c)]
        gAh, gAP = torch.autograd.grad(A, [h, P], retain_graph=True, allow_unused=True, create_graph=True)
        gBh, gBP = torch.autograd.grad(B, [h, P], retain_graph=True, allow_unused=True, create_graph=True)
        z = lambda g: torch.zeros(Lr, Lr) if g is None else g
        tot = tot + (z(gAh) * z(gBP)).sum() - (z(gAP) * z(gBh)).sum()
    return tot

def check(R, nsamp=8):
    worst = 0.0
    for kind, pool in (('V2', enum_V2(R)), ('T3', enum_T3(R))):
        for m in random.sample(pool, nsamp):
            cfg = make_cfg()
            col = col_V2(m) if kind == 'V2' else col_T3(m)
            e = eval_dict(col, cfg)
            if kind == 'V2':
                a = ag_bracket(eval_dict(T2('N'), cfg), eval_dict(V2_of(m, 'M'), cfg), cfg) + ag_bracket(eval_dict(V2_of(m, 'N'), cfg), eval_dict(T2('M'), cfg), cfg)
            else:
                a = ag_bracket(eval_dict(C1('N'), cfg), eval_dict(V2_of(m, 'M'), cfg), cfg) + ag_bracket(eval_dict(V2_of(m, 'N'), cfg), eval_dict(C1('M'), cfg), cfg)
            worst = max(worst, abs(float(e.detach()) - float(a.detach())) / (1 + abs(float(a.detach()))))
    return worst

for R in (1, 2):
    print("2D R", R, "worst rel err engine-vs-autograd:", check(R))

# degree-1 identity with an independent ring formula for G1[xi0] in 2D (including xy-face terms)
cfg = make_cfg()
lhs = ag_bracket(eval_dict(C1('N'), cfg), eval_dict(T2('M'), cfg), cfg) + ag_bracket(eval_dict(T2('N'), cfg), eval_dict(C1('M'), cfg), cfg)
N_, M_ = cfg[('N', 0)], cfg[('M', 0)]
sh = lambda a, dx, dy: torch.roll(a, shifts=(-dx, -dy), dims=(0, 1))
xix = 0.25 * (sh(N_, 1, 0) * M_ - N_ * sh(M_, 1, 0))      # xi_x on x-bond (i,j)->(i+1,j)
xiy = 0.25 * (sh(N_, 0, 1) * M_ - N_ * sh(M_, 0, 1))
Pxx, Pyy, Pxy = cfg[('P', XX)], cfg[('P', YY)], cfg[('P', XY)]
# G[xi] = sum P_ij (d_i xi_j + d_j xi_i): P_xx*2*(xi_x(n)-xi_x(n-1)) + P_yy*2*(xi_y(n)-xi_y(n-1)) + P_xy(face i+1/2,j+1/2)*[(xi_y(i+1,j)-xi_y(i,j)) + (xi_x(i,j+1)-xi_x(i,j))]
G = (2 * Pxx * (xix - sh(xix, -1, 0))).sum() + (2 * Pyy * (xiy - sh(xiy, 0, -1))).sum() \
    + (Pxy * ((sh(xiy, 1, 0) - xiy) + (sh(xix, 0, 1) - xix))).sum()
print("2D degree-1 numeric: lhs", float(lhs.detach()), " independent G1[xi0]", float(G.detach()))
