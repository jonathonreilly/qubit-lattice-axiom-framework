# Independent potential-reconstruction diagnostic

This calculation uses only my own already frozen fourteen synthetic epochs and my recovered momentum quantities and candidate beta. I have not opened the author's potential/postprocess implementation or results. The derivation, source and resulting output were frozen in that order. No ODE was rerun, no threshold was changed or newly chosen for this diagnostic, and no empirical or observed-precision claim follows. Parent remains the scientific author.

The radial Jordan action gives omega=(1/q-3)/2 and

    3FH^2=rho+omega Fdot^2/(2F)+VJ-3H Fdot.

With g=F'/F, R=rhoJ0/(3H0^2 F), E=HJ/H0 and a=aJ/aJ0, this is the derivative-free readout

    vbar=VJ/(F H0^2)=E^2[3+3g-(1/q-3)g^2/4]-3R a^-3.

I insert recovered R,g,q, and the same saved expansion readout E, rather than the source R,g,q values. The absence of g' is useful here; it is the background 00 equation directly, with the action's radial omega(q) identification explicitly supplied. It does not select a potential independently of that action.

For the supplied candidate chart, k=(1-sqrt(4-12beta))/3, alpha=sqrt(beta), s=(1+k)/(k(1-3k)), and

    X=(beta/q-1)/[(1-3beta)s], u=ln(X)/(2alpha), T=1+sX,
    A^2=(1+s)X/T,
    U0=3/2+3s(X-1)^2/(2T^2), U1=(1+s)u^2/(2T^2).

Here beta is my independently fitted value from the momentum reconstruction, not its supplied truth. The conformal potential transformation supplies the decisive normalization:

    VJ=2Q Hv^2(U0+nu U1)/A^4, F=Q/A^2,
    (A^2/2)vbar=lambda U0+mu U1,
    lambda=(Hv/H0)^2, mu=lambda nu.

The factor 1/2 comes from the original action's potential normalization. The canonical field and Jordan-time conventions are those of the preceding frozen independent review.

A two-by-two solve at fixed protocol epochs 0 and 2 determines lambda and mu; nu=mu/lambda. Nothing from the source parameter truth enters that solve. The same pair is used at epochs 3,4,5,6. Epoch 1 is computed and retained but is neither calibration nor a declared reserved test. Source values are consulted only afterward for diagnostic errors.

| Case | Reconstructed (Hv/H0)^2 | Reconstructed nu | Absolute lambda error | Absolute nu error |
| --- | --- | --- | --- | --- |
| positive_roll | 0.7886707325594247 | 0.6999999900775549 | 9.3881e-12 | 9.9225e-9 |
| negative_roll | 0.7152287893155684 | 1.399999995673176 | 4.3321e-12 | 4.3269e-9 |

Both fitted lambda and nu are finite and positive. The largest absolute residual of lambda U0+mu U1 minus its independently reconstructed target at the declared later epochs is 1.1607e-12 for positive_roll and 5.1915e-13 for negative_roll. The respective largest target-relative residuals are 9.810e-13 and 4.839e-13. These are reported diagnostics, not a newly invented pass rule or an empirical test.

Conditioning must be kept with those numbers. The raw two-column matrix condition numbers are 976255.3 and 107337.1, with determinants 4.6163e-6 and 4.1969e-5. Normalizing each column to unit Euclidean norm still leaves condition numbers 393.26 and 34.77; the issue is not solely the small U1 unit scale. The source readout vbar differs from the source potential by at most 1.777e-15, but the reconstructed chart has maximum |delta u|=2.528e-10 and |delta A^2|=1.409e-11, inherited from finite-precision beta/q inference. Tiny potential residuals therefore do not imply equally accurate nu.

A separate closed two-by-two arithmetic expression on the same rounded matrix gives nu=0.6999999900619752 and 1.3999999956670248. This small solver-order difference is retained. It is not higher input precision, a high-precision trajectory, a fit to the source answer or a reason to alter tolerances. The weak basis separation and shared upstream inversion errors remain.

The full source contains no parent import, result read or numerical integration. It uses the same fourteen independently saved rows and fixed protocol. The original input result SHA256 is `9c43264dff6a2009ff93d90e297d1fc4fbacda865d8687c8cf75225f4f99c462`; `independent_potential_v1.py` is `5951e4c2bfb4e1b8f87945244554d21cf9b13283f163b115b00c52d5419adf07`. The original potential output is `02c4d58c9519db01d8b4c381092f71622b88375ca0c456a84d871837698cc504`, and its pre-parent-exposure result freeze is `3665ca0e8eac776f41c79655b8a897c49640bab1f7ac32be593ec62b9dbc1a88`. Empty stderr and unmodified stdout are retained alongside every row, matrix, coefficient and residual.

This reconstructs two parameters within the supplied U0+nu U1 family and supplied conformal normalization. It does not derive why that family or normalization is physical, establish a unique fundamental potential outside the visited radial interval, identify an absolute gravitational normalization, certify numerical trajectories, or resolve the previously reported pointwise zero-roll crossings. No formal audit, canonical-source verdict, external publication or parent-file change is performed. A correspondence comparison with author potential artifacts would be a separate post-exposure supplement.
