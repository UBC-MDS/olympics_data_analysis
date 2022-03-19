# Reflection for Milestone 4

### Has it been easy to use your app?

We aimed to make this app as easy to use for our target audience (general public) as possible. Our attempts to do this included implementing 'guidance' features into the app, such as an 'I need help' collapsable button, and a tooltip on the word 'Density', which explains what this term means.

### What we have implemented in your dashboard so far:

#### For both R and Python Dashboards:

The dashboard is for both R and Python Dashboard are similar, although the Python app is more developed and is visually more appealing.

We have implemented three plots, which are:

1.  `Number of medals won by each country` world map
2.  `Number of Gold, Silver and Bronze medals across Gender` bar plot
3.  `Number of medals across Age` histogram
4.  Data table showing aggregated features by team (Only DashPy app)

#### Changes made in the Python Dashboard:

We have taken the feedback of our peers and TA and implemented the following changes:

1.  [Included a drop down button, `I need help`, which tells the user how they can use the app. Included a tooltip to explain the term `density`](https://github.com/UBC-MDS/olympics_data_analysis/commit/de3f57cd7ee455bc99167816abf4f928ea31fa1f)
2.  [Converted the age distribution from bar chart to a density plot](https://github.com/UBC-MDS/olympics_data_analysis/commit/03dd216d05f3aae6a33bc5887e28afbb681774d5)
3.  [Added a `Data` tab where the user can filter and look at tabular data that is used to make the dashboard](https://github.com/UBC-MDS/olympics_data_analysis/commit/85e0160dfc09412b5edb17395e2ac54f0c7e70cb)
4.  [Improved the description tab and added the clickable link to the github repo](https://github.com/UBC-MDS/olympics_data_analysis/commit/de3f57cd7ee455bc99167816abf4f928ea31fa1f)
5.  [Changed the theme to `Minty`](https://github.com/UBC-MDS/olympics_data_analysis/commit/4ba94f8d3b24eca1e1acdec09f3a34877929c1e5)
6.  [We added cards to improve the layout of the app](https://github.com/UBC-MDS/olympics_data_analysis/commit/7e8b06a9e2222509d820a2704fe3b989bdac0c87)

#### Differences between DashR and DashPy app:

The the DashR app does not contain many of the aesthetic improvements that we made for the DashPy app. For example, we did not have time to include the 'I need help' collapsable button or the `Density` tooltip, which act as guides for the users. This means that our DashPy app is more visually appealing and likely more usable for our target audience compared to the DashR app. Additionally, we did not have time to include the data table tab, which was another important addition to our DashPy app.

#### Are there reoccurring themes in your feedback on what is good and what can be improved?

There is no particular theme in the feedback. We planned to include the `Country` filter to go along with the other filters, but we could not implement this feature because it required complex wrangling of the data at different levels for each graph and it became too complicated to complete within the given time contraint. 

#### Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?

The suggestion for the Data table was helpful and we found the TA's suggestion about implementing a `Country` drop down menu very valuable, although we regrettably did not have enough time to complete this feature. 

#### What are potential improvements and additions

If we had more time in the future, we have a couple of potential additions or editions in mind:

-   We look to continually make cosmetic improvements in the plots such as font size, color schemes and titles, as well as the dashboard as a whole

-   Add a country filter for both the DashR and DashPy app

-   Include a Data tab in the DashR app
