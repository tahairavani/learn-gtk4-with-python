import gi


gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_open_application(app):
    window = Gtk.ApplicationWindow(application = app)
    window.present()


app = Gtk.Application()
app.connect("activate",on_open_application)
app.run(None)


