"""Exact peeling: Groebner bases of closed sub-systems of the (complexified) unitarity
equations sum_n A_n A_{n-d}^dag = delta_{d0} I  and  sum_n A_n^dag A_{n+d} = delta_{d0} I,
restricted to a chosen set of difference vectors d. Every equation used is one of the
true unitarity equations, so any consequence is exact. w_j stands for conj(z_j).
usage: python3 peel.py GROUP 'd-filter python expr' 'comma list of vars already zero'
"""
import sys, time, itertools, sympy as sp
from setup import GROUPS, build, conjA, NBR, IDX, I2

def eqs_for(A, Ad, dfilter):
    out = []
    for d in itertools.product(range(-2, 3), repeat=3):
        if not dfilter(d):
            continue
        S1 = sp.zeros(2); S2 = sp.zeros(2)
        for n in NBR:
            m = (n[0] - d[0], n[1] - d[1], n[2] - d[2])
            if m in IDX:
                S1 += A[n] * Ad[m]
            m2 = (n[0] + d[0], n[1] + d[1], n[2] + d[2])
            if m2 in IDX:
                S2 += Ad[n] * A[m2]
        if d == (0, 0, 0):
            S1 -= I2; S2 -= I2
        out += [sp.expand(e) for e in list(S1) + list(S2)]
    return [e for e in set(out) if e != 0]

def run(group, dfilter_src, zero_src, maxk=6):
    basis, z, A = build(GROUPS[group], 'z')
    m = len(z)
    w = sp.symbols(f'w0:{m}')
    Ad = conjA(A, z, w)
    zero = [int(s) for s in zero_src.split(',') if s.strip() != '']
    sub = {}
    for j in zero:
        sub[z[j]] = 0; sub[w[j]] = 0
    dfilter = eval('lambda d: ' + dfilter_src)
    eqs = [sp.expand(e.subs(sub)) for e in eqs_for(A, Ad, dfilter)]
    eqs = [e for e in set(eqs) if e != 0]
    vars_ = sorted({s for e in eqs for s in e.free_symbols}, key=lambda s: (s.name[0], int(s.name[1:])))
    # put z0,w0 last
    vars_ = [v for v in vars_ if v.name not in ('z0', 'w0')] + [v for v in vars_ if v.name in ('z0', 'w0')]
    print(f'[{group}] d-filter: {dfilter_src}; zero: {zero}; {len(eqs)} eqs in {len(vars_)} vars', flush=True)
    t = time.time()
    G = sp.groebner(eqs, *vars_, order='grevlex', domain=sp.QQ_I)
    print(f'  GB: {len(G.exprs)} elements, {time.time()-t:.1f}s', flush=True)
    if G.exprs == [1]:
        print('  ideal = (1): no solutions'); return G, z, w
    killed = []
    for j in range(m):
        if z[j] not in vars_:
            continue
        hit = None
        for k in range(1, maxk + 1):
            if G.contains(z[j] ** k):
                hit = f'z{j}^{k} in I (z{j}=0 on complex variety)'; break
            if G.contains((z[j] * w[j]) ** k):
                hit = f'(z{j}*w{j})^{k} in I (|z{j}|^2=0 on real points)'; break
        if hit:
            killed.append(j); print('  ', hit)
    print('  newly zero:', killed)
    return G, z, w

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '')
