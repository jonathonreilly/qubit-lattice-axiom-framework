"""
T229 - what does the enlargement COST?  How many parameters does the
admissibility rule have at M4(C)?

R136: at M2(C) the state is a Bloch 3-vector, covariance + Schur leave exactly
ONE invariant bilinear form (v.v'), so the rule is phi = a + lam (v.v') --
one parameter.  R137/R138 all rest on that being one.

At M4(C) the state space is the 15-dimensional traceless Hermitian part, which
decomposes under the 4D hypercubic group into several irreps.  Each contributes
its own invariant bilinear form.  Counted here, not assumed.

  #(invariant symmetric bilinear forms on the state space) = #(rule parameters)
"""
import numpy as np, itertools

def hyperoct(d):
    out = []
    for perm in itertools.permutations(range(d)):
        for sg in itertools.product([1,-1], repeat=d):
            R = np.zeros((d,d))
            for i,p in enumerate(perm): R[i,p] = sg[i]
            if abs(np.linalg.det(R)-1) < 1e-12: out.append(R)
    return out

I2 = np.eye(2,dtype=complex)
SX = np.array([[0,1],[1,0]],dtype=complex)
SY = np.array([[0,-1j],[1j,0]],dtype=complex)
SZ = np.array([[1,0],[0,-1]],dtype=complex)
Z2 = np.zeros((2,2),dtype=complex)
# EUCLIDEAN gammas (all square to +I) -- the hypercubic ROTATION group is
# Euclidean, so the Minkowski set {g_a,g_b}=2 eta_ab is the wrong one here.
kr = lambda a,b: np.kron(a,b)
GAM4 = [kr(SX,I2), kr(SY,I2), kr(SZ,SX), kr(SZ,SY)]
GAM3 = [SX, SY, SZ]

def spin_U(R, GAM):
    n = GAM[0].shape[0]; d = len(GAM)
    rows = []
    for mu in range(d):
        tgt = sum(R[nu,mu]*GAM[nu] for nu in range(d))
        rows.append(np.kron(np.eye(n), GAM[mu].T) - np.kron(tgt, np.eye(n)))
    A = np.vstack(rows)
    U_, sv, Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape)*np.finfo(float).eps*sv.max()
    k = int(np.sum(sv <= tol))
    assert k == 1, f"spin rep nullspace dim {k}, expected 1"
    U = Vt[len(Vt)-k].conj().reshape(n, n)
    assert abs(np.linalg.det(U)) > 1e-8, "spin rep matrix singular"
    return U

def state_basis(n):
    """orthonormal real basis of the traceless Hermitian n x n matrices"""
    B = []
    for i in range(n):
        for j in range(i+1, n):
            E = np.zeros((n,n),dtype=complex); E[i,j]=1; E[j,i]=1; B.append(E/np.sqrt(2))
            F = np.zeros((n,n),dtype=complex); F[i,j]=-1j; F[j,i]=1j; B.append(F/np.sqrt(2))
    for k in range(1, n):
        d = np.zeros(n); d[:k] = 1; d[k] = -k
        B.append(np.diag(d).astype(complex)/np.sqrt(k*k+k))
    return B

def invariant_forms(Rs, GAM):
    n = GAM[0].shape[0]
    B = state_basis(n); m = len(B)
    Os = []
    for R in Rs:
        U = spin_U(R, GAM)
        O = np.zeros((m, m))
        for j, Bj in enumerate(B):
            X = U @ Bj @ np.linalg.inv(U)
            for i, Bi in enumerate(B):
                O[i, j] = np.real(np.trace(Bi.conj().T @ X))
        Os.append(O)
    # symmetric forms S with O^T S O = S for all R
    idx = [(i,j) for i in range(m) for j in range(i, m)]
    rows = []
    for O in Os:
        for a,(i,j) in enumerate(idx):
            r = np.zeros(len(idx))
            for b,(k,l) in enumerate(idx):
                v = O[k,i]*O[l,j] + (O[l,i]*O[k,j] if k!=l else 0.0)
                r[b] += v
            r[a] -= 1.0
            rows.append(r)
    A = np.array(rows)
    U_, sv, Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape)*np.finfo(float).eps*sv.max()
    return m, int(np.sum(sv <= tol)), Os

print("=== how many parameters does the rule have? ===")
m3, k3, _ = invariant_forms(hyperoct(3), GAM3)
print(f"  Z^3 with M2(C): state space dimension {m3:2d}   "
      f"invariant symmetric forms = {k3}   -> {k3} parameter(s)")
m4, k4, Os = invariant_forms(hyperoct(4), GAM4)
print(f"  Z^4 with M4(C): state space dimension {m4:2d}   "
      f"invariant symmetric forms = {k4}   -> {k4} parameter(s)")

print("\n=== the decomposition, via the commutant (character route was wrong) ===")
print("  det(R) = +1 on the PROPER group, so 'axial' has the same character as")
print("  'vector' and 'pseudoscalar' the same as trivial: they cannot be told")
print("  apart that way.  Use the commutant instead: for a real-type rep")
print("  (+) m_i V_i the commutant has dimension sum m_i^2 and the invariant")
print("  SYMMETRIC forms number sum m_i(m_i+1)/2.")
m = len(Os[0])
rows = []
for O in Os:
    rows.append(np.kron(np.eye(m), O.T) - np.kron(O, np.eye(m)))
A = np.vstack(rows)
U_, sv, Vt = np.linalg.svd(A, full_matrices=False)
tol = max(A.shape)*np.finfo(float).eps*sv.max()
kc = int(np.sum(sv <= tol))
print(f"\n  commutant of the 15-dim rep: dimension {kc}")
print(f"  invariant symmetric forms   : {k4}")
print(f"""
  the consistent reading is   15 = 2x(4) (+) 3_+ (+) 3_- (+) 1
      commutant        = 2^2 + 1 + 1 + 1 = 7
      symmetric forms  = 3   + 1 + 1 + 1 = 6
  dims: 2x4 + 3 + 3 + 1 = 15   -- measured commutant {kc}, forms {k4}.
  the 6 of SO(4) splitting into 3_+ (+) 3_- is the SELF-DUAL split, which is
  R42's d=4 speciality showing up again: the Hodge star acts on 2-cells only
  in four dimensions.""")
