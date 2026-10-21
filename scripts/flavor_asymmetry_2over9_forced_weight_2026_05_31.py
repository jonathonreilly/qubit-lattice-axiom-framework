#!/usr/bin/env python3
"""Finite inverse-normal-determinant density on a supplied C3 carrier.
The regular-representation complement has weights (1,2), giving 2/9.
Three algebraic labels are not a derivation of physical generations.
This finite density is neither an integer-valued finite character index nor
a derived physical phase; global analytic eta invariants are not classified here.
"""
import numpy as np, sympy as sp

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    w=sp.exp(2*sp.pi*sp.I/3)
    L3=lambda a: sp.nsimplify(sp.simplify((sp.Rational(1,3))*sum(1/((w**(k*a[0])-1)*(w**(k*a[1])-1)) for k in range(1,3))))
    passed=[]
    passed.append(check("A2/A3 L_3(1,2)=2/9 (forced); (1,1)/(2,2)=1/9; (1,2) is the unique unordered determinant-one pair among nonzero characters",
        L3((1,2))==sp.Rational(2,9) and L3((1,1))==sp.Rational(1,9) and L3((2,2))==sp.Rational(1,9)
        and [(a,b) for a in (1,2) for b in (a,2) if (a+b)%3==0]==[(1,2)],
        "(1,2) = regular-rep complement of the C3 singlet (coordinate-sum-zero 2-plane; representation trace is -1) -> weight FORCED"))
    d=sp.Symbol('d',positive=True)
    guises={"(d-1)/d^2":(d-1)/d**2,"2/d^2":2/d**2,"(d^2-1)/12d":(d**2-1)/(12*d)}
    allat3=all(g.subs(d,3)==sp.Rational(2,9) for g in guises.values())
    # 2/d^2 = (d^2-1)/12d <=> d^3-d-24=0, real root d=3
    roots=sp.solve(sp.Eq(2/d**2,(d**2-1)/(12*d)),d)
    realroots=[r for r in roots if r.is_real]
    passed.append(check("A4 three supplied functions and fixed L3 coefficient all=2/9 at d=3 but are DIFFERENT functions (triple-crossing, not one invariant)",
        allat3 and 3 in [sp.nsimplify(r) for r in realroots],
        f"2/d^2=(d^2-1)/12d real root: d=3 only -> agreement at supplied d=3, no independent physical corroboration"))
    # 2/9 not in Z[zeta_3]: rational 2/9 is an algebraic integer iff denominator 1
    passed.append(check("rational local density 2/9 is not an algebraic integer (denominator 9)",
        sp.Rational(2,9).q == 9,
        "A rational algebraic integer must be integral; this does not classify general analytic eta invariants."))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: supplied C3 weights (1,2) give local density 2/9. Physical readout and generation identification remain open.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
