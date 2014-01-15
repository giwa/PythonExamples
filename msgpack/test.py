import msgpack

print 'list'
packed = msgpack.packb([1,2,3])
print packed
unpack = msgpack.unpackb(packed, use_list=False)
print unpack

print 'dict'
packed = msgpack.packb({'f/oo':1, 'b/az':2, 'bar':3})
print packed
unpack = msgpack.unpackb(packed, use_list=False)
print unpack
