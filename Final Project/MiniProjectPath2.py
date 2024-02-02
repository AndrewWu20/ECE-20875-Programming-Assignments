import pandas
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.api as stats

''' 
The following is the starting code for path2 for data reading to make your first step easier.
'dataset_2' is the clean data for path1.
'''
dataset_2 = pandas.read_csv('NYC_Bicycle_Counts_2016.csv')
brooklyn = dataset_2['Brooklyn Bridge']      = pandas.to_numeric(dataset_2['Brooklyn Bridge'].replace(',','', regex=True))
manhattan = dataset_2['Manhattan Bridge']     = pandas.to_numeric(dataset_2['Manhattan Bridge'].replace(',','', regex=True))
queensboro = dataset_2['Queensboro Bridge']    = pandas.to_numeric(dataset_2['Queensboro Bridge'].replace(',','', regex=True))
williamsburg = dataset_2['Williamsburg Bridge']  = pandas.to_numeric(dataset_2['Williamsburg Bridge'].replace(',','', regex=True))
dataset_2['Williamsburg Bridge']  = pandas.to_numeric(dataset_2['Williamsburg Bridge'].replace(',','', regex=True))


# Question 1

for i in range(0, len(brooklyn)):
    brooklyn[i] = int(brooklyn[i])

for i in range(0, len(manhattan)):
    manhattan[i] = int(manhattan[i])

for i in range(0, len(queensboro)):
    queensboro[i] = int(queensboro[i])

for i in range(0, len(williamsburg)):
    williamsburg[i] = int(williamsburg[i])
 
X = np.zeros(214)
for i in range(214):
    X[i] = i


#Creating subplots of each bridge data

fig, pos = plt.subplots(2,2)
fig.suptitle("Number of Bikes on Each Bridge Per Day")
pos[0,0].plot(X, brooklyn)
pos[0,0].set_title('Brooklyn Bridge')
pos[0,0].set(xlim = (0,214), ylim = (0, 10000))
pos[0,0].set(xlabel = 'Day', ylabel = 'Number of Bikes')

pos[1,0].plot(X, manhattan)
pos[1,0].set_title('Manhattan Bridge')
pos[1,0].set(xlim = (0,214), ylim = (0, 10000))
pos[1,0].set(xlabel = 'Day', ylabel = 'Number of Bikes')

pos[0,1].plot(X, williamsburg)
pos[0,1].set_title('Williamsburg Bridge')
pos[0,1].set(xlim = (0,214), ylim = (0, 10000))
pos[0,1].set(xlabel = 'Day', ylabel = 'Number of Bikes')

pos[1,1].plot(X, queensboro)
pos[1,1].set_title('Queensboro Bridge')
pos[1,1].set(xlim = (0,214), ylim = (0, 10000))
pos[1,1].set(xlabel = 'Day', ylabel = 'Number of Bikes')

plt.show()


#Prints each bridge mean, standard deviation, and variance

print("Brooklyn Bridge Mean: ", np.mean(brooklyn))
print("Brooklyn Bridge Standard Deviation: ", np.std(brooklyn))
print("Brooklyn Bridge Variance: ", np.var(brooklyn))
print("\n")

print("Manhattan Bridge Mean: ", np.mean(manhattan))
print("Manhattan Bridge Standard Deviation: ", np.std(manhattan))
print("Manhattan Bridge Variance: ", np.var(manhattan))
print("\n")

print("Queensboro Bridge Mean: ", np.mean(queensboro))
print("Queensboro Bridge Standard Deviation: ", np.std(queensboro))
print("Queensboro Bridge Variance: ", np.var(queensboro))
print("\n")

print("Williamsburg Bridge Mean: ", np.mean(williamsburg))
print("Williamsburg Bridge Standard Deviation: ", np.std(williamsburg))
print("Williamsburg Bridge Variance: ", np.var(williamsburg))
print("\n")


#Finds the bridges with the closest means and prints them

overall_average_num_of_bikers = ((np.mean(brooklyn) + np.mean(manhattan) + np.mean(queensboro) + np.mean(williamsburg)) / 4)

bridge_list = [('Brooklyn', abs(np.mean(brooklyn) - overall_average_num_of_bikers)), ('Manhattan', abs(np.mean(manhattan) - overall_average_num_of_bikers)), ('Queensboro', abs(np.mean(queensboro) - overall_average_num_of_bikers)), ('Williamsburg', abs(np.mean(williamsburg) - overall_average_num_of_bikers))]

bridge_list.sort(key = lambda x: x[1])

print(f'\nThe three bridges with the most similar number of bikers to the overall average are: {bridge_list[0][0]}, {bridge_list[1][0]}, and {bridge_list[2][0]}\n')


#Question 2

temp_high = list(dataset_2['High Temp'])
temp_low = list(dataset_2['Low Temp'])
precip = list(dataset_2['Precipitation'])

final_total = list(dataset_2['Total'])
final_total = [i.replace(",","") for i in final_total]

for i in range(0, len(final_total)):
    final_total[i] = float(final_total[i])


#Model and graph for riders vs. high temperatures

linear_model_temp_high = np.polyfit(temp_high,final_total,1)
rsquared_temp_high = np.corrcoef(final_total, np.polyval(linear_model_temp_high,temp_high))[0,1]**2
formatted_rsquared_temp_high = "{:.3f}".format(rsquared_temp_high)

M = "{:.3f}".format(linear_model_temp_high[0])
B = "{:.3f}".format(linear_model_temp_high[1])
print("\nM value for high temperature: ", M)
print("B value for high temperature: \n", B)
print("R^2 value for high temperature: \n", formatted_rsquared_temp_high)

plt.figure("Number of Bike Riders vs. High Temperatures")
plt.plot(temp_high, np.polyval(linear_model_temp_high,temp_high), color = 'red')
plt.scatter(temp_high,final_total)
plt.title("Number of Bike Riders vs. High Temperatures")
plt.xlabel('Temperature')
plt.ylabel('Number of Riders')
plt.grid(True)
plt.show()


#Model and graph for riders vs. low temperatures

linear_model_temp_low = np.polyfit(temp_low,final_total,1)
rsquared_temp_low = np.corrcoef(final_total, np.polyval(linear_model_temp_low,temp_low))[0,1]**2
formatted_rsquared_temp_low = "{:.3f}".format(rsquared_temp_low)

M = "{:.3f}".format(linear_model_temp_low[0])
B = "{:.3f}".format(linear_model_temp_low[1])
print("\nM value for low temperature: ", M)
print("B value for low temperature: \n", B)
print("R^2 value for low temperaturee: \n", formatted_rsquared_temp_low)

plt.figure("Bike Riders vs. Lower Temperatures")
plt.plot(temp_low, np.polyval(linear_model_temp_low,temp_low), color = 'red')
plt.scatter(temp_low,final_total)
plt.title("Number of Bike Riders vs. Low Temperatures")
plt.xlabel('Temperature')
plt.ylabel('Number of Riders')
plt.grid(True)
plt.show()


#Model and graph for riders vs. precipitation levels

linear_model_precip = np.polyfit(precip,final_total,1)
rsquared_precip = np.corrcoef(final_total, np.polyval(linear_model_precip,precip))[0,1]**2
formatted_rsquared_precip = "{:.3f}".format(rsquared_precip)

M = "{:.3f}".format(linear_model_precip[0])
B = "{:.3f}".format(linear_model_precip[1])
print("\nM value for precipitation: ", M)
print("B value for precipitation: \n", B)
print("R^2 value for precipitation: \n", formatted_rsquared_precip)

plt.figure("Number of Bike Riders vs. Precipitation")
plt.plot(precip,np.polyval(linear_model_precip,precip), color = 'red')
plt.scatter(precip,final_total)
plt.title("Number of Bike Riders vs. Precipitation")
plt.xlabel('Precipitation')
plt.ylabel('Number of Riders')
plt.grid(True)
plt.show()


# Question 3

week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
Days = list(dataset_2['Day'])
num_total_riders = list(dataset_2['Total'])

num_monday = 31
num_tuesday = 31
num_wednesday = 30
num_thursday = 31
num_friday = 30
num_saturday = 31
num_sunday = 30

week_days_count = [num_monday, num_tuesday, num_wednesday, num_thursday, num_friday, num_saturday, num_sunday]


#Z* values for confidence intervals

Z80 = 1.282
Z90 = 1.645
Z95 = 1.96


#Formatting data and inserting data into arrays

num_riders = {}
filtered = {}
combined = {}
for element in range(0, len(num_total_riders)):
    num_riders[element] = [Days[element], num_total_riders[element]]
for element in week_days:
    filtered[element] = [val for val in num_riders.values() if val[0] == element]
for element in week_days:
    combined[element] = [val[1] for val in filtered[element]]
for element in week_days:
    combined[element] = [int(val.replace(",","")) for val in combined[element]]

complete_day_array = [np.mean(combined['Sunday']), 
                    np.mean(combined['Monday']), 
                    np.mean(combined['Tuesday']), 
                    np.mean(combined['Wednesday']), 
                    np.mean(combined['Thursday']), 
                    np.mean(combined['Friday']), 
                    np.mean(combined['Saturday'])]

mean_riders_sunday = np.mean(combined['Sunday'])
mean_riders_monday = np.mean(combined['Monday'])
mean_riders_tuesday = np.mean(combined['Tuesday'])
mean_riders_wednesday = np.mean(combined['Wednesday'])
mean_riders_thursday = np.mean(combined['Thursday'])
mean_riders_friday = np.mean(combined['Friday'])
mean_riders_saturday = np.mean(combined['Saturday'])


#80% confidence intervals

upper_confidence_interval80 = []

upper_confidence_interval_sun80 = Z80 * np.std(combined['Sunday']) / np.sqrt(num_sunday)
upper_confidence_interval80.append(upper_confidence_interval_sun80)

upper_confidence_interval_mon80 = Z80 * np.std(combined['Monday']) / np.sqrt(num_monday)
upper_confidence_interval80.append(upper_confidence_interval_mon80)

upper_confidence_interval_tue80 = Z80 * np.std(combined['Tuesday']) / np.sqrt(num_tuesday)
upper_confidence_interval80.append(upper_confidence_interval_tue80)

upper_confidence_interval_wed80 = Z80 * np.std(combined['Wednesday']) / np.sqrt(num_wednesday)
upper_confidence_interval80.append(upper_confidence_interval_wed80)

upper_confidence_interval_thu80 = Z80 * np.std(combined['Thursday']) / np.sqrt(num_thursday)
upper_confidence_interval80.append(upper_confidence_interval_thu80)

upper_confidence_interval_fri80 = Z80 * np.std(combined['Friday']) / np.sqrt(num_friday)
upper_confidence_interval80.append(upper_confidence_interval_fri80)

upper_confidence_interval_sat80 = Z80 * np.std(combined['Saturday']) / np.sqrt(num_saturday)
upper_confidence_interval80.append(upper_confidence_interval_sat80)


plt.bar(week_days,complete_day_array, color = 'white', yerr = upper_confidence_interval80, capsize = 10)
plt.scatter(np.arange(len(complete_day_array)),complete_day_array, color = 'red')
plt.title('Riders vs. Day of the week with 80% Confidence Intervals')
plt.xlabel('Day of the week')
plt.ylabel('Riders')
plt.grid(True)
plt.show()



#95% confidence intervals

upper_confidence_interval95 = []

upper_confidence_interval_sun95 = Z95 * np.std(combined['Sunday']) / np.sqrt(num_sunday)
upper_confidence_interval95.append(upper_confidence_interval_sun95)

upper_confidence_interval_mon95 = Z95 * np.std(combined['Monday']) / np.sqrt(num_monday)
upper_confidence_interval95.append(upper_confidence_interval_mon95)

upper_confidence_interval_tue95 = Z95 * np.std(combined['Tuesday']) / np.sqrt(num_tuesday)
upper_confidence_interval95.append(upper_confidence_interval_tue95)

upper_confidence_interval_wed95 = Z95 * np.std(combined['Wednesday']) / np.sqrt(num_wednesday)
upper_confidence_interval95.append(upper_confidence_interval_wed95)

upper_confidence_interval_thu95 = Z95 * np.std(combined['Thursday']) / np.sqrt(num_thursday)
upper_confidence_interval95.append(upper_confidence_interval_thu95)

upper_confidence_interval_fri95 = Z95 * np.std(combined['Friday']) / np.sqrt(num_friday)
upper_confidence_interval95.append(upper_confidence_interval_fri95)

upper_confidence_interval_sat95 = Z95 * np.std(combined['Saturday']) / np.sqrt(num_saturday)
upper_confidence_interval95.append(upper_confidence_interval_sat95)


plt.bar(week_days,complete_day_array, color = 'white', yerr = upper_confidence_interval95, capsize = 10)
plt.scatter(np.arange(len(complete_day_array)),complete_day_array, color = 'red')
plt.title('Riders vs. Day of the week with 95% Confidence Intervals')
plt.xlabel('Day of the week')
plt.ylabel('Riders')
plt.grid(True)
plt.show()