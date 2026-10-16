"""Exact development controls for explicitly supplied deterministic models."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as s

P = Path(__file__).resolve().parent
checks = []


def check(name, ok, **kw):
    assert ok, name
    checks.append({"name": name, "passed": True, **kw})


def step(u, p):
    assert 0 <= u < 1 and 0 < p < 1
    return (0, u / p) if u < p else (1, (u - p) / (1 - p))


def companion(v, q):
    assert 0 < v <= 1 and 0 < q < 1
    # Returns whether this second detector clicks.
    return (1, v / q) if v <= q else (0, (v - q) / (1 - q))


def cylinders(depth, control):
    leaves = [((), F(0), F(1), F(1))]
    for _ in range(depth):
        following = []
        for hist, lo, hi, prob in leaves:
            p = control(hist)
            middle = lo + (hi - lo) * p
            following.extend([(hist + (0,), lo, middle, prob * p),
                              (hist + (1,), middle, hi, prob * (1 - p))])
        leaves = following
    return leaves


for label, control in [
    ("fixed thirds", lambda h: F(1, 3)),
    ("fixed balanced", lambda h: F(1, 2)),
    ("prescribed", lambda h: [F(1, 4), F(2, 3), F(1, 2)][len(h) % 3]),
    ("past-adaptive", lambda h: F(1 + sum(h) % 3, 4)),
]:
    leaves = cylinders(9, control)
    assert sum(prob for _, _, _, prob in leaves) == 1
    for hist, lo, hi, prob in leaves:
        assert hi - lo == prob
        u = (lo + hi) / 2
        generated = ()
        for bit in hist:
            z, u = step(u, control(generated))
            assert z == bit
            generated += (z,)
        assert u == F(1, 2)
    check("exact cylinder " + label, True, cylinders=len(leaves))

p, u, v, a = s.symbols("p u v a", real=True)
c = p**2 + (1 - p)**2
rho = 1 + a * (2 * u - 1)
Lrho = p * rho.subs(u, p * u) + (1 - p) * rho.subs(u, p + (1 - p) * u)
check("linear density exact contraction", s.simplify(Lrho - (1 + a * c * (2 * u - 1))) == 0)
check("density normalization", s.integrate(Lrho, (u, 0, 1)) == 1)
check("linear density output probability", s.simplify(s.integrate(rho, (u, 0, p)) - (p - a * p * (1 - p))) == 0)
tv_without_a = (s.integrate(1 - 2*u, (u, 0, s.Rational(1, 2))) + s.integrate(2*u - 1, (u, s.Rational(1, 2), 1))) / 2
check("linear density total variation", tv_without_a == s.Rational(1, 4))
check("contraction gap is positive on declared domain", s.factor(1 - c) == -2*p*(p - 1), domain="0<p<1")

rows = []
for pp in [F(1, 3), F(1, 2), F(3, 4)]:
    for burn in [1, 2, 4]:
        all_leaves = cylinders(burn + 3, lambda h: pp)
        actual = Counter()
        for hist, lo, hi, prob in all_leaves:
            actual[hist[burn:]] += hi*hi - lo*lo  # Integral of 2*u.
        target = {h: width for h, _, _, width in cylinders(3, lambda h: pp)}
        tv = sum(abs(actual[h] - target[h]) for h in target) / 2
        bound = (pp*pp + (1-pp)*(1-pp))**burn / 4
        assert tv <= bound
        # Direct Perron-density evaluation gives the same future distribution.
        for h, lo, hi, width in cylinders(3, lambda h: pp):
            slope_factor = (pp*pp + (1-pp)*(1-pp))**burn
            assert actual[h] == width + slope_factor * (hi*hi-hi-lo*lo+lo)
        rows.append({"p": str(pp), "burn": burn, "TV": str(tv), "bound": str(bound)})
check("burn-in controls from original nonuniform seed", True, rows=rows)

pair_cases = 0
for u0 in [F(k, 40) for k in range(40)]:
    for pp in [F(1, 4), F(1, 2), F(3, 4)]:
        z, un = step(u0, pp)
        click1, vn = companion(1-u0, 1-pp)
        assert int(z == 0) + click1 == 1
        assert vn == 1-un
        pair_cases += 1
check("two local detector rules and equality conventions", True, cases=pair_cases)
for initial in [F(0), F(1, 7), F(7, 8)]:
    state = initial
    bits = []
    for _ in range(18):
        bit, state = step(state, F(1, 2));bits.append(bit)
    if initial == 0: assert bits == [0]*18
    if initial == F(1, 7): assert bits == [0,0,1]*6
    if initial == F(7, 8): assert bits == [1,1,1]+[0]*15
check("exceptional realized seeds remain non-iid", True)

for z, uv in [(0, s.Matrix([u/p, p*v])), (1, s.Matrix([(u-p)/(1-p), p+(1-p)*v]))]:
    assert s.simplify(uv.jacobian([u,v]).det()) == 1
    back = s.Matrix([p*uv[0], uv[1]/p]) if z == 0 else s.Matrix([p+(1-p)*uv[0], (uv[1]-p)/(1-p)])
    assert all(s.simplify(q) == 0 for q in back-s.Matrix([u,v]))
check("baker branches invertible and area preserving", True)
for pp in [F(1, 3),F(1,2),F(3,4)]:
    for uu,vv in product([F(0),F(1,3),F(1,2),F(3,4),F(9,10)],repeat=2):
        z,un=step(uu,pp)
        vn=pp*vv if z==0 else pp+(1-pp)*vv
        zi=int(vn>=pp)
        assert zi==z
        ub=pp*un if zi==0 else pp+(1-pp)*un
        vb=vn/pp if zi==0 else (vn-pp)/(1-pp)
        assert (ub,vb)==(uu,vv)
check("inverse branches including equality", True)

finite_rows=[]
for m in [2,3,4,5]:
    for n in [m-1,m,m+1,m+3]:
        counts=Counter(tuple(seed[j % m] for j in range(n)) for seed in product([0,1],repeat=m))
        distribution={word:F(num,2**m) for word,num in counts.items()}
        tv=sum(abs(distribution.get(word,0)-F(1,2**n)) for word in product([0,1],repeat=n))/2
        predicted=F(0) if n<=m else 1-F(2**m,2**n)
        assert tv==predicted
        finite_rows.append({"seed_bits":m,"record_length":n,"support":len(counts),"TV":str(tv)})
check("finite cyclic reservoir exact support and TV", True, rows=finite_rows)

w0,w1=s.symbols("w0 w1",real=True);weights=[w0,w1,1-w0-w1]
fs=s.symbols("f0:3",real=True);gs=s.symbols("g0:3",real=True)
cov=sum(w*f*g for w,f,g in zip(weights,fs,gs))-sum(w*f for w,f in zip(weights,fs))*sum(w*g for w,g in zip(weights,gs))
rhs=sum(weights[i]*weights[j]*(fs[i]-fs[j])*(gs[i]-gs[j]) for i in range(3) for j in range(3))/2
check("detector covariance identity", s.expand(cov-rhs)==0)
ws=[F(1,5),F(1,2),F(3,10)];js=[F(0),F(1),F(4)]
f=[j/(1+j) for j in js];g=[2*j/(1+2*j) for j in js]
alpha=sum(w*ff*gg for w,ff,gg in zip(ws,f,g))/(sum(w*ff for w,ff in zip(ws,f))*sum(w*gg for w,gg in zip(ws,g)))
check("monotone detector synthetic ratio", alpha>=1,alpha=str(alpha),calibrated_eta_example="7/10",registered_ratio=str(F(7,10)*alpha))
check("complementary detector state exits independence class", F(0)/(F(1,2)*F(1,2))==0,scope="Counterexample to extending bound to arbitrary shared detector state, not data validation.")

result={"source_sha256":hashlib.sha256((P/'NETWORK_EVOLUTION_BLOCK04_v1.md').read_bytes()).hexdigest(),"runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"checks":checks,"summary":{"passed":len(checks),"failed":0},"empirical_test":False,"scope":"Conditional synthetic identities and exact finite distributions; a deliberately selected deterministic detector model, not a derived physical law."}
text=json.dumps(result,indent=2)+'\n';(P/'RECORD_RESERVOIR_CONTROLS_v1.json').write_text(text);print(text,end='')
