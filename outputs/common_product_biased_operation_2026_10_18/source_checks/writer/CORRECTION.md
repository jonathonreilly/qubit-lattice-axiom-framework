# Endpoint correction to equation (2)

This note corrects the frozen `PROPOSAL.md`, SHA256 `dfe071282ac3d160073b85caa0bd11d4e1834e58278e1da8a3c354fec5440c18`. The source and its distinct review remain unchanged.

The displayed chain `0<=k-q<=r/(2*.99)<r` incorrectly includes a strict final inequality at r=0. Replace it by

    0 <= k-q <= r/(2*.99) <= r.

The final inequality is strict when r>0. At r=0, q=k and every quantity in this chain is zero.

All subsequent estimates use only the non-strict bound |k-q|<=r. The bounds for the outgoing self-energy, inverse, flux factors, scattering error and packet variable change are therefore unchanged, including their validity at zero bias. This is an endpoint correction, not a change of domain or constants.

The network author identified the typo after the local source's distinct review; ROOT requested this separate correction. No frozen source, review, W, Git or checkpoint was modified, and no publication was performed.
