import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDCodins(self):
        #for cod in self._model.getCodins():
        #    self._view._ddCodins.options.append(ft.dropdown.Option(cod))
        for c in self._model.getAllCorsi():
            self._view._ddCodins.options.append(ft.dropdown.Option(key=str(c), text= c.codins, data=c, on_click=self._choiceDDCodins))

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)

    def ddCodinsSelected(self, e):
        print(type(self._view._ddCodins.value))

    def handlePrintCorsiPD(self, e):
        self._view._lvTxtout.controls.clear()
        pd = self._view._ddPD.value
        if pd is None:
            #print(self._view._lvTxtout.controls.append(ft.Text("Attenzione, selezionare un periodo didattico", color= "red")))
            self._view.create_alert("Attenzione, selezionare un periodo didattico!")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else: pdInt = 2

        corsiPD = self._model.getCorsiPD(pdInt)
        self._view._lvTxtout.controls.append(ft.Text(f"Corsi del {pd} periodo didattico."))
        for c in corsiPD:
            self._view._lvTxtout.controls.append(ft.Text(c))
        self._view.update_page()



    def handlePrintIscrittiCorsiDD(self, e):
        self._view._lvTxtout.controls.clear()
        pd = self._view._ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico!")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else: pdInt = 2

        corsiPDwI = self._model.getCorsiPDwithIscritti(pdInt)
        self._view._lvTxtout.controls.append(ft.Text(f"Dettagli corsi del {pd} periodo didattico."))
        for c in corsiPDwI:
            self._view._lvTxtout.controls.append(ft.Text(f"{c[0]} -- numero iscritti {c[1]}"))
        self._view.update_page()



    def handlePrintIscrittiCodins(self, e):
        if self._ddCodinsValue is None: #ho l'oggetto -> metodo dentro il controller
            #stampa qualcosa
            self._view.create_alert("Selezionare un corso di interesse!")
            return

        #stampiamo gli studenti
        self._view._lvTxtout.controls.clear()
        students = self._model.getStudentiCorso(self._ddCodinsValue.codins) #passiamo il codins dell'oggetto corso
        self._view._lvTxtout.controls.append(ft.Text(f"Studenti iscritti al corso {self._ddCodinsValue}"))
        for s in students:
            self._view._lvTxtout.controls.append(ft.Text(s))  #appendo direttamente s perché studente ha un metodo string

        self._view.update_page()



    def handlePrintCDSCodins(self, e):
        if self._ddCodinsValue is None:
            self._view.create_alert("Selezionare un corso di interesse!")
            return

        self._view._lvTxtout.controls.clear()
        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)

        self._view._lvTxtout.controls.append(ft.Text(f"CDS che frequentano il corso {self._ddCodinsValue}:"))
        for c in cds:
            self._view._lvTxtout.controls.append(ft.Text(f"{c[0]} -- numero iscritti {c[1]}"))

        self._view.update_page()
