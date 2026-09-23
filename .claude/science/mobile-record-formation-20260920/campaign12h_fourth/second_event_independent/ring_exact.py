from pathlib import Path
from collections import defaultdict
from itertools import combinations
import json
import sympy as sp
import numpy as np
from operators import charge_basis, hops, add_shift, ring_operators
D = Path(__file__).resolve().parent
L = 4; M = 6; edges = [(x, (x + 1) % 8) for x in range(8)]
A = set(range(0, 8, 2)); pairs = list(combinations(range(4), 2))
z = sp.symbols('z', nonzero=True)


def label(q):
    pair = tuple(j for j in range(4) if q[2*j+1])
    occ = [x for x,c in enumerate(q) if c]
    return pair, occ.index(q.index(-1))


def paths(q, levels):
    states = {(q, (0,)*8): 1}
    for w in levels:
        new = defaultdict(int)
        for (q0, shift), value in states.items():
            for q1, delta, amp in hops(q0, edges):
                if sum(q1[x] == 0 for x in A) == w:
                    new[q1, add_shift(shift, delta)] += amp * value
        states = dict(new)
    return states


def charge_matrix(levels):
    result = sp.zeros(6)
    for col, pair in enumerate(pairs):
        occ = sorted(list(A) + [2*j+1 for j in pair])
        q = tuple(-1 if x == occ[3] else 1 if x in occ else 0 for x in range(8))
        for (out, shift), amp in paths(q, levels).items():
            target, r = label(out)
            power = 3-r
            assert abs(power) <= 2 and shift[-1] == power
            result[pairs.index(target), col] += amp * z**power
    return result.applyfunc(sp.expand)


M0 = charge_matrix([1,0])
MM = charge_matrix([1,0,1,0])
ZZ = charge_matrix([1,2,1,0])
H2 = -M0
C = M0 - 4*sp.eye(6)
H4 = MM-ZZ/2
G = sp.diag(*[4 if (b-a) % 4 in (1,3) else 0 for a,b in pairs])
assert MM == M0*M0
assert (H4*C-C*H4).applyfunc(sp.simplify) == sp.zeros(6)
Q = H4-12*sp.eye(6)-4*C
assert (Q*G-G*Q).applyfunc(sp.simplify) == sp.zeros(6)
assert Q*C == sp.zeros(6) and C*Q == sp.zeros(6)
adj = [i for i,p in enumerate(pairs) if G[i,i] == 4]
opp = [i for i,p in enumerate(pairs) if G[i,i] == 0]
R = C.extract(adj,opp)
assert Q.extract(opp,opp) == sp.zeros(2)
assert Q.extract(adj,opp) == sp.zeros(4,2)
gram = (R.T.subs(z,1/z)*R).applyfunc(sp.expand)
s = sp.symbols('s')
char = sp.factor(gram.charpoly(s).as_expr())
assert sp.expand(char-(s*s-8*s+8-4*(z+1/z))) == 0
charC = sp.factor(C.charpoly(s).as_expr())
assert sp.expand(charC-s*s*char.subs(s,s*s)) == 0

# Compare the six-dimensional formula with separately assembled complete A,Z
# operators at generic fibers, using all six word sectors, not eigenvalues.
errors=[]
for theta in (.193, .877):
    basis, full2, full4, fullG, _, _ = ring_operators(4,theta)
    for j in range(M):
        alpha=(4*theta+2*np.pi*j)/M
        V=np.zeros((36,6),complex)
        for i,q in enumerate(basis):
            pair,r=label(q)
            V[i,pairs.index(pair)] = np.exp(1j*r*(alpha-theta))/np.sqrt(M)
        exact4=np.array(H4.subs(z,np.exp(1j*alpha)),complex)
        error=float(np.max(abs(full4@V-V@exact4)))
        assert error<1e-12
        assert np.max(abs(fullG@V-V@np.array(G,float)))<1e-12
        errors.append({'theta':theta,'word_branch':j,'H4_full_operator_residual':error})

out={'pair_basis':pairs,'adjacent_indices':adj,'opposite_indices':opp,
     'C':str(C),'H4':str(H4),'Gamma':str(G),'Q=H4-12I-4C':str(Q),
     'R=adjacent_to_opposite_block':str(R),'R_dagger_R':str(gram),
     'R_dagger_R_characteristic':str(char),'C_characteristic':str(charC),
     'exact_identities':['H4 C = C H4','Q C = C Q = 0','Q Gamma = Gamma Q',
                          'Q vanishes on opposite-pair coordinates','Gamma=4 P_adjacent'],
     'complete_operator_checks':errors}
(D/'RING_EXACT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
