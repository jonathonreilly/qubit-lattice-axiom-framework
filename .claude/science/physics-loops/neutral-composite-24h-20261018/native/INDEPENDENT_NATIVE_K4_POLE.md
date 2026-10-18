# Focused corrected-fast / long-slow K4 pole check

Checked 2026-10-18. Read the canonical note, native/neutral_native_order4_pole.py/json, the independent long-row kernel report, and imported host/fast-boundary routines. This check reuses the earlier independently checked host/Schur algebra and the separately reviewed corrected-arm strip lemma. No expensive pole grid was replayed, and no parent files were changed.

## Exact coefficient arithmetic

The long-row K4 symbol excluding its linear tension is

    s(k)=29/192+(19/16) cos k-(13/64) cos(2k).

Thus s(0)=109/96 and s(k)=109/96-(3/16)k^2+O(k^4). This is its value at the leading K2 band bottom, not the minimum of the isolated K4 symbol. The earlier independent local-wall enumeration supports the hopping coefficients and long-interval extension (ell>=5); the earlier diagonal check supports ell/8+29/192. These do not establish the full short-interval K4 matrix.

For a=-0.2796521330954-0.4544316488004i,

    109/96+(2+Re a)/8 = 1.35046015002974,
    -Im a/4 = 0.1136079122001.

Both reported numbers and the retarded width sign Gamma=-2 Im E are correct.

## Airy power counting and its scope

Write f=lambda^2/8 and n=ell-2>=1. The uncorrected slow-arm potential is f(n+2), explaining the offset f(2+a), rather than f(1+a). The leading spatial scale is f^(-1/3). The K4 constant shifts the slow-unit energy by the real amount lambda^2*109/96. Its kinetic correction is O(lambda^2 f^(2/3)); multiplied by the physical Jz lambda^2 this is O(Jz lambda^(16/3)), smaller than lambda^4. Changes of finite boundary matrix entries of size O(lambda^2) ordinarily change the scattering length by O(lambda^2), giving pole changes O(f lambda^2) in slow units, hence O(Jz lambda^6). This statement requires a nonsingular boundary matching problem and controlled continued-channel resolvent; it is not a bound on arbitrary omitted native channels.

The range-two kinetic recurrence also has an additional short decay root. For small lambda its boundary effect is perturbative, rather than a new near-threshold root, provided that the same nonsingularity condition is checked. The real bulk shift changes the host energy by O(lambda^2); host Green functions are smooth near the slow energy -2, so this alters a only subleadingly. The previously checked fast Schur correction is O(lambda/log(1/lambda)) at the boundary and gives the smaller physical displacement O(Jz lambda^5/log(1/lambda)).

Consequently the displayed lambda^4 real and imaginary coefficients are consistent asymptotic predictions for the specified completed coefficient model. The imaginary coefficient is unchanged at leading order because the added bulk coefficients are real and their changes of the kinetic/boundary matching data vanish as lambda->0.

A formal power count alone is not a uniform complex Airy theorem for the perturbed range-two recurrence. To promote the displayed little-o remainder to a proved model theorem, establish a uniform turning-point/matching expansion on the complex pole contour after the real bulk shift, including the extra decay root, or an equivalent controlled comparison. The note's phrase 'asymptotic prediction' and its explicit warning that the finite calculations do not certify the remainder are therefore important and should remain. No full-native pole follows.

## Numerical model audit

The script's diagonal f*(arange(N)+3)+lambda^2*29/192 starts at ell=3. Its nearest hopping is -1+19lambda^2/32 and next-nearest hopping -13lambda^2/128. The baseline -4 is external: physical energy is 8Jz+Jz lambda^2*(e-4), where the root variable e is near -2. Thus its subtraction used to extract the real lambda^4 coefficient is correct.

The slow host input host(e) uses the matching shifted energy. Fast input lambda*(e-4) is likewise correct. The rectangular coupling V has columns -d2-e1 and -2e1, as specified. M=V.T R V and G=(I-g lambda M)^(-1)g implement the stated finite-rank correction without assuming invertibility of g itself. The tail Schur complement retains the next-neighbor boundary bond in its first row and column, and subtracts the effective host G_AA once. No missing hopping factor was found.

Applying the long-row diagonal and hopping coefficients all the way to ell=3 is a particular short-boundary completion of the model. It is not a claim that every native ell=3/4 K4 entry has been derived. Native short-boundary and other-channel limitations remain material.

The five stored values and residuals match the note. A nonlinear scalar root residual is a determinant-equation check, not a microscopic eigenvector residual. In particular, the 3.53e-10 value at lambda=.05 is an absolute equation residual, not a rigorous pole-error enclosure without a derivative bound.

One additional asymptotic qualification: N=int(20*f^(-1/3)) holds the scaled far endpoint near 20. Its Airy-tail error is exponentially tiny for the displayed finite runs, but its scaled coefficient does not go to zero as lambda->0. Strictly, that fixed-scaled-cutoff sequence is not sufficient to demonstrate an o(lambda^2) error in slow units at arbitrarily small lambda. Use the infinite arm, or let N*f^(1/3) grow slowly to infinity with sufficient tail control, in a proof. This does not invalidate the reported finite numerical comparisons.

## Conclusion

No sign, coefficient, indexing, or Schur-complement error found. The 1.35046015003 real coefficient and 0.11360791220 width coefficient are correct conditional model predictions. Keep the prediction/theorem distinction, the native boundary omissions, and the full Schrieffer-Wolff remainder limitation explicit. This block does not derive a preparation, observed scale, detector map, universal coupling, or cosmological scalar.
