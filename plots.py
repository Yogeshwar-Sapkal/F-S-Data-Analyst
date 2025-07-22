import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_population_distribution(df, city, year):
    data = {"Total Estimate":df['Estimate'][0], "Male Estimate": df['Estimate.2'][0], "Female Estimate":df['Estimate.4'][0]}
    total_population = pd.DataFrame(data=data, index=[0])
    cols = ['Total Estimate', 'Male Estimate','Female Estimate']
    total_population[cols] = total_population[cols].apply(lambda x: x.str.replace(",", "").astype(int))
    size = [total_population['Male Estimate'][0],total_population['Female Estimate'][0]]
    labels = [total_population.columns[1],total_population.columns[2]]

    fig, ax = plt.subplots()
    ax.pie(size, labels=labels, autopct='%1.1f%%', startangle=90,
           colors=['cornflowerblue', 'lightgray'])
    ax.axis('equal') 
    fig.suptitle(f'Gender Distribution of {city}, {year}')
    fig.text(0.88, 0.01, "Source: US Census Bureau", ha="left", fontsize=6, color="gray")
    return fig , total_population

def generate_age_wise_distribution(df, city, year):
    data = {"Age":df['Label'][2:20],"Total Estimate":df['Estimate'][2:20],"Male Estimate":df['Estimate.2'][2:20],"Female Estimate":df['Estimate.4'][2:20]}
    Age = pd.DataFrame(data=data)
    cols = ['Female Estimate', 'Male Estimate', 'Total Estimate']
    Age[cols] = Age[cols].apply(lambda x: x.str.replace(",", "").astype(int))
    
    fig1, ax1 = plt.subplots()  # Optional: set figure size
    ax1.bar(Age['Age'], Age['Total Estimate'], color='cornflowerblue')
    ax1.set_xlabel("Age Distribution")
    ax1.set_ylabel("Total Estimate")
    ax1.set_title(f"Age Wise Population Distribution, {city}, {year}")
    ax1.set_xticklabels(Age['Age'], rotation=80)
    fig1.text(0.88, 0.001, "Source: US Census Bureau", ha="left", fontsize=6, color="gray")


    Age['Female Estimate'] = -Age['Female Estimate']
    fig2, ax2 = plt.subplots()
    ax2.barh(Age['Age'], Age['Male Estimate'], color='cornflowerblue', label='Male')
    ax2.barh(Age['Age'], Age['Female Estimate'], color='lightgray', label='Female')
    ax2.set_title(f'Age and Gender Demographics, {city}, {year}')
    ax2.set_xlabel('Population')
    ax2.set_ylabel('Age Group')
    ax2.legend(loc='lower right')
    ax2.grid(axis='x', linestyle='--', alpha=0.7)
    ax2.set_xlim([-4000, 4000])  # Adjust based on your data range
    xticks = range(-4000, 4001, 1000)
    ax2.set_xticks(xticks)
    ax2.set_xticklabels([abs(x) for x in xticks])
    fig2.text(0.88, 0.001, "Source: US Census Bureau", ha="left", fontsize=6, color="gray")
    return fig1, fig2 , Age