import PySimpleGUI as sg
"""
sg.theme_input_text_color('#000000')
import os
os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
os.environ['DISPLAY']=':1.0'    # tell X clients to use our virtual DISPLAY :1.0


layout = [
    [sg.Text("Hello")],
    [sg.Button("ok")]
]

window = sg.Window("demo", layout)

while True:
  event, values = window.read()

  if event == "ok" or event == sg.WIN_CLOSED:
    break
window.close()

"""

val_list = []
sg.theme_input_text_color('#000000')

layout = [[sg.Text("Search query")],
          [sg.Input(key='query')],
          [sg.Button('Search')],
          [sg.Text(size=(30, 1))],
          [sg.Table(values=val_list, headings=["Name", "Title", "publications_url"], background_color='white',
                    auto_size_columns=False, display_row_numbers=False, justification='left', num_rows=15,
                    col_widths=[5, 20, 40, 100, 10, 20],
                    key='TABLE', row_height=25, enable_events=False)],
          [sg.Button('Exit')]]

window = sg.Window('Vertical Search Engine', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    query = values['query']

    try:
        idx, results = process_and_search(query)#(index, data, 30, query, "Name", "Title")
        print(results)

        window['TABLE'].update(values=results)
    except:
        print("error")

window.close()