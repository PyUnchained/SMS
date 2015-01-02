from django.shortcuts import render

# Create your views here.
import time, datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from cal.models import*
from datetime import date, datetime, timedelta
import calendar
from django.template import loader, Context, RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.forms.models import modelformset_factory

from cal.forms import EventDayForm

mnames = 'January February March April May June July August September October November December'
mnames = mnames.split()


@login_required
def day(request, year = None, month = None, day = None):
    """View the entries for the day"""

    current_user = request.user

    if year == month == day == None:
        year, month, day = time.localtime()[:3]
    
    if request.method == 'POST':
        
        form = EventDayForm(request.POST)
        if form.is_valid():
            allclean = form.cleaned_data

            #create a string suitable to be used by the datetime module
            #using request.POST['date'], since the information for that
            #field is altered by is_valid() method, and so cannot be
            #used
            new_date = datetime_str(request.POST['date'],allclean['time'])

            #Create and save the new event
            new_event = Entry.objects.create(title = allclean['title'],
                date = new_date,
                remind = allclean['remind'],
                creator = current_user,
                body = allclean['body'],
                snippet = allclean['snippet'])

            #Rebuild the list of entries for the day
            all_entries = Entry.objects.filter(
                date__year = year,
                date__month = month,
                date__day = day)
            my_entries = all_entries.filter(creator = request.user)
            other_entries = all_entries.exclude(creator = request.user)

            #Find the name of the current month
            monthtext = mnames[int(month)-1]

            #New blank form
            form = EventDayForm()

            return render_to_response("day.html", dict(
                year = year, month = month, day = day,
                all_entries = other_entries,
                my_entries = my_entries, form = form,
                monthtext = monthtext),
                context_instance = RequestContext(request))


        return render_to_response("day.html",
            dict(year = year, month = month, day = day,
            form = form,),
            context_instance = RequestContext(request))
    
    else:

        all_entries = Entry.objects.filter(
                date__year = year,
                date__month = month,
                date__day = day)
        my_entries = all_entries.filter(creator = request.user)
        all_entries = all_entries.exclude(creator = request.user)
        monthtext = mnames[int(month)-1]

        form = EventDayForm()
        
        return render_to_response("day.html", dict(
                year = year, month = month, day = day,
                monthtext = monthtext, form = form,
                all_entries = all_entries,
                my_entries = my_entries),
                context_instance = RequestContext(request))
                                

@login_required
def month(request,year=None,month=None):
    """Listing of the days in 'month'"""
    
    if month == None:
        month = int(time.localtime()[1])
    
    if year == None:
        year = int(time.localtime()[0])
        
    
            
        
    year = int(year)
    month = int(month)
    
    #If we've gotten to the beginning of the year:
    if month < 1:
        
        #Set the calendar to Dec of the previous year
        month = 12
        year=year-1
    
    #If we've scrolled to the end of the year:
    if month >12:
        
        #Set the calendar to Jan of the next year
        month = 1
        year=year+1
    
    #init variables
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year,month)
    nyear, nmonth, nday = time.localtime()[:3]
    
    lst = [[]]
    week = 0
    
    #make month list of days for each week
    #each day tuple will contain list of entries and 'current' indicator
    for day in month_days:
        entries = current = False  
        #Are there entries for this day, and is it the current day
        if day:
            entries = Entry.objects.filter(date__year = year,
                                        date__month = month,
                                        date__day = day)
            if day == nday and year == nyear and month == nmonth:
                current = True
        
        lst[week].append((day,entries,current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1
    return render_to_response ("month.html", dict(year=year,month=month,
                                                    user = request.user,
                                                    month_days = lst,
                                                    mname = mnames[month-1]))
            

@login_required
def main(request,year=None):
    """Main listing of years and month, with 3 years per page"""
    #Go to previous/next set of years
    if year:year = int(year)
    else:year = time.localtime()[0]
    
    msg = time.localtime()[1]
        
    nowy, nowm = time.localtime()[:2]
    lst = []
    
    #Create a list of months for each year, indicating which ones contain
    #entries and the current month
    for y in [year,year+1,year+2]:
        mlst = []
        for n,month in enumerate(mnames):
            entry = current = False
            
            entries = Entry.objects.filter(date__year = y, date__month = n+1)
            #Check to see if there are any Entries and whether or not there
            #are entries for the current month.
            
            if entries:
                entry= True
            if y == nowy and n+1 == nowm:
                current = True
            
            mlst.append(dict(n=n+1,name=month,entry=entry,current=current))
        lst.append((y,mlst))
    
    return render_to_response( 'main_cal.html',dict(years=lst,msg = msg,user=request.user,year=year))

def datetime_str(date,new_time):
    """
    Forms and returns a date-time object when supplied with strings
    representing the date and time.

    Date - must be in the format mm/dd/yyyy
    Time - must be in the format hh:mm AM/PM or h:mm AM/PM

    """
    
    #if 12 hour clock was used: 
    if new_time.index(':') == 1:
        #add a 'O' to the string.
        new_time = '0'+new_time

        #if the time is in the afternoon:
        if new_time[-2:] == 'PM' or new_time[-2:] == 'pm':

            #add 12 to convert to 24 hr format then remove am or pm
            new_num = str(int(new_time[:2]) + 12)
            new_time = new_num + new_time[2:-3]
        else:
            #just remove am or pm
            new_time = new_time[:-3]

    #if already in 24 hr format:
    else:
        #just remove am or pm
        new_time = new_time[:-3]
    

    #reform the date to YYYY-MM-DD format
    month, day, year = date.split('/')
    date = year + '-' + month + '-' + day
    
    #combine into a single datetime string and return it
    date_string = date +' '+ new_time
    return date_string


