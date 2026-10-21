# Controlled marker SU(3) representations

On a qubit chain, define a valid seven-bit word as110|one-hot(3)|0. The three words are1101000,1100100,1100010. Let P_x select a valid word beginning at x and let T^a be the fundamental SU(3) matrices on its one-hot register. Set G_x^a=P_x T^a P_x, zero elsewhere. The representation is reducible and state-controlled: most bit configurations carry no active charge at x.

No proper suffix of a valid word equals a prefix of a valid word. Exhausting the three words and shifts1..6 is a finite exact parse certificate. Thus overlapping active words are incompatible. Colour moves preserve the predicate at their own word and cannot create an overlapping valid word. For compatible separated words the acted-on registers are disjoint. Consequently

[G_x^a,G_x^b]=i f_abc G_x^c, [G_x^a,G_y^b]=0 for x!=y,
T G_x^a T†=G_(x+1)^a.

This is a full-space controlled-operator argument, rather than a check restricted to one chosen marker sector. The Casimir is sum_a(G_x^a)²=(4/3)P_x, explicitly displaying the inactive complement.

The linked nineteen-bit token is110|q(3)|0|p(3)|0|A(3)|0|B(3)|0. The q,p registers are each empty or one-hot with at most one occupied; A,B are both empty or both one-hot. There are7 matter patterns and10 link patterns, hence70 valid words. The same exhaustive proper-overlap test applies to these words. With V(x) the token predicate, P_x=V(x)V(x-19), define

G_x^a=P_x[T^a(q_x)-conjugate(T^a)(p_x)-conjugate(T^a)(A_x)+T^a(B_(x-19))]P_x.

Every token predicate is colour-blind on each complete register. Jointly compatible tokens share no acted-on register; adjacent generators can read the same marker without acting on the same colour register. The direct sum and tensor sum of fundamental/conjugate representations therefore obey the SU(3) algebra and cross commutation on the full Hilbert space. The finite parse test covers all overlapping offsets; nonoverlapping supports commute directly.

A link creation operator maps an empty pair of neighboring matter registers and an empty link to sum_(a,b)|q_x=a,A_x=a,B_x=b,p_(x+19)=b>, with appropriate valid-token projectors. The q/A and B/p contractions are fundamental–conjugate singlets. Therefore each endpoint Gauss generator annihilates the created state, and K+K† commutes with the generators. Diagonal colour-blind matter/link occupation energies also commute. Summing translates makes the supplied law translation-covariant. This does not prove its ground state or continuum physics.

The original35-bit rod extension supplies separate x/y/z link registers and translated marker predicates in three dimensions. It is anisotropic and requires its own parse/colour-blind conditions; no cubic-rotation or QCD-universality claim follows. Its complete construction sources remain inspectable with these restrictions.

The abstract dimension inequality3^k<=2^n applies only to a simultaneously nontrivial joint sector carrying k independent fundamental factors. It is not a global count of all conditional sectors. No general physical-qubit ownership theorem or forced block interpretation is asserted: such stronger original conclusions require hypotheses not supplied by these controlled constructions.

## Explicit three-dimensional register allocation

For the 35-bit rod beginning at p, the marker and matter offsets are those of the nineteen-bit token. For mu=x,y,z use A_mu at offsets 11+8mu through 13+8mu, a zero at 14+8mu, B_mu at 15+8mu through 17+8mu, and a zero at 18+8mu, numbering mu=0,1,2. Each of the three links has ten empty-or-paired patterns; hence there are 7*10^3=7000 valid rods. Let n_x(p)=p-35e_x, n_y(p)=p-e_y, n_z(p)=p-e_z and Pi_p=V(p) product_mu V(n_mu(p)). The complete generator is

G_p^a=Pi_p [T^a(q_p)-conjugate(T^a)(p_p)-sum_mu conjugate(T^a)(A_mu,p)+sum_mu T^a(B_mu,n_mu(p))] Pi_p.

All rods lie along x. In a common row the proper-overlap certificate forces distinct simultaneously valid rods to have disjoint supports; on different rows the supports are already disjoint. Two predicates can demand the identical rod. Its colour moves preserve validity because all restrictions concern occupation counts, not colour. Each A register is assigned to the starting vertex and each B register to precisely its translated far endpoint. Thus distinct compatible generators have disjoint acted-on colour registers even when they inspect a common rod. This proves the required colour blindness and cross commutation; incompatible predicates multiply to zero and their colour moves cannot change compatibility. The primary exhausts all 7000 word suffix/prefix tests and the potentially overlapping displacement box for this role allocation. The two local fundamental–conjugate singlets used above define each directional link creation term. This is the complete conditional algebraic construction; it does not select a rod configuration or imply rotationally invariant low-energy dynamics.
