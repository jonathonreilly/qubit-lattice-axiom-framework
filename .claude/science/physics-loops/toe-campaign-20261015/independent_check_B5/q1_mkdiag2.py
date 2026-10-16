import sympy as sp, pickle
from q1_trig import tcoeffs, t
free, Fs, coeqs = pickle.load(open('q1.pkl','rb'))
diag,L0,Lpi = pickle.load(open('q1_restr.pkl','rb'))
# rescale vector-part unknowns: x3_i = y3_i/sqrt(3)  -> everything rational
ys = {v: sp.Symbol('y'+str(v)[1:])/sp.sqrt(3) for v in free if str(v).startswith('x3')}
nfree = [sp.Symbol('y'+str(v)[1:]) if str(v).startswith('x3') else v for v in free]
base = [sp.expand(e.subs(ys)) for e in coeqs]
assert all(not e.has(sp.sqrt(3)) for e in base)
for m in (0,3):
    eqs = tcoeffs(diag[0] - sp.cos(m*t)) + sum([tcoeffs(sp.sqrt(3)*diag[j].subs(ys) - sp.sin(m*t)) for j in (1,2,3)], [])
    eqs = [sp.expand(e) for e in eqs if e!=0]
    assert all(not e.has(sp.sqrt(3)) for e in eqs)
    vars_ = ','.join(str(v) for v in nfree)
    with open(f'q1_real_m{m}.sing','w') as fh:
        fh.write(f'LIB "realrad.lib"; LIB "primdec.lib"; option(redSB); ring r=0,({vars_}),dp;\n')
        fh.write('ideal I=' + ',\n'.join(str(sp.Poly(e,*nfree).clear_denoms()[1].as_expr()).replace('**','^') for e in base+eqs) + ';\n')
        fh.write('ideal J=std(I); "vdim:"; vdim(J);\n')
        fh.write('ideal RR=realrad(J); RR=std(RR); "realrad:"; RR; "vdim realrad:"; vdim(RR);\n')
        fh.write('"minAss:"; list L=minAssGTZ(J); size(L); int i; for(i=1;i<=size(L);i++){ "prime",i, vdim(std(L[i])); }\nquit;\n')
pickle.dump(nfree, open('q1_nfree.pkl','wb'))
