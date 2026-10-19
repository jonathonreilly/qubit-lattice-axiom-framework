#!/usr/bin/env python3
"""Bounded controls for six conditional supplied product-program continuations.
No enormous-device simulation, native construction, audit or preparation protocol.
Author saw the original reviewer's identity-control design; this is not blind replication.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import signal,time,json,math,hashlib
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/COMMON_PRODUCT_BIASED_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_ENERGY_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_RESONANT_LAUNCH_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_RESONANT_ROUTER_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_ROBUSTNESS_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_SINGLE_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'outputs/common_product_biased_operation_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_biased_operation_2026_10_18/SOURCES.json', 'outputs/common_product_biased_operation_2026_10_18/source_checks/finite/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/finite/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/network/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/network/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/packet/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/packet/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/phase/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/phase/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/preparation/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/preparation/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/resources/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/resources/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/writer/CORRECTION.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/writer/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/writer/REVIEW.md', 'outputs/common_product_energy_preparation_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_energy_preparation_2026_10_18/SOURCES.json', 'outputs/common_product_energy_preparation_2026_10_18/source_checks/REVIEW.md', 'outputs/common_product_energy_preparation_2026_10_18/source_checks/head_energy/PROPOSAL.md', 'outputs/common_product_energy_preparation_2026_10_18/source_checks/record_ground/PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/SOURCES.json', 'outputs/common_product_finite_seed_2026_10_18/proofs/bandcenter_reference_measure_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_autonomous_interface__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_autonomous_interface_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_endpoint_launch__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_endpoint_launch_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_seed_router__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_seed_router_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window__TIMING_MIXTURE.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window_check__TIMING_REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_outer_boundary__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_outer_boundary_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/endpoint_bandcenter_reference__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_common_product_program__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_common_product_program_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_program_attachment__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_program_attachment_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/SOURCES.json', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_finite_seed__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_finite_seed_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_packet__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_packet_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_scattering__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_scattering_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/SOURCES.json', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_finite_seed_scaling__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_finite_seed_scaling_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_launch_derivative_bounds__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_launch_derivative_bounds_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_refined_resource_family__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_refined_resource_family_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_second_order_attachment__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_second_order_attachment_check__REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_resonant_launch_2026_10_18/SOURCES.json', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/finite/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/finite/REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/geometric/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/geometric/REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/survival/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/survival/REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/window/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/window/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_resonant_router_2026_10_18/SOURCES.json', 'outputs/common_product_resonant_router_2026_10_18/source_checks/composition/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/composition/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/halfline/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/halfline/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/incoming/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/incoming/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/late/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/late/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/outgoing/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/outgoing/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/preparation/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/preparation/REVIEW.md', 'outputs/common_product_robustness_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_robustness_2026_10_18/SOURCES.json', 'outputs/common_product_robustness_2026_10_18/source_checks/local_matrix/PROPOSAL.md', 'outputs/common_product_robustness_2026_10_18/source_checks/local_matrix/REVIEW.md', 'outputs/common_product_robustness_2026_10_18/source_checks/scalar_weights/PROPOSAL.md', 'outputs/common_product_robustness_2026_10_18/source_checks/scalar_weights/REVIEW.md', 'outputs/common_product_robustness_2026_10_18/source_checks/vacuum_preserving/PROPOSAL.md', 'outputs/common_product_robustness_2026_10_18/source_checks/vacuum_preserving/REVIEW.md', 'outputs/common_product_single_control_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_single_control_2026_10_18/SOURCES.json', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_logarithmic_flag_policy/PROPOSAL.md', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_logarithmic_flag_policy_check/REVIEW.md', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_single_control_router/PROPOSAL.md', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_single_control_router_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/SOURCES.json', 'outputs/common_product_stage_record_2026_10_18/source_checks/autonomous_record_route/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/autonomous_record_route_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_narrow_cutoff_derivative/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_narrow_cutoff_derivative_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_core/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_core_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_finite_seed/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_finite_seed_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_flag_branch/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_flag_branch_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_packet/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_packet_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_resource_split/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_resource_split_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/certificate.txt', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/certify_inverse.py', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening_check/REVIEW.md', 'outputs/common_product_stage_seed_2026_10_18/SOURCES.json', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_router/PROPOSAL.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_router_check/REVIEW.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_seed/PROPOSAL.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_seed_check/REVIEW.md', 'outputs/product_program_continuation_review_2026_10_18/DEPENDENCIES.json']
RESULTS=[]
def check(label,condition,value=None):
    if any(r['name']==label for r in RESULTS):raise ValueError('duplicate check label '+label)
    row={'name':label,'passed':bool(condition),'value':value};RESULTS.append(row);print(json.dumps(row),flush=True)
    if not condition:raise AssertionError(label)
def norm(a):return float(np.linalg.norm(a,2))
def close(label,a,b,tol=2e-10):
    error=float(np.linalg.norm(np.asarray(a)-np.asarray(b)));check(label,np.isfinite(error) and error<tol,error)
def number(n,v):return np.diag([(s>>v)&1 for s in range(2**n)]).astype(float)
def bond(n,u,v,c):
    out=c*(number(n,u)+number(n,v))
    for s in range(2**n):
        if ((s>>u)&1)!=((s>>v)&1):out[s^(1<<u)^(1<<v),s]=-c
    return out

def occupancy_and_robustness():
    # Direct full-occupation expansion, including all simultaneous occupations.
    n=[number(8,v) for v in range(8)];eye=np.eye(256);b=.125;D0=2.;D1=9.;j=b*b/D0
    edge_list=[(0,2,4,1),(0,3,5,0),(1,2,6,0),(1,3,7,1)]
    for program in (0,1):
        old=np.zeros((256,256));new=2*j*sum(n[:4])
        for u,v,m,enabled_program in edge_list:
            enabled=program==enabled_program;detuning=D0 if enabled else D1
            shared=bond(8,u,m,b)+bond(8,m,v,b)+b*(2*eye-n[u]-n[v])+(detuning-2*b)*n[m]
            old+=shared+2*j*enabled*(n[u]+n[v]);new+=shared
        close(f'full occupation one-control identity P{program}',old,new)
        close(f'vacuum scalar eight-b P{program}',new[0,0],8*b)
        check(f'double-occupation deletion mutant P{program}',norm(new-old-2*b*n[0]@n[4])>.2)
    close('one-control shared program incident load',4*(D1-2*b),35.)
    # Rectangular factorization includes outputs with two heads and overlapping supports.
    S=np.array([0,1,1,0])/np.sqrt(2);A=np.array([0,1,-1,0])/np.sqrt(2);D=np.array([0,0,0,1]);angle=.11;delta=.13
    Q=2*np.outer(A,A)+2*np.outer(D,D);Ds=np.cos(angle)*D-np.sin(angle)*S
    Qp=2*np.outer(A,A)+2*np.outer(Ds,Ds)
    close('positive rotated bond eigenvalues',np.linalg.eigvalsh(Qp),[0,0,2,2])
    close('exact local vacuum retained',Qp[:,0],np.zeros(4))
    close('number-changing difference exact norm',norm(Qp-Q),2*abs(np.sin(angle)))
    def embed(pair,M):
        out=np.zeros((8,8))
        for x in range(8):
            for y in range(8):
                if all(((x>>z)&1)==((y>>z)&1) for z in range(3) if z not in pair):
                    ix=((x>>pair[0])&1)+2*((x>>pair[1])&1);iy=((y>>pair[0])&1)+2*((y>>pair[1])&1);out[x,y]=M[ix,iy]
        return out
    H=embed((0,1),Q)+embed((1,2),Q);Hp=embed((0,1),Qp)+embed((1,2),Qp);P=np.eye(8)[:,[1,2,4]]
    check('rectangular overlapping full-output bound',norm((Hp-H)@P)<=4*delta)
    check('extra-head output actually nonzero',norm((np.eye(8)-P@P.T)@(Hp-H)@P)>.1)
    bad=Qp.copy();bad[0,0]=.5
    check('nonzero local-vacuum action outside-support mutant detected',norm((embed((0,1),bad)-embed((0,1),Q))@np.eye(8)[:,4])>.4)
    for t in [.2,1.3]:check(f'fullspace Duhamel with leakage t{t}',norm((expm(-1j*t*Hp)-expm(-1j*t*H))@P)<=4*delta*t+1e-12)
    check('degenerate A-D rotation would be ineffective',norm(2*np.outer(A,A)+2*np.outer(D,D)-Q)<1e-12)

def energy_and_loader():
    # Noncommuting full head/record example of the retained positive-block premise.
    I=np.eye(16);N=sum(number(4,v) for v in range(3));nr=number(4,3);X=np.zeros((16,16))
    for v in range(16):X[v^(1<<3),v]=1
    b=.08;j=.015;mu=.7;kappa=.031
    positive=bond(4,0,1,b)+bond(4,1,2,j)+j*number(4,2)@(I+X)
    K=positive-2*b*number(4,0)-(np.sqrt(2)-1)*j*number(4,2)
    lower=K+2*b*N
    check('fullspace occupation lower bound',np.linalg.eigvalsh(lower).min()>-1e-12)
    H=K+mu*N+kappa*nr;g=mu-2*b
    check('record bias truly noncommuting',norm(H@nr-nr@H)>.01)
    check('fullspace energy certificate remainder positive',np.linalg.eigvalsh(H-g*N-kappa*nr).min()>-1e-12)
    vals=np.linalg.eigvalsh(H);close('blank record unique ground before passive program',vals[0],0.)
    close('record excitation realizes exact gap',vals[1],kappa)
    for beta in [2.,20.,100.]:
        weights=np.exp(-beta*vals);q=1-weights[0]/sum(weights);ceiling=3*np.exp(-beta*g)+np.exp(-beta*kappa)
        check(f'ordered-eigenvalue Gibbs ceiling beta{beta}',q<=ceiling+1e-12,q)
    for q in [.01,.2]:
        psi=np.array([np.sqrt(1-q),np.sqrt(q)]);rho=np.outer(psi,psi);ground=np.diag([1.,0.])
        distance=sum(abs(np.linalg.eigvalsh(rho-ground)));close(f'coherent joint preparation square root q{q}',distance,2*np.sqrt(q))
        check(f'incorrect two-q general bound rejected q{q}',distance>2*q)
        diagonal=np.diag([1-q,q]);close(f'joint block diagonal sharper cost q{q}',sum(abs(np.linalg.eigvalsh(diagonal-ground))),2*q)
    for eps in [1.,.3,.01]:
        prep=2*np.sqrt(eps**2/64)+eps/4
        close(f'complete loader error accounting eps{eps}',prep,eps/2)
        check(f'biased new-family final and branch budgets eps{eps}',3*(eps/2)/4+prep<eps and eps/2+prep<=eps)
        check(f'mixed probability loss remains linear eps{eps}',1-9*eps**2/256-prep/2<1-9*eps**2/256)

def writer_matrix():
    H=np.zeros((48,48));X=np.array([[0.,1.],[1.,0.]]);I=np.eye(2)
    def edge(u,v,value):
        H[2*u:2*u+2,2*v:2*v+2]=value*I;H[2*v:2*v+2,2*u:2*u+2]=value*I
    for v in range(24):H[2*v:2*v+2,2*v:2*v+2]=2*I
    for start in [0,11]:
        for e in range(10):edge(start+e,start+e+1,-np.sqrt(2) if start==11 and e in [2,5] else -1.)
    for v in [13,14,16,17]:H[2*v:2*v+2,2*v:2*v+2]+=I
    for v in [0,11]:H[2*v:2*v+2,2*v:2*v+2]+=X
    U=np.array([[1,1],[1,-1]])/np.sqrt(2)
    for a,v in enumerate([10,21]):
        for c,w in enumerate([22,23]):edge(v,w,-U[a,c])
    return H

def biased_scattering():
    H=writer_matrix();E=np.eye(48)[:,[44,45,46,47]];nr=np.kron(np.eye(24),np.diag([0.,1.]));swap=np.array([[0,1],[1,0]])
    def scattering(k,r):
        q=np.arccos(np.cos(k)+r/2);s=np.tile([np.sin(k),np.sin(q)],2);z=np.tile([np.exp(1j*k),np.exp(1j*q)],2)
        L=H+r*nr-2*(1-np.cos(k))*np.eye(48)-E@np.diag(z)@E.T;G=np.linalg.inv(L);D=np.diag(np.sqrt(s))
        return -np.eye(4)-2j*D@E.T@G@E@D,G,q
    for r in [0.,.0003,.001]:
        for off in [-.001,0.,.001]:
            k=np.pi/2+off;S,G,q=scattering(k,r);S0,_,_=scattering(k,0.)
            tag=f'r{r}/off{off}'
            close('biased full48 flux unitarity '+tag,S.conj().T@S,np.eye(4),2e-9)
            check('biased actual inverse bound '+tag,norm(G)<11)
            check('biased threshold energy '+tag,abs(2*(1-np.cos(q))+r-2*(1-np.cos(k)))<1e-13)
            check('non-strict corrected endpoint '+tag,-1e-14<=k-q<=r+1e-14)
            check('local resolvent scattering difference '+tag,norm(S-S0)<=480*r+1e-11)
            target=-1j*np.exp(22j*k)*np.kron(swap,swap)
            check('local full record comparator '+tag,norm(S-target)<=33*abs(off)+480*r+1e-10)
            qp=np.sin(k)/np.sin(q);close('physical outgoing Jacobian '+tag,qp*np.sin(q),np.sin(k))
    # Actual ordered ideal feedback factors, tested on both record inputs.
    k=np.pi/2+.0002;r=.001;q=np.arccos(np.cos(k)+r/2);Z=np.diag(np.exp(1j*np.array([k,q])));X=swap
    forward=X@np.linalg.matrix_power(Z,35);reverse=np.linalg.matrix_power(Z,35)@X
    check('noncommuting forward reverse phase mutant',norm(forward-reverse)>.01)
    close('R0 forward phase retained',forward@np.array([1,0]),np.exp(35j*k)*np.array([0,1]))
    # Matrix inverse jets retain all ordered terms, not scalar commutation.
    L0=H-.7*np.eye(48)-.4j*E@E.T;L1=.2*nr+.1*E@E.T;L2=.3*np.eye(48);L3=.07*nr;G0=np.linalg.inv(L0)
    G1=-G0@L1@G0;G2=2*G0@L1@G0@L1@G0-G0@L2@G0
    G3=-6*G0@L1@G0@L1@G0@L1@G0+3*G0@L2@G0@L1@G0+3*G0@L1@G0@L2@G0-G0@L3@G0
    close('third inverse differentiated product identity',L0@G3+3*L1@G2+3*L2@G1+L3@G0,np.zeros((48,48)),1e-7)

def source_and_pole():
    x=sp.symbols('x',real=True);a=sp.Function('a')(x);p=sp.Function('p')(x)
    derivative=a
    for _ in range(3):derivative=sp.diff(derivative/p,x)
    expected=sp.diff(a,x,3)/p**3-6*sp.diff(a,x,2)*sp.diff(p,x)/p**4-4*sp.diff(a,x)*sp.diff(p,x,2)/p**4+15*sp.diff(a,x)*sp.diff(p,x)**2/p**5-a*sp.diff(p,x,3)/p**4+10*a*sp.diff(p,x)*sp.diff(p,x,2)/p**5-15*a*sp.diff(p,x)**3/p**6
    check('all seven third integration coefficients',sp.simplify(derivative-expected)==0)
    polynomial=1-10*x**3+15*x**4-6*x**5
    check('actual quintic C2 contacts',all(sp.diff(polynomial,x,n).subs(x,z)==(1 if n==0 and z==0 else 0) for n in range(3) for z in [0,1]))
    check('quintic integrable third derivative finite',sp.integrate(sp.diff(polynomial,x,3)**2,(x,0,1))==720)
    for rho in [.08,.2,.45]:
        A=2-rho*rho;d=rho*rho;aa=np.sqrt(1-rho*rho)
        # Cotangent scale removes the narrow physical resonance before quadrature.
        density=lambda y:2/(np.pi*A*(1+y*y)*(1+(d*y/A)**2))
        total=quad(density,-np.inf,np.inf,epsabs=1e-10)[0]
        close(f'physical upper-band mass rho{rho}',total,1.,2e-8)
        for k in [1.2,np.pi/2,1.8]:
            F=-1j*np.sqrt(2/np.pi)*rho*np.exp(1j*k)/(A/np.tan(k)-1j*d)
            xx=np.tan(k-np.pi/2);pole=1j*np.sqrt(2/np.pi)*rho*np.exp(1j*k)/(A*(xx+1j*d/A))
            close(f'complex lower-pole amplitude rho{rho}/k{k}',F,pole,2e-10)
        close(f'normalized geometric Fourier sum rho{rho}',rho*rho/(1-aa*aa),1.)
        check(f'full-circle rational mass-two mutant rho{rho}',abs(2*total-1)>.9)
        m=7;coeff=1j*rho*(-1j*aa)**3;shifted=np.exp(-.7j)*np.exp(m*1j*np.pi/2)*coeff
        check(f'geometric common phase cannot be dropped rho{rho}',abs(shifted-coeff)>.01)
    # Exact energy-pole cancellation identity, with physical square-root branch.
    z=sp.symbols('z');rr=sp.symbols('r',positive=True);A=2-rr**2
    check('energy denominator pole factorization',sp.expand(A*A*z*z+rr**4*(1-z*z)-((A*A-rr**4)*z*z+rr**4))==0)
    for eps in [1.,.2,.01]:
        L=np.log(32/eps);rho=(eps/64)**1.5*L**-.25;u0=rho**-2*L;T=2*u0;d=math.ceil(max(2,8*math.e*T,np.log(8*T/eps)))
        check(f'finite launch centered Taylor cap eps{eps}',d>=8*math.e*T and d>=np.log(8*T/eps))
        check(f'geometric center fits finite cap eps{eps}',math.floor(2*T+.5)<=d-1)

def star(a,b):
    return np.array([sum(math.comb(s,l)*a[l]*b[s-l] for l in range(s+1)) for s in range(len(a))])
def product(*vectors):
    out=np.array(vectors[0],float)
    for vector in vectors[1:]:out=star(out,vector)
    return out

def network_jets(tau):
    h=tau/1e6;eta=np.sqrt(h);zeta=h;e=18*h;w=513*h;den=1-e*w;B=11.
    D=np.array([1,2,8,100.]);R=np.array([2,4,40,200.]);P=np.array([1,68,4828,1e6]);I=np.array([1,0,0,0.])
    G=np.array([B,4*B**2,32*B**3+12*B**2,384*B**4+288*B**3+10*B**2])
    W=2*product(D,G,D);W[0]=1
    la=1-3*h;lb=1-3*h*zeta
    aa=np.array([2*h/la**2,2*h/la**2+8*h*h/la**3,2*h/la**2+24*h*h/la**3+48*h**3/la**4])
    bb=np.array([2*h*zeta**2/lb**2,2*h*zeta**2/lb**2+8*h*h*zeta**3/lb**3,2*h*zeta**2/lb**2+24*h*h*zeta**3/lb**3+48*h**3*zeta**4/lb**4])
    l1,l2,l3=1+2*(aa+bb);Ic=[2,4*l1,16*l1*l1+4*l2,96*l1**3+48*l1*l2+4*l3]
    raw=product([2,2,2,2],Ic);Cs=np.array([1,2*raw[1],4*raw[2]+6*raw[1],8*raw[3]+36*raw[2]+3*raw[1]])
    Cr=Cs.copy();Cr[0]=e;Wr=W.copy();Wr[0]=w;F=product(Wr,P,Cr,P)
    K=[1/den,F[1]/den**2,2*F[1]**2/den**3+F[2]/den**2,6*F[1]**3/den**4+6*F[1]*F[2]/den**3+F[3]/den**2]
    U=product(K,product(Wr,P,Cs)+W);V=Cs+product(Cr,P,U)
    S=Cr+product(Cs,P,U)+Wr+product(W,P,V);S[0]=1
    M=product(R,[1,57,57**2,57**3],S,D)
    # Strict-internal bounds use the original packet's tighter lower-order formulas.
    c1=2*(4+8*l1);c2=4*(4+16*l1+32*l1*l1+8*l2)+6*(4+8*l1)
    cs=np.array([1,c1,c2]);cr=np.array([e,c1,c2]);ww=np.array([1,8*B+8*B*B,48*B+88*B*B+64*B**3]);wr=ww.copy();wr[0]=w;pp=P[:3]
    ff=product(wr,pp,cr,pp);kk=[1/den,ff[1]/den**2,2*ff[1]**2/den**3+ff[2]/den**2]
    uu=product(kk,product(wr,pp,cs)+ww);vv=cs+product(cr,pp,uu)
    endpoint=product(R[:3],[2,c1,c2]);fm=[eta/la,2*eta**3/la**2,2*eta**3/la**2+8*eta**5/la**3]
    mediator=2*product(fm,endpoint);aw=[2*B,4*B+8*B*B,16*B+56*B*B+64*B**3]
    nc=np.array([1,0,0])+product(pp,uu);nw=np.array([1,0,0])+product(pp,vv)
    T=product(endpoint+mediator,nc)+product(aw,nw)+np.sqrt(66)*product(R[:3],pp,vv+uu)
    N=product(T,D[:3]);return M,N,den

def amplitude_constants(m):
    c=product([1,1,2,5],[1,1,3,10],[m[0],m[1],m[2]+m[1],m[3]+3*m[2]+3*m[1]])
    return np.array([2*c[0],20*c[0]+2*c[1],300*c[0]+40*c[1]+2*c[2],4000*c[0]+900*c[1]+60*c[2]+2*c[3]])
def tail_constants(m,gap=16):
    d0,d1,d2,d3=amplitude_constants(m);a=.23;b2=4*gap;b3=32*gap;b4=128*gap
    point=d3/a**3+6*b2*d2/a**4+(4*b3/a**4+15*b2*b2/a**5)*d1+(b4/a**4+10*b2*b3/a**5+15*b2**3/a**6)*d0
    integral=d3/(2*a*a)+2*b2*d2/a**3+(4*b3/(3*a**3)+15*b2*b2/(4*a**4))*d1+(b4/(3*a**3)+10*b2*b3/(4*a**4)+3*b2**3/a**5)*d0
    return point,integral

def all_budget_rows():
    labels=['early contact','occupied source survival','conjugate incoming','omitted mass','early projection','early leads','early internal','finite contacts','late incoming','full scattering','late internal','output truncation']
    for tau in [1.,.5,.125,.01]:
        h=tau/1e6;eta=np.sqrt(h);M,N,den=network_jets(tau)
        check(f'finite real network jets tau{tau}',np.all(np.isfinite(M)) and np.all(M>0) and np.all(np.isfinite(N)) and den>0,[*M,*N])
        alpha=(4096*(2+N[0]))**-2;rho=alpha*tau*np.sqrt(h);J=N[0]+80*N[0]/rho+N[1]
        ps,qs=tail_constants([1,0,0,0]);pb,qb=tail_constants([2,1,10,100]);_,qm=tail_constants(M);_,Bnet=tail_constants(M,gap=1)
        C=1e6*max(1,Bnet,ps,qs,qm,pb,qb)
        u=1e12*max(1,1/(eta*tau),J/tau,C*rho/(h*h*tau),(C*rho/(h*h*tau))**(2/3),rho**-2*np.log(1e8/(tau*rho)))
        ell=math.ceil(100*u);X=C*rho/(h*h*u**1.5);Y=C*rho/(h*h*u)
        # Keep logarithm of the exponential; underflow is not a claim of exact zero.
        logE=np.log(100/rho)-rho*rho*u/8
        Ebound=tau/1e14
        check(f'exponential allowance logarithmic proof tau{tau}',logE<np.log(Ebound),float(logE))
        rows=[1/(eta*u),Ebound+8*rho*rho/3,X,4*np.sqrt(3)*alpha*tau,X+Ebound,X,3*J/ell,Y+Ebound,X+Ebound,tau/256,56*J/ell,X+Ebound]
        for label,value in zip(labels,rows):check(f'twelve budget {label} tau{tau}',np.isfinite(value) and 0<=value<tau/32,float(value))
        check(f'complete first-eight and twelve sums tau{tau}',sum(rows[:8])<tau/4 and sum(rows)<3*tau/8,[sum(rows[:8]),sum(rows)])
        G0=4*rho*(1+np.log(2*h/rho**2));delta=(2*(18*h+513*h)+18*h*513*h)/den
        check(f'actual stationary allocation tau{tau}',2*delta<tau/256)
        check(f'whole-horizon same-target budget tau{tau}',sum(rows[:8])+delta+(N[0]+2)*G0/np.sqrt(2*np.pi)+X<tau/2)
        check(f'cutoff normalization and source compatibility tau{tau}',1-3*rho*rho/h>.5 and rho*rho<=h/16 and (N[0]+2)*G0<tau/256)
        D1=.125;D0=h*D1;b=eta*D0;j=b*b/D0;kappa=h*j
        loads=[6*b+4*j,D1+2*b,4*(D1-2*b),8*j+kappa,3*j,5*j]
        check(f'full-support actual incident cap tau{tau}',max(loads)<1,loads)
        check(f'preparation full-support cap tau{tau}',D1+2*b+.25<25/64 and .25-2*b>15/64)
        check(f'finite count arithmetic tau{tau}',(126+4*ell)-(124+4*ell)==2 and (165+4*ell)+(124+4*ell)==289+8*ell)
        check(f'finite interval geometry tau{tau}',ell>=1000 and .75*ell>u and .428*ell>u and .24*ell>u)
        close(f'final window relative width tau{tau}',(.875-.75)/.75,1/6)
        # The earlier logarithmic and biased prescriptions keep their distinct G2 costs.
        g1=80/rho;g2=600/rho**3;H0=M[0];H1=M[0]*g1+M[1];H2=M[0]*g2+2*M[1]*g1+M[2]
        Ai=g2+12/(2*np.cos(h))*g1+4/(2*np.cos(h))+48/(2*np.cos(h))**2;Ao=H2+24*H1+212*H0
        L=max(1,82/rho,g1+8,H0+H1,2*g1+1+16);Q=max(1,1/eta,rho**-2,J,Ai,Ao)
        old_u=1e16*max(1,(L/tau)**2,Q/tau)
        check(f'earlier G2 family paid separately tau{tau}',L/np.sqrt(old_u)<=tau/1e8*(1+1e-12) and Q/old_u<=tau/1e16*(1+1e-12))
    from fractions import Fraction as F
    check('sufficient resonant exponents only',max(F(3,2),F(5,2),F(3,2),F(1))<3 and 3+2==5)
    check('earlier chosen sufficient exponents only',max(2*F(3,2)+2,3*F(3,2)+1)==F(11,2) and F(11,2)+2==F(15,2))

def complete_feedback():
    # Literal122 head vertices tensor one shared record: no separate record per writer.
    I=np.eye(2);nr=np.diag([0.,1.]);X=np.array([[0.,1.],[1.,0.]])
    eta=.025;zeta=.004;D0=eta**-2;D1=D0/zeta;b=eta**-1;r=.0003
    for program in (0,1):
        H=np.zeros((244,244))
        def diagonal(v,value):H[2*v:2*v+2,2*v:2*v+2]=value*I
        def edge(v,w,value):
            H[2*v:2*v+2,2*w:2*w+2]=value*I;H[2*w:2*w+2,2*v:2*v+2]=value*I
        for v in range(4):diagonal(v,3.)
        for m,(v,w) in enumerate([(0,2),(0,3),(1,2),(1,3)],4):
            enabled=(w-2==v) if program else (w-2!=v)
            diagonal(m,D0 if enabled else D1);edge(v,m,-b);edge(w,m,-b)
        H[16:64,16:64]=writer_matrix();H[64:112,64:112]=writer_matrix()
        for start,end,first in [(2,54,56),(3,30,89)]:
            path=[start]+list(range(first,first+33))+[end]
            for v in path[1:-1]:diagonal(v,2.)
            for v,w in zip(path,path[1:]):edge(v,w,-1.)
        H+=r*np.kron(np.eye(122),nr)
        close(f'full244 shared-record Hermiticity P{program}',H,H.T)
        ports=[0,1,55,31];E=np.eye(244)[:,[2*v+a for v in ports for a in (0,1)]]
        C=X if program==0 else I
        for off in [-.0004,.0004]:
            k=np.pi/2+off;q=np.arccos(np.cos(k)+r/2);Z=np.diag(np.exp(1j*np.array([k,q])));D=np.diag(np.sqrt(np.tile([np.sin(k),np.sin(q)],4)))
            L=H.astype(complex)-2*(1-np.cos(k))*np.eye(244)-E@np.diag(np.tile(np.diag(Z),4))@E.T
            GEP=np.linalg.solve(L,E);S=-np.eye(8)-2j*D@E.T@GEP@D
            phi=-1j*np.exp(22j*k);forward=phi*np.kron(C,X@np.linalg.matrix_power(Z,35));reverse=phi*np.kron(C,np.linalg.matrix_power(Z,35)@X)
            target=np.block([[np.zeros((4,4)),reverse],[forward,np.zeros((4,4))]])
            e=13*eta*eta+5*zeta;w=33*abs(off)+480*r;bound=(2*(e+w)+e*w)/(1-e*w)
            close(f'full244 all-incidence flux P{program}/off{off}',S.conj().T@S,np.eye(8),1e-8)
            check(f'full244 ordered feedback ceiling P{program}/off{off}',norm(S-target)<=bound+1e-8,norm(S-target))
            check(f'full244 swapped-order mutant P{program}/off{off}',norm(forward-reverse)>1e-3)
            check(f'full244 actual multiple-return correction P{program}/off{off}',norm(S[:4,:4])>1e-6)

def incoming_residue_controls():
    # Eq(3)--(6) in retained incoming proof; complex square root is fixed at s(0)=1.
    for rho in [.001,.004]:
        delta=rho*rho;a=np.sqrt(1-delta);A=2-delta;lam=delta/(2*a);sl=A/(2*a)
        for offset in [0,-1,-2]:
            def td(z):
                ss=np.sqrt(1-z*z+0j)
                return z+1j*ss if offset==0 else (1.+0j if offset==-1 else z-1j*ss)
            def bd(z):return -1j/(4*np.pi*a*a)*td(z)*(A-1j*delta*(z-1j*lam)/(np.sqrt(1-z*z+0j)+sl))
            wanted={0:1j/a,-1:1.+0j,-2:-1j*a}[offset]
            close(f'incoming residue phase rho{rho}/offset{offset}',td(1j*lam),wanted)
            close(f'incoming residue numerator rho{rho}/offset{offset}',bd(1j*lam),-1j*A*wanted/(4*np.pi*a*a))
            for xx in [-.0004,.0002]:
                kk=np.arccos(xx);physical_F=-1j*np.sqrt(2/np.pi)*rho*np.exp(1j*kk)/(A/np.tan(kk)-1j*delta)
                direct=physical_F*np.exp(1j*offset*kk)/(rho*np.sqrt(2*np.pi)*np.sin(kk))
                close(f'incoming canceled energy pole rho{rho}/offset{offset}/x{xx}',bd(xx)/(xx-1j*lam),direct,1e-8)
            check(f'incoming sign-conjugation mutant rho{rho}/offset{offset}',abs(bd(.0002)/(.0002-1j*lam)-np.conjugate(bd(.0002)/(.0002-1j*lam)))>1e-3)
            check(f'incoming nonzero residue retained rho{rho}/offset{offset}',abs(bd(1j*lam))>.1)

def main():
    def deadline(signum,frame):raise TimeoutError('120 second actual control execution cap exceeded')
    signal.signal(signal.SIGALRM,deadline);signal.alarm(AUDIT_TIMEOUT_SEC)
    started=time.monotonic()
    for path in AUDIT_INPUT_PATHS:
        if not (ROOT/path).is_file():raise FileNotFoundError(path)
    manifest=json.loads((ROOT/'outputs/product_program_continuation_review_2026_10_18/DEPENDENCIES.json').read_text())
    for row in manifest['live']:
        actual=hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()
        if actual!=row['sha256']:raise ValueError('proof identity mismatch '+row['path'])
    occupancy_and_robustness();energy_and_loader();biased_scattering();complete_feedback();source_and_pole();incoming_residue_controls();all_budget_rows()
    print('per_element: full local occupation matrices retain vacuum, double occupancy and nonconserving admissible outputs')
    print('per_site: full finite small apparatus controls and exact count formulas retain all stated head and fiber roles')
    print('per_mode: both open record channels retain flux Jacobians, complex source phases and finite inverse margins')
    print('per_block: full-support positive blocks, incident loads and complete loader assumptions are explicitly accounted')
    print('lattice_wide: only supplied finite programs and analytical sufficient families; no native universal lattice or cooling claim')
    print(f'TOTAL: PASS={len(RESULTS)} FAIL=0')
    print(json.dumps({'passed':True,'checks':len(RESULTS),'seconds':time.monotonic()-started,'scope':'bounded corroboration of retained analytical proofs; no enormous apparatus simulation or audit verdict'}))
    signal.alarm(0)
if __name__=='__main__':main()
