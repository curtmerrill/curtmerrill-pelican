title: Shutting down Indego+Status Board
date: 2017-02-02
tags: projects


While I was living in Philadelphia, the city launched a bike share program,
[Indego](http://rideindego.com). I signed up early and used it regularly
to get from my apartment in Society Hill to [CityCoHo](http://www.citycoho.com/), 
where I was renting a desk.

![Indego key fob]({attach}indego-fob.jpg)

I had played around with Status Board, but hadn’t had much of a use for 
it until I found the
[API for the status of the bike share stations](https://www.rideindego.com/about/data/).
It didn’t happen often, but it was annoying to get to a station and find
that there are no bikes to check out, or no docks available to return a bike.

Since I used the same stations regularly, it seemed like a good use case
of Status Board: I could create a table showing the available bikes and
docks for my favorite stations and check it whenever I was about to head out.

So I created [Indego+Status Board](http://bikes.scurt.me).

I built the site using [Flask](http://flask.pocoo.org/). The index page
calls the bike share API to create a map of stations. You can click on
stations to add them to your list and then view them in Status Board
or in the browser. 

The data are collected the same way for both Status Board and the HTML view.
The URL contains a list of station IDs as part of the query string. When
the Flask route is called, it fetches the station data from the API, loops
through the stations to find the ones with the right IDs and then renders a 
simple HTML table with the requested data.

The [Status Board table](https://github.com/curtmerrill/indego-statusboard/blob/master/templates/table.html)
has very little styling—the app has a table style already—just enough to
align the blue and gray bars. 

![Status Board screenshot]({attach}status-board-screenshot.png)

I used it pretty regularly, though, and it was useful for me. There were a
couple of times that I could see that the station nearest my apartment was
full, so I knew to use an alternate on my way home. 

But then I moved out of Philly and [Panic announced they were shutting
down Status Board](https://panic.com/blog/the-future-of-status-board/), so
now seems like a good time to retire this project and save myself a few
bucks a month by powering down the droplet[^1].

The [code is on GitHub](https://github.com/curtmerrill/indego-statusboard) if you’d like to run your own version. And it turns
out that other bike share programs have data APIs, so it could be adapted.
For instance:

  * [CitiBike](https://www.citibikenyc.com/system-data) (New York)
  * [Capital Bikeshare](https://www.capitalbikeshare.com/system-data) (Washington, D.C.)
  * [Santander Cycle](https://api.tfl.gov.uk/bikepoint) (London)


[^1]: If you’re looking for a cloud server, I’ve been happy with
    [Digital Ocean](https://m.do.co/c/3e6472201e1a). If you use this link to
    sign up, you’ll get $10 in credit. If you keep your account for a while,
    I get a referral discount.
