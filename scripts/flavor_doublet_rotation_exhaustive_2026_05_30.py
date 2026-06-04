#!/usr/bin/env python3
"""Finite doublet-rotation checks for the hw=1 generation packet.

This runner intentionally does not prove a broad exhaustive classification of
all anti-unitary, projective, coin, or induced representation routes. It checks
the finite pieces available inside the packet:

* signed-permutation/O_h action on the hw=1 set;
* elementary bit-flip non-preservation of the hw=1 set;
* central scalar i*I_3 versus the non-central J_cs;
* exact uniqueness of the C3-equivariant doublet complex structure up to sign.

The det_C/det_R and Q=2/3 versus Q=1 readout labels remain downstream measure
context, not a load-bearing result of this finite symmetry runner.

  E1 finite signed-permutation/O_h action: hw=1 stabilizer = exactly 6 = S3.
  E2 full O_h (48): ZERO of O_h's 12 order-4 (90deg/factor-of-i)
     elements preserve hw=1 -> the lattice NEVER makes a 90deg rotation within one doublet. discrete.
  E3 elementary bit-flips do not preserve hw=1, so this finite route supplies
     no intra-doublet rotation.
  E4 central scalar i*I3 commutes with C but is distinct from J_cs.
  E5 exact C3-equivariant solve: the only real circulant J with J*1=0 and
     J^2=-P_doublet are +/-J_cs.
"""
import numpy as np, itertools, sympy as sp

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    passed=[]
    corners=list(itertools.product([0,1],repeat=3)); hw1=set(c for c in corners if sum(c)==1)
    def act(perm,sf,c):
        c2=[c[perm[i]] for i in range(3)]; return tuple(c2[i]^sf[i] for i in range(3))
    stabilizer_maps = []
    o4=o4p=0
    for perm in itertools.permutations(range(3)):
        for sf in itertools.product([0,1],repeat=3):
            mp={c:act(perm,sf,c) for c in corners}; o=1; cur=dict(mp)
            while any(cur[c]!=c for c in corners) and o<10: cur={c:mp[cur[c]] for c in corners}; o+=1
            if all(mp[c] in hw1 for c in hw1):
                stabilizer_maps.append(tuple(mp[c] for c in sorted(hw1)))
            if o==4:
                o4+=1
                if all(mp[c] in hw1 for c in hw1): o4p+=1

    passed.append(check("E1 finite O_h/signed-permutation stabilizer of hw=1 has six actions, i.e. S3/D3 on the three hw=1 vertices",
        len(set(stabilizer_maps)) == 6, f"distinct hw=1 stabilizer actions={len(set(stabilizer_maps))}"))
    passed.append(check("E2 finite O_h: 0 of 12 order-4 elements preserve hw=1",
        o4==12 and o4p==0, f"order-4 total={o4}, preserve-hw1={o4p}"))

    # E3 single bit-flip does not preserve hw=1.
    leaves=all(sum(tuple(c[i]^(j==i) for i in range(3)))!=1 for c in hw1 for j in range(3))
    passed.append(check("E3 elementary bit-flips do not preserve hw=1, so this finite route gives no intra-doublet rotation",
        leaves, "each one-bit flip sends an hw=1 vertex to Hamming weight 0 or 2"))

    # E4 central scalar vs J_cs.
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); Jcs=(C-C.T)/np.sqrt(3)
    passed.append(check("E4 central i*I3 commutes with C and is distinct from non-central J_cs",
        np.allclose((1j*np.eye(3))@C-C@(1j*np.eye(3)),0) and abs(np.linalg.eigvals(Jcs)[np.argmin(np.abs(np.linalg.eigvals(Jcs)))])<1e-9))

    # E5 exact C3-equivariant J uniqueness in the real circulant packet.
    a,b,c=sp.symbols('a b c',real=True)
    I=sp.eye(3); Csp=sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    P=I-sp.Rational(1,3)*sp.ones(3,3)
    X=a*I+b*Csp+c*Csp**2
    exprs=list(X*sp.ones(3,1)) + list((X**2 + P).reshape(9,1))
    sol=sp.solve([sp.Eq(e,0) for e in exprs], [a,b,c], dict=True)
    expected=[
        {a: 0, b: -sp.sqrt(3)/3, c: sp.sqrt(3)/3},
        {a: 0, b: sp.sqrt(3)/3, c: -sp.sqrt(3)/3},
    ]
    passed.append(check("E5 exact solve: only +/-J_cs satisfy C3-equivariance, J*1=0, and J^2=-P_doublet",
        sol == expected, f"solutions {sol}"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: bounded finite-operator support only.")
    print("The runner checks O_h/hw1 finite actions, bit-flip non-preservation,")
    print("central i*I3 versus J_cs, and exact +/-J_cs uniqueness in the real")
    print("C3-circulant packet. It does not prove broad exhaustive classification,")
    print("cohomology backstops, anti-unitary/coin/induced collapse, or det_C/det_R")
    print("readout values.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
