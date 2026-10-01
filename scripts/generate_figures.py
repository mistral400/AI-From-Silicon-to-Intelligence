#!/usr/bin/env python3
"""Generate the original neural-network figures used by the book."""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "book" / "figures"

BLUE = "#0072B2"
ORANGE = "#D55E00"
GREEN = "#009E73"
PURPLE = "#CC79A7"
INK = "#263238"
MUTED = "#65727A"


def draw_network(path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8.4, 4.5), dpi=180)
    ax.set_xlim(-0.65, 3.6)
    ax.set_ylim(-0.7, 3.0)
    ax.axis("off")

    layers = [
        (0.0, [("x₁", 1.85), ("x₂", 0.55)], "Entrées"),
        (1.45, [("h₁", 2.35), ("h₂", 1.2), ("h₃", 0.05)], "Couche cachée"),
        (2.9, [("z₁", 1.85), ("z₂", 0.55)], "Logits"),
    ]

    for layer_index in range(len(layers) - 1):
        x0, left_nodes, _ = layers[layer_index]
        x1, right_nodes, _ = layers[layer_index + 1]
        for _, y0 in left_nodes:
            for _, y1 in right_nodes:
                ax.add_patch(
                    FancyArrowPatch(
                        (x0 + 0.19, y0),
                        (x1 - 0.19, y1),
                        arrowstyle="-|>",
                        mutation_scale=9,
                        linewidth=1.0,
                        color="#9BA8AE",
                        alpha=0.9,
                        zorder=1,
                        shrinkA=1,
                        shrinkB=1,
                    )
                )

    palette = [BLUE, ORANGE, GREEN]
    for layer_index, (x, nodes, title) in enumerate(layers):
        ax.text(x, 2.72, title, ha="center", va="bottom", color=INK, fontsize=11, weight="bold")
        for label, y in nodes:
            ax.add_patch(
                Circle(
                    (x, y),
                    0.19,
                    facecolor="white",
                    edgecolor=palette[layer_index],
                    linewidth=2,
                    zorder=3,
                )
            )
            ax.text(x, y, label, ha="center", va="center", color=INK, fontsize=11, zorder=4)

    ax.text(1.45, -0.48, "ReLU sur les unités cachées", ha="center", color=MUTED, fontsize=9)
    ax.text(2.9, -0.48, "scores avant softmax", ha="center", color=MUTED, fontsize=9)
    fig.tight_layout(pad=0.5)
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def draw_activations(path: Path) -> None:
    x = np.linspace(-4.0, 4.0, 801)
    sigmoid = 1.0 / (1.0 + np.exp(-x))
    tanh = np.tanh(x)
    relu = np.maximum(0.0, x)
    cdf = np.vectorize(lambda value: 0.5 * (1.0 + math.erf(value / math.sqrt(2.0))))(x)
    gelu = x * cdf

    fig, ax = plt.subplots(figsize=(8.2, 4.4), dpi=180)
    ax.plot(x, sigmoid, color=BLUE, linewidth=2.2, label="sigmoïde")
    ax.plot(x, tanh, color=ORANGE, linewidth=2.2, label="tanh")
    ax.plot(x, relu, color=GREEN, linewidth=2.2, label="ReLU")
    ax.plot(x, gelu, color=PURPLE, linewidth=2.2, linestyle="--", label="GELU")
    ax.axhline(0.0, color="#7C878C", linewidth=0.8)
    ax.axvline(0.0, color="#7C878C", linewidth=0.8)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.25, 4.2)
    ax.set_xlabel("entrée x")
    ax.set_ylabel("sortie φ(x)")
    ax.grid(True, color="#DCE2E5", linewidth=0.7, alpha=0.8)
    ax.legend(frameon=False, ncols=2, loc="upper left")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(pad=0.7)
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare regenerated figures with committed images")
    args = parser.parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)

    expected = {
        OUTPUT / "fig-03-mlp-01.png": draw_network,
        OUTPUT / "fig-03-activations-01.png": draw_activations,
    }
    if args.check:
        import tempfile
        from PIL import Image

        with tempfile.TemporaryDirectory(prefix="ai-silicon-figures-") as temporary:
            temporary_root = Path(temporary)
            for destination, draw in expected.items():
                generated = temporary_root / destination.name
                draw(generated)
                if not destination.is_file():
                    parser.error(f"missing generated figure: {destination.relative_to(ROOT)}")
                with Image.open(generated) as new_image, Image.open(destination) as committed_image:
                    if new_image.size != committed_image.size:
                        parser.error(f"figure dimensions changed: {destination.relative_to(ROOT)}")
                    new_pixels = np.asarray(new_image.convert("RGBA"), dtype=np.int16)
                    old_pixels = np.asarray(committed_image.convert("RGBA"), dtype=np.int16)
                differing = np.any(np.abs(new_pixels - old_pixels) > 3, axis=2)
                fraction = float(np.mean(differing))
                if fraction > 0.005:
                    parser.error(
                        f"figure differs by {fraction:.2%}; run python scripts/generate_figures.py "
                        f"({destination.relative_to(ROOT)})"
                    )
    else:
        for destination, draw in expected.items():
            draw(destination)
            print(f"Wrote {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
