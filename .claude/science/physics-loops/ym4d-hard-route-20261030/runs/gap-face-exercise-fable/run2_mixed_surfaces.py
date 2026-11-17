# Run 2: closed mixed surfaces in the box A x B, A and B 3x3 grids of sites.
import itertools
def grid():
    sites=[(i,j) for i in range(3) for j in range(3)]
    edges=[((i,j),(i+1,j)) for i in range(2) for j in range(3)]+[((i,j),(i,j+1)) for i in range(3) for j in range(2)]
    squares=[]
    for i in range(2):
        for j in range(2):
            squares.append([((i,j),(i+1,j)),((i,j+1),(i+1,j+1)),((i,j),(i,j+1)),((i+1,j),(i+1,j+1))])
    return sites,edges,squares
sA,eA,qA = grid(); sB,eB,qB = grid()
plaq = [(e,f) for e in eA for f in eB]; pidx={p:i for i,p in enumerate(plaq)}
links = [('L',e,b) for e in eA for b in sB]+[('T',a,f) for a in sA for f in eB]; lidx={l:i for i,l in enumerate(links)}
# boundary of each plaquette as a bitmask over links
bd=[]
for (e,f) in plaq:
    m=0
    for b in f: m ^= 1<<lidx[('L',e,b)]
    for a in e: m ^= 1<<lidx[('T',a,f)]
    bd.append(m)
# rank over F_2 of the plaquette->link map (rows = plaquettes)
def rank(rows):
    rows=list(rows); r=0
    piv={}
    for v in rows:
        while v:
            h=v.bit_length()-1
            if h in piv: v^=piv[h]
            else: piv[h]=v; r+=1; break
    return r
rk = rank(bd)
print('plaquettes', len(plaq), 'links', len(links), 'rank', rk, 'kernel dim', len(plaq)-rk)
shells=[]
for P in qA:
    for Q in qB:
        m=0
        for e in P:
            for f in Q: m ^= 1<<pidx[(e,f)]
        shells.append(m)
def closed(m):
    t=0
    for i in range(len(plaq)):
        if m>>i & 1: t ^= bd[i]
    return t==0
print('shells', len(shells), 'all closed:', all(closed(m) for m in shells), 'rank of shells', rank(shells))
# histogram of areas over all 2^16 sums (Gray code)
hist={}
cur=0
hist[0]=1
for k in range(1,1<<16):
    low=(k & -k).bit_length()-1
    cur ^= shells[low]
    a=bin(cur).count('1')
    hist[a]=hist.get(a,0)+1
print('number of surfaces', sum(hist.values()))
print('area : count (areas up to 48):', {a:hist[a] for a in sorted(hist) if a<=48})
print('largest area', max(hist))
for u in (0.479,0.507,0.520):
    Z=sum(n*u**a for a,n in hist.items())
    lead=16*u**16
    print('u=%.3f  Z_box-1 = %.6e   leading 16 u^16 = %.6e   ratio = %.4f' % (u, Z-1, lead, (Z-1)/lead))
