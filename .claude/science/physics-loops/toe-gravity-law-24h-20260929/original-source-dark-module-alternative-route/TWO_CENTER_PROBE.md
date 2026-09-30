# A physical two-center protected component has constant Dirichlet energies 5 and 7

Independent final geometry probe under TWO_CENTER_TARGET.md. The parent disclosed the possible two-center mechanism and the proposed values5,7. I read the actual protected-column definition and earlier proof, but did NOT open the new unaccepted fixed-energy/common-spectrum proof. This is an analytic reconstruction, not a blind review, formal audit, or scientific execution. All earlier frozen files remain unchanged.

The proposed component EXISTS. It has two possible positions of ONE hole, so W=1 throughout. Its principal Hamiltonian has eigenvalues5 and7 at every physical cycle phase. This refutes a universal assertion that6 is the only possible phase-independent energy of the physical protected Dirichlet family. It does not assert that5 or7 solves an additional specified intersection of spectra, is an eigenvalue with protected support for the full H, or carries actual source mass.

## 1. Literal protected condition and supplied normalization

Use the original H=C+[F,F*] on the physical Gauss rotor. A protected plus word with hole h has:

    every other A at graph distance <=2 from h of charge +1;
    every B at graph distance <=3 from h occupied;
    every immediate B neighbor of h of charge +1.       (1)

Complete the hole by plus to define alpha, the full A charge pattern, and let chi be the B charge/vacancy pattern. A physical one-hole word then requires

    sum alpha+sum chi=n+1,  n=|A|.                     (2)

The completed pair is bookkeeping, not itself a physical zero-hole state of total charge n. The set F_(alpha,chi) consists of ALL eligible plus-hole centers satisfying (1), not a chosen two-column subset.

The actual canceled H has no negative same-hole first hop on a protected column, because all B sites within three are occupied. Each of its six filling/return paths contributes1. A moving hole travels through a shared B to an A at distance two; that A is plus by (1), so the B charge stays plus and the completed background is unchanged. Distinct-intermediate terms cancel in the original commutator. Thus the protected columns are exactly the original magnetic two-hop matrix T=K* K, including the outgoing rows. T has diagonal6, range two between A sites, and an axial off-diagonal entry of unit modulus from its single shared B. No independent hopping phases or missing rows are supplied by this reduction.

## 2. A globally physical completed background

Choose the cubic torus L=16, so n=2048. Let

    h0=(0,0,0),    h1=(2,0,0),    v=(8,0,1) in B,
    k=N_B=n-1=2047.

Put charge plus on every B except the sole vacancy v. Let E_r(h) denote the A sites at periodic l1 distance at most r from h, and set

    P=E_2(h0) union E_2(h1),
    U=E_4(h0) union E_4(h1).                            (3)

Set alpha plus on P and minus on U outside P. Complete the A pattern outside U by choosing enough plus sites to give exactly1025 plus A sites in all; all other A sites are minus.

This is possible with exact counts. An A ball of radius two has19 sites. The intersection of the two such balls consists of h0,h1 and (1,+-1,0),(1,0,+-1), so |P|=32. An A ball of radius four has1+18+66=85 sites, so |U|<=170. There are at least1878 A sites outside U, whereas only1025-32=993 of them need be chosen plus. Thus the negative guard is compatible with the total charge and can never be overwritten by the far completion.

The completed A pattern has1025 plus and1023 minus sites, hence sum alpha=2. The B sum is2047, so (2) holds:2+2047=2049=n+1. Removing plus at either h0 or h1 gives a physical W1 charge pattern of total charge n. The negative count is1023=(k-1)/2, exactly the required physical sector.

For EACH allowed hole center, an integer tree flow solves div E=q-1_A because the divergence demand is an integer vector of sum zero. All its integer cycle translates are included. This supplies the full physical Gauss fiber and normalizable finite-field words; no freely chosen independent edge phase or illegal charge pattern is used.

## 3. Every protected neighbor of the pair is checked

Both h0 and h1 belong to the complete F_(alpha,chi). Their distance-two A cones lie in P and are plus. The vacancy has distances9 and7 from them, respectively, so neither B ball of radius three contains a vacancy. Their immediate B stars are plus.

Every center that could be coupled by T to h0 or h1 lies in P. I show that every c in P other than h0,h1 FAILS the A-sign part of (1), irrespective of all far choices.

Use the local integer representatives c=(x,y,z); no coordinate in the following witnesses wraps on L16. If a transverse coordinate, say y, is nonzero, choose

    d=c+2 sign(y) e_y.

For each of h0,h1, its distance from c is a positive even integer, at least two. The outward transverse move increases both distances by two, so d lies outside P. Since c was within distance two of at least one center, d remains within distance four of that center: d lies in U outside P. It therefore has charge minus and is an occupied A site at distance two from c. The same construction with z handles the remaining case of nonzero z. The transverse coordinates of d have absolute value at most four, and all relevant x differences are at most four, so periodic distance agrees with these integer calculations.

If y=z=0, even parity and membership in P leave x=-2,0,2,4. Excluding h0,h1, choose d=-4 e_x for c=-2 e_x, and d=6 e_x for c=4 e_x. Each witness lies in U outside P and has charge minus; the relevant distances are four or six, below the L16 wrapping threshold in that coordinate.

These are ALL possible adjacent A centers, including the face-diagonal neighbors. Hence

    F_(alpha,chi) intersect P={h0,h1}.                  (4)

Other protected centers may exist far away. They cannot join this component: a first edge of any T-path from the pair to a different protected center would have to be a distance-two neighbor in P, which (4) excludes. The pair is therefore an isolated component of the complete principal matrix P_F T P_F, not merely of an artificially selected submatrix.

## 4. Exact physical principal spectrum, including all phase variables

The two centers share exactly one B, b=(1,0,0). Let u(theta) be the actual two-hop coefficient from h0 to h1, in any physical Gauss phase chart. Its form in a connection representative is exp(i A_(h0,b)-i A_(h1,b)), up to the charge-chart basis gauge. In particular |u|=1 at EVERY physical cycle phase. The principal block, ordered h0,h1, is

    D_pair(theta) = [[6, conjugate(u(theta))],
                     [u(theta), 6]],
    det(D_pair-lambda I)=(6-lambda)^2-1.                (5)

Thus its two eigenvalues are exactly5 and7, independently of every physical phase. This uses a single original axial edge, not a selected phase point or a rank sample. All return coefficients and diagonal normalization are those of H=C+[F,F*]. A separate prefactor delta on H would of course multiply these energy values by delta.

The result can also be stated in the full normalizable rotor Hilbert space for the PRINCIPAL compression. The unique axial path is a unitary U between the complete physical field spaces over the two hole positions, with its actual Gauss-preserving link translation. The compressed block is [[6I,U*],[U,6I]]. For any unit vector phi in the h0 field space, (phi,+U phi)/sqrt(2) and (phi,-U phi)/sqrt(2) are normalizable compressed eigenvectors of energies7 and5. This does not turn an isolated phase delta into a physical state.

There is no hidden opposite-polarity protected neighbor of this block in the full protected UNION. Protected columns preserve their B charge/vacancy pattern, and chi here has no negative B charges at all. Consequently no negative-polarity protected column with that chi exists. Positive-polarity completed backgrounds have unique outgoing completion; a column of a different such background cannot feed this block. Thus the isolated block is also present in the principal compression onto the full protected union at this physical k. This is still a compression, not an invariant subspace for H.

## 5. An explicit outgoing row prevents the incorrect full-H inference

Take c=-2 e_x. It lies in P and has charge plus, but is unprotected because of the negative witness -4 e_x. It is an axial distance-two neighbor of h0 and at distance four from h1. The actual H has exactly one shared-B path from h0 to this c, of unit modulus and the correct field translation; there is no h1-to-c term. Therefore each normalized vector just displayed has an outgoing c component of H of norm exactly1/sqrt(2).

In particular, for the corresponding compressed eigenvalue lambda=5 or7,

    ||(H-lambda) psi_pair|| >= 1/sqrt(2).               (6)

The exterior row is a real physical charge/field row, not an auxiliary boundary condition. It cannot be canceled by the other member of this pair. A larger coherent state using additional backgrounds/centers would be a different problem. Equations (5)-(6) distinguish phase-independent DIRICHLET energies from actual H eigenvectors, invariant dark modules, decay rates or source-populated modes.

The only negative conclusion here is that a universal “6 is the only constant protected Dirichlet energy” assertion would be false. No unaccepted fixed-energy theorem was used or checked. Whether5,7 survive any additional required common-spectrum intersection and the full boundary/source equations remains open under that separate target.

## 6. Evidence and boundaries

This proof is analytic: exact finite geometry, counts, the full protected-column conditions, actual two-hop coefficients and Gauss completion. No enumeration, numerical spectrum, scientific runner, changed source law or added record label was used. The parent supplied the candidate idea; the source reading and reconstruction were independent of the new fixed-energy proof. Main fb5da8dd and selected7146 methodology/primitive closure are reused at their unchanged actual bound identities. The previously frozen core and edge supplement are not edited by this probe. A focused independent check is required before downstream use of the new example.
