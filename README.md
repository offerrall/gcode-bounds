# gcode-bounds

Fast G-code frame bounding box generator and framing G-code generator in pure C, designed for CNC, laser, and 3D printer files. This library is optimized for speed and efficiency, making it ideal for processing large files quickly.


## Features

- ⚡ **Pure C implementation** - 26x faster than Python
- 🎯 **Zero runtime dependencies** - only Python standard library
- 📦 **Universal compatibility** - handles CNC (.nc), laser (.gcode), 3D printer files
- 🔧 **Professional grade** - processes 500MB+ files in seconds
- 🌍 **Cross-platform** - Windows, macOS, Linux with automatic compilation

## Install

```bash
git clone https://github.com/offerrall/gcode-bounds
cd gcode-bounds
pip install .
```

## Use

```python
from gcode_bounds import get_bounding_box, generate_framing_gcode

# Get bounding box
bounds = get_bounding_box("part.nc")

# Generate frame
gcode = generate_framing_gcode(*bounds, power=15, speed=1500)

# Save
with open("frame.gcode", "w") as f:
    f.write("\n".join(gcode))
```

## Performance

| Implementation | 500MB file | Lines/sec |
|---------------|------------|-----------|
| **gcode-bounds** | **2.8s** | **13.4M** |
| Python regex | 75s | 500K |

## Compatible

- CNC files (`.nc`)
- Laser files (`.gcode`)
- 3D printer files (`.gcode`)

## Requirements

- Python 3.8+
- C compiler (auto-detected)

## Troubleshooting

**Windows**: Install Visual Studio Build Tools  
**Linux**: `sudo apt install build-essential python3-dev`  
**macOS**: `xcode-select --install`

## License

MIT