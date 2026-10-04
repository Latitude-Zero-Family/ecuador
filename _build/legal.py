HERO_PHOTO.update({"Privacy policy": "mitad", "Disclosure": "mitad"})

privacy = hero("Privacy policy", "Privacy <em>policy</em>",
  "How we handle your information on Latitude Zero. Last updated October 3, 2026.") + '''
<main>
  <section>
    <div class="wrap prose legal">
      <p>Latitude Zero is a family travel blog run by Austin and Dennisse. We want you to be able to read, watch and play along without worrying about your privacy. This page explains what we collect, why, and the choices you have.</p>
      <h2>What we collect</h2>
      <p><b>Newsletter.</b> If you join our newsletter, we collect your email address so we can send you new stories. You can unsubscribe at any time using the link in every email.</p>
      <p><b>Emails you send us.</b> If you write to us, we keep your message and email address so we can reply. If we turn your question into a post or video, we only use your first name, and only with your permission.</p>
      <p><b>Analytics.</b> With your consent, we use analytics to understand which pages people read and how they find us. This uses cookies. We never use it to identify you personally.</p>
      <p><b>Things that stay on your device.</b> Some features, like the moving checklist, your quiz answers and your Top 20 vote, are saved only in your own browser. We can't see them.</p>
      <h2>What we don't do</h2>
      <p>We don't sell your personal information. We don't share your email address with partners or sponsors.</p>
      <h2>Services we use</h2>
      <p>We use a small number of trusted services to run the site, such as our website host, our email newsletter provider and, with your consent, an analytics provider. They only process your information to provide their service to us.</p>
      <h2>Cookies and your choices</h2>
      <p>When analytics is turned on, we'll ask for your consent before setting any analytics cookies. You can change your choice at any time with the "Cookie settings" link at the bottom of every page, or by clearing your browser's cookies.</p>
      <h2>Children</h2>
      <p>Our site is written for adults. We don't knowingly collect information from children.</p>
      <h2>Your rights</h2>
      <p>You can ask us to see, correct or delete the information we hold about you by emailing us. Depending on where you live, you may have additional rights under local law.</p>
      <h2>Contact</h2>
      <p>Questions about this policy? Email <code>hola@latitudezerofamily.com</code>.</p>
    </div>
  </section>
</main>'''
page("privacy.html", "Privacy Policy · Latitude Zero", "", privacy)

disc = hero("Disclosure", "Partnerships <em>&amp; disclosure</em>",
  "How we work with brands, hotels and tourism partners, and how we tell you about it. Last updated October 3, 2026.") + '''
<main>
  <section>
    <div class="wrap prose legal">
      <p>Latitude Zero is our family's story. Trust matters more to us than any partnership, so here's exactly how we handle them.</p>
      <h2>Right now</h2>
      <p>Everything on the site today is independent. We haven't been paid or given anything free for any content you see here.</p>
      <h2>Sponsored content</h2>
      <p>When we work with a brand, hotel or tourism board in the future, the post or video will say so clearly at the top, with a label like "In partnership with" or "Sponsored."</p>
      <h2>Affiliate links</h2>
      <p>Some future links may be affiliate links. If you buy through one, we may earn a small commission at no extra cost to you. We'll mark these links and only recommend things we actually use.</p>
      <h2>Our opinions are our own</h2>
      <p>Partners never get to approve what we say. If something doesn't work for our family, we'll tell you, or we won't feature it.</p>
      <h2>Questions</h2>
      <p>Email <code>hola@latitudezerofamily.com</code>. Brands interested in working with us can start with our <a href="media-kit.html">media kit</a>.</p>
    </div>
  </section>
</main>'''
page("disclosure.html", "Disclosure · Latitude Zero", "", disc)

nf = '''<header class="page-hero"><div class="wrap">
  <span class="eyebrow">Error 404</span>
  <h1>Lost at <em>latitude zero</em></h1>
  <p>This page wandered off the map. Let's get you back on the route.</p>
</div></header>
<main>
  <section>
    <div class="wrap">
      <div class="paths">
        <a class="path" href="./"><span class="alt">HOME</span><h3>Back to the start</h3><p>The home page and our latest stories.</p><span class="go">Home →</span></a>
        <a class="path" href="top-20.html"><span class="alt">TOP 20</span><h3>The places we plan to visit</h3><p>Our Ecuador bucket list, with a map.</p><span class="go">Top 20 places →</span></a>
        <a class="path" href="quiz.html"><span class="alt">PLAY</span><h3>Which region fits your family?</h3><p>A five-question quiz.</p><span class="go">Take the quiz →</span></a>
      </div>
    </div>
  </section>
</main>'''
page("404.html", "Page Not Found · Latitude Zero", "", nf)
