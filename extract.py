import FreeSimpleGUI as fg
from zip_extract import extract_archive


fg.theme('black')
label1 = fg.Text('select archive')
input1 = fg.Input()
choose_button1 = fg.FileBrowse('choose', key= 'archive')

label2= fg.Text('selectb destination folder: ')
input2= fg.Input()
choose_button2= fg.FolderBrowse('choose', key= 'folder')

extract_button = fg.Button("extract")
output_label = fg.Text(key= "output", text_color='green')
col1 = fg.Column([[label1], [label2]])
col2 = fg.Column([[input1], [input2]])
col3 = fg.Column([[choose_button1], [choose_button2]])

window= fg.Window("Archive extractor", layout= [[col1, col2, col3], [extract_button]])


while True:
    event,values = window.read()
    print(event,values)
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window["output"].update(value= "extraction completed")

    
window.read()
window.close()