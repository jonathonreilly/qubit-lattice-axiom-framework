"""Write a Singular script computing the charge module C = N / im(sigma) of a translation-invariant
Pauli stabilizer rule (q qubits per site, generators given as dicts position -> list of q labels),
and test for 3D-mobile charges via Ext^3_R(C, R) != 0 with support off the coordinate planes."""
import sys, itertools
LAB = 'IXYZ'
def sym(l):          # label -> (xbit, zbit)
    return {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
def mono(p, shift=2):
    e = [p[i] + shift for i in range(3)]
    return '*'.join(f'{v}^{k}' for v, k in zip('xyz', e) if k) or '1'
def singular_script(gens, q, name, shift=2):
    """gens: list of dicts {pos: tuple(labels per qubit)}; positions within distance 1 of origin (star)."""
    k = len(gens)
    # G: 2q x k matrix, column j = symplectic vector of generator j (positions -> monomials x^p, shifted)
    G = [[[] for _ in range(k)] for _ in range(2 * q)]
    S = [[[] for _ in range(2 * q)] for _ in range(k)]   # sigma: k x 2q, sigma_{ja} = antipode of (Lambda g_j)_a
    for j, g in enumerate(gens):
        for p, labs in g.items():
            for a in range(q):
                xb, zb = sym(labs[a])
                if xb: G[a][j].append(mono(p, shift))
                if zb: G[q + a][j].append(mono(p, shift))
                # Lambda swaps x and z blocks; antipode p -> -p
                if zb: S[j][a].append(mono(tuple(-c for c in p), shift))
                if xb: S[j][q + a].append(mono(tuple(-c for c in p), shift))
    fmt = lambda terms: '+'.join(terms) if terms else '0'
    Gs = ',\n'.join(fmt(G[r][c]) for r in range(2 * q) for c in range(k))
    Ss = ',\n'.join(fmt(S[r][c]) for r in range(k) for c in range(2 * q))
    return f'''LIB "homolog.lib"; LIB "primdec.lib"; LIB "elim.lib";
ring r=2,(x,y,z),dp;
option(redSB);
matrix Gm[{2*q}][{k}] = {Gs};
matrix Sm[{k}][{2*q}] = {Ss};
module imS = Sm;            // columns: syndromes of the 2q single-site Pauli basis elements
module syzG = simplify(syz(module(Gm)), 2);   // relations among generators (columns c with G c = 0), zero columns removed
// physical syndromes: N = kernel of s -> (bar c . s); bar c = antipode, approximated by transposing
// relations after substituting x -> 1/x via multiplication by a large monomial
int nrel = size(syzG);
print("generators: {k}, relations (syzygies): " + string(nrel));
module N;
if (nrel == 0) {{ N = freemodule({k}); }}
else {{
  matrix Cm = matrix(syzG);
  // antipode: substitute x->1/x and clear denominators by x^D y^D z^D
  int D = 12;
  matrix Cb[{k}][nrel];
  int i; int j;
  for (i=1;i<={k};i++) {{ for (j=1;j<=nrel;j++) {{
     poly f = Cm[i,j]; poly g = 0;
     while (f != 0) {{ intvec e = leadexp(f); g = g + leadcoef(f)*x^(D-e[1])*y^(D-e[2])*z^(D-e[3]); f = f - lead(f); }}
     Cb[i,j] = g; }} }}
  N = syz(module(transpose(Cb)));
}}
module imSs = std(imS);
// charge module C = N / imS  (as a presentation: generators N, relations imS)
module Cpres = modulo(N, imS);
print("charge module presentation computed; F2-dimension of C (vdim; -1 = infinite):");
print(vdim(std(Cpres)));
def E3 = Ext_R(3, Cpres);
module E3s = std(E3);
ideal annE = std(Ann(E3s));
ideal annEs = sat(annE, x*y*z);
print("support of Ext^3 off coordinate planes nonempty (3D-mobile charge exists)?");
print(annEs[1] != 1);
print("Ann(Ext^3) saturated:"); print(annEs);
print("minimal primes of Ann(C):"); print(minAssGTZ(sat(std(Ann(Cpres)), x*y*z)));
quit;
'''
