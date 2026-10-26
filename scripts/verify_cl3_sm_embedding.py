"""Finite supplied Cl(3) carrier checks; no physical Standard Model derivation.

Dimensions, chosen normalization arithmetic and commuting matrix embeddings are
separate statements. The restricted determinant follows from anticommutators
and trace, not Kramers invariance. Floating-point checks support the note's proof.
"""
from itertools import product, permutations
import numpy as np

AUDIT_TIMEOUT_SEC = 120
EPS = 1e-12
PASS_COUNT = FAIL_COUNT = 0


def check(label, condition):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def equal(a, b):
    return np.allclose(a, b, atol=EPS, rtol=0)


def kron(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = np.kron(out, x)
    return out


def main():
    I2, I4, I8 = (np.eye(n, dtype=complex) for n in (2, 4, 8))
    X = np.array([[0, 1], [1, 0]], complex)
    Yp = np.array([[0, -1j], [1j, 0]], complex)
    Z = np.diag([1, -1])
    G = [kron(X, I2, I2), kron(Z, X, I2), kron(Z, Z, X)]
    check('Clifford anticommutators on supplied 8D carrier', all(
        equal(a @ b + b @ a, 2 * (i == j) * I8)
        for i, a in enumerate(G) for j, b in enumerate(G)))
    e12, e13, e23 = G[0] @ G[1], G[0] @ G[2], G[1] @ G[2]
    even = [I8, e12, e13, e23]
    omega = G[0] @ G[1] @ G[2]
    def real_rank(xs):
        a = np.stack([x.reshape(-1) for x in xs], axis=1)
        return np.linalg.matrix_rank(np.concatenate([a.real, a.imag]))
    check('Real even basis has dimension four', real_rank(even) == 4)
    check('Quaternion imaginary units square to -I', all(equal(e @ e, -I8) for e in even[1:]))
    check('Quaternion product and anticommutation', equal(e23 @ e13, e12) and equal(e13 @ e23, -e12))
    check('Central omega squares to -I', equal(omega @ omega, -I8) and all(equal(omega @ g, g @ omega) for g in G))
    check('Adding omega gives real dimension five', real_rank(even + [omega]) == 5)
    u = np.cos(.3) * I8 + np.sin(.3) * omega
    check('Supplied central exponential is unitary', equal(u @ u.conj().T, I8))
    J = [1j * e / 2 for e in [e23, e13, e12]]
    Jf = [kron(I4, s / 2) for s in [X, Yp, Z]]
    for name, js in [('Clifford', J), ('fiber', Jf)]:
        check(name + ' Hermitian su(2) generators', all(equal(j, j.conj().T) for j in js) and all(
            equal(js[i] @ js[j] - js[j] @ js[i], 1j * js[k]) for i, j, k in [(0,1,2),(1,2,0),(2,0,1)]))
        check(name + ' Casimir 3/4', equal(sum(j @ j for j in js), .75 * I8))
    check('Ordinary 8D fiber trace is 2 delta', all(equal(np.trace(a @ b), 2 * (i == j)) for i,a in enumerate(Jf) for j,b in enumerate(Jf)))
    g2sq, gYsq = 1 / real_rank(even), 1 / real_rank(even + [omega])
    check('Supplied reciprocal-dimension prescription gives ratio 4/9', abs(gYsq / (g2sq + gYsq) - 4/9) < EPS)
    def perm(p):
        m = np.zeros((8,8))
        for bits in product(range(2), repeat=3):
            old = sum(bits[i] * 2**(2-i) for i in range(3))
            new = sum(bits[p[i]] * 2**(2-i) for i in range(3))
            m[new, old] = 1
        return m
    swap, cycle = perm([1,0,2]), perm([2,0,1])
    ps, pa = (I8+swap)/2, (I8-swap)/2
    Y = ps/3-pa
    check('Selected symmetric/antisymmetric projectors have ranks 6/2', equal(ps @ ps, ps) and equal(pa @ pa, pa) and np.linalg.matrix_rank(ps)==6 and np.linalg.matrix_rank(pa)==2)
    check('Selected Y spectrum and trace', equal(np.linalg.eigvalsh(Y), [-1,-1]+[1/3]*6) and abs(np.trace(Y))<EPS)
    check('Selected Y commutes with fiber su(2)', all(equal(Y @ j, j @ Y) for j in Jf))
    check('Six supplied coordinate permutations close', all(any(equal(a @ b,c) for c in [perm(p) for p in permutations(range(3))]) for a in [perm(p) for p in permutations(range(3))] for b in [perm(p) for p in permutations(range(3))]))
    check('S3 characters give 4 trivial plus 2 standard modules', equal([np.trace(I8),np.trace(swap),np.trace(cycle)], [8,4,2]))
    ids = [4,2,1]
    check('Three-state cyclic orbit', all(equal(cycle[:,ids[i]], I8[:,ids[(i+1)%3]]) for i in range(3)))
    check('Orbit Y spectrum is not uniform', equal(np.linalg.eigvalsh(Y[np.ix_(ids,ids)]), [-1,1/3,1/3]))
    # Supply standard Gell-Mann generators on a selected complex three-space.
    ts=[]
    for i,j in [(0,1),(0,2),(1,2)]:
        a=np.zeros((3,3),complex);a[i,j]=a[j,i]=.5;ts.append(a)
        a=np.zeros((3,3),complex);a[i,j]=-.5j;a[j,i]=.5j;ts.append(a)
    ts += [np.diag([1,-1,0])/2,np.diag([1,1,-2])/(2*np.sqrt(3))]
    check('Fundamental su(3) trace convention', all(equal(np.trace(a @ b), .5*(i==j)) for i,a in enumerate(ts) for j,b in enumerate(ts)))
    emb=np.array([[1,0,0],[0,0,1/np.sqrt(2)],[0,0,1/np.sqrt(2)],[0,1,0]])
    cs=[kron(emb @ t @ emb.T,I2) for t in ts]
    check('Supplied base su(3) commutes with fiber and selected Y', all(equal(c @ j,j @ c) for c in cs for j in Jf+[Y]))
    check('Embedded su(3) preserves computed structure constants', all(equal(
        cs[a] @ cs[b]-cs[b] @ cs[a],sum(2*np.trace((ts[a] @ ts[b]-ts[b] @ ts[a]) @ ts[c])*cs[c] for c in range(8))) for a in range(8) for b in range(8)))
    lhs=sum(np.einsum('ij,kl->ijkl',t,t) for t in ts)
    rhs=np.array([.5*(i==l)*(k==j)-(i==j)*(k==l)/6 for i,j,k,l in product(range(3),repeat=4)]).reshape(3,3,3,3)
    check('Fundamental Fierz completeness', equal(lhs,rhs))
    check('Adjoint dimension fraction is 8/9', real_rank(ts)==8 and abs(real_rank(ts)/9-8/9)<EPS)
    # Projection fraction varies with the matrix; dimension is not amplitude.
    projection=lambda a:a-np.trace(a)*np.eye(3)/3
    check('Non-universal amplitude controls: identity versus traceless matrix', equal(projection(np.eye(3)),0) and equal(projection(ts[0]),ts[0]))
    ix=[n for n in range(8) if n.bit_count()%2==0]
    js=[j[np.ix_(ix,ix)] for j in J]
    check('Even-parity restriction is invariant', all(equal(j @ np.diag([n in ix for n in range(8)]),np.diag([n in ix for n in range(8)]) @ j) for j in J))
    check('Restricted anticommutators and zero traces', all(equal(a @ b+b @ a,.5*(i==j)*I4) for i,a in enumerate(js) for j,b in enumerate(js)) and all(abs(np.trace(j))<EPS for j in js))
    U=2*js[1]
    check('Normalized T=2J2 K is antiunitary and T squared=-I', equal(U @ U.conj().T,I4) and equal(U @ U.conj(),-I4))
    check('T sends J2 to -J2: generic span element fails invariance', equal(U @ js[1].conj() @ U.conj().T,-js[1]) and not equal(js[1],-js[1]))
    check('Unnormalized J2 K is not antiunitary', not equal(js[1] @ js[1].conj().T,I4))
    for a,b in [(0,[0,0,0]),(2,[0,0,0]),(0,[1,2,3]),(1,[2,0,0]),(-2,[1,-3,2])]:
        B=sum(x*j for x,j in zip(b,js));H=a*I4+B;r2=np.dot(b,b)/4
        check(f'Restricted polynomial determinant at a={a}, b={b}', equal(B @ B,r2*I4) and abs(np.linalg.det(H)-(a*a-r2)**2)<1e-10)
    check('Generic Hermitian negative determinant control', abs(np.linalg.det(np.diag([-1,2,3,4]))+24)<EPS)
    check('Nonnegative determinant does not imply positivity', np.linalg.det(-I4).real>0 and np.max(np.linalg.eigvalsh(-I4))<0)
    print(f'PASS={PASS_COUNT} FAIL={FAIL_COUNT}')
    print('Scope: finite supplied algebra only; physical couplings, species, anomaly cancellation and sheet selection remain unproved.')
    return int(FAIL_COUNT != 0)


if __name__ == '__main__':
    raise SystemExit(main())
