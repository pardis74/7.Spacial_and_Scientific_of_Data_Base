from intervaltree import Interval, IntervalTree #we use the intervaltree library
import math

#We are building a class as a collection of time-geometry-pairs
#We have ti and gi, ti is the temporal extent and gi is the spatial extent
class TimeGeometryPair:
      def __init__(self, temporal_extent, spatial_extent):
            self.temporal_extent = temporal_extent #ti
            self.spatial_extent = spatial_extent #gi

#Here we made a list of time_geometry_pair
class Trajectory:
  def __init__(self, traj_id, tgpairs):
    self.traj_id = traj_id
    self.tgpairs = tgpairs     
  
  def __str__(self):
    return f"{self.traj_id}" # replace as needed

# t1 = Trajectory("John", None)
# print(t1)

#tgpairs1 = TimeGeometryPair(temporal_extent=(1, 10), spatial_extent=(2, 3)),
#tgpairs2 = TimeGeometryPair(temporal_extent=(5, 15), spatial_extent=(4, 5)),
#tgpairs3 = TimeGeometryPair(temporal_extent=(20, 30), spatial_extent=(30, 30)),
#tgpairs4 = TimeGeometryPair(temporal_extent=(40, 50), spatial_extent=(40, 40)),

#t1 = Trajectory(traj_id="pardis_1", tgpairs=tgpairs1)
#t2 = Trajectory(traj_id="pardis_2", tgpairs=tgpairs2)

#print (t1)
#print (t2)
