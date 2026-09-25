"""Exact rational full original-birth charge controls; root personal, no fitting."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib, json, time

def geometry(L):
    vertices=list(product(range(L),repeat=3)); index={v:i for i,v in enumerate(vertices)}
    A=[i for i,v in enumerate(vertices) if sum(v)%2==0]
    edges=[]
    for a in A:
        near=set()
        for axis in range(3):
            for sign in (-1,1):
                v=list(vertices[a]); v[axis]=(v[axis]+sign)%L; near.add(index[tuple(v)])
        edges.extend((a,b) for b in sorted(near))
    adjacent={a:[] for a in A}
    for e,(a,b) in enumerate(edges): adjacent[a].append((b,e))
    return vertices,A,edges,adjacent

def gauss(q,E,A,edges):
    div=[0]*len(q)
    for value,(a,b) in zip(E,edges): div[a]+=value; div[b]-=value
    assert div==[value-int(i in A) for i,value in enumerate(q)]

def birth(q,E,a,b,c,eb,ec,sigma,A,edges):
    out=list(q); field=list(E)
    assert out[a]==1 and out[c]==0
    out[a]=0; out[c]=1; field[ec]-=1
    gauss(out,field,A,edges)
    assert out[a]==out[b]==0
    out[a]=sigma; out[b]=-sigma; field[eb]+=sigma
    gauss(out,field,A,edges)
    return tuple(out),tuple(field)

def moments(values):
    mean=F(sum(values),len(values)); second=F(sum(v*v for v in values),len(values))
    return mean,second-mean*mean

def short_link(x,y,L):
    d=[]
    for a,b in zip(x,y):
        r=(b-a)%L
        d.append(-1 if r==L-1 and L>2 else r)
    assert sum(abs(x) for x in d)==1
    return d

def main():
    started=time.perf_counter(); rows=[]; primitive_rows=[]; totals=Counter(); summaries=[]
    for L in (2,4,6):
        vertices,A,edges,adjacent=geometry(L); q=[int(i in A) for i in range(len(vertices))]
        E=[0]*len(edges); z=len(adjacent[A[0]])
        tests=[('constant',[1]*len(q)),('x',[v[0] for v in vertices]),
               ('polynomial',[v[0]**2+2*v[1]-v[2] for v in vertices])]
        # Gaussian integer Fourier values, without floating trigonometry.
        roots=[(1,0),(0,-1),(-1,0),(0,1)]
        phase=[roots[(sum(v) if L==4 else 2*v[0])%4] for v in vertices]
        tests += [('Fourier_real',[p[0] for p in phase]),('Fourier_imag',[p[1] for p in phase])]
        seen={}; cubic_tensors=Counter()
        for a in A:
            for b,eb in adjacent[a]:
                outputs=[]; allowed=[(c,ec) for c,ec in adjacent[a] if c!=b]
                d=short_link(vertices[a],vertices[b],L)
                for sigma in (-1,1):
                    for c,ec in allowed:
                        out,field=birth(q,E,a,b,c,eb,ec,sigma,A,edges)
                        assert (out[a]-1)+out[b]==-1
                        assert sum(out[v] for v in range(len(q)) if v in [x for x,_ in allowed])==1
                        assert sum(out)==sum(q) and sum(abs(v) for v in out)==sum(q)+2
                        outputs.append((sigma,c,out,field)); totals['primitive_paths']+=1
                        primitive_rows.append([L,a,b,c,sigma,[[i,v-q[i]] for i,v in enumerate(out) if v!=q[i]],[[i,v] for i,v in enumerate(field) if v]])
                        if sigma==-1:
                            reverse=birth(q,E,a,c,b,ec,eb,sigma,A,edges)
                            assert reverse==(out,field); totals['negative_mark_ambiguity_controls']+=1
                        if L>=4:
                            r=short_link(vertices[a],vertices[c],L)
                            dipole=[r[j]-sigma*d[j] for j in range(3)]
                            for i in range(3):
                                for j in range(3): cubic_tensors[(i,j)]+=dipole[i]*dipole[j]
                assert len({(out,field) for _,_,out,field in outputs})==2*(z-1)
                # Matter words already distinguish all paths, so the same
                # orthogonality holds for arbitrary normal field input.
                assert len({out for _,_,out,_ in outputs})==2*(z-1)
                totals['edge_marks']+=1
                for name,f in tests:
                    values=[sum(f[i]*(v-q[i]) for i,v in enumerate(out)) for _,_,out,_ in outputs]
                    outgoing=[f[c] for c,_ in allowed]; mu_plus,var_plus=moments(outgoing)
                    mu,var=moments(values); dip=f[a]-f[b]
                    assert mu==mu_plus-f[a] and var==var_plus+dip*dip
                    negative=[f[a]*(out[a]-1)+f[b]*out[b] for _,_,out,_ in outputs]
                    assert moments(negative)==(-F(f[a]),F(dip*dip))
                    for sigma in (-1,1):
                        selected=[sum(f[i]*(v-q[i]) for i,v in enumerate(out)) for s,_,out,_ in outputs if s==sigma]
                        assert moments(selected)==(mu_plus-f[a]+sigma*dip,var_plus)
                    assert sum(s*f[c] for s,c,_,_ in outputs)==0
                    # Exact characteristic law as the full rational-valued
                    # charge distribution, without numerical exponentials.
                    law=Counter(values); expected=Counter(f[c]-f[a]+s*dip for c,_ in allowed for s in (-1,1))
                    assert law==expected
                    rows.append([L,a,b,name,str(mu),str(var),str(mu_plus),str(var_plus),dip,sorted(law.items())])
                    totals['charge_moment_controls']+=1
                real=tests[-2][1]; imag=tests[-1][1]
                S=F(sum(sum(f[i]*(v-q[i]) for i,v in enumerate(out))**2 for _,_,out,_ in outputs for f in (real,imag)),len(outputs))
                direct=F(sum((real[c]-real[a])**2+(imag[c]-imag[a])**2 for c,_ in allowed),z-1)+(real[a]-real[b])**2+(imag[a]-imag[b])**2
                assert S==direct
                if L==4:
                    # Allowed k=(pi/2,pi/2,pi/2): all three cosines vanish.
                    assert S==4
                if L==6:
                    # Allowed k=(pi,0,0): sum cos=1, cos(k.d)=1-2d_x^2.
                    assert S==4-F(4,5)-F(8,5)*(1-2*d[0]**2)
                totals['complex_structure_factor_controls']+=1
                seen[(a,b)]=S
        if L>=4:
            denominator=2*len(edges)*(z-1)
            tensor=[[str(F(cubic_tensors[(i,j)],denominator)) for j in range(3)] for i in range(3)]
            assert tensor==[['2/3' if i==j else '0' for j in range(3)] for i in range(3)]
            S_average=sum(seen.values(),F(0))/len(edges)
            assert S_average==(4 if L==4 else F(8,3))
        else: tensor=None; S_average=sum(seen.values(),F(0))/len(edges)
        summaries.append({'L':L,'n_A':len(A),'degree':z,'edge_marks':len(edges),
            'resolved_rate_per_edge_sign_in_kappa':z-1,'coherent_rate_per_edge_in_kappa':2*(z-1),
            'total_first_birth_rate_in_kappa':2*len(edges)*(z-1),
            'orientation_averaged_dipole_second_moment':tensor,'selected_wavevector_structure_factor':str(S_average)})
    result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Original conditional rotor birth, exact charge statistics and Gauss controls; no finite-time particle transport, physical spin, cross section, units or empirical confirmation.',
      'summaries':summaries,'counts':dict(totals),
      'row_columns':['L','a','b','test','mean','variance','outgoing_mean','outgoing_variance','internal_dipole','charge_distribution_multiplicities'],
      'rows':rows,'primitive_columns':['L','a','b','c','sigma','delta_q_sparse','delta_E_sparse'],
      'primitive_rows':primitive_rows,'all_assertions_passed':True,'elapsed_seconds':time.perf_counter()-started}
    print(json.dumps(result,indent=2,allow_nan=False))

if __name__=='__main__': main()
