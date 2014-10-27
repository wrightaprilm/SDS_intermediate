
# coding: utf-8

# #Classes
# 
# We've discussed grouping code by it's function. We can also group objects by their properties. We've talked so far about different kinds of objects. Objects, in Python, have properties. A list, for example, if ordered. This is something that is true about a list, no matter how we call it. 
# 
# Classes allow us to make custom objects with our own needed properties. Classes have what are called **methods**. Methods are functions that allow us to define the properties of our class. These properties are often called **attributes**.
# 

# In[51]:

class Coordinates(object):
    def __init__(self, name):
        self.name = name
    def set_lat(self, lat):
        self.lat = lat
    def set_long(self, long):
        self.long = long
    def set_date(self, date):
        self.date = date


# What we have defined above are four methods: one which initializes the class (*init*), one which sets the longitudes of the class (*set_lat*), one which defines longitudes (*set_long*) and one which defines when the data were collected (*set_date*). This translates to the class having a name, a latitude, a longitude and a date attribute. We can now define these at the command line.
# 

# In[2]:

lat = [43.661476,39.332604,45.703255,43.661476,39.166381,36.802151,37.808381,41.790113,41.744949,51.559882,42.727288,54.980095,53.523454,49.261715,39.32758,48.831673,42.359133,43.47013,44.632261,43.783551,53.948193,59.939959,40.808078,40.428267,37.875928,49.261715,37.8695,54.980095,34.141411,38.831513,51.757137,43.261328,38.648056,32.89533,34.227425,21.300662,55.945328,30.283599,49.261715,41.790113,45.417417,43.469128,49.261715,48.264934,43.647118,48.53698,40.808078,37.228384,49.261715,-33.773636,-37.825328,47.655965,37.875928,38.031441,33.900058,41.744949,22.3101,32.236358,51.524789,-33.929492,53.467102,37.8695,53.478349,48.82629,39.291389,43.07718,52.33399,54.32707,39.07141,37.42949,37.875928,43.64712,51.759865,38.54926,36.00803,50.060833,36.00283,40.03131,42.388889,53.52345,50.937716,42.35076,41.789722,49.276765,32.887151,41.790113,42.3625,30.283599,-43.523333,35.20859,59.939959,30.538978,39.166381,51.377743,37.228384,41.7408,41.70522,47.655,40.443322,44.968657,38.958455,32.30192,43.07718,41.66293,51.457971,43.468889,42.724085,-34.919159,49.261111,-37.9083,34.052778,41.526667,]


# In[3]:

long = [-79.395189,-76.62319,13.718013,-79.395189,-86.526621,-121.788163,-122.267579,-87.600732,-111.804294,-0.133458,-84.482106,-1.614614,-113.525995,-123.25343,-76.620758,2.355623,-71.093201,-80.535771,-63.580263,-79.186397,-1.052914,10.72175,-73.963568,-86.914325,-122.250042,-123.25343,-122.258949,-1.614614,-118.1249,-77.308746,-1.256905,-79.920248,-90.305096,-117.242188,-77.879179,-157.819165,-3.191184,-97.734428,-123.25343,-87.600732,-73.948928,-80.539865,-123.25343,11.669121,-79.3943,9.058935,-73.963568,-80.423417,-123.25343,151.112005,144.951621,-122.309377,-122.250042,-78.499356,35.482727,-111.804294,39.1259,-110.94954,-0.133578,18.865391,-2.233958,-122.258949,-2.241605,2.34642,-76.625,-89.40399,4.86305,10.18265,-77.46427,-122.17186,-122.250042,-79.3943,-1.258648,-121.76709,-78.92323,19.932778,-78.93827,-105.2459,-72.527778,-113.526,-1.395599,-71.06274,-87.599722,-122.917957,-117.246212,-87.600732,-71.085,-97.734428,172.581944,-97.44566,10.72175,114.321928,-86.526621,-2.326378,-80.423417,-111.81416,-86.23531,-122.303333,-79.943583,-93.27457,-95.243284,-90.873352,-89.40399,-91.56203,-2.601474,-80.54,-84.476265,138.60414,-123.253056,145.138,-118.255833,-70.663056,]


# In[4]:

our_coords = Coordinates('our_coords')


# In the above, we've defined the name of our variable to our_coords, with the value our_coords. Defining the name looks a little different than other class definitions, because it is initializing and defining the class. If we call this object, we see the below:
# 

# In[5]:

our_coords


# In[52]:

our_coords.set_lat(lat)
our_coords.set_long(long)
our_coords.set_date('2014-10-27')


# In[53]:

our_coords.date


# This dot notation works because we already have a memory address for this Class. Once initialized, we can just add attributes (that we defined when we set up the class) with this notation. Try looking at a couple attributes. We can also act on these attributes in standard ways:

# In[10]:

sum(our_coords.lat)/len(our_coords.lat)


# OK, so why? We've organized attributes of our code. But so what, would it be worse if our objects were separate? Maybe, maybe not. For complex data structures, this code is readble. We know what, to what, exactly 'lat' and 'long' belong. If we have multiple years of data, we might make each year an instance of the coordinate class. This would spare us having to define lat_2010, lat_2011, lat_2012, lat_2013, lat_2014, long_2010, long_2011, long_2012, long_2013, long_2014, date_2010, date_2011, date_2012, date_2013, date_2014, and keep all that straight. Instead, we have simpler notation of coords_2010.date and so on. 
# 
# Also, consider the following situation: You collected your data one year, but subsequently decided that to collect some data from the previous year.

# In[74]:

class new_coords(Coordinates):
     def __init__(self):
        print("initializing new class")
    def num_of_workshops(self, num):
        self.num = num



# What do we think happened here?  What will happen if we try to access the attributes of our_coords here?

# In[76]:

nc = new_coords()
nc.set_long(long)
nc.num = '113'


# In[77]:

nc.long


# In[78]:

nc.num


# In[ ]:

#Chalenge

+ Create a class called student. What is information an instructor might want about a student? Code this information as an attribute
get_ipython().set_next_input(u'+ Create subclasses for individual students. What might be personalized info an instructor would want about a student');get_ipython().magic(u'pinfo student')


# In[ ]:



