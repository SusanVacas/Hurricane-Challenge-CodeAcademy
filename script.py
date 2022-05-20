# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def updates_damages(lista):
    new_list=[]
    for i in lista:
        if 'B' in i:
            i=float(i[:-1])*1000000000
        elif 'M' in i:
            i=float(i[:-1])*1000000
        else:
            i='Damages not recorded'
        new_list.append(i)
    return new_list
print('updates damages are',updates_damages(damages))
damages=updates_damages(damages)


# write your construct hurricane dictionary function here:
dict2={}

for i in range(len(names)):
    dict2[names[i]]={"names":names[i],"months":months[i],"years":years[i], "max_sustained_winds": max_sustained_winds[i],"areas_affected":areas_affected[i],"damages":damages[i],"deaths":deaths[i]}






# write your construct hurricane by year dictionary function here:
years_unique=[]
for a in years:
    if a not in years_unique:
        years_unique.append(a)


dict_years={}
c=0
for i in years_unique:
    for names,records in dict2.items():
        if records["years"]==i:
            if i in dict_years:
                if not isinstance(dict_years[i],list):
                    dict_years[i]=[dict_years[i]]
                dict_years[i].append(records)
            else:
                dict_years[i]=[records]



# write your count affected areas function here:
def AffectedAreas(areas):
    dict_areas={}
    for a in areas:
        for b in a:
            if b not in dict_areas:
                dict_areas[b]=a.count(b)
            else:
                dict_areas[b]=dict_areas.get(b)+1
    return dict_areas

print("Listas de areas afectadas:  ",AffectedAreas(areas_affected))
lista_afectados=AffectedAreas(areas_affected)



# write your find most affected area function here:
def most_affected(affected):
    maximo= max(affected.values())
    area1=[k for k, v in affected.items() if v==maximo]
    area=''.join(area1)
    return area,maximo
print(most_affected(lista_afectados))




# write your greatest number of deaths function here:
def most_deaths(d):
    maximo=max(deaths)
    for name,records in d.items():
        if records['deaths']==maximo:
            return name, maximo
print(most_deaths(dict2))





# write your catgeorize by mortality function here:
dict_mortality_scale={0:[],1:[],2:[],3:[],4:[],5:[]}
for name,records in dict2.items():
    if records["deaths"]== 0:
        dict_mortality_scale[0].append(records)
    elif records["deaths"]>0 and records["deaths"]<=100:
        dict_mortality_scale[1].append(records)
    elif records["deaths"]>100 and records["deaths"]<=500:
        dict_mortality_scale[2].append(records)
    elif records["deaths"]>500 and records["deaths"]<=1000:
        dict_mortality_scale[3].append(records)
    elif records["deaths"] >1000 and records["deaths"] <= 10000:
        dict_mortality_scale[4].append(records)
    else:
        dict_mortality_scale[5].append(records)
print("Dictionary of mortality scale \n",dict_mortality_scale)
# write your greatest damage function here:
def greatest_damage(dictionary):
    list_sin_str=[]
    for m in damages:
        if isinstance(m,float):
            list_sin_str.append(m)
    maximo=max(list_sin_str)
    for name,records in dictionary.items():
        if records["damages"]==maximo:
            return print("El huracan mas costoso ha sido",str(name),"con un costo de",str(maximo),"dolares.")

greatest_damage(dict2)


# write your catgeorize by damage function here:
dict_damages_scale={0:[],1:[],2:[],3:[],4:[],5:[]}
for name,records in dict2.items():
    if isinstance(records["damages"], float):
        if records["damages"]== 0:
            dict_damages_scale[0].append(records)
        elif records["damages"]>0 and records["damages"]<=100000000:
            dict_damages_scale[1].append(records)
        elif records["damages"]>100000000 and records["damages"]<=1000000000:
            dict_damages_scale[2].append(records)
        elif records["damages"]>1000000000 and records["damages"]<=10000000000:
            dict_damages_scale[3].append(records)
        elif records["damages"] >10000000000 and records["damages"] <= 50000000000:
            dict_damages_scale[4].append(records)
        else:
            dict_damages_scale[5].append(records)
print("Dictionary of damages scale \n",dict_damages_scale)