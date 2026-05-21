import argparse
from pathlib import Path
from typing import Sequence

from .config import GenerationConfig
from .generator import generate_images


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="film-color",
        description="Generate synthetic pH-sensitive film color datasets.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate a synthetic image dataset.",
    )
    generate_parser.add_argument(
        "--samples",
        type=int,
        default=20,
        help="Number of variations to generate for each base HSV profile.",
    )
    generate_parser.add_argument(
        "--output",
        type=Path,
        default=Path("dataset"),
        help="Directory where generated class folders will be written.",
    )
    generate_parser.add_argument(
        "--image-size",
        type=int,
        default=600,
        help="Square image size in pixels.",
    )
    generate_parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducible output.",
    )
    return parser


def run_generate(args: argparse.Namespace) -> int:
    if args.samples < 1:
        raise ValueError("--samples must be at least 1")
    if args.image_size < 1:
        raise ValueError("--image-size must be at least 1")

    config = GenerationConfig(
        image_size=(args.image_size, args.image_size),
        num_variations=args.samples,
        output_dir=args.output,
        random_seed=args.seed,
    )
    generated = generate_images(config)
    print(f"Generated {len(generated)} images in {config.output_dir}")
    print(f"Metadata saved to {config.output_dir / 'metadata.json'}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "generate":
            return run_generate(args)
    except ValueError as exc:
        parser.error(str(exc))

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
