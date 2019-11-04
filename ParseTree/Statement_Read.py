# Chaulagain, Sameer
# sxc8268
# 2019-10-22
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Read() :
  def __init__( self, lineNum,idList ) :
    self.m_NodeType = 'Statement_Read'

    self.m_LineNum   = lineNum
    self.m_IdList      =idList
  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (READ)', fp )

    dumpHeaderLine( indent+1, self.m_LineNum,f'ID LIST [{len(self.m_IdList)}]', fp )
    for s in self.m_IdList :
      s.dump( indent+2, fp = fp )
    



#---------#---------#---------#---------#---------#--------#
