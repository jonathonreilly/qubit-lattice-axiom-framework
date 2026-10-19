"""Exact coefficient certificate for the supplied finite corner reflection.

Input is the integer cell graph and GF(2) solution, not fitted spectral data.
No finite differences, numerical rounding, or historical check results enter.
"""
# Execution occurs inside the owning primary and inherits its actual 600-second timer.
AUDIT_TIMEOUT_SEC = 600

import sympy as sp


def certificate(corners, edge_types, flux_bits):
    index = {corner: i for i, corner in enumerate(corners)}
    n = len(corners)
    assert n == 12 and len(edge_types) == len(flux_bits)
    onsite = sp.zeros(n)
    link = sp.zeros(n)
    derivative = [sp.zeros(n) for _ in range(3)]
    shifts = {}
    for (a, b, displacement), bit in zip(edge_types, flux_bits):
        bit = int(bit)
        assert bit in (0, 1)
        amplitude = -(-1)**bit
        ia, ib = index[a], index[b]
        if displacement == (0, 0, 0):
            onsite[ib, ia] += amplitude
            onsite[ia, ib] += amplitude
            continue
        # The Fourier convention is H_ba(k)=amp exp(i k.d).
        d = tuple(int(x) for x in displacement)
        phase = sp.I ** ((d[0] - d[1] + d[2]) % 4)
        link[ib, ia] += amplitude * phase
        link[ia, ib] += amplitude / phase
        for axis in range(3):
            derivative[axis][ib, ia] += sp.I * d[axis] * amplitude * phase
            derivative[axis][ia, ib] -= sp.I * d[axis] * amplitude / phase
        for shift, row, col in ((d, ib, ia), (tuple(-x for x in d), ia, ib)):
            if shift not in shifts:
                shifts[shift] = sp.zeros(n)
            shifts[shift][row, col] += amplitude
    # Full Laurent convolution proves the link-square identity for every k.
    square = {}
    for a, A in shifts.items():
        for b, B in shifts.items():
            shift = tuple(x+y for x, y in zip(a, b))
            square[shift] = square.get(shift, sp.zeros(n)) + A*B
    assert all(M == (2*sp.eye(n) if d == (0,0,0) else sp.zeros(n)) for d, M in square.items())
    assert all(M.trace() == 0 for M in shifts.values())
    vectors = (onsite-2*sp.eye(n)).nullspace()
    assert len(vectors) == 4
    B = sp.Matrix.hstack(*vectors)
    P = B*(B.H*B).inv()*B.H
    U = sp.eye(n)-2*P
    assert U*U == sp.eye(n)
    W = link*U/sp.sqrt(2)
    vectors = (W-sp.eye(n)).nullspace()
    assert len(vectors) == 6
    N = sp.Matrix.hstack(*vectors)
    Ginv = (N.H*N).inv()
    # Coordinates in a possibly nonorthogonal exact kernel basis.
    # -i W^dagger dW is Hermitian in the physical inner product.
    first = [sp.simplify(Ginv*N.H*(-sp.I)*U*link.H*D*U*N/2) for D in derivative]
    q = sp.symbols('q_x q_y q_z', real=True)
    M = sum((x*A for x, A in zip(q, first)), sp.zeros(6))
    norm2 = sum(x*x for x in q)
    cubic = (M**3 - norm2*M/3).applyfunc(sp.expand)
    assert cubic == sp.zeros(6)
    assert sp.expand(sp.trace(M)) == 0
    assert sp.expand(sp.trace(M*M)-4*norm2/3) == 0
    # These traces plus the cubic identity give multiplicities 2,2,2
    # for 0,+|q|/sqrt(3),-|q|/sqrt(3), for real q != 0.
    return {
        'onsite': onsite,
        'reflection': U,
        'link_at_fixed_momentum': link,
        'first_order_matrices': first,
        'node_dimension': N.cols,
        'laurent_square_coefficients': len(square),
        'trace_square': str(sp.expand(sp.trace(M*M))),
        'cubic_residual': str(cubic),
    }
