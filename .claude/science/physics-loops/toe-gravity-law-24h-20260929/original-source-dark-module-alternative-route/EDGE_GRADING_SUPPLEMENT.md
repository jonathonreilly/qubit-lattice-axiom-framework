# Actual one-edge Laurent grading: exact nilpotence and its failure to close the full ideal

Separate analytic supplement on the same safe finite cubic tori L>=8 and their physical W1 sectors. The core DERIVATION/REPORT and their identities remain unchanged. This is a direct reconstruction from the already checked canceled H formula, with the original physical rotor, all occupations, fields, charges and compensation gates. It is not a full generic-phase theorem, a replacement dynamics, or a numerical test. The initially announced T_+^2 A target is supplemented by the stronger full-carrier local support fact T_+^3=0, derived below.

## 1. Actual field bands, not freely assigned configuration phases

Fix a physical link e=(a,b), with a in A and b in B. Let E_e be its integer field operator. The complete bounded W1 Hamiltonian has the exact decomposition

    H=T_-+T_0+T_+,
    T_r=(1/(2pi)) integral_0^(2pi)
          exp(-ir phi) exp(i phi E_e) H exp(-i phi E_e) dphi,
    r=-1,0,+1.                                         (S1)

Each T_r contains exactly the original full-H matrix elements changing E_e by r. A same-edge two-hop return has zero net field change; every other two-hop term uses e at most once. Thus there are no omitted field bands. The Fourier average defines bounded operators on the FULL physical Hilbert space, without deleting transitions or imposing a field box. The diagonal phase exp(i phi E_e) preserves the physical Gauss constraint.

If e is a chord of the chosen Gauss spanning tree, (S1) corresponds to the actual Laurent decomposition H(z)=z_e^-1 H_-+H_0+z_e H_+, with all remaining physical cycle variables retained. A cubic-torus edge can be chosen as a chord because deleting it leaves the graph connected. This does not assign independent phases to the different two-hop paths.

Let A again be the aligned full-star projector around the unique hole. The claims are

    T_+^3=T_-^3=0        on the complete W1 carrier,
    T_+^2 A=T_-^2 A=0.                                 (S2)

These are operator-support statements, not positivity estimates. The signs of surviving paths are retained by T_r, but cannot create a transition absent from the support analysis.

## 2. Complete endpoint-charge transition table

Write (x,y)=(sigma_a,sigma_b). A contribution to T_+ uses e either as a plus charge moving b to a, or a minus charge moving a to b. With exactly two elementary hops, the second hop shares a or b with e. The complete canceled formula has only:

* either order of a moving-hole shared-B commutator, whose A endpoints include a;
* a same-hole term F_a F_a* when the hole is a;
* a negative same-hole term -F_a*F_a when the hole is an A site at distance two from a.

Distinct-intermediate commutator paths have canceled, and the last family is precisely the uncanceled compensation remainder. All allowed changes of the endpoint pair are contained in the following table. Some rows require additional local vacancy/gate conditions, which may remove a transition but cannot add a new one.

|input (x,y)|possible output (x,y) under T_+|
|---|---|
|(-1,-1)|(0,-1)|
|(-1,0)|(-1,-1), (+1,-1), (0,0)|
|(-1,+1)|(0,-1), (+1,0)|
|(0,-1)|none|
|(0,0)|(0,-1), (+1,0)|
|(0,+1)|(0,0), (+1,-1), (+1,+1)|
|(+1,-1)|none|
|(+1,0)|none|
|(+1,+1)|(+1,0)|

For completeness, the origins of the nontrivial rows are as follows. A positive-order moving-hole step filling a through e brings a plus charge from b: (0,+1) becomes (+1,tau), where tau is the charge sent from the other A endpoint into b. Conversely a positive-order moving-hole step emptying a through e moves a minus charge into b, after b's old charge fills the original hole: (-1,tau) becomes (0,-1). Here tau is nonzero. The NEGATIVE-order commutator is also essential on initially empty b: moving a minus out through e and then into the other hole gives (-1,0)->(0,0); moving a plus from the other A into b and then through e to hole a gives (0,0)->(+1,0). In the positive same-hole term with hole a, filling through e and leaving through another empty B gives (0,+1)->(0,0); filling from a different negative B and leaving through e gives (0,0)->(0,-1). In a negative same-hole term, leaving through e first gives (-1,0)->(tau,-1), while entering through e second gives (tau,+1)->(+1,0). These enumerate the table, including both signs of tau, both commutator orders and every possible same-hole charge exchange.

There is no directed path of length three in this table. The only length-two patterns are

    (-1,0)->(-1,-1)->(0,-1),
    (-1,0)->(0,0)-> either (0,-1) or (+1,0),
    (0,+1)->(0,0)-> either (0,-1) or (+1,0),
    (0,+1)->(+1,+1)->(+1,0).                            (S3)

This proves T_+^3=0 without dropping coherent combinations. Every basis-word path contributing to that product is absent, so no choice of field phases or cancellations can change the zero. Exchanging the local charge signs gives the identical statement for T_-; this is an enumeration symmetry of the local word algebra, NOT a claim that global charge inversion is a symmetry within the total-charge-n Gauss sector.

## 3. Why two increments already vanish on aligned inputs

Each possible length-two chain in (S3) is blocked by an aligned initial star.

For (-1,0)->(-1,-1)->(0,-1), the first step is a same-hole negative term: a negative charge leaves a through e into the initially empty b, and a different negative B charge fills a. The original hole h is unchanged. Since b was initially empty and the hole's star was full, h was not adjacent to b. The second step would have to move the hole from h to a through b, which requires h adjacent to b. It is therefore absent.

For (-1,0)->(0,0), the first step is the negative-order moving-hole commutator through the empty b. Its original hole must be an A neighbor of that empty B. The initial star would already be bright, contradicting the aligned-input condition.

For either chain beginning (0,+1)->(0,0), a is the initial hole. The first step would fill a from b and then move that charge into a DIFFERENT empty B neighbor of a. An aligned input has no such empty neighbor.

For (0,+1)->(+1,+1)->(+1,0), the first step moves the hole from a to a second A center through b, preserving the B occupation mask and leaving a plus. All six B neighbors of a remain occupied. The second step would be a negative same-hole term at a, first sending its plus charge into an empty B neighbor before refilling it through e. There is no empty B neighbor of a, so that step is absent.

This proves T_+^2 A=0 even though the first output was NOT silently projected back into A. The local sign-reversed argument proves T_-^2 A=0. It covers both polarities, all charge assignments outside the star and arbitrary fields. In the actual Laurent coefficients the corresponding equalities are H_+^3=H_-^3=0 and H_+^2 A=H_-^2 A=0.

## 4. A complete physical nonzero mixed-band coefficient

The nilpotence in (S2) does not persist when T_0 is interspersed. A fixed safe physical example uses L=24, n=6912, W=1, k=n-1 and r=(n-2)/2=3455 negative charges. Put the hole at h=0 and the sole B vacancy at v=(12,0,1). All occupied B sites are plus. All occupied A sites at l1 distance at most six from h are plus; place exactly r negative A charges outside that ball and make the remaining A sites plus. There are only230 nonzero A sites in the ball, whereas3456 plus A sites are available, so this completion is possible. Total charge is n. An integer Gauss tree flow supplies a normalized physical initial word xi, with no field cutoff.

Through three Hamiltonian powers every input hole lies within distance four of h and hence at distance at least nine from v. All B sites at distance three of those input holes are occupied. The negative same-hole terms vanish on EVERY such input column, and the remaining columns have positive return/shared-B coefficients. Every A site reached through three steps lies in the declared plus ball. This is a finite-column property of the full H, not a global incidence-square substitution.

Choose the plaquette

    h=(0,0,0), b=(1,0,0), a=(1,1,0), c=(0,1,0),
    e=(h,b).

In this plaquette notation h is the A endpoint of e and a is the other A corner.

The following three actual moving-hole steps contribute to T_+ T_0 T_+ xi, in right-to-left operator order:

    h -> a through b,
    a -> h through c,
    h -> a through b.                                  (S4)

Each has coefficient +1. Their final word beta has the same occupied B mask and all the same charges except that the plus at a has filled h and the hole is at a. The field displacement is exactly

    Delta E_(h,b)=+2,  Delta E_(a,b)=-2,
    Delta E_(a,c)=+1,  Delta E_(h,c)=-1.                (S5)

All other link displacements are zero. The divergence of (S5) is +1 at h, -1 at a and zero elsewhere, exactly the matter-charge change. Thus beta is physical and aligned.

The coefficient is exactly

    <beta,T_+ T_0 T_+ xi>=1.                            (S6)

Here is a complete coefficient check, not merely the selection of one summand. The first T_+ must move the initial hole h through e to some A neighbor a' of b. The third T_+ must again start from hole h: all relevant A charges are plus, every B neighbor of h remains occupied, so there is neither a negative-charge outward use of e nor a same-hole reshuffle through e. The middle T_0 must therefore return a' to h through a shared B different from b. The target displacement -2 on edge (a,b) forces a'=a. The face-diagonal pair a,h has exactly two shared B sites, so the return uses c. This gives only (S4). No negative coefficient from the omitted families can cancel it, because the full input-column protection was verified before selecting the coefficient.

Consequently T_+ T_0 T_+ A is nonzero. In the actual Laurent chart with e as a chord, its coefficient is a nonzero Laurent polynomial in the other physical cycle variables. This does not assert a uniform nonzero value at every phase. It is an exact full-field coefficient and therefore cannot vanish identically as a Laurent matrix.

The same occupied plaquette also permits arbitrarily many repetitions of its PARTICULAR two-step loop as a product of elementary path operators, changing a physical circulation field while returning the charge/occupation word. Such selected paths are not the full H evolution. They establish only that a finite local charge grading cannot price all intervening circulation words by the nilpotence of a single sign of a single edge.

## 5. Consequence for the attempted invariant-ideal proof

For a hypothetical Laurent null vector v(z)=sum_j z_e^j v_j with v_j in A, the highest a-priori pure-positive coefficient of H(z)^m v automatically vanishes for m>=2 because H_+^2 A=0. These particular coefficient equations therefore cannot force the top coefficient v_j to vanish. The m=1 exit equation remains a genuine condition, but is not injective on A in the dense physical sectors used above: the complete canceled H gives T_+ P_h=0 whenever the A endpoint a_e of e has distance greater than two from the hole h, and these sectors contain aligned stars at such h. Lower Laurent coefficients contain mixed words involving H_0 and H_-; (S6) shows a real surviving mixed word on the actual carrier. The argument cannot discard those words or treat the phase coefficients of different paths as freely independent.

This is a precise obstruction to the proposed one-edge leading-coefficient elimination, not to all Laurent or charge-domain methods. The full surviving system still requires (I-A)H(z)^m v=0 for every m, with all its mixed words and all physical cycle variables. The supplement neither constructs a nonzero vector satisfying that complete system nor proves it has no solution. No generic-phase verdict, actual-source reachability, normalizable nondecaying state, finite-spin conclusion or microscopic failure follows from (S2) or (S6).

No scientific runner was used. The evidence consists of the exhaustive actual endpoint table, the occupation conditions removing its two-step chains on aligned inputs, and the exact Gauss/field/charge coefficient (S6). These need their own focused independent check before being reused beyond this failed-elimination diagnosis. Core source and procedural bindings remain unchanged.
