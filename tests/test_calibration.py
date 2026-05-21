import json

import pytest

from film_color.calibration import load_calibrated_colors
from film_color.config import GenerationConfig


def test_load_calibrated_colors(tmp_path):
    path = tmp_path / "calibration.json"
    path.write_text(json.dumps({"colors": [[70, 255, 255], [30, 240, 220]]}), encoding="utf-8")

    colors = load_calibrated_colors(path)

    assert colors == ((70, 255, 255), (30, 240, 220))


def test_generation_config_can_load_calibrated_colors(tmp_path):
    path = tmp_path / "calibration.json"
    path.write_text(json.dumps({"colors": [[70, 255, 255]]}), encoding="utf-8")

    config = GenerationConfig.from_calibration_file(path, output_dir=tmp_path / "dataset")

    assert config.colors == ((70, 255, 255),)
    assert config.output_dir == tmp_path / "dataset"


def test_load_calibrated_colors_rejects_invalid_hsv(tmp_path):
    path = tmp_path / "calibration.json"
    path.write_text(json.dumps({"colors": [[200, 255, 255]]}), encoding="utf-8")

    with pytest.raises(ValueError, match="invalid HSV"):
        load_calibrated_colors(path)
