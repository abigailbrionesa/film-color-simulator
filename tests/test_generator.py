import json

from PIL import Image

from film_color.config import GenerationConfig
from film_color.generator import create_image, generate_images, get_label_for_color


def test_create_image_uses_configured_dimensions():
    image = create_image((70, 255, 255), size=(32, 24))

    assert image.size == (32, 24)
    assert image.mode == "RGB"


def test_create_image_supports_optional_lighting_and_texture():
    image = create_image(
        (70, 255, 255),
        size=(32, 24),
        enable_lighting=True,
        enable_texture=True,
    )

    assert image.size == (32, 24)
    assert image.mode == "RGB"


def test_get_label_for_color_uses_threshold():
    config = GenerationConfig(fresh_threshold=60)

    assert get_label_for_color((70, 255, 255), config) == "fresh"
    assert get_label_for_color((30, 255, 255), config) == "altered"


def test_generate_images_creates_class_folders_and_metadata(tmp_path):
    config = GenerationConfig(
        output_dir=tmp_path,
        image_size=(24, 24),
        num_variations=1,
        random_seed=123,
        colors=((70, 255, 255), (30, 255, 255)),
    )

    generated = generate_images(config)

    assert len(generated) == 2
    assert (tmp_path / "fresh").is_dir()
    assert (tmp_path / "altered").is_dir()
    assert (tmp_path / "metadata.json").is_file()

    for item in generated:
        assert item.path.suffix == ".png"
        assert item.path.exists()
        assert Image.open(item.path).size == (24, 24)

    metadata = json.loads((tmp_path / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["random_seed"] == 123
    assert metadata["generated_count"] == 2
    assert metadata["class_counts"] == {"fresh": 1, "altered": 1}
