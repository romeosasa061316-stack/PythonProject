// ── LANGUAGE MARQUEE ──
const langs = ["English","Mandarin Chinese","Hindi","Spanish","Arabic","Bengali","Portuguese","Russian","Urdu","Indonesian","German","Japanese","Swahili","Marathi","Telugu","Turkish","Tamil","Thai","Korean","French","Italian","Shona ✦","English","Mandarin Chinese","Hindi","Spanish","Arabic","Bengali","Portuguese","Russian","Urdu","Indonesian","German","Japanese","Swahili","Marathi","Telugu","Turkish","Tamil","Thai","Korean","French","Italian","Shona ✦"];

const mq = document.getElementById('langMarquee');

langs.forEach(function(l) {
  const s = document.createElement('span');
  s.textContent = l;

  if (l.indexOf('Shona') !== -1 || l === 'English') {
    s.classList.add('highlight');
  }

  mq.appendChild(s);
});








