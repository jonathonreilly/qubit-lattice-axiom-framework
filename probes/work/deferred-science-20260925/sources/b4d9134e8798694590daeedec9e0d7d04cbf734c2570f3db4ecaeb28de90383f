#!/usr/bin/env python3
"""Disclosed root controls for the original-record bridge; no empirical fit."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ORIGINAL_FORMATION_RECORD_PHOTON_READOUT_AND_MICROSCOPIC_FINITE_BINS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from collections import defaultdict, Counter
from itertools import product
from pathlib import Path
import hashlib, json, time, math
import numpy as np
import scipy
from scipy.linalg import eigh
from scipy import sparse
from scipy.sparse.linalg import expm_multiply
from numpy.polynomial.legendre import leggauss
import mpmath as mp
import sympy as sp
mp.mp.dps=80
ROOT_CONTROL_SOURCES = [('record-photon-readout-personal/record_photon_readout_controls.py', '0ed685625ec78c571229885c5fbca8e3e538f2ca5f7516fccaf8fa0a50dab4b0'), ('record-photon-readout-personal/narrow_packet_control.py', '9331da643e2b6be3a80abbcb43cd59e5fb8684417af4697e324aa37a5bff3b0a'), ('microscopic-record-readout-personal/finite_register_controls.py', 'dc9952e2ae47f69cc9a258b72c01d009b356b6459e168e830dc045dfaca59771'), ('magnetic-lag-photon-personal/magnetic_lag_controls.py', '337a224e11f31f835510ef1a7d0a7b91cae2a5a96ff7323f1fd98eee2fbd0225')]
RESULT_PATH = 'outputs/original_record_photon_bridge_20260924/ORIGINAL_RECORD_PHOTON_BRIDGE_RESULTS.json'

def geometry(periods):
    vertices=tuple(product(*(range(L) for L in periods)))
    ix={v:i for i,v in enumerate(vertices)}
    A={i for i,v in enumerate(vertices) if sum(v)%2==0}
    edges=[]
    for a in sorted(A):
        neighbors=set()
        for j,L in enumerate(periods):
            for sign in (-1,1):
                p=list(vertices[a]);p[j]=(p[j]+sign)%L;neighbors.add(ix[tuple(p)])
        edges.extend((a,b) for b in sorted(neighbors))
    adj=defaultdict(list)
    for e,(a,b) in enumerate(edges):adj[a].append((b,e))
    return vertices,ix,A,tuple(edges),adj

def marked_words(periods):
    vv,ix,A,edges,adj=geometry(periods);nd=len(periods)
    def v(x,y,z=0):return ix[tuple((x,y,z)[:nd])]
    a,d=v(0,0),v(1,1)
    if periods==(2,2,2):b,f=v(0,0,1),v(1,1,1)
    else:b,f=v(periods[0]-1,0),v(2,1)
    q0=tuple(1 if i in A else 0 for i in range(len(vv)))
    e0=(0,)*len(edges);psi={(q0,e0):1}
    def valid(q,flux):
        div=[0]*len(vv)
        for (aa,bb),val in zip(edges,flux):div[aa]+=val;div[bb]-=val
        assert all(div[i]==q[i]-q0[i] for i in range(len(vv)))
    def B(states,aa,bb,signs):
        out=defaultdict(int);eb=edges.index((aa,bb))
        for (q,flux),amp in states.items():
            old=q[aa]
            if not old or q[bb]:continue
            for cc,ec in adj[aa]:
                if cc==bb or q[cc]:continue
                qh=list(q);eh=list(flux)
                qh[aa]=0;qh[cc]=old;eh[ec]-=old;valid(qh,eh)
                for sigma in signs:
                    qj=qh.copy();ej=eh.copy();qj[aa]=sigma;qj[bb]=-sigma;ej[eb]+=sigma
                    valid(qj,ej);out[tuple(qj),tuple(ej)]+=amp
        return dict(out)
    def effect(states):
        grouped=defaultdict(list)
        for (q,e),amp in states.items():grouped[q].append((e,amp))
        kernel=Counter()
        for entries in grouped.values():
            for e,amp in entries:
                for ep,ampt in entries:
                    shift=tuple(y-x for x,y in zip(e,ep));kernel[shift]+=amp*ampt
        return kernel
    rows=[]
    z=len(adj[a]);constant=(z-1)**2-2
    for signs1,signs2 in product(((-1,),(1,),(-1,1)),repeat=2):
        first=B(psi,a,b,signs1);second=B(first,d,f,signs2);eff=effect(second)
        mult=len(signs1)*len(signs2)
        assert effect(first)==Counter({e0:len(signs1)*(z-1)})
        assert eff[e0]==mult*constant
        shifts=[k for k,vv in eff.items() if k!=e0 and vv]
        assert len(shifts)==2 and shifts[0]==tuple(-v for v in shifts[1])
        assert set(eff[k] for k in shifts)=={mult}
        assert all(sum(v*v for v in k)==4 for k in shifts)
        for k in shifts:
            valid(q0,k)
        # Actually dephase the intermediate matter, then apply the second mark.
        first_by_charge=defaultdict(dict)
        for state,amp in first.items():first_by_charge[state[0]][state]=amp
        pinched=Counter()
        for sector in first_by_charge.values():pinched.update(effect(B(sector,d,f,signs2)))
        assert pinched==Counter({e0:mult*constant})
        rows.append({'signs1':signs1,'signs2':signs2,'first_paths':len(first),
                     'second_words':len(second),'constant':eff[e0],
                     'plaquette_coefficients':[eff[k] for k in shifts],
                     'plaquette_shifts':[[[i,x] for i,x in enumerate(k) if x] for k in shifts],
                     'after_extra_matter_dephasing_constant':pinched[e0],
                     'extra_matter_dephasing_contrast':0})
    return {'periods':periods,'vertices':len(vv),'edges':len(edges),'degree':z,'rows':rows}

def rotor_error_control(g,N=256):
    # Separate one-circle rotor, H=(g^2/2)E^2+(1-cos A)/g^2.
    # These are numerical controls of the O(g^4) expectation-error mechanism,
    # not the cubic many-body or marked-process theorem.
    theta=2*np.pi*np.arange(N)/N-np.pi
    modes=np.fft.fftfreq(N,d=1/N)
    eye=np.eye(N)
    kinetic=np.fft.ifft((modes*modes)[:,None]*np.fft.fft(eye,axis=0),axis=0).real
    H=(g*g/2)*kinetic+np.diag((1-np.cos(theta))/(g*g))
    ev,U=eigh(H,check_finite=False);O=2*(np.cos(theta)-1)
    rows=[];chars={}
    for n in (0,1):
        psi=np.exp(-theta**2/(2*g*g))
        if n:psi*=np.sqrt(2)*theta/g
        psi/=np.linalg.norm(psi)
        coeff=U.T@psi
        for t in (.7,2.,4.):
            actual=U@(np.exp(-1j*t*ev)*coeff)
            ref=np.exp(-1j*(n+.5)*t)*psi
            err=np.linalg.norm(actual-ref)
            expect_actual=np.vdot(actual,O*actual).real
            expect_ref=np.vdot(ref,O*ref).real
            bound=2*err*np.linalg.norm(O*ref)+4*err*err
            assert abs(expect_actual-expect_ref)<=bound+1e-13
            gaussian_char=np.exp(-g*g/4)*(1-n*g*g/2)
            char=np.vdot(actual,np.cos(theta)*actual).real
            chars[n,t]=char
            rows.append({'g':g,'grid':N,'n':n,'time':t,'vector_error_over_g2':float(err/(g*g)),
                         'observable_error_over_g4':float(abs(expect_actual-expect_ref)/(g**4)),
                         'expectation_error_bound':float(bound),
                         'reference_characteristic_error':float(abs(np.vdot(ref,np.cos(theta)*ref).real-gaussian_char)),
                         'actual_cosine':float(char)})
    return {'rows':rows,'contrast_rows':[{'g':g,'time':t,
            'actual_one_minus_vac_over_g2':float((chars[1,t]-chars[0,t])/(g*g)),
            'harmonic_one_minus_vac_over_g2':float(-.5*np.exp(-g*g/4))}
              for t in (.7,2.,4.)]}

def selection_rules():
    W=sp.diag(0,1,0,1,0);N=sp.diag(0,0,2,2,4);P=sp.diag(1,0,1,0,1)
    T=sp.zeros(5);C=sp.diag(1,0,1,0,0);j=sp.zeros(5)
    T[0,1]=T[1,0]=T[2,3]=T[3,2]=-1;j[2,1]=j[4,3]=1
    assert W*j-j*W==-j and j*P==sp.zeros(5)
    assert N*j-j*N==2*j and N*T==T*N and C*W==W*C
    A=W*T*P;M=A.T*A;C0=P*C*P
    H2=C0-M;H4=M*M-(M*C0+C0*M)/2+A.T*(W*C*W)*A
    Beff=-P*j*W*T*P
    assert H2==H4==sp.zeros(5)
    assert Beff[2,0]==Beff[4,2]==1 and sum(abs(v) for v in Beff)==2
    # Fixed-bin word append is isometric on legal prefixes; the terminal
    # missing image is irrelevant because the corresponding physical j=0.
    words=[(),(0,),(1,),(0,0),(0,1),(1,0),(1,1)]
    checked=0
    for symbol in (0,1):
        images=[w+(symbol,) for w in words if len(w)<2]
        assert len(images)==len(set(images));checked+=len(images)
    assert j[:,4]==sp.zeros(5,1)
    return {'states':['P0','Q0','P1','Q1','P2'],'H2_zero':True,'H4_zero':True,
            'effective_transitions':[[0,2,1],[2,4,1]],'legal_append_images_checked':checked,
            'scope':'Separate abstract parent-class finite model; not the actual cube.'}

def waiting_cdf(epsilon,delta,kappa,u):
    e=epsilon
    a=-1j*delta/e**2;d=-1j*delta/e**4-kappa/(2*e**2);off=1j*delta/e**3
    tr=a+d;det=a*d-off*off;root=mp.sqrt(tr*tr-4*det)
    ls,lf=sorted(((tr+root)/2,(tr-root)/2),key=abs)
    ce=off/(ls-lf)
    def integ(z):return mp.expm1(z*u)/z if z else u
    value=kappa/e**2*abs(ce)**2*(integ(2*mp.re(ls))+integ(2*mp.re(lf))-2*mp.re(integ(ls+mp.conj(lf))))
    assert abs(mp.im(value))<mp.mpf('1e-65')
    value=mp.re(value)
    assert -mp.mpf('1e-60')<=value<=1+mp.mpf('1e-60')
    return value

def waiting_controls():
    delta=mp.mpf(1);kappa=mp.mpf('.7');t=mp.mpf('.3');h=mp.mpf('.4');b=mp.mpf('.1')
    target=(mp.exp(-kappa*t)-mp.exp(-kappa*(t+h)))*(-mp.expm1(-kappa*b))
    rows=[]
    for se in ('.4','.2','.1','.05','.025','.0125'):
        e=mp.mpf(se);F=lambda u:waiting_cdf(e,delta,kappa,u)
        prob=(F(t+h)-F(t))*F(b);tiny=e**6;ratio=F(tiny)/(kappa*tiny)
        asympt=delta**2*e**4/3
        rows.append({'epsilon':se,'fixed_bin_probability':str(prob),'target_probability':str(target),
                     'fixed_bin_absolute_error':str(abs(prob-target)),
                     'shrinking_bin':str(tiny),'microscopic_CDF_over_kappa_bin':str(ratio),
                     'target_CDF_over_kappa_bin':str(-mp.expm1(-kappa*tiny)/(kappa*tiny)),
                     'ratio_to_predicted_small_bin_asymptotic':str(ratio/asympt)})
    assert mp.mpf(rows[-1]['fixed_bin_absolute_error'])<mp.mpf('1e-4')
    assert abs(mp.mpf(rows[-1]['ratio_to_predicted_small_bin_asymptotic'])-1)<mp.mpf('1e-6')
    assert mp.mpf(rows[-1]['microscopic_CDF_over_kappa_bin'])<mp.mpf('1e-7')
    return rows

def grid_controls():
    k=mp.mpf('.7');T=mp.mpf('1.2');t=mp.mpf('.3');h=mp.mpf('.4');b=mp.mpf('.1')
    exact=(mp.exp(-k*t)-mp.exp(-k*(t+h)))*(-mp.expm1(-k*b));rows=[]
    for mm in (6,12,24,48,96):
        eta=T/mm;lower=upper=mp.mpf(0);total=mp.mpf(0)
        for r in range(mm):
            x0=r*eta;x1=(r+1)*eta
            for s in range(r,mm):
                y0=s*eta;y1=(s+1)*eta
                if r==s:mass=mp.exp(-k*x0)*(1-mp.exp(-k*eta)*(1+k*eta))
                else:mass=eta*k*(mp.exp(-k*y0)-mp.exp(-k*y1))
                total+=mass
                intersects=x1>t and x0<t+h
                subset=x0>=t and x1<=t+h
                minlag=max(mp.mpf(0),y0-x1);maxlag=y1-x0
                if intersects and minlag<=b:upper+=mass
                if subset and maxlag<=b:lower+=mass
        assert abs(total-(1-mp.exp(-k*T)*(1+k*T)))<mp.mpf('1e-65')
        assert lower<=exact+mp.mpf('1e-65') and exact<=upper+mp.mpf('1e-65')
        assert upper-lower<=8*k*eta
        rows.append({'bins':mm,'mesh':str(eta),'lower':str(lower),'exact':str(exact),
                     'upper':str(upper),'sandwich_gap':str(upper-lower),
                     'proved_loose_gap_bound':str(8*k*eta),'all_two_event_word_mass':str(total)})
    return rows

def probe(g, cutoff_width):
    n = math.ceil(cutoff_width / g) + 3
    m = np.arange(-n, n + 1, dtype=float)
    d = len(m)
    eye = sparse.eye(d, format="csc", dtype=complex)
    shift = sparse.diags(np.ones(d-1), -1, shape=(d, d), format="csc", dtype=complex)
    cosine = (shift + shift.getH()) / 2
    h0 = (g*g/2)*sparse.diags(m*m, format="csc") + (eye-cosine)/(g*g)
    v0 = np.exp(-g*g*m*m/2).astype(complex)
    v1 = -1j*g*m*v0
    v0 /= np.linalg.norm(v0)
    v1 /= np.linalg.norm(v1)
    states = expm_multiply(-0.23j*h0, np.column_stack([v0, v1]))
    norm_defects = np.sum(np.abs(states)**2, axis=0)-1
    assert np.max(np.abs(states.conj().T @ states - np.eye(2))) < 1e-11
    # Correct numerical unitary norm drift before resolving a small contrast
    # against the common constant background; the exact orbit is normalized.
    states /= np.linalg.norm(states, axis=0)
    h4 = sparse.bmat([
        [-3*eye+0.4*cosine, eye+0.2*cosine],
        [eye+0.2*cosine, -3*eye-0.4*cosine]], format="csc")
    # A finite Laurent jump with three terminal outputs. In the infinite
    # model L*L[0,0]=(23+2 cos(theta))/5 exactly.
    jump = sparse.bmat([
        [math.sqrt(21/5)*eye, None],
        [(eye+shift)/math.sqrt(5), 0.3*eye],
        [None, 2*eye]], format="csc")
    effect = jump.getH() @ jump
    loss = effect + sparse.eye(2*d, format="csc")
    electric = sparse.block_diag([
        sparse.diags(m*m), sparse.diags(m*(m-1))], format="csc")
    kappa = 0.3
    generator = -1j*((g*g/2)*electric + h4/(4*g*g)) - kappa*loss/2
    magnetic = -1j*h4/(4*g*g)
    eta = np.vstack([math.sqrt(5)*(shift @ states), np.zeros_like(states)])
    boundary = np.sum(eta.conj()*(effect @ eta), axis=0).real
    boundary_delta = boundary[1]-boundary[0]
    edge_mass = float(np.sum(np.abs(states[:3])**2)+np.sum(np.abs(states[-3:])**2))
    assert edge_mass < 1e-15
    nodes, weights = leggauss(20)
    rows = []
    for family, b in [("b_0.2_g3", 0.2*g**3),
                      ("b_0.2_g2", 0.2*g*g)]:
        full_values, magnetic_values, errors = [], [], []
        for z in nodes:
            u = b*(z+1)/2
            full = expm_multiply(u*generator, eta)
            mag = expm_multiply(u*magnetic, eta)
            assert np.max(np.linalg.norm(full, axis=0)-np.linalg.norm(eta,axis=0)) < 2e-11
            full_values.append(np.sum(full.conj()*(effect @ full),axis=0).real)
            magnetic_values.append(np.sum(mag.conj()*(effect @ mag),axis=0).real)
            errors.append(float(np.max(np.linalg.norm(full-mag,axis=0))/u))
        full_integral = b*np.dot(weights,np.array(full_values))/2
        magnetic_integral = b*np.dot(weights,np.array(magnetic_values))/2
        delta = full_integral[1]-full_integral[0]
        rows.append({
            "family":family, "b":b, "b_over_g2":b/g**2, "b_over_g4":b/g**4,
            "integrated_effect_vacuum":float(full_integral[0]),
            "integrated_effect_packet":float(full_integral[1]),
            "contrast_over_b_g2":float(delta/(b*g*g)),
            "boundary_contrast_over_g2":float(boundary_delta/(g*g)),
            "lag_contrast_remainder_over_b2":float((delta-b*boundary_delta)/(b*b)),
            "magnetic_contrast_over_b_g2":float((magnetic_integral[1]-magnetic_integral[0])/(b*g*g)),
            "maximum_sampled_full_minus_magnetic_norm_over_u":max(errors)})
    return {"g":g,"cutoff_width":cutoff_width,"fourier_cutoff":n,
            "component_dimension":d,"initial_orbit_edge_mass":edge_mass,
            "numerical_prebirth_squared_norm_defects_before_normalizing":norm_defects.tolist(),"rows":rows}

def narrow_controls():
    start=time.monotonic()
    N=12
    ann=np.diag(np.sqrt(np.arange(1,N)),1);q=ann+ann.T
    d=np.array([.7,-.4]);X=d[0]*np.kron(q,np.eye(N))+d[1]*np.kron(np.eye(N),q)
    ev,U=eigh(X);vac=np.zeros(N*N,dtype=complex);vac[0]=1
    alpha=np.array([np.sqrt(.3),1j*np.sqrt(.7)]);omega=np.array([.9,1.7])
    fock=[]
    for g in (.1,.25,.4):
        W=(U*np.exp(1j*g*ev))@U.T
        for t in (0.,.7,2.,4.):
            at=alpha*np.exp(-1j*omega*t);psi=np.zeros(N*N,dtype=complex)
            psi[N]=at[0];psi[1]=at[1]
            chi=np.dot(at,d);expected=np.exp(-g*g*np.dot(d,d)/2)*(1-g*g*abs(chi)**2)
            actual=np.vdot(psi,W@psi);error=abs(actual-expected)
            assert error<2e-13
            fock.append({'g':g,'time':t,'chi_abs_squared':float(abs(chi)**2),
                         'actual_real':float(actual.real),'actual_imaginary':float(actual.imag),
                         'formula':float(expected),'absolute_error':float(error)})

    L=64;V=L*6*6;k=2*np.pi*np.array([5,6,7])/L;k0=k[1];sigma=k[2]-k0
    omegas=2*np.sin(k/2);omega0=2*np.sin(k0/2);velocity=np.cos(k0/2)
    weights=np.array([1.,2.,1.])/np.sqrt(6)*np.exp(-1j*k*10)
    d0=(np.exp(1j*k)-1)/np.sqrt(2*V)/np.sqrt(omegas)
    A=float(np.sum(abs(weights*d0)));M=float(np.pi/(k0-sigma));xs=np.arange(L)
    packets=[]
    for t in (0.,8.,20.):
        actual=np.exp(1j*np.outer(xs,k))@(weights*d0*np.exp(-1j*omegas*t))
        linear=np.exp(1j*np.outer(xs,k))@(weights*d0*np.exp(-1j*(omega0+velocity*(k-k0))*t))
        error=float(np.max(abs(actual-linear)));bound=A*M*t*sigma*sigma/2
        contrast_error=float(np.max(abs(abs(actual)**2-abs(linear)**2)))
        contrast_bound=A*A*M*t*sigma*sigma
        assert error<=bound+1e-16 and contrast_error<=contrast_bound+1e-16
        packets.append({'time':t,'max_amplitude_error':error,'amplitude_bound':bound,
                        'max_intensity_error':contrast_error,'intensity_bound':contrast_bound,
                        'actual_peak_site':int(np.argmax(abs(actual)**2)),
                        'linear_peak_site':int(np.argmax(abs(linear)**2))})
    result={'scope':'Separate Fock space and harmonic packet controls, not telescope data or full postbirth propagation',
            'finite_fock_rows':fock,'packet_parameters':{'V':V,'k0':float(k0),'band_radius':float(sigma),
                  'group_velocity_sites_per_time':float(velocity),'coarse_Hessian_bound':M,'A':A},
            'packet_rows':packets,'elapsed_seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return result

def main():
    start=time.monotonic()
    probes=[probe(g,w) for g in (.4,.2,.1,.05) for w in (8,10)]
    differences=[]
    for coarse,fine in zip(probes[::2],probes[1::2]):
        values=[abs(a["contrast_over_b_g2"]-b["contrast_over_b_g2"])
                for a,b in zip(coarse["rows"],fine["rows"])]
        assert max(values)<2e-9
        differences.append({"g":fine["g"],"scaled_contrast_cutoff_differences":values})
    assert abs(probes[-1]["rows"][0]["contrast_over_b_g2"]+1)<.04
    result={
      "scope":"Author controls, not new independent computations; auxiliary models and observations are distinguished.",
      "primitive_graphs":[marked_words(p) for p in ((2,2,2),(6,6),(6,6,6))],
      "separate_rotor_controls":[rotor_error_control(g) for g in (.3,.2,.14,.1,.07)],
      "grid_repeat":rotor_error_control(.1,512),
      "narrow_controls":narrow_controls(),
      "separate_five_state_register":{"selection_rules":selection_rules(),"waiting_rows":waiting_controls(),"grid_rows":grid_controls()},
      "separate_two_component_rotor":{"probes":probes,"cutoff_comparisons":differences},
      "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "elapsed_seconds":time.monotonic()-start,
      "all_assertions_passed":True}
    path=Path(__file__).resolve().parents[1]/RESULT_PATH
    path.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(result,indent=2,allow_nan=False)+"\n"
    path.write_text(data)
    print(data,end="")
    print("TOTAL_PASS: 7")

if __name__=="__main__":main()
