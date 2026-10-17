# A concrete open-band inverse bound for the attached gate load

Status: root-authored candidate with one exact symbolic calculation, requiring distinct checking. This supplies an actual local-load inverse bound, not the whole attached emitter inverse, spectral mass or runtime.

Sources are record_attached_kernel/PROPOSAL.md fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457 (attachment still under separate check), and record_gate_closed_spectrum/PROPOSAL.md9450be53 with independent check0fac60ea. Keep their 24-site h_x, input p, output o and scalar subtraction exactly. Define D2(q)=E(q)-h_x+j exp(iq)(P_p+P_o), and D1(q)=E(q)-h_x+j exp(iq)P_o. D1 is D_x^R in the attachment proposal, with the input bond diagonal retained and only the output lead eliminated. It is not a global inverse.

At q0=pi/2, scale j to1. The checked simultaneous rotation of both lead coordinates also rotates the two port coordinates of the compressed 24-site matrix; equal two-port selfenergies i preserve that rotation. D2 becomes the direct sum of two 12-site tridiagonal matrices, n=0 terminal through n=10 arm end, n=11 port. Their diagonal is -x at n0, i at n11, zero elsewhere except phase-cell endpoints -1 on arm1. Offdiagonal entries are +1, except +sqrt2 on bonds n2--3 and n5--6 of arm1. This is the actual E-h sign convention.

The included check.py performs exact symbolic inversion of these four matrices (both arms and x=±1), verifies D R=I entry by entry, and computes exact Frobenius and port-column squared norms. RESULT.json records the sole execution (SymPy1.14.0); no numerical approximation, dynamics simulation or sweep ran. The data are:

x=+1: arm0 ||R||_F²=72, ||R e11||²=6, R11,11=(1-i)/2;
       arm1 ||R||_F²=159/2, ||R e11||²=13/2, R11,11=(-1-i)/2.
x=-1: arm0 ||R||_F²=72, ||R e11||²=6, R11,11=(-1-i)/2;
       arm1 ||R||_F²=129/2, ||R e11||²=11/2, R11,11=(1-i)/2.

The physical input port is an equal superposition of the two rotated ports. Therefore with R2=D2(q0)^(-1), its diagonal entry g2=-i/(2j), full Frobenius norm at most sqrt(303/2)/j, and ||R2 e_p||² at most25/(4j²). Since D2 is complex symmetric, the input ROW has the same Euclidean norm as this column. This equality is transpose symmetry, not an erroneous Hermitian-column identification.

D1=D2-i j P_p. Exact Sherman--Morrison gives

 R1=R2 + (i j)/(1-i j g2) R2 e_p e_p^T R2
    =R2+2i j R2 e_p e_p^T R2.

The denominator is exactly1/2 in both sectors. Hence

 ||R1|| <= [sqrt(303/2)+25/2]/j <25/j,

since sqrt(303/2)<25/2. This pays the norm of the rank-one update with the input row/column norms, not with a squared whole-matrix norm.

For REAL q with u=|q-pi/2|, |E(q)-2j|<=2ju and |exp(iq)-i|<=u. Thus ||D1(q)-D1(q0)||<=3ju. Neumann inversion gives

 ||D1(q)^(-1)|| < (25/j)/(1-75u) <26/j

through the entire selected u<=4e-6 band (indeed75u<=0.0003). This proves an actual uniform open-load inverse margin, including all 24 local head coordinates in both record sectors. It does not derive a complex-contour or whole-source inverse estimate; those require their own perturbation domains.

The isolated gate recovery from its core boundary a is -j D1(q)^(-1)e_p. Consequently its norm into ALL24 gate sites is <26 on the selected open channel. For the inherited real CLOSED channels, the attachment proposal's independent row bound, if checked with |s|<1/60, gives ||D1^(-1)||<1/(56j), so a direct sum over the orthogonal B spectral fibers has open-plus-closed recovery norm<26. This last full-fiber application remains conditional on that attachment closed-gap check; no four/eight-column maximum shortcut is used. The closed downstream tail excluding the port has norm <=a/sqrt(1-a²) times its port amplitude in each orthogonal channel, with a<1/60, and must be counted separately in a full output contract.

This result removes one explicit auxiliary open-load pole concern for the frozen geometry. It leaves source feedback, actual seed spectral regularity, all-time branch profile and normalized early-time correctness unresolved. Root authored this calculation after reading the local gate and attachment sources. A separate reviewer must check the chain coordinates, exact symbolic data, input-port transformation, rank-one sign, and perturbation constants before downstream use. No science Git branch, axioms, editable prompts or audit status changed.
