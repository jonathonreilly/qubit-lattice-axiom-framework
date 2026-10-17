"""Exact author corroboration only. No inherited scientific program is imported."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from collections import deque
import argparse
import json
import sys
import time

ap=argparse.ArgumentParser()
ap.add_argument("--packet-root",required=True)
ap.add_argument("--prelaunch",required=True)
args=ap.parse_args()
D=Path(args.packet_root).resolve()
start=time.monotonic()
records=[]
def record(name,value): records.append({"test":name,"result":value})
def demand(name,condition,detail):
    record(name,{"satisfied":bool(condition),"detail":detail})
    if not condition: raise AssertionError(name)
def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,tuple): return [encode(v) for v in x]
    if isinstance(x,list): return [encode(v) for v in x]
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    return x

# Rational complex arithmetic, with no floating acceptance tests.
def z(a=0,b=0): return (F(a),F(b))
def za(x,y): return (x[0]+y[0],x[1]+y[1])
def zn(x): return (-x[0],-x[1])
def zs(x,y): return za(x,zn(y))
def zm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zc(x): return (x[0],-x[1])
def za2(x): return x[0]*x[0]+x[1]*x[1]
def zero(m,n=None): return [[z() for _ in range(n or m)] for _ in range(m)]
def eye(m):
    a=zero(m)
    for j in range(m): a[j][j]=z(1)
    return a
def add(a,b): return [[za(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a): return [[zn(x) for x in r] for r in a]
def sub(a,b): return add(a,neg(b))
def scale(a,q): return [[zm(x,q) for x in r] for r in a]
def mul(a,b):
    return [[sumz(zm(a[i][k],b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sumz(seq):
    ans=z()
    for x in seq: ans=za(ans,x)
    return ans
def adj(a): return [[zc(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]
def conj(a): return [[zc(x) for x in r] for r in a]
def kron(a,b):
    return [[zm(a[i//len(b)][j//len(b[0])],b[i%len(b)][j%len(b[0])]) for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]

ok=False
try:
    manifest=json.loads((D/"SOURCE_MANIFEST.json").read_text())
    hashes=[]
    for entry in manifest["entries"]:
        digest=sha256((D/entry["snapshot"]).read_bytes()).hexdigest()
        demand("snapshot:"+entry["snapshot"],digest==entry["sha256"],digest)
        hashes.append({"path":entry["snapshot"],"sha256":digest})
    pre=json.loads(Path(args.prelaunch).read_text())
    pre_bound=[]
    for e in pre["bindings"]:
        p=Path(e["path"])
        if not p.is_absolute(): p=D/p
        digest=sha256(p.read_bytes()).hexdigest()
        demand("prelaunch:"+e["label"],digest==e["identity"]["sha256"],digest)
        pre_bound.append(e["label"])
    inp=json.loads((D/"SCALAR_INPUTS.json").read_text())
    p={k:F(v) for k,v in inp.items()}
    q=p["q0"]; J=p["J"]; kap=p["kappa_max"]; nu=p["nu"]
    ck=(q*q-1)/(q*q+1); sk=2*q/(q*q+1)
    c=ck*ck-sk*sk; s=2*ck*sk; d=1+c+s; E0=2*J*(1-ck)
    demand("central_phase_unit_circle",c*c+s*s==1,{"cos_phi":c,"sin_phi":s})
    demand("central_phase_and_positive_onsite",c>0 and s>0 and d<3 and E0>3*kap,{"d":d,"E0_minus_3kappa_max":E0-3*kap})

    jf=[[z(),z(-1)],[z(1),z()]]
    vp=[[z(1)],[z(0,-1)]]; vm=conj(vp)
    demand("chiral_flag_eigenvalues",mul(jf,vp)==scale(vp,z(0,1)) and mul(jf,vm)==scale(vm,z(0,-1)),{"J":jf,"v_plus_unnormalized":vp,"v_minus_unnormalized":vm})
    Pplus=scale(sub(eye(2),scale(jf,z(0,1))),z(F(1,2)))
    Pminus=sub(eye(2),Pplus)
    e0flag=[[z(1)],[z()]]
    wp=mul(adj(mul(Pplus,e0flag)),mul(Pplus,e0flag))[0][0]
    wm=mul(adj(mul(Pminus,e0flag)),mul(Pminus,e0flag))[0][0]
    demand("product_flag_half_weights",wp==z(F(1,2)) and wm==z(F(1,2)),{"plus":wp,"minus":wm})

    # Local complex core in order e,c_L,c_(L+2), and its six-dimensional lift.
    H=zero(3); H[0][0]=z(E0)
    H[1][0]=H[0][1]=z(kap)
    H[2][0]=z(-kap*c,-kap*s); H[0][2]=zc(H[2][0])
    A=[[z(x[0]) for x in r] for r in H]
    B=[[z(x[1]) for x in r] for r in H]
    HR=add(kron(A,eye(2)),kron(B,jf))
    Tp=kron(eye(3),vp); Tm=kron(eye(3),vm)
    demand("six_by_six_sector_intertwining",HR==adj(HR) and mul(HR,Tp)==mul(Tp,H) and mul(HR,Tm)==mul(Tm,conj(H)),{"H":H,"HR":HR})
    # In the lift order e0,e1,cL0,cL1,cL20,cL21.
    expected={(2,0):kap,(3,1):kap,(4,0):-kap*c,(5,1):-kap*c,(4,1):kap*s,(5,0):-kap*s}
    demand("six_real_edge_signs",all(HR[i][j]==z(h) for (i,j),h in expected.items()),{str(edge):h for edge,h in expected.items()})
    wrong=[r[:] for r in HR]
    wrong[4][1]=wrong[1][4]=z(-kap*s)
    defect=sub(mul(wrong,Tp),mul(Tp,H))
    demand("wrong_cross_sign_is_detected",any(x!=z() for r in defect for x in r),{"nonzero_defect_entries":[[i,j,x] for i,r in enumerate(defect) for j,x in enumerate(r) if x!=z()]})

    for sign in (-1,1):
        Q=zero(4); Q[1][1]=Q[2][2]=z(1); Q[3][3]=z(2); Q[1][2]=Q[2][1]=z(sign)
        demand("positive_cell_polynomial_sign_"+str(sign),mul(Q,Q)==scale(Q,z(2)) and Q==adj(Q),{"Q":Q,"spectrum_by_polynomial_and_trace":[0,0,2,2]})
    coeff=[F(0)]*6
    for (i,j),h in expected.items(): coeff[i]+=abs(h); coeff[j]+=abs(h)
    coeff[0]+=E0-kap*d; coeff[1]+=E0-kap*d
    coeff[2]-=kap; coeff[3]-=kap
    coeff[4]-=kap*(c+s); coeff[5]-=kap*(c+s)
    scalar=2*kap*d
    demand("full_occupation_identity",coeff==[E0,E0,F(0),F(0),F(0),F(0)],{"remaining_number_coefficients":coeff,"contact_vacancy_scalar":scalar,"complete_scalar":2*nu+scalar,"difference_from_original_physical_scalar":nu+2*kap*(c+s)})
    demand("seed_second_moment",kap*kap+(kap*c)**2+(kap*s)**2==2*kap*kap,{"variance_addition":2*kap*kap})

    X=[[z(),z(1)],[z(1),z()]]; Z=[[z(1),z()],[z(),z(-1)]]
    K=add(scale(eye(4),z(2)),kron(Z,Z)); P=kron(X,X)
    Wgate=add(scale(eye(4),z(F(9,25),F(12,25))),scale(P,z(F(-16,25),F(12,25))))
    demand("literal_target_unitary_and_old_commutation",mul(adj(Wgate),Wgate)==eye(4) and mul(K,Wgate)==mul(Wgate,K),{"K":K,"W":Wgate})
    uplus=[[z()],[z(1)],[z(1)],[z()]]; uminus=[[z()],[z(1)],[z(-1)],[z()]]
    omega=z(F(-7,25),F(24,25))
    demand("same_energy_real_old_falsifier",mul(K,uplus)==uplus and mul(K,uminus)==uminus and mul(Wgate,uplus)==scale(uplus,omega) and mul(Wgate,uminus)==uminus,{"u_plus_unnormalized":uplus,"u_minus_unnormalized":uminus,"omega_plus":omega})
    separation_squared=za2(zs(omega,z(1)))/2
    lower_squared=separation_squared/4
    demand("common_output_separation",separation_squared==F(32,25) and lower_squared==F(8,25) and lower_squared>F(9,16)**2,{"environment_separation_squared":separation_squared,"minimax_lower_bound_squared":lower_squared})

    def coord(rail,n):
        if rail==0:
            if n==0:return (0,1,1)
            if n==1:return (1,1,1)
            if n==2:return (1,1,2)
            if n==3:return (1,1,3)
            if 4<=n<=10:return (n-2,1,3)
            if n==11:return (8,1,2)
            if n==12:return (8,1,1)
            if n==13:return (9,1,1)
            if n==14:return (9,2,1)
            return (n-5,2,1)
        if n<=9:return (n,1,-1)
        if n==10:return (9,2,-1)
        if n==11:return (9,3,-1)
        if n==12:return (9,3,0)
        if n==13:return (8,3,0)
        if n==14:return (8,3,1)
        return (8,n-11,1)
    vertices={"old1":(0,0,0),"old2":(1,0,0),"A":(0,1,0),"B":(1,1,0),"e0":(8,2,1),"e1":(9,3,1)}
    for rail in range(2):
        for n in range(20):vertices[f"c{n},{rail}"]=coord(rail,n)
    edges=[("old1","old2"),("old1","A"),("old2","B"),("A","B")]
    head_edges=[]
    for rail in range(2):
        edges.extend([("A",f"c0,{rail}"),("B",f"c1,{rail}")])
        head_edges.extend([(f"c{n},{rail}",f"c{n+1},{rail}") for n in range(19)])
        head_edges.append((f"e{rail}",f"c12,{rail}"))
        for target in range(2):head_edges.append((f"e{rail}",f"c14,{target}"))
    edges+=head_edges
    demand("cubic_NN_embedding",len(vertices)==len(set(vertices.values())) and all(sum(abs(x-y) for x,y in zip(vertices[a],vertices[b]))==1 for a,b in edges),{"vertices":vertices,"installed_support_edges":edges,"vertex_count":len(vertices),"edge_count":len(edges)})
    graph={name:set() for name in vertices}
    for a,b in head_edges:graph[a].add(b);graph[b].add(a)
    dist={"e0":0}; todo=deque(["e0"])
    while todo:
        a=todo.popleft()
        for b in graph[a]:
            if b not in dist:dist[b]=dist[a]+1;todo.append(b)
    demand("first_omitted_distance_prefix_M19",dist["c19,0"]==6 and dist["c19,1"]==6,{"retained_M":19,"distance_to_first_omitted_each_rail":[dist["c19,0"],dist["c19,1"]],"general_formula":"M-13, proved by no attachment beyond index14"})
    demand("infinite_tail_symbolic_conditions",coord(0,15)==(10,2,1) and coord(1,15)==(8,4,1),{"rail0_tail":"(n-5,2,1), n>=15","rail1_tail":"(8,n-11,1), n>=15","proof":"Each step has length1; tails have respectively x>=10,y=2 and x=8,y>=4, and no core site has those tail coordinates."})

    loads={"old1_added":2*p["gA"],"old2_added":2*p["gB"],"old_edge_separate":F(3),
      "A":p["DeltaA"]+2*p["hAB"]+p["u"]+2*p["gA"]+4*p["lambdaA"],
      "B":p["DeltaB"]+2*p["hAB"]+p["u"]+2*p["gB"]+4*p["lambdaB"],
      "each_c0":3*J+2*p["lambdaA"]+p["mu0"],"each_c1":4*J+2*p["lambdaB"]+nu,
      "ordinary_clock":4*J,"each_c12":4*J+3*kap,"each_c14":4*J+3*kap*(c+s),"each_emitter":E0+kap*d,"each_far_end":3*J}
    demand("exact_source_loads",loads["A"]==F("27.936224853155858") and loads["B"]==F("22.228906875353305"),loads)
    v=p["v"]; C=p["T_scaled"]; sig=p["sigma"]
    reverse=p["seed_error"]+F(1001)/(v*C)+F(5,2)*sig+F(1,100)/(v*C)+F(5,2)*sig+F(3,2)/(v*C)
    demand("reverse_branch_complete_budget",reverse==F("0.0431054") and reverse<F("0.044"),{"seed_plus_incoming_plus_normalization_plus_localized":reverse})
    error_squared=(p["forward_error"]**2+F("0.044")**2)/2
    demand("orthogonal_branch_error",error_squared==F(61,62500) and error_squared<F(8,250)**2,{"branch_error_squared":error_squared})
    lower_coarse=F(9,16)-F(8,250)
    demand("strict_full_output_falsifier",lower_coarse>F("0.53") and lower_coarse-F("0.001")>F("0.52"),{"infinite_strict_lower_bound":lower_coarse,"finite_strict_lower_bound":lower_coarse-F("0.001")})
    Tmin=C/(kap*kap); margin=F(22,5)*Tmin-22
    finite=F(32,5)*F(3,8)**9
    demand("finite_buffer_and_error",margin>0 and finite==F(19683,20971520) and finite<F("0.001"),{"minimum_T":Tmin,"minimum_margin":margin,"finite_error_ceiling":finite,"qubits":"2 ceil(50T)+6"})
    record("actual_dimensions",{"maximum_matrix_dimension":6,"graph_vertices":len(vertices),"scientific_parameter_samples":0,"dynamics_steps":0,"quadrature_nodes":0})
    ok=True
finally:
    print(json.dumps(encode({"status":"completed" if ok else "failed","author_corroboration_only":True,"source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),"prelaunch_sha256":sha256(Path(args.prelaunch).read_bytes()).hexdigest(),"program_wall_seconds":time.monotonic()-start,"records":records}),indent=2),flush=True)
