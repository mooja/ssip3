// Your Client ID can be retrieved from your project in the Google
// Developer Console, https://console.developers.google.com
var CLIENT_ID = '364067510002-l5u0nenknn11r7eho8eb9ka7h1ri8d3k.apps.googleusercontent.com'; 
var SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"];

/**
 * Check if current user has authorized this application.
 */
function checkAuth() {
  gapi.auth.authorize(
      {
        'client_id': CLIENT_ID,
        'scope': SCOPES.join(' '),
        'immediate': true
      }, handleAuthResult);
}

/**
 * Handle response from authorization server.
 *
 * @param {Object} authResult Authorization result.
 */
function handleAuthResult(authResult) {
  var authorizeDiv = document.getElementById('authorize-div');
  if (authResult && !authResult.error) {
    // Hide auth UI, then load client library.
    authorizeDiv.style.display = 'none';
    loadCalendarApi();
  } else {
    // Show auth UI, allowing the user to initiate authorization by
    // clicking authorize button.
    authorizeDiv.style.display = 'inline';
  }
}

/**
 * Initiate auth flow in response to user clicking authorize button.
 *
 * @param {Event} event Button click event.
 */
function handleAuthClick(event) {
  gapi.auth.authorize(
      {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
      handleAuthResult);
  return false;
}

/**
 * Load Google Calendar client library. List upcoming events
 * once client library is loaded.
 */
function loadCalendarApi() {
  gapi.client.load('calendar', 'v3', listUpcomingEvents);
}

/**
 * Print the summary and start datetime/date of the next ten events in
 * the authorized user's calendar. If no events are found an
 * appropriate message is printed.
 */
function listUpcomingEvents() {
  var request = gapi.client.calendar.events.list({
    'calendarId': 'primary',
    'timeMin': (new Date()).toISOString(),
    'showDeleted': false,
    'singleEvents': true,
    'maxResults': 5,
    'orderBy': 'startTime'
  });

  request.execute(function(resp) {
    var events = resp.items;
    if (events.length > 0) {
      var events_ul = $('<ul class="events-list"></li>');
      for (i = 0; i < events.length; i++) {
        var event = events[i];
        var when = event.start.dateTime;
        if (!when) {
          when = event.start.date;
        }

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

        events_ul.append(event_li);
      } // end for
      $('#calendar').append(events_ul);
    } 
  });
}

/**
 * Append a pre element to the body containing the given message
 * as its text node.
 *
 * @param {string} message Text to be placed in pre element.
 */
function appendPre(message) {
  var pre = document.getElementById('calendar');
  var textContent = document.createTextNode(message + '\n');
  pre.appendChild(textContent);
}
