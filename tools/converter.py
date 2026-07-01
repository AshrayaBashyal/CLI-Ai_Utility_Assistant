from typing import Dict, Any

# Multipliers relative to base units (m, g, l)
UNIT_REGISTRY: Dict[str, Dict[str, float]] = {
    "length": {
        "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
        "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344
    },
    "weight": {
        "mg": 0.001, "g": 1.0, "kg": 1000.0, 
        "oz": 28.349523, "lb": 453.59237
    },
    "volume": {
        "ml": 0.001, "l": 1.0, "tsp": 0.004929, "tbsp": 0.014787,
        "fl_oz": 0.029574, "cup": 0.236588, "gal": 3.78541
    },
    "temperature": {"c": 1.0, "f": 1.0, "k": 1.0}
}

def find_category(unit: str) -> str:
    """Finds unit category (length, weight, volume, temperature)."""
    for category, units in UNIT_REGISTRY.items():
        if unit in units:
            return category
    return ""

def convert_temp(val: float, src: str, dest: str) -> float:
    """Handles non-linear temperature formulas using Kelvin base."""
    # Convert to Kelvin
    k = val if src == "k" else (val + 273.15 if src == "c" else (val - 32) * 5/9 + 273.15)
    # Convert from Kelvin to target
    return k if dest == "k" else (k - 273.15 if dest == "c" else (k - 273.15) * 9/5 + 32)

def convert(value: float, from_unit: str, to_unit: str) -> Dict[str, Any]:
    try:
        # Enforce string types and normalize inputs
        src, dest = str(from_unit).lower().strip(), str(to_unit).lower().strip()
        val = float(value)
        
        # Look up categories
        cat_src, cat_dest = find_category(src), find_category(dest)
        
        # Validation checks
        if not cat_src: return {"success": False, "error": {"mesage": f"Invalid unit: '{from_unit}'"}}
        if not cat_dest: return {"success": False, "error": {"mesage": f"Invalid unit: '{to_unit}'"}}
        if cat_src != cat_dest: return {"success": False, "error": {"message": f"Cannot convert {cat_src} to {cat_dest}"}}
        
        # Calculate result
        if cat_src == "temperature":
            result = round(convert_temp(val, src, dest), 2)
        else:
            factors = UNIT_REGISTRY[cat_src]
            result = round((val * factors[src]) / factors[dest], 6)
            
        return {
            "success": True,
            "data": {"value": result, "unit": dest, "category": cat_src}
        }
    except Exception as e:
        return {"success": False, "error": {"message": str(e)}}
