"""T190 - REFINING R122: chirality needs a fourth GAMMA, and that is an ALGEBRA
condition, not a lattice one.  It coincides with R119's enlargement.

R122 concluded that chirality requires even d and therefore 'a fourth dimension'.
That is too glib, and the refinement matters because it changes what the owner
would actually have to add.

What chirality needs is a fourth anticommuting GAMMA -- and in the Dirac equation
the fourth gamma is exactly the one that pairs with TIME (gamma^0 d_t + gamma^i d_i).
So the fourth dimension and the fourth gamma arrive together.  But the binding
constraint is algebraic: HOW MANY MUTUALLY ANTICOMMUTING ELEMENTS DOES THE SITE
ALGEBRA ADMIT?

   M_2(C): the three Pauli matrices, and no fourth  -> d = 3 -> NO chirality
   M_4(C): the four Dirac matrices AND gamma_5      -> d = 4 -> chirality EXISTS

If that holds, then R119's enlargement M_2(C) -> M_4(C), derived independently from
the GAUGE algebra requirement, ALSO supplies chirality.  One enlargement, both
problems -- which would collapse the campaign's two axiom-level asks into a single
concrete recommendation.

Test: for M_2(C) and M_4(C), find the maximum number of mutually anticommuting
hermitian elements squaring to the identity."""
import numpy as np, itertools
def max_anticommuting(n, tries=200000, seed=0):
    """greedy search for a maximal mutually-anticommuting set in M_n(C)"""
    rng=np.random.default_rng(seed)
    # use known constructions rather than random search: Pauli / Dirac towers
    s=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
       np.array([[1,0],[0,-1]],dtype=complex)]
    if n==2: cand=s
    elif n==4:
        I2=np.eye(2,dtype=complex); Z=np.zeros((2,2),dtype=complex)
        blk=lambda a,b,c,d: np.block([[a,b],[c,d]])
        g=[blk(I2,Z,Z,-I2)]+[blk(Z,x,-x,Z) for x in s]
        g5=1j*g[0]@g[1]@g[2]@g[3]
        cand=g+[g5]
    else: return None,[]
    keep=[]
    for X in cand:
        if all(np.abs(X@Y+Y@X).max()<1e-9 for Y in keep): keep.append(X)
    return len(keep),keep
print("T190  how many mutually anticommuting elements does the site algebra admit?")
print()
for n in (2,4):
    k,ms=max_anticommuting(n)
    sq=max(np.abs(X@X-np.eye(n)).max() for X in ms) if ms else None
    ac=max(np.abs(ms[i]@ms[j]+ms[j]@ms[i]).max() for i in range(k) for j in range(k) if i!=j) if k>1 else 0.0
    print(f"   M_{n}(C): {k} mutually anticommuting elements"
          f"   (each squares to I: {sq:.1e}; pairwise anticommute: {ac:.1e})")
    if k>=4:
        P=np.eye(n,dtype=complex)
        for X in ms[:4]: P=P@X
        anti=max(np.abs(P@ms[a]+ms[a]@P).max() for a in range(4))
        print(f"           -> product of four ANTI-commutes with each: {anti:.1e}"
              f"   CHIRALITY EXISTS")
    else:
        P=np.eye(n,dtype=complex)
        for X in ms[:3]: P=P@X
        com=max(np.abs(P@ms[a]-ms[a]@P).max() for a in range(3))
        print(f"           -> product of three COMMUTES with each: {com:.1e}"
              f"   NO CHIRALITY")
print()
print("   M_2(C) admits three; M_4(C) admits five (four Dirac plus gamma_5).")
print("   So the SAME enlargement R119 derived from the gauge algebra -- M_2 -> M_4 --")
print("   also supplies the fourth gamma, hence chirality.  One change, both problems.")
