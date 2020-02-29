import PySimpleGUI as sg
import TextFileMergerFnFile

sg.theme('BluePurple')
layout  = [ [sg.Text('Folder of text files:*')],
            [sg.InputText('',key='input_folderpath',size=(80,1),disabled=True,enable_events=True),
             sg.FolderBrowse('Browse',key='fb_infilefolder',enable_events=True)],
            [sg.Text('Output File path:')],
            [sg.InputText('',key='output_folderpath',size=(80,1),disabled=True,enable_events=True),
             sg.FolderBrowse('Browse',key='fb_outfilefolder')],
            [sg.Check('Remove empty lines from the output file**',key='_CHK_EMTYLINE_REMOVE_',default=False)],
            [sg.Text('Output Text FileName (No extension please!!) : '),sg.InputText('',size=(45,1),key='output_filename',enable_events = True)],
            [sg.Text('Status :',key='resultLabel',size=(6,1),justification='Left',text_color='Green'),
             sg.InputText('',key='resultbox',disabled=True,size=(30,1),text_color='Green')],
            [sg.Button('Submit',key='btn_submit',disabled=True),sg.Button('Reset',key='btn_reset'),
             sg.Button('Exit',key='btn_exit')],
            [sg.Text('How to use the tool:',text_color='Red')],
            [sg.Text('1. Place all text files(.txt) to be merged in a folder\n'
                     '2. Browse the folder as "Folder of text files" \n'
                     '3. Browse output file folder as "Output File path"\n'
                     '   This is optional. In case output folder is not provided, Output file will be placed at same location as Application\n'
                     '4. **Checking this option will remove all empty lines from the file**\n'
                     '5. Default output file name would be - Output_MergedFile.txt\n'
                     '6. Click Submit button to merge files\n',text_color='Red')]]

window = sg.Window('Text File Merger',layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit', 'btn_exit'):   # if user closes window or clicks Exit
        break
    elif event == 'input_folderpath':
        window['btn_submit'](disabled=False) 
        print('Folder path event!!')
        print(event,values)
    
    elif event in ['output_folderpath']:        
        print('Folder path event!!')
        print(event,values)
        
    elif event == 'btn_submit':        
        print("Clicked Submit button")
        #print (event,values)
        print(values)
        file_count,result = TextFileMergerFnFile.fileMerger(values)
        if result == 'Merged':
            window['resultbox']('Done, '+str(file_count)+' Files Merged!!')
    #elif event == 'output_filename':
    elif len(values['output_filename']) > 40:
        window['output_filename'](values['output_filename'][:-1])
        
    elif event == 'btn_reset':
        window['input_folderpath']('')
        window['output_folderpath']('')
        window['btn_submit'](disabled=True)
        window['resultbox']('')
        window['_CHK_EMTYLINE_REMOVE_'](False)
        window['output_filename']('')
        
window.close()
