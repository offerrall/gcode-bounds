from pathlib import Path

from . import _gcode_parser

__version__ = "1.0.0"

def get_bounding_box(file_path: str | Path) -> tuple[float, float, float, float]:
    """
    Extract bounding box coordinates from a G-code file.
    
    Args:
        file_path: Path to the G-code file (string or Path object)
        
    Returns:
        Tuple of (min_x, max_x, min_y, max_y) rounded to 3 decimal places
        
    Raises:
        FileNotFoundError: If the file doesn't exist or cannot be opened
        ValueError: If no valid X/Y coordinates are found in the file
        
    Example:
        >>> bounds = get_bounding_box("part.nc")
        >>> print(f"Bounds: X({bounds[0]} to {bounds[1]}), Y({bounds[2]} to {bounds[3]})")
    """
    return _gcode_parser.get_bounding_box(str(file_path))

def generate_framing_gcode(min_x: float,
                           max_x: float,
                           min_y: float,
                           max_y: float,
                           power: float = 10.0,
                           speed: int = 1000) -> list[str]:
    """
    Generate G-code for framing a bounding box.
    
    Args:
        min_x, max_x, min_y, max_y: Bounding box coordinates
        power: Laser power percentage (0-100, default: 10.0)
        speed: Feed rate in mm/min (default: 1000)
        
    Returns:
        List of G-code command strings
        
    Raises:
        ValueError: If coordinates or parameters are invalid
    """
    if min_x >= max_x:
        raise ValueError(f"min_x ({min_x}) must be less than max_x ({max_x})")
    if min_y >= max_y:
        raise ValueError(f"min_y ({min_y}) must be less than max_y ({max_y})")
    
    if not (0 <= power <= 100):
        raise ValueError(f"Power must be between 0 and 100, got {power}")
    if speed <= 0:
        raise ValueError(f"Feed rate must be positive, got {speed}")
    
    return [
        f"G0 X{min_x} Y{min_y}",
        f"M3 S{power:.3f} F{speed}",
        f"G1 Y{max_y}",
        f"G1 X{max_x}",
        f"G1 Y{min_y}",
        f"G1 X{min_x}",
        "M5",
        "G0 X0 Y0"
    ]

__all__ = ["get_bounding_box", "generate_framing_gcode"]