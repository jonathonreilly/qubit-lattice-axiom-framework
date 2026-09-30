from common import *
for n in INT_IRREPS + SPIN_IRREPS:
    print(n, IRREP_DIM[n], check_rep([n]))
# characters: irreducibility check via sum |chi|^2 = 24 (integer) or 48 (spinorial: use both signs => 24 rotations x 2 -> |chi|^2 same for +-g since chi(-g)=-chi(g))
for n in INT_IRREPS + SPIN_IRREPS:
    tot = sum(abs(np.trace(irrep_matrix(n, R)))**2 for R in ROTS)
    print(n, 'sum|chi|^2 over 24 rotations =', round(tot, 6), '(expect 24)')
for names in [['H1'], ['A1','E','T1'], ['H1','H1']]:
    s, b0, bN = covariant_basis(names)
    print(names, 's=', s, 'dim A0 space', len(b0), 'dim A_z space', len(bN))
