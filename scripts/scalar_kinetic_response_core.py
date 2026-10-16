"""Conditional scalar kinetic controls; computed action/record inputs only."""
AUDIT_TIMEOUT_SEC = 120
import sympy as s
import json, time


def run_checks():
    start=time.monotonic()

    checks=[]

    def zero(name,x):
        x=s.factor(s.simplify(x));checks.append({'name':name,'pass':bool(x==0),'residual':str(x)})

    def truth(name,x):checks.append({'name':name,'pass':bool(x)})

    q,qp,A,F,Fp,E,S,P,J,Jp=s.symbols('q qp A F Fp E S P J Jp',nonzero=True)

    deltaY=A*A*(q*Jp-q*q*P)

    Yp=A*A*q*(qp+q*q)

    QYY=S/(A*A*q*q)

    QYz=(Fp-QYY*Yp)/q

    original=(F+S)*deltaY/(A*A)+(q*q*QYz-E)*J

    Xi=q*Jp-q*q*P-(qp+q*q)*J

    rewrite=F*(q*Jp-q*q*P)+(q*Fp-E)*J+S*Xi

    zero('arbitrary_jet_density_rewrite',original-rewrite)

    zero('transverse_state_displacement',deltaY-(Yp/q)*J-A*A*Xi)

    t=s.symbols('t',positive=True)

    r=s.Rational(5,2)

    A=t**r

    a=t**4

    def dp(f):return s.factor(s.diff(f,t)/A)

    q=r*t**(-r-1)

    ell=s.Rational(3,2)*t**(-r-1)

    R=s.Rational(1,2)*t**-7

    F=s.Rational(2,5)

    E=4*t**-7

    def record(m,j,u,b):
        P=t**m;J=j*P;Z=A*u*t*P;db=b*P
        Xi=s.factor(q*dp(J)-q*q*P-(dp(q)+q*q)*J)
        Bd=s.factor(-6*ell*(dp(P)+ell*P)-F*(q*dp(J)-q*q*P)-(q*dp(F)-E+R)*J)
        V=s.factor(dp(Bd/R)-3*dp(P))
        return {'P':P,'J':J,'Z':Z,'db':db,'Xi':Xi,'Bd':Bd,'V':V}

    rows=[]

    for n in [s.Integer(1),s.Rational(3,2),s.Integer(2)]:
        S=s.Rational(2,5)*(2*n-2);U=s.factor(S/R)
        modes=[(0,s.Rational(5,2),-1,-s.Rational(9,2)),(-s.Rational(5,2),-s.Rational(5,3),s.Rational(2,3),3)]
        m=s.symbols('m')
        roots=s.solve((2*n-1)*(2*m*m+7*m)+6,m)
        for root in roots:
            j=s.factor((2*root*root+10*root+10)/(root+4))
            u=s.factor(2*(j-2*root-3))
            modes.append((root,j,u,s.Integer(3)))
        recs=[record(*mode) for mode in modes]
        for i,rec in enumerate(recs):
            zero(f'n{n}_mode{i}_density',rec['Bd']-S*rec['Xi']-R*rec['db'])
            zero(f'n{n}_mode{i}_coefficient_equation',rec['V']-dp(U)*rec['Xi']-U*dp(rec['Xi']))
            zero(f'n{n}_mode{i}_dust',dp(rec['db'])-3*dp(rec['P']))
        for i in [0,1]:
            zero(f'n{n}_tangent_mode{i}',recs[i]['Xi'])
            truth(f'n{n}_nonzero_metric_mode{i}',recs[i]['P']!=0)
        r1,r2=recs[2:]
        M=s.Matrix([[r1['Xi'],dp(r1['Xi'])],[r2['Xi'],dp(r2['Xi'])]])
        det=s.factor(s.simplify(M.det()))
        truth(f'n{n}_two_record_rank',det!=0)
        sol=list(map(lambda v:s.factor(s.simplify(v)),M.inv()*s.Matrix([r1['V'],r2['V']])))
        zero(f'n{n}_inferred_Uprime',sol[0]-dp(U))
        zero(f'n{n}_inferred_U',sol[1]-U)
        zero(f'n{n}_derivative_consistency',dp(sol[1])-sol[0])
        zero(f'n{n}_inferred_sound_speed',F/(F+R*sol[1])-1/(2*n-1))
        for i,rec in enumerate(recs):
            zero(f'n{n}_density_initial_data_recovered_{i}',(rec['Bd']-R*sol[1]*rec['Xi'])/R-rec['db'])
        clone=s.Matrix([[r1['Xi'],dp(r1['Xi'])],[3*r1['Xi'],3*dp(r1['Xi'])]])
        zero(f'n{n}_same_temporal_mode_rank_failure',clone.det())
        if n!=1:
            truth(f'n{n}_wrong_canonical_curvature_rejected',r1['V']!=0 and r2['V']!=0)
        rows.append({'n':str(n),'determinant':str(det),'U':str(sol[1]),'Uprime':str(sol[0]),'sound_speed_squared':str(s.factor(F/(F+R*sol[1]))),'n_dependent_modes':[str(v) for v in roots]})

    M=s.Matrix([[2,1],[1,3]])

    dM=s.Matrix([[s.Rational(1,100),0],[0,-s.Rational(1,100)]])

    theta=s.Matrix([s.Rational(3,2),-s.Rational(2,3)])

    dV=s.Matrix([s.Rational(1,1000),-s.Rational(1,2000)])

    actual=(M+dM).inv()*(M*theta+dV)-theta

    def norminf(m):
        if m.cols==1:return max(abs(v) for v in m)
        return max(sum(abs(m[i,j]) for j in range(m.cols)) for i in range(m.rows))

    eta=norminf(M.inv()*dM)

    bound=norminf(M.inv())/(1-eta)*(norminf(dV)+norminf(dM)*norminf(theta))

    truth('synthetic_matrix_invertibility_margin',eta<1)

    truth('synthetic_matrix_error_bound',norminf(actual)<=bound)

    return {'scope': 'Conditional action-jet coefficient inverse; constructed action modes only', 'passed': sum((x['pass'] for x in checks)), 'failed': sum((not x['pass'] for x in checks)), 'checks': checks, 'reconstructions': rows, 'synthetic_matrix_error': str(norminf(actual)), 'synthetic_matrix_bound': str(bound)}
