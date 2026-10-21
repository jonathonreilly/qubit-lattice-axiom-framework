exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
Tb1=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/Tb1.npy')
Tb2=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/Tb2.npy')
b1=blocks_from(Tb1); b2=blocks_from(Tb2)
G=Hk(blon,kst)+0.37*Lam+0.23*Hk(blli,kst); w,V=np.linalg.eigh(G)
dbl=[V[:,i:i+2] for i in range(11) if abs(w[i+1]-w[i])<1e-8 and (i==0 or abs(w[i]-w[i-1])>1e-8) and (i+2>11 or abs(w[i+2]-w[i])>1e-8)]
ks=[np.array([0.37,1.1,-0.4]),np.array([2.0,-0.3,0.9]),kst+0.2]
base={"Hon":lambda k:Hon0,"Hli":lambda k:Hk(blli,k),"Tb1":lambda k:Hk(b1,k),"Tb2":lambda k:Hk(b2,k),"Lam":lambda k:Lam}
names=list(base)
rng=np.random.default_rng(0)
combos=[]
for a,b in itertools.combinations(names,2):
    for ca,cb in ((1,1),(1,-1),(1,1j),(1,np.sqrt(2)),(1,2)):
        combos.append((f"{ca}*{a}+{cb}*{b}",lambda k,a=a,b=b,ca=ca,cb=cb: ca*base[a](k)+cb*base[b](k)))
combos+= [("Tb1+Tb2+Hli",lambda k: Hk(b1,k)+Hk(b2,k)+Hk(blli,k)),("Tb1-Tb2",lambda k:Hk(b1,k)-Hk(b2,k)),
          ("i[Hli,Tb1]",lambda k:1j*(Hk(blli,k)@Hk(b1,k)-Hk(b1,k)@Hk(blli,k))),("{Hli,Tb1}",lambda k:Hk(blli,k)@Hk(b1,k)+Hk(b1,k)@Hk(blli,k))]
for nm,A in combos:
    M=[A(k) for k in ks]
    if not all(np.allclose(m,m.conj().T) for m in M): continue
    specs=[np.round(np.linalg.eigvalsh(m),6) for m in M]
    const=all(np.allclose(s,specs[0],atol=1e-6) for s in specs)
    nd=len(set(specs[0]))
    h=1e-6; vel=[]
    for P in dbl:
        dA=[(A(kst+h*e)-A(kst-h*e))/(2*h) for e in np.eye(3)]
        vel.append(max(np.linalg.norm(P.conj().T@d@P-np.trace(P.conj().T@d@P)/2*np.eye(2)) for d in dA))
    if const or nm.startswith("Tb1") or "Tb" in nm and max(vel)>1e-3 and nd<=4:
        print(f"{nm:20s} const-spectrum {const} distinct {nd} doublet vel {np.round(vel,4)} spec {specs[0][::2] if const else ''}")
