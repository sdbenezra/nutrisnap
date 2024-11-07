# Creates health scale svg files

svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 60">
  <rect width="240" height="60" fill="#f8f9fa" rx="8" />
  <rect x="16" y="18" width="208" height="24" fill="#e9ecef" rx="12" />
  <circle cx="64" cy="30" r="10" fill="#22c55e" />
  <circle cx="120" cy="30" r="10" fill="#fbbf24" />
  <circle cx="176" cy="30" r="10" fill="#ef4444" />
  <text x="64" y="54" text-anchor="middle" font-family="Arial" font-size="10">Healthy</text>
  <text x="120" y="54" text-anchor="middle" font-family="Arial" font-size="10">Moderate</text>
  <text x="176" y="54" text-anchor="middle" font-family="Arial" font-size="10">Low</text>
  {indicator}
</svg>"""

# Store indicator positions for different ratings
indicators = {
    'healthy': '<path d="M 54 8 L 74 8 L 64 16 Z" fill="#000000"/>',
    'moderate': '<path d="M 110 8 L 130 8 L 120 16 Z" fill="#000000"/>',
    'low': '<path d="M 166 8 L 186 8 L 176 16 Z" fill="#000000"/>'  # renamed from 'unhealthy'
}

def get_health_scale_svg(rating='moderate'):
    """Generate SVG with indicator at specified rating position
    
    Args:
        rating (str): One of 'healthy', 'moderate', or 'low'
        
    Returns:
        str: Complete SVG with indicator positioned appropriately
    """
    rating = rating.lower()
    if rating not in indicators:
        raise ValueError("Rating must be one of: 'healthy', 'moderate', 'low'")
        
    return svg_template.format(indicator=indicators[rating])


def save_svg(rating='moderate', filename='health_scale.svg'):
    """Save the health scale SVG to a file
    
    Args:
        rating (str): One of 'healthy', 'moderate', or 'low'
        filename (str): Output filename
    """
    svg_content = get_health_scale_svg(rating)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)


def main():
    save_svg('healthy', 'healthy_scale.svg')
    save_svg('moderate', 'moderate_scale.svg')
    save_svg('low', 'low_scale.svg')