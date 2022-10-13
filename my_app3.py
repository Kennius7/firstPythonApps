import PySimpleGUI as psg

layout = [
    [psg.Text("Input File: "), psg.Input(key="-IN-"), psg.FileBrowse()],
    [psg.Text("Output File: "), psg.Output(key="-OUT-"), psg.FolderBrowse()],
    [psg.Exit(), psg.Button("Convert to CSV")]
]

window = psg.Window("Excel2 CSV Converter", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (psg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert to CSV":
        psg.popup_error("Not yet implemented")
window.close()
