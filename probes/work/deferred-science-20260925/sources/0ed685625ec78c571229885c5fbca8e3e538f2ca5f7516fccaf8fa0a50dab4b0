#!/usr/bin/env python3
"""Direct original-mark word effects and a separate compact-rotor error control."""
from collections import defaultdict,Counter
from itertools import product
from pathlib import Path
import hashlib,json,time
import numpy as np
from scipy.linalg import eigh


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


def main():
    start=time.monotonic()
    result={'primitive_graphs':[marked_words(p) for p in ((2,2,2),(6,6),(6,6,6))],
            'separate_rotor_controls':[rotor_error_control(g) for g in (.3,.2,.14,.1,.07)],
            'grid_repeat':rotor_error_control(.1,512),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result['elapsed_seconds']=time.monotonic()-start
    Path(__file__).with_name('READOUT_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
