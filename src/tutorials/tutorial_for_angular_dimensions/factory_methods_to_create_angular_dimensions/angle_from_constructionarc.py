import ezdxf

doc = ezdxf.new(setup=True)
msp = doc.modelspace()

arc = msp.add_arc(
    center=(0, 0),
    radius=5,
    start_angle = 60,
    end_angle = 120,
)
msp.add_angular_dim_arc(
    arc.construction_tool(),
    distance=2,
).render()

doc.saveas("output/angle_from_constructionarc.dxf")
