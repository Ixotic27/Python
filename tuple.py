import ezdxf
import math

# Create a new DXF document
doc = ezdxf.new()
msp = doc.modelspace()

# Pentagon properties
edge_length = 25
center = (0, 0, 0)
angle = 72  # Interior angle for regular pentagon

# Generate pentagon vertices in 3D (assuming it starts on HP)
pentagon_3d = []
for i in range(5):
    x = edge_length * math.cos(math.radians(i * angle))
    y = edge_length * math.sin(math.radians(i * angle))
    pentagon_3d.append([x, y, 0])  # Initially on HP (z = 0)

# Rotation matrices
def rotate_x(point, theta):
    """Rotate point around X-axis by theta degrees."""
    x, y, z = point
    theta = math.radians(theta)
    y_new = y * math.cos(theta) - z * math.sin(theta)
    z_new = y * math.sin(theta) + z * math.cos(theta)
    return [x, y_new, z_new]

def rotate_z(point, phi):
    """Rotate point around Z-axis by phi degrees."""
    x, y, z = point
    phi = math.radians(phi)
    x_new = x * math.cos(phi) - y * math.sin(phi)
    y_new = x * math.sin(phi) + y * math.cos(phi)
    return [x_new, y_new, z]

# Apply first rotation (60° about X-axis)
pentagon_rotated_x = [rotate_x(p, 60) for p in pentagon_3d]

# Apply second rotation (45° about Z-axis)
pentagon_final = [rotate_z(p, 45) for p in pentagon_rotated_x]

# Project onto 2D (ignore Z values)
pentagon_2d = [(x, y) for x, y, _ in pentagon_final]

# Draw the pentagon in DXF
for i in range(5):
    x1, y1 = pentagon_2d[i]
    x2, y2 = pentagon_2d[(i + 1) % 5]  # Loop back to first point
    msp.add_line(start=(x1, y1), end=(x2, y2))

# Save DXF file
dxf_filename = "pentagon_projection.dxf"
doc.saveas(dxf_filename)
print(f"DXF file saved as {dxf_filename}")
