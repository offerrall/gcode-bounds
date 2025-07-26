## Features

- ⚡ **Pure C implementation** - 12x faster than Python 
- 🎯 **Zero runtime dependencies** - only Python standard library
- 📦 **Universal compatibility** - handles CNC (.nc), laser (.gcode), 3D printer files
- 🔧 **Professional grade** - processes 300MB+ files in seconds
- 🌍 **Cross-platform** - Windows, macOS, Linux with automatic compilation# gcode-bounds

High-performance G-code file parser with framing G-code generation.
Built with a **pure C extension** for maximum speed and zero runtime dependencies.

## Installation

```bash
git clone https://github.com/offerrall/gcode-bounds
cd gcode-bounds
pip install .
```

## Usage

```python
from gcode_bounds import get_bounding_box, generate_framing_gcode

# Extract bounding box
bounds = get_bounding_box("part.nc")
print(f"Size: {bounds[1] - bounds[0]:.1f} x {bounds[3] - bounds[2]:.1f} mm")

# Generate framing G-code
gcode = generate_framing_gcode(*bounds, power=15, speed=1500)

# Save to file
with open("frame.gcode", "w") as f:
    f.write("\n".join(gcode))
```

## Compatible Files

- CNC files (`.nc`)
- Laser files (`.gcode`) 
- 3D printer files (`.gcode`)
- Any file with X/Y coordinates

## API

### `get_bounding_box(file_path) -> (min_x, max_x, min_y, max_y)`

Extract bounding box coordinates from G-code file.

### `generate_framing_gcode(min_x, max_x, min_y, max_y, power=10, speed=1000) -> list[str]`

Generate rectangular frame G-code for alignment.

## Technical Details

- **Core parsing**: Pure C99 implementation
- **Python integration**: Native C extension using Python.h API (no CFFI overhead)
- **Memory efficiency**: Streaming parser, processes files larger than available RAM
- **Error handling**: Comprehensive validation with clear error messages

### Installation Issues

**Windows:**
```bash
# Install Visual Studio Build Tools if compilation fails
# Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install build-essential python3-dev
```

**macOS:**
```bash
xcode-select --install
```

## License

MIT License - Production ready, commercial use allowed.