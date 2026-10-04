def mail_form(fid, subject, fields, button):
    inner = ""
    for kind, fid2, label, req, ph in fields:
        r = " required" if req else ""
        p = f' placeholder="{ph}"' if ph else ""
        if kind == "textarea":
            inner += f'<div class="field"><label for="{fid2}">{label}</label><textarea id="{fid2}" rows="4" maxlength="800" data-label="{label}"{r}{p}></textarea></div>'
        else:
            inner += f'<div class="field"><label for="{fid2}">{label}</label><input id="{fid2}" maxlength="80" data-label="{label}"{r}{p}></div>'
    return f'''<form class="mail-form" id="{fid}" data-subject="{subject}" novalidate>{inner}
        <label class="consent"><input type="checkbox" required><span>I'm happy for Latitude Zero to reply and, if chosen, share my first name.</span></label>
        <p class="mf-err cm-err" hidden>Please fill in the required fields and tick the box.</p>
        <button class="btn btn-sun" type="submit">{button}</button></form>
      <div class="mf-done" hidden><span class="eyebrow">Almost done</span><p>Send this to us by email. Copy it, or open it in your email app.</p><textarea rows="5" readonly aria-label="Your message"></textarea>
        <div class="copy-row" style="margin-top:0"><button class="btn btn-sun mf-copy" type="button">Copy</button><a class="btn btn-line mf-mail" href="#">Open in email app</a></div><p class="mf-to">hola@latitudezerofamily.com</p></div>'''

