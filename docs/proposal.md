---
editor_options: 
  markdown: 
    wrap: 72
---

# Olympic Events App Proposal

Date: February 14th, 2022

## Motivation and Purpose

*Our role:* Data Scientist Team Hired By an Olympic Media Outlet

*Target audience:* Community members who are interested in the olympics

With the 2022 Beijing Olympics currently underway, community members are
steeped in anticipation for what is to come. The huge diversity of
sports available to watch creates an overwhelming number of statistics
that can be difficult for community members to comprehend. However,
greater accessibility to Olympic data is necessary to inform users'
decisions about what sports to watch at the 2022 Beijing Olympics and
future Olympic games. For example, a community member may want to know
which sport their home country has historically performed better or
worse at since this could influence their decision about what sports to
tune in to in future Olympic games. Our data visualization app aims to
make Olympic data accessible and digestible for community members, and
potentially inform individual watching behaviours at future Olympic
games. Our app will show the distribution of factors contributing to
gold medals in past Olympic games and will allow users to explore
various aspects of this data with ease by filtering and re-ordering on
different variables, such as country, geographical location, and sport.

## Description of the Data

The data used in this project is a historical one on the modern Olympic
Games, including all the Games from Athens 1896 to Rio 2016. The Winter
and Summer Games were held in the same year up until 1992. After that,
they staggered them such that Winter Games occur on a four year cycle
starting with 1994, then Summer in 1996, then Winter in 1998, and so on.

The data is sourced from kaggle which can be found
[here](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results?select=noc_regions.csv).
It has two files `athlete_events.csv` and `noc_regions.csv`. We will be
visualizing a data-set that contains 271116 rows and 15 columns. Each
row is an athlete-event. The ID column can be used to uniquely identify
athletes, since some athletes have the same name. Following are some of
the important features that will displayed on the dashboard. `ID`,
`NAME`, `SEX`, `AGE`, `HEIGHT`, `WEIGHT`, `TEAM`, `COUNTRY`, `GAMES`,
`YEAR`, `SPORT`, `SEASON`, `CITY`, `EVENT` and `MEDAL`.

## Research Question and Usage Scenarios

## Description of the App and Sketch
