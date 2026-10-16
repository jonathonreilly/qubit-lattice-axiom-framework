#!/usr/bin/env python3
"""Exact controls for real-form proof; examples do not replace general proof."""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('docs/INVARIANT_REAL_FORM_FINITE_REPRESENTATION_NOTE_2026-10-16.md',)
import sympy as s

def realify(a):
    return s.BlockMatrix([[s.re(a),-s.im(a)],[s.im(a),s.re(a)]]).as_explicit()

def symmetric_commutant(gens):
    n=gens[0].rows
    variables=s.symbols('c:'+str(n*(n+1)//2))
    m=s.zeros(n);k=0
    for i in range(n):
        for j in range(i,n):m[i,j]=m[j,i]=variables[k];k+=1
    equations=[entry for a in gens for entry in m*a-a*m]
    return m,variables,s.linsolve(equations,variables)

def main():
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
    for generators in ([realify(s.Matrix([[s.I]]))],[realify(s.I*a) for a in (X,Y,Z)]):
        m,variables,solutions=symmetric_commutant(generators)
        solution=next(iter(solutions));resolved=m.subs(dict(zip(variables,solution)))
        assert resolved==resolved[0,0]*s.eye(m.rows)
        assert len(set().union(*(x.free_symbols for x in solution)))==1
    a,b,c,d=s.symbols('a b c d',real=True)
    v=s.Matrix([a+s.I*b,c+s.I*d]);J=s.Matrix([[0,1],[-1,0]])
    assert J*J.conjugate()==-s.eye(2)
    pair=v.col_join(-J*v.conjugate())
    F=s.BlockMatrix([[s.zeros(2),J],[-J,s.zeros(2)]]).as_explicit()
    assert F*F.conjugate()==s.eye(4)
    assert F*pair.conjugate()==pair
    assert (v+v.conjugate())/2+s.I*(v-v.conjugate())/(2*s.I)==v
    # Complexification of real rotations: projection onto the real coordinates.
    rotation=s.Matrix([[0,-1,0],[1,0,0],[0,0,1]])
    P=s.diag(1,1,1,0,0,0)
    assert P**2==P and P.rank()==3 and P*realify(rotation)==realify(rotation)*P
    print('PASS: exact U(1)/SU(2) symmetric commutants, quaternionic pairing, real-form decomposition and real projection.')
    print('General criterion follows from the note proof, not these examples.')
    print('per_element: exact symbolic matrix identities for real, complex and quaternionic examples')
    print('per_site: checked and not executed — representation theorem has no site model')
    print('per_mode: supplied finite representation coordinates only')
    print('per_block: complex and quaternionic examples and doubled real form')
    print('lattice_wide: checked and not executed — no lattice or physical exclusion is claimed')

if __name__=='__main__':main()
