"""Executable formulas of L1-L26; author candidate, not an independent checker."""
import numpy as np

TIME_SIGN = +1
PROJECTOR_SIGN = -1
CELL_POWER = -0.5
MASS_SIGN = -1
SPACE_SIGN = -1
JW_TAILS = True
EVEN_ONLY = True
WICK_ALTERNATING = True

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.diag([1, -1]).astype(complex)

def couplings(a, m, v):
    sigma = np.sqrt(m*m/4 + v*v/(a*a))
    return sigma/2+m/4, sigma/2-m/4

def discrete_symbol(q, a, m, v):
    g, J = couplings(a, m, v)
    q = np.asarray(q)
    result = np.zeros(q.shape+(2, 2), dtype=complex)
    result[..., 0, 1] = 2j*(g-J*np.exp(-1j*a*q))
    result[..., 1, 0] = -2j*(g-J*np.exp(1j*a*q))
    return result

def continuum_symbol(q, m, v):
    q = np.asarray(q)
    return SPACE_SIGN*v*q[..., None, None]*SX + MASS_SIGN*m*SY

def continuum_position(f, df, m, v):
    return -1j*SPACE_SIGN*v*np.einsum('ij,...j->...i', SX, df) + MASS_SIGN*m*np.einsum('ij,...j->...i', SY, f)

def open_kernel(N, g, J):
    D = np.zeros((2*N, 2*N), dtype=complex)
    for n in range(N):
        D[2*n, 2*n+1] = 2j*g
        D[2*n+1, 2*n] = -2j*g
        if n:
            D[2*n, 2*n-1] = -2j*J
            D[2*n-1, 2*n] = 2j*J
    return D

def unitary(D, t):
    vals, vecs = np.linalg.eigh(D)
    return np.einsum('...ij,...j,...kj->...ik', vecs, np.exp(TIME_SIGN*1j*t*vals), vecs.conj())

def positive(D):
    vals, vecs = np.linalg.eigh(D)
    return np.einsum('...ij,...j,...kj->...ik', vecs, (1+PROJECTOR_SIGN*np.sign(vals))/2, vecs.conj())

def cell_factor(a):
    return a**CELL_POWER

def jw(n, component, N, left=0):
    result = np.ones((1, 1), dtype=complex)
    for j in range(N):
        factor = (SX if component == 0 else SY) if j == n else SZ if JW_TAILS and left <= j < n else np.eye(2)
        result = np.kron(result, factor)
    return result

def claims_endpoint_independence(degree):
    return degree % 2 == 0 if EVEN_ONLY else True

def pfaffian(W):
    if len(W) == 0:
        return 1.0+0j
    answer = 0j
    for j in range(1, len(W)):
        indices = [k for k in range(len(W)) if k not in (0, j)]
        sign = (-1)**(j+1) if WICK_ALTERNATING else 1
        answer += sign*W[0, j]*pfaffian(W[np.ix_(indices, indices)])
    return answer
