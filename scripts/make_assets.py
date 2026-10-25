#!/usr/bin/env python3
"""Generate static brand assets for the personal site."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"

# ---------------------------------------------------------------------------
# Avatar: centre the head and full upper body inside the circular crop
# ---------------------------------------------------------------------------
src = Image.open(ROOT / "scripts" / "profile-source.png").convert("RGB")
# The source is a wide classroom photo. This square keeps the full upper
# and middle body with a little headroom while centring the torso.
avatar = src.crop((690, 522, 2090, 1922)).resize((480, 480), Image.LANCZOS)
avatar.save(IMG / "avatar.webp", "WEBP", quality=90, method=6)
avatar.save(IMG / "avatar.jpg", "JPEG", quality=88, optimize=True, progressive=True)

# ---------------------------------------------------------------------------
# Favicon: monogram "AK"
# ---------------------------------------------------------------------------
favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#0b0c0f"/>
  <rect x="1" y="1" width="62" height="62" rx="13" fill="none" stroke="#34343a"/>
  <text x="32" y="42" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif"
        font-size="28" font-weight="700" letter-spacing="-1" fill="#f1ede5">AK</text>
  <circle cx="50" cy="16" r="3" fill="#c2a274"/>
</svg>
"""
(IMG / "favicon.svg").write_text(favicon_svg, encoding="utf-8")

# raster favicon + apple touch icon
def find_font(candidates: list[str]) -> str | None:
    for p in candidates:
        if Path(p).exists():
            return p
    return None


font_path = find_font(
    [
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
    ]
)

def make_icon(size: int, out: Path) -> None:
    scale = 4
    canvas = Image.new("RGBA", (size * scale, size * scale), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)
    s = size * scale
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=int(s * 0.22), fill="#0b0c0f")
    d.rounded_rectangle(
        (1 * scale, 1 * scale, s - 1 * scale, s - 1 * scale),
        radius=int(s * 0.21),
        outline="#34343a",
        width=max(1, scale),
    )
    if font_path:
        try:
            font = ImageFont.truetype(font_path, int(s * 0.44))
        except OSError:
            font = ImageFont.load_default()
        text = "AK"
        box = d.textbbox((0, 0), text, font=font)
        tw, th = box[2] - box[0], box[3] - box[1]
        d.text(
            ((s - tw) / 2 - box[0], (s - th) / 2 - box[1] - s * 0.02),
            text,
            font=font,
            fill="#f1ede5",
        )
    d.ellipse(
        (
            s - s * 0.28,
            s * 0.12,
            s - s * 0.16,
            s * 0.24,
        ),
        fill="#c2a274",
    )
    canvas.resize((size, size), Image.LANCZOS).save(out)


make_icon(180, IMG / "apple-touch-icon.png")
make_icon(32, IMG / "favicon-32.png")
make_icon(512, IMG / "icon-512.png")

print("wrote", IMG / "avatar.webp", (IMG / "avatar.webp").stat().st_size)
print("font:", font_path)
