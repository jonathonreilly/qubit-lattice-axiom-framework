"""New bounded exact check of grid, spectral factors and input error budget."""
import json, signal, sys
import sympy as z
signal.alarm(30)
t=z.Symbol('s',real=True)
I=z.eye(2); X=z.Matrix([[0,1],[1,0]]);Y=z.Matrix([[0,-z.I],[z.I,0]]);Z=z.diag(1,-1)
H=X+2*Y+3*Z;C=I+Z;B=I+X+Z
def gramdet(G,port,adjoint=True):
    cols=[];F=port;d=G.rows
    for k in range(1,d*(d-1)+1):
        F=G*F-F*G;cols.append(F)
    return z.factor(z.Matrix([[z.trace((A.H if adjoint else A)*D) for D in cols] for A in cols]).det())
p=gramdet(H+t*C,B)
S=t*t+6*t+14;R=t*t+4*t+12
assert z.expand(p-256*S*R**2)==0
assert H*C-C*H!=z.zeros(2)
assert gramdet(C,B)==256
assert z.expand(gramdet(H+t*C,B,False)+p)==0
d=2;m=2;D=6;qpair=1
Lam=z.Rational(1,8);Lam0=z.Integer(1);a0=z.Integer(256)
nodes=[Lam*(z.Rational(1,2)+z.Rational(j,2*(D+1))) for j in range(D+1)]
vals=[p.subs(t,s) for s in nodes]
step=Lam/(2*(D+1))
fd=sum((-1)**(D-j)*z.binomial(D,j)*vals[j] for j in range(D+1))
assert fd==a0*z.factorial(D)*step**D
assert fd!=a0*z.factorial(D)*step**D/Lam  # wrong Lambda exponent
AV=z.Integer(4*(D+1))**D/z.factorial(D)
L=a0*Lam**D/AV
assert max(vals)>=L and all(0<s<Lam for s in nodes)
K=z.Integer(6);b=z.Integer(3);U=2*(K+1);v=b+1
A_det=2*m*(m*d)**m*v**(2*m-1)*U**(2*m*m)
C_eval=A_det*(1+2*m*b*(1+Lam0)/U)
delta=min(1/(1+Lam0),L/(8*C_eval))
Ht=H+delta*X;Ct=C+delta*I;Bt=B+delta*Z
approx=[gramdet(Ht+s*Ct,Bt) for s in nodes]
errors=[abs(aa-vv) for aa,vv in zip(approx,vals)]
assert all(e<=C_eval*delta and e<=L/8 for e in errors)
accepted=[j for j,aa in enumerate(approx) if aa-L/8>L/2]
assert accepted
j=accepted[0];selected=nodes[j]
assert vals[j]>L/2
Ss=S.subs(t,selected);Rs=R.subs(t,selected)
G=H+selected*C;T=G-selected*I
assert z.simplify(T*T-Ss*I)==z.zeros(2)
Pplus=(I+T/z.sqrt(Ss))/2;Pminus=(I-T/z.sqrt(Ss))/2
off2=z.simplify(z.trace(Pplus*B*Pminus*B))
assert off2==Rs/Ss
gap2=4*Ss;sep2=16*Ss
factor=z.simplify(off2**2*gap2**2*sep2)
assert factor==vals[j]
low_b2=(L/2)/(b**(2*(m-1))*(2*K)**(2*m)*(4*K)**(2*qpair))
low_g2=(L/2)/(b**(2*m)*(2*K)**(2*(m-1))*(4*K)**(2*qpair))
low_sep2=(L/2)/(b**(2*m)*(2*K)**(2*m)*(4*K)**(2*(qpair-1)))
assert off2>=low_b2 and gap2>=low_g2 and sep2>=low_sep2
assert gramdet(z.zeros(2),B)==0
assert gramdet(Z,I+Z)==0
assert gramdet(z.diag(0,1,2),z.ones(3))==0
bits=0
while z.Rational(2*d,2**bits)>delta:bits+=1
print(json.dumps({
 'role':'Exposed same-model exact discriminator; not universal proof or physical calibration',
 'python':sys.version,'sympy':z.__version__,
 'p':str(p),'leading_coefficient':256,'degree':6,
 'Lambda':str(Lam),'nodes':[str(s) for s in nodes],
 'all_exact_values':[str(a) for a in vals],
 'finite_difference':str(fd),'wrong_grid_exponent_rejected':True,
 'L':str(L),'A_D':str(AV),'K':str(K),'b':str(b),
 'A_det':str(A_det),'C_eval':str(C_eval),'matrix_operator_error_delta':str(delta),
 'requested_real_imag_bits':bits,'max_error_over_allowed_L_over_8':str(max(errors)/(L/8)),
 'selected_index':j,'selected_s':str(selected),
 'selected_value':str(vals[j]),'actual_squared_transition_magnitude':str(off2),
 'actual_squared_nonzero_gap':str(gap2),'actual_squared_signed_gap_separation':str(sep2),
 'certified_squared_transition_lower_bound':str(low_b2),
 'certified_squared_gap_lower_bound':str(low_g2),
 'certified_squared_signed_separation_lower_bound':str(low_sep2),
 'spectral_factorization_exact':True,'omitted_adjoint_mutant_equals_minus_p':True,
 'zero_gap_missing_transition_repeated_gap_cases_rejected':True,
 'limits':{'child_alarm_seconds':30,'physical_dimension_max':3,'Gram_dimension_max':6},
 'all_assertions_passed':True
},indent=2))
