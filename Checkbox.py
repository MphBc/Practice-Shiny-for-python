from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_text("x", "Text input", placeholder="Enter text"),
    ui.output_text_verbatim("txt"),
    ui.input_checkbox("y", "Checkbox input"),
    ui.output_text_verbatim("txt2"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f'x: "{input.x()}"'

    @output
    @render.text
    def txt2():
        return f'y: {"Checked" if input.y() else "Unchecked"}'

app = App(app_ui, server, debug=True)
