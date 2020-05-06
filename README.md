# Celestial Coordinate System Converter
![header](https://scontent.fmnl17-2.fna.fbcdn.net/v/t1.15752-9/95736226_259143208571065_3115483286978166784_n.jpg?_nc_cat=111&_nc_sid=b96e70&_nc_ohc=YOxydQh7PdQAX9WQrmm&_nc_ht=scontent.fmnl17-2.fna&oh=1481d2e5dcc4683e9a49426be0dd45be&oe=5ED9FA14)

## Execution
To execute this program, download the `coordinatesconverter.py` file then run it using your Python3 IDE.

## Contact
markydotes@gmail.com

## Background
This repository is designed to create an automated celestial coordinate system converter using `Python3`. Because the process of calculations by hand is tedious, we tend to design a converter programatically.

A **Celestial Coordinate System** is a reference system used to define the positions of objects on the **celestial sphere**. This is where the positions of planets, stars, satellites, and other celestial bodies are specified. 

For more information about this, see:
* [This resource](https://dept.astro.lsa.umich.edu/resources/ugactivities/Labs/coords/) by SAM & MSO, *University of Michigan
* [This lecture index](https://faculty.virginia.edu/ASTR5610/lectures/COORDS/coords.html) by Steve Majewski, *University of Virginia
* [This book](https://books.google.com.ph/books?id=w5AzyQEACAAJ&dq=astronomical+algorithms&hl=en&sa=X&ved=0ahUKEwjck-yl3Z_pAhUIzTgGHQNxBQMQ6AEIKDAA) by Jean Meeus(1991), *Astronomical Algorithms

In this program, three coordinate systems are included namely: 

* **Horizontal Coordinate System**
* **Equatorial Coordinate System**
* **Ecliptic Coordinate System**

| Coordinate System | Principal Great Circle | Coordinates | 
| --- | --- | --- |
| Horizontal | Observer's horizon | altitude, azimuth | 
| Equatorial | Earth's equator | right ascension, declination |
| Ecliptic | Plane of earth's revolution | ecliptic longitude ,ecliptic latitude |


### Horizontal Coordinate System
The horizontal, or altitude-azimuth, system is based on the position of the observer on Earth, which revolves around its own axis once per sidereal day (23 hours, 56 minutes and 4.091 seconds) in relation to the star background. The positioning of a celestial object by the horizontal system varies with time, but is a useful coordinate system for locating and tracking objects for observers on Earth. It is based on the position of stars relative to an observer's ideal horizon.

### Equatorial Coordinate System
The equatorial coordinate system is centered at Earth's center, but fixed relative to the celestial poles and the March equinox. The coordinates are based on the location of stars relative to Earth's equator if it were projected out to an infinite distance. The equatorial describes the sky as seen from the Solar System, and modern star maps almost exclusively use equatorial coordinates.

The equatorial system is the normal coordinate system for most professional and many amateur astronomers having an equatorial mount that follows the movement of the sky during the night. Celestial objects are found by adjusting the telescope's or other instrument's scales so that they match the equatorial coordinates of the selected object to observe.

Popular choices of pole and equator are the older B1950 and the modern J2000 systems, but a pole and equator "of date" can also be used, meaning one appropriate to the date under consideration, such as when a measurement of the position of a planet or spacecraft is made. There are also subdivisions into "mean of date" coordinates, which average out or ignore nutation, and "true of date," which include nutation.

### Ecliptic System
The fundamental plane is the plane of the Earth's orbit, called the ecliptic plane. There are two principal variants of the ecliptic coordinate system: geocentric ecliptic coordinates centered on the Earth and heliocentric ecliptic coordinates centered on the center of mass of the Solar System.

The geocentric ecliptic system was the principal coordinate system for ancient astronomy and is still useful for computing the apparent motions of the Sun, Moon, and planets.

The heliocentric ecliptic system describes the planets' orbital movement around the Sun, and centers on the barycenter of the Solar System (i.e. very close to the center of the Sun). The system is primarily used for computing the positions of planets and other Solar System bodies, as well as defining their orbital elements.



