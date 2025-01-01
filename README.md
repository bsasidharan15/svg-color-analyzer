# Memory Efficient Color Ensemble

A Python library for efficiently extracting and analyzing dominant colors from SVG files using memory-optimized clustering techniques.

## Features

- 🎨 Extract colors from SVG files in both RGB and hexadecimal formats
- 🚀 Memory-efficient color clustering using MiniBatchKMeans
- 📊 Multiple visualization options for color analysis
- 🔄 Automatic conversion between RGB and hexadecimal color formats
- 💾 Batch processing support for large SVG files
- 📈 Color swatch generation and visualization

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/memory-efficient-color-ensemble.git

# Navigate to the project directory
cd memory-efficient-color-ensemble

# Install required dependencies
pip install -r requirements.txt
```

## Dependencies

- Python 3.7+
- NumPy
- scikit-learn
- matplotlib
- xml.etree.ElementTree (built-in)
- re (built-in)
- collections (built-in)

## Usage

### Basic Usage

```python
from color_ensemble import MemoryEfficientColorEnsemble

# Initialize the ensemble
ensemble = MemoryEfficientColorEnsemble(n_colors=5, batch_size=100)

# Read your SVG file
with open('your_svg_file.svg', 'r') as file:
    svg_content = file.read()

# Find dominant colors
dominant_colors = ensemble.find_dominant_colors(svg_content)

# Print the results
print("Dominant colors found:")
for i, color in enumerate(dominant_colors, 1):
    print(f"{i}. {color}")
```

### Visualization

```python
from color_ensemble import visualize_colors, create_color_swatches

# Visualize colors as a bar chart
visualize_colors(dominant_colors, title="Dominant Colors in SVG")

# Create detailed color swatches
create_color_swatches(dominant_colors, title="Dominant Colors with Swatches")
```

## API Reference

### MemoryEfficientColorEnsemble

```python
class MemoryEfficientColorEnsemble(n_colors=5, batch_size=100)
```

#### Parameters:
- `n_colors` (int): Number of dominant colors to extract (default: 5)
- `batch_size` (int): Batch size for MiniBatchKMeans clustering (default: 100)

#### Methods:

##### find_dominant_colors(svg_content)
Extracts and returns dominant colors from SVG content.

Parameters:
- `svg_content` (str): Content of the SVG file

Returns:
- List of hexadecimal color codes

### Visualization Functions

#### visualize_colors(colors, title="Dominant Colors in SVG")
Creates a horizontal bar chart of colors.

Parameters:
- `colors` (list): List of hexadecimal color codes
- `title` (str): Title for the visualization

#### create_color_swatches(colors, title="Dominant Colors with Swatches")
Creates detailed color swatches with hexadecimal values.

Parameters:
- `colors` (list): List of hexadecimal color codes
- `title` (str): Title for the visualization

## Examples

### Basic Color Extraction
```python
# Initialize with custom parameters
ensemble = MemoryEfficientColorEnsemble(n_colors=3, batch_size=50)

# Process SVG file
with open('example.svg', 'r') as file:
    svg_content = file.read()

# Get dominant colors
colors = ensemble.find_dominant_colors(svg_content)
print(f"Found {len(colors)} dominant colors: {colors}")
```

### Creating Visualizations
```python
# Create both types of visualizations
visualize_colors(colors)
create_color_swatches(colors)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Sasidharan B

## Acknowledgments

- Thanks to scikit-learn for the MiniBatchKMeans implementation
- Inspired by color quantization techniques in image processing
- Built with Python and its amazing scientific computing ecosystem
