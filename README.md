
# Olympic Games Analysis Visualization Project

Welcome to our Olympic Games Analysis Dashboard! Our dashboard is currently deployed as a herokuapp [here](https://olympic-dash-app.herokuapp.com/)

We hope you learn something new about the Olympic Games, or that we can inspire you to contribute to our ongoing project.

## Welcome!

* [Here is a quick demo of our app](#app-demonstration)
* [Why Analyze The Olympics?](#motivation)
* [Interested In Contributing?](#contribute-to-the-cause)
* [Get In Touch With Us](#get-in-contact-with-us)
* [Contributing Guidelines](#contributing)
* [License](#license)
* [Reflecting on Our Project](https://github.com/UBC-MDS/olympics_data_analysis/blob/main/docs/reflection-milestone2.md)


## App Demonstration

<p align="center">
  <img width="600" height="400" src="https://media.giphy.com/media/Fsx8KoF0Ko0Q0C0JZm/giphy.gif">
</p>

## Motivation

*Overview*


2022 was another great year of sports at the Olympic Games in Beijing. It is quite incredible to see the countless hours of effort from thousands of athletes manifest at the Olympic Games. For viewers, it may be overwhelming to analyze the large number of statistics available for the Olympic Games over the years. 


This app will provide a dashboard that summarizes a few of the key statistics that we have extracted from this data. Specifically, our dashboard aims to provide accessible visuals that demonstrate the differences in biological sex, geographic location, and the age of athletes and how these factors impact performance within the Olympic Games.

![sketch](https://github.com/UBC-MDS/olympics_data_analysis/blob/main/reports/Dashboard.png)

Our dashboard will contain a global map to give users easy access to the number of medals received by each country at the Olympic Games within a specified year. Specific years, sports, and biological sexes can be selected for by using 3 drop-down menus at the top of the dashboard. This will update the map to show each country's performance within the year, sport, and for the biological sex specified. Note that the default behaviour of each drop down menu is to include the overall data. For example, if the user does not select a specific sport, all sports will be included in the analysis. Additionally, users can interact with the plots by hovering their mouse over the map or the age distribution plot. By hovering their mouse over the map, they can obtain exactly how many medals each country received within the specified filters. By hovering over the age distribution plot, the user can obtain how many medals were received by the athletes of a given age. The users will also be able to see the number of bronze, silver, and gold medals received by both male and female individuals. This plot will be updated based on the sport and year specified by the user.


## Contribute To The Cause

Thank you for your interest in contributing to our project! Here are some instructions to get you started.

*Installation instructions*

### Manually install our app:

Install all of the required dependencies for our application with the following commands:


| Package                     | Command Line                |
|-----------------------------|---------------------------------------|
|         pandas              |         conda install pandas          |
|        numpy            |         pip install altair vega_datasets          |
|        dash              |   conda install -c conda-forge dash   |
|       dash bootstrap components          |     pip install dash-bootstrap-components        |


Next, clone our repository and navigate into the root of our project. You can then run the following command in your terminal to initiate a local version of the application:

```
python src/app.py
```

The app will run in your local host ip and port, which you can open in a browser of your choice.

### Automatically install our app:

Clone our repository and navigate into the root of our project:

```
cd olympics_data_analysis
```
Next, run the following command to automatically install all of the required dependencies:
```
docker-compose up
```
The app will run in your local host ip and port, which you can open in a broswer of your choice

If you think about anything you would like to contribute or improve, don't hesitate to contact us!

## Get In Contact With Us

At any time, you can open an issue in this GitHub repository if you would like to report a bug or provide recommendations to improve the project. Additionally, if you would like to contact us for any other reason, please feel free to do so at kphaterp@student.ubc.ca.

## Contributing

This app is authored by Kiran Phaterpekar, Karanpreet Kaur, Sanchit Singh, Lakshmi Santosha Valli Akella. You can see the list of all contributors in the contributors tab.

We welcome and recognize all contributions. If you wish to participate, please review our [Contributing guidelines](CONTRIBUTING.md)

## License

The app is licensed under the terms of the MIT license.
