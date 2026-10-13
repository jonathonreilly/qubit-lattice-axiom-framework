#!/usr/bin/env python3
"""Independent bounded checks; never imports or executes the author runner."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from datetime import datetime, timezone
import difflib
import hashlib
import json
import math
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_bvp, simpson

HERE=Path(__file__).resolve().parent
SNAP=HERE/'snapshots_v1'
R=json.loads((SNAP/'evidence_v2/RESULTS.json').read_text())
FIX=json.loads((SNAP/'NUMERICAL_FIXTURES.json').read_text())
OBS=json.loads((SNAP/'OBSERVATION_INPUTS.json').read_text())
checks=[]
details={}


def check(name,condition,**data):
    checks.append(dict(name=name,passed=bool(condition),**data))


def near(name,actual,expected,rtol=2e-8,atol=0):
    err=abs(float(actual)-float(expected))
    check(name,err<=atol+rtol*abs(float(expected)),actual=float(actual),expected=float(expected),
          relative_error=err/max(abs(float(expected)),1e-300),absolute_error=err,rtol=rtol,atol=atol)


def identities():
    # Frame conversion, envelope response, and polytropic scaling.
    G,A,a,M1,M2,RJ,Gs=sp.symbols('G A a M1 M2 RJ Gstar',positive=True)
    estar=-Gs*(1+a)*(A*M1)*(A*M2)/(RJ/A)
    check('physical G from energy and distance conversion',sp.simplify(estar/A+Gs*A*A*(1+a)*M1*M2/RJ)==0)
    E=sp.Function('E')(G);s=-G*sp.diff(E,G)/E
    check('general sensitivity second derivative identity',sp.simplify(G*sp.diff(s,G)-s-s*s+G*G*sp.diff(E,G,2)/E)==0)
    # A two-coordinate positive-Hessian model, independent of the polytrope.
    H=sp.Matrix([[3,1],[1,2]]);w=sp.Matrix([2,-1]);xeq=-G*H.inv()*w
    ee=100+(xeq.T*H*xeq)[0]/2+G*(w.T*xeq)[0]
    check('explicit stable Hessian envelope model',sp.simplify(sp.diff(ee,G)-(w.T*xeq)[0])==0)
    check('explicit stable Hessian curvature',sp.diff(ee,G,2)==-(w.T*H.inv()*w)[0]<0)
    n,B,C=sp.symbols('n B C',positive=True);p=3/(3-n);epoly=B-C*G**p;spoly=-G*sp.diff(epoly,G)/epoly
    check('polytropic susceptibility symbolic',sp.simplify(G*sp.diff(spoly,G)-p*spoly-spoly**2)==0)
    check('polytropic envelope uses gravitational energy',sp.simplify(G*sp.diff(epoly,G)-p*(epoly-B))==0)
    # Derive the radial operator directly from Lagrangian mass-shell balance.
    r,gamma,omega=sp.symbols('r gamma omega',positive=True)
    P=sp.Function('P')(r);rho=sp.Function('rho')(r);eta=sp.Function('eta')(r)
    deltaP=-gamma*P*(3*eta+r*sp.diff(eta,r))
    # rho * delta acceleration = -4 P' eta - deltaP'.
    perturbed=(-4*sp.diff(P,r)*eta-sp.diff(deltaP,r)+rho*omega**2*r*eta)*r**3
    standard=sp.diff(gamma*P*r**4*sp.diff(eta,r),r)+(3*gamma-4)*r**3*sp.diff(P,r)*eta+rho*r**4*omega**2*eta
    check('mass-shell derivation of full radial operator',sp.simplify(perturbed-standard)==0)
    se,sm,ss,t=sp.symbols('se sm ss t',real=True)
    eacc=1+a*(1-2*t*se)*(1-2*t*ss);macc=1+a*(1-2*t*sm)*(1-2*t*ss)
    delta=2*(eacc-macc)/(eacc+macc)
    check('Earth-minus-Moon leading sign',sp.simplify(sp.diff(delta,t).subs(t,0)+2*a*(se-sm)/(1+a))==0)
    check('solar sensitivity absent at first order',sp.diff(sp.diff(delta,t).subs(t,0),ss)==0)
    details['symbolic']={'stable_model_E':str(ee),'stable_model_second_derivative':str(sp.diff(ee,G,2)),
        'radial_route':'Lagrangian mass-shell perturbation, then multiply by r^3.',
        'LLR_first_order':str(sp.simplify(sp.diff(delta,t).subs(t,0)))}


def profile(n):
    # Collocation on a fixed unit interval with unknown first zero lambda;
    # distinct from author's adaptive initial-value shooting.
    x=np.linspace(0,1,161)
    theta=np.sinc(x);slope=np.zeros_like(x)
    slope[1:]=(math.pi*x[1:]*np.cos(math.pi*x[1:])-np.sin(math.pi*x[1:]))/(math.pi*x[1:]**2)
    def fun(x,y,p):return np.vstack((y[1],-p[0]**2*np.maximum(y[0],0)**n))
    def bc(ya,yb,p):return np.array([ya[0]-1,ya[1],yb[0]])
    sol=solve_bvp(fun,bc,x,np.vstack((theta,slope)),p=[4.],S=np.array([[0.,0.],[0.,-2.]]),tol=3e-10,max_nodes=18000)
    check('BVP converged n='+str(n),sol.success,status=int(sol.status),nodes=len(sol.x),max_residual=float(max(sol.rms_residuals)))
    if not sol.success:raise RuntimeError('Independent BVP did not converge: '+str(n))
    lam=sol.p[0];mu=-lam*sol.y[1,-1]
    rows=[]
    for count in [4096,8192]:
        xx=np.linspace(0,1,count+1);th,thx=sol.sol(xx);th=np.maximum(th,0)
        mass=-lam*xx**2*thx
        im=lam**3*simpson(xx**2*th**n,x=xx)
        iw=lam**2*simpson(xx*mass*th**n,x=xx)
        ip=lam**3*simpson(xx**2*th**(n+1),x=xx)
        rows.append(dict(nodes=count+1,im=im,iw=iw,ip=ip))
    for key in ['im','iw','ip']:near('independent Simpson refinement '+str((n,key)),rows[0][key],rows[1][key],rtol=1e-8)
    reported=next(v for v in R['Lane_Emden_shapes'] if v['n']==n)
    values={'x1':lam,'mu':mu,**{k:rows[-1][k] for k in ['im','iw','ip']}}
    for k,v in values.items():near('independent profile '+str((n,k)),reported[k],v,rtol=2e-8)
    if n==1:
        near('BVP n1 first zero',lam,math.pi,rtol=3e-10);near('BVP n1 mass',mu,math.pi,rtol=3e-10)
    rhoc=lam**3/(4*math.pi*mu)
    result=dict(n=n,lambda_first_zero=float(lam),mu=float(mu),rho_c=float(rhoc),quadratures=rows,
                nodes=len(sol.x),max_residual=float(max(sol.rms_residuals)))
    return sol,result


def structures():
    shapes={};profile_records=[];radial_records=[]
    for n in FIX['polytrope_indices']:
        sol,rec=profile(n);shapes[n]=(sol,rec);profile_records.append(rec)
    check('all12 base body keys complete',sorted((r['n'],r['base']['G']) for r in R['equilibrium_bodies'])==sorted(product(FIX['polytrope_indices'],FIX['initial_G_J'])))
    for row in R['equilibrium_bodies']:
        n=row['n'];base=row['base'];g=base['G'];p=3/(3-n);sol,sh=shapes[n]
        tag=str((n,g));ug0=-3*g/(5-n);binding0=ug0/p;mass0=1+binding0;s0=-ug0/mass0
        eos0=4*math.pi*g/((n+1)*sh['lambda_first_zero']**2)*sh['rho_c']**(1-1/n)
        def body(z):
            rho=sh['rho_c']*math.exp(6*z*n/(3-n));radius=math.exp(-2*z*n/(3-n));ug=ug0*math.exp(2*p*z)
            binding=ug/p;mass=1+binding
            return dict(G=g*math.exp(2*z),rho_c=rho,L=radius/sh['lambda_first_zero'],R=radius,M_b=1,
                        U_G=ug,U_int=-n*ug/3,binding=binding,M_J=mass,s=-ug/mass,K_EOS=eos0)
        for key,value in body(0).items():near('base '+tag+' '+key,base[key],value)
        near('body power '+tag,row['p'],p)
        dlogs=[]
        for deriv in row['equilibrium_derivatives']:
            h=deriv['zeta_step'];plus,minus=body(h),body(-h)
            for label,expected in [('plus',plus),('minus',minus)]:
                for key,value in expected.items():near('shift '+str((n,g,h,label,key)),deriv[label][key],value)
            db=(plus['binding']-minus['binding'])/(2*h)
            dl=(math.log1p(plus['binding'])-math.log1p(minus['binding']))/(2*h)
            ds=(plus['s']-minus['s'])/(2*h);dlogs.append(dl)
            for key,value in [('d_binding_d_zeta',db),('d_log_M_d_zeta',dl),('d_s_d_zeta',ds)]:near('derivative '+str((n,g,h,key)),deriv[key],value,rtol=5e-8)
        near('independent body charge derivative '+tag,row['b_over_alpha_from_difference'],1+(4*dlogs[2]-dlogs[1])/3,rtol=2e-12)
        near('body charge analytic '+tag,row['b_over_alpha_analytic'],1-2*s0,rtol=2e-12)
        # Independent radial trial integrals: pressure differentiated directly
        # from the collocation profile instead of using enclosed-mass gravity.
        x=np.linspace(0,1,8193);th,thx=sol.sol(x);th=np.maximum(th,0);rho=sh['rho_c']*th**n
        P=eos0*sh['rho_c']**(1+1/n)*th**(n+1)
        Pprime=(n+1)*eos0*sh['rho_c']**(1+1/n)*th**n*thx
        gamma=1+1/n
        check('radial Gamma above 4/3 '+tag,gamma>4/3)
        for rr in row['radial_Rayleigh_controls']:
            co=rr['coefficients'];eta=sum(c*x**(2*j) for j,c in enumerate(co))
            prime=sum(2*j*c*x**(2*j-1) for j,c in enumerate(co) if j)
            numerator=simpson(gamma*P*x**4*prime**2-(3*gamma-4)*x**3*Pprime*eta**2,x=x)
            denominator=simpson(rho*x**4*eta**2,x=x);omega2=numerator/denominator
            for key,value in [('numerator',numerator),('denominator',denominator),('omega_squared_Rayleigh',omega2),('omega_squared_in_GM_over_R3',omega2/g)]:near('radial '+str((n,g,co,key)),rr[key],value,rtol=3e-8)
            check('independent radial positivity '+str((n,g,co)),numerator>0 and denominator>0)
            radial_records.append(dict(n=n,G=g,coefficients=co,omega_squared_over_G=float(omega2/g)))
        check('total-binding replacement mutation rejected '+tag,abs((-binding0/mass0)-s0)>0.2*s0)
    details['profiles']=profile_records;details['radial_controls']=radial_records


def design14():
    points=[];weights=[]
    for i in range(3):
        for sign in [-1,1]:
            q=np.zeros(3);q[i]=sign;points.append(q);weights.append(1/15)
    for signs in product([-1,1],repeat=3):points.append(np.array(signs)/math.sqrt(3));weights.append(3/40)
    return points,np.array(weights)


def fourier_derivative(values,order,omega):
    modes=np.fft.fftfreq(len(values),1/len(values))
    shape=(len(values),)+(1,)*(values.ndim-1)
    return np.fft.ifft(np.fft.fft(values,axis=0)*(1j*omega*modes.reshape(shape))**order,axis=0).real


def radiation():
    K=np.array(FIX['K']);check('K positive',np.linalg.eigvalsh(K).min()>0)
    f=FIX['f_for_binary_examples'];a=f/(1-f);direction=np.array(FIX['alpha_direction'])
    alpha=direction*math.sqrt(a/np.dot(direction,np.linalg.solve(K,direction)))
    for i in range(2):near('alpha component '+str(i),R['radiation']['alpha'][i],alpha[i],rtol=1e-13)
    points,weights=design14();near('14point area mean',sum(weights),1,rtol=1e-14)
    for i in range(3):
        near('14point second moment '+str(i),sum(w*q[i]**2 for q,w in zip(points,weights)),1/3,rtol=1e-14)
        near('14point fourth moment '+str(i),sum(w*q[i]**4 for q,w in zip(points,weights)),1/5,rtol=1e-14)
    all_records=[]
    fixture_keys=[(r['fixture'],r['speed']) for r in R['radiation']['rows']]
    check('all18 binary keys complete',fixture_keys==list(product(range(6),FIX['orbital_v_over_c'])))
    for row in R['radiation']['rows']:
        pair=row['profile_pair'];g=pair['G_J'];ns=[pair['n1'],pair['n2']]
        ms=[1-(3-n)*g/(5-n) for n in ns]
        sens=[(3*g/(5-n))/m for n,m in zip(ns,ms)]
        bs=[alpha*(1-2*s) for s in sens];m1,m2=ms;M=sum(ms);mu=m1*m2/M
        scalar_product=lambda b,c:float(np.dot(b,np.linalg.solve(K,c)))
        gs=g/(1+a);mutual=scalar_product(bs[0],bs[1]);g12=gs*(1+mutual);v=row['speed'];sep=g12*M/v**2;omega=v/sep
        tag=str((row['fixture'],v));bq=(m2*bs[0]+m1*bs[1])/M
        for key,val in [('G_star',gs),('G12',g12),('separation',sep),('omega',omega),('max_R_over_r',1/sep),('max_omega_t_internal',omega/math.sqrt(g))]:near('binary '+tag+' '+key,row[key],val,rtol=3e-10)
        for i in range(2):
            near('mass '+tag+str(i),row['masses'][i],ms[i],rtol=1e-12);near('sensitivity '+tag+str(i),row['sensitivities'][i],sens[i],rtol=3e-9)
            for j in range(2):near('body covector '+tag+str((i,j)),row['b'+str(i+1)][j],bs[i][j],rtol=1e-12)
        times=2*math.pi*np.arange(16)/16;relative=np.column_stack((np.cos(times),np.sin(times),np.zeros(16)))*sep
        positions=[m2/M*relative,-m1/M*relative]
        I=sum(m*np.einsum('pi,pj->pij',x,x) for m,x in zip(ms,positions))
        D=sum(m*x[:,:,None]*b[None,None,:] for m,x,b in zip(ms,positions,bs))
        Ib=sum(m*np.einsum('pi,pj,k->pijk',x,x,b) for m,x,b in zip(ms,positions,bs))
        I3=fourier_derivative(I,3,omega);D2=fourier_derivative(D,2,omega);Ib3=fourier_derivative(Ib,3,omega)
        normI3=32*mu*mu*sep**4*omega**6;gr=g12*normI3/5
        for phase in range(16):
            flux=np.zeros(4)
            for q,w in zip(points,weights):
                # Use transverse polarization components, not author's TT projection array.
                seed=np.eye(3)[int(np.argmin(abs(q)))];e1=np.cross(q,seed);e1/=np.linalg.norm(e1);e2=np.cross(q,e1)
                plus=(e1@I3[phase]@e1-e2@I3[phase]@e2)/2;cross=e1@I3[phase]@e2
                dip=q@D2[phase];quad=sum(q[i]*q[j]*Ib3[phase,i,j]/2 for i in range(3) for j in range(3))
                flux+=w*np.array([gs*(plus*plus+cross*cross),gs*scalar_product(dip,dip),gs*scalar_product(quad,quad),2*gs*scalar_product(dip,quad)])
            normalized=flux/gr
            for observed in [s for s in row['direct_sphere_controls'] if s['phase_index']==phase]:
                for j,key in enumerate(['tensor','dipole','scalar_quadrupole','interference']):
                    near('DFT14 sphere '+str((row['fixture'],v,phase,observed['quadrature_index'],key)),observed['powers_over_same_orbit_GR'][key],normalized[j],rtol=8e-8,atol=3e-14 if key=='interference' else 1e-19)
            if phase==0:all_records.append(dict(fixture=row['fixture'],speed=v,independent_powers_over_GR=normalized.tolist(),tidal_fraction_estimate=max(m1/m2,m2/m1)/sep**3))
        expected={'tensor':gs*normI3/5,'dipole':gs*mu**2*scalar_product(bs[0]-bs[1],bs[0]-bs[1])*sep**2*omega**4/3,
                  'scalar_quadrupole':gs*scalar_product(bq,bq)*normI3/30}
        for key,val in expected.items():near('leading channel '+tag+' '+key,row['analytic_powers'][key]/gr,val/gr,rtol=3e-8,atol=1e-19)
        near('GR same-orbit normalization '+tag,row['same_orbit_GR_power']/gr,1,rtol=3e-9)
        near('channel sum '+tag,row['leading_channel_ratio'],sum(expected.values())/gr,rtol=3e-9)
    check('dipole-omission mutation rejected',any(r['independent_powers_over_GR'][1]>0.01 for r in all_records))
    check('equal-sensitivity dipole zero',all(r['independent_powers_over_GR'][1]==0 for r in all_records if r['fixture']==0))
    details['radiation_independent']=all_records


def observation_and_sources():
    mean=F(OBS['LLR_total_EP']['Earth_minus_Moon_mean']);sigma=F(OBS['LLR_total_EP']['reported_uncertainty']);ud=F(OBS['geophysical_self_energy_difference']['Earth_minus_Moon'])
    rows=R['observation']['frozen_predictions']
    for row,fs in zip(rows,OBS['scalar_force_fraction']['frozen_prediction_grid']):
        f=F(fs);pred=2*f*ud;res=mean-pred;z=res/sigma
        for key,value in [('f',f),('prediction',pred),('residual_observed_minus_prediction',res),('z_summary',z),('composition_nuisance_matching_mean',res)]:near('LLR '+fs+' '+key,row[key],value,rtol=1e-14)
        check('LLR exact residual '+fs,F(row['z_exact'])==z)
        check('free nuisance exact fit '+fs,res+pred==mean)
    for row in R['observation']['working_intersections']:
        k=row['reported_uncertainties'];ends=sorted([(mean-k*sigma)/(2*ud),(mean+k*sigma)/(2*ud)])
        lo=max(F(0),ends[0]);hi=min(F(1,2500),ends[1])
        check('LLR exact working interval '+str(k),F(row['lower_exact'])==lo and F(row['upper_exact'])==hi)
        near('LLR lower '+str(k),row['lower'],lo,rtol=1e-14);near('LLR upper '+str(k),row['upper'],hi,rtol=1e-14)
    check('LLR no fit or blind claim',R['observation']['fit_performed'] is False and OBS['blind_holdout'] is False)
    check('LLR sign-reversal mutation rejected',2*F(1,2500)*ud<0)
    correction=json.loads((SNAP/'ANGULAR_CONTRACTION_CORRECTION_v2.json').read_text())
    old=(SNAP/'evidence_v1/source_snapshot/check_body_sensitivity.py').read_bytes();new=(SNAP/'check_body_sensitivity.py').read_bytes()
    diff=''.join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile='v1',tofile='v2'))
    check('complete one-line correction exactly recorded',diff==correction['diff'] and hashlib.sha256(old).hexdigest()==correction['old_sha256'] and hashlib.sha256(new).hexdigest()==correction['new_sha256'])
    for version in [1,2]:
        freeze=json.loads((SNAP/f'evidence_v{version}/FREEZE.json').read_text());ex=json.loads((SNAP/f'evidence_v{version}/EXECUTION.json').read_text())
        for path,h in freeze['files'].items():
            check('frozen execution source '+str((version,path)),hashlib.sha256((SNAP/f'evidence_v{version}/source_snapshot'/path).read_bytes()).hexdigest()==h)
        check('execution chronology '+str(version),freeze['frozen_at']<ex['started_at']<ex['ended_at'])
        check('preserved execution disposition '+str(version),ex['exit_code']==(1 if version==1 else 0) and ex['result_present']==(version==2))
    check('result matches v2 input hashes',R['source_sha256']==json.loads((SNAP/'evidence_v2/FREEZE.json').read_text())['files'])
    author_checks=R['checks'];check('all2818 author checks consumed and passed',len(author_checks)==R['check_count']==2818 and all(c['passed'] for c in author_checks))
    check('author check names unique',len({c['name'] for c in author_checks})==len(author_checks))
    check('original contraction failure preserved',b'ValueError' in (SNAP/'evidence_v1/stderr.txt').read_bytes() and not (SNAP/'evidence_v1/RESULTS.json').exists())
    check('successful stderr empty',(SNAP/'evidence_v2/stderr.txt').stat().st_size==0)
    details['observation']={'predictions':rows,'rectangles':R['observation']['working_intersections'],'mean_only_nuisance_rank':1,'principal_fit_performed':False}


def main():
    out=Path(sys.argv[1])
    if out.exists():raise RuntimeError('Preserve every executed version; choose new output path.')
    for fn in [identities,structures,radiation,observation_and_sources]:fn()
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),method='Independent BVP collocation + Simpson, Fourier multipoles + 14-point sphere, exact algebra and rational LLR map.',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_result_sha256=hashlib.sha256((SNAP/'evidence_v2/RESULTS.json').read_bytes()).hexdigest(),
                check_count=len(checks),passed=all(c['passed'] for c in checks),failures=[c for c in checks if not c['passed']],checks=checks,details=details)
    out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:result[k] for k in ['created_utc','check_count','passed','failures']},sort_keys=True))
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
