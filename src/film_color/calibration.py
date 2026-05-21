import json
from pathlib import Path


def load_calibrated_colors(path: Path) -> tuple[tuple[int, int, int], ...]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_colors = payload.get("colors")
    if not isinstance(raw_colors, list) or not raw_colors:
        raise ValueError("calibration file must contain a non-empty 'colors' list")

    colors: list[tuple[int, int, int]] = []
    for color in raw_colors:
        if not isinstance(color, list | tuple) or len(color) != 3:
            raise ValueError("each calibrated color must contain three HSV values")
        hue, saturation, value = (int(channel) for channel in color)
        if not (0 <= hue <= 179 and 0 <= saturation <= 255 and 0 <= value <= 255):
            raise ValueError(f"invalid HSV color: {color}")
        colors.append((hue, saturation, value))

    return tuple(colors)
