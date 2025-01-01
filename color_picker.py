import re
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import xml.etree.ElementTree as ET
from collections import defaultdict
import matplotlib.pyplot as plt

class MemoryEfficientColorEnsemble:
    def __init__(self, n_colors=5, batch_size=100):
        """
        Initialize the color ensemble with specified parameters.

        Args:
            n_colors (int): Number of dominant colors to find
            batch_size (int): Batch size for MiniBatchKMeans
        """
        self.n_colors = n_colors
        self.batch_size = batch_size
        self.color_pattern = re.compile(r'#[0-9a-fA-F]{6}|rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)')

    def _rgb_to_hex(self, rgb_str):
        """Convert RGB color string to hexadecimal format."""
        try:
            # Extract RGB values
            rgb = tuple(map(int, re.findall(r'\d+', rgb_str)))
            return '#{:02x}{:02x}{:02x}'.format(*rgb)
        except:
            return None

    def _hex_to_rgb_array(self, hex_color):
        """Convert hexadecimal color to RGB numpy array."""
        hex_color = hex_color.lstrip('#')
        return np.array([int(hex_color[i:i+2], 16) for i in (0, 2, 4)])

    def _extract_colors(self, svg_content):
        """Extract all colors from SVG content."""
        colors = set()

        # Find all color matches
        for color in self.color_pattern.findall(svg_content):
            if color.startswith('rgb'):
                hex_color = self._rgb_to_hex(color)
                if hex_color:
                    colors.add(hex_color)
            else:
                colors.add(color.lower())

        return list(colors)

    def _cluster_colors(self, colors):
        """Cluster colors using MiniBatchKMeans."""
        if not colors:
            return []

        # Convert colors to RGB arrays
        color_arrays = np.array([self._hex_to_rgb_array(color) for color in colors])

        # Use MiniBatchKMeans for memory-efficient clustering
        n_clusters = min(self.n_colors, len(colors))
        kmeans = MiniBatchKMeans(
            n_clusters=n_clusters,
            batch_size=self.batch_size,
            random_state=42
        )
        kmeans.fit(color_arrays)

        # Convert cluster centers back to hex colors
        dominant_colors = []
        for center in kmeans.cluster_centers_:
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                int(center[0]),
                int(center[1]),
                int(center[2])
            )
            dominant_colors.append(hex_color)

        return dominant_colors

    def find_dominant_colors(self, svg_content):
        """
        Find dominant colors in SVG content.

        Args:
            svg_content (str): SVG file content

        Returns:
            list: List of dominant colors in hexadecimal format
        """
        # Extract all colors
        colors = self._extract_colors(svg_content)

        # If few unique colors, return them all
        if len(colors) <= self.n_colors:
            return colors

        # Cluster colors to find dominant ones
        return self._cluster_colors(colors)

def visualize_colors(colors, title="Dominant Colors in SVG"):
    """
    Visualize the dominant colors as a horizontal bar chart
    """
    plt.figure(figsize=(12, 3))

    for i, color in enumerate(colors):
        plt.bar(i, 1, color=color, width=1)

    plt.title(title, pad=20)
    plt.xticks(range(len(colors)), colors, rotation=45)
    plt.yticks([])

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    plt.tight_layout()
    plt.show()

def create_color_swatches(colors, title="Dominant Colors with Swatches"):
    """
    Create a more detailed visualization with color swatches
    """
    n_colors = len(colors)
    fig, axes = plt.subplots(1, n_colors, figsize=(3*n_colors, 3))
    fig.suptitle(title, y=1.05, fontsize=14)

    if n_colors == 1:
        axes = [axes]

    for ax, color in zip(axes, colors):
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=color))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title(color, pad=10)

    plt.tight_layout()
    plt.show()

def main():
    # File path to your SVG
    svg_file_path = '/content/project-svgrepo-com.svg'

    # Read SVG content
    with open(svg_file_path, 'r') as file:
        svg_content = file.read()

    # Create and use ensemble
    ensemble = MemoryEfficientColorEnsemble()
    dominant_colors = ensemble.find_dominant_colors(svg_content)

    print("Dominant colors found:")
    for i, color in enumerate(dominant_colors, 1):
        print(f"{i}. {color}")

    # Visualize the colors in two different styles
    visualize_colors(dominant_colors)
    create_color_swatches(dominant_colors)

if __name__ == "__main__":
    main()