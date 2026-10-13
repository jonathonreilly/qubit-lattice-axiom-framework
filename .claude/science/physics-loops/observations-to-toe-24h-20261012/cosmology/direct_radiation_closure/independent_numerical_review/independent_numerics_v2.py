#!/usr/bin/env python3
"""Reviewer-owned recomputation; no author module imports or calls.

Positive evidence uses z=S**(1/6), canonical field derivatives/velocities,
high-precision quadrature and independent Planck phase-space normalization.
Author RESULTS.json is comparison data only. All outputs are exclusive writes.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, math, hashlib, sys
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp, quad

ROOT=Path(__file__).resolve().parent
SNAP=ROOT/'snapshot'
FIX=json.loads((SNAP/'NUMERICAL_FIXTURES_v1.json').read_text())
AUTHOR=json.loads((SNAP/'evidence_v1/RESULTS.json').read_text())
mp.mp.dps=100
CHECKS=[]

def m(x): return mp.mpf(str(x))
def s(x): return mp.nstr(x,95)
def ck(name,ok,**data): CHECKS.append(dict(name=name,passed=bool(ok),**data))
def compare(name,got,expected,atol='0',rtol='3e-12'):
    got,expected=m(got),m(expected)
    error=abs(got-expected);bound=m(atol)+m(rtol)*abs(expected)
    ck(name,mp.isfinite(got) and error<=bound,error=s(error),bound=s(bound),got=s(got),expected=s(expected))

def thermal():
    h,k,c,G=[m(FIX['constants'][x])for x in ['h_Js','k_J_per_K','c_m_per_s','G_N_SI']]
    H0=m(FIX['H0_km_per_s_Mpc'])*1000/m(FIX['constants']['Mpc_m'])
    # Two photon polarizations, d^3p/(2*pi*hbar)^3, E=cp.
    integrals=[mp.quad(lambda x:x**j/mp.expm1(x),[0,1,5,20,mp.inf])for j in [2,3]]
    for j,num in zip([2,3],integrals):compare('phase space Bose integral '+str(j),num,mp.gamma(j+1)*mp.zeta(j+1),rtol='1e-90')
    rows=[]
    for row in AUTHOR['thermal']['thermal_rows']:
        T=m(FIX['temperature_K'])+row['sigma_shift']*m(FIX['temperature_sigma_K'])
        energy=mp.pi**2*(k*T)**4/(15*(h/(2*mp.pi))**3*c**3)
        number=2*mp.zeta(3)/mp.pi**2*(k*T/(h/(2*mp.pi)*c))**3
        rho=energy/c**2;omega=8*mp.pi*G*rho/(3*H0**2)
        vals={'temperature_K':T,'energy_J_per_m3':energy,'mass_density_kg_per_m3':rho,'number_per_m3':number,'Omega_gamma':omega}
        for key,v in vals.items():compare('thermal '+str(row['sigma_shift'])+' '+key,row[key],v,rtol='2e-14')
        rows.append({k:s(v)for k,v in vals.items()})
    compare('H0',AUTHOR['thermal']['H0_s_inverse'],H0,rtol='1e-15')
    parsed=[]
    for line in (SNAP/'data/FIRAS_monopole.txt').read_text().splitlines():
        if line.strip() and not line.startswith('#'):parsed.append([m(v)for v in line.split()])
    ck('43 source table rows',len(parsed)==43)
    T=m(FIX['baseline_temperature_K'])
    # Algebra expressed directly in spatial wavenumber rather than frequency.
    def bb(w):return 2*h*c*(100*w)**3/mp.expm1(h*c*100*w/(k*T))/m('1e-20')
    wpeak=mp.findroot(lambda w:mp.diff(bb,w),[m('5'),m('6')])
    table=[];chi2=mp.mpf(0);weights=mp.mpf(0)
    keys=['wavenumber_cm_inverse','absolute_MJy_per_sr','residual_kJy_per_sr','sigma_kJy_per_sr','galaxy_kJy_per_sr']
    for i,(w,I,res,err,gal) in enumerate(parsed):
        pubs=AUTHOR['thermal']['FIRAS_rows'][i]
        for key,val in zip(keys,[w,I,res,err,gal]):compare('FIRAS source cell '+str(i)+' '+key,pubs[key],val,rtol='0')
        lo_w=w-m('.005');hi_w=w+m('.005')
        nodes=[lo_w,hi_w]+([wpeak]if lo_w<=wpeak<=hi_w else [])
        vals=[bb(q)for q in nodes];lo=min(vals)+res/1000-m('.001');hi=max(vals)+res/1000+m('.001')
        ck('FIRAS independent rounding '+str(i),lo<=I<=hi and err>0,lower=s(lo),upper=s(hi),observed=s(I))
        compare('FIRAS stored lower '+str(i),pubs['rounded_baseline_interval'][0],lo,atol='4e-12',rtol='1e-14')
        compare('FIRAS stored upper '+str(i),pubs['rounded_baseline_interval'][1],hi,atol='4e-12',rtol='1e-14')
        table.append({'row':i,'lower':s(lo),'upper':s(hi),'minimum_margin':s(min(I-lo,hi-I))})
        chi2+=(res/err)**2;weights+=1/err**2
    compare('FIRAS residual diagonal sum',AUTHOR['thermal']['FIRAS_diagonal_residual_sum_only'],chi2,rtol='1e-14')
    compare('FIRAS residual weighted rms',AUTHOR['thermal']['FIRAS_weighted_RMS_kJy_per_sr'],mp.sqrt(chi2/weights),rtol='1e-14')
    return {'thermal':rows,'H0':s(H0),'FIRAS_rows':table,'FIRAS_peak_wavenumber':s(wpeak),'diagonal_sum':s(chi2),'weighted_rms':s(mp.sqrt(chi2/weights))}

def canonical_functions(a,b,L):
    # z=S**(1/6); its canonical Jacobian follows directly from Sdot and chidot.
    def S(z):return z**6
    def R(z):return b*z**8
    def H2(z):return mp.mpf(2)/3*((1+a)*(S(z)+R(z))+L)
    def J(z):return -2*mp.sqrt(a)*z**2*mp.sqrt(1+4*b*z*z/3)/mp.sqrt(H2(z))
    def U(z):return L+a*S(z)/2+a*R(z)/3
    def dc(f,z):return mp.diff(f,z)/J(z)
    def C2(z):return dc(lambda q:dc(U,q),z)
    def M(z):return a*dc(S,z)**2/C2(z)+a*S(z)**2/U(z)
    return S,R,H2,J,U,dc,C2,M

def grid():
    out=[]
    for i,row in enumerate(AUTHOR['local_grid']):
        a,b,L=map(m,[row['a'],row['R_over_S'],row['L_over_S']]);z=mp.mpf(1)
        S,R,H2,J,U,dc,C2,M=canonical_functions(a,b,L)
        g=(z*J(z)/6)**2
        Gamma=z*mp.diff(lambda t:mp.log((t*J(t)/6)**2),z)/12
        Uq=z*mp.diff(U,z)/6
        Uqq=z*mp.diff(lambda t:t*mp.diff(U,t)/6,z)/6
        vals={'S':S(z),'R':R(z),'W':S(z)+4*R(z)/3,'C':3*H2(z)/2,'H2':H2(z),'g':g,'Gamma':Gamma,'U':U(z),'Uq':Uq,'Uqq':Uqq,'Uchichi':C2(z),'M':M(z)}
        for key,v in vals.items():compare('grid '+str(i)+' '+key,row['local'][key],v,atol='2e-15',rtol='2e-13')
        A=M(z)/H2(z);D=C2(z)/H2(z);B=-mp.sqrt(a)*dc(S,z)/H2(z)
        det=A*D-B*B;high=(A+D+mp.sqrt((A-D)**2+4*B*B))/2;low=det/high
        ck('canonical Hessian positivity '+str(i),A>0 and D>0 and det>0 and low>0,det=s(det),min_eigenvalue=s(low))
        compare('grid low eigenvalue '+str(i),row['eigenvalues_over_H2'][0],low,atol='1e-14',rtol='2e-10')
        compare('grid high eigenvalue '+str(i),row['eigenvalues_over_H2'][1],high,rtol='2e-13')
        minimum=U(z)-a*S(z)**2/(2*M(z));ck('global actual minimum '+str(i),minimum>=U(z)/2,minimum=s(minimum),bound=s(U(z)/2))
        test_values=[]
        for u in map(m,[-10,-1,-math.sqrt(float(a)),0,math.sqrt(float(a)),1,10]):
            V=U(z)-mp.sqrt(a)*S(z)*u+M(z)*u*u/2;ck('sample lower bound '+str(i),V>=U(z)/2)
            test_values.append({'u':s(u),'V':s(V)})
        out.append({'row':i,'min_eigenvalue':s(low),'max_eigenvalue':s(high),'minimum_over_U':s(minimum/U(z)),'sample_values':test_values})
    return out

def old_residue():
    out=[]
    for i,row in enumerate(AUTHOR['old_potential']):
        a,S0,R0,L=map(m,[row['a'],row['S'],row['R'],FIX['old_potential_L']])
        # Differentiate along N directly, conserving both fluids independently.
        def fried(N):
            S=S0*mp.exp(-3*N);R=R0*mp.exp(-4*N)
            Hd=2*((1+a)*S+L)/3
            return Hd*(1+2*R/((2+a)*S+2*L))
        F=fried(0);Hd=2*((1+a)*S0+L)/3
        ray=-S0-4*R0/3-a*S0*F/Hd
        exact=(mp.diff(fried,0)/2-ray)/F
        closed=2*a*R0*S0*((2+a)*S0-L)/(3*((2+a)*S0+2*L)**2*F)
        compare('old high precision derivative identity '+str(i),exact,closed,rtol='1e-85')
        compare('old stored closed residue '+str(i),row['residual_over_H2'],exact,rtol='2e-14')
        compare('old stored subtractive residue '+str(i),row['derivative_residual_over_H2'],exact,atol='3e-14',rtol='2e-10')
        tol=m('3e-14')+m('2e-10')*abs(m(row['derivative_residual_over_H2']))
        ck('old residue zero is rejected '+str(i),abs(m(row['derivative_residual_over_H2']))>tol)
        out.append({'row':i,'a':row['a'],'z':row['z'],'independent':s(exact),'float_subtraction_relative_error':s(abs(m(row['derivative_residual_over_H2'])/exact-1)),'zero_rejection_tolerance_units':s(abs(m(row['derivative_residual_over_H2']))/tol)})
    return out

def fast_local(ell,a,b,L):
    # Independent log(z) coordinate, with canonical rather than coordinate velocity.
    S=np.exp(6*ell);R=b*np.exp(8*ell);W=S+4*R/3;H2=2*((1+a)*(S+R)+L)/3
    U=L+a*S/2+a*R/3
    Uell=3*a*S+8*a*R/3;Uell2=18*a*S+64*a*R/3
    D=-2*np.sqrt(a*W/H2)
    Dlog=((6*S+32*R/3)/W-4*(1+a)*W/H2)/2
    curvature=(Uell2-Dlog*Uell)/D**2
    M=a*(6*S/D)**2/curvature+a*S*S/U
    return S,R,W,H2,U,Uell,D,Dlog,M

def canonical_rhs(N,y,a,b,L):
    u,ell,vu,vc,lm,lr,chi=y
    S,R,W,Hb,U,Uell,D,Dlog,M=fast_local(ell,a,b,L)
    Mell=np.imag(fast_local(ell+1e-25j,a,b,L)[-1])/1e-25
    V=U-np.sqrt(a)*S*u+M*u*u/2
    Vu=-np.sqrt(a)*S+M*u
    Vell=Uell-6*np.sqrt(a)*S*u+Mell*u*u/2
    sm,sr=np.exp(lm),np.exp(lr)
    denominator=3-vu*vu-vc*vc
    H2=2*(sm+sr+V)/denominator
    if denominator<=0 or H2<=0:raise ValueError('nonpositive independent Friedmann domain')
    h=-(sm+4*sr/3)/H2-vu*vu-vc*vc
    return np.array([vu,vc/D,-(3+h)*vu-(Vu+np.sqrt(a)*sm)/H2,-(3+h)*vc-Vell/(D*H2),-3+np.sqrt(a)*vu,-4.,vc])

def histories():
    out=[];operator=[]
    for i,row in enumerate(AUTHOR['new_background']):
        a,b,L,S0,R0=[row[k]for k in ['a','b','L','S0','R0']];sites=np.array(row['sites_N']);n0=sites[0]
        target=np.array([[0,np.log(S0)-3*n,0,-3,np.log(S0)-3*n,np.log(R0)-4*n]for n in sites])
        stored_target=np.array(row['target_states'])
        ck('stored target '+str(i),np.max(abs(target-stored_target))<2e-13,max_error=float(np.max(abs(target-stored_target))))
        for j,run in enumerate(row['runs']):
            vals=np.array(run['states']);tol=2e-8+2e-7*np.maximum(abs(vals),abs(target));units=np.max(abs(vals-target)/tol)
            compare('stored run units '+str(i)+'/'+str(j),run['max_tolerance_units'],units,atol='5e-8',rtol='1e-8')
            ck('stored every state within tolerance '+str(i)+'/'+str(j),units<1,max_units=float(units),components=vals.size)
        independent_quad=[]
        for j,q in enumerate(row['canonical_coordinates']):
            def integrand(N):
                S=S0*np.exp(-3*N);R=R0*np.exp(-4*N)
                return np.sqrt(a*(S+4*R/3)/(2*((1+a)*(S+R)+L)/3))
            chi,err=quad(integrand,0,sites[j],epsabs=2e-14,epsrel=2e-13)
            compare('canonical N integral '+str(i)+'/'+str(j),q['chi_minus_chi_present'],chi,atol='3e-12',rtol='2e-13')
            S,R,W,H2,U,Uell,D,Dlog,M=fast_local(np.log(S0)/6-sites[j]/2,a,b,L)
            speed=np.sqrt(W/H2);slope=-Uell/(U*D)
            compare('canonical speed '+str(i)+'/'+str(j),q['field_speed_over_sqrt_a'],speed,rtol='2e-13')
            compare('canonical slope '+str(i)+'/'+str(j),q['potential_slope_minus_dlogU_dchi'],slope,rtol='2e-13')
            independent_quad.append(chi)
            # Explicit nearby non-solution; do not enforce p=-3 in the canonical EOM.
            ell=np.log(S0)/6-sites[j]/2
            base=fast_local(ell,a,b,L)
            yy=np.array([.003*np.sqrt(a),ell+.001,.004*np.sqrt(a),1.03*np.sqrt(a*base[2]/base[3]),np.log(S0)-3*sites[j]+.02,np.log(R0)-4*sites[j]-.01,0.])
            rr=canonical_rhs(sites[j],yy,a,b,L)
            D=fast_local(yy[1],a,b,L)[6];Dl=fast_local(yy[1],a,b,L)[7]
            pprime=6*(rr[3]-yy[3]*Dl*rr[1])/D
            ck('nonzero canonical off-trajectory p acceleration '+str(i)+'/'+str(j),abs(pprime)>1e-6,p_acceleration=float(pprime))
            operator.append({'a':a,'N':float(sites[j]),'canonical_state':yy.tolist(),'canonical_rhs':rr.tolist(),'p_acceleration':float(pprime)})
        ell0=np.log(S0)/6-n0/2;z0=fast_local(ell0,a,b,L)
        initial=np.array([0.,ell0,0.,np.sqrt(a*z0[2]/z0[3]),np.log(S0)-3*n0,np.log(R0)-4*n0,independent_quad[0]])
        sol=solve_ivp(lambda n,y:canonical_rhs(n,y,a,b,L),(n0,6),initial,method='RK45',rtol=2e-12,atol=1e-16,max_step=.01,t_eval=sites)
        ck('independent canonical RK45 success '+str(i),sol.success,nfev=sol.nfev,message=sol.message)
        vals=sol.y.T;converted=[];denoms=[]
        for y in vals:
            u,ell,vu,vc,lm,lr,chi=y;D=fast_local(ell,a,b,L)[6]
            converted.append([u,6*ell,vu,6*vc/D,lm,lr]);denoms.append(3-vu*vu-vc*vc)
        converted=np.array(converted);tol=2e-8+2e-7*np.maximum(abs(converted),abs(target));units=np.max(abs(converted-target)/tol)
        ck('independent canonical trajectory '+str(i),units<1,max_units=float(units),max_abs_error=float(np.max(abs(converted-target))))
        compare('independent integrated chi '+str(i),np.max(abs(vals[:,-1]-np.array(independent_quad))),0,atol='3e-10',rtol='0')
        ck('independent denominator positive '+str(i),min(denoms)>0,minimum=min(denoms))
        out.append({'a':a,'method':'RK45 canonical velocities/log(S**(1/6))','nfev':sol.nfev,'states':vals.tolist(),'converted_states':converted.tolist(),'N_quadrature_chi':independent_quad,'max_tolerance_units':float(units),'min_denominator':min(denoms)})
    return {'histories':out,'off_trajectory_controls':operator}

def endpoint():
    out=[]
    for i,row in enumerate(AUTHOR['endpoint']):
        a,b,L=map(m,[row['a'],row['b'],row['L']]);Hv=mp.sqrt(2*L/3);scale=2*mp.sqrt(a)/(3*Hv)
        S,R,H2,J,U,dc,C2,M=canonical_functions(a,b,L)
        compare('endpoint scale '+str(i),row['canonical_endpoint_scale'],scale,rtol='1e-65')
        rows=[]
        for j,data in enumerate(row['series']):
            sigma=m(data['S']);z=sigma**(mp.mpf(1)/6)
            # Scale to the fixed interval [0,1]; no small endpoint/square-root singularity.
            q=3*mp.sqrt(sigma)*mp.quad(lambda t:t*t*mp.sqrt(1+4*b*z*z*t*t/3)/mp.sqrt(1+(1+a)/L*(sigma*t**6+b*z**8*t**8)),[0,1])
            delta=scale*q
            sc=(sigma-q*q)/(b*q**(mp.mpf(8)/3));uc=(U(z)-L-a*q*q/2)/(a*b*q**(mp.mpf(8)/3))
            third=dc(C2,z);scaled=third*delta**(mp.mpf(1)/3);limit=16*a*b/(81*scale**(mp.mpf(8)/3))
            vals={'delta_chi':delta,'S_series_coefficient':sc,'U_series_coefficient':uc,'U_chichi':C2(z),'scaled_third_derivative':scaled,'third_derivative_limit':limit}
            for key,v in vals.items():
                # The author computes U-L after adding order-one L at 70 digits.
                # This is a floating-point conditioning budget, not an interval certificate.
                budget=max(m('2e-33'),32*mp.power(10,-FIX['endpoint_series']['digits'])*max(1,abs(L))/(a*b*q**(mp.mpf(8)/3))) if key=='U_series_coefficient' else m('2e-33')
                compare('endpoint row '+str(i)+'/'+str(j)+' '+key,data[key],v,atol=budget,rtol='2e-32')
            rows.append({k:s(v)for k,v in vals.items()})
        ck('endpoint coefficients approach declared limits '+str(i),abs(sc+mp.mpf(4)/5)<m('2e-8')*m('.8') and abs(uc+mp.mpf(1)/15)<m('2e-8')/15)
        out.append({'a':s(a),'b':s(b),'rows':rows})
    return out

def account_author_checks():
    names={};bad=[]
    for i,c in enumerate(AUTHOR['checks']):
        names[c['name']]=names.get(c['name'],0)+1
        if not c['passed']:bad.append(i)
        if 'actual'in c and 'expected'in c:
            error=abs(c['actual']-c['expected']);tol=c['tolerance']
            ck('author comparison accounting '+str(i),math.isfinite(c['actual']) and error<=tol and abs(error-c['error'])<1e-25+1e-14*abs(error))
        elif 'reduced_expression'in c:ck('author symbolic row accounting '+str(i),c['reduced_expression']=='0')
        elif c['name'].startswith('FIRAS stated baseline'):ck('author FIRAS accounting '+str(i),c['lower']<=c['published_MJy_per_sr']<=c['upper'])
        elif c['name']=='grid positive bare Hessian':ck('author Hessian accounting '+str(i),min(c['eigenvalues_over_H2'])>0)
        elif c['name']=='grid global transverse lower bound':ck('author bound accounting '+str(i),c['value']>=c['bound'])
        elif 'max_tolerance_units'in c:ck('author trajectory accounting '+str(i),c['max_tolerance_units']<1)
        elif 'error_kJy_per_sr'in c:ck('author error accounting '+str(i),c['error_kJy_per_sr']>0)
        else:ck('author status accounting '+str(i),c['passed'],record=c)
    ck('author count consistency',len(AUTHOR['checks'])==1195 and AUTHOR['checks_passed']==1195 and AUTHOR['checks_failed']==0 and not bad)
    return {'all_rows':len(AUTHOR['checks']),'name_counts':names,'note':'Accounting of recorded assertions is separate from independent positive recomputation. Solver nfev/messages are recorded, not independently reproducible physical claims.'}

def main():
    dest=ROOT/'RESULTS_v2.json'
    if dest.exists():raise FileExistsError(dest)
    result={'started_at':datetime.now(timezone.utc).isoformat(),'scope':'independent numerical two-field block only'}
    for name,fun in [('thermal',thermal),('grid',grid),('old_residue',old_residue),('histories',histories),('endpoint',endpoint),('author_accounting',account_author_checks)]:
        print('begin',name,flush=True);result[name]=fun();print('complete',name,flush=True)
    result['checks']=CHECKS;result['passed']=sum(x['passed']for x in CHECKS);result['failed']=sum(not x['passed']for x in CHECKS)
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();result['ended_at']=datetime.now(timezone.utc).isoformat()
    with dest.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[x for x in CHECKS if not x['passed']]},indent=2))
    return bool(result['failed'])

if __name__=='__main__':sys.exit(main())
