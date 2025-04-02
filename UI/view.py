import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore Corsi edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddPD = None
        self._ddCodins = None
        self._btnPrintCorsiPD = None
        self._btnPrintIscrittiCorsiPD = None
        self._btnPrintIcrittiCodins = None
        self._btnPrintCDSCodins = None
        self._lvTxtout = None

    def load_interface(self):
        # title
        self._title = ft.Text("Gestione Corsi", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddPD = ft.Dropdown(label = "Periodo Didattico", options=[ft.dropdown.Option("I"), ft.dropdown.Option("II")], width = 200)
        self._ddCodins = ft.Dropdown(label = "Corso", width = 200, on_change=self._controller.ddCodinsSelected)
        self._controller.fillDDCodins()

        self._btnPrintCorsiPD = ft.ElevatedButton(text="Stampa Corsi", on_click=self._controller.handlePrintCorsiPD, width=200)
        self._btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa Iscritti", on_click=self._controller.handlePrintIscrittiCorsiDD, width=200)
        self._btnPrintIcrittiCodins = ft.ElevatedButton(text="Stampa Iscritti Corso", on_click=self._controller.handlePrintIscrittiCodins, width=200)
        self._btnPrintCDSCodins = ft.ElevatedButton(text="Stampa CDS", on_click=self._controller.handlePrintCDSCodins, width=200)

        self._lvTxtout = ft.ListView(expand = True)

        row1 = ft.Row([self._ddPD, self._btnPrintCorsiPD, self._btnPrintIscrittiCorsiPD], alignment = ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._ddCodins, self._btnPrintIcrittiCodins, self._btnPrintCDSCodins], alignment = ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, self._lvTxtout)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
