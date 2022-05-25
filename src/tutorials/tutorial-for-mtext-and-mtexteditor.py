import ezdxf

doc = ezdxf.new('R2007', setup=True)
msp = doc.modelspace()

"""
lorem_ipsum = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum.
'''

mtext = msp.add_mtext(lorem_ipsum, dxfattribs={'style': 'TimeNewRomanRegular'})
mtext.text += 'Append additional text to the MText entity.'
mtext += 'Append additional text to the MText entity.'
mtext.dxf.char_height = 3
mtext.dxf.width = 60
"""

# Mtext formatting
'''
mtext = msp.add_mtext('{\\C1;red text} - {\\C3;green text} - {\\C5;blue text}', dxfattribs={'style': 'TimeNewRomanRegular'})
'''

# Stacked text
'''
mtext = msp.add_mtext('\\A1;\\SUpper^ Lower; - \\SUpper/ Lower;} - \\SUpper# Lower;', dxfattribs={'style': 'TimeNewRomanRegular'})
'''

# Background color(filling)
"""
text = lorem_ipsum = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum.
'''
mtext = msp.add_mtext(text, dxfattribs={'style': 'TimeNewRomanRegular'})
mtext.set_bg_color(2, scale=1.5)
"""

# MTextEditor
from ezdxf.tools.text import MTextEditor

text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, ... see prolog code
'''
NP = MTextEditor.NEW_PARAGRAPH
ATTRIBS = {
    'char_height': 0.7,
    'style': 'OpenSans',
    'width': 10,
}
editor = MTextEditor(text + NP)
mtext = msp.add_mtext(str(editor), dxfattribs={'style': 'TimeNewRomanRegular'})

doc.saveas('output/mtext.dxf')
