# make.fun art entry: food-picture-03

`main.py` publishes `entry.png` as the entry image. It locates `entry.png`
beside itself and copies it byte for byte into `MAKEFUN_OUTPUT_DIR` (default
`/output`), creating the directory if needed. It prints the output path and
the number of bytes written, and exits non-zero with a clear error if the
source is missing, the copy is empty, or the copy is not byte-identical to
the source.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` will be an exact copy of the submitted image.
