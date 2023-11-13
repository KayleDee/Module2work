from django.shortcuts import render
from django.shortcuts import render
from dataclasses import dataclass
# Create your views here.
@dataclass
class Team:
    name: str
    desc: str
    members: list

def homepage(request):
    return render (request, "index.html")

def leadership(request, team):
    if team == "management":
        context = {"mark": Team("Management", 
        "They manage the cleaning supplies and decides who does chores each day.", ["Ab", "Jeremiah", "Abigail", "Owen", "Nick", "Matthew"])}
    elif team == "procurement":
        context = {"mark": Team("Procurement", 
        "They prepare lunches for BCCA and come up with new food ideas.", ["Bryce", "Big John", "Adrian", "Blaine", "Wyatt"])}
    elif team == "documentation":
        context = {"mark": Team("Documentation", 
        "They take pictures, post online about BCCA and makes the yearbook.", ["Blair", "Jay", "Kayleah", "Josh", "Conner", "Kaleigh", "Mina"])}
    elif team == "community":
        context = {"mark": Team("Community", 
        "They plan events for BCCA and set up birthdays", ["Caleb", "Jordan", "Joby", "Aj", "Micah"])}
    return render(request, "team.html", context)


