// circadian.js — Rose Pine Moon × Phosphor Noir
// Four phases. No noise. Updates every 60s.

const PHASES = {
  dawn: {
    range:  [5, 11],
    bg:         '#1a1826',
    surface:    '#232136',
    overlay:    '#2a273f',
    accent:     '#ea9a97',
    accentDark: '#c47a77',
    accentRgb:  '234,154,151',
    muted:      '#6e6a86',
    label:      'hidden-heart 🖤',
  },
  day: {
    range:  [11, 17],
    bg:         '#232136',
    surface:    '#2a273f',
    overlay:    '#393552',
    accent:     '#9ccfd8',
    accentDark: '#6eadb6',
    accentRgb:  '156,207,216',
    muted:      '#908caa',
    label:      'choice 🧩',
  },
  dusk: {
    range:  [17, 21],
    bg:         '#1f1d2e',
    surface:    '#26233a',
    overlay:    '#312e4a',
    accent:     '#f6c177',
    accentDark: '#d4a356',
    accentRgb:  '246,193,119',
    muted:      '#908caa',
    label:      'desire ☠️',
  },
  night: {
    range:  [21, 29],  // 21–04 (hours <5 get +24)
    bg:         '#191724',
    surface:    '#1f1d2e',
    overlay:    '#26233a',
    accent:     '#c4a7e7',
    accentDark: '#9c7dc7',
    accentRgb:  '196,167,231',
    muted:      '#6e6a86',
    label:      'still-pine <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABCGlDQ1BJQ0MgUHJvZmlsZQAAeJxjYGA8wQAELAYMDLl5JUVB7k4KEZFRCuwPGBiBEAwSk4sLGHADoKpv1yBqL+viUYcLcKakFicD6Q9ArFIEtBxopAiQLZIOYWuA2EkQtg2IXV5SUAJkB4DYRSFBzkB2CpCtkY7ETkJiJxcUgdT3ANk2uTmlyQh3M/Ck5oUGA2kOIJZhKGYIYnBncAL5H6IkfxEDg8VXBgbmCQixpJkMDNtbGRgkbiHEVBYwMPC3MDBsO48QQ4RJQWJRIliIBYiZ0tIYGD4tZ2DgjWRgEL7AwMAVDQsIHG5TALvNnSEfCNMZchhSgSKeDHkMyQx6QJYRgwGDIYMZAKbWPz9HbOBQAAACyElEQVR4nG2TyW8cRRhHX1VXV/f0zPRsnoUEBodFijFMYhaJAygh4saFC4fwb0XiyN/AkQNHhACDkJDBCcQyNjGeGc+eWXqt4pAQQsR3f0/6Sd8TgOWZc4SgVQioeB6+1izzjOPxhNwaAMRTkHhW0Ks3uNm9QicI0FJSrYQUiiXOlw/56vg+Xx4e/gdU/4BaSj68/AK7tRqdUhlPe1zMJxhH0bCS3nOXeH9nh2vNNne++Zp1liEAJR4L3mt36G1tIZFM1yt0EmMRTKcTiq7LMokJpOSTN98mjmPu7H+HsRZpgav1Or1Gi8Vmg5CC3OQ4UoKxNKpVarUaeZqxns2ZpSmf3viAWy+/irUWKYXg9UoNYXJ818UYgyMk0oCnXDpbTWphiK80g/6QXw/voj3Nx73rjybUPY+m9vG1R2oyHCkpKM0r29sMRmMqxTJhUESGZQpFn53OdTzPoxsW6QQBKvR86pUQB4g3OWluKCjLg0Gf1XrD5O6US602aZrR6+3SaG+xvBiRbyLaYQUlsBSUIopTmuUyucnJjGW2eEjB1cR5zi+//0a1XCFexUxOz1jM56QG8tygplHEdLWhVSqhtQZhiaIEpIPnagLfB+CdvbdwlWQ8nnB8esJ4sWC0WqJmScLGGlxHEhmDyA0l30fYR48S+D6tZhNpDEkSM51POBtccJHGDKM1yljLj6MB73Zf5GQ4xPd8qtUKxaCIgyROEh70zzkfDJjHG7IspRmGfHFwRG4sSgjBD/1zDhYzbr22S2QNjpS4rotX8BkPR/haM17MuXd6wkvNDsfRmoPpBAFIgMwYPvv+W+5lEXt71+hefh4lBDbLUK6DkAKM4Y3uNlEp4POff8JY+28TTxd1+8ZNPrq6SyVO0NIhyVKO/jxj/48j7kdr9vt/Yax9EtMTVgiBfWxVjsOVeoOSdBBCMt6sOJ3P/jfhvwHSDzv+RE4/JQAAAABJRU5ErkJggg==" style="width:14px;height:14px;border-radius:50%;vertical-align:middle;margin-left:3px;opacity:0.9;">',  
  },
}

function getPhase(h) {
  const hour = h < 5 ? h + 24 : h
  for (const [name, p] of Object.entries(PHASES)) {
    if (hour >= p.range[0] && hour < p.range[1]) return { name, ...p }
  }
  return { name: 'night', ...PHASES.night }
}

function apply(phase) {
  const r = document.documentElement
  r.style.setProperty('--bg',          phase.bg)
  r.style.setProperty('--surface',     phase.surface)
  r.style.setProperty('--surface-light', phase.overlay)
  r.style.setProperty('--accent',      phase.accent)
  r.style.setProperty('--accent-dark', phase.accentDark)
  r.style.setProperty('--accent-rgb',  phase.accentRgb)
  r.style.setProperty('--accent-glow', `rgba(${phase.accentRgb}, 0.14)`)
  r.style.setProperty('--text-muted',  phase.muted)
  r.dataset.phase = phase.name

  const dot   = document.getElementById('phase-dot')
  const label = document.getElementById('phase-label')
  if (dot) {
    dot.style.background  = phase.accent
    dot.style.boxShadow   = `0 0 7px rgba(${phase.accentRgb}, 0.7)`
  }
  if (label) label.innerHTML = phase.label
}

function tick() {
  apply(getPhase(new Date().getHours()))
}

tick()
setInterval(tick, 60000)
