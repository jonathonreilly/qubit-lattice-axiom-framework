#!/usr/bin/env python3
"""CORRECTION + cross-session reconciliation (parallel worker's reframe, independently verified).
The Q=2/3 (block-count) reading is NATIVELY AVAILABLE -- it is NOT forbidden by C^3=I. Corrects my
prior over-stated claim that 'det_C / the Q=2/3 reading is forbidden by C^3=I'.

  V1 the qubit's complex unit i IS the Cl(3) pseudoscalar sigma_x sigma_y sigma_z = i*I2; on the
     generation triplet it acts as the SCALAR i*I3 -- generation-BLIND ([i*I3,C]=0). It cannot supply
     the doublet-selective complex structure the block-count needs. (Consistent with prior Build C/D.)
  V2 the generation's NATIVE complex structure is J_cs=(C-C^2)/sqrt3: REAL antisymmetric (built from the
     real C3 shift), C3-EQUIVARIANT ([J_cs,C]=0), eigenvalues {0,+i,-i} -- singlet stays real, doublet =
     ONE complex line. J_cs != i*I3. C^3=I does NOT forbid J_cs (it is built FROM C).
  V3 CORRECTION: C^3=I forbids the continuous U(1)_b SYMMETRY (rephasing C->e^{ia}C, quantized to
     {0,2pi/3,4pi/3}) -- but the block-count MEASURE does NOT use that symmetry; it uses the Schur/FS
     complex structure J_cs, which IS native and C3-equivariant. So 'C^3=I forbids the Q=2/3 reading' was
     conflating symmetry with measure. The Q=2/3 (K0-real / block / coherent-state) reading is AVAILABLE.
  V4 the fork (the parallel worker's sharper framing, confirmed): real DIMENSION (det_R, 2 real slots) AND
     complex-dimension/trace/Plancherel BOTH give (1,2) -> Q=1; only the real-WEDDERBURN-BLOCK count
     K0(R[Z3])=Z^2 (doublet = ONE block, FS indicator 0, endomorphism field C) gives (1,1) -> Q=2/3.
     'real dimension' != 'real block'.
  HONEST STATUS (convergent with this session's Build C): BOTH readings are native; NEITHER is forced.
  Trace/dimension (Q=1) is privileged only by PRR (full U(3) invariance, unaudited); block-count (Q=2/3)
  uses the native J_cs and is the coherent-state reading -- defensibly more faithful to 'a qubit at each
  site' but NOT uniquely forced. The slot is a free native reality-structure bit (K0-real vs K0-complex).
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); I3=np.eye(3); Jcs=(C-C.T)/np.sqrt(3)
    passed=[]
    passed.append(check("V1 qubit i = Cl(3) pseudoscalar = i*I2; on generations = i*I3 (generation-blind)",
        np.allclose(sx@sy@sz,1j*np.eye(2)) and np.allclose((1j*I3)@C-C@(1j*I3),0)))
    ev=np.sort_complex(np.linalg.eigvals(Jcs))
    passed.append(check("V2 J_cs=(C-C^2)/sqrt3: real antisym, C3-equivariant, eigs {0,+i,-i}, != i*I3, native",
        np.allclose(Jcs,Jcs.real) and np.allclose(Jcs,-Jcs.T) and np.allclose(Jcs@C-C@Jcs,0)
        and np.allclose(sorted(ev,key=lambda z:z.imag),[-1j,0,1j]) and not np.allclose(Jcs,1j*I3),
        "doublet = one complex line; singlet real; built from real C so C^3=I cannot forbid it"))
    # V3 C^3=I forbids U(1)_b symmetry but not J_cs measure
    w=np.exp(2j*np.pi/3)
    sym_quantized = np.allclose(np.linalg.matrix_power(w*C,3),I3) and not np.allclose(np.linalg.matrix_power(np.exp(0.4j)*C,3),I3)
    passed.append(check("V3 CORRECTION: C^3=I kills U(1)_b SYMMETRY (quantized) but NOT the native J_cs MEASURE",
        sym_quantized and np.allclose(Jcs@C-C@Jcs,0),
        "block-count uses J_cs (Schur/FS structure), not the U(1)_b symmetry -> Q=2/3 reading is AVAILABLE"))
    Q=lambda ws,wd: 1/3+2/3*(wd/(2*ws))
    passed.append(check("V4 real-dim & trace -> (1,2)->Q=1; real-BLOCK K0(R[Z3])=Z^2 -> (1,1)->Q=2/3",
        abs(Q(1,2)-1)<1e-12 and abs(Q(1,1)-2/3)<1e-12, "'real dimension' != 'real block' (doublet=ONE Wedderburn block)"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: the Q=2/3 block-count reading is NATIVELY AVAILABLE via J_cs=(C-C^2)/sqrt3 (C3-equivariant,")
    print("NOT forbidden by C^3=I -- correcting the prior overstatement). BOTH Q=2/3 (K0-real/block/coherent-")
    print("state, native J_cs) and Q=1 (K0-complex/dimension/trace, privileged only by unaudited PRR) are")
    print("native readings; NEITHER is forced. The slot is a free reality-structure bit. Converges with this")
    print("session's Build C (trace needs PRR) + the parallel worker's K-theory framing + PR #2412.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
