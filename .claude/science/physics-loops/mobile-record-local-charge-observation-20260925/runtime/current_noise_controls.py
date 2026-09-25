"""Personal exact original-instrument current/covariance controls.
Fresh standard-library implementation. No earlier program imports.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib,json,time

def torus(L):
    xyz=list(product(range(L),repeat=3));ix={p:i for i,p in enumerate(xyz)}
    A={i for i,p in enumerate(xyz) if sum(p)%2==0};edges=[]
    for a in sorted(A):
        near=set()
        for j in range(3):
            for sign in (-1,1):
                p=list(xyz[a]);p[j]=(p[j]+sign)%L;near.add(ix[tuple(p)])
        edges.extend((a,b) for b in sorted(near))
    return xyz,A,edges

def cases():
    for L in (2,4,6):
        xyz,A,edges=torus(L);yield 'torus'+str(L),xyz,A,edges,L
    yield 'path7',[(i,0,0) for i in range(7)],{0,2,4,6},[(a,b) for a in (0,2,4,6) for b in (a-1,a+1) if 0<=b<7],None
    yield 'K2_3',[(i,0,0) for i in range(5)],{0,1},[(a,b) for a in (0,1) for b in (2,3,4)],None

def main():
    started=time.perf_counter();summaries=[];primitive=[];total_bilinear=0
    for name,xyz,A,edges,L in cases():
        nv=len(xyz);near={a:[] for a in A}
        for e,(a,b) in enumerate(edges):assert a in A and b not in A;near[a].append((b,e))
        degree={a:len(near[a]) for a in A}
        tests=[('constant',[1]*nv),('site0',[int(i==0) for i in range(nv)]),
               ('coordinate',[x-2*y+3*z for x,y,z in xyz]),
               ('staggered',[1 if i in A else -1 for i in range(nv)])]
        if L==4:
            tests.extend([('Fourier_re',[(1,0,-1,0)[x] for x,y,z in xyz]),
                          ('Fourier_im',[(0,-1,0,1)[x] for x,y,z in xyz])])
        elif L==6:
            tests.extend([('Fourier_re',[(-1)**x for x,y,z in xyz]),('Fourier_im',[0]*nv)])
        else:
            tests.extend([('index_mod3',[i%3 for i in range(nv)]),('index_mod5',[i%5 for i in range(nv)])])
        nt=len(tests);mean=[0]*nt;cov=[[0]*nt for _ in range(nt)]
        field_drift=[0]*len(edges);charge_drift=[0]*nv;mark_rows=[];raw_count=0
        for a in sorted(A):
            for b,eb in near[a]:
                branches=[]
                for sigma in (-1,1):
                    for c,ec in near[a]:
                        if c==b:continue
                        # F first transports the original plus a->c; j then
                        # fills empty a,b with sigma,-sigma. Both steps obey
                        # hard-core occupancy. Electric shifts use A->B.
                        q=[int(x in A) for x in range(nv)];E=[0]*len(edges)
                        assert q[a]==1 and q[c]==q[b]==0
                        q[a]=0;q[c]=1;E[ec]-=1
                        assert q[a]==q[b]==0
                        q[a]=sigma;q[b]=-sigma;E[eb]+=sigma
                        delta=[q[x]-int(x in A) for x in range(nv)]
                        div=[0]*nv
                        for e,(u,v) in enumerate(edges):div[u]+=E[e];div[v]-=E[e]
                        assert div==delta and sum(delta)==0
                        assert sum(abs(v) for v in q)==len(A)+2 and sum(q)==len(A)
                        values=[sum(f[x]*delta[x] for x in range(nv)) for label,f in tests]
                        assert values==[f[c]-f[a]+sigma*(f[a]-f[b]) for label,f in tests]
                        for i in range(nt):
                            mean[i]+=values[i]
                            for j in range(nt):cov[i][j]+=values[i]*values[j]
                        field_drift=[x+y for x,y in zip(field_drift,E)]
                        charge_drift=[x+y for x,y in zip(charge_drift,delta)]
                        branches.append(tuple(q));raw_count+=1
                        primitive.append(dict(graph=name,a=a,b=b,c=c,sigma=sigma,
                            delta_q=[[i,v] for i,v in enumerate(delta) if v],
                            delta_E=[[i,v] for i,v in enumerate(E) if v],charge_tests=values))
                assert len(branches)==len(set(branches))==2*(degree[a]-1)
                # Orthogonal matter words make all charge-diagonal cross
                # terms vanish for the unnormalized coherent edge mark.
                mark_rows.append([a,b,len(branches),degree[a]-1,2*(degree[a]-1)])
        expected_mean=[sum(2*(degree[a]-1)*(f[b]-f[a]) for a,b in edges) for label,f in tests]
        expected_cov=[[sum(4*(degree[a]-1)*(f[b]-f[a])*(g[b]-g[a]) for a,b in edges)
                       for name_g,g in tests] for name_f,f in tests]
        assert mean==expected_mean and cov==expected_cov
        assert all(v==0 for v in cov[0]) and mean[0]==0
        assert all(cov[i][i]>=0 and all(cov[i][j]==cov[j][i] for j in range(nt)) for i in range(nt))
        current=[-v for v in field_drift]
        assert current==[2*(degree[a]-1) for a,b in edges]
        divJ=[0]*nv
        for (a,b),j in zip(edges,current):divJ[a]+=j;divJ[b]-=j
        assert charge_drift==[-v for v in divJ]
        assert mean==[sum((f[b]-f[a])*j for (a,b),j in zip(edges,current)) for label,f in tests]
        rate=2*sum(z*(z-1) for z in degree.values());assert raw_count==rate
        fourier=None
        if L in (4,6):
            # Complex covariance by exact real/imaginary polarization.
            sdot=cov[4][4]+cov[5][5]
            cross_imag=cov[4][5]-cov[5][4];assert cross_imag==0
            cos_sum_defect=1 if L==4 else 2
            assert sdot==80*len(A)*cos_sum_defect
            fourier=dict(allowed_k_in_pi=['1/2' if L==4 else '1','0','0'],
                full_initial_second_moment_slope_in_kappa=sdot,
                site_normalized_slope_in_kappa=sdot//nv,
                defect_sum=cos_sum_defect,imaginary_self_covariance=cross_imag)
        total_bilinear+=nt*nt
        summaries.append(dict(graph=name,vertices=nv,A=len(A),edges=edges,A_degrees=[[a,degree[a]] for a in sorted(A)],
            test_names=[label for label,f in tests],initial_mean_slope_in_kappa=mean,
            initial_covariance_slope_in_kappa=cov,formation_current_in_kappa=current,
            initial_charge_drift_in_kappa=charge_drift,mark_squared_norms=mark_rows,
            total_first_event_rate_in_kappa=rate,primitive_rows=raw_count,Fourier=fourier))
    print(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope='Exact initial charge means, covariance and formation-current coefficients from the original primitive births; no finite-lag or measured noise spectrum.',
        graph_summaries=summaries,primitive_rows=primitive,primitive_count=len(primitive),
        real_polarized_covariance_entries=total_bilinear,all_assertions_passed=True,
        elapsed_seconds=time.perf_counter()-started),separators=(',',':')))

if __name__=='__main__':main()
