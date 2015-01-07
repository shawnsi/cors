CORS Cookie Sharing
===================

This is a demonstration of how cookies can be passed cross domain via AJAX + CORS.  I don't take any responsibility for mayhem caused by an improper implementation of this logic.

This is usually handled by making AJAX calls to a subdomain with a parent common to the original document.  CORS will allow native cookie sharing in that case.  The common parent cannot be a TLD though.

In the event that the number of subdomains to manage becomes unwieldy this technique can be used without a shared domain.

Quickstart
----------

Setup a virtualenv if you don't want to use the system wide python installation:

```bash
$ cd cors
$ virtualenv-2.7 . # First time only
$ source bin/activate
```

Install our dependencies:

```bash
$ pip install -r requirements.txt
```

Run the app:

```bash
$ python app.py
```

Hit the home page in your browser via localhost:

[http://localhost:8090](http://localhost:8090)

Take a look at developer tools to see the AJAX request to an external domain.  The X-Cookies response header is automatically unpacked into the localhost cookie store.
