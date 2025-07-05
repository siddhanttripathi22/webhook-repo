function getIcon(type) {
  switch (type) {
    case 'push': return '📦';
    case 'pull_request': return '🔀';
    case 'merge': return '✅';
    default: return '📄';
  }
}

function getColor(type) {
  switch (type) {
    case 'push': return 'border-blue-300';
    case 'pull_request': return 'border-yellow-300';
    case 'merge': return 'border-green-300';
    default: return 'border-gray-300';
  }
}

function fetchEvents() {
  $.get('/events', function (data) {
    console.log("Events data received:", data);

    $('#loading').hide();           // Hide loader
    const $list = $('#events-list');
    $list.show();                   // Show events container
    $list.empty();

    if (!data || data.length === 0) {
      $('#no-events').show();      // Show "no events" box
      return;
    }

    $('#no-events').hide();        // Hide if events exist

    data.forEach(event => {
      const icon = getIcon(event.type);
      const colorClass = getColor(event.type);
      const timeString = formatTime(event.timestamp);
      const timeHtml = timeString ? `<p class="text-sm text-gray-500 mt-1">${timeString}</p>` : '';

      const html = `
        <li class="bg-white p-5 rounded-xl shadow-sm border-l-4 ${colorClass} animate-fade-in">
          <div class="flex items-start gap-3">
            <div class="text-2xl">${icon}</div>
            <div class="flex-1">
              <p class="text-base font-semibold text-gray-800">${event.message}</p>
              ${timeHtml}
            </div>
          </div>
        </li>
      `;
      $list.append(html);
    });

    $('#last-update').text(`Last updated: ${new Date().toLocaleTimeString()}`);
  }).fail(() => {
    console.error("Failed to fetch events");
  });
}


function formatTime(iso) {
  if (!iso) return '';
  const date = new Date(iso);
  if (isNaN(date.getTime())) return '';
  return date.toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    timeZoneName: 'short'
  });
}


fetchEvents();
setInterval(fetchEvents, 15000);