> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Inhomogeneous finite compass attachment — proposed strengthening

Status: ROOT-authored proposal; distinct check requested. This is a conditional positive construction, not a general robustness or native-supply claim.

## Model and exact local accounting

Use the literal K=2I+Z1Z2 and W=exp(i theta) exp(i theta X1X2), cos(theta)=3/5, sin(theta)=4/5. Use the accepted interior geometry and any containing finite open rectangular box. Every directional nearest-neighbor edge e carries its own positive block j_e(I-sigma_u^a sigma_v^a). All edges remain installed. No coefficient equality between distinct edges is imposed.

Denote the old x coefficient J0, the immediately adjacent exterior x coefficients JL,JR, and g=JL+JR. Let b be the sum of coefficients of the eight old/E transverse edges (four y, four z). Let c be the sum of coefficients of the eight E/E transverse edges incident on L,R (four y, four z). Let HE be the actual isolated E-only block sum. Let HEref omit only these latter eight E/E transverse blocks. Every retained term touching L or R is an x term, so [HEref,XL]=[HEref,XR]=0 for arbitrary coefficients. No norm estimate on all of HE is needed.

Define

    H4 = K + (JL+J0+JR)I - JL XLX1 - J0 X1X2 - JR X2XR.

The installed Hamiltonian is exactly

    H = H4 + HEref + (b+c)I + V,
    ||V|| <= b+c,
    HE = HEref + cI - BE,  ||BE|| <= c.

Here V contains exactly the sixteen transverse signed Pauli terms touching S={L,1,2,R}; BE contains the eight E/E ones. They need not commute. The final phase scalar, after restoring the actual environment, is JL+J0+JR+b. Identity coefficients are accounted for term by term; actual environment coefficients outside these sets occur unchanged in both H and HE.

## Full-space bound

Decompose H4 by XL=a,XR=d and X1X2=p, with signs a,d,p. On the old two-dimensional p sector use Z=Z1Z2 and Xprime=X1. Then

    H4_sector=(2+JL+J0+JR-J0*p)I + Z - q Xprime,
    q=JL*a+JR*d*p,  |q|<=g.

The exact Pauli axis/frequency estimate from the accepted homogeneous argument applies for every real q:

    ||exp[-it(Z-qXprime)]-exp(-itZ)|| <= |q|+q^2*t/2, t>=0.

Taking the maximum over all sectors and paying the XX angle mismatch gives g+g^2*t/2+|J0*t-theta|. Commutation with HEref allows exact factorization. Duhamel pays (b+c)t for the sixteen physical transverse terms and ct to replace the comparison environment by the actual HE. Hence the proposed full-space statement is

    ||exp(-itH)-T(t)|| <= g+g^2*t/2+|J0*t-theta|+(b+2c)t,
    T(t)=exp[-i((JL+J0+JR+b)t+theta)] exp(-itK)W tensor exp(-itHE).

This is uniform over every joint old/environment/passive-reference state. The corresponding unhalved joint channel distance is at most twice the displayed bound. Product targets require initial independence across the old/reference versus E split; arbitrary correlations are retained in the joint comparator. No reset or input-state preparation is inferred.

## Explicit independent-coefficient sufficient policy

For 0<epsilon<=1 choose a nominal J>0 and

    J0 in [J(1-eta),J(1+eta)],
    0<JL,JR<=2J,
    J<=epsilon/[512(theta+1)],
    0<=eta<=epsilon/[64(theta+1)],
    b+2c<=epsilon*J/[64(theta+1)],
    |t-theta/J|<=epsilon/(64J).

Thus Jt<theta+1 and g<=4J. The four costs obey respectively

    g < epsilon/128,
    g^2*t/2 < epsilon/64,
    |J0*t-theta| <= J|t-theta/J|+eta*Jt < epsilon/32,
    (b+2c)t < epsilon/64.

Their sum is <9epsilon/128<epsilon/8; the unhalved full channel error is <9epsilon/64<epsilon/4. In particular the center time uses the nominal J, not a fitted actual J0. The phase in T(t) is the exact input-independent phase for the actual coefficients; this is not a phase guarantee relative to an unknown nominal apparatus phase.

The old incident cap is bounded by 3+2(J0+max(JL,JR)+b), which is <3+8J under this policy. Thus imposing additionally J<=(Lambda-3)/8 for Lambda>3 suffices at the old sites. All other site incident sums must separately obey the chosen cap; arbitrary remote coefficients means arbitrary values consistent with this physical cap, not unbounded hardware resources. Feasibility follows, for example, by choosing every remaining x coefficient <=J and every transverse coefficient positive and sufficiently small. Strong remote transverse coefficients are also allowed if their local caps hold; only the sixteen specified near-S transverse edges enter the error certificate.

The original Q-qubit, M-edge inventory remains Q physical qubits and M+1 positive blocks, degree at most six. No coefficient equality, extensive error penalty or exact homogeneity away from S is needed. The small local coefficients, their directional matrix form, fixed given K and observation time are still supplied. Errors changing the Pauli directions, K, graph, positivity or the all-state comparison have not been covered. The policy is sufficient, not optimal and not an empirical fabrication specification.

## Evidence and exposure

This derivation adapts the fully read accepted interior source 1d27903b2dbe3041bc76f8cf52085dc59a6bf0d3463a65c377e166f82a416af8, actual-environment addendum ab9a2d00dbf10754235adad790a6ba0d6bd67fd273aab1a7a5f0ab96a273d08f and distinct review b5bbc7a528244cd95ad4efa55b6ca4ac63584ea0dfd35e785ff1818b180b91d4. The exact signed-sector argument is reproduced above. ROOT proposed the inhomogeneous extension and policy; the assigned checker is source-exposed, same-model, with shared campaign ancestry. Until the completed check is read, this note remains proposed. No scientific executable, retained audit, physical experiment or new microscopic identification is claimed.
