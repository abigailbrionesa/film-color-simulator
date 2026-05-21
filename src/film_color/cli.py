import argparse
from pathlib import Path
from typing import Sequence

from .config import GenerationConfig
from .evaluation import EvaluationConfig, evaluate_model
from .generator import generate_images
from .training import TrainingConfig, train_model


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

    train_parser = subparsers.add_parser(
        "train",
        help="Train the baseline CNN classifier.",
    )
    train_parser.add_argument(
        "--data",
        type=Path,
        default=Path("dataset"),
        help="Generated dataset directory.",
    )
    train_parser.add_argument(
        "--epochs",
        type=int,
        default=10,
        help="Number of training epochs.",
    )
    train_parser.add_argument(
        "--batch-size",
        type=int,
        default=32,
        help="Training batch size.",
    )
    train_parser.add_argument(
        "--image-size",
        type=int,
        default=600,
        help="Square image size in pixels.",
    )
    train_parser.add_argument(
        "--model-output",
        type=Path,
        default=Path("artifacts/model.keras"),
        help="Path where the trained model will be saved.",
    )
    train_parser.add_argument(
        "--seed",
        type=int,
        default=123,
        help="Dataset split seed.",
    )

    evaluate_parser = subparsers.add_parser(
        "evaluate",
        help="Evaluate a trained classifier.",
    )
    evaluate_parser.add_argument(
        "--data",
        type=Path,
        default=Path("dataset"),
        help="Generated dataset directory.",
    )
    evaluate_parser.add_argument(
        "--model",
        type=Path,
        default=Path("artifacts/model.keras"),
        help="Path to a trained Keras model.",
    )
    evaluate_parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/evaluation.json"),
        help="Path where evaluation metrics JSON will be saved.",
    )
    evaluate_parser.add_argument(
        "--batch-size",
        type=int,
        default=32,
        help="Evaluation batch size.",
    )
    evaluate_parser.add_argument(
        "--image-size",
        type=int,
        default=600,
        help="Square image size in pixels.",
    )
    evaluate_parser.add_argument(
        "--seed",
        type=int,
        default=123,
        help="Dataset split seed.",
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


def run_train(args: argparse.Namespace) -> int:
    if args.epochs < 1:
        raise ValueError("--epochs must be at least 1")
    if args.batch_size < 1:
        raise ValueError("--batch-size must be at least 1")
    if args.image_size < 1:
        raise ValueError("--image-size must be at least 1")

    config = TrainingConfig(
        data_dir=args.data,
        epochs=args.epochs,
        batch_size=args.batch_size,
        image_size=(args.image_size, args.image_size),
        model_output=args.model_output,
        seed=args.seed,
    )
    metrics = train_model(config)
    print(f"Saved model to {metrics['model_path']}")
    print(f"Validation accuracy: {metrics['validation_accuracy']:.4f}")
    return 0


def run_evaluate(args: argparse.Namespace) -> int:
    if args.batch_size < 1:
        raise ValueError("--batch-size must be at least 1")
    if args.image_size < 1:
        raise ValueError("--image-size must be at least 1")
    if not args.model.exists():
        raise ValueError(f"model path does not exist: {args.model}")
    if not args.data.exists():
        raise ValueError(f"dataset path does not exist: {args.data}")

    config = EvaluationConfig(
        data_dir=args.data,
        model_path=args.model,
        output_path=args.output,
        image_size=(args.image_size, args.image_size),
        batch_size=args.batch_size,
        seed=args.seed,
    )
    metrics = evaluate_model(config)
    print(f"Validation accuracy: {metrics['validation_accuracy']:.4f}")
    print(f"Confusion matrix: {metrics['confusion_matrix']}")
    print(f"Saved metrics to {args.output}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "generate":
            return run_generate(args)
        if args.command == "train":
            return run_train(args)
        if args.command == "evaluate":
            return run_evaluate(args)
    except ValueError as exc:
        parser.error(str(exc))

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
