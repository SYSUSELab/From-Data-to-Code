# Release checks and figures

Run commands from the repository root. `validate_release.py` requires Python 3.10+ and the standard library. It checks identities, membership counts, scoring agreement, normalized evidence links, branch totals, flow conservation, panel geometry, automation references, sensitivity counts, and the released data hashes.

```bash
python3 scripts/validate_release.py
python3 scripts/render_sankey.py --no-static-export
python3 scripts/render_sankey_panels.py --no-static-export
```

The main renderer writes the standalone, network-free interactive HTML and SVG to `figures/rq3/`. The panel renderer writes its left, right, and assembled figures to the ignored `.local/rq3-panels/` directory. Renderers are adapted from the final revision's figure-generation code and read published final tables; no private source files or candidate checkpoints are required.

Optional static export uses Python Playwright:

```bash
python3 -m pip install playwright==1.64.0
python3 -m playwright install chromium
python3 scripts/render_sankey.py
python3 scripts/render_sankey_panels.py
```

The diagram overview generator uses only the standard library:

```bash
python3 scripts/render_overviews.py
```

The six taxonomy and method SVGs take their labels and counts from the released codebook and membership tables. The homepage's light/dark promotional PNGs are maintained separately and are not overwritten by this script. Overview diagrams summarize the web presentation; the manuscript's Sankey PDF is preserved separately.

The language checker scans all existing Git-tracked and non-ignored new files, including path names, decoded JSON, and extracted PDF text. It exits nonzero for detected Chinese characters or unsupported non-text files. Raster images are reported for visual inspection; taxonomy/method and manuscript figures can also be checked against their SVG/PDF sources. The two promotional hero PNGs require direct review of their English labels and counts.

```bash
python3 -m pip install pymupdf==1.28.2
python3 scripts/check_english.py
```

`--text-only` explicitly skips PDF extraction. It is a partial check and should not replace the full release check.

For the site, install the Ruby dependencies with `bundle install`, then run `bundle exec jekyll serve`. The website reads the released CSV tables, so paper lists, method counts, and family summaries use the same data as the downloadable package.
