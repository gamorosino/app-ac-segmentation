# This file intentionally does not vendor Allen Institute's segment_array.py.
#
# That script is GPLv3-licensed (AllenInstitute/ac_segmentation) and is never
# copied into this repo -- it runs from inside the pinned container image
# (gamorosino/ac-segmentation:latest, built from ac_segmentation's own
# Dockerfile), which keeps its original GPLv3 terms intact. See main and
# _brainlife_run.py for the exact invocation:
#
#   /ac_segmentation/src/ac_segmentation/methods/segment_array.py
#
# Upstream: https://github.com/AllenInstitute/ac_segmentation
