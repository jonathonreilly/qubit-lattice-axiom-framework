"""T189 - WHY Z^3 CANNOT BE CHIRAL, AND WHY THAT LINKS THE TWO OPEN ITEMS.

R121 asked whether the framework's rule admits a Ginsparg-Wilson form.  GW is
   {gamma_5, D} = a D gamma_5 D
which requires a chirality that ANTI-commutes with the Dirac matrices (up to the
correction).  But R121 found the framework's Z = Gamma_1 Gamma_2 Gamma_3 COMMUTES
with every Gamma -- it is central.  So GW is not merely hard here; it may not be
formulable.

The reason is elementary and dimensional.  For the product of ALL d gammas,
moving one Gamma_a through it costs one sign per gamma it anticommutes with, i.e.
(d-1) signs.  So
      d ODD  -> (d-1) even -> the product COMMUTES  -> NO CHIRALITY EXISTS
      d EVEN -> (d-1) odd  -> the product ANTI-commutes -> gamma_5 EXISTS
The axioms give Z^3.  Three is odd.

This is checkable and both halves are already in the packet: R121 measured the
d=3 product as central, and T148 measured the d=4 product CL = Gamma_1..Gamma_4 as
anticommuting at 0.0e+00.  Confirm both here in one place, for d = 2..5.

WHY IT MATTERS.  If chirality requires even d, then the framework's chirality
problem is not a separate difficulty from its missing dynamics -- it is the SAME
gap.  R112 established that the axioms supply no time.  ADDING TIME AS A FOURTH
DIMENSION WOULD MAKE d EVEN AND CHIRALITY WOULD EXIST.  The two axiom-level
findings would then have one cause."""
import numpy as np, itertools
def gammas(d):
    """irreducible Clifford generators for R^d, built by tensor recursion"""
    s=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
       np.array([[1,0],[0,-1]],dtype=complex)]
    if d==1: return [np.array([[1]],dtype=complex)*1.0]
    if d==2: return [s[0],s[1]]
    if d==3: return [s[0],s[1],s[2]]
    G=gammas(d-2); n=G[0].shape[0]
    out=[np.kron(g,s[2]) for g in G]
    out.append(np.kron(np.eye(n),s[0]))
    out.append(np.kron(np.eye(n),s[1]))
    return out
print("T189  does the product of all gammas commute or anticommute?")
print()
print(f"   {'d':>3} {'dim':>5} {'Clifford check':>15} {'[prod,G] max':>14} {'{prod,G} max':>14} {'chirality?':>12}")
for d in (2,3,4,5):
    G=gammas(d); n=G[0].shape[0]
    cl=max(np.abs(G[a]@G[b]+G[b]@G[a]-2*(a==b)*np.eye(n)).max() for a in range(d) for b in range(d))
    P=np.eye(n,dtype=complex)
    for g in G: P=P@g
    com=max(np.abs(P@G[a]-G[a]@P).max() for a in range(d))
    anti=max(np.abs(P@G[a]+G[a]@P).max() for a in range(d))
    verdict = "YES (anti)" if anti<1e-9 else ("NO (commutes)" if com<1e-9 else "?")
    print(f"   {d:3d} {n:5d} {cl:15.1e} {com:14.1e} {anti:14.1e} {verdict:>12}")
print()
print("   d odd  -> the product COMMUTES -> there is no chirality operator at all")
print("   d even -> it ANTI-commutes     -> gamma_5 exists and GW is formulable")
print()
print("   the axioms give Z^3.  Three is odd.")
