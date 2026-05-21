from pathlib import Path

import numpy as np

from .color_extractor import ColorExtractor


if __name__ == "__main__":
    extractor = ColorExtractor()

    fresco_dir = Path("./dataset/fresco")
    alterado_dir = Path("./dataset/alterado")

    muestra = fresco_dir / "fresco_0_0.png"
    if muestra.exists():
        color = extractor.get_dominant_color(muestra)
        print("Color LAB dominante:", color)

    fresco_stats = extractor.analyze_dataset(fresco_dir, max_images=10)
    print("\nPromedios FRESCO:")
    print("  L:", np.mean(fresco_stats["l_values"]))
    print("  a:", np.mean(fresco_stats["a_values"]))
    print("  b:", np.mean(fresco_stats["b_values"]))

    alterado_stats = extractor.analyze_dataset(alterado_dir, max_images=10)
    print("\nPromedios ALTERADO:")
    print("  L:", np.mean(alterado_stats["l_values"]))
    print("  a:", np.mean(alterado_stats["a_values"]))
    print("  b:", np.mean(alterado_stats["b_values"]))
