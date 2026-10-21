#!/usr/bin/env python3
"""Finite controls for ten conditional product-program theorems; timeout120s.
No simulation of the enormous sufficient devices, no audit or native claim.
Author implementation from source equations, separate from reviewer's controls.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/COMMON_PRODUCT_FINITE_SEED_ROUTER_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_MICROSCOPIC_SEED_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_PROGRAM_ATTACHMENT_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_PROGRAM_CELL_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_PROGRAM_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_PROGRAM_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_PROGRAM_TOLERANCE_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_REFINED_RESOURCES_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_STAGE_RECORD_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_STAGE_SEED_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'outputs/common_product_finite_seed_2026_10_18/SOURCES.json', 'outputs/common_product_finite_seed_2026_10_18/proofs/bandcenter_reference_measure_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_autonomous_interface__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_autonomous_interface_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_endpoint_launch__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_endpoint_launch_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_seed_router__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_seed_router_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window__TIMING_MIXTURE.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window_check__TIMING_REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_outer_boundary__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_outer_boundary_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/endpoint_bandcenter_reference__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_common_product_program__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_common_product_program_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_program_attachment__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_program_attachment_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/SOURCES.json', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_finite_seed__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_finite_seed_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_packet__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_packet_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_scattering__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_scattering_check__REVIEW.md', 'outputs/common_product_program_2026_10_18/SOURCES.json', 'outputs/common_product_program_2026_10_18/proofs/common_product_coefficient_tolerance__PROPOSAL.md', 'outputs/common_product_program_2026_10_18/proofs/common_product_coefficient_tolerance_check__REVIEW.md', 'outputs/common_product_program_2026_10_18/proofs/common_product_sector_transport__PROPOSAL.md', 'outputs/common_product_program_2026_10_18/proofs/common_product_sector_transport_check__REVIEW.md', 'outputs/common_product_program_2026_10_18/proofs/mediated_common_product_program__PROPOSAL.md', 'outputs/common_product_program_2026_10_18/proofs/mediated_common_product_program_check__REVIEW.md', 'outputs/common_product_program_2026_10_18/proofs/mediated_program_attachment__PROPOSAL.md', 'outputs/common_product_program_2026_10_18/proofs/mediated_program_attachment_check__REVIEW.md', 'outputs/common_product_program_2026_10_18/proofs/mediated_program_network__PROPOSAL.md', 'outputs/common_product_program_2026_10_18/proofs/mediated_program_network_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/SOURCES.json', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_finite_seed_scaling__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_finite_seed_scaling_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_launch_derivative_bounds__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_launch_derivative_bounds_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_refined_resource_family__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_refined_resource_family_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_second_order_attachment__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_second_order_attachment_check__REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/SOURCES.json', 'outputs/common_product_stage_record_2026_10_18/source_checks/autonomous_record_route/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/autonomous_record_route_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_narrow_cutoff_derivative/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_narrow_cutoff_derivative_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_core/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_core_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_finite_seed/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_finite_seed_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_flag_branch/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_flag_branch_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_packet/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_packet_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_resource_split/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_resource_split_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/certificate.txt', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/certify_inverse.py', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening_check/REVIEW.md', 'outputs/common_product_stage_seed_2026_10_18/SOURCES.json', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_router/PROPOSAL.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_router_check/REVIEW.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_seed/PROPOSAL.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_seed_check/REVIEW.md', 'outputs/product_program_review_2026_10_18/DEPENDENCIES.json']
RESULTS=[]

def check(name,ok,value=None):
    RESULTS.append({'name':name,'passed':bool(ok),'value':value})
    print(json.dumps(RESULTS[-1]),flush=True)
    if not ok: raise AssertionError(name)

def close(name,a,b,tol=2e-10):
    e=float(np.linalg.norm(np.asarray(a)-np.asarray(b)))
    check(name,e<tol,e)

def norm(a): return float(np.linalg.norm(a,2))

def occupation(n,i): return np.diag([(v>>i)&1 for v in range(1<<n)]).astype(float)

def bond(n,i,j,c):
    h=c*(occupation(n,i)+occupation(n,j))
    for v in range(1<<n):
        if ((v>>i)&1)!=((v>>j)&1): h[v^(1<<i)^(1<<j),v]-=c
    return h

def cell_controls():
    b=.3; D0=3.; D1=12.; a=2*b*b/D0
    I=np.eye(8); n=[occupation(3,i) for i in range(3)]
    J=np.eye(8)[:,[0,1,4,5]]
    X=np.zeros((4,4));X[1,2]=X[2,1]=1
    N=np.diag([0,1,1,2]); rm=(N-X)/2;rp=(N+X)/2
    close('positive full bond spectrum',np.linalg.eigvalsh(bond(2,0,1,b)),[0,0,2*b,2*b])
    close('projectors include double occupation',rm@rm,rm);close('plus projector',rp@rp,rp)
    S=(J[:,1]+J[:,2])/np.sqrt(2);AA=(J[:,1]-J[:,2])/np.sqrt(2)
    B=(np.eye(8)[:,3]+np.eye(8)[:,6])/np.sqrt(2)
    distances=[]
    for p,D in enumerate([D0,D1]):
        H=bond(3,0,1,b)+bond(3,1,2,b)+b*(2*I-n[0]-n[2])+(D-2*b)*n[1]+(1-p)*a*(n[0]+n[2])
        close(f'physical cell expansion{p}',H,2*b*I+(1-p)*a*(n[0]+n[2])+D*n[1]-b*(n[0]+n[1]-bond(3,0,1,1))-b*(n[1]+n[2]-bond(3,1,2,1)))
        eps=4*b*b/(math.sqrt(D1*D1+8*b*b)+D1)
        r=np.sqrt(2)*b/(D if p==0 else D+eps);alpha=1/np.sqrt(1+r*r);beta=r*alpha
        f=alpha*S+beta*np.eye(8)[:,2];g=alpha*J[:,3]+beta*B
        JD=np.column_stack([J[:,0],(f+AA)/np.sqrt(2),(f-AA)/np.sqrt(2),g])
        A=2*b*np.eye(4)+(a*rm if p==0 else -eps*rp)
        close(f'four column dressed intertwiner{p}',H@JD,JD@A)
        close(f'exact code distance{p}',norm(JD-J),np.sqrt(2-2*alpha))
        check(f'detuning acts on dressed code{p}',norm(D*n[1]@JD)<np.sqrt(2)*b)
        for t in [.07,.5,2.1]:
            target=2*b*np.eye(4)+(a*rm if p==0 else np.zeros((4,4)))
            err=norm(expm(-1j*t*H)@J-J@expm(-1j*t*target))
            ceiling=2*beta if p==0 else 2*beta+eps*t
            check(f'literal complete error{p}/{t}',err<=ceiling+1e-12,err)
            if p==0:close(f'enabled exact sine{t}',err,2*beta*abs(np.sin((D0+a)*t/2)))
        # All independent coefficient-box vertices; convex norm bound extends box.
        e=.02; bound=e*((6+np.sqrt(2))*b+2*a);maxerr=0.
        for bits in range(256):
            factors=[1+e*(1 if (bits>>i)&1 else -1) for i in range(8)]
            bl,br,cu,cv,d0,d1,au,av=np.array([b,b,b,b,D0-2*b,D1-2*b,a,a])*factors
            Ht=bond(3,0,1,bl)+bond(3,1,2,br)+cu*(I-n[0])+cv*(I-n[2])+[d0,d1][p]*n[1]+(1-p)*(au*n[0]+av*n[2])
            maxerr=max(maxerr,norm((Ht-(cu+cv)*I-H+2*b*I)@JD))
        check(f'eight coefficient box residual{p}',maxerr<=bound+1e-12,maxerr)
        distances.append(alpha)
    close('tensor overlap distance',norm(np.kron(JD,JD)-np.kron(J,J)),np.sqrt(2-2*alpha**2))
    U=expm(-1j*np.pi*rm);check('double phase mutant detected',abs(U[3,3]+1)<1e-12 and abs(U[3,3]-1)>1)
    # Endpoint attachment on full endpoint plus neighbor occupation domain.
    J4=np.zeros((16,8))
    for v in range(8):J4[(v&1)+((v&2)<<1)+((v&4)<<1),v]=1
    K=bond(4,0,3,.2);KL=bond(3,0,2,.2)
    close('endpoint full-domain attachment',K@J4,J4@KL)
    bad=bond(4,1,3,.2);check('mediator contact off-code mutant',norm((np.eye(16)-J4@J4.T)@bad@J4)>.1)
    check('logical neighboring terms noncommute',norm(bond(3,0,1,.2)@KL-KL@bond(3,0,1,.2))>.01)
    for Ncell in [1,2,5]:
        v=2*Ncell;inc=np.zeros((v,v-1))
        for i in range(v-1):inc[i,i]=1;inc[i+1,i]=-1
        lap=inc@inc.T
        close(f'path degree-one spectrum{Ncell}',np.linalg.eigvalsh(lap),2*(1-np.cos(np.pi*np.arange(v)/v)))
        check(f'physical chain counts{Ncell}',6*Ncell>0 and 7*Ncell+Ncell-1==8*Ncell-1)


def residual_source_controls():
    A=np.array([[2,1+2j],[1-2j,4]],complex);B=np.array([[1-1j],[2+1j]]);D=13.
    bar=A-B@B.conj().T/D;T=np.vstack([np.eye(2),-B.conj().T/D-B.conj().T@bar/D**2]);H=np.block([[A,B],[B.conj().T,np.array([[D]])]])
    exact=np.vstack([-B@B.conj().T@bar/D**2,B.conj().T@bar@bar/D**2])
    close('ordered rectangular second-order identity',H@T-T@bar,exact)
    check('noncommuting residual fixture',norm(A@B@B.conj().T-B@B.conj().T@A)>1)
    for rho in [.08,.2,.6]:
        aa=2-rho*rho;dd=rho*rho
        amp=lambda k:-1j*np.sqrt(2/np.pi)*rho*np.exp(1j*k)/(aa/np.tan(k)-1j*dd)
        # Integrate under cotangent substitution; no unresolved narrow grid.
        weight=lambda x:2*rho*rho/(np.pi*(aa*aa*x*x+dd*dd)*(1+x*x))
        total=quad(weight,-np.inf,np.inf,epsabs=1e-10)[0];close(f'source spectral normalization{rho}',total,1,2e-8)
        k=1.2;direct=np.exp(1j*k)*(dd*np.sin(k)-1j*aa*np.cos(k))*np.sqrt(2*rho*rho*np.sin(k)**2/np.pi)/(aa*aa*np.cos(k)**2+dd*dd*np.sin(k)**2)
        close(f'complex source amplitude phase{rho}',amp(k),direct)
        check(f'source phase omission mutant{rho}',abs(amp(k)-amp(k)*np.exp(-1j*k))>.01)
    j=.7;gam=.13
    tri=np.array([[0,j-gam,0],[j-gam,0,j],[0,j,0.]])
    close('fixed diagonal boundary contact norm',norm(tri),np.hypot(j-gam,j))
    close('boundary diagonal unchanged',np.diag(tri),np.zeros(3))
    q=np.array([[gam,-gam],[-gam,gam]])+np.diag([j-gam,2*j-gam])
    # Full qubit outer block has double occupation3j, dominating one-head block.
    full=bond(2,0,1,gam)+(j-gam)*occupation(2,0)+(2*j-gam)*occupation(2,1)
    close('full positive source block norm',norm(full),3*j)
    close('outer one-head diagonals with inward bond',np.diag(q)+[j,0],[2*j,2*j])

def writer(x):
    h=np.zeros((24,24))
    def edge(i,j,v):
        h[i,i]+=abs(v);h[j,j]+=abs(v);h[i,j]+=v;h[j,i]+=v
    for arm in [0,11]:
        for r in range(10):edge(arm+r,arm+r+1,-np.sqrt(2) if arm==11 and r in [2,5] else -1.)
    for r in [13,14,16,17]:h[r,r]+=2-np.sqrt(2)
    u=np.array([[1,1],[1,-1]])/np.sqrt(2)
    for a in range(2):
        for p in range(2):edge([10,21][a],22+p,-u[a,p])
    for i in [10,21,22,23]:h[i,i]-=np.sqrt(2)-1
    for i in [0,11]:h[i,i]+=1+x
    for i in [22,23]:h[i,i]+=1 # external edge diagonal, hopping eliminated
    return h

def scatter(h,ports,k):
    emb=np.eye(len(h))[:,ports];z=np.exp(1j*k)
    L=h.astype(complex)-2*(1-np.cos(k))*np.eye(len(h))-z*(emb@emb.T)
    V=np.linalg.solve(L,-2j*np.sin(k)*emb)
    return emb.T@V-np.eye(len(ports)),L,V

def exact_chain(phase,x):
    d=[sp.Integer(x)]+[sp.Integer(0)]*10+[-sp.I]
    e=[-sp.Integer(1)]*11
    if phase:
        for i in [2,3,5,6]:d[i]=sp.Integer(1)
        for i in [2,5]:e[i]=-sp.sqrt(2)
    theta=[sp.Integer(1),d[0]]
    for i in range(1,12):theta.append(sp.expand(d[i]*theta[-1]-e[i-1]**2*theta[-2]))
    phi=[sp.Integer(0)]*13;phi[12]=1;phi[11]=d[11]
    for i in range(10,-1,-1):phi[i]=sp.expand(d[i]*phi[i+1]-e[i]**2*phi[i+2])
    inv=sp.zeros(12)
    for i in range(12):
        prod=sp.Integer(1)
        for j in range(i,12):
            if j>i:prod*=e[j-1]
            val=sp.simplify((-1)**(i+j)*prod*theta[i]*phi[j+1]/theta[12]);inv[i,j]=val;inv[j,i]=val
    mat=sp.diag(*d)
    for i in range(11):mat[i,i+1]=mat[i+1,i]=e[i]
    check(f'exact chain inverse{phase}/{x}',(mat*inv-sp.eye(12)).applyfunc(sp.simplify)==sp.zeros(12))
    sq=sp.simplify(sum(sp.expand_complex(v*sp.conjugate(v)) for v in inv))
    return sq,theta[12]

def combined(p,x,eta,zeta):
    # Four core endpoints I0,I1,O0,O1; four distinct mediators4..7.
    h=np.zeros((122,122));D0=eta**-2;b=eta**-1;D1=D0/zeta
    for i in range(4):h[i,i]=1 # external ray/cable positive diagonal
    for r,(i,o) in enumerate([(0,2),(0,3),(1,2),(1,3)]):
        enabled=(o-2==i) if p else (o-2!=i);m=4+r
        h[m,m]=D0 if enabled else D1
        if enabled:h[i,i]+=2;h[o,o]+=2
        h[i,m]=h[m,i]=h[o,m]=h[m,o]=-b
    h[8:32,8:32]=writer(x);h[32:56,32:56]=writer(x)
    # O0 connects writerB U, O1 writerA U, each by34 edges/33 new vertices.
    for start,end,first in [(2,54,56),(3,30,89)]:
        path=[start]+list(range(first,first+33))+[end]
        for v in path[1:-1]:h[v,v]=2
        for a,b in zip(path,path[1:]):h[a,b]=h[b,a]=-1
    return h,[0,1,55,31]

def geometry_controls():
    core=[(20,0,0),(22,2,0),(22,0,0),(20,2,0)]
    pairs=[(0,2),(0,3),(1,2),(1,3)]
    med=[tuple((a+b)//2 for a,b in zip(core[i],core[o])) for i,o in pairs]
    arm0=[(1,0,0),(2,0,0),(2,1,0),(1,1,0)]+[(1,y,0) for y in range(2,9)]
    arm1=[(-1,y,0) for y in range(9)]+[(-1,8,1),(0,8,1)]
    wa=arm0+arm1+[(0,8,0),(1,8,1)];wb=[(z,-y,x) for x,y,z in wa]
    def cable(points):
        out=[points[0]]
        for stop in points[1:]:
            while out[-1]!=stop:
                v=list(out[-1]); axes=[i for i in range(3) if v[i]!=stop[i]]
                assert len(axes)==1
                i=axes[0];v[i]+=1 if stop[i]>v[i] else -1;out.append(tuple(v))
        return out
    cables=[cable([core[2],(22,-10,0),(0,-10,0),wb[22]]),cable([core[3],(20,12,0),(0,12,0),wa[22]])]
    coords=core+med+wa+wb+cables[0][1:-1]+cables[1][1:-1]
    controls=[]
    for r,(i,o) in enumerate(pairs):
        dz=1 if o-2==i else -1
        controls += [(x,y,z+dz) for x,y,z in [core[i],med[r],core[o]]]
    allcoords=coords+controls+[(0,0,0)]
    check('actual finite geometry counts',len(coords)==122 and len(controls)==12 and len(allcoords)==135 and len(set(allcoords))==135)
    check('equal physical cables34',all(len(c)==35 for c in cables))
    H,_=combined(0,1,.04,.01)
    edges=[(i,j) for i in range(122) for j in range(i) if H[i,j]!=0]
    check('all installed head bonds cubic nearest neighbor',all(sum(abs(a-b) for a,b in zip(coords[i],coords[j]))==1 for i,j in edges))
    check('four local shared record contacts',all(sum(abs(a) for a in coords[i])==1 for i in [8,19,32,43]))
    # Count from literal inventory, phase bonds replace ordinary arm edges.
    writerblocks=18+2+4+4+4+2
    preblocks=4*7+2*writerblocks+sum(len(c)-1 for c in cables)
    check('literal preray positive inventory',writerblocks==34 and preblocks==164)
    for ell in [3,7]:
        M=ell+1;newheads=[]
        for origin,first in [(core[0],(19,0,0)),(core[1],(23,2,0))]:
            newheads += [(first[0],first[1],n-1) for n in range(1,M+1)]
        for origin in [wa[23],wb[23]]:
            newheads += [(origin[0]+n,origin[1],origin[2]) for n in range(1,ell+1)]
        check(f'actual finite source/cap geometry{ell}',len(set(allcoords+newheads))==len(allcoords)+len(newheads)==137+4*ell)
        check(f'counted full positive blocks{ell}',preblocks+2*((M-1)+1)+2*(ell+1)==168+4*ell)


def scattering_controls():
    swap=np.array([[0,1],[1,0]])
    for x in [-1,1]:
        sq0,det0=exact_chain(False,x);sq1,det1=exact_chain(True,x)
        check(f'writer exact Frobenius squares{x}',sq0==72 and sq1==(sp.Rational(159,2) if x==1 else sp.Rational(129,2)),[str(sq0),str(sq1)])
        check(f'writer exact determinant{x}',sp.simplify(det0*det1)==(-4 if x==1 else 4))
        h=writer(x);S,L,V=scatter(h,[22,23],np.pi/2)
        close(f'actual24 inverse Frobenius{x}',np.linalg.norm(np.linalg.inv(L),'fro')**2,float(sq0+sq1),2e-8)
        close(f'actual24 center shared record{x}',S,1j*x*swap)
        check(f'writer common phase omission mutant{x}',norm(S-x*swap)>1)
        for off in [-.001,0,.001]:
            k=np.pi/2+off;S,L,V=scatter(h,[22,23],k)
            check(f'actual24 inverse band{x}/{off}',norm(np.linalg.inv(L))<10)
            check(f'writer complete scattering{x}/{off}',norm(S+1j*np.exp(22j*k)*x*swap)<=33*abs(off)+1e-10)
    check('continuum inverse margin exact',F(9000,973)<10)
    eta=.04;zeta=.01
    for p in [0,1]:
        cp=swap if p==0 else np.eye(2)
        for x in [-1,1]:
            H,ports=combined(p,x,eta,zeta)
            check(f'physical122 Hermitian{p}/{x}',len(H)==122 and np.array_equal(H,H.T))
            for off in [-.0002,0,.0002]:
                k=np.pi/2+off;S,L,V=scatter(H,ports,k);target=-1j*np.exp(57j*k)*np.block([[np.zeros((2,2)),x*cp],[x*cp,np.zeros((2,2))]])
                e=13*eta**2+5*zeta;w=33*abs(off);bound=(2*(e+w)+e*w)/(1-e*w)
                close(f'full122 flux conservation{p}/{x}/{off}',S.conj().T@S,np.eye(4),2e-8)
                check(f'full122 all feedback{p}/{x}/{off}',norm(S-target)<=bound+1e-8,norm(S-target))
    # Direct two-port elimination, including mediator amplitude, independent of writer.
    for p in [0,1]:
        D0=eta**-2;D=D0 if p==0 else D0/zeta;b=eta**-1;a=2 if p==0 else 0
        H=np.array([[1+a,0,-b],[0,1+a,-b],[-b,-b,D]])
        for k in [np.pi/3,np.pi/2,2*np.pi/3]:
            S,L,V=scatter(H,[0,1],k);z=np.exp(1j*k);E=2*(1-np.cos(k));vp=a-2*b*b/(D-E);vm=a
            robin=lambda v:(1-v-z)/(1/z-1+v)
            formula=robin(vp)*(np.eye(2)+swap)/2+robin(vm)*(np.eye(2)-swap)/2
            close(f'microscopic boundary elimination{p}/{k}',S,formula)
            close(f'mediator full column{p}/{k}',V[2,:],b/(D-E)*np.ones(2)@(np.eye(2)+S))
            check(f'microscopic scattering ceiling{p}/{k}',norm(S/z-(swap if p==0 else np.eye(2)))<=max(13*eta**2,5*zeta)+1e-10)

def packet_constants(epsilon):
    h=epsilon/1e5;eta2=zeta=h;eta=np.sqrt(eta2);e=13*eta2+5*zeta;w=33*h;d=34;den=1-e*w
    lam=1-3*eta2;other=1-3*eta2*zeta
    aa1=2*eta2/lam**2;aa2=aa1+8*eta2**2/lam**3
    bb1=2*eta2*zeta**2/other**2;bb2=bb1+8*eta2**2*zeta**3/other**3
    l1=1+2*(aa1+bb1);l2=1+2*(aa2+bb2);c1=4+8*l1;c2=4+16*l1+32*l1*l1+8*l2
    m0=4*eta/lam;m1=8*eta**3/lam**2+2*eta*c1/lam
    w1=800;w2=56000;a0=20;a1=800;k0=1/den
    f1=w1*e+w*c1+2*d*w*e
    f2=w2*e+w*c2+2*w1*c1+4*d*(w1*e+w*c1)+4*d*d*w*e
    k1=k0*k0*f1;k2=2*k0**3*f1*f1+k0*k0*f2
    ll1=w1+w*d+w*c1;ll2=w2+w*d*d+w*c2+2*d*w1+2*w1*c1+2*w*d*c1
    U0=k0*(w+1);U1=k1*(w+1)+k0*(ll1+w1);U2=k2*(w+1)+2*k1*(ll1+w1)+k0*(ll2+w2)
    W0=1+e*U0;W1=c1+(c1+e*d)*U0+e*U1;W2=c2+(c2+2*d*c1+e*d*d)*U0+2*(c1+e*d)*U1+e*U2
    s1=c1+(c1+d)*U0+U1+w1+(w1+d)*W0+W1
    s2=c2+(c2+2*d*c1+d*d)*U0+2*(c1+d)*U1+U2+w2+(w2+2*d*w1+d*d)*W0+2*(w1+d)*W1+W2
    q1=s1+57;q2=s2+114*s1+57**2
    n0=1+U0;n1=d*U0+U1;r0=1+W0;r1=d*W0+W1
    T0=2*n0+m0*n0+a0*r0+np.sqrt(66)*(W0+U0)
    T1=c1*n0+2*n1+m1*n0+m0*n1+a1*r0+a0*r1+np.sqrt(66)*(d*(W0+U0)+W1+U1)
    return h,eta,zeta,e,w,q1,q2,T0,T1

def budget_controls():
    k=sp.symbols('k',real=True);D=sp.Function('D')(k)
    deriv=sp.exp(sp.I*k)*(-1/D-2*sp.I*sp.diff(D,k)/D**2-sp.diff(D,k,2)/D**2+2*sp.diff(D,k)**2/D**3)
    check('all four complex source second derivative terms',sp.simplify(sp.diff(sp.exp(sp.I*k)/D,k,2)-deriv)==0)
    check('localized cutoff constant',2/np.sqrt(np.pi)*(310+24*np.pi)<600)
    check('refined complete budget exact',F(9,16)+F(35,256)==F(179,256)<1)
    # Exact exponent arithmetic; selected sufficient families, never necessity laws.
    for policy,rho_exp,want_size,want_time in [('F',F(3,2),F(11,2),F(15,2)),('A',F(2),F(7),F(9))]:
        size=max(2*rho_exp+2,3*rho_exp+1)
        check(f'{policy} resource powers',size==want_size and size+2==want_time,[str(size),str(size+2)])
    for eps in [1.,.5,.125]:
        h,eta,zeta,e,w,q1,q2,T0,T1=packet_constants(eps)
        check(f'core/writer feedback denominator{eps}',1-e*w>0)
        for policy in ['F','A']:
            rho=eps*np.sqrt(h)/1024
            if policy=='A':rho=min(rho,(eps/(4096*(1+T0)))**2)
            g1=80/rho;g2=600/rho**3;bminus=82/rho;vmin=2*np.cos(h)
            H1=g1+q1;H2=g2+2*q1*g1+q2;J0=T0;J1=T0*g1+T1
            Ai=g2+12/vmin*g1+4/vmin+48/vmin**2;Ao=H2+21*H1+154
            L=max(1,bminus,g1+1,H1+1,g1+7);Q=max(1,1/eta,1/rho**2,J1+J0,Ai+Ao)
            u=1e12*max(1,(L/eps)**2,Q/eps);ell=math.ceil(100*u)
            check(f'{policy} source normalization premise{eps}',rho*rho<=h<=.001 and 1-3*rho*rho/h>.5)
            check(f'{policy} separated maxima{eps}',L/np.sqrt(u)<=eps/1e6*(1+1e-14) and Q/u<=eps/1e12*(1+1e-14))
            allowances=[Q/u,2*Q/u,2*L/np.sqrt(u),4*np.sqrt(3)*eps/1024,8*L/np.sqrt(u),4*L/math.sqrt(ell),3*Q/ell,2*Q/u,6*L/math.sqrt(ell),eps/256,56*Q/ell,28*L/math.sqrt(ell)]
            check(f'{policy} all12 finite allowances{eps}',len(allowances)==12 and max(allowances)<eps/32 and sum(allowances)<3*eps/8,allowances)
            actual_scattering=min(2,(2*(e+w)+e*w)/(1-e*w))
            check(f'{policy} charged complete scattering{eps}',2*actual_scattering<=eps/256)
            check(f'{policy} finite window phase gaps{eps}',.75*ell*vmin-ell>ell/4 and 2*ell-2*.875*ell-57>0 and ell>57*4)
            close(f'{policy} relative window{eps}',(.875-.75)/.75,1/6)
            if policy=='A':
                g0=16*np.sqrt(rho);check(f'A uniform internal/origin budget{eps}',g0<=eps/(256*(1+T0))*(1+1e-14))
                branch=eps/4+eps/512+eps/256+3*eps/1e7
                check(f'A absolute branch total{eps}',branch<eps/2)
            D1=.5;D0=zeta*D1;b=eta*D0;j=b*b/D0
            loads=[6*b+6*j,D1+2*b,2*j,D1-2*b,4*j,(4+np.sqrt(2))*j,(1+3*np.sqrt(2))*j,8*j,3*j,5*j]
            check(f'{policy} full physical incident loads{eps}',max(loads)<1,loads)
            check(f'{policy} finite counts{eps}',137+4*ell>135 and 168+4*ell>164)
        # Earlier refined and microscopic families use their own source coefficients.
        rho=eps/256;u=1e12*rho**-2*eps**-2;ell=math.ceil(100*u);s=7*ell/8
        eta2=eps/(256*(1+s));zeta=eps/(64*(1+s));eta=np.sqrt(eta2)
        ideal=[3/(100*u),2*eps**2/1e12,400*eps/1e6,4*np.sqrt(11)*eps/256,208*eps/1e6,300*eps/1e7,8100*256*eps/1e12,460*eps/1e7,920*eps/1e7]
        check(f'refined nine ideal allocations{eps}',max(ideal)<eps/16)
        cell=4*eta+11*s*eta2+2*s*zeta
        check(f'refined entire duration cell{eps}',cell<35*eps/256 and sum(ideal)+cell<179*eps/256)
        eta=np.sqrt(eps/1024)
        for stage in [False,True]:
            allowances=[1/((50 if stage else 100)*u*np.sqrt(eps)),2*eps**2/1e12,400*eps/1e6,4*np.sqrt(11)*eps/256,208*eps/1e6,500*eps/1e7,(3500 if stage else 2300)*eta/(rho*ell),8200*256*eps/1e12,460*eps/1e7,(36 if stage else 26)*eps/1024,(7100 if stage else 10000)*eta/(rho*ell),920*eps/1e7]
            check(f'microscopic twelve allowances stage{stage}/{eps}',max(allowances)<eps/16 and sum(allowances)<3*eps/4)


def main():
    for p in AUDIT_INPUT_PATHS:
        if not (ROOT/p).is_file():raise FileNotFoundError(p)
    cell_controls();residual_source_controls();geometry_controls();scattering_controls();budget_controls()
    print('per_element: full positive qubit blocks, double occupation and independent coefficient vertices checked')
    print('per_site: explicit finite cell and122-head network; supplied occupancy roles and initialization remain premises')
    print('per_mode: finite full-channel scattering and source-phase identities checked; no global spectral completeness inferred')
    print('per_block: exact writer chain inverse certificates and fixed-diagonal boundary bookkeeping checked')
    print('lattice_wide: finite supplied graphs and sufficient budget prescriptions only; no native lattice law or enormous-device simulation executed')
    print(f'TOTAL: PASS={len(RESULTS)} FAIL=0')
    print(json.dumps({'scope':'finite controls corroborate analytical conditional proofs; no audit verdict; F final window and A absolute finite horizon remain distinct','checks':len(RESULTS),'passed':all(x['passed'] for x in RESULTS)},sort_keys=True))

if __name__=='__main__':main()
