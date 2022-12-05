import csv
import os

inputpath = './input'
#Set the header size (number of lines)
header_size = 2
#Set the chunk size (number of rows per file)
chunk_size = 2000

#Initialize empty file list
onlyfiles = []

#Read all file names from inputhpath and store them in onlyfiles
for f in os.listdir(inputpath):
    if os.path.isfile(os.path.join(inputpath,f)):
        onlyfiles.append(f)

#CSV file write function
def write_chunk(filename,part, lines):
    with open('./output/'+filename+'_'+str(part)+'.csv','w') as f_out:
        f_out.writelines(header_lines)
        f_out.writelines(lines)
        f_out.close
        print(f'{f_out.name} created')


cnt = 0
#Loop throug files in onlyfiles
for file in onlyfiles:
    #Split file name into name and extension
    split_tup = os.path.splitext(file)
    #Check if file is CSV file
    if split_tup[1] == '.csv':
        #open file
        with open('./input/'+onlyfiles[cnt],'r') as f:
            count = 0
            header_lines = []
            i = 0
            #create header
            while i < header_size:
                header = f.readline()
                header_lines.append(header)
                i+=1
            #create lines to push to new CSV file
            lines = []
            for line in f:
                count += 1
                lines.append(line)
                if count % chunk_size == 0:
                    write_chunk(onlyfiles[cnt],count,lines)
                    lines= []
            if len(lines) > 0:
                write_chunk(onlyfiles[cnt],count + 1,lines)
    #else statement for other file types in input folder
    else:
        print(f'{file} is not a CSV file and was ignored.')
    cnt += 1