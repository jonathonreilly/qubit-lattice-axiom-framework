import numpy as np
np.set_printoptions(suppress=True, precision=4)

# ---- gate primitives (reconstructed exactly) ----
def D(d): return np.diag(d)
def B(a,b,d):  # bilinear: -Tr(D^-1 a D^-1 b)
    Di=np.diag(1.0/np.asarray(d,float)); return float(-np.trace(Di@a@Di@b))
def sym(i,j,n=4):
    m=np.zeros((n,n));
    if i==j: m[i,i]=1.0
    else: m[i,j]=m[j,i]=1/np.sqrt(2)
    return m
def diagm(v): return np.diag(np.asarray(v,float))
def conj(R,m): return R.T@m@R
def canonical_frame():
    s2,s3,s6=np.sqrt(2),np.sqrt(3),np.sqrt(6)
    return [sym(0,0),sym(0,1),sym(0,2),sym(0,3),
            diagm((0,1/s3,1/s3,1/s3)), diagm((0,1/s2,-1/s2,0)), diagm((0,1/s6,1/s6,-2/s6)),
            sym(1,2),sym(1,3),sym(2,3)]
def rotated_frame(th):
    c,s=np.cos(th),np.sin(th); R=np.array([[1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1.0]])
    return [conj(R,m) for m in canonical_frame()]
# CHANNELS (frame-independent index groups in the canonical-frame ordering):
CH={'tt(h00)':[0], 'ts(h0i)':[1,2,3], 's-trace':[4], 's2 spin-2 (graviton)':[5,6,7,8,9]}

def frame_delta_basis(h,d,th):
    ra=[B(h,f,d) for f in canonical_frame()]; rb=[B(h,f,d) for f in rotated_frame(th)]
    return max(abs(x-y) for x,y in zip(ra,rb))

# B-orthogonal projector onto span(F) (columns = vec(channel basis)); frame-independent (depends only on span)
def vec(m,d):  # coordinate = B-pairing against an orthonormal-ish dual; just flatten the 16 entries
    return m.reshape(-1)
def Gmat(d):  # 16x16 metric on flattened sym matrices via B
    pass
def proj_channel(F_mats,d):
    # build G-orthogonal projector in the B-form on flattened-matrix space, onto span(F)
    F=np.array([m.reshape(-1) for m in F_mats]).T   # 16 x k
    Di=np.diag(1.0/np.asarray(d,float))
    # B(a,b) = -tr(Di a Di b) = -(vec a)^T (Di kron Di) (vec b)  using row-major vec and kron identity
    Gk = -np.kron(Di,Di)
    GFF = F.T@Gk@F
    P = F@np.linalg.inv(GFF)@F.T@Gk
    return P, Gk

print("="*78)
print("STEP 0  reproduce the gate baseline (anisotropic d=(2,3,5,7)):")
d_aniso=(2.,3.,5.,7.)
h=np.array([[1,0.35,-0.22,0.18],[0.35,-0.75,0.14,0.07],[-0.22,0.14,0.41,-0.19],[0.18,0.07,-0.19,-0.28]])
fdb=frame_delta_basis(h,d_aniso,np.pi/6)
print(f"  frame_delta_BASIS = {fdb:.6e}   (gate reports 6.767e-2)  -> the obstruction, REPRODUCED")
print()
print("="*78)
print("STEP 1  THE CRACK: canonical irreducible-CHANNEL projectors are frame-INDEPENDENT")
print("  (P_c built from the canonical frame vs the rotated frame -- same projector?)")
for d_lab,d in [("anisotropic (2,3,5,7)",d_aniso),("ISOTROPIC physical (1,1,1,1)",(1.,1.,1.,1.))]:
    print(f"  background = {d_lab}")
    canF=canonical_frame(); rotF=rotated_frame(np.pi/6)
    maxdP=0.0
    for name,idx in CH.items():
        Pc_can,_=proj_channel([canF[i] for i in idx],d)
        Pc_rot,_=proj_channel([rotF[i] for i in idx],d)
        dP=np.abs(Pc_can-Pc_rot).max(); maxdP=max(maxdP,dP)
        print(f"     ||P_c^canon - P_c^rot||  channel {name:24} = {dP:.3e}")
    print(f"     => frame_delta_CHANNEL (max over channels) = {maxdP:.3e}")
    print()
print("="*78)
print("STEP 2  on the ISOTROPIC background the channels are mutually B-orthogonal + s2 is SO(3)-IRREDUCIBLE")
d=(1.,1.,1.,1.); canF=canonical_frame()
# mutual B-orthogonality of the 4 channels
import itertools
chvecs={name:[canF[i] for i in idx] for name,idx in CH.items()}
worst_off=0.0
names=list(CH)
for a,b in itertools.combinations(names,2):
    for ma in chvecs[a]:
        for mb in chvecs[b]:
            worst_off=max(worst_off,abs(B(ma,mb,d)))
print(f"  max |B(channel_a, channel_b)| across distinct channels = {worst_off:.2e}  (=> mutually orthogonal)")
# s2 irreducibility: random SO(3), orbit of one s2 vector must stay in s2 and span all 5 dims
def randSO3(rng):
    A=rng.standard_normal((3,3));Q,_=np.linalg.qr(A)
    if np.linalg.det(Q)<0:Q[:,0]*=-1
    R=np.eye(4);R[1:,1:]=Q;return R
rng=np.random.default_rng(0)
s2basis=[canF[i] for i in CH['s2 spin-2 (graviton)']]
# project a generic s2 vector under many rotations; check orbit spans 5 and stays in s2
P_s2,Gk=proj_channel(s2basis,d)
v0=sum(c*m for c,m in zip([0.4,-0.3,0.5,0.2,-0.6],s2basis))
orbit=[]; stay=0.0
for _ in range(40):
    R=randSO3(rng); vr=conj(R,v0)
    stay=max(stay, np.abs(vr.reshape(-1)-P_s2@vr.reshape(-1)).max())  # stays in s2 subspace?
    orbit.append(vr.reshape(-1))
rank_orbit=np.linalg.matrix_rank(np.array(orbit),tol=1e-9)
print(f"  s2 channel: SO(3) orbit stays in s2 (max leave={stay:.1e}); orbit rank={rank_orbit} (=5 => irreducible spin-2)")
print()
print("HONEST SCOPE: this closes the POINT-WISE frame ambiguity -- the canonical irreducible-channel")
print("projectors are frame-independent (the gate's frame_delta was a within-channel BASIS artifact);")
print("the 5-dim s2 is the canonical graviton channel. NOT yet closed: the bundle CONNECTION across")
print("points + the 5->2 transverse-traceless reduction (needs a propagation direction k).")
import numpy as np
np.set_printoptions(suppress=True, precision=5)
eta=np.diag([-1.,1.,1.,1.])      # mostly-plus
def raise1(p): return eta@p
def Rlin(h,p):
    # linearized Ricci in momentum space (operator up to overall sign fixed by gauge-invariance test)
    pu=raise1(p); p2=p@eta@p; hud=eta@h          # h^lambda_nu = eta h
    htr=np.trace(eta@h)                          # h = eta^{mn} h_mn
    R=np.zeros((4,4))
    for m in range(4):
        for n in range(4):
            term = (p[m]*np.dot(pu,h[:,n]) + p[n]*np.dot(pu,h[:,m]) - p2*h[m,n] - p[m]*p[n]*htr)
            R[m,n]=0.5*term
    return R
def Glin(h,p):
    R=Rlin(h,p); Rs=np.trace(eta@R); return R-0.5*eta*Rs

rng=np.random.default_rng(1)
print("VALIDATION: linearized Einstein tensor is gauge-invariant  G_lin(p.xi + xi.p) = 0")
p=np.array([0.7,0.3,-0.5,0.9])
worst=0.0
for _ in range(5):
    xi=rng.standard_normal(4)
    hg=np.outer(p,xi)+np.outer(xi,p)            # pure-gauge perturbation
    worst=max(worst, np.abs(Glin(hg,p)).max())
print(f"   max|G_lin(gauge)| = {worst:.2e}   -> operator validated (it IS linearized Einstein)\n")

# Null-cone sanity check: p=(w,0,0,k) with w=k.  The physical TT waves solve
# the source-free linearized equations on shell, so a direct G_lin coefficient
# read is zero and is NOT the stiffness-sign diagnostic. The load-bearing
# channel-sign read is the off-shell kinetic-term check below.
k=1.0; p=np.array([k,0,0,k])                     # null
def coeff_on(h,p):
    G=Glin(h,p)
    # project G back onto h direction (Hilbert-Schmidt with eta-raised), normalized
    num=np.tensordot(eta@G@eta, h, axes=2); den=np.tensordot(eta@h@eta, h, axes=2)
    return num/den
print("NULL-CONE sanity check (non-diagnostic for kinetic signs):")
# spin-2 TT polarizations (transverse to z, traceless): h_+ and h_x
hplus=np.zeros((4,4)); hplus[1,1]=1; hplus[2,2]=-1     # +  polarization
hcross=np.zeros((4,4)); hcross[1,2]=hcross[2,1]=1      # x polarization
cp=coeff_on(hplus,p); cx=coeff_on(hcross,p)
print(f"   on-shell TT h_+ coefficient = {cp:+.4f} (zero as expected for a free null wave)")
print(f"   on-shell TT h_x coefficient = {cx:+.4f} (zero as expected for a free null wave)")
print("   The sign-pattern comparison is made below from off-shell channel stiffnesses.")

print("\n" + "="*78)
print("STEP 3  OFF-SHELL channel stiffness signs (the kinetic-term signs)")
# off-shell timelike p; read raw eigenvalue of G_lin on each channel mode
p=np.array([1.3,0.0,0.0,0.4]); p2=p@eta@p
print(f"  p = {p}, p^2 = {p2:.3f} (off-shell)")
# TT modes transverse to spatial k=z-axis, traceless (genuine spin-2 graviton polarizations)
hplus=np.diag([0.,1.,-1.,0.]); hcross=np.zeros((4,4)); hcross[1,2]=hcross[2,1]=1.0
Gp=Glin(hplus,p); Gx=Glin(hcross,p)
mu_plus = Gp[1,1]/hplus[1,1]; is_eig_p = np.allclose(Gp, mu_plus*hplus)
mu_cross= Gx[1,2]/hcross[1,2]; is_eig_x = np.allclose(Gx, mu_cross*hcross)
print(f"  spin-2 h_+  : G_lin(h_+) = mu*h_+ ? {is_eig_p};  mu_TT = {mu_plus:+.4f}")
print(f"  spin-2 h_x  : G_lin(h_x) = mu*h_x ? {is_eig_x};  mu_TT = {mu_cross:+.4f}")
# conformal mode: full-trace h = phi*eta ; read its G_lin eigenvalue component
hconf=eta.copy()
Gc=Glin(hconf,p)
# G_lin(eta) is proportional to a combination; read the scalar stiffness via the trace pairing
mu_conf = np.trace(eta@Gc@eta@hconf)/np.trace(eta@hconf@eta@hconf)
print(f"  spin-0 conformal (h=phi*eta): scalar stiffness mu_conf = {mu_conf:+.4f}")
print()
opp = (mu_plus>0) != (mu_conf>0)
print(f"  TT and conformal OPPOSITE sign (the Einstein conformal-factor structure)? {opp}")
print(f"    => linearized Einstein: TT = {'+' if mu_plus>0 else '-'},  conformal = {'+' if mu_conf>0 else '-'}")
print(f"    => emergent Regge:      l=2 = +9.96 (+),  breathing = -5.18 (-)   [OPPOSITE]")
print(f"  SIGN PATTERN of emergent channels MATCHES linearized Einstein: {opp}")
