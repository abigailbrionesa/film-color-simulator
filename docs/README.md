# Film Color Simulator

Tool to generate synthetic datasets of intelligent films that change color based on pH levels (from fuchsia to green) 

## Use Cases
- Training computer vision models for freshness detection.
- Lab experiments simulation (color vs pH).

## How It Works
1. **Color Profiles**: HSV-based gradients (`fresco` = pink/purple, `alterado` = green/yellow).
2. **Variations**: Adds noise, brightness, and small hue deviations.
3. **Output**: Synthetic images (600x600px by default).