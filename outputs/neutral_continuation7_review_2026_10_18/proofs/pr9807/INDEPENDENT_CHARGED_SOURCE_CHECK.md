<!-- Original PR9807 source SHA256 db7242e165e086a940fe907c86714abc741f882fef78667f0bd93738eed08908. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent check: original whole-column charged source

The proposed leading pole amplitude and weight are correct in the matched canonical frame, for the isolated single-column charged branch described in the task. The statements about a uniform actual pole additionally use the previously established low-energy positivity embedding and the charged-sector isolation; they are not consequences of the dressing calculation alone.

## Exact charges and normalization

Let D_r be the product of X on the ten sites of one vertical column. It commutes with H0 and hence with the wall-count N. It commutes with every physical X plane. Its intersection with the relevant Y plane contains ten sites, so it also commutes with every Y plane. It intersects each horizontal Z plane once and anticommutes with each of them. Applied to an all-positive-plane ground, it therefore reaches X/Y positive and every Z-plane character negative, exactly as stated.

In the aligned-column representation it flips one logical column and creates the four plaquettes incident to that column. This is the odd-column-parity Q4 configuration with the shortest rectangle, 1 by 1. Adjacent logical pair flips move this single-column configuration to its neighbor, with the native coefficient -J gamma lambda^10.

The single-column images of the selected flat vacuum are orthonormal at distinct r on a sufficiently large torus: their difference flips two columns, which cannot be a nontrivial flat row/column pattern. Thus D_k=(1/R)sum_r exp(i k dot r)D_r creates a normalized leading Bloch state. This is the correct area normalization, without an extra factor of L or R. The sign of the momentum label follows the chosen translation convention but does not change the weight.

## Explicit second-order source dressing

Let S1 be the leading anti-Hermitian wall-elimination generator. Decompose S1=A+B where B is precisely the part odd under conjugation by D_r. D_r commutes with H0, so conjugation changes only the transverse Pauli signs and preserves the energy denominators. B contains the 2L incident y-directed YY bonds, with both transverse neighbors counted; x-directed XX bonds are unchanged. Each such bond takes a flat state to four vertical walls, energy cost 8J, and its generator amplitude has magnitude lambda/8.

Writing S1'=D_r S1 D_r=A-B,

e^(S1) D_r e^(-S1)=e^(S1)e^(-S1')D_r.

Its second-order coefficient is

[ (S1^2+S1'^2)/2-S1 S1']D_r
 = [2B^2+[A,B]]D_r.

Within N0, the mixed commutator has zero matrix elements: two distinct transverse bonds cannot return to N0 at this order, and the A and B sets have no identical bond. Each returning term in B^2 has the negative sign from anti-Hermiticity, giving

P0 B^2 P0=-(2L)(lambda/8)^2 P0.

Therefore

P0 e^S D_r e^-S P0
 =[1-L lambda^2/16]D_r+O(lambda^4)

at the asserted leading orders. The order-two generator contributes no additional P0 commutator in the off-block canonical gauge; D_r preserves N0. An arbitrary additional block-diagonal gauge would require corresponding state rotation and must not be inserted into this coefficient alone.

The sign has the expected interpretation: this is a reduction of the low-wall component of the original operator, not a renormalization of its microscopic norm to a number less than one. Some spectral weight goes to higher-wall states.

## Other state mixing and even powers

The flat vacuum's winding dressing starts at lambda^6 because the off-diagonal Hamiltonian begins at lambda^10 and its flux gap is lambda^4. The charged single-column branch's admixture of other Q4 shapes begins at lambda^4 under the stated lambda^6 shape separation. Neither creates a second-order competing amplitude. The latter's first admixture is orthogonal to the leading single-column Bloch source; the conservative O(lambda^4) remainder is sufficient without extracting its higher normalization correction.

The transverse checkerboard Z product sends H(lambda) to H(-lambda). Since L=10 is even, it commutes with D_r at both checkerboard colors. It preserves the relevant plane sectors. Its translation covariance differs at most by total physical Z, which is positive in both specified sectors for even L. Thus the corresponding momentum-resolved spectral weight is even in lambda. In a consistent analytic branch/frame there is no cubic term. The residue, unlike an eigenvector's arbitrary overall phase, is the invariant even quantity.

Consequently the pole weight is

[1-L lambda^2/16]^2+O(lambda^4)
 =1-L lambda^2/8+O(lambda^4).

For L=10 this is 1-(5/4)lambda^2+O(lambda^4). The amplitude can be chosen positive in the canonical real phase convention; the weight is phase independent.

## Actual-grid qualifications

For each fixed polynomial size exponent, sufficiently high local normal-form orders make the global tail smaller than the charged fibre gap and the lambda^2 correction being resolved. The local Fourier Gram argument, not the crude norm of the whole source, controls retained coefficients. Exact momentum restriction avoids using neighboring-momentum spacings as projector denominators. This is compatible with the earlier all-polynomial low-energy embedding, but requires the charged branch to be isolated in the stated symmetry fibre.

The operator changes plane charges. It is therefore not the neutral ZZ readout or a neutral scalar coupling. Its substantial leading residue does not replace the much smaller neutral-source residue, and it supplies no statistics, electromagnetic charge identification, or emission rate by itself.
