import ezdxf

doc = ezdxf.new("R2018", setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()

'''
msp.add_text('A Simple Text').set_pos((2, 3), align='MIDDLE_RIGHT')

msp.add_text('Text Style Example: Liberation Serif',
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 0.35
             }).set_pos((2, 6), align='LEFT')
'''

doc.styles.new('SimSun', dxfattribs={'font': 'simsun.ttf'})
msp.add_text("AC", dxfattribs={}).set_pos((10, 10))
msp.add_text("AC", dxfattribs={
    "height": 4,
    "style": "SimSun",
}).set_pos((0, 0))

msp.add_lwpolyline([(0, 0), (0, 4), (4, 4), (4, 0)], close=True, dxfattribs={
    "color": 4,
})
doc.saveas('output/simple_text.dxf')
