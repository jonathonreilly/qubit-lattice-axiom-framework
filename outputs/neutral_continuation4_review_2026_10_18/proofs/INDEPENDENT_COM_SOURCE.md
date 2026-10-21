<!-- Owning original: PR9764; source SHA256 758fcec916e6d1f83d7bdc60b87b6b93c50a0ef557a298fbee10f6d5beecdecc. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Native original-readout longitudinal Fourier factor

Take C_p=V^(-1/2) sum_(r,j) exp[ip(j+1)] Z_(r,j)Z_(r,j+2), with the bond-center phase stated in the request, and the aligned all-up reference. C_p dagger=C_-p. The calculation below is a dressing of this existing observable by the supplied Hamiltonian, not an introduced detector coupling. Longitudinal boundaries must be absent or sufficiently far away for the bulk counting.

## One-layer pair flip: exact first-order source

One flipped spin at layer z changes exactly the distance-two bonds starting at z-2 and z. Their centers are z-1 and z+1, and each ZZ eigenvalue changes by -2. Thus its readout change is -4 exp(ipz)cos p/sqrt(V). Two distinct columns flipped at that layer give

Delta C_p=-8 exp(ipz)cos p/sqrt(V).

The intermediate state is the native E8 four-wall state, with excitation denominator 8Jz. Write H/Jz=H0+lambda V1. The first ground-state correction is -lambda V1|vac>/8. Acting with the connected readout gives

s_p^(1)=lambda cos p/sqrt(V) sum_(native transverse pair flips at z) exp(ipz) <pair|V1|vac> |pair>.

Thus the source is exactly the p-fiber version of the original zero-momentum first-order source, multiplied by cos p. XX and YY have their native relative signs: V1 matrix elements from all-up are -1 for XX and +1 for YY. These generate the same transverse scalar/d-wave combination as previously, not a newly chosen source. Reversing the Fourier convention changes p to -p but not the real cos p factor.

There is no additional factor from center coordinates: a one-layer interval has center z. A leading squared source norm or residue factor from this piece alone is multiplied by cos^2 p relative to the correspondingly normalized fiber source. Its absolute numerical normalization still depends on the existing per-site/per-rung convention. Near p=0 the factor is nonzero. The zero at p=pi/2 only cancels this first-order contribution; it is not an all-orders darkness result.

## Two-layer adjacent interval: useful second-order component

For a two-layer interval [z,z+1], the changed distance-two bonds in each column have centers z-1,z,z+1,z+2. For the two columns together,

Delta C_p=-4 sum_(h=-1)^2 exp[ip(z+h)]/sqrt(V)
          =-16 exp[ip(z+1/2)] cos p cos(p/2)/sqrt(V).

In the canonical orthogonal ground/E8 block dressing, let P denote E8 and H1=P V1 P. The E8 component of the second ground correction is H1 V1|vac>/64. Orthogonality supplies the compensating vacuum-readout term from the second band correction. The cross term between first band and first ground corrections vanishes because the first band correction is outside P whereas the first ground correction lies in P, and this readout is diagonal in spin configurations. Therefore the second-order source is the diagonal readout difference applied to H1 V1|vac>/64.

Restricting this statement to its adjacent two-layer component yields the zero-momentum component multiplied by cos p cos(p/2), with the center phase exp[ip(z+1/2)]. Equivalently this component can be written -lambda^2 cos p times the corresponding length-changing H1(p) action on the normalized one-layer source, divided by four, because H1(p) itself supplies the cos(p/2) factor. This equivalence concerns the two-layer component only.

In the bulk model H1 V1|vac> can also contain same-layer separated-column states, unlike a pure single-arm truncation. Their readout change remains the one-layer -8 cos p factor, so the complete second-order source cannot be inferred solely from the two-layer formula. Nor does this check establish the final outgoing slow-pole residue: direct slow-source pieces and fast-sector dressing must be combined in the same gauge and normalization.

The first-order cos p factor and the two-layer component are exact local geometric consequences of the specified microscopic readout. Reference-state selection, full native pole transfer, and physical measurement identification remain separate issues.
