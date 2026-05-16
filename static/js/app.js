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

// copy-to-clipboard buttons (MCP URL)
document.querySelectorAll('.copy-btn[data-copy]').forEach(btn => {
  const original = btn.textContent;
  btn.addEventListener('click', async () => {
    const text = btn.getAttribute('data-copy');
    try {
      await navigator.clipboard.writeText(text);
    } catch (e) {
      const url = btn.parentElement.querySelector('.url');
      if (url) {
        const range = document.createRange();
        range.selectNodeContents(url);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
      }
    }
    btn.textContent = 'Copied';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = original;
      btn.classList.remove('copied');
    }, 1600);
  });
});

// pricing seat calculator
const calcRange = document.getElementById('calcRange');
if (calcRange) {
  const seatsEl = document.getElementById('calcSeats');
  const monthlyEl = document.getElementById('calcMonthly');
  const breakdownEl = document.getElementById('calcBreakdown');
  const stepBtns = document.querySelectorAll('.calc-step');
  const min = +calcRange.min;
  const max = +calcRange.max;
  const fmt = n => '$' + n.toLocaleString('en-US');

  function paint() {
    const seats = +calcRange.value;
    const monthly = 19 * Math.max(1, seats - 1);
    const pct = ((seats - min) / (max - min)) * 100;
    calcRange.style.setProperty('--pct', pct + '%');
    seatsEl.textContent = seats;
    monthlyEl.textContent = fmt(monthly);
    const extras = Math.max(0, seats - 2);
    if (seats <= 2) {
      breakdownEl.textContent = '$19 base · covers seats 1–2';
    } else {
      breakdownEl.textContent = `$19 base (covers 2) + $19 × ${extras} extra seat${extras === 1 ? '' : 's'}`;
    }
  }
  calcRange.addEventListener('input', paint);
  stepBtns.forEach(b => b.addEventListener('click', () => {
    const next = Math.min(max, Math.max(min, +calcRange.value + +b.dataset.step));
    calcRange.value = next;
    paint();
  }));
  paint();
}

// typing-style placeholder rotation in compose
const input = document.getElementById('composeInput');
if (input) {
  const phrases = [
    "Ask Flitsy anything once you're set up…",
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
