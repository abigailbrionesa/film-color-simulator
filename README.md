![Fresh and altered synthetic film samples](examples/sample_dataset/fresh/fresh_0_0.png)

<samp>

# Film Color Simulator

<p>
Film Color Simulator is a lightweight applied ML project for generating synthetic image datasets of pH-sensitive freshness indicator films. It creates controlled HSV-based <code>fresh</code> and <code>altered</code> samples, saves them in a Keras-compatible folder structure, and provides a compact CNN workflow for training, evaluation, and single-image prediction.
</p>

<p>
Built with <strong>Python</strong>, <strong>OpenCV</strong>, <strong>Pillow</strong>, and <strong>TensorFlow/Keras</strong>, the project demonstrates synthetic data generation, reproducible ML workflows, CLI design, package structure, testing, and honest model-scope documentation.
</p>

## Topic Rationale

<p>
Real lab image data for freshness indicator films can be expensive, scarce, or inconsistent. This project explores a practical first step: generate controlled synthetic images, validate the data pipeline with a baseline classifier, and keep the system small enough for another engineer to inspect quickly.
</p>

<p>
This is not a food safety product. It is a focused prototype for synthetic data generation and applied computer vision workflow design.
</p>

## Highlights

<ul>
  <li>
    <strong>Synthetic film generator</strong><br>
    Creates <code>fresh</code> and <code>altered</code> film images from configurable HSV color profiles.
  </li>
  <li>
    <strong>Reproducible data output</strong><br>
    Supports random seeds and writes dataset metadata to <code>metadata.json</code>.
  </li>
  <li>
    <strong>Applied ML workflow</strong><br>
    Includes commands for dataset generation, baseline CNN training, evaluation, and prediction.
  </li>
  <li>
    <strong>Calibration-ready design</strong><br>
    Supports optional calibrated HSV profiles when real lab measurements become available.
  </li>
  <li>
    <strong>Engineering polish</strong><br>
    Uses a package layout, typed configuration, tests, GitHub Actions, and portfolio-ready documentation.
  </li>
</ul>

## Example Output

<table>
  <tr>
    <th>Fresh</th>
    <th>Altered</th>
  </tr>
  <tr>
    <td><img src="examples/sample_dataset/fresh/fresh_0_0.png" alt="Fresh synthetic film sample"></td>
    <td><img src="examples/sample_dataset/altered/altered_1_0.png" alt="Altered synthetic film sample"></td>
  </tr>
</table>

## Tech Stack

<table>
  <tr>
    <th>Area</th>
    <th>Tools</th>
  </tr>
  <tr>
    <td>Language</td>
    <td>Python 3.10+</td>
  </tr>
  <tr>
    <td>Image generation</td>
    <td>NumPy, OpenCV, Pillow</td>
  </tr>
  <tr>
    <td>ML workflow</td>
    <td>TensorFlow / Keras</td>
  </tr>
  <tr>
    <td>CLI</td>
    <td><code>argparse</code></td>
  </tr>
  <tr>
    <td>Testing</td>
    <td>pytest</td>
  </tr>
  <tr>
    <td>Packaging</td>
    <td><code>pyproject.toml</code>, setuptools</td>
  </tr>
  <tr>
    <td>CI</td>
    <td>GitHub Actions</td>
  </tr>
</table>

## Quickstart

<p>Install the lightweight local package and generator dependencies:</p>

<pre><code class="language-powershell">py -m pip install -e . --no-deps
py -m pip install numpy opencv-python Pillow pytest</code></pre>

<p>Generate a small synthetic dataset:</p>

<pre><code class="language-powershell">film-color generate --samples 20 --output dataset --image-size 128 --seed 123</code></pre>

<p>This creates:</p>

<pre><code>dataset/
  fresh/
  altered/
  metadata.json</code></pre>

<p>Install TensorFlow in a compatible Python environment for training and evaluation:</p>

<pre><code class="language-powershell">py -m pip install tensorflow</code></pre>

<p>Train the baseline classifier:</p>

<pre><code class="language-powershell">film-color train --data dataset --epochs 10 --image-size 128 --model-output artifacts/model.keras</code></pre>

<p>Evaluate the trained model:</p>

<pre><code class="language-powershell">film-color evaluate --data dataset --image-size 128 --model artifacts/model.keras --output artifacts/evaluation.json</code></pre>

<p>Run inference on one image:</p>

<pre><code class="language-powershell">film-color predict --image examples/sample_dataset/fresh/fresh_0_0.png --model artifacts/model.keras --image-size 128</code></pre>

## CLI Reference

<table>
  <tr>
    <th>Command</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><code>film-color generate</code></td>
    <td>Generate synthetic <code>fresh</code> and <code>altered</code> image folders.</td>
  </tr>
  <tr>
    <td><code>film-color train</code></td>
    <td>Train the compact CNN baseline on a generated dataset.</td>
  </tr>
  <tr>
    <td><code>film-color evaluate</code></td>
    <td>Save validation accuracy and confusion matrix metrics.</td>
  </tr>
  <tr>
    <td><code>film-color predict</code></td>
    <td>Classify a single image with a trained model.</td>
  </tr>
</table>

<pre><code class="language-powershell">film-color --help
film-color generate --help
film-color train --help
film-color evaluate --help
film-color predict --help</code></pre>

## System Flow

<pre><code>HSV color profiles
  -> Synthetic generator
  -> Keras-compatible image folders
  -> Baseline CNN training
  -> Evaluation metrics
  -> Single-image prediction</code></pre>

## Project Structure

<pre><code>src/film_color/
  calibration.py       # optional calibrated HSV profile loading
  cli.py               # command-line interface
  config.py            # generation configuration
  dataset.py           # TensorFlow dataset loading
  evaluation.py        # validation metrics and confusion matrix
  generator.py         # synthetic image generation
  model.py             # baseline CNN architecture
  prediction.py        # single-image inference helper
  profiles.py          # default HSV color profiles
  training.py          # training workflow
tests/
  test_calibration.py
  test_cli.py
  test_generator.py
  test_profiles.py
docs/
  PRD.md
  ISSUES.md
  RESULTS.md
examples/
  sample_dataset/</code></pre>

## Validation

<p>Run the fast test suite:</p>

<pre><code class="language-powershell">py -m pytest</code></pre>

<p>Current local validation:</p>

<pre><code>12 passed</code></pre>

<ul>
  <li>HSV profile validity.</li>
  <li>Calibrated color loading and validation.</li>
  <li>Generated image dimensions and RGB mode.</li>
  <li>Class label assignment.</li>
  <li>Dataset folder and metadata creation.</li>
  <li>CLI generation and invalid-argument handling.</li>
</ul>

## Results

<p>
The committed sample dataset demonstrates generator output and reproducible metadata. See <a href="docs/RESULTS.md">docs/RESULTS.md</a> for the current validation summary and the exact commands for producing baseline model metrics.
</p>

<p>
Model accuracy is not claimed in this README because it should be regenerated in the reviewer's TensorFlow environment from the documented commands.
</p>

## Limitations

<ul>
  <li>The project uses synthetic images only.</li>
  <li>It does not fully model real lab lighting, camera sensors, film texture, sample handling, or environmental noise.</li>
  <li>A classifier trained only on this data is a prototype baseline, not a validated food freshness or safety system.</li>
  <li>Real lab images would be required to measure generalization.</li>
</ul>
</samp>
