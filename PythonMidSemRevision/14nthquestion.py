import shapes

print("--- Testing shapes module calculations ---")

# Square example
s_area, s_perim = shapes.square_metrics(4)
print(f"Square (side=4): Area = {s_area}, Perimeter = {s_perim}")

# Cylinder example
cy_area, cy_vol = shapes.cylinder_metrics(3, 7)
print(f"Cylinder (r=3, h=7): Surface Area = {cy_area:.2f}, Volume = {cy_vol:.2f}")
