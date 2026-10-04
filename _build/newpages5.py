HERO_PHOTO.update({"Explorer passport": "cotopaxi", "Send a postcard": "montanita", "Community": "otavalo"})

# ---------- PASSPORT ----------
STAMP_INFO = [
 ("story", "Story reader", "Read a story to the end", "journal-why-ecuador.html"),
 ("quiz", "Region quiz", "Find your Ecuador region", "quiz.html"),
 ("planner", "Trip planner", "Build a family trip plan", "trip-planner.html"),
 ("plate", "Full plate", "Build an Ecuadorian plate", "food.html"),
 ("pack", "Packed and ready", "Pack the whole suitcase", "gear.html"),
 ("flash", "Slang student", "Flip a slang flashcard", "dennisse.html"),
 ("vote", "First vote", "Vote on where we go first", "top-20.html"),
 ("checklist", "Getting ready", "Tick off a checklist item", "checklist.html"),
 ("postcard", "Postcard sender", "Send a postcard", "postcard.html"),
 ("festival", "Fiesta fan", "Visit the festival calendar", "festivals.html"),
 ("guide", "Four regions", "Explore the Ecuador guide", "ecuador.html"),
 ("spanish", "¡Hola!", "Read any page in Spanish", "es.html"),
]
ROT = [-8, 5, -3, 9, -6, 4, -10, 7, -4, 6, -7, 3]
stamps_html = "".join(f'''<a class="pp-stamp" data-k="{k}" href="{h}" style="--rot:{ROT[i]}deg"><span class="pp-ring"><b>{t}</b><span class="pp-date"></span></span><span class="pp-how">{how}</span></a>''' for i, (k, t, how, h) in enumerate(STAMP_INFO))
passport = hero("Explorer passport", "Your Latitude Zero <em>explorer passport</em>",
  "Collect a stamp for each adventure around the site. Get all 12 and earn your official Ecuador Explorer certificate.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="pp-progress"><span><b id="pp-count">0</b> / 12 stamps</span><div class="bar" aria-hidden="true"><i id="pp-fill"></i></div></div>
      <div class="pp-book" id="passport-book">{stamps_html}</div>
      <p class="credit-note">Your stamps are saved in this browser on this device.</p>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap pp-cert-wrap">
      <div id="pp-locked" class="pp-locked"><span class="eyebrow">The reward</span><h2>Your explorer certificate</h2><p>Collect all 12 stamps to unlock a personalized Ecuador Explorer certificate with your name on it.</p></div>
      <div id="pp-cert" hidden class="pp-cert">
        <span class="eyebrow">¡Felicidades!</span><h2>You collected every stamp</h2>
        <div class="pp-cert-form"><label for="pp-name">Name for your certificate</label><input id="pp-name" maxlength="40" autocomplete="name"><button class="btn btn-sun" type="button" id="pp-make">Make my certificate</button></div>
        <canvas id="pp-canvas" width="1200" height="680" hidden></canvas>
        <img id="pp-img" hidden alt="Your Ecuador Explorer certificate">
        <a class="btn btn-line" id="pp-dl" download="latitude-zero-explorer.png" hidden>Download certificate</a>
      </div>
    </div>
  </section>
</main>'''
# passport page switched off for now
# page("passport.html", "Explorer Passport · Latitude Zero", "passport", passport)

# ---------- POSTCARD ----------
PC = [("quilotoa", "Quilotoa"), ("mitad", "Mitad del Mundo"), ("frailes", "Los Frailes"), ("santacruz", "Galápagos"), ("cotopaxi", "Cotopaxi"), ("cuenca", "Cuenca"), ("banos", "Baños"), ("mindo", "Mindo")]
picks = "".join(f'<button type="button" class="pc-pick" data-p="{k}" aria-pressed="{"true" if i == 0 else "false"}"><img src="img/{k}-800.jpg" alt=""><span>{n}</span></button>' for i, (k, n) in enumerate(PC))
postcard = hero("Send a postcard", "Send a postcard <em>from the equator</em>",
  "Pick a photo, write a note and send it to someone you love. No stamps required.") + f'''
<main>
  <section>
    <div class="wrap pc-grid">
      <form class="pc-form" id="pc-form" novalidate>
        <div class="pc-received" id="pc-received" hidden><span class="eyebrow">You've got mail</span><b>Someone sent you a postcard from Latitude Zero!</b><span>Send one back below.</span></div>
        <fieldset class="field"><legend>1. Pick a photo</legend><div class="pc-picks">{picks}</div></fieldset>
        <div class="field"><label for="pc-to">2. Who's it for?</label><input id="pc-to" maxlength="40" required placeholder="e.g. Grandma"></div>
        <div class="field"><label for="pc-msg">3. Your message <small><span id="pc-left">200</span> left</small></label><textarea id="pc-msg" rows="4" maxlength="200" required placeholder="Wish you were here!"></textarea></div>
        <div class="field"><label for="pc-from">4. From</label><input id="pc-from" maxlength="40" required placeholder="Your name"></div>
        <p class="cm-err" id="pc-err" hidden>Please fill in who it's for, your message and your name.</p>
        <button class="btn btn-sun" type="submit">Make my postcard</button>
      </form>
      <div class="pc-side">
        <div class="pc-card" id="pc-card">
          <div class="pc-face pc-front" id="pc-front"><span class="pc-greet">Greetings from <b>Ecuador</b></span><span class="pc-lat">0° 00′ 00″</span></div>
          <div class="pc-face pc-back"><div class="pc-left"><p class="pc-to">To <b id="pc-to-out">…</b></p><p class="pc-msg" id="pc-msg-out"></p><p class="pc-from">— <b id="pc-from-out">…</b></p></div><div class="pc-right"><span class="pc-stamp" aria-hidden="true"></span><span class="pc-post" aria-hidden="true">LATITUDE ZERO · EC</span><span class="pc-lines" aria-hidden="true"></span></div></div>
        </div>
        <button type="button" class="link-more pc-flip" id="pc-flip">Flip the postcard ↻</button>
        <div class="pc-done" id="pc-done" hidden>
          <span class="eyebrow">Ready to send</span>
          <p>Copy this link and send it by text, WhatsApp or email.</p>
          <input id="pc-link" readonly aria-label="Postcard link">
          <div class="copy-row" style="margin-top:0"><button class="btn btn-sun" type="button" id="pc-copy">Copy link</button><button class="btn btn-line" type="button" id="pc-share" hidden>Share</button></div>
        </div>
      </div>
    </div>
  </section>
</main>'''
page("postcard.html", "Send a Postcard · Latitude Zero", "postcard", postcard)

# ---------- COMMUNITY ----------
COURSE = [("Day 1", "Is Ecuador right for your family?", "The questions we asked ourselves before deciding."),
          ("Day 2", "Planning the move with little ones", "Timelines, documents and the paperwork mindset."),
          ("Day 3", "Packing for a baby or toddler", "What to bring, what to buy there, what to leave."),
          ("Day 4", "Your first week in Ecuador", "Altitude, rest, food and finding your feet."),
          ("Day 5", "Exploring Ecuador as a family", "How to plan trips around naps and little legs.")]
course_html = "".join(f'<li><span class="alt">{d}</span><b>{t}</b><span>{x}</span></li>' for d, t, x in COURSE)
community = hero("Community", "The Latitude Zero <em>community</em>",
  "Contests, photos, a free email course and more ways to join in, wherever you're reading from.") + f'''
<main>
  <section>
    <div class="wrap contest">
      <div class="contest-art" aria-hidden="true"><svg viewBox="0 0 120 64"><g fill="#5f8f6e"><rect x="30" y="44" width="10" height="14" rx="4"/><rect x="76" y="44" width="10" height="14" rx="4"/><ellipse cx="104" cy="40" rx="11" ry="8"/></g><circle cx="108" cy="37" r="1.8" fill="#0f3b3a"/><path d="M18 48 Q20 10 58 8 Q96 10 98 48 Z" fill="#c9a24a"/><path d="M38 47 L44 26 L58 18 L72 26 L78 47 M44 26 L72 26 M58 18 L58 8" stroke="#8a6a24" stroke-width="2.5" fill="none"/><rect x="14" y="44" width="88" height="7" rx="3.5" fill="#a8843a"/></svg><span class="contest-q">?</span></div>
      <div class="contest-copy">
        <span class="eyebrow">Contest · Open now</span>
        <h2>Name our tortoise</h2>
        <p>Our Galápagos tortoise strolls along the bottom of every page, but it still doesn't have a name. Suggest one! We'll pick a favorite and announce it in the newsletter and on Instagram.</p>
        {mail_form("contest-form", "Tortoise name suggestion", [("input", "ct-name", "Tortoise name idea", True, "e.g. Lentito"), ("input", "ct-you", "Your first name", True, ""), ("textarea", "ct-why", "Why this name?", False, "Optional")], "Suggest this name")}
      </div>
    </div>
  </section>
  <section class="regions-bg" id="course">
    <div class="wrap course">
      <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">Free email course</span><h2>Ecuador with Kids, in 5 days</h2><p>One short email a day with what we're learning as we plan our own move. Free, in English or Spanish.</p>
        <a class="btn btn-sun" href="#newsletter">Sign up below</a><p class="credit-note">Launching with our first newsletter.</p></div>
      <ol class="course-days">{course_html}</ol>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Reader photo wall</span><h2>#latitudezerofamily</h2><p>Traveling Ecuador with your family? Tag your photos #latitudezerofamily on Instagram and we may feature them here, with your permission.</p></div>
      <div class="photo-wall-empty"><span class="pw-frame" aria-hidden="true"></span><span class="pw-frame" aria-hidden="true"></span><span class="pw-frame" aria-hidden="true"></span><div><b>Your photo could be first</b><span>No reader photos yet.</span></div></div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap giveaway">
      <div class="gw-badge" aria-hidden="true"><span>Coming soon</span></div>
      <div><span class="eyebrow">Monthly giveaway</span><h2>A taste of Ecuador</h2><p>Once the newsletter launches, we'll give a newsletter subscriber a little taste of Ecuador each month, like coffee or chocolate. Details and official rules will be posted here before the first giveaway.</p><a class="link-more" href="#newsletter">Join the newsletter to be ready →</a></div>
    </div>
  </section>
</main>'''
page("community.html", "Community · Latitude Zero", "community", community)
