from Trajectory import Trajectory, TimeGeometryPair

from intervaltree import Interval, IntervalTree #we use the intervaltree library
import math

class GIT:
    sf_xmin = 0
    sf_xmax = 0
    sf_ymin = 0
    sf_ymax = 0
    delta_x = 0
    delta_y = 0

    def __init__(self, sf_xmin, sf_xmax, sf_ymin, sf_ymax, delta_x, delta_y):
        self.sf_xmin = sf_xmin #minimum x-coordinator value for the spatial framework
        self.sf_xmax = sf_xmax #maximum x-coordinator value for the spatial framework
        self.sf_ymin = sf_ymin #minimum y-coordinator value for the spatial framework
        self.sf_ymax = sf_ymax #maximum y-coordinator value for the spatial framework
        self.delta_x = delta_x #step size for grid cells in x-dimension
        self.delta_y = delta_y #step size for grid cells in y-dimension

        #Now we need nx and ny for spatial grid
        self.nx = math.ceil((self.sf_xmax - self.sf_xmin)/ self.delta_x) + 1 #nx = ⌈(sf_xmax-sf_xmin) / Δx⌉

        self.ny = math.ceil((self.sf_ymax - self.sf_ymin)/ self.delta_y) + 1 #ny = ⌈(sf_ymax-sf_ymin) / Δy⌉

        self.grid = {} # initialize the grid dictionary for temporal_extent

        self.trajectory = {} # initialize the trajectory dictionary for spatial_extent

            #Insertion Query temporal
    def insert(self, traj):
        for tgp in traj.tgpairs:
            #inserting t1 and t2 in the key of the grid dictionary
            t_start, t_end = tgp.temporal_extent
            # check if this temporal extent already exists in the grid
            if (t_start, t_end) not in self.grid:
                self.grid[(t_start, t_end)] = [] # if not, create a new list
            # add the trajectory ID to the list corresponding to this temporal extent
            self.grid[(t_start, t_end)].append(traj.traj_id)

#-----------------------------------------------------------------------------------------------------------------------------------------
    #Deletion Query
    #We consider it as the boolean to find out it is inside the dictionary or not and if it is existed inside the dictionary then we remove it
    #delete one of the trajectories by ID
    def delete_by_id(self, traj_id: str) -> bool:
      deleted = False
      for key, value in list(self.grid.items()):
        if traj_id in value:
            value.remove(traj_id)
            deleted = True
        if not value:
            del self.grid[key]
      return deleted

#-----------------------------------------------------------------------------------------------------------------------------------------
    #Temporal_Window Query 
    #In this part we are given two (orderd) time points (t1,t2) that is the time range. We will find the trajectories that overlap with the given box. 
    def t_window(self, t1, t2):
        results = []
        for key in self.grid:
            if key[0] <= t2 and key[1] >= t1:
                results.append (self.grid[key])
        return results

#-----------------------------------------------------------------------------------------------------------------------------------------
    #Insertion Query for sp_window query
    def insert_trajectory(self, traj):
        for tgp in traj.tgpairs:
            #inserting x and y in the key of the trajectory dictionary
            x, y = tgp.spatial_extent
            # check if this temporal extent already exists in the trajectory
            if (x, y) not in self.trajectory:
                self.trajectory[(x, y)] = [] # if not, create a new list
            # add the trajectory ID to the list corresponding to this temporal extent
            self.trajectory[(x, y)].append(traj.traj_id)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
    #Spatial Window query, given two coordinators (x1,y1), (x2,y2). We also need the trajectory dictionary that is consis of spatial_extent 
    #as the key values and values as the trajectory id
    def sp_window (self, x1, y1, x2, y2, dictionary_spatial_extent):

      dictionary_spatial_extent_list_keys = dictionary_spatial_extent.keys()
      list1 = list(dictionary_spatial_extent_list_keys)
      #We need to find the range of the grid cells that are intersects with the bounding box
      start_x = math.floor((min(x1, x2) - self.sf_xmin) / self.delta_x)
      #print (start_x) 
      end_x = math.ceil((max(x1, x2) - self.sf_xmin) / self.delta_x)
      #print (end_x) 
      start_y = math.floor((min(y1, y2) - self.sf_ymin) / self.delta_y)
      #print (start_y) 
      end_y = math.ceil((max(y1, y2) - self.sf_ymin) / self.delta_y)
      #print (end_y) 

      list_range = [] #Creating a list of the range of grid cells that are intersects with the bounding box

      #build the list for the range of grid cells that are intersects with the bounding
      for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
          cell_id = (i, j)
          list_range.append (cell_id)
          # Return the set of intersecting trajectory IDs

      result_sp_window_list = [t for t in list1 if t in list_range]

      print (result_sp_window_list)

      final_list_results = []

      for t in result_sp_window_list:
      # check if the tuple is a key in the dictionary
        if t in dictionary_spatial_extent:
            # if it is, print the corresponding value (list of ids)
            final_list_results.append (dictionary_spatial_extent[t])

      result = []
      for sub_list in final_list_results:
         result.append(sub_list[0])
      return (result)

    def st_window(self, t1, t2, x1, y1, x2, y2, dictionary_spatial_extent):
      results = []
      for key in self.grid:
            if key[0] <= t2 and key[1] >= t1:
                results.append (self.grid[key])
      
      print (results)

      dictionary_spatial_extent_list_keys = dictionary_spatial_extent.keys()
      list2 = list(dictionary_spatial_extent_list_keys)

      #We need to find the range of the grid cells that are intersects with the bounding box
      start_x = math.floor((min(x1, x2) - self.sf_xmin) / self.delta_x)
      #print (start_x) 
      end_x = math.ceil((max(x1, x2) - self.sf_xmin) / self.delta_x)
      #print (end_x) 
      start_y = math.floor((min(y1, y2) - self.sf_ymin) / self.delta_y)
      #print (start_y) 
      end_y = math.ceil((max(y1, y2) - self.sf_ymin) / self.delta_y)
      #print (end_y) 

      list_range = [] #Creating a list of the range of grid cells that are intersects with the bounding box

      #build the list for the range of grid cells that are intersects with the bounding
      for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
          cell_id = (i, j)
          list_range.append (cell_id)
          # Return the set of intersecting trajectory IDs

      #print (list_range)

      result_st_window_list = [t for t in list2 if t in list_range]

      #print (result_st_window_list)

      final_list_results = []

      for t in result_st_window_list:
      # check if the tuple is a key in the dictionary
        if t in dictionary_spatial_extent:
            # if it is, print the corresponding value (list of ids)
            final_list_results.append (dictionary_spatial_extent[t])
      print (final_list_results)
      common_elements = [element for element in results if element in final_list_results]
      result = []
      for sub_list in common_elements:
         result.append(sub_list[0])
      return (result) 
