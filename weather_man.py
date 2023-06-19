from pathlib import Path
import pandas as pd
import os



class CityWeather:
    c_data_path=[]
    def __init__(self, c_name, folder_path):
        self.c_data_path=[os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]  #folder_path = './Weather man/Dubai_weather/'
        self.c_name=c_name
             
    def get_file_of_year(self,year):
        year_file=[]
        for path in self.c_data_path:
            if year in path:
                year_file.append(path)
        return year_file
            
    def get_all_file_of_month(self,month):
        month_file=[]
        for path in self.c_data_path:
            if month in path:
                month_file.append(path)
        return month_file
                
    def get_month_in_year(self,year,month):
        print(year, month)
        year_paths=self.get_file_of_year(year)
        for path in year_paths:
            if month in path:
                return path
  

    def get_high_low_tem_mostHumidity_day(self,year,code):
        high_temp=0
        low_temp=0
        most_hum=0
        ht_date=""
        lt_date=""
        mh_date=""
        paths=self.get_file_of_year(year)
        for path in paths:
            df=pd.read_csv(path)
            #finding max temperature in file along with day
            maxtem=df["Max TemperatureC"].max()
            date=df.loc[df["Max TemperatureC"].idxmax(),code]
            #print(date)
            #checking and storing 
            if maxtem>high_temp:
                high_temp=maxtem
                ht_date=date  
            #finding min temperature in file along with day
            mintem=df["Min TemperatureC"].min()
            date=df.loc[df["Min TemperatureC"].idxmin(),code]
            #checking and storing 
            if mintem<low_temp:
                low_temp=mintem
                lt_date=date
            #finding Most Humidity in file along with day
            maxhum=df["Max Humidity"].max()
            date=df.loc[df["Max Humidity"].idxmax(),code]
            #checking and storing 
            if maxhum>most_hum:
                most_hum=maxhum
                mh_date=date
        print(f"\nHighest Temperature is: {high_temp} and date is: {ht_date}")
        print(f"\nLowest Temperature is: {low_temp} and date is: {lt_date}")
        print(f"\nMost Humidity is: {most_hum} and date is: {mh_date}")
        
    def avg_htem_ltem_hum_for_month(self,year,month):
        path=self.get_month_in_year(year,month)
        df=pd.read_csv(path)
        avghtem=round(df["Max TemperatureC"].mean(),2)
        avgltem=round(df["Min TemperatureC"].mean(),2)
        avghum=round(df["Max Humidity"].mean(),2)
        print(f"Average Highest Temperature is: {avghtem}")
        print(f"Average Lowest Temperature is: {avgltem}")
        print(f"Average Most Humidity Temperature is: {avghum}")
        
    def bar_chart_of_days(self,year,month):
        path=self.get_month_in_year(year,month)
        df=pd.read_csv(path)
        highest_tem=df["Max TemperatureC"]
        lowest_tem=df["Min TemperatureC"]
        for i in range(0,len(highest_tem)-1):
            print("Day:",i+1)
            print('\033[91m+\033[0m'*int(highest_tem[i]))
            print('\033[94m+\033[0m'*int(lowest_tem[i]))
            print("\n")

    def bar_chart_of_month(self,year,month):
        path=self.get_month_in_year(year,month)  #\033[94m  \033[0m
        df=pd.read_csv(path) 
        highest_tem=df["Max TemperatureC"]
        lowest_tem=df["Min TemperatureC"]        
        for i in range(0,len(highest_tem)-1):
            print(f"Day:{i+1}","\033[94m+\033[0m"*int(lowest_tem[i])+'\033[91m+\033[0m'*int(highest_tem[i]))
            print("\n") 
        


def check_month_input(month):
    mm=""
    
    input_dict={
        "Jan":["jan","Jan",0o1,1,"1","01","one","January","january"],
        "Feb":["feb","Feb",0o2,2,"2","02","february","February"],
        "Mar":["mar","Mar",0o3,3,"3","03","march","March"],
        "Apr":["apr","Apr",0o4,4,"4","04","april","April"],
        "May":["may","May",0o5,5,"5","05","may","May"],
        "Jun":["jun","Jun",0o6,6,"6","06","june","June"],
        "Jul":["jul","Jul",0o7,7,"7","07","july","July"],
        "Aug":["aug","Aug",8,"8","08","august","August"],
        "Sep":["sep","Sep",9,"9","09","september","September"],
        "Oct":["oct","Oct",0o10,10,"10","october","October"],
        "Nov":["nov","Nov",0o11,11,"11","november","November"],
        "Dec":["dec","Dec",0o12,12,"12","december","December"]
    }
    for key, value_list in input_dict.items():
        if month in value_list:
            #return key
            mm=key
    while mm not in input_dict.keys():
        month=str(input("Enter Right Month (like July,july,7,07): "))
        for key, value_list in input_dict.items():
            if month in value_list:
                #return key
                mm=key
    return mm

def menu():
    print("""
          ------------------------------------Welcome to Weather Man--------------------------------\n
          1. For a given year show the highest, lowest temperature and most Humidity along its day
          2. For given month display the average of all highest, lowest temperature and most humidity
          3. For given month it display a 2-bar(1st for High_temp, 2nd for low_temp) for each day
          4. For given month it display a single bar for each day in a month
          """)

def checker(inpt,down_limit,up_limit):
    while int(inpt)<down_limit or int(inpt)>up_limit:
        inpt=input(f"Please enter your choice from {down_limit} to {up_limit}: ")
    return inpt
 
def select_country():
    print("""
          -------Select country-----
          1. Dubai
          2. Lahore
          3. Murree
          """)

def return_city(country):
    if country==1:
        dubai=CityWeather("Lahore",'./Weather man/Dubai_weather/')
        return dubai
    elif country==2:
        lahore=CityWeather("Lahore",'./Weather man/lahore_weather/')
        return lahore
    elif country==3:
        murree=CityWeather("Lahore",'./Weather man/Murree_weather/')
        return murree
        
    
def operation(choice,year,month,obj,code):
    
    if (choice==1):
        obj.get_high_low_tem_mostHumidity_day(year,code)
    elif choice==2:
        obj.avg_htem_ltem_hum_for_month(year,month)
    elif choice==3:
        obj.bar_chart_of_days(year,month)
    elif choice==4:
        obj.bar_chart_of_month(year,month)



if __name__=="__main__":
    
    menu()
    
    choice=int(input(("Enter your choice: ")))
    checker(choice,1,4)
    
    select_country()
    
    country=int(input("Select the country: "))
    checker(country,1,3)
    
    obj=return_city(country)
    
    year=str(input("Enter the Year (like 2007): "))
    mnth=str(input("Enter the name of month (like Jul): "))
    month=check_month_input(mnth)
    
    if country==1:
        operation(choice,year,month,obj,"GST")
    else:
        operation(choice,year,month,obj,"PKT")
    
    

