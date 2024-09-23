import importlib
upmap_remapped = importlib.import_module('upmap-remapped')

def test_gen_upmap():
  assert upmap_remapped.gen_upmap([2,11,5,9,20,12], [2,11,5,9,14,12]) == [(20,14)]
  assert upmap_remapped.gen_upmap([6,12,10,0,2,17], [6,12,17,15,2,35]) == [(17,35),(0,15),(10,17)]
  assert upmap_remapped.gen_upmap([16,4,12,6,11,0], [6,20,12,4,11,0]) == [(4,20),(6,4),(16,6)]
  assert upmap_remapped.gen_upmap([7,1,12,2,17,9], [7,0,8,12,4,2]) == [(1,0),(12,8),(2,12),(17,4),(9,2)]
  assert upmap_remapped.gen_upmap([0,2,6,15,4,17], [8,0,6,14,4,2]) == [(0,8),(2,0),(15,14),(17,2)]
  assert upmap_remapped.gen_upmap([11,6,13,16,8,0], [16,6,11,12,4,0]) == [(16,12),(11,16),(13,11),(8,4)]
  assert upmap_remapped.gen_upmap([0,6,2,9,5,11], [8,6,0,2,5,11]) == [(0,8),(2,0),(9,2)]
  assert upmap_remapped.gen_upmap([17,4,7,10,14,2], [16,7,4,11,14,0]) == [(17,16),(10,11),(2,0)]

def test_upmap_pg_items():
  assert upmap_remapped.upmap_pg_items('1.ba4', [[123, 456]]) == 'ceph osd pg-upmap-items 1.ba4 123 456 &'
  assert upmap_remapped.upmap_pg_items('9.10', [[13, 36], [2, 5], [1, 28]]) == 'ceph osd pg-upmap-items 9.10 13 36 2 5 1 28 &'
  assert upmap_remapped.upmap_pg_items('11.a7d', [[0, 16], [6, 0], [4, 5]]) == 'ceph osd pg-upmap-items 11.a7d 0 16 6 0 4 5 &'

def test_rm_upmap_pg_items():
  assert upmap_remapped.rm_upmap_pg_items('3.14') == 'ceph osd rm-pg-upmap-items 3.14 &'
  assert upmap_remapped.rm_upmap_pg_items('15.1bf8') == 'ceph osd rm-pg-upmap-items 15.1bf8 &'
