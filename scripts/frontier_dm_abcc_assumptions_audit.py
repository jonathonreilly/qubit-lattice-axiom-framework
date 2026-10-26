"""Finite quaternion and supplied-chart checks; no general A-BCC no-go.

No current experimental exclusions or formal audit statuses are inferred.
"""
import numpy as np
import sympy as s

AUDIT_TIMEOUT_SEC = 120

PASS=FAIL=0


def check(name,ok,detail=''):
    global PASS,FAIL
    ok=bool(ok);PASS+=int(ok);FAIL+=int(not ok)
    print(('PASS' if ok else 'FAIL')+': '+name+' '+detail)


def qmul(a,b):
    a0,a1,a2,a3=a;b0,b1,b2,b3=b
    return s.Matrix([a0*b0-a1*b1-a2*b2-a3*b3,
                     a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1,
                     a0*b3+a1*b2-a2*b1+a3*b0])


def quaternion_checks():
    basis=[s.eye(4)[:,j] for j in range(4)]
    left=[s.Matrix.hstack(*(qmul(q,x) for x in basis)) for q in basis]
    right=[s.Matrix.hstack(*(qmul(x,q) for x in basis)) for q in basis]
    C=s.diag(1,-1,-1,-1)
    for j in range(4):
        check('conjugation turns left into right opposite action basis '+str(j),C*left[j]*C==(right[j] if j==0 else -right[j]))
    check('Hamilton units square to -I',all(A*A==-s.eye(4) for A in left[1:]))
    check('Hamilton multiplication ij=k and ji=-k',left[1]*left[2]==left[3] and left[2]*left[1]==-left[3])
    check('left/right actions commute',all(A*B==B*A for A in left for B in right))
    # Direct explicit larger lift; contradicts the old unrestricted obstruction.
    A=s.diag(-1,2,3); Z=s.zeros(3);I=s.eye(3)
    J=Z.row_join(I).col_join((-I).row_join(Z))
    lift=s.diag(A,s.conjugate(A))
    check('six-dimensional lift has antiunitary square -I',J*s.conjugate(J)==-s.eye(6))
    check('six-dimensional lift is T invariant',J*s.conjugate(lift)==lift*J)
    check('quaternionic lift does not imply original positivity',A.det()<0 and lift[0,0]<0 and lift.det()>0)
    check('odd-dimensional antiunitary square determinant obstruction',(-s.eye(3)).det()==-1)
    # Even-dimensional counterexample: T odd generators evade Kramers hypotheses.
    sy=s.Matrix([[0,-s.I],[s.I,0]])
    sz=s.diag(1,-1);U=s.I*sy
    check('normalized spin-half T has square -I',U*s.conjugate(U)==-s.eye(2))
    check('spin generator is T odd, not a Kramers-invariant observable',U*s.conjugate(sz)*U.inv()==-sz and sz.eigenvals()=={s.Integer(1):1,s.Integer(-1):1})
    print('INFO: uniqueness of the irreducible real H module follows from the division-algebra argument in the note, not from a finite PASS count.')


def chart_checks():
    E1=s.sqrt(s.Rational(8,3));E2=s.sqrt(8)/3
    H=s.Matrix([[0,E1,-E1-s.I/2],[E1,0,-E2],[-E1+s.I/2,-E2,0]])
    M=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    D=s.Matrix([[0,-1,1],[-1,1,0],[1,0,-1]])
    Q=s.Matrix([[0,1,1],[1,0,1],[1,1,0]])
    m=s.symbols('m',real=True)
    check('exact baseline determinant is positive',s.simplify(H.det())>0,str(s.simplify(H.det())))
    p=s.Poly(s.expand((H+m*M+E1*Q).det()),m)
    check('fixed chamber ray has negative cubic leading coefficient',p.LC()==-1)
    negative=s.simplify(p.as_expr().subs(m,10))
    check('exact chamber witness delta=0 q=E1 m=10 is negative',negative<0,str(negative))
    h=np.array(H,dtype=complex);mm=np.array(M,float);dd=np.array(D,float);qq=np.array(Q,float)
    def det(m,d,q):return np.linalg.det(h+m*mm+d*dd+q*qq).real
    n=neg=0
    for a in np.linspace(0,5,20):
        for b in np.linspace(0,3,10):
            for c in np.linspace(max(0,float(E1)-b),5,10):
                n+=1;neg+=int(det(a,b,c)<0)
    print(f'INFO: finite chamber sample {neg}/{n} negative; not a chamber measure or general physical exclusion.')
    check('finite chamber sample includes negative witnesses',neg>0)
    basins={'1':(.657061,.933806,.715042),'2':(28.006,20.722,5.012),'X':(21.128264,12.680028,2.089235)}
    for name,(a,b,c) in basins.items():
        values=[det(t*a,t*b,t*c) for t in np.linspace(0,1,1001)]
        print(f'INFO: supplied decimal basin {name}, endpoint={values[-1]}, sampled minimum={min(values)}; no physical solution or interval certificate asserted.')
    print('INFO: opposite endpoint signs imply some continuous-path zero by IVT. A sample of positive values cannot prove full-path nonsingularity.')


def main():
    quaternion_checks();chart_checks()
    print('per_element: real quaternion basis products and exact finite determinant witnesses checked.')
    print('per_site: checked and not executed — no site-local physical law is instantiated.')
    print('per_mode: finite antiunitary symmetry and a T-odd nondegenerate observable were checked.')
    print('per_block: 2, 3, 4 and 6-dimensional supplied matrices; no general physical carrier selection.')
    print('lattice_wide: checked and not executed — no thermodynamic limit or complete source-space classification.')
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
    return int(FAIL>0)


if __name__=='__main__':
    raise SystemExit(main())
