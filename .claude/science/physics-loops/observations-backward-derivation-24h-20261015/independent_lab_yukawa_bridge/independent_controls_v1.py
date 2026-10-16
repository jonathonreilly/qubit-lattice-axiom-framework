"""Independent pre-author-runner laboratory Yukawa checks; all synthetic."""
import json,math,hashlib,sys
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import quad
HERE=Path(__file__).resolve().parent;checks=[];detail={}
def ck(name,ok,**data):checks.append({'name':name,'passed':bool(ok),**data})
def ex(name,value):
    v=s.simplify(value);ck(name,v==0,value=str(v))
r,m=s.symbols('r m',positive=True);G=s.exp(-m*r)/r
ex('exterior Yukawa PDE',s.diff(r*r*s.diff(G,r),r)/(r*r)-m*m*G)
ex('source flux -4pi',s.limit(r*r*s.diff(G,r),r,0)+1)
ex('long range torque has no linear mass term',s.diff((1+m*r)*s.exp(-m*r),m).subs(m,0))
z=s.symbols('z',positive=True)
ex('uniform central concentration limit',s.limit(3*(z*s.cosh(z)-s.sinh(z))/z**3,z,0)-1)
ex('radial kernel decreasing formula',s.diff((1+m*r)*s.exp(-m*r)/r**2,r)+s.exp(-m*r)*(m*m/r+2*(1+m*r)/r**3))
# Independent radial profile including a nonconstant allowed pressure trace.
rho=lambda x:math.exp(-4*x*x);sigma=lambda x:rho(x)*(1-.2*x*x)
M=4*math.pi*quad(lambda x:x*x*rho(x),0,1,epsabs=1e-12)[0]
rad=[]
for mm in [0.,.7,2.3]:
    Q=4*math.pi*quad(lambda x:x*x*sigma(x)*(math.sinh(mm*x)/(mm*x)if mm*x else 1),0,1,epsabs=1e-12)[0]
    upper=M*(math.sinh(mm)/mm if mm else 1)
    ck('pressure support '+str(mm),.8*M<=Q<=upper,M=M,Q=Q,lower=.8*M,upper=upper)
    for rr in [1.15,2.4]:
        def radial(y):
            angular=quad(lambda c:math.exp(-mm*math.sqrt(rr*rr+y*y-2*rr*y*c))/math.sqrt(rr*rr+y*y-2*rr*y*c),-1,1,epsabs=2e-11,epsrel=2e-11)[0]
            return 2*math.pi*y*y*sigma(y)*angular
        direct=quad(radial,0,1,epsabs=2e-10,epsrel=2e-10)[0]
        reduced=math.exp(-mm*rr)*Q/rr
        err=abs(direct-reduced)
        ck('independent angular convolution '+str((mm,rr)),err<3e-10,error=err)
        rad.append(dict(m=mm,r=rr,direct=direct,reduced=reduced,error=err))
detail['radial']=rad
# Genuine rotation torque; vertical separation supplies a uniform d=1 certificate.
XA=np.array([[.4,0,0],[-.3,.1,.2],[.15,.28,-.1]]);XB=np.array([[.9,.2,1.2],[-.2,.8,1.4]])
wa=np.array([1.1,.7,.4]);wb=np.array([.9,1.3]);dwa=np.array([.10,-.05,.02]);dwb=np.array([-.07,.08])
L=float(max(np.linalg.norm(XA[:,:2],axis=1)));d=1.
def evaluate(theta,mm,aw=wa,bw=wb,ax=XA):
    co,si=math.cos(theta),math.sin(theta);rot=np.array([[co,-si,0],[si,co,0],[0,0,1]])
    x=ax@rot.T;Jx=np.column_stack((-x[:,1],x[:,0],np.zeros(len(x))))
    v=x[:,None,:]-XB[None,:,:];rr=np.linalg.norm(v,axis=-1);mass=aw[:,None]*bw[None,:]
    energy=-np.sum(mass*np.exp(-mm*rr)/rr)
    kernel=-np.sum(v*Jx[:,None,:],axis=-1)*(1+mm*rr)*np.exp(-mm*rr)/rr**3
    return float(energy),float(np.sum(mass*kernel))
theta=2*np.pi*np.arange(1024)/1024
fourier=[]
for mm in [0.,.8,2.2]:
    ut=np.array([evaluate(t,mm)for t in theta]);un=np.fft.fft(ut[:,0])/len(theta);tn=np.fft.fft(ut[:,1])/len(theta)
    bound=L*(1+mm*d)*math.exp(-mm*d)/d**2
    for n in [1,2,4]:
        err=abs(tn[n]+1j*n*un[n]);ck('complex torque Fourier '+str((mm,n)),err<2e-13,error=err,coefficient=[tn[n].real,tn[n].imag])
        ck('harmonic support '+str((mm,n)),abs(tn[n])<=bound*sum(wa)*sum(wb))
    ck('periodic mean torque '+str(mm),abs(tn[0])<1e-13,error=abs(tn[0]))
    for angle in [.13,.71,2.14]:
        h=1e-4;deriv=(evaluate(angle-2*h,mm)[0]-8*evaluate(angle-h,mm)[0]+8*evaluate(angle+h,mm)[0]-evaluate(angle+2*h,mm)[0])/(12*h)
        err=abs(evaluate(angle,mm)[1]+deriv);ck('physical torque sign '+str((mm,angle)),err<3e-10,error=err)
    pert=np.fft.fft([evaluate(t,mm,wa+dwa,wb+dwb)[1]for t in theta])/len(theta)
    dbound=bound*(sum(wa)*sum(abs(dwb))+sum(wb)*sum(abs(dwa))+sum(abs(dwa))*sum(abs(dwb)))
    for n in [1,2,4]:ck('density L1 norm '+str((mm,n)),abs(pert[n]-tn[n])<=dbound,error=float(abs(pert[n]-tn[n])),bound=float(dbound))
    # A positive half-turn symmetric body has exactly vanishing odd harmonics.
    axis=np.array([[.4,0,0],[-.4,0,0]]);sym=np.fft.fft([evaluate(t,mm,np.array([1.,1.]),wb,axis)[1]for t in theta])/len(theta)
    ck('positive-mass harmonic cancellation '+str(mm),max(abs(sym[1]),abs(sym[3]))<1e-13,residual=float(max(abs(sym[1]),abs(sym[3]))))
    # Signed contrast zero total mass is not zero total variation.
    signed=np.array([1.,-1.]);old=np.fft.fft([evaluate(t,mm,signed,wb,axis)[1]for t in theta])/len(theta);new=np.fft.fft([evaluate(t,mm,signed,1.05*wb,axis)[1]for t in theta])/len(theta)
    witness=abs(new[1]-old[1]);valid=bound*sum(abs(signed))*.05*sum(wb)
    ck('signed mass must use total variation '+str(mm),witness>1e-6 and witness<=valid,invalid_signed_mass_bound=0,actual=float(witness),tv_bound=float(valid))
    fourier.append(dict(m=mm,coefficients=[[float(tn[n].real),float(tn[n].imag)]for n in [1,2,4]]))
detail['torque']=fourier
# Complex common gain with nonzero scalar calibration response.
Nc=2+.3j;Yc=.4-.2j;Ni=np.array([.6+1.2j,-.8+.4j]);Yi=np.array([-.25+.6j,1.1-.2j]);gain=1.2+.4j;GT=.7
ratio_rows=[]
for a in [0.,.37,1.8]:
    zi=gain*GT*(Ni+a*Yi);zc=gain*GT*(Nc+a*Yc);rr=zi/zc;A=Yi-rr*Yc;b=rr*Nc-Ni;fit=b/A
    ck('complex ratio strength '+str(a),max(abs(fit-a))<3e-14,error=float(max(abs(fit-a))))
    ck('exact common gain scale '+str(a),max(abs((gain/3.7)*(GT*3.7)*(Ni+a*Yi)-zi))<1e-14)
    if a:
        naive=b/Yi;ck('nonzero calibration leakage bias '+str(a),max(abs(naive-a))>.01,bias=float(max(abs(naive-a))))
    for i in range(2):
        e=2e-5
        for phase in np.linspace(0,2*np.pi,19,endpoint=False):
            delta=e*np.exp(1j*phase);rh=rr[i]+delta;Ah=Yi[i]-rh*Yc;ah=(rh*Nc-Ni[i])/Ah
            margin=abs(Ah)-abs(Yc)*e;bound=e*abs(Nc*Yi[i]-Ni[i]*Yc)/(abs(Ah)*margin)
            ck('complex error disk '+str((a,i,float(phase))),margin>0 and abs(ah-a)<=bound+1e-13,error=float(abs(ah-a)),bound=float(bound))
        delta=-e*abs(Yc)*A[i]/(abs(A[i])*Yc);rh=rr[i]+delta;Ah=Yi[i]-rh*Yc;ah=(rh*Nc-Ni[i])/Ah
        bound=e*abs(Nc*Yi[i]-Ni[i]*Yc)/(abs(Ah)*(abs(Ah)-abs(Yc)*e));relative=abs(abs(ah-a)/bound-1)
        ck('sharp complex ratio error '+str((a,i)),relative<3e-9,relative=float(relative))
    ratio_rows.append(dict(a=a,ratios=[[z.real,z.imag]for z in rr]))
# Algebraic degeneracy and false determinant-only compatibility.
r0=np.array([.4+.7j,-.3+.2j]);yc=2.;nc=1.;yi=r0*yc;ni=r0*nc;A=yi-r0*yc;b=r0*nc-ni
ck('A0 b0 unidentified',max(abs(A))==0 and max(abs(b))==0)
bbad=r0*nc-(ni+np.array([1.,0.]));ck('A0 bnonzero incompatible despite determinants',max(abs(A))==0 and max(abs(bbad))>0 and abs(A[0]*bbad[1]-A[1]*bbad[0])==0)
for a in [0,.2,3.]:ck('massless ratio no strength '+str(a),max(abs((Ni+a*Ni)/(Nc+a*Nc)-Ni/Nc))<1e-14)
e=1e-4;rh=r0[0]+e;Ah=yi[0]-rh*yc;ck('pole boundary is not admitted',not (abs(Ah)>abs(yc)*e*(1+1e-12)))
detail['ratios']=ratio_rows
result={'scope':'Independent pre-runner algebra and synthetic finite-source/torque/complex calibration checks; no physical calibration or empirical test','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'passed':sum(x['passed']for x in checks),'failed':sum(not x['passed']for x in checks),'checks':checks,'details':detail};(HERE/'INDEPENDENT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failed_checks':[c for c in checks if not c['passed']]}));sys.exit(bool(result['failed']))
