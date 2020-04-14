#
# Autogenerated by Thrift Compiler (0.12.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Table(object):
    """
    Attributes:
     - col1
     - col2
     - col3

    """


    def __init__(self, col1=None, col2=None, col3=None,):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.LIST:
                    self.col1 = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI64()
                        self.col1.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.col2 = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readDouble()
                        self.col2.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.col3 = []
                    (_etype15, _size12) = iprot.readListBegin()
                    for _i16 in range(_size12):
                        _elem17 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.col3.append(_elem17)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Table')
        if self.col1 is not None:
            oprot.writeFieldBegin('col1', TType.LIST, 2)
            oprot.writeListBegin(TType.I64, len(self.col1))
            for iter18 in self.col1:
                oprot.writeI64(iter18)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.col2 is not None:
            oprot.writeFieldBegin('col2', TType.LIST, 3)
            oprot.writeListBegin(TType.DOUBLE, len(self.col2))
            for iter19 in self.col2:
                oprot.writeDouble(iter19)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.col3 is not None:
            oprot.writeFieldBegin('col3', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.col3))
            for iter20 in self.col3:
                oprot.writeString(iter20.encode('utf-8') if sys.version_info[0] == 2 else iter20)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Table)
Table.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.LIST, 'col1', (TType.I64, None, False), None, ),  # 2
    (3, TType.LIST, 'col2', (TType.DOUBLE, None, False), None, ),  # 3
    (4, TType.LIST, 'col3', (TType.STRING, 'UTF8', False), None, ),  # 4
)
fix_spec(all_structs)
del all_structs