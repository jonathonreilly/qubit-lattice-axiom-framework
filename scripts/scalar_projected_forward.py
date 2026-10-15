"""Full supplied scalar/dust evolution and algebraically projected covariance checks."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scalar_dynamical_forward import candidate

r,k,chi=sp.symbols('r k chi',positive=True)
K=lambda z:r*sp.diff(z,r)
D=lambda z:sp.diff(z,r)/r
E=lambda z:r*r/(4*chi*chi)*(K(z)+2*z)-z
def P(z):
    for shift in [-4,-2,0,2]:z=sp.expand(K(z)+shift*z)
    return z
j0=sp.sin(k*r)/(k*r)
qf=P(E(E(D(j0))))
# Algebraic representations of the common operator, including the geometry commutator; not independent numerical implementations.
eval_kernels=sp.lambdify((r,k,chi),[qf,P(E(E(D(j0)))),P(E(E(D(j0)))),P(E(E(D(j0))+D(j0))),P(E(E(D(j0)))+E(D(j0)))],'numpy',cse=True)
cov=[np.eye(3) for _ in range(5)]
for i,a,b,delta in [(1,0,0,.5),(2,0,1,.25),(3,0,2,.2),(4,1,2,1/6)]:
    cov[i][a,b]+=delta
    if a!=b:cov[i][b,a]+=delta

def validate_protocol(protocol):
    if protocol['Q'] != 1 or protocol['Hv'] != 1:
        raise ValueError('This synthetic implementation uses Q=Hv=1; changed units need a changed implementation')
    if protocol['inverse_rows'] != list(range(5)) or protocol['reserved_row'] != 5:
        raise ValueError('This diagnostic uses the first five rows and reserves row 5')
    if len(protocol['comoving_wavenumbers_over_initial_aE_HE']) != 5 or len(protocol['separation_fractions_of_chi']) != 6:
        raise ValueError('This protocol requires five spectral shells and six separation rows')


def experiment(case, protocol):
    validate_protocol(protocol)
    vals,params=candidate(case['k'],case['nu']);c0=vals(case['u'])
    u0,ud0,rho0=case['u'],case['ud'],case['rho'];ae0=1/c0['A']
    HE0=math.sqrt((c0['K']*ud0*ud0+c0['V']+rho0)/3);s0=c0['cu']*ud0
    C0=HE0+c0['b']*s0;HJ0=C0/c0['A'];km=np.array(protocol['comoving_wavenumbers_over_initial_aE_HE'])*ae0*HE0
    initial=[u0,ud0,rho0,ae0,0.0]
    for i,kk in enumerate(km):
        columns=np.linalg.cholesky(cov[i])*protocol['amplitude']
        for j in range(3):
            S,V,T=columns[:,j];phi=S/2;X=T/(2*c0['b']);v=V/C0
            Z=protocol['amplitude']*HE0*(.1+.07*j-.03*i)
            n=(-(2*(kk/ae0)**2-s0*s0)*phi-s0*Z-(c0['V1']+c0['b']*rho0+3*HE0*s0)*X+3*HE0*rho0*v)/rho0
            initial.extend([phi,X,Z,n,v])
    def rhs(t,state):
        u,ud,rho,ae,_=state[:5];c=vals(u);ss=c['cu']*ud
        H=math.sqrt((c['K']*ud*ud+c['V']+rho)/3)
        udd=-3*H*ud-c['Ku']*ud*ud/(2*c['K'])-c['Uu']/c['K']-c['L']*rho/(2*c['K'])
        out=[ud,udd,(-3*H+c['L']*ud)*rho,H*ae,-1/ae]
        for i,kk in enumerate(km):
            for j in range(3):
                start=5+5*(3*i+j);phi,X,Z,n,v=state[start:start+5];p2=(kk/ae)**2
                pd=-H*phi+(ss*X-rho*v)/2
                out.extend([pd,Z,-3*H*Z-(p2+c['V2']+c['b1']*rho)*X+4*ss*pd-2*(c['V1']+c['b']*rho)*phi-c['b']*rho*(n+c['b']*X),p2*v+3*pd,-phi-c['b']*X-c['b']*ss*v])
        return out
    Tfinal=protocol['duration_times_initial_HE']/HE0;sc=protocol['solver']
    sol=solve_ivp(rhs,(0,Tfinal),initial,method=sc['method'],rtol=sc['rtol'],atol=sc['atol'],max_step=Tfinal*sc['maximum_step_fraction'],dense_output=True)
    if not sol.success:raise RuntimeError(sol.message)
    endpoint=sol.y[4,-1];epochs=[]
    for frac in protocol['epoch_fractions']:
        state=sol.sol(frac*Tfinal);ds=rhs(frac*Tfinal,state);u,ud,rho,ae,rad=state[:5];distance=rad-endpoint
        c=vals(u);ss=c['cu']*ud;HE=math.sqrt((c['K']*ud*ud+c['V']+rho)/3);Cc=HE+c['b']*ss
        sd=-3*HE*ss-c['V1']-c['b']*rho;HEd=-(ss*ss+rho)/2;Ccd=HEd+c['b1']*ss*ss+c['b']*sd
        HJ=Cc/c['A'];aj=c['A']*ae;N=math.log(aj);h=(Ccd-Cc*c['b']*ss)/(Cc*Cc)
        x=-2*c['b']*ss/Cc;q=2*c['b']**2;y=x/q;R=rho*ae**3*c['A']/(3*HJ0**2);J=3*math.exp(-3*N)/(HJ/HJ0)**2;m=J*R
        g=2/(aj*HJ*distance);covs=[];constraint=[]
        for i,kk in enumerate(km):
            values=[];derivs=[]
            for j in range(3):
                start=5+5*(3*i+j);phi,X,Z,n,v=state[start:start+5];pd=ds[start];vd=ds[start+4]
                values.append([2*phi,Cc*v,2*c['b']*X])
                derivs.append([2*pd/Cc,(Ccd*v+Cc*vd)/Cc,2*(c['b1']*ss*X+c['b']*Z)/Cc])
                parts=[(2*(kk/ae)**2-ss*ss)*phi,rho*n,ss*Z,(c['V1']+c['b']*rho+3*HE*ss)*X,-3*HE*rho*v]
                constraint.append(abs(sum(parts))/(sum(map(abs,parts))+1e-30))
            mat=np.array(values).T;dm=np.array(derivs).T;cv=mat@mat.T;dc=dm@mat.T+mat@dm.T;covs.append((cv,dc))
        rows=[];right=[];records=[]
        for factor in protocol['separation_fractions_of_chi']:
            rr=factor*distance;dat=np.zeros(6)
            for kk,(cv,dc) in zip(km,covs):
                qkernel,bkernel,ckernel,geom_one,geom_two=map(float,eval_kernels(rr,kk,distance))
                # U_N=E D C_VV,N+g(E+1)D C_VV; the final subtraction is not optional.
                C1=ckernel*dc[1,1]+g*(geom_one-geom_two)*cv[1,1]
                dat+=np.array([qkernel*cv[0,0],bkernel*cv[0,1],ckernel*cv[1,1],qkernel*dc[0,0],bkernel*dc[0,1],C1])
            A,B,C,A1,B1,C1=dat;row=np.array([A/2,-A/2-B1+(h-1)*B,C1/2+B/2-h*C,B,-C]);target=-A1/2-A
            true=np.array([x,y,y*y,m-x*y/2,m*y]);den=sum(abs(row*true))+abs(target)+1e-300
            residual=(row@true-target)/den;rows.append(row);right.append(target);records.append({'r':rr,'data':dat.tolist(),'identity_scaled':float(residual)})
        mat=np.array(rows[:5]);target=np.array(right[:5]);row_scale=np.maximum(np.max(abs(mat),axis=1),abs(target));scaled=mat/row_scale[:,None]
        try:
            recovered=np.linalg.solve(scaled,target/row_scale);inverse_error=float(max(abs(recovered-np.array([x,y,y*y,m-x*y/2,m*y]))));inverse_status='solved diagnostic'
        except np.linalg.LinAlgError:
            recovered=None;inverse_error=None;inverse_status='singular diagnostic'
        epochs.append({'fraction':frac,'N':N,'chi':distance,'H':HJ,'a':aj,'h':h,'x':x,'y':y,'q':q,'m':m,'constraint_scaled_max':max(constraint),'rows':records,'condition_row_scaled':float(np.linalg.cond(scaled)),'inverse_status':inverse_status,'inverse_absolute_error':inverse_error,'inverse_lift':None if recovered is None else recovered.tolist()})
    checks=[{'name':case['id']+'_constraint_propagation','passed':max(e['constraint_scaled_max'] for e in epochs)<protocol['checks']['constraint_scaled']},{'name':case['id']+'_projected_constraint','passed':max(abs(row['identity_scaled']) for e in epochs for row in e['rows'])<protocol['checks']['projected_identity_scaled']}]
    return {'case':case,'initial_state':initial,'modes':km.tolist(),'epochs':epochs,'checks':checks,'solver':{'success':sol.success,'nfev':sol.nfev,'steps':len(sol.t)}}
