from color_extractor_class import ColorExtractor
from pathlib import Path
import numpy as np

if __name__ == "__main__":
    extractor = ColorExtractor()

    FRESCO_DIR = Path("./dataset/fresco")
    ALTERADO_DIR = Path("./dataset/alterado")

    muestra = FRESCO_DIR / "fresco_0_0.png"
    if muestra.exists():
        color = extractor.get_dominant_color(muestra)
        print("Color LAB dominante:", color)

    fresco_stats = extractor.analyze_dataset(FRESCO_DIR, max_images=10)
    print("\nPromedios FRESCO:")
    print("  L:", np.mean(fresco_stats['l_values']))
    print("  a:", np.mean(fresco_stats['a_values']))
    print("  b:", np.mean(fresco_stats['b_values']))

    alterado_stats = extractor.analyze_dataset(ALTERADO_DIR, max_images=10)
    print("\nPromedios ALTERADO:")
    print("  L:", np.mean(alterado_stats['l_values']))
    print("  a:", np.mean(alterado_stats['a_values']))
    print("  b:", np.mean(alterado_stats['b_values']))
