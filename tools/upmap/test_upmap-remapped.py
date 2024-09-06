import importlib
upmap_remapped = importlib.import_module("upmap-remapped")

def test_rm_upmap_pg_items():
  assert upmap_remapped.rm_upmap_pg_items("3.14") == "ceph osd rm-pg-upmap-items 3.14 &"
  assert upmap_remapped.rm_upmap_pg_items("15.1bf8") == "ceph osd rm-pg-upmap-items 15.1bf8 &"
