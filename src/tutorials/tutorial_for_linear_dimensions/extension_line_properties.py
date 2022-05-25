import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_line((0, 0), (20, 0))

msp.add_linear_dim(
    base=(3, 2),
    p1=(3, 0),
    p2=(6, 0),
    override={
        "dimclre": 1,  # red
        "dimltex1": "DASHED2",
        "dimltex2": "CENTER2",
        "dimlwe": 35,  # 0.35mm line weight
        "dimexe": 0.3,  # length above dimension line
        "dimexo": 0.1,  # offset from measurement point
    }).render()


dim = msp.add_linear_dim(base=(7, 2), p1=(7, 0), p2=(10, 0))
dim.set_extline_format(color=1, lineweight=35, extension=0.3, offset=0.1)
dim.set_extline1(linetype="DASHED2")
dim.set_extline2(linetype="CENTER2")
dim.render()

msp.add_linear_dim(
    base=(11, 0.4),
    p1=(11, 0),
    p2=(14, 0),
    override={
        "dimfxlon": 1,  # fixed length extension lines
        "dimexe": 0.2,  # length above dimension line
        "dimfxl": 0.4,  # length below dimension line
    }
).render()

dim1 = msp.add_linear_dim(base=(15, 2), p1=(15, 0), p2=(18, 0))
dim1.set_extline_format(extension=0.2, fixed_length=0.4)
dim1.render()

msp.add_linear_dim(
    base=(19, 2),
    p1=(19, 0),
    p2=(22, 0),
    override={
        "dimse1": 1,  # suppress first extension line
        "dimse2": 1,  # suppress second extension line
        "dimblk": ezdxf.ARROWS.closed_filled,  # arrows just looks better
    }
).render()

dim2 = msp.add_linear_dim(base=(23, 2), p1=(23, 0), p2=(26, 0))
dim2.set_arrows(blk=ezdxf.ARROWS.closed_filled)
dim2.set_extline1(disable=True)
dim2.set_extline2(disable=True)
dim2.render()

doc.saveas("output/extension_line_properties.dxf")
