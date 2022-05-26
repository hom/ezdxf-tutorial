import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_circle((0, 0), radius=2.5)  # add a CIRCLE entity, not required

dim = msp.add_diameter_dim(
    center=(0, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 0},
)
dim.render()  # always required, but not shown in the following examples

msp.add_circle((10, 0), radius=2.5)
dim1 = msp.add_diameter_dim(
    center=(10, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 1},
)
dim1.render()  # always required, but not shown in the following examples

msp.add_circle((20, 0), radius=2.5)
dim2 = msp.add_diameter_dim(
    center=(20, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 2}
)
dim2.render()  # always required, but not shown in the following examples

msp.add_circle((30, 0), radius=2.5)
dim3 = msp.add_diameter_dim(
    center=(30, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 3}
)
dim3.render()  # always required, but not shown in the following examples

msp.add_circle((40, 0), radius=2.5)
dim4 = msp.add_diameter_dim(
    center=(40, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 4}
)
dim4.render()  # always required, but not shown in the following examples

msp.add_circle((50, 0), radius=2.5)
dim5 = msp.add_diameter_dim(
    center=(50, 0),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 0, "dimtad": 4, "dimtih": 1,}
)
dim5.render()  # always required, but not shown in the following examples

# dimtmove
msp.add_circle((0, 20), radius=2.5)
dim6 = msp.add_diameter_dim(
    center=(0, 20),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 0}
)
dim6.render()

msp.add_circle((10, 20), radius=2.5)
dim7 = msp.add_diameter_dim(
    center=(10, 20),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 1}
)
dim7.render()

msp.add_circle((20, 20), radius=2.5)
dim8 = msp.add_diameter_dim(
    center=(20, 20),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 2}
)
dim8.render()

msp.add_circle((30, 20), radius=2.5)
dim9 = msp.add_diameter_dim(
    center=(30, 20),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 3}
)
dim9.render()

msp.add_circle((40, 20), radius=2.5)
dim10 = msp.add_diameter_dim(
    center=(40, 20),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 4}
)
dim10.render()

msp.add_circle((50, 20), radius=2.5)
dim11 = msp.add_diameter_dim(
    center=(50, 20),
    radius=2.5,
    angle=30,
    dimstyle="EZ_RADIUS_INSIDE",
    override={"dimtmove": 1, "dimtad": 4, "dimtih": 1,}
)
dim11.render()

doc.saveas("output/default_text_locations_inside__diameter.dxf")
