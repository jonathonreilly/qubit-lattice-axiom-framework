"""Finite conditional diagnostics; no gravity-phase no-go or Newton verification.

Inputs are supplied matrices, product states, four historical comparison numbers,
and three historical mass anchors. No files, ledger, gravity runner, physical
Laplacian, Green function, or gravitational self-consistency equation are read.
See the paired note for exact hypotheses and the non-identifiability proof.
"""
import numpy as np

U = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
OMEGA = np.exp(2j * np.pi / 3)


def circulant(a, b):
    return a * np.eye(3) + b * U + np.conj(b) * U.conj().T


def main():
    results = []

    def check(label, predicate):
        ok = bool(predicate)
        results.append(ok)
        print(('PASS' if ok else 'FAIL') + ': ' + label)

    a, b = 1., 1 / np.sqrt(2.)
    H = circulant(a, b)
    check('supplied circulant is Hermitian and C3 equivariant',
          np.allclose(H, H.conj().T) and np.allclose(H @ U, U @ H))
    eig = np.linalg.eigvalsh(H)
    expected = sorted(a + 2*b*np.cos(2*np.pi*k/3) for k in range(3))
    check('three supplied eigenvalues match formula', np.allclose(eig, expected, atol=1e-10))
    check('supplied target gives Frobenius coefficient equipartition',
          abs((np.trace(H @ H).real-3*a*a)/(3*a*a)-1) < 1e-10)
    check('supplied target gives Brannen c squared = 2', abs((2*b/a)**2-2) < 1e-10)
    F = np.column_stack([np.ones(3), [1, OMEGA, OMEGA**2],
                         [1, OMEGA**2, OMEGA]]) / np.sqrt(3)
    v = F @ np.array([1, b, b])
    check('conjugate Fourier pair gives real vector', np.allclose(v.imag, 0))
    masses = v.real**2
    check('chosen positive branch has physical Koide Q = 2/3',
          np.all(v.real > 0) and abs(masses.sum()/np.sqrt(masses).sum()**2-2/3) < 1e-10)
    # Signed roots alone do not guarantee the physical absolute-root identity.
    vs = F @ np.array([1, b*np.exp(1j*np.pi/3), b*np.exp(-1j*np.pi/3)])
    qs = np.sum(vs.real**2)/np.sum(np.abs(vs.real))**2
    check('mixed-sign branch refutes unrestricted physical-Q equivalence', abs(qs-2/3) > 1e-3)

    # A is deliberately an arbitrary finite matrix, not a lattice operator.
    A = np.array([[2, -1], [-1, 3]], dtype=float)
    lifted = np.kron(A, np.eye(3))
    for r in [.1, .3, .5, .8, 1.5]:
        h = np.kron(np.eye(2), circulant(1, np.sqrt(r)))
        check(f'tensor-factor commutator vanishes at supplied ratio {r}',
              np.allclose(lifted @ h-h @ lifted, 0))

    # Scalar source sums flavor components. This assumption is essential.
    va = F @ np.array([1, b, b])
    zb = np.sqrt((np.vdot(va, va).real-.25)/2)
    vb = F @ np.array([.5, zb, zb])
    na, nb = np.vdot(va, va).real, np.vdot(vb, vb).real
    check('two flavor vectors have equal norm', abs(na-nb) < 1e-10)
    check('their coefficient ratios differ', abs(b*b-zb*zb/.25) > 1e-3)
    psi = np.array([1, 2j])/np.sqrt(5)
    ra = np.sum(np.abs(psi[:, None]*va[None, :])**2, axis=1)
    rb = np.sum(np.abs(psi[:, None]*vb[None, :])**2, axis=1)
    check('flavor-summed scalar Born sources coincide', np.allclose(ra, rb))
    check('same arbitrary linear map gives equal outputs', np.allclose(A @ ra, A @ rb))
    # A component-sensitive positive observable distinguishes them without
    # changing the Born rule or probability conservation.
    P = np.outer(F[:, 0], F[:, 0].conj())
    check('positive flavor projector distinguishes the normalized states',
          abs(np.vdot(va, P @ va).real/na-np.vdot(vb, P @ vb).real/nb) > 1e-3)

    check('only trivial Z2^3 to C3 generator images satisfy order two',
          [k for k in range(3) if (2*k) % 3 == 0] == [0])
    check('only trivial C3 to Z2^3 image satisfies order three',
          [x for x in range(8) if x ^ x ^ x == 0] == [0])
    # Coordinate cyclic permutation is an additional symmetry, not a
    # homomorphism from Z2^3. Thus group mismatch is not a universal barrier.
    corners = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    C = np.zeros((8, 8))
    for j, (x, y, z) in enumerate(corners):
        C[corners.index((z, x, y)), j] = 1
    hw1 = [corners.index(t) for t in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    check('cube coordinate permutation has C3 action on hw=1',
          np.array_equal(C @ C @ C, np.eye(8)) and np.array_equal(C[np.ix_(hw1, hw1)], U))

    supplied = [-1., 1.21, -.58, np.log(2)]
    check('four supplied historical numbers are not 1/2 at tolerance 1e-3',
          all(abs(x-.5) > 1e-3 for x in supplied))
    check('their ordered distinct pairwise ratios are not 1/2 at tolerance 1e-3',
          all(abs(x/y-.5) > 1e-3 for i,x in enumerate(supplied)
              for j,y in enumerate(supplied) if i != j and abs(y)>1e-12))
    m = np.array([.5109989461, 105.6583745, 1776.86])
    q = m.sum()/np.sqrt(m).sum()**2
    print(f'Historical mass anchor only: Q={q:.12f}, absolute residual={abs(q-2/3):.6g}')
    # N5 resolution report only; no new checks or scientific verdict.
    print('per_element: The supplied 3 by 3 circulant is checked entrywise for Hermiticity and commutation; the two scalar source components are compared with NumPy allclose. These are floating-point finite checks, not exact symbolic certification.')
    print('per_site: The spatial state has exactly two supplied components, with probabilities 1/5 and 4/5. Flavor probabilities are summed separately at each component; no lattice neighbor relation or spatial field equation is supplied.')
    print('per_mode: Three supplied C3 Fourier vectors construct the flavor states; the three real-b circulant eigenvalues are compared to their cosine formula. A mixed-sign phase example checks the physical absolute-root limitation.')
    print('per_block: The 2 by 2 arbitrary matrix and 3 by 3 circulants are lifted to 6 by 6 tensor-product matrices. Their commutators are checked at five supplied ratios; factorization and flavor blindness are assumptions.')
    print('lattice_wide: No physical lattice Laplacian, Green function, gravitational iteration, volume scan, continuum limit, or Newton self-consistency is computed. The result is only finite scalar-source non-identifiability under the stated product-state and flavor-sum hypotheses.')
    print('NOT VERIFIED: physical gravity, Laplacian/Green inversion, Newton constant,')
    print('self-consistency, ledger status, exhaustive induction maps, or five-route no-go.')
    print(f'Total: {sum(results)} PASS / {len(results)-sum(results)} FAIL')
    return 0 if all(results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
