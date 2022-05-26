import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_circle((0, 0), radius=2.5)  # add a CIRCLE entity, not required

dim = msp.add_radius_dim(
    center=(0, 0),
    radius=2.5,
    angle=0,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 0, "dimcen": 0,},
)
dim.render()  # always required, but not shown in the following examples

msp.add_circle((6, 6), radius=2.5)
dim1 = msp.add_radius_dim(
    center=(6, 6),
    radius=2.5,
    angle=15,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 0, "dimcen": 0.25,},
)
dim1.render()  # always required, but not shown in the following examples


msp.add_circle((12, 12), radius=2.5)
dim2 = msp.add_radius_dim(
    center=(12, 12),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS",
    override={"dimtad": 0, "dimcen": -0.25,}
)
dim2.render()  # always required, but not shown in the following examples


doc.saveas("output/center_mark_lines.dxf")
