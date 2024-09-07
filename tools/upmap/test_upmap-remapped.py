import importlib
upmap_remapped = importlib.import_module('upmap-remapped')

def test_upmap_pg_items():
  assert upmap_remapped.upmap_pg_items('1.ba4', [[123, 456]]) == 'ceph osd pg-upmap-items 1.ba4 123 456 &'
  assert upmap_remapped.upmap_pg_items('9.10', [[13, 36], [2, 5], [1, 28]]) == 'ceph osd pg-upmap-items 9.10 13 36 2 5 1 28 &'
  assert upmap_remapped.upmap_pg_items('11.a7d', [[0, 16], [6, 0], [4, 5]]) == 'ceph osd pg-upmap-items 11.a7d 0 16 6 0 4 5 &'

def test_rm_upmap_pg_items():
  assert upmap_remapped.rm_upmap_pg_items('3.14') == 'ceph osd rm-pg-upmap-items 3.14 &'
  assert upmap_remapped.rm_upmap_pg_items('15.1bf8') == 'ceph osd rm-pg-upmap-items 15.1bf8 &'
