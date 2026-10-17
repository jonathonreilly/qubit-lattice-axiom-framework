import sys; sys.argv=['q','4']
exec(open('cocyc.py').read().split("# check translation invariance")[0])
LI={l:i for i,l in enumerate(LINKS)}
def img_link(k,l):
    h0,_=lhalves(*l); return link_of_half(int(rot[k][0][h0]))
# composite F_ab as set of links (all links), computed per link via its first half
Fs={}
for a in range(24):
    for b in range(24):
        ab=rid(ROTS[a]@ROTS[b]); S=set()
        for l in LINKS:
            h0,h1=lhalves(*l)
            l0=U(a,U(b,(1<<h0,0,0))); r0=U(ab,(1<<h0,0,0))
            if l0[2]!=r0[2]: S.add(LI[link_of_half(int(rot[ab][0][h0]))])
        Fs[(a,b)]=S
print('computed cocycle')
# orbits of links under O
orb=[]; seen=set()
for l in LINKS:
    if l in seen: continue
    o=set(img_link(k,l) for k in range(24)); seen|=o; orb.append(sorted(o))
print(len(orb),'link orbits; sizes',sorted(set(len(o) for o in orb)))
inv=[rid(np.round(np.linalg.inv(R)).astype(int)) for R in ROTS]
bad_orbits=[]
for o in orb:
    idx={l:i for i,l in enumerate(o)}; m=len(o); n=24*m
    var=lambda k,l: k*m+idx[l]
    piv={}; incons=False
    for a in range(24):
        for b in range(24):
            ab=rid(ROTS[a]@ROTS[b])
            for l in o:
                # T_a(l) + T_b(a^-1 l) + T_ab(l) = F_ab(l)
                r=(1<<var(a,l))^(1<<var(b,img_link(inv[a],l)))^(1<<var(ab,l))
                x=r|((1 if LI[l] in Fs[(a,b)] else 0)<<n)
                while True:
                    low=x&((1<<n)-1)
                    if low==0:
                        if x: incons=True
                        break
                    c=low.bit_length()-1
                    if c in piv: x^=piv[c]
                    else: piv[c]=x; break
    if incons:
        stab=[k for k in range(24) if img_link(k,o[0])==o[0]]
        bad_orbits.append((m,o[0],len(stab)))
print('obstructed orbits:',len(bad_orbits))
for b in bad_orbits[:10]: print('  size',b[0],'rep',b[1],'stabilizer order',b[2])
