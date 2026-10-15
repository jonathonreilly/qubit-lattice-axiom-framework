#!/usr/bin/env python3
"""Single selected Fraction fixture; geometry plus direct one-particle inversions."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib, datetime, traceback
ROOT=Path(__file__).resolve().parent
INPUT=json.loads((ROOT/'INPUT.json').read_text())
checks=[]
def check(name, condition, **details):
    checks.append({'name':name,'pass':bool(condition),**details})
    if not condition:
        raise AssertionError(name)
def ident(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A); R=[list(row)+eye for row,eye in zip(A,ident(n))]
    for c in range(n):
        p=next(i for i in range(c,n) if R[i][c])
        R[c],R[p]=R[p],R[c]
        fac=R[c][c]; R[c]=[x/fac for x in R[c]]
        for i in range(n):
            if i!=c and R[i][c]:
                fac=R[i][c]
                R[i]=[x-fac*y for x,y in zip(R[i],R[c])]
    return [r[n:] for r in R]
def verify_inverse(A,R):
    n=len(A)
    return all(sum(A[i][k]*R[k][j] for k in range(n) if A[i][k])==int(i==j) for i in range(n) for j in range(n))
def edge(a,b): return tuple(sorted((a,b)))
def dist(a,b): return sum(abs(x-y) for x,y in zip(a,b))
def line(waypoints):
    out=[waypoints[0]]
    for b in waypoints[1:]:
        a=out[-1]; axes=[i for i in range(3) if a[i]!=b[i]]
        assert len(axes)==1
        k=axes[0]; step=1 if b[k]>a[k] else -1
        while out[-1]!=b:
            t=list(out[-1]); t[k]+=step; out.append(tuple(t))
    return out
def path_edges(p): return {edge(a,b) for a,b in zip(p,p[1:])}
def cycle_edges(p): return path_edges(p+[p[0]])
def rectangle(x,y,q,z):
    return line([(x,y,z),(x+q,y,z),(x+q,y+q,z),(x,y+q,z),(x,y,z)])[:-1]
def qstr(x): return str(x)
def response(R,idx,a,q,phases,beta,active,p):
    # Complex coefficients are represented by pairs of exact real Fractions.
    src=[(idx[a],F(p)*q,F(0))]
    src.extend((idx[u],z[0]/be,z[1]/be) for u,z,be,j in zip(PORTS,phases,beta,range(len(PORTS))) if j in active)
    return sum((xr*yr+xi*yi)*R[u][v] for u,xr,xi in src for v,yr,yi in src)

def run():
    global PORTS
    L=INPUT['L_b']; Qm=INPUT['Q_mem']; oldn=INPUT['n_old']; M=INPUT['M']; qc=M//4
    X=max(oldn-1,Qm)+2; Y=1-L
    C={'v0':(0,1,1),'v1':(-1,0,0)}
    C.update({f'v{j}':(0,1-j,-1) for j in range(2,L+1)})
    C.update({'a0':(-1,1,0),'b0':(0,1,0),'a0p':(-1,0,1),'b0p':(0,0,1),'a1':(-1,-1,0),'b1':(0,-1,0),'a1p':(-1,0,-1),'b1p':(0,0,-1)})
    rays={'v0':((0,2,1),1),'v1':((-2,0,0),-1),'a0':((-2,1,0),-1),'b0':((1,1,0),1),'a0p':((-2,0,1),-1),'b0p':((1,0,1),1),'a1':((-2,-1,0),-1),'b1':((1,-1,0),1),'a1p':((-2,0,-1),-1),'b1p':((1,0,-1),1)}
    rays.update({f'v{j}':((1,1-j,-1),1) for j in range(2,L+1)})
    mem=[(p[0]+k*d,p[1],p[2]) for p,d in rays.values() for k in range(Qm)]
    clock=rectangle(X,Y,qc,3)
    originals=[(j,0,0) for j in range(oldn)]+list(C.values())+mem+clock
    check('original_inventory_unique',len(set(originals))==len(originals),count=len(originals))
    orig=set(originals); c=C['v0']; e=rays['v0'][0]
    v1_neighbors=[tuple(C['v1'][i]+(sgn if i==axis else 0) for i in range(3)) for axis in range(3) for sgn in (-1,1)]
    check('v1_all_six_original_neighbors',all(p in orig for p in v1_neighbors),neighbors=v1_neighbors)
    components=[]
    a1=(-1,1,1); b1=(-1,2,1); r1=(-2,1,1)
    cy1=rectangle(X,Y,qc,2)
    tail1=line([(-3,1,1),(-3,3,1),(-3,3,-2),(-3,Y-4,-2),(X,Y-4,-2),(X,Y-4,2),(X,Y,2)])
    components.append({'core':[a1,b1,(-2,2,1),r1],'r':r1,'a':a1,'b':b1,'cycle':cy1,'tail':tail1,'ports':[(x,y,2) for x,y,z in clock],'expected_m':M+X+27-Y})
    a2=(0,1,2); b2=(0,2,2); r2=(-1,1,2)
    cy2=rectangle(X,Y,qc,4)
    tail2=line([(-1,1,3),(-1,3,3),(-1,3,5),(-1,Y-3,5),(X,Y-3,5),(X,Y,5),(X,Y,4)])
    components.append({'core':[a2,b2,(-1,2,2),r2],'r':r2,'a':a2,'b':b2,'cycle':cy2,'tail':tail2,'ports':[(x,y,4) for x,y,z in clock],'expected_m':M+X+19-Y})
    a3=(1,1,1); b3=(0,3,1); r3=(2,4,3)
    p3=line([a3,(1,1,2),(1,3,2),(0,3,2),b3])
    q3=line([a3,(2,1,1),(2,1,3),r3,(0,4,3),(0,4,1),b3])
    core3=p3+list(reversed(q3))[1:-1]
    cy3=rectangle(X-1,Y-1,qc+2,3)
    tail3=line([(3,4,3),(3,Y-2,3),(X-1,Y-2,3),(X-1,Y-1,3)])
    ports3=[]
    for j,(x,y,z) in enumerate(clock):
        if j<qc: ports3.append((x,y-1,z))
        elif j<2*qc: ports3.append((x+1,y,z))
        elif j<3*qc: ports3.append((x,y+1,z))
        else: ports3.append((x-1,y,z))
    components.append({'core':core3,'r':r3,'a':a3,'b':b3,'cycle':cy3,'tail':tail3,'ports':ports3,'expected_m':M+X+27-Y})
    G=[[F(1),-F(1,960),F(1,8)],[-F(1,960),F(1),F(1,8)],[F(1,8),F(1,8),F(1)]]
    D=inv(G); den=F(892769)
    D_claim=[[F(907200)/den,F(15360)/den,-F(115320)/den],[F(15360)/den,F(907200)/den,-F(115320)/den],[-F(115320)/den,-F(115320)/den,F(921599)/den]]
    check('core_cofactors',D==D_claim and verify_inverse(G,D))
    basephase=[(F(*a),F(*b)) for a,b in INPUT['transported_phases']]
    check('constant_transported_modulus',all(a*a+b*b==1 and abs(a)<1 for a,b in basephase))
    h=F(1,4); c0=F(961,960); w=F(1,12); q=F(INPUT['q']); lam=F(INPUT['Lambda'])
    occupied=set(orig); allnew=[]; all_new_edges=set(); comp_out=[]
    for no,comp in enumerate(components):
        core=comp['core']; r,a,b=(comp[k] for k in ('r','a','b')); terminals=[r,a,b]; cidx={v:i for i,v in enumerate(terminals)}
        cycle=comp['cycle']; tail=comp['tail']; PORTS=comp['ports']
        check(f'axis{no}_core_simple',len(core)==len(set(core)) and set(terminals)<=set(core))
        check(f'axis{no}_tail_unique_attachment',len(tail)==len(set(tail)) and set(tail)&set(cycle)=={tail[-1]})
        transport=cycle+tail[:-1]; te=cycle_edges(cycle)|path_edges(tail)
        fullset=set(core)|set(transport)
        check(f'axis{no}_fresh_disjoint',not fullset&occupied and not set(core)&set(transport),count=len(fullset))
        occupied|=fullset; allnew.extend(fullset)
        check(f'axis{no}_count',len(fullset)==comp['expected_m'],expected=comp['expected_m'],actual=len(fullset))
        physical=cycle_edges(core)|te|{edge(r,tail[0])}
        check(f'axis{no}_all_aux_edges_NN',all(dist(*ed)==1 for ed in physical))
        external={edge(c,a),edge(e,b)}|{edge(x,u) for x,u in zip(clock,PORTS)}
        check(f'axis{no}_source_ports_NN',len(PORTS)==len(set(PORTS)) and set(PORTS)<=set(transport) and all(dist(*ed)==1 for ed in external))
        check(f'axis{no}_edge_count',len(physical)==len(fullset)+1,edges=len(physical))
        deg={v:sum(v in ed for ed in physical|external) for v in fullset}
        check(f'axis{no}_fresh_degree_at_most4',max(deg.values())<=4,max_degree=max(deg.values()))
        tdeg={v:sum(v in ed for ed in te) for v in transport}
        check(f'axis{no}_transport_degree_at_most3',max(tdeg.values())<=3)
        all_new_edges|=physical|external
        # Consecutive terminal arcs in cyclic order.
        terminal_positions=[i for i,v in enumerate(core) if v in terminals]; arcs=[]
        for k,start in enumerate(terminal_positions):
            end=terminal_positions[(k+1)%len(terminal_positions)]; path=[core[start]]; t=(start+1)%len(core)
            while t!=end: path.append(core[t]); t=(t+1)%len(core)
            path.append(core[end]); arcs.append(path)
        internal=[v for arc in arcs for v in arc[1:-1]]
        E=transport+internal; ix={v:i for i,v in enumerate(E)}; ne=len(E)
        T=ident(ne)
        for u,v in te|set().union(*(path_edges(arc[1:-1]) for arc in arcs)):
            T[ix[u]][ix[v]]=T[ix[v]][ix[u]]=-F(1,12)
        Ti=inv(T)
        check(f'axis{no}_internal_inverse',verify_inverse(T,Ti))
        Q=[[F(0)]*3 for _ in E]
        Q[ix[tail[0]]][0]=-w
        for arc in arcs:
            if len(arc)>2:
                i=cidx[arc[0]]; j=cidx[arc[-1]]; first=ix[arc[1]]; last=ix[arc[-2]]
                g_arc=Ti[first][last]
                check(f'axis{no}_arc_{i}_{j}_positive_path_inverse',g_arc>0)
                Q[first][i]+=1; Q[last][j]+=-D[i][j]/g_arc
        support=[[(u,Q[u][i]) for u in range(ne) if Q[u][i]] for i in range(3)]
        compensate=[[sum(qu*Ti[u][v]*qv for u,qu in support[i] for v,qv in support[j]) for j in range(3)] for i in range(3)]
        B=[[F(0)]*(ne+3) for _ in range(ne+3)]
        for i in range(ne):
            for j in range(ne): B[i][j]=T[i][j]
            for j in range(3): B[i][ne+j]=B[ne+j][i]=Q[i][j]
        for i in range(3):
            for j in range(3): B[ne+i][ne+j]=D[i][j]+compensate[i][j]
        coords=E+terminals; idx={v:i for i,v in enumerate(coords)}
        actual={edge(coords[i],coords[j]) for i in range(len(B)) for j in range(i+1,len(B)) if B[i][j]}
        check(f'axis{no}_physical_matrix_support',actual==physical and all(B[i][i]>0 for i in range(len(B))))
        Qabs=sum(abs(x) for row in Q for x in row); gap=F(11,20)/(1+F(4,3)*Qabs)**2
        check(f'axis{no}_positive_schur_certificate',gap>0)
        beta=[w*Ti[ix[u]][ix[tail[0]]] for u in PORTS]
        gamma=[Ti[ix[u]][ix[u]] for u in PORTS]
        check(f'axis{no}_clock_transfers_positive',all(be>0 for be in beta))
        rotation=INPUT['axis_rotations'][no]; phase=basephase[rotation:]+basephase[:rotation]
        f=[z[0]/120 for z in phase]
        sj=[lam*lam*(ga/be**2+c0) for ga,be in zip(gamma,beta)]
        d=(q*q+lam*lam)/240; s0=c0*q*q
        inverses={}
        maxdef=F(0)
        for s in (1,-1):
            Bs=[row[:] for row in B]; Bs[idx[b]][idx[b]]+=s*h
            Ri=inv(Bs); inverses[s]=Ri
            check(f'axis{no}_sign{s}_direct_inverse_product',verify_inverse(Bs,Ri))
            ds=[row[:] for row in D]; ds[2][2]+=s*h
            check(f'axis{no}_sign{s}_core_green',all(Ri[idx[v]][idx[t]]==inv(ds)[i][j] for i,v in enumerate(terminals) for j,t in enumerate(terminals)))
            check(f'axis{no}_sign{s}_cross_odd_only',Ri[idx[r]][idx[a]]==-F(s,240) and Ri[idx[a]][idx[a]]==c0-F(s,240))
            for j,u in enumerate(PORTS):
                check(f'axis{no}_sign{s}_port{j}_green',Ri[idx[u]][idx[a]]==-F(s,240)*beta[j] and Ri[idx[u]][idx[u]]==gamma[j]+beta[j]**2*(c0-F(s,240)))
                for p in (-1,1):
                    value=response(Ri,idx,a,q,phase,beta,{j},p)
                    expected=s0+sj[j]-d*s-f[j]*p*s
                    maxdef=max(maxdef,abs(value-expected))
                    check(f'axis{no}_sign{s}_port{j}_pc{p}_response',value==expected)
        # Fixed selected mutations, not fitted after seeing results.
        realphase=[(z[0],F(0)) for z in phase]
        odd=[]
        for j in range(M):
            vplus=sum(response(inverses[1],idx,a,q,realphase,beta,{j},p) for p in (-1,1))/2
            vminus=sum(response(inverses[-1],idx,a,q,realphase,beta,{j},p) for p in (-1,1))/2
            odd.append((vplus-vminus)/2)
        check(f'axis{no}_real_source_mutation_unequal_odd_diagonals',len(set(odd))>1 and odd==[-(q*q+z[0]**2)/240 for z in phase],odd=[str(x) for x in odd])
        v=response(inverses[1],idx,a,q,phase,beta,{0},1)
        omission=(s0+sj[0])-v-f[0]
        partial=(s0+sj[0]-lam*lam/240)-v-f[0]
        check(f'axis{no}_omit_Pe_counterterm_detected',omission==d and omission!=0,residual=str(omission))
        check(f'axis{no}_omit_Pc_square_counterterm_detected',partial==q*q/240 and partial!=0,residual=str(partial))
        vacuum_defect=s0-d-response(inverses[1],idx,a,q,phase,beta,set(),1)
        check(f'axis{no}_clock_vacuum_outside_domain',vacuum_defect==-lam*lam/240,residual=str(vacuum_defect))
        two_defect=s0+sj[0]+sj[1]-d-response(inverses[1],idx,a,q,phase,beta,{0,1},1)-f[0]-f[1]
        check(f'axis{no}_two_clock_input_outside_domain',two_defect!=0,residual=str(two_defect))
        if no==0:
            theta=w*w*Ti[ix[tail[0]]][ix[tail[0]]]
            mutant=[row[:] for row in B]; mutant[idx[b]][idx[b]]+=h; mutant[idx[r]][idx[r]]-=theta
            mutant_inv=inv(mutant)
            check('root_compensation_mutant_inverse_product',verify_inverse(mutant,mutant_inv))
            check('missing_root_compensation_changes_cross',mutant_inv[idx[r]][idx[a]]!=-F(1,240),actual=str(mutant_inv[idx[r]][idx[a]]),desired='-1/240')
        comp_out.append({'axis':no,'m':len(B),'edges':len(physical),'Qabs':str(Qabs),'certified_full_sector_gap':str(gap),'Tr_B':str(sum(B[i][i] for i in range(len(B)))),'beta':[str(x) for x in beta],'gamma':[str(x) for x in gamma],'f':[str(x) for x in f],'Pe_counterterm_d':str(d),'onsite_counterterms_sj':[str(x) for x in sj],'max_exact_response_defect':str(maxdef),'coordinates':coords,'auxiliary_edges':sorted(physical),'source_detuning_edges':sorted(external)})
    check('all_three_fresh_total',len(allnew)==121 and len(set(allnew))==121,total=len(allnew))
    c_ports={b if a==c else a for a,b in all_new_edges if c in (a,b)}
    e_ports={b if a==e else a for a,b in all_new_edges if e in (a,b)}
    fresh_c_neighbors={tuple(c[i]+(sgn if i==axis else 0) for i in range(3)) for axis in range(3) for sgn in (-1,1)}-orig
    check('c_uses_exact_three_fresh_neighbors',c_ports==fresh_c_neighbors and len(c_ports)==3,ports=sorted(c_ports))
    check('e_uses_three_fresh_neighbors',len(e_ports)==3 and not e_ports&orig,ports=sorted(e_ports))
    clock_degrees=[]
    for x in clock:
        count=sum(x in ed for ed in all_new_edges)+2; clock_degrees.append(count)
    check('clock_total_used_degree5',all(d==5 for d in clock_degrees))
    return {'components':comp_out,'original_count':len(orig),'original_coordinates':sorted(orig),'fresh_count':len(allnew),'mathematical_execution_count':1,'scope':'Exact selected geometry and one-particle fixture only; full-sector dynamics are analytic, unreviewed.'}

if __name__=='__main__':
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result={'started_utc':started,'input_sha256':hashlib.sha256((ROOT/'INPUT.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    try:
        result.update(run()); result['status']='PASS_SELECTED_FIXTURE'
    except BaseException:
        result['status']='FAILED_OR_EXCEPTION'; result['exception']=traceback.format_exc()
    result['checks']=checks; result['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (ROOT/'EXACT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':len(checks),'passed':sum(c['pass'] for c in checks),'exception':result.get('exception'),'result':'EXACT_RESULT.json'},indent=2))
    raise SystemExit(0 if result['status']=='PASS_SELECTED_FIXTURE' else 1)
