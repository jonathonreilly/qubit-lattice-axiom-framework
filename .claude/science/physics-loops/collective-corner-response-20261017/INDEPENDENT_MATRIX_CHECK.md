# Independent full-band staggered response check

Inputs inspected: `/private/tmp/scalar-environment-20261017/data/collective_corner_response/candidate.json` and `scripts/collective_corner_response.py`. Candidate provenance states PR9671 C19 head a96cefd1901938c6e4b6155a3576477d78ed6c87. I used the supplied numerical hopping/mass arrays directly, without importing the author's runner. This checks the conditioned response of those arrays; it does not independently establish their upstream extraction, flux choice, or physical identification.

Independent code `/private/tmp/collective-matrix-check.py`; output `/private/tmp/collective-matrix-check.json`. Eight grouped checks passed. No repository writes.

## Independent construction and quantitative result

At N=4 I selected exactly32 representatives of the64 momentum points, first momentum index0 or1, each paired with k+Q. I formed32 actual24×24 folded Hamiltonians

H_f(m)=[[H(k),mM],[mM,H(k+Q)]].

The grand potential per original cell is Ω(m)=−T/N³ sum_all_folded_eigenvalues log(1+exp[(mu−E)/T]). There is no additional factor2 here because only one representative per Q-pair is used. At T=.03, mu=−2.28284271247462:

- χ=−Ω''(0)=7.157298788740817 from independently summed spectral divided differences;
- five-point grand-potential derivatives:7.157298767177198,7.157298788600521,7.157298796284701 at steps .001,.0003,.0001;
- exactly degenerate static contribution1.0811934946903061;
- author's full-zone Kubo normalization and degenerate contribution agree to1e−10.

Thus the author's use of all64 pairs and a1/(2N³) folded-free-energy normalization is correct. The all-zone12-band Kubo sum has1/N³ with no extra half, also correct.

## Kubo signs and order of limits

For H=H0+mV, Ω''=sum_ij [(f(Ei)−f(Ej))/(Ei−Ej)]|Vij|². This is nonpositive. Hence χ=−Ω'' is positive; the author's (f_low−f_high)/(E_high−E_low) convention agrees.

At Ei=Ej the divided difference is f'(Ei)=−f(1−f)/T. Its positive contribution to χ is f(1−f)|Vij|²/T, including the complete degenerate block, not merely selected diagonal entries in an arbitrary eigenbasis. The author's construction includes that block and is basis-independent within it.

At a nonzero bosonic imaginary frequency the paired spectral terms acquire Δ²/(Δ²+ω²). Exactly degenerate terms vanish. Taking ω→0 through nonzero frequency gives χ_collisionless=χ_static−χ_degenerate for this finite collisionless model. This is not the equilibrium static susceptibility and does not include relaxation. The positivity and monotonicity checks are appropriate. A1e−9 degeneracy tolerance is a numerical implementation choice, not a physical broadening. Do not infer a continuum order-of-limits conclusion from these finite meshes alone.

## Four node states

The energy-window projectors select two states at each of the two valleys. The inter-valley projected mass vertex has singular values1.4040589577986065 and1.4040589577986051. The four folded node levels shift as ±mλ1,±mλ2. At mu equal to their common energy,

χ_node=(λ1²+λ2²)/(2TN³)=λ²/(TN³) when λ1=λ2=λ.

At N4,T.03 this is1.026761227590889, below the full degenerate contribution1.0811934946903061. Thus the node formula and the warning that it is not the entire degenerate contribution are both correct. This finite exactly sampled node contribution scales1/(TN³); it cannot be used alone as a thermodynamic instability argument. A shifted mesh need not contain the exact node.

## Conditional interaction threshold

If one separately postulates a static mean-field functional Ω(m)+m²/(2G), its quadratic coefficient is(1/G−χ)/2, so Gcrit=1/χ is the local curvature-change threshold for G>0. It does not establish a stable ordered phase, a global transition, or an autonomous scalar. Higher-order stability, an actual microscopic interaction and its derivation, fluctuations, dynamics, ensemble and finite-size limits remain additional obligations. Checked the author's selected result row16 really is N12,half-shift,T.03.

No material mathematical flaw found in these conditioned calculations. The choice of vertex normalization, hopping coefficients, chemical potential, temperature and hypothetical interaction remain supplied development inputs. The source M is not a derived scalar field, nor a universal conformal coupling. If the upstream identification is a pseudoscalar Dirac mass, a further symmetry/physical bridge is needed before identifying its collective variable with the cosmological conformal scalar.
