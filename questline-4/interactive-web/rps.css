# Counter App — files for /questline-4/interactive-web/

Below are the three files you need to upload to your GitHub repository folder `/questline-4/interactive-web/`.

---

## `index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Counter — Interactive Web</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="container">
    <h1>Simple Counter</h1>
    <div class="counter-card" role="region" aria-label="counter">
      <button id="decrement" class="btn" aria-label="decrement">−</button>
      <div id="count" class="count" aria-live="polite">0</div>
      <button id="increment" class="btn" aria-label="increment">+</button>
    </div>

    <div class="controls">
      <button id="reset" class="secondary">Reset</button>
      <label class="step-label">Step:
        <input id="step" type="number" value="1" min="1" />
      </label>
    </div>

    <p class="hint">Click + to increase, − to decrease. The number updates instantly.</p>
  </main>

  <script src="script.js"></script>
</body>
</html>
```

---

## `style.css`

```css
:root{
  --bg:#0f1724;
  --card:#0b1220;
  --muted:#9aa6b2;
  --accent:#60a5fa;
}
*{box-sizing:border-box}
html,body{height:100%;margin:0;font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial}
body{background:linear-gradient(180deg,#071021 0%, var(--bg) 100%);color:#e6f0ff;display:flex;align-items:center;justify-content:center;padding:32px}
.container{max-width:520px;width:100%;text-align:center}
h1{margin:0 0 18px;font-size:28px}
.counter-card{display:flex;align-items:center;justify-content:center;gap:18px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:20px;border-radius:12px;box-shadow:0 6px 18px rgba(2,6,23,0.6)}
.btn{font-size:38px;width:72px;height:72px;border-radius:10px;border:none;background:transparent;color:var(--accent);cursor:pointer;transition:transform .12s ease, background .12s}
.btn:active{transform:translateY(2px) scale(.98)}
.count{font-size:36px;width:140px;text-align:center;background:rgba(255,255,255,0.02);padding:18px;border-radius:8px}
.controls{margin-top:14px;display:flex;gap:10px;align-items:center;justify-content:center}
.secondary{background:transparent;border:1px solid rgba(255,255,255,0.06);padding:8px 12px;border-radius:8px;color:var(--muted);cursor:pointer}
.step-label{color:var(--muted);font-size:14px;display:flex;align-items:center;gap:8px}
.step-label input{width:64px;padding:6px;border-radius:6px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:inherit}
.hint{color:var(--muted);font-size:13px;margin-top:12px}
@media (max-width:420px){.btn{width:56px;height:56px;font-size:30px}.count{font-size:28px;width:110px}}
```

---

## `script.js`

```javascript
// Simple counter logic — instantly updates UI
(function(){
  const countEl = document.getElementById('count');
  const inc = document.getElementById('increment');
  const dec = document.getElementById('decrement');
  const reset = document.getElementById('reset');
  const stepInput = document.getElementById('step');

  let count = 0;

  function render(){
    countEl.textContent = count;
  }

  function getStep(){
    const val = parseInt(stepInput.value, 10);
    return Number.isFinite(val) && val > 0 ? val : 1;
  }

  inc.addEventListener('click', ()=>{
    count += getStep();
    render();
  });

  dec.addEventListener('click', ()=>{
    count -= getStep();
    render();
  });

  reset.addEventListener('click', ()=>{
    count = 0;
    render();
  });

  // keyboard support: ArrowUp -> increment, ArrowDown -> decrement, r -> reset
  window.addEventListener('keydown', (e)=>{
    if (e.key === 'ArrowUp') { count += getStep(); render(); }
    else if (e.key === 'ArrowDown') { count -= getStep(); render(); }
    else if (e.key.toLowerCase() === 'r') { count = 0; render(); }
  });

  // initial render
  render();
})();
```

---

## How to submit

1. Create folder in your repo: `/questline-4/interactive-web/`.
2. Add the three files above (`index.html`, `style.css`, `script.js`).
3. Commit and push:

```bash
mkdir -p questline-4/interactive-web
# copy the files into that folder, then:
cd questline-4/interactive-web
git add index.html style.css script.js
git commit -m "Add counter app for questline-4/interactive-web"
git push origin main
```

4. Run the app locally: open `index.html` in a browser. Take a screenshot of the running app (show the counter UI and buttons) and upload that screenshot to the same folder in your repo — name it `screenshot.png`.

---

If you'd prefer the Rock–Paper–Scissors game instead, or want the files combined into a single-file variant (for easier preview), tell me and I'll add it. Otherwise this is ready to copy & upload.
