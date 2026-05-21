import pytest

from film_color.cli import main


def test_generate_cli_creates_dataset(tmp_path):
    exit_code = main(
        [
            "generate",
            "--samples",
            "1",
            "--output",
            str(tmp_path),
            "--image-size",
            "24",
            "--seed",
            "123",
        ]
    )

    assert exit_code == 0
    assert (tmp_path / "fresh").is_dir()
    assert (tmp_path / "altered").is_dir()
    assert (tmp_path / "metadata.json").is_file()
    assert len(list(tmp_path.glob("*/*.png"))) == 9


def test_generate_cli_rejects_invalid_sample_count(tmp_path):
    with pytest.raises(SystemExit) as exc_info:
        main(["generate", "--samples", "0", "--output", str(tmp_path)])

    assert exc_info.value.code == 2


def test_predict_cli_rejects_missing_image(tmp_path):
    with pytest.raises(SystemExit) as exc_info:
        main(["predict", "--image", str(tmp_path / "missing.png")])

    assert exc_info.value.code == 2
