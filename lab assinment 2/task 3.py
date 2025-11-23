import math

def calculate_area(shape: str, **kwargs) -> float | str:
    """Calculates the area of various geometric shapes."""
    if shape == "circle":
        return math.pi * kwargs.get("radius", 0)**2
    elif shape == "rectangle":
        return kwargs.get("length", 0) * kwargs.get("width", 0)
    elif shape == "triangle":
        return 0.5 * kwargs.get("base", 0) * kwargs.get("height", 0)
    else:
        return "Unknown shape"

# Example usage:
print(calculate_area("circle", radius=5))
print(calculate_area("rectangle", length=4, width=6))
print(calculate_area("triangle", base=10, height=5))
