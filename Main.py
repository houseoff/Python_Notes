from controllers.controller import Controller
from views.consoleui import ConsoleUI
from models.notes import Notes

app = Controller(Notes(), ConsoleUI())
app.run()