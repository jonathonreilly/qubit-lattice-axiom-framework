#!/usr/bin/env python3
"""Exact Q(sqrt(2), i) certificate; no numerical spectral computation."""
import sympy as s

r = s.sqrt(2)
I = s.I
n = 24

def writer_matrix(x):
    # Arm0: 0..10; arm1: 11..21; ports U,F: 22,23.
    H = s.zeros(n)
    def bond(a, b, hopping, magnitude):
        H[a,a] += magnitude
        H[b,b] += magnitude
        H[a,b] += hopping
        H[b,a] += hopping
    for arm in (0, 1):
        base = 11*arm
        for edge in range(10):
            phase = arm == 1 and edge in (2,5)
            magnitude = r if phase else s.Integer(1)
            bond(base+edge, base+edge+1, -magnitude, magnitude)
            if phase:
                H[base+edge,base+edge] += 2-r
                H[base+edge+1,base+edge+1] += 2-r
    # Hopping block -U, U = [[1,1],[1,-1]]/sqrt(2).
    for a,b,sign in ((10,22,-1),(10,23,-1),(21,22,-1),(21,23,1)):
        bond(a,b,sign/r,1/r)
    # Four vacancies: remove their common scalar and keep -coefficient*n.
    for a in (10,21,22,23):
        H[a,a] -= r-1
    # Shared record X sector at the two terminals.
    for a in (0,11):
        H[a,a] += 1+x
    # Deleted external lead hoppings retain one j diagonal at each port.
    for a in (22,23):
        H[a,a] += 1
    return H.applyfunc(s.simplify)

def exact_zero(M):
    return all(s.simplify(v) == 0 for v in M)

for x in (1,-1):
    H = writer_matrix(x)
    P = s.diag(*([0]*22+[1,1]))
    L = H-2*s.eye(n)-I*P
    inverse = L.inv(method='DM')
    assert exact_zero(L*inverse-s.eye(n))
    assert exact_zero(inverse*L-s.eye(n))
    frobenius_squared = s.simplify(sum(s.conjugate(v)*v for v in inverse))
    # Independent representation check: Hadamard rotation of port coordinates
    # must split the actual positive-block assembly into two twelve-site chains.
    T = s.eye(n)
    T[22,22]=T[22,23]=T[23,22]=1/r
    T[23,23]=-1/r
    rotated = (T.T*L*T).applyfunc(s.simplify)
    left = list(range(11))+[22]
    right = list(range(11,22))+[23]
    assert exact_zero(rotated.extract(left,right))
    assert exact_zero(rotated.extract(right,left))
    chain_totals=[]
    row_certificates=[]
    for indices in (left,right):
        chain=rotated.extract(indices,indices)
        J=chain.inv(method='DM')
        assert exact_zero(chain*J-s.eye(12))
        # Independent continuant formula for each inverse entry.
        diagonal=[chain[a,a] for a in range(12)]
        edge=[chain[a,a+1] for a in range(11)]
        theta=[s.Integer(1),diagonal[0]]
        for a in range(1,12):
            theta.append(s.simplify(diagonal[a]*theta[a]-edge[a-1]**2*theta[a-1]))
        phi=[s.Integer(0)]*13
        phi[12]=1
        phi[11]=diagonal[11]
        for a in range(10,-1,-1):
            phi[a]=s.simplify(diagonal[a]*phi[a+1]-edge[a]**2*phi[a+2])
        for a in range(12):
            for b in range(a,12):
                entry=(-1)**(a+b)*s.prod(edge[a:b])*theta[a]*phi[b+1]/theta[12]
                assert s.simplify(entry-J[a,b])==0
        rows=[s.simplify(sum(s.conjugate(J[a,b])*J[a,b] for b in range(12))) for a in range(12)]
        row_certificates.append(rows)
        chain_totals.append(s.simplify(sum(s.conjugate(v)*v for v in J)))
    assert s.simplify(sum(chain_totals)-frobenius_squared)==0
    assert all(value < 81 for value in chain_totals)
    print('record_X =',x)
    print('exact full inverse residual = 0 (left and right)')
    print('chain Frobenius norm squared =',chain_totals)
    print('chain inverse row norm squares =',row_certificates)
    print('continuant entry checks = exact equality')
    print('full Frobenius norm squared =',frobenius_squared)
    print('determinant =',s.simplify(L.det(method='domain-ge')))
