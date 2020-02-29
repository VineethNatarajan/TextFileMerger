# Functions for test merger app

import glob
import os

def fileMerger(GUIValues):
    if GUIValues['output_filename'] == '':
        GUIValues['output_filename'] = 'Output_MergedFile'
        
    if GUIValues['output_folderpath'] == '':
        outFilePath = os.getcwd()
        print(outFilePath)
        outputFilePath = outFilePath + "/"+ GUIValues['output_filename']+ ".txt"
        tempFilePath = outFilePath + "/tempFile.txt"
    else:
        outputFilePath = GUIValues['output_folderpath'] + "/" + GUIValues['output_filename']+ ".txt"
        tempFilePath = GUIValues['output_folderpath'] + "/tempFile.txt"
        
    inFilePath = GUIValues['input_folderpath']
    print(inFilePath)
    inFilePath = inFilePath +"/*.txt"
    
    read_files = glob.glob(inFilePath)
    print (read_files)
    sorted_list = sorted(read_files)
    print ("Sorted List:")
    print (sorted_list)
    fcount = len(sorted_list)

    if GUIValues['_CHK_EMTYLINE_REMOVE_'] == True:   

        with open(tempFilePath, "w") as outfile:
            for f in sorted_list:
                print (f)
                with open(f, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')
    
        with open(tempFilePath) as infile, open(outputFilePath, 'w') as outfile:
            for line in infile:
                if not line.strip(): continue  # skip the empty line
                outfile.write(line)


        os.remove(tempFilePath)

    else:
        with open(outputFilePath, "w") as outfile:
            for f in sorted_list:
                print (f)
                with open(f, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')
    
    return fcount,"Merged"


