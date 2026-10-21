<!-- Original PR9809 source SHA256 d6b4fa93a58a9b739bbb5e1a0f91261ae83fd5fe1243d937323db78bb66132a9. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native six-layer neutral bound mode

Status: conditional-support. The native coefficient pole and source are derived; the supplied Hamiltonian, six-layer geometry, weak anisotropy and selected symmetry-sector vacuum are premises. No observed scalar, universal force, or three-dimensional field is identified.

Throughout, omega denotes excitation energy; writing it as angular frequency uses the convention hbar=1. No physical unit scale is fitted.

## 1. Microscopic setting and state

Use H=-J sum_z ZZ-Jlambda(sum_x XX+sum_y YY), one physical qubit per site, on an even R by R by 6 periodic grid, R>=8. Column Pauli operators act on aligned columns. P_p is the product of four column Z operators around a transverse plaquette; E_e is a nearest-column X pair. Restrict to the compatible exact + sectors of X on x-normal planes, Y on y-normal planes, and Z on z-normal planes. In the wall-free block these select uniform row/column-flip orbits and even column parity. Use the lowest vacuum in this specified sector; it has NOT been proved to be the global ground across all symmetry sectors. The uniform original bond readout further selects transverse momentum zero and the even square-rotation representation.

Within this sector the flat-plaquette subspace has one vector g0, the normalized uniform flat orbit. This state choice introduces no interaction, but remains an explicit preparation premise. All changes of effective frame require matching dressed state and readout.

## 2. Sixth-order native coefficients

In units J, omitting scalar terms, the wall-free block through sixth order is

 H_b/J = -(3/64)lambda^4 sum_p P_p
          +lambda^6[-(25/3072)sum_p P_p
                    -(18/8192)sum_<p,q> P_p P_q
                    -(63/8192)sum_e E_e] + higher orders.       (1)

Here <p,q> runs over nearest plaquette pairs once. The fourth-order and first column-winding terms were derived in WHOLE_COLUMN_MODE_PROOF.md. The winding coefficient is binomial(10,5)/8^5=63/8192.

For the diagonal sixth order, each layer's transverse edge word must have even spin incidence. Modulo repeated edges, a word of length at most six is empty, a four-edge plaquette, or a six-edge 1 by 2 rectangle. Transverse periods greater than six exclude short wraps. Empty words are background scalars. Plaquette plus a doubled edge renormalizes sum P. A rectangle contributes the product of its two adjacent plaquettes. Denominators depend on broken vertical bonds, not on aligned background signs. No other diagonal background invariant occurs at this order. Height-six column winding is off-diagonal and is the last term of (1).

The 720 rectangle orderings give -3/8192 per longitudinal layer, with no proper return to the wall-free block. Folded terms cannot produce a rectangle at order six because lower nonconstant diagonal words require four insertions. Thus its total coefficient is -18/8192.

For a fixed plaquette and a repeated bond b, the sixth-order connected coefficient is the raw six-word sum plus 7/16384. Specifically E2_b=-1/8, the plaquette E4=-1/128, the sum of the three squared-resolvent four-word insertions is 5/2048, and <VR²V>_b=1/64. The folded contribution is -E2_b(5/2048)-E4(1/64)=7/16384. Exact repeated-word multiplicities matter when b is itself a plaquette edge. Summing incident bonds gives 7/2048 at the plaquette layer and -11/4608 at each neighboring layer. Separated layers cancel. Their sum is -25/18432 per layer, giving -25/3072 at height six. An independent multivariate Rayleigh-Schrödinger recursion reproduces these subtotals without using the folded formula.

## 3. Exact four-defect dynamics

Four bad plaquettes must be rectangle corners: each row and column has even bad-plaquette count. In the positive column-parity sector the rectangle area ab is even. On the infinite plane this follows by filling the rectangle with column flips; on the even torus the row/column kernel also preserves parity.

An x-edge E has a 2 by 1 syndrome, and a y-edge E a 1 by 2 syndrome. A move remains in the four-defect subspace exactly when it shares two corners with the current rectangle. Equal syndromes annihilate to the vacuum and are excluded from this first projected coefficient. Other overlaps leave this subspace and contribute only at higher order.

The edge-source component has center C=(2,2), two arms (a,2), a>=3 and (2,b), b>=3, and two arms (2n,1), n>=1 and (1,2n), n>=1. Their first sites are A=(2,1), B=(1,2). All other even-area rectangles are immobile at this order and not source-connected. Each relative move has two physical realizations. At zero center-of-mass momentum their amplitudes add.

Four isolated bad plaquettes have rectangle-interaction cost 32b6, b6=18/8192. A thin rectangle has two neighboring bad pairs, reducing this by 8b6. Including the single-plaquette renormalization gives the common reference 13/96. Set t=2gamma6=63/4096. Relative to that reference, divide the four-defect coefficient by t: the graph is a four-arm star with hopping -1, center onsite zero, two arms onsite zero and two onsite -w, where w=8b6/t=8/7. No graph coupling or potential has been selected independently of (1).

## 4. Isolated coefficient mode and readout

The endpoint Green function of an arm with onsite d is g_d(x)=[x-d-sqrt((x-d)^2-4)]/2 above its band. The center equation is

 x=2g_0(x)+2g_-w(x).

Above the common top edge 2 the left-minus-right function increases strictly from a negative value to infinity, so there is exactly one bound state. Its root is

 x_star=2.114475316300649...,
 147x^4+448x^3-528x²-1792x-1024=0.

The polynomial alone does not select the root; the Green equation and x>2 do. There is no lower bound state at w=8/7: the lower-state condition w<2sqrt(2)-2 fails.

Let eta_h=.714088323587102..., eta_l=.343149334563223... be the positive decay magnitudes on the high and low arms. Wave amplitudes are u(-eta_s)^n, n>=1. Normalization gives

 u²=[1+2eta_h²/(1-eta_h²)+2eta_l²/(1-eta_l²)]^-1
    =.298693004501705... .

For the unnormalized source A+B the pole weight is W=4eta_l²u²=.140686156430488... . It is about 7.0343 percent of that source's total norm squared 2. This is a repulsively bound state above the continuum, not a claim that the lowest neutral response is a pole.

## 5. Periodic finite-array control

For even R>=8, quotient the exact four-defect syndrome basis by translations and the + row/column background orbit. Shapes satisfy 1<=a,b<=R/2, ab even. A shape's translation orbit has size n_ab=(R if a<R/2 else R/2)(R if b<R/2 else R/2). If k_ab,cd moves from a representative reach shape cd, the normalized hopping is -gamma6 k_ab,cd sqrt(n_ab/n_cd). Self-transitions and folded terminal bonds are retained. The native source T g0/R is exactly A+B.

The source component is the same star with finite folded arms. Removing its center leaves path operators with spectral top at most 2 in the above units; the thin arms have top at most 2-w. The two high-arm endpoint Green functions at 2 equal 1 by their terminal sqrt(2) continued fraction. Thus the center Schur function is negative at 2 and has exactly one root above 2. Interlacing excludes a second such root. Its source overlap is nonzero. The arm resolvents converge exponentially outside their bands to the infinite-arm Green functions, so x_R and the source weight converge to x_star and W. Exact syndrome enumeration independently checked R8,10,12; the reduced runner checks R through120. These numerical checks corroborate, rather than replace, the finite-arm argument.

## 6. Original microscopic readout and prepared heavy vertex

Use the same original normalized bond readout C as LIGHT_COLUMN_WINDOW_PROOF.md. Its centered four-defect vector includes the ground-mixing subtraction. At L=6, A6=40/3, so

 C g = -(11/3) gamma6 lambda^6 T g0/sqrt(6R²) + higher orders
     = -11 gamma6 lambda^6 (A+B)/(3sqrt6) + higher orders.

Therefore the pole's original-readout weight, in the fixed-size weak-coupling coefficient limit followed by increasing R, is

 gamma6² (121/54) W lambda^12
   =1.86442186268e-5 lambda^12 .                         (2)

It is not an arbitrarily normalized new scalar source. Its frequency coefficient is

 omega/J = (3/8)lambda^4
          +[13/96+(63/4096)x_star]lambda^6+o(lambda^6),

with sixth-order coefficient .167939114158596... . The separation above the four-defect continuum at zero momentum is .001760728741929... Jlambda^6 at this coefficient limit. State and readout must be dressed together.

The all-height canonical prepared heavy hop also gives a direct connection: at L6 its x-edge background-changing vertex is -Jlambda^5 E_e/16. For a single local edge, the normalized zero-momentum pole overlap of E_e g0 is -eta_l u/R. Hence its squared projected prepared vertex is J²lambda^10 W/(1024R²) at leading order. The volume factor is essential. This is a prepared background-channel matrix element, not a relaxed-heavy scattering amplitude, emission rate or universal mass coupling.

## 7. Dispersion and limits

At small transverse momentum the two high-arm hoppings are cos(qx/2), cos(qy/2); low-arm outward hoppings are cos(qx), cos(qy). Center-to-low-x and center-to-low-y links are cos(qy/2), cos(qx/2). The derived branch is

 omega(q)-omega(0) = -(63/4096) .1481097616... Jlambda^6
                     (qx²+qy²)+O(Jlambda^6 |q|^4)

at coefficient order. It is square-rotation even and planar, but has negative curvature near zero momentum. This does not supply a positive-gradient relativistic scalar. The branch merges with its continuum farther from zero. No longitudinal propagation, global ground selection, cosmological field, physical scale or empirical success is inferred. All calculations are exposed model development.

## 8. Actual microscopic transfer in a logarithmically growing box

Choose even R comparable to c log(1/lambda), any fixed c>0. There is a dimension-independent polynomial remainder argument. At fixed height six the perturbation norm is O(R²), while the unperturbed N0 spectral cluster has an order-J gap. A Riesz contour around it has bounded resolvent norm independent of Hilbert-space dimension. Its resolvent expansion bounds every fixed-order coefficient and remainder by a fixed polynomial in R. The normalized original C has norm O(R), adding only a polynomial factor. The same fixed-order canonical gauge as (1) and the inherited readout must be retained: one can complete that finite-order construction with an exact block identification at higher order. A different intra-block gauge cannot be inserted silently.

After subtracting scalar energy and dividing by lambda^4, D4 has a fixed gap between flux-count clusters. Reducing those clusters gives the four-defect operator with remainder O(Jlambda^7 poly(R))+O(Jlambda^8 poly(R)). The latter is the D6 inter-cluster correction (lambda^6)^2/lambda^4. The upper D6 eigenvalue is separated from the entire other four-defect spectrum by a positive constant for large R, as proved by the finite-arm argument. Its projector error is therefore O(lambda poly(R)). All these errors vanish at the required relative order along logarithmic R; no exponential dimension factor is used.

Source control is separate from energy control. Use an exact N0 block identification or an off-block completion beyond sixth order. The source is scalar through orders below four on N0, and its lower nonconstant term is diagonal in flux. Perform the centering and ground/excited block-mixing cancellation before estimating the remainder. The explicit sixth-order P0-to-P4 vector in section6 then has error O(lambda^7 poly(R)). Projecting this small vector onto the D6 mode adds only another O(lambda^7 poly(R)); multiplying raw ||C|| by a projector error would be invalid. Thus (2) holds with relative o(1) error along the stated logarithmic-volume family.

Consequently the selected exact symmetry fibre of the actual finite microscopic Hamiltonian has a simple isolated mode with the frequency and positive original-readout atom above, along that joint family. The finite-arm root/residue converge exponentially, and their limits give the quoted coefficients. This proves neither a fixed-lambda thermodynamic pole nor that the selected vacuum is the global ground. Momentum fibres outside the uniform readout sector may have different energies; isolation is asserted in the specified fibre.
