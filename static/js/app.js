// sticky nav border on scroll
const nw = document.getElementById('navwrap');
if (nw) {
  const onScroll = () => nw.classList.toggle('scrolled', window.scrollY > 4);
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// smooth scroll for in-page anchor links
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const id = a.getAttribute('href').slice(1);
    const el = document.getElementById(id);
    if (!el) return;
    e.preventDefault();
    window.scrollTo({ top: el.offsetTop - 70, behavior: 'smooth' });
  });
});

// typing-style placeholder rotation in compose
const input = document.getElementById('composeInput');
if (input) {
  const phrases = [
    "Ask Flitsy anything once it's up…",
    "Who's gone quiet on the Acme deal?",
    "Draft a follow-up to the 6 stalled deals.",
    "Summarize the Northwind account in 4 bullets.",
    "Who haven't I emailed in 30 days?",
  ];
  let pi = 0, ci = 0, dir = 1, paused = false;
  input.addEventListener('focus', () => { paused = true; });
  input.addEventListener('blur', () => { if (!input.value) paused = false; });
  function tick() {
    if (paused) { setTimeout(tick, 400); return; }
    const s = phrases[pi];
    if (dir === 1) {
      ci++;
      if (ci > s.length) { dir = -1; setTimeout(tick, 1800); return; }
    } else {
      ci--;
      if (ci < 0) { dir = 1; pi = (pi + 1) % phrases.length; setTimeout(tick, 350); return; }
    }
    input.placeholder = s.slice(0, ci) + (dir === 1 && ci < s.length ? '▍' : '');
    setTimeout(tick, dir === 1 ? 38 + Math.random() * 30 : 18);
  }
  tick();
}
