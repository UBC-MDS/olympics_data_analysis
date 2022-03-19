# Reflection for Milestone 4

### Has it been easy to use your app?

The dashboard is fairly easy to use where the user will get all the help they need with the `About` section and `I need help` drop down button.

### What we have implemented in your dashboard so far:

#### For both R and Python Dashboards:

The dashboard is for both R and Python Dashboard are similar.

We have implemented three plots, which are:

1.  `Number of medals won by each country` world map
2.  `Number of Gold, Silver and Bronze medals across Gender` bar plot
3.  `Number of medals across Age` histogram

#### Changes made in the Python Dashboard:

We have taken the feedback of our peers and TA and implemented the following changes:

1.  [Included a drop down button, `I need help`, which tells the user how they can use the app. Included a tooltip to explain the term `density`](https://github.com/UBC-MDS/olympics_data_analysis/commit/de3f57cd7ee455bc99167816abf4f928ea31fa1f)
2.  [Converted the age distribution from bar chart to a density plot](https://github.com/UBC-MDS/olympics_data_analysis/commit/03dd216d05f3aae6a33bc5887e28afbb681774d5)
3.  [Added a `Data` tab where the user can filter and look at tabular data that is used to make the dashboard](https://github.com/UBC-MDS/olympics_data_analysis/commit/85e0160dfc09412b5edb17395e2ac54f0c7e70cb)
4.  [Improved the description tab and added the clickable link to the github repo](https://github.com/UBC-MDS/olympics_data_analysis/commit/de3f57cd7ee455bc99167816abf4f928ea31fa1f)
5.  [Changed the theme to `Minty`](https://github.com/UBC-MDS/olympics_data_analysis/commit/4ba94f8d3b24eca1e1acdec09f3a34877929c1e5)
6.  [We added cards to improve the layout of the app](https://github.com/UBC-MDS/olympics_data_analysis/commit/7e8b06a9e2222509d820a2704fe3b989bdac0c87)

#### Differences between DashR and DashPy app:

The the DashR app doesn't have the drop down mentioned in the DashPy app along with the data table tab.

#### Are there reoccurring themes in your feedback on what is good and what can be improved?

There is no particular theme in the feedback. We planned to include the `Country` filter to go along with the other filters, but, owing to the time constraint, we could not implement it because that would require wrangling data at different levels for each graph.

#### Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?

The suggestion for the Data table was helpful and we have implemented the same

#### What are potential improvements and additions

If we had more time in the future, we have a couple of potential additions or editions in mind:

-   We look to continually make cosmetic improvements in the plots such as font size, color schemes and titles, as well as the dashboard as a whole

-   Add a country filter for both the DashR and DashPy app

-   Include a Data tab in the DashR app
