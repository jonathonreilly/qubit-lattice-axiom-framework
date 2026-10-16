from setup import *
for k,G in GROUPS.items():
    print(k, len(G), all(g.det()==1 for g in G))
    # check D adjoint action matches R
    for R in G:
        D=D_of(R)
        assert sp.simplify(D*D.H-sp.eye(2))==sp.zeros(2) and sp.simplify(D.det()-1)==0
        for j in range(3):
            lhs=sp.simplify(D*SIG[j+1]*D.H); rhs=sum((R[i,j]*SIG[i+1] for i in range(3)),sp.zeros(2))
            assert sp.simplify(lhs-rhs)==sp.zeros(2)
    b=covariant_basis(G); print(' cov dim (complex):',len(b))
    # double check basis is covariant via D directly
    basis,z,A=build(G)
    for R in G:
        D=D_of(R)
        for n in NBR:
            Rn=tuple(R*sp.Matrix(n))
            assert sp.simplify(A[Rn]-D*A[n]*D.H)==sp.zeros(2)
    print(' D-check ok')
