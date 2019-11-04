# Chaulagain, Sameer
# sxc8268
# 2019-10-22
#---------#---------#---------#---------#---------#--------#
INDENT_STR = '  '

#---------#---------#---------#---------#---------#--------#
def dumpHeaderLine( indent, lineNum, contents, fp ) :
  print( f'({lineNum:4d}) '+(INDENT_STR*indent)+contents, file = fp )

#---------#---------#---------#---------#---------#--------#
