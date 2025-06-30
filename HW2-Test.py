from Trajectory import Trajectory, TimeGeometryPair
from GIT import GIT
from intervaltree import Interval, IntervalTree #we use the intervaltree library
import math

#Insertion Query 
#print test case 1
tgpairs1 = TimeGeometryPair(temporal_extent=(1, 10), spatial_extent=(2, 3)),
tgpairs2 = TimeGeometryPair(temporal_extent=(5, 15), spatial_extent=(4, 5)),
tgpairs3 = TimeGeometryPair(temporal_extent=(20, 30), spatial_extent=(30, 30)),
tgpairs4 = TimeGeometryPair(temporal_extent=(40, 50), spatial_extent=(40, 40)),


t1 = Trajectory(traj_id="pardis_1", tgpairs=tgpairs1)
t2 = Trajectory(traj_id="pardis_2", tgpairs=tgpairs2)
t3 = Trajectory(traj_id="pardis_3", tgpairs=tgpairs3)
t4 = Trajectory(traj_id="pardis_4", tgpairs=tgpairs4)
git_index1 = GIT(sf_xmin=0, sf_xmax=10, sf_ymin=0, sf_ymax=10, delta_x=10, delta_y=10)

git_index1.insert(t1)
git_index1.insert(t2)
git_index1.insert(t3)
git_index1.insert(t4)

#test case 1 for the insertion query
print ("test case 1 Insertion")
print(git_index1.grid)

#print test case 2
tgpairs1 = TimeGeometryPair(temporal_extent=(1, 2), spatial_extent=(10, 10)),
tgpairs2 = TimeGeometryPair(temporal_extent=(3, 14), spatial_extent=(20, 20)),
tgpairs3 = TimeGeometryPair(temporal_extent=(5, 6), spatial_extent=(30, 30)),
tgpairs4 = TimeGeometryPair(temporal_extent=(7, 8), spatial_extent=(40, 40)),


t1 = Trajectory(traj_id="pardis_1", tgpairs=tgpairs1)
t2 = Trajectory(traj_id="pardis_2", tgpairs=tgpairs2)
t3 = Trajectory(traj_id="pardis_3", tgpairs=tgpairs3)
t4 = Trajectory(traj_id="pardis_4", tgpairs=tgpairs4)
git_index2 = GIT(sf_xmin=1, sf_xmax=5, sf_ymin=1, sf_ymax=5, delta_x=20, delta_y=20)

git_index2.insert(t1)
git_index2.insert(t2)
git_index2.insert(t3)
git_index2.insert(t4)

#test case 2 for the insertion query
print ("test case 2 Insertion")
print(git_index2.grid)

print ('---------------------------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#delete one of the trajectories by ID
#test case 1
print ("test case 1 Deletion")
deleted = git_index2.delete_by_id("pardis_1")

if deleted:
    print("Trajectory deleted successfully")
    print(git_index2.grid)
else:
    print("Trajectory not found")

#test case 2
print ("test case 2 Deletion")
deleted = git_index2.delete_by_id("pardis_5")
if deleted:
    print("Trajectory deleted successfully")
    print(git_index2.grid)
else:
    print("Trajectory not found")

print ('---------------------------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Temporal_Window_Query 
#test case 1
print ("test case 1 Temporal_Window_Query")
results_tWindow = git_index1.t_window(25, 45) #Shoud return pardis_3 and pardis_4

if results_tWindow:
    print("Temporal trajectory overlap find successfully")
    print(results_tWindow)
else:
    print("Temporal trajectory overlap")

#test case 2
print ("test case 2 Temporal_Window_Query")
results_tWindow = git_index1.t_window(60, 70) #Shoud return nothing

if results_tWindow:
    print("Temporal trajectory overlap find successfully")
    print(results_tWindow)
else:
    print("Temporal trajectory overlap not find")

print ('---------------------------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#test case 1 for sp_window query
#This part is for building a trajectory dictionary for sp_window() query so we can compare it with cells that are overlapping we also give 
#new tgpairs for our code

print ("test case 1 sp_window query")

tgpairs1 = TimeGeometryPair(temporal_extent=(1, 2), spatial_extent=(2, 3)),
tgpairs2 = TimeGeometryPair(temporal_extent=(3, 14), spatial_extent=(4, 5)),
tgpairs3 = TimeGeometryPair(temporal_extent=(5, 6), spatial_extent=(30, 30)),
tgpairs4 = TimeGeometryPair(temporal_extent=(7, 8), spatial_extent=(40, 40)),


t1 = Trajectory(traj_id="pardis_1", tgpairs=tgpairs1)
t2 = Trajectory(traj_id="pardis_2", tgpairs=tgpairs2)
t3 = Trajectory(traj_id="pardis_3", tgpairs=tgpairs3)
t4 = Trajectory(traj_id="pardis_4", tgpairs=tgpairs4)
git_index3 = GIT(sf_xmin=0, sf_xmax=10, sf_ymin=0, sf_ymax=10, delta_x=5, delta_y=5)

git_index3.insert_trajectory(t1)
git_index3.insert_trajectory(t2)
git_index3.insert_trajectory(t3)
git_index3.insert_trajectory(t4)

#check for the trajectory build successfully
print(git_index3.trajectory)

dictionary_spatial_extent = git_index3.trajectory

result_sp_window = git_index3.sp_window(10, 10, 30, 30, dictionary_spatial_extent)

print (result_sp_window)

#test case 2 for sp_window query
#This part is for building a trajectory dictionary for sp_window() query so we can compare it with cells that are overlapping we also give 
#new tgpairs for our code

print ("test case 2 sp_window query")

tgpairs1 = TimeGeometryPair(temporal_extent=(1, 2), spatial_extent=(2, 3)),
tgpairs2 = TimeGeometryPair(temporal_extent=(3, 14), spatial_extent=(4, 5)),
tgpairs3 = TimeGeometryPair(temporal_extent=(5, 6), spatial_extent=(11, 15)),
tgpairs4 = TimeGeometryPair(temporal_extent=(7, 8), spatial_extent=(6, 8)),


t1 = Trajectory(traj_id="pardis_1", tgpairs=tgpairs1)
t2 = Trajectory(traj_id="pardis_2", tgpairs=tgpairs2)
t3 = Trajectory(traj_id="pardis_3", tgpairs=tgpairs3)
t4 = Trajectory(traj_id="pardis_4", tgpairs=tgpairs4)
git_index3 = GIT(sf_xmin=0, sf_xmax=10, sf_ymin=0, sf_ymax=10, delta_x=2, delta_y=2)

git_index3.insert_trajectory(t1)
git_index3.insert_trajectory(t2)
git_index3.insert_trajectory(t3)
git_index3.insert_trajectory(t4)

#check for the trajectory build successfully
print(git_index3.trajectory)

dictionary_spatial_extent = git_index3.trajectory

result_sp_window = git_index3.sp_window(10, 10, 30, 30, dictionary_spatial_extent)

print (result_sp_window)

print ('---------------------------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#test case 1 for st_window query
print ("test case 1 st_window query")
tgpairs1 = TimeGeometryPair(temporal_extent=(0, 10), spatial_extent=(1, 1)),
tgpairs2 = TimeGeometryPair(temporal_extent=(5, 15), spatial_extent=(4, 5)),
tgpairs3 = TimeGeometryPair(temporal_extent=(20, 30), spatial_extent=(30, 30)),
tgpairs4 = TimeGeometryPair(temporal_extent=(40, 50), spatial_extent=(40, 40)),


t1 = Trajectory(traj_id="pardis_1", tgpairs=tgpairs1)
t2 = Trajectory(traj_id="pardis_2", tgpairs=tgpairs2)
t3 = Trajectory(traj_id="pardis_3", tgpairs=tgpairs3)
t4 = Trajectory(traj_id="pardis_4", tgpairs=tgpairs4)
git_index4 = GIT(sf_xmin=0, sf_xmax=10, sf_ymin=0, sf_ymax=10, delta_x=10, delta_y=10)

git_index4.insert(t1)
git_index4.insert(t2)
git_index4.insert(t3)
git_index4.insert(t4)

#test case 2 for the insertion query
print(git_index4.grid)
dictionary_temporal_extent_list_keys = git_index4.grid.keys()
my_list = list(dictionary_temporal_extent_list_keys)
print (my_list)

git_index4.insert_trajectory(t1)
git_index4.insert_trajectory(t2)
git_index4.insert_trajectory(t3)
git_index4.insert_trajectory(t4)

#check for the trajectory build successfully
print(git_index4.trajectory)
dictionary_spatial_extent_list_keys = git_index4.trajectory.keys()
my_list = list(dictionary_spatial_extent_list_keys)
print (my_list)

dictionary_spatial_extent = git_index4.trajectory

result_st_window = git_index4.st_window(0, 10, 10, 10, 30, 30, dictionary_spatial_extent)

print (result_st_window)

#test case 2 for st_window query
print ("test case 2 st_window query")
tgpairs1 = TimeGeometryPair(temporal_extent=(0, 10), spatial_extent=(1, 1)),
tgpairs2 = TimeGeometryPair(temporal_extent=(5, 15), spatial_extent=(4, 5)),
tgpairs3 = TimeGeometryPair(temporal_extent=(20, 30), spatial_extent=(30, 30)),
tgpairs4 = TimeGeometryPair(temporal_extent=(40, 50), spatial_extent=(40, 40)),


t1 = Trajectory(traj_id="pardis_1", tgpairs=tgpairs1)
t2 = Trajectory(traj_id="pardis_2", tgpairs=tgpairs2)
t3 = Trajectory(traj_id="pardis_3", tgpairs=tgpairs3)
t4 = Trajectory(traj_id="pardis_4", tgpairs=tgpairs4)
git_index4 = GIT(sf_xmin=0, sf_xmax=50, sf_ymin=0, sf_ymax=50, delta_x=1, delta_y=1)

git_index4.insert(t1)
git_index4.insert(t2)
git_index4.insert(t3)
git_index4.insert(t4)

#test case 1 for the insertion query
print(git_index4.grid)
dictionary_temporal_extent_list_keys = git_index4.grid.keys()
my_list = list(dictionary_temporal_extent_list_keys)
print (my_list)

git_index4.insert_trajectory(t1)
git_index4.insert_trajectory(t2)
git_index4.insert_trajectory(t3)
git_index4.insert_trajectory(t4)

#check for the trajectory build successfully
print(git_index4.trajectory)
dictionary_spatial_extent_list_keys = git_index4.trajectory.keys()
my_list = list(dictionary_spatial_extent_list_keys)
print (my_list)

dictionary_spatial_extent = git_index4.trajectory

result_st_window = git_index4.st_window(25, 45, 10, 10, 30, 30, dictionary_spatial_extent)

print (result_st_window)

