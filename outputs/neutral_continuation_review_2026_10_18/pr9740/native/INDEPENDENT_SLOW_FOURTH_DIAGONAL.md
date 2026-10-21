# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused check: fourth-order axial-interval diagonal

The canonical formula, exact rational implementation, and finite values check. A connected-word argument extends the affine dependence to every ell>=3 in the same uniform-reference geometry; the intercept still comes from the exact finite endpoint calculation, not an independent second enumeration.

## Canonical expression and implementation

Let R=Q/(E0-H0), and suppose PVP|a>=0. In the diagonal canonical fourth-order coefficient, every term with an outer K1 annihilates |a> or its bra. The remaining expression is

<a|V R V R V R V|a>
- (1/2)<a|{P V R^2 V P, P V R V P}|a>.

For real matrix elements, define B_s=<s|V R V|a> and A_s=<s|V R^2 V|a>. The diagonal becomes

sum_(s in Q) B_s^2/(E0-E_s) - sum_(s in P) A_s B_s.

This is exactly the formula in the script. Its integer B and A accumulators represent 8B_s and 64A_s respectively, explaining the divisors 64 and 512. Coincident two-edge XOR masks are aggregated before squaring, as required. The zero mask includes repeated identical-edge paths. The first-step costs are indeed only 4 or 8 for these slow axial configurations, so the integer divisions are exact. The vacuum calculation uses its own E0=0 and the same geometry; subtraction removes the extensive vacuum term.

The energy routine correctly counts longitudinal domain walls, excludes artificial links between adjacent encoded columns, and adds the two fixed-up exterior end bonds. K1|a>=0 is essential for this simplified K4 formula; it must not be reused unchanged for the adjacent fast arm.

## Why sufficiently long intervals have an exactly affine diagonal

A diagonal four-V word must flip each physical bit an even number of times. Since V bonds lie in transverse layers, its bond multigraph is Eulerian separately at each longitudinal layer. With four factors on the square lattice, the possibilities are:

1. One edge used four times.
2. Two edges each used twice.
3. Four distinct edges around one transverse elementary square.

For two edges with independent H0 energy changes c,d, the disconnected contribution cancels exactly. The intermediate two-edge state contributes -(c+d)/(c^2 d^2), while the cross term of the zero-mask fold contributes +(c+d)/(c^2 d^2). This cancellation includes arbitrary separation. Here c,d are positive, so no additional P intermediate invalidates this calculation.

Dependence between two repeated edges is possible only if they overlap or interact through a longitudinal H0 bond. Thus a surviving cluster occupies one longitudinal layer, or two adjacent layers; its energy denominators inspect at most the nearest longitudinal neighbors of those layers. No surviving cluster can touch both interval boundaries when ell>=3. Each endpoint contribution is then independent of ell, while extending the interior by one layer repeats the same bulk contribution. The vacuum-subtracted diagonal is therefore exactly affine for all ell>=3. This is a locality/cancellation argument, not an extrapolation from five lengths.

## Independent interior slope

Inside a long interval, the aligned signs of each whole column can be reversed without changing the denominators of repeated-edge diagrams. Their four Pauli factors multiply to a state-independent scalar, so they have no bulk dependence on the column-sign pattern. The only pattern-dependent four-factor word is the transverse square loop, proportional to the four-corner Z parity.

An independent enumeration of all 24 orders around one square, with each flipped spin costing four, gives -1/128 for even corner parity and +1/128 for odd corner parity. Thus the bulk fourth-order term is -P_square/128 per layer. The two columns at axial distance two share no elementary square. Reversing their signs changes eight square parities per layer; each costs 2/128, yielding slope 8*(2/128)=1/8.

The supplied exact ell=3 result is 101/192. Subtracting 3/8 gives the endpoint constant 29/192. Combined with the connected-support argument, this establishes

K4_diag(excess,ell)=ell/8+29/192, ell>=3,

within the stated canonical coefficient and uniform-reference setup. The additional exact results 125/192,149/192,173/192,221/192 at ell=4,5,6,8 are consistency checks, not the basis for the all-length inference.

## Geometry and scope

The initial columns have transverse margins of two, sufficient for all changed square loops and connected repeated-edge clusters. Longitudinal margin three contains their endpoint neighborhoods and the external-spin energy checks. Omitted exterior transverse clusters are identical in state and vacuum and cancel. This geometry is therefore adequate for this local excess coefficient.

This result identifies the diagonal native string tension at order four. It does not compute the complete K4 operator, its endpoint off-diagonals, induced virtual K3 terms, a selected background, or a native resonance. In particular the intercept is an exact diagonal coefficient, not yet the entire physical mass correction after channel mixing.
