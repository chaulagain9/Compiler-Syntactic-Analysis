# Chaulagain, Sameer
# sxc8268
# 2019-10-22
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Write() :
  def __init__( self, lineNum,exprList ) :
    self.m_NodeType = 'Statement_Write'

    self.m_LineNum   = lineNum
    self.m_ExprList      =exprList
  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (WRITE)', fp )

    dumpHeaderLine( indent+1, self.m_LineNum,f'EXPR LIST [{len(self.m_ExprList)}]', fp )
    for s in self.m_ExprList :
      s.dump( indent+2, fp = fp )
    



#---------#---------#---------#---------#---------#--------#
