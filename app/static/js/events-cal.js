$.ajax({
    url: 'https://www.googleapis.com/calendar/v3/calendars/me9gs7qmheh6ofpfn294fikmlk@group.calendar.google.com/events',
    type: 'get',
    data: {
        key: 'AIzaSyCXYss3YMn2IJN12Um9hQyzrU6tzwqbP70',
        singleEvents: true,
        timeMin: (new Date()).toISOString(),
        maxResults: 10,
        orderBy: 'startTime',
    },
    success: function(resp) {
        listUpcomingEvents(resp);
    }
});

function listUpcomingEvents(resp) {
    var events = resp.items;
    var uniq_events = {};
    events.forEach(function(e) {
        if(!(e.summary in uniq_events))
            uniq_events[e.summary] = e;
    });

    // only show events with unique event titles 
    events = Object.keys(uniq_events).map(function(k) {
        return uniq_events[k];
    });

    if (events.length > 0) {
        var events_ul = $('<ul class="events-list"></li>');
        for (i = 0; i < events.length; i++) {
            var event = events[i];
            var when = event.start.dateTime;
            if (!when) {
                when = event.start.date;
            }

            event_li = buildEventListItem(event);
            events_ul.append(event_li);
        } // end for
        $('#calendar').append(events_ul);
    } 
}


function buildEventListItem(event) {
    var sdate = moment(event.start.dateTime);

    var event_date_month_div = $('<div class="month">' + sdate.format('MMM') + '</div>');
    var event_date_date_div = $('<div class="date">' + sdate.format('D') + '</div>');
    var event_date_weekday_div = $('<div class="weekday">' + sdate.format('ddd') + '</div>');
    var event_date_div = $('<div class="event-date"></div>');
    event_date_div.append(event_date_month_div);
    event_date_div.append(event_date_date_div);
    event_date_div.append(event_date_weekday_div);

    var event_description_title = $('<h3 class="event-title">' + event.summary + '</h3>');
    var event_description_location = $('<h4 class="event-location">' + event.location.split(',')[0] + '</h4>');
    var event_description_time = $('<h4 class="event-time">' + sdate.format('h:mma') + '</h4>');
    var event_description_div = $('<div class="event-description"></div');
    event_description_div.append(event_description_title);
    event_description_div.append(event_description_location);
    event_description_div.append(event_description_time);

    event_group_div = $('<div class="group"></div>');
    event_group_div.append(event_date_div);
    event_group_div.append(event_description_div);

    var event_li = $('<li></li>');
    event_li.append(event_group_div);

    return event_li;
}

$(document).ready(function() {
   $('#contact-us').on('click', function(e) {
        $('#message-form').toggleClass('hidden');
   });
});
