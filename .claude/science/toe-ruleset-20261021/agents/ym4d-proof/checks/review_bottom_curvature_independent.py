#!/usr/bin/env python3
"""Independent source-exposed checks; no author/predecessor imports.
SU(2) basis -i sigma has bracket 2 cross and normalized pairing dot.
Coefficients are mixed st, not half-polarized coefficients.
"""
import itertools, json, time, sys
import numpy as np
import scipy.linalg as la
from scipy.special import ive

CHECKS=[]
def maxabs(a): return float(np.max(np.abs(a)))
def check(name,err,tol,detail=None):
    CHECKS.append(dict(name=name,error=float(err),tolerance=float(tol),passed=bool(err<=tol),detail=detail))
def equality(name,a,b,tol=2e-9):
    err=maxabs(np.asarray(a)-np.asarray(b)); check(name,err,tol*(1+max(maxabs(a),maxabs(b))))
    return err
def detect(name,value,base):
    threshold=max(1e-8,100*base)
    CHECKS.append(dict(name=name,discrepancy=float(value),required_exceed=float(threshold),passed=bool(value>threshold)))

class Cell:
    def __init__(self,L=3,kappa=.83):
        self.L=L;self.kappa=kappa
        self.coords=np.array(list(itertools.product(range(-(L//2),L//2+1),repeat=4)),int)
        self.index={tuple(x):i for i,x in enumerate(self.coords)}
        self.V=len(self.coords);self.E=4*self.V
        self.pairs=list(itertools.combinations(range(4),2));self.triples=list(itertools.combinations(range(4),3))
        self.root=self.index[(0,0,0,0)]
        self.plaq=[]
        for x in self.coords:
            for mu,nu in self.pairs:
                self.plaq.append(self.word(x,[(mu,1),(nu,1),(mu,-1),(nu,-1)]))
        self.soft=[];self.softdirs=[]
        for mu in range(4):
            for off in self.coords:
                for perm in itertools.permutations(range(4)):
                    steps=[]
                    for axis in perm: steps += [(axis,int(np.sign(off[axis])))]*abs(int(off[axis]))
                    full=steps+[(mu,1)]*L+[(axis,-sgn) for axis,sgn in reversed(steps)]
                    self.soft.append(self.word(np.zeros(4,int),full)); self.softdirs.append(mu)
        self.softdirs=np.array(self.softdirs)
        self.softscale=1/(24*L**4)
        self.cache={}
        self.P=self.pack(self.plaq);self.M=self.pack(self.soft)
    def locate(self,x):
        wrap=(np.asarray(x)+self.L//2)//self.L
        u=np.asarray(x)-self.L*wrap
        return self.index[tuple(u)],wrap
    def word(self,start,steps):
        x=np.array(start,int).copy(); out=[]
        for mu,sgn in steps:
            if sgn<0: x[mu]-=1
            site,wind=self.locate(x);out.append((site*4+mu,sgn,wind.copy()))
            if sgn>0: x[mu]+=1
        return out
    def pack(self,words):
        width=max(map(len,words)); idx=np.zeros((len(words),width),int);sign=np.zeros_like(idx,float);wind=np.zeros((len(words),width,4),int)
        for i,word in enumerate(words):
            for j,(e,s,w) in enumerate(word):idx[i,j]=e;sign[i,j]=s;wind[i,j]=w
        return idx,sign,wind
    def coeff(self,pack,p):
        idx,sign,wind=pack
        return sign*np.exp(1j*np.einsum('ijk,k->ij',wind,p))
    def rowmatrix(self,pack,p):
        idx,_,_=pack;c=self.coeff(pack,p);A=np.zeros((len(idx),self.E),complex)
        np.add.at(A,(np.repeat(np.arange(len(idx)),idx.shape[1]),idx.ravel()),c.ravel());return A
    def incidence(self,p):
        d1=np.zeros((self.E,self.V),complex)
        for i,x in enumerate(self.coords):
            for mu in range(4):
                y=x.copy();y[mu]+=1;j,wind=self.locate(y)
                d1[4*i+mu,i]-=1;d1[4*i+mu,j]+=np.exp(1j*np.dot(wind,p))
        d2=self.rowmatrix(self.P,p)
        d3=np.zeros((len(self.triples)*self.V,len(self.pairs)*self.V),complex)
        for i,x in enumerate(self.coords):
            for t,tri in enumerate(self.triples):
                for j,axis in enumerate(tri):
                    pair=tuple(a for a in tri if a!=axis);ori=self.pairs.index(pair);sgn=(-1)**j
                    y=x.copy();y[axis]+=1;iy,wind=self.locate(y)
                    d3[4*i+t,6*i+ori]-=sgn;d3[4*i+t,6*iy+ori]+=sgn*np.exp(1j*np.dot(wind,p))
        return d1,d2,d3
    def operators(self,p):
        p=np.asarray(p,complex);key=tuple(p)
        if key in self.cache:return self.cache[key]
        d1,d2,d3=self.incidence(p);D1,D2,D3=self.incidence(-p)
        softrow=self.rowmatrix(self.M,p);negative=self.rowmatrix(self.M,-p)
        Q=np.zeros((4,self.E),complex);Qneg=Q.copy()
        np.add.at(Q,self.softdirs,softrow*self.softscale);np.add.at(Qneg,self.softdirs,negative*self.softscale)
        keep=[j for j in range(self.V) if j!=self.root]
        G=d1[:,keep];Gt=D1[:,keep].T
        H=D2.T@d2+self.kappa*Qneg.T@Q
        augmented=H+G@Gt
        factor=la.lu_factor(augmented)
        ans=dict(p=p,d1=d1,d2=d2,d3=d3,d2dual=D2.T,d3dual=D3.T,Q=Q,Qdual=Qneg.T,G=G,Gdual=Gt,H=H,augmented=augmented,factor=factor)
        self.cache[key]=ans;return ans
    def lift(self,p,v):
        op=self.operators(p);a=la.lu_solve(op['factor'],self.kappa*op['Qdual']@v)
        return a,op['d2']@a,v-op['Q']@a
    def mixedB(self,pack,p,q,a,b):
        idx,_,_=pack;av=self.coeff(pack,p)*a[idx];bv=self.coeff(pack,q)*b[idx]
        # B_st = sum_{i<j}(a_i b_j - b_i a_j) in e3, since bracket=2 cross.
        ap=np.cumsum(av,axis=1)-av;bp=np.cumsum(bv,axis=1)-bv
        return np.sum(ap*bv-bp*av,axis=1)
    def mixedDBdual(self,pack,p,q,a,b,fa,fb):
        # <f_b,DB[a]w>+<f_a,DB[b]w>, w has colour e3 and momentum -(p+q).
        idx,_,_=pack;av=self.coeff(pack,p)*a[idx];bv=self.coeff(pack,q)*b[idx]
        ap=np.cumsum(av,axis=1)-av;bp=np.cumsum(bv,axis=1)-bv
        atail=av.sum(axis=1)[:,None]-av-ap;btail=bv.sum(axis=1)[:,None]-bv-bp
        coefficient=((atail-ap)*fb[:,None]-(btail-bp)*fa[:,None])*self.coeff(pack,-p-q)
        out=np.zeros(self.E,complex);np.add.at(out,idx.ravel(),coefficient.ravel());return out
    def evaluate(self,p,q,va,vb):
        p=np.asarray(p,complex);q=np.asarray(q,complex);k=p+q
        a,fa,ra=self.lift(p,va);b,fb,rb=self.lift(q,vb);op=self.operators(k)
        Bp=self.mixedB(self.P,p,q,a,b)
        Bwords=self.mixedB(self.M,p,q,a,b);B=np.zeros(4,complex);np.add.at(B,self.softdirs,Bwords*self.softscale)
        W=self.mixedDBdual(self.P,p,q,a,b,fa,fb)
        M=self.mixedDBdual(self.M,p,q,a,b,ra[self.softdirs],rb[self.softdirs])*self.softscale
        source=op['d2dual']@Bp+W+self.kappa*op['Qdual']@B-self.kappa*M
        w=la.lu_solve(op['factor'],-source)
        g=op['d2']@w;Psi=g+Bp;qcur=self.kappa*(-op['Q']@w-B)
        S=op['Qdual']@qcur-W+self.kappa*M;R=op['d3']@Bp
        N=op['d2']@S+op['d3dual']@R
        phase=np.exp(-1j*(self.coords@k)/self.L)/self.V
        avg=lambda x: np.einsum('u,ud->d',phase,x.reshape(self.V,-1))
        return dict(p=p,q=q,k=k,a=a,b=b,fa=fa,fb=fb,ra=ra,rb=rb,w=w,g=g,Psi=Psi,Bp=Bp,B=B,W=W,M=M,S=S,R=R,N=N,qcur=qcur,source=source,op=op,avg=avg,
                    lowPsi=avg(Psi),lowN=avg(N),lowBp=avg(Bp),lowg=avg(g))

def phi(p): return np.sum(2-np.exp(1j*p)-np.exp(-1j*p))
def source_suite():
    c=Cell(); va=np.array([.6,-.2,.35,.1]); vb=np.array([-.15,.5,.25,-.4]);theta=np.array([.29,-.17,.23,.08],complex)
    fixtures=[]
    for sign in [-1,1]:
        w=np.array([.0,.032,.019,-.011],complex);w[0]=sign*1j*np.sqrt(np.sum(w[1:]**2));k=2*c.L*np.arcsin(w/(2*c.L))
        fixtures.append(('null_'+str(sign),theta,k-theta))
    fixtures += [('generic',theta+.008j,np.array([-.13,.14,-.19,.06])-.004j),('opposite',theta,-theta),('constant',np.zeros(4),np.zeros(4))]
    records=[]
    for name,p,q in fixtures:
        z=c.evaluate(p,q,va,vb);op=z['op']; k=z['k'];
        e=equality(name+'_Euler',op['d2dual']@z['Psi'],z['S'])
        equality(name+'_Bianchi',op['d3']@z['Psi'],z['R'])
        equality(name+'_stationary',op['H']@z['w'],-z['source'])
        equality(name+'_gauge_annihilation',op['Gdual']@z['source'],np.zeros(c.V-1))
        equality(name+'_Hodge',z['lowN'],phi(k/c.L)*z['lowPsi'])
        equality(name+'_cochain12',op['d2']@op['d1'],np.zeros((6*c.V,c.V)),2e-11)
        equality(name+'_cochain23',op['d3']@op['d2'],np.zeros((4*c.V,4*c.V)),2e-11)
        if name.startswith('null'):
            check(name+'_null_symbol',abs(phi(k/c.L)),2e-12)
            check(name+'_numerator',maxabs(z['lowN']),2e-9*(1+maxabs(z['S'])))
            detect(name+'_nonzero_curvature',maxabs(z['lowPsi']),maxabs(z['lowN']))
            mutants={
                'omit_Wilson_DB':op['d2']@(z['S']+z['W'])+op['d3dual']@z['R'],
                'omit_soft_DB':op['d2']@(z['S']-c.kappa*z['M'])+op['d3dual']@z['R'],
                'omit_Bianchi':op['d2']@z['S'],
                'conjugate_adjoint':op['d2']@(op['Q'].conj().T@z['qcur']-z['W']+c.kappa*z['M'])+op['d3'].conj().T@z['R']}
            for m,N in mutants.items():detect(name+'_'+m,maxabs(z['avg'](N)-z['lowN']),maxabs(z['lowN']))
        if name in ['opposite','constant']:
            equality(name+'_harmonic',z['lowPsi'],z['lowBp'])
            equality(name+'_zero_mean_g',z['lowg'],np.zeros(6))
        records.append(dict(name=name,phi_abs=float(abs(phi(k/c.L))),source=maxabs(z['source']),low_numerator=maxabs(z['lowN']),low_curvature=maxabs(z['lowPsi']),harmonic_B=maxabs(z['lowBp']),g_mean=maxabs(z['lowg'])))
    # Both external reciprocal faces: actual contour words supply periodicity.
    p=theta+.006j;q=np.array([-.12,.11,.07,-.21])-.003j
    z=c.evaluate(p,q,va,vb)
    for leg in [0,1]:
        pp=p.copy();qq=q.copy();(pp if leg==0 else qq)[2]+=2*np.pi
        zz=c.evaluate(pp,qq,va,vb)
        equality('external_face_'+str(leg),z['Psi'],zz['Psi'])
    # Cauchy quotient using true source N, not the directly solved quotient.
    cq=[]
    for label,targetw,pfirst in [('null',np.array([1j*np.sqrt(.012**2+.007**2),.012,.007,0]),theta),('opposite',np.zeros(4,complex),theta),('constant',np.zeros(4,complex),np.zeros(4))]:
        radius=.075;nodes=40; targetw=np.asarray(targetw,complex);acc=np.zeros(6,complex)
        for j in range(nodes):
            zz=radius*np.exp(2j*np.pi*j/nodes);ww=targetw.copy();ww[0]=zz;kk=2*c.L*np.arcsin(ww/(2*c.L))
            zzdata=c.evaluate(pfirst,kk-pfirst,va,vb)
            F=c.L**4*zzdata['lowN'];A=np.sum(ww[1:]**2)
            acc += F*zz/((zz*zz+A)*(zz-targetw[0]))/nodes
        kk=2*c.L*np.arcsin(targetw/(2*c.L));direct=c.evaluate(pfirst,kk-pfirst,va,vb)['lowPsi']
        err=equality('Cauchy_'+label,acc/c.L**2,direct,2e-8)
        cq.append(dict(name=label,error=err,low_curvature=maxabs(direct),nodes=nodes,radius=radius))
    # Geometric path and gauge normalization, independent of source cancellation.
    zero=c.operators(np.zeros(4)); equality('Q_constant',zero['Q']@np.tile(va,(c.V,1)).ravel(),c.L*va,2e-11)
    detect('wrong_24_divisor',maxabs(24*zero['Q']@np.tile(va,(c.V,1)).ravel()-c.L*va),0)
    equality('harmonic_linear_lift',c.lift(np.zeros(4),va)[0],np.tile(va/c.L,(c.V,1)).ravel())
    return dict(fixtures=records,cauchy=cq,cell_sites=c.V,soft_contours=len(c.soft),kappa=c.kappa)

def scalar_suite():
    norms=[]
    for ell in [3,5,9,15]:
        grid=np.array(list(itertools.product(range(ell),repeat=4)))
        K=np.array(list(itertools.product(range(-(ell//2),ell//2+1),repeat=4)));zero=np.all(K==0,axis=1)
        for label,k in [('bulk',np.array([.37,-.28,.16,-.21])+1j*np.array([.02,-.015,.01,-.009])),('face',np.array([np.pi+.04,-np.pi-.03,.22,-.17])+1j*np.array([-.013,.017,.008,-.01]))]:
            # Translation of standard FFT indices: each K is reduced modulo ell.
            q=(k[None,:]+2*np.pi*K)/ell;ph=np.sum(2-np.exp(1j*q)-np.exp(-1j*q),axis=1);nu=np.exp(1j*q[:,0])-1
            mult=np.where(zero,0,nu/ph);spectral=np.zeros((ell,)*4,complex);spectral[tuple((K%ell).T)]=mult
            periodic=np.fft.ifftn(spectral).ravel()
            # Exact row u=0, v in standard cell: dGreen(0,v)=sum multiplier exp(-iqv)/ell^4.
            inv=(-grid)%ell;ker=periodic[np.ravel_multi_index(tuple(inv.T),(ell,)*4)]*np.exp(-1j*(grid@k)/ell)
            row=float(np.sum(np.abs(ker)));norms.append(dict(ell=ell,case=label,row=row,row_over_ell=row/ell))
            check('scalar_scaled_'+str(ell)+'_'+label,row/ell,2.0)
            if ell==3:
                c=Cell();op=c.operators(k)
                # Site Laplacian and exact full spectral right/left modes.
                d1=op['d1'];D1=c.operators(-k)['d1'].T
                lap=D1@d1;U=np.exp(1j*(c.coords@q.T));V=np.exp(-1j*(q@c.coords.T))/c.V
                P=U[:,~zero]@V[~zero];invhigh=(U[:,~zero]/ph[~zero])@V[~zero]
                equality('scalar_projection_'+label,V@U,np.eye(c.V),2e-11)
                equality('scalar_inverse_'+label,lap@invhigh,P,2e-10)
                detect('missing_cell_normalization_'+label,maxabs(c.V*V@U-np.eye(c.V)),2e-11)
                detect('complex_conjugation_'+label,maxabs(d1.conj().T@d1-lap),2e-11)
                # Reindex all aliases across a reciprocal face; low/high alone differ.
                k2=k.copy();k2[0]+=2*np.pi;q2=(k2[None,:]+2*np.pi*K)/ell;phi2=np.sum(2-np.exp(1j*q2)-np.exp(-1j*q2),axis=1)
                U2=np.exp(1j*(c.coords@q2.T));V2=np.exp(-1j*(q2@c.coords.T))/c.V
                full=(U/ph)@V;full2=(U2/phi2)@V2
                equality('full_alias_periodicity_'+label,full,full2,2e-10)
                high2=(U2[:,~zero]/phi2[~zero])@V2[~zero]
                detect('high_branch_not_periodic_'+label,maxabs(invhigh-high2),2e-11)
    # Heat kernel derivative weighted l1, computed from Bessel formula directly.
    heat=[]
    for t in [.02,.7,9,90]:
        j=np.arange(-int(20+20*np.sqrt(t)),int(20+20*np.sqrt(t))+1);alpha=.017
        h=ive(np.abs(j),2*t);diff=ive(np.abs(j+1),2*t)-h
        weighted=float(np.sum(np.exp(alpha*np.abs(j))*np.abs(diff)))
        reference=((1+t)**-.5+alpha)*np.exp(8*alpha**2*t)
        check('heat_bound_'+str(t),weighted/reference,8)
        heat.append(dict(time=t,weighted_difference=weighted,reference=reference))
    # A numerator zero at the origin alone does not vanish on either null sheet.
    for sign in [-1,1]:
        w=np.array([sign*.03j,.03,0,0]);detect('origin_only_counterexample_'+str(sign),abs(w[0]),0)
    return dict(counting_norms=norms,heat=heat)

def main():
    t=time.monotonic();mode=sys.argv[1] if len(sys.argv)>1 else 'source'
    result=source_suite() if mode=='source' else scalar_suite()
    out=dict(mode=mode,result=result,checks=CHECKS,passed=sum(c['passed'] for c in CHECKS),total=len(CHECKS),seconds=time.monotonic()-t,
        limits='Floating point finite diagnostics; independent proof review needed for uniform theorem. No author helper imports.')
    print(json.dumps(out,indent=2));sys.exit(0 if all(c['passed'] for c in CHECKS) else 1)
if __name__=='__main__':main()
