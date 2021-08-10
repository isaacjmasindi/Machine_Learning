
import math

import random

import matplotlib.pyplot as plt

import csv	




#this function will be used to read the information from the csv file
def Csc_reader(file_name):
	
    with open(file_name, 'r') as datafile:
		
        data = csv.reader(datafile)
		
        countrie_info = []
        
        #this for loop will be used to append the data from the file into a list 
		
        for i in data:
			
            countrie_info.append(i) 
		
        return countrie_info[1:]

# this function will be used to convert the numbers from strings to float 
def Convert_list(country_info):
	
    data_info = []
	
    #this for loop will be used to append a list with strings numbers to a new list with float numbers 
    
    for i in country_info:
		
        data_info.append([ i[0], float(i[1]), float(i[2]) ])
	
    return data_info # return original list, but with numbers converted from string to float

#this function will be used to create a new list that only stores the numbers of  life expectency and birth rate
def numbers_list(Converted_list):
	
    numbers_list = []
    
    #this for loop  will be used to append only the numbers of life expectency and birth rate into a new list 
	
    for i in Converted_list :
		
        numbers_list.append([ (i[1]), (i[2]) ])
	
    return(numbers_list)  


def Clusters(list_countries, centriods,number_loops,num_itrate):
   
    Cluster_list = []

    #this for loop will be used to create the list for the clusters

    for i in centroids:
        Cluster_list.append([])
    
    #this for loop will be used to store only the x and y coordinates 
    for l in list_countries:
        x_y = [l[1], l[2]]
        
        distance_value = []
        
        #this nested for loop will be used to calculate the distance between the X values and Y values using the Euclidean formula
        # #the distances will then be appended into the list
        for c in centriods:
            distance = math.pow( math.pow(x_y[1] - c[1], 2)  +   math.pow(x_y[0] - c[0], 2),  0.5)
            
            distance_value.append(distance)
    
        #The closest disatnce varible will store the the index of the minium disatnce which is the closest distance 
        closest_distance = distance_value.index(min(distance_value))
        
        Cluster_list[closest_distance].append(l)
        
    #this if statment will be excuted if the for loop is done and returns the cluster_list so that the list could be used to print and plot
    if number_loops==num_itrate:
        return Cluster_list
    
    return centroids
	


#the file name can be either of the 3
filename = "databoth.csv"

k_value=int(input("\nplease enter the number of clusters you would like to cluster the countries into:  "))

num_itrate=int(input("\nPlease enter the number of iterations: "))

File_info=Csc_reader(filename)

converted_list=Convert_list(File_info)

x_y_list=numbers_list(converted_list)

#centroid varible will store randomly selected x and y values from the list 
centroids = random.sample(x_y_list, k_value) 
X_centriods=[]
Y_centriods=[]
for i in centroids:
    X_centriods.append([i[0]])
    Y_centriods.append([i[1]])

number_loops=1
for i in range(0,num_itrate):
	
    Clusters_list = Clusters(converted_list, centroids, number_loops,num_itrate)	
    
    number_loops+=1


#this for loop will be used to print out the countries in each cluster,the mean of the Birthate and life expectancy
#!NB the cluster are divded by ==============when being pring as there are alot of countries
for i in range(len(Clusters_list)):
    Country_sum=0
    
    print("\n=============================================\nCluster " + str(i + 1) + ": ")
    
    #this for loop will print the country names
    for j in Clusters_list[i]:
        print("\n",j[0])
    
    sum_of_x = 0
    
    #this for loop will be used to calculate the Birthate sum so that the mean is caculated 
    for j in Clusters_list[i]:
        Country_sum+=1
        
        sum_of_x += j[1]
   
    print("\nMean of Birthate",sum_of_x / len(Clusters_list[i]))
    
    sum_of_y = 0
    
    #this for loop will be used to calculate the expectancy sum so that the mean is caculated 
    for j in Clusters_list[i]:
        sum_of_y += j[2]
   
    print("\nMean of life expectancy",sum_of_y / len(Clusters_list[i]))
        
    print("\nSum of countries is :", Country_sum)

count=1
#this for loop will be used to plot the cluster on the graph
for i in range(len(Clusters_list)):
   
    X = []
    
    Y = []
    
    #this for loop will be used to to get the X and Y coorindites and appended to the lists
    for j in range(len(Clusters_list[i])):
       
        X.append(Clusters_list[i][j][1])
        
        Y.append(Clusters_list[i][j][2])
    #this will plot the birthrate and life expectancy 
    plt.scatter(X, Y,label="Cluster number"+str(count))
    
    count += 1

#this will plot the centriods on to the graph that has the clusters 
plt.scatter(X_centriods,Y_centriods,marker="*",color="black")

plt.legend()  

plt.show()






