# Flitsy — Brand assets

The Flitsy mark is **`{f|}`** — a lowercase "f" framed by curly braces with a blinking cursor. The braces nod to MCP / function-call vocabulary; the cursor signals that Flitsy is something you _talk to_, not click around in.

## Files

```
brand/
├── colors.css                                 ← drop-in CSS variables
├── Brand Guide.html                           ← visual reference / spec page
├── logos/
│   ├── flitsy-mark.svg                        ← primary, static (cursor solid)
│   ├── flitsy-mark-animated.svg               ← primary, cursor blinks (1.1s)
│   ├── flitsy-mark-dark.svg / -animated.svg   ← cream on ink for product surfaces
│   ├── flitsy-mark-amber.svg                  ← all-ink on amber ground
│   ├── flitsy-mark-mono.svg                   ← no accent, single-color
│   ├── flitsy-wordmark.svg / -dark.svg
│   ├── flitsy-lockup-horizontal.svg           ← mark + wordmark side by side
│   ├── flitsy-lockup-horizontal-animated.svg
│   ├── flitsy-lockup-horizontal-dark.svg
│   └── flitsy-lockup-stacked.svg / -dark.svg
├── icons/
│   ├── favicon.svg                            ← 32×32 transparent
│   ├── favicon-dark.svg                       ← 32×32 with dark fill
│   ├── favicon-rounded.svg                    ← 32×32 rounded square
│   ├── apple-touch-icon-180.svg               ← 180×180 with safe area
│   └── app-icon-512.svg                       ← 512×512 master app icon
└── exports/                                   ← rasterized PNGs (see below)
```

## Color tokens

| Token              | Hex        | Use                                       |
| ------------------ | ---------- | ----------------------------------------- |
| `--flitsy-cream`   | `#fdf8ee`  | Primary ground (matches flitsy.app)       |
| `--flitsy-ink`     | `#1a1714`  | Body text, brace strokes, dark surfaces   |
| `--flitsy-ink-3`   | `#8a8378`  | Muted text, mono labels                   |
| `--flitsy-amber`   | `oklch(0.72 0.14 65)` / `#d09863` | Cursor, single accent |

The amber is intentionally low-saturation so it sits next to the warm cream without clashing. Don't use it for primary text or large fills.

## Type

- **Display & body:** Geist (500/600). [Google Fonts](https://fonts.google.com/specimen/Geist).
- **Mono / technical labels:** JetBrains Mono (400/500).

Both are open-source. Embed via Google Fonts or self-host.

## Mark — anatomy

The mark is built from four parts. The proportions below are fixed; don't redraw or eyeball.

1. **Left brace** — custom-drawn (not a font character). Sharp middle pinch, rounded terminals.
2. **Lowercase f** — stroked path, round caps. Crossbar stops short of the curl on the right.
3. **Cursor bar** — amber, rounded rect, ~70% of f height.
4. **Right brace** — left brace, mirrored.

All four sit on a single baseline. The visual rhythm relies on this consistency — when you scale, scale the whole group.

### Clear space

Leave at least the width of one cursor bar (≈ 5% of mark width) on every side. For the stacked lockup, the gap below the mark equals the wordmark's cap height.

### Minimum sizes

- Mark only: **24 px**.
- Wordmark: **80 px** wide.
- Horizontal lockup: **120 px** wide.

Below 24 px, use the favicon SVG — it's tuned for that scale (stroke widths bumped so the brace pinch survives).

### Animation

The cursor blinks at **1.1s, 50/50 duty cycle**. Don't change the period or override the easing — it's tuned to feel "typing-cursor" not "warning-light." For static contexts (print, social avatars, motion-sensitive viewers), use the non-`-animated` variants — same composition with a solid cursor bar.

## What to avoid

- **No standalone lowercase "f" inside a rounded square.** Reads as Facebook. Use the mark with both braces, or the wordmark.
- **No outlined / hollow versions.** The mark is built around stroke weight; outlining flips the visual balance.
- **No gradients on the cursor.** Solid amber only.
- **No emoji or extra decoration.** The cursor is the only "alive" element; let it carry the personality.

## PNG exports

The `exports/` folder has rasterized PNGs of the mark at common sizes:

| File                          | Use                                       |
| ----------------------------- | ----------------------------------------- |
| `flitsy-mark-256/512/1024.png`| General-purpose, social, OG images        |
| `flitsy-mark-dark-*.png`      | On dark backgrounds                       |
| `flitsy-mark-mono-512.png`    | Single-color contexts (laser, embroidery) |
| `favicon-16/32/48.png`        | Web favicons                              |
| `apple-touch-icon-180.png`    | iOS home-screen icon                      |
| `app-icon-512/1024.png`       | App stores, larger product icons          |

For anywhere you can use SVG, prefer SVG — it's vector and the animated variants only work as SVG.

## Working with the SVGs

- **`<text>` uses a font-family stack** (Geist → Helvetica Neue → Arial). When opened standalone without Geist installed, the wordmark falls back to Helvetica — visually close enough for handoff. For final production assets, **outline the text in Figma / Illustrator** so the wordmark renders identically everywhere.
- **The mark itself uses no fonts** — every shape is a path or rect. It rasterizes consistently in any environment.

## License

These assets are proprietary to Flitsy. Internal use only unless you've cleared otherwise.

— Generated as a brand-handoff package. Open `Brand Guide.html` in a browser for the visual reference.
