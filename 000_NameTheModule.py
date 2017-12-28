# http://composingprograms.com/pages/16-higher-order-functions.html

originalString = """
Chapter 3: Interpreting Computer Programs
"""

dstString = originalString.replace('  ', '_').replace('.', '_').replace(' ', '').replace(':', '_')

print(dstString)