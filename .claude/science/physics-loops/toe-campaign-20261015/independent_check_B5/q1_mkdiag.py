import sympy as sp, pickle
from q1_trig import tcoeffs, t
free, Fs, coeqs = pickle.load(open('q1.pkl','rb'))
diag,L0,Lpi = pickle.load(open('q1_restr.pkl','rb'))
r3 = sp.Symbol('r3')
for m in range(4):
    eqs = tcoeffs(diag[0] - sp.cos(m*t)) + sum([tcoeffs(r3*diag[j] - sp.sin(m*t)) for j in (1,2,3)], [])
    eqs = [e for e in eqs if e!=0]
    vars_ = ','.join(str(v) for v in free)
    with open(f'q1_diag_m{m}.sing','w') as fh:
        fh.write(f'option(redSB); ring r=(0,r3),({vars_}),dp; minpoly=r3^2-3;\n')
        fh.write('ideal I=' + ',\n'.join(str(e).replace('**','^') for e in list(coeqs)+eqs) + ';\n')
        fh.write('ideal J=std(I); "dim:"; dim(J); "vdim:"; vdim(J); J;\nquit;\n')
    print(m, len(eqs), eqs[:3])
