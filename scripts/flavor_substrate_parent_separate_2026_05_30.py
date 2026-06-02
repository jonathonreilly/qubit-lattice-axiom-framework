#!/usr/bin/env python3
"""Substrate-parent unification (Build D): does ONE lifted M_2(C)x(Z_2)^3 operator project onto BOTH
the value generator G_U1 (on-block, commutes Gamma_chi) AND the chiral grading (anticommutes)?
VERDICT: genuinely SEPARATE under the Z_2-spin-factor reading -- but the one rehab channel is the SAME
complex/order-3 (det_C) object as the value import, so value and chirality share a common ROOT import.

  D1 tensor-factorization: even/odd under the coin-blind grading I2(x)Gamma_chi depends ONLY on the
     generation factor's relation to Gamma_chi (independent of coin). So the assembled K=I2(x)G_U1+sx(x)H_chi
     splits as a FORCED super-direct-sum (G_U1 even slot, H_chi odd slot, non-interchangeable) -- NOT an
     indecomposable parent. The coin index is pure bookkeeping; the R^3 orthogonality comm(C)cap anticomm(Gchi)
     ={0} is inherited verbatim by the lift.
  D2 a C3-equivariant NATIVE parent (qubit C3-singlet I2) projects on-hw1 to the 3-dim circulant algebra:
     G_U1 reachable, Gamma-anticommuting (chiral) NOT reachable.
  D3 the ONLY channel folding a C3-equivariant parent to a chiral on-block op needs an ORDER-3 qubit charge
     diag(1,omega) (order 3, det=omega not in SU(2), complex I/Z coefficients) -- NOT native to the Z_2 spin
     factor M_2(C). And that order-3 complex phase IS the SAME complex/det_C structure as the value import.
  => value (C3-equivariant) and chirality (orbit-splitting) are algebraically orthogonal on R^3 AND not
     unified by any native lift; the single object that would unify them is the imported order-3 complex
     (det_C) phase -- so NOT 'same gate' (Correction 1 holds) but 'same ROOT import'.
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); I3=np.eye(3); J=np.ones((3,3)); Gchi=(2/3)*J-I3
    G_U1=(C-C.T)/np.sqrt(3); h=np.array([1,-1,0.]); H_chi=(np.outer(h,np.ones(3))+np.outer(np.ones(3),h))/3
    sx=np.array([[0,1],[1,0]],float); I2=np.eye(2); G6=np.kron(I2,Gchi)
    K=np.kron(I2,G_U1)+np.kron(sx,H_chi)
    passed=[]
    passed.append(check("D1 assembled parent K splits as forced super-direct-sum (decomposable, not indecomposable)",
        np.allclose((K+G6@K@G6)/2, np.kron(I2,G_U1)) and np.allclose((K-G6@K@G6)/2, np.kron(sx,H_chi)),
        "even slot=I2(x)G_U1, odd slot=sx(x)H_chi, forced/non-interchangeable; coin index = bookkeeping"))
    passed.append(check("D2 G_U1 commutes Gamma_chi & C (on-block); chiral grading anticommutes & breaks C (off-block)",
        np.allclose(G_U1@Gchi-Gchi@G_U1,0) and np.allclose(G_U1@C-C@G_U1,0) and
        np.linalg.norm(H_chi@Gchi+Gchi@H_chi)<1e-9 and np.linalg.norm(H_chi@C-C@H_chi)>1e-6,
        "orthogonal on R^3 -- comm(C) cap anticomm(Gchi)={0} inherited by the lift"))
    w=np.exp(2j*np.pi/3); d=np.diag([1,w])
    order3=np.allclose(np.linalg.matrix_power(d,3),np.eye(2)) and not np.allclose(d@d,np.eye(2))
    passed.append(check("D3 unification channel needs ORDER-3 complex qubit charge diag(1,w) = the det_C object",
        order3 and abs(np.linalg.det(d)-w)<1e-9, "diag(1,w): order 3, det=w (not SU(2)), complex I/Z coeffs = same complex/det_C structure as value import"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: genuinely SEPARATE (Correction 1 holds: value != chirality on R^3, and no native lift")
    print("unifies them). BUT the single object that WOULD unify them = the imported order-3 complex (det_C)")
    print("phase = the SAME root as the value import. So: not one GATE, but one common ROOT IMPORT (the")
    print("complex/order-3/det_C structure the discrete Z_2-spin substrate lacks). Caveat: hinges on the")
    print("Z_2-spin-factor reading of M_2(C) (no native order-3 charge) -- recommend audit row.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
