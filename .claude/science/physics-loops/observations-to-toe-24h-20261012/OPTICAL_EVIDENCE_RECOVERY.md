# Exact optical review evidence recovery

The two OPTICAL_IMMUTABLE JSON archives at this campaign root preserve the
exact bytes of raw review differences and six reviewer files whose whitespace
would otherwise fail the repository check. Original local files are unchanged.
REVIEW_DISPLAY.md files add an explicit identity prefix and remove EOF blank
lines for reading; receipts refer to the original bytes in the archive.

To reconstruct any archived file, decode its base64 field, verify the listed
SHA-256 and byte length, and write it under the listed campaign-relative path.
Refuse to overwrite any existing file with a different hash. The independent
programs must be recovered together with their pinned source snapshots before
reproduction; the archive is not a claim that normalized code was executed.
