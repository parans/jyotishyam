#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_general.py -- module General. All general computations for any chart [D1-D60 charts]
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

import generic.mod_constants as c

###############################################################################
##                                  DATA                                     ##
###############################################################################
nakshatras = [  "Ashwini", "Bharani", "Kritika", 
                "Rohini", "Mrigashira", "Ardra", 
                "Punarvasu", "Pushya", "Ashlesha", 
                "Magha", "Purva Phalguni", "Uttara Phalguni", 
                "Hasta", "Chitra", "Swati", 
                "Vishaka", "Anurada", "Jyeshta", 
                "Mula", "Purva Ashadha", "Uttara Ashadha", 
                "Shravana", "Dhanishta", "Shatabhishak", 
                "Purva Bhadrapada", "Uttara Bhadrapada", "Revati" ]

nakshatra_rulers = [    "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", 
                        "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", 
                        "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", ]

nakshatra_dieties = [   "Ashwini kumaras", "Yama", "Agni", 
                        "Bramha", "Soma", "Rudra", 
                        "Aditi", "Brihaspathi", "Nagas", 
                        "Pitris", "Aryaman", "Bhaga", 
                        "Surya", "Vishwakarma", "Vaayu", 
                        "Indra - Agni", "Mitra", "Indra", 
                        "Niriti", "Apah", "Vishwe Devatas", 
                        "Vishnu", "Ashta Vasu", "Varuna", 
                        "Ajikapada", "Ahir Budhyana", "Pushan" ]

signs = [ "Aries",       "Taurus",    "Gemini",   "Cancer",
          "Leo",         "Virgo",     "Libra",    "Scorpio",
          "Saggitarius", "Capricorn", "Aquarius", "Pisces",
        ]

rashis = ["Mesha",       "Vrushaba",  "Mithuna",  "Karka",
          "Simha",       "Kanya",     "Tula",     "Vruschika",
          "Dhanu",       "Makara",    "Kumbha",   "Meena",
         ]

signlords = [ "Mars",    "Venus",     "Mercury",  "Moon",
              "Sun",     "Mercury",   "Venus",    "Mars",
              "Jupiter", "Saturn",    "Saturn",   "Jupiter",
            ]

signtatvas = [  c.FIRE, c.EARTH, c.AIR, c.WATER,
                c.FIRE, c.EARTH, c.AIR, c.WATER,
                c.FIRE, c.EARTH, c.AIR, c.WATER,
             ]

planets = [ "Sun",      "Moon",     "Mars",
            "Mercury",  "Jupiter",  "Venus",
            "Saturn",   "Rahu",     "Ketu"
          ]

exhaltation_signs = [   "Aries",        "Taurus",       "Capricorn",
                        "Virgo",        "Cancer",       "Pisces",
                        "Libra",        "Taurus",       "Scorpio"
                    ]

debilitation_signs = [  "Libra",        "Scorpio",      "Cancer",
                        "Pisces",       "Capricorn",    "Virgo",
                        "Aries",        "Scorpio",      "Taurus"
                     ]

diety_of_nakshatra = dict(zip(nakshatras, nakshatra_dieties))
ruler_of_nakshatra = dict(zip(nakshatras, nakshatra_rulers))
lord_of_sign       = dict(zip(signs, signlords))
lord_of_rashi      = dict(zip(rashis, signlords))
tatva_of_sign      = dict(zip(signs, signtatvas))
tatva_of_rashi     = dict(zip(rashis, signtatvas))
exhaltationSign_of_planet  = dict(zip(planets, exhaltation_signs))
debilitationSign_of_planet = dict(zip(planets, debilitation_signs))

###############################################################################
##                              lamda functions                              ##
###############################################################################

signnum = lambda signstr: signs.index(signstr) + 1

###############################################################################
##                                 APIs                                      ##
###############################################################################
def housediff(fromsign, tosign):
  ''' Computes how many houses is difference between froimsign to to sign
      This function is sed to compute housenumber for planets too '''
  if(tosign > fromsign):
    house = tosign - fromsign + 1
  elif(tosign < fromsign):
    house = 12 + tosign - fromsign + 1
  else: #same signs
    house = 1 #first house
  return house

def compute_nthsign(fromsign, n):
    s = (fromsign + n - 1) % 12
    if (s == 0):
        s = 12
    return (s)

def compute_nthsign_backwards(fromsign, n):
    s =  (12 + fromsign - n + 1) % 12
    if (s == 0):
        s = 12
    return (s)

def compute_aspects4planet(planetname,aspectnum,division):
    ''' Computes the aspects of each planet in planet group and 
        updates its Aspects elements - planets, signs and houses '''
    planetgroup = division["planets"]
    planet = planetgroup.get(planetname, "NOT_FOUND")
    if (planet != "NOT_FOUND"):
        #if planet is present. Compute its aspects
        houseno = planet["house-num"]
        signno = signnum(planet["sign"])
        aspecthousenum = compute_nthsign(houseno, aspectnum)
        planet["Aspects"]["houses"].append(aspecthousenum) #nth house aspect
        planet["Aspects"]["signs"].append(signs[compute_nthsign(signno, aspectnum)-1]) #nth sign aspect
        planets = get_planets_in_house(aspecthousenum, division["planets"])
        for p in planets:    
            planet["Aspects"]["planets"].append(p)
    else:
        print(planetname + " Not found in planet group.")
    return

def compute_aspects(division):
    ''' Computes the aspects of each planet in planet group and 
        updates its Aspects elements - planets, signs and houses '''
    # Sun aspects 7th house
    compute_aspects4planet("Sun", 7, division)
    # Moon aspects 7th house
    compute_aspects4planet("Moon", 7, division)
    # Mars aspects 4th house
    compute_aspects4planet("Mars", 4, division)
    # Mars aspects 7th house
    compute_aspects4planet("Mars", 7, division)
    # Mars aspects 8th house
    compute_aspects4planet("Mars", 8, division)
    # Mercury aspects 7th house
    compute_aspects4planet("Mercury", 7, division)
    # Jupiter aspects 5th house
    compute_aspects4planet("Jupiter", 5, division)
    # Jupiter aspects 7th house
    compute_aspects4planet("Jupiter", 7, division)
    # Jupiter aspects 9th house
    compute_aspects4planet("Jupiter", 9, division)
    # Venus aspects 7th house
    compute_aspects4planet("Venus", 7, division)
    # Saturn aspects 3rd house
    compute_aspects4planet("Saturn", 3, division)
    # Saturn aspects 7th house
    compute_aspects4planet("Saturn", 7, division)
    # Saturn aspects 10th house
    compute_aspects4planet("Saturn", 10, division)
    # Rahu aspects 5th house
    compute_aspects4planet("Rahu", 5, division)
    # Rahu aspects 7th house
    compute_aspects4planet("Rahu", 7, division)
    # Rahu aspects 9th house
    compute_aspects4planet("Rahu", 9, division)
    # Ketu aspects 5th house
    compute_aspects4planet("Ketu", 5, division)
    # Ketu aspects 7th house
    compute_aspects4planet("Ketu", 7, division)
    # Ketu aspects 9th house
    compute_aspects4planet("Ketu", 9, division)
    return

def compute_aspectedby(division):
    ''' Computes the aspects on each planet in planet group '''
    planetgroup = division["planets"]
    for planetname in planetgroup:
        planet = planetgroup[planetname]    #geteach planet sturcuture
        house_no = planet["house-num"]
        for p in division["houses"][house_no - 1]["aspect-planets"]:
            planet["Aspected-by"].append(p)
    return

def compute_conjuncts(division):
    ''' Computes the conjuncted planets of each planet in planet group '''
    planetgroup = division["planets"]
    for planetname in planetgroup:
        planet = planetgroup[planetname]    #geteach planet sturcuture
        house_no = planet["house-num"]
        for p in division["houses"][house_no - 1]["planets"]:
            planet["conjuncts"].append(p)
        planet["conjuncts"].remove(planetname)
    return



def get_planets_in_house(houseno, planetgroup):
    houseplanets = []
    for planetname in planetgroup:
        planet = planetgroup[planetname]
        if (planet["house-num"] == houseno):
            houseplanets.append(planet["name"])
    return houseplanets


def update_houses(division):
    ''' Computes the houses properties for each house like
        planets in house
        house sign and sign number with rashi
    '''
    
    for housenum in range(1, 13):   #house 1 to 12
        house = {"planets"      : [],
                 "house-num"    : 0,
                 "sign-num"     : 0,
                 "sign"         : "Aries",
                 "sign-lord"    : "Aries",
                 "rashi"        : "Mesha",
                 "aspect-planets": []
                }        

        #get planets sitting in that house
        planets = get_planets_in_house(housenum, division["planets"])
        for planet in planets:    
            house["planets"].append(planet)

        #put house number
        house["house-num"] = housenum

        #get sign of the house
        mysignnum = compute_nthsign(signnum(division["ascendant"]["sign"]),housenum)
        house["sign-num"] = mysignnum
        house["sign"] = signs[mysignnum - 1]
        house["sign-lord"] = signlords[mysignnum - 1]
        house["rashi"] = rashis[mysignnum - 1]

        #compute planets which are aspecting this house
        #all planets will have 7th aspect.So add planets in 7th from it
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,7), division["planets"])
        for planet in planets:    
            house["aspect-planets"].append(planet)
        #Mars has 4th aspect. so check if mars is present in 4 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,4), division["planets"])
        if ("Mars" in planets):
            house["aspect-planets"].append("Mars")
        #Mars has 8th aspect. so check if mars is present in 8 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,8), division["planets"])
        if ("Mars" in planets):
            house["aspect-planets"].append("Mars")
        #Saturn has 3rd aspect. so check if saturn is present in 3 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,3), division["planets"])
        if ("Saturn" in planets):
            house["aspect-planets"].append("Saturn")
        #Saturn has 10th aspect. so check if saturn is present in 10 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,10), division["planets"])
        if ("Saturn" in planets):
            house["aspect-planets"].append("Saturn")
        #Jupiter has 5th aspect. so check if jupiter is present in 5 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,5), division["planets"])
        if ("Jupiter" in planets):
            house["aspect-planets"].append("Jupiter")
        #Jupiter has 9th aspect. so check if jupiter is present in 9 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,9), division["planets"])
        if ("Jupiter" in planets):
            house["aspect-planets"].append("Jupiter")
        #Rahu has 5th aspect. so check if Rahu is present in 5 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,5), division["planets"])
        if ("Rahu" in planets):
            house["aspect-planets"].append("Rahu")
        #Rahu has 9th aspect. so check if Rahu is present in 9 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,9), division["planets"])
        if ("Rahu" in planets):
            house["aspect-planets"].append("Rahu")
        #Ketu has 5th aspect. so check if Ketu is present in 5 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,5), division["planets"])
        if ("Ketu" in planets):
            house["aspect-planets"].append("Ketu")
        #Ketu has 9th aspect. so check if Ketu is present in 9 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,9), division["planets"])
        if ("Ketu" in planets):
            house["aspect-planets"].append("Ketu")
        division["houses"].append(house)
    return

if __name__ == "__main__":
    print(signnum("Scorpio"))
    #print(debilitationSign_of_planet)