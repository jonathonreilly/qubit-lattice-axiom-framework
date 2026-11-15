# Theorem 3 / C2 mechanism on a REDUCED ANALOG (not an instance of the statement: the smallest instance has 280 modes).
# Ring of 3 sites, one matter flavour, one rishon per link end, link number m=1 (U-type).  9 modes, dim 512.
# Original structure: matter CAR (3 modes) (x) three link factors (2 fermion modes each); link factors commute with matter and each other.
import numpy as np, itertools
a=np.array([[0,1.],[0,0]]); Zm=np.diag([1.,-1]); I=np.eye(2)
def kron(*ms):
    out=np.array([[1.]])
    for m in ms: out=np.kron(out,m)
    return out
# qubit order: m0 m1 m2 | L01:(end at 0, end at 1) | L12:(end1,end2) | L20:(end2,end0)
def op(pos,strings):
    ms=[I]*9
    for s in strings: ms[s]=Zm
    ms[pos]=a
    return kron(*ms)
c=[op(0,[]),op(1,[0]),op(2,[0,1])]                       # matter CAR
links={(0,1):(3,4),(1,2):(5,6),(2,0):(7,8)}
r={}                                                      # r[(link,site)] ; JW only inside the link
for (x,y),(px,py) in links.items():
    r[((x,y),x)]=op(px,[]); r[((x,y),y)]=op(py,[px])
dag=lambda m: m.conj().T
def anti(A,B): return np.allclose(A@B+B@A,0)
def comm(A,B): return np.allclose(A@B-B@A,0)
assert comm(c[0],r[((0,1),0)]) and comm(r[((0,1),0)],r[((1,2),1)]) and anti(r[((0,1),0)],r[((0,1),1)])
# law hop on link (x,y): c_y^dag r^y r^x^dag c_x + h.c.
def hop(x,y):
    t=dag(c[y])@r[((x,y),y)]@dag(r[((x,y),x)])@c[x]
    return t+dag(t)
# clusters: site s owns matter s and the two rishon ends at s
cluster_modes={s:[('m',s)]+[(l,s) for l in links if s in l] for s in range(3)}
# Klein: species order matter, L01, L12, L20
par=lambda ops: np.linalg.multi_dot([np.eye(512)]+[np.eye(512)-2*dag(o)@o for o in ops]+[np.eye(512)])
Pm=par(c); Pl={l:par([r[(l,l[0])],r[(l,l[1])]]) for l in links}
order=list(links)
g={('m',s):c[s] for s in range(3)}
for i,l in enumerate(order):
    K=Pm
    for l2 in order[:i]: K=K@Pl[l2]
    for s in l: g[(l,s)]=K@r[(l,s)]
keys=list(g)
assert all(anti(g[k1],g[k2]) for k1 in keys for k2 in keys if k1!=k2) and all(np.allclose(g[k]@dag(g[k])+dag(g[k])@g[k],np.eye(512)) for k in keys)
# J: graded modes -> Jordan-Wigner modes ordered cluster by cluster
seq=[k for s in range(3) for k in cluster_modes[s]]
jw=[op(i,list(range(i))) for i in range(9)]
vac=np.zeros(512); vac[0]=1
assert all(np.allclose(g[k]@vac,0) for k in keys)
J=np.zeros((512,512))
for occ in itertools.product([0,1],repeat=9):
    v1=vac.copy(); v2=vac.copy()
    for i in reversed(range(9)):
        if occ[i]: v1=dag(g[seq[i]])@v1; v2=dag(jw[i])@v2
    J+=np.outer(v2,v1)
assert np.allclose(J@J.T,np.eye(512))
def acts_trivially_on(O,cl):
    # O = O' (x) 1 on qubits of cluster cl (positions 3cl..3cl+2)
    T=O.reshape([2]*18)
    qs=[3*cl,3*cl+1,3*cl+2]
    rest=[i for i in range(9) if i not in qs]
    T=np.transpose(T,rest+qs+[9+i for i in rest]+[9+i for i in qs]).reshape(64,8,64,8)
    red=np.einsum('aibi->ab',T)/8
    return np.allclose(T,np.einsum('ab,ij->aibj',red,np.eye(8)))
ok=True
def chk(n,cnd):
    global ok; ok&=bool(cnd); print(('PASS ' if cnd else 'FAIL ')+n)
chk('hop on link (0,1) maps to an operator acting trivially on cluster 2', acts_trivially_on(J@hop(0,1)@J.T,2))
chk('hop on link (1,2) maps to an operator acting trivially on cluster 0', acts_trivially_on(J@hop(1,2)@J.T,0))
chk('hop on link (2,0) maps to an operator acting trivially on cluster 1', acts_trivially_on(J@hop(2,0)@J.T,1))
# centre at site s = (-1)^(matter + incident rishon ends) -> cluster parity (Z on its three qubits)
for s in range(3):
    cen=par([c[s]]+[r[(l,s)] for l in links if s in l])
    ms=[I]*9
    for q in (3*s,3*s+1,3*s+2): ms[q]=Zm
    chk(f'centre at site {s} maps to the cluster parity', np.allclose(J@cen@J.T,kron(*ms)))
# control: a single odd matter operator is NOT local on its cluster
chk('control: single matter mode c_1 is not mapped to an operator trivial on cluster 0', not acts_trivially_on(J@c[1]@J.T,0))
# control: a centre-odd link operator (single rishon) times nothing: not local
chk('control: single rishon at site 2 of link (1,2) is not trivial on cluster 0', not acts_trivially_on(J@r[((1,2),2)]@J.T,0))
# C2: a centre-even operator that is not a product of cluster-even factors by inspection:
O=c[0]@dag(r[((0,1),0)])@r[((0,1),1)]@dag(c[1]) + dag(c[1])@c[2]@dag(r[((1,2),2)])@r[((1,2),1)]@(np.eye(512)-2*dag(c[0])@c[0])
cents=[par([c[s]]+[r[(l,s)] for l in links if s in l]) for s in range(3)]
chk('C2 sample operator commutes with all three centres', all(comm(O,z) for z in cents))
img=J@O@J.T
# local = finite sum of products of cluster operators: every cluster-factor-local operator basis; test: image commutes with nothing extra; here T = all three clusters, so test instead that the image is a sum of products of cluster-EVEN-or-odd tensor factors, i.e. simply an operator on the tensor product (trivial), and that each term preserves each cluster parity
chk('C2 image commutes with each cluster parity', all(comm(img,kron(*[Zm if q//3==s else I for q in range(9)])) for s in range(3)))
print('ALL PASS' if ok else 'SOME FAIL')
