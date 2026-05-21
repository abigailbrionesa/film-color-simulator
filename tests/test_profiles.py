from film_color.config import GenerationConfig
from film_color.profiles import COLORS


def test_default_profiles_are_valid_hsv_values():
    assert COLORS

    for hue, saturation, value in COLORS:
        assert 0 <= hue <= 179
        assert 0 <= saturation <= 255
        assert 0 <= value <= 255


def test_generation_config_uses_expected_default_labels():
    config = GenerationConfig()

    assert config.fresh_label == "fresh"
    assert config.altered_label == "altered"
    assert config.fresh_dir.name == "fresh"
    assert config.altered_dir.name == "altered"
