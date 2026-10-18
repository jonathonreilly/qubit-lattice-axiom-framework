#!/usr/bin/env python3
"""B20 part 1: why the X-type nodes (pi/2)e_i of the S^2 word S2.H20.S2.L202 are isotropic at the k* speed,
and the full node census of that word at E = -pi with chiralities from velocity determinants.
Exact identities checked at random momenta (they are finite Fourier-polynomial identities):
  (a) S^2(k) = diag(exp(2i k.f_c)) (gauge signs square to 1).
  (b) S^2(k + (pi/2)e_i) = S^2(k) Z_i, Z_i = diag((-1)^{f_c,i}) (corner-plane signs), and
      S^2(k + (pi/4)(1,1,1)) = S^2(k) Y, Y = diag((-1)^{f_c.(1,1,1)/2}).
  (c) For W = S^2 A S^2 B: Z_i W(k) Z_i = W(k + (pi/2)e_i) whenever [B, Z_i] = 0, and
      Y W(k) Y = -W(k + (pi/4)(1,1,1)) whenever {B, Y} = 0.
  (d) L202 is block diagonal in the three corner planes (it is the in-plane square hopping), so it commutes
      with every Z_i and anticommutes with Y.
Consequences: (pi/2)e_i is the image of the O-fixed copy k = 0 under an exact unitary taste whose linear part
is the identity, so the node there has the identical cone metric M M^T and chirality (M itself is fixed only up to the SU(2) basis choice in the doublet); its little group in the
enlarged group contains t R t^{-1} for every PSG rotation R, i.e. a copy of O.  Prints PASS/FAIL, TOTAL."""
import time
exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
t0=time.time(); PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
rng=np.random.default_rng(20); KS=rng.uniform(-np.pi,np.pi,(5,3))
S2=lambda k: Wk(['S2'],k)
Z=[np.diag((-1.0)**F[:,i]) for i in range(3)]; Y=np.diag((-1.0)**(F.sum(1)/2))
check("(a) S^2(k) = diag(exp(2i k.f_c)) and equals the library S(k)^2",
      all(np.allclose(S2(k),np.diag(np.exp(2j*F@k))) and np.allclose(S2(k),SK(k)@SK(k)) for k in KS))
check("(b) S^2(k+(pi/2)e_i) = S^2(k) Z_i (i=x,y,z) and S^2(k+(pi/4)(1,1,1)) = S^2(k) Y",
      all(np.allclose(S2(k+np.pi/2*EX[i]),S2(k)@Z[i]) for k in KS for i in range(3)) and all(np.allclose(S2(k+np.pi/4*np.ones(3)),S2(k)@Y) for k in KS))
A=onH(2,0); B=onL(2,0,2); w=['S2',A,'S2',B]
check("(d) L202 commutes with Z_x, Z_y, Z_z (block diagonal in the corner planes) and anticommutes with Y; H20 does neither",
      all(np.allclose(Z[i]@B,B@Z[i]) for i in range(3)) and np.allclose(Y@B,-B@Y) and not np.allclose(Z[0]@A,A@Z[0]) and not np.allclose(Y@A,-A@Y) and not np.allclose(Y@A,A@Y))
blk=np.abs(B)>1e-12; cross=[(i,j) for i in range(12) for j in range(12) if blk[i,j] and PLANE[i]!=PLANE[j]]
inplane=sorted({tuple(np.abs(F[i]-F[j]).astype(int)) for i in range(12) for j in range(12) if blk[i,j]})
check("(d') L202 = (i/sqrt2) x (signed in-plane square hopping): nonzero entries only between corners of one plane sharing one axis, modulus 1/sqrt2",
      not cross and np.allclose(np.abs(B[blk]),1/np.sqrt(2)) and set(inplane)=={(2,0,0),(0,2,0),(0,0,2)},f"|f_c - f_d| patterns {inplane}")
check("(c) Z_i W(k) Z_i = W(k + (pi/2) e_i) exactly (unitary taste, linear part 1) for W = S2.H20.S2.L202",
      all(np.allclose(Z[i]@Wk(w,k)@Z[i],Wk(w,k+np.pi/2*EX[i])) for k in KS for i in range(3)))
check("(c) Y W(k) Y = -W(k + (pi/4)(1,1,1)) exactly (taste combined with a quasi-energy shift by pi)",
      all(np.allclose(Y@Wk(w,k)@Y,-Wk(w,k+np.pi/4*np.ones(3))) for k in KS))
# controls: the X taste needs [B,Z]=0; with B = H20 (no plane structure) it fails, with A, B swapped it fails too
w2=['S2',B,'S2',A]
check("control: for S2.L202.S2.H20 (B = H20) the operator Z_x does not intertwine W(k) and W(k+(pi/2)e_x)",
      not np.allclose(Z[0]@Wk(w2,KS[0])@Z[0],Wk(w2,KS[0]+np.pi/2*EX[0])))
E=-np.pi
v0=vel_matrix(w,np.zeros(3),E); vX=vel_matrix(w,np.pi/2*EX[0],E); vs=vel_matrix(w,kst,E)
check("the node at (pi/2)e_x has the identical cone metric M M^T and chirality (M itself is fixed only up to the SU(2) basis choice in the doublet) as the O-fixed copy k = 0 (isotropic, speed 4 sqrt2/3 for two S^2)",
      np.allclose(v0['M']@v0['M'].T,vX['M']@vX['M'].T,atol=1e-9) and v0['chi']==vX['chi'] and v0['aniso']<1e-9 and abs(v0['sv'][0]-4*np.sqrt(2)/3)<1e-9,
      f"sv {np.round(vX['sv'],9)} chi {vX['chi']}")
# census in the pi/2 cube (exact period cell of the node set at E: the (pi/2)e_i tastes; the (pi/4)(1,1,1) taste maps E to E+pi)
sols,gmin=find_crossings(w,E,ngrid=20,nstart=150,lo=-np.pi/4,hi=np.pi/4,period=np.pi/2)
rows=[]
for s in sols:
    v=vel_matrix(w,s,E); fl=chirality_flux(w,s,E)
    rows.append((s,v,fl)); print(f"   node at k/pi = {np.round(s/np.pi,4)}: speeds {np.round(v['sv'],6)} chi(det M) {v['chi']:+d} lattice flux {fl:+.3f} tilt {v['tilt']:.1e} split {v['spread']:.1e}")
iso=[r for r in rows if r[1]['aniso']<1e-6]; uni=[r for r in rows if r[1]['aniso']>1e-3]
check("census at E=-pi in the (pi/2)-cube: 8 linear Weyl nodes; 2 isotropic (k=0 and a (pi/4)(1,1,1)-type point) with opposite chiralities, "
      "6 uniaxial at (pi/4)e_i-type points (3 of each chirality); net chirality 0",
      len(rows)==8 and len(iso)==2 and len(uni)==6 and sum(r[1]['chi'] for r in iso)==0 and sum(r[1]['chi'] for r in uni)==0,
      f"uniaxial speeds {sorted(set(np.round(uni[0][1]['sv'],6))) if uni else None}")
check("lattice Berry flux agrees with -sign det M at every node (B18's 'flux +1 at every class' is not reproduced)",
      all(abs(r[2]+r[1]['chi'])<1e-2 for r in rows))
# certify that there are no further crossings of E in the cube (Lipschitz certificate outside balls of radius 0.03 around the 8 nodes)
ok,bad,ev,mm=certify_clean(w,E,[r[0] for r in rows],0.03,lo=-np.pi/4,hi=np.pi/4,n0=16,maxdepth=7)
check("Lipschitz certificate: no crossing of E in the (pi/2)-cube outside 0.03-balls around these 8 nodes",ok,f"{ev} evaluations, {bad} uncertified cells")
# local cone check inside the balls: dist to E grows linearly with |q| on shells r = 0.03 ... 0.001
lin=True
for s,v,fl in rows:
    for r_ in (0.03,0.01,0.003,0.001):
        dd=dist_to_E(w,s+r_*np.array(DIRS[:30]),E); lin&=dd.min()>0.3*v['sv'].min()*r_
check("inside each ball, dist(spec, E) >= 0.3 v_min |q| on shells |q| = 0.03, 0.01, 0.003, 0.001 (isolated linear nodes; numerical, not certified)",lin)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
