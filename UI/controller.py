import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_analisiAeroporti(self, e):
        txt_x=self._view.txt_distanza_minima.value

        if txt_x=="":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione! Inserire un valore nel campo della distanza", color="red"))
            self._view.update_page()
            return

        try:
            x=float(txt_x)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Inserire un valore numerico nel della distanza", color="red"))
            self._view.update_page()
            return

        self._view.txt_result.controls.clear()
        self._model.buildGraph(x)
        self._view.txt_result.controls.append(ft.Text(f"Il numero di vertici del grafo è {self._model.getNumNodes()}."))
        self._view.txt_result.controls.append(ft.Text(f"Il numero di archi del grafo è {self._model.getNumEdges()}."))
        for u,v, peso in self._model.getEdgesPesati():
            self._view.txt_result.controls.append(ft.Text(f"{u} - {v}. Distanza: {peso["weight"]:.2f}"))
        self._view.update_page()

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
