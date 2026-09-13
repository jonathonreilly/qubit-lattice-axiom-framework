"""Author challenges for the native full-frame response; no lattice fit is a proof."""
from pathlib import Path
from itertools import product
from collections import deque
import hashlib
import json
import math
import time
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
SIG=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),
     np.diag([1,-1]).astype(complex)]


def run():
    started=time.monotonic();checks=[]
    def check(name,ok,**detail):
        assert bool(ok),(name,detail)
        checks.append(dict(name=name,**detail))
    def eq(name,a,b):
        d=a-b
        vals=list(d) if isinstance(d,s.MatrixBase) else [d]
        check(name,all(s.expand(x)==0 or s.simplify(x)==0 for x in vals))
    def near(name,a,b,tol=2e-11):
        err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
        check(name,err<tol,max_residual=err,tolerance=tol)
    pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    def slash(v):return sum((pauli[i]*v[i] for i in range(3)),s.zeros(2))
    n,m,u,vv=[s.Matrix(s.symbols(p+'0:3',real=True)) for p in ['n','m','u','v']]
    tr=s.trace((s.eye(2)-slash(n))*slash(u)*(s.eye(2)+slash(m))*slash(vv))/4
    jj=(1+n.dot(m))*u.dot(vv)-n.dot(u)*m.dot(vv)-n.dot(vv)*m.dot(u)
    eq('Pauli_trace_real_arbitrary_components',2*s.re(tr.expand()),jj)
    eq('Pauli_trace_imaginary_arbitrary_components',s.im(tr.expand()),-(n+m).dot(u.cross(vv))/2)

    # Direct occupation-sign CAR implementation checks the complex protected
    # path extension of the current-main real-hopping dictionary.
    car=[];dim=32
    for site in range(5):
        op=np.zeros((dim,dim),complex)
        for bits in range(dim):
            if bits>>site&1:
                op[bits^(1<<site),bits]=(-1)**((bits&((1<<site)-1)).bit_count())
        car.append(op)
    majors=[op+op.conj().T for op in car]
    signs=[np.eye(dim)-2*op.conj().T@op for op in car]
    ap=np.eye(dim,dtype=complex)
    for length in range(1,5):
        ap=ap@(-1j*majors[length-1]@majors[length])
        path=(1j)**(length-1)*ap
        near('ordered_Majorana_path_'+str(length),path,-1j*majors[0]@majors[length])
        real=car[0].conj().T@car[length]+car[length].conj().T@car[0]
        imag=1j*(car[0].conj().T@car[length]-car[length].conj().T@car[0])
        near('real_path_hopping_'+str(length),1j*path@(signs[0]-signs[length])/2,real)
        near('imaginary_path_hopping_'+str(length),-path@(np.eye(dim)-signs[0]@signs[length])/2,imag)
    stencils=[]
    for a in range(3):
        for j in range(3):
            if a<2 and j<2:
                disp=[tuple(sg*int(i==j) for i in range(3)) for sg in [-1,1]]
            elif a<2:
                disp=[(0,0,sg*l) for l in [1,2] for sg in [-1,1]]
            elif j<2:
                disp=[tuple(sg*int(i==j)+sz*int(i==2) for i in range(3)) for sg,sz in product([-1,1],repeat=2)]
            else:disp=[(0,0,0),(0,0,1),(0,0,-1)]
            stencils.append((a,disp))
    for box in [(1,3,3),(2,2,3),(3,3,3)]:
        cells=list(product(*(range(k) for k in box)));cellset=set(cells)
        verts={(2*c[0]+rr,c[1],c[2]) for c in cells for rr in [0,1]}
        def distance(start,end):
            todo=deque([(start,0)]);seen={start}
            while todo:
                here,d=todo.popleft()
                if here==end:return d
                if d==4:continue
                for j,sg in product(range(3),[-1,1]):
                    other=list(here);other[j]+=sg;other=tuple(other)
                    tail=min(here,other)
                    if other not in verts or other in seen or (j==1 and (tail[0]+tail[1])%2):continue
                    seen.add(other);todo.append((other,d+1))
            return 99
        lengths=[]
        for a,disps in stencils:
            for disp,c in product(disps,cells):
                dest=tuple(c[j]+disp[j] for j in range(3))
                if dest not in cellset:continue
                for rr,ss in product([0,1],repeat=2):
                    if SIG[a][rr,ss]==0:continue
                    lengths.append(distance((2*c[0]+rr,c[1],c[2]),(2*dest[0]+ss,dest[1],dest[2])))
        check('protected_vertex_paths_'+str(box),max(lengths)<=4,hops_checked=len(lengths),maximum_length=max(lengths))

    # Expand the geometric expression from its three factors, independently
    # of the proposed C2 formula. Generic symmetric fields and first jets.
    def smat(prefix):
        a=s.symbols(prefix+'0:6',real=True)
        return s.Matrix([[a[0],a[3],a[4]],[a[3],a[1],a[5]],[a[4],a[5],a[2]]])
    S=smat('s');jets=[smat('j'+str(i)+'_') for i in range(3)]
    vel=s.symbols('vel',positive=True);D=s.diag(1,1,vel)
    t=s.symbols('t',real=True);F=(s.eye(3)+t*S)*D
    inverse=D.inv()*(s.eye(3)-t*S+t*t*S*S)
    cc=-sum(s.LeviCivita(a,b,c)*F[a,i]*(t*jets[i]*D)[b,j]*inverse[j,c]
            for a,b,c,i,j in product(range(3),repeat=5))/4
    c2=sum(s.LeviCivita(a,b,c)*D[a,a]*jets[a][b,j]*S[j,c]
           for a,b,c,j in product(range(3),repeat=4))/4
    eq('connection_linear_term_zero',s.expand(cc).coeff(t,1),0)
    eq('connection_quadratic_term_generic',s.expand(cc).coeff(t,2),c2)

    # Re-establish the actual native node jets used by the uniform remainder
    # argument, without importing a sibling branch or its receipt.
    kx,ky,kz,theta=s.symbols('kx ky kz theta',real=True)
    zeta_s=s.cos(theta);v_s=s.sin(theta);b_s=zeta_s-s.cos(kz)
    native=s.Matrix([s.sin(kx),s.sin(ky),2+zeta_s-s.cos(kx)-s.cos(ky)-s.cos(kz)])
    vertices=s.Matrix([[s.sin(kx),s.sin(ky),b_s*s.sin(kz)/v_s**2],
                       [s.sin(kx),s.sin(ky),b_s*s.sin(kz)/v_s**2],
                       [s.sin(kz)*s.sin(kx)/v_s,s.sin(kz)*s.sin(ky)/v_s,b_s/v_s]])
    for sign in [-1,1]:
        sub={kx:0,ky:0,kz:sign*theta};rr=s.diag(1,1,sign)
        eq('native_zero_'+str(sign),native.subs(sub),s.zeros(3,1))
        eq('native_tangent_'+str(sign),native.jacobian([kx,ky,kz]).subs(sub),rr*s.diag(1,1,v_s))
        eq('frame_vertices_zero_'+str(sign),vertices.subs(sub),s.zeros(3))
        for j,k in enumerate([kx,ky,kz]):
            target=s.zeros(3);target[:,j]=s.Matrix([1,1,sign])
            eq('frame_vertex_jet_'+str((sign,j)),vertices.diff(k).subs(sub),target)

    # Exact annulus coefficients with truncated polynomial multiplication.
    z,w=s.symbols('z w',real=True)
    def cut(expr):return s.Poly(s.expand(expr),t).slice(0,5).as_expr()
    def inv(poly):
        c0=poly.subs(t,0);rest=cut(poly/c0-1)
        return cut(sum((-rest)**k for k in range(5))/c0)
    roots=[]
    for sign in [-1,1]:
        arg=sign*t*z+t*t/4
        roots.append(cut(sum(s.binomial(s.Rational(1,2),k)*arg**k for k in range(5))))
    pr=cut(roots[0]*roots[1]);ss=cut(roots[0]+roots[1])
    deninv=inv(cut(pr*cut(w*w*t*t+ss*ss)))
    coeff=[cut(num*ss*deninv).coeff(t,4) for num in [pr+1-t*t/4,-2,t*t/2]]
    proposed=[(35*z**4-50*z*z+15+20*w*w*(1-z*z)+8*w**4)/128,
              -(63*z**4-70*z*z+15+4*w*w*(5-7*z*z)+8*w**4)/128,
              (5*z*z-3-2*w*w)/32]
    for i in range(3):eq('annulus_coefficient_'+str(i),coeff[i],proposed[i])
    x,y=s.symbols('x y',real=True);nn=s.Matrix([x,y,z]);A=smat('a');B=smat('b')
    ua=A*nn;ub=B*nn
    poly=s.expand(coeff[0]*ua.dot(ub)+coeff[1]*nn.dot(ua)*nn.dot(ub)+coeff[2]*ua[2]*ub[2])
    mean=0
    for powers,c in s.Poly(poly,x,y,z).terms():
        if any(k%2 for k in powers):continue
        mean+=c*s.prod(s.factorial2(k-1) for k in powers)/s.factorial2(sum(powers)+1)
    K=s.Matrix([w,0,0,1]);R=(1+w*w)*s.eye(4)-K*K.T
    A4=s.diag(0,-A);B4=s.diag(0,-B)
    tensor=s.trace(R*A4*R*B4)-s.trace(R*A4)*s.trace(R*B4)/3
    eq('all_symmetric_polarizations_all_frequency_ratios',mean,tensor/80)
    lapse=s.symbols('lapse',real=True)
    eq('four_dimensional_trace_null',s.trace(R*R*B4)-s.trace(R)*s.trace(R*B4)/3,0)
    eq('two_node_measure_coefficient',2*4*s.pi/((2*s.pi)**3*80*vel),1/(80*s.pi*s.pi*vel))
    eq('Dirac_primary_source_normalization',2/s.pi**4/320*s.pi**2*2,1/(80*s.pi**2))
    eq('legacy_displayed_matching_algebra',s.solve(s.Eq(1/(16*s.pi*t),1/(48*s.pi*s.pi)),t)[0],3*s.pi)

    # Independent exact ellipsoidal phase-space contraction. The shell
    # covariance and fourth moment are contracted without the annulus series.
    om,qq=s.symbols('om qq',positive=True);L=s.diag(om*om-qq*qq,om*om-qq*qq,om*om)
    shell2=s.trace(A*L*B*L)/24
    shell4=-(s.trace(A*L)*s.trace(B*L)+2*s.trace(A*L*B*L))/120
    shelltensor=s.trace(A*L*B*L)-s.trace(A*L)*s.trace(B*L)/3
    eq('ellipsoid_fourth_moment_contraction',shell2+shell4,shelltensor/40)
    eq('ellipsoid_measure_two_nodes',2*4*s.pi/(4*(2*s.pi)**3*40),1/(160*s.pi**2))
    eq('spectral_polynomial_euclidean_continuation',shelltensor.subs({om*om:-w*w,qq:1}),tensor)
    xx,ww,aa,bb,cc=s.symbols('xx ww aa bb cc',real=True)
    pp=aa*xx*xx+bb*xx+cc
    eq('dispersion_polynomial_division',pp,(xx+ww)*(aa*xx+bb-aa*ww)+pp.subs(xx,-ww))
    Q=s.Matrix([0,0,qq]);P3=s.diag(1,1,0)
    fp=qq*qq*s.trace(A*B)-2*(A*Q).dot(B*Q)+(Q.dot(A*Q))*s.trace(B)
    fp+=(Q.dot(B*Q))*s.trace(A)-qq*qq*s.trace(A)*s.trace(B)
    eq('spatial_Fierz_Pauli_tensor',fp,qq*qq*(s.trace(P3*A*P3*B)-s.trace(P3*A)*s.trace(P3*B)))
    space,cR=s.symbols('space cR',positive=True)
    eq('finite_physical_gradient_contact_limit',s.limit(8*cR*s.sin(space*qq/2)**2/space**2,space,0),2*cR*qq*qq)
    eq('vanishing_one_particle_contact_bound',s.limit(space**3*cR*qq*qq,space,0),0)

    # Direct continuum projectors on pair-energy shells, using quadrature
    # whose angular order integrates the surviving quartic polynomial exactly.
    eta,ew=np.polynomial.legendre.leggauss(10)
    az=2*np.pi*np.arange(16)/16
    sphere=np.array([[math.sqrt(1-e*e)*math.cos(ph),math.sqrt(1-e*e)*math.sin(ph),e]
                     for e in eta for ph in az])
    weights=np.repeat(ew/2,16)/16
    polar=[np.diag([1.,0.,0.]),np.diag([0.,1.,0.]),np.diag([0.,0.,1.]),
           np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,0.]])/math.sqrt(2),
           np.array([[0.,0.,1.],[0.,0.,0.],[1.,0.,0.]])/math.sqrt(2),
           np.array([[0.,0.,0.],[0.,0.,1.],[0.,1.,0.]])/math.sqrt(2)]
    for Q in [np.array([0.,0.,.3]),np.array([.13,-.21,.34]),np.zeros(3)]:
        qabs=np.linalg.norm(Q)
        for Omega in [qabs+.07,qabs+.81]:
            LL=(Omega*Omega-Q@Q)*np.eye(3)+np.outer(Q,Q)
            le,lu=np.linalg.eigh(LL);root=(lu*np.sqrt(le))@lu.T
            p=sphere@root.T/2;pm=p-Q/2;pp=p+Q/2
            em=np.linalg.norm(pm,axis=1);ep=np.linalg.norm(pp,axis=1)
            nm=pm/em[:,None];np_=pp/ep[:,None]
            near('pair_shell_energy_'+str((Q.tolist(),Omega)),em+ep,Omega)
            actual=np.empty((6,6));target=np.empty((6,6))
            for a,b in product(range(6),repeat=2):
                ua=p@polar[a].T;ub=p@polar[b].T
                J=(1+(nm*np_).sum(1))*(ua*ub).sum(1)
                J-=(nm*ua).sum(1)*(np_*ub).sum(1)+(nm*ub).sum(1)*(np_*ua).sum(1)
                actual[a,b]=np.dot(weights,J*em*ep)/(4*np.pi**2)
                target[a,b]=(np.trace(polar[a]@LL@polar[b]@LL)
                             -np.trace(polar[a]@LL)*np.trace(polar[b]@LL)/3)/(160*np.pi**2)
            near('full_shell_projector_density_'+str((Q.tolist(),Omega)),actual,target)
            check('positive_spectral_matrix_'+str((Q.tolist(),Omega)),np.linalg.eigvalsh(actual).min()>-1e-13)

    # Independent finite position-space shift operators. Twisted boundary
    # conditions avoid exact zero modes; these are auxiliary periodic grids.
    shape=(4,3,5);sites=list(product(*(range(n) for n in shape)));index={x:i for i,x in enumerate(sites)}
    vol=len(sites);twist=np.array([.137,.211,.173]);shifts=[]
    for j in range(3):
        T=np.zeros((vol,vol),complex)
        for xx in sites:
            yy=list(xx);yy[j]=(yy[j]+1)%shape[j]
            T[index[xx],index[tuple(yy)]]=np.exp(2j*np.pi*twist[j]) if xx[j]==shape[j]-1 else 1
        shifts.append(T)
    sine=[(T-T.conj().T)/(2j) for T in shifts]
    cosine=[(T+T.conj().T)/2 for T in shifts]
    moms=np.array([[2*np.pi*(xx[j]+twist[j])/shape[j] for j in range(3)] for xx in sites])
    coords=np.array(sites);plane=np.exp(1j*coords@moms.T)/math.sqrt(vol)
    near('twisted_fourier_unitary',plane.conj().T@plane,np.eye(vol))
    for j in range(3):near('shift_symbol_'+str(j),shifts[j]@plane,plane*np.exp(1j*moms[:,j]))
    basis=[]
    for j in range(3):
        aa=np.zeros((3,3));aa[j,j]=1;basis.append(aa)
    for j,k in [(0,1),(0,2),(1,2)]:
        aa=np.zeros((3,3));aa[j,k]=aa[k,j]=1/math.sqrt(2);basis.append(aa)
    summaries=[]
    for zeta in [.5,.8]:
        vel=math.sqrt(1-zeta*zeta);ds=np.array([1.,1.,vel]);ident=np.eye(vol)
        b0=zeta*ident-cosine[2]
        spatial=[[sine[0],sine[1],b0@sine[2]/vel**2],
                 [sine[0],sine[1],b0@sine[2]/vel**2],
                 [sine[2]@sine[0]/vel,sine[2]@sine[1]/vel,b0/vel]]
        d0=[sine[0],sine[1],(2+zeta)*ident-sum(cosine)]
        h0=sum(np.kron(d0[j],SIG[j]) for j in range(3))
        energies,vectors=np.linalg.eigh(h0);occ=energies<0
        check('gapped_half_filled_grid_'+str(zeta),occ.sum()==vol and np.min(np.abs(energies))>.01,
              gap=float(np.min(np.abs(energies))))
        pminus=vectors[:,occ]@vectors[:,occ].conj().T
        near('flat_density_one_'+str(zeta),np.diag(pminus).reshape(vol,2).sum(1),np.ones(vol))
        flatops=[sum(aa[a,j]*ds[j]*np.kron(spatial[a][j],SIG[a])
                     for a,j in product(range(3),repeat=2)) for aa in basis]+[h0]
        for qn in [(0,0,0),(1,0,1),(1,1,1)]:
            q=2*np.pi*np.array(qn)/shape;phi=np.cos(coords@q);Phi=np.diag(np.repeat(phi,2))
            pos=[(Phi@op+op@Phi)/2 for op in flatops]
            mats=[vectors[:,occ].conj().T@op@vectors[:,~occ] for op in pos]
            delta=energies[~occ][None,:]-energies[occ][:,None]
            km=moms;kp=moms+q
            def symbol(k):
                sn=np.sin(k);cs=np.cos(k);bb=zeta-cs[:,2]
                dd=np.column_stack([sn[:,0],sn[:,1],2+zeta-cs.sum(1)])
                vertices=np.zeros((vol,3,3))
                vertices[:,0,:2]=vertices[:,1,:2]=sn[:,:2]
                vertices[:,0,2]=vertices[:,1,2]=bb*sn[:,2]/vel**2
                vertices[:,2,:2]=sn[:,2,None]*sn[:,:2]/vel
                vertices[:,2,2]=bb/vel
                return dd,vertices
            dm,vm=symbol(km);dp,vp=symbol(kp)
            em=np.linalg.norm(dm,axis=1);ep=np.linalg.norm(dp,axis=1)
            nm=dm/em[:,None];np_=dp/ep[:,None];gap=em+ep
            um=[np.einsum('aj,j,kaj->ka',aa,ds,(vm+vp)/2) for aa in basis]+[(dm+dp)/2]
            for omega in [0.,.47,1.3]:
                poschi=np.array([[-2*np.real(np.sum(np.conj(ma)*mb*delta/(delta*delta+omega*omega)))/vol
                                 for mb in mats] for ma in mats])
                momchi=np.empty((7,7))
                for a,b in product(range(7),repeat=2):
                    ua,ub=um[a],um[b]
                    jj=(1+np.sum(nm*np_,axis=1))*np.sum(ua*ub,axis=1)
                    jj-=np.sum(nm*ua,axis=1)*np.sum(np_*ub,axis=1)
                    jj-=np.sum(nm*ub,axis=1)*np.sum(np_*ua,axis=1)
                    momchi[a,b]=-np.mean(gap*jj/(gap*gap+omega*omega))
                factor=1 if not any(qn) else .5
                near('full_seven_source_position_response_'+str((zeta,qn,omega)),poschi,factor*momchi)
                check('negative_semidefinite_response_'+str((zeta,qn,omega)),np.linalg.eigvalsh(momchi).max()<2e-12,
                      largest_eigenvalue=float(np.linalg.eigvalsh(momchi).max()))
            # Full joint H[N,S]={N,h_F[S]}/2 has a mixed contact.
            # The affine seven-source Kato matrix above alone omits it.
            dback,vback=symbol(km-q)
            contact_pos=np.array([np.trace(pminus@(Phi@op+op@Phi)/2).real/vol for op in pos[:6]])
            contact_mom=[]
            for aa in basis:
                vec=np.einsum('aj,j,kaj->ka',aa,ds,2*vm+vp+vback)
                contact_mom.append(-np.mean(np.sum(nm*vec,axis=1))/4)
            near('joint_lapse_frame_mixed_contacts_'+str((zeta,qn)),contact_pos,factor*np.array(contact_mom))
            if qn==(1,0,1):
                aa=np.array([.31,-.23,.17,.09,-.21,.13,.27]);op=sum(aa[j]*pos[j] for j in range(7))
                exact=-2*np.sum(np.abs(sum(aa[j]*mats[j] for j in range(7)))**2/delta)/vol
                e0=energies[occ].sum();errs=[]
                for eps in [.002,.001]:
                    ee=[np.linalg.eigvalsh(h0+sign*eps*op)[:vol].sum() for sign in [-1,1]]
                    fd=(sum(ee)-2*e0)/(eps*eps*vol);errs.append(abs(fd-exact))
                check('direct_energy_second_difference_'+str(zeta),errs[-1]<3e-7,errors=errs)
                joint2=aa[6]*(Phi@sum(aa[j]*pos[j] for j in range(6))
                              +sum(aa[j]*pos[j] for j in range(6))@Phi)/2
                joint_exact=exact+2*np.trace(pminus@joint2).real/vol
                eps=.001
                ee=[np.linalg.eigvalsh(h0+sign*eps*op+eps*eps*joint2)[:vol].sum() for sign in [-1,1]]
                fd=(sum(ee)-2*e0)/(eps*eps*vol)
                near('full_joint_lapse_frame_energy_second_difference_'+str(zeta),fd,joint_exact,4e-6)
                # A native on-site quadratic source adds only its expected
                # contact at second order; evaluate the full new spectrum.
                dc=4*np.sin(q/2)**2;coef=-.37
                diff=sum((np.cos((coords+np.eye(3,dtype=int)[j])@q)-phi)**2 for j in range(3))
                onsite=np.diag(np.repeat(coef*diff,2));contact=2*np.trace(pminus@onsite).real/vol
                near('on_site_contact_exact_'+str(zeta),contact,coef*dc.sum())
                eps=.001
                ee=[np.linalg.eigvalsh(h0+sign*eps*pos[0]+eps*eps*onsite)[:vol].sum() for sign in [-1,1]]
                fd=(sum(ee)-2*e0)/(eps*eps*vol)
                original=-2*np.sum(np.abs(mats[0])**2/delta)/vol
                near('on_site_contact_changes_energy_hessian_'+str(zeta),fd,original+contact,4e-6)
        # Nonzero geometric mixed contact from A cos(qz)+B sin(qz).
        qz=2*np.pi/shape[2];zz=coords[:,2]*qz
        C2=-vel*qz/4*np.ones(vol)
        Bop=np.kron(sine[2]/vel,np.eye(2));Cdiag=np.diag(np.repeat(C2,2))
        H2=(Cdiag@Bop+Bop@Cdiag)/2
        check('mixed_geometric_contact_operator_nonzero_'+str(zeta),np.linalg.norm(H2)>.1)
        near('mixed_geometric_contact_expectation_zero_'+str(zeta),np.trace(pminus@H2),0)
        for eps in [.03,.015]:
            exactC=[]
            for phase in zz:
                a=1+eps*np.cos(phase);b=eps*np.sin(phase)
                exactC.append(-vel*eps*eps*qz/(4*(a-b*b)))
            err=max(abs(np.array(exactC)/eps**2-C2))
            check('geometric_contact_quadratic_limit_'+str((zeta,eps)),err<eps*vel*qz,
                  normalized_error=float(err))
        summaries.append(dict(zeta=zeta,volume=vol,dimension=2*vol))

    result=dict(status='ok',check_count=len(checks),checks=checks,finite_grids=summaries,
                elapsed_seconds=time.monotonic()-started,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope='Author finite and symbolic challenges. Uniform infrared remainder is an analytical argument, not a fit. Independent review pending.')
    (HERE/'BLOCK07_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':run()
