#!/usr/bin/env python3
"""Exact controls for a supplied finite circulant algebra; no physical limit exclusion."""
from pathlib import Path
import math
import sympy as sp
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ["docs/KOIDE_A1_PROBE_CONTINUUM_LIMIT_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe15.md"]
ROOT=Path(__file__).resolve().parents[1]

def main():
    failures=[]
    def check(label,condition):
        ok=bool(condition)
        print(("PASS: " if ok else "FAIL: ")+label)
        if not ok: failures.append(label)
    C=sp.Matrix([[0,0,1],[1,0,0],[0,1,0]]); I=sp.eye(3)
    z=sp.symbols("z", nonzero=True); t=sp.symbols("t")
    check("supplied cyclic matrix is unitary of order three", C.T*C==I and C**3==I)
    check("basis independence", sp.Matrix.hstack(*(m.reshape(9,1) for m in [I,C,C**2])).rank()==3)
    defect=(z**-1-z**2)*C**2
    check("multiplicativity defect factors as (1-z^3)/z", sp.simplify(z*defect-(1-z**3)*C**2)==sp.zeros(3))
    check("source characteristic polynomial", C.charpoly(t).as_expr()==t**3-1)
    check("target characteristic polynomial", sp.expand((z*C).charpoly(t).as_expr())==t**3-z**3)
    # Work modulo z^3-1 to check all nine products exactly, not sampled angles.
    powers=[0,1,-1]
    for i in range(3):
        for j in range(3):
            d=z**powers[(i+j)%3]-z**(powers[i]+powers[j])
            numerator=sp.fraction(sp.cancel(d))[0]
            check(f"basis product {i},{j} modulo cubic relation", sp.rem(numerator,z**3-1,z)==0)
    D=sp.diag(1,z,z**2)
    residual=D*C*D.inv()-z*C
    check("discrete character implementation modulo cubic relation", all(sp.rem(sp.fraction(sp.cancel(x))[0],z**3-1,z)==0 for x in residual))
    a,b,c=sp.symbols("a b c"); X=a*I+b*C+c*C**2
    check("conjugation by C fixes every supplied circulant", C*X*C.T==X)
    u,v,w=sp.symbols("u v w",nonzero=True); diagonal=sp.diag(u,v,w)
    eigenX=sp.diag(a,b,c)
    check("diagonal conjugation fixes diagonal algebra", diagonal*eigenX*diagonal.inv()==eigenX)
    check("z=i supplies exact nonmultiplicative counterexample", defect.subs(z,sp.I)!=sp.zeros(3))
    check("z=1 supplies exact multiplicative case", defect.subs(z,1)==sp.zeros(3))
    # Finite illustrations of the separately proved mesh bound; not execution of closure.
    for n in [0,1,4,8]:
        N=3*2**n
        check(f"C3 inclusion at finite grid n={n}", N%3==0)
        for theta in [0.0,0.41,1.7,2*math.pi-0.01]:
            k=math.floor(N*theta/(2*math.pi)); error=theta-2*math.pi*k/N
            check(f"finite grid bound n={n}, theta={theta}", -1e-14<=error<2*math.pi/N+1e-14)
    note=(ROOT/AUDIT_INPUT_PATHS[0]).read_text()
    check("documentary supplied scope and withdrawn universal mechanism", "closure can enlarge cardinality" in note and "No broad N1-N8 PASS" in note)
    print("per_element: exact finite basis and matrix-entry controls executed; this is not a physical local-element model.")
    print("per_site: checked and not executed; no site-indexed dynamics or physical qubit projection is instantiated.")
    print("per_mode: checked and not executed; algebra basis labels are not an evaluated momentum spectrum or limit.")
    print("per_block: one supplied three-dimensional circulant algebra evaluated; no exhaustive physical block classification.")
    print("lattice_wide: checked and not executed; finite angle grids illustrate a proved bound, not a lattice or infinite-volume run.")
    print(f"FINITE CONTROLS FAIL={len(failures)}; physical admissibility and BAE selection remain open.")
    return 1 if failures else 0
if __name__=="__main__":
    raise SystemExit(main())
