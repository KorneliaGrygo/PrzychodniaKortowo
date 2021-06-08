const events = [
    {
      summary:  'Gastrolog Adam Nowak',
      description:
        'Notatka do umieszczenia : uwagi , wskazówki, uczulenia, stosowane wcześniej leki',
      start: {
        date: Calendar.moment.format('DD/MM/YYYY'),
        dateTime: Calendar.moment.format('DD/MM/YYYY') + ' 10:00',
      },
      end: {
        date: Calendar.moment.format('DD/MM/YYYY'),
        dateTime: Calendar.moment.format('DD/MM/YYYY') + ' 11:00',
      },
      color: {
        background: '#1266F1',
        foreground: 'white',
      },
    },
    
    {
      summary: 'Okulista Jan Kowalczyk',
      description:
        'Notatka do umieszczenia : uwagi , wskazówki, uczulenia, stosowane wcześniej leki',
      start: {
        date: Calendar.moment.add(1, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(1, 'day').format('DD/MM/YYYY') + ' 8:00',
      },
      end: {
        date: Calendar.moment.add(1, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(1, 'day').format('DD/MM/YYYY') + ' 8:40',
      },
      color: {
        background: '#1266F1',
        foreground: 'white',
      },
    },
    {
      summary: 'Pulmonolog Olga Kamińska',
      description:
        'Notatka do umieszczenia : uwagi , wskazówki, uczulenia, stosowane wcześniej leki',
      start: {
        date: Calendar.moment.add(2, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(2, 'day').format('DD/MM/YYYY') + ' 15:00',
      },
      end: {
        date: Calendar.moment.add(2, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(2, 'day').format('DD/MM/YYYY') + ' 15:30',
      },
      color: {
        background: '#1266F1',
      },
     
    },
    {
      summary: 'Internista Magda Jankowska',
      description:
        'Notatka do umieszczenia : uwagi , wskazówki, uczulenia, stosowane wcześniej leki',
      start: {
        date: Calendar.moment.add(3, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(3, 'day').format('DD/MM/YYYY') + ' 9:00',
      },
      end: {
        date: Calendar.moment.add(3, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(3, 'day').format('DD/MM/YYYY') + ' 10:00',
      },
      color: {
        background: '#1266F1',
      },
     
    },
    {
      summary: 'Gastrolog Adam Nowak',
      description:
        'Notatka do umieszczenia : uwagi , wskazówki, uczulenia, stosowane wcześniej leki',
      start: {
        date: Calendar.moment.add(4, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(4, 'day').format('DD/MM/YYYY') + ' 12:00',
      },
      end: {
        date: Calendar.moment.add(4, 'day').format('DD/MM/YYYY'),
        dateTime: Calendar.moment.add(4, 'day').format('DD/MM/YYYY') + ' 12:50',
      },
      color: {
        background: '#1266F1',
      },
     
    }
  ];
  
  const calendarElement = document.getElementById('calendar');
  const calendarInstance = Calendar.getInstance(calendarElement);
  calendarInstance.addEvents(events);