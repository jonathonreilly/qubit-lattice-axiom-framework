import itertools, numpy as np
from indep_bubble import *
rng = np.random.default_rng(1)
# hyperoctahedral group B4 as signed permutation matrices
G4 = []
for perm in itertools.permutations(range(4)):
    for sg in itertools.product((1, -1), repeat=4):
        R = np.zeros((4, 4)); R[range(4), perm] = sg; G4.append(R)
def act(R, T):
    return np.einsum('ai,bj,ck,dl,em,fn,ijklmn->abcdef', R, R, R, R, R, R, T, optimize=True)
def symm(T):
    T = (T + T.transpose(1,0,2,3,4,5)) / 2; T = (T + T.transpose(0,1,3,2,4,5)) / 2
    T = (T + T.transpose(0,1,2,3,5,4)) / 2; T = (T + T.transpose(2,3,0,1,4,5)) / 2
    return T
# B4 Reynolds operator applied to random symmetric tensors -> basis of invariant symbols
vecs = []
for _ in range(40):
    T = symm(rng.normal(size=(4,)*6))
    T = sum(act(R, T) for R in G4) / len(G4)
    vecs.append(T.ravel())
U, s, Vt = np.linalg.svd(np.array(vecs), full_matrices=False)
r = int((s > 1e-8 * s[0]).sum()); B = Vt[:r].reshape(r, *(4,)*6)
print("dim of B4-invariant two-derivative symbol space:", r)
# also Lorentz (O(4)) subspace: average over random rotations
def ward_coef(T):  # k_m T_{mnrsab} k_a k_b  -> symmetrise over (m,a,b)
    C = T.transpose(1,2,3,0,4,5)  # n r s m a b
    perms = list(itertools.permutations((3,4,5)))
    return sum(C.transpose(0,1,2,*p) for p in perms) / 6
Wm = np.array([ward_coef(b).ravel() for b in B]).T
sw = np.linalg.svd(Wm, compute_uv=False)
print("singular values of Ward map on B4 symbols:", np.round(sw, 6))
_, _, vt = np.linalg.svd(Wm); null = vt[-1]
Tinv = np.tensordot(null, B, 1)
# compare to linearised EH (hand-written, independent normalisation)
d = np.eye(4)
EH = symm(0.5*np.einsum('ac,bd,ef->abcdef', d,d,d) - np.einsum('ae,cf,bd->abcdef', d,d,d)
          + 0.5*(np.einsum('ab,ce,df->abcdef', d,d,d) + np.einsum('cd,ae,bf->abcdef', d,d,d))
          - 0.5*np.einsum('ab,cd,ef->abcdef', d,d,d))
print("EH Ward residual", np.abs(ward_coef(EH)).max())
cos = abs(np.vdot(Tinv.ravel(), EH.ravel())) / np.linalg.norm(Tinv) / np.linalg.norm(EH)
print("unique gauge-invariant B4 symbol vs EH: |cos| = %.12f" % cos)
# fit my measured symbol (m=0.7, N=12) from several directions
m, N = 0.7, 12
dirs = [np.array([1.0, 0.37, 0.61, -0.23]), np.array([0.2, 1.0, -0.5, 0.8]), np.array([1.0, 1.0, 0.0, 0.0]),
        np.array([0.3, -0.1, 0.9, 0.4]), np.array([1.0, 0.0, 0.0, 0.0])]
P0 = bubble(np.zeros(4), N, m)
rows, rhs = [], []
Ms = []
for v in dirs:
    v = v / np.linalg.norm(v)
    Ma = (bubble(0.1*v, N, m) - P0) / 0.01; Mb = (bubble(0.05*v, N, m) - P0) / 0.0025
    M2 = ((4*Mb - Ma) / 3).real; Ms.append((v, M2))
    rows.append(np.einsum('iabcdef,e,f->abcdi', B, v, v).reshape(-1, r)); rhs.append(M2.ravel())
A = np.vstack(rows); y = np.concatenate(rhs)
c, *_ = np.linalg.lstsq(A, y, rcond=None)
print("B4 fit relative residual: %.2e" % (np.linalg.norm(A@c - y) / np.linalg.norm(y)))
Tmeas = np.tensordot(c, B, 1)
# minimal-norm restoration to the gauge-invariant line (Frobenius on the 6-tensor)
a = np.vdot(EH.ravel(), Tmeas.ravel()) / np.vdot(EH.ravel(), EH.ravel())
print("a_EH = %.6f ; ||T - a EH||/||T|| = %.4f" % (a, np.linalg.norm(Tmeas - a*EH) / np.linalg.norm(Tmeas)))
# relative Ward violation of measured symbol, max over sampled directions
for v, M2 in Ms:
    print("dir", np.round(v, 3), " max|n.M2|/max|M2| = %.4f" % (np.abs(np.einsum('m,mnrs->nrs', v, M2)).max() / np.abs(M2).max()))
# TT-pol stiffness ratios: raw vs restored (E vs T2 along x)
v = np.array([0, 1.0, 0, 0])
def sym4(T, k): return np.einsum('abcdef,e,f->abcd', T, k, k)
eT2 = np.zeros((4, 4)); eT2[2, 3] = eT2[3, 2] = 1/np.sqrt(2)
eE = np.zeros((4, 4)); eE[2, 2] = 1/np.sqrt(2); eE[3, 3] = -1/np.sqrt(2)
for lab, T in (("raw", Tmeas), ("EH-restored", a*EH)):
    M = sym4(T, v); q = lambda e_: np.einsum('ab,abcd,cd->', e_, M, e_)
    print(lab, "along x: E/T2 =", q(eE) / q(eT2))
np.save('Tmeas_m0.7_N12.npy', Tmeas)
