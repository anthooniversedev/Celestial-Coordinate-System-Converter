import math as m 
from math import *

ob = 23.4392911

while True:
    print("Press A to convert Horizontal To Equatorial Coordinates")
    print("Press B to convert Equatorial To Horizontal Coordinates")
    print("Press C to convert Equatorial To Ecliptic Coordinates")
    print("Press D to convert Ecliptic To Equatorial Coordinates")
    response = str(input("Response: "))

    if response == "A":
        class Hor2Eq:
            print("Welcome to the Horizontal to Equatorial Coordinates Converter")
            alt = float(input("Insert Altitude:"))
            az = float(input("Insert Azimuth:"))
            lat = float(input("Insert North Latitude:"))
            sid = float(input("Insert Local Sidereal Time:"))

            #Display of unknown parameters
            print("\nRequired:\n Declination = ? \n Hour Angle = ?\n Right Ascension = ?")

            print("\nFinal Answer: ")
            #Formula for Declination
            sin_dec = m.sin(m.radians(alt)) * m.sin(m.radians(lat)) + m.cos(m.radians(alt)) * m.cos(m.radians(lat)) * m.cos(m.radians(az))
            xdec = m.asin(sin_dec)
            dec = m.degrees(xdec)

            def deg_min_sec(dec):
                if type(dec) != 'float':
                    try:
                        dec = float(dec)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(dec))
                        return 0
                minutes = dec % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(dec)), int(floor(minutes)), seconds)

            print ("Declination(d,m,s): " + deg_min_sec(dec))

            #Formula for Hour Angle
            num_ha = m.sin(m.radians(alt)) - m.sin(m.radians(dec)) * m.sin(m.radians(lat))
            den_ha = m.cos(m.radians(dec)) * m.cos(m.radians(lat))
            cos_ha = num_ha / den_ha
            xha = m.acos(cos_ha)
            ha = m.degrees(xha) / 15

            def deg_min_sec(ha):
                if type(ha) != 'float':
                    try:
                        ha = float(ha)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(ha))
                        return 0
                minutes = ha % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(ha)), int(floor(minutes)), seconds)

            print ("Hour Angle(h,m,s): " + deg_min_sec(ha))

            #Formula for Right Ascension
            ra = sid - ha
            def deg_min_sec(ra):
                if type(ra) != 'float':
                    try:
                        ra = float(ra)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(ra))
                        return 0
                minutes = ra % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(ra)), int(floor(minutes)), seconds)

            print ("Right Ascension(h,m,s): " + deg_min_sec(ra))
    

    if response == "B":
        class Eq2Hor:
            #User input of parameters
            print("Welcome to the Equatorial to Horizontal Coordinates Converter")
            ra = float(input("Insert Right Ascension: "))
            dec = float(input("Insert Declination: "))
            sid = float(input("Insert Local Sidereal Time: "))
            lat = float(input("Insert North Latitude: "))

            #Display of unknown parameters
            print("\nRequired: \n  Altitude = ? \n  Azimuth = ?")
            print("\nFinal Answer: ")
            #Formula for Altitude
            ha = (sid - ra) * 15
            sin_alt = m.sin(m.radians(dec)) * m.sin(m.radians(lat)) + m.cos(m.radians(dec)) * m.cos(m.radians(lat)) * m.cos(m.radians(ha))
            xalt = m.asin(sin_alt)
            alt = m.degrees(xalt)

            def deg_min_sec(alt):
                if type(alt) != 'float':
                    try:
                        alt = float(alt)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(alt))
                        return 0
                minutes = alt % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(alt)), int(floor(minutes)), seconds)

            print ("Altitude(d,m,s): " + deg_min_sec(alt))

            #Formula for Azimuth
            num_az = m.sin(m.radians(ha)) * m.cos(m.radians(dec))
            den_az = m.cos(m.radians(alt))
            sin_az = -(num_az/den_az)
            xaz = m.asin(sin_az)
            az = m.degrees(xaz)

            def deg_min_sec(az):
                if type(az) != 'float':
                    try:
                        az = float(az)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(az))
                        return 0
                minutes = az % 1.0 * 60
                seconds = round(minutes % 1.0 * 60, 2)

                return '\n%s°%s\'%s"\n' % (int(floor(az)), int(floor(minutes)), seconds)

            print ("Azimuth(d,m,s): " + deg_min_sec(az))

    if response == "C":
        class Eq2Ec:
            #User input of parameters
            print("Welcome to the Equatorial to Ecliptic Coordinates Converter")
            ra = float(input("Insert Right Ascension: "))
            dec = float(input("Insert Declination: "))

            #Display of Unknown Parameters
            print("\nRequired: \n  Ecliptic Longitude = ? \n Ecliptic Latitude = ?")
            print("\nFinal Answer: ")

            #Formula for Ecliptic Longitude
            ra = ra * 15
            num_eclong = m.sin(m.radians(ra)) * m.cos(m.radians(ob)) + m.tan(m.radians(dec)) * m.sin(m.radians(ob))
            den_eclong = m.cos(m.radians(ra))
            tan_eclong = num_eclong / den_eclong
            xeclong = m.atan(tan_eclong)
            eclong = m.degrees(xeclong)

            def deg_min_sec(eclong):
                if type(eclong) != 'float':
                    try:
                        eclong = float(eclong )
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(eclong))
                        return 0
                minutes = eclong % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(eclong)), int(floor(minutes)), seconds)

            print ("Ecliptic Longitude(d,m,s): " + deg_min_sec(eclong))

            #Formula for Ecliptic Latitude
            sin_eclat1 = m.sin(m.radians(dec)) * m.cos(m.radians(ob))
            sin_eclat2 = m.cos(m.radians(dec)) * m.sin(m.radians(ob)) * m.sin(m.radians(ra))
            sin_eclat = sin_eclat1 - sin_eclat2
            xeclat = m.asin(sin_eclat)
            eclat = m.degrees(xeclat)

            def deg_min_sec(eclat):
                if type(eclat) != 'float':
                    try:
                        eclat = float(eclat)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(eclat))
                        return 0
                minutes = eclat % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(eclat)), int(floor(minutes)), seconds)

            print ("Ecliptic Latitude(d,m,s): " + deg_min_sec(eclat))
        
    if response == "D":
        class Ec2Eq:
            #User input of parameters
            print("Welcome to the Ecliptic to Equatorial Coordinates Converter")
            eclong = float(input("Insert Ecliptic Longitude: "))
            eclat = float(input("Insert Ecliptic Latitude: "))

            #Display of Unknown Parameters
            print("\nRequired: \n Right Ascension = ? \n Declination = ?")
            print("\nFinal Answer: ")

            #Formula for Right Ascension
            num_ra = m.sin(m.radians(eclong)) * m.cos(m.radians(ob)) - m.tan(m.radians(eclat)) * m.sin(m.radians(ob))
            den_ra = m.cos(m.radians(eclong))
            tan_ra = (num_ra / den_ra)
            xra = m.atan(tan_ra)
            ra = m.degrees(xra) / 15

            def deg_min_sec(ra):
                if type(ra) != 'float':
                    try:
                        ra = float(ra)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(ra))
                        return 0
                minutes = ra % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(ra)), int(floor(minutes)), seconds)

            print("Right Ascension(h,m,s): " + deg_min_sec(ra))
            
        

            #Formula for Declination
            sin_dec = m.sin(m.radians(eclat)) * m.cos(m.radians(ob)) + m.cos(m.radians(eclat)) * m.sin(m.radians(ob)) * m.sin(m.radians(eclong))
            xdec = m.asin(sin_dec)
            dec = m.degrees(xdec)

            def deg_min_sec(dec):
                if type(dec) != 'float':
                    try:
                        dec = float(dec)
                    except:
                        print
                        '\nERROR: Could not conveart %s to float.' % (type(dec))
                        return 0
                minutes = dec % 1.0 * 60
                seconds = round(minutes % 1.0 * 60,2)

                return '\n%s°%s\'%s"\n' % (int(floor(dec)), int(floor(minutes)), seconds)

            print("Declination(d,m,s): " + deg_min_sec(dec))
            


    print("You done bro?")
    jexit = input(print("Convert More? (Y/N)\n "))

    if jexit == "Y":
        print("Commencing...")
        continue
    else:
        break
   
