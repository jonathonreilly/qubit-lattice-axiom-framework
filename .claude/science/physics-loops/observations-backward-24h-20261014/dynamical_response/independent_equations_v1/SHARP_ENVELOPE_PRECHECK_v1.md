# Independent sharp-envelope witness derivation

This derivation uses only the two fixture specifications sent by root. It is frozen before reading the new author controls. It checks the sharpness witnesses for the already reviewed coefficient perturbation formulas; it does not change those formulas or make a physical error claim.

## Matrix denominator

Let P=(2,4,6), rhat=(0,0,1/3), zhat=(9/10,1/2,1) and d=1/100. The row matrix is

    Lhat=[[1,-1,0],[1,-2,0],[1,-3,-1]],
    Lhat^-1=[[2,-1,0],[1,-1,0],[-1,2,-1]].

Thus ||Lhat^-1||_infinity=4. With eP=eM=0 and er_i=2d/P_i, the error formula gives matrix_delta=d, eta=4d=1/25 and epsilon=4d/(1-4d)=1/24.

Choose the true r shift (-er1,+er2,-er3), holding M=Lhat zhat fixed. Then L-Lhat=d(1,-1,1)^T(0,0,1), and Lhat^-1 d(1,-1,1)^T=d(3,2,-4)^T. The exact rank-one inverse therefore gives

    z-zhat=(-1/32,-1/48,+1/24),
    z=(139/160,23/48,25/24).

The actual infinity error is exactly epsilon. The deliberately wrong denominator 1+eta would give 4d/(1+4d)=1/26, strictly below the actual 1/24. This is an attained matrix-norm bound, not a merely conservative corner example.

## Ratio denominator

Let P=(-7/3,2/3,5/3), rhat=(6/7,0,6/5), zhat=(1,1/2,1), e=1/100 and zero coefficient errors. Then

    Lhat=[[1,7/6,1],[1,-1/3,0],[1,-5/6,-1]].

Its inverse has induced infinity norm 4. Since matrix_delta=0, the state bound is epsilon=4e=1/25. Use delta M=e(1,-1,1). Solving Lhat delta z=delta M gives

    delta z=(1/300,+1/25,-1/25),
    z=(301/300,27/50,24/25),
    qhat=1/2, q=9/16.

Hence |q-qhat|=1/16. The correct ratio bound is

    epsilon(1+|qhat|)/(|yhat|-epsilon)=1/16,

while the deliberately wrong plus denominator gives 3/52<1/16. Both true R and q remain positive and y remains away from zero. These are exact supplied-rational witnesses. They do not infer an observationally achieved envelope or make the coefficient certificate a full observable-denominator certificate.

The failed ratio fixture with first r=-6/7 is not silently corrected here: root reports that its failed source/run is preserved. This independent derivation binds only the corrected +6/7 fixture. A mutation run whose baseline failed cannot support mutation sensitivity; that accounting remains separate from these exact calculations.
