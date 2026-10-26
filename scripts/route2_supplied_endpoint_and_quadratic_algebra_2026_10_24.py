#!/usr/bin/env python3
"""Exact supplied endpoint/quadratic identities and finite counterexamples.

No physical selector or archived negative theorem is imported. Real-exponent
monomial uniqueness is proved analytically in the note; the sweep is finite.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ("docs/ROUTE2_SUPPLIED_ENDPOINT_AND_QUADRATIC_ALGEBRA_NOTE_2026-10-24.md",)
ROOT = Path(__file__).resolve().parents[1]


def dot_g(x, y, a, b, c):
    return a*x[0]*y[0] + c*(x[0]*y[1]+x[1]*y[0]) + b*x[1]*y[1]


def residual(a, b, c, q):
    return a*(q*q-1)+2*c*(2-F(5,3)*q)-F(11,9)*b


def row_outputs(r):
    matrix = ((F(1), F(0), r, F(0)), (F(0), F(-2), F(0), F(2)))
    columns = ((F(1),F(0),F(0),F(0)), (F(1),F(0),F(1,6),F(0)),
               (F(0),F(1),F(0),F(0)), (F(0),F(1),F(0),F(1,6)))
    return tuple(tuple(sum(x*y for x,y in zip(row,col)) for row in matrix) for col in columns)


def nonlinear(w, t):
    return F(5,24)/(w*w)+t*(w-F(1,3))*(w-F(1,2))


def main():
    outcomes=[]
    def check(label, ok, detail=""):
        outcomes.append(bool(ok))
        print(f"{'PASS' if ok else 'FAIL'}: {label}"+(f" :: {detail}" if detail else ""))
    qt=1+F(-1)/6; qe=1+F(21,4)/6; mu=F(-2)
    check("supplied endpoint comparator values", qt==F(5,6) and qe==F(15,8))
    check("supplied c_TE and ratio", mu*qt/qe==F(-8,9) and qe/qt==F(9,4))
    check("inverse comparator transformations", 6*(qe-1)==F(21,4) and mu*qt/F(-8,9)==qe)
    candidates=[F(-1),F(0),F(1),F(21,4)]
    rows=[row_outputs(r) for r in candidates]
    check("supplied matrix products match four columns", all(out==((F(1),F(0)),(1+r/6,F(0)),(F(0),F(-2)),(F(0),F(-5,3))) for r,out in zip(candidates,rows)))
    check("three fixed outputs across finite candidates", all(len({out[k] for out in rows})==1 for k in (0,2,3)))
    check("second output distinguishes finite candidates", len({out[1] for out in rows})==len(candidates))
    we,wt=F(1,3),F(1,2)
    hits=[p for p in range(-8,9) if (we/wt)**p==F(9,4)]
    check("bounded integer monomial sweep",hits==[-2],str(hits))
    norm=qt*wt*wt
    check("conditional inverse-square normalization", norm==F(5,24) and norm/we**2==qe)
    for t in [F(-2),F(0),F(1),F(3,2)]:
        check(f"nonmonomial family matches supplied endpoints at t={t}",nonlinear(we,t)==qe and nonlinear(wt,t)==qt)
    check("positive nonmonomial witness differs away from endpoints",nonlinear(F(1),F(1))-F(5,24)==F(1,3))
    check("positive lower bound for t=1 on endpoint interval", F(5,6)-F(1,144)>0)
    shell=(F(1),F(-2)); center=lambda q:(q,F(-5,3))
    fixtures=[(F(1),F(1),F(0)),(F(3),F(2),F(1)),(F(704),F(1449),F(0)),(F(1),F(3357,3520),F(3,5))]
    for a,b,c in fixtures:
        check(f"expanded norm identity on supplied grid G={a,b,c}",all(dot_g(center(q),center(q),a,b,c)-dot_g(shell,shell,a,b,c)==residual(a,b,c,q) for q in [F(-15,8),F(0),F(1,8),qe]))
    check("comparator residual coefficients",residual(F(1),F(0),F(0),qe)==F(161,64) and residual(F(0),F(0),F(1),qe)==F(-9,4) and residual(F(0),F(1),F(0),qe)==F(-11,9))
    check("diagonal positive metric ratio", F(9,11)*(qe*qe-1)==F(1449,704))
    check("both signs solve diagonal equation",residual(F(704),F(1449),F(0),qe)==0 and residual(F(704),F(1449),F(0),-qe)==0)
    a,b,c=fixtures[-1]
    check("two-positive-root example is SPD",a>0 and a*b-c*c==F(10449,17600)>0)
    # Exact coefficient identity proves factorization, independently of root substitution.
    check("two-positive-root polynomial coefficients",(a,-F(10,3)*c,-a+4*c-F(11,9)*b)==(F(1),F(-2),F(15,64)))
    check("distinct positive roots satisfy equal norm",F(1,8)>0 and qe>F(1,8) and residual(a,b,c,F(1,8))==residual(a,b,c,qe)==0)
    metric_hits=[];tested=0
    for ai in range(16,65,16):
        for bi in range(1,65):
            tested+=1;ci=F(1449*ai-704*bi,1296)
            if ci.denominator==1 and -64<=ci<=64 and ai*bi-ci*ci>0:
                metric_hits.append((ai,bi,int(ci)))
    check("bounded integer SPD search after mod16 reduction",tested==256 and metric_hits==[],str(metric_hits))
    check("explicit unrestricted SPD solution outside search box",704*1449>0 and residual(F(704),F(1449),F(0),qe)==0 and 704>64)
    text=(ROOT/AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    flat=" ".join(text.split())
    check("documentary scope only", "supplied comparison data" in flat and "within the monomial family" in flat and "compatibility, not unique selection" in flat and "two distinct positive roots" in flat)
    print("INFO: exact rational fixtures do not derive physical endpoints; no route-exhaustion claim.")
    print(f"TOTAL: PASS={sum(outcomes)} FAIL={len(outcomes)-sum(outcomes)}")
    return 0 if all(outcomes) else 1


if __name__=="__main__":
    raise SystemExit(main())
